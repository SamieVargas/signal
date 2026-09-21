"""The analysis brief as a JSON Schema, built from the same constants the
prompt uses, so the native structured-output contract and the prompt-only
contract cannot drift apart."""
from __future__ import annotations

from prompts import CONFIDENCES, PERSONA_FIELDS, RISK_TYPES, SECTIONS, SEVERITIES


def _str() -> dict:
    return {"type": "string"}


def _str_list() -> dict:
    return {"type": "array", "items": {"type": "string"}}


def _obj(props: dict) -> dict:
    return {
        "type": "object",
        "properties": props,
        "required": list(props),
        "additionalProperties": False,
    }


def analysis_schema() -> dict:
    """JSON Schema for the brief. Every field is required so a native response
    always has the same shape; empty strings and arrays are how a focus mode
    leaves a section blank."""
    leverage_point = _obj({
        "rank": {"type": "integer"},
        "what": _str(),
        "why": _str(),
        "timeline": _str(),
    })
    secondary_contact = _obj({"name_title": _str(), "note": _str()})
    return _obj({
        "situation": _str(),
        "risk_type": {"type": "string", "enum": RISK_TYPES},
        "risk_severity": {"type": "string", "enum": SEVERITIES},
        "data_sources_detected": _str_list(),
        "leverage_points": {"type": "array", "items": leverage_point},
        "do_this_today": _str(),
        "contact_persona": _obj({f: _str() for f in PERSONA_FIELDS}),
        "secondary_contacts": {"type": "array", "items": secondary_contact},
        "section_sources": _obj({s: _str_list() for s in SECTIONS}),
        "data_gaps": _str_list(),
        "confidence": {"type": "string", "enum": CONFIDENCES},
        "confidence_note": _str(),
        "suggested_questions": _str_list(),
    })


def output_config() -> dict:
    """The `output_config` value for a native structured-output request."""
    return {"format": {"type": "json_schema", "schema": analysis_schema()}}
