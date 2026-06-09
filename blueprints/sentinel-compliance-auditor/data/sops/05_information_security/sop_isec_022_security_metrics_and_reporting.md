---
sop_id: "SOP-ISEC-022"
title: "Security Metrics and Reporting"
business_unit: "Information Security"
version: "4.6"
effective_date: "2025-04-26"
last_reviewed: "2026-12-20"
next_review: "2027-06-25"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Security Metrics and Reporting

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for the systematic definition, collection, analysis, reporting, and governance of security metrics across Meridian Health Technologies, Inc. ("Meridian" or the "Company"). The primary purpose is to provide a data-driven mechanism for measuring the effectiveness of the information security program, enabling informed risk management decisions, demonstrating control effectiveness to external auditors and regulators, and facilitating continuous improvement.

Specifically, this SOP aims to:
- Define the cadence, format, and audience for formal security reporting.
- Establish clear ownership and data lineage for all security metrics.
- Standardize Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs) in alignment with the SOC 2 Trust Services Criteria and the NIST AI RMF.
- Ensure timely escalation of metric deviations through predefined thresholds.
- Provide a single source of truth for security posture through centralized dashboards.

### 1.2 Scope

This SOP applies to all Meridian business units, technology platforms, and third-party integrations that generate, store, or process data relevant to the Company's security posture.

**In-Scope Systems and Operations:**
- **Meridian SaaS Platform:** Including AWS (us-east-1, eu-west-1) and Azure DR environments.
- **Clinical AI Platform:** All model training pipelines (Kubeflow, SageMaker), inference endpoints, and clinical data stores (Snowflake, Pinecone).
- **HealthPay Financial Services:** Payment processing infrastructure, credit scoring models subject to SR 11-7, and patient financing portals.
- **MedInsight Analytics:** Population health data stores containing Protected Health Information (PHI) for ~12M patients.
- **Corporate IT:** Endpoints, identity systems (Okta), and collaboration tools for ~2,400 employees across global offices.

**Out of Scope:**
- Financial reporting metrics not directly related to information security (managed under SOP-FIN-045).
- Clinical efficacy metrics for AI models (managed under SOP-CLIN-012).
- Customer satisfaction surveys (managed by Customer Operations).

**Target Audience:**
This SOP is binding upon the Information Security team, IT Operations, Engineering leads, Compliance, the AI Governance Committee, and any role specifically named in Section 3.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **ALM** | Alert Lifecycle Management. The process from security alert generation to closure. |
| **APT** | Advanced Persistent Threat. A sophisticated, sustained cyber threat actor. |
| **AWS KMS** | Amazon Web Services Key Management Service. Used for encryption key management. |
| **CCM** | Cloud Controls Matrix. A cybersecurity controls framework aligned to SOC 2. |
| **CISO** | Chief Information Security Officer. The Owner of this SOP (Rachel Kim). |
| **CSF** | Cybersecurity Framework. Refers specifically to the NIST CSF mapping within Meridian’s risk register. |
| **CSPM** | Cloud Security Posture Management. Automated scanning of cloud misconfigurations (Tool: Wiz). |
| **D&R** | Detection and Response. The operational function of the Meridian SOC. |
| **EDR** | Endpoint Detection and Response (Tool: CrowdStrike Falcon). |
| **KPI** | Key Performance Indicator. A lagging metric measuring the execution of security controls (e.g., % of servers with compliant agents). |
| **KRI** | Key Risk Indicator. A leading or predictive metric indicating elevated risk exposure (e.g., a spike in exposed attack surface). |
| **MTTD** | Mean Time to Detect. The average time between the start of a security incident and its identification. Target: < 5 minutes for critical alerts. |
| **MTTR** | Mean Time to Respond/Remediate. The average time between detection and containment/remediation. Target: < 30 minutes for P1 incidents. |
| **PCI DSS** | Payment Card Industry Data Security Standard. Applies to HealthPay systems. |
| **PHI** | Protected Health Information. Defined under HIPAA, applicable to MedInsight and Clinical AI data. |
| **P1/P2/P3** | Priority 1 (Critical), Priority 2 (High), Priority 3 (Medium) incident severity levels. |
| **RACI** | Responsible, Accountable, Consulted, Informed. A responsibility assignment matrix. |
| **SIEM** | Security Information and Event Management (Tool: Splunk Enterprise Security). |
| **SOC** | Security Operations Center. The internal team responsible for detection and response, or the System and Organization Controls (SOC 2) Trust Services Criteria. |
| **SOP** | Standard Operating Procedure. |
| **SVM** | Software Vulnerability Management. Distinct from cloud misconfigurations. |
| **TSC** | Trust Services Criteria. The specific criteria under SOC 2 (Security, Availability, Confidentiality). |
| **Wiz** | Cloud Security Posture Management (CSPM) tool used for vulnerability and configuration scanning. |
| **Zero Trust** | A security model based on strict identity verification (Meridian’s phased implementation). |

