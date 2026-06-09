---
sop_id: "SOP-DGP-014"
title: "Anonymization and Pseudonymization"
business_unit: "Data Governance & Privacy"
version: "4.1"
effective_date: "2024-09-25"
last_reviewed: "2025-12-02"
next_review: "2026-06-20"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# SOP-DGP-014: Anonymization and Pseudonymization

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework, technical controls, and operational workflows for the anonymization and pseudonymization of personal data and protected health information (PHI) processed by Meridian Health Analytics. The purpose of this document is to:

- Define clear, auditable criteria for determining when anonymization or pseudonymization is required versus when the underlying personal data must remain identifiable.
- Specify approved technical techniques and algorithms for rendering data into an anonymized or pseudonymized state, including permissible transformations, generalization thresholds, and noise injection parameters.
- Govern the lifecycle of pseudonymization keys, including generation, storage, rotation, access control, and destruction.
- Mitigate re-identification risk through rigorous assessment, monitoring, and post-processing controls aligned with the Health Insurance Portability and Accountability Act (HIPAA) and the General Data Protection Regulation (GDPR).
- Enable lawful secondary use of data for research, analytics, and machine learning (ML) model development by ensuring that anonymized data is no longer subject to data protection obligations and pseudonymized data benefits from reduced exposure risk.

### 1.2 Scope

This SOP applies to:

| Scope Area | Coverage |
|---|---|
| **Data Subjects** | All patients, clinical trial participants, health plan members, and consumers whose data is collected, stored, or processed by Meridian. |
| **Data Types** | Structured datasets (CSV, Parquet, database extracts), unstructured clinical notes, DICOM imaging headers, genomic variant files, patient-reported outcomes, wearable device streams, and telemetry logs containing PHI or Personally Identifiable Information (PII). |
| **Business Units** | Data Governance & Privacy (DG&P), Data Engineering Platform (DEP), Research & Advanced Analytics (RAA), Clinical Informatics, Product Development, and any third-party vendor or contractor handling Meridian data. |
| **Processing Environments** | Meridian production Data Lake (AWS S3), Snowflake Data Warehouse, Databricks Unified Analytics Platform, JupyterHub research sandbox, and FHIR API endpoints. |
| **Lifecycle Phases** | Data ingestion, transformation, storage, transfer, analytics, ML training, reporting, archival, and disposal. |
| **Exclusions** | Data that is *not* subject to HIPAA or GDPR, such as publicly available statistics, purely synthetic data generated from noise distributions with no lineage to real individuals, and aggregate reports where no individual-level data can be discerned. However, if aggregate data is later joined with quasi-identifiers, this SOP's re-identification risk procedures immediately apply. |

Any personnel, contractor, or third party handling Meridian data that qualifies as personal data or PHI **must** comply with this SOP irrespective of geographic location.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Anonymization** | The irreversible process of transforming personal data such that the data subject can no longer be identified, taking into account all means reasonably likely to be used (e.g., cost of mounting singling-out, linkability, and inference attacks). Under HIPAA, this corresponds to meeting the Expert Determination or Safe Harbor de-identification standards. Under GDPR, truly anonymized data ceases to be personal data (Recital 26). |
| **Pseudonymization** | The processing of personal data in such a manner that the data can no longer be attributed to a specific data subject without the use of *additional information* (the pseudonymization key). That additional information must be kept separately and subject to technical and organizational measures to ensure non-attribution. Under GDPR Article 4(5), pseudonymized data remains personal data. |
| **Re-identification** | The act of reversing anonymization or pseudonymization by associating data with a known individual, whether through brute-force linkage, statistical inference, background knowledge attacks, or unauthorized access to keys. |
| **Quasi-identifier (QID)** | A variable or combination of variables that, while not a direct identifier (e.g., name, SSN), can be used with reasonable effort to re-identify individuals if linked with external datasets. Examples: date of birth + ZIP code + gender; rare disease diagnosis + admission date. |
| **Key Vault** | The centralized, FIPS 140-2 Level 3 compliant Hardware Security Module (HSM)-backed service used for storing all pseudonymization key material (Hashicorp Vault Enterprise). |
| **Expert Determination (HIPAA)** | The de-identification standard defined at 45 CFR § 164.514(b)(1), wherein a qualified statistician determines that the risk is very small that anticipated recipients could identify an individual, using generally accepted statistical and scientific principles and methods. |
| **Safe Harbor (HIPAA)** | The de-identification standard defined at 45 CFR § 164.514(b)(2), requiring the removal of 18 specific identifiers enumerated in the regulation. |
| **DPIA (GDPR)** | Data Protection Impact Assessment as required by GDPR Article 35 for processing likely to result in high risk to the rights and freedoms of natural persons. |
| **k-anonymity** | A property of a dataset ensuring that for any record, there are at least k-1 other records sharing the same combination of quasi-identifier values. k is a configurable parameter (default: k=25). |
| **l-diversity** | An extension of k-anonymity requiring that each equivalence class has at least `l` well-represented sensitive attribute values, preventing homogeneity attacks. |
| **t-closeness** | A further refinement requiring that the distribution of a sensitive attribute in any equivalence class does not deviate from its distribution in the overall dataset beyond a threshold `t`. |

