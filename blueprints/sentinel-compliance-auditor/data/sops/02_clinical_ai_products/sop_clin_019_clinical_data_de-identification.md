---
sop_id: "SOP-CLIN-019"
title: "Clinical Data De-identification"
business_unit: "Clinical AI Products"
version: "1.7"
effective_date: "2025-09-22"
last_reviewed: "2026-08-21"
next_review: "2027-02-05"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Clinical Data De-identification

**SOP-CLIN-019 | Version 1.7**
**Effective Date:** 2025-09-22
**Owner:** Dr. Aisha Okafor, VP of Clinical AI Products
**Classification:** Internal

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework, methodologies, and operational controls for the de-identification of Protected Health Information (PHI) and personal data used across Meridian Health Technologies, Inc.’s Clinical AI Platform, MedInsight Analytics, and related research initiatives. The purpose of this SOP is to enable the lawful secondary use of clinical data for algorithm training, product development, population health analytics, and collaborative research, while ensuring compliance with the Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule, the EU General Data Protection Regulation (GDPR), and Meridian’s contractual obligations to its Covered Entity and Payer clients.

The de-identification process is a foundational requirement for Meridian’s AI governance strategy, specifically enabling the transition of data from a regulated, restricted state to a lower-risk state suitable for sandbox environments, model training pipelines, and analytics workspaces.

### 1.2 Scope

This SOP applies to all workforce members, contractors, vendors, and third-party partners who access, process, transfer, or store clinical datasets containing direct or indirect identifiers within the Meridian ecosystem.

**In-Scope Data and Systems:**
- All structured and unstructured clinical data ingested into the MedInsight Analytics platform (covering ~12M patient lives).
- DICOM imaging studies, radiology reports, and clinical notes processed by the Clinical AI Platform.
- Claims and remittance data processed by HealthPay Financial Services when utilized for secondary analytical purposes.
- Data stored within the Meridian SaaS Platform data layer, including Amazon S3 data lakes (us-east-1, eu-west-1), Snowflake analytical warehouses, and PostgreSQL operational databases.
- Training, validation, and test datasets used for PyTorch and TensorFlow model development managed via Kubeflow pipelines and MLflow.

**Out-of-Scope:**
- Production transactional data flowing through the HealthPay Financial Services payment gateway for primary payment processing (governed by SOP-FIN-042).
- Employee human resources data.
- De-identification of audio or video recordings (future scope).

**Target Audience:**
Data Engineers, Machine Learning Engineers, Clinical Informaticists, Data Privacy Analysts, Compliance Officers, and Data Governance Managers within the Clinical AI Products business unit.

---

## 3. Roles and Responsibilities

The following RACI matrix delineates the specific responsibilities for executing this SOP.

| Role | Responsibility | Classification (R/A/C/I) |
|------|----------------|--------------------------|
| **Chief Medical Officer (Dr. Priya Patel)** | Ultimate sign-off authority on Expert Determination certifications and re-identification risk acceptance. | Accountable |
| **VP of Clinical AI Products (Dr. Aisha Okafor)** | Process owner; ensures operational adherence to de-identification procedures and resource allocation. | Accountable |
| **Data Privacy Officer (DPO)** | Monitors regulatory compliance with HIPAA and GDPR; approves adequacy of de-identification methodology; manages breach notification procedures. | Accountable |
| **Data Governance Manager** | Maintains the data catalog, tags de-identified datasets with appropriate metadata, and manages access controls. | Responsible |
| **Lead Clinical Informaticist** | Executes Expert Determination reviews, documenting the statistical risk of re-identification. | Responsible |
| **Data Engineering Lead** | Implements the automated Safe Harbor de-identification pipelines within AWS Glue and Snowflake. | Responsible |
| **Machine Learning Engineers** | Consume de-identified data for model training; validate that ingested data meets de-identification standards. | Informed |
| **Chief AI Officer (Dr. Marcus Rivera)** | Sponsors strategic needs for data minimization and synthetic data goals. | Informed |
| **Sales & Partnerships** | Initiates requests for data sharing with academic partners; ensures Business Associate Agreements (BAAs) are in place. | Consulted |
| **Internal Audit** | Conducts biannual audits of de-identification logs and processes. | Consulted |

---

## 4. Policy Statements

Meridian Health Technologies is committed to the following high-level policy mandates regarding the handling of clinical data:

4.1 **De-identification by Default.** Clinical data designated for non-production research and development purposes must be de-identified prior to ingestion into model training environments. The use of raw PHI for sandbox testing or exploratory data analysis is strictly prohibited.

