"""Naive single-pass RAG baseline: one retrieval, one LLM call, no tools."""
from __future__ import annotations

import time

from sentinel.config import MODEL, MODEL_MAX_TOKENS
from sentinel.retrieval.local import load_sop_by_id, load_sop_chunks
from sentinel.retrieval.regulations import (
    format_regulation_context,
    retrieve_regulation_text,
)

NAIVE_TOP_K = 20
NAIVE_CONTEXT_CHARS = 12_000

NAIVE_PROMPT = """You are a regulatory compliance analyst. Answer the question using ONLY the regulation excerpts and SOP text provided. Cite the regulation and section for every claim.

If the question asks whether a specific SOP complies with a regulation, end your answer with a line in this exact form:

Compliance level: <compliant|partial|gap>

Question:
{question}

{sop_block}Retrieved regulation excerpts:
{context}

Answer:"""


def _build_naive_model():
    from sentinel.chat_model import build_chat_model

    return build_chat_model(
        "nebius",
        max_tokens=MODEL_MAX_TOKENS,
        extra_metadata={"eval_mode": "naive"},
    )


def naive_rag_answer(question: str, sop_id: str | None = None) -> dict:
    """Run naive RAG: single Pinecone retrieval + single LLM call. No tools, no iteration.

    The retrieval is intentionally unfiltered (no `regulations=` filter, no edition
    filter) so the comparison highlights what the agentic stack's iterative,
    metadata-aware retrieval adds.
    """
    start = time.time()

    sop_text = ""
    if sop_id:
        sop = load_sop_by_id(sop_id)
        if sop is not None:
            chunks = load_sop_chunks(sop)
            sop_text = "\n\n".join(f"[{c.section}]\n{c.chunk_text}" for c in chunks)

    retrieved = retrieve_regulation_text(question, regulations=None, top_k=NAIVE_TOP_K)
    context = format_regulation_context(retrieved, max_chars=NAIVE_CONTEXT_CHARS)

    sop_block = f"SOP under review ({sop_id}):\n{sop_text}\n\n" if sop_text else ""
    prompt = NAIVE_PROMPT.format(question=question, sop_block=sop_block, context=context)

    model = _build_naive_model()
    response = model.invoke([{"role": "user", "content": prompt}])
    elapsed = time.time() - start

    usage = getattr(response, "usage_metadata", None) or {}
    return {
        "answer": response.content if hasattr(response, "content") else str(response),
        "retrieved_chunks": retrieved,
        "input_tokens": usage.get("input_tokens", 0),
        "output_tokens": usage.get("output_tokens", 0),
        "latency_s": elapsed,
        "model": MODEL,
        "mode": "naive",
    }
