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
signal_cli.py     # CLI entry — argparse, orchestration, rich output, --dry-run, --contract
ingest.py         # file reading, type detection, smart truncation, PNG/PDF -> content blocks
summarize.py      # Call 1: per-doc summarization
analyze.py        # Call 2: synthesis -> structured JSON brief, prompt or native contract
schema.py         # the brief as a JSON Schema, built from the prompt's constants
dryrun.py         # token estimates shared by the CLI and the eval runner
chat.py           # interactive follow-up loop
prompts.py        # all prompt templates + the contract constants
config.py         # model, token limits, client setup
tests/            # mock_docs/ + offline pipeline test (no API key needed)
evals/            # golden set, runner, results (see Evals below)
```

## Tests

```bash
python tests/test_pipeline.py     # offline, uses a stub client: pipeline, both contracts, parse paths
python evals/test_run.py          # offline: scoring functions and one stubbed golden case
```

## Evals

The stub-client test checks plumbing. This measures output quality.

**Golden set.** `evals/golden/` holds thirteen synthetic accounts, each with
its documents in the formats the app accepts (three include a PNG chart or a
PDF deck) and a hand-written `expected.json`: the risk types from the
taxonomy, the economic buyer's name, the source labels the brief must cite,
and whether data gaps are expected. The labels were written before any
pipeline run on these files, so they are not anchored on the model's output.
The set was built to include the cases that separate a good read from a
plausible one: the most-mentioned contact is not the buyer, chat is positive
while the CRM notes are not, no real risk at all, and a transcript long
enough to truncate with the signal at the end.

**Runner.** `evals/run.py` reuses the CLI's ingest, summarize, and analyze
functions, so a score is a score for the real pipeline.

```bash
python evals/run.py --dry-run                      # token estimate per case, no API calls
python evals/run.py                                # full mode, prompt contract, weighted prompt
python evals/run.py --contract native              # same set, native structured outputs
python evals/run.py --arm unweighted --runs 20     # one arm of the ablation
python evals/run.py --mode revenue                 # any focus mode
```

Per case it scores risk-type recall (the primary metric) and precision,
economic-buyer accuracy (the labeled name inside the brief's primary
contact, whitespace and case normalized), attribution coverage (every
required source label appears somewhere in `section_sources`), data gaps
present when expected, the parse path (`native`, `recovered_by_parser`, or
`failed`), and tokens and latency for the analysis call. Results go to
`evals/results/<date>-<mode>-<contract>-<arm>.md` with the raw briefs beside
them as JSON. A failed parse, or an empty brief on a case with expected
risks, is a hard fail and exits 1.

**Two contracts.** `--contract prompt` is the original: the JSON shape is
described in the prompt and a tolerant parser strips fences and prose.
`--contract native` sends the same shape as a JSON Schema through the API's
structured outputs (`output_config.format`, no beta header), with the schema
built from the same constants as the prompt so they cannot drift. The parser
stays as the fallback under both contracts because a constrained response
still has ways to disappoint: the model can hit `max_tokens` mid-object, a
proxy between the app and the API can drop the parameter, and an older
model in the allowlist may not honour it. Recording which path handled each
reply is how the two contracts are compared, and how a silent regression
would show up.

**Ablation.** `--arm unweighted` removes the source-weighting block from the
analysis prompt (no ranking of decks and CRM notes over chat, no
economic-buyer-over-most-mentioned rule) and changes nothing else. Twenty
runs per arm on the same set. The case built to separate the arms is
`most-mentioned-not-buyer`; if it does not, that is the finding.

**Results.** Not yet run. The runs below need an `ANTHROPIC_API_KEY`; from
the dry-run figures, one full pass is roughly 15k Haiku input tokens for the
summaries plus at most 30k Sonnet input tokens and around 20k output tokens
for the analyses, on the order of half a dollar. The two contract passes and
the forty ablation passes together are in the low tens of dollars.

| Run | Risk recall | Risk precision | Buyer accuracy | Attribution | Parse native / recovered / failed |
| --- | --- | --- | --- | --- | --- |
| prompt contract, weighted | pending | pending | pending | pending | pending |
| native contract, weighted | pending | pending | pending | pending | pending |
| ablation arm A, weighted, 20 runs | pending | pending | pending | pending | pending |
| ablation arm B, unweighted, 20 runs | pending | pending | pending | pending | pending |

Fill the table from the four results files:

```bash
python evals/run.py --contract prompt
python evals/run.py --contract native
python evals/run.py --contract native --arm weighted --runs 20
python evals/run.py --contract native --arm unweighted --runs 20
```
