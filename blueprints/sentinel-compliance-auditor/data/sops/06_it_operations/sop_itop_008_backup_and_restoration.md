---
sop_id: "SOP-ITOP-008"
title: "Backup and Restoration"
business_unit: "IT Operations & Infrastructure"
version: "5.8"
effective_date: "2025-09-07"
last_reviewed: "2026-01-14"
next_review: "2026-07-16"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Meridian Health Technologies, Inc.
# Standard Operating Procedure: Backup and Restoration
**SOP-ITOP-008 | Version 5.8**

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the enterprise-wide framework, technical specifications, and operational procedures governing the backup, replication, and restoration of all Meridian Health Technologies, Inc. (“Meridian”) information systems, applications, and data assets. The purpose is to ensure the confidentiality, integrity, and availability (CIA) of critical information in alignment with our regulatory obligations, contractual commitments, and the Board-level risk appetite defined by the AI Governance Committee.

This SOP is designed to mitigate risks associated with data corruption, accidental deletion, ransomware attacks, insider threats, and catastrophic infrastructure failure. It provides a standardized, repeatable methodology for recovering Meridian’s Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform to operational states within prescribed Recovery Time Objectives (RTOs) and Recovery Point Objectives (RPOs).

### 1.2 Scope
This SOP applies to all production, staging, and development environments that support or store data for Meridian’s four business lines, with a specific emphasis on systems handling Electronic Protected Health Information (ePHI), Personally Identifiable Information (PII), and regulated financial models.

**In-Scope Systems and Data:**
- **Clinical AI Platform:** Training datasets, model weights (PyTorch/TensorFlow), inference configurations, clinical decision support logs, FDA-validated model artifacts, and adverse event prediction data stored in Amazon S3 (us-east-1, eu-west-1) and Snowflake.
- **HealthPay Financial Services:** Transactional databases (PostgreSQL), claims automation logs, credit scoring model parameters (subject to SR 11-7), patient financing records, and Kafka event streams.
- **MedInsight Analytics:** Population health datasets, PHI warehouses (~12M patient records), care gap analytics stores, and outcomes prediction models in Redis and Pinecone vector databases.
- **Meridian SaaS Platform:** Multi-tenant application configurations, AWS infrastructure as code (Terraform state), Okta identity provider configurations, HashiCorp Vault secrets, and CI/CD pipeline definitions (Kubeflow, MLflow).

**Out-of-Scope:**
- End-user local workstations (managed under SOP-ITOP-012: Endpoint Management). Employees are responsible for storing business data on OneDrive for Business or SharePoint Online, which are backed up under Microsoft’s shared responsibility model.
- Third-party SaaS platforms where Meridian has no administrative backup control (e.g., raw PagerDuty alert payloads, Datadog telemetry data older than 30 days).

### 1.3 Applicability
This SOP is binding upon all employees, contractors, consultants, and Managed Service Providers (MSPs) who provision, manage, or decommission Meridian IT assets. The primary executing bodies are the IT Operations & Infrastructure team, the Cloud Platform Engineering team, and the Information Security team. Violations of this SOP may result in disciplinary action, up to and including termination of employment and legal referral.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **Air-Gapped Backup** | A backup copy stored in a network environment physically or logically isolated from the production network. Meridian utilizes AWS S3 Glacier Deep Archive with a separate AWS Organization account and MFA-protected root credentials under the control of the CISO. |
| **BCP** | Business Continuity Plan. Meridian’s enterprise-wide framework for responding to significant disruptions (SOP-BCM-001). |
| **CMK** | Customer Master Key. AWS KMS keys generated and managed by Meridian, as opposed to AWS-managed default keys. |
| **Cross-Region Replication (CRR)** | Automated, asynchronous copying of S3 objects from a source bucket in `us-east-1` to a destination bucket in `eu-west-1` (and vice versa) for geographical redundancy. |
| **ePHI** | Electronic Protected Health Information. Individually identifiable health information transmitted or stored electronically, subject to HIPAA. |
| **Immutable Backup** | A backup copy that cannot be modified or deleted by any user, process, or application, even a compromised root account, for its prescribed retention duration (enforced via S3 Object Lock in Compliance mode). |
| **IaaS** | Infrastructure as Code. Terraform and AWS CloudFormation templates defining Meridian’s cloud footprint. |
| **IRP** | Incident Response Plan (SOP-ISEC-001). |
| **NIST AI RMF** | National Institute of Standards and Technology AI Risk Management Framework. Adopted voluntarily. |
| **Object Lock** | S3 feature enforcing WORM (Write Once Read Many) immutability on objects. |
| **RPO** | Recovery Point Objective. The maximum acceptable amount of data loss measured in time. |
| **RTO** | Recovery Time Objective. The maximum acceptable downtime before systems are operationally functional. |
| **SR 11-7** | Federal Reserve and Office of the Comptroller of the Currency Supervisory Guidance on Model Risk Management. |
| **Vault (HashiCorp)** | Meridian’s enterprise secrets management system. |
| **WORM** | Write Once, Read Many. Immutable storage technology. |