### 2.2 Acronyms

| Acronym | Meaning |
|---|---|
| **PHI** | Protected Health Information (as defined by HIPAA) |
| **PII** | Personally Identifiable Information |
| **DSAR** | Data Subject Access Request (GDPR) |
| **KMS** | Key Management Service |
| **HARRT** | HIPAA Anonymization & Re-identification Risk Team (internal governance body) |
| **RDS** | Research Data Sandbox |
| **TDE** | Transparent Data Encryption |
| **EHR** | Electronic Health Record |
| **SHA** | Secure Hash Algorithm |
| **HMAC** | Hash-based Message Authentication Code |

---

## 3. Roles and Responsibilities

This section assigns accountability using a RACI model (Responsible, Accountable, Consulted, Informed).

| Activity / Decision | Chief Privacy Officer (CPO) | Data Governance Lead | Data Engineering Lead | Research Analytics Lead | Security Architect | Data Steward (Business) | HARRT | General Counsel |
|---|---|---|---|---|---|---|---|---|
| **1. Policy Authority & Final Approval** | A | R | C | C | C | C | R | I |
| **2. Determining "Identifiable" vs. "Anonymized" Status** | A | C | C | R | I | C | R | I |
| **3. Approving Re-identification Risk Score Threshold** | C | A | I | C | I | I | R | I |
| **4. Approving Pseudonymization Transformations** | A | R | R | R | C | C | C | I |
| **5. Generating, Storing, Rotating Keys** | I | I | A/R | I | C | I | I | I |
| **6. Approving Data Access for Pseudonymized Datasets** | A | R | I | I | I | R | I | I |
| **7. Quarterly Re-identification Attack Testing** | I | R | C | C | A/R | I | R | I |
| **8. Approving Exception to Anonymization Standard** | A | R | C | C | R | I | C | R |
| **9. GDPR Data Subject Requests (Pseudonymized Data)** | A | R | R | I | I | I | I | C |
| **10. Incident Response for Key Compromise** | A | I | R | I | R | I | I | C |

**HARRT (HIPAA Anonymization & Re-identification Risk Team):** A standing committee chaired by a qualified statistician (Dr. Lise Fournier, Director of Statistical Privacy). HARRT meets bi-weekly to review new datasets flagged as high-risk and to certify Expert Determination. Membership consists of Data Governance (1 member), Security Architecture (1 member), Clinical Informatics (1 member), and Legal (1 non-voting advisor).

**Data Stewards:** Assigned to each clinical domain (Cardiology, Oncology, Genomics, etc.). Responsible for maintaining the Business Glossary that tags columns as "Direct Identifier," "Quasi-Identifier," or "Non-Identifying."

---

## 4. Policy Statements

This section sets forth the high-level policy commitments that govern all downstream procedures.

