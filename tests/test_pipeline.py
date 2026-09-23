"""Offline end-to-end test: exercises the whole pipeline with a fake client.

Run from the repo root:
    python tests/test_pipeline.py
No API key required — the Anthropic client is replaced by a stub.
"""
import json
import os
import sys
from types import SimpleNamespace

# Make the package importable when run as a plain script from anywhere.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import MODELS, PRICES, PRICES_DATED, BATCH_MULTIPLIER, cost_usd
from ingest import read_docs, make_doc, smart_truncate, detect_type
from summarize import summarize_all
from analyze import build_analysis_prompt, analyze, analyze_brief, extract_json, parse_brief, ParseFailure
from prompts import RISK_TYPES, SOURCE_WEIGHTING
import schema
from chat import chat_loop

MOCK_DIR = os.path.join(os.path.dirname(__file__), "mock_docs")

SAMPLE_BRIEF = {
    "situation": "Adoption stalled; champion isolated.",
    "risk_type": "Adoption failure",
    "risk_severity": "medium",
    "data_sources_used": ["Kick-off deck", "MBR notes", "Teams chat"],
    "leverage_points": [
        {"rank": 1, "what": "Find active users", "why": "only 3 weekly-active", "timeline": "this week"},
    ],
    "do_this_today": "Send Sarah a 3-bullet usage summary.",
    "contact_persona": {
        "primary_contact": "Sarah Chen",
        "comm_style": "async",
        "decision_style": "consensus",
        "what_they_say_vs_mean": "'exploring' = 'nobody's using it'",
        "approach_recommendation": "give her something to react to",
    },
    "confidence": "medium",
    "confidence_note": "need Marcus's view",
    "suggested_questions": ["Who should be power users?"],
}


def _block(text):
    return SimpleNamespace(type="text", text=text)


def _msg(text, stop_reason="end_turn", usage=None):
    m = SimpleNamespace(content=[_block(text)], stop_reason=stop_reason)
    if usage:  # (input_tokens, output_tokens), the way the API reports them
        m.usage = SimpleNamespace(input_tokens=usage[0], output_tokens=usage[1])
    return m


class FakeMessages:
    def __init__(self, analysis_reply=None, stop_reason="end_turn", usage=None):
        self.calls = []
        # What Call 2 returns; tests swap this to exercise the parse paths.
        self.analysis_reply = analysis_reply or ("```json\n" + json.dumps(SAMPLE_BRIEF) + "\n```")
        self.stop_reason = stop_reason
        self.usage = usage  # analysis-call tokens, None for "not recorded"

    def create(self, model, max_tokens, messages, system=None, **kwargs):
        self.calls.append({"model": model, "max_tokens": max_tokens,
                           "system": system, "messages": messages, **kwargs})
        content = messages[-1]["content"]
        # Media requests carry a list of blocks; the prompt is the first text block.
        user_text = content if isinstance(content, str) else next(b["text"] for b in content if b.get("type") == "text")
        if user_text.lstrip().startswith("You are Signal, an expert CS strategist. Analyze"):
            return _msg(self.analysis_reply, self.stop_reason, self.usage)   # Call 2
        if system is not None:
            return _msg("Here's my read on that.")                          # chat
        return _msg("Tight 3-sentence summary of the doc.")                 # Call 1


class FakeClient:
    def __init__(self, analysis_reply=None, stop_reason="end_turn", usage=None):
        self.messages = FakeMessages(analysis_reply, stop_reason, usage)


def check(name, cond):
    print(f"  {'PASS' if cond else 'FAIL'}  {name}")
    if not cond:
        raise AssertionError(name)


