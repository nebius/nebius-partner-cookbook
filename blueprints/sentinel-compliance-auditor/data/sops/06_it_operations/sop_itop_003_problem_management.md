---
sop_id: "SOP-ITOP-003"
title: "Problem Management"
business_unit: "IT Operations & Infrastructure"
version: "4.2"
effective_date: "2025-12-16"
last_reviewed: "2026-02-25"
next_review: "2026-08-27"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Problem Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for Problem Management at Meridian Health Technologies, Inc. The purpose of Problem Management is to identify the root causes of recurring incidents and systemic weaknesses within the Meridian technology estate, initiate permanent corrective actions, and prevent the recurrence of service disruptions that could impact the availability, confidentiality, and processing integrity of the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the underlying Meridian SaaS Platform.

This SOP defines the lifecycle of a problem record from initial detection and logging, through root cause analysis (RCA) and permanent fix implementation, to final closure and knowledge base population. By managing problems proactively, Meridian reduces the business impact of IT service failures, minimizes downtime for the 340+ hospitals and clinics served globally, protects approximately $4.2B in annual payment processing transactions, and upholds our commitments to patient safety and data integrity.

### 1.2 Scope

This SOP applies to:

- **All Business Units:** Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and Meridian SaaS Platform.
- **All Environments:** Production, staging, disaster recovery (AWS us-east-1, AWS eu-west-1, Azure DR), and pre-production environments that simulate or mirror production workloads.
- **All Technology Layers:** Application logic, machine learning models (including those managed under Kubeflow, MLflow, and SageMaker), data pipelines (Snowflake, Apache Kafka, PostgreSQL, Redis), infrastructure (AWS, Azure), network, and third-party integrations (Pinecone, CrowdStrike, Okta).
- **All Personnel:** Full-time employees, contractors, and managed service providers who support the Meridian technology ecosystem.
- **All Regulatory Domains:** The processes herein are designed to contribute to Meridian's compliance with SOC 2 (Availability, Processing Integrity), the EU AI Act (Article 17 – Quality Management for high-risk AI systems), NIST AI RMF (MAP and MEASURE functions), HIPAA (administrative safeguards for system availability), and SR 11-7 (model risk management for HealthPay).

This SOP does **not** cover the initial restoration of service during an active outage; that process is governed by **SOP-ITOP-002: Incident Response**. Recurring or major incidents, as identified during the Incident Response process, serve as primary inputs to this Problem Management process.

---

## 2. Definitions and Acronyms

| Term | Definition |
|---|---|
| **Problem** | The underlying cause of one or more incidents that have occurred, or a potential future cause of service disruption. |
| **Problem Record** | A structured, auditable ticket maintained in ServiceNow (Meridian’s ITSM platform) documenting the lifecycle of a problem. |
| **Known Error** | A problem that has a documented root cause and a viable workaround or permanent fix that has not yet been implemented. |
| **Known Error Database (KEDB)** | A centralized repository, maintained within ServiceNow and Confluence, containing all Known Errors, their workarounds, and resolution status. |
| **Root Cause Analysis (RCA)** | A formal, structured investigation methodology used to determine the fundamental failure mechanism. Meridian mandates the use of the **Apollo Root Cause Analysis** methodology, supplemented by the **5 Whys** technique for lower-severity problems. |
| **Permanent Fix** | A code change, infrastructure modification, architecture alteration, or process update that eliminates the root cause and prevents future recurrence. |
| **Workaround** | A temporary method to restore service functionality while the permanent fix is being developed. Workarounds must not introduce security or compliance vulnerabilities. |
| **Problem Manager** | A dedicated role within the IT Operations & Infrastructure business unit responsible for overseeing the end-to-end problem lifecycle. |
| **Problem Task Force (PTF)** | A cross-functional team assembled ad-hoc to investigate a specific, high-severity problem. |
| **P1/P2/P3/P4** | Priority levels for problems, mirroring the severity matrix in SOP-ITOP-002. P1 is highest. |
| **EU AI Act** | Regulation (EU) 2024/1689, under which Meridian's Clinical AI products are classified as high-risk AI systems (Annex III). |
| **SR 11-7** | Federal Reserve and OCC Supervisory Guidance on Model Risk Management. |
| **KPI** | Key Performance Indicator. |
| **MTTR** | Mean Time to Resolve (for problems, measured from logging to permanent fix implemented). |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the authority and accountability for Problem Management activities. R=Responsible, A=Accountable, C=Consulted, I=Informed.

