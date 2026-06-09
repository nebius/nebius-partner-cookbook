# Regulation Source Texts

Reference texts for Sentinel's target regulations. Used for grounding the compliance auditor's assessments. Text files (`.txt` and `.md`) are ingested into Pinecone namespace `regulations` via `make ingest-regulations`. PDFs are extracted to `.txt` first via `scripts/extract_pdf_text.py`.

**Knowledge base**: 2,386 chunks across 22 source documents covering 9 regulation frameworks (core set). An additional 27 external standards referenced by SOPs are available for ingestion.

## SOC 2

Not included — AICPA copyrighted material. Download from [AICPA Trust Services Criteria](https://us.aicpa.org/interestareas/frc/assuranceadvisoryservices/trustservicescriteria) and place as:
- `soc2_trust_services_criteria_2017_revised_2022.pdf` — 2017 Trust Services Criteria with Revised Points of Focus (2022)
- `soc2_description_criteria_2018_revised_2022.pdf` — 2018 SOC 2 Description Criteria (revised 2022)

Then run `python scripts/extract_pdf_text.py` to generate `.txt` files.

## HIPAA

### Current (2025)

| File | Description | Source |
|------|-------------|--------|
| `hipaa_45cfr_part160_general_admin.xml` | 45 CFR Part 160 — General Administrative Requirements (XML) | eCFR API |
| `hipaa_45cfr_part160_general_admin.txt` | Same, converted to plain text (124 chunks) | eCFR API → convert script |
| `hipaa_45cfr_part162_admin_requirements.xml` | 45 CFR Part 162 — Administrative Requirements (XML) | eCFR API |
| `hipaa_45cfr_part162_admin_requirements.txt` | Same, converted to plain text (111 chunks) | eCFR API → convert script |
| `hipaa_45cfr_part164_security_privacy.xml` | 45 CFR Part 164 — Security and Privacy (XML) | eCFR API |
| `hipaa_45cfr_part164_security_privacy.txt` | Same, converted to plain text — **main HIPAA Security Rule** (228 chunks) | eCFR API → convert script |
| `hipaa_ecfr_45cfr_parts_160_162_164.pdf` | Combined eCFR printout of all three parts (not ingested) | eCFR |
| `hipaa_public_law_104_191_1996.pdf` | Original HIPAA statute (not ingested) | HHS ASPE |

### Historical Editions

| File | Description | Date | Source |
|------|-------------|------|--------|
| `hipaa_45cfr_part164_2017.xml` / `.txt` | Part 164 as of Jan 2017 (earliest in eCFR, post-Omnibus Rule) — 218 chunks | 2017-01-01 | eCFR API |
| `hipaa_45cfr_part164_2020.xml` / `.txt` | Part 164 as of Jan 2020 (pre-pandemic baseline) — 218 chunks | 2020-01-01 | eCFR API |
| `hipaa_45cfr_part164_2024.xml` / `.txt` | Part 164 as of Jan 2024 (before 2025 cybersecurity update) — 218 chunks | 2024-01-01 | eCFR API |
| `hipaa_45cfr_part160_2020.xml` / `.txt` | Part 160 as of Jan 2020 — 123 chunks | 2020-01-01 | eCFR API |
| `hipaa_45cfr_part162_2020.xml` / `.txt` | Part 162 as of Jan 2020 — 110 chunks | 2020-01-01 | eCFR API |

## GDPR

| File | Description | Source |
|------|-------------|--------|
| `gdpr_regulation_eu_2016_679.pdf` | Regulation (EU) 2016/679 — official EUR-Lex text (not ingested) | EUR-Lex |
| `gdpr_full_text.md` | Navigable article-by-article text (124 chunks) | gdpr-info.eu |

GDPR has not been substantively amended since adoption (April 2016, effective May 2018).

## EU AI Act

| File | Description | Source |
|------|-------------|--------|
| `eu_ai_act_regulation_eu_2024_1689.pdf` | Regulation (EU) 2024/1689 — official final text (not ingested, covered by .md) | EUR-Lex |
| `eu_ai_act_full_text.md` | Navigable article-by-article text, current edition (111 chunks) | artificialintelligenceact.eu |
| `eu_ai_act_2021_commission_proposal.pdf` | COM/2021/206 — original Commission proposal (108 pages) | EUR-Lex |
| `eu_ai_act_2021_commission_proposal.txt` | Same, extracted text (237 chunks, edition: 2021-proposal) | pypdf |

The AI Act entered into force 1 Aug 2024, fully applicable 2 Aug 2026. An "AI omnibus" simplification package had political agreement on 7 May 2026.

## NIST AI RMF

| File | Description | Source |
|------|-------------|--------|
| `nist_ai_rmf_100_1.pdf` | NIST AI 100-1: AI Risk Management Framework (final, Jan 2023) | NIST |
| `nist_ai_rmf_100_1.txt` | Same, extracted text (80 chunks) | pypdf |
| `nist_ai_600_1_genai_profile.pdf` | NIST AI 600-1: Generative AI Profile (Jul 2024) | NIST |
| `nist_ai_600_1_genai_profile.txt` | Same, extracted text (106 chunks) | pypdf |
| `nist_ai_rmf_100_1_draft1_2022.pdf` | NIST AI 100-1: 1st public draft (Mar 2022) | NIST |
| `nist_ai_rmf_100_1_draft1_2022.txt` | Same, extracted text (44 chunks, edition: 2022-draft1) | pypdf |
| `nist_ai_rmf_100_1_draft2_2022.pdf` | NIST AI 100-1: 2nd public draft (Aug 2022) | NIST |
| `nist_ai_rmf_100_1_draft2_2022.txt` | Same, extracted text (64 chunks, edition: 2022-draft2) | pypdf |

## SR 11-7 / Model Risk Management

| File | Description | Source |
|------|-------------|--------|
| `sr_11_7_occ_model_risk_management.pdf` | OCC Bulletin 2011-12a: original guidance (2011) | OCC |
| `sr_11_7_occ_model_risk_management.txt` | Same, extracted text (15 chunks) | pypdf |

## California AI Laws

| File | Description | Source |
|------|-------------|--------|
| `california_sb53_frontier_ai_transparency.txt` | SB 53: Transparency in Frontier AI Act (signed Sep 29, 2025) — 36 chunks | CA leginfo |
| `california_sb942_ai_transparency_act.txt` | SB 942: California AI Transparency Act (signed Sep 19, 2024) — 10 chunks | CA leginfo |
| `california_ab853_ai_transparency_amendments.txt` | AB 853: AI Transparency Act Amendments (signed Sep 16, 2025) — 10 chunks | CA leginfo |

SB 1047 was vetoed Sep 2024. SB 53 is its successor — lighter-touch transparency for frontier AI developers (>10^26 FLOPS, >$500M revenue).

## NIST Special Publications

| File | Description | Source |
|------|-------------|--------|
| `nist_sp_800_53_rev5.pdf` / `.txt` | SP 800-53 Rev 5: Security and Privacy Controls (492 pages) | NIST |
| `nist_sp_800_88_rev1.pdf` / `.txt` | SP 800-88 Rev 1: Media Sanitization Guidelines (65 pages) | NIST |
| `nist_sp_800_61_rev2.pdf` / `.txt` | SP 800-61 Rev 2: Computer Security Incident Handling (80 pages) | NIST |
| `nist_csf_2_0.pdf` / `.txt` | Cybersecurity Framework 2.0 (32 pages) | NIST |
| `nist_sp_800_63b.pdf` / `.txt` | SP 800-63B: Digital Identity — Authentication (80 pages) | NIST |
| `nist_sp_800_207.pdf` / `.txt` | SP 800-207: Zero Trust Architecture (59 pages) | NIST |
| `nist_sp_800_34_rev1.pdf` / `.txt` | SP 800-34 Rev 1: Contingency Planning (149 pages) | NIST |
| `nist_sp_1270.pdf` / `.txt` | SP 1270: Towards a Standard for Identifying and Managing Bias in AI (86 pages) | NIST |
| `nist_privacy_framework_1_0.pdf` / `.txt` | Privacy Framework v1.0 (43 pages) | NIST |
| `nist_sp_800_161_rev1.pdf` / `.txt` | SP 800-161 Rev 1: Cybersecurity Supply Chain Risk Management (327 pages) | NIST |
| `nist_sp_800_218.pdf` / `.txt` | SP 800-218: Secure Software Development Framework (SSDF) (36 pages) | NIST |

## FDA / 21 CFR

| File | Description | Source |
|------|-------------|--------|
| `fda_21cfr_part820_qsr.xml` / `.txt` | 21 CFR Part 820: Quality System Regulation | eCFR API |
| `fda_21cfr_part11_electronic_records.xml` / `.txt` | 21 CFR Part 11: Electronic Records / Signatures | eCFR API |
| `fda_21cfr_part807_premarket.xml` / `.txt` | 21 CFR Part 807: Premarket Notification (510k) | eCFR API |
| `fda_ai_ml_samd_framework.pdf` / `.txt` | FDA AI/ML-Based SaMD Action Plan (8 pages) | FDA |
| `fda_clinical_decision_support_guidance.pdf` / `.txt` | Clinical Decision Support Software Guidance (27 pages) | FDA |

## EU Directives & Regulations (Non-Core)

| File | Description | Source |
|------|-------------|--------|
| `eu_mdr_regulation_2017_745.pdf` / `.txt` | Regulation (EU) 2017/745: Medical Device Regulation (175 pages) | EUR-Lex |
| `eu_standard_contractual_clauses_2021_914.pdf` / `.txt` | Commission Decision (EU) 2021/914: Standard Contractual Clauses (31 pages) | EUR-Lex |
| `eu_eprivacy_directive_2002_58.pdf` / `.txt` | Directive 2002/58/EC: ePrivacy Directive (11 pages) | EUR-Lex |
| `eu_amld4_directive_2015_849.pdf` / `.txt` | Directive (EU) 2015/849: 4th Anti-Money Laundering Directive (45 pages) | EUR-Lex |
| `eu_funds_transfer_regulation_2015_847.pdf` / `.txt` | Regulation (EU) 2015/847: Funds Transfer Regulation (18 pages) | EUR-Lex |

## OWASP

Not included — OWASP content is licensed CC BY-SA 4.0 and is not redistributed here. Download from OWASP and place the files in this directory, then run `make ingest-regulations`:

- `owasp_top_10_2021.md` — [OWASP Top 10:2021](https://owasp.org/Top10/)
- `owasp_api_security_top_10_2023.md` — [OWASP API Security Top 10 2023](https://owasp.org/API-Security/editions/2023/en/0x00-header/)

## Financial Laws

| File | Description | Source |
|------|-------------|--------|
| `bsa_31cfr_chapter_x.xml` / `.txt` | Bank Secrecy Act: 31 CFR Chapter X (FinCEN rules, AML, CTR, SAR) | eCFR API |
| `ecoa_regulation_b_12cfr1002.xml` / `.txt` | Equal Credit Opportunity Act: Regulation B (12 CFR 1002) | eCFR API |
| `fcra_fair_credit_reporting_act.pdf` / `.txt` | Fair Credit Reporting Act (15 USC Chapter 41 Subchapter III, 67 pages) | GovInfo/GPO |

PCI DSS Quick Reference Guide (PCI SSC, copyrighted) is not included. Download from [PCI SSC Document Library](https://www.pcisecuritystandards.org/document_library/) and place as `pci_dss_quick_guide.pdf`, then run `python scripts/extract_pdf_text.py`.

## Utilities

| Script | Description |
|--------|-------------|
| `scripts/convert_ecfr_xml_to_txt.py` | Converts eCFR XML to readable plain text |
| `scripts/extract_pdf_text.py` | Extracts text from regulation PDFs via pypdf |
| `scripts/fetch_gdpr_articles.py` | Fetches GDPR articles from gdpr-info.eu |
| `scripts/fetch_eu_ai_act_articles.py` | Fetches EU AI Act articles from artificialintelligenceact.eu |
