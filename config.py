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

# ── Model ──
# Brief specified claude-sonnet-4-20250514, which is deprecated (retires
# 2026-06-15). claude-sonnet-4-6 is its drop-in replacement.
MODEL = "claude-sonnet-4-6"


def get_client():
    """Return an Anthropic client.

    `anthropic` is imported lazily so `--dry-run` works even without the
    package installed or an API key set.
    """
    import anthropic
    return anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
