---
sop_id: "SOP-ITOP-019"
title: "Log Management and Retention"
business_unit: "IT Operations & Infrastructure"
version: "4.2"
effective_date: "2024-06-12"
last_reviewed: "2025-02-17"
next_review: "2025-08-26"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the lifecycle management of log data at Meridian Health Technologies, Inc. ("Meridian"). The purpose of this document is to define the requirements for the collection, centralization, normalization, security, retention, and disposal of machine-generated log data to ensure the confidentiality, integrity, and availability (CIA) of information assets. Effective log management provides the foundational telemetry necessary to detect cybersecurity incidents, troubleshoot operational failures, maintain audit trails for all regulated products, and demonstrate compliance with the Trust Services Criteria (TSC) under SOC 2, specifically the Security and Availability criteria.

### 1.2 Scope
This SOP applies to all Meridian information systems, including but not limited to:

| **Business Unit** | **Systems in Scope** | **Specific Applicability** |
| :--- | :--- | :--- |
| **SaaS Platform & IT Infrastructure** | AWS production accounts (`prod-us-east-1`, `prod-eu-central-1`), Azure DR tenant, Okta identity fabric, corporate network devices, Datadog agents. | All OS, application, database, and network logs. |
| **Clinical AI Platform** | SageMaker instances, Kubeflow pipelines, MLflow tracking server, inference endpoints (FDA 510(k) cleared), MDR CE-marked model containers. | Model input/output logs, inference latency, training audit trails. |
| **HealthPay Financial Services** | AWS payment card environment enclave, ECS Fargate containers, RDS for Aurora clusters. | Access logs, transaction logs, API gateway logs. |
| **MedInsight Analytics** | ETL pipeline workers (Airflow), data warehouse compute (Snowflake), web application servers. | Query execution logs, data access telemetry, ETL job status logs. |

All components in the Meridian asset inventory (CMDB, tracked via ServiceNow) must output logs in accordance with the configuration baselines defined herein. Shadow IT and unmanaged endpoints outside the CMDB are explicitly excluded, but any connection to Meridian systems must be logged at the corporate proxy boundary (Zscaler).

---

## 2. Definitions and Acronyms

For the purposes of this document, the following terms and acronyms are defined:

| **Term** | **Definition** |
| :--- | :--- |
| **Aggregated Log** | A log source that is collected, parsed, and centralized in the SIEM/data lake (Splunk). A log is "active" when it is searchable within the Hot/Warm tier of the Splunk index. |
| **Audit Trail** | A chronological sequence of log records sufficient to reconstruct the sequence of activities surrounding an event or operation (SOC 2 CC7.2). |
| **Cold Storage (Frozen)** | A non-searchable, immutable storage archive (AWS S3 Glacier Deep Archive). Data in cold storage must undergo a thawing (restore) process before analysis, subject to a standard 24-hour retrieval SLA. |
| **HIPAA-designated Data** | Log data that directly or indirectly contains electronic Protected Health Information (ePHI). This includes payloads from MedInsight clinical data exchanges or clinical audit events from the CE-marked platform. |
| **Log Integrity** | The property that log data has not been altered or destroyed in an unauthorized manner. Meridian implements cryptographic signing via SHA-256 hashing and write-once-read-many (WORM) storage models. |
| **PHI Exposure** | A state wherein ePHI is present in an unstructured or unencrypted log stream outside of the authorized database layer, such as a DEBUG-level application log. |
| **Retention Period** | The duration, measured in days from the event timestamp, for which a specific log source is retained in an indexed (hot/warm) or archived (cold) state. |

### 2.2 Acronyms

- **AWS:** Amazon Web Services
- **CIS:** Center for Internet Security
- **CSPM:** Cloud Security Posture Management (Wiz)
- **FIM:** File Integrity Monitoring
- **SIEM:** Security Information and Event Management (Splunk)
- **S3:** Simple Storage Service
- **TSC:** Trust Services Criteria (SOC 2)
- **WORM:** Write Once, Read Many

