#!/usr/bin/env python3
"""Signal — account intelligence CLI.

Pipeline: ingest docs -> summarize each (Call 1) -> analyze summaries (Call 2)
-> print brief -> save JSON -> interactive chat.

NOTE: this entry point is named signal_cli.py, not signal.py, on purpose.
A module named signal.py on sys.path shadows the standard-library `signal`
module, which `anthropic` -> `anyio` import at startup — so an entry named
signal.py crashes the real pipeline with `ImportError: cannot import name
'Signals'`.

Usage:
    python signal_cli.py --account "Koala" --docs ./koala_docs/
    python signal_cli.py --account "Koala" --contact "Sarah Chen, VP" --arr 180000 --renewal 67 --docs ./koala_docs/
    python signal_cli.py --account "Koala" --paste
    python signal_cli.py --account "Koala" --docs ./koala_docs/ --dry-run
"""
import argparse
import json
import sys
from datetime import date
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

import config
from ingest import read_docs, make_doc, estimate_tokens
from prompts import SUMMARIZE_PROMPT
from summarize import summarize_all
from analyze import build_analysis_prompt, analyze
from chat import chat_loop

console = Console()


def gather_docs(args) -> list[dict]:
    if args.paste:
        console.print("[dim]Paste account text, then Ctrl-D (Ctrl-Z on Windows):[/]")
        content = sys.stdin.read()
        if not content.strip():
            console.print("[red]No input received on stdin.[/]")
            sys.exit(1)
        return [make_doc("pasted_input.txt", content)]
    try:
        return read_docs(args.docs)
    except (FileNotFoundError, NotADirectoryError) as e:
        console.print(f"[red]{e}[/]")
        sys.exit(1)


def dry_run(docs, args) -> None:
    """Show what would be sent to the API — no calls made."""
    table = Table(title="Call 1 — summarize each document")
    table.add_column("Document", style="bold")
    table.add_column("Type")
    table.add_column("Raw tok", justify="right")
    table.add_column("Truncated tok", justify="right")
    table.add_column("Prompt tok", justify="right")

    call1_total = 0
    naive_total = 0
    for d in docs:
        prompt = SUMMARIZE_PROMPT.format(
            doc_type=d["type"], doc_name=d["name"], content=d["content"]
        )
        ptok = estimate_tokens(prompt)
        call1_total += ptok
        naive_total += estimate_tokens(d["raw"])
        table.add_row(
            d["name"], d["type"],
            str(estimate_tokens(d["raw"])),
            str(estimate_tokens(d["content"])),
            str(ptok),
        )
    console.print(table)

    # Ceiling for Call 2: summaries are bounded by MAX_SUMMARY_TOKENS each,
    # regardless of how large the raw docs are. That bound is the whole point.
    summary_cap = config.MAX_SUMMARY_TOKENS * len(docs)
    placeholder = "x" * (config.MAX_SUMMARY_TOKENS * config.CHARS_PER_TOKEN)
    call2_ceiling = estimate_tokens(build_analysis_prompt(
        args.account, args.contact, args.renewal, args.arr,
        [{"type": d["type"], "name": d["name"], "summary": placeholder} for d in docs],
    ))

    # Apples-to-apples "naive" baseline: the same analysis prompt, but with the
    # full raw docs inlined instead of summaries (what the JS version did).
    naive_prompt = estimate_tokens(build_analysis_prompt(
        args.account, args.contact, args.renewal, args.arr,
        [{"type": d["type"], "name": d["name"], "summary": d["raw"]} for d in docs],
    ))

    console.print(
        f"\n[bold]Call 1[/] (summarize) input ≈ [cyan]{call1_total}[/] tok "
        f"across {len(docs)} call(s)"
    )
    console.print(
        f"[bold]Call 2[/] (analyze) input ≤ [cyan]{call2_ceiling}[/] tok "
        f"— bounded by ≤{config.MAX_SUMMARY_TOKENS} tok/summary ({summary_cap} tok max total)"
    )
    console.print(
        f"\n[bold]Naive single-prompt analysis[/] would inline all raw docs ≈ "
        f"[yellow]{naive_prompt}[/] tok into the analysis call."
    )

    if naive_prompt > call2_ceiling:
        pct = (naive_prompt - call2_ceiling) / naive_prompt * 100
        console.print(
            f"[green]→ Two-call caps the analysis call ~{pct:.0f}% smaller[/] "
            f"({naive_prompt} → ≤{call2_ceiling} tok), and the gap grows with doc size."
        )
    else:
        console.print(
            "[dim]→ These docs are already under the truncation cap, so summarizing "
            "adds overhead here. The win kicks in once raw docs exceed "
            f"~{config.MAX_DOC_TOKENS} tok each (e.g. long transcripts), where Call 2 "
            "stays flat while the naive prompt keeps growing.[/]"
        )
    console.print("\n[dim]No API calls were made (--dry-run).[/]")


