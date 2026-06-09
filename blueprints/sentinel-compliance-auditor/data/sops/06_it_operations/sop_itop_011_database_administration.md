---
sop_id: "SOP-ITOP-011"
title: "Database Administration"
business_unit: "IT Operations & Infrastructure"
version: "4.7"
effective_date: "2024-11-01"
last_reviewed: "2025-05-26"
next_review: "2025-11-18"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Database Administration

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the formalized framework for the lifecycle management, security administration, and operational governance of all database systems within Meridian Health Technologies, Inc. The purpose is to ensure the confidentiality, integrity, and availability (CIA) of data assets, with specific attention to protected health information (PHI) and financial model data, through standardized, repeatable processes that align with our Trust Services Criteria (TSC) obligations under SOC 2 and our architectural commitments to our multi-tenant SaaS platform.

### 1.2 Scope

This SOP applies to all database workloads—whether relational, non-relational, or vector-based—operating within the Meridian production, staging, development, and disaster recovery environments hosted on Amazon Web Services (AWS) and Microsoft Azure.

**In-Scope Data Stores:**
| Service | Engine/Tool | Primary Use Case | Environment |
| :--- | :--- | :--- | :--- |
| Amazon RDS | PostgreSQL 15.x | Clinical AI Platform, Patient Risk Scoring, HealthPay Transactions | us-east-1, eu-west-1 |
| Amazon Aurora | PostgreSQL-compatible | MedInsight Analytics, Care Gap Identification | us-east-1 |
| Amazon ElastiCache | Redis 7.x | Session Management, Queue Processing, Real-time Claims Scoring | us-east-1, eu-west-1 |
| Snowflake | Snowflake (Enterprise) | MedInsight Data Lake, Population Health Aggregation | Cross-region |
| Pinecone | Vector Database | AI Clinical Decision Support Embeddings, Diagnostic Imaging Inference | eu-west-1 |
| Azure SQL Managed Instance | SQL Server 2022 | Disaster Recovery Warm Standby, Financial Reconstitution | Azure East US2 |

**Out of Scope:** End-user desktop databases (MS Access, SQLite), local development Docker volumes not containing obfuscated production data, and static application configuration files stored in HashiCorp Vault.

### 1.3 Applicability

This policy applies to all personnel who provision, configure, monitor, or decommission database instances at Meridian. This includes:
- **IT Operations & Infrastructure** (Database Reliability Engineering team)
- **Engineering** (Platform squads with self-service provisioning permissions)
- **Clinical AI Products** (ML Ops engineers accessing feature stores)
- **Financial Services** (Developers and QA accessing synthetic test data)
- **Third-Party Contractors** who manage underlying infrastructure (AWS/Azure support) with Just-in-Time (JIT) access.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **ACID** | Atomicity, Consistency, Isolation, Durability — core transaction properties required for HealthPay lending models. |
| **BCP/DR** | Business Continuity Plan / Disaster Recovery. |
| **CJIS** | Criminal Justice Information Services — not directly applicable but used as a reference frame for encryption strength. |
| **CSP** | Cloud Service Provider (AWS, Azure). |
| **DBA** | Database Administrator — the responsible role within IT Operations. |
| **DBRE** | Database Reliability Engineering — Meridian's SRE-centric approach to database management, emphasizing automation. |
| **DLM** | Database Lifecycle Management. |
| **HA** | High Availability — defined as 99.99% uptime for financial transaction processing excluding planned maintenance windows. |
| **IAM** | Identity and Access Management. |
| **IOPS** | Input/Output Operations Per Second — provisioned metric for RDS performance. |
| **JIT** | Just-in-Time Access — temporary credential elevation via Okta and HashiCorp Vault lasting < 1 hour. |
| **KMS** | Key Management Service — AWS KMS or Azure Key Vault used for envelope encryption. |
| **PHI** | Protected Health Information — any individually identifiable health information processed by Meridian. |
| **PITR** | Point-in-Time Recovery. |
| **RPO/RTO** | Recovery Point Objective / Recovery Time Objective. |
| **SRE** | Site Reliability Engineering. |
| **TDE** | Transparent Data Encryption — encryption at rest at the storage layer. |
| **TLS** | Transport Layer Security — encryption in transit (minimum version 1.2). |
| **TSC** | Trust Services Criteria — SOC 2 framework pillars (Security, Availability, Confidentiality, Processing Integrity, Privacy). |
| **WAL** | Write-Ahead Log — PostgreSQL transaction logs used for PITR and replication. |

