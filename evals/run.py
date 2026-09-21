#!/usr/bin/env python3
"""Score Signal's analysis brief against the golden set.

    python evals/run.py --dry-run                    # token estimate per case, no API calls
    python evals/run.py                              # full mode, prompt contract, weighted
    python evals/run.py --contract native            # the same set under native structured outputs
    python evals/run.py --arm unweighted --runs 20   # one arm of the source-weighting ablation
    python evals/run.py --mode revenue               # any focus mode

Reuses the CLI's pipeline functions (ingest, summarize, analyze) rather than
re-implementing them, so a score here is a score for the real pipeline.
Writes a markdown table to evals/results/<date>-<mode>-<contract>-<arm>.md and
the raw briefs beside it as JSON.
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
from analyze import CONTRACTS, ParseFailure, analyze_brief, build_analysis_prompt  # noqa: E402
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


def run_case(client, case: dict, *, mode: str, contract: str, weighted: bool) -> dict:
    docs = case_docs(case)
    media = read_media(str(case["dir"]))
    acct = case["account"]
    t0 = time.perf_counter()
    summaries = summarize_all(client, docs)
    prompt = build_analysis_prompt(
        acct.get("account"), acct.get("contact"), acct.get("renewal_days"), acct.get("arr"),
        summaries, mode=mode, weighted=weighted,
    )
    brief, meta, error, raw_head = None, None, None, None
    try:
        brief, meta = analyze_brief(client, prompt, contract=contract, media=media, mode=mode)
    except ParseFailure as e:
        meta = getattr(e, "meta", {"parse_path": "failed"})
        error = str(e)
        raw_head = (e.raw or "")[:800]  # kept in the JSON so a failure can be diagnosed
    total_ms = round((time.perf_counter() - t0) * 1000)
    scores = score_case(case["expected"], brief)
    return {
        "case": case["id"], "brief": brief, "meta": meta, "error": error, "raw_head": raw_head,
        "scores": scores, "total_ms": total_ms, "docs": len(docs), "media": len(media),
        "hard_fail": (meta or {}).get("parse_path") == "failed"
                     or (scores["empty"] and bool(case["expected"].get("risk_types"))),
    }


def aggregate(results: list[dict]) -> dict:
    n = len(results) or 1
    s = [r["scores"] for r in results]
    paths = {p: 0 for p in ("native", "recovered_by_parser", "failed")}
    for r in results:
        paths[(r["meta"] or {}).get("parse_path", "failed")] += 1
    tok_in = [r["meta"].get("input_tokens") for r in results if r["meta"] and r["meta"].get("input_tokens") is not None]
    tok_out = [r["meta"].get("output_tokens") for r in results if r["meta"] and r["meta"].get("output_tokens") is not None]
    lat = [r["meta"].get("latency_ms") for r in results if r["meta"] and r["meta"].get("latency_ms") is not None]
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
        "hard_fails": sum(1 for r in results if r["hard_fail"]),
    }


def _pct(x) -> str:
    return "—" if x is None else f"{100 * x:.0f}%"


def _num(x, unit="") -> str:
    return "—" if x is None else f"{x:,.0f}{unit}"


def render_table(results: list[dict], agg: dict, *, mode: str, contract: str, arm: str, runs: int) -> str:
    lines = [
        f"# Signal eval — {date.today().isoformat()} · mode `{mode}` · contract `{contract}` · arm `{arm}` · {runs} run(s) per case",
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
        f"| Hard fails | {agg['hard_fails']} |",
        "",
        "| Case | Expected risk | Predicted | Recall | Buyer | Attribution | Gaps | Parse | ms |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in results:
        exp = ", ".join(r["expected_risk"]) or "(none)"
        pred = (r["brief"] or {}).get("risk_type") or ("FAILED" if r["error"] else "—")
        sc = r["scores"]
        attr = sc["attribution"]
        attr_s = _pct(attr["coverage"]) + (f" (missing {', '.join(attr['missing'])})" if attr["missing"] else "")
        lines.append(
            f"| {r['case']}{' #' + str(r['run']) if runs > 1 else ''} | {exp} | {pred} | {_pct(sc['risk']['recall'])} | "
            f"{'✓' if sc['buyer'] else '✗'} | {attr_s} | {'✓' if sc['gaps_ok'] else '✗'} | "
            f"{(r['meta'] or {}).get('parse_path', 'failed')} | {(r['meta'] or {}).get('latency_ms', '—')} |"
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
    p.add_argument("--out", default=str(RESULTS))
    return p.parse_args(argv)


def main(argv=None, client=None) -> int:
    args = parse_args(argv)
    cases = load_cases(Path(args.golden), args.only)
    weighted = ARMS[args.arm]
    if args.dry_run:
        print_dry_run(cases, mode=args.mode, weighted=weighted)
        return 0

    if client is None:
        if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
            print("No Anthropic credentials found. Set ANTHROPIC_API_KEY, or use --dry-run.", file=sys.stderr)
            return 2
        client = config.get_client()

    results = []
    for run in range(1, args.runs + 1):
        for c in cases:
            print(f"[{run}/{args.runs}] {c['id']} …", end=" ", flush=True)
            r = run_case(client, c, mode=args.mode, contract=args.contract, weighted=weighted)
            r["run"] = run
            r["expected_risk"] = c["expected"].get("risk_types", [])
            results.append(r)
            sc = r["scores"]
            print(f"risk={(r['brief'] or {}).get('risk_type')!s:<26} recall={sc['risk']['recall']:.2f} "
                  f"buyer={'✓' if sc['buyer'] else '✗'} parse={(r['meta'] or {}).get('parse_path')}"
                  + (f"  ERROR {r['error'][:80]}" if r["error"] else ""))

    agg = aggregate(results)
    table = render_table(results, agg, mode=args.mode, contract=args.contract, arm=args.arm, runs=args.runs)
    print("\n" + table)

    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    stem = f"{date.today().isoformat()}-{args.mode}-{args.contract}-{args.arm}"
    # Explicit UTF-8: Windows defaults to cp1252, which cannot encode the table.
    (out / f"{stem}.md").write_text(table, encoding="utf-8")
    (out / f"{stem}.json").write_text(json.dumps({
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mode": args.mode, "contract": args.contract, "arm": args.arm, "runs": args.runs,
        "models": config.MODELS, "aggregate": agg,
        "results": [{k: v for k, v in r.items() if k != "brief"} | {"brief": r["brief"]} for r in results],
    }, indent=2, default=str), encoding="utf-8")
    print(f"Wrote {out / (stem + '.md')} and .json")
    if agg["hard_fails"]:
        print(f"HARD FAIL: {agg['hard_fails']} case(s) failed to parse or returned an empty brief with expected risks.",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
