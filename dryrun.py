"""Token estimates for a run, without calling the API.

Shared by the CLI's --dry-run and the eval runner's --dry-run so both report
the same numbers for the same documents.
"""
from __future__ import annotations

import config
from analyze import build_analysis_prompt
from ingest import estimate_tokens
from prompts import SUMMARIZE_PROMPT


def estimate(docs: list[dict], account: str, contact: str, renewal_days, arr,
             *, mode: str = "full", weighted: bool = True) -> dict:
    """Return per-doc rows and the Call 1 / Call 2 / naive totals."""
    rows = []
    call1_total = 0
    for d in docs:
        prompt = SUMMARIZE_PROMPT.format(doc_type=d["type"], doc_name=d["name"], content=d["content"])
        ptok = estimate_tokens(prompt)
        call1_total += ptok
        rows.append({
            "name": d["name"], "type": d["type"],
            "raw_tokens": estimate_tokens(d["raw"]),
            "truncated_tokens": estimate_tokens(d["content"]),
            "prompt_tokens": ptok,
        })

    # Ceiling for Call 2: summaries are bounded by MAX_SUMMARY_TOKENS each,
    # regardless of how large the raw docs are. That bound is the whole point.
    placeholder = "x" * (config.MAX_SUMMARY_TOKENS * config.CHARS_PER_TOKEN)
    call2_ceiling = estimate_tokens(build_analysis_prompt(
        account, contact, renewal_days, arr,
        [{"type": d["type"], "name": d["name"], "summary": placeholder} for d in docs],
        mode=mode, weighted=weighted,
    ))
    # Apples-to-apples naive baseline: the same analysis prompt with the full
    # raw docs inlined instead of summaries.
    naive_prompt = estimate_tokens(build_analysis_prompt(
        account, contact, renewal_days, arr,
        [{"type": d["type"], "name": d["name"], "summary": d["raw"]} for d in docs],
        mode=mode, weighted=weighted,
    ))
    return {
        "rows": rows,
        "call1_total": call1_total,
        "call2_ceiling": call2_ceiling,
        "summary_cap": config.MAX_SUMMARY_TOKENS * len(docs),
        "naive_prompt": naive_prompt,
    }
