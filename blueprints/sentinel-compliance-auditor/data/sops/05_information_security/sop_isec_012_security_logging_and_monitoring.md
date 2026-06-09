---
sop_id: "SOP-ISEC-012"
title: "Security Logging and Monitoring"
business_unit: "Information Security"
version: "3.3"
effective_date: "2024-02-16"
last_reviewed: "2025-08-19"
next_review: "2026-02-09"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Security Logging and Monitoring

**SOP-ID:** SOP-ISEC-012
**Version:** 3.3
**Effective Date:** 2024-02-16
**Owner:** Rachel Kim, Chief Information Security Officer
**Classification:** Internal

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for security event logging, continuous monitoring, investigation, and alerting at Meridian Health Technologies, Inc. The purpose of this document is to define the requirements, procedures, and responsibilities necessary to ensure the confidentiality, integrity, and availability of Meridian’s information systems and the sensitive data they process, including Protected Health Information (PHI), personally identifiable information (PII), and proprietary financial models.

This SOP operationalizes the detection and response capabilities required to identify anomalous activity, security incidents, policy violations, and operational degradation in real-time or near-real-time. It establishes the technical architecture, procedural workflows, and governance structures that enable Meridian to meet its regulatory obligations, contractual commitments, and internal risk appetite.

### 1.2 Scope

The provisions of this SOP apply to all information systems, networks, applications, and data stores operated by or on behalf of Meridian Health Technologies, Inc., including but not limited to:

- **Corporate Infrastructure:** End-user workstations (macOS, Windows), mobile devices enrolled in Mobile Device Management (MDM), on-premise and cloud-hosted servers, network infrastructure (firewalls, routers, switches, wireless access points), and collaboration platforms.
- **Product Environments:**
    - **Meridian SaaS Platform:** Multi-tenant cloud infrastructure hosted on AWS (us-east-1, eu-west-1) and Azure DR regions, including Kubernetes clusters (EKS/AKS), container images, serverless functions (AWS Lambda), and API gateways.
    - **Clinical AI Platform:** AI/ML training and inference pipelines, model registries (MLflow), clinical decision support APIs, and diagnostic imaging processing engines.
    - **HealthPay Financial Services:** Payment processing gateways, medical lending origination and servicing platforms, credit decisioning engines, and fraud detection models subject to SR 11-7.
    - **MedInsight Analytics:** Population health analytics engines, data warehousing (Snowflake), and ETL pipelines processing PHI for ~12 million patients.
- **Data Stores:** Structured databases (PostgreSQL, Snowflake), caching layers (Redis), message queues (Apache Kafka), vector databases (Pinecone), object storage (AWS S3, Azure Blob), and encrypted backup archives.
- **Security Tooling:** Endpoint Detection and Response (CrowdStrike Falcon), Identity Providers (Okta), Secrets Management (HashiCorp Vault), Key Management (AWS KMS), Cloud Security Posture Management (Wiz), and observability platforms.
- **All Personnel:** Full-time employees, contractors, consultants, interns, and third-party vendors accessing Meridian networks, systems, or data.

This SOP covers log generation, collection, aggregation, correlation, analysis, retention, and secure disposal. It applies to all environments, including production, staging, development, and disaster recovery.

### 1.3 Ownership and Maintenance

The Chief Information Security Officer (CISO), Rachel Kim, is the owner of this SOP. The Security Operations (SecOps) team within the Information Security business unit is responsible for its implementation, ongoing maintenance, and annual review. All Meridian personnel are responsible for adhering to the procedures outlined herein.

---

## 2. Definitions and Acronyms

| Acronym/Term | Definition |
| :--- | :--- |
| **AIOps** | Artificial Intelligence for IT Operations; application of ML to automate and enhance IT operations, including anomaly detection in log data. |
| **ALE** | Annual Loss Expectancy; a quantitative risk metric used to prioritize control investments based on SLE × ARO. |
| **ARO** | Annualized Rate of Occurrence; the estimated frequency at which a threat event is expected to occur within a year. |
| **AWS CloudTrail** | AWS service that provides a record of governance, compliance, and operational and risk auditing of AWS API calls. |
| **CI/CD** | Continuous Integration / Continuous Delivery; the automated pipeline for building, testing, and deploying code. |
| **CISO** | Chief Information Security Officer. |
| **CSIRT** | Computer Security Incident Response Team; a cross-functional team led by the CISO responsible for incident handling. |
| **CSPM** | Cloud Security Posture Management; tools that continuously monitor cloud infrastructure for misconfigurations and compliance violations. |
| **Data Lake** | A centralized repository (AWS S3 + Snowflake) used to store all structured and unstructured security log data at scale. |
| **DLP** | Data Loss Prevention; tools and processes to ensure that sensitive data is not lost, misused, or accessed by unauthorized users. |
| **EDR** | Endpoint Detection and Response; an endpoint security solution that continuously monitors end-user devices (e.g., CrowdStrike). |
| **ePHI** | Electronic Protected Health Information; individually identifiable health information transmitted or maintained in electronic media. |
| **FIM** | File Integrity Monitoring; a security process that validates the integrity of operating system and application files. |
| **IAM** | Identity and Access Management. |
| **IDS/IPS** | Intrusion Detection System / Intrusion Prevention System. |
| **IRP** | Incident Response Plan; documented procedures for managing and mitigating security incidents (SOP-ISEC-004). |
| **KPI** | Key Performance Indicator. |
| **KRI** | Key Risk Indicator. |
| **MTTD** | Mean Time to Detect; the average time elapsed between the onset of a security incident and its discovery. |
| **MTTR** | Mean Time to Respond; the average time elapsed between the discovery of a security incident and its effective containment. |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **PII** | Personally Identifiable Information. |
| **QSA** | Qualified Security Assessor; an individual certified to perform SOC 2 and PCI-DSS assessments. |
| **RACI** | Responsibility Assignment Matrix (Responsible, Accountable, Consulted, Informed). |
| **SAST/DAST** | Static/Dynamic Application Security Testing. |
| **SCIM** | System for Cross-domain Identity Management; a standard for automating the exchange of user identity information between identity domains. |
| **SecOps** | Security Operations; the team within Information Security responsible for monitoring, detection, and incident response. |
| **SIEM** | Security Information and Event Management; the centralized platform (Splunk) used for aggregation, correlation, and alerting. |
| **SLE** | Single Loss Expectancy; the monetary loss expected from the occurrence of a single risk event. |
| **SOAR** | Security Orchestration, Automation, and Response; a platform (Splunk Phantom) used to automate investigative playbooks. |
| **SOC 2** | Service Organization Control 2; a framework for managing customer data based on five Trust Service Criteria: Security, Availability, Processing Integrity, Confidentiality, and Privacy. |
| **UEBA** | User and Entity Behavior Analytics; a security process that uses analytics to understand how users and entities normally behave and detect anomalous activity. |
| **VPC** | Virtual Private Cloud; a logically isolated section of the AWS cloud. |
| **WAF** | Web Application Firewall; a service that protects web applications from common web exploits (AWS WAF). |

