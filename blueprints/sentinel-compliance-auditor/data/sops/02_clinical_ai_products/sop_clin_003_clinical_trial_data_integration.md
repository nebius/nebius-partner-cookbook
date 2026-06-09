---
sop_id: "SOP-CLIN-003"
title: "Clinical Trial Data Integration"
business_unit: "Clinical AI Products"
version: "3.5"
effective_date: "2024-12-07"
last_reviewed: "2025-05-08"
next_review: "2025-11-18"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Clinical Trial Data Integration

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the framework, controls, and procedural requirements for the ingestion, validation, transformation, and integration of external clinical trial data into the Meridian Health Technologies Clinical AI Platform. The objective is to ensure that all third-party clinical trial datasets leveraged for AI model training, validation, and fine-tuning are integrated with demonstrable integrity, traceability, and regulatory compliance, thereby preserving the safety and efficacy of Meridian’s high-risk AI systems.

### 1.2 Scope
This SOP applies to all Meridian Health Technologies employees, contractors, and authorized third parties involved in the lifecycle of clinical trial data integration for the Clinical AI Products business unit. Specifically, this document governs:

- **Data Types:** Individual Participant Data (IPD), clinical study reports, tabulation datasets, analysis datasets, and associated metadata from completed pharmaceutical and medical device trials.
- **Data Sources:** Direct transfers from sponsor organizations, data aggregator portals, academic medical centers, and regulatory submission data packages publicly released with appropriate usage rights.
- **Systems:** All data staging, transformation, and storage environments within the Meridian SaaS Platform, including AWS S3 data lakes, Snowflake schemas, and ML feature stores managed via SageMaker and MLflow.
- **Geographies:** All data integration activities across Meridian’s global offices in Boston, London, Berlin, Singapore, and Toronto.

### 1.3 Applicability
This SOP is binding upon:
- **Clinical Data Engineering Team:** Responsible for pipeline execution.
- **AI Model Development Team:** Responsible for defining data requirements.
- **Information Security Team:** Responsible for environmental controls.
- **Data Protection & Privacy Team:** Responsible for lawful basis assessments for EU/EEA data subjects.
- **Compliance & Quality Assurance:** Responsible for auditing adherence.

### 1.4 Out of Scope
This SOP does not cover the primary collection of clinical trial data by Meridian acting as a Clinical Research Organization (CRO). It solely addresses the integration of pre-existing trial data from external custodians. Raw imaging integration pipelines are addressed in SOP-CLIN-004 (Medical Imaging Data Onboarding). Real-world evidence (RWE) data integration is addressed in SOP-CLIN-005.

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **AE** | Adverse Event |
| **CDISC** | Clinical Data Interchange Standards Consortium |
| **CDM** | Clinical Data Management |
| **CRO** | Contract Research Organization |
| **DTA** | Data Transfer Agreement |
| **eCRF** | Electronic Case Report Form |
| **GDPR** | General Data Protection Regulation (Regulation (EU) 2016/679) |
| **IPD** | Individual Participant Data |
| **LAB** | Laboratory Test Results domain (CDISC SDTM) |
| **MLflow** | Machine Learning lifecycle management platform used by Meridian |
| **PHI** | Protected Health Information (as defined by HIPAA) |
| **PII** | Personally Identifiable Information (as defined under GDPR) |
| **PRO** | Patient-Reported Outcome |
| **SAE** | Serious Adverse Event |
| **SDTM** | Study Data Tabulation Model (CDISC standard) |
| **SME** | Subject Matter Expert |
| **SOP** | Standard Operating Procedure |
| **ADaM** | Analysis Data Model (CDISC standard) |

## 3. Roles and Responsibilities

The following responsibility assignment matrix (RACI) delineates the specific accountabilities for the Clinical Trial Data Integration lifecycle.

