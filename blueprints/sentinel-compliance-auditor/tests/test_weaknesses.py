"""Planted-weakness recall scoring."""
from __future__ import annotations

from sentinel.eval.weaknesses import weakness_hit, weakness_recall


class TestWeaknessHit:
    def test_clause_reference_match(self):
        weakness = "No post-market monitoring plan as required by Article 72"
        findings = "EUAI-Art.72: gap (high) — SOP lacks the post-market monitoring plan required by Article 72"
        assert weakness_hit(weakness, findings)

    def test_clause_reference_alone_suffices(self):
        # Even with different wording, citing the same article counts.
        weakness = "No provisions for AI system registration in the EU database per Article 49"
        findings = "EUAI-Art.49: gap (high) — registration requirement unaddressed (Article 49)"
        assert weakness_hit(weakness, findings)

    def test_term_overlap_match(self):
        weakness = "Human oversight mechanisms entirely absent despite high-risk classification"
        findings = "EUAI-Art.14: gap (high) — no human oversight defined for this high-risk system; classification noted"
        assert weakness_hit(weakness, findings)

    def test_unrelated_finding_misses(self):
        weakness = "No post-market monitoring plan as required by Article 72"
        findings = "HIPAA-164.312(a): gap (high) — encryption at rest is not specified for ePHI storage"
        assert not weakness_hit(weakness, findings)

    def test_empty_findings_miss(self):
        assert not weakness_hit("Anything at all", "")

    def test_generic_words_do_not_match(self):
        # Findings full of generic audit vocabulary must not match a specific weakness.
        weakness = "Business Associate Agreements mentioned but no BAA inventory or review cycle"
        findings = "SOC2-CC1.1: partial (medium) — control requirements are documented but the process lacks specific procedures"
        assert not weakness_hit(weakness, findings)


class TestWeaknessRecall:
    MATRIX = [
        {"sop_id": "SOP-A", "regulation": "EU AI Act", "compliance_level": "gap",
         "weaknesses": ["No post-market monitoring plan as required by Article 72",
                        "Human oversight mechanisms entirely absent"]},
        {"sop_id": "SOP-B", "regulation": "HIPAA", "compliance_level": "partial",
         "weaknesses": ["Audit controls referenced but logging granularity and retention unspecified"]},
        {"sop_id": "SOP-C", "regulation": "GDPR", "compliance_level": "compliant", "weaknesses": []},
    ]

    def test_recall_counts_unscored_pairs_as_missed(self):
        pair_texts = {
            ("SOP-A", "EU AI Act"): "EUAI-Art.72: gap — post-market monitoring plan missing per Article 72",
            # SOP-B has no findings in this run at all.
        }
        w = weakness_recall(self.MATRIX, pair_texts)
        assert w["total_weaknesses"] == 3
        assert w["hits"] == 1
        assert w["recall"] == 1 / 3
        # Among scored pairs only, SOP-A's two weaknesses were assessable: 1/2.
        assert w["scored_total"] == 2
        assert w["scored_hits"] == 1
        assert w["recall_scored"] == 0.5

    def test_per_regulation_breakdown(self):
        pair_texts = {
            ("SOP-A", "EU AI Act"): "Article 72 monitoring missing; human oversight absent for the high-risk system",
            ("SOP-B", "HIPAA"): "HIPAA-164.312(b): partial — audit controls exist but logging granularity and retention are unspecified",
        }
        w = weakness_recall(self.MATRIX, pair_texts)
        assert w["per_regulation"]["EU AI Act"]["n"] == 2
        assert w["per_regulation"]["HIPAA"]["recall"] == 1.0
        assert w["recall"] == 1.0
