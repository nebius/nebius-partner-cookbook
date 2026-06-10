"""LangSmith trace propagation into sub-agent worker threads.

Trace context is contextvars-based and dies at the ThreadPoolExecutor
boundary; the audit tools pass their RunnableConfig callbacks into
subagent.invoke explicitly. These tests lock in the three contracts:
the injected `config` param stays out of the model-visible tool schema,
the parent callback manager is copied (not mutated) with parentage
preserved, and validate_run excludes tagged sub-agent LLM runs from
outer-agent token totals.
"""
from __future__ import annotations

import uuid
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from langchain_core.callbacks import CallbackManager, UsageMetadataCallbackHandler

from sentinel.graph.tools import _subagent_invoke_config, build_tools


class TestToolSchemas:
    def test_config_param_not_exposed_to_model(self):
        tools = {t.name: t for t in build_tools(use_tavily=False)}
        assert set(tools["audit_single_sop"].args) == {"sop_id"}
        assert set(tools["audit_sops"].args) == {"sop_ids"}
        assert set(tools["audit_all_sops"].args) == set()


class TestSubagentInvokeConfig:
    def test_manager_copied_with_parentage_preserved(self):
        parent_id = uuid.uuid4()
        sentinel_handler = MagicMock()
        parent = CallbackManager(
            handlers=[sentinel_handler],
            inheritable_handlers=[sentinel_handler],
            parent_run_id=parent_id,
        )
        usage_cb = UsageMetadataCallbackHandler()

        cfg = _subagent_invoke_config(usage_cb, parent)

        assert cfg["recursion_limit"] == 120
        child = cfg["callbacks"]
        assert child is not parent
        assert child.parent_run_id == parent_id
        assert sentinel_handler in child.handlers
        assert usage_cb in child.handlers
        # The shared parent must NOT gain this sub-agent's usage handler —
        # sibling workers reuse it and their token counts would bleed together.
        assert usage_cb not in parent.handlers

    def test_list_and_none_forms(self):
        usage_cb = UsageMetadataCallbackHandler()
        other = MagicMock()
        assert _subagent_invoke_config(usage_cb, [other])["callbacks"] == [usage_cb, other]
        assert _subagent_invoke_config(usage_cb, None)["callbacks"] == [usage_cb]


class TestImplPropagation:
    def test_parent_callbacks_reach_subagent_invoke(self):
        from sentinel.graph.tools import _audit_single_sop_impl
        from sentinel.retrieval.local import list_all_sops

        parent_id = uuid.uuid4()
        parent = CallbackManager(handlers=[], parent_run_id=parent_id)
        captured = {}

        def fake_create_agent(model=None, tools=None, system_prompt=None, name=None, **kw):
            agent = MagicMock()

            def invoke(payload, config=None, **kwargs):
                captured["config"] = config
                return {"messages": []}

            agent.invoke.side_effect = invoke
            return agent

        sop_id = list_all_sops()[0]["sop_id"]
        with patch("sentinel.graph.tools._build_subagent_model", return_value=MagicMock()), \
             patch("langchain.agents.create_agent", fake_create_agent):
            _audit_single_sop_impl(sop_id, parent_callbacks=parent)

        callbacks = captured["config"]["callbacks"]
        assert isinstance(callbacks, CallbackManager)
        assert callbacks.parent_run_id == parent_id
        assert any(isinstance(h, UsageMetadataCallbackHandler) for h in callbacks.handlers)


class TestValidateRunExclusion:
    def _run(self, metadata):
        return SimpleNamespace(extra={"metadata": metadata}, prompt_tokens=100, completion_tokens=10)

    def test_subagent_runs_detected(self):
        from scripts.validate_run import _is_subagent_llm_run

        assert _is_subagent_llm_run(self._run({"sentinel_subagent": True}))
        assert not _is_subagent_llm_run(self._run({"ls_model_name": "x"}))
        assert not _is_subagent_llm_run(SimpleNamespace(extra=None))
