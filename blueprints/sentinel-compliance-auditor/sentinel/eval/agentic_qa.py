"""Agentic Q&A baseline.

Thin wrapper that builds a ReAct agent over the *same* sub-agent tools the
demo uses (`retrieve_regulation`, `search_web`, `read_sop`). For
`sop_compliance` questions, the SOP is loaded and `read_sop` is wired in;
otherwise only retrieval + web search are exposed.
"""
from __future__ import annotations

import time

from sentinel.graph.tools import _build_subagent_model, _build_subagent_tools
from sentinel.retrieval.local import load_sop_by_id, load_sop_chunks

QA_AGENT_PROMPT = """You are a regulatory compliance analyst. Answer the user's question using the available tools.

Available tools:
- `retrieve_regulation(query, regulation)` — semantic search over the regulation knowledge base (HIPAA, SOC 2, GDPR, EU AI Act, NIST AI RMF, SR 11-7). Use the optional `regulation` filter when the question targets a specific framework.
- `search_web(query)` — Tavily search for recent guidance, enforcement actions, or news not in the knowledge base.
- `read_sop()` — only available for SOP-grounded questions; returns the full SOP text.

Rules:
- Every tool call MUST include a non-empty `query` (or appropriate arguments). Never call a tool with empty arguments.
- Issue MULTIPLE retrievals when the question spans multiple regulations or editions — one call per framework. Naive single-shot retrieval is insufficient.
- Cite the regulation and section for every factual claim.
- If the question asks whether a specific SOP complies, end your final answer with a line in this exact form:

  Compliance level: <compliant|partial|gap>

Be specific. If a control is missing, say what's missing. If guidance is recent, cite the source URL."""


def agentic_qa_answer(
    question: str,
    sop_id: str | None = None,
    use_tavily: bool = True,
    recursion_limit: int = 30,
    provider: str = "nebius",
    model_name: str | None = None,
) -> dict:
    """Run the agentic Q&A path: ReAct agent with the demo's sub-agent toolset.

    `provider` swaps the underlying chat model — `"nebius"` (default) uses
    DeepSeek-V4-Pro; `"openai"` uses gpt-5.5. Tools and prompt are identical
    so the comparison isolates the model variable.
    """
    from langgraph.prebuilt import create_react_agent

    sop_text = ""
    resolved_sop_id = sop_id or ""
    sop_title = ""

    if sop_id:
        sop = load_sop_by_id(sop_id)
        if sop is not None:
            fm = sop["frontmatter"]
            resolved_sop_id = fm.get("sop_id", sop_id)
            sop_title = fm.get("title", "")
            chunks = load_sop_chunks(sop)
            sop_text = "\n\n---\n\n".join(f"[{c.section}]\n{c.chunk_text}" for c in chunks)

    tools, _recorded = _build_subagent_tools(
        sop_text=sop_text,
        sop_id=resolved_sop_id,
        sop_title=sop_title,
        use_tavily=use_tavily,
    )
    # Drop tools irrelevant to Q&A eval
    tools = [t for t in tools if getattr(t, "name", "") != "record_finding"]
    if not sop_text:
        tools = [t for t in tools if getattr(t, "name", "") != "read_sop"]

    model = _build_subagent_model(provider=provider, model_name=model_name)
    agent = create_react_agent(model=model, tools=tools, prompt=QA_AGENT_PROMPT, name="qa_agent")

    start = time.time()
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
        config={"recursion_limit": recursion_limit},
    )
    elapsed = time.time() - start

    messages = result.get("messages", [])
    input_tokens = 0
    output_tokens = 0
    tool_calls = 0
    for msg in messages:
        usage = getattr(msg, "usage_metadata", None)
        if usage:
            input_tokens += usage.get("input_tokens", 0)
            output_tokens += usage.get("output_tokens", 0)
        tcalls = getattr(msg, "tool_calls", None) or []
        tool_calls += len(tcalls)

    final = messages[-1] if messages else None
    answer = final.content if final and hasattr(final, "content") else ""

    finish_reason = ""
    rm = getattr(final, "response_metadata", None) or {}
    if isinstance(rm, dict):
        finish_reason = rm.get("finish_reason", "") or rm.get("stop_reason", "")
    answer_str = answer if isinstance(answer, str) else ""
    incomplete = (not answer_str.strip()) or finish_reason == "length"

    return {
        "answer": answer,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "tool_calls": tool_calls,
        "latency_s": elapsed,
        "model": getattr(model, "model_name", ""),
        "mode": f"agentic-{provider}" if provider != "nebius" else "agentic",
        "incomplete": incomplete,
        "finish_reason": finish_reason,
    }
