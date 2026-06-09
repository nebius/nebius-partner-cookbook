"""Act 0 — Naive RAG agent.

Single retrieval over the Pinecone regulation knowledge base plus a single
LLM call. No tools, no ReAct loop, no Tavily — the deliberate baseline the
demo contrasts against the agentic stack. Same retrieval primitive
(`retrieve_regulation_text`) as the agentic graphs, same model
(DeepSeek-V4-Pro on Nebius) — only the orchestration differs.
"""
from __future__ import annotations

from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, BaseMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

from sentinel.config import MODEL_MAX_TOKENS

NAIVE_TOP_K = 20
NAIVE_CONTEXT_CHARS = 12_000

NAIVE_PROMPT = """You are a regulatory compliance analyst. Answer the question using ONLY the regulation excerpts below. Cite the regulation and section for every claim. If the excerpts don't contain enough information to answer, say so explicitly — do not invent details.

Question:
{question}

Retrieved regulation excerpts:
{context}

Answer:"""


class _NaiveState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def _build_model():
    from sentinel.chat_model import build_chat_model

    return build_chat_model(
        "nebius",
        max_tokens=MODEL_MAX_TOKENS,
        extra_metadata={"act": "act0_naive"},
    )


def _extract_user_message(state: _NaiveState) -> str:
    """Pull the most recent human message from the conversation."""
    for msg in reversed(state.get("messages", [])):
        # LangGraph sometimes hands us dict form, sometimes BaseMessage
        if isinstance(msg, dict):
            if msg.get("role") in ("user", "human") or msg.get("type") in ("human", "user"):
                return msg.get("content", "") or ""
        else:
            mtype = getattr(msg, "type", "")
            if mtype in ("human", "user"):
                return getattr(msg, "content", "") or ""
    return ""


def _naive_node(state: _NaiveState) -> dict:
    from sentinel.retrieval.regulations import (
        format_regulation_context,
        retrieve_regulation_text,
    )

    question = _extract_user_message(state)
    if not question.strip():
        return {"messages": [AIMessage(content="Ask a regulatory compliance question and I'll retrieve the relevant excerpts.")]}

    chunks = retrieve_regulation_text(question, regulations=None, top_k=NAIVE_TOP_K)
    context = format_regulation_context(chunks, max_chars=NAIVE_CONTEXT_CHARS)
    if not context:
        context = "(no retrieval results — the knowledge base returned nothing for this query)"

    prompt = NAIVE_PROMPT.format(question=question, context=context)
    model = _build_model()
    response = model.invoke([{"role": "user", "content": prompt}])
    return {"messages": [response]}


def build_naive_graph():
    """Build the Act 0 naive RAG graph (single retrieval + single LLM call)."""
    g = StateGraph(_NaiveState)
    g.add_node("naive_rag", _naive_node)
    g.add_edge(START, "naive_rag")
    g.add_edge("naive_rag", END)
    return g.compile()


def agent_naive():
    """Entry point for langgraph.json — returns the compiled naive graph."""
    return build_naive_graph()