---

## 3. Roles and Responsibilities

The following RACI matrix governs the activities defined in this SOP.

| Role / Individual | Responsibility |
| :--- | :--- |
| **Rachel Kim, CISO** | **[A] Accountable.** Owns the overall security metrics strategy. Approves the selection of KPIs/KRIs, threshold changes, and final board reports. |
| **Security Operations Lead (Vacant, Interim: Rachel Kim)** | **[R] Responsible** for the execution of operational metrics collection (MTTD, MTTR, Phishing Simulation Rate). Manages detection and response dashboards. |
| **GRC Lead, Information Security (Maria Hernandez)** | **[R] Responsible** for the collection and governance of compliance metrics (Control Testing %, Audit Finding Remediation). Manages the risk register integration. |
| **VP of Engineering (Platform)** | **[R] Responsible** for the supply of data inputs related to infrastructure telemetry (Agent Coverage %, CSPM Scan Results). Responsible for remediation SLAs. |
| **AI Governance Committee (Lead: Dr. Anya Sharma)** | **[C] Consulted** on metrics related to AI security risks (Model Poisoning, Adversarial Drift). They receive specific KRI reports monthly. |
| **Internal Audit (David Chen)** | **[I] Informed** (Quarterly). Reviews metric definitions for auditability and validates evidence used in SOC 2 Type II reports. |
| **Board of Directors** | **[I] Informed** (Quarterly). Receives the consolidated "State of Security" dashboard and briefing. |

---

## 4. Policy Statements

Meridian Health Technologies is committed to a transparent, measurable, and objective-driven security program. The following policy statements guide the execution of this SOP:

- **Quantitative Governance:** The security posture shall be governed through quantitative metrics. Subjective or qualitative assessments alone are insufficient for board-level reporting or critical risk decisions.
- **SOC 2 Alignment:** All security KPIs and KRIs shall be explicitly mapped to the applicable SOC 2 TSC (Security, Availability, and Confidentiality) categories and criteria numbers, ensuring audit readiness.
- **Source of Truth:** The Splunk ES SIEM (augmented by Wiz CSPM data) shall serve as the centralized data lake and "single pane of glass" for all security metrics. No "shadow IT" spreadsheets shall be used for official KPI reporting.
- **Timeliness:** Metrics shall be collected in near real-time via automated APIs. Manual data collation is only permissible for metrics explicitly designated as "Manual/Quarterly" in Section 6.
- **No Tolerance for Stale Data:** Dashboards visible to Directors and above must reflect the state of the environment within the prior 24 hours. Stale dashboards shall be treated as an availability breach of the monitoring system.
- **Transparency:** Raw data, not just "green lights," must be accessible to Internal Audit upon request to support the SOC 2 Type II report attestation.

---

## 5. Detailed Procedures

This section outlines the end-to-end lifecycle of a security metric, from definition to operational consumption.

### 5.1 Annual KPI/KRI Refresh and Strategy Alignment

**Timing:** Fiscal Year (FY) end / Board Strategy Session (Typically November).
**Participants:** CISO, GRC Lead, D&R Lead, VP of Engineering, Internal Audit.