| Activity | Problem Manager (IT Ops) | VP of IT Ops (S. Torres) | Technical SMEs (Eng/DevOps/ML) | Business Unit VP | Chief AI Officer (M. Rivera) | CISO / CPO | Customer Ops (M. Chang) |
|---|---|---|---|---|---|---|---|
| Problem Detection & Logging | R | A | C | I | I | I | C |
| Prioritization (P1-P4) | C | A | R | C | C | I | I |
| Root Cause Analysis (RCA) | C | I | R | I | C (if AI-related) | C (if PHI/security) | I |
| Permanent Fix Development | C | I | R | C | A (if AI model) | C | I |
| Known Error Database (KEDB) Maintenance | R | A | C | I | I | I | I |
| Problem Closure | R | A | C | I | I | I | I |
| Trend Reporting & SLT Dashboard | R | A | C | I | I | I | I |
| Emergency Change Authorization | I | A | I | R | R | I | I |

**Key Personnel:**

- **Samantha Torres (VP of IT Operations):** Accountable for the overall Problem Management process health, resource allocation, and escalation resolution.
- **Thomas Anderson (Chief Compliance Officer):** Provides regulatory interpretation for RCA documentation to ensure it meets SOC 2 evidence standards.
- **Dr. Marcus Rivera (Chief AI Officer):** Must be consulted and provide approval on any permanent fix that alters a Clinical AI model’s weights, architecture, or inference pipeline, per EU AI Act requirements.
- **Robert Liu (VP of Financial Services):** Accountable for problems affecting HealthPay payment processing, ensuring SR 11-7 model risk compliance for any fix touching credit scoring or claims automation.

---

## 4. Policy Statements

1.  **Proactive and Reactive Obligation:** Meridian IT Operations shall operate both a reactive problem management process (triggered by P1/P2 incidents, per SOP-ITOP-002) and a proactive problem management process (driven by monitoring trend analysis and AI drift detection).
2.  **Permanent Fixes Over Workarounds:** The objective of all problem investigations shall be the implementation of a permanent, auditable fix. Workarounds recorded in the KEDB are temporary measures with a maximum lifetime of 90 calendar days, after which a formal exception and remediation plan is required, approved by the VP of IT Operations.
3.  **Regulatory Documentation:** All RCA documentation, particularly for problems impacting the Clinical AI Platform and HealthPay, shall be maintained for a minimum of seven (7) years in accordance with SOC 2, HIPAA, and EU MDR records retention requirements.
4.  **Model Risk Alignment:** Any problem related to model performance degradation, feature drift, or anomalous outputs in the Clinical AI Platform or HealthPay credit scoring models shall be managed with the additional rigor prescribed by the NIST AI RMF and SR 11-7, including independent validation as documented in **SOP-AI-008: AI Model Change Control**.
5.  **Change Control Gating:** No permanent fix resulting from a Problem Record shall be deployed into a production environment without passing through the formal Change Management process defined in **SOP-ITOP-001: Change Management**.
6.  **No Blame Culture:** Problem investigations shall be conducted utilizing a "blameless postmortem" philosophy. The goal is to identify process and systemic failures, not individual fault. Human error is recognized as a symptom of a deeper systemic issue.
7.  **Availability Oversight:** Monitoring systems (Datadog, PagerDuty) are configured to continuously observe system health. The IT Operations team is responsible for reviewing monitoring dashboards to identify problem trends. Specific alert routing logic is documented within the system configurations.

---

## 5. Detailed Procedures

### 5.1 Problem Detection and Logging

Problems can be identified through multiple triggers. All identified problems must be logged in ServiceNow using the "Problem Management" module within one business hour of identification.

**5.1.1 Triggers for Problem Creation:**
- **Major Incident Review:** Completion of a P1 or P2 incident postmortem (per SOP-ITOP-002) where the root cause was not fully determined during incident resolution.
- **Repeating Incidents:** Any configuration item (CI) generating three or more incidents of the same classification within a rolling 30-day window.
- **Proactive Analysis:** Trend analysis performed by the AI Operations team using LangSmith and automated Datadog anomaly detection flags a degradation in model accuracy, data drift exceeding a threshold of 15%, or a system resource utilization pattern predicted to reach 90% capacity within 30 days.
- **Vendor Notification:** A security bulletin or end-of-life notification from a critical vendor (e.g., AWS, CrowdStrike, Snowflake) that affects Meridian's current production stack.
- **Risk Assessment Findings:** A finding from an internal audit, penetration test, or the annual SOC 2 Type II assessment identifying a systemic vulnerability.