---

## 3. Roles and Responsibilities

The following table defines the RACI (Responsible, Accountable, Consulted, Informed) matrix for the Log Management Lifecycle. All named roles represent Meridian staff or designated groups defined in Active Directory.

| **Activity / Decision** | **VP, IT Ops** <br>(S. Torres) | **VP, Engineering** <br>(D. Park) | **Security Architect** <br>(A. Vance) | **Log Mgmt. Engineer** <br>(IT Ops) | **Product Owners** | **Compliance Officer** <br>(L. Chen) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Policy & SOP Authoring** | **A/R** | A | R | C | C | C |
| **Log Source Onboarding** | I | I | C | **A/R** | C | I |
| **Parser Configuration (Ingestion Pipeline)** | I | I | C | **A/R** | C | I |
| **SIEM Dashboard Creation** | C | I | **A/R** | R | I | I |
| **Cold Storage Archive Management** | C | I | C | **A/R** | I | C |
| **Incident Investigation Support** | C | C | **A/R** | C | C | I |
| **Compliance Evidence Delivery (SOC 2)** | C | I | C | R | C | **A/R** |
| **PHI/PII Data Masking Configuration** | I | C | **A/R** | R | C | C |
| **Exception Approval** | C | **A** | C | R | I | R |

**Specific Role Definitions:**

- **Log Management Engineer (IT Operations):** A designated individual reporting to the Director of ITOps. This role holds administrative rights on the Splunk Forwarder management console, the Zscaler Private Access proxy, and the SIEM (Search Head and Indexer Clusters).
- **Product Owner:** Responsible for defining the "logging standard" for their specific application (e.g., HealthPay API logging formats) and approving the ingestion of business-layer audit logs.

---

## 4. Policy Statements

Meridian Health Technologies, Inc. establishes the following high-level enterprise policy statements regarding Log Management and Retention. These statements are binding and enforced via the technical controls described in Section 6.

**PS-019-01: Centralized Aggregation Mandate**
All production environments, CI/CD pipelines, and corporate identity systems must stream high-fidelity logs to the centralized Meridian log aggregation platform (Splunk) in real-time or near-real-time (≤ 5-minute latency). Local storage on ephemeral containers and virtual machines is prohibited as a primary log retention strategy.

**PS-019-02: Retention Schedule Adherence**
Log data must be managed strictly according to the defined retention schedule tiers (detailed in Section 5.3). Under no circumstances shall logs be deleted to circumvent forensic investigation or compliance audits. Automated destructive deletion scripts are permitted strictly for the "Stale" tier, subject to dual-approval by the VP of IT Operations and the Compliance Officer via change control.

**PS-019-03: Integrity and Non-Repudiation**
All log data traversing the ingestion pipeline must be encrypted in transit (TLS 1.2+). Log data in persistent storage (Hot, Warm, or Cold tiers) must be stored on an immutable storage layer. Any mechanism designed for log deletion or modification must generate its own immutable audit trail recording the identity of the actor, the timestamp, and the justification ticket (SOP-ISMS-004).

**PS-019-04: Sensitive Data Masking**
Log content must not contain unstructured ePHI or PCI-DSS cardholder data. Application developers are required to utilize parameterized logging templates that scrub or tokenize sensitive data prior to writing to STDOUT/STDERR. Production log stream regex filters are mandated as a secondary control at the ingestion pipeline level.

**PS-019-05: Access Review for Log Data**
Access to the Splunk platform (raw log indices) must be reviewed on a quarterly basis according to the access control matrix defined in SOP-IAM-001. Access to raw log data is restricted to the IT Operations, Security Architecture, and Compliance Officer roles. Product Owners are granted only pre-built dashboard access, not raw search capabilities, unless specific approval is granted for incident triage.

---