---

## 3. Roles and Responsibilities

The following responsibility assignment matrix defines the roles and obligations for the execution of this SOP. All named roles are expected to ensure their teams and functions adhere to these assignments.

| Role | Responsibility | Details |
| :--- | :--- | :--- |
| **All Personnel** | Responsible (R) | Generate security events through standard system usage. Immediately report any suspected security anomaly, phishing attempt, or policy violation to the Service Desk for tier-1 triage. Do not tamper with security tools or local logging agents. |
| **Service Desk** | Responsible (R), Consulted (C) | Perform initial triage of all user-reported security events. Categorize the ticket appropriately and, for any event with a potential security nexus, escalate directly to the SecOps team within 15 minutes of receipt. |
| **Security Operations (SecOps)** | Responsible (R), Accountable (A) | The primary custodian of this SOP. Owns the SIEM, IDS/IPS, EDR, and SOAR platforms. Responsible for 24/7/365 monitoring of all security dashboards, tuning correlation rules, responding to all automated alerts, performing threat hunting, and managing the incident queue. |
| **Chief Information Security Officer (CISO)** | Accountable (A), Approver | Rachel Kim is the executive owner of the enterprise monitoring strategy. Approves all exceptions to this SOP, major architectural changes to the SIEM/SOAR, and the annual review. She is the primary point of contact for regulatory examiners regarding this control. |
| **IT Infrastructure & DevOps** | Responsible (R) | Ensures all infrastructure, from bare-metal servers in corporate data centers to ephemeral Kubernetes pods, is configured to emit logs in the standardized format and that the Syslog/TCP forwarders are properly configured and healthy. Owns the "Log Source Health" dashboard. |
| **Application Engineering (Clinical, FinTech, Analytics)** | Responsible (R) | Instrument application code to emit comprehensive, structured (JSON) security and audit logs. Ensures CI/CD pipelines include checks for logging health. Participates in the "AppSec Monitoring Council" to review application-level threats. |
| **Compliance & Privacy Officer** | Informed (I), Consulted (C) | Janeese Holloway (Chief Privacy Officer) is consulted for any monitoring use cases involving user behavior analytics (UEBA) or data loss prevention (DLP) to balance security and privacy legal obligations. She is automatically informed of all confirmed PII/PHI incidents. |
| **Chief AI Officer (CAIO)** | Accountable (A) | Dr. Aris Thorne is accountable for the security monitoring of the AI model lifecycle. Co-owns the "AI Model & Data Poisoning" correlation rules with the CISO. |
| **Internal Audit** | Informed (I) | Receives all monthly KPI/KRI reports and the list of all approved exceptions. They perform a semi-annual audit of logging effectiveness against SOC 2 criteria. |

---

## 4. Policy Statements

Meridian Health Technologies is committed to maintaining a state of continuous security monitoring to protect its information assets and fulfill its trust obligations to customers, patients, and partners. The following high-level policy statements are binding and enforceable.

**POL-ISEC-012-001: Universal Log Generation**
All information systems, applications, network devices, and security tools operating within the Meridian scope must generate comprehensive security-relevant audit logs. Log events must, at a minimum, capture user identity (where applicable), timestamp synchronized to the corporate NTP pool (`ntp.meridian.local`), source IP address, the event or object of the action, the action performed (success/failure), and the outcome status. Logging must be enabled by default in all infrastructure-as-code blueprints, and developers must instrument all new applications to emit structured JSON logs as a part of the Definition of Done.

**POL-ISEC-012-002: Centralized Collection and Tamper-Proofing**
All security logs must be forwarded to the centralized Security Information and Event Management (SIEM) system, currently Splunk Cloud, via encrypted channels (TLS 1.3). Logs in transit from source to SIEM must be hashed (SHA-256) to detect manipulation. Upon ingestion into the SIEM, logs must be stored in immutable, append-only indexes to prevent tampering by internal or external threat actors. Direct access to log source hosts to modify or delete logs is a violation of this policy, and any such attempt, even by privileged users, must trigger a high-severity alert.

