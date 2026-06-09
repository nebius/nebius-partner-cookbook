"""Shared LangSmith annotation helpers."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from dataclasses import asdict, is_dataclass
from datetime import date, datetime
from typing import Any

EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\b(?:\+?\d[\d .()-]{7,}\d)\b")
SECRET_KEY_MARKERS = ("api_key", "authorization", "password", "secret")
MAX_STRING_LENGTH = 1_000
MAX_SEQUENCE_ITEMS = 12


def redact_text(value: str) -> str:
    """Remove common direct identifiers from trace previews."""
    value = EMAIL_RE.sub("[redacted-email]", value)
    return PHONE_RE.sub("[redacted-phone]", value)


def process_langsmith_inputs(inputs: dict[str, Any]) -> dict[str, Any]:
    """Sanitize traced function inputs before LangSmith receives them."""
    return _sanitize_mapping(inputs)


def process_langsmith_outputs(outputs: Any) -> Any:
    """Sanitize traced function outputs before LangSmith receives them."""
    return _sanitize(outputs)


def summarize_agent_events(events: Sequence[Any]) -> dict[str, Any]:
    """Reduce a streamed agent run to useful trace metadata."""
    token_count = 0
    status_phases: list[str] = []
    answer_preview: list[str] = []
    done_payload: Any = None
    for event in events:
        name = getattr(event, "name", None)
        data = getattr(event, "data", {})
        if name == "status" and isinstance(data, Mapping):
            phase = data.get("phase")
            if isinstance(phase, str):
                status_phases.append(phase)
        elif name == "token" and isinstance(data, Mapping):
            token_count += 1
            text = data.get("text")
            if isinstance(text, str) and not text.startswith("\n\n---\nTime:"):
                answer_preview.append(text)
        elif name == "done":
            done_payload = data
    return {
        "tokens_streamed": token_count,
        "status_phases": status_phases,
        "answer_preview": redact_text("".join(answer_preview))[:MAX_STRING_LENGTH],
        "usage": _sanitize(done_payload),
    }


def summarize_chat_chunks(chunks: Sequence[Any]) -> dict[str, Any]:
    """Reduce streamed Nebius chunks so traces do not store every token."""
    text_chunks: list[str] = []
    input_tokens = 0
    output_tokens = 0
    for chunk in chunks:
        text = getattr(chunk, "text", "")
        if isinstance(text, str) and text:
            text_chunks.append(text)
        input_tokens = int(getattr(chunk, "input_tokens", None) or input_tokens)
        output_tokens = int(getattr(chunk, "output_tokens", None) or output_tokens)
    return {
        "text_preview": redact_text("".join(text_chunks))[:MAX_STRING_LENGTH],
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
    }


def _sanitize(value: Any) -> Any:
    if isinstance(value, str):
        return redact_text(value)[:MAX_STRING_LENGTH]
    if value is None or isinstance(value, bool | int | float):
        return value
    if isinstance(value, datetime | date):
        return value.isoformat()
    if hasattr(value, "model_dump"):
        return _sanitize(value.model_dump())
    if is_dataclass(value) and not isinstance(value, type):
        return _sanitize(asdict(value))
    if isinstance(value, Mapping):
        return _sanitize_mapping(value)
    if isinstance(value, Sequence) and not isinstance(value, bytes | bytearray):
        items = [_sanitize(item) for item in value[:MAX_SEQUENCE_ITEMS]]
        if len(value) > MAX_SEQUENCE_ITEMS:
            items.append({"truncated": len(value) - MAX_SEQUENCE_ITEMS})
        return items
    return repr(value)[:MAX_STRING_LENGTH]


def _sanitize_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    sanitized: dict[str, Any] = {}
    for key, item in value.items():
        normalized_key = str(key).lower()
        if key == "self":
            continue
        if _is_secret_key(normalized_key):
            sanitized[str(key)] = "[redacted]"
            continue
        sanitized[str(key)] = _sanitize(item)
    return sanitized


def _is_secret_key(normalized_key: str) -> bool:
    if any(marker in normalized_key for marker in SECRET_KEY_MARKERS):
        return True
    return normalized_key == "token" or normalized_key.endswith("_token")
