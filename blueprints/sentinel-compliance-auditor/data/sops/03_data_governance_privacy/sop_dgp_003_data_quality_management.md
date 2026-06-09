---
sop_id: "SOP-DGP-003"
title: "Data Quality Management"
business_unit: "Data Governance & Privacy"
version: "4.0"
effective_date: "2025-06-15"
last_reviewed: "2026-04-01"
next_review: "2026-10-23"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Data Quality Management

**SOP-ID:** SOP-DGP-003
**Version:** 4.0
**Effective Date:** 2025-06-15
**Owner:** Chief Privacy Officer / DPO
**Classification:** Internal

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for Data Quality Management (DQM) at Meridian Health Technologies, Inc. The purpose of this SOP is to ensure that all data assets—whether used in clinical decision support, financial transactions, population health analytics, or platform operations—meet defined quality standards that safeguard patient safety, financial integrity, regulatory compliance, and operational excellence.

Data quality is a foundational requirement for Meridian's mission to deliver trustworthy AI-powered healthcare fintech solutions. Poor data quality in any business line can propagate through machine learning models, financial calculations, and clinical recommendations, creating cascading risks. This SOP defines the systematic controls necessary to identify, measure, remediate, and prevent data quality issues across the data lifecycle.

### 1.2 Scope

This SOP applies to:

| **In Scope** |
|--------------|
| All structured and unstructured data ingested, stored, processed, or transmitted by Meridian systems, including the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform |
| All data environments: production, staging, testing, development, and disaster recovery (AWS us-east-1, eu-west-1, Azure DR) |
| All personnel—employees, contractors, vendors, and third-party partners—who create, collect, process, manage, or consume Meridian data assets |
| Data across all architectural layers: ingestion pipelines (Kafka), data warehousing (Snowflake), operational databases (PostgreSQL, Redis), vector stores (Pinecone), and ML feature stores |
| Protected Health Information (PHI), Personally Identifiable Information (PII), financial transaction data, clinical data, and synthetic data used for model training |

| **Out of Scope** |
|------------------|
| Physical security controls for data centers (addressed in SOP-IS-007, *Physical Security Management*) |
| Network security and perimeter defense (addressed in SOP-IS-012, *Network Security Operations*) |
| Business Continuity and Disaster Recovery (addressed in SOP-BC-005) |

### 1.3 Applicability by Business Unit

| Business Unit | Critical Data Quality Domains |
|---------------|-------------------------------|
| Clinical AI Platform | Clinical data completeness and accuracy for diagnostic imaging, patient risk scores, adverse event prediction |
| HealthPay Financial Services | Transaction integrity, claims data accuracy, credit model input consistency, regulatory reporting data |
| MedInsight Analytics | PHI completeness, care gap identification accuracy, outcomes data reliability |
| Meridian SaaS Platform | Multi-tenant data isolation integrity, system log quality, monitoring data accuracy |

---

## 2. Definitions and Acronyms

### 2.1 Acronyms

| Acronym | Definition |
|---------|------------|
| DQM | Data Quality Management |
| DQ | Data Quality |
| PHI | Protected Health Information |
| PII | Personally Identifiable Information |
| SLA | Service Level Agreement |
| KPI | Key Performance Indicator |
| DQ-DL | Data Quality Defect Log |
| DQ-IR | Data Quality Incident Report |
| DQ-SC | Data Quality Steering Committee |
| DQWG | Data Quality Working Group |
| ETL/ELT | Extract, Transform, Load / Extract, Load, Transform |
| FMEA | Failure Mode and Effects Analysis |
| RACI | Responsible, Accountable, Consulted, Informed |
| DPO | Data Protection Officer |
| CISO | Chief Information Security Officer |
| CCO | Chief Compliance Officer |

### 2.2 Definitions

| Term | Definition |
|------|------------|
| **Data Quality** | The degree to which a data asset meets the requirements for its intended use, measured across defined dimensions. |
| **Data Quality Dimension** | A measurable characteristic of data that defines its fitness for use. Meridian recognizes seven core dimensions (see Section 2.3). |
| **Data Quality Metric** | A quantifiable measure that evaluates a specific DQ dimension against a defined threshold. |
| **Data Quality Rule** | An automated or manual check that validates data against defined business or technical requirements. |
| **Data Quality SLA** | A formal agreement defining minimum acceptable data quality levels, measurement methodology, and remediation timelines for a given data asset or data product. |
| **Data Quality Incident** | A confirmed breach of a defined DQ SLA that results in or could result in business impact. |
| **Critical Data Element (CDE)** | A data element designated as essential to patient safety, financial integrity, regulatory compliance, or core business operations. All CDEs are subject to mandatory quality controls. |
| **Data Profiling** | The systematic analysis of data content, structure, and relationships to identify patterns, anomalies, and quality issues. |
| **Data Cleansing** | The process of detecting and correcting (or removing) corrupt, inaccurate, or inconsistent records from a dataset. |
| **Data Lineage** | Documentation of the data's origins, movements, transformations, and destinations throughout its lifecycle. |
| **Golden Record** | A single, authoritative, consolidated representation of an entity (e.g., patient, provider, payer) derived from multiple source systems. |
| **Data Steward** | A designated individual responsible for the quality of a defined data domain within their business unit. |
| **Data Owner** | A senior leader with accountability for the data assets within their business function. |

### 2.3 Data Quality Dimensions

Meridian evaluates data quality across the following seven dimensions. Each dimension must be measured for all Critical Data Elements and is required for all data products published to production environments.

