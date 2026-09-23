#!/usr/bin/env python3
"""Render a trace written by `--trace <file.json>` as an SVG waterfall.

    python evals/tools/render_trace.py trace.json docs/trace.svg
    python evals/tools/render_trace.py trace.json docs/trace.svg --caption "text under the chart"

One row per span, indented by depth, bars on a shared time axis, each
label carrying the span's duration and its token attributes. Plain SVG
with inline styles and a system font stack, no external assets, laid out
for 900px wide.
"""
from __future__ import annotations

import argparse
import sys
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))

from tracing import read_trace  # noqa: E402

WIDTH = 900
LEFT = 300          # label column
RIGHT_PAD = 16
ROW = 24
HEADER = 34
FOOTER = 20
INDENT = 14
COLORS = {
    "signal.brief": "#4b5563",
    "signal.ingest": "#2563eb",
    "signal.summarize": "#d97706",
    "signal.analyze": "#dc2626",
    "signal.parse": "#16a34a",
    "signal.batch": "#7c3aed",
}
DEFAULT_COLOR = "#6b7280"


def order_spans(spans: list[dict]) -> list[tuple[dict, int]]:
    """Depth-first by start time: every span after its parent, siblings in
    time order. Spans whose parent is missing from the file are roots."""
    ids = {s["span_id"] for s in spans}
    children: dict = {}
    for s in spans:
        parent = s.get("parent") if s.get("parent") in ids else None
        children.setdefault(parent, []).append(s)
    for v in children.values():
        v.sort(key=lambda s: s["start"])
    out = []

    def walk(parent, depth):
        for s in children.get(parent, []):
            out.append((s, depth))
            walk(s["span_id"], depth + 1)

    walk(None, 0)
    return out


def fmt_ms(ms: float) -> str:
    if ms >= 1000:
        return f"{ms / 1000:.2f} s"
    if ms >= 10:
        return f"{ms:.0f} ms"
    return f"{ms:.2f} ms"


def short_label(s: dict) -> str:
    a = s.get("attributes") or {}
    name = s["name"].replace("signal.", "")
    extra = a.get("name") or a.get("label") or a.get("case") or a.get("account")
    return f"{name} {extra}" if extra else name


def detail(s: dict) -> str:
    a = s.get("attributes") or {}
    bits = [fmt_ms(s.get("duration_ms") or 0.0)]
    if "input_tokens" in a or "output_tokens" in a:
        bits.append(f"{a.get('input_tokens', '?')} in / {a.get('output_tokens', '?')} out")
    for key in ("chars", "parse_path", "stop_reason", "contract", "arm", "kind"):
        if key in a and key != "kind":
            bits.append(f"{key}={a[key]}")
        elif key == "kind" and a.get("kind") not in (None, "text"):
            bits.append(str(a["kind"]))
    return " · ".join(bits)


def render_svg(spans: list[dict], caption: str | None = None) -> str:
    rows = order_spans(spans)
    if not rows:
        raise SystemExit("no spans to render")
    t0 = min(s["start"] for s, _ in rows)
    t1 = max(s["end"] for s, _ in rows)
    total_ns = max(t1 - t0, 1)
    plot_w = WIDTH - LEFT - RIGHT_PAD
    caption_lines = textwrap.wrap(caption, 150) if caption else []
    height = HEADER + ROW * len(rows) + FOOTER + 16 * len(caption_lines)

    def x(ns: int) -> float:
        return LEFT + (ns - t0) / total_ns * plot_w

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}" '
        f'font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="12">',
        f'<rect width="{WIDTH}" height="{height}" fill="#ffffff"/>',
        f'<text x="8" y="16" font-weight="600">Signal trace · {len(rows)} spans · {fmt_ms(total_ns / 1e6)} wall clock</text>',
    ]
    # Time axis with five ticks.
    for i in range(6):
        ns = t0 + total_ns * i // 5
        xi = x(ns)
        out.append(f'<line x1="{xi:.1f}" y1="{HEADER - 6}" x2="{xi:.1f}" y2="{HEADER + ROW * len(rows)}" stroke="#e5e7eb" stroke-width="1"/>')
        anchor = "end" if i == 5 else ("start" if i == 0 else "middle")
        out.append(f'<text x="{xi:.1f}" y="{HEADER - 10}" text-anchor="{anchor}" fill="#6b7280" font-size="10">{fmt_ms((ns - t0) / 1e6)}</text>')
    for i, (s, depth) in enumerate(rows):
        y = HEADER + ROW * i
        if i % 2:
            out.append(f'<rect x="0" y="{y}" width="{WIDTH}" height="{ROW}" fill="#f9fafb"/>')
        color = COLORS.get(s["name"], DEFAULT_COLOR)
        x0 = x(s["start"])
        w = max(x(s["end"]) - x0, 1.5)
        out.append(f'<rect x="{x0:.1f}" y="{y + 5}" width="{w:.1f}" height="{ROW - 10}" rx="2" fill="{color}" fill-opacity="0.85"/>')
        out.append(f'<text x="{8 + depth * INDENT}" y="{y + 16}" fill="#111827">{escape(short_label(s))}</text>')
        # Detail text sits inside a wide bar, right of a narrow one when
        # there is room, otherwise just left of it, never in the label column.
        fill = "#374151"
        if w > 200:
            tx, anchor, fill = x0 + 6, "start", "#ffffff"
        elif x0 + w + 6 < WIDTH - 180:
            tx, anchor = x0 + w + 6, "start"
        else:
            tx, anchor = x0 - 6, "end"
        out.append(f'<text x="{tx:.1f}" y="{y + 16}" text-anchor="{anchor}" fill="{fill}" font-size="11">{escape(detail(s))}</text>')
    for i, line in enumerate(caption_lines):
        out.append(f'<text x="8" y="{HEADER + ROW * len(rows) + FOOTER + 16 * i}" fill="#6b7280" font-size="11">{escape(line)}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="evals/tools/render_trace.py", description="Render a --trace file as an SVG waterfall")
    p.add_argument("trace", help="JSON file written by --trace (one span per line, or a list)")
    p.add_argument("svg", help="output .svg path")
    p.add_argument("--caption", default=None, help="one line under the chart")
    args = p.parse_args(argv)
    spans = read_trace(args.trace)
    svg = render_svg(spans, caption=args.caption)
    out = Path(args.svg)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({len(spans)} spans)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