**POL-ISEC-012-003: Proactive Threat Detection**
The SecOps team must not rely solely on manual log review. They shall maintain a library of automated, behaviorally-driven correlation rules within the SIEM. This library must be continuously updated based on the latest threat intelligence (MITRE ATT&CK framework alignment), lessons learned from Meridian-specific incidents, and outputs from red-team exercises. The goal is to detect and alert on known threats, anomalous user behavior (UEBA), and deviations from established operational baselines.

**POL-ISEC-012-004: HIPAA Audit Controls**
In compliance with HIPAA Security Rule § 164.312(b), Meridian implements hardware, software, and procedural mechanisms that record and examine activity in information systems that contain or use electronic Protected Health Information (ePHI). Access to ePHI is controlled, and all access events (read, write, modify, delete, export) are captured by the audit log. System administrators and specific named roles with elevated privileges are subject to enhanced monitoring, including keystroke-level recording for high-risk activities in production ePHI environments. For breach notification purposes, the log data serves as the primary forensic evidence. The Security Operations team will utilize logs during incident analysis to determine the scope of a breach, including the specific individuals and records affected.

**POL-ISEC-012-005: Data Retention and Disposal**
Meridian adheres to a risk-based data retention schedule. Hot storage (readily searchable, Splunk indexes) must be retained for 90 days for immediate, high-performance investigation. Warm storage (searchable at a lower performance tier, S3/Snowflake) must be retained for a minimum of 1 year. Cold storage (archival, offline S3 Glacier Deep Archive) must be retained for 7 years to satisfy financial (SR 11-7) and healthcare regulatory statutes of limitations. A secure, documented chain of custody process must be used for the forensic collection of logs from all tiers. Upon the expiration of the 7-year archival period, logs must be cryptographically shredded and securely disposed of in accordance with Meridian's Data Classification and Handling Policy (SOP-ISEC-003).

---

## 5. Detailed Procedures

This section outlines the operational procedures that translate the policy statements into actionable, repeatable workflows. These procedures are the primary responsibility of the SecOps and IT Infrastructure teams.

### 5.1 Log Source Identification and Onboarding

The first step to effective monitoring is ensuring pervasive visibility. A formal onboarding process is required for all new applications, infrastructure, and services.

**Procedure:**
1.  **Requirement Trigger:** The IT Infrastructure, Application Engineering, or DevOps team identifies a new system, application, or service being deployed. The project's Security Architect (or an appointed representative) initiates a "Log Source Onboarding" ticket in Jira Service Management (Project: "ISEC-LOG").
2.  **Standard Definition:** The project team, in consultation with a SecOps Engineer, documents the standard log source definition. This definition includes:
    - **Log Source Name:** (e.g., `[prod]-[us-east-1]-[medinsight-api-v3]`)
    - **Asset Type and Criticality:** Classified as High (ePHI/PCI/HCM), Medium (PII, non-public financial), or Low (internal docs, dev/test). This drives the SLA for alerting.
    - **Technology Stack:** The specific software and version emitting the logs (e.g., `nginx Plus R29`, `RHEL 9.2 kernel 5.14.0-284`).
    - **Log Format and Protocol:** The standardized format, ideally RFC 5424-compliant syslog or structured JSON over TLS 1.3 TCP. The default syslog facility is `local0` for applications and `authpriv` for access control events.
    - **Event Schema:** A complete, machine-readable (JSON Schema) definition of every event type the source will emit, its fields, and its severity level (`DEBUG`, `INFO`, `WARN`, `ERROR`, `CRITICAL`).
3.  **Technical Configuration and Validation:**
    - **Agent Management (Fluent Bit):** For Kubernetes environments, the DevOps pipeline automatically injects a Fluent Bit sidecar container configured with a Meridian-standard ConfigMap. For non-containerized hosts, Ansible playbooks deploy the Meridian-built `mdn-log-forwarder` agent.
    - **Pre-Production Validation:** The project team provisions a "logging-test" endpoint in their staging environment. The SecOps team uses this endpoint to validate the event schema, parsing logic (regex/GROK patterns), and end-to-end delivery before the production deployment. No application is approved to go live without passing this validation gate.
4.  **Production Onboarding and SOAR Integration:** Once validated in staging, the source is promoted to production. The SecOps Lead Engineer performs the final cutover, including:
    - Enabling the Splunk HTTP Event Collector (HEC) token.
    - Deploying the relevant correlation rules and analytic stories from the Dev-SIEM to Prod-SIEM.
    - Creating the SOAR (Splunk Phantom) playbook entry to automatically enrich and triage alerts from the new source.
5.  **Decommissioning:** When a system is decommissioned, its VRT must be removed. The responsible IT team follows the SOP-ISEC-006 (Asset Management) decommissioning process, which triggers the SecOps team to archive existing logs, remove the HEC token, and disable any source-specific correlation rules.

### 5.2 SIEM Correlation Rule Engineering and Lifecycle

Static rules are ineffective. Meridian employs a threat-informed, iterative lifecycle for detection engineering.

**Procedure:**
1.  **Use Case Identification:** New detection use cases are identified from several sources: threat intelligence feeds (MITRE ATT&CK Navigator), findings from penetration tests and the quarterly Red Team exercises, analysis of closed ServiceNow security incidents ("lessons learned"), and proactive threat-hunting hypotheses.
2.  **Use Case Definition Document (UCDD):** The Senior Detection Engineer authors a UCDD in Confluence for each proposed use case. The UCDD defines:
    - **MITRE ATT&CK Tactic and Technique:** (e.g., TA0006: Credential Access, T1555.003: Credentials from Password Stores: Web Browser)
    - **Narrative Description:** A plain-language description of the attack pattern the rule is designed to detect.
    - **Log Source Requirements:** The specific log sources and fields required (e.g., `Okta` `event_type` and `target`, `Windows Event Log` `EventID 4663` for `lsass.exe`).
    - **Proposed Correlation Logic:** The initial Splunk Processing Language (SPL) query.
    - **Risk Scoring:** The proposed priority (P1-Critical to P5-Informational).