| Dimension | Definition | Example (Clinical AI) | Example (HealthPay) |
|-----------|------------|------------------------|---------------------|
| **Completeness** | The proportion of data records that contain all expected values for mandatory attributes. | Percentage of radiology images with complete DICOM header metadata. | Percentage of claims with a valid CPT code and provider NPI. |
| **Accuracy** | The degree to which data correctly represents the real-world object or event it describes. | Correctness of tumor size measurement in structured report vs. clinical ground truth. | Accuracy of patient responsibility calculation against payer contract terms. |
| **Consistency** | The absence of logical contradictions across datasets and systems. | Patient allergy profile matches between EMR feed and Meridian ingestion database. | Patient demographic data matches across claims, payment, and enrollment records. |
| **Timeliness** | The degree to which data represents the current state of the real-world object within required time windows. | ICU vital signs data latency < 5 minutes for real-time deterioration scoring. | Payment posting reflected in patient ledger within 15 minutes of batch processing. |
| **Uniqueness** | No record, attribute, or entity instance is duplicated within a dataset. | Single patient record exists per unique patient identifier; no duplicate MRN entries. | No duplicate payment transactions for the same claim line item. |
| **Validity** | Data conforms to defined business rules, formats, enumerations, and value ranges. | Lab result values fall within clinically plausible ranges; LOINC codes are valid. | ICD-10 codes are valid and match the current code set version. |
| **Integrity** | Referential integrity is maintained across related datasets; relationships are complete and accurate. | All patient encounters reference a valid patient record (no orphaned encounters). | All payment transactions reference a valid claim record. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for Data Quality Management at Meridian. Each named role has specific obligations defined in their position descriptions and performance objectives.

| Role | Responsibility | RACI Assignment |
|------|---------------|-----------------|
| **Chief AI Officer (CAIO)** | Chairs the DQ-SC; approves DQ SLAs for AI/ML data products; authorizes exceptions to enterprise DQ standards. | Accountable for DQ program governance |
| **Chief Privacy Officer / DPO (Dr. Klaus Weber)** | Owns this SOP; defines data quality policies; ensures DQ practices support privacy and data protection obligations. | Accountable for DQ policy; Responsible for SOP content |
| **Chief Medical Officer (CMO)** | Defines clinical data quality thresholds; can issue clinical holds on systems with unsafe DQ levels. | Accountable for clinical DQ; Consulted on clinical rules |
| **Chief Information Security Officer (CISO)** | Ensures DQ controls preserve data confidentiality and security posture. | Consulted on security-impacting DQ controls |
| **Chief Compliance Officer (CCO)** | Validates DQ controls for regulated data (HIPAA, MDR, 510(k) submission data). | Accountable for regulatory DQ |
| **Data Stewards (per Business Unit)** | Perform data profiling; define and maintain DQ rules; monitor DQ dashboards; resolve DQ incidents within SLA. | Responsible for day-to-day DQ operations |
| **VP, Clinical AI Engineering** | Submits Clinical AI data quality evidence packages for CAIO approval; remediates DQ incidents in Clinical AI pipelines. | Responsible for Clinical AI data quality |
| **VP, HealthPay Engineering** | Submits HealthPay data quality evidence packages; maintains financial data DQ rules; remediates DQ incidents. | Responsible for HealthPay data quality |
| **VP, Data Platform Engineering** | Maintains Jira Service Management DQ dashboards; ensures TSM correctly routes DQ tickets; supports automated DQ rule deployment. | Responsible for DQ infrastructure |
| **Director of Analytics (MedInsight)** | Defines and monitors DQ SLAs for MedInsight reporting data; validates report data accuracy. | Responsible for analytics DQ |
| **ML Engineering Directors (per product)** | Ensure training data and feature stores meet DQ standards; document data lineage for ML pipelines. | Responsible for ML data quality |
| **All Personnel** | Report suspected DQ issues upon discovery; adhere to data entry standards; complete DQ awareness training. | Informed of DQ responsibilities |

### 3.1 Data Quality Steering Committee (DQ-SC)

The DQ-SC meets monthly and is the governance body for enterprise data quality. Membership:

- **Chair:** Chief AI Officer
- **Standing Members:** CPO/DPO, CMO, CISO, CCO, VP-Data Platform Engineering, VP-Clinical AI Engineering, VP-HealthPay Engineering, Director of Analytics
- **Rotating Members:** One Data Steward per business unit per quarter

The DQ-SC is responsible for approving enterprise DQ SLAs, reviewing Critical Data Element classification, resolving escalated DQ incidents, and endorsing DQ tooling investments.

### 3.2 Data Quality Working Group (DQWG)

The DQWG meets bi-weekly and comprises all Data Stewards and key engineering leads. The DQWG manages operational DQ issues, reviews profiling results, recommends CDE classification changes, and proposes rule updates to the DQ-SC.

---

## 4. Policy Statements

Meridian Health Technologies commits to the following data quality policies:

### 4.1 Data Quality by Design

Data quality requirements must be defined during the design phase of any new system, pipeline, or data product—not retrofitted post-implementation. All new data product proposals must include a Data Quality Plan covering the seven dimensions, proposed SLAs, Critical Data Element classification, and automated validation rules.

### 4.2 Mandatory Profiling

All new data sources must undergo mandatory data profiling prior to integration into any production pipeline. Profiling results must be documented in the source system onboarding package and reviewed by the relevant Data Steward. Profiling must include: column-level statistics (null counts, distinct values, value distributions), pattern analysis, data type conformance, cross-column relationship checks, and completeness scoring.