4.2 **Methodology Selection.** Meridian employs two recognized methods for de-identification: the HIPAA Safe Harbor method and the Expert Determination method. The Safe Harbor method is the default operational procedure for structured data. Expert Determination is required for unstructured free-text datasets and DICOM imaging headers where complete removal of identifiers via Safe Harbor is impractical or compromises clinical utility.

4.3 **Prohibition on Re-identification.** Workforce members are expressly prohibited from attempting to re-identify de-identified datasets unless performing an authorized re-identification risk assessment as part of an Expert Determination validation, and only on explicitly designated test datasets. Any accidental re-identification must be reported immediately.

4.4 **Data Minimization.** Per GDPR principles and Meridian’s data governance charter, only the minimum necessary identifiers shall be retained during the pseudonymization phase before Safe Harbor stripping is executed.

4.5 **Breach Notification.** In the event of a data spill or accidental exposure of PHI during the de-identification pipeline, the incident response protocol defined in SOP-SEC-007 (Information Security Incident Response) is invoked. Workforce members are required to report potential breaches to the Security Operations Center (SOC) and the Data Privacy Officer immediately, as notification requirements to clients and regulators are time-sensitive.

---

## 5. Detailed Procedures

This section outlines the step-by-step operational procedures for the two primary de-identification pathways, validation quality assurance, and secure data transfer.

### 5.1 Data Intake and Classification

Prior to any de-identification procedure, incoming datasets must be classified.

1.  **Source Verification:** The Data Engineering Lead verifies the source system (e.g., Epic Clarity, Cerner Millennium, Flatiron EMR cloud feed) and ensures that a valid Data Sharing Agreement (DSA) or BAA is active.
2.  **Data Profiling:** Using the Meridian SaaS Platform profiling tool (AWS Glue DataBrew), Source Data Engineers run an automated scan to identify columns containing direct identifiers (Names, MRNs, SSNs) and quasi-identifiers (Dates, ZIP codes).
3.  **Workspace Assignment:**
    -   **Source_Raw_PHI:** Access restricted to certified Data Engineers only (AD Group: `CLIN-RW-PHI-ENG`).
    -   **Source_Limited_DS:** Pseudonymized staging area where global patient IDs are replaced with salted hashes.

### 5.2 Method A: HIPAA Safe Harbor Execution

This pipeline is implemented via the `cln_deid_safeharbor_v2` AWS Glue job, orchestrated by Airflow DAG `dag_deid_safeharbor`.

**5.2.1 Removal of Direct Identifiers (18 HIPAA Attributes):**

The automated job executes the following transformations. Manual QA verification is required for any records flagged by the probabilistic match failure.

| HIPAA Identifier Category | Transformation Logic | Tool/System |
|---|---|---|
| Names (Patient, Provider, Guarantor) | Named Entity Recognition (NER) model `clinic-ner-v3` detects names; replaced with token `[NAME_REDACTED]`. | Spark NLP on EMR |
| Geographic Subdivisions (Smaller than State) | Drop columns `ADDRESS_LINE`, `CITY`, `COUNTY`. Retain `STATE` and `COUNTRY`. Zip codes: truncate to first 3 digits if population >20,000 per US Census Bureau crosswalk; else set to `000`. | Snowflake UDF `TRUNC_ZIP()` |
| Dates (All types, except year) | Shift dates by a random offset (90-365 days) using consistent hash per patient to preserve temporal intervals but break actual calendar dates. Year is retained. | Python UDF `shift_date()` |
| Telephone Numbers, Fax Numbers, Email, URLs, IP Addresses | Full-field redaction (set to `NULL`). | Glue Transform `DropField` |
| Social Security Numbers, Medical Record Numbers, Health Plan Beneficiary Numbers, Account Numbers, Certificate/License Numbers, Vehicle Identifiers, Device Identifiers, Biometric Identifiers | SHA-256 salted hash replacement. Salt rotated quarterly via AWS Secrets Manager. | Python UDF `crypto_hash()` |
| Full-face photographic images | Rejected at intake by image classification filter `deid-mgr-dicom`. | Amazon Rekognition |

**5.2.2 Free-Text Scrubber (Post-Processing):**

After structured field removal, a secondary NER scrubber (`monq-text-scrubber-v3`) scans narrative fields (e.g., `NURSING_NOTE`, `RADIOLOGY_REPORT_TEXT`).
- **Whitelist Validation:** The scrubber is configured with a clinical whitelist (`meridian_whitelist_v4.txt`) to preserve medical terms (e.g., "Huntington's disease" is preserved, while "Huntington, NY" is redacted).
- **Manual Review Queue:** Notes with confidence scores < 85% are routed to the `CLIN-DEID-MANUAL-REVIEW` queue (Jira Project: DEIDR) for Clinical Informaticist review.