---

## 3. Roles and Responsibilities

The following Responsibility Assignment Matrix details the accountable, responsible, consulted, and informed parties for the lifecycle of backup and restoration operations.

- **(R) Responsible:** Executes the task.
- **(A) Accountable:** Answerable for the outcome; must be a single role.
- **(C) Consulted:** Subject matter expert input required.
- **(I) Informed:** Kept up-to-date on progress.

| Activity | Cloud Platform Engineering | IT Operations (Backup Admins) | Information Security | Data Governance Officer | Business Unit Owner |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Backup Job Definition & Scheduling** | R | A | C | I | I |
| **Encryption Key Lifecycle (CMK Rotation)** | C | R | A | I | I |
| **Quarterly Restoration Testing (All Systems)** | R | A | C | I | C |
| **HIPAA ePHI Restoration Compliance Audits** | C | R | C | A | I |
| **Financial Model (SR 11-7) Snapshot Verification** | I | R | I | C | A |
| **Annual Offsite Tape/Media Vault Reconciliation** | I | R | C | A | - |
| **Exception Approval (non-standard RPO/RTO)** | C | R | A | C | A |

**Named Operational Roles:**
- **Backup Administrator (Lead):** An assigned Level-3 engineer within the IT Operations & Infrastructure team responsible for the overall execution of this SOP, management of the Commvault/Rubrik backup fabric, and remediation of failed backup jobs. Currently designated as the Senior Cloud Operations Manager.
- **Information Security Officer (CISO):** Rachel Kim, accountable for the logical and physical security controls, including key management and immutability enforcement.
- **Data Governance Officer (DGO):** Thomas Bell, responsible for classifying data sensitivity and verifying that restoration practices meet HIPAA de-identification standards (HIPAA §164.514) when required for non-production restoration.
- **Business Continuity Manager:** Reports to the VP of IT Operations, serves as the primary liaison during DR activation, and coordinates tabletop exercise logistics.

---

## 4. Policy Statements

The following high-level policy statements derive from Meridian’s Enterprise Risk Management (ERM) framework and compliance mandates.

1.  **Policy of Universality:** All production data, configurations, and stateful application data MUST be backed up. No production IaaS component shall be provisioned without a corresponding backup tag and policy assignment within 4 hours of deployment.
2.  **Recovery Point Objective (RPO) Compliance:** All Tier-1 systems (Clinical AI Platform, HealthPay Core, MedInsight PHI) MUST maintain a documented and monitored RPO of 15 minutes or less. Tier-2 systems (analytics data marts, staging environments) must maintain an RPO of 4 hours or less.
3.  **Immutable Backups Mandate:** To defend against ransomware and advanced persistent threats, all critical data cataloged as Tier-1 MUST possess an immutable backup instance protected by WORM storage policies (S3 Object Lock in Compliance mode) for a minimum of 30 days.
4.  **Encryption at Rest and in Transit:** All backup data, irrespective of location or media, must be encrypted using AES-256. Encryption keys must be Meridian-owned Customer Master Keys (CMKs) managed via HashiCorp Vault or AWS KMS, never provider-managed defaults.
5.  **Geo-Redundancy Mandate:** No single critical dataset may exist solely in one AWS region. Cross-Region Replication (CRR) or equivalent must be active for all S3 buckets identified in the Data Classification Matrix (DC-MAT-001).
6.  **Verification Responsibility:** The IT Operations team is solely accountable for the verifiable recovery of data. A "Backup Success" notification without a periodic, automated restoration test is insufficient proof of control efficacy.
7.  **No Backdoor Modification:** Backup retention lock configurations SHALL NOT be overridden by privileged IAM roles without a documented and approved Emergency Break-Glass Procedure, which requires concurrent approval from the CISO and the VP of IT Operations.