### 4.3 Critical Data Element Governance

Critical Data Elements must be formally classified, documented, and assigned to a named Data Steward. Each CDE must have: a defined minimum quality threshold across applicable dimensions, automated monitoring with real-time alerting, a documented quality issue resolution procedure, and defined escalation path for SLA breaches.

### 4.4 Data Quality SLA Enforcement

All data published to production environments is subject to Data Quality SLAs. SLA violations trigger the incident management process defined in Section 8. Chronic SLA violations ( > 3 breaches in a rolling 30-day window ) require a formal remediation plan approved by the DQ-SC Chair.

### 4.5 Prohibition of Unassessed Data

Data that has not undergone profiling and quality assessment, or data that does not meet minimum quality thresholds for its intended use, is prohibited from use in clinical decision support, financial model input, regulatory submissions, or patient-facing systems.

### 4.6 Data Cleansing Standards

Data cleansing must be performed at the source of the quality issue whenever feasible. If source cleansing is not possible, the cleansing transformation must be: fully documented in data lineage records, approved by the relevant Data Steward, logged with cleansing metadata (records affected, transformation applied, timestamp), and auditable for regulatory review.

### 4.7 PHI/PII Integrity

All PHI and PII datasets must meet 100% uniqueness and referential integrity standards. Any duplicate patient records or orphaned clinical records must be escalated to the DPO and CMO within 4 hours of detection.

---

## 5. Detailed Procedures

This section defines the operational procedures for Data Quality Management. All procedures assume use of the Jira Service Management (JSM) ticketing system for workflow tracking.

### 5.1 Procedure: New Data Source Onboarding and Profiling

**Objective:** Ensure all new data sources meet defined quality standards before integration into Meridian production environments.

**Frequency:** Performed once per new data source onboarding event.

**Responsible:** Business Unit Data Steward, with support from Data Platform Engineering.

#### 5.1.1 Onboarding Steps

**Step 1: Initiate Onboarding Request**
- The requesting team submits a "Data Source Onboarding Request" via JSM using the Data Governance project workflow.
- The request must specify: source system name, data owner/requestor, business justification, intended use(s), estimated volume, update cadence (real-time, batch, etc.), and whether the data contains PHI/PII.
- JSM auto-assigns a unique Onboarding ID (format: ONB-YYYY-NNNN).

**Step 2: Assign Data Steward**
- The DQ-SC Chair (or delegate) assigns a Data Steward based on the business domain of the requesting team.
- The assigned Steward acknowledges the assignment in JSM within 2 business days.
- If the data spans multiple business units, a lead Steward is assigned with coordination responsibility.

**Step 3: Preliminary Risk Classification**
- The assigned Data Steward classifies the data source risk level using the following matrix:

| Risk Level | Criteria | Required Controls |
|------------|----------|-------------------|
| **High** | Data feeds clinical decision support, financial transaction processing, regulatory submission, or is PHI/PII | Full profiling, all 7 DQ dimensions, real-time monitoring, CDE classification |
| **Medium** | Data supports analytics, internal reporting, or model training (non-clinical) | Full profiling, 5 dimensions (Completeness, Accuracy, Validity, Timeliness, Uniqueness), daily monitoring |
| **Low** | Internal operational data, non-critical reporting | Standard profiling, 3 dimensions (Completeness, Validity, Uniqueness), weekly monitoring |

**Step 4: Execute Data Profiling**
- The Data Steward initiates profiling using Meridian's approved Data Quality toolset (Soda DQ for data warehouse sources, Monte Carlo for pipeline-native sources, or manual SQL profiling for low-volume sources).
- Profiling must execute over a representative sample period as follows:
  - Batch sources: Minimum 3 full load cycles
  - Streaming/real-time sources: Minimum 72 hours of continuous data
  - One-time/snapshot sources: Full dataset analysis
- Profiling output includes: record counts and uniqueness checks, null value analysis per column (completeness assessment), value distribution and pattern analysis, data type and format conformance check, cross-column consistency analysis, referential integrity checks against existing catalogs (e.g., ICD-10, LOINC, CPT, NPI), and range/boundary analysis for numeric fields.

**Step 5: Document Profiling Results**
- Profiling results are documented in a "Data Quality Profiling Report" (template FORM-DQP-v2.0 in JSM).
- The report includes: source metadata, profiling methodology, summary statistics per dimension, identified anomalies and data quality defects, a DQ Defect Log for each identified issue, and recommended Critical Data Element designations.

**Step 6: Defect Remediation**
- Each defect identified during profiling is logged as a DQ Defect in JSM (linked to the Onboarding ID).
- Defects are prioritized:
  - **Critical (P1):** Defect renders data unfit for critical clinical or financial use; must be remediated before source integration.
  - **Major (P2):** Defect impacts key DQ dimension below SLA threshold; remediation plan required before source integration; temporary conditional integration may be approved.
  - **Minor (P3):** Defect identified but does not breach SLA; tracked for resolution within 30 days.
- The source team remediates Critical and Major defects. The Data Steward re-profiles to confirm resolution.

**Step 7: Source Integration Approval**
- Upon satisfactory profiling and P1/P2 defect resolution, the Data Steward submits a "Source Integration Approval" in JSM.
- Approval includes: final DQ profile summary, approved DQ SLA levels, classified CDEs with assigned stewards, and defined DQ monitoring rules.
- The DQ-SC Chair (or delegate for Low-risk sources) approves integration.
- Data Platform Engineering executes the approved integration pipeline.

