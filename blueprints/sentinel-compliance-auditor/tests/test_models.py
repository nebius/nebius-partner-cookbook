"""Regression tests for Pydantic models and enums."""
from __future__ import annotations

import pytest

from sentinel.models import (
    AuditFinding,
    AuditMetrics,
    ComplianceLevel,
    Severity,
    SOPChunk,
    normalize_compliance_level,
    normalize_level,
    normalize_severity,
)


class TestNormalization:
    """Centralized aliases used by the audit pipeline and the eval scorers."""

    def test_compliance_level_enum_with_conservative_default(self):
        assert normalize_compliance_level("Compliant") == ComplianceLevel.COMPLIANT
        assert normalize_compliance_level("info") == ComplianceLevel.COMPLIANT
        assert normalize_compliance_level("non-compliant") == ComplianceLevel.GAP
        assert normalize_compliance_level("non_compliant") == ComplianceLevel.GAP
        assert normalize_compliance_level("garbage") == ComplianceLevel.GAP  # default

    def test_severity_enum_with_conservative_default(self):
        assert normalize_severity("CRITICAL") == Severity.CRITICAL
        assert normalize_severity("gap") == Severity.HIGH       # level->severity alias
        assert normalize_severity("compliant") == Severity.INFO
        assert normalize_severity("garbage") == Severity.HIGH   # default

    def test_level_string_passthrough_for_eval(self):
        assert normalize_level("Compliant") == "compliant"
        assert normalize_level("noncompliant") == "gap"
        assert normalize_level("unexpected") == "unexpected"    # passes unknown through


class TestComplianceLevel:
    def test_values(self):
        assert ComplianceLevel.COMPLIANT.value == "compliant"
        assert ComplianceLevel.PARTIAL.value == "partial"
        assert ComplianceLevel.GAP.value == "gap"

    def test_from_string(self):
        assert ComplianceLevel("compliant") == ComplianceLevel.COMPLIANT
        assert ComplianceLevel("gap") == ComplianceLevel.GAP

    def test_invalid_raises(self):
        with pytest.raises(ValueError):
            ComplianceLevel("invalid")


class TestSeverity:
    def test_values(self):
        assert Severity.CRITICAL.value == "critical"
        assert Severity.HIGH.value == "high"
        assert Severity.MEDIUM.value == "medium"
        assert Severity.LOW.value == "low"
        assert Severity.INFO.value == "info"

    def test_from_string(self):
        assert Severity("critical") == Severity.CRITICAL
        assert Severity("info") == Severity.INFO


class TestAuditFinding:
    def test_required_fields(self, compliant_finding):
        assert compliant_finding.clause_id == "HIPAA-TECH-1"
        assert compliant_finding.compliance_level == ComplianceLevel.COMPLIANT
        assert compliant_finding.severity == Severity.INFO

    def test_optional_defaults(self):
        f = AuditFinding(
            clause_id="X", clause_title="X", regulation="X",
            sop_id="X", sop_title="X", business_unit="X",
            compliance_level=ComplianceLevel.GAP, severity=Severity.HIGH,
        )
        assert f.evidence_quote == ""
        assert f.gap_description == ""
        assert f.remediation == ""
        assert f.reasoning == ""

    def test_model_dump_roundtrip(self, gap_finding):
        data = gap_finding.model_dump()
        restored = AuditFinding(**data)
        assert restored == gap_finding

    def test_json_serialization(self, gap_finding):
        json_str = gap_finding.model_dump_json()
        assert '"gap"' in json_str
        assert '"high"' in json_str


class TestSOPChunk:
    def test_defaults(self):
        chunk = SOPChunk(sop_id="X", title="T", business_unit="BU", chunk_text="text")
        assert chunk.section == ""
        assert chunk.page_estimate == 0
        assert chunk.score == 0.0


class TestAuditMetrics:
    def test_all_defaults_zero(self):
        m = AuditMetrics()
        assert m.total_findings == 0
        assert m.total_tokens == 0
        assert m.total_cost == 0.0
        assert m.avg_latency_per_cell == 0.0
