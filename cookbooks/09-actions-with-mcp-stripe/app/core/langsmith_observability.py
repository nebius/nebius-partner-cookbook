"""LangSmith tracing and feedback helpers."""

from __future__ import annotations

import asyncio
import re
import uuid
from datetime import UTC, datetime
from typing import Any

import structlog

from app.config import Settings, get_settings

logger = structlog.get_logger()

EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\b(?:\+?\d[\d .()-]{7,}\d)\b")


class LangSmithObserver:
    """Small adapter around LangSmith's client.

    The adapter is intentionally disabled by default so local tests and five-minute
    cookbook runs do not require SaaS credentials.
    """

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._enabled = bool(settings.langsmith_tracing and settings.langsmith_api_key)
        self._client: Any | None = None

    @property
    def enabled(self) -> bool:
        return self._enabled

    def _get_client(self) -> Any:
        if self._client is None:
            from langsmith import Client

            self._client = Client(
                api_key=self._settings.langsmith_api_key,
                api_url=str(self._settings.langsmith_endpoint),
            )
        return self._client

    async def start_run(
        self,
        *,
        prompt: str,
        thread_id: str,
        user_id: str,
        model: str,
        env: str,
    ) -> str | None:
        """Create a LangSmith run and return the run id."""
        if not self.enabled:
            return None
        run_id = str(uuid.uuid4())
        inputs = {
            "prompt_preview": _redact(prompt)[:500],
            "thread_id": thread_id,
            "user_id": user_id,
        }
        extra = {
            "metadata": {
                "cookbook": "09-actions-with-mcp-stripe",
                "env": env,
                "thread_id": thread_id,
                "user_id": user_id,
            }
        }
        tags = ["nebius-cookbook", "observability", env, model]
        try:
            await asyncio.to_thread(
                self._get_client().create_run,
                name="agent.run",
                inputs=inputs,
                run_type="chain",
                id=run_id,
                project_name=self._settings.langsmith_project,
                start_time=datetime.now(UTC),
                extra=extra,
                tags=tags,
            )
        except Exception as exc:
            logger.warning("langsmith_create_run_failed", error=str(exc))
            return None
        return run_id

    async def finish_run(
        self,
        run_id: str | None,
        *,
        output: str,
        error: str | None = None,
    ) -> None:
        """Mark a LangSmith run complete."""
        if not self.enabled or run_id is None:
            return
        try:
            await asyncio.to_thread(
                self._get_client().update_run,
                run_id,
                end_time=datetime.now(UTC),
                outputs={"answer_preview": _redact(output)[:1_000]} if error is None else None,
                error=error,
            )
        except Exception as exc:
            logger.warning("langsmith_update_run_failed", run_id=run_id, error=str(exc))

    async def create_feedback(
        self,
        *,
        run_id: str,
        key: str,
        score: float | int | bool | None,
        comment: str | None,
    ) -> bool:
        """Attach feedback to a LangSmith run."""
        if not self.enabled:
            return False
        try:
            await asyncio.to_thread(
                self._get_client().create_feedback,
                run_id=run_id,
                key=key,
                score=score,
                comment=_redact(comment) if comment else None,
                source_info={"source": "cookbook-api"},
            )
        except Exception as exc:
            logger.warning("langsmith_feedback_failed", run_id=run_id, error=str(exc))
            return False
        return True


def _redact(value: str) -> str:
    value = EMAIL_RE.sub("[redacted-email]", value)
    return PHONE_RE.sub("[redacted-phone]", value)


_observer: LangSmithObserver | None = None


def get_langsmith_observer() -> LangSmithObserver:
    """FastAPI dependency for LangSmith observability."""
    global _observer
    if _observer is None:
        _observer = LangSmithObserver(get_settings())
    return _observer