### 5.3 Method B: Expert Determination

Used specifically for DICOM imaging studies and complex multi-modal datasets where Safe Harbor stripping destroys algorithmic integrity.

1.  **Commissioning:** The Lead Clinical Informaticist convenes an Expert Panel (statistician, subject matter expert, data engineer).
2.  **Risk Analysis:** The panel utilizes the k-anonymity and l-diversity models against the dataset census tract linkage risk.
    -   **Threshold:** Re-identification risk must be ≤ 0.05 (5% probability threshold).
    -   **Genomic Data:** Any dataset containing genetic variants (VCF files) automatically qualifies for Expert Determination regardless of Safe Harbor application.
3.  **Statistical Methodology:** Application of differential privacy via local random-noise injection into quasi-identifier columns (weight, BMI) to achieve plausible deniability while preserving cohort-level statistics.
4.  **Certification Document:** The Expert Panel completes Form **CLIN-019-F02 (Expert Determination Certificate)**. This certificate is reviewed by the DPO and signed by the Chief Medical Officer. The certificate is valid for 12 months or until the dataset linkage environment changes.

### 5.4 De-identification Validation Quality Assurance

A validation step is mandatory before moving data to the "De-identified" data lake zone (`s3://meridian-deid-analytics`).

1.  **Automated Validation Suite (`deid-val-suite`):** Weekly scans check for known patterns (e.g., uncorrupted SSN patterns `XXX-XX-XXXX`). Any hit triggers a pipeline halt.
2.  **Re-identification Penetration Test:** The Security Team (SOP-SEC-015) performs biannual "Capture-the-Flag" attacks on a 10,000 record de-identified dataset to simulate external linkage.
3.  **GDPR Lawful Basis Documentation:** Processing activities for de-identification must be logged in the Record of Processing Activities (ROPA). The lawful basis (e.g., processing for scientific research purposes, Article 89 GDPR) must be reviewed by the DPO. Workforce members are trained annually on the specific lawful bases applicable to their data workflows.

### 5.5 Handling Data Subject Access Requests

Data subject rights procedures are managed by the Privacy Operations team. When a verified request for access, rectification, or erasure is received, the team reconciles the subject's identity against the pseudonymization tokenization service (`meridian-token-svc`). Processing of these requests will be carried out without undue delay and confirmed back to the requestor via standard communication channels.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

- **Data Handling Agreement:** All employees must sign the Meridian Employee Confidentiality and IP Agreement, which includes specific clauses on re-identification prohibition.
- **Annual Policy Attestation:** Workforce members with access to `Source_Raw_PHI` must complete mandatory annual HIPAA Privacy and Security training, administered via Workday Learning. This training covers Meridian’s de-identification standards, Safe Harbor methodology, and breach reporting obligations.
- **Sanctions:** Violation of this SOP will result in disciplinary action, up to and including termination and legal referral.

### 6.2 Technical Controls

| Control | Implementation Mechanism | Objective |
|---------|---------------------------|-----------|
| Role-Based Access Control (RBAC) | Microsoft Entra ID Groups tied to Snowflake Roles; `CLIN-PHI-RO` vs. `CLIN-DEID-RO` | Prevent unauthorized access to raw PHI source zones |
| Salted Hashing | One-way SHA-256 with HMAC; keys stored in AWS Secrets Manager with auto-rotation (90 days) | Render identifiers non-reversible |
| Data Loss Prevention (DLP) | Netskope CASB monitoring for uploads to Snowflake staging buckets | Block transmission of files containing `^[0-9]{3}-[0-9]{2}-[0-9]{4}$` (SSN pattern) to unapproved buckets |
| Audit Logging | Snowflake `ACCESS_HISTORY` and `QUERY_HISTORY` views streaming to Splunk | Immutable logging of all queries against raw and de-identified schemas |

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness of the de-identification program is tracked via the Meridian Corporate Compliance Dashboard.

**7.1 Key Performance Indicators (KPIs):**

| Metric | Target Threshold | Measurement Cadence |
|--------|------------------|---------------------|
| **Safe Harbor Pipeline Error Rate** | < 0.25% of records requiring manual correction | Weekly |
| **Free-Text Redaction Precision** | ≥ 97% (avoidance of clinical false positives) | Monthly |
| **Expert Determination Aging** | Certificates renewed > 30 days before expiry | Monthly |
| **Manual Review Queue Backlog** | < 50 items open > 7 days | Weekly |
| **De-identification Validation Failure** | Zero un-scrubbed PII slips into `deid-analytics` zone | Continuous |