**Procedure:**
1.  **Strategic Alignment Review:** The CISO presents the business objectives for the upcoming FY. The team evaluates if the current metrics support these goals. Example: If a new Clinical AI product launch shifts the risk profile, new KRIs regarding data lineage and model drift must be added.
2.  **Metric Efficacy Review:** The team analyzes the previous year's trending data. Metrics that consistently report "100%" without driving action are either "over-controlled" (setting the bar too low) or ineffective and must be redefined.
3.  **Threshold Tuning:** Thresholds (Section 6.2) are reviewed against actual operational performance. The target for "Critical Alert MTTD" might be reduced from 5 minutes to 3 minutes based on new SOAR capabilities.
4.  **Offboarding Obsolete Metrics:** Metrics that no longer align with TSC or threats are formally retired. For example, if legacy on-premise servers are fully decommissioned, metrics related to them are removed from the dashboard.
5.  **Sign-off:** The updated "Metrics Catalog" (Form ISEC-022-A01) is reviewed and approved by the CISO.

### 5.2 Automated Data Collection and Aggregation

Daily operational data must flow into the centralized Splunk ES index without manual intervention.

**Step 1: Source Configuration (VP of Engineering)**
To ensure data validity, only the following sanctioned data sources are permitted to populate the Security Metrics Index (`idx_sec_metrics_v2`):
- **Splunk Universal Forwarder:** Deployed on 100% of production virtual machine instances (AMIs).
- **AWS Security Hub (SIEM Connector):** Aggregates GuardDuty, IAM Access Analyzer, and Inspector findings.
- **CrowdStrike Falcon Data Replicator (FDR):** Streams EDR telemetry (detections, agent status, vulnerabilities) via SQS to Splunk.
- **Wiz API:** Ingests CSPM misconfiguration data and vulnerability findings (including container/K8s scans).
- **Okta Log Stream:** Ingests authentication events, including MFA bypass attempts and anomalous travel detections.

**Step 2: Data Normalization (Security Data Engineering team)**
Raw logs must be normalized using the Meridian Common Information Model (`meridian_cim_v3`). Key fields standardized:
- `business_unit`: (e.g., HealthPay, Clinical_AI, Corp_IT)
- `asset_class`: (e.g., Server, Container, User_Endpoint)
- `control_family`: (e.g., Vulnerability_Management, Identity_Access)
- `compliance_map`: (e.g., SOC2-CC6.1, SOC2-CC7.2)
- `severity`: (Critical, High, Medium, Low)

**Step 3: Quality Assurance (InfoSec GRC)**
Daily, an automated Splunk job must run the "Data Integrity Check" report. This report verifies that every defined source in the Metrics Catalog has submitted an expected "heartbeat" event within the last 120 minutes. If a source is silent, a P3 alert is generated for the Data Engineering team.

### 5.3 KPI/KRI Calculation and Dashboarding

Metrics are calculated using Splunk’s Summary Indexing to optimize graph rendering on dashboards.

**Procedure:**
1.  **Scheduled Search Execution:** At `00:05 UTC` daily, a batch of Splunk Saved Searches calculates the previous day’s metrics (e.g., `Daily_MTTD_AVG`). These searches populate the summary index `meridian_summary_metrics`.
2.  **Threshold Comparison:** A secondary job immediately compares the calculated metric against the defined threshold in the Metrics Catalog. If a metric is out of tolerance (e.g., `agent_coverage` < 99.5%), the dashboard widget automatically changes from Green (Normal) to Amber (Warning) or Red (Breach).
3.  **Dashboard Hierarchy:**
    - **Executive (Board/CEO) Dashboard:** Consolidated "State of Security," weighted security scorecard, top 5 open risks, key audit deadlines. (Updated Quarterly).
    - **Operational (SOC) Dashboard:** Real-time MTTD, Incident Volumes, Remediation SLA tracking. (Instant Refresh).
    - **Compliance Dashboard:** Control testing status, vendor risk ratings, audit finding aging. (Updated Daily/Weekly).
    - **Vulnerability Management Dashboard:** Patch compliance, CSPM severity breakdown by business unit. (Updated Hourly).

### 5.4 Monthly Security Operations Review

**Occurrence:** Second Thursday of each month, 10:00 AM EST.
**Attendees:** CISO, Security Operations Lead, VP of Engineering, IT Operations Director.

**Agenda and Procedure:**
1.  **Alert Hygiene Review:** Analyze the last month's D&R data. Calculate `False Positive Rate` per detection rule. Any rule with > 20% False Positive Rate must be tuned or suspended, as it degrades analyst performance and MTTD.
2.  **SLA Performance:** Review MTTD and MTTR for the past month. Identify any P1 or P2 incidents that violated SLA. The Security Operations Lead presents a 1-slide "Root Cause Analysis" (RCA) summary for each SLA breach. The focus is *process failure*, not blaming individuals.
3.  **Vulnerability & Posture Review:** The VP of Engineering presents the CSPM dashboard. Focus is on *aging* High and Critical findings. Findings older than 30 days require a formal exception or a remediation acceleration plan.