## 5. Detailed Procedures

This section outlines the operational procedures for the end-to-end log lifecycle. Unless otherwise specified, all steps must be conducted by the Log Management Engineer.

### 5.1 Log Collection and Source Configuration

Log collection involves deploying forwarders and configuring endpoint agents on every Meridian digital asset.

#### 5.1.1 AWS CloudWatch to Splunk Integration

1.  **Role Validation:** Navigate to AWS IAM. Validate that the `Splunk-EventBridge-Forwarder` role has the managed policy `Meridian-AuditStream-Policy` attached, restricting access to only the `Prod-Audit` and `Prod-AppLogs` log groups.
2.  **EventBridge Rule Assessment:** In AWS EventBridge, verify the rule `KinesisFirehose-CWE` is active. This rule captures all API calls matching `kms.amazonaws.com` (Key Administration), `iam.amazonaws.com` (Policy Changes), and `ec2.security-group` modifications.
3.  **Kinesis Firehose Stream Configuration:**
    - Navigate to Kinesis > Delivery Streams. Select `meridian-aws-audit-firehose`.
    - Verify the "Destination" is set to `Splunk Cloud (HTTP Event Collector - HEC)`.
    - **Indexer Acknowledgment:** Ensure "Retry Duration" is set to `300 seconds`. If Splunk indexers are down, Firehose must buffer data in the `meridian-firehose-backup-s3` bucket (Retention: 30 days). Validate the backup bucket S3 lifecycle rule `MoveToGlacierAfter7Days` is active.
    - **Metadata Extraction:** Validate the transformer Lambda `meridian-log-enricher-prod` is attached to the stream, injecting `account_id`, `timestamp`, and `region` metadata into the raw JSON payload.
4.  **Agent Health Check (Universal Forwarder):** For EC2 instances (HealthPay Payment API, Clinical ML inference servers):
    - Execute SSH using a privileged ITOps account via AWS Session Manager.
    - Run `sudo /opt/splunkforwarder/bin/splunk status`.
    - Confirm status is `running` and tailing the correct `inputs.conf` stanza (e.g., `/var/log/apps/*.log`).
    - In the Splunk Deployment Server UI, verify the client is reporting a `PhoneHome` interval of ≤ 300 seconds.

#### 5.1.2 Kubernetes (Kubeflow/ML Inference) Logs

1.  **DaemonSet Verification:** Using `kubectl` context for `prd-eks-clinical-us-east-1`, run `kubectl get pods -n logging | grep splunk-forwarder`.
    - Validate that there are `N` running pods, where `N` equals the number of worker nodes.
    - Describe a pod to check for errors: `kubectl describe pod [pod-id] -n logging`.
2.  **Sidecar Pattern (GPU Nodes):** For GPU inference workloads running the CE-marked Clinical AI models, verify the `log-router` sidecar container is running in the same pod as the Triton Inference Server. Validate the shared `emptyDir` volume mount ` /var/log/triton-shared ` is present, acting as a staging scratch pad for the Fluent Bit sidecar.

#### 5.1.3 Corporate Infrastructure (Okta & Zscaler)

1.  **Okta System Log (API Streaming):**
    - Access the Okta Admin Console > Reports > System Log.
    - Select the "API Access" tab. Verify the token `Meridian-SIEM-Token` is Active.
    - Validate the polling script on the `meridian-log-collector-prod` EC2 instance (`crontab -l | grep okta_audit`) queries the `/logs` endpoint every 60 seconds.
    - Critical event streams: `user.session.start`, `user.authentication.failure`, `group.member.add`, `system.agent.update`.
2.  **Zscaler Private Access (ZPA):**
    - Navigate to the Zscaler Admin Portal > Administration > Log Receiver.
    - Validate the LogStream (NSS WebSocket endpoint) points to the Meridian Splunk Indexer Cluster Load Balancer URL: `https://splunk-hec.meridian.internal:8088`.
    - Health check: Confirm the "Active" pulse status on the NSS feed. If "Disconnected," escalate immediately to Network Engineering (Priority 1).