3.  **Rule Development and Stage 1 (Alpha) Deployment:**
    - The Detection Engineer develops the rule as a Risk-based Alert (RBA) in Splunk.
    - The rule is deployed in a **"Log-Only"** state to the production SIEM. In this state, the alert fires, creates an event in the `detection_lab` index, but does NOT create a ticket or trigger a pager notification. This allows the team to tune the rule's signal-to-noise ratio over a 7-day observation period.
4.  **Stage 2 (Beta) and Performance Tuning:**
    - After analysis, the analyst reduces noise by adding exclusion logic, creating allow lists, or adding additional correlated context to reduce false positives. The goal is a true positive rate (TPR) of >85% for P1-P3 alerts.
    - The rule is graduated to a **"Beta"** state where it creates a low-priority, auto-assigned task for the Detection Engineering team for an additional 14 days.
5.  **Stage 3 (Production) and Alerting Onboarding:**
    - The UCDD is reviewed and approved by the SecOps Lead.
    - The rule is moved to a **"Production"** state. A corresponding SOAR playbook is created and linked. The on-call rotation is updated with the new alert schema. The rule's lifecycle is tracked in the "Correlation Rule Inventory" ServiceNow table.

### 5.3 Continuous Security Monitoring and Alert Triage

The Meridian Security Operations Center (SOC), staffed by the SecOps team, provides 24/7/365 monitoring. During business hours in primary geographies, Level 1 (L1) triage is handled internally. Meridian contracts with a managed SOC provider to act as an extension of L1 during overnight and non-business hours, with a strict SLA to escalate any potential P1 incident to the on-call Meridian Senior Security Analyst within 15 minutes.

**Procedure:**
1.  **Dashboard Monitoring (Proactive):** Each shift begins with a structured review of the primary operational dashboards:
    - **CISO Command Center:** High-level SLA compliance, count of open P1/P2 incidents.
    - **Real-Time Threat Map:** Geo-spatial view of IDS/IPS active alerts.
    - **Log Source Health & Data Gap Dashboard:** A heatmap showing log volume deviation from a calculated baseline. A sudden drop in logs from a P0 asset (e.g., HealthPay payment gateway) is a P1 incident in itself.
    - **EDR Command Center (CrowdStrike Falcon):** Top detections by host and global policy violations.
2.  **Alert Triage (Reactive):**
    - **L1 Analyst (Triage):** An alert is generated. The L1 analyst has **15 minutes** to acknowledge the alert in the SIEM. They then begin the SOAR playbook, which executes automated enrichment tasks: geolocation of IP addresses, WHOIS lookups, internal CMDB lookup for the host, and a VirusTotal scan for file hashes.
    - **L1 Analyst (Analysis):** Within the first **30 minutes**, the analyst must make a disposition:
        - **False Positive:** Clear noise. The analyst documents the reason, adds a tuning recommendation, and closes the alert.
        - **Authorized Activity:** A legitimate but poorly-documented change. The analyst contacts the relevant team for a change ticket reference. If no ticket exists, the finding is escalated as a Security Incident (P3).
        - **Security Incident:** The finding is deemed a confirmed or highly-likely security incident. The analyst escalates to a Senior Security Analyst (L2) and initiates the Incident Response Plan (IRP, SOP-ISEC-004) by declaring an incident in ServiceNow.
3.  **Escalation and War Room:** An L2 Analyst takes ownership of the VRT within **15 minutes** of escalation. For P1 (Critical) and P2 (High) incidents, the CSIRT is paged immediately. A designated Incident Commander (rotating responsibility) establishes a "War Room" (persistent video conference bridge), declares a command-and-control cadence, and the team begins formal containment and forensic analysis procedures.

### 5.4 Threat Hunting

Meridian adopts a continuous, intelligence-driven threat hunting model. This is not a reaction to an alert but a proactive search for the unknown attackers that bypassed our automated controls.

**Procedure:**
1.  **Hunt Hypothesis Generation:** Twice a month, the lead Threat Hunter and Detection Engineering lead co-author a "Hunt Hypothesis" document. Hypotheses are built on three pillars:
    - **Intelligence-Driven:** A specific, high-profile Advanced Persistent Threat (APT) Tactics, Techniques, and Procedures (TTPs) targeting the Healthcare or FinTech sector. (e.g., "APT41 has been observed using a novel malware dropper in the US healthcare sector that exploits the `Atlassian Confluence CVE-2024-XXXXX`. We hypothesize we were targeted with this CVE in the 30 days around its disclosure.")
    - **Baseline-Driven:** Anomalies identified by the AIOps anomaly detection engine. (e.g., "The engine detected a 400% increase in outbound DNS TXT queries from the `med-corp` subnet to a newly registered domain. We hypothesize this is a command-and-control beacon.")
    - **Asset-Focused:** A deep dive into the logs of a single "crown jewel" asset. (e.g., "We hypothesize we can find evidence of lateral movement from the Dev to Prod HealthPay Kubernetes cluster by analyzing the full mesh of 6 months of VPC Flow Logs.")
