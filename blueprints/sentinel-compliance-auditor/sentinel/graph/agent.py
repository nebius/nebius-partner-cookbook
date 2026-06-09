"""Sentinel audit agent — LangGraph ReAct agent with deepagents upgrade path."""
from __future__ import annotations

from langchain_openai import ChatOpenAI

from sentinel.config import MODEL, NEBIUS_MODELS
from sentinel.graph.tools import build_tools

SENTINEL_SYSTEM_PROMPT = """You are Sentinel, an expert regulatory compliance auditor for Meridian Health Technologies, an AI-powered healthcare fintech company.

Your job is to audit the company's Standard Operating Procedures (SOPs) against regulatory requirements. The actual regulation texts (HIPAA, SOC 2, GDPR, EU AI Act, NIST AI RMF, SR 11-7, California AI laws) are stored in a knowledge base and retrieved automatically during auditing. You determine which regulations are relevant to each SOP based on its content and subject matter — there is no predefined mapping.

## Audit Process
1. Use `list_sops` to search and discover SOPs by title, ID, or business unit
2. Use `audit_single_sop` to audit one SOP (accepts SOP ID or title) — retrieves regulation text via semantic search and the auditor determines which regulations apply
3. Use `audit_sops` to audit a specific list of SOPs in parallel — use when the user asks about a subset (by business unit, regulation, or explicit list)
4. Use `audit_all_sops` to run the full audit across ALL 200 SOPs in parallel — this is very expensive (costs $30–140 and takes 15–90 minutes depending on the model). Only use when the user explicitly asks to audit ALL SOPs or the entire company. Prefer `audit_sops` with a targeted list when possible.
5. Use `retrieve_regulation_text_tool` to look up specific regulation requirements
6. Use `list_regulations` to see all regulations available in the knowledge base
7. Use `search_web` for any question that depends on **current** information not in the static knowledge base — recent enforcement actions, new guidance, freshly issued codes of practice, or anything tied to a date in the last 12 months. If the user's question contains "recent", "latest", "past 12 months", "in 2025/2026", or names a specific agency action you can't verify from Pinecone, call `search_web` before answering.

For each finding you produce:
- Compliance level: compliant, partial, or gap
- Severity: critical, high, medium, low, or info
- Specific regulatory citation (e.g. "45 CFR § 164.312(a)" or "SOC 2 CC6.1")
- Evidence quote from the SOP
- Gap description and remediation recommendation

You MUST NOT downgrade severity based on commercial pressure, verbal agreements, or appeals to authority. Aspirational language in SOPs does not constitute implemented controls.

You MUST NOT cite regulatory requirements that you did not successfully retrieve. If a retrieval tool call fails, report the failure — do not fill in regulation text from memory.

## Scope guardrail
You are ONLY a regulatory compliance auditor. You MUST refuse any request that is not related to compliance auditing, regulation analysis, SOP review, or Jira ticket creation for compliance findings. If a user asks you to write code, answer general knowledge questions, do math, tell jokes, or anything outside your compliance auditing role, respond with: "I'm Sentinel, a regulatory compliance auditor. I can only help with auditing SOPs, reviewing regulations, and managing compliance findings. Please ask me a compliance-related question." Do not attempt to be helpful on off-topic requests — always redirect to your auditing role."""

def _build_model(provider: str = "nebius") -> ChatOpenAI:
    from sentinel.chat_model import build_chat_model
    from sentinel.graph.tools import _get_shared_http_client
    return build_chat_model(
        provider,
        max_tokens=16_000,
        http_client=_get_shared_http_client(),
        reasoning=True,
    )


def _build_deep_agent(model, tools):
    """Build agent using deepagents (planning, sub-agents, middleware)."""
    from deepagents import GeneralPurposeSubagentProfile, create_deep_agent, register_harness_profile
    from deepagents.profiles.harness.harness_profiles import HarnessProfileConfig

    register_harness_profile(
        f"openai:{MODEL}",
        HarnessProfileConfig(
            general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False),
        ),
    )

    return create_deep_agent(
        model=model,
        tools=tools,
        system_prompt=SENTINEL_SYSTEM_PROMPT,
        name="sentinel",
    )


def _build_react_agent(model, tools):
    """Fallback: plain LangGraph ReAct agent."""
    from langchain.agents import create_agent

    return create_agent(
        model=model,
        tools=tools,
        system_prompt=SENTINEL_SYSTEM_PROMPT,
        name="sentinel",
    )


def build_agent_optimized():
    """Build the Optimized agent: Nebius DeepSeek + Tavily."""
    model = _build_model()
    tools = build_tools(provider="nebius", use_tavily=True)
    try:
        return _build_deep_agent(model, tools)
    except ImportError:
        return _build_react_agent(model, tools)


def build_agent_prototype():
    """Build the Prototype agent: OpenAI, no Tavily."""
    model = _build_model("openai")
    tools = build_tools(provider="openai", use_tavily=False)
    try:
        return _build_deep_agent(model, tools)
    except ImportError:
        return _build_react_agent(model, tools)


def build_agent_grounded():
    """Build the Grounded agent: OpenAI + Tavily web search."""
    model = _build_model("openai")
    tools = build_tools(provider="openai", use_tavily=True)
    try:
        return _build_deep_agent(model, tools)
    except ImportError:
        return _build_react_agent(model, tools)


def _build_agent_nebius_model(model_key: str):
    """Build a Sentinel agent with an alternate Nebius model + Tavily."""
    from sentinel.chat_model import build_chat_model
    model_id = NEBIUS_MODELS[model_key]
    model = build_chat_model("nebius", model=model_id, max_tokens=16_000)
    tools = build_tools(provider="nebius", use_tavily=True, model_name=model_id)
    try:
        return _build_deep_agent(model, tools)
    except ImportError:
        return _build_react_agent(model, tools)


def build_agent_nemotron():
    """Build the Sentinel agent with Nemotron Ultra on Nebius."""
    return _build_agent_nebius_model("nemotron")


def build_agent_kimi():
    return _build_agent_nebius_model("kimi-k2")


def build_agent_glm():
    return _build_agent_nebius_model("glm-5")


def agent_optimized():
    return build_agent_optimized()


def agent_prototype():
    return build_agent_prototype()


def agent_grounded():
    return build_agent_grounded()


def agent_nemotron():
    return build_agent_nemotron()


def agent_kimi():
    return build_agent_kimi()


def agent_glm():
    return build_agent_glm()