---

## 5. Detailed Procedures

This section outlines the step-by-step procedures for configuring, executing, verifying, and restoring backups. All automation scripts referenced reside in the Meridian GitLab repository at `gitlab.internal.meridian.com/ops/backup-automation`.

### 5.1 Backup Schedule and Frequency

The backup schedule is defined via a GitOps workflow utilizing Kubernetes `CronJob` objects for database dumps and AWS Backup Plans for native AWS resources.

#### 5.1.1 Tier-1 Data Assets (e.g., HealthPay PostgreSQL, MedInsight Snowflake)
- **Continuous Backups:** AWS-native continuous backup (Point-in-Time Recovery, PITR) is enabled for RDS PostgreSQL instances and DynamoDB tables. Transaction logs are streamed to a dedicated S3 bucket encrypted with `CMK-ITOP-008`.
- **Daily Incremental Backups:** Taken every 4 hours via AWS Backup Plan `prod-tier1-incr`. Snapshots are retained for 7 days.
- **Weekly Full Backups:** Taken every Sunday at 0200 UTC via AWS Backup Plan `prod-tier1-full`. Snapshots are retained for 90 days.

#### 5.1.2 Tier-2 Data Assets (e.g., Redis ephemeral stores, Dev S3 buckets)
- **Daily Full Backup:** Initiated at 0300 local time per region via AWS Backup Plan `nonprod-tier2-full`. Snapshots are retained for 30 days.

#### 5.1.3 Financial Model Snapshots (SR 11-7)
- **Manual Pre-Release Snapshots:** Before any new credit scoring model or algorithm is deployed to the `HealthPay-Prod` inference cluster, a manual, named snapshot of the SageMaker endpoint configuration, model artifact in S3, and feature store tables MUST be performed by the deploying MLOps engineer.

### 5.2 Backup Types and Methodology

| Asset Class | Primary Tool | Backup Type | Mechanism | Destination |
| :--- | :--- | :--- | :--- | :--- |
| **Relational DBs (PostgreSQL)** | AWS Backup & PITR | Full & Transaction Log | Storage Gateway snapshot, native `pg_dump` for logical exports | S3 (`meridian-db-backups-prod-us-east-1`) |
| **NoSQL (DynamoDB)** | AWS Backup | Full Table Snapshot | AWS Backup Service role | S3 (`meridian-nosql-backups`) |
| **Object Storage (S3 ePHI)** | AWS Replication & Object Lock | Asynchronous CRR | S3 Replication Rules, WORM lock applied on destination | S3 (`meridian-immutable-eu-west-1`) |
| **Model Weights & Artifacts** | S3 Object Lock & MLflow | Immutable Snapshot | MLflow artifact API, version-based locking | S3 (`meridian-ml-artifacts`) |
| **Infra-as-Code (Terraform)** | GitLab CI/CD Pipelines | Git Repository | `git backup` via cron, exported to S3 bucket | S3 (`meridian-iac-prod`) |
| **Kafka Event Streams** | Confluent Cloud Connector | Tiered Storage | Cold storage connector to S3, daily offset snapshots | S3 (`meridian-kafka-offload`) |

### 5.3 Encryption Standards

