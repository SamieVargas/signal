"""Configuration: model, token limits, and Anthropic client setup."""
import os

try:
    from dotenv import load_dotenv
    load_dotenv()  # read a local .env if present (ANTHROPIC_API_KEY=...)
except Exception:
    pass

# ── Token limits ──
MAX_DOC_TOKENS = 1500       # per doc, before summarization
MAX_SUMMARY_TOKENS = 300    # per-doc summary output
MAX_ANALYSIS_TOKENS = 1500  # main analysis output
MAX_CHAT_TOKENS = 600       # per chat response

# Rough estimate used for truncation + dry-run token accounting (1 tok ~ 4 chars)
CHARS_PER_TOKEN = 4

# ── Models ──
# One place to swap models per role. Brief specified claude-sonnet-4-20250514
# (deprecated, retires 2026-06-15); claude-sonnet-4-6 is its replacement.
# Haiku handles extraction/summarization and chat — ~25x cheaper than Sonnet,
# and plenty for that work. Sonnet stays on the main synthesis where reasoning
# quality matters. All must be in the Worker's allowlist if proxied.
MODELS = {
    "analysis": "claude-sonnet-4-6",  # main synthesis — keep the strong model
    "summary": "claude-haiku-4-5",    # per-doc extraction — cheap + fast
    "chat": "claude-haiku-4-5",       # follow-up Q&A — cheap + fast
}

# Backward-compatible alias for anything still referencing a single model.
MODEL = MODELS["analysis"]


def get_client():
    """Return an Anthropic client.

    `anthropic` is imported lazily so `--dry-run` works even without the
    package installed or an API key set.
    """
    import anthropic
    return anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
