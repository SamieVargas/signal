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

from config import MODELS
from ingest import read_docs, make_doc, smart_truncate, detect_type
from summarize import summarize_all
from analyze import build_analysis_prompt, analyze, extract_json
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


def _msg(text):
    return SimpleNamespace(content=[_block(text)])


class FakeMessages:
    def __init__(self):
        self.calls = []

    def create(self, model, max_tokens, messages, system=None):
        self.calls.append({"model": model, "max_tokens": max_tokens,
                           "system": system, "messages": messages})
        user_text = messages[-1]["content"]
        if user_text.lstrip().startswith("You are Signal, an expert CS strategist. Analyze"):
            return _msg("```json\n" + json.dumps(SAMPLE_BRIEF) + "\n```")  # Call 2 (fenced on purpose)
        if system is not None:
            return _msg("Here's my read on that.")                          # chat
        return _msg("Tight 3-sentence summary of the doc.")                 # Call 1


class FakeClient:
    def __init__(self):
        self.messages = FakeMessages()


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

    print("chat loop (injected io)")
    replies = []
    scripted = iter(["what changed?", "quit"])
    chat_loop(client, brief, summaries,
              ask=lambda _p: next(scripted), say=replies.append)
    check("chat produced a reply", replies == ["Here's my read on that."])
    check("chat sent system prompt", client.messages.calls[-1]["system"] is not None)
    check("chat routed to chat model", client.messages.calls[-1]["model"] == MODELS["chat"])

    print("paste-mode doc")
    d = make_doc("pasted_input.txt", "Sarah said churn risk is high.")
    check("paste builds a doc dict", d["name"] == "pasted_input.txt" and d["raw"])

    print("\nALL CHECKS PASSED")


if __name__ == "__main__":
    main()