**5.1.2 Problem Record Fields (Required):**
The following fields are mandatory in ServiceNow at the time of logging:
- **Configuration Item (CI):** The impacted ServiceNow CI (e.g., "SaaS Platform - us-east-1", "HealthPay - Lending Model v2.3"). If unknown, use "Unknown - Investigation Pending."
- **Problem Statement:** A 5W1H (What, When, Where, Who, Impact, How) structured description.
- **Source:** (Incident ID, Event ID, Audit Finding ID, Manual Observation).
- **Detection Method:** (Automated Alert, Engineer Review, User Report).
- **Priority:** Initial assessment per Section 5.2.
- **Assigned To:** Automatically assigned to the Problem Manager queue upon creation.

### 5.2 Problem Prioritization and Categorization

The Problem Manager shall review and finalize the priority within two (2) business hours of ticket creation, consulting the VP of IT Operations for P1 confirmation. Prioritization follows a standard Impact × Urgency matrix.

| Priority | Description | Response Time (Time to Assign PTF) | Resolution Objective (Known Error Identified) | Examples |
|---|---|---|---|---|
| **P1 - Critical** | Systemic failure causing repeated P1 incidents, a complete service outage with unknown root cause, or a security breach vector. | < 1 hour | 24 hours | Recurring database crashes causing total SaaS unavailability; AI model producing clinically unsafe outputs. |
| **P2 - High** | Causing recurring P2 incidents with no workaround; significant degradation for >50% of users or significant financial integrity risk. | < 4 hours | 72 hours | Intermittent claims processing failures in HealthPay; memory leak degrading clinical inference latency by >40%. |
| **P3 - Medium** | Causing recurring P3 incidents; a localized impact on a small user group, or a proactive finding with moderate business impact. | < 8 hours | 5 business days | Specific report generation failure; single AWS availability zone performance issues. |
| **P4 - Low** | Minor cosmetic issues, documentation errors, proactive improvements with zero current user impact. | < 24 hours | TBD/Backlog | A typo in an admin panel; a deprecated library scheduled for upgrade in the next maintenance window. |

Problems impacting the Clinical AI Platform or HealthPay shall be biased towards P2 or P1 if there is any potential for patient harm or financial misstatement, a direct requirement under the EU AI Act and SR 11-7.

### 5.3 Root Cause Analysis (RCA)

All P1 and P2 problems, and a representative sample of P3 problems, require formal Root Cause Analysis. The Problem Manager assigns a Problem Task Force (PTF) via ServiceNow, pulling the required technical SMEs.

**5.3.1 RCA Methodology:**
- **P1/P2 AI/Complex Problems:** The PTF shall use the **Apollo Root Cause Analysis** methodology. This reality-charting method maps all causal relationships, including latent conditions in the Meridian deployment pipeline (Kubeflow, SageMaker), and identifies actionable solutions at multiple points in the causal chain.
- **P3 and Non-Complex P4 Problems:** The assigned SME shall utilize the **"5 Whys"** technique, documented directly within the ServiceNow Problem Record.

**5.3.2 RCA Execution Steps:**
1.  **Data Collection (Phase 1):** The PTF gathers all relevant telemetry, logs, and artifacts. This includes:
    - Datadog APM traces, log streams, and infrastructure host metrics.
    - LangSmith tracing data showing the exact prompt, chain, and tool execution path for AI-related problems.
    - Database query performance logs from Snowflake and PostgreSQL.
    - Recent change records from ServiceNow (**SOP-ITOP-001**) within the affected CI’s topology.
    - HealthPay transaction logs for financial service issues.