---

## 3. Roles and Responsibilities

The following Responsibility Assignment Matrix (RACI) defines the interaction of roles with database operations.
**R = Responsible, A = Accountable, C = Consulted, I = Informed**

| Activity Task | VP IT Ops (S. Torres) | DBRE Lead | Security Engineering (R. Kim) | Compliance (T. Anderson) | Engineering (D. Park) | Application Owner |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Provisioning Approval** | A | R | C | I | C | I |
| **Access Control Management** | I | R | C | A | C | I |
| **Backup Verification** | I | R | I | I | I | A |
| **Patching & Maintenance** | A | R | C | I | I | I |
| **Performance Tuning** | I | R | I | I | C | C |
| **PHI Deletion/Anonymization** | I | C | I | I | R | A |
| **Incident Response (Data Breach)** | I | R | R | A | R | C |
| **Schema Change Review** | I | C | A | I | R | C |

**Named Role Definitions:**
- **VP of IT Operations (Samantha Torres):** Budget owner for infrastructure, final approver for production provisioning and extended maintenance windows.
- **DBRE Lead:** Senior engineer responsible for the automation pipeline, script integrity, and on-call rotation leadership.
- **Chief Information Security Officer (Rachel Kim):** Authority on encryption standards, network segmentation, and zero-trust architecture implementation for data stores.
- **Chief Compliance Officer (Thomas Anderson):** Authority on regulatory interpretation mapping controls to TSC criteria; responsible for audit evidence collection.
- **VP of Engineering (David Park):** Owner of the SDLC; ensures application code interacts with databases safely (parameterized queries, connection pooling).
- **Application Owner:** Designated product manager or tech lead responsible for verifying logical data integrity during restore drills (e.g., Dr. Aisha Okafor for Clinical AI; Robert Liu for HealthPay).

---

## 4. Policy Statements

Meridian Health Technologies commits to the following high-level policy principles regarding database administration:

**4.1 Least Privilege Access**
All database access shall be predicated on the principle of least privilege. No user, application service account, or system process shall possess schema-level access rights exceeding the minimum necessary to perform its function. Direct `DROP`, `TRUNCATE`, or `ALTER TABLE` permissions are denied in production environments outside of approved change windows managed by the DBRE team.

**4.2 Encryption by Default**
All data managed by this SOP shall be encrypted at rest and in transit. Unencrypted database snapshots, exports, or logical dumps are prohibited in any environment containing production data. Meridian utilizes AES-256 envelope encryption via AWS KMS for all RDS instances; key rotation occurs automatically every 365 days or immediately upon security event suspicion.

**4.3 Immutable Audit Logging**
Database-native audit logs (pgAudit for PostgreSQL, SQL Server Audit for Azure) shall be enabled, shipped to a centralized immutable logging bucket (CloudTrail/S3), and retained for a minimum of 365 days. Logs cannot be altered or deleted by any system administrator during this window. This supports the "Security" and "Availability" criteria of our SOC 2 audit.

**4.4 Infrastructure as Code**
Manual "ClickOps" provisioning via AWS Console is strictly prohibited for Tier 1 (Production) databases. All database creation, parameter group assignment, and option group configuration must be defined in Terraform (stored in Meridian’s GitHub Enterprise repository) and deployed via the CI/CD pipeline (GitHub Actions).

**4.5 Segmentation of Duties**
Developers cannot approve their own schema change requests. The database reliability engineering (DBRE) team executes changes, but cannot unilaterally approve changes to financial schemas (HealthPay) or clinical schemas (Clinical AI). A formal Schema Change Advisory Board (S-CAB) review is required for these high-risk systems.

---

## 5. Detailed Procedures

### 5.1 Database Provisioning

All new database instances—whether for new product features, microservices isolation, or analytics—must follow the standardized intake-to-provisioning pipeline.

**5.1.1 Intake Assessment**
Prior to provisioning, the Application Owner must submit a "Database Provisioning Request" via ServiceNow (Catalog Item: `SOP-ITOP-011-DB-PROV`).

