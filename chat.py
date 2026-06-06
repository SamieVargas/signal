"""Interactive follow-up loop after analysis."""
from __future__ import annotations

import json

from config import MODELS, MAX_CHAT_TOKENS
from prompts import CHAT_SYSTEM_PROMPT
from analyze import format_summaries

QUIT_WORDS = {"quit", "exit", "q"}


def build_system(brief: dict, summaries: list[dict]) -> str:
    return CHAT_SYSTEM_PROMPT.format(
        brief_json=json.dumps(brief, indent=2),
        summaries=format_summaries(summaries),
    )


def chat_loop(client, brief: dict, summaries: list[dict], ask=input, say=print):
    """Run the interactive Q&A loop. `ask`/`say` are injectable for testing."""
    system = build_system(brief, summaries)
    history: list[dict] = []
    while True:
        try:
            msg = ask("\nAsk Signal anything about this account (or 'quit'):\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            say("")
            break
        if not msg:
            continue
        if msg.lower() in QUIT_WORDS:
            break

        history.append({"role": "user", "content": msg})
        resp = client.messages.create(
            model=MODELS["chat"],
            max_tokens=MAX_CHAT_TOKENS,
            system=system,
            messages=history[-10:],  # keep the last few turns
        )
        reply = "".join(b.text for b in resp.content if b.type == "text").strip()
        history.append({"role": "assistant", "content": reply})
        say(reply)