def render_brief(brief: dict, account: str, renewal_days) -> None:
    sources = " · ".join(brief.get("data_sources_used") or [])
    header = f"[bold]SIGNAL[/]  ·  {account}"
    if renewal_days is not None:
        header += f"  ·  {renewal_days} days to renewal"
    if sources:
        header += f"\nSources: {sources}"
    console.print(Panel(header, expand=False))

    console.print("\n[bold]SITUATION[/]")
    console.print(brief.get("situation", "—"))

    console.print(
        f"\n[bold]RISK TYPE[/]  {brief.get('risk_type', '—')}     "
        f"[bold]SEVERITY[/]  {brief.get('risk_severity', '—')}     "
        f"[bold]CONFIDENCE[/]  {brief.get('confidence', '—')}"
    )
    if brief.get("confidence_note"):
        console.print(f"[dim]{brief['confidence_note']}[/]")

    p = brief.get("contact_persona") or {}
    persona = Table(
        title=f"CONTACT READ — {p.get('primary_contact', 'Unknown')}",
        show_header=False, box=None, title_justify="left", pad_edge=False,
    )
    persona.add_column(style="bold cyan", no_wrap=True)
    persona.add_column()
    persona.add_row("Comm style", p.get("comm_style", "—"))
    persona.add_row("Decision style", p.get("decision_style", "—"))
    persona.add_row("Says vs means", p.get("what_they_say_vs_mean", "—"))
    persona.add_row("How to engage", p.get("approach_recommendation", "—"))
    console.print("")
    console.print(persona)

    console.print("\n[bold]WHERE TO PRESS[/]")
    for lp in brief.get("leverage_points") or []:
        console.print(
            f"  [bold]Priority {lp.get('rank', '?')}[/]  "
            f"[dim][{lp.get('timeline', '')}][/]  {lp.get('what', '')}"
        )
        console.print(f"      [dim]{lp.get('why', '')}[/]")

    console.print("\n[bold]DO THIS TODAY[/]")
    console.print(brief.get("do_this_today", "—"))

    qs = brief.get("suggested_questions") or []
    if qs:
        console.print("\n[bold]SUGGESTED QUESTIONS[/]")
        for q in qs:
            console.print(f"  • {q}")


def save_output(brief: dict, account: str) -> Path:
    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)
    safe = "".join(c if c.isalnum() else "_" for c in account).strip("_") or "account"
    fp = out_dir / f"signal_output_{safe}_{date.today().isoformat()}.json"
    fp.write_text(json.dumps(brief, indent=2), encoding="utf-8")
    return fp


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        prog="signal_cli.py", description="Signal — account intelligence CLI"
    )
    p.add_argument("--account", required=True, help="account name")
    p.add_argument("--contact", default="", help='e.g. "Sarah Chen, VP of Product"')
    p.add_argument("--arr", default="", help="annual recurring revenue")
    p.add_argument("--renewal", type=int, default=None, help="days to renewal")

    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--docs", help="directory of account documents")
    src.add_argument("--paste", action="store_true", help="read one document from stdin")

    p.add_argument("--dry-run", action="store_true",
                   help="show what would be sent to the API without calling it")
    p.add_argument("--no-chat", action="store_true",
                   help="skip the interactive chat loop")
    return p.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    docs = gather_docs(args)
    if not docs:
        console.print("[red]No readable documents found.[/]")
        sys.exit(1)

    if args.dry_run:
        dry_run(docs, args)
        return

    # Credentials are checked at request time by the SDK, not construction —
    # so fail early with a clear message instead of a traceback mid-pipeline.
    import os
    if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
        console.print("[red]No Anthropic credentials found.[/]")
        console.print("[dim]Set ANTHROPIC_API_KEY in your environment or a .env file, "
                      "then retry. Use --dry-run to test without a key.[/]")
        sys.exit(1)

    client = config.get_client()

    def progress(i, n, name):
        console.print(f"[dim]Summarizing ({i}/{n}): {name}[/]")

    try:
        summaries = summarize_all(client, docs, on_progress=progress)
        console.print("[dim]Analyzing summaries…[/]")
        prompt = build_analysis_prompt(
            args.account, args.contact, args.renewal, args.arr, summaries
        )
        brief = analyze(client, prompt)
    except Exception as e:
        console.print(f"\n[red]API call failed:[/] {type(e).__name__}: {e}")
        sys.exit(1)

    console.print("")
    render_brief(brief, args.account, args.renewal)
    fp = save_output(brief, args.account)
    console.print(f"\n[green]Saved[/] {fp}")

    if not args.no_chat:
        chat_loop(client, brief, summaries)


if __name__ == "__main__":
    main()
