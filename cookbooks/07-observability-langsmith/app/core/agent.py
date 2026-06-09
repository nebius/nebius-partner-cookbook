"""LangGraph-backed agent logic. Pure async generator yielding typed events."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from dataclasses import dataclass
from time import perf_counter
from typing import Literal, TypedDict

from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END, START, StateGraph
from langsmith import traceable
from openai.types.chat import ChatCompletionMessageParam

from app.core.langsmith_annotations import (
    process_langsmith_inputs,
    process_langsmith_outputs,
    summarize_agent_events,
)
from app.core.nebius_client import NebiusClient
from app.core.nebius_pricing import NebiusPricing
from app.observability.metrics import agent_first_token_seconds, agent_route_total

SYSTEM_PROMPT = (
    "You are a helpful, concise assistant for a book recommendation agent. "
    "Answer the user's book question directly first. Then add a brief operational note "
    "about whether the request was simple enough to answer directly, needed a curated "
    "book recommendation layer, needed fresh publication or review context, or needed both. "
    "For latest/current publication questions, give the best-known answer and clearly say "
    "that a production version should verify it with fresh context. Do not claim live tools "
    "were called in this cookbook. Use plain text unless markdown adds clarity."
)

FRESH_CONTEXT_MARKERS = (
    "today",
    "latest",
    "current",
    "recent",
    "pricing",
    "price",
    "benchmark",
    "grounding",
    "compare",
    "review",
    "published",
    "publication",
    "since ",
    "2026",
)

RECOMMENDATION_MARKERS = (
    "recommend",
    "what should i read",
    "read next",
    "more books",
    "books on",
    "books about",
    "similar to",
    "i loved",
    "i liked",
)


@dataclass
class Event:
    name: str
    data: dict[str, object]


@dataclass(frozen=True)
class AgentRunOptions:
    temperature: float
    max_tokens: int
    history: list[dict[str, str]]


class AgentState(TypedDict):
    prompt: str
    history: list[dict[str, str]]
    requested_max_tokens: int
    route: Literal["direct", "deliberate"]
    context_need: Literal[
        "direct_answer",
        "curated_recommendation",
        "fresh_publication_context",
        "curated_plus_fresh_context",
    ]
    route_reason: str
    plan: str
    messages: list[ChatCompletionMessageParam]
    max_tokens: int


class Agent:
    """LangGraph skeleton that makes latency decisions explicit."""

    def __init__(
        self,
        client: NebiusClient,
        model: str,
        *,
        direct_max_tokens: int,
        deliberate_max_tokens: int,
        first_token_target_ms: int,
        pricing: NebiusPricing,
    ) -> None:
        self._client = client
        self._model = model
        self._direct_max_tokens = direct_max_tokens
        self._deliberate_max_tokens = deliberate_max_tokens
        self._first_token_target_ms = first_token_target_ms
        self._pricing = pricing
        self._prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "{system_prompt}\n\nOrchestration plan: {plan}"),
                ("human", "{prompt}"),
            ]
        )
        self._graph = self._build_graph()

    def _build_graph(self):
        graph = StateGraph(AgentState)
        graph.add_node("route", self._route_request)
        graph.add_node("prepare_direct", self._prepare_direct_messages)
        graph.add_node("prepare_deliberate", self._prepare_deliberate_messages)
        graph.add_edge(START, "route")
        graph.add_conditional_edges(
            "route",
            lambda state: state["route"],
            {
                "direct": "prepare_direct",
                "deliberate": "prepare_deliberate",
            },
        )
        graph.add_edge("prepare_direct", END)
        graph.add_edge("prepare_deliberate", END)
        return graph.compile()

    @staticmethod
    @traceable(
        name="agent.route_request",
        run_type="chain",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
    def _route_request(state: AgentState) -> dict[str, str]:
        prompt = state["prompt"].strip()
        history_text = " ".join(item.get("content", "") for item in state.get("history", [])[-4:])
        lower_prompt = f"{history_text} {prompt}".lower()
        needs_fresh_context = any(marker in lower_prompt for marker in FRESH_CONTEXT_MARKERS)
        needs_curated_recommendations = any(
            marker in lower_prompt for marker in RECOMMENDATION_MARKERS
        )

        if needs_fresh_context and needs_curated_recommendations:
            context_need = "curated_plus_fresh_context"
            route_reason = (
                "recommendation request also depends on recent publication or review context"
            )
        elif needs_fresh_context:
            context_need = "fresh_publication_context"
            route_reason = "question depends on latest/current publication context"
        elif needs_curated_recommendations:
            context_need = "curated_recommendation"
            route_reason = "question asks for taste or topic-based book recommendations"
        else:
            context_need = "direct_answer"
            route_reason = "question can be answered directly without extra context"

        needs_deliberate_path = len(prompt) > 280 or context_need != "direct_answer"
        route = "deliberate" if needs_deliberate_path else "direct"
        return {
            "route": route,
            "context_need": context_need,
            "route_reason": route_reason,
        }

    @traceable(
        name="agent.prepare_direct_messages",
        run_type="chain",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
    def _prepare_direct_messages(
        self, state: AgentState
    ) -> dict[str, str | int | list[ChatCompletionMessageParam]]:
        prompt = state["prompt"].strip()
        plan = (
            "Fast path: answer directly, avoid unnecessary planning tokens, and be concise. "
            f"Routing summary: {state['context_need']} because {state['route_reason']}."
        )
        return {
            "plan": plan,
            "messages": self._messages_from_template(
                system_prompt=SYSTEM_PROMPT,
                plan=plan,
                prompt=prompt,
                history=state.get("history", []),
            ),
            "max_tokens": min(state["requested_max_tokens"], self._direct_max_tokens),
        }

    @traceable(
        name="agent.prepare_deliberate_messages",
        run_type="chain",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
    def _prepare_deliberate_messages(
        self, state: AgentState
    ) -> dict[str, str | int | list[ChatCompletionMessageParam]]:
        prompt = state["prompt"].strip()
        plan = (
            "Deliberate path: answer the user first, keep the answer bounded, then explain "
            f"the routing note. Routing summary: {state['context_need']} because "
            f"{state['route_reason']}. Avoid extra tool or model calls unless a later "
            "cookbook adds them."
        )
        return {
            "plan": plan,
            "messages": self._messages_from_template(
                system_prompt=(
                    f"{SYSTEM_PROMPT} Prefer a compact answer with bullets only when they "
                    "improve scanability."
                ),
                plan=plan,
                prompt=prompt,
                history=state.get("history", []),
            ),
            "max_tokens": min(state["requested_max_tokens"], self._deliberate_max_tokens),
        }

    @traceable(
        name="agent.render_prompt_messages",
        run_type="chain",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
    def _messages_from_template(
        self,
        *,
        system_prompt: str,
        plan: str,
        prompt: str,
        history: list[dict[str, str]] | None = None,
    ) -> list[ChatCompletionMessageParam]:
        if history:
            recent = history[-6:]
            context = "\n".join(
                f"{item['role']}: {item['content'][:800]}" for item in recent if item.get("content")
            )
            prompt = (
                "Recent conversation context:\n"
                f"{context}\n\nCurrent user request:\n{prompt}\n\n"
                "Resolve references like 'that topic' from the recent conversation."
            )
        messages = self._prompt.format_messages(
            system_prompt=system_prompt,
            plan=plan,
            prompt=prompt,
        )
        return [self._to_openai_message(message) for message in messages]

    @staticmethod
    @traceable(
        name="agent.to_openai_message",
        run_type="chain",
        process_inputs=process_langsmith_inputs,
        process_outputs=process_langsmith_outputs,
    )
    def _to_openai_message(message: BaseMessage) -> ChatCompletionMessageParam:
        content = message.content if isinstance(message.content, str) else str(message.content)
        role = "system" if message.type == "system" else "user"
        return {"role": role, "content": content}

    @traceable(
        name="agent.stream_response",
        run_type="chain",
        process_inputs=process_langsmith_inputs,
        reduce_fn=summarize_agent_events,
    )
    async def run(
        self,
        prompt: str,
        *,
        options: AgentRunOptions,
        cancel_event: asyncio.Event | None = None,
    ) -> AsyncIterator[Event]:
        started_at = perf_counter()
        yield Event(
            "status",
            {
                "phase": "routing",
                "targetFirstTokenMs": self._first_token_target_ms,
            },
        )

        final_state: AgentState | None = None
        route: Literal["direct", "deliberate"] = "direct"
        context_need = "direct_answer"
        route_reason = "question can be answered directly without extra context"
        async for update in self._graph.astream(
            {
                "prompt": prompt,
                "requested_max_tokens": options.max_tokens,
                "history": options.history,
            },
            stream_mode="updates",
        ):
            if cancel_event is not None and cancel_event.is_set():
                return
            if "route" in update:
                route = update["route"]["route"]
                context_need = update["route"]["context_need"]
                route_reason = update["route"]["route_reason"]
                agent_route_total.labels(route=route).inc()
                yield Event(
                    "status",
                    {
                        "phase": "routed",
                        "route": route,
                        "contextNeed": context_need,
                        "reason": route_reason,
                    },
                )
            if "prepare_direct" in update:
                final_state = {
                    "prompt": prompt,
                    "requested_max_tokens": options.max_tokens,
                    "route": route,
                    "context_need": context_need,
                    "route_reason": route_reason,
                    **update["prepare_direct"],
                }
                yield Event(
                    "status",
                    {"phase": "writing", "route": "direct", "contextNeed": context_need},
                )
            if "prepare_deliberate" in update:
                final_state = {
                    "prompt": prompt,
                    "requested_max_tokens": options.max_tokens,
                    "route": route,
                    "context_need": context_need,
                    "route_reason": route_reason,
                    **update["prepare_deliberate"],
                }
                yield Event(
                    "status",
                    {"phase": "writing", "route": "deliberate", "contextNeed": context_need},
                )

        if final_state is None:
            return

        first_token_seen = False
        input_tokens = 0
        output_tokens = 0
        async for chunk in self._client.stream_chat(
            model=self._model,
            messages=final_state["messages"],
            temperature=options.temperature,
            max_tokens=final_state["max_tokens"],
        ):
            if cancel_event is not None and cancel_event.is_set():
                return
            if chunk.input_tokens is not None:
                input_tokens = chunk.input_tokens
            if chunk.output_tokens is not None:
                output_tokens = chunk.output_tokens
            if not chunk.text:
                continue
            if not first_token_seen:
                first_token_seen = True
                first_token_seconds = perf_counter() - started_at
                agent_first_token_seconds.labels(route=final_state["route"]).observe(
                    first_token_seconds
                )
                yield Event(
                    "status",
                    {
                        "phase": "first_token",
                        "elapsedMs": round(first_token_seconds * 1000),
                    },
                )
            yield Event("token", {"text": chunk.text})

        elapsed_seconds = perf_counter() - started_at
        cost_usd = (
            input_tokens * self._pricing.get_prices().input_per_million / 1_000_000
            + output_tokens * self._pricing.get_prices().output_per_million / 1_000_000
        )
        usage = {
            "inputTokens": input_tokens,
            "outputTokens": output_tokens,
            "totalTokens": input_tokens + output_tokens,
            "costUsd": round(cost_usd, 6),
            "elapsedSeconds": round(elapsed_seconds, 3),
        }
        yield Event(
            "token",
            {
                "text": (
                    "\n\n---\n"
                    f"Time: {elapsed_seconds:.2f}s | "
                    f"Tokens: {input_tokens} in, {output_tokens} out | "
                    f"Cost: ${cost_usd:.6f} | "
                    f"Routing: {final_state['route']} / {final_state['context_need']}"
                )
            },
        )
        yield Event(
            "status",
            {
                "phase": "done",
                "route": final_state["route"],
                "contextNeed": final_state["context_need"],
                "maxTokens": final_state["max_tokens"],
                "elapsedMs": round(elapsed_seconds * 1000),
                "usage": usage,
            },
        )
        yield Event("done", usage)
