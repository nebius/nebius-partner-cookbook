"""Agent endpoint with SSE streaming."""

import asyncio
import json
from collections.abc import AsyncIterator

import structlog
from fastapi import APIRouter, Depends, Request
from starlette.responses import StreamingResponse

from app.config import Settings, get_settings
from app.core.agent import Agent
from app.core.nebius_client import NebiusClient, build_nebius_client
from app.schemas.agent import AgentRunRequest

logger = structlog.get_logger()
router = APIRouter()

HEARTBEAT_INTERVAL_SECONDS = 15


def _sse(event: str, data: dict[str, object]) -> bytes:
    # SSE wire format: each frame is `event: <name>\ndata: <json>\n\n`.
    # The blank line terminates the frame; the browser EventSource API parses it.
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n".encode()


@router.post("/run")
async def run_agent(
    payload: AgentRunRequest,
    request: Request,
    settings: Settings = Depends(get_settings),
    client: NebiusClient = Depends(build_nebius_client),
) -> StreamingResponse:
    """Run the agent and stream SSE events back to the client."""
    agent = Agent(client=client, model=settings.nebius_model)

    async def event_stream() -> AsyncIterator[bytes]:
        # `cancel_event` is the bridge between the disconnect watcher and the
        # agent loop: when the client goes away, the watcher sets it and the
        # agent stops fetching tokens on its next iteration.
        cancel_event = asyncio.Event()

        async def watch_disconnect() -> None:
            # Polled, because Starlette doesn't push disconnects — we ask.
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
            async for event in agent.run(
                payload.prompt,
                history=payload.history,
                cancel_event=cancel_event,
            ):
                # Heartbeat keeps proxies and load balancers from closing an
                # idle stream during slow LLM responses.
                now = loop.time()
                if now - last_event_at > HEARTBEAT_INTERVAL_SECONDS:
                    yield _sse("heartbeat", {})
                last_event_at = now
                yield _sse(event.name, event.data)
            yield _sse("done", {})
        except Exception as exc:
            # Never leak internals to the client; full stack trace goes to logs.
            logger.exception("agent_failed", error=str(exc))
            yield _sse("error", {"detail": "internal error"})
        finally:
            cancel_event.set()
            watcher.cancel()

    # `x-accel-buffering: no` tells nginx (and similar) to forward chunks
    # immediately rather than buffering the response.
    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"cache-control": "no-cache", "x-accel-buffering": "no"},
    )
