"""Document ingestion: read files, detect type, smart-truncate.

Ported from the JS `detectType()` logic, with front/back truncation added.
"""
from __future__ import annotations

from pathlib import Path

from config import MAX_DOC_TOKENS, CHARS_PER_TOKEN

# Filename keyword patterns -> human label. Priority order: first match wins,
# so put more specific multi-keyword patterns before broad single-keyword ones.
FILENAME_PATTERNS = [
    (("kick", "off"), "Kick-off deck"),
    (("kickoff",), "Kick-off deck"),
    (("abr",), "ABR notes"),
    (("mbr",), "MBR notes"),
    (("qbr",), "QBR notes"),
    (("ebr",), "EBR notes"),
    (("swot",), "SWOT"),
    (("zoom",), "Zoom transcript"),
    (("transcript",), "Call transcript"),
    (("teams", "chat"), "Teams chat"),
    (("teams",), "Teams chat"),
    (("slack",), "Slack thread"),
    (("email",), "Email thread"),
    (("notes",), "Internal notes"),
]

EXTENSION_LABELS = {
    ".csv": "CSV data",
    ".tsv": "CSV data",
    ".json": "JSON data",
    ".vtt": "Call transcript",
}

# Extensions we'll attempt to read as text. Files with any other non-empty
# extension are skipped as probably-binary.
TEXT_EXTENSIONS = {
    ".txt", ".md", ".markdown", ".csv", ".tsv", ".json",
    ".log", ".vtt", ".rtf", ".text",
}


def estimate_tokens(text: str) -> int:
    """Rough token estimate (1 token ~ 4 chars)."""
    return max(1, len(text) // CHARS_PER_TOKEN)


def smart_truncate(content: str, max_tokens: int = MAX_DOC_TOKENS) -> str:
    """Keep the first 45% and last 35% of content, drop the middle filler.

    Preserves intro/agenda/stated concerns and action items/next steps, which
    is where the signal lives in transcripts and notes.
    """
    max_chars = max_tokens * CHARS_PER_TOKEN
    if len(content) <= max_chars:
        return content
    front = int(max_chars * 0.45)
    back = int(max_chars * 0.35)
    return content[:front] + "\n\n[... middle truncated ...]\n\n" + content[-back:]


def detect_type(filename: str, content: str) -> str:
    """Return a human label for a document. filename keywords -> extension ->
    content sniffing."""
    name = filename.lower()

    # 1. filename keyword patterns
    for keywords, label in FILENAME_PATTERNS:
        if all(k in name for k in keywords):
            return label

    # 2. file extension
    ext = Path(filename).suffix.lower()
    if ext in EXTENSION_LABELS:
        return EXTENSION_LABELS[ext]

    # 3. content sniffing
    head = content[:800]
    lower = head.lower()
    if "00:" in head or " --> " in head:           # timestamps / vtt cues
        return "Call transcript"
    if head.count(",") > 12 and "\n" in head:        # comma-dense rows
        return "CSV data"
    if any(s in lower for s in ("subject:", "from:", "to:")):
        return "Email thread"
    return "Document"


def read_docs(docs_dir: str) -> list[dict]:
    """Read every text-like file in a directory into doc dicts.

    Each dict: {name, type, raw, content} where `content` is smart-truncated.
    """
    path = Path(docs_dir)
    if not path.exists():
        raise FileNotFoundError(f"--docs path does not exist: {docs_dir}")
    if not path.is_dir():
        raise NotADirectoryError(f"--docs path is not a directory: {docs_dir}")

    docs: list[dict] = []
    for fp in sorted(path.iterdir()):
        if not fp.is_file():
            continue
        ext = fp.suffix.lower()
        if ext and ext not in TEXT_EXTENSIONS:
            continue  # skip likely-binary files (.pdf, .docx, .png, ...)
        try:
            content = fp.read_text(encoding="utf-8", errors="replace").strip()
        except Exception:
            continue
        if not content:
            continue
        docs.append({
            "name": fp.name,
            "type": detect_type(fp.name, content),
            "raw": content,
            "content": smart_truncate(content),
        })
    return docs


def make_doc(name: str, content: str) -> dict:
    """Build a single doc dict (used for --paste / stdin input)."""
    content = content.strip()
    return {
        "name": name,
        "type": detect_type(name, content),
        "raw": content,
        "content": smart_truncate(content),
    }