2.  **Hunt Execution:** The Threat Hunter uses the SIEM's big data lake to execute complex, unfiltered SPL queries over weeks of data, looking for patterns that match the hypothesis. This involves pivoting across disparate datasets: DNS queries, network flows, endpoint process trees, and authentication events.
3.  **Hunt Closure and Feedback Loop:** A hunt is formally closed in two ways:
    - **Finding of "No Contact":** A detailed report documents the exhaustive search, the data analyzed, and the conclusion that the TTP was not observed. This creates a valuable "negative evidence" baseline.
    - **Confirmed Finding:** A new malicious pattern is found. The Hunter immediately initiates an incident (P1/P2) and takes direct command as the initial Incident Commander. Concurrently, they develop a new UCDD to automate detection for future occurrences, feeding the Rule Engineering Lifecycle (Section 5.2).

### 5.5 AI-Specific Model Monitoring

The Clinical AI Platform introduces unique monitoring requirements that extend beyond standard infrastructure, in alignment with the NIST AI RMF. Data integrity and model behavior are critical indicators of security compromise.

**Procedure:**
1.  **Data Poisoning Detection:** AI/ML Pipelines must emit high-fidelity logs on the statistical distribution of incoming training data features. A dedicated monitoring rule in Splunk, co-owned by the Chief AI Officer (Dr. Aris Thorne) and the CISO, triggers a P2 security incident if the distribution of any critical feature deviates from its validated, historical baseline by more than three standard deviations. This rule, codified as `AI-RUL-004`, is specifically designed as the detection logic for a Model Poisoning attack.
2.  **Model Evasion and Adversarial Inputs:** All Clinical AI model inference APIs (both internal and customer-facing) must log every input/output pair, stripped of ePHI for privacy, to a dedicated `clinical_ai_audit` index. The AI-SecOps team runs a weekly behavioral analytics job (AIOps) to detect adversarial inputs. A statistically significant cluster of inputs designed to cause an abnormal model response will trigger an automated P3 creation and a rollback of the model to the last known-good version.
3.  **Model Exfiltration:** Network proxy and gateway logs are correlated with CI/CD pipeline events. A custom SOAR playbook (`playbook_ai_model_exfil`) is triggered by the conjunction of two events: a large egress data transfer (over 100MB) from a production inference pod, and a file read event on an encrypted model container file (.h5/.pb/.pt) originating from the same pod. This triggers an immediate P1 incident.

### 5.6 Secure Log Retention and Disposal

**Procedure:**
1.  **Lifecycle Management (ILM):** Logs in Splunk follow a defined Index Lifecycle Management (ILM) policy. After 90 days, data is automatically transitioned from hot, high-performance NVMe storage to warm, capacity-optimized HDD-backed storage. After 1 year, data is automatically rolled from Splunk to the Meridian Security Data Lake (AWS S3 Deep Archive, governed by `glacier-vault-lock-policy.json` which enforces a 7-year "write once, read many" WORM lock).
2.  **Legal Hold:** Any non-expired data subject to a legal hold request from Meridian's General Counsel is immediately taken out of the standard ILM process and preserved. A tag is applied to the relevant indexes in Splunk, preventing any policy-based deletion.
3.  **Custodial Retrieval:** Retrieving data from cold storage is restricted. A request must be submitted via Jira to the SecOps Data Custodian. The request must detail the legal or business reason, the scope of the data, and justification for urgency. Retrieval is a break-glass, audited operation.
4.  **Cryptographic Disposal:** 7 years after the initial ingestion timestamp, the WORM lock on the cold storage objects expires. An automated AWS Lambda function (`mdn-secure-shred`), triggered by S3 object expiration events, invokes AWS Key Management Service (KMS) to securely destroy the unique per-bucket customer managed key (CMK) that was used for envelope encryption. Without the key, the immutable objects are rendered cryptographically inaccessible, completing the disposal process.

---

## 6. Controls and Safeguards

This section enumerates the specific technical, administrative, and physical controls that operationalize the policy statements and procedures defined above. These controls are mapped directly to the SOC 2 Trust Services Criteria (TSC) and the HIPAA Security Rule.

### 6.1 SOC 2 Trust Services Criteria (TSC) Controls

Meridian’s security logging and monitoring program directly supports the achievement of the Security, Availability, and Confidentiality criteria defined in Trust Services Criteria for Security (AICPA, TSP Section 100, 2017 TSC, including revised CC2.2 and PI1.5 as of SOC 2® Type II examination, 2025 cycle).

