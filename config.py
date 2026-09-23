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
MAX_ANALYSIS_TOKENS = 4000  # main analysis output (the full brief needs ~2-3k)
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


# ── Prices ──
# List prices per million tokens, read from https://www.anthropic.com/pricing
# on PRICES_DATED. Re-check them against that page before quoting any dollar
# figure computed here; they change without notice. Batch API requests are
# billed at BATCH_MULTIPLIER of list.
PRICES_DATED = "2026-09-23"
PRICES = {
    "claude-sonnet-4-6": {"input": 3.00, "output": 15.00},
    "claude-haiku-4-5": {"input": 1.00, "output": 5.00},
}
BATCH_MULTIPLIER = 0.5


def cost_usd(model: str, input_tokens, output_tokens, batch: bool = False):
    """Dollars for one call at list price, or None when a token count is
    missing (results files written before tokens were recorded). Unknown
    models raise, because a silent zero would be quoted as a real number."""
    if model not in PRICES:
        raise KeyError(f"no price on file for {model!r}; add it to config.PRICES")
    if input_tokens is None or output_tokens is None:
        return None
    p = PRICES[model]
    usd = (input_tokens * p["input"] + output_tokens * p["output"]) / 1_000_000
    return usd * (BATCH_MULTIPLIER if batch else 1.0)