All backup artifacts must be encrypted data-at-rest using the specific operational pattern:
1.  **Key Material:** A dedicated KMS CMK (Alias: `alias/sop-itop008-backup-cmk`) is used for all backup vaults. The CMK policy denies `kms:Decrypt` and `kms:Encrypt` permissions to any principal except the AWS Backup service role and the Break-Glass IAM Role (`arn:aws:iam::111122223333:role/BreakGlass-Backup-Restore`).
2.  **Envelope Encryption:** Backup data files are encrypted with a data key generated by the CMK. The encrypted data key is stored alongside the backup artifact.
3.  **In-Transit:** All backup operations traverse TLS 1.2+ encrypted channels. S3 bucket policies explicitly deny `s3:PutObject` requests where `aws:SecureTransport` is `false`.

### 5.4 Procedure: Performing a Manual Backup Before Major Change

This procedure MUST be executed by a DevOps Engineer in the Cloud Platform Engineering team before any database schema migration or major platform release (refer to SOP-CHM-004 Change Management).

**Steps:**
1.  **Identify Source:** Identify the ARN of the Aurora RDS cluster or DynamoDB table from the release manifest (`release-manifest.yaml`).
2.  **Initiate Snapshot:** Log into the Meridian AWS Management Console (production account, `us-east-1` region, with an approved break-glass role assumption). Navigate to the AWS Backup service.
3.  **Run On-Demand Job:** Select "Create On-Demand Backup." Choose the target resource ARN. For the `vault-name` parameter, select `meridian-prechange-vault`.
4.  **Tag Artifact:** Mandatory tags: `SOP-ID=SOP-ITOP-008`, `CHG-Ticket=<CHG-Ticket-Number>`, `Retention=30-days`, `Initiated-by=<User LDAP>`.
5.  **Verify:** Once in the `Completed` state, validate the by checking the Job UUID. Log the UUID in the Change Management Ticket (Jira/ServiceNow) validation field.
6.  **Proceed:** After successful validation, the Release Manager may permit the change window to commence.

### 5.5 Restoration Testing Procedures (Compliance Validation)

Restoration testing is not a DR exercise; it is a technical verification of backup fidelity. Meridian conducts a tiered restoration test program.

**5.5.1 Automated Integrity Verification (Nightly)**
- **Procedure:** A Jenkins pipeline (`backup-integrity-test-pipeline`) executes nightly at 0600 UTC.
- **Scope:** Selects a random, statistically significant sample of 1% of all backup files from the previous 24 hours.
- **Action:**
    1.  Downloads the backup artifact to an isolated, air-gapped sandbox environment.
    2.  Validates the SHA-256 checksum against the index stored in DynamoDB.
    3.  Decrypts the data key using the non-production test KMS key `alias/test-backup-cmk`.
    4.  Mounts the database backup to a transient, sterile PostgreSQL container.
    5.  Runs `pg_verify_checksums` (or equivalent filesystem verification).
    6.  Writes the pass/fail result to CloudWatch Metrics (`Meridian/BackupIntegrity`).
- **Failure Escalation:** A failure triggers a P3 incident via PagerDuty to the on-call IT Operations engineer.

**5.5.2 Quarterly Full-Scale Restoration Test (HIPAA §164.310 and §164.314)**
- **Schedule:** The first Saturday of each fiscal quarter (Jan, Apr, Jul, Oct) from 0800 to 1600 ET.
- **Procedure:**
    1.  **Environment:** Deploy a parallel, sterile "recovery" VPC in the secondary AWS region (`eu-west-1`) using Terraform from the IaC backup.
    2.  **PHI Integrity:** Restore the `MedInsight-PHI-Prod` RDS instance from a snapshot. Run a comprehensive SQL script (`phi_comparison_queries.sql`) to validate row counts, schema structures, and referential integrity against the production baseline.
    3.  **Model Fidelity:** Restore a specific `Clinical-AI-Model-v3` artifact from S3. Launch a SageMaker Batch Transform job against a standardized holdout dataset. Compare the inference accuracy scores with the baseline scores documented in the Model Registry. Allowable variance: ±0.5%.
    4.  **HealthPay Ledger Balance:** Restore the HealthPay PostgreSQL database. Replay the continuous transaction logs to a specific Point-in-Time (12:00 UTC). Execute a `SELECT SUM(amount) FROM transactions WHERE status='cleared'` and reconcile this with the ledger balance stored in the Snowflake financial warehouse. Discrepancies must be fully investigated and resolved before the test is marked successful.
