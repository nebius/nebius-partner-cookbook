"""Jira actuation: ticket field building, the batch tool's handling of
LLM-supplied JSON, and the REST client (httpx mocked throughout — no network).
"""
from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import httpx
import pytest

from sentinel.actuation.jira_client import (
    SEVERITY_TO_PRIORITY,
    JiraClient,
    JiraError,
    _plain_text_to_adf,
)
from sentinel.graph.tools import (
    _build_jira_issue_fields,
    _render_ticket_description,
    _slug,
    create_jira_ticket,
    create_jira_tickets,
)

CFG = {"base_url": "https://x.atlassian.net", "email": "e@x.io",
       "api_token": "tok", "project_key": "SENT", "issue_type": "Task"}


class TestSlug:
    def test_basic(self):
        assert _slug("SOC 2") == "soc-2"
        assert _slug("HIPAA §164.312(a)") == "hipaa-164-312-a"
        assert _slug("SOP-ISEC-008") == "sop-isec-008"

    def test_empty_and_symbols(self):
        assert _slug("") == ""
        assert _slug("___") == ""


class TestBuildJiraIssueFields:
    def _build(self, severity="high"):
        return _build_jira_issue_fields(
            sop_id="SOP-ISEC-008", clause_id="HIPAA-164.312(a)",
            clause_title="Access Control", regulation="HIPAA",
            severity=severity, gap_description="No MFA",
            remediation="Add MFA", evidence_quote="quote", reasoning="why",
        )

    def test_summary_format(self):
        summary, _, _, _ = self._build()
        assert summary == "[HIGH] HIPAA-164.312(a): Access Control (SOP-ISEC-008)"

    def test_labels(self):
        _, labels, _, _ = self._build()
        assert set(labels) == {"sentinel", "compliance-finding", "sev-high", "hipaa", "sop-isec-008"}

    def test_priority_mapping(self):
        for sev, prio in SEVERITY_TO_PRIORITY.items():
            _, _, _, priority = self._build(severity=sev)
            assert priority == prio

    def test_unknown_severity_falls_back_to_medium(self):
        summary, labels, _, priority = self._build(severity="bananas")
        assert priority == "Medium"
        assert "[MEDIUM]" in summary
        assert "sev-medium" in labels

    def test_description_sections(self):
        _, _, description, _ = self._build()
        for fragment in ["SOP: SOP-ISEC-008", "Regulation: HIPAA", "Gap:", "Recommended remediation:", "Reasoning:", "Sentinel"]:
            assert fragment in description

    def test_description_omits_empty_optionals(self):
        desc = _render_ticket_description(
            sop_id="S", clause_id="C", clause_title="T", regulation="R",
            severity="high", gap_description="g", remediation="",
            evidence_quote="", reasoning="",
        )
        assert "Recommended remediation" not in desc
        assert "Evidence" not in desc


class TestCreateJiraTicketTool:
    ARGS = {
        "sop_id": "SOP-ISEC-008", "clause_id": "CC6.1", "clause_title": "Access",
        "regulation": "SOC 2", "severity": "high", "gap_description": "No MFA",
    }

    def test_unconfigured_reports_missing_vars(self):
        with patch("sentinel.graph.tools._jira_config", return_value=({}, ["JIRA_BASE_URL"])):
            out = create_jira_ticket.invoke(self.ARGS)
        assert "Jira not configured" in out
        assert "JIRA_BASE_URL" in out

    def test_success_returns_key_and_url(self):
        client = MagicMock()
        client.create_issue.return_value = {"key": "SENT-42", "url": "https://x/browse/SENT-42"}
        with patch("sentinel.graph.tools._jira_config", return_value=(CFG, [])), \
             patch("sentinel.graph.tools._make_jira_client", return_value=client):
            out = create_jira_ticket.invoke(self.ARGS)
        assert "SENT-42" in out
        client.close.assert_called_once()

    def test_client_error_reported_not_raised(self):
        client = MagicMock()
        client.create_issue.side_effect = JiraError("create_issue failed: HTTP 400 — priority invalid")
        with patch("sentinel.graph.tools._jira_config", return_value=(CFG, [])), \
             patch("sentinel.graph.tools._make_jira_client", return_value=client):
            out = create_jira_ticket.invoke(self.ARGS)
        assert "Jira ticket creation failed" in out
        assert "priority invalid" in out