2.  **Causal Analysis (Phase 2):** The PTF conducts a structured workshop (in-person or in a dedicated Slack war room) to construct the Apollo chart or 5 Whys chain. All findings must be evidence-based; assumptions must be explicitly logged and validated.
3.  **Documentation (Phase 3):** The final RCA is documented in a standardized RCA Report PDF attached to the ServiceNow Problem Record. This report **must** delineate:
    - The **Physical Root Cause** (the tangible, mechanical failure).
    - The **Human Root Cause** (the decision or action that triggered the failure).
    - The **Latent/Systemic Root Cause** (the process gap, insufficient training, architecture flaw, or missing monitoring alert that enabled the failure to occur and escape detection). *Note: For SOC 2 and EU AI Act compliance, identifying the Latent Root Cause is mandatory to close a P1/P2 problem.*
4.  **AI-Specific Requirements:** For problems within the Clinical AI Platform or any HealthPay SR 11-7 model, the RCA must additionally include:
    - A review of the training data pipeline for poisoning or skew.
    - An evaluation of the model’s explainability output (SHAP/LIME) at the point of failure.
    - A signed confirmation from the Chief AI Officer's delegated validator.

### 5.4 Known Error Database (KEDB) and Workarounds

When a problem has a successfully identified root cause but a permanent fix is not immediately deployable, it transitions to a Known Error state.

1.  **KEDB Entry:** The Problem Manager creates a KEDB article linked to the Problem Record in ServiceNow. The KEDB article must contain:
    - **Symptoms:** A clear description matching the incident pattern.
    - **Affected Services:** Specific CI names.
    - **Root Cause Summary:** Condensed from the RCA.
    - **Workaround Procedure:** A step-by-step guide that the Customer Operations team (Tier 1/2) can execute. This must be validated in a non-production environment before publication. *Example: "If the MedInsight dashboard returns Error 504, clear the Redis cache 'medinsight-session' key via the Admin CLI."*
    - **Expiration Date:** Default is 90 days from entry.
2.  **Workaround Governance:** The Customer Operations team uses KEDB articles to accelerate incident resolution. Each use of a workaround automatically generates a task in ServiceNow to review the permanent fix plan.

### 5.5 Permanent Fix Implementation

This is the primary exit criterion for a Problem Record.

1.  **Solution Design:** The PTF SME designs the code, infrastructure, or process change. For AI models, this may involve re-training, data augmentation, or architectural changes. This design must be documented in a Solution Design Document (SDD) and linked to the Problem Record.
2.  **Change Request (CR) Creation:** The SME creates a formal Change Request in ServiceNow, strictly adhering to **SOP-ITOP-001: Change Management**. The CR must explicitly reference the Problem Record ID, ensuring the full causal history is visible to the Change Advisory Board (CAB).
3.  **Validation and Testing:** The proposed fix must be deployed through the standard CI/CD pipeline (GitHub Actions -> ArgoCD -> Staging -> Production). Specific testing gates include:
    - **Unit/Integration Tests:** Standard pipeline gates.
    - **Non-Regression Testing:** A targeted test suite proving the original failure no longer occurs.
    - **AI Model Validation:** For Clinical AI, a silent deployment and a shadow-mode evaluation against a hold-out dataset for a minimum of 7 days, reviewed and approved by Dr. Marcus Rivera’s AI governance team.
    - **Performance Testing:** Ensuring the fix introduces no latency or throughput degradation exceeding 5% of baseline.
4.  **Deployment and Verification:** Upon CAB approval, the change is deployed. The Problem Manager monitors the production environment via the Datadog problem dashboard for seven (7) calendar days post-deployment to confirm zero recurrence of the problem symptoms.

### 5.6 Problem Closure

A Problem Record is eligible for closure by the Problem Manager only when all the following conditions are met:
1.  The permanent fix has been successfully deployed and verified in production for the defined monitoring period.
2.  The associated KEDB article (if any) has been marked as "Resolved – Superseded by Permanent Fix."
3.  The RCA report and SDD are finalized and attached.
4.  Closure notes contain a "lessons learned" summary, including recommendations for proactive monitoring improvements and updated alert thresholds.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls
- **ServiceNow Workflow Engine:** Enforces mandatory fields, state transitions (New -> Assigned -> Under Investigation -> Known Error -> Fix in Progress -> Resolved -> Closed), and SLA timers. The system is configured to not allow closure of a P1/P2 problem without an attached RCA document.
- **GitHub Code Ownership:** Any code changed as part of a permanent fix requires approval from a designated CODEOWNER file, which includes the AI Governance team for all `ml-models/` directory changes or any change to the HealthPay scoring algorithms.
- **HashiCorp Vault Integration:** Any new secrets or configuration parameters created for a permanent fix must be stored in HashiCorp Vault, not hardcoded or stored in plaintext in the SDD.
- **Immutable Logging:** RCA evidence and problem records are logged to an immutable, append-only backup in AWS S3 with Object Lock enabled, providing a non-repudiable audit trail for the seven-year regulatory retention period.