### 5.2 Centralization and Normalization (Ingestion Pipeline)

The Meridian log pipeline indexes raw data into the Meridian Splunk Indexer Cluster at `indexer-cluster.prod.meridian.internal`. A mandatory normalization step ensures SOC 2 audit readiness.

#### 5.2.1 Index-Time Field Extraction

1.  **Source-typing Validation:** Logs are automatically source-typed based on the `sourcetype` field. The Log Management Engineer must validate that custom Source Types (`meridian:healthpay:api`, `meridian:clinical:nvidia`) are mapped correctly.
2.  **CIM Compliance (Common Information Model):** Run the following Splunk Search Processing Language (SPL) weekly to check CIM data model acceleration:
    ```spl
    | tstats summariesonly=false count from datamodel="Change.All" by _time span=1h
    | timechart avg(count) as "Event Density"
    ```
    - Target: No zero-density anomalies during business hours for the `Change` data model (maps to `Change.All_Types`). Failures indicate broken acceleration tags and must be fixed within 8 business hours (SLA: `SYS-NORMAL-8h`).

#### 5.2.2 Sensitive Data Masking (Ingestion Layer)

This pipeline control handles potential leaks from poorly configured Application Developers.

1.  **SEDCMD Transformation (Regex Masking):** On the **Heavy Forwarder** tier (`/opt/splunk/etc/apps/`):
    - Open `props.conf`.
    - Verify the presence of the `[meridian:clinical:hl7]` stanza.
    - Validate the `SEDCMD-PHI_mask = s/(\b[0-9]{3}-[0-9]{2}-[0-9]{4}\b)/<SSN_REDACTED>/g` expression is active. This mask operates at wire-speed before the data is written to the disk queue.
2.  **Validation Procedure:**
    - Inject a non-malicious test message containing a known synthetic Social Security Number via a REST call to the `meridian-inject-test` endpoint.
    - Wait 15 seconds. In Splunk, execute `index="*medinsight_test*" SSN_REDACTED`.
    - If the raw log string is returned showing the synthetic SSN, the pipeline has failed. This is a **Severity 1** security incident (Potential ePHI leak, refer to Section 8).

### 5.3 Retention Management

This is the authoritative procedure for lifecycle transition. Data management must comply with TSC CC6.1 (Logical and Physical Access Controls).

| **Data Classification** | **Source Examples** | **Tier: Hot (Indexed)** | **Tier: Warm (Searchable)** | **Tier: Cold (Frozen)** | **Tier: Stale (Destruction)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Core Security Audit** | AWS CloudTrail (Mgmt), Okta Audit, VPC Flow Logs, Wiz CSPM | 90 days | 275 days (365 total) | 1,825 days (5 years) | Day 2,191: Secure Overwrite |
| **Application (HIPAA/PHI)** | MedInsight ETL Jobs, Clinical Logs (`triton.log`), HealthPay Transaction | 30 days | 60 days (90 total) | 640 days (~2 years) | Day 731: Secure Overwrite |
| **Infrastructure** | CPU/Memory Metrics, K8s Pod Status, NGINX Access logs (non-ePHI) | 7 days | 30 days | 330 days (1 year) | Day 366: Simple Delete |

#### 5.3.1 Index Retirement and S3 Archival

1.  **Retention Script Execution:** On the 1st day of each month, the Splunk search head invokes the `meridian_retention_script.py` to "freeze" buckets older than the Warm tier threshold.
2.  **S3 Glacier Deep Archive WORM:** Frozen data is streamed to the S3 bucket `meridian-log-immutable-archive`. The bucket policy enforces **S3 Object Lock in Governance Mode** with a minimum retention period of `180 days`.
3.  **Archival Audit Trail:** Freezing an index triggers a record in the local audit index: `index="_internal" sourcetype="splunk_archiver"`.

