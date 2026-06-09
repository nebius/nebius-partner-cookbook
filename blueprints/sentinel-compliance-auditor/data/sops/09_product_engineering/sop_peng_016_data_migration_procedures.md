---
sop_id: "SOP-PENG-016"
title: "Data Migration Procedures"
business_unit: "Product & Engineering"
version: "5.5"
effective_date: "2025-05-22"
last_reviewed: "2026-07-23"
next_review: "2027-01-12"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Data Migration Procedures

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the standardized framework, governance, and technical controls governing all data migration activities across Meridian Health Technologies, Inc. ("Meridian"). Given the organization's stewardship of protected health information (PHI) across its Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the underlying Meridian SaaS Platform, uncontrolled data migration poses unacceptable risks to data integrity, patient safety, and regulatory compliance. This document prescribes the end-to-end lifecycle management to ensure that every data migration event is executed with precision, traceability, and a fully validated rollback capability.

### 1.2 Scope
This SOP applies to all employees, contractors, vendors, and temporary personnel involved in the planning, authorization, execution, validation, and post-migration monitoring of data movement within or between the following environments:

| Environment Type | Description | Examples |
|---|---|---|
| Production Environments | Live systems handling active patient, provider, or financial data | Clinical AI Platform (us-east-1, eu-west-1), MedInsight production clusters |
| Staging/Pre-Production | Environments that mirror production and may contain de-identified production data | Pre-prod SageMaker endpoints, staging Snowflake instances |
| Development & Testing | Non-production environments used for engineering | Dev sandboxes, QA clusters, local development databases |
| Disaster Recovery (DR) | Standby environments used for business continuity | Azure DR regions, AWS cross-region replicas |
| Third-Party SaaS Tools | Approved ancillary tools containing business-critical data | Observability platforms, ticketing systems, CRM instances |

**In-Scope Migration Types:**
- **Platform Migrations:** Movement of datasets between cloud providers or regions (e.g., AWS to Azure, eu-west-1 to us-east-1).
- **Storage Tier Migration:** Relocation of data between hot, warm, and cold storage classes (e.g., S3 Standard to S3 Glacier Deep Archive).
- **Schema/Structural Migration:** Database refactoring, table restructuring, or index rebuilds in PostgreSQL, Snowflake, or Redis clusters.
- **Application-Level Migration:** Re-platforming data as part of a product upgrade (e.g., migrating patient risk scores from a legacy Python service to a new Kubeflow pipeline).
- **Ingestion Pipeline Changes:** Modifications to how data is imported into the Meridian ecosystem via Apache Kafka or AWS Kinesis.
- **EOL/EOS System Decommissioning:** Migration of data away from end-of-life systems per SOP-IT-042 (Asset Lifecycle Management).

**Out of Scope:**
This SOP does not cover routine data backups and restores managed by the IT Operations team (see SOP-IT-008, Backup and Recovery Operations), nor does it cover the continuous real-time data streaming which is governed by SOP-PENG-022 (Stream Processing and Event Management). Standard single-record updates through application interfaces are also excluded.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
|---|---|
| **PHI** | Protected Health Information, as defined under HIPAA 45 CFR § 160.103. Any individually identifiable health information held or transmitted by Meridian. |
| **ePHI** | Electronic Protected Health Information. All PHI created, received, maintained, or transmitted in electronic form. |
| **CDSM** | Clinical Decision Support Mechanism. A tool within the Clinical AI Platform that provides patient-specific assessments or recommendations. |
| **Migration Owner** | The senior engineer or architect accountable for the success of a specific migration event. |
| **IdP** | Identity Provider (Okta). Centralized authentication and authorization mechanism for all Meridian systems. |
| **KMS** | Key Management Service (AWS KMS, HashiCorp Vault). Cryptographic key lifecycle management tools used for data encryption. |
| **ETL/ELT** | Extract, Transform, Load / Extract, Load, Transform. Methods for moving and reshaping data from sources to targets. |
| **CBDT** | Cutover Binding Decision Time. The point of no return after which the rollback procedure transitions from a fast-fail cutover to a high-effort disaster recovery scenario. |
| **Data Lineage** | The documented lifecycle of data, including its origins, transformations, movements, and consumption within the Meridian ecosystem. |
| **MTD** | Migration Test Dataset. A representative subset of data used for dry-run validation. |
| **Runbook** | An executable sequence of migration steps, including manual checks, automated scripts, and defined exit criteria for each phase. |
| **ACID** | Atomicity, Consistency, Isolation, Durability. Set of properties of database transactions intended to guarantee validity despite errors. |
| **HIPAA Security Rule** | 45 CFR Part 160 and Subparts A and C of Part 164. Standards for the protection of ePHI. |
| **HIPAA Minimum Necessary Standard** | Requirement under HIPAA Privacy Rule § 164.502(b) that only the minimum necessary PHI is accessed or used to accomplish the intended purpose. |

