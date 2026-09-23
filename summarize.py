"""Call 1: summarize each document individually (cheap, keeps tokens small)."""
from __future__ import annotations

import time

from config import MODELS, MAX_SUMMARY_TOKENS
from prompts import SUMMARIZE_PROMPT
import tracing


def _text(resp) -> str:
    return "".join(b.text for b in resp.content if b.type == "text").strip()


def summarize_doc(client, doc: dict) -> str:
    """Summarize one (already truncated) document into ~3-5 sentences."""
    prompt = SUMMARIZE_PROMPT.format(
        doc_type=doc["type"],
        doc_name=doc["name"],
        content=doc["content"],
    )
    usage = None
    with tracing.span("signal.summarize", model=MODELS["summary"], name=doc["name"], label=doc["type"]) as sp:
        t0 = time.perf_counter()
        resp = client.messages.create(
            model=MODELS["summary"],
            max_tokens=MAX_SUMMARY_TOKENS,
            messages=[{"role": "user", "content": prompt}],
        )
        usage = getattr(resp, "usage", None)
        sp.set_attributes({
            "latency_ms": round((time.perf_counter() - t0) * 1000),
            "input_tokens": getattr(usage, "input_tokens", None),
            "output_tokens": getattr(usage, "output_tokens", None),
        })
    return _text(resp)


def summarize_all(client, docs: list[dict], on_progress=None) -> list[dict]:
    """Summarize every doc. Returns [{name, type, summary}, ...]."""
    summaries = []
    for i, doc in enumerate(docs, 1):
        if on_progress:
            on_progress(i, len(docs), doc["name"])
        summaries.append({
            "name": doc["name"],
            "type": doc["type"],
            "summary": summarize_doc(client, doc),
        })
    return summaries