**Required Fields:**
| Field | Expected Value / Constraint |
| :--- | :--- |
| **Data Classification** | `Public`, `Internal`, `Confidential`, `Restricted` (per SOP-DSEC-003) |
| **Contains PHI?** | Yes / No |
| **Contains Payment Card Data?** | Yes / No |
| **Estimated Storage (6 months)** | GB/TB forecast |
| **Peak IOPS Requirement** | Based on load testing |
| **Backup Retention Policy** | Default (30 Days) / Extended (7 Years for financial compliance) |
| **Regulatory Framework** | HIPAA, GDPR, SOC 2, SR 11-7 |
| **Business Unit Approver** | Must be Director-level or higher |

**5.1.2 Approval Chain**
The ServiceNow ticket automatically routes through the following gates:
1.  **Manager Approval:** BU Director validates business justification and budget code.
2.  **Security Architecture (Rachel Kim’s team):** Validates network placement (private subnet, no public accessibility flag) and encryption compliance. If the flag `publicly_accessible` is `True`, the request is auto-rejected without an exception signed by the CISO.
3.  **DBRE Capacity Check:** Automated script queries AWS Resource Groups to ensure service quota limits for the target region (e.g., RDS instance count limit of 40 per region) are not exceeded.
4.  **Compliance (Automated):** If "Contains PHI?" is "Yes", the workflow triggers a pre-provisioning compliance check in Drata against HIPAA controls; if the business unit has not completed the annual HIPAA refresher training, provisioning is blocked.

**5.1.3 Terraform Deployment**
Once approved, the DBRE Lead merges the provisioning Terraform module. The standard module applies these defaults:
- `storage_encrypted = true`
- `backup_retention_period = 30` (Overrideable via ticket)
- `auto_minor_version_upgrade = false` (Managed via patching windows)
- `deletion_protection = true`
- `monitoring_interval = 60` (Enhanced Monitoring)
- Tagging: `Environment`, `DataClass`, `Owner`, `CostCenter` (Tag policy enforcement prevents launch if missing).

### 5.2 Access Controls

Access to the database layer is segregated from the application layer. Meridian uses a zero-trust network access (ZTNA) model.

**5.2.1 Authentication**
- **Human Users:** No human persistent database credentials exist. DBRE engineers must authenticate via Okta SSO, then assume a role in HashiCorp Vault (AWS Secrets Engine) to generate temporary, single-use database credentials. These credentials expire after 1 hour.
- **Application Service Accounts:** Services running on Kubernetes (EKS) authenticate via IAM Roles for Service Accounts (IRSA). The `meridian-clinical-ai-role` maps to a database role `app_clinical_ro` (read-only) or `app_clinical_rw` (read-write), bypassing the need for static secrets.
- **Emergency "Break-Glass" Access:** A static credential for the `breakglass_admin` role exists physically sealed in a safe accessible only to the VP of IT Ops (Samantha Torres) and the CISO (Rachel Kim). Accessing this generates a PagerDuty Critical Alert and automated notification to the Board AI Governance Committee within 5 minutes.

**5.2.2 Authorization Model (RBAC)**
Database permissions are managed via Role-Based Access Control (RBAC) and audited quarterly.
| Database Role | Postgres Permissions | Use Case |
| :--- | :--- | :--- |
| `db_owner_automation` | `SUPERUSER` equivalent | Terraform provisioning pipelines, not accessible to humans. |
| `dba_admin` | `ALL PRIVILEGES` on objects, no `SUPERUSER` | DBRE Team JIT credentials. |
| `app_rw` | `SELECT, INSERT, UPDATE, DELETE` | Standard microservice connection pool. Schema changes restricted. |
| `app_readonly` | `SELECT` | Analytics and reporting replicas. |
| `audit_logger` | `SELECT` on `pg_catalog` | Datadog and LangSmith tracing extraction. |

**5.2.3 User Access Review (Control Activity)**
Per SOC 2 CC6.1 (Logical and Physical Access Controls), the DBRE Lead and Compliance Team execute a quarterly Access Recertification.
1.  **Extraction:** Automated script extracts all roles and grants from `pg_authid` and `information_schema.role_table_grants`, exporting to a CSV.
2.  **Attestation:** The CSV is sent via Drata to Application Owners. They must explicitly sign off that all listed users/service accounts are authorized and require the granted role.
3.  **Remediation:** Unattested access is revoked within 72 business hours. Dormant accounts (no login for 90 days) are automatically de-provisioned.

### 5.3 Backup and Restore

Meridian adheres to a "Defense in Depth" backup strategy to satisfy the Availability TSC.

**5.3.1 Backup Cadence and Types**
All production databases are subject to the following automated backup mechanisms managed by AWS Backup.