---

## 3. Roles and Responsibilities

The following responsibility matrix applies to all migration activities. A single individual may hold multiple roles only if explicitly approved by the Chief Information Security Officer (CISO, Rachel Kim) and VP of Engineering (David Park).

| Role | Designated Authority | Responsibility |
|---|---|---|
| **Executive Sponsor** | Dr. Sarah Chen (CEO) or Dr. Marcus Rivera (CAIO) | Provides strategic authorization for major migration programs. Final approver for CBDT authorization for migrations impacting >1M patient records. |
| **Migration Governance Board (MGB)** | VP of Engineering, CISO, Chief Privacy Officer/DPO, VP of IT Operations | Reviews and approves all migration requests of "Major" and "Critical" severity. Chaired by the VP of Engineering. |
| **Migration Owner** | Senior Engineer or Engineering Manager (appointed per migration) | Accountable for the complete migration lifecycle: planning documentation, runbook creation, validation sign-off, and post-migration monitoring. Must hold an active Meridian Engineering Certification Level 3. |
| **Data Steward (HIPAA)** | Dr. Priya Patel (CMO) for Clinical; James Thornton (CFO) for Financial | Authorizes the use and movement of PHI, ensuring compliance with the HIPAA Minimum Necessary Standard (§ 164.502(b)). Validates that datasets requested for migration are strictly necessary for the stated business purpose. |
| **Data Protection Officer (GDPR)** | Dr. Lena Voss, DPO (Berlin) | Authorizes migration of personal data of EU residents, ensuring compliance with GDPR data residency requirements, particularly for cross-border transfers. |
| **Security Architect** | InfoSec Senior Manager | Validates encryption-in-transit and at-rest architecture. Confirms IdP integration readiness for the target environment per SOP-IS-014 (Access Control). |
| **Validation Engineer (QE)** | QA Lead, Independent from Dev Team | Independent execution of the Migration Test Dataset (MTD) against the runbook. Records pass/fail exit criteria with digital signatures. Owns the "Validation Complete" gate. |
| **Release Manager** | Product Operations Manager | Approves the integration of the migration runbook into the Meridian Change Advisory Board (CAB) schedule. Manages the cutover communication plan to all stakeholders. |

---

## 4. Policy Statements

### 4.1 General Policy
All data migration activities, regardless of environment or perceived triviality, shall be treated as controlled technical change events.

- **Universal Documentation Policy:** Every migration must have a formal Migration Plan and an approved Runbook prior to execution. No ad-hoc data movement via `psql`, `redis-cli`, or SDK utilities is permitted against production-grade datasets.
- **Zero-Data-Loss Policy:** Every migration must demonstrate a point-in-time rollback capability to the immediate pre-migration state. Data loss incidents during migration shall be immediately escalated to the CISO and VP of Engineering and trigger the Incident Response Protocol (SOP-IS-011).
- **PHI Discovery Policy:** During migration planning, if source schemas are found to contain PHI not previously cataloged, the Migration Owner must halt planning and file a "PHI Storage Anomaly" report with the CISO before proceeding.

