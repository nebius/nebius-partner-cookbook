"""Agent endpoint with SSE streaming."""

import asyncio
import json
from collections.abc import AsyncIterator

import structlog
from fastapi import APIRouter, Depends, Request
from starlette.responses import StreamingResponse

from app.config import Settings, get_settings
from app.core.agent import Agent, AgentRunOptions
from app.core.approvals import ApprovalStore, get_approval_store
from app.core.book_catalog import load_book_catalog
from app.core.guardrails import get_guardrails
from app.core.langsmith_observability import LangSmithObserver, get_langsmith_observer
from app.core.long_term_memory import (
    LongTermMemoryStore,
    extract_memories,
    get_long_term_memory_store,
    memories_as_history,
)
from app.core.nebius_client import NebiusClient, build_nebius_client
from app.core.nebius_pricing import NebiusPricing
from app.core.purchase_intent import is_purchase_intent
from app.core.thread_memory import ThreadMemoryStore, get_thread_memory_store
from app.schemas.agent import AgentRunRequest

logger = structlog.get_logger()
router = APIRouter()

HEARTBEAT_INTERVAL_SECONDS = 15


def _sse(event: str, data: dict[str, object]) -> bytes:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n".encode()


@router.post("/run")
async def run_agent(
    payload: AgentRunRequest,
    request: Request,
    settings: Settings = Depends(get_settings),
    client: NebiusClient = Depends(build_nebius_client),
    memory: ThreadMemoryStore = Depends(get_thread_memory_store),
    observer: LangSmithObserver = Depends(get_langsmith_observer),
    long_term_memory: LongTermMemoryStore = Depends(get_long_term_memory_store),
    approvals: ApprovalStore = Depends(get_approval_store),
) -> StreamingResponse:
    """Run the agent and stream SSE events back to the client."""
    agent = Agent(
        client=client,
        model=settings.nebius_model,
        direct_max_tokens=settings.direct_response_max_tokens,
        deliberate_max_tokens=settings.deliberate_response_max_tokens,
        first_token_target_ms=settings.first_token_target_ms,
        pricing=NebiusPricing(settings),
    )

    async def event_stream() -> AsyncIterator[bytes]:
        cancel_event = asyncio.Event()

        async def watch_disconnect() -> None:
            while not cancel_event.is_set():
                if await request.is_disconnected():
                    logger.info("client_disconnected")
                    cancel_event.set()
                    return
                await asyncio.sleep(1)

        watcher = asyncio.create_task(watch_disconnect())
        loop = asyncio.get_event_loop()
        last_event_at = loop.time()

        try:
            assistant_chunks: list[str] = []
            run_id = await observer.start_run(
                prompt=payload.prompt,
                thread_id=payload.thread_id,
                user_id=payload.user_id,
                model=settings.nebius_model,
                env=settings.env,
            )
            guardrails = get_guardrails(settings)
            input_decision = guardrails.validate_input(payload.prompt)
            yield _sse(
                "status",
                {
                    "phase": "input_guardrail",
                    "rule": input_decision.rule,
                    "outcome": input_decision.outcome,
                },
            )
            if not input_decision.allowed:
                yield _sse(
                    "error",
                    {
                        "detail": "request blocked by input guardrail",
                        "rule": input_decision.rule,
                        "langsmithRunId": run_id,
                    },
                )
                await observer.finish_run(
                    run_id,
                    output="",
                    error=f"input guardrail blocked: {input_decision.rule}",
                )
                yield _sse("done", {})
                return

            if is_purchase_intent(input_decision.text):
                try:
                    catalog = load_book_catalog(settings.book_catalog_path)
                    selected_book = catalog.select_for_prompt(input_decision.text)
                    approval = approvals.create(
                        thread_id=payload.thread_id,
                        user_id=payload.user_id,
                        prompt=input_decision.text,
                        book=selected_book,
                        ttl_seconds=settings.approval_ttl_seconds,
                    )
                except RuntimeError as exc:
                    yield _sse(
                        "error",
                        {
                            "detail": str(exc),
                            "langsmithRunId": run_id,
                        },
                    )
                    await observer.finish_run(run_id, output="", error=str(exc))
                    yield _sse("done", {})
                    return

                message = (
                    "I can create a Stripe test-mode checkout link for "
                    f"{selected_book.title}, but I need your approval first."
                )
                yield _sse(
                    "approval_required",
                    {
                        "approvalId": approval.id,
                        "action": "stripe.create_payment_link",
                        "expiresAt": approval.expires_at.isoformat(),
                        "book": {
                            "slug": selected_book.slug,
                            "title": selected_book.title,
                            "author": selected_book.author,
                            "amount": selected_book.amount,
                            "currency": selected_book.currency,
                            "prices": selected_book.prices,
                        },
                    },
                )
                yield _sse("answer", {"text": message})
                await observer.finish_run(run_id, output=message)
                yield _sse("done", {})
                return

            stored_history = await memory.get_history(payload.thread_id)
            recalled = await long_term_memory.recall(
                payload.user_id,
                input_decision.text,
                limit=settings.long_term_memory_limit,
            )
            history = [
                *memories_as_history(recalled),
                *stored_history,
                *(item.model_dump() for item in payload.history),
            ]
            yield _sse(
                "status",
                {
                    "phase": "memory_loaded",
                    "threadId": payload.thread_id,
                    "userId": payload.user_id,
                    "langsmithRunId": run_id,
                    "messages": len(stored_history),
                    "longTermMemories": len(recalled),
                },
            )
            async for event in agent.run(
                input_decision.text,
                options=AgentRunOptions(
                    temperature=payload.temperature,
                    max_tokens=payload.max_tokens,
                    history=history,
                ),
                cancel_event=cancel_event,
            ):
                now = loop.time()
                if now - last_event_at > HEARTBEAT_INTERVAL_SECONDS:
                    yield _sse("heartbeat", {})
                last_event_at = now
                if event.name == "done":
                    continue
                if event.name == "token":
                    text = event.data.get("text")
                    if isinstance(text, str) and not text.startswith("\n\n---\nTime:"):
                        assistant_chunks.append(text)
                        continue
                if event.name == "token":
                    continue
                yield _sse(event.name, event.data)
            if not cancel_event.is_set():
                answer = "".join(assistant_chunks).strip()
                output_decision = guardrails.validate_output(answer)
                yield _sse(
                    "status",
                    {
                        "phase": "output_guardrail",
                        "rule": output_decision.rule,
                        "outcome": output_decision.outcome,
                    },
                )
                if not output_decision.allowed:
                    yield _sse(
                        "error",
                        {
                            "detail": "response blocked by output guardrail",
                            "rule": output_decision.rule,
                            "langsmithRunId": run_id,
                        },
                    )
                    await observer.finish_run(
                        run_id,
                        output="",
                        error=f"output guardrail blocked: {output_decision.rule}",
                    )
                    yield _sse("done", {})
                    return
                yield _sse("answer", {"text": output_decision.text})
                retained = await memory.append_turn(
                    payload.thread_id,
                    user=input_decision.text,
                    assistant=output_decision.text,
                )
                yield _sse(
                    "status",
                    {
                        "phase": "memory_saved",
                        "threadId": payload.thread_id,
                        "messages": retained,
                    },
                )
                saved_memories = []
                for text in extract_memories(input_decision.text):
                    saved = await long_term_memory.save_memory(
                        payload.user_id,
                        text,
                        source="user_prompt",
                    )
                    saved_memories.append(saved.id)
                if saved_memories:
                    yield _sse(
                        "status",
                        {
                            "phase": "long_term_memory_saved",
                            "userId": payload.user_id,
                            "memories": len(saved_memories),
                        },
                    )
                await observer.finish_run(run_id, output=output_decision.text)
            yield _sse("done", {})
        except Exception as exc:
            logger.exception("agent_failed", error=str(exc))
            await observer.finish_run(
                run_id if "run_id" in locals() else None,
                output="",
                error=str(exc),
            )
            yield _sse("error", {"detail": "internal error"})
        finally:
            cancel_event.set()
            watcher.cancel()

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"cache-control": "no-cache", "x-accel-buffering": "no"},
    )