### 4.1 Default Posture

1. **Privacy by Design (PbD):** All new data pipelines, analytics projects, and product features must undergo a Privacy Impact Screening (Form PRV-102) during the Solution Design Review (SDR) gate. The screening output dictates whether data must be pseudonymized at rest, anonymized before use, or kept fully identifiable within a hardened enclave.

2. **Default Pseudonymization:** Any dataset containing PHI or PII that is moved out of a production Electronic Health Record (EHR) system or claims adjudication engine **must** be pseudonymized at rest unless an explicit exception is granted (Section 8). Production Direct Identifiers (name, SSN, medical record number) **must** be stripped and replaced with a system-assigned opaque pseudonym.

3. **HIPAA De-identification Standard:** Meridian adopts the **Expert Determination** method (45 CFR § 164.514(b)(1)) as the primary operational standard for creating de-identified data for analytics. Safe Harbor (45 CFR § 164.514(b)(2)) is used strictly for externally published reports and is verified by a two-person review.

### 4.2 Anonymization Commitments

1. **Irreversibility:** Anonymization processes must be mathematically proven to be one-way functions or destructive transformations such that the original identifiers cannot be retrieved. Salting and hashing with key destruction **must** be applied.
2. **k-anonymity Threshold:** All datasets released to non-production environments must satisfy **k ≥ 25** for all quasi-identifier equivalence classes. Meridian establishes 25 as a "commercially reasonable" high-water mark for health data.
3. **Prohibition of Re-identification:** Any deliberate attempt to re-identify anonymized data is a violation of the Meridian Code of Conduct and may result in termination and civil/criminal referral. Authorized "attack testing" under Section 7 is the sole exception.

### 4.3 Pseudonymization Commitments

1. **Separation of Domains:** The pseudonymization mapping table (linking clear-text identifiers to pseudonyms) **must** be stored in an isolated, hardened database schema ("Pseudonym Vault") physically and logically separated from the analytic data lake environment.
2. **Key Rotation:** Symmetric keys used for pseudonymization must be rotated every **90 days**. Deprecated keys must be retained for a minimum of 7 years for audit purposes but disabled and moved to offline cold storage.
3. **Data Subject Rights:** Data subjects whose pseudonymized data is held within the Meridian Data Lake shall have rights regarding access, rectification, and erasure (GDPR) or amendment and accounting of disclosures (HIPAA). Procedures must ensure that a DSAR can be traced to all associated pseudonyms.

---

## 5. Detailed Procedures

This section comprises the bulk of the operational workflow. It is broken down into five distinct procedural phases.

### 5.1 Phase I: Project Intake and Data Classification

**Step 5.1.1: Project Registration.** The Project Lead logs the analytic initiative in the Meridian Compliance Portal (ServiceNow module "Privacy-CMP"), registering the specific data sources, anticipated consumer base, and purpose limitation.

**Step 5.1.2: Column-Level Classification.** The Data Steward runs the automated "DataSight Classifier" script against the source schema. This script cross-references the Meridian Data Catalog to tag every column:

| Tag | Criteria |
|---|---|
| `DIRECT_ID` | Column contains HIPAA direct identifiers (Name, SSN, MRN, etc.) or GDPR Art. 4(1) identifiers. |
| `QID` | Column is classified as a high-risk quasi-identifier (ZIP3, DOB, rare disease diagnosis, procedure date). |
| `SENSITIVE_ATTRIBUTE` | Column contains diagnosis, procedure, medication, genomic variant, or financial data not a QID. |
| `NON_PII` | Column contains administrative or free-text verified as non-re-identifiable. |

**Step 5.1.3: Determination of Output State.** Based on the classification, the Project Lead selects one of three target output states:
1.  **Pseudo_Analysis:** Dataset retains `SENSITIVE_ATTRIBUTE` tags, has `DIRECT_ID` substituted by pseudonym. Used for longitudinal analysis. Subject to full Governance oversight.
2.  **Anon_Publication:** Dataset is fully anonymized. All `DIRECT_ID` removed. `QID` processed via k-anonymity engine. Used for public health publications.
3.  **Anon_Sandbox:** Dataset is anonymized for internal model training. `DIRECT_ID` destroyed. `QID` generalized.

