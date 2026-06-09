"""LangSmith tracing and feedback helpers."""

from __future__ import annotations

import asyncio
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

import structlog

from app.config import Settings, get_settings
from app.core.langsmith_annotations import redact_text

logger = structlog.get_logger()


@dataclass
class LangSmithTrace:
    """Active LangSmith root trace for one guarded agent request."""

    run_id: str | None
    _run_tree: Any | None = None
    _finished: bool = False

    def finish(self, *, output: str, error: str | None = None) -> None:
        """Finalize the root trace without making tracing a response dependency."""
        if self._run_tree is None or self._finished:
            return
        self._finished = True
        try:
            self._run_tree.end(
                outputs={"answer_preview": redact_text(output)[:1_000]} if error is None else None,
                error=error,
                end_time=datetime.now(UTC),
            )
        except Exception as exc:
            logger.warning("langsmith_trace_finish_failed", run_id=self.run_id, error=str(exc))


class LangSmithObserver:
    """Small adapter around LangSmith's client.

    The adapter is disabled unless both tracing and an API key are configured, so
    local tests and five-minute cookbook runs never require SaaS credentials.
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

    @contextmanager
    def trace_agent_run(
        self,
        *,
        prompt: str,
        thread_id: str,
        user_id: str,
        model: str,
        env: str,
    ) -> Iterator[LangSmithTrace]:
        """Create the root trace and let @traceable child spans attach to it."""
        if not self.enabled:
            yield LangSmithTrace(run_id=None)
            return

        from langsmith import trace, tracing_context, uuid7

        run_id = uuid7()
        client = self._get_client()
        metadata = {
            "cookbook": "08-adding-guardrails-langchain",
            "env": env,
            "thread_id": thread_id,
            "user_id": user_id,
            "model": model,
        }
        tags = ["nebius-cookbook", "cookbook-08", "guardrails", env, model]
        manager = trace(
            "agent.run",
            run_type="chain",
            inputs={
                "prompt_preview": redact_text(prompt)[:500],
                "thread_id": thread_id,
                "user_id": user_id,
            },
            project_name=self._settings.langsmith_project,
            client=client,
            run_id=run_id,
            metadata=metadata,
            tags=tags,
        )

        try:
            run_tree = manager.__enter__()
        except Exception as exc:
            logger.warning("langsmith_trace_start_failed", error=str(exc))
            yield LangSmithTrace(run_id=None)
            return

        annotation_manager = tracing_context(
            enabled=True,
            client=client,
            project_name=self._settings.langsmith_project,
            parent=run_tree,
            metadata=metadata,
            tags=tags,
        )
        try:
            annotation_manager.__enter__()
        except Exception as exc:
            logger.warning("langsmith_annotation_context_failed", error=str(exc))
            annotation_manager = None

        active_trace = LangSmithTrace(run_id=str(run_id), _run_tree=run_tree)
        exc_info: tuple[type[BaseException] | None, BaseException | None, Any] = (
            None,
            None,
            None,
        )
        try:
            yield active_trace
        except BaseException as exc:
            exc_info = (type(exc), exc, exc.__traceback__)
            active_trace.finish(output="", error=str(exc))
            raise
        finally:
            if not active_trace._finished:
                active_trace.finish(output="")
            if annotation_manager is not None:
                try:
                    annotation_manager.__exit__(*exc_info)
                except Exception as exc:
                    logger.warning(
                        "langsmith_annotation_context_close_failed",
                        run_id=active_trace.run_id,
                        error=str(exc),
                    )
            try:
                manager.__exit__(*exc_info)
            except Exception as exc:
                logger.warning(
                    "langsmith_trace_submit_failed",
                    run_id=active_trace.run_id,
                    error=str(exc),
                )

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
                comment=redact_text(comment) if comment else None,
                source_info={"source": "cookbook-api"},
            )
        except Exception as exc:
            logger.warning("langsmith_feedback_failed", run_id=run_id, error=str(exc))
            return False
        return True


_observer: LangSmithObserver | None = None


def get_langsmith_observer() -> LangSmithObserver:
    """FastAPI dependency for LangSmith observability."""
    global _observer
    if _observer is None:
        _observer = LangSmithObserver(get_settings())
    return _observer