### 6.2 Process Controls
- **Segregation of Duties:** The individual who identifies a problem can log it. However, the PTF lead performing the RCA for a P1/P2 problem cannot be the same individual who authored the original change that introduced the problem.
- **RCA Review Board:** All P1 RCAs are reviewed within ten (10) business days by a board comprising the VP of IT Operations, CISO (Rachel Kim), and the relevant Business Unit VP.
- **Problem Task Force Charter:** Every PTF must have its scope, timeline, and access rights formally authorized in ServiceNow. This ensures no unauthorized access to PHI during the investigation; access is granted temporarily via Okta workflows that auto-expire.

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness of the Problem Management process is continuously measured. Meridian IT Operations uses a dedicated Datadog dashboard overlaid with ServiceNow data and a monthly executive PowerBI report aligned to the IT Balanced Scorecard.

### 7.1 Key Performance Indicators (KPIs)

| KPI Category | Metric | Target | Calculation Method |
|---|---|---|---|
| Operational Health | Number of Recurring Incidents Prevented | 95% of resolved problems show zero recurrence within 180 days | (Problems resolved / (Problems resolved + Problems with recurrences)) * 100 |
| Timeliness | Mean Time to Resolve (MTTR) by Priority | P1: < 7 days, P2: < 30 days, P3: < 90 days | Average((Problem.Closed_Date - Problem.Opened_Date)) per Priority |
| Quality | RCA Quality Score | Average Score > 4.2/5.0 | Monthly audit of a random 15% sample of RCAs against a standardized 10-criteria rubric measuring completeness of latent cause identification |
| Backlog Health | Aging Problem Backlog | No P1/P2 open > 60 days; No P3 open > 180 days | Count of Problem Records grouped by Priority and Age Bucket |

### 7.2 Reporting Cadence
- **Weekly Operations Review:** The Problem Manager presents a "Problem Aging" report and highlights any problems breaching SLA to the VP of IT Operations.
- **Monthly IT Governance Meeting:** A trend analysis dashboard showing problem volume by business unit, top problematic CIs, and a Pareto chart of problem categories is presented to the CIo, CTO, and CISO.
- **Quarterly Board-Level AI Governance:** Dr. Marcus Rivera presents a specific sub-section on AI and model-related problems, their resolution status, and EU AI Act remediation efforts.

### 7.3 Proactive Problem Signal Monitoring
The Datadog dashboard is configured to generate a proactive problem candidate in ServiceNow when:
- A specific model's prediction confidence score drops below a pre-defined function-specific threshold for a continuous window of 30 minutes.
- A critical API endpoint experiences a 10% increase in 5xx error rate hour-over-hour, but has not yet triggered a PagerDuty incident.
- Alert thresholds and escalation paths are defined in the respective monitoring system configurations to ensure consistent notification.

---

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Process
Any deviation from this SOP's defined timelines, mandatory fields, or process steps must be managed through a formal, auditable exception. The requestor must file a "Problem Management Exception Request" form, linked to the specific Problem Record. This form requires:
- Specific process deviation request.
- Compelling business justification.
- Risk assessment of not following the standard process.
- Proposed alternative action and timeline.

**Approval Matrix:**
- **P3/P4 SLA Extensions:** Approved by the IT Operations Problem Manager.
- **P1/P2 SLA Extensions:** Approved by the VP of IT Operations (Samantha Torres).
- **RCA Methodology Substitution:** Approved by the Chief AI Officer (if AI-related) or CISO.
- **Workaround Lifetime Extension (>90 days):** This constitutes a formal risk acceptance and must be approved by the Business Unit VP, CISO, and the VP of IT Operations.