| Backup Type | Frequency | Retention | Storage Location | Encryption |
| :--- | :--- | :--- | :--- | :--- |
| **Automated Snapshots (RDS)** | Daily (03:00 AM EST) | 30 Days (Default) | S3 Standard (Same region) | AWS KMS CMK |
| **Continuous WAL Archiving (PITR)** | 5-minute intervals | 30 Days (Default) | S3 Standard | AWS KMS CMK |
| **Long-Term Retention (LTR) Snapshots** | Monthly (1st of month) | 7 Years | S3 Glacier Deep Archive (Cross-region copy) | Cross-region KMS |
| **Logical Dumps (pg_dump)** | Weekly (Sunday 01:00 AM) | 90 Days | S3 Standard-IA | AWS KMS CMK |

**Exception for Financial Systems:** HealthPay databases (subject to SR 11-7 model governance) have WAL retention boosted to 7 years to allow for model recalculation and regulatory examination. This is configured via the `rds_backtrack_window` and explicit WAL archival scripts.

**5.3.2 Backup Validation (Recovery Drills)**
A backup is not considered successful until it is verified restorable.
- **Automated Integrity Check:** Every snapshot triggers an automated "Restore To Test" process (SOP-ITOP-011-SCRIPT-02). An ephemeral RDS instance `*-restore-test` is spawned in an isolated subnet. The restoration log is scraped for corruption errors. Success/failure is logged to Datadog.
- **Quarterly Disaster Recovery Drill (Tabletop & Technical):** The DBRE team performs a full production cutover to the Azure DR environment. The drill is graded on meeting RPO (1 hour) and RTO (4 hours) objectives. A report is presented to the VP of Engineering and the Board AI Governance Committee.

**5.3.3 Restoration Request (ServiceNow)**
If a restore is required (excluding automated tests):
1.  Requester submits `SOP-ITOP-011-DB-RESTORE`.
2.  **VP of Engineering Approval** is mandatory for Production restores.
3.  DBRE performs the restore to a new instance (not in-place overwrite). The `meridian_rds_restore` runbook ensures the restored instance is in a `sandbox` security group with zero egress to production until data integrity is confirmed.

### 5.4 Performance Tuning and Monitoring

Performance management is proactive, driven by the SRE principle of eliminating toil through observability.

**5.4.1 Thresholds and Alerting**
Datadog Database Monitoring (DDM) is configured to alert via PagerDuty based on the following baseline metrics:

| Metric | Warning Threshold | Critical Threshold | Action |
| :--- | :--- | :--- | :--- |
| **CPU Utilization** | 70% sustained > 15 min | 85% sustained > 5 min | Evaluate connection pooling; scale instance class. |
| **Read IOPS Latency** | > 10ms/op | > 50ms/op | Enable Enhanced Monitoring; check for `FULL TABLE SCAN` locks. |
| **Storage Space Available** | < 25% | < 10% | Auto-scale storage (enabled by default up to 5 TB cap) or manual purge. |
| **Connection Count** | 80% of `max_connections` | 90% of `max_connections` | Drain connections; check for connection leak in app pool. |
| **Replication Lag** | > 60 seconds | > 120 seconds | Investigate reader node; potentially restart replication. |

**5.4.2 Index Management**
Unbridled index creation degrades write performance.
- **Automated Unused Index Detection:** MLflow runs a weekly scan on `pg_stat_user_indexes`. Indexes with an `idx_scan` of 0 for 60 days and no `pg_stat_user_indexes.idx_tup_read` activity are flagged for dropping.
- **`pg_stat_statements` Review:** Top 20 slow queries are posted to a #db-perf-eng Slack channel weekly by the DataDog digest bot. Application owners have 2 sprints (4 weeks) to optimize queries ranked above the "red line" (>100ms average latency).

**5.4.3 Major Version Upgrades**
Due to the risk profile of clinical systems, in-place major version upgrades (MVU) are prohibited. The DBRE team uses the Blue/Green deployment strategy for relational engines:
1.  Provision new "Green" cluster with target version (e.g., PostgreSQL 16).
2.  Use AWS Database Migration Service (DMS) for full load and ongoing Change Data Capture (CDC).
3.  Application flip-over via weighted DNS (Route 53) during the window.
4.  Retention of "Blue" cluster in a stopped state (cost-optimized) for 7 days for rollback safety.

