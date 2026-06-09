"""Agent endpoint with SSE streaming."""

import asyncio
import json
from collections.abc import AsyncIterator

import structlog
from fastapi import APIRouter, Depends, Request
from starlette.responses import StreamingResponse

from app.config import Settings, get_settings
from app.core.agent import Agent, AgentRunOptions
from app.core.nebius_client import NebiusClient, build_nebius_client
from app.core.nebius_pricing import NebiusPricing
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
            stored_history = await memory.get_history(payload.thread_id)
            history = [*stored_history, *(item.model_dump() for item in payload.history)]
            yield _sse(
                "status",
                {
                    "phase": "memory_loaded",
                    "threadId": payload.thread_id,
                    "messages": len(stored_history),
                },
            )
            async for event in agent.run(
                payload.prompt,
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
                yield _sse(event.name, event.data)
            if not cancel_event.is_set():
                retained = await memory.append_turn(
                    payload.thread_id,
                    user=payload.prompt,
                    assistant="".join(assistant_chunks).strip(),
                )
                yield _sse(
                    "status",
                    {
                        "phase": "memory_saved",
                        "threadId": payload.thread_id,
                        "messages": retained,
                    },
                )
            yield _sse("done", {})
        except Exception as exc:
            logger.exception("agent_failed", error=str(exc))
            yield _sse("error", {"detail": "internal error"})
        finally:
            cancel_event.set()
            watcher.cancel()

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"cache-control": "no-cache", "x-accel-buffering": "no"},
    )