**7.2 Reporting Cadence:**
- **Monthly Operational Review:** VP of Clinical AI Products reviews pipeline performance and queue backlogs.
- **Quarterly Management Review:** Data Privacy Officer presents findings to the Risk and Compliance Steering Committee.
- **Biannual Audit Report:** Internal Audit provides a control effectiveness rating, focusing on linkage attack resilience.

---

## 8. Exception Handling and Escalation

Exceptions to this policy are tightly controlled due to regulatory risk.

**8.1 Exception Types:**
- **Type 1 (Safe Harbor Deviation):** Request to retain certain geographic units (e.g., full ZIP code) for a specific epidemiological study.
- **Type 2 (Date Retention):** Request to avoid date shifting in a longitudinal algorithm where timeline integrity is paramount.

**8.2 Process for Exception:**
1.  **Requestor:** Completes Form **CLIN-019-F03 (De-identification Exception Request)**, detailing the technical justification, the specific data fields, and compensating controls proposed (e.g., use of restricted synthetic data generation environments).
2.  **Technical Review:** Lead Clinical Informaticist evaluates the re-identification risk impact.
3.  **Compliance Review:** DPO evaluates lawful basis and regulatory impact.
4.  **Approval Committee:** Exceptions must be approved jointly by the Chief Medical Officer (Dr. Priya Patel) and the VP of Clinical AI Products (Dr. Aisha Okafor). Exceptions are time-bound and recorded in the GRC platform (Archer).

**8.3 Escalation Matrix:**

| Incident Severity | Trigger | Escalation Path | Response SLA |
|-------------------|---------|-----------------|--------------|
| **Critical (P1)** | Confirmed leak of raw PHI into de-identified environment | Incident Commander > CISO > CEO | 1 Hour |
| **High (P2)** | Pipeline automation failure exposing PHI in logs | Data Engineering Lead > DPO | 4 Hours |
| **Medium (P3)** | Manual review backlog exceeding 200 items | Clinical Informaticist > VP, Clin Ops | 24 Hours |

---

## 9. Training Requirements

All personnel governed by this SOP must fulfill specific competency attestations.

**9.1 Required Training Modules:**
- **CLIN-TR-101:** HIPAA Privacy in Machine Learning Pipelines (Annual).
- **CLIN-TR-203:** Practical Safe Harbor De-identification using Meridian Tools (Role-Specific; On-boarding).
- **CLIN-TR-450:** Expert Determination Certification Workshop (Clinical Informaticists and Biostatisticians only).

**9.2 Tracking:**
Training compliance is tracked automatically via the Workday Learning Management System (LMS). Managers receive monthly non-compliance reports. Access to data engineering production systems (`Source_Raw_PHI`) is automatically suspended in Microsoft Entra ID if annual training is overdue by more than 15 days.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Policy Title | Relationship |
|--------|--------------|--------------|
| SOP-SEC-001 | Information Security Governance | Overarching security framework |
| SOP-DAT-015 | Data Classification and Handling Standard | Defines data zones (Raw, Limited, De-identified) |
| SOP-FIN-042 | Payment Data Processing Controls | Governs raw claims processing, upstream of analytical de-id |
| SOP-CLIN-022 | Synthetic Data Generation for Rare Diseases | Next-stage derivative process |
| SOP-SEC-007 | Information Security Incident Response Plan | Incident response protocols |
| SOP-HR-005 | Workforce Onboarding and Offboarding | Access provisioning lifecycle |

### 10.2 External References
- 45 CFR §164.514(a) — Standards for de-identification of protected health information
- 45 CFR §164.502(d)(2) — Uses and disclosures of de-identified information
- EU General Data Protection Regulation (GDPR), Recital 26 — Not applicable to anonymous information
- ISO 27001:2022 — Information Security, Cybersecurity and Privacy Protection
- HHS Guidance Regarding Methods for De-identification of PHI (Nov 2012)

---

## 11. Revision History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2022-11-10 | Dr. Aisha Okafor | Initial policy draft; Safe Harbor procedures defined. |
| 1.3 | 2023-06-14 | J. Chen (Data Governance) | Added Expert Determination process (Section 5.3); integrated DICOM image de-id requirements. |
| 1.5 | 2024-08-01 | M. Rossi (DPO) | Major revision integrating GDPR data minimization mandates; updated escalation matrix to align with Global SOC. |
| 1.6 | 2025-09-01 | Dr. Aisha Okafor | Updated Safe Harbor free-text scrubber to `monq-text-scrubber-v3`; moved from Tableau to Splunk for audit logging. |
| 1.7 | 2026-08-21 | Dr. Aisha Okafor | Annual review; updated roles to reflect RACI adjustments for Lead Clinical Informaticist; added CE Marking context under MDR. |