---

## 6. Controls and Safeguards

This section defines the specific technical and administrative controls that ensure the integrity, confidentiality, and availability of the metrics pipeline itself. These controls are audited as part of the SOC 2 Security and Availability criteria.

### 6.1 Technical Controls

| Control ID | Control Description | SOC 2 TSC Mapping | Implementation Detail |
| :--- | :--- | :--- | :--- |
| **TC-022-01** | **Metrics Data Integrity Verification** | Availability (A1.2), Security (CC7.1) | Automated Splunk job (`Data Integrity Check`) runs every hour. It verifies cryptographic hashes (SHA-256) of all data ingested into the `idx_sec_metrics_v2` index against the source’s generated manifest. Failed checks generate a Critical (`P1`) incident. |
| **TC-022-02** | **Access Control to Dashboards** | Security (CC6.1, CC6.2) | Access to the Executive and Compliance dashboards is restricted via Okta SSO and an `sec_metrics_viewer` AD Group. Access reviews are conducted quarterly. Direct query access to the summary index (`meridian_summary_metrics`) is restricted to the Splunk Admin role via Role-Based Access Control (RBAC); read-only access is permitted for the `sec_analyst` role. |
| **TC-022-03** | **Encryption of Data in Transit and At Rest** | Security (CC6.1) | All data ingests from AWS (HealthPay, Clinical AI) to Splunk are via PrivateLink endpoints encrypted with TLS 1.2 minimum. Summary index data at rest is encrypted using AWS KMS CMKs (`splunk-summary-dashboard`) with automatic annual key rotation. |
| **TC-022-04** | **Anti-Tampering and Audit Logging** | Security (CC7.3, System Integrity) | Splunk audit logs track all changes to dashboards, metric definitions, and alert thresholds. Any modification to a "board-visible" dashboard triggers an automatic notification to the CISO and GRC Lead. This data feeds the `user_control_modifications` metric. |

### 6.2 Metric Thresholds and Business Rules

The following precise thresholds must be configured in Splunk ITSI or the glass-table executive module. Amber status prompts an email to the metric owner; Red status generates an incident ticket and pager alert for the responsible engineering manager.

| Metric | Owner | Amber Threshold | Red Threshold | SOC 2 Link |
| :--- | :--- | :--- | :--- | :--- |
| EDR Agent Coverage (Clinical AI) | VP, Platform AI & Data | < 99.5% | < 99.0% | CC7.1 |
| Critical Vulnerability Rem. SLA | VP, Corporate IT | > 14 Days (since detection) | > 30 Days | CC7.1, CC7.4 |
| Production CSPM "Critical" Open | VP, Infrastructure | > 5 open findings | > 10 open findings | CC6.1 |
| MFA Adoption (`okta_auth_method != okta_push`) | Dir, IAM | < 99% of employees | < 100% of privileged users | CC6.3 |
| Mean Time to Contain (P1/P2) | Dir, Security Operations | > 60 Minutes | > 120 Minutes | CC7.3 |

---

## 7. Monitoring, Metrics, and Reporting

This section defines the cadence and composition of all formal reports generated by the Information Security team.

### 7.1 Reporting Cadence and Recipients

| Report Name | Frequency | Recipients | Content Summary |
| :--- | :--- | :--- | :--- |
| **Executive Security Scorecard** | Quarterly | Board of Directors, CEO, CISO | Overall security posture rating (S1-S5), Top 5 KRIs trending, alignment to NIST CSF, audit roadmap status. |
| **SOC 2 Monitoring Pack** | Monthly (Internal) / Semi-Annual (Audit) | GRC Lead, Internal Audit | Detailed control test results against all SOC 2 TSC. Mapped to specific evidence packages. |
| **Operational D&R Report** | Weekly | CISO, D&R Lead, VP of Engineering | MTTD/MTTR data, Incident volume by severity and business unit, analyst workload index. |
| **Third-Party Risk Snapshot** | Monthly | CISO, General Counsel, VP of Engineering | Aggregate risk score of critical vendors (e.g., AWS, CrowdStrike, Wiz). Includes analysis of recent fourth-party incidents. |
| **Vulnerability Management Report** | Weekly | VP of Engineering, IT Directors | Patch compliance %, High/Crit finding aging by server group. Breakdown by business unit. |