### 5.4 Integrity Protection

The implementation of the WORM policy and Hash Chain Verification serves as the compensating control for the Availability and Integrity Trust Services Criteria.

#### 5.4.1 Hash Chain Verification
1.  **SHA-256 Fingerprinting:** Upon archival (Step 5.3.1, Item 3), the S3 PUT operation triggers a Lambda function that computes a SHA-256 hash of the raw `.tsidx` bucket file.
2.  **Tamper-Evident Ledger:** The hash is written to the `meridian-log-integrity-lock` DynamoDB table, which has Point-in-Time Recovery (PITR) enabled.
3.  **Periodic Attestation (Quarterly):** The Compliance Officer requests a forensic sample of 5 log buckets from the archive. The Log Mgt. Engineer generates a fresh hash of the S3 object and compares it against the DynamoDB ledger. A match validates the "Integrity" control.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| **Control ID** | **Control Description** | **Mechanism** | **SOC 2 Mapping** |
| :--- | :--- | :--- | :--- |
| **TC-019-01** | Encryption of Log Data in Transit | Universal Forwarder (UF) to Splunk Indexer data streams are force-wrapped in TLS 1.2 using a Meridian Internal Certificate Authority (CA) certificate; the `sslVerifyServerCert = true` flag is set in `outputs.conf`. Kinesis Firehose stream transmission to Splunk HEC endpoint uses TLS 1.3. | CC6.1 |
| **TC-019-02** | Encryption of Log Data at Rest | AWS S3 objects in the `meridian-log-immutable-archive` bucket are encrypted using the `meridian-archive-key` managed by AWS Key Management Service (KMS). The KMS key policy restricts `kms:Decrypt` to the `Log-Access-Role`. | CC6.1 |
| **TC-019-03** | FIM for Log Binaries | AWS Inspector and Trend Micro Deep Security agent perform File Integrity Monitoring on Splunk Heavy Forwarders (`/opt/splunkforwarder/bin/` and `/opt/splunk/etc/system/local/`). Any unplanned modification triggers a Security Hub alert. | CC7.2 |
| **TC-019-04** | Immutable Storage | S3 Object Lock (Governance mode) prevents deletion of cold-tier log objects, even by root administrator users, for a period of 180 days. A Retention Time Extension mechanism exists for Legal Holds. | CC6.1, A1.2 |

### 6.2 Administrative Controls

| **Control ID** | **Control Description** | **Evidence / Frequency** |
| :--- | :--- | :--- |
| **AC-019-01** | Quarterly Access Review | The VP of IT Operations and the Compliance Officer review the Splunk `system_auth` role list. Members of `splunk_admin` and `splunk_power` must be verified against current active Employee IDs. (TSC A2.2). |
| **AC-019-02** | Minimum Necessary Access for PHI | The `medinsight_raw_log` index is configured with a granular access control list (ACL) in Splunk. Access is restricted to a Security Group containing the `MedInsight_Support_Engineers` role. Access to ePHI-level logs requires justification in a ticket referencing SOP-PRIV-002. The minimum necessary standard is enforced by role limitations, but per-team granularity within the MedInsight index is managed by the Product Owner, not centrally enforced by the ITOps log platform team for every sub-search. |
| **AC-019-03** | Breach Notification Procedure | Upon detection of unauthorized access to a log repository, Security Architecture executes SOP-IR-003 (Incident Response). Log data exposure is treated as a breach. Notification to affected customers and the Meridian Legal team must proceed promptly upon confirmation. Coordination with Product Management for user notification is mandated. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The ITOps team leverages the Meridian Operations portal (Grafana) for real-time monitoring, supported by the metrics below:

| **Metric** | **Definition** | **Critical Threshold (Alert)** | **Warning Threshold** | **Measurement Tool** |
| :--- | :--- | :--- | :--- | :--- |
| **Log Ingestion Latency** | Delta between event timestamp and index timestamp in Splunk. | > 15 minutes (for Security logs like Okta) | > 5 minutes | Splunk `_internal` index props latency |
| **Forwarder Connectivity** | Percentage of universal forwarders reporting to the Deployment Server. | < 85% | < 95% | Splunk Deployment Server Monitoring Console |
| **Storage Volume Rate** | Daily GB of log data ingested, tracked per index to catch "log-explosion" incidents (e.g., verbose debugging left on). | % deviation > 40% day-over-day per index | % deviation > 20% | Splunk License Usage Report / CloudWatch Metrics |
| **Masking Engine Failure Rate** | Count of logs hitting the `regex_fail` metric on the Heavy Forwarder (meaning data passed without being matched). | > 0 events / hour | N/A (Zero-tolerance) | DataDog APM custom metric on `splunk-hwf-prod` fleet |

### 7.2 Reporting Cadence

A standardized "Log Health & Compliance Report" is generated by the Splunk Enterprise Security (ES) reporting suite. The following reports are packaged and submitted:

- **Weekly (Operations):** "License Usage & Storage Trending" report to the Director of IT Operations. Includes a breakdown of the top-10 log-producing hosts and a "Data Quality" score (percentage of logs with valid timestamps).
- **Monthly (Compliance):** "Splunk Access Audit" report detailing all user search actions, role changes, and index retirement activities over the past 30 days. Submitted to Compliance Officer (L. Chen).
- **Quarterly (Stakeholders):** "Log Retention Attestation" report presented to VP of Engineering (D. Park) and CISO. This report includes the quarterly hash-chain attestation results (Section 5.4.1, Item 3) and a status update on any legal holds impacting log destruction timelines.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling

Any deviation from the configuration baselines or procedures defined in this SOP must be managed through the Meridian Information Security Management System (ISMS) exception process.

**Procedure:**
1.  **Request Initiation:** The requestor completes the "Logging Non-Compliance Exception" form within ServiceNow (GRC Module), detailing the technical rationale, the specific control being waived, the systems impacted, and the proposed compensating control.
2.  **Risk Assessment:** The Compliance Officer (L. Chen) performs a risk assessment on the exception. Scenarios involving ePHI or PCI data receive an automatic "High Risk" designation.
3.  **Approval Workflow:**
    - *Low/Medium Risk:* Approval required from the VP of IT Operations (S. Torres) and the Security Architect (A. Vance).
    - *High Risk:* Approval required from the VP of Engineering (D. Park) and the CISO.
4.  **Time Limit:** All exceptions are time-bound with a defined expiry date, not exceeding 12 months.

### 8.2 Escalation Path

| **Priority** | **Incident Type** | **Immediate Action** | **Escalation (First Contact)** |
| :--- | :--- | :--- | :--- |
| **P1-Critical** | Log Indexing Pipeline Down (< 50% ingestion); WORM Storage Compromised; Unauthorized Destruction of "Hot" data. | Trigger major incident response (SOP-IR-001); Engage Splunk vendor emergency support. | VP of IT Operations (S. Torres) via PagerDuty (`ops-exec-lead`) |
| **P2-High** | Masking Engine Failure (Section 5.2.2); Detection of ePHI in production log stream due to developer error. | Manually isolate the specific Heavy Forwarder; Quarantine the raw log file via S3 bucket policy denial. | Security Architect (A. Vance) via PagerDuty (`sec-on-call`) |
| **P3-Medium** | Archival (Cold Tier) job failure; Forwarder Connectivity < 90%. | Manual restart of the Splunk archiving task; Standard ticket triage for forwarder connectivity. | Log Management Engineer / ITOps Queue |
| **P4-Low** | Dashboard rendering delay; Non-critical alert noise. | Standard Helpdesk ticket. | Log Management Engineer |