| Control ID | Control Description | SOC 2 Ref. | Measurement Metric | Target | Verification Frequency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SOC2-LM-001** | Newly provisioned production assets are automatically enrolled in the SIEM via the CI/CD pipeline, a Fluent Bit sidecar, or an Ansible playbook. | **CC6.1, CC6.8, A1.2** | Percentage of operational production assets actively generating and forwarding logs to the central SIEM as verified by a daily CMDB-to-SIEM reconciliation script. | 100% | Daily (Automated script), Monthly (Manual SecOps review) |
| **SOC2-LM-002** | The SIEM (Splunk) performs automated behavioral analytics to detect anomalous user activities that may constitute a security threat. Access to ePHI generates a high-severity audit event. | **CC7.3, PI1.4** | Mean Time to Detect (MTTD) for all validated internal security incidents, measured from the timestamp of the first malicious activity in the logs to the moment the CSIRT Incident Commander declares the incident. | MTTD < 1 hour | Monthly (CISO & SecOps Lead) |
| **SOC2-LM-003** | A continuous monitoring (CM) process is in place, where a dedicated team (SecOps) actively reviews dashboards and a SIEM console for security-relevant events. | **CC7.2, A1.2** | Time an automated High (P2) or Critical (P1) alert remains unacknowledged in the SIEM user interface by a Tier-1 analyst. | Acknowledged within 15 minutes, 24/7/365 | Weekly, reported in the CISO's monthly KRI report |
| **SOC2-LM-004** | The security incident response process is activated by SIEM/SOAR alerting. The effectiveness of this hand-off is regularly measured. | **CC7.4, PI1.4, A1.3** | Mean Time to Contain (MTTC) for P1 and P2 incidents. This is measured from the time of the CSIRT war room declaration to the point where the Incident Commander confirms that lateral movement is halted. | MTTC < 4 hours | Per-incident review, trended quarterly |
| **SOC2-LM-005** | Log data is retained in an immutable and encrypted state for a defined period to support investigation and reporting. | **CC6.1, PI1.5** | A quarterly test performed by IT where a designated SecOps Data Custodian attempts to delete an encrypted log object from the cold storage WORM bucket. The action must fail with a `AccessDenied` error. | 100% of test attempts fail | Annually (Internal Audit) / Quarterly (SecOps Test) |
| **SOC2-LM-006** | A formal vulnerability assessment and penetration test (VAPT) is conducted annually to test detective controls. This includes a "blind" test where the QSA introduces controlled malicious behavior to validate the SOC's ability to detect and respond. | **CC7.1, A1.2** | MTTD for all 5 "blind" adversary simulation exercises conducted by the external QSA during the annual SOC 2 audit window. | MTTD < 1 hour for all 5 exercises | Annually (External Audit) |
| **SOC2-LM-007** | A formal, risk-based process is used to assess, approve, and track exceptions to the requirements of this SOP. | **CC5.1, CC9.2** | Number of active, unresolved exceptions older than 90 days. | 0 | Monthly (CISO & Compliance Officer) |

### 6.2 HIPAA Security Rule Safeguards

The covered functions within the Meridian SaaS Platform, Clinical AI Platform, and MedInsight Analytics environments implement the following safeguards to comply with the Technical Safeguards of the HIPAA Security Rule (45 CFR § 164.312).

**Audit Controls (§ 164.312(b))**
Meridian implements hardware, software, and procedural mechanisms to record and examine activity in information systems that contain or use ePHI.
- **Administrative Safeguard:** The CISO and Chief Privacy Officer annually review a defined scope of access, which is formally approved by system owners. This review examines records of access attempts to ePHI data stores (both successful and denied) and changes to elevated privilege group memberships.
- **Technical Safeguard:** All access to database tables, file shares, and application objects tagged with the `data_classification: PHI` label is captured at the application layer and routed to the dedicated, access-restricted `hipaa_audit` index in Splunk. Access to this index is granted only via a highly restricted role that is subject to quarterly access reviews.
- **Procedural Weakness:** While all access to systems containing ePHI is logged and reviewed, the **Minimum Necessary** standard (§ 164.514(d)) is not fully operationalized by the logging system. A SIEM correlation rule exists to flag "excessive" downloads (e.g., >50 records from the MedInsight UI) for a given role, but there is no automated, per-transaction enforcement mechanism that intercepts a broader-than-necessary query before it executes.

**Person or Entity Authentication (§ 164.312(d))**
All ePHI access requires unique user identification. Meridian's SSO (Okta) and Multi-Factor Authentication (MFA) system provides this safeguard. All authentication events (successes, failures, MFA challenges, and SSO token grants) are forwarded to the SIEM.

**Transmission Security (§ 164.312(e)(1))**
Meridian protects against unauthorized access to ePHI being transmitted over an electronic communications network. Log forwarding from ePHI systems is performed exclusively over mutually authenticated TLS 1.3 channels.

**Integrity Controls (§ 164.312(c)(1))**
Implementing electronic mechanisms to corroborate that ePHI has not been altered or destroyed in an unauthorized manner.
- **Control:** File Integrity Monitoring (FIM) agents are deployed on all Windows and Linux servers within the ePHI enclave (the `ephil` VPC) to monitor critical system files, application configuration, and cryptographic key stores. Events are correlated in the SIEM.

**Breach Notification (§ 164.404)**
- **Procedural Control:** In the event of a confirmed breach, the CSIRT Incident Commander will generate a forensic report from the SIEM audit logs, detailing the specific records, the scope of the compromise, and the individuals involved. The Compliance and Privacy Officer uses this forensic output as the primary input to the breach notification process.
- **Procedural Detail:** The notification procedure requires identification of the affected individuals and the nature of the breach. Upon validation of a Breach of Unsecured PHI, the Privacy Officer will coordinate notification to affected individuals, the Secretary of HHS, and, where applicable, the media, in accordance with established IRP timelines. The investigation leverages the immutable forensic logs to ascertain the exact scope of the breach.

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness of this SOP is continuously measured. A multi-tiered reporting structure ensures that actionable KPIs reach operators, while risk-driven KRIs inform senior leadership.

### 7.1 Operational Dashboards (Real-time)

These dashboards are displayed on large-format monitors in the SOC and are accessible to on-call personnel.

| Dashboard Name | Primary Audience | Key Metrics Displayed |
| :--- | :--- | :--- |
| **SOC Alert Queue Health** | L1/L2 Analysts | Unacknowledged Alert Count (by Severity), Average Time to Acknowledge (last 1 hr), Top 5 Active Alert Signatures, On-Duty Analyst Name. |
| **Log Source Health Matrix** | IT Infrastructure & DevOps, SecOps | A live heatmap where each cell represents a `Log Source Group -> [Region, Function]`. Green = volume within 2 std deviations of baseline. Red = silent. Drill-down to see the last event timestamp from a specific source. |
| **CSIRT War Room Status** | CISO, Incident Commander | For all open P1/P2 incidents: Incident ID, Current MTTC clock (starts ticking at declaration), Commander, current containment status phase. |