### 5.5 Patching and Vulnerability Management

**5.5.1 Patch Classifications**
- **Emergency Security Patches (Zero-Day):** CVE score ≥ 9.0. Action initiated within 24 hours of NIST NVD notification. Requires Emergency Change Advisory Board (eCAB) bypass.
- **Routine Security Patches:** CVE score ≥ 7.0 and < 9.0. Actioned within 14 days.
- **Scheduled Minor Version Upgrades:** Bug fixes and performance improvements. Batched into a monthly maintenance window.
- **Operating System Patching:** Managed by AWS RDS; Meridian subscribes to maintenance event SNS topics. If "Required" maintenance causes an availability disruption during business hours, we have a ServiceNow playbook to reschedule window within AWS limits.

**5.5.2 Maintenance Windows**
- **Tier 1 (Clinical AI / HealthPay):** Sundays 02:00 - 06:00 AM EST. Bi-weekly rotation.
- **Tier 2 (Internal Analytics, Dev/Staging):** Saturdays 01:00 - 05:00 AM EST. Monthly.
- **Validation:** Post-patch, regression tests from the application health-check suite (`app-health-check-suite`) must run and pass "green" before the change ticket is closed. The test suite explicitly validates key cryptographic functions (TLS handshake, cipher suite negotiation) to ensure no downgrade occurs.

### 5.6 PHI Protection

Meridian databases handling PHI must implement specific technical controls at the data layer. Application-level controls are defined in the product-specific SOPs.

**5.6.1 Data Sanitization**
Before production data is copied to non-production environments (Dev/Staging), it must pass through an automated sanitization pipeline (see SOP-ITOP-040).

**5.6.2 Data Disposal**
When a database instance is decommissioned, the following procedure is strictly followed:
1.  **Logical Deletion:** Drop all tables and schema using the `drop cascade` command.
2.  **Physical Overwrite:** Execute AWS RDS `restore-deleted-db` is not an option; final snapshot is taken, and deletion is executed.
3.  **Snapshot Deletion:** The final snapshot retention is set to 0 days (immediate delete) to avoid dangling data stores. For PHI-bearing systems, the KMS CMK used for encryption is scheduled for deletion (pending window enabled), ensuring cryptographic erasure. Certificate of Destruction is filed in the ServiceNow asset record per SOP-ASSET-009.

---

## 6. Controls and Safeguards

This section maps Meridian’s specific technical and administrative controls to the Trust Services Criteria (TSC) for SOC 2, ensuring that logical access, security, and availability criteria are met.

### 6.1 Security Controls (Common Criteria)

| Control ID | Control Description | TSC Mapping | Mechanism |
| :--- | :--- | :--- | :--- |
| **DBA-C1** | Multi-Factor Authentication (MFA) is required for all interactive database access (including JIT). | CC6.1, CC6.6 | Okta SSO + Vault LDAP bind enforcing MFA challenge. |
| **DBA-C2** | Network segmentation prevents direct internet exposure of databases. | CC6.6 | All RDS instances deployed in private subnets (10.0.x.x). Security Groups restrict ingress only to EKS node group and Bastion Host. |
| **DBA-C3** | Audit logging captures all DDL, DCL, and DML modifications on Restricted data. | CC7.2 | pgAudit extension configured to `audit.log = 'write, ddl, role'`. Logs streamed to CloudWatch and S3. |
| **DBA-C4** | Keys are managed centrally with separation of duties from operations. | CC6.1, CC6.3 | AWS KMS keys managed via a dedicated `security-account`. IT Ops account has `encrypt/decrypt` usage rights but no key modification/rotation rights. |

### 6.2 Availability Controls (Availability TSC)

| Control ID | Control Description | TSC Mapping | Mechanism |
| :--- | :--- | :--- | :--- |
| **DBA-AV1** | Real-time replication of transactional financial data. | A1.3 | Aurora Global Database spanning `us-east-1` (Primary) and `eu-west-1` (Replica) for HealthPay. |
| **DBA-AV2** | Automated health check monitoring and automatic failover. | A1.3 | RDS Multi-AZ (Multi-Availability Zone) deployment with a Standby instance in a physically separate AZ. Automatic DNS switch on primary failure (60-120s failover). |
| **DBA-AV3** | Capacity planning and predictive scaling threshold alerts. | A1.2 | Datadog forecast engine monitors storage growth. A ticket is auto-generated when forecasted storage reaches 80% of allocated within 45 days. |