### 4.2 HIPAA-Specific Policy Statements
In full compliance with the HIPAA Security Rule (45 CFR Part 164, Subpart C), the following policies are non-negotiable for any data event involving ePHI:

- **Encryption in Transit (§ 164.312(e)(1)):** All data streams containing ePHI must be encrypted end-to-end using TLS 1.3 with Meridian internal Certificate Authority (CA) signed certificates. Termination of TLS at any point other than the application container or database endpoint is prohibited. TLS 1.2 is acceptable only for legacy system interfaces approaching EOL, subject to an approved Security Exception valid for no more than 90 days.
- **Encryption at Rest (§ 164.312(a)(2)(iv)):** The target storage environment must be pre-configured with AES-256 or equivalent encryption. AWS RDS, S3, and Snowflake tables must have encryption enabled using a Meridian-managed KMS key that is rotated per SOP-IS-018 (Key Management). HashiCorp Vault must be the source of truth for all encryption keys.
- **Audit Controls (§ 164.312(b)):** The migration procedure itself must produce an immutable audit trail. The Migration Runbook execution engine must log all steps—including who invoked a step, the timestamp, and the exit code—to the centralized SIEM (Splunk). Audit logs must record the specific PHI datasets accessed, the identity of the accessing process, and a success/failure indicator.
- **Integrity Controls (§ 164.312(c)(1)):** Cryptographic checksums (SHA-512) must be computed on source and target datasets. An electronic mechanism must exist to authenticate the source and target checksums match before a migration can be deemed "Complete."
- **PHI De-identification Policy:** Under HIPAA § 164.514(a), any migration from a Production environment to a Development or QA environment must either (a) involve data fully de-identified via expert determination or Safe Harbor method, or (b) have a fully executed Business Associate Agreement (BAA) in place with the Dev/QA environment owner, treating the Engineering team as an internal workforce member with tightly controlled access.

---

## 5. Detailed Procedures

This section outlines the five-phase lifecycle for a standard data migration event. Each phase contains mandatory sub-steps. Completion of a phase constitutes a formal gate.

### 5.1 Phase 1: Initiation and Impact Assessment
**Gate Owner:** Data Steward (HIPAA) or Product Manager (Non-PHI)

| Step | Action | Responsible Party | Tools |
|---|---|---|---|
| 1.1 | **Ticket Creation:** Create a Migration Request in Jira (Project: `PENG-MIG`, Issue Type: "Data Migration"). Unique Jira ID (e.g., `PENG-MIG-1425`) is generated. | Requester | Jira Service Management |
| 1.2 | **Dataset Classification:** Identify the data to be moved. Run the Meridian Data Classifier (In-House Tool, `mdclass`) against the source catalog. Output a **Data Profile Report** listing the exact schemas, table sizes, presence of regulated data (PHI, PCI, PII), and criticality tier (T0-T3). | Data Analyst | `mdclass`, AWS Glue Catalog |
| 1.3 | **PHI/PCI Determination:** If the Data Profile Report flags PHI/PCI, immediately route to the Data Steward for a "Minimum Necessary" justification. Under HIPAA § 164.514(a), document precisely why the required dataset cannot be de-identified or aggregated. | Requester / Data Steward | Jira `PENG-MIG` form field |
| 1.4 | **Criticality Rating:** The Migration Owner and Data Steward assign an initial criticality rating. | Migration Owner, Data Steward | Internal Rating Matrix (Table 5.1-A) |
| 1.5 | **Go/No-Go Decision:** The MGB convenes (or Chair makes decision for "Minor" migrations). Migration ticket status moves to `IN_PLANNING` or `CLOSED_REJECTED`. | MGB | Jira |

**Table 5.1-A: Migration Criticality Matrix**