### 5.2 Procedure: Data Quality Rule Implementation

**Objective:** Define and deploy automated data quality validation rules that enforce DQ SLAs.

**Frequency:** Initial implementation per data source; ongoing maintenance as business rules change.

**Responsible:** Data Steward (rule definition), Data Platform Engineering (technical deployment).

#### 5.2.1 DQ Rule Types

| Rule Type | Description | Example |
|-----------|-------------|---------|
| **Completeness Check** | Validates that mandatory columns do not contain NULL values. | `claims.cpt_code IS NOT NULL` |
| **Validity Check** | Validates data against reference datasets, enumerations, or format patterns. | `diagnosis.icd10_code IN (SELECT code FROM ref.icd10_codes)` |
| **Uniqueness Check** | Detects duplicate records based on defined key columns. | `COUNT(DISTINCT patient_mrn) = COUNT(*)` |
| **Consistency Check** | Cross-table or cross-system validation. | `SELECT * FROM ingestion.patients p LEFT JOIN emr.feed_patients e ON p.mrn = e.mrn WHERE p.allergy_profile != e.allergy_profile` |
| **Accuracy Check** | Validates against trusted source or reference standard. | `payment.patient_responsibility = calculated_responsibility_per_contract` (within 1% tolerance) |
| **Timeliness Check** | Validates data freshness. | `MAX(ingestion_timestamp) >= NOW() - INTERVAL '15 minutes'` |
| **Range/Boundary Check** | Validates numeric values fall within plausible or expected bounds. | `lab_results.value BETWEEN lab_results.ref_range_low AND lab_results.ref_range_high` OR flagged as abnormal |
| **Referential Integrity Check** | Validates foreign key relationships. | All `encounter.patient_mrn` exist in `patients` table |

#### 5.2.2 Rule Deployment Steps

**Step 1: Rule Specification**
- Data Steward documents each rule in the "DQ Rule Specification" form within JSM.
- Each rule is linked to: the target dataset/source system ID, applicable DQ dimension(s), CDE designation if applicable, severity (Critical/Major/Minor), threshold for alerting (e.g., > 0.1% violation rate triggers alert; > 1.0% triggers Incident), and remediation guidance.

**Step 2: Technical Review**
- Data Platform Engineering reviews the rule for technical feasibility and performance impact.
- For rules targeting Snowflake, rules are implemented as Soda DQ checks.
- For real-time/streaming rules targeting Kafka topics, rules are implemented via Monte Carlo monitors or custom Flink/KSQL-based validation logic.

**Step 3: Alert Configuration**
- Data Platform Engineering configures alerting in JSM OpsGenie integration.
- P1 (Critical) rule violations trigger immediate OpsGenie alerts to the owning Data Steward, the relevant VP Engineering, and the DQ-SC distribution list.
- P2 (Major) rule violations trigger JSM ticket creation within 15 minutes.
- P3 (Minor) rule violations are logged to the DQ monitoring dashboard for weekly review.

**Step 4: Test and Validate**
- Rules are deployed to a staging environment first.
- Data Steward validates that rules detect known quality issues correctly and do not generate excessive false positives.
- After validation, rules are promoted to production.

### 5.3 Procedure: Data Cleansing

**Objective:** Correct identified data quality defects in a controlled, auditable manner while maintaining data lineage.

**Responsible:** Source system team (preferred); Data Steward (approval and oversight).

#### 5.3.1 Cleansing Decision Framework

When a data quality defect is identified, the following decision framework determines the approach:

```
Data quality defect identified
    │
    ├── Can source system correct the root cause?
    │       ├── YES → Source correction (preferred path)
    │       │       │ 1. Document root cause
    │       │       │ 2. Request source correction via JSM
    │       │       │ 3. Validate correction in source
    │       │       │ 4. Re-profile data at ingestion
    │       │       │ 5. Close JSM defect ticket
    │       │
    │       └── NO → Assess cleansing approach
    │               ├── Automated transformation in pipeline?
    │               │       ├── YES → Implement pipeline cleansing (see 5.3.2)
    │               │       └── NO → Manual cleansing (see 5.3.3)
    │               │
    │               └── Is historical correction required?
    │                       ├── YES → Initiate backfill/retroactive cleanse
    │                       └── NO → Future-only correction
```

#### 5.3.2 Automated Pipeline Cleansing

**Step 1: Define Cleansing Rule**
- Data Steward documents the required corrective transformation.
- Examples: NULL value defaults for non-critical fields, data type casting, reference data mapping (e.g., mapping deprecated codes to current codes), deduplication logic ("keep first/last record by timestamp").

**Step 2: Review and Approve**
- Cleansing rules modifying PHI or clinical data require CMO approval (for clinical fields) or DPO approval (for privacy-sensitive fields).
- Cleansing rules modifying financial data require VP, HealthPay Engineering approval.
- All automated cleansing rules require CAIO or delegate approval.

**Step 3: Implement and Document**
- Data Platform Engineering implements the transformation rule in the ingestion/ETL pipeline (dbt models).
- The transformation is documented including: transformation logic, fields affected, justification, approver, and effective date.
- Data lineage is updated in the Collibra data catalog to reflect the cleansing transformation.

**Step 4: Validate**
- Data Steward validates cleansed output against defined DQ rules.
- A 72-hour monitoring period follows deployment, during which elevated alert sensitivity is configured.

#### 5.3.3 Manual Cleansing

