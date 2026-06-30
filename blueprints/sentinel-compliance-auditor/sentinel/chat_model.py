"""Factory for the chat-model instances used across Sentinel.

Centralizes the provider branching (Nebius vs OpenAI), credentials, base URL,
and LangSmith metadata tagging that were previously duplicated across
``graph/agent.py``, ``graph/tools.py``, ``graph/naive_agent.py``, and the
``eval/*`` modules. The Nebius provider uses ``langchain_nebius.ChatNebius``
(the official integration, a ``BaseChatOpenAI`` subclass) and the OpenAI
provider uses ``ChatOpenAI``; both are imported lazily so this module stays
cheap to import in the LangGraph Cloud container (see CLAUDE.md on lazy
imports).
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
    extra_body: dict | None = None,
):
    """Construct a chat-model client for the given provider.

    Returns a ``ChatNebius`` for the ``"nebius"`` provider and a ``ChatOpenAI``
    for ``"openai"``. Both are ``BaseChatOpenAI`` subclasses, so tool calling,
    ``stream_usage``, ``max_tokens``, and ``extra_body`` behave identically; the
    difference is ``ChatNebius._get_ls_params`` natively reports
    ``ls_provider="nebius"`` (used for harness-profile resolution and trace
    provenance) rather than relying on the faked metadata tag.

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
        extra_body: explicit request-body extras (e.g.
            ``{"chat_template_kwargs": {"thinking": False}}`` to disable a
            model's reasoning). Mutually exclusive with ``reasoning=True``.
    """
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
    if extra_body is not None:
        kwargs["extra_body"] = extra_body
    elif reasoning and not is_openai and REASONING_EFFORT != "off":
        kwargs["extra_body"] = {
            "chat_template_kwargs": {"thinking": True, "reasoning_effort": REASONING_EFFORT},
        }

    if is_openai:
        # OpenAI reasoning models reject `max_tokens`; ChatOpenAI remaps it to
        # `max_completion_tokens`, so the OpenAI agents must stay on ChatOpenAI.
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(**kwargs)

    from langchain_nebius import ChatNebius

    return ChatNebius(**kwargs)