class TestCreateJiraTicketsBatch:
    def _invoke(self, findings_json, client=None):
        client = client or MagicMock(
            create_issue=MagicMock(return_value={"key": "SENT-1", "url": "u"})
        )
        with patch("sentinel.graph.tools._jira_config", return_value=(CFG, [])), \
             patch("sentinel.graph.tools._make_jira_client", return_value=client):
            return create_jira_tickets.invoke({"findings_json": findings_json}), client

    def test_invalid_json(self):
        out, _ = self._invoke("not json at all {")
        assert "Invalid JSON" in out

    def test_non_array(self):
        out, _ = self._invoke('{"sop_id": "S"}')
        assert "Expected a JSON array" in out

    def test_empty_array(self):
        out, _ = self._invoke("[]")
        assert "No findings provided" in out

    def test_creates_one_ticket_per_finding(self):
        findings = [
            {"sop_id": "SOP-A-001", "clause_id": "CC6.1", "clause_title": "T",
             "regulation": "SOC 2", "severity": "high", "gap_description": "g"},
            {"sop_id": "SOP-B-001", "clause_id": "HIPAA-164.312", "clause_title": "T",
             "regulation": "HIPAA", "severity": "medium", "gap_description": "g"},
        ]
        out, client = self._invoke(json.dumps(findings))
        assert "Created 2 Jira ticket(s), 0 failed" in out
        assert client.create_issue.call_count == 2
        client.close.assert_called_once()

    def test_non_dict_element_lands_in_failed_list(self):
        """Regression: a string element used to raise an uncaught AttributeError."""
        findings = json.dumps([
            "just a string",
            {"sop_id": "SOP-A-001", "clause_id": "CC6.1", "clause_title": "T",
             "regulation": "SOC 2", "severity": "high", "gap_description": "g"},
        ])
        out, client = self._invoke(findings)
        assert "Created 1 Jira ticket(s), 1 failed" in out
        assert "expected an object, got str" in out
        assert client.create_issue.call_count == 1

    def test_per_ticket_failure_does_not_abort_batch(self):
        client = MagicMock()
        client.create_issue.side_effect = [JiraError("HTTP 400"), {"key": "SENT-2", "url": "u"}]
        findings = json.dumps([
            {"sop_id": "SOP-A-001", "clause_id": "C1", "clause_title": "T",
             "regulation": "SOC 2", "severity": "high", "gap_description": "g"},
            {"sop_id": "SOP-B-001", "clause_id": "C2", "clause_title": "T",
             "regulation": "HIPAA", "severity": "high", "gap_description": "g"},
        ])
        out, client = self._invoke(findings, client=client)
        assert "Created 1 Jira ticket(s), 1 failed" in out
        client.close.assert_called_once()


def _client_with_response(response: httpx.Response) -> JiraClient:
    client = JiraClient(**{k: v for k, v in CFG.items() if k != "issue_type"})
    client._http = MagicMock()
    client._http.post.return_value = response
    return client


def _response(status: int, body: dict) -> httpx.Response:
    req = httpx.Request("POST", "https://x.atlassian.net/rest/api/3/issue")
    return httpx.Response(status, request=req, json=body)


class TestJiraClient:
    def test_create_issue_posts_expected_fields(self):
        client = _client_with_response(_response(201, {"key": "SENT-7"}))
        result = client.create_issue(
            summary="Line one\nline two", description="para1\n\npara2",
            labels=["sentinel"], priority="High",
        )
        assert result == {"key": "SENT-7", "url": "https://x.atlassian.net/browse/SENT-7"}
        fields = client._http.post.call_args.kwargs["json"]["fields"]
        assert fields["summary"] == "Line one line two"  # newlines collapsed
        assert fields["project"] == {"key": "SENT"}
        assert fields["priority"] == {"name": "High"}
        assert fields["description"]["type"] == "doc"

    def test_long_summary_truncated_to_240(self):
        client = _client_with_response(_response(201, {"key": "SENT-7"}))
        client.create_issue(summary="x" * 500, description="d", labels=[])
        fields = client._http.post.call_args.kwargs["json"]["fields"]
        assert len(fields["summary"]) == 240

    def test_error_body_surfaced_in_jira_error(self):
        client = _client_with_response(
            _response(400, {"errors": {"priority": "Priority name 'Sev1' is not valid"}})
        )
        with pytest.raises(JiraError) as exc:
            client.create_issue(summary="s", description="d", labels=[])
        assert "HTTP 400" in str(exc.value)
        assert "Sev1" in str(exc.value)

    def test_list_issues_returns_issue_array(self):
        client = _client_with_response(_response(200, {"issues": [{"key": "SENT-1"}]}))
        issues = client.list_issues(jql="labels = sentinel")
        assert issues == [{"key": "SENT-1"}]

    def test_adf_paragraphs_per_blank_line_block(self):
        adf = _plain_text_to_adf("first\n\nsecond block")
        assert adf["type"] == "doc"
        assert len(adf["content"]) == 2
        assert adf["content"][1]["content"][0]["text"] == "second block"