Manual cleansing is reserved for scenarios where:
- Source correction is not feasible within required timelines.
- Automated transformation is not possible due to complex business logic.
- One-time correction of historical data is required.

Manual cleansing must be:
- Performed using documented SQL scripts or approved data manipulation tools.
- Executed with a second reviewer approval (peer-reviewed change control).
- Logged with full audit trail: who executed, what records were modified, what transformation was applied, timestamp of execution, and approval ticket reference.
- Confirmed via post-cleansing DQ rule re-validation.

### 5.4 Procedure: Data Quality Assessment for Model Training Data

**Objective:** Validate that training data for AI/ML models meets required quality standards before use.

**Responsible:** ML Engineering Director, with review by Data Steward.

**Procedure Steps:**

1. **Identify Training Data Sources:** Catalog all datasets used for model training.
2. **Profile Each Source:** Execute profiling for completeness, accuracy, and consistency as defined in 5.1.
3. **Assess Sample Representativeness:** Validate that training data adequately represents the target population, including edge cases.
4. **Label Quality Assessment:** For supervised learning datasets, validate label quality—accuracy of clinical annotations, correctness of structured labels (e.g., ICD-10 codes for disease classification), and inter-rater reliability for expert-annotated datasets.
5. **Document in Model DQ Package:** Results are documented in a Model Data Quality Package that includes: source data profiling summaries, label quality assessment results, known DQ defects and their accepted risk rationale, remediation applied (cleansing, augmentation), and CAIO acceptance signature.
6. **Model Training Approval:** The CAIO must approve the Model Data Quality Package before the model enters training. No model may be promoted to staging validation without this approval.

### 5.5 Procedure: Data Quality Monitoring and Dashboard Review

**Objective:** Ensure continuous visibility into DQ metrics against established SLAs.

**Frequency:** Weekly review by Data Stewards; Monthly review by DQ-SC.

**Procedure:**

1. **Automated Monitoring:** Soda DQ and Monte Carlo execute all deployed DQ rules on their defined schedules.
2. **Dashboard Access:** DQ dashboards are available in two views:
   - **Operational Dashboard (Grafana):** Real-time DQ rule execution status; alert history; current DQ scores per data source.
   - **Governance Dashboard (Looker):** Trended DQ scores per dimension per data source; SLA adherence rates; open defect counts and aging; CDE health summary for DQ-SC monthly review.
3. **Weekly Steward Review:** Each Data Steward reviews their assigned data sources' DQ dashboards weekly. Actions logged in JSM.
4. **Monthly DQ-SC Review:** The CAIO presents the Governance Dashboard summary to the DQ-SC, including enterprise DQ scorecard, top risks, chronic SLA breaches requiring remediation, open Critical (P1) incidents.
5. **Quarterly Executive Review:** The DPO and CAIO provide a DQ summary to the Executive Leadership Team as part of the Data Governance quarterly review.

---

## 6. Controls and Safeguards

The following technical and administrative controls are implemented to ensure adherence to this SOP.

### 6.1 Preventative Controls

| Control ID | Control Description | Implementation |
|------------|---------------------|----------------|
| DQC-001 | **Schema Validation on Ingestion:** All production data pipelines validate schema conformity before data is committed to persistent storage. | Kafka topic schemas registered in Confluent Schema Registry with compatibility modes. |
| DQC-002 | **Mandatory Field Enforcement:** Database-level NOT NULL constraints on all identified mandatory fields. | PostgreSQL DDL constraints; Snowflake table definitions. |
| DQC-003 | **Referential Integrity Constraints:** Foreign key constraints enforced at the database level where feasible. | PostgreSQL FK constraints. Where FK constraints are not feasible (e.g., cross-database relationships), automated DQ rules monitor referential integrity. |
| DQC-004 | **Lookup Reference Validation:** All enumerated/coded data validated against Meridian maintained reference datasets. | Soda DQ validity checks against Snowflake reference tables updated each code set release. |
| DQC-005 | **Data Lineage Registration:** All production data assets must have lineage registered in the Collibra data catalog. | Collibra integration with dbt metadata for transformation lineage. |

### 6.2 Detective Controls

| Control ID | Control Description | Implementation |
|------------|---------------------|----------------|
| DQC-006 | **Automated DQ Rule Execution:** All deployed DQ rules execute on defined schedules with real-time violation alerting. | Soda DQ (batch Snowflake checks); Monte Carlo (real-time and pipeline monitors). |
| DQC-007 | **Data Drift Monitoring:** ML feature store data monitored for statistical distribution drift. | Monte Carlo drift detection monitors on Snowflake feature tables. |
| DQC-008 | **Duplicate Record Detection:** Uniqueness rules deployed for all CDEs and entity master records. | Soda DQ uniqueness checks; custom deduplication logic for Golden Record creation. |
| DQC-009 | **Latency Monitoring:** Kafka pipeline lag monitoring; batch job completion monitoring. | Datadog pipeline monitors; JSM alerting on batch job failure or extended runtime. |

### 6.3 Corrective Controls

| Control ID | Control Description | Implementation |
|------------|---------------------|----------------|
| DQC-010 | **JSM Incident Management Workflow:** All DQ SLA breaches automatically create JSM incidents routed to the responsible Data Steward. | JSM automation rules triggered by monitoring alerts. |
| DQC-011 | **Data Cleansing Approval Gate:** All automated cleansing transformations require Data Steward approval and are versioned in dbt. | dbt code review workflow; JSM approval gate. |
| DQC-012 | **Rollback Capability:** Data transformation errors detected post-release can be reverted via dbt rollback and data partition reprocessing. | dbt version control and deployment pipeline supports rollback; Snowflake Time Travel enabled for 90-day window. |