- **Deliverable:** A Quarterly Restoration Test Report (template `SOP-ITOP-008-F02`) signed by the VP of IT Operations and reviewed by the CISO within 10 business days of the test.

### 6.3 Immutability Safeguard (WORM)
- **S3 Object Lock Configuration:** The S3 bucket in the secondary region (`meridian-immutable-eu-west-1`) has a default Object Lock retention policy of 30 years in `GOVERNANCE` mode, with strict IAM policies preventing the `s3:BypassGovernanceRetention` permission from all non-break-glass roles. A secondary Object Lock in `COMPLIANCE` mode is set for 1 year for legal hold requirements, which cannot be lifted by any user, including the root account.

### 6.4 Change Management for Backup Policies
Any modification to the backup scripts in GitLab, AWS Backup Plans, retention periods, or RPO/RTO targets is classified as a Standard Change (per SOP-CHM-004). Change requests must include a rollback plan detailing how the original backup policy will be reinstated if the change results in data inconsistency. The requester must execute the validation in GitLab CI before the change can be approved and merged by a peer reviewer.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Mechanism |
| :--- | :--- | :--- |
| **ACL-BR-01** | **Separation of Duties (Backup/Restoration):** No single individual may possess the technical ability to both initiate an irreversible backup deletion and authorize such a deletion. The action of applying a backup policy is separated from the action of vault management. | `sop-itop008-backup-cmk` Key Policy grants `kms:CreateGrant` to the Backup Admin role but `kms:Decrypt` and `kms:ScheduleKeyDeletion` exclusively to the `BreakGlass-Backup-Restore` role, which requires dual-approval. |
| **ACL-BR-02** | **Least Privilege Access:** Access to backup vaults in AWS is restricted to the `ops-backup-admin` IAM group. Direct access to the backup S3 bucket console is prohibited; all operations must go through the AWS Backup API or approved automation pipelines. | IAM Policy `meridian-deny-console-s3-access` attached to all IAM users except `break-glass` roles. |
| **ACL-BR-03** | **Quarterly Access Review:** The CISO’s office reviews the members of the `ops-backup-admin` IAM group on a quarterly basis. Any unauthorized membership will be treated as a security incident. | Automated audit via AWS IAM Access Analyzer and a Jira governance ticket raised by the Identity Governance team. |

### 6.2 Technical Controls

| Control ID | Control Description | Technology |
| :--- | :--- | :--- |
| **TEC-ENC-01** | **AES-256 Envelope Encryption** | AWS KMS CMK (`sop-itop008-backup-cmk`) with automatic annual rotation. |
| **TEC-IMM-01** | **WORM Immutability Layer** | AWS S3 Object Lock in Compliance mode (1 year) and Governance mode (30 day). |
| **TEC-GEO-01** | **Cross-Region Digital Redundancy** | S3 Cross-Region Replication (CRR) with a replication time control (RTC) SLA of 15 minutes for 99% of objects. |
| **TEC-VAL-01** | **Automated Checksum & Restore Integrity** | Nightly Jenkins pipeline generating CloudWatch Metrics. |
| **TEC-AIR-01** | **Logical Air-Gap for BCP Copies** | A dedicated AWS Organization account, `Meridian-Backup-Security`, houses the ultimate immutable copy. Access to this account requires a temporary STS token issued by the VP of IT Ops and CISO. |

---

## 7. Monitoring, Metrics, and Reporting

