"""SSE endpoint for book recommendations."""

from __future__ import annotations

import asyncio
import json
import time
from collections.abc import AsyncIterator

from fastapi import APIRouter, Depends, Request
from starlette.responses import StreamingResponse

from app.config import Settings, get_settings
from app.core.book_rag import BookRag, UsageSummary
from app.schemas.agent import AgentRunRequest

router = APIRouter()


def _sse(event: str, data: dict[str, object]) -> bytes:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n".encode()


def _combine_usage(*items: UsageSummary) -> UsageSummary:
    return UsageSummary(
        embedding_tokens=sum(item.embedding_tokens for item in items),
        input_tokens=sum(item.input_tokens for item in items),
        output_tokens=sum(item.output_tokens for item in items),
        cost_usd=sum(item.cost_usd for item in items),
    )


def _metrics_line(elapsed_seconds: float, usage: UsageSummary) -> str:
    return (
        "\n\n---\n"
        f"Time: {elapsed_seconds:.2f}s | "
        f"Tokens: {usage.embedding_tokens} embed, {usage.input_tokens} in, "
        f"{usage.output_tokens} out | "
        f"Cost: ${usage.cost_usd:.6f}"
    )


@router.post("/run")
async def run_agent(
    payload: AgentRunRequest,
    request: Request,
    settings: Settings = Depends(get_settings),
) -> StreamingResponse:
    """Retrieve Goodreads book context and stream a grounded recommendation answer."""

    async def event_stream() -> AsyncIterator[bytes]:
        if await request.is_disconnected():
            return

        started_at = time.perf_counter()
        rag = BookRag(settings)
        progress_messages = await asyncio.to_thread(rag.narrate_progress, payload.prompt)
        yield _sse(
            "agent_message",
            {"text": progress_messages[0]},
        )
        yield _sse("status", {"phase": "embedding", "message": "Preparing the semantic query"})

        try:
            yield _sse(
                "status",
                {"phase": "sending_to_nebius", "message": "Sending to Nebius Token Factory"},
            )
            query_vector, embedding_tokens = await asyncio.to_thread(
                rag.embed_query, payload.prompt
            )
            prices = await asyncio.to_thread(rag.pricing.get_prices)
            embedding_cost = embedding_tokens * prices.embedding_per_million / 1_000_000
            retrieval_usage = UsageSummary(
                embedding_tokens=embedding_tokens,
                cost_usd=embedding_cost,
            )

            yield _sse(
                "agent_message",
                {"text": progress_messages[1]},
            )
            yield _sse("status", {"phase": "knowledge", "message": "Requesting Pinecone Knowledge"})
            books = await asyncio.to_thread(
                rag.retrieve_books_from_vector,
                query_vector,
                payload.top_k,
                payload.related_top_k,
                payload.include_related,
            )
            yield _sse("context", {"books": [book.to_public_dict() for book in books]})
            yield _sse(
                "agent_message",
                {"text": f"{progress_messages[2]} ({len(books)} candidates)"},
            )

            yield _sse("status", {"phase": "synthesizing", "message": "Synthesizing"})
            input_tokens = 0
            output_tokens = 0
            stream = await asyncio.to_thread(rag.stream_synthesis, payload.prompt, books)
            for chunk in stream:
                if await request.is_disconnected():
                    return
                usage_data = getattr(chunk, "usage", None)
                if usage_data is not None:
                    input_tokens = int(getattr(usage_data, "prompt_tokens", 0) or 0)
                    output_tokens = int(getattr(usage_data, "completion_tokens", 0) or 0)

                for choice in getattr(chunk, "choices", []) or []:
                    piece = getattr(getattr(choice, "delta", None), "content", None)
                    if piece:
                        yield _sse("token", {"text": piece})

            prices = await asyncio.to_thread(rag.pricing.get_prices)
            synthesis_cost = (
                input_tokens * prices.input_per_million / 1_000_000
                + output_tokens * prices.output_per_million / 1_000_000
            )
            usage = _combine_usage(
                retrieval_usage,
                UsageSummary(
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    cost_usd=synthesis_cost,
                ),
            )
            elapsed_seconds = time.perf_counter() - started_at
            yield _sse("token", {"text": _metrics_line(elapsed_seconds, usage)})
            yield _sse(
                "status",
                {
                    "phase": "done",
                    "message": (
                        f"Done ({usage.input_tokens} token in | "
                        f"{usage.output_tokens} token out | "
                        f"{elapsed_seconds:.2f}s | "
                        f"Cost: {usage.cost_usd:.6f} USD)"
                    ),
                    "usage": usage.to_public_dict(),
                    "elapsedSeconds": round(elapsed_seconds, 3),
                },
            )
            done_payload = usage.to_public_dict()
            done_payload["elapsedSeconds"] = round(elapsed_seconds, 3)
            yield _sse("done", done_payload)
        except Exception:
            yield _sse("error", {"detail": "book recommendation failed"})

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"cache-control": "no-cache", "x-accel-buffering": "no"},
    )
