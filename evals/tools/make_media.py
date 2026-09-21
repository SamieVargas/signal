"""Regenerate the binary sources in the golden set (a usage chart PNG and a
kick-off deck PDF). Pure Python plus Pillow, no network, deterministic.

    python evals/tools/make_media.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

GOLDEN = Path(__file__).resolve().parents[1] / "golden"


def usage_chart(path: Path, title: str, weeks: list[int], label: str) -> None:
    """A weekly-active-users bar chart, the kind an admin screenshots."""
    w, h, pad = 720, 360, 48
    img = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((pad, 14), title, fill="black", font=font)
    d.text((pad, 30), label, fill=(110, 110, 110), font=font)
    top, bottom = 60, h - pad
    d.line([(pad, bottom), (w - pad, bottom)], fill="black")
    d.line([(pad, top), (pad, bottom)], fill="black")
    mx = max(weeks) or 1
    bw = (w - 2 * pad) / len(weeks)
    for i, v in enumerate(weeks):
        x0 = pad + i * bw + 4
        y0 = bottom - (bottom - top) * v / mx
        d.rectangle([x0, y0, x0 + bw - 8, bottom], fill=(26, 107, 90))
        d.text((x0, bottom + 6), f"W{i + 1}", fill="black", font=font)
        d.text((x0, y0 - 14), str(v), fill="black", font=font)
    img.save(path)


def _pdf_escape(s: str) -> str:
    """Standard-14 fonts are Latin-1; fold the few typographic characters."""
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\u2019", "'").replace("\u00d7", "x")
    s = s.encode("latin-1", "replace").decode("latin-1")
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def text_pdf(path: Path, pages: list[list[str]]) -> None:
    """A minimal multi-page PDF of Helvetica text lines. Standard-14 font,
    nothing embedded, so pdftotext and the API both read it."""
    objs: list[bytes] = []

    def add(obj: str | bytes) -> int:
        objs.append(obj.encode("latin-1") if isinstance(obj, str) else obj)
        return len(objs)

    font_id = add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    page_ids = []
    pages_id_placeholder = None
    content_ids = []
    for lines in pages:
        y = 760
        ops = ["BT", "/F1 12 Tf", "14 TL", f"56 {y} Td"]
        for ln in lines:
            ops.append(f"({_pdf_escape(ln)}) Tj T*")
        ops.append("ET")
        stream = "\n".join(ops)
        content_ids.append(add(f"<< /Length {len(stream)} >>\nstream\n{stream}\nendstream"))
    pages_id = len(objs) + len(pages) + 1
    for cid in content_ids:
        page_ids.append(add(
            f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 612 792] "
            f"/Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {cid} 0 R >>"
        ))
    kids = " ".join(f"{p} 0 R" for p in page_ids)
    assert add(f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>") == pages_id
    catalog_id = add(f"<< /Type /Catalog /Pages {pages_id} 0 R >>")

    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for i, body in enumerate(objs, 1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode()
    for off in offsets:
        out += f"{off:010d} 00000 n \n".encode()
    out += f"trailer\n<< /Size {len(objs) + 1} /Root {catalog_id} 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    path.write_bytes(bytes(out))


def main() -> None:
    usage_chart(
        GOLDEN / "silent-decay" / "weekly_active_users.png",
        "Northwind Analytics — Weekly active users, last 12 weeks",
        [41, 40, 39, 37, 33, 31, 28, 24, 22, 19, 17, 15],
        "Source: admin console export, 2026-08-30",
    )
    usage_chart(
        GOLDEN / "power-user-concentration" / "logins_by_user.png",
        "Halvorsen Logistics — Logins by user, August 2026",
        [212, 9, 7, 5, 4, 3, 2, 1],
        "Bars are individual users, left to right: D. Okafor, then everyone else",
    )
    text_pdf(GOLDEN / "adoption-failure" / "kickoff_deck.pdf", [
        [
            "Brightwater Health x Signal Platform",
            "Kick-off deck — 14 January 2026",
            "",
            "Goals for year one",
            "  - 120 licensed seats live across Clinical Ops and Revenue Cycle by end of Q2",
            "  - Replace the weekly manual reconciliation spreadsheet",
            "  - Executive dashboard reviewed at every monthly ops meeting",
            "",
            "Executive sponsor: Dr. Elena Vasquez, Chief Operating Officer",
            "Project lead: Tom Reyes, Director of Clinical Operations",
            "Day-to-day admin: Jenna Park, Systems Analyst",
        ],
        [
            "Rollout plan",
            "  Phase 1 (Feb): Clinical Ops pilot, 25 seats",
            "  Phase 2 (Apr): Revenue Cycle, 60 seats",
            "  Phase 3 (Jun): remaining teams, 35 seats",
            "",
            "Success criteria agreed with Dr. Vasquez",
            "  - 80% weekly active rate on licensed seats",
            "  - Reconciliation spreadsheet retired by 1 May",
            "",
            "Renewal: 15 January 2027 · ARR $96,000",
        ],
    ])
    text_pdf(GOLDEN / "stalled-expansion" / "annual_review.pdf", [
        [
            "Corvid Media — Annual Review, 22 July 2026",
            "",
            "Where we are",
            "  - 40 seats, 92% weekly active, NPS 61 from the last survey",
            "  - Editorial team calls the dashboard 'the morning read'",
            "",
            "Expansion proposal (presented by CSM)",
            "  - Add Audience Insights module, +$38,000 ARR",
            "  - Extend to the sales team, +25 seats",
            "",
            "Decision from Marcus Whitfield, VP Product:",
            "  'Not this quarter. Finance has frozen new spend until the",
            "   reorg settles. Come back in October.'",
            "",
            "Renewal: 1 December 2026 · ARR $84,000",
        ],
    ])
    print("wrote media into", GOLDEN)


if __name__ == "__main__":
    main()