All backup operations must be continuously monitored. The following Key Performance Indicators (KPIs) and Service Level Agreements (SLAs) provide measurable, objective evidence of control performance for SOC 2 and HIPAA compliance.

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | Metric | Target | Measurement Mechanism |
| :--- | :--- | :--- | :--- |
| **KPI-BR-01** | **Backup Job Success Rate** | ≥ 99.9% monthly | AWS Backup CloudWatch Dashboard filtered by `Status="COMPLETED"` vs. `Status="FAILED"`. |
| **KPI-BR-02** | **RPO Compliance** (All Tier-1) | 100% of snapshots taken within the 15-minute window | Prometheus metric `rpo_compliance_percent` scraped from the HealthPay RDS Event Stream. |
| **KPI-BR-03** | **Quarterly Restore Test Success** | ≥ 95% of critical artifacts fully restored and verified within a single test window per quarter | Manual validation checklist (Form `SOP-ITOP-008-F02`). Test fails if an ePHI dataset cannot be restored to full integrity. |
| **KPI-BR-04** | **Replication Latency Geo-Lag** | P99 latency < 1 hour | S3 Replication Time Control (RTC) metrics in CloudWatch. |

### 7.2 Dashboards and Reporting
- **Real-Time Operations Dashboard:** A Grafana dashboard (`#Ops-Backup-SLA`) displays job success/failure, current geo-replication lag, and vault capacity utilization (warning at 80%, critical at 95%). This is displayed on a NOC wall monitor.
- **Monthly Operations Report:** A PDF report is automatically generated, summarizing KPI compliance, a summary of failed jobs and root cause analyses, and capacity trending. Distributed to `dist-dl-it-operations-vp@meridian.com` and `dist-dl-ciso-office@meridian.com` by the 5th business day of the succeeding month.
- **Bi-Annual Audit Report:** A formal report covering HIPAA §164.314 and SR 11-7 compliance is prepared by the Data Governance Officer and submitted to the AI Governance Committee.

---

## 8. Exception Handling and Escalation

### 8.1 Backup Job Failure Escalation
1.  **Automated Detection:** AWS Backup job enters a `FAILED` status. CloudWatch alarm `CRITICAL-Backup-Job-Failure` triggers.
2.  **PagerDuty Alert:** An incident (`sev2-backup-failure`) is created and assigned to the on-call Backup Administrator. SLA for acknowledgment is 15 minutes.
3.  **Immediate Triage:** Admin verifies if the failure is due to a transient IAM timeout or a substantiative data issue. First action is to manually re-trigger the job.
4.  **Continuous Failure:** If a Tier-1 backup fails for 3 consecutive scheduled attempts, the incident escalates to `sev1-data-protection-compromise`. The VP of IT Operations and CISO are paged immediately. This triggers a risk of regulatory non-compliance (HIPAA data backup failure).
5.  **Manual Intervention:** The VP of IT Operations may authorize a manual, on-demand snapshot as a temporary compensating control while root cause is investigated.

### 8.2 Restoration Failure (Quarterly Test)
- If a critical artifact (ePHI database, ML model, financial ledger) fails to restore and pass integrity checks during the scheduled quarterly test (Section 5.5.2), the test is immediately suspended.
- The VP of IT Operations must classify the failure as a **High-Severity Incident** under the IRP.
- A Formal Root Cause Analysis (RCA) must be completed within 72 hours and reviewed with the CISO.
- The next quarterly test cannot be passed until the specific failure mode is verified as resolved in a re-run of the test.

### 8.3 Standard Exception Requests
Requests for non-standard RPO/RTO or resource exclusions must be submitted via the IT Service Management (ITSM) portal using the "Policy Exception Request" form. The request must include:
- Technical justification.
- Proposed compensating controls.
- Duration for which the exception is requested (not to exceed 90 days without re-approval).
Approval requires sign-off from the system Business Unit Owner and the VP of IT Operations. All approved exceptions are logged in the `grcregs.internal.meridian.com` central register.

---

## 9. Training Requirements

In alignment with HIPAA §164.530(b)(1) and Meridian’s internal compliance programs, role-based training is required for all personnel with access or oversight of backup systems.