### 5.2 Phase II: Pseudonymization Execution

**Step 5.2.1: Direct Identifier Extraction.** Using the AWS Glue "PHI-Extractor" job, all columns tagged `DIRECT_ID` are read from the source (Snowflake/S3). The job validates checksums to ensure complete read before applying transformations.

**Step 5.2.2: Cryptographic Key Retrieval.** The Glue job authenticates via IAM role `pseudo-exec-role` to the Hashicorp Vault. The active pseudonymization key (`pseudo-key-v-current`) is retrieved. The key material is processed only in-memory (never logged).

**Step 5.2.3: Opaque Pseudonym Generation.** Meridian uses HMAC-SHA3-512 (keyed-hashing) to generate the pseudonym.
- **Input:** `DIRECT_ID` value + a static 64-byte Meridian-specific salt.
- **Transformation:** `Pseudonym = HMAC-SHA3_512(key, [salt + identifier])`.
- **Truncation:** Output truncated to 64 characters for legacy system compatibility.
- **Collision check:** A uniqueness constraint is enforced; no two distinct identifiers may map to the same pseudonym.

**Step 5.2.4: Mapping Table Persistence.** The mapping `{Pseudonym_Value, Source_Table, Source_Column, Transformation_Timestamp}` is written to the `pseudo_vault.mappings` schema in the isolated PostgreSQL instance on an EC2 Dedicated Host. The `DIRECT_ID` value is *not* written to the vault as plain text; it is wrapped with a Vault transit encryption key for an additional layer of envelope encryption.

**Step 5.2.5: Analytic Data Delivery.** The Glue job writes the analytic dataset (with `DIRECT_ID` columns replaced by the `Pseudonym` value) to the approved S3 bucket prefix `s3://meridian-data-lake/pseudonymized/<project_id>/`.

### 5.3 Phase III: Anonymization Execution (Expert Determination)

This process is owned by HARRT (Dr. Lise Fournier).

**Step 5.3.1: Re-identification Risk Assessment.** For a new dataset destined for anonymization, a formal statistical risk assessment must be completed using the `ARX De-identification Tool` integrated with the Meridian DataBricks platform. The process includes:
1.  **Threat Modeling:** Identify plausible attackers (e.g., data journalist with public census data, curious clinician, competitor with commercial data-broker data). Assign each plausible attacker a "Motivation" and "Capability" score (low/med/high).
2.  **Vulnerability Analysis:**
    -   *Singling Out:* Calculate the proportion of unique records in the dataset.
    -   *Linkability:* Using the probabilistic linkage engine, compare against the "Shadow Data" repository (a collection of publicly available datasets: Census, voter registration, hospital rankings).
    -   *Inference:* Determine the confidence with which a sensitive attribute can be inferred from non-sensitive attributes.

**Step 5.3.2: Application of Transformations.** Based on the HARRT-approved transformation plan, the Data Engineering team applies a series of Privacy Models to the QIDs using the `MeridianPrivacyLib` (Python library wrapping ARX):

| Privacy Model | Parameter | Default Meridian Threshold | Application |
|---|---|---|---|
| **k-Anonymity** | `k` | `k = 25` | Applied to all QIDs. Exceptions for rare disease cohorts (k=5) require GC & CPO sign-off. |
| **l-Diversity** | `l` | `l = 5` (distinct sensitivity) | Applied to groupings of diagnosis codes and medications. |
| **t-Closeness** | `t` | `t = 0.15` (EMD distance) | Applied to high-sensitivity genomic variant files, age, and race. |
| **δ-Presence** | `δ_min`, `δ_max` | `[0.15, 1.25]` | Applied to datasets representing a sub-cohort sampled from a larger public registry. |

