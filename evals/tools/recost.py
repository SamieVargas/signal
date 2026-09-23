#!/usr/bin/env python3
"""Rewrite the cost rows and the cost column of existing results tables.

    python evals/tools/recost.py                         # every evals/results/*.json
    python evals/tools/recost.py evals/results/2026-09-21-full-prompt-weighted.json

Reads the tokens recorded in each results JSON, prices them with
config.PRICES (list, or batch when the JSON says the run went through the
Batch API), and rewrites only the cost rows of the aggregate block and the
Cost column of the case table in the .md beside it. Every other line of the
table is left byte for byte as it was, so this never re-runs or re-scores
anything. Rows are matched to JSON results by case and run number, and the
script refuses to write if they do not line up.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
sys.path.insert(0, str(HERE.parent))

import run  # noqa: E402

COST_ROW_PREFIXES = ("| Cost per run", "| Cost for the whole run", "| Prices |")


def recost_results(data: dict) -> tuple[list[dict], dict]:
    """Attach cost_usd to a copy of each result's meta and return them with
    the recomputed aggregate."""
    batch = bool(data.get("batch"))
    model = (data.get("models") or {}).get("analysis")
    results = copy.deepcopy(data["results"])
    for r in results:
        run.attach_cost(r["meta"], batch=batch, model=model)
    return results, run.aggregate(results, batch=batch)


def _row_label(r: dict, runs: int) -> str:
    return r["case"] + (f" #{r['run']}" if runs > 1 else "")


def rewrite_table(md: str, results: list[dict], agg: dict, runs: int) -> str:
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    seen_case_table = False
    while i < len(lines):
        line = lines[i]
        if line.startswith(COST_ROW_PREFIXES):
            i += 1  # drop an existing cost row; the new ones go in below
            continue
        if line.startswith("| Hard fails |"):
            out.extend(run.cost_rows(agg))
            out.append(line)
            i += 1
            continue
        if line.startswith("| Case |"):
            seen_case_table = True
            had_cost = line.rstrip().endswith("| Cost |")
            out.append(run.CASE_HEADER)
            out.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
            i += 2  # header + separator
            rows = []
            while i < len(lines) and lines[i].startswith("| "):
                rows.append(lines[i])
                i += 1
            if len(rows) != len(results):
                raise SystemExit(f"table has {len(rows)} case rows but the JSON has {len(results)} results")
            for row, r in zip(rows, results):
                cells = row.strip().strip("|").split("|")
                label = cells[0].strip()
                if label != _row_label(r, runs):
                    raise SystemExit(f"row {label!r} does not match JSON result {_row_label(r, runs)!r}")
                if had_cost:
                    row = row.rstrip()[: row.rstrip().rfind("|", 0, -1) + 1]
                out.append(f"{row.rstrip()} {run._usd(r['meta'].get('cost_usd'))} |")
            continue
        out.append(line)
        i += 1
    if not seen_case_table:
        raise SystemExit("no case table found in the markdown")
    return "\n".join(out)


def recost_file(json_path: Path) -> Path:
    md_path = json_path.with_suffix(".md")
    if not md_path.exists():
        raise SystemExit(f"{md_path} not found")
    data = json.loads(json_path.read_text(encoding="utf-8"))
    results, agg = recost_results(data)
    md = md_path.read_text(encoding="utf-8")
    new_md = rewrite_table(md, results, agg, int(data.get("runs") or 1))
    md_path.write_text(new_md, encoding="utf-8")
    print(f"{md_path.name}: per run {run._usd(agg['cost_per_run_usd'])}, whole run {run._usd(agg['cost_total_usd'])}"
          f" ({'batch' if agg['pricing']['batch'] else 'list'} prices, {agg['pricing']['dated']})")
    return md_path


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    paths = [Path(a) for a in argv] or sorted(run.RESULTS.glob("*.json"))
    if not paths:
        print("no results JSON files found", file=sys.stderr)
        return 1
    for p in paths:
        recost_file(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
