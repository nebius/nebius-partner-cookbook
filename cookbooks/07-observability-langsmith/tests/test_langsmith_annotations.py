"""Tests for LangSmith annotation helpers."""

from __future__ import annotations

from dataclasses import dataclass

from app.config import Settings
from app.core.agent import Event
from app.core.langsmith_annotations import (
    process_langsmith_inputs,
    process_langsmith_outputs,
    redact_text,
    summarize_agent_events,
    summarize_chat_chunks,
)
from app.core.langsmith_observability import LangSmithObserver
from app.core.nebius_client import ChatStreamChunk


@dataclass(frozen=True)
class ExampleOutput:
    email: str
    value: int


def test_langsmith_redaction_removes_direct_identifiers() -> None:
    text = redact_text("Contact reader@example.com or +33 6 12 34 56 78.")

    assert "reader@example.com" not in text
    assert "+33 6 12 34 56 78" not in text
    assert "[redacted-email]" in text
    assert "[redacted-phone]" in text


def test_langsmith_input_processing_redacts_secrets_and_self() -> None:
    processed = process_langsmith_inputs(
        {
            "self": object(),
            "prompt": "Email me at reader@example.com",
            "api_key": "sk-secret",
            "messages": [{"content": "hello"}],
        }
    )

    assert "self" not in processed
    assert processed["api_key"] == "[redacted]"
    assert processed["prompt"] == "Email me at [redacted-email]"
    assert processed["messages"] == [{"content": "hello"}]


def test_langsmith_output_processing_handles_dataclasses() -> None:
    processed = process_langsmith_outputs(ExampleOutput(email="reader@example.com", value=42))

    assert processed == {"email": "[redacted-email]", "value": 42}


def test_agent_event_reducer_summarizes_stream_without_cost_footer() -> None:
    summary = summarize_agent_events(
        [
            Event("status", {"phase": "routing"}),
            Event("token", {"text": "Useful "}),
            Event("token", {"text": "answer."}),
            Event("token", {"text": "\n\n---\nTime: 1.00s | Tokens: 1 in, 1 out"}),
            Event("done", {"inputTokens": 2, "outputTokens": 3}),
        ]
    )

    assert summary["tokens_streamed"] == 3
    assert summary["status_phases"] == ["routing"]
    assert summary["answer_preview"] == "Useful answer."
    assert summary["usage"] == {"inputTokens": 2, "outputTokens": 3}


def test_chat_chunk_reducer_summarizes_token_usage() -> None:
    summary = summarize_chat_chunks(
        [
            ChatStreamChunk(text="Hello "),
            ChatStreamChunk(text="reader@example.com"),
            ChatStreamChunk(input_tokens=10, output_tokens=4),
        ]
    )

    assert summary == {
        "text_preview": "Hello [redacted-email]",
        "input_tokens": 10,
        "output_tokens": 4,
    }


def test_disabled_langsmith_trace_yields_no_run_id() -> None:
    settings = Settings(langsmith_tracing=False, langsmith_api_key=None)
    observer = LangSmithObserver(settings)

    with observer.trace_agent_run(
        prompt="hello",
        thread_id="thread-1",
        user_id="user-1",
        model=settings.nebius_model,
        env=settings.env,
    ) as trace_run:
        trace_run.finish(output="done")

    assert trace_run.run_id is None