**Transformations include:**
-   **Generalization:** ZIP code 02139 → 0213\*. Diagnosis date: 2023-05-15 → 2023-Q2.
-   **Suppression:** Records with insufficient k-map size are suppressed entirely (row deletion).
-   **Sub-sampling / Differential Privacy:** For genomic data, calibrated Laplace noise with epsilon ε=1.0 is introduced.

**Step 5.3.3: Safe Harbor Scrub (Supplementary).** Once Expert Determination is complete, a separate Safe Harbor pipeline (`SH-Scrubber`) automatically scans free-text fields (clinical notes, radiology reports) to remove 18 HIPAA identifiers using a Named Entity Recognition (NER) model trained on MIMIC-IV and i2b2 data sets.

**Step 5.3.4: Certification & Sign-Off.** Dr. Fournier signs a "Certificate of Anonymization" (Form ANON-104). The cert records the specific statistical techniques, thresholds used, and the final re-identification risk score (Section 6.2). The certificate is valid for **12 months**, after which revalidation is required if the external data landscape is judged to have changed materially.

### 5.4 Phase IV: Data Subject Rights (Pseudonymized Data)

Data subject requests for information, amendment, or deletion against pseudonymized datasets trigger a specific tracing procedure.

**Step 5.4.1: Request Validation.** The Privacy Operations Team validates the data subject's identity using a government-issued ID and verifies the Meridian "master identifier" (EID) in the CRM.

**Step 5.4.2: Pseudonym Tracing.** Privacy Operations submits a ticket (Jira `PRV`) to Data Engineering. The Data Engineer, using the `pseudo-trace` CLI tool with elevated privileges, queries the `pseudo_vault.mappings` table against the subject's EID to extract all associated pseudonyms across all analytic datasets.

**Step 5.4.3: Data Aggregation and Review.** The relevant data tables are queried using the extracted pseudonym list. The output is aggregated into a structured report. The Privacy Operations Team reviews the report and prepares a response communication. The standard procedure aims to fulfill requests within the regulatory frameworks; timelines for data subject responses are managed through the Privacy Operations case management system and coordinated with the CPO office for alignment with specific data subject request requirements.

### 5.5 Phase V: Pseudonymization Key Lifecycle Management

| Key State | Trigger Event | Action | Execution |
|---|---|---|---|
| **Creation** | New project | Key generated via HashiCorp Vault API `HSM/generate-key`. Algorithm: AES-256-GCM. | Automated via Terraform `vault_key` resource. |
| **Active** | Rotation time | The current active key `pseudo-key-v-current` is updated. A new version is created. | CI/CD pipeline `key-rotation-job`. Runs monthly. |
| **Deactivated** | Replaced by newer version | Key is marked `deactivated` but retained in the Vault for decryption/re-pseudonymization of historical data. | Manual intervention by Security Architect if needed for data recovery. |
| **Compromised** | Security Incident | Immediate revocation. Access policy enforcement. HARRT and CISO launch an Emergency Re-identification Assessment to determine if compromised keys + accessible data = high-risk linkability. | Incident Response workflow `IR-KEY-COMP`. |
| **Destroyed** | Anonymization | As a final step to transform Pseudonymized data to Anonymized data (irreversible), the mapping table is securely cryptographically shredded (NIST 800-88 Purge). The pseudonym keys used to create those pseudonyms are destroyed after verifying no other projects depend on them. | Dual authorization required (CPO + CISO). |

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Mechanism |
|---|---|---|
| **TC-01** | Direct Identifiers must be encrypted at rest and in transit. | AWS KMS envelope encryption for all S3 buckets; TLS 1.3 for all connections. |
| **TC-02** | Pseudonymization mapping table must reside in a separate hardened database instance from the analytic data. | Network segmentation (AWS Security Group `sg-pseudo-vault` allowing ingress only from Glue IAM role). |
| **TC-03** | Anonymization transformation code must be immutable and version-controlled. | Git-based workflow (`master` branch requires HARRT lead approval). All releases tagged. |
| **TC-04** | Access to pseudonymized data in the Data Lake must be role-based and time-bound. | AWS IAM roles. Access grants are limited to 90 days and require Data Steward and Project Lead approval. |
| **TC-05** | Attempts to re-identify pseudonymized data by joining datasets with external, unapproved tables must be automatically blocked. | Databricks Unity Catalog row-level filters and column-masking policies. |
| **TC-06** | All data movements (extraction, loading, transformation) must be fully logged. | AWS CloudTrail logging for all S3/Glue API calls, forwarded to Sumo Logic SIEM for UEBA analysis. |

