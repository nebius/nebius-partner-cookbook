"""Citation extraction, corpus-backed verification, and context parsing.

verify_citations runs against the REAL regulation corpus in data/regulations/
(local files, no network) — so these tests also guard the corpus index.
"""
from __future__ import annotations

from sentinel.eval.citations import (
    citation_hit,
    extract_citations,
    normalize_citation,
    parse_formatted_context,
    verify_citations,
)


class TestNormalizeCitation:
    def test_known_formats(self):
        assert normalize_citation("§164.308(a)(1)(ii)(A)") == ("164.308(a)(1)(ii)(a)", "164.308")
        assert normalize_citation("Article 32") == ("article 32", "article 32")
        assert normalize_citation("CC6.1") == ("cc6.1", "cc6.1")
        assert normalize_citation("GOVERN 1.1") == ("govern 1.1", "govern 1.1")
        assert normalize_citation("Sections II-IV") == ("roman:ii-iv", "roman:ii-iv")


class TestParseFormattedContext:
    def test_groups_by_regulation_header(self):
        text = (
            "Retrieved 3 sections:\n\n### HIPAA\n\n**164.312 Technical safeguards.**\n"
            "Implement technical policies for ePHI access control.\n\n### GDPR\n\n"
            "**Article 32**\nSecurity of processing requires appropriate measures.\n"
        )
        chunks = parse_formatted_context(text)
        regs = [c["regulation"] for c in chunks]
        assert "HIPAA" in regs and "GDPR" in regs
        hipaa = next(c for c in chunks if c["regulation"] == "HIPAA")
        assert "164.312" in hipaa["text"]

    def test_citation_hit_against_parsed_context(self):
        text = "### GDPR\nArticle 32 Security of processing...\n### EU AI Act\nArticle 9 Risk management...\n"
        chunks = parse_formatted_context(text)
        # Article 9 must hit only via the EU AI Act group, not GDPR's.
        assert citation_hit({"regulation": "EU AI Act", "section": "Article 9"}, chunks) == (True, True)
        assert citation_hit({"regulation": "GDPR", "section": "Article 9"}, chunks) == (False, False)


class TestExtractCitations:
    def test_hipaa_paths(self):
        cites = extract_citations("Per 45 CFR §164.312(a)(2)(iv), encryption is addressable; see also 164.308.")
        bases = {(c["regulation"], c["base"]) for c in cites}
        assert ("HIPAA", "164.312") in bases
        assert ("HIPAA", "164.308") in bases

    def test_article_attributed_to_nearest_regulation(self):
        cites = extract_citations(
            "Under GDPR, Article 32 mandates security of processing. The EU AI Act's Article 9 requires risk management."
        )
        pairs = {(c["regulation"], c["base"]) for c in cites}
        assert ("GDPR", "article 32") in pairs
        assert ("EU AI Act", "article 9") in pairs

    def test_soc2_and_ai_rmf(self):
        cites = extract_citations("SOC 2 CC6.1 covers logical access; NIST AI RMF GOVERN 1.1 covers policies.")
        pairs = {(c["regulation"], c["base"]) for c in cites}
        assert ("SOC 2", "cc6.1") in pairs
        assert ("NIST AI RMF", "govern 1.1") in pairs

    def test_bare_numbers_not_extracted(self):
        # Version numbers / quantities must not become citations.
        assert extract_citations("Version 3.2 shipped with 12.5 percent improvement.") == []

    def test_empty(self):
        assert extract_citations("") == []


class TestVerifyCitations:
    def test_real_hipaa_clause_verifies(self):
        v = verify_citations("HIPAA §164.312(a) requires access control.")
        assert v["n"] == 1
        assert v["n_verified"] == 1
        assert v["precision"] == 1.0

    def test_invented_section_flagged(self):
        v = verify_citations("Per HIPAA §164.999, all data must be purple.")
        assert v["n"] == 1
        assert v["n_verified"] == 0
        flagged = v["citations"][0]
        assert flagged["exists"] is False

    def test_invented_article_flagged(self):
        v = verify_citations("GDPR Article 999 covers teleportation.")
        assert v["n"] == 1
        assert v["n_verified"] == 0

    def test_real_article_verifies(self):
        v = verify_citations("GDPR Article 32 requires security of processing.")
        assert v["n_verified"] == 1

    def test_no_citations_gives_none_precision(self):
        v = verify_citations("The SOP looks generally reasonable.")
        assert v["n"] == 0
        assert v["precision"] is None