| Activity / Decision Point | Data Engineering Lead | Clinical Data Steward | Chief Privacy Officer / DPO (Dr. Weber) | VP Clinical AI (Dr. Okafor) | CISO (Rachel Kim) | Compliance (Thomas Anderson) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intake Request Approval** | I | C | I | A | I | R |
| **Data Privacy Impact Assessment (DPIA)** | C | I | A/R | I | C | C |
| **GDPR Lawful Basis Determination** | I | I | A/R | I | I | I |
| **Data Transfer Agreement Execution** | I | I | C | A | I | R |
| **CDISC Compliance Validation** | R | A | I | C | I | I |
| **PHI/PII Minimization Enforcement** | I | C | R | I | I | A |
| **Data Quality Gate Approval** | C | R | I | A | I | I |
| **Integration Pipeline Execution** | A/R | C | I | I | I | I |
| **Audit Log Review** | I | R | I | I | I | A |

*Key: R=Responsible, A=Accountable, C=Consulted, I=Informed*

### 3.1 Named Role Descriptions
- **VP of Clinical AI Products (Dr. Aisha Okafor):** Ultimate business owner of integrated datasets. Approves high-risk integrations and any exceptions to data quality thresholds.
- **Chief Privacy Officer / DPO (Dr. Heinrich Weber):** Singular authority for determining GDPR applicability and Article 6/9 lawful bases for processing clinical trial data containing information on EU data subjects. Chairs the weekly Privacy Review Board.
- **Chief Information Security Officer (Rachel Kim):** Ensures the technical infrastructure for data transfer and storage aligns with Meridian’s ISO 27001:2022 and SOC 2 control sets.
- **Clinical Data Steward:** A domain expert responsible for clinical concept mapping and verifying the semantic integrity of SDTM mappings.

## 4. Policy Statements

### 4.1 Data Minimization and Purpose Limitation (GDPR Compliance — Thorough Coverage)
Meridian Health Technologies strictly adheres to the principles of data minimization and purpose limitation as mandated by the General Data Protection Regulation (Regulation (EU) 2016/679). In the context of clinical trial data integration, the following binding policy statements apply:

- **Article 5(1)(b) — Purpose Specification:** Integrated clinical trial data shall be repurposed exclusively for the defined secondary purpose of improving diagnostic AI algorithms. This purpose is explicitly documented in Section 4.2 of the mandatory Data Privacy Impact Assessment (DPIA) template (FRM-PRIV-102). Re-identification of any pseudonymized data subjects using the integrated dataset is strictly prohibited and constitutes a Level 1 Security Incident per SOP-SEC-001.
- **Article 5(1)(c) — Data Minimization:** Prior to ingestion into Snowflake, the Data Ingestion Pipeline must execute a script (`clean_script_pro.sh`) to strip all Free Text fields from SDTM datasets unless a documented and approved exception exists. The default configuration rejects all `CO` (Comments) domains. Any request to retain specific Comment domains must be justified via the Clinical Relevance Exception Form (FRM-CLIN-007) and approved by both Dr. Okafor and Dr. Weber.
- **Article 5(1)(e) — Storage Limitation:** Integrated clinical trial data stored in the `prod-clinical-ai-ingested` S3 bucket is subject to a lifecycle policy. Data that has not been accessed for model training within 36 months will be automatically archived to Glacier Deep Archive. Full deletion of the source integration dataset occurs 60 months after contract termination with the Data Controller, unless a separate regulatory retention mandate (e.g., FDA 21 CFR Part 11 linkage) is in effect.
- **Article 25(1) — Data Protection by Design and by Default:** The default configuration for the Ingestion Pipeline maps only the standardized controlled terminology value (`STDVAL`), not the collected verbatim term (`ORVAL`), unless the Verbatim Term is crucial for NLP-based feature engineering (e.g., for AE indication coding). This configuration is enforced by Infrastructure-as-Code templates in Terraform, preventing manual overrides without a validated change request.
- **Article 32(1)(a) — Pseudonymization and Encryption:** Upon ingestion, all direct identifiers specified in the Data Transfer Agreement are immediately pseudonymized using a SHA-256 one-way hash function. The pseudo-identifier crosswalk file is stored in a separate, isolated AWS Secrets Manager vault, accessible only to the CISO and Chief Medical Officer. This crosswalk is never merged into the ML feature store.
- **Article 9(2)(j) — Processing of Special Categories of Data:** Given that clinical trial data invariably contains data concerning health (Art. 9(1)), Meridian's lawful basis for processing is solely under Article 9(2)(j), processing for scientific research purposes in accordance with Article 89(1). Meridian’s “Scientific Research Derogation Protocol” (Document-POL-015), approved by the independent Meridian Research Ethics Board, details the proportionate safeguards.