### 6.2 Administrative Controls

| Control ID | Control Description | Metric |
|---|---|---|
| **AC-01** | Annual mandatory "Privacy & Anonymization" training (see Section 9). | Completion Rate > 98%. |
| **AC-02** | Bi-weekly review by HARRT of all datasets classified as "High Risk." | Review Completion: 100% within SLA. |
| **AC-03** | Quarterly re-identification penetration testing by external red team. | Red team must report no successful re-identification of datasets classified as `k=25`. |
| **AC-04** | Annual review and approval of this SOP. | Review completion by `next_review` date. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The Data Governance & Privacy Unit tracks the following, viewable on the Executive Privacy Dashboard (Tableau):

| Metric | Calculation | Target | Frequency |
|---|---|---|---|
| **Anonymized Dataset Output** | Count of distinct datasets achieving HARRT certification. | -- | Monthly |
| **Average k-anonymity Realized** | Mean `k`-value across all equivalence classes in all certified datasets released in the period. | `k ≥ 30` | Monthly |
| **Pseudonymization Coverage** | % of Data Lake tables containing PHI that have `DIRECT_ID` columns pseudonymized at rest. | 99.5% | Weekly |
| **DSAR Pseudonym Trace SLA** | Time from validated DSAR to completion of pseudonym tracing (Step 5.4.2). | Mean < 72 hours | Monthly |
| **Key Rotation Compliance** | % of active pseudonymization keys with `last_created` date > 90 days. | 0% (all within limit) | Weekly |
| **Open HARRT Remediation Findings** | Number of open findings requiring re-processing of a dataset due to failed risk thresholds. | < 5 (at any point) | Bi-weekly |

### 7.2 Audit Log Review

The Security Operations Center (SOC) Tier 2 analysts review the SIEM dashboard for anomalies daily. Specific UEBA rules monitor:
- A single user executing >50 pseudonym look-ups in 10 minutes.
- Detected network traffic between the pseudonymized data S3 bucket and an unregistered external IP address.
- A Glue job failing the `pseudo-exec-role` authentication >3 times in sequence.

The Director of Security Architecture reviews the quarterly SIEM summary.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

| Exception ID | Exception Type | Example Scenario |
|---|---|---|
| **EXC-01** | Low k-anonymity Threshold | Rare disease genomic cohort where `k=5` is the only viable grouping before data becomes useless. |
| **EXC-02** | Pseudonymized Data Export to Untrusted Environment | A clinical research partner requires a dataset where pseudonyms must be re-derived using their own salt schema. |
| **EXC-03** | Identifiable Data Retention Override | Longitudinal study where full identifiers must be retained for 15+ years for ongoing patient re-contact consent. |
| **EXC-04** | Algorithm Deviation | Use of a non-standard differential privacy algorithm (e.g., RAPPOR vs. MeridianPrivacyLib) for a specific ML application. |

### 8.2 Exception Handling Workflow

**Step 8.2.1: Submission.** The Project Lead submits "Exception Request Form" (FRM-EXC-101) in the Compliance Portal. The form requires detailed justification, a risk assessment, and proposed compensating controls.

**Step 8.2.2: Risk Analysis.** The CPO or their delegate conducts a Privacy Impact Analysis, scoring the exception on a scale of 1 (Negligible) to 5 (Critical) residual privacy risk.

**Step 8.2.3: Approval Authority.**
- **Risk Score 1-2:** Data Governance Lead approval.
- **Risk Score 3-4:** CPO approval, with documented compensating controls (e.g., enhanced auditing, restricted access).
- **Risk Score 5:** Executive Risk Committee (CPO, CISO, GC) approval required. Exception has a fixed maximum 12-month expiry and must be reviewed quarterly.

