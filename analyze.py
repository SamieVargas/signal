"""Call 2: synthesize doc summaries into a structured account brief."""
from __future__ import annotations

import json
import re

from config import MODELS, MAX_ANALYSIS_TOKENS
from prompts import ANALYZE_PROMPT


def format_summaries(summaries: list[dict]) -> str:
    return "\n\n".join(
        f"[{s['type']}] {s['name']}\n{s['summary']}" for s in summaries
    )


def build_analysis_prompt(account, contacts, renewal_days, arr, summaries) -> str:
    return ANALYZE_PROMPT.format(
        account_name=account or "Unknown",
        contacts=contacts or "Unknown",
        renewal_days=renewal_days if renewal_days is not None else "Unknown",
        arr=arr or "Unknown",
        summaries=format_summaries(summaries),
    )


def extract_json(text: str) -> dict:
    """Parse the model's JSON, tolerating stray markdown fences or prose."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text).strip()
    # Fall back to the outermost { ... } if there's surrounding prose.
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end != -1 and end > start:
        text = text[start:end + 1]
    return json.loads(text)


def analyze(client, prompt: str) -> dict:
    resp = client.messages.create(
        model=MODELS["analysis"],
        max_tokens=MAX_ANALYSIS_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = "".join(b.text for b in resp.content if b.type == "text")
    return extract_json(raw)