### 7.2 Key Metrics and Analytics for SOC 2 Reporting

To provide thorough coverage for SOC 2 TSC (Security, Availability, Confidentiality), the following specific metrics are mandatory.

#### Section 7.2.1: Security (Common Criteria CC6.1 - CC6.8)

**CC6.1 (Logical and Physical Access Controls):**
1.  **Metric:** `IAM_Permissions_Modified_Since_Last_Review`
    - **Description:** Tracks changes to IAM policies, security groups, and Okta roles that occurred outside of scheduled quarterly access reviews.
    - **Target:** 0% unauthorized changes.
2.  **Metric:** `Production_Public_Exposure`
    - **Description:** CSPM (Wiz) scan result showing any production S3 bucket, EC2 instance, or RDS database marked as `Public` or `Externally Accessible`.
    - **Target:** 0 Public assets. Breach is a P1 incident.

**CC7.1 (Incident Detection):**
1.  **Metric:** `MTTD_P1_Critical`
    - **Description:** Mean time from an alert being generated in the SIEM to an analyst acknowledging the alert.
    - **Target:** < 5 minutes.
2.  **Metric:** `Coverage_Bl_Host_No_EDR`
    - **Description:** Number of production assets (EC2, K8s pods) in the CMDB "Active" state without a corresponding active EDR agent ID.
    - **Target:** 0.

**CC7.3 & CC7.4 (Incident Response & Remediation):**
1.  **Metric:** `Remediation_SLA_Audit_Age`
    - **Description:** Average age in days of "Remediation Complete" tickets after "Resolved" time.
    - **Target:** P1: < 30 min. P2: < 4 hours.

#### Section 7.2.2: Availability (A1.2)

1.  **Metric:** `Metrics_Pipeline_Uptime`
    - **Description:** Uptime of the Splunk ingestion pipeline (internal "availability of monitoring" control).
    - **Target:** 99.9% (Monthly).

#### Section 7.2.3: Confidentiality (C1.1)

1.  **Metric:** `DLP_Incidents_Remediated_Within_SLA`
    - **Description:** Number of sensitive data exfiltration alerts (via Netskope CASB) resolved within the 1-hour mandatory window.
    - **Target:** 100% remediation within SLA.

---

## 8. Exception Handling and Escalation

Deviations from the technical controls, threshold targets, or procedures defined in this SOP must be managed through the formal exception process.

### 8.1 Exception Request Procedure

1.  **Initiator:** The VP/Leader of the business unit failing to meet a metric threshold must submit **Form ISEC-022-E01 (Security Metric Exception Request)** via ServiceNow GRC. The form requires:
    - Business justification for the non-compliance.
    - Detailed compensating controls currently in place.
    - A proposed remediation plan with a hard deadline (not to exceed 90 days).
    - The approved risk acceptance signature from the relevant business unit VP.
2.  **Technical Review (InfoSec GRC):** Maria Hernandez (GRC Lead) performs a technical review within 5 business days. The review assesses the proposed compensating controls against the relevant SOC 2 TSC to determine if they sufficiently reduce residual risk.
3.  **CISO Approval:** Rachel Kim reviews the GRC Lead’s analysis and either approves, denies, or modifies the exception duration. No exception regarding the exposure of PHI or PCI DSS data shall be accepted; these findings must be remediated immediately or the vulnerable system must be isolated from the network.

### 8.2 Breach Escalation Pathway

If a metric falls into a Red Threshold for more than 24 hours without an approved exception, the following automatic escalation occurs:

- **0 Hour:** Red threshold breached. Email notification sent to the responsible Engineering Manager and the InfoSec GRC Lead. A ServiceNow Incident is automatically generated.
- **24 Hours:** Issue remains unresolved. The ServiceNow incident is automatically escalated to Priority 2. The CISO and relevant VP are added as watchers.
- **72 Hours:** Issue remains unresolved. The CISO initiates a formal stand-up call with the VP of Engineering. The issue is flagged as a "Failed Control" in the quarterly SOC 2 evidence package. This is a pre-audit risk escalation, not a final determination.

