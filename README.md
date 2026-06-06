# Signal v0.3

**Paste the mess --> get the read.**  
AI-powered account intelligence for CS teams.

---

## Architecture

```
Browser (index.html on GitHub Pages)
    ↓ POST request (account data + prompt)
Cloudflare Worker (worker.js)
    ↓ forwards with API key in header
Anthropic API
    ↓ returns analysis JSON
Cloudflare Worker
    ↓ strips headers, adds CORS
Browser renders brief + chat
```

The API key never touches the browser. 

---

## New in v0.3

- Source weighting (all-hands/CRM as primary, chat as secondary) + a contact read that targets the economic buyer, not chat-log noise
- Per-section source attribution and a Data Gaps callout
- Per-document removal, plus an analysis focus toggle (Full / Revenue Risk / Relationship / Pre-Call) that trims tokens on focused modes
- Collapsible + copy-to-clipboard brief sections, skeleton loader, Export to PDF, Cmd/Ctrl+Enter to re-analyze, mobile layout, and assorted polish

## What's in v0.0.1

- Portfolio view — 4 demo accounts + add your own
- File upload — PDF, DOCX, XLSX/XLS, plus .txt, .csv, .vtt, .srt, .md, .json, .html, .log, .tsv (parsed in-browser; scanned/image-only PDFs are flagged with a clear message since they have no text layer to read)
- Paste input — raw text, Teams chat, MBR notes, etc.
- Auto content-type detection (transcript, MBR/QBR, CSV, chat log, email, SWOT)
- AI synthesis — situation read, contact persona, ranked leverage points, "do this today"
- Chat interface — interrogate Signal about this specific account
- Privacy — nothing stored, session only, cleared on close

---

## What's next (v0.1+)

- [ ] Longitudinal memory — compare this call to the last one
- [ ] Feedback loop — "here's what happened after you suggested that"
- [ ] Multi-contact persona — different reads for champion vs economic buyer
- [ ] Revenue trend visualization from CSV input
- [ ] Export brief as PDF / shareable link

---

# Signal — Python CLI

> "I spent eight years doing this hour of account digging manually every month
> across a $14M enterprise book. This is the Python version of what I wished existed."

A command-line rebuild of the analysis engine using the Anthropic Python SDK
directly — no browser, no Worker proxy. Built to keep token usage under control
on real, messy account data.

## Highlights

- **Two-call LLM architecture** with explicit token management: summarize each
  doc individually (cheap), then analyze the small summaries — not the raw docs.
  On large inputs this cuts the main analysis call by **~96%** (measured via
  `--dry-run`: 22,976 → ≤1,012 input tokens for two long transcripts).
- **Smart document truncation** — front/back extraction (45% front, 35% back),
  preserving intros/stated concerns + action items and dropping middle filler.
- **Content-type auto-detection** across 15+ formats (transcripts, MBR/QBR/EBR,
  Teams/Slack, CSV, email, SWOT), ported from the JS `detectType()` logic.
- **Structured JSON output** with the 11-type risk taxonomy and 5-field contact
  persona carried over from the web app; tolerant JSON parsing.
- **`rich` terminal output**, JSON saved to `./output/`, interactive chat loop.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...      # or put it in a .env file
```

## Usage

```bash
# Analyze a directory of account docs
python signal_cli.py --account "Koala" --contact "Sarah Chen, VP of Product" \
  --arr 180000 --renewal 67 --docs ./tests/mock_docs/

# Paste a single doc from stdin
python signal_cli.py --account "Koala" --paste

# Inspect token counts before spending credits — no API calls
python signal_cli.py --account "Koala" --docs ./tests/mock_docs/ --dry-run

# Skip the interactive chat loop
python signal_cli.py --account "Koala" --docs ./tests/mock_docs/ --no-chat
```

> The entry point is `signal_cli.py`, **not** `signal.py`: a module named
> `signal.py` on the path shadows the standard-library `signal` module that
> `anthropic`/`anyio` import at startup, which would crash the pipeline.

## Project layout

```
signal_cli.py     # CLI entry — argparse, orchestration, rich output, --dry-run
ingest.py         # file reading, type detection, smart truncation
summarize.py      # Call 1: per-doc summarization
analyze.py        # Call 2: synthesis -> structured JSON brief
chat.py           # interactive follow-up loop
prompts.py        # all prompt templates
config.py         # model, token limits, client setup
tests/            # mock_docs/ + offline pipeline test (no API key needed)
```

## Tests

```bash
python tests/test_pipeline.py     # offline, uses a stub client
```
