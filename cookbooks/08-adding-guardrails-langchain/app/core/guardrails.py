"""Deterministic guardrails for the cookbook agent."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Literal

from langchain.agents.middleware import AgentMiddleware
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage
from langsmith import traceable

from app.config import Settings
from app.core.langsmith_annotations import process_langsmith_inputs, process_langsmith_outputs
from app.observability.metrics import guardrail_events_total

EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\b(?:\+?\d[\d .()-]{7,}\d)\b")

PROMPT_INJECTION_MARKERS = (
    "ignore previous instructions",
    "ignore all previous",
    "reveal your system prompt",
    "show me the developer message",
    "bypass guardrails",
    "disable safety",
)

UNSUPPORTED_ACTION_MARKERS = (
    "buy this book",
    "purchase this book",
    "charge my card",
    "create a checkout",
)

BOOK_TOPIC_MARKERS = (
    "audiobook",
    "award",
    "bestseller",
    "bibliography",
    "book",
    "book club",
    "bookstore",
    "chapter",
    "classic",
    "comic",
    "criticism",
    "ebook",
    "essay",
    "genre",
    "goodreads",
    "graphic novel",
    "hardcover",
    "isbn",
    "literary",
    "literature",
    "memoir",
    "novella",
    "paperback",
    "plot",
    "poem",
    "poetry",
    "prose",
    "publisher",
    "publishing",
    "reading list",
    "review",
    "series",
    "short story",
    "story",
    "stories",
    "translation",
    "writer",
    "writing",
    "young adult",
    "ya",
    "book",
    "books",
    "novel",
    "novels",
    "read",
    "reading",
    "reader",
    "author",
    "authors",
    "fiction",
    "nonfiction",
    "sci-fi",
    "fantasy",
    "memoir",
    "biography",
    "poetry",
    "literature",
    "story",
    "stories",
    "edition",
    "publisher",
    "published",
    "library",
    "houellebecq",
    "ursula le guin",
    "le guin",
    "octavia butler",
    "dune",
    "station eleven",
)

NON_BOOK_REQUEST_MARKERS = (
    "bash",
    "bitcoin",
    "carbonara",
    "celebrity gossip",
    "chmod",
    "crypto",
    "delete files",
    "deploy my server",
    "execute a script",
    "forecast",
    "give me a recipe",
    "latest news",
    "medical advice",
    "portfolio",
    "python script",
    "recipe for",
    "rm -rf",
    "run a command",
    "run a script",
    "shell command",
    "stock price",
    "sports score",
    "terraform",
    "weather",
    "write a script",
)

FALSE_TOOL_CLAIMS = (
    "i searched the web",
    "i checked live",
    "i accessed your account",
    "i charged",
    "payment link",
)

UNSAFE_OUTPUT_MARKERS = (
    "kill yourself",
    "self-harm instructions",
)


@dataclass(frozen=True)
class GuardrailDecision:
    """Guardrail verdict for one stage."""

    allowed: bool
    text: str
    stage: Literal["input", "output"]
    rule: str
    outcome: Literal["passed", "blocked", "redacted"]
    reasons: list[str] = field(default_factory=list)


class Guardrails:
    """Facade around LangChain-compatible guardrail middleware."""

    def __init__(self, settings: Settings) -> None:
        self.input_middleware = BookInputGuardrailMiddleware(settings)
        self.output_middleware = BookOutputGuardrailMiddleware(settings)

    def validate_input(self, prompt: str) -> GuardrailDecision:
        """Validate and possibly redact user input."""
        return self.input_middleware.validate_prompt(prompt)

    def validate_output(self, text: str) -> GuardrailDecision:
        """Validate generated text before streaming it to the client."""
        return self.output_middleware.validate_answer(text)


class BookInputGuardrailMiddleware(AgentMiddleware):
    """LangChain middleware for pre-model book-domain input validation."""

    def __init__(self, settings: Settings) -> None:
        super().__init__()
        self._settings = settings

    def before_agent(self, state: dict[str, Any], runtime: object) -> dict[str, Any] | None:
        """Apply input guardrails to the last human message in a LangChain agent state."""
        messages = list(state.get("messages", []))
        prompt = _last_human_text(messages)
        if prompt is None:
            return None

        decision = self.validate_prompt(prompt)
        if not decision.allowed:
            raise ValueError(f"input guardrail blocked: {decision.rule}")
        if decision.text == prompt:
            return None
        return {"messages": _replace_last_human_text(messages, decision.text)}

    @traceable(
        name="guardrails.input.validate",
        run_type="chain",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
    def validate_prompt(self, prompt: str) -> GuardrailDecision:
        """Validate and possibly redact user input."""
        if not self._settings.guardrails_enabled:
            return _decision(True, prompt, "input", "disabled", "passed")

        lower = prompt.lower()
        for marker in PROMPT_INJECTION_MARKERS:
            if marker in lower:
                return _decision(False, prompt, "input", "prompt_injection", "blocked", marker)

        for marker in UNSUPPORTED_ACTION_MARKERS:
            if marker in lower:
                return _decision(False, prompt, "input", "unsupported_action", "blocked", marker)

        if not _is_book_related(lower):
            return _decision(
                False,
                prompt,
                "input",
                "topic_boundary",
                "blocked",
                self._settings.guardrails_topic,
            )

        redacted = EMAIL_RE.sub("[redacted-email]", prompt)
        redacted = PHONE_RE.sub("[redacted-phone]", redacted)
        if redacted != prompt:
            return _decision(True, redacted, "input", "pii", "redacted", "PII redacted")

        return _decision(True, prompt, "input", "all", "passed")


class BookOutputGuardrailMiddleware(AgentMiddleware):
    """LangChain middleware for post-model answer validation."""

    def __init__(self, settings: Settings) -> None:
        super().__init__()
        self._settings = settings

    def after_agent(self, state: dict[str, Any], runtime: object) -> dict[str, Any] | None:
        """Validate the last AI message in a LangChain agent state."""
        messages = list(state.get("messages", []))
        answer = _last_ai_text(messages)
        if answer is None:
            return None
        decision = self.validate_answer(answer)
        if not decision.allowed:
            raise ValueError(f"output guardrail blocked: {decision.rule}")
        if decision.text == answer:
            return None
        return {"messages": _replace_last_ai_text(messages, decision.text)}

    @traceable(
        name="guardrails.output.validate",
        run_type="chain",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
    def validate_answer(self, text: str) -> GuardrailDecision:
        """Validate generated text before streaming it to the client."""
        if not self._settings.guardrails_enabled:
            return _decision(True, text, "output", "disabled", "passed")

        if not text.strip():
            return _decision(False, text, "output", "non_empty", "blocked", "empty output")

        if len(text) > self._settings.guardrails_max_output_chars:
            return _decision(False, text, "output", "length", "blocked", "output too long")

        lower = text.lower()
        for marker in FALSE_TOOL_CLAIMS:
            if marker in lower:
                return _decision(False, text, "output", "false_tool_claim", "blocked", marker)

        for marker in UNSAFE_OUTPUT_MARKERS:
            if marker in lower:
                return _decision(False, text, "output", "safety", "blocked", marker)

        return _decision(True, text, "output", "all", "passed")


def _last_human_text(messages: list[AnyMessage]) -> str | None:
    for message in reversed(messages):
        if isinstance(message, HumanMessage):
            return str(message.content)
    return None


def _last_ai_text(messages: list[AnyMessage]) -> str | None:
    for message in reversed(messages):
        if isinstance(message, AIMessage):
            return str(message.content)
    return None


def _replace_last_human_text(messages: list[AnyMessage], text: str) -> list[AnyMessage]:
    replaced = list(messages)
    for index in range(len(replaced) - 1, -1, -1):
        message = replaced[index]
        if isinstance(message, HumanMessage):
            replaced[index] = HumanMessage(content=text, id=message.id, name=message.name)
            break
    return replaced


def _replace_last_ai_text(messages: list[AnyMessage], text: str) -> list[AnyMessage]:
    replaced = list(messages)
    for index in range(len(replaced) - 1, -1, -1):
        message = replaced[index]
        if isinstance(message, AIMessage):
            replaced[index] = AIMessage(content=text, id=message.id, name=message.name)
            break
    return replaced


def _decision(
    allowed: bool,
    text: str,
    stage: Literal["input", "output"],
    rule: str,
    outcome: Literal["passed", "blocked", "redacted"],
    reason: str | None = None,
) -> GuardrailDecision:
    guardrail_events_total.labels(stage=stage, rule=rule, outcome=outcome).inc()
    return GuardrailDecision(
        allowed=allowed,
        text=text,
        stage=stage,
        rule=rule,
        outcome=outcome,
        reasons=[reason] if reason else [],
    )


def _is_book_related(lower_prompt: str) -> bool:
    if any(marker in lower_prompt for marker in NON_BOOK_REQUEST_MARKERS):
        return False
    return any(marker in lower_prompt for marker in BOOK_TOPIC_MARKERS)


def get_guardrails(settings: Settings) -> Guardrails:
    """Build guardrails from validated settings."""
    return Guardrails(settings)