### 4.2 Clinical Data Integrity
Meridian commits to maintaining the scientific integrity of integrated trial data. No transformation pipeline shall alter the statistical interpretation of a submitted clinical endpoint. Specifically, changes to SDTM Controlled Terminology (CT) mappings require Medical Monitor review.

## 5. Detailed Procedures

The integration lifecycle is segmented into six sequential phases, each gated by explicit approval milestones.

### 5.1 Phase 1: Intake and Feasibility Assessment

1.  The Clinical AI Product Manager initiates a request via the Meridian ServiceNow portal (`SOP Intake Form | CLIN-003`).
2.  The form captures:
    -   **Data Controller Identity:** Legal entity name and contact.
    -   **Trial Registry Identifier(s):** ClinicalTrials.gov (NCT) and/or EU Clinical Trials Register (EudraCT) numbers.
    -   **Data Volume:** Estimated number of subjects and gigabytes per domain.
    -   **Proposed Use Case:** Specific AI model version and indication.
3.  The Clinical Data Steward receives the ticket and performs a preliminary CDISC standards feasibility check within 3 business days. The Steward verifies whether the source data packaging indicates SDTM v3.3 or v3.4 metadata versioning.
4.  If the data standard is non-CDISC (e.g., custom sponsor database), a Level 2 Exception (Section 8) is automatically triggered, requiring VP Clinical AI sign-off.

### 5.2 Phase 2: Compliance Assessment & Agreement Execution

This phase is governed primarily by the Office of the DPO and Legal Department.

1.  **DPIA Trigger:** The DPO (Dr. Weber) reviews the intake form. If any trial site is located in the EEA, or the sponsor is an EU-based entity, a full DPIA (FRM-PRIV-102) is mandatory, irrespective of subject-level data residency.
2.  **Lawful Basis Mapping (GDPR Art. 6 & 9):** Dr. Weber's team explicitly maps the processing onto Articles 6(1)(f) (Legitimate Interest) and 9(2)(j) (Scientific Research). The Legitimate Interest Assessment (LIA) must be documented and linked to the ServiceNow ticket.
3.  **Data Transfer Agreement (DTA):** Legal drafts the DTA. Key mandatory Meridian-specific clauses are enforced:
    -   Clause 3.1: Sponsor warrants data is SDTM-compliant.
    -   Clause 3.2: Sponsor assumes responsibility for original consent scope, confirming re-analysis for algorithm training is permitted.
    -   Clause 4.1: Meridian is a Controller for the pseudonymized derived dataset.
4.  Execution of the DTA by both parties unlocks the technical S3 staging dropzone.

### 5.3 Phase 3: Technical Ingestion and Pseudonymization

1.  **Dropzone Configuration:** CISO (Rachel Kim) configures a dedicated, time-limited (30-day) S3 bucket dropzone (`sponsor-drop-{trial_id}`). Access is via pre-signed URLs with enforced TLS 1.3 encryption.
2.  **Data Landing:** Sponsor uploads data. Meridian's AWS EventBridge listens for `PutObject` events and logs the arrival in an immutable CloudTrail log.
3.  **Automated Pseudonymization & Minimization Pipeline:**
    -   **Step 3A (Identify):** Script `sdtm_scanner.py` scans all `.xpt` (SAS V5 Transport) files. It searches for SDTM variables flagged in the Global Clinical Variable Dictionary (GCVD) as "Direct Identifier" (e.g., `SUBJID`, `USUBJID` in DM domain).
    -   **Step 3B (Hash/Pseudo):** The scanner invokes an AWS Lambda (`pseudo_engine`) that replaces `SUBJID` with a Trial-Specific Subject ID (`TSSID`). `TSSID` is structured as `{Meridian_Study_Index}-{sequential_random_number}`. The mapping secret is vaulted.
    -   **Step 3C (Minimize):** The pipeline automatically drops:
        -   The `CO` (Comments) domain entirely.
        -   Variables annotated as `Origin = CRF Collected` and `QRS = Yes` (Questionnaire, Rating Scale) where verbatim text is freeform, unless a specific variable exemption exists.
    -   **Step 3D (Partition):** Data is written into an Apache Iceberg table format in a secured S3 Data Lake, partitioned by `StudyID`.