def main():
    print("ingest")
    docs = read_docs(MOCK_DIR)
    check("read 3 mock docs", len(docs) == 3)
    types = {d["type"] for d in docs}
    check("detected Kick-off deck", "Kick-off deck" in types)
    check("detected MBR notes", "MBR notes" in types)
    check("detected Teams chat", "Teams chat" in types)
    check("smart_truncate inserts marker on long input",
          "[... middle truncated ...]" in smart_truncate("A" * 100000))
    check("smart_truncate leaves short input untouched",
          smart_truncate("short") == "short")
    check("detect_type sniffs transcript timestamps",
          detect_type("unknown.dat", "00:01 Sarah: hello") == "Call transcript")

    print("pipeline (fake client)")
    client = FakeClient()
    summaries = summarize_all(client, docs)
    check("one summary per doc", len(summaries) == len(docs))
    check("Call 1 used MAX_SUMMARY_TOKENS cap", client.messages.calls[0]["max_tokens"] == 300)
    check("Call 1 routed to summary model", client.messages.calls[0]["model"] == MODELS["summary"])

    prompt = build_analysis_prompt("Koala", "Sarah Chen, VP", 67, 180000, summaries)
    check("analysis prompt embeds account", "Koala" in prompt)
    check("analysis prompt embeds summaries", "Tight 3-sentence" in prompt)

    brief = analyze(client, prompt)
    check("analyze parses fenced JSON", brief["risk_type"] == "Adoption failure")
    check("brief has leverage points", brief["leverage_points"][0]["rank"] == 1)
    check("Call 2 routed to analysis model",
          client.messages.calls[len(docs)]["model"] == MODELS["analysis"])

    print("extract_json robustness")
    check("plain JSON", extract_json('{"a": 1}') == {"a": 1})
    check("fenced JSON", extract_json('```json\n{"a": 1}\n```') == {"a": 1})
    check("JSON with surrounding prose",
          extract_json('Sure!\n{"a": 1}\nDone.') == {"a": 1})

    print("contract")
    check("analysis prompt carries the source-weighting block by default",
          SOURCE_WEIGHTING.splitlines()[0] in prompt)
    unweighted = build_analysis_prompt("Koala", "Sarah Chen, VP", 67, 180000, summaries, weighted=False)
    check("weighted=False drops it and nothing else",
          SOURCE_WEIGHTING.splitlines()[0] not in unweighted and "SOURCE ATTRIBUTION" in unweighted)
    check("prompt lists every risk type", all(r in prompt for r in RISK_TYPES))
    sch = schema.analysis_schema()
    check("schema risk_type enum is the taxonomy constant", sch["properties"]["risk_type"]["enum"] == RISK_TYPES)
    check("schema persona fields match the constant",
          list(sch["properties"]["contact_persona"]["properties"]) == ["primary_contact", "comm_style", "decision_style", "what_they_say_vs_mean", "approach_recommendation"])
    check("schema is strict at every level", sch["additionalProperties"] is False
          and sch["properties"]["contact_persona"]["additionalProperties"] is False)

    print("native contract request shape")
    native_client = FakeClient(analysis_reply=json.dumps(SAMPLE_BRIEF))
    brief_n, meta_n = analyze_brief(native_client, prompt, contract="native")
    req = native_client.messages.calls[-1]
    check("native sends output_config.format.type=json_schema",
          req.get("output_config", {}).get("format", {}).get("type") == "json_schema")
    check("native schema in the request is the one schema.py builds",
          req["output_config"]["format"]["schema"] == sch)
    check("native reply parsed on the native path", meta_n["parse_path"] == "native" and meta_n["contract"] == "native")
    check("prompt contract sends no output_config", "output_config" not in client.messages.calls[len(docs)])

    print("parse paths")
    check("clean JSON -> native", parse_brief('{"a": 1}')[1] == "native")
    check("fenced JSON -> recovered_by_parser", parse_brief('```json\n{"a": 1}\n```')[1] == "recovered_by_parser")
    check("prose-wrapped JSON -> recovered_by_parser", parse_brief('Sure!\n{"a": 1}\nDone.')[1] == "recovered_by_parser")
    fenced_client = FakeClient()  # default reply is fenced on purpose
    _, meta_f = analyze_brief(fenced_client, prompt, contract="native")
    check("fallback path is recorded when a native reply still needs recovery", meta_f["parse_path"] == "recovered_by_parser")
    broken = FakeClient(analysis_reply="I could not produce a brief for this account.")
    try:
        analyze_brief(broken, prompt)
        check("unparseable reply raises ParseFailure", False)
    except ParseFailure as e:
        check("unparseable reply raises ParseFailure", True)
        check("ParseFailure carries meta with parse_path=failed", e.meta["parse_path"] == "failed")

    print("token cap")
    check("full mode asks for the browser's 4000-token budget",
          client.messages.calls[len(docs)]["max_tokens"] == 4000)
    cut = FakeClient(analysis_reply=json.dumps(SAMPLE_BRIEF)[:200], stop_reason="max_tokens")
    try:
        analyze_brief(cut, prompt)
        check("a max_tokens reply raises ParseFailure", False)
    except ParseFailure as e:
        check("a max_tokens reply raises ParseFailure", True)
        check("and names the token cap as the reason", e.reason == "max_tokens" and "max_tokens=4000" in str(e))
        check("meta records stop_reason", e.meta["stop_reason"] == "max_tokens" and e.meta["parse_path"] == "failed")

    print("media blocks")
    media = [{"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": "AAAA"}}]
    media_client = FakeClient(analysis_reply=json.dumps(SAMPLE_BRIEF))
    analyze_brief(media_client, prompt, media=media)
    content = media_client.messages.calls[-1]["messages"][0]["content"]
    check("prompt becomes the first text block, media follow",
          isinstance(content, list) and content[0]["type"] == "text" and content[1]["type"] == "image")

    print("chat loop (injected io)")
    replies = []
    scripted = iter(["what changed?", "quit"])
    chat_loop(client, brief, summaries,
              ask=lambda _p: next(scripted), say=replies.append)
    check("chat produced a reply", replies == ["Here's my read on that."])
    check("chat sent system prompt", client.messages.calls[-1]["system"] is not None)
    check("chat routed to chat model", client.messages.calls[-1]["model"] == MODELS["chat"])

    print("cost per call")
    check("price table names both models the pipeline calls",
          MODELS["analysis"] in PRICES and MODELS["summary"] in PRICES and len(PRICES_DATED) == 10)
    check("one million tokens each way at Sonnet list price",
          cost_usd("claude-sonnet-4-6", 1_000_000, 1_000_000) == 18.0)
    check("Haiku list price", cost_usd("claude-haiku-4-5", 1_000_000, 1_000_000) == 6.0)
    check("batch applies the multiplier",
          BATCH_MULTIPLIER == 0.5 and cost_usd("claude-sonnet-4-6", 1_000_000, 1_000_000, batch=True) == 9.0)
    check("the recorded run: 4,579 in / 1,974 out costs $0.0433 at list",
          round(cost_usd("claude-sonnet-4-6", 4579, 1974), 4) == 0.0433)
    check("missing tokens give None, not zero", cost_usd("claude-sonnet-4-6", None, 10) is None)
    try:
        cost_usd("claude-nonexistent", 1, 1)
        check("an unpriced model raises", False)
    except KeyError:
        check("an unpriced model raises", True)
    check("analysis meta records the model it called", meta_n["model"] == MODELS["analysis"])

    print("paste-mode doc")
    d = make_doc("pasted_input.txt", "Sarah said churn risk is high.")
    check("paste builds a doc dict", d["name"] == "pasted_input.txt" and d["raw"])

    print("\nALL CHECKS PASSED")


def test_pipeline():
    """pytest entry point: the checks above, in one collected test."""
    main()


if __name__ == "__main__":
    main()