### 6.4 Administrative Controls

| Control ID | Control Description | Implementation |
|------------|---------------------|----------------|
| DQC-013 | **Annual DQ SOP Review:** This SOP undergoes mandatory annual review and approval by the CPO/DPO and General Counsel. | Document revision workflow in JSM. |
| DQC-014 | **DQ Training** | See Section 9. |
| DQC-015 | **Vendor/Third-Party DQ Requirements:** All third-party data providers must meet DQ requirements defined in their Data Processing Agreements. | Supplier management review per SOP-LGL-009, *Third-Party Data Management*. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following enterprise KPIs are tracked monthly and reported to the DQ-SC:

| KPI ID | Metric | Target | Calculation |
|--------|--------|--------|-------------|
| KPI-DQ-01 | **Enterprise DQ Score** | ≥ 98% | Weighted average of DQ dimension scores across all CDEs. |
| KPI-DQ-02 | **SLA Adherence Rate** | ≥ 99% | Percentage of CDEs meeting all defined DQ SLA thresholds during the measurement period. |
| KPI-DQ-03 | **Critical Incident Count** | 0 | Number of confirmed P1 DQ Incidents in the period. |
| KPI-DQ-04 | **Mean Time to Detect (MTTD) - Critical** | < 1 hour | Time from defect introduction to automated alert generation. |
| KPI-DQ-05 | **Mean Time to Resolve (MTTR) - Critical** | < 4 hours | Time from incident creation to resolution confirmation. |
| KPI-DQ-06 | **Open Defect Aging** | No P1 > 24 hours; No P2 > 7 days; No P3 > 30 days | Time since defect creation for unresolved defects. |
| KPI-DQ-07 | **Profiling Coverage** | 100% of production data sources | Percentage of production data sources with current ( < 12 month ) profiling documentation. |
| KPI-DQ-08 | **Training Compliance** | ≥ 95% | Percentage of assigned personnel current on DQ training (see Section 9). |

### 7.2 Key Performance Indicators by Business Unit

| Business Unit | Additional KPI | Target |
|---------------|----------------|--------|
| Clinical AI Platform | **Clinical Data Completeness** - Percentage of patient encounters with complete mandatory clinical data elements. | ≥ 99.5% |
| Clinical AI Platform | **Image Metadata Integrity** - Percentage of radiology images with valid, consistent DICOM metadata. | ≥ 99.9% |
| HealthPay Financial Services | **Payment Accuracy** - Percentage of payment postings with correct patient responsibility calculation (validated against contract terms). | ≥ 99.95% |
| HealthPay Financial Services | **Duplicate Payment Rate** - Instances of duplicate payments per million claims processed. | ≤ 1 per million |
| MedInsight Analytics | **Golden Record Match Rate** - Percentage of records successfully matched to Golden Patient Record without manual intervention. | ≥ 98% |

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Owner |
|--------|----------|-----------|-------|
| DQ Operational Scorecard | Data Stewards, DQWG | Weekly (automated) | Data Platform Engineering |
| DQ Governance Dashboard | DQ-SC | Monthly | CAIO |
| Enterprise DQ Executive Summary | Executive Leadership Team | Quarterly | DPO (Dr. Weber), CAIO |
| Regulatory DQ Report (for applicable products) | CCO, CMO | Quarterly | CCO |
| Annual DQ Program Review | Board of Directors / Audit Committee | Annual | CAIO, DPO |

---

## 8. Exception Handling and Escalation

### 8.1 Data Quality Incidents

A Data Quality Incident is formally declared when a P1 DQ rule violation is confirmed, or any DQ SLA breach persists for more than one measurement cycle.

#### 8.1.1 Incident Declaration

- Automated P1 alert triggers JSM incident creation.
- The assigned Data Steward acknowledges the incident within 30 minutes of alert.
- The Data Steward assesses impact and either: (a) confirms the incident and assigns severity, or (b) closes as false positive with root cause analysis for rule refinement.

#### 8.1.2 Severity Classification

| Severity | Definition | Examples |
|----------|-----------|----------|
| **P1 - Critical** | Immediate threat to patient safety; financial loss in progress; regulatory reporting impacted; core platform functionality impacted. | Inaccurate patient allergy data propagating to clinical decision support; duplicate payments actively processing; PHI integrity breach. |
| **P2 - Major** | Data unfit for intended use in a production system; SLA breach confirmed; no immediate patient/financial harm but operational impact significant. | Batch claims processing delayed due to invalid ICD-10 codes; reporting data showing material inaccuracies. |
| **P3 - Minor** | DQ SLA breach detected but impact limited to non-critical analytics or internal reporting; minor discrepancies. | Data freshness delayed beyond SLA for non-critical dashboard; minor data inconsistency identified without business impact. |

#### 8.1.3 Incident Response Procedure (P1 and P2)

**Step 1: Triage (0-30 minutes)**
- Data Steward acknowledges incident in JSM.
- Data Steward performs initial impact assessment: affected data, systems, business processes.
- If clinical impact suspected, CMO is immediately notified.
- If PHI/PII impact suspected, DPO is immediately notified.
- If financial impact suspected, VP HealthPay Engineering is immediately notified.