---

## 9. Training Requirements

All roles defined in Section 3 must complete specific training to ensure compliance and efficacy of this SOP. Training is tracked via Workday Learning.

### 9.1 Role-Based Training Curriculum

| Target Role | Course Title (ID) | Frequency | Content |
| :--- | :--- | :--- | :--- |
| **Security Operations Analysts** | `SOC-IR-201: Metrics-Driven Hunting` | Semi-Annual | Advanced Splunk SPL for hunting based on KRI deviations, understanding false positive ratios, and ALM hygiene. |
| **IT Managers / Directors** | `SOP-ISEC-022: Security Metrics Remediation` | Annual | A detailed walkthrough of this SOP. Focus is on the "Red Threshold" escalation pathway, SLA timers for vulnerability management, and the exception request process in ServiceNow. |
| **All Employees** | `SEC-GEN-001: Role in Security Culture` | Annual | A short, mandatory module explaining how personal actions (like failing phishing tests) contribute to the aggregate phishing KPI reported to the board. |

### 9.2 SOP Onboarding
Upon version change (e.g., 4.6 to 5.0), all direct stakeholders named in Section 3 are auto-enrolled in a targeted "SOP Delta" training module. Failure to complete the module within 15 days results in a "Non-Compliant" status in the security scorecard.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| Document ID | Document Title | Relationship |
| :--- | :--- | :--- |
| **SOP-ISEC-002** | Vulnerability Management | Mandatory input for SVM KPIs and remediation SLA tracking. |
| **SOP-ISEC-010** | Incident Response Protocol | Defines P1/P2/P3 classifications and the operational actions MTTD/MTTR measure. |
| **SOP-ISEC-019** | Third-Party Risk Management | Governs the vendor risk data feeding the Quarterly TPRM Snapshot. |
| **SOP-CLIN-012** | Clinical Model Governance & Risk | Cross-references AI-specific KRIs maintained by the AI Governance Committee. |
| **SOP-ISEC-024** | Access Management & Segregation of Duties | Input for the IAM permission review metrics and MFA adoption KPIs. |

### 10.2 External Frameworks and Standards

- **AICPA SOC 2 (TSC 2017):** Specifically Security, Availability, and Confidentiality Criteria CC6.1 to CC7.4, A1.2, and C1.1.
- **NIST Cybersecurity Framework (CSF) v1.1:** Function: Identify (ID.AM-4), Protect (PR.PT-1), Detect (DE.DP-4), Respond (RS.CO-4), Recover (RC.RP-1).
- **PCI DSS v4.0 Requirement 11:** Regular testing of security systems and processes.
- **HIPAA Security Rule:** §164.308(a)(1)(ii)(D) (Information System Activity Review).

---

## 11. Revision History

| Version | Date | Author | Description of Significant Changes |
| :--- | :--- | :--- | :--- |
| **4.6** | 2025-04-26 | Rachel Kim | Interim update pending Q3 Audit: Explicitly added MFA Adoption KPI thresholds for privileged users; updated D&R Lead role to interim; added PrivateLink requirement to technical controls table (TC-022-03). |
| **4.5** | 2025-01-14 | Maria Hernandez | Full annual review. Replaced "Qualys" with "Wiz" as primary CSPM for Cloud/K8s. Aligned KRI wording with updated Clinical AI governance requirements. Added new quarterly AI-specific risk reporting line. |
| **4.4** | 2024-08-03 | Rachel Kim | Emergency revision: Increased severity of CSPM scan alert for public-facing assets to P1 following a near-miss exposure event in HealthPay. Updated MTTD target to < 5 mins. |
| **4.3** | 2024-05-12 | Maria Hernandez | Standardization update: Formally mapped every KPI to a specific SOC 2 TSC paragraph. Added Section 9 (Training). Approved by Internal Audit for SOC 2 Type II scope. |
| **4.2** | 2024-02-01 | Rachel Kim | Initial creation of the consolidated Security Metrics SOP, merging former Alerting SOP (ISEC-015) and Board Reporting guide. Defined new KRI for Zero Trust rollout progress. |
| **4.0–4.1** | 2023-Q4 | Maria Hernandez | Draft versions prior to executive approval. Defined data normalization taxonomy. |