### 7.2 Monthly KPI/KRI Reporting

The CISO generates a formal "Security Monitoring Effectiveness Report" by the 5th business day of each month. This report is distributed to all A and C in the RACI matrix, the Technology Risk Committee, and Internal Audit.

**Key Performance Indicators (KPIs)**
*Metrics showing operational performance.*

| KPI | Calculation | Current Quarter Target |
| :--- | :--- | :--- |
| **Log Source Coverage** | `(Hosts actively logging via SIEM / Total CMDB prod hosts) * 100` | 100% (Green: >=99.9%) |
| **Mean Time to Acknowledge (MTTA)** | `(Σ Time to Acknowledge all P2/P3 alerts) / Total Alerts` | < 15 minutes |
| **False Positive Rate (FPR) - P1/P2** | `(False Positive P1/P2 alerts / Total P1/P2 alerts) * 100` | < 5% |
| **Mean Time to Contain (MTTC) - P1** | `(Σ Time from War Room declaration to lateral movement stop) / Total P1 Incidents` | < 2 hours |

**Key Risk Indicators (KRIs)**
*Metrics with a direct correlation to risk. Thresholds set by the CISO and Board Risk Committee.*

| KRI | Calculation | Risk Thresholds (Red) |
| :--- | :--- | :--- |
| **Mean Time to Detect (MTTD)** | `(Σ(Time 1st Malicious Action -> Incident Declaration)) / Total Incidents` | > 4 hours |
| **Critical Data Store Audit Failures** | A count of failed file-integrity checks on PHI/PCI data stores. | Any single failure |
| **Overdue Exception Count** | Number of active, approved exceptions to this SOP without a completed, approved 90-day review. | > 0 |
| **Unpatched Critical Vulnerability (Logging)** | Presence of an unpatched, Critical-severity CVE on a logging or monitoring server (SIEM, Syslog, Fleet Manager). | > 0 for > 72 hours |

### 7.3 Annual Board-Level Reporting

Annually, the CISO presents a strategic summary to the Meridian Board of Directors Audit Committee. This report contextualizes the KRI trends, details the ROI of the monitoring program using ALE calculations (e.g., reduction in probable cost of a major breach due to decreased MTTD/MTTR), and outlines the strategic roadmap for the next fiscal year's tooling and staffing investments.

---

## 8. Exception Handling and Escalation

This section defines the process for requesting, approving, and managing deviations from the requirements of this SOP. This process is itself a critical compliance control.

### 8.1 Exception Request Procedure

1.  **Initiation:** Any Meridian personnel can initiate an exception. The requestor submits a "Security Policy Exception Request" form (available in ServiceNow, via the "ISEC-EXCEPTION" portal). The form requires:
    - The specific Policy Statement ID (e.g., `POL-ISEC-012-002`) or Procedure (e.g., `5.1, Step 3`) from which the exception is requested.
    - A detailed technical and business justification. A statement such as "vendor doesn't support it" is insufficient; the justification must explain *why* the control cannot be implemented, the technical barriers, and the specific business impact of not implementing the solution.
    - A clear description of the proposed compensating control(s) that will be implemented to reduce the risk to an acceptable level. A compensating control must have a measurable effect.
    - A proposed duration for the exception, not to exceed 90 days for the initial request.
    - The formal risk acceptance by the business unit owner (e.g., CAIO for Clinical AI, CTO for IT Infrastructure). This acknowledges they accept the residual risk to their business function.
2.  **Technical Review:** The SecOps Lead Engineer reviews the request for technical accuracy and evaluates the effectiveness of the proposed compensating controls. They provide a written "risk opinion" detailing whether the compensating controls actually reduce the risk and what new monitoring they may require.
3.  **Approval Authority:** The exception request, with its business justification, risk acceptance, and technical risk opinion, is routed for final approval.
    - **Duration < 90 days, Criticality Medium/Low:** Approved by the CISO.
    - **Duration > 90 days (up to 1 year max) OR Criticality High (ePHI/PCI assets):** Must be approved by both the CISO and the Chief Risk Officer (CRO).

### 8.2 Exception Lifecycle Management

- **Registration:** All approved exceptions are registered in the ServiceNow "Policy Exception" module with a start date, expiration date, and a mandatory review task.
- **Remediation Tracking:** The exception approval triggers a Jira task assigned to the requestor, with the expiration date as the hard deadline. The task tracks the engineering work to close the gap.
- **Expiration:** 7 days before expiration, both the requestor and approver receive an automated notification. If the Jira task is not complete by the expiration date, the CISO is automatically notified. The CISO may, at their discretion, grant a single 30-day extension only if remediation is blocked by a vendor and an active support case number is provided. No other extensions are permitted.
- **Revocation:** If an exception expires without renewal, the responsible system is immediately classified as "Non-Compliant." The SecOps team adjusts monitoring (e.g., changing the alert from P3 to P1 for that specific asset) and the Internal Audit team is notified to open a formal audit finding.

---

## 9. Training Requirements

The effectiveness of technical controls depends on proficient operators. Meridian mandates a tiered training program.

### 9.1 General User Awareness Training

- **Content:** All personnel, upon hire and annually thereafter, must complete the "Security Awareness and You" module in Litmos. This training covers how to identify and report a phishing email, a suspicious USB device, or a tailgater in a secure area. It explicitly instructs users to report any "odd computer behavior" to the Service Desk immediately.
- **Tracking:** Completion is tracked in Workday. Non-completion by the annual deadline triggers automated HR disciplinary procedures.

### 9.2 SecOps Specialized Role-Based Training