**Step 2: Containment (0-2 hours)**
- Data Steward coordinates with Data Platform Engineering to isolate affected data pipeline if ongoing ingestion is compounding the issue.
- If downstream systems are consuming bad data, implement circuit-breaker pattern: stop data publication to downstream consumers; notify downstream system owners via JSM.
- Snowflake Time Travel is leveraged to identify the pre-incident clean data state.

**Step 3: Root Cause Analysis (2-8 hours, parallel)**
- Engineering team performs technical root cause analysis.
- Data Steward assesses business process root cause (e.g., source system change, data entry procedure failure).
- Findings documented in JSM incident record.

**Step 4: Remediation (duration per severity)**
- P1 resolution target: < 4 hours from incident declaration.
- P2 resolution target: < 24 hours from incident declaration.
- Remediation includes: source correction if feasible; data cleansing for affected records (per Section 5.3); DQ rule adjustment if false-negative detection failure identified; affected downstream data or reports regeneration.

**Step 5: Verification and Closure**
- Remediation actions validated: DQ rules re-executed confirming compliance; representative data sample manually reviewed; impacted downstream teams confirm data integrity.
- Incident summarized with timeline, root cause, impact, remediation, and preventative actions.
- Incident closure approved by CAIO (P1) or relevant VP Engineering (P2).

### 8.2 Exceptions to DQ SLA

There are circumstances where a temporary exception to a DQ SLA may be necessary (e.g., source system migration, planned downtime, new data source stabilization). Exceptions must follow the formal exception process:

**Step 1: Exception Request Submission**
- Requestor submits a "DQ SLA Exception Request" in JSM.
- Required fields: affected data source(s), affected DQ rule(s) and dimension(s), exception justification, business impact assessment (including residual risk acceptance), proposed start and end dates for exception period, mitigating controls during exception period.

**Step 2: Exception Review**
- Data Steward reviews and documents: current DQ score for affected dimension, trend analysis, risk of cascading impact.
- CISO, DPO, and/or CMO consulted as required by data classification.

**Step 3: Exception Approval Authority**

| Exception Duration | Risk Level | Approver |
|--------------------|------------|----------|
| ≤ 24 hours | Any | Data Steward (with notification to DQ-SC Chair) |
| 24 hours - 7 days | Low/Medium | CAIO or delegate |
| 24 hours - 7 days | High | CAIO + relevant domain officer (CMO for clinical; DPO for PHI; VP Eng for financial) |
| > 7 days | Any | Full DQ-SC approval |

**Step 4: Exception Monitoring**
- Approved exceptions are tracked on the DQ governance dashboard as a separate category.
- If the exception period must be extended, a new exception request must be submitted before the original expiration.
- All exceptions, including emergency verbal approvals, must be retroactively documented in JSM within 1 business day.

### 8.3 Escalation Matrix

| Escalation Level | Trigger | Escalate To | Response Time |
|------------------|---------|-------------|---------------|
| **Level 1 - Standard** | P1 incident declared | CAIO, relevant VP Engineering | Immediate (automated alert) |
| **Level 2 - Clinical Safety** | P1 incident with potential patient safety impact | CMO (in addition to Level 1) | Within 15 minutes of clinical impact assessment |
| **Level 3 - Privacy/Regulatory** | P1 incident involving PHI integrity, potential breach | DPO, CCO (in addition to Level 1) | Within 1 hour |
| **Level 4 - Executive** | Incident unresolved beyond MTTR target; multiple concurrent P1 incidents | Executive Leadership Team notification via CAIO | Within 4 hours of Level-1 escalation if unresolved |
| **Level 5 - Board/Material** | P1 incident with potential material financial, legal, or public safety impact | General Counsel, CEO notification | Within 24 hours per Incident Response Plan SOP-IR-001 |

---

## 9. Training Requirements

### 9.1 Required Training

All personnel covered by this SOP must complete the following training:

| Training Module | Audience | Frequency | Delivery Method | Tracking |
|-----------------|----------|-----------|-----------------|----------|
| **DQM-101: Data Quality Awareness** | All personnel | Annual | LMS online course with knowledge assessment | Workday Learning |
| **DQM-201: Data Quality for Data Stewards** | All Data Stewards | Annual + on new Steward assignment | LMS + live workshop with DQWG lead | Workday Learning; JSM tracked workshop registration |
| **DQM-301: Critical Data Element Management** | Data Stewards assigned to CDEs; VP Engineering | Biennial (every 2 years) | Live workshop with CPO/DPO | Workday Learning |
| **DQM-401: PHI Data Quality** | All roles handling PHI data | Annual | LMS online course; includes HIPAA refresher elements | Workday Learning |
| **DQM-501: DQ Monitoring Tooling** | Data Stewards, Data Platform Engineers | On tooling version upgrade or role change | Vendor-provided training + internal lab | JSM tracked |

### 9.2 Training Compliance Tracking

- Training completion is tracked in Workday Learning.
- Managers receive automated monthly training compliance dashboards for their direct reports.
- 95% compliance threshold is measured as of the training due date. Individuals not compliant within 30 days of due date receive an automated reminder; within 60 days, their manager receives an escalation; within 90 days, non-compliance is reported to the DQ-SC and may result in access restrictions to affected systems.

### 9.3 Role-Based Training Mapping