Incident communications must strictly follow the Meridian Major Incident Communication Template (`FORM-COMM-002`).

---

## 9. Training Requirements

### 9.1 Training Curricula

All personnel responsible for implementing or adhering to this SOP must complete the following mandatory training.

| **Training Module Name** | **Code** | **Target Audience** | **Frequency** | **Delivery Mode** |
| :--- | :--- | :--- | :--- | :--- |
| Secure Logging & Privacy Awareness | `SEC-LOG-101` | All Application Developers & Product Owners | Annually | LMS (Meridian Learn) / Recorded Webinar |
| Splunk Administration & Operations (Advanced) | `SEC-LOG-201` | IT Operations (Log Mgt. Engineers), Security Architecture | Bi-Annually | Instructor-Led (Vendor Bootcamp) |
| HIPAA & The Audit Trail | `COMP-PHI-103` | MedInsight Analytics & Clinical AI Engineers | Annually | LMS (Meridian Learn) |

### 9.2 Tracking and Competency

- **LMS Tracking:** Completion status is tracked in the Meridian Learning Management System (SAP SuccessFactors).
- **Non-Compliance:** Personnel who are overdue for training by 30 days will have their access to Splunk administrative roles and code repositories automatically suspended by the automated Identity Governance (IGA) pipeline (Okta Workflows).
- **Attestation:** Successful completion of `SEC-LOG-201` requires a passing score of ≥ 85% on the "Meridian Splunk Architecture Lab" practical exam.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

- **SOP-ISMS-004:** Information Security Management System - Document Control & Record Keeping
- **SOP-IR-001:** Incident Response Lifecycle
- **SOP-IAM-001:** Identity and Access Management
- **SOP-PRIV-002:** Handling and De-Identification of Protected Health Information
- **SOP-CM-003:** Configuration and Change Management for Infrastructure

### 10.2 External Standards and Regulatory Frameworks

- **Trust Services Criteria (TSC) 2017 (SOC 2):** Specifically CC5.2 (Risk Assessment), CC6.1 (Logical & Physical Access), CC6.6 (External Threats), CC7.2 (Monitoring of Deviations), A1.2 (Input Integrity).
- **HIPAA Security Rule:** 45 CFR § 164.312(b) (Audit Controls) and § 164.306(d)(3) (Integrity Controls).
- **NIST SP 800-92:** Guide to Computer Security Log Management.
- **PCI DSS v4.0:** Requirement 10.7 (Retention of Audit Trail History).

---

## 11. Revision History

| **Version** | **Date** | **Author** | **Summary of Changes** |
| :--- | :--- | :--- | :--- |
| **1.0** | 2020-01-15 | J. Smith (Former CISO) | Initial creation of Log Management SOP. Baseline AWS collection and S3 archiving defined. |
| **2.0** | 2021-06-22 | A. Vance (Sec. Arch.) | Major revision to incorporate Kubernetes DaemonSet collection. Splunk CIM model compliance checks added. |
| **3.1** | 2022-09-10 | T. Nguyen (IT Ops) | Updated retention schedules to align with new MedInsight Analytics product launch. Changed from S3 "Deep Archive" to "Glacier Deep Archive" with WORM locks. |
| **4.0** | 2024-01-05 | S. Torres (VP, ITOps) | Added explicit HealthPay PCI enclave procedures. Introduced Heavy Forwarder Masking engine (Section 5.2.2) to manage ePHI risk. |
| **4.1** | 2024-03-18 | S. Torres (VP, ITOps) | Updated Zscaler NSS endpoint following internal network segmentation project. |
| **4.2** | 2025-02-17 | M. Patel (Log Mgt. Eng) | Updated approver field to David Park. Clarified Access Review cadence in Section 6.2.1. Fixed typo in S3 WORM bucket ARN reference. Added "Breach Notification" procedure in Controls section. |