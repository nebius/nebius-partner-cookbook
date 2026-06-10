"""Shared fixtures for Sentinel regression tests."""
from __future__ import annotations

import os

# Tests are hermetic — nothing calls an external API. Dummy credentials let
# modules that validate keys at import/construction time load in CI where no
# .env exists: ui.server's fail-fast UI_API_KEY gate, and ChatOpenAI's client
# construction in the graph smoke test. setdefault keeps real values when the
# shell already has them. Must run before any sentinel/ui import (config
# freezes env at import time).
for _var in ("NEBIUS_API_KEY", "OPENAI_API_KEY", "UI_API_KEY"):
    if not os.environ.get(_var):  # absent OR empty — both break construction
        os.environ[_var] = "test-key"

import pytest

from sentinel.models import AuditFinding, ComplianceLevel, Severity


@pytest.fixture
def compliant_finding():
    return AuditFinding(
        clause_id="HIPAA-TECH-1",
        clause_title="Access Control",
        regulation="HIPAA Security Rule",
        sop_id="SOP-ISEC-001",
        sop_title="Access Control Policy",
        business_unit="information_security",
        compliance_level=ComplianceLevel.COMPLIANT,
        severity=Severity.INFO,
        evidence_quote="Role-based access controls are implemented.",
        gap_description="",
        remediation="",
        reasoning="Full RBAC implementation documented.",
    )


@pytest.fixture
def gap_finding():
    return AuditFinding(
        clause_id="HIPAA-TECH-2",
        clause_title="Encryption",
        regulation="HIPAA Security Rule",
        sop_id="SOP-ISEC-002",
        sop_title="Data Encryption Standard",
        business_unit="information_security",
        compliance_level=ComplianceLevel.GAP,
        severity=Severity.HIGH,
        evidence_quote="Encryption is under development.",
        gap_description="No encryption at rest for ePHI.",
        remediation="Implement AES-256 encryption.",
        reasoning="SOP uses aspirational language.",
    )


@pytest.fixture
def partial_finding():
    return AuditFinding(
        clause_id="SOC2-CC6.1",
        clause_title="Logical Access",
        regulation="SOC 2",
        sop_id="SOP-ISEC-003",
        sop_title="Logical Access Controls",
        business_unit="information_security",
        compliance_level=ComplianceLevel.PARTIAL,
        severity=Severity.MEDIUM,
        evidence_quote="MFA is required for production systems.",
        gap_description="MFA not enforced for staging.",
        remediation="Extend MFA to all environments.",
        reasoning="Partial coverage across environments.",
    )