| Role Group | Required Modules | Initial Onboarding Deadline | Recurring Deadline |
|------------|------------------|-----------------------------|---------------------|
| All Personnel | DQM-101 | Within 30 days of start | Annual from date of last completion |
| Data Stewards | DQM-101, DQM-201, DQM-501 | Within 30 days of Steward assignment | Annual (201, 501); Biennial (301) |
| VP/Director Engineering (Clinical AI, HealthPay, Data Platform) | DQM-101, DQM-201, DQM-301, DQM-501 | Within 60 days of role assumption | As per matrix |
| DQ-SC Members | DQM-101, DQM-201, DQM-301 | Within 60 days of committee appointment | Annual (101); Biennial (201, 301) |
| Personnel with PHI access | DQM-101, DQM-401 | Within 30 days of access grant | Annual |

---

## 10. Related Policies and References

### 10.1 Meridian Internal Policies

| SOP-ID | Document Title | Relationship |
|--------|---------------|--------------|
| SOP-DGP-001 | Data Governance Framework | Parent governance policy; defines Data Owner and Data Steward appointment process |
| SOP-DGP-002 | Data Classification and Handling | Defines PHI/PII/Confidential classification levels referenced in this SOP |
| SOP-DGP-004 | Data Lineage and Metadata Management | Defines Collibra catalog standards and lineage registration requirements |
| SOP-IS-007 | Physical Security Management | Controls for physical data access |
| SOP-IS-012 | Network Security Operations | Network controls for data in transit |
| SOP-IS-014 | Access Control Management | Role-based access provisioning; access review cadence |
| SOP-BC-005 | Business Continuity and Disaster Recovery | Data recovery prioritization and RTO/RPO definitions |
| SOP-SDM-001 | Secure Software Development Lifecycle | Data quality requirements in system design phase |
| SOP-MLO-001 | ML Model Lifecycle Management | Model training data quality requirements; model validation |
| SOP-IR-001 | Incident Response Plan | P1/P2 incident response procedure; executive escalation |
| SOP-LGL-009 | Third-Party Data Management | DQ requirements for third-party data providers |

### 10.2 External Standards and References

| Reference | Description |
|-----------|-------------|
| ISO 8000-61 | Data Quality Management Process Reference Model |
| DAMA-DMBOK 2nd Edition | DAMA Guide to the Data Management Body of Knowledge; Data Quality Management chapter |
| ISO 25012 | Data Quality Model for software product quality |
| HIPAA Security Rule (45 CFR § 164.308) | Administrative safeguards for ePHI integrity |

### 10.3 Meridian Tooling References

| Tool | Purpose | Business Owner |
|------|---------|---------------|
| Soda DQ | Automated data quality checks on Snowflake | Data Platform Engineering |
| Monte Carlo | Data observability, pipeline monitoring, drift detection | Data Platform Engineering |
| Collibra | Data catalog, lineage, and metadata management | Data Governance & Privacy (Dr. Weber) |
| Jira Service Management (JSM) | DQ incident management, exception workflow, onboarding workflow | Data Platform Engineering |
| dbt | Data transformation and cleansing rule implementation | Data Platform Engineering |
| Workday Learning | Training assignment and compliance tracking | Human Resources |
| Grafana | Operational DQ dashboards | Data Platform Engineering |
| Looker | Governance DQ dashboards | Data Governance & Privacy |

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|---------------------|
| 1.0 | 2021-09-10 | Dr. Klaus Weber (CPO) | Initial release. Defined foundational DQ dimensions, profiling procedures, and Steward roles. |
| 1.1 | 2022-02-14 | Dr. Klaus Weber (CPO) | Minor revision: Added MTTD/MTTR KPIs; clarified Data Steward appointment process for new sources. |
| 2.0 | 2022-11-01 | Dr. Klaus Weber (CPO) | Major revision: Introduced CDE classification framework; added Golden Record definition; expanded HealthPay-specific DQ requirements; integrated post-HealthPay-acquisition data sources. |
| 2.1 | 2023-06-20 | Maria Gonzalez (GC) on behalf of Dr. Weber | Minor revision: Updated legal references to reflect CE marking under EU MDR; added third-party DQ requirements (SOP-LGL-009 reference). |
| 3.0 | 2024-03-15 | Dr. Klaus Weber (CPO) | Major revision: Restructured procedures section; introduced severity classification (P1/P2/P3) and formal incident management; added Section 5.4 (Model Training Data DQ) for Clinical AI Platform; expanded tooling references to Soda DQ and Monte Carlo; added Section 9 Training Requirements; added Section 11 Revision History. |
| 3.1 | 2024-11-08 | Dr. Klaus Weber (CPO) | Minor revision: Updated escalation matrix to reflect current organizational structure; updated Data Steward roster appendix; revised KPI-DQ-04 target from 2 hours to 1 hour; added quarterly executive reporting requirement. |
| 4.0 | 2025-06-15 | Dr. Klaus Weber (CPO) | Major revision: Full restructure for clarity and operational precision. Added detailed procedure for exception handling (Section 8.2); introduced risk-based profiling levels (Section 5.1, Step 3); added Cleansing Decision Framework (Section 5.3.1); expanded Controls and Safeguards section with control IDs; updated roles for new organizational alignment; added KPI-DQ-07 and KPI-DQ-08; revised document metadata to reflect EU AI Act and NIST AI RMF regulatory applicability. |

---

**Document Control:**
- This document is controlled in the Meridian Policy Management System (JSM Confluence).
- Printed copies are uncontrolled and valid only on the date of printing.
- The most current version of this SOP is maintained at: `https://meridian-confluence.internal/policies/SOP-DGP-003`
- Questions regarding this SOP should be directed to: `dgovernance@meridian-health.com`

--- END OF SOP-DGP-003 ---