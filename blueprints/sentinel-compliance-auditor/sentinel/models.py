from __future__ import annotations

from enum import Enum
from pydantic import BaseModel


class ComplianceLevel(str, Enum):
    COMPLIANT = "compliant"
    PARTIAL = "partial"
    GAP = "gap"


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


# Raw-string -> canonical-value aliases, centralized so the audit pipeline
# (graph/tools.py) and the eval scorers (eval/metrics.py, scripts/validate_run.py)
# normalize identically.
COMPLIANCE_LEVEL_ALIASES = {
    "compliant": "compliant",
    "partial": "partial",
    "gap": "gap",
    "info": "compliant",
    "non-compliant": "gap",
    "non_compliant": "gap",
    "noncompliant": "gap",
}

SEVERITY_ALIASES = {
    "critical": "critical",
    "high": "high",
    "medium": "medium",
    "low": "low",
    "info": "info",
    "compliant": "info",
    "partial": "medium",
    "gap": "high",
}


def normalize_compliance_level(raw: str) -> ComplianceLevel:
    """Map a raw compliance string to a ComplianceLevel; unknown -> GAP (conservative)."""
    return ComplianceLevel(COMPLIANCE_LEVEL_ALIASES.get(raw.strip().lower(), "gap"))


def normalize_severity(raw: str) -> Severity:
    """Map a raw severity string to a Severity; unknown -> HIGH (conservative)."""
    return Severity(SEVERITY_ALIASES.get(raw.strip().lower(), "high"))


def normalize_level(level: str) -> str:
    """Canonicalize a compliance-level string, passing unknown values through.

    Used by the eval scorers, which compare arbitrary parsed levels rather than
    constructing enums.
    """
    key = level.strip().lower()
    return COMPLIANCE_LEVEL_ALIASES.get(key, key)


class SOPChunk(BaseModel):
    sop_id: str
    title: str
    business_unit: str
    chunk_text: str
    section: str = ""
    page_estimate: int = 0
    score: float = 0.0


class AuditFinding(BaseModel):
    clause_id: str
    clause_title: str
    regulation: str
    sop_id: str
    sop_title: str
    business_unit: str
    compliance_level: ComplianceLevel
    severity: Severity
    evidence_quote: str = ""
    gap_description: str = ""
    remediation: str = ""
    reasoning: str = ""


class AuditMetrics(BaseModel):
    total_clauses: int = 0
    total_sops_audited: int = 0
    total_findings: int = 0
    compliant_count: int = 0
    partial_count: int = 0
    gap_count: int = 0
    critical_count: int = 0
    high_count: int = 0
    medium_count: int = 0
    low_count: int = 0
    total_tokens: int = 0
    total_retrieval_steps: int = 0
    avg_latency_per_cell: float = 0.0
    total_latency: float = 0.0
    total_cost: float = 0.0