### 6.3 Process Integrity Controls (Processing Integrity TSC)

| Control ID | Control Description | TSC Mapping | Mechanism |
| :--- | :--- | :--- | :--- |
| **DBA-PI1** | Schema changes managed through a formal promotion pipeline. | PI1.3 | Liquibase changesets stored in GitHub, executed by the CI/CD runner (`github-actions`), not manual SQL CLI. |
| **DBA-PI2** | Input validation at the database layer. | PI1.3 | Strict `CHECK` constraints and `ENUM` data types enforced at the schema level for data classes like `Patient_Risk_Score` (0.0 to 1.0) to prevent out-of-bounds ingestion errors. |
| **DBA-PI3** | Checksum validation during replication transport. | PI1.4 | Aurora global database replication validates block-checksums continuously; any mismatch triggers a PagerDuty alert and halts replication to the secondary region until resolved. |

---

## 7. Monitoring, Metrics, and Reporting

Accountability for database health is driven by real-time dashboards and monthly business reviews.

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target | Measurement Method | Frequency |
| :--- | :--- | :--- | :--- |
| **Availability (Uptime)** | 99.99% (Financial) / 99.95% (Clinical) | CloudWatch Composite Alarm (Excludes defined windows) | Monthly |
| **Mean Time to Recovery (MTTR)** | < 1 hour for Tier 1 | PagerDuty analytics from alert trigger to all-clear | Rolling Quarter |
| **Backup Success Rate** | 100% | AWS Backup vault metrics | Weekly |
| **Restore Drills Success Rate** | 100% (Quarterly) | Automated test script outcome log | Quarterly |
| **Access Recertification Timeliness** | 100% completed by due date | Drata dashboard control status | Quarterly |
| **Patching SLA Adherence** | 100% for Critical CVEs | Kenna Security / Datadog dashboard | Monthly |

### 7.2 Reporting Cadence

- **Weekly Operations Review:** DBRE Lead reviews the "Wall of Health" (Datadog dashboard) with the VP of IT Operations. Focus on P1/P2 incident resolution and capacity anomalies.
- **Monthly Service Review (MSR):** VP of IT Operations presents database operational performance to the CTO/VP Engineering and CISO. Includes KPI traffic light reporting (Red/Yellow/Green) and a review of any major schema changes impacting the SOC 2 control design.
- **Quarterly Audit Review:** Compliance team extracts access logs, patching reports, and backup logs to provide to external SOC 2 auditors as evidence for Controls DBA-C3, DBA-AV1, and DBA-PI1.

### 7.3 Dashboard Specification
The "Meridian Ops Command Center" wall display must include the following database widgets:
1.  **Geo-Map:** Live traffic routes between Boston `us-east-1` and Berlin `eu-west-1`.
2.  **Top-N Slow Queries:** Scrollable list of `pg_stat_statements` sorted by total_time in the last hour.
3.  **Replication Lag Heatmap:** Visual indicator of lag times in milliseconds for all reader nodes in the Global Database configuration.
4.  **Encryption Verification:** A binary script check (1 = all instances encrypted with active keys; 0 = violation). Red alert if state changes to 0.

---

## 8. Exception Handling and Escalation

Meridian recognizes that strict compliance may impede urgent business objectives. Exceptions to this SOP must be managed rigorously.

### 8.1 Exception Process
1.  **Submission:** A "Policy Exception Request" is raised in ServiceNow (Catalog Item: `SOP-EXCEPTION`), with a link to this SOP (`SOP-ITOP-011`) and the specific control being exempted (e.g., "Disable deletion protection for 24 hours to remove stale staging stack").
2.  **Risk Assessment:** The CISO (Rachel Kim) or delegate (Security Architecture Lead) must provide a written risk acknowledgment, quantifying the potential severity and likelihood of exploitation.
3.  **Approval Authority:**
    - **Tier 1 (Non-PHI/Prod):** VP of IT Operations.
    - **Tier 2 (PHI/Financial):** VP of Engineering AND CISO joint approval.
    - **Regulatory Impact (GDPR/EU AI Act):** Must include General Counsel (Maria Gonzalez) signature.
4.  **Expiration:** Exceptions are time-bound. Maximum duration of 90 days, after which a new exception or a permanent control modification (via SOP version update) is required.

