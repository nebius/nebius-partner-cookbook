"""Regression: partial findings after a sub-agent crash must be flagged truncated.

When a sub-agent raises but `record_finding` already captured findings, those
partial results were being reported as a clean audit because `truncated` was
set True on the exception path and then unconditionally reset to False before
the (empty) truncation-detection loop.
"""
from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import sentinel.graph.tools as tools


def _fake_sop():
    return {
        "frontmatter": {
            "sop_id": "SOP-ISEC-001",
            "title": "MFA Enforcement",
            "business_unit": "Information Security",
        }
    }


def _recorded_finding():
    return {
        "requirement_id": "HIPAA-164.312(a)",
        "requirement_title": "Access Control",
        "regulation": "HIPAA",
        "compliance_level": "gap",
        "severity": "high",
        "evidence_quote": "",
        "gap_description": "No MFA enforced",
        "remediation": "Require MFA",
        "reasoning": "",
    }


def test_crash_with_recorded_findings_is_marked_partial():
    """A sub-agent exception with recorded findings surfaces them flagged PARTIAL."""
    chunk = SimpleNamespace(section="Body", chunk_text="MFA is optional.")
    recorded = [_recorded_finding()]

    crashing_agent = MagicMock()
    crashing_agent.invoke.side_effect = RuntimeError("sub-agent boom")

    with patch("sentinel.retrieval.local.load_sop_by_id", return_value=_fake_sop()), \
         patch("sentinel.retrieval.local.load_sop_chunks", return_value=[chunk]), \
         patch.object(tools, "_build_subagent_tools", return_value=([], recorded)), \
         patch.object(tools, "_build_subagent_model", return_value=MagicMock()), \
         patch("langchain.agents.create_agent", return_value=crashing_agent):
        result = tools._audit_single_sop_impl("SOP-ISEC-001")

    # The partial finding is surfaced...
    assert len(result.findings) == 1
    assert result.findings[0].clause_id == "HIPAA-164.312(a)"
    # ...and explicitly flagged as a sub-agent-limit partial, NOT a clean audit.
    assert "[PARTIAL — sub-agent hit limit]" in result.summary
    assert "[truncated]" not in result.summary  # the partial tag supersedes