### 8.2 Escalation Path
If a problem is not receiving the required attention or resources, or if permanent fix development is stalled, the following hierarchical escalation applies:
1.  **Problem Manager:** Direct oversight of PTF execution.
2.  **VP of IT Operations (Samantha Torres):** Escalated for resource contention, cross-team conflict, or P1/P2 resolution delays. Samantha Torres has the authority to commandeer resources from non-patient-facing projects to resolve critical infrastructure problems.
3.  **Chief AI Officer (Dr. Marcus Rivera) & CISO (Rachel Kim):** Escalated for any problem with direct, articulable patient safety risk or a security vulnerability being actively exploited.
4.  **CEO (Dr. Sarah Chen):** Final escalation for enterprise-critical, reputationally damaging problems impacting multiple business lines, per the Crisis Management Plan.

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Role | Training Module | Delivery Method | Frequency | Tracking |
|---|---|---|---|---|
| All IT, Engineering, ML Staff | PM-101: Intro to Problem Management | Meridian LMS (Workday Learning) | Within 30 days of hire; Annual Refresh | Workday HR Records |
| Problem Manager | PM-201: Advanced RCA Facilitation & Apollo Methodology | Instructor-led (3-day course) by Certified Apollo Instructor | Once; Recertification every 2 years | IT Ops Training Register |
| Technical SMEs (DevOps, SRE, MLE) | PM-202: Technical RCA Writing & Blameless Postmortems | Internal Workshop (quarterly) led by Problem Manager | Annual | IT Ops Training Register |
| VP-Level & Above | PM-301: Problem Governance & Escalation | Video briefing + sign-off acknowledgement | Annual | Workday HR Records |

### 9.2 Competency Assessment
- All technical staff must complete a simulated Problem Investigation exercise as part of the annual SOC 2 compliance readiness tabletop exercise, coordinated by the Chief Compliance Officer (Thomas Anderson).
- The Problem Manager must maintain active certification in a recognized RCA methodology as part of their annual performance goals.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- **SOP-ITOP-001: Change Management** — Governing the deployment of all permanent fixes.
- **SOP-ITOP-002: Incident Response** — Primary input source for reactive problem management.
- **SOP-SEC-004: Vulnerability Management** — For security-originated problems.
- **SOP-AI-008: AI Model Change Control** — Additional gates for Clinical AI and HealthPay model changes.
- **SOP-PRI-010: PHI Data Handling During Investigations** — Ensuring RCA data use compliance.
- **SOP-INF-015: AWS Infrastructure Monitoring and Alerting** — Configuration details for proactive problem detection.

### 10.2 External Standards and Regulatory References
- **SOC 2 (TSP Section 100):** 2017 Trust Services Criteria – Availability and Processing Integrity. This process directly supports A1.2 (The entity authorizes, designs, develops or acquires, implements, operates, approves, maintains, and monitors environmental protections, software, data backup processes, and recovery infrastructure to meet its objectives) and PI1.1 (The entity obtains or generates, uses, and communicates relevant, quality information regarding the objectives related to processing, including definitions of data processed and product and service specifications).
- **NIST AI RMF 1.0:** MAP 3.5, MEASURE 2.6, MANAGE 3.1.
- **EU AI Act (2024/1689):** Article 15 (Accuracy, Robustness, Cybersecurity), Article 17 (Quality Management System), Recital 66.
- **HIPAA:** 45 CFR § 164.308(a)(7) – Contingency Operations.
- **SR 11-7:** Section III (Model Development, Implementation, and Use) & Section V (Model Validation).

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 1.0 | 2021-03-10 | Samantha Torres | Initial release. Established core problem lifecycle for SOC 2 Type II preparation. |
| 2.0 | 2022-06-05 | Samantha Torres | Added formal KEDB procedures and integration with ServiceNow CSDM. |
| 3.0 | 2023-11-14 | Thomas Anderson | Major revision to incorporate NIST AI RMF requirements and Apollo RCA mandate for AI incidents. |
| 4.0 | 2024-09-20 | Dr. Marcus Rivera | Updated to reflect EU AI Act Article 17 obligations for high-risk AI systems; added AI-specific RCA data requirements (Section 5.3.2). |
| 4.1 | 2025-08-15 | Samantha Torres | Refined Proactive Problem Detection (Section 7.3) to include LangSmith drift metrics; updated roles for HealthPay SR 11-7 alignment. |
| 4.2 | 2025-12-16 | Samantha Torres | Full annual review. Updated escalation paths, added immutable logging control (Section 6.1), and refined SOC 2 availability monitoring language. |