### 8.2 Escalation Path for Database Incidents
| Severity | Alert Channel | First Responder | Escalation Trigger (Time to Acknowledge) | Escalation Target |
| :--- | :--- | :--- | :--- | :--- |
| **SEV 1** (Full outage) | PagerDuty Direct Page | DBRE On-Call | 5 minutes | VP of IT Ops (S. Torres), Incident Commander |
| **SEV 2** (Degraded Perf) | PagerDuty / Slack `#ops-incident` | DBRE On-Call | 15 minutes | DBRE Lead, Application Owner |
| **SEV 3** (Warning) | Slack `#ops-alert` | DBRE Squad | Business Hours (4 hours) | Automated ticket creation in Jira |

---

## 9. Training Requirements

Personnel responsible for executing this SOP must maintain demonstrable competency.

### 9.1 Required Training Matrix
| Role | Training Module | Provider | Frequency | Retake Policy |
| :--- | :--- | :--- | :--- | :--- |
| **DBRE Engineers** | Advanced PostgreSQL Administration | External (A Cloud Guru) | Annually | Fail > 80% score requires 3 days retraining |
| **DBRE Engineers** | Meridian Data Handling & PHI Sanitization | Internal (LMS) | Annually | Mandatory 100% Score |
| **Application Owners** | Secure Database Coding (SQL Injection Prevention) | Internal (LMS) | Annually | Locked from production access until passed |
| **Compliance/Internal Audit** | Access Review Auditing in Drata | Internal (Lunch & Learn) | Annually | N/A |
| **Everyone** | SOC 2 Trust Services Criteria Overview | Internal (LMS) | Annually | Mandatory for system access |

### 9.2 Competency Validation
The VP of IT Operations will validate DBRE competencies bi-annually through "Game Days" (Chaos Engineering events). Database-specific scenarios (e.g., "Corrupted WAL segment", "AZ failure") are injected into the staging environment, and engineer response time and accuracy are evaluated against a standardized incident response checklist.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
| SOP ID | Document Title | Relationship |
| :--- | :--- | :--- |
| `SOP-DSEC-003` | Data Classification and Handling | Defines data sensitivity labels used in provisioning. |
| `SOP-ITOP-002` | Change Management Policy | Governs schema and infrastructure change approvals. |
| `SOP-ITOP-005` | Incident Response Plan | Defines SEV levels and communication frameworks. |
| `SOP-ITOP-040` | Data Lifecycle Management & Sanitization | Rules for masking/obfuscating data pre-refresh. |
| `SOP-IA-001` | Identity and Access Management | Okta and Vault integration standards. |
| `SOP-AI-007` | AI Model Data Input/Output Validation | Data quality constraints for Clinical AI Platform feature stores. |
| `SOP-FIN-015` | HealthPay Credit Risk Model Governance | SR 11-7 model data validation and retention standards. |

### 10.2 External Standards and Regulations
- **AICPA SOC 2** (TSP Section 100, Trust Services Criteria: CC6 series, A1 series, PI1 series)
- **NIST SP 800-53 Rev. 5** (Access Control, Audit and Accountability, Contingency Planning families)
- **CIS Benchmark for AWS RDS PostgreSQL** (Version 1.3.0)
- **AWS Well-Architected Framework** (Reliability and Security Pillars)

---

## 11. Revision History

| Version | Date | Author | Description of Change |
| :--- | :--- | :--- | :--- |
| 1.0 | 2020-03-15 | IT Ops (Initial) | Initial policy creation covering on-premise PostgreSQL migration. |
| 2.4 | 2021-06-01 | Samantha Torres | Major rewrite for AWS cloud-native migration; introduced JIT access. |
| 3.1 | 2022-09-12 | Rachel Kim | Added TDE enforcement section, upgraded TLS cipher requirements to 1.3. |
| 4.2 | 2023-01-20 | DBRE Lead | Introduced Blue/Green deployment strategy and LangSmith tracing integration. |
| 4.5 | 2024-04-10 | Thomas Anderson | Strengthened SOC 2 controls mapping, added DBA-PI3 checksum control, updated access recertification timelines to quarterly. |
| 4.7 | 2024-11-01 | Samantha Torres | Updated for EU AI Act high-risk classification alignment; added Snowflake and Pinecone governance modules; updated DR drill cadence to Quarterly; extended Financial WAL retention to 7 years. |

---
**Document Classification: Internal**
© 2024 Meridian Health Technologies, Inc. Unauthorized reproduction or distribution is subject to disciplinary action.