**Step 8.2.4: Escalation.** If an exception request is denied by the CPO, the Project Lead may escalate to the Chief Data Officer (CDO). The CDO and GC hold the final decision authority for business-critical projects.

---

## 9. Training Requirements

### 9.1 Curriculum

| Module | Course Code | Target Audience | Content | Duration |
|---|---|---|---|---|
| **General Privacy & Data Ethics** | DGP-TRN-101 | All personnel | Distinction between anonymized/pseudonymized/de-identified data. Meridian's commitment to not re-identify. Reporting channels. | 45 min |
| **Technical Anonymization for Engineers** | DGP-TRN-201 | Data Engineering, Platform, DevOps | ARX tool usage, `MeridianPrivacyLib` implementation, key management via Vault API, tagging logic. | 3.5 hrs |
| **Statistical Risk Assessment** | DGP-TRN-301 | HARRT Members, Sr. Data Scientists | Threat modeling, k-anonymity/l-diversity mathematical foundations, DPIA methodology, NIST SP 800-188 de-id guidance. | 8.0 hrs |

### 9.2 Frequency and Tracking

- **Frequency:** Annual refresher. Role-specific changes trigger a new assignment within 90 days.
- **Tracking:** Compliance is tracked via the Workday Learning Management System (LMS). A mandatory compliance score of 100% on the post-course quiz is required for modules DGP-TRN-201 and DGP-TRN-301.
- **Non-Compliance:** System access to analytic tools (Databricks, Snowflake) is automatically suspended 7 days past the training due date.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Policy Name | Relationship to This SOP |
|---|---|---|
| **SOP-DGP-003** | Data Classification and Handling | Source for column-level tagging rules applied in Phase I. |
| **SOP-DGP-009** | Data Subject Access Request (DSAR) Management | Governs the overall DSAR workflow into which tracing in Phase IV is plugged. |
| **SOP-IS-015** | Cryptographic Key Management | Provides the foundational key management standards for the Vault described in Phase II and V. |
| **SOP-RAA-021** | Research Data Sandbox (RDS) Access | Describes the environment for which Anon_Sandbox data is provisioned. |
| **SOP-CS-008** | Information Security Incident Response | Governs the execution of a key compromise response. |

### 10.2 External References

| Standard | Reference |
|---|---|
| **HIPAA Privacy Rule** | 45 CFR § 164.514 (a)-(c) (Requirements regarding de-identification). |
| **GDPR** | Recital 26 (Not applicable to anonymous data); Article 4(5) (Pseudonymisation). |
| **NIST** | Special Publication 800-188 (De-identifying Government Datasets). |
| **ISO** | ISO/IEC 20889:2018 (Privacy enhancing data de-identification terminology and classification of techniques). |

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 4.1 | 2025-12-02 | Dr. Klaus Weber | Minor update: Added genomic data differential privacy parameter (ε=1.0) to Section 5.3.2; clarified key rotation SLA in Section 5.5. |
| 4.0 | 2024-09-25 | Dr. Klaus Weber | Major revision: Migrated anonymization standard from Safe Harbor (v3.x) to Expert Determination as primary; introduced HARRT governance; bumped k-anonymity default from 11 to 25; integrated new `MeridianPrivacyLib` library. |
| 3.2 | 2024-03-10 | J. Chen (DG&P) | Remediation update: Tightened DSAR tracing procedures and aligned with new HashiCorp Vault API for key management; added technical controls table. |
| 3.1 | 2023-08-15 | J. Chen (DG&P) | Added Databricks Unity Catalog column-masking integration to technical controls; updated reporting metrics to reflect CloudTrail migration. |
| 3.0 | 2023-01-20 | Dr. Klaus Weber | Full rewrite to align with CE marking under EU MDR and GDPR Chapter IV obligations. Introduced formal DPIA integration points. |