#!/usr/bin/env python3
"""Score Signal's analysis brief against the golden set.

    python evals/run.py --dry-run                    # token estimate per case, no API calls
    python evals/run.py                              # full mode, prompt contract, weighted
    python evals/run.py --contract native            # the same set under native structured outputs
    python evals/run.py --arm unweighted --runs 20   # one arm of the source-weighting ablation
    python evals/run.py --mode revenue               # any focus mode
    python evals/run.py --batch --runs 20            # the analysis calls through the Batch API, half price

Reuses the CLI's pipeline functions (ingest, summarize, analyze) rather than
re-implementing them, so a score here is a score for the real pipeline.
Writes a markdown table to evals/results/<date>-<mode>-<contract>-<arm>.md (-x<runs> on the end when runs > 1,
-batch when the analysis calls went through the Batch API) and the raw briefs beside it as JSON.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(ROOT))

import config  # noqa: E402
import dryrun  # noqa: E402
import tracing  # noqa: E402
from analyze import CONTRACTS, ParseFailure, analyze_brief, build_analysis_prompt, build_analysis_request, finish_analysis  # noqa: E402
from ingest import read_docs, read_media, media_names  # noqa: E402
from prompts import FOCUS_INSTRUCTIONS, RISK_TYPES  # noqa: E402
from summarize import summarize_all  # noqa: E402

GOLDEN = ROOT / "evals" / "golden"
RESULTS = ROOT / "evals" / "results"
ARMS = {"weighted": True, "unweighted": False}
# The two control files in each case directory are labels, not account documents.
CONTROL_FILES = {"expected.json", "account.json"}
NO_RISK = {"Healthy", "Unknown"}


# ── Golden set ───────────────────────────────────────────────────────
def load_cases(golden: Path, only: list[str] | None = None) -> list[dict]:
    cases = []
    for d in sorted(golden.iterdir()):
        if not d.is_dir() or not (d / "expected.json").exists():
            continue
        if only and d.name not in only:
            continue
        expected = json.loads((d / "expected.json").read_text(encoding="utf-8"))
        account = json.loads((d / "account.json").read_text(encoding="utf-8")) if (d / "account.json").exists() else {}
        unknown = [r for r in expected.get("risk_types", []) if r not in RISK_TYPES]
        if unknown:
            raise ValueError(f"{d.name}: expected.json names risk types outside the taxonomy: {unknown}")
        cases.append({"id": d.name, "dir": d, "expected": expected, "account": account})
    if not cases:
        raise SystemExit(f"no cases found under {golden}")
    return cases


# ── Scoring ──────────────────────────────────────────────────────────
def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def score_risk(expected: list[str], predicted: str | None) -> dict:
    """Recall and precision of the single predicted risk type against the
    expected set. An empty expected set means "no real risk": recall is
    trivially 1 and precision is 1 only if the model said Healthy/Unknown."""
    exp = set(expected)
    pred = {predicted} if predicted else set()
    if not exp:
        ok = bool(pred) and pred <= NO_RISK
        return {"recall": 1.0, "precision": 1.0 if ok else 0.0, "hit": ok}
    hit = len(exp & pred)
    return {
        "recall": hit / len(exp),
        "precision": (hit / len(pred)) if pred else 0.0,
        "hit": hit > 0,
    }


def score_buyer(expected: str, primary_contact: str | None) -> bool:
    """The brief returns "Name and title"; the label is the name. Match the
    whole normalized name inside the normalized prediction."""
    e, p = _norm(expected), _norm(primary_contact or "")
    if not e:
        return True
    return re.search(r"(?<![a-z])" + re.escape(e) + r"(?![a-z])", p) is not None


def score_attribution(must_cite: list[str], section_sources) -> dict:
    """Every required source label appears somewhere in section_sources."""
    cited = set()
    if isinstance(section_sources, dict):
        for v in section_sources.values():
            if isinstance(v, list):
                cited.update(_norm(x) for x in v)
            elif isinstance(v, str):
                cited.add(_norm(v))
    hits = [c for c in must_cite if any(_norm(c) in x for x in cited)]
    return {
        "coverage": (len(hits) / len(must_cite)) if must_cite else 1.0,
        "missing": [c for c in must_cite if c not in hits],
    }


def score_case(expected: dict, brief: dict | None) -> dict:
    if brief is None:
        return {"risk": {"recall": 0.0, "precision": 0.0, "hit": False}, "buyer": False,
                "attribution": {"coverage": 0.0, "missing": list(expected.get("must_cite_sources", []))},
                "gaps_ok": False, "empty": True}
    persona = brief.get("contact_persona") or {}
    gaps = brief.get("data_gaps") or []
    empty = not (brief.get("situation") or brief.get("risk_type"))
    return {
        "risk": score_risk(expected.get("risk_types", []), brief.get("risk_type")),
        "buyer": score_buyer(expected.get("economic_buyer", ""), persona.get("primary_contact")),
        "attribution": score_attribution(expected.get("must_cite_sources", []), brief.get("section_sources")),
        "gaps_ok": (bool(gaps) if expected.get("data_gaps_expected") else True),
        "empty": empty,
    }


# ── Running ──────────────────────────────────────────────────────────
def case_docs(case: dict) -> list[dict]:
    return [d for d in read_docs(str(case["dir"])) if d["name"] not in CONTROL_FILES]


def prepare_case(client, case: dict, *, mode: str, contract: str, weighted: bool) -> dict:
    """Everything before the analysis call: read the documents, summarize
    them (live, per case-run, as the CLI does), render the prompt and build
    the analysis request. Shared by the live and the Batch API paths."""
    docs = case_docs(case)
    media = read_media(str(case["dir"]))
    acct = case["account"]
    t0 = time.perf_counter()
    summaries = summarize_all(client, docs)
    prompt = build_analysis_prompt(
        acct.get("account"), acct.get("contact"), acct.get("renewal_days"), acct.get("arr"),
        summaries, mode=mode, weighted=weighted,
    )
    request = build_analysis_request(prompt, contract=contract, media=media, mode=mode)
    return {"docs": docs, "media": media, "summaries": summaries, "prompt": prompt,
            "request": request, "contract": contract, "t0": t0}


def finish_case(case: dict, prep: dict, *, brief, meta, error, raw_head, batch: bool = False) -> dict:
    """Score one case-run. The same function closes a live call and a batch
    result, so the two modes produce comparable rows."""
    total_ms = round((time.perf_counter() - prep["t0"]) * 1000)
    attach_cost(meta, batch=batch)
    scores = score_case(case["expected"], brief)
    return {
        "case": case["id"], "brief": brief, "meta": meta, "error": error, "raw_head": raw_head,
        "scores": scores, "total_ms": total_ms, "docs": len(prep["docs"]), "media": len(prep["media"]),
        "hard_fail": (meta or {}).get("parse_path") == "failed"
                     or (scores["empty"] and bool(case["expected"].get("risk_types"))),
    }


def run_case(client, case: dict, *, mode: str, contract: str, weighted: bool) -> dict:
    prep = prepare_case(client, case, mode=mode, contract=contract, weighted=weighted)
    brief, meta, error, raw_head = None, None, None, None
    try:
        brief, meta = analyze_brief(client, prep["prompt"], contract=contract, media=prep["media"], mode=mode,
                                    arm="weighted" if weighted else "unweighted")
    except ParseFailure as e:
        meta = getattr(e, "meta", {"parse_path": "failed"})
        error = str(e)
        raw_head = (e.raw or "")[:800]  # kept in the JSON so a failure can be diagnosed
    return finish_case(case, prep, brief=brief, meta=meta, error=error, raw_head=raw_head)


# ── Batch API ────────────────────────────────────────────────────────
def custom_id(case_id: str, run: int, arm: str, contract: str) -> str:
    return f"{case_id}-{run}-{arm}-{contract}"


def _batch_error(result) -> str:
    """One line naming why a batch result did not succeed."""
    kind = getattr(result, "type", "unknown")
    err = getattr(result, "error", None)
    inner = getattr(err, "error", None) or err
    etype = getattr(inner, "type", None)
    msg = getattr(inner, "message", None)
    detail = ": ".join(x for x in (etype, msg) if x)
    return f"batch result {kind}" + (f" ({detail})" if detail else "")


def _failed_meta(request: dict, contract: str) -> dict:
    return {"model": request["model"], "contract": contract, "parse_path": "failed", "stop_reason": None,
            "input_tokens": None, "output_tokens": None, "latency_ms": None}


def run_batch(client, jobs: list[dict], *, sleep=time.sleep, first_wait: float = 5.0,
              max_wait: float = 60.0, log=print) -> list[dict]:
    """Send every prepared case-run as one Message Batches request, wait for
    it to end, and score each result through the same path as a live call.

    `jobs` are {case, run, prep} dicts in table order; results come back in
    any order and are keyed by custom_id, then returned in job order. A
    result that errored, expired, or was canceled counts as a failed parse
    for that case-run with the cause in `error`.
    """
    by_id = {}
    requests = []
    for j in jobs:
        cid = custom_id(j["case"]["id"], j["run"], j["arm"], j["prep"]["contract"])
        by_id[cid] = j
        requests.append({"custom_id": cid, "params": j["prep"]["request"]})
    with tracing.span("signal.batch", requests=len(requests)) as sp:
        batch = client.messages.batches.create(requests=requests)
        sp.set_attribute("batch_id", batch.id)
        log(f"batch {batch.id}: {len(requests)} request(s) submitted, polling until it ends")

        wait = first_wait
        while True:
            batch = client.messages.batches.retrieve(batch.id)
            counts = getattr(batch, "request_counts", None)
            log(f"batch {batch.id}: {batch.processing_status}"
                + (f" · processing {counts.processing} · succeeded {counts.succeeded} · errored {counts.errored}"
                   if counts is not None else ""))
            if batch.processing_status == "ended":
                break
            sleep(wait)
            wait = min(wait * 2, max_wait)
        outcomes = _collect_batch(client, batch, by_id, log)
    return _score_batch(by_id, outcomes, log)


def _collect_batch(client, batch, by_id: dict, log) -> dict:
    outcomes = {}
    for item in client.messages.batches.results(batch.id):
        j = by_id.get(item.custom_id)
        if j is None:
            log(f"batch {batch.id}: ignoring unknown custom_id {item.custom_id}")
            continue
        prep, contract = j["prep"], j["prep"]["contract"]
        brief, meta, error, raw_head = None, None, None, None
        if item.result.type == "succeeded":
            try:
                brief, meta = finish_analysis(item.result.message, contract=contract, request=prep["request"])
            except ParseFailure as e:
                meta = getattr(e, "meta", _failed_meta(prep["request"], contract))
                error = str(e)
                raw_head = (e.raw or "")[:800]
        else:
            meta = _failed_meta(prep["request"], contract)
            error = _batch_error(item.result)
        outcomes[item.custom_id] = (brief, meta, error, raw_head)
    return outcomes


def _score_batch(by_id: dict, outcomes: dict, log) -> list[dict]:
    results = []
    for cid, j in by_id.items():
        brief, meta, error, raw_head = outcomes.get(cid) or (
            None, _failed_meta(j["prep"]["request"], j["prep"]["contract"]), "batch returned no result for this custom_id", None)
        r = finish_case(j["case"], j["prep"], brief=brief, meta=meta, error=error, raw_head=raw_head, batch=True)
        r["run"] = j["run"]
        r["expected_risk"] = j["case"]["expected"].get("risk_types", [])
        r["custom_id"] = cid
        results.append(r)
        sc = r["scores"]
        log(f"[{r['run']}] {r['case']:<30} risk={(r['brief'] or {}).get('risk_type')!s:<26} recall={sc['risk']['recall']:.2f} "
            f"buyer={'✓' if sc['buyer'] else '✗'} parse={(r['meta'] or {}).get('parse_path')}"
            + (f"  ERROR {r['error'][:80]}" if r["error"] else ""))
    return results


# ── Cost ─────────────────────────────────────────────────────────────
# Only the analysis call records tokens; the per-document summary calls do
# not, so every dollar figure below covers the analysis call and says so.
COST_COVERS = "analysis call"


def attach_cost(meta: dict | None, *, batch: bool = False, model: str | None = None) -> dict | None:
    """Add `cost_usd` to a meta dict from its recorded tokens. None when the
    tokens were not recorded, so a table can say so instead of guessing."""
    if meta is None:
        return None
    meta["cost_usd"] = config.cost_usd(
        model or meta.get("model") or config.MODELS["analysis"],
        meta.get("input_tokens"), meta.get("output_tokens"), batch=batch,
    )
    return meta


def pricing(batch: bool = False) -> dict:
    return {"dated": config.PRICES_DATED, "batch": batch,
            "multiplier": config.BATCH_MULTIPLIER if batch else 1.0, "covers": COST_COVERS}


def aggregate(results: list[dict], *, batch: bool = False) -> dict:
    n = len(results) or 1
    s = [r["scores"] for r in results]
    paths = {p: 0 for p in ("native", "recovered_by_parser", "failed")}
    for r in results:
        paths[(r["meta"] or {}).get("parse_path", "failed")] += 1
    tok_in = [r["meta"].get("input_tokens") for r in results if r["meta"] and r["meta"].get("input_tokens") is not None]
    tok_out = [r["meta"].get("output_tokens") for r in results if r["meta"] and r["meta"].get("output_tokens") is not None]
    lat = [r["meta"].get("latency_ms") for r in results if r["meta"] and r["meta"].get("latency_ms") is not None]
    costs = [r["meta"].get("cost_usd") for r in results if r["meta"] and r["meta"].get("cost_usd") is not None]
    return {
        "n": len(results),
        "risk_recall": sum(x["risk"]["recall"] for x in s) / n,
        "risk_precision": sum(x["risk"]["precision"] for x in s) / n,
        "buyer_accuracy": sum(1 for x in s if x["buyer"]) / n,
        "attribution_coverage": sum(x["attribution"]["coverage"] for x in s) / n,
        "gaps_ok": sum(1 for x in s if x["gaps_ok"]) / n,
        "parse_paths": paths,
        "mean_input_tokens": (sum(tok_in) / len(tok_in)) if tok_in else None,
        "mean_output_tokens": (sum(tok_out) / len(tok_out)) if tok_out else None,
        "mean_latency_ms": (sum(lat) / len(lat)) if lat else None,
        # Per run is one case, one pass; whole run is every case-run summed.
        # Both cover the analysis call only, at list or batch price.
        "cost_per_run_usd": (sum(costs) / len(costs)) if costs else None,
        "cost_total_usd": sum(costs) if costs else None,
        "cost_covers": COST_COVERS,
        "pricing": pricing(batch),
        "hard_fails": sum(1 for r in results if r["hard_fail"]),
    }


def _pct(x) -> str:
    return "—" if x is None else f"{100 * x:.0f}%"


def _num(x, unit="") -> str:
    return "—" if x is None else f"{x:,.0f}{unit}"


def _usd(x) -> str:
    return "not recorded" if x is None else f"${x:.4f}"


def cost_rows(agg: dict) -> list[str]:
    """The three cost rows of the aggregate block; recost.py rewrites these
    into older tables, so they live in one place."""
    p = agg.get("pricing") or pricing()
    basis = f"batch ({p['multiplier']:g}× list)" if p.get("batch") else "list"
    return [
        f"| Cost per run ({COST_COVERS}, USD) | {_usd(agg.get('cost_per_run_usd'))} |",
        f"| Cost for the whole run ({COST_COVERS}s, USD) | {_usd(agg.get('cost_total_usd'))} |",
        f"| Prices | {basis}, read {p['dated']} |",
    ]


CASE_HEADER = "| Case | Expected risk | Predicted | Recall | Buyer | Attribution | Gaps | Parse | ms | Cost |"


def render_table(results: list[dict], agg: dict, *, mode: str, contract: str, arm: str, runs: int,
                 batch: bool = False) -> str:
    lines = [
        f"# Signal eval — {date.today().isoformat()} · mode `{mode}` · contract `{contract}` · arm `{arm}` · {runs} run(s) per case"
        + (" · batch" if batch else ""),
        "",
        "| Metric | Value |",
        "| --- | --- |",
        f"| Cases × runs | {agg['n']} |",
        f"| Risk-type recall (primary) | {_pct(agg['risk_recall'])} |",
        f"| Risk-type precision | {_pct(agg['risk_precision'])} |",
        f"| Economic-buyer accuracy | {_pct(agg['buyer_accuracy'])} |",
        f"| Attribution coverage | {_pct(agg['attribution_coverage'])} |",
        f"| Data gaps present when expected | {_pct(agg['gaps_ok'])} |",
        f"| Parse: native / recovered / failed | {agg['parse_paths']['native']} / {agg['parse_paths']['recovered_by_parser']} / {agg['parse_paths']['failed']} |",
        f"| Mean tokens in / out (analysis call) | {_num(agg['mean_input_tokens'])} / {_num(agg['mean_output_tokens'])} |",
        f"| Mean analysis latency | {_num(agg['mean_latency_ms'], ' ms')} |",
        *cost_rows(agg),
        f"| Hard fails | {agg['hard_fails']} |",
        "",
        CASE_HEADER,
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in results:
        exp = ", ".join(r["expected_risk"]) or "(none)"
        pred = (r["brief"] or {}).get("risk_type") or ("FAILED" if r["error"] else "—")
        sc = r["scores"]
        attr = sc["attribution"]
        attr_s = _pct(attr["coverage"]) + (f" (missing {', '.join(attr['missing'])})" if attr["missing"] else "")
        meta = r["meta"] or {}
        lat = meta.get("latency_ms")
        lines.append(
            f"| {r['case']}{' #' + str(r['run']) if runs > 1 else ''} | {exp} | {pred} | {_pct(sc['risk']['recall'])} | "
            f"{'✓' if sc['buyer'] else '✗'} | {attr_s} | {'✓' if sc['gaps_ok'] else '✗'} | "
            f"{meta.get('parse_path', 'failed')} | {'—' if lat is None else lat} | {_usd(meta.get('cost_usd'))} |"
        )
    return "\n".join(lines) + "\n"


def print_dry_run(cases: list[dict], *, mode: str, weighted: bool) -> None:
    total1 = total2 = 0
    print(f"{'case':30s} {'docs':>4s} {'media':>5s} {'call1 tok':>10s} {'call2 ≤ tok':>12s} {'naive tok':>10s}")
    for c in cases:
        docs = case_docs(c)
        a = c["account"]
        est = dryrun.estimate(docs, a.get("account"), a.get("contact"), a.get("renewal_days"), a.get("arr"),
                              mode=mode, weighted=weighted)
        m = len(media_names(str(c["dir"])))
        total1 += est["call1_total"]; total2 += est["call2_ceiling"]
        print(f"{c['id']:30s} {len(docs):4d} {m:5d} {est['call1_total']:10d} {est['call2_ceiling']:12d} {est['naive_prompt']:10d}")
    print(f"\nPer pass over {len(cases)} cases: Call 1 ≈ {total1} input tokens, Call 2 ≤ {total2} input tokens "
          f"(text only; PNG/PDF blocks add to Call 2 and are not estimated here).")
    print("No API calls were made (--dry-run).")


def parse_args(argv=None):
    p = argparse.ArgumentParser(prog="evals/run.py", description="Score Signal against the golden set")
    p.add_argument("--golden", default=str(GOLDEN))
    p.add_argument("--mode", choices=list(FOCUS_INSTRUCTIONS), default="full")
    p.add_argument("--contract", choices=list(CONTRACTS), default="prompt")
    p.add_argument("--arm", choices=list(ARMS), default="weighted",
                   help="source-weighting ablation arm (default: weighted, the prompt as shipped)")
    p.add_argument("--runs", type=int, default=1, help="repeat each case N times")
    p.add_argument("--only", action="append", help="run one case (repeatable)")
    p.add_argument("--dry-run", action="store_true", help="print token estimates and exit")
    p.add_argument("--batch", action="store_true",
                   help="send the analysis calls through the Message Batches API (half price, same scoring); "
                        "the per-document summaries stay live")
    p.add_argument("--out", default=str(RESULTS))
    p.add_argument("--trace", metavar="FILE.json", default=None,
                   help="write one OpenTelemetry span per line to this file (pip install -r requirements-trace.txt)")
    return p.parse_args(argv)


def main(argv=None, client=None, sleep=time.sleep) -> int:
    args = parse_args(argv)
    cases = load_cases(Path(args.golden), args.only)
    weighted = ARMS[args.arm]
    if args.trace:
        tracing.install_json_exporter(args.trace)
    if args.dry_run:
        print_dry_run(cases, mode=args.mode, weighted=weighted)
        return 0

    if client is None:
        if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
            print("No Anthropic credentials found. Set ANTHROPIC_API_KEY, or use --dry-run.", file=sys.stderr)
            return 2
        client = config.get_client()

    results = []
    interrupted = False
    planned = args.runs * len(cases)
    try:
        if args.batch:
            jobs = []
            for run in range(1, args.runs + 1):
                for c in cases:
                    print(f"[{run}/{args.runs}] {c['id']}: summarizing and preparing the analysis request", flush=True)
                    with tracing.span("signal.brief", case=c["id"], run=run, mode=args.mode, contract=args.contract, arm=args.arm):
                        prep = prepare_case(client, c, mode=args.mode, contract=args.contract, weighted=weighted)
                    jobs.append({"case": c, "run": run, "arm": args.arm, "prep": prep})
            results = run_batch(client, jobs, sleep=sleep)
        else:
            for run in range(1, args.runs + 1):
                for c in cases:
                    print(f"[{run}/{args.runs}] {c['id']} …", end=" ", flush=True)
                    with tracing.span("signal.brief", case=c["id"], run=run, mode=args.mode, contract=args.contract, arm=args.arm):
                        r = run_case(client, c, mode=args.mode, contract=args.contract, weighted=weighted)
                    r["run"] = run
                    r["expected_risk"] = c["expected"].get("risk_types", [])
                    results.append(r)
                    sc = r["scores"]
                    print(f"risk={(r['brief'] or {}).get('risk_type')!s:<26} recall={sc['risk']['recall']:.2f} "
                          f"buyer={'✓' if sc['buyer'] else '✗'} parse={(r['meta'] or {}).get('parse_path')}"
                          + (f"  ERROR {r['error'][:80]}" if r["error"] else ""))
    except KeyboardInterrupt:
        # Ctrl+C, or credit running out mid-run, used to lose every finished
        # case. Write what completed, marked partial, and say so. A batch
        # has nothing finished until it ends, so an interrupt there writes
        # nothing.
        interrupted = True
        print(f"\ninterrupted after {len(results)} of {planned} case-runs; writing the partial table", file=sys.stderr)
    if not results:
        return 130 if interrupted else 1

    agg = aggregate(results, batch=args.batch)
    table = render_table(results, agg, mode=args.mode, contract=args.contract, arm=args.arm, runs=args.runs,
                         batch=args.batch)
    if interrupted:
        table = table.replace("\n", f" · PARTIAL: {len(results)} of {planned} case-runs\n", 1)
    print("\n" + table)

    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    # More than one run per case gets a suffix, so a twenty-run table never
    # overwrites the single pass written earlier the same day.
    stem = (f"{date.today().isoformat()}-{args.mode}-{args.contract}-{args.arm}" + (f"-x{args.runs}" if args.runs > 1 else "")
            + ("-batch" if args.batch else "") + ("-partial" if interrupted else ""))
    # Explicit UTF-8: Windows defaults to cp1252, which cannot encode the table.
    (out / f"{stem}.md").write_text(table, encoding="utf-8")
    (out / f"{stem}.json").write_text(json.dumps({
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mode": args.mode, "contract": args.contract, "arm": args.arm, "runs": args.runs, "batch": args.batch,
        "completed": len(results), "planned": planned, "partial": interrupted,
        "models": config.MODELS, "pricing": agg["pricing"], "aggregate": agg,
        "results": [{k: v for k, v in r.items() if k != "brief"} | {"brief": r["brief"]} for r in results],
    }, indent=2, default=str), encoding="utf-8")
    print(f"Wrote {out / (stem + '.md')} and .json")
    if interrupted:
        return 130
    if agg["hard_fails"]:
        print(f"HARD FAIL: {agg['hard_fails']} case(s) failed to parse or returned an empty brief with expected risks.",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
