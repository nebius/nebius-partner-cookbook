"""Factory for the ChatOpenAI instances used across Sentinel.

Centralizes the provider branching (Nebius vs OpenAI), credentials, base URL,
and LangSmith metadata tagging that were previously duplicated across
``graph/agent.py``, ``graph/tools.py``, ``graph/naive_agent.py``, and the
``eval/*`` modules. ``ChatOpenAI`` is imported lazily so this module stays cheap
to import in the LangGraph Cloud container (see CLAUDE.md on lazy imports).
"""
from __future__ import annotations


def build_chat_model(
    provider: str = "nebius",
    model: str | None = None,
    *,
    temperature: float = 0.1,
    max_tokens: int | None = None,
    stream_usage: bool = True,
    http_client=None,
    reasoning: bool = False,
    extra_metadata: dict | None = None,
):
    """Construct a ``ChatOpenAI`` client for the given provider.

    Args:
        provider: ``"openai"`` or ``"nebius"`` (default) — selects credentials
            and base URL.
        model: model id; defaults to ``OPENAI_MODEL`` / ``MODEL`` for the provider.
        temperature: sampling temperature.
        max_tokens: omitted from the request entirely when ``None``.
        stream_usage: forwards ``stream_options: {include_usage: true}`` so
            custom base_url providers populate ``usage_metadata`` (see CLAUDE.md).
        http_client: pass a shared ``httpx.Client`` to enable connection pooling;
            omitted when ``None``.
        reasoning: enable Nebius thinking / ``reasoning_effort`` via ``extra_body``
            (honors ``REASONING_EFFORT``; never applied to the openai provider).
        extra_metadata: merged into the LangSmith metadata dict.
    """
    from langchain_openai import ChatOpenAI
    from sentinel.config import (
        MODEL,
        NEBIUS_API_KEY,
        NEBIUS_BASE_URL,
        OPENAI_API_KEY,
        OPENAI_MODEL,
        REASONING_EFFORT,
    )

    is_openai = provider == "openai"
    name = model or (OPENAI_MODEL if is_openai else MODEL)

    metadata = {
        "ls_provider": "openai" if is_openai else "nebius",
        "ls_model_name": name,
    }
    if extra_metadata:
        metadata.update(extra_metadata)

    kwargs: dict = {
        "model": name,
        "api_key": OPENAI_API_KEY if is_openai else NEBIUS_API_KEY,
        "temperature": temperature,
        "stream_usage": stream_usage,
        "metadata": metadata,
    }
    if not is_openai:
        kwargs["base_url"] = NEBIUS_BASE_URL
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens
    if http_client is not None:
        kwargs["http_client"] = http_client
    if reasoning and not is_openai and REASONING_EFFORT != "off":
        kwargs["extra_body"] = {
            "chat_template_kwargs": {"thinking": True, "reasoning_effort": REASONING_EFFORT},
        }
    return ChatOpenAI(**kwargs)