### 5.4 Phase 4: CDISC Compliance and Structural Validation

1.  **OpenCDISC/Define-XML Check:** The Data Steward validates the supplied Define-XML metadata against the actual XPT file contents using the Pinnacle 21 Community tool.
2.  **Standard Conformance Rules:**
    -   **Rule SD0037:** Check that all AE (Adverse Events) records have a populated `AETERM` (Reported Term for the AE).
    -   **Rule LB0042:** Check that Lab Test results in LB domain with `LBTOX=’Y’` have a populated `LBTOXGR` (Toxicity Grade).
3.  **Non-Conformance Handling:** If a dataset fails a Pinnacle 21 check with a severity of "Error," ingestion is paused. If it fails with a "Warning" severity, a data conformance waiver must be signed by the Clinical Data Steward and stored in the Meridian Document Management System (DMS) linked to the trial.

### 5.5 Phase 5: Clinical Data Quality and Harmonization

The Clinical Data Engineer executes the harmonization routine using the Meridian Integrated Mapping Layer (MIML) on AWS Glue.

1.  **Adverse Event Harmonization:** `AETERM` is mapped to MedDRA (Medical Dictionary for Regulatory Activities) Preferred Terms (PT) and System Organ Class (SOC). The mapping logic uses a validated dictionary lookup table within Snowflake. Unmapped terms are routed to a QA queue for manual coding.
2.  **Medication Harmonization:** Concomitant medications (`CMTRT` in CM domain) are mapped to WHODrug Global dictionary. A fuzzy string matching algorithm (`T_CM_HARMONIZE`) attempts mapping; a confidence score > 90 is auto-accepted; lower scores are routed for manual review.
3.  **Safety Signal Check:** A mandatory aggregate query checks for any 1.5x disproportionality in SAE reporting compared to the sponsor’s Clinical Study Report summary table. Variance triggers a Clinical Scientist investigation.
4.  **Outlier Detection:** Numeric lab data (`LBTESTCD` = select tests) is subjected to an interquartile range (IQR) outlier check. Outliers are not removed automatically; a Quality Flag variable (`LBQUAL_N` = 1) is added to the dataset row. The dataset is deemed non-suitable for AI training until 100% of Quality Flag rows are reviewed.

### 5.6 Phase 6: Release to ML Feature Store

1.  **Review Gate:** The Clinical Data Steward presents the final Data Quality Dashboard (see Section 7) to Dr. Okafor.
2.  **Approval:** Dr. Okafor approves the batch in the Meridian Metadata Repository (Collibra). This approval triggers the MLflow Experiment Registry to unlock the dataset.
3.  **Lineage Capture:** The SageMaker training job automatically captures the Dataset URI and Version (e.g., `s3://meridian-ml-features/vault/clin/trial_nct0012345_ver_1`) as immutable Run Metadata.

## 6. Controls and Safeguards

### 6.1 Technical Controls
| Control ID | Control Name | Implementation Detail |
| :--- | :--- | :--- |
| **TC-01** | Immutable Audit Logging | AWS CloudTrail enabled for all S3, Lambda, and Glue operations. Logs are stored in a write-once-read-many (WORM) compliant log archive bucket. No delete permissions are granted to root or admin users on this bucket. |
| **TC-02** | Multi-Factor Authentication (MFA) | MFA enforcement policy applied to all IAM roles capable of accessing the Clinical Trial S3 staging or production zones. YubiKey hardware tokens required for privilege escalation. |
| **TC-03** | VPC Isolation | All data transformation Glue jobs run within a private subnet (Meridian-Clinical-Prod-VPC) with no direct internet egress. NAT gateways are disabled for this subnet. |
| **TC-04** | Secrets Vaulting | The `pseudo_engine` Lambda retrieves salt values and the crosswalk storage location from AWS Secrets Manager. Access is restricted to just-in-time (JIT) elevation via PAM. |
| **TC-05** | End-to-End Encryption | TLS 1.3 used for data in transit. All at-rest data in S3 and Snowflake encrypted using AWS KMS customer-managed keys with automatic annual rotation. |

