"""Call 2: synthesize doc summaries into a structured account brief.

Two contracts are supported and measured against each other:

- `prompt`: the JSON shape is described in the prompt and the model is asked
  to return only JSON. A tolerant parser recovers fenced or prose-wrapped
  output.
- `native`: the same shape is sent as a JSON Schema in `output_config.format`,
  so the API constrains the response. The tolerant parser stays as the
  fallback path, and every call records which path handled the response.
"""
from __future__ import annotations

import json
import re
import time

from config import MODELS, MAX_ANALYSIS_TOKENS
from prompts import ANALYZE_PROMPT, FOCUS_INSTRUCTIONS, FOCUS_MAX_TOKENS, RISK_TYPES, SOURCE_WEIGHTING
import schema

CONTRACTS = ("prompt", "native")
PARSE_PATHS = ("native", "recovered_by_parser", "failed")


class ParseFailure(ValueError):
    """The response could not be turned into a brief by any path."""

    def __init__(self, raw: str, cause, *, reason: str = "parse"):
        super().__init__(f"could not parse analysis JSON: {cause}")
        self.raw = raw
        self.reason = reason  # "parse" or "max_tokens"


def format_summaries(summaries: list[dict]) -> str:
    return "\n\n".join(
        f"[{s['type']}] {s['name']}\n{s['summary']}" for s in summaries
    )


def build_analysis_prompt(account, contacts, renewal_days, arr, summaries,
                          *, mode: str = "full", weighted: bool = True) -> str:
    """Render the analysis prompt.

    `weighted=False` drops the source-weighting and economic-buyer block; it
    exists for the ablation and nothing else should turn it off.
    """
    if mode not in FOCUS_INSTRUCTIONS:
        raise ValueError(f"unknown focus mode {mode!r}; expected one of {list(FOCUS_INSTRUCTIONS)}")
    return ANALYZE_PROMPT.format(
        weighting=(SOURCE_WEIGHTING + "\n") if weighted else "",
        focus=FOCUS_INSTRUCTIONS[mode],
        account_name=account or "Unknown",
        contacts=contacts or "Unknown",
        renewal_days=renewal_days if renewal_days is not None else "Unknown",
        arr=arr or "Unknown",
        summaries=format_summaries(summaries),
        risk_types=" | ".join(RISK_TYPES),
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


def parse_brief(raw: str) -> tuple[dict, str]:
    """Return (brief, parse_path). `native` means the raw text was valid JSON
    as-is; `recovered_by_parser` means fences or prose had to be stripped."""
    try:
        return json.loads(raw), "native"
    except (json.JSONDecodeError, TypeError):
        pass
    try:
        return extract_json(raw), "recovered_by_parser"
    except (json.JSONDecodeError, TypeError, ValueError) as e:
        raise ParseFailure(raw, e)


def _text(resp) -> str:
    return "".join(b.text for b in resp.content if b.type == "text")


def _usage(resp, key: str):
    usage = getattr(resp, "usage", None)
    return getattr(usage, key, None) if usage is not None else None


def analyze_brief(client, prompt: str, *, contract: str = "prompt", media=None,
                  mode: str = "full", model: str | None = None,
                  max_tokens: int | None = None) -> tuple[dict, dict]:
    """Run the analysis call and return (brief, meta).

    meta: contract, parse_path, stop_reason, input_tokens, output_tokens,
    latency_ms. Raises ParseFailure when neither path yields JSON, after
    filling meta["parse_path"] = "failed" on the exception for the caller.
    """
    if contract not in CONTRACTS:
        raise ValueError(f"unknown contract {contract!r}; expected one of {CONTRACTS}")
    content = [{"type": "text", "text": prompt}, *media] if media else prompt
    kwargs = dict(
        model=model or MODELS["analysis"],
        max_tokens=max_tokens or FOCUS_MAX_TOKENS.get(mode, MAX_ANALYSIS_TOKENS),
        messages=[{"role": "user", "content": content}],
    )
    if contract == "native":
        kwargs["output_config"] = schema.output_config()

    t0 = time.perf_counter()
    resp = client.messages.create(**kwargs)
    latency_ms = round((time.perf_counter() - t0) * 1000)
    raw = _text(resp)
    meta = {
        "model": kwargs["model"],
        "contract": contract,
        "parse_path": "failed",
        "stop_reason": getattr(resp, "stop_reason", None),
        "input_tokens": _usage(resp, "input_tokens"),
        "output_tokens": _usage(resp, "output_tokens"),
        "latency_ms": latency_ms,
    }
    # A reply cut off at the output cap is not a parsing problem, and it is
    # worth naming as what it is, because raising max_tokens is the fix.
    if meta["stop_reason"] == "max_tokens":
        e = ParseFailure(raw, f"reply cut off at max_tokens={kwargs['max_tokens']}; raise the budget", reason="max_tokens")
        e.meta = meta
        raise e
    try:
        brief, path = parse_brief(raw)
    except ParseFailure as e:
        e.meta = meta
        raise
    meta["parse_path"] = path
    return brief, meta


def analyze(client, prompt: str) -> dict:
    """Backward-compatible entry point: prompt contract, brief only."""
    brief, _ = analyze_brief(client, prompt)
    return brief
