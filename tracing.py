"""Optional OpenTelemetry spans around the pipeline.

One root span per brief (`signal.brief`), a child per document read
(`signal.ingest`), per summary call (`signal.summarize`), the analysis call
(`signal.analyze`) and its parsing (`signal.parse`). The pipeline modules
call `span()` unconditionally; what it does depends on what is installed:

- `opentelemetry-api` and `opentelemetry-sdk` absent (the default install):
  `span()` yields a no-op object and nothing else happens. Every test runs
  this way without the packages.
- present but nothing installed: the OpenTelemetry API's own non-recording
  spans, also a no-op.
- `install_json_exporter(path)` called (the CLI's and the runner's
  `--trace <file.json>`): a TracerProvider with a SimpleSpanProcessor that
  appends one JSON object per finished span to the file, which
  `evals/tools/render_trace.py` turns into an SVG waterfall.

Install the packages with `pip install -r requirements-trace.txt`.
"""
from __future__ import annotations

import contextlib
import json
from pathlib import Path

try:
    from opentelemetry import trace as _otel
    HAVE_OTEL = True
except ImportError:  # the shim path
    _otel = None
    HAVE_OTEL = False

SPAN_NAMES = ("signal.brief", "signal.ingest", "signal.summarize", "signal.analyze", "signal.parse", "signal.batch")

_provider = None      # the SDK TracerProvider once an exporter is installed
_exporters: list = []


class NoopSpan:
    """What `span()` yields when OpenTelemetry is not installed."""

    def set_attribute(self, key, value):
        return None

    def set_attributes(self, attributes):
        return None

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def clean(attributes: dict) -> dict:
    """OpenTelemetry attribute values must be str, bool, int or float; drop
    None (a token count the stub client never reports) and stringify the
    rest so a span never fails to record."""
    out = {}
    for k, v in attributes.items():
        if v is None:
            continue
        out[k] = v if isinstance(v, (str, bool, int, float)) else str(v)
    return out


class _Recording:
    """Thin wrapper so callers can pass None values without checking."""

    def __init__(self, span):
        self._span = span

    def set_attribute(self, key, value):
        if value is not None:
            self._span.set_attribute(key, value if isinstance(value, (str, bool, int, float)) else str(value))

    def set_attributes(self, attributes):
        self._span.set_attributes(clean(attributes))


@contextlib.contextmanager
def span(_name: str, **attributes):
    """Context manager for one span. Attributes may be None; those are
    dropped. The span name is positional so `name=` stays free for an
    attribute (the document's filename)."""
    if not HAVE_OTEL:
        yield NoopSpan()
        return
    tracer = _otel.get_tracer("signal")
    with tracer.start_as_current_span(_name, attributes=clean(attributes)) as s:
        yield _Recording(s)


def _hex(span_id: int | None, width: int) -> str | None:
    return None if span_id is None else format(span_id, f"0{width}x")


def span_record(s) -> dict:
    """The JSON shape one exported span is written as."""
    ctx = s.get_span_context()
    parent = s.parent.span_id if s.parent is not None else None
    return {
        "name": s.name,
        "trace_id": _hex(ctx.trace_id, 32),
        "span_id": _hex(ctx.span_id, 16),
        "parent": _hex(parent, 16),
        "start": s.start_time,          # ns since the epoch
        "end": s.end_time,
        "duration_ms": round((s.end_time - s.start_time) / 1e6, 3) if s.end_time and s.start_time else None,
        "attributes": dict(s.attributes or {}),
        "status": s.status.status_code.name.lower() if s.status is not None else None,
    }


def install_json_exporter(path):
    """Install (once) a TracerProvider whose SimpleSpanProcessor appends one
    JSON object per line to `path`. Requires opentelemetry-sdk; raises
    ImportError with the install line otherwise. Returns the provider."""
    global _provider
    try:
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor, SpanExporter, SpanExportResult
    except ImportError as e:
        raise ImportError("--trace needs the optional packages: pip install -r requirements-trace.txt") from e

    class JsonFileExporter(SpanExporter):
        def __init__(self, path):
            self.path = Path(path)
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self._fh = self.path.open("w", encoding="utf-8")

        def export(self, spans):
            for s in spans:
                self._fh.write(json.dumps(span_record(s), ensure_ascii=False) + "\n")
            self._fh.flush()
            return SpanExportResult.SUCCESS

        def shutdown(self):
            self._fh.close()

        def force_flush(self, timeout_millis: int = 30000) -> bool:
            self._fh.flush()
            return True

    if _provider is None:
        _provider = TracerProvider()
        _otel.set_tracer_provider(_provider)
    exporter = JsonFileExporter(path)
    _exporters.append(exporter)
    _provider.add_span_processor(SimpleSpanProcessor(exporter))
    return _provider


def read_trace(path) -> list[dict]:
    """Read a trace file written by the exporter: one JSON object per line,
    or a JSON list of the same objects."""
    text = Path(path).read_text(encoding="utf-8").strip()
    if not text:
        return []
    if text.startswith("["):
        return json.loads(text)
    return [json.loads(line) for line in text.splitlines() if line.strip()]