### 6.2 Administrative Controls
| Control ID | Control Name | Implementation Detail |
| :--- | :--- | :--- |
| **AC-01** | Annual Permissions Review | Rachel Kim’s team performs an annual IAM access review. A report is produced and reviewed with Dr. Okafor. Any stale accounts or permissions exceeding least-privilege baselines are remediated within 14 days. |
| **AC-02** | Monthly EU/EEA Subject Validation (GDPR-Specific) | Dr. Weber’s Data Protection Office performs a manual reconciliation of processed NCT records against sponsor Data Privacy Notices to ensure the Article 14 transparency obligation (Indirect Collection) has been discharged. |

## 7. Monitoring, Metrics, and Reporting

The Clinical Data Integration program success is tracked via a real-time PowerBI dashboard, refreshed from Snowflake query logs and the Clinical Metadata Repository (Collibra). A monthly QMR (Quarterly Management Review) deck is produced by the Clinical AI QA Lead and reviewed by the VP of Clinical AI Products.

### 7.1 Key Performance Indicators (KPIs)

| # | Key Performance Indicator | Target Threshold | Measurement Methodology |
| :--- | :--- | :--- | :--- |
| **KPI-1** | **Integrated Record Completeness** | ≥ 98% | Ratio of successful row insertions to total rows received in source XPT files. Failures logged to `sop_clin_003_log`. |
| **KPI-2** | **CDISC Domain Conformance** | Pass (No Errors) | Number of Pinnacle 21 “ERROR” findings from Phase 4 validation. The metric is binary (Pass/Fail) for production approval. |
| **KPI-3** | **Ingestion Timeliness** | 95% within 7 business days | Time from DTA signature receipt (`status=dta_done`) to successful data landing in Iceberg table. |
| **KPI-4** | **Pseudonymization Efficacy** | 100% | Binary scan of all DM-domain tables ensuring no raw original `SUBJID` or `USUBJID` strings exist in production schemas. |
| **KPI-5** | **Data Minimization Efficiency (GDPR)** | ≥ 90% | Percentage of imported SDTM domains where Free Text variables have been correctly stripped or pseudo-tokenized out of total imported domains. |
| **KPI-6** | **Manual Coding Queue Backlog** | < 24 hours TAT | Median time a verbatim term (e.g., `AETERM`) sits in the Manual Harmonization Queue (MIML-Queue-1) before clinical expert review and resolution. |

### 7.2 Reporting Cadence
- **Daily:** Automated Jenkins job `sop-clin-003-dq-report` sends an email to the Clinical Data Engineering distribution list containing the pass/fail result of the previous night's scheduled ingestion jobs.
- **Weekly:** The Data Steward compiles the "Weekly Trial Data Harmonization Backlog" report, distributed to Dr. Okafor and the Clinical Science team leads.
- **Monthly:** Dr. Okafor and the DPO Office review the "Data Protection Compliance Dashboard," specifically reviewing the Log of Article 15 Access Requests (Subject Access Requests) attempting to query integrated trial data.

## 8. Exception Handling and Escalation

Deviations from this SOP must follow a strict governance path to ensure accountability without halting critical AI safety research.

### 8.1 Exception Classification
- **Level 1 (Informational):** Minor deviations captured in automated logs that do not impact data quality (e.g., a source file using a deprecated CDISC controlled terminology version, but still mapping correctly). Auto-approved by the pipeline, logged for retrospective review.
- **Level 2 (Clinical Discretion):** Waiver of a specific Pinnacle 21 "Warning," or ingestion of a non-standard raw domain. Requires completion of form FRM-CLIN-008.
    - *Approver:* Clinical Data Steward.
    - *Notification:* VP of Clinical AI Products.