| Factor | Minor (Tier 3) | Major (Tier 2) | Critical (Tier 1) |
|---|---|---|---|
| **Data Class** | Non-PHI, Non-PCI, Internal Docs, Dev/Test Logs. | De-identified PHI, Billing/Admin PHI, PCI. | Direct ePHI, Clinical Decision Support inputs, Genomic data. |
| **Maximum Downtime** | < 5 minutes | < 1 hour | Near-Zero (Blue/Green, Canary) |
| **Record Count** | < 100,000 records | 100,000 - 10,000,000 records | > 10,000,000 records OR any number of CDSM inputs |
| **Approval Authority** | Engineering Manager | MGB via asynchronous approval | MGB convened meeting + Executive Sponsor |

*Gate Exit Criteria:* Jira ticket status is `IN_PLANNING`, Criticality Rating assigned, Phase 1 checklist signed off in Jira.

---

### 5.2 Phase 2: Migration Planning and Runbook Creation
**Gate Owner:** Migration Owner

| Step | Action | Responsible Party | Artifacts |
|---|---|---|---|
| 2.1 | **Target Environment Provisioning:** Create the target environment using Infrastructure as Code (IaC) exclusively via the `TF-Meridian-Core` Terraform module repository. Manual console provisioning is disallowed. The IaC must pre-declare encryption at rest, TLS endpoints, and baseline IAM roles. | SRE Team | Terraform Pull Request, Terraform Plan Output |
| 2.2 | **Schema Reconciliation:** Compare source and target schemas using `pgquarrel` or Snowflake's `INFORMATION_SCHEMA` comparators. Generate a delta report of tables, columns, constraints, and indexes. | Database Reliability Engineer (DBRE) | Schema Delta Report (Excel/PDF) |
| 2.3 | **Runbook Authoring:** Write the executable runbook in a Meridian-standard format. The runbook must be a `.yaml` file, compatible with the `meridian-runner` orchestration tool. It must contain at minimum: a) Pre-flight checks (connectivity, authn, capacity); b) Sequence of `EXEC` (executable) steps for the actual migration; c) Sequence of `VALIDATE` steps (row counts, checksums, random sampling); d) A `ROLLBACK` function for each step or logical group of steps. | Migration Owner | `migration-runbook-{Jira-ID}.yaml`, committed to `git.meridian.internal/sre-migrations` |
| 2.4 | **Rollback Plan Documentation:** Explicitly define the Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for the migration rollback. For a `Major` or `Critical` migration, this must include a procedure for a full-point-in-time restore from a pre-migration backup. | Migration Owner | Section within the Runbook header |
| 2.5 | **Dry-Run Execution on MTD:** Execute the runbook against a pre-production environment using the Migration Test Dataset (MTD). The MTD must be a realistic, representative subset of source data, including edge cases (e.g., NULL values, special characters, max-length fields). Record all `VALIDATE` exit criteria results. | Migration Owner (Run), Validation Engineer (Witness) | MTD Validation Log, signed by Migration Owner and Validation Engineer. |
| 2.6 | **HIPAA Technical Controls Review:** For migrations involving ePHI, the Security Architect must review and co-sign the runbook, confirming TLS 1.3 enforcement and AES-256 at-rest encryption in the target. | Security Architect | Jira checklist sign-off "HIPAA Technical Controls Satisfied" |

*Gate Exit Criteria:* Runbook complete and approved via PR in GitHub; Dry-Run log shows 100% pass on `VALIDATE` steps with zero critical errors; Rollback procedure validated during Dry-Run; MGB approves advancement to Phase 3 for `Major` and `Critical` migrations.

---

### 5.3 Phase 3: Pre-Execution Verification and Cutover Authorization
**Gate Owner:** Release Manager and MGB Chair

