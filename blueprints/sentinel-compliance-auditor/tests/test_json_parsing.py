"""Regression tests for JSON parsing and enum mapping from sub-agent responses.

These import the real symbols (`_parse_findings_json` from tools.py, the alias
maps and normalizers from models.py) rather than local copies, so the tests
fail when the production logic drifts.
"""
from __future__ import annotations

import json
from types import SimpleNamespace

from sentinel.graph.tools import _parse_findings_json
from sentinel.models import (
    COMPLIANCE_LEVEL_ALIASES,
    SEVERITY_ALIASES,
    ComplianceLevel,
    Severity,
    normalize_compliance_level,
    normalize_severity,
)


class TestComplianceLevelAliases:
    def test_standard_values(self):
        assert COMPLIANCE_LEVEL_ALIASES["compliant"] == "compliant"
        assert COMPLIANCE_LEVEL_ALIASES["partial"] == "partial"
        assert COMPLIANCE_LEVEL_ALIASES["gap"] == "gap"

    def test_info_maps_to_compliant(self):
        assert COMPLIANCE_LEVEL_ALIASES["info"] == "compliant"

    def test_non_compliant_variants_map_to_gap(self):
        assert COMPLIANCE_LEVEL_ALIASES["non-compliant"] == "gap"
        assert COMPLIANCE_LEVEL_ALIASES["non_compliant"] == "gap"
        assert COMPLIANCE_LEVEL_ALIASES["noncompliant"] == "gap"

    def test_normalize_unknown_defaults_to_gap(self):
        assert normalize_compliance_level("unknown") is ComplianceLevel.GAP
        assert normalize_compliance_level("") is ComplianceLevel.GAP

    def test_normalize_strips_and_lowercases(self):
        assert normalize_compliance_level("  Non-Compliant ") is ComplianceLevel.GAP
        assert normalize_compliance_level("COMPLIANT") is ComplianceLevel.COMPLIANT


class TestSeverityAliases:
    def test_standard_values(self):
        for sev in ["critical", "high", "medium", "low", "info"]:
            assert SEVERITY_ALIASES[sev] == sev

    def test_compliance_level_crossover(self):
        assert SEVERITY_ALIASES["compliant"] == "info"
        assert SEVERITY_ALIASES["partial"] == "medium"
        assert SEVERITY_ALIASES["gap"] == "high"

    def test_normalize_unknown_defaults_to_high(self):
        assert normalize_severity("unknown") is Severity.HIGH
        assert normalize_severity("") is Severity.HIGH


def _msg(content):
    """Message-like object the way _parse_findings_json receives them."""
    return SimpleNamespace(content=content)


def _parse(*contents):
    """Run the real extractor over messages and return the parsed array (or None)."""
    raw = _parse_findings_json([_msg(c) for c in contents])
    return None if raw is None else json.loads(raw)


class TestParseFindingsJson:
    def test_clean_json_array(self):
        result = _parse('[{"clause_id": "X", "compliance_level": "gap"}]')
        assert result is not None
        assert len(result) == 1
        assert result[0]["clause_id"] == "X"

    def test_json_with_markdown_fences(self):
        result = _parse('```json\n[{"clause_id": "X"}]\n```')
        assert result is not None
        assert result[0]["clause_id"] == "X"

    def test_code_fence_no_lang_tag(self):
        result = _parse('```\n[{"x": 1}]\n```')
        assert result is not None

    def test_json_with_preceding_text(self):
        result = _parse('Here are the findings:\n[{"clause_id": "X"}]')
        assert result is not None

    def test_trailing_comma_repaired(self):
        result = _parse('[{"clause_id": "X"},]')
        assert result is not None
        assert len(result) == 1

    def test_truncated_array_repaired(self):
        result = _parse('[{"clause_id": "A"}, {"clause_id": "B"')
        assert result is not None
        assert len(result) == 1
        assert result[0]["clause_id"] == "A"

    def test_truncated_after_complete_object(self):
        result = _parse('[{"clause_id": "A"}, {"clause_id": "B"}, {"clau')
        assert result is not None
        assert len(result) == 2

    def test_no_json_returns_none(self):
        assert _parse("I could not produce findings for this SOP.") is None

    def test_empty_array_returns_none(self):
        assert _parse("[]") is None

    def test_empty_messages_returns_none(self):
        assert _parse_findings_json([]) is None

    def test_non_string_content_skipped(self):
        result = _parse_findings_json([
            _msg([{"type": "text", "text": "block content"}]),
            _msg('[{"clause_id": "X"}]'),
        ])
        assert result is not None

    def test_multiple_items(self):
        result = _parse('[{"clause_id": "A"}, {"clause_id": "B"}, {"clause_id": "C"}]')
        assert result is not None
        assert len(result) == 3

    def test_nested_objects(self):
        result = _parse('[{"clause_id": "X", "details": {"sub": "value"}}]')
        assert result is not None
        assert result[0]["details"]["sub"] == "value"

    def test_scans_messages_in_reverse(self):
        """The LAST message containing a findings array wins."""
        result = _parse(
            '[{"clause_id": "OLD"}]',
            "some interleaved tool output",
            '[{"clause_id": "NEW"}]',
        )
        assert result is not None
        assert result[0]["clause_id"] == "NEW"