- **Level 3 (Regulatory/Privacy):** Urgent risk of PII re-identification, ingestion of data without an executed DTA, or a material finding in a DPIA. Level 3 exceptions trigger a stop-work order for the specific trial pipeline.
    - *Approver:* VP of Clinical AI Products (Dr. Okafor) AND Chief Privacy Officer (Dr. Weber).
    - *Escalation Path:* Immediate notification to the Chief Medical Officer (Dr. Priya Patel) and General Counsel.
    - *Remediation SLA:* Work must not resume until a formal corrective action report (CAR) is presented within 5 business days.

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum
All personnel assigned to roles in Section 3 are required to complete the training modules listed below.

| Training Module Code | Module Name | Assigned Roles | Frequency | Assessment |
| :--- | :--- | :--- | :--- | :--- |
| **TR-CLIN-003A** | Foundations of CDISC SDTM & ADaM | Data Engineer, Data Steward, Clinical Scientist | Annually | 80% pass rate on 50-question MCQ |
| **TR-CLIN-003B** | Meridian Pseudonymization Pipeline & Secrets Vault | Data Engineer, DevOps | Annually/Upon Deployment | Practical Lab (HashiCorp Vault Query) |
| **TR-CLIN-003C** | GDPR in Practice: Clinical Data Repurposing | Data Steward, Product Manager, DPO Office, Clinical Scientist | Semi-Annually | 90% pass rate on quiz covering Art. 9(2)(j) derogation & Art. 89 safeguards |
| **TR-CLIN-003D** | SOP-CLIN-003 Revision Walkthrough | All Applicable Roles | Upon Effective Date | Electronic Attestation in Workday |

### 9.2 Training Tracking and Enforcement
Workday serves as the Learning Management System (LMS) of record. Before an engineer is granted write-access to the `prod-clinical-ai` AWS environment (via Active Directory group `AZ-RO-CLINICAL-ENG`), the SailPoint IdentityIQ integration queries Workday to validate that all training assignments are in `Completed` status. Expired training triggers an automated revocation of administrative Snowflake and S3 privileges.

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- **SOP-CLIN-002:** AI Model Training and Algorithm Change Control
- **SOP-CLIN-004:** Medical Imaging Data Onboarding
- **SOP-CLIN-005:** Real-World Evidence (RWE) Data Integration
- **SOP-SEC-001:** Incident Response and Management (For PII re-identification events)
- **SOP-PRIV-101:** Data Privacy Impact Assessment (DPIA) Procedure
- **SOP-QA-101:** Corrective and Preventive Action (CAPA) Process

### 10.2 External References
- **CDISC SDTM Implementation Guide (Version 3.4)**
- **21 CFR Part 11: FDA Electronic Records; Electronic Signatures**
- **EU General Data Protection Regulation (GDPR) 2016/679**
- **EU MDR 2017/745 (Annex II, Technical Documentation)**
- **Pinnacle 21 Community Edition Documentation**

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **1.0** | 2021-03-15 | J. Kim, M. Lefevre | Initial document creation. Established manual upload and basic SDTM validation steps. |
| **2.2** | 2022-01-20 | M. Lefevre, A. Okafor | Added pseudonymization engine (v1.0) and automated AWS Lambda triggers. Introduced role of Clinical Data Steward. |
| **3.0** | 2023-08-01 | A. Okafor, H. Weber | Major revision for post-MDR CE marking compliance. Added GDPR Art. 9(2)(j) scientific research derogation framework and explicit DPIA linkage. Replaced legacy FTP dropzone with S3 Pre-signed URLs. |
| **3.1** | 2023-10-10 | A. Okafor, R. Kim | Modified Section 6 (TC-01) to address IAM privilege escalation vulnerability. Enforced MFA for data lake access. Clarified retention lifecycle in Policy Statement. |
| **3.5** | 2024-12-07 | Dr. Aisha Okafor, Clinical Data Engineering Team | Refined Phase 3 ingestion to use Apache Iceberg partitioning. Updated Pinnacle 21 conformance rules (SD0037, LB0042). Updated RACI matrix to reflect new Compliance oversight model. Added detailed KPI thresholds for reporting cadence. Replaced "Subject ID" with "Trial-Specific Subject ID (TSSID)" in pseudonym definitions. |