| Step | Action | Responsible Party (RACI) | Verification |
|---|---|---|---|
| 3.1 | **Source System Snapshot:** In coordination with the IT Operations team (per SOP-IT-008), trigger an on-demand full backup of the source dataset. Record the backup Job ID. Validate backup integrity. | SRE (Responsible), IT Ops (Consulted) | Backup Job ID logged in runbook |
| 3.2 | **Maintenance Window Communication:** For migrations requiring downtime, the Release Manager must issue a "Data Maintenance Notice" to all impacted service desk teams, customer success managers, and internal stakeholders via the `#migration-status` Slack channel and email. Notice must contain the scheduled start, expected end, and system unavailability details. | Release Manager | Notice ID logged |
| 3.3 | **Final Reconciliation:** Execute a final data profiling script (`mdclass --diff-only`) that compares the source and target schemas and provides a final row/column count against the source. Must match expected values from Step 2.2. This is the last moment to detect drift. | DBRE | Final Delta Report (should show zero drifts in critical tables) |
| 3.4 | **Cutover Authorization:** Present the complete packet—Dry-Run Report, Final Delta Report, Maintenance Window Notice, and Rollback Confirmation—to the authorizing party defined in Table 5.1-A. Authorization is the **Cutover Binding Decision Time (CBDT)** . After this moment, only the formal Rollback procedure is authorized, not ad-hoc adjustments. | Authorizer (e.g., MGB, Executive) | `CUTOVER_AUTHORIZED` status in Jira |

*Gate Exit Criteria:* Source snapshot verified; Communication plan acknowledged; Jira status is `CUTOVER_AUTHORIZED`.

---

### 5.4 Phase 4: Execution
**Gate Owner:** Migration Owner (Operational Command)

This is the execution window. All steps run directly from the approved `migration-runbook-{Jira-ID}.yaml` file; no modifications are permitted post-CBDT.