All members of the Information Security team, and the extended CSIRT, must maintain advanced proficiency.
- **SIEM/SOAR Proficiency (L1 and L2 Analysts):** Must achieve and maintain the "Splunk Core Certified Power User" certification. Meridian will fund two exam attempts per analyst. This ensures deep comfort with the SPL language for triage and hunting.
- **Live-Fire Exercise (All CSIRT members):** Annually, the entire CSIRT participates in a one-day, immersive "Capture the Flag" (CTF) style exercise. The exercise, designed by the Detection Engineering Lead, uses the Meridian Cyber Range and replays two major incidents from the previous year, mixed with novel TTPs. This tests the IRP under stress and builds team cohesion. Participation is mandatory for all CSIRT members.
- **Cloud Detection (DevOps & Infrastructure):** Senior engineers responsible for Kubernetes and AWS must attend the "Cloud Native Security & Threat Detection" (SANS SEC541 or equivalent) training. This is a bi-annual requirement, to keep pace with the attack surface evolution.

### 9.3 Developer Secure Coding Training

All developers, as part of their annual secure coding training (SOP-ISEC-008), must complete a module specifically on "Security Logging Failures" (aligned with OWASP Top 10 A09:2021). The module covers Meridian's standard logging library, the required fields for an audit event, and examples of good versus bad logging practice. All new application code promoting to production must pass a SAST check that includes a rule for the `meridian-security-logging-standard`.

---

## 10. Related Policies and References

This SOP does not stand alone. It integrates with the broader Meridian Governance, Risk, and Compliance (GRC) framework.

### 10.1 Internal Meridian Policies

| SOP-ID | Policy Name | Relationship to this SOP |
| :--- | :--- | :--- |
| **SOP-ISEC-001** | Information Security Policy | The foundational policy. SOP-ISEC-012 is a direct sub-procedure, operationalizing the Logging & Monitoring section. |
| **SOP-ISEC-003** | Data Classification and Handling Policy | Defines the classification (`PHI`, `PCI`, `Internal`) that drives log criticality, access controls, and retention schedules. |
| **SOP-ISEC-004** | Incident Response Plan (IRP) | The "downstream" process. Sections 5.3 and 5.4 of this SOP define the hand-off criteria from detection to formal IR. |
| **SOP-ISEC-006** | Asset Management Policy | The CMDB, which is the source of truth for the 100% Log Source Coverage KPI, is governed by this policy. |
| **SOP-ISEC-008** | Secure Software Development Lifecycle (SDLC) | Defines the SAST/DAST requirements that validate logging standards in CI/CD pipelines. |
| **SOP-ISEC-011** | User Access Lifecycle Management | Governs the accounts and access that generate the log data. The UEBA process in this SOP relies on an accurate list of accounts and their expected behaviors. |
| **SOP-CLIN-003** | Clinical AI Model Lifecycle Management | This defines the model registration, versioning, and decommissioning triggers that Section 5.5 procedures monitor for security-relevant state change. |

### 10.2 External Standards and Regulatory References

- **Trust Services Criteria for Security (SOC 2):** As defined by the AICPA, 2017 TSC (with 2023 revisions). Specifically criteria **CC6.1, CC6.8, CC7.1-CC7.4, CC9.2, A1.2, A1.3, and PI1.4-PI1.5**.
- **HIPAA Security Rule:** 45 CFR Part 164, Subparts A and C (Security Standards for the Protection of Electronic Protected Health Information), specifically § 164.312(b) (Audit Controls), § 164.308(a)(5) (Security Awareness and Training), and § 164.404 (Breach Notification).
- **NIST AI RMF 1.0:** Governs the AI-specific monitoring procedures detailed in section 5.5.
- **Reserve Requirements for Depository Institutions (Regulation D, 12 CFR 204):** The 7-year archival requirement for cold storage aligns with federal financial recordkeeping obligations.
- **MITRE ATT&CK for Enterprise, v15:** The taxonomy used for all threat detection logic and correlation rule mapping in section 5.2.

---

## 11. Revision History

The following table captures the revision lifecycle of this document. Each new version renders the previous version obsolete, which must be archived in the official document management system.

| Version | Revision Date | Effective Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 2019-02-01 | 2020-03-15 | P. Chen (CISO) | Initial document creation. Established central logging for corporate infrastructure only. No cloud/SIEM coverage. |
| 2.0 | 2021-06-01 | 2021-07-01 | M. Dubois (Dir. SecOps) | Major rewrite. Rolled out Splunk Cloud. Created log onboarding procedure. Added SOAR (Phantom) integration. Scope expanded to HealthPay and initial Clinical AI. |
| 3.0 | 2022-10-10 | 2022-11-01 | A. Vance (Sr. SecOps Eng) | Complete rewrite to a threat-informed model. Introduced the UCDD lifecycle. Added Sections 5.4 (Threat Hunting) and 5.5 (AI-Specific Monitoring). Aligned rules to MITRE ATT&CK v10. |
| 3.1 | 2023-04-01 | 2023-05-01 | J. Okonkwo (GRC Analyst) | Minor revision. Formalized SOC 2 TSC mapping table in Section 6.1 after external audit finding. Added KRI metric for overdue exceptions to Section 7.2. |
| 3.2 | 2023-11-18 | 2023-12-01 | R. Kim (CISO) & A. Vance | Post-2023 Penetration Test revision. Added "Blind" adversary simulation control (SOC2-LM-006). Updated retention to include 7-year cold storage. |
| 3.3 | 2024-02-16 | 2024-02-16 | R. Kim (CISO) | Annual review. Updated references to new SOP-CLIN-003. Clarified breach notification procedure in Section 6.2. Minor updates to RACI for CAIO role. |