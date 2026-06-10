"""The benchmark pipeline: classification, aggregation, and the emit↔parse
round-trip between the audit tools and scripts/validate_run.py.

The round-trip test runs the real _audit_single_sop_impl (only the LLM agent
is faked — it records findings through the real record_finding tool), feeds
the real _audit_all_sops_impl summary into the real parse_full_findings, and
asserts the findings classify back out. If either side's format drifts, this
breaks — which is the point: validate_run produces the headline benchmark
numbers.
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scripts.validate_run import (
    classify_regulation,
    compute_metrics,
    macro_f1_for,
    parse_full_findings,
    worst_level,
)
from sentinel.graph.tools import _audit_all_sops_impl, _audit_single_sop_impl


class TestClassifyRegulation:
    @pytest.mark.parametrize("criterion,expected", [
        ("HIPAA-164.312(a)", "HIPAA"),
        ("SOC2-CC6.1", "SOC 2"),
        ("SOC 2 CC7.2", "SOC 2"),
        ("GDPR-Art32", "GDPR"),
        ("EU AI Act Art 9", "EU AI Act"),
        ("NIST-AI-RMF GOVERN 1.1", "NIST AI RMF"),
        ("NIST AI RMF MAP 2.3", "NIST AI RMF"),
        ("GOVERN 1.1", "NIST AI RMF"),
        ("MAP-2.3", "NIST AI RMF"),
        ("MEASURE 4.2", "NIST AI RMF"),
        ("SR 11-7 Section V", "SR 11-7"),
        # bare clause IDs without a framework prefix
        ("CC6.1", "SOC 2"),
        ("CC 7.2", "SOC 2"),
        ("164.312(a)(2)(iv)", "HIPAA"),
        ("§ 164.308(a)(1)", "HIPAA"),
        ("160.103", "HIPAA"),
        # must NOT classify
        ("NIST SP 800-53 AC-2", None),
        ("NIST 800-63B", None),
        ("NIST CSF PR.AC-1", None),
        ("Art. 13", None),  # GDPR vs EU AI Act is ambiguous without context
        ("California SB 53", None),
        ("MANAGEMENT review", None),
    ])
    def test_classification(self, criterion, expected):
        assert classify_regulation(criterion) == expected


class TestWorstLevel:
    def test_gap_dominates(self):
        assert worst_level(["compliant", "gap", "partial"]) == "gap"

    def test_partial_beats_compliant(self):
        assert worst_level(["compliant", "partial"]) == "partial"

    def test_empty_defaults_compliant(self):
        assert worst_level([]) == "compliant"


class TestComputeMetricsWrapper:
    GT = {
        ("SOP-A", "HIPAA"): "gap",
        ("SOP-A", "SOC 2"): "partial",
        ("SOP-B", "HIPAA"): "compliant",
    }

    def test_mismatch_shape_and_directions(self):
        predicted = {
            ("SOP-A", "HIPAA"): "gap",        # match
            ("SOP-A", "SOC 2"): "compliant",  # too lenient → false negative
            ("SOP-C", "GDPR"): "gap",         # extra
        }
        m = compute_metrics(self.GT, predicted)
        assert m["matched"] == 1
        assert m["total"] == 2
        assert m["false_negatives"] == 1
        assert m["false_positives"] == 0
        assert m["missing_in_run"] == [("SOP-B", "HIPAA")]
        assert m["extra_in_run"] == 1
        mm = m["mismatches"][0]
        assert mm["sop_id"] == "SOP-A"
        assert mm["regulation"] == "SOC 2"
        assert mm["expected"] == "partial"
        assert mm["predicted"] == "compliant"

    def test_macro_f1_perfect_prediction(self):
        m = compute_metrics(self.GT, dict(self.GT))
        assert macro_f1_for(m["confusion"]) == pytest.approx(1.0)


# ── emit ↔ parse round-trip ──────────────────────────────────────────────────

def _recording_agent_factory(findings):
    """A create_agent stand-in whose invoke records `findings` through the
    real record_finding tool it was handed."""
    def create_agent(model=None, tools=None, system_prompt=None, name=None, **kw):
        record = next(t for t in tools if t.name == "record_finding")
        agent = MagicMock()

        def invoke(payload, config=None, **kwargs):
            for f in findings:
                record.invoke(f)
            return {"messages": []}

        agent.invoke.side_effect = invoke
        return agent
    return create_agent


def _silent_agent_factory():
    """An agent that finishes without recording anything → no_findings path."""
    def create_agent(model=None, tools=None, system_prompt=None, name=None, **kw):
        agent = MagicMock()
        agent.invoke.return_value = {"messages": []}
        return agent
    return create_agent


def _run_impl(sop_id, agent_factory):
    with patch("sentinel.graph.tools._build_subagent_model", return_value=MagicMock()), \
         patch("langchain.agents.create_agent", agent_factory):
        return _audit_single_sop_impl(sop_id)


@pytest.fixture(scope="module")
def real_sop_ids():
    from sentinel.retrieval.local import list_all_sops
    sops = list_all_sops()
    return sops[0]["sop_id"], sops[1]["sop_id"]


class TestEmitParseRoundTrip:
    def test_full_pipeline(self, real_sop_ids):
        sop_ok, sop_silent = real_sop_ids

        findings = [
            {"requirement_id": "HIPAA-164.312(a)(2)(iv)", "requirement_title": "Encryption",
             "regulation": "HIPAA", "compliance_level": "gap", "severity": "high",
             "reasoning": "r", "gap_description": "No encryption at rest"},
            {"requirement_id": "HIPAA-164.308(a)(1)", "requirement_title": "Risk Analysis",
             "regulation": "HIPAA", "compliance_level": "compliant", "severity": "info",
             "reasoning": "r"},
            {"requirement_id": "SOC2-CC6.1", "requirement_title": "Logical Access",
             "regulation": "SOC 2", "compliance_level": "compliant", "severity": "info",
             "reasoning": "r"},
        ]

        result_ok = _run_impl(sop_ok, _recording_agent_factory(findings))
        assert result_ok.status == "ok"
        assert len(result_ok.findings) == 3

        result_silent = _run_impl(sop_silent, _silent_agent_factory())
        assert result_silent.status == "no_findings"

        results = {sop_ok: result_ok, sop_silent: result_silent}

        def run_one(sop_id):
            if sop_id == "SOP-ZZ-999":
                raise RuntimeError("504 gateway timeout")
            return results[sop_id]

        listed = [
            {"sop_id": sop_ok, "title": "A", "business_unit": "bu", "regulations": []},
            {"sop_id": sop_silent, "title": "B", "business_unit": "bu", "regulations": []},
            {"sop_id": "SOP-ZZ-999", "title": "C", "business_unit": "bu", "regulations": []},
        ]
        with patch("sentinel.retrieval.local.list_all_sops", return_value=listed):
            summary = _audit_all_sops_impl(run_one, max_workers=2)

        assert "Audit complete: 3 findings across 3 SOPs" in summary
        assert "Failed after retries: 2" in summary  # no_findings + error

        # Now the real parser over the real emitter output.
        parsed, total_parsed, failed_sops, error_sops = parse_full_findings(summary)
        assert total_parsed == 3
        assert failed_sops == [sop_silent]
        assert error_sops == ["SOP-ZZ-999"]

        predicted = {key: worst_level(levels) for key, levels in parsed.items()}
        assert predicted[(sop_ok, "HIPAA")] == "gap"      # worst of gap+compliant
        assert predicted[(sop_ok, "SOC 2")] == "compliant"

    def test_impl_exception_format_parses_as_error(self, real_sop_ids):
        """The sub-agent-crash format ('FAILED: {id} — ...') must be counted
        by the error regex — it appears verbatim in the batch summary."""
        sop_ok, _ = real_sop_ids

        def create_agent(model=None, tools=None, system_prompt=None, name=None, **kw):
            agent = MagicMock()
            agent.invoke.side_effect = RuntimeError("nebius 504")
            return agent

        result = _run_impl(sop_ok, create_agent)
        assert result.status == "failed"

        _, _, _, error_sops = parse_full_findings(result.summary)
        assert error_sops == [sop_ok]