| Step | Action | Tooling | Status |
|---|---|---|---|
| 4.1 | **Orchestrator Invocation:** The Runbook is invoked by the `meridian-runner` CLI, which acquires an OAuth2 token from Okta. All commands are executed under this token's identity for audit. | `meridian-runner execute --runbook-id migration-runbook-PENG-MIG-1425` | `IN_PROGRESS` |
| 4.2 | **Automated Pre-Flight Checks:** The runner executes the `PREFLIGHT` block: validates TLS 1.3 connectivity to source and target, verifies service account IAM permissions, checks target storage capacity (>20% free space), and confirms source system backup status. Any failure halts the process immediately. | `meridian-runner`, integrated AWS/NET health checks | `PREFLIGHT_PASS` / `PREFLIGHT_FAIL` |
| 4.3 | **Data Movement (`EXEC` block):** Depending on the migration type, one or more of the following standardized Meridian Workers is invoked: `pgcopy-worker` (PostgreSQL logical replication), `snowpipe-worker` (Snowflake ingestion), `s3-sync-worker` (bulk S3 transfer with checksums), or `kafka-mirror-worker` (stream mirroring). The process logs progress to Splunk every 60 seconds. | Worker Pods on Kubernetes cluster | `EXEC_IN_PROGRESS` |
| 4.4 | **Cutover Toggle (Optional):** For Blue/Green migrations, a scripted DNS cutover or application config flip happens at this sub-step, after the `EXEC` block successfully completes for the main dataset. | Terraform Runbook step changing DNS CNAME or app ConfigMap | `CUTOVER_EXECUTED` |
| 4.5 | **Immediate Validation (`VALIDATE` block):** The runner executes all post-move validation scripts declared in the runbook. This includes `pgquarrel` diffs (expecting zero), row counts, and random PHI record audit (compare 1,000 random rows from source and target via Meridian's `audit-compare` tool). | `meridian-runner`, `audit-compare`, `pgquarrel` | `VALIDATE_IN_PROGRESS` |

*Gate Exit Criteria:* All `EXEC` and `VALIDATE` steps report an exit code of `0`. If any validation step fails, the Runbook immediately halts and invokes the `ROLLBACK` function automatically.

---

### 5.5 Phase 5: Post-Migration Verification and Handover
**Gate Owner:** Data Steward (HIPAA) / Product Manager

| Step | Action | Responsible Party | Evidence |
|---|---|---|---|
| 5.1 | **Application-Level Smoke Test:** Engineering teams responsible for consuming the data run their automated integration test suite against the new target environment. | Service Teams | Green test run log uploaded to Jira |
| 5.2 | **Data Integrity Certification:** The Data Steward reviews the `VALIDATE` block output logs, focusing on the `audit-compare` random PHI sample. If satisfied, the Data Steward digitally signs the "Data Integrity Certification" form within Jira. This is the formal attestation that Meridian, based on best efforts, has ensured the accuracy of the PHI per HIPAA. For financial data, James Thornton (CFO) performs a similar certification. | Data Steward (Dr. Patel / J. Thornton) | Signed Jira form |
| 5.3 | **Decommission of Source (Optional):** If the migration was part of a system decommissioning (EOL), the source dataset is not deleted immediately. It must be logically air-gapped (security group removed, access keys revoked) for a period of 90 days. Permanent data destruction follows SOP-IT-042. | SRE Team | Source access control modification logs |
| 5.4 | **Handover to Operations:** The Migration Owner transitions monitoring ownership to the Network Operations Center (NOC). Alerts on target system latency, error budget consumption, and storage capacity are added to the NOC dashboards. | Migration Owner, NOC Lead | Alerts verified as firing/healthy in PagerDuty |
| 5.5 | **Jira Closure:** The Migration Owner attaches all artifacts (Final Runbook execution log, Smoke Test results, Signed Certifications) to the Jira ticket. Ticket status is set to `DONE_MIGRATED`. | Migration Owner | Jira `PENG-MIG` ticket |

---

## 6. Controls and Safeguards

### 6.1 HIPAA Administrative Safeguards (§ 164.308)
- **Security Management Process (§ 164.308(a)(1)(ii)(A)):** The Migration Governance Board (MGB) quarterly meeting includes a review of all non-standard rollbacks and migration incidents in the preceding period. A report is generated from Splunk dashboards and reviewed by the CISO to identify and mitigate systemic risks.
- **Assigned Security Responsibility (§ 164.308(a)(2)):** The Information Security Senior Manager (Security Architect role in Section 3) is the designated Security Officer for all migration activities, accountable for the technical enforcement of HIPAA Security Rule controls during data movement.
- **Workforce Security (§ 164.308(a)(3)(ii)(B)):** Only personnel holding an active Meridian Engineering Certification Level 3 and having completed the "HIPAA & Data Handling for SRE" annual training (See Section 9) are permitted to hold the Migration Owner role for ePHI migrations.
- **Security Incident Procedures (§ 164.308(a)(6)(i)):** An "Abnormal Migration Termination" event, where a runbook halts unexpectedly or a rollback is invoked non-voluntarily, is classified as a Security Incident, triggering SOP-IS-011 (Incident Response) and its associated timelines (P1 notification within 15 minutes).

### 6.2 HIPAA Technical Safeguards (§ 164.312)
- **Unique User Identification (§ 164.312(a)(2)(i)):** The `meridian-runner` and all ETL worker pods must authenticate using their unique individual Service Principal Names (SPNs) via Okta IdP. Shared service accounts are permitted, but any individual invocation must be traceable back to the human operator who initiated the runbook.
- **Person or Entity Authentication (§ 164.312(d)):** The source and target databases must verify the identity of the running ETL process through certificate-based mutual TLS (mTLS). No migration process shall connect to a production database using password-based authentication.
- **Transmission Security (§ 164.312(e)(1)):** Meridian’s Service Mesh (Istio) enforces strict mTLS and TLS 1.3 encryption on all inter-service communication within the Kubernetes cluster. External transfer to Snowflake or S3 uses the respective native SDKs which are configured with enforced HTTPS-only.

### 6.3 Audit Control and Lineage
Every row-level operation of a migration runbook generates a structured audit log in the following format, streamed directly to the immutable Meridian Audit Log Storage (Amazon QLDB).

```json
{
  "auditId": "uuid",
  "runbookId": "migration-runbook-PENG-MIG-1425",
  "stepId": "VALIDATE_step_04b_AuditCompare",
  "principal": "svc-okta-runner-prod-meridian-sre-role/avery.patel@meridian.internal",
  "timestamp": "2025-10-24T18:02:15.321Z",
  "action": "CHECKSUM_COMPARE",
  "source": { "host": "pg-source-prod-eu-west-1.internal", "table": "patient_records", "range": "rows 1-1000" },
  "target": { "host": "pg-target-prod-eu-central-1.internal", "table": "patient_records_new", "range": "rows 1-1000" },
  "outcome": "MATCH",
  "hash_source": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "hash_target": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
```

The Data Lineage Graph (Apache Atlas) is automatically updated to reflect the new location of the data asset, mapping `patient_records -> patient_records_new`.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The VP of Engineering and the MGB track the following metrics on a monthly basis via the Engineering Operations dashboard in Tableau.

| Metric Category | KPI Name | Definition | Target | Measurement Tool |
|---|---|---|---|---|
| **Execution Quality** | Migration Success Rate | `(Completed w/o Rollback) / Total Migrations` per month | ≥ 98% | Jira `PENG-MIG` |
| **Execution Quality** | Runbook Adherence | `(Migrations Executed via meridian-runner) / Total Migrations` | 100% | Splunk, CI/CD Pipeline logs |
| **HIPAA Compliance** | PHI Audit Completeness | `(Migration Steps with full audit trail) / Total Steps` per ePHI migration | 100% | QLDB Audit Ledger |
| **HIPAA Compliance** | Post-Migration Data Integrity | `(Certifications signed without Exception) / Total ePHI Migrations` | 99.5% | Jira Signed Forms |
| **Operational** | Mean Time to Rollback (MTTR) | Time from `ROLLBACK_FUNCTION_INVOKED` to service health restored. | < 30 minutes (Major), < 5 minutes (Minor) | PagerDuty, Runbook logs |

### 7.2 Reporting Cadence
- **Weekly:** VP of Engineering reviews "In Progress" Major and Critical migrations in the `PENG-MIG` Kanban board. Blockers are escalated.
- **Monthly:** A formal "Data Operations Health Report" including KPI performance, is distributed to the MGB, CISO, and CMO. The report includes a RAG (Red-Amber-Green) status for each KPI.
- **Quarterly:** The MGB conducts a Process Improvement Review of this SOP, analyzing rollback root causes and proposing changes to `meridian-runner` templates or validation procedures.

---

## 8. Exception Handling and Escalation

### 8.1 Real-Time Exception Handling
During a migration execution (Phase 4), only the predefined automated Rollback procedure or the manual Rollback procedure documented in the approved Runbook may be executed.
- **Pipeline Halt:** If an `EXEC` step fails, the `meridian-runner` automatically stops the sequence, logs the failure, and notifies the Migration Owner in Slack `#migration-warroom`.
- **Validation Failure:** If a `VALIDATE` step fails, the Runbook does *not* proceed. The Migration Owner has a 15-minute window to diagnose the issue (e.g., schema drift, network timeout). If the issue cannot be root-caused and resolved within 15 minutes, the mandatory Rollback protocol is initiated by the Migration Owner. A decision to *not* roll back (i.e., to proceed with a known validation failure) requires a live exception approval from the CISO and VP of Engineering.

### 8.2 Formal SOP Exception Handling
Any deviation from the procedures in this SOP must be documented before the Phase 3 final Cutover Authorization. This includes items like the use of TLS 1.2 for legacy EOL systems.

| Step | Action |
|---|---|
| 1 | The Migration Owner opens a "Policy Exception" linked to the main `PENG-MIG` Jira ticket. The exception must clearly state the section of the SOP being deviated from, the technical justification, and the compensating control in place. |
| 2 | The CISO (Rachel Kim) reviews the technical justification and compensating controls. Approval constitutes acceptance of risk by the Security Office. |
| 3 | For any exception involving PHI, the Chief Medical Officer (Dr. Patel) or her delegated HIPAA Privacy Officer must co-approve. |
| 4 | Approved exceptions are valid for the duration of the specific migration event only. A blanket exception for multiple events is not permitted. |

---

## 9. Training Requirements

### 9.1 Required Courses and Certifications

| Role | Training Course | Delivery | Frequency | Tracking |
|---|---|---|---|---|
| **All Personnel** | HIPAA & Privacy Basics (MER-SEC-101) | LMS (Workday) | Annual | Workday Transcript |
| **Migration Owner, SRE, DBRE** | HIPAA & Data Handling for SRE (MER-SEC-205) | Instructor-Led, Lab Exam | Annual (Certification valid 365 days) | Engineering Cert Registry |
| **Migration Owner (PHI-specific)** | `meridian-runner` Advanced Operator (MER-PENG-RUN) | LMS & Lab Exam | Once, version-specific retake if CLI updates occur | GitHub Repo Access Control (grants access to `sre-migrations` repo) |
| **Validation Engineer (QE)** | Automated HIPAA Validation Testing (MER-QE-307) | Instructor-Led | Biannual | Quality Assurance Skills Matrix |

### 9.2 Policy Attestation
Before being granted the `migration-executor` role in Okta (which permits invoking `meridian-runner` against production), every engineer must digitally sign an attestation that they have read, understood, and will abide by SOP-PENG-016. This attestation is tracked in Workday and is a pre-requisite for Okta Active Directory group membership `sec-role-eng-migration-exec`.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Document Title | Relationship |
|---|---|---|
| SOP-IS-011 | Incident Response Protocol | Triggered by abnormal migration termination or data loss |
| SOP-IS-014 | Access Control Management | Governs IdP role assignment and IAM policy creation |
| SOP-IS-018 | Cryptographic Key Management | Governs KMS and Vault lifecycle used for migration encryption |
| SOP-IT-008 | Backup and Recovery Operations | Defines backup process invoked in Phase 3 Step 3.1 |
| SOP-IT-042 | IT Asset Lifecycle Management | Governs source environment decommissioning post-migration |
| SOP-PENG-022 | Stream Processing and Event Management | Governs the continuous data streams not covered by this SOP |
| SOP-QA-009 | Change Advisory Board (CAB) Procedures | Defines the release management and stakeholder communication process |

### 10.2 External Regulatory References

| Regulation | Identifier | Key Section(s) |
|---|---|---|
| HIPAA Security Rule | 45 CFR Part 164 | Subpart C § 164.302 - 164.318 |
| HIPAA Privacy Rule | 45 CFR Part 164 | Subpart E § 164.502 (Minimum Necessary), § 164.514 (De-identification) |
| GDPR | EU 2016/679 | Art. 44-49 (Cross-Border Data Transfers), Art. 25 (Data Protection by Design) |

---

## 11. Revision History

| Version | Effective Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| 5.0 | 2024-09-01 | D. Park, VP Eng. | Dr. S. Chen, CEO | Major overhaul. Introduced Meridian Runner Automation, QLDB Audit Trail, and new MGB governance structure. |
| 5.1 | 2024-11-15 | A. Dubois, InfoSec | D. Park, VP Eng. | Updated TLS 1.2 exception handling section to mandate security exception ticket; increased rigor on rollback timing. |
| 5.2 | 2025-01-20 | L. Kim, DBRE Lead | R. Kim, CISO | Introduced mandatory `mdclass` profiling step in Phase 1; removed outdated "DBA-supervised" mode of execution. |
| 5.3 | 2025-03-10 | P. Gonzalez, QE Dir. | D. Park, VP Eng. | Added independent QE validation step for MTD in Phase 2; strengthened post-migration smoke test requirements. |
| 5.4 | 2025-04-05 | D. Voss, DPO | Dr. S. Chen, CEO | Incorporated DPO role and responsibilities for EU data migrations; clarified cross-border transfer controls. |
| 5.5 | 2025-05-22 | S. Cho, SRE Mgr. | Dr. S. Chen, CEO | Refined Phase 4 execution to mandate mTLS authentication; update data integrity KPI to 99.5%; annual review of roles matrix completed. |