| Target Audience | Training Module | Frequency | Delivery Method |
| :--- | :--- | :--- | :--- |
| IT Operations (Backup Admins) | `TR-SOP-ITOP-008-001` SOP v5.8 Deep Dive & Practical Lab | Annually | Instructor-led workshop with hands-on restoration lab. |
| Cloud Platform Engineering | `TR-SOP-ITOP-008-002` IaC & Terraform State Recovery | Annually | Online course (LMS) with lab. |
| Information Security Team | `TR-SOP-ITOP-008-003` Auditing Immutability & Key Management | Annually | Online course (LMS). |
| Release Managers | `TR-SOP-ITOP-008-004` Pre-Change Backup Mandate | Onboarding & Annually thereafter | Self-paced Wiki reading with quiz. |
| Incident Response Team | `TR-SOP-ITOP-008-005` BCP & Emergency Restoration | Biannually | Live drill incorporating both DR and physical-media awareness. |

**Tracking and Non-Compliance:**
Training completion is tracked via the corporate Learning Management System (Workday Learning). Personnel failing to complete mandatory training within 30 days of the assignment will have their access to production AWS accounts temporarily suspended until compliance is achieved.

---

## 10. Related Policies and References

This SOP is not a standalone document. It interfaces critically with the following Meridian governance and operational documents.

### 10.1 Internal Meridian Policies
- **SOP-BCM-001:** Business Continuity and Disaster Recovery Plan (defines RTOs/RPOs).
- **SOP-ISEC-001:** Incident Response Plan (defines the sev2/sev1 escalation framework used here).
- **SOP-CHM-004:** IT Change Management Policy (mandates pre- and post-change validation backups).
- **SOP-CAP-005:** Cryptographic Key Operations (SOP for KMS and Vault management).
- **SOP-DAT-003:** Data Classification and Handling Policy (defines Tier-1/Tier-2 data catalog).
- **SOP-ASSET-001:** Asset Management Lifecycle (tagging schema enforcement).
- **DC-MAT-001:** Data Classification Matrix (lists all regulated data stores).

### 10.2 External Regulatory and Standards References
- **HIPAA 45 CFR §164.310:** Physical Safeguards, specifically (c) Workstation and (d)(1) Device and Media Controls (Disposal and Re-use).
- **HIPAA 45 CFR §164.314:** Administrative Safeguards, specifically (a)(1) Business Associate Contracts and (b)(1) Business Management Plans, requiring a Data Backup Plan and a Disaster Recovery Plan.
- **HIPAA 45 CFR §164.316:** Policies and Procedures and Documentation Requirements, specifically (b)(1)(ii) requiring documentation to be retained for 6 years from the date of creation or last effective date.
- **SOC 2 Common Criteria CC6.1:** The entity implements logical access security controls over infrastructure, applications, and data.
- **SOC 2 Common Criteria CC7.1:** The entity’s system availability meets the defined objectives for system uptime and recovery.
- **NIST AI RMF (AI 100-1) Map Function #2.5:** Reliability, Safety, and appropriate use (applies to backing up ML artifacts safely).

---

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 5.0 | 2024-12-02 | S. Torres, J. Mbeki (IT Ops) | Major revision. Added immutable backup mandate in response to FINRA/SEC advisory. Integrated SR 11-7 specific procedure for HealthPay model artifacts. |
| 5.4 | 2025-03-11 | A. Chen (Cloud Eng) | Updated Section 5.1 to reflect migration from weekly full backups to daily incremental with weekly synthetic fulls. Updated KPI-BR-02 threshold from 99% to 99.9%. Added explicit `CHG-Ticket` tagging to manual backup procedure. |
| 5.6 | 2025-06-20 | M. Rossi (InfoSec) | Incorporated CISO review feedback: added CMK rotation policy in definitions, clarified air-gap logical architecture using AWS Organizations, and added `s3:BypassGovernanceRetention` to explicit IAM deny statements. |
| 5.7 | 2025-08-05 | S. Torres | Minor revision. Updated PagerDuty escalation matrix. Replaced "Nightly Jenkins" with "GitLab CI/CD" for automated verification pipeline. Added quarterly access review (ACL-BR-03) to administrative controls. |
| 5.8 | 2025-09-07 | D. Park (Engineering) | Final approval for v5.8. Incorporated 2026 RPO planning feedback from MedInsight product team. Clarified distinction between snapshot and Continuous PITR in definitions table. Updated Next Review Date. |