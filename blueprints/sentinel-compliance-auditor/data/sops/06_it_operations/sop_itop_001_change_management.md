---
sop_id: "SOP-ITOP-001"
title: "Change Management"
business_unit: "IT Operations & Infrastructure"
version: "2.8"
effective_date: "2024-08-09"
last_reviewed: "2025-05-21"
next_review: "2025-11-20"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Change Management

**SOP-ITOP-001 | Version 2.8**
**Effective Date: 2024-08-09**
**Owner: Samantha Torres, VP of IT Operations**
**Classification: Internal**

---

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish a standardized, auditable, and regulatory-compliant framework for managing all changes to the Meridian Health Technologies, Inc. information technology environment. This framework ensures that all modifications to production systems, applications, network infrastructure, and underlying cloud resources are assessed, authorized, implemented, and validated in a controlled manner that minimizes risk to the confidentiality, integrity, and availability (CIA) of protected health information (PHI) and other sensitive data, while maintaining the stability and reliability of critical healthcare and financial services platforms.

This SOP operationalizes the Change Management policy requirements mandated by the SOC 2 Trust Services Criteria (TSC) for Change Management (CC8.1), HIPAA Security Rule (45 CFR § 164.312), and internal AI governance controls derived from the NIST AI RMF and EU AI Act.

### 1.2 Scope

This SOP applies to:

- **All production environments** across the Meridian SaaS Platform, HealthPay Financial Services, Clinical AI Platform, and MedInsight Analytics.
- **All infrastructure components** hosted on AWS (us-east-1, eu-west-1) and Azure (DR).
- **All software**, including custom-developed code, commercial off-the-shelf (COTS) applications, container images, serverless functions, and AI/ML models.
- **All configurations**, including operating systems, databases (Snowflake, PostgreSQL, Redis), network devices, security tools (CrowdStrike, Okta), CI/CD pipelines, and Infrastructure-as-Code (IaC) templates.
- **All data-related changes**, including schema modifications, data migration scripts, and ETL pipeline alterations.
- **All personnel** (employees, contractors, consultants, and third-party vendors) with access to production systems or the ability to initiate, approve, or implement changes.

This SOP covers the entire lifecycle of a change, from initial request through post-implementation review, and applies regardless of whether the change is executed manually or via automated pipelines. Emergency changes are addressed through an expedited but equally rigorous process defined in Section 5.7.

### 1.3 Out of Scope

This SOP does not directly govern changes to physical office facilities, human resources policies, or financial accounting processes unless such changes directly impact the IT control environment. Standard operational tasks that do not alter the configuration, code, or data structure of a system (e.g., routine health checks, viewing logs, acknowledging PagerDuty alerts) are not considered changes for the purpose of this SOP.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
| :--- | :--- |
| **Change** | Any addition, modification, or removal of anything that could have an effect on IT services, including software, hardware, system configurations, network topology, documentation, or associated processes. |
| **Standard Change** | A low-risk, pre-authorized change that follows a documented, repeatable procedure and is performed frequently. These changes do not require full CAB review for each instance but must be registered and tracked. |
| **Normal Change** | A non-emergency change that follows the complete change management process flow, including CAB review and formal approval. |
| **Emergency Change** | A change required to address a critical incident or prevent an imminent and significant business disruption. Emergency changes bypass the standard lead-time requirements but still require post-facto review and documentation. |
| **Major Change** | A Normal Change posing a high risk, requiring extensive planning, a technical review board, and a formal CAB presentation by the Change Owner. |
| **Change Impact Analysis (CIA)** | A documented evaluation of the potential effects of a proposed change on systems, data integrity (especially PHI), security posture, performance, and dependent services. Distinct from the acronym for Confidentiality, Integrity, Availability. |
| **Rollback Plan** | A pre-defined, tested procedure to revert a system to its known-good state prior to the change implementation. |
| **Back-Out Window** | The specific time limit within which a change must be successfully executed or fully rolled back to avoid service disruption. |
| **Maintenance Window** | A pre-approved, recurring timeframe during which specific maintenance activities are permitted. |
| **Technical Review Board (TRB)** | A panel of senior architects and principal engineers responsible for vetting the technical soundness of Major Changes prior to CAB submission. |
| **Frozen Period** | A defined interval during which non-emergency changes are prohibited to ensure system stability (e.g., year-end financial processing, peak healthcare enrollment periods). |

### 2.2 Acronyms

| Acronym | Definition |
| :--- | :--- |
| AWS | Amazon Web Services |
| BIA | Business Impact Analysis |
| CAB | Change Advisory Board |
| CCB | Change Control Board (synonymous with CAB) |
| CI/CD | Continuous Integration / Continuous Deployment |
| CMDB | Configuration Management Database |
| CM | Change Manager |
| CMB | Clinical Model Board (for Clinical AI Platform changes) |
| ePHI | Electronic Protected Health Information |
| IaC | Infrastructure as Code |
| JML | Joiner, Mover, Leaver (Identity Lifecycle) |
| KPI | Key Performance Indicator |
| MLAI | Machine Learning / Artificial Intelligence |
| PIR | Post-Implementation Review |
| RFC | Request for Change |
| SLA | Service Level Agreement |
| SRM | SaaS Release Manager |
| TSC | Trust Services Criteria (SOC 2) |
| WO | Work Order |

---

## 3. Roles and Responsibilities

The following matrix defines the functional roles and their responsibilities within the Change Management process. Individuals may hold multiple roles, but segregation of duties must be maintained between the Change Requester, Change Implementer, and Change Approver for all Normal and Major Changes.

### 3.1 Responsibility Assignment Matrix (RACI)

| Activity / Task | Change Requester | Change Owner | CAB Members | Change Manager | Change Implementer | VP IT Ops (Sponsor) | Security / Privacy |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **RFC Submission** | **R**, A | C | I | I | I | I | I |
| **Impact & Risk Analysis** | C | **R**, A | C | C | C | I | C |
| **Technical Review (TRB)** | I | C | C | I | **R** | I | C |
| **CAB Agenda & Facilitation** | I | I | C | **R**, A | I | I | I |
| **Change Approval** | I | I | **R**, A | C | I | A | A |
| **Implementation Execution** | I | A | I | I | **R** | I | I |
| **Post-Impl. Review (PIR)** | I | **R**, A | C | C | C | I | I |
| **CMDB Update** | I | C | I | **R**, A | C | I | I |
| **Rollback Execution** | I | A | I | I | **R** | I | I |

**R = Responsible** (performs the task), **A = Accountable** (approves/signs off), **C = Consulted**, **I = Informed**

### 3.2 Named Role Assignments

| Role | Individual / Group | Core Responsibility |
| :--- | :--- | :--- |
| **VP of IT Operations (Sponsor)** | Samantha Torres | Ultimate authority for Emergency Change approval; resolves escalated disputes; approves Change Freezes. |
| **Change Manager (CM)** | Michael Okonkwo (Sr. Manager, IT Service Mgmt) | Day-to-day process owner; manages RFC queue, chairs CAB meetings, enforces SLAs, maintains KPIs. |
| **SaaS Release Manager (SRM)** | Assigned per sprint (Engineering team) | Coordinates code deployment schedules, merging of feature branches, and release tagging. |
| **CAB Members (Standing)** | See Section 5.5.2 | Reviews and approves/rejects Normal and Major Changes based on operational readiness and risk. |
| **Clinical Model Board (CMB)** | Dr. Aisha Okafor (Chair), Dr. Marcus Rivera | Reviews all changes to Class III (high-risk) clinical AI models subject to EU AI Act and FDA oversight. |
| **Security Assessor** | InfoSec Team (CISO: Rachel Kim) | Mandatory reviewer for any change impacting network security, IAM, ePHI handling, or cryptographic controls. |
| **Privacy Assessor** | CPO/DPO Office (Dr. Klaus Weber) | Mandatory reviewer for changes affecting the processing of personal data of EU data subjects (GDPR Art. 35 triggers). |
| **Data Steward** | Lead Data Architect (Maria Santos) | Reviews schema changes, ETL modifications, and data lifecycle management alterations. |
| **Incident Commander** | On-call SRE Lead | Authorized to declare an incident requiring an Emergency Change. |

---

## 4. Policy Statements

Meridian Health Technologies is committed to the following high-level policy mandates, which form the foundation of this SOP:

1.  **Integrity and Stability:** All changes to production environments shall be managed to prevent unintended disruptions, maintain data integrity, and ensure the continuous availability of critical healthcare and financial systems supporting patient safety. Unauthorized changes are strictly prohibited.
2.  **Risk-Based Classification:** Every change shall be classified according to risk, scope, and potential impact on system security and PHI. The rigor of review, testing, and approval shall be directly proportional to the change's risk classification.
3.  **Formal Authorization:** No change shall be implemented in a production environment without documented authorization from the appropriate authority, as defined in Section 5.5 and its subsections. Changes to high-risk AI systems, as classified under the EU AI Act Annex III, require additional authorization from the Clinical Model Board (CMB).
4.  **Segregation of Duties:** No individual shall develop, approve, and implement a Normal or Major Change into production. The Change Requester, Approver, and Implementer must be distinct individuals where operationally feasible. Automated CI/CD pipelines that bypass this segregation require compensating controls validated during SOC 2 audits.
5.  **Comprehensive Testing:** All changes must undergo appropriate levels of testing in isolated environments that mirror production before being approved for deployment. For clinical AI models, testing must include algorithmic fairness, bias evaluation, and performance drift analysis per the NIST AI RMF.
6.  **Auditable Logging:** All RFCs, approvals, implementation actions, rollback events, and post-implementation reviews shall be recorded in a centralized, immutable, and tamper-proof system (ServiceNow). These records serve as the official audit trail for SOC 2, HIPAA, and FDA 510(k) post-market surveillance.
7.  **Right to Roll Back:** Every change must have a pre-defined, tested rollback plan or back-out strategy. If a rollback is technically impossible (e.g., destructive schema change), a compensating exception plan must be documented, reviewed by the CAB, and approved in advance.
8.  **Continuous Improvement:** The Change Management process shall be regularly reviewed and optimized using data-driven KPIs (Section 7) to reduce failure rates and increase throughput without compromising compliance.

---

## 5. Detailed Procedures

### 5.1 Change Lifecycle Overview

The standard change lifecycle consists of five sequential phases:

1.  **Request & Triage:** A Request for Change (RFC) is created, categorized, and logged in ServiceNow.
2.  **Impact Analysis & Planning:** The Change Owner performs a detailed risk assessment and develops implementation, testing, and rollback plans, consulting subject matter experts as required.
3.  **Review & Approval:** The RFC is reviewed by the appropriate authority (CAB, CMB, or automated pre-authorization for Standard Changes) and either approved, rejected, or deferred.
4.  **Implementation & Monitoring:** The Change Implementer executes the change during the assigned maintenance window, with real-time monitoring by the IT Operations Command Center.
5.  **Validation & Closure:** The Change Owner verifies successful implementation, updates the CMDB, captures lessons learned in a Post-Implementation Review (PIR), and formally closes the RFC.

### 5.2 Change Classification and Lead Times

Changes must be classified by the Change Owner at the time of submission. The Change Manager validates the classification during triage.

| Change Type | Risk Level | Definition Examples | Minimum Lead Time Before CAB/WO | Approval Body |
| :--- | :--- | :--- | :--- | :--- |
| **Standard** | Low | Routine OS patching via AWS Patch Manager, deploying a pre-approved container image version bump, adding a user to a non-privileged AD group. | 24 hours (Automated) | Pre-authorized by Change Manager + ServiceNow workflow |
| **Normal** | Medium | Feature enhancement to MedInsight Analytics dashboard (non-PHI facing), database index addition, firewall rule modification, minor infrastructure-as-code (Terraform) update. | 3 business days | CAB (weekly meeting) |
| **Major** | High | Upgrading a production Kubernetes cluster, migrating a PostgreSQL RDS instance, deploying a new Clinical AI model version, significant changes to Snowflake data access controls, merging a long-lived feature branch to `main`. | 7 business days (incl. TRB review) | CAB + CMB (if applicable) + Security + Privacy |
| **Emergency** | Critical | Patching an actively exploited zero-day vulnerability, restarting a cascading failure in the Kafka message broker, revoking a compromised API key. | Immediate (authorization within 1 hour) | Incident Commander + VP IT Ops (or delegate) |

### 5.3 Request for Change (RFC) Submission

A Change Owner initiates the process by submitting an RFC in ServiceNow using the **`MHT-CHG-RFC`** form. The RFC is a controlled document and cannot be deleted once submitted; it can only be closed as "Cancelled."

**Mandatory Fields on the RFC Form:**

1.  **General Information:**
    *   **Requestor Name / Dept:** Auto-populated via Okta SSO.
    *   **Change Owner:** The single accountable person.
    *   **Change Implementer(s):** Named individuals or the service account for automation.
    *   **Title:** Concise description of the change.
    *   **Description:** Executive summary including the business need and technical approach.
    *   **Business Justification:** Link to a Jira epic, problem ticket (PBI), or strategic initiative.
    *   **Change Type:** [Standard / Normal / Major / Emergency]
    *   **Priority:** [Critical / High / Medium / Low] based on urgency.

2.  **Systems Affected:**
    *   **Configuration Item(s) (CI):** Specific servers, services, applications (e.g., `prd-mia-db-01`, `svc-claims-engine`).
    *   **Environment(s):** [Production, Staging, DR]. Note: Changes to production require staging validation.
    *   **Data Sensitivity:** Checkboxes for [PHI/ePHI | PCI-DSS Financial Data | EU Personal Data | Proprietary AI Model Weights].

3.  **Scheduling & Risk:**
    *   **Proposed Maintenance Window:** Start and end time (typically in UTC). Refer to Section 5.4.1 for global window policy.
    *   **Outage / Downtime Expected:** [Yes / No]. If yes, attach the BIA summary.
    *   **Back-Out Window:** The absolute drop-dead time for a rollback decision (e.g., "If step 3 is not completed by 03:00 UTC, initiate rollback").
    *   **Risk Score (Pre-assessment):** Auto-calculated based on CI criticality, PHI involvement, and outage flag.

4.  **Plan Attachments (Mandatory for Normal/Major):**
    *   **Technical Implementation Plan:** A step-by-step command sequence or automated pipeline job reference.
    *   **Test Plan:** Evidence of successful completion in staging, including automated integration tests, smoke tests, and NLP model accuracy thresholds (if applicable).
    *   **Rollback Plan:** Detailed, step-by-step instructions to revert to the last known good state. Must be executed by the same Implementer or their identified backup.
    *   **DPIA Reference:** Mandatory if EU Personal Data processing is affected (GDPR Art. 35).

5.  **Post-Change Validation:**
    *   **Success Criteria:** Specific, measurable outcomes (e.g., "p95 latency for /api/v2/claims remains < 200ms", "model precision for ADR detection >= 0.92 on validation set").
    *   **Validation Steps:** Commands and checks to be performed post-implementation to confirm success.

### 5.4 Planning: Maintenance Windows and Change Freezes

#### 5.4.1 Global Maintenance Windows

To minimize operational disruption to our clients, which include 24/7 hospitals and health systems, routine maintenance is scheduled during low-activity periods.

| Environment | Primary Window (Local Time) | Day | UTC Equivalent |
| :--- | :--- | :--- | :--- |
| **us-east-1 Production** | 01:00 - 06:00 EST | Saturday | 06:00 - 11:00 UTC |
| **eu-west-1 Production** | 01:00 - 06:00 CET | Saturday | 00:00 - 05:00 UTC |
| **Financial Batch Processing**| 02:00 - 06:00 EST | Sunday | 07:00 - 11:00 UTC |

Any change requiring a window outside of these slots must be explicitly justified, noting the impact on SLA windows, and approved by the VP of IT Operations.

#### 5.4.2 Annual Change Freeze Calendar

No Normal or Major Changes are permitted during the following periods without a formal Emergency RFC and explicit approval from the Chief Compliance Officer, Thomas Anderson, and the CISO, Rachel Kim.

| Period | Description | Business Unit Impacted | Dates (2025) |
| :--- | :--- | :--- | :--- |
| **Year-End Processing** | Financial close for HealthPay | HealthPay Financial Services | Dec 22, 2025 – Jan 5, 2026 |
| **Open Enrollment Peak** | High-volume benefit verification | MedInsight Analytics | Oct 15 – Dec 7, 2025 |
| **SOC 2 Audit Window** | External auditor observation period | SaaS Platform (All Prod) | Sep 14 – Sep 25, 2025 |

Standard Changes (routine patching) may continue during freeze periods, but all automation schedules should be reviewed by the Change Manager 48 hours prior to the freeze.

### 5.5 Review and Approval Workflows

#### 5.5.1 Standard Change Pre-Authorization

Standard Changes bypass the full CAB meeting but are not unmanaged. To qualify for a Standard Change template, a process owner must submit a detailed request to the Change Manager, including the exact script/playbook. The Change Manager and Security Assessor jointly review and, if accepted, create a reusable ServiceNow template. This template is re-validated on a 6-month cycle. Every execution of a Standard Change generates a unique RFC with a "STD-####" identifier, which is linked to the template and logged in the CMDB.

#### 5.5.2 Change Advisory Board (CAB) Operations

The CAB is the central governance body for all Normal and Major Changes. The CAB is not a democracy; it is a consultative forum. The Change Manager is responsible for facilitating the meeting, but the CAB's output is a recommendation. The final approval authority for a Normal Change lies with the Change Manager; for a Major Change, it lies jointly with the VP of IT Operations or their delegate and the VP of Engineering or CISO, depending on the domain.

**Standing CAB Membership:**
- Chair / Facilitator: **Michael Okonkwo** (Change Manager)
- IT Operations: **Samantha Torres** (or delegate from SRE team)
- Engineering: **David Park** (or delegate, typically the SaaS Release Manager)
- Security: **Rachel Kim** (or delegate from InfoSec GRC)
- Customer Operations: **Michael Chang** (or delegate)
- Clinical Informatics: **Dr. Aisha Okafor** (required for any clinical workflow changes)
- Financial Services: **Robert Liu** (required for any HealthPay changes)
- Data Management: **Maria Santos** (Lead Data Architect)

**CAB Meeting Cadence:**
- **Frequency:** Weekly, Tuesday 10:00 - 12:00 EST.
- **Submission Deadline:** All RFCs must be in "Ready for Review" status by the preceding Friday at 12:00 EST. The Change Manager publishes the agenda ("Forward Schedule of Change" or FSC) by Friday 17:00 EST.
- **Quorum:** Requires the Chair, one IT Operations representative, and one representative from either Engineering or Security. No decisions affecting clinical systems without the Clinical Informatics representative.

#### 5.5.3 Clinical Model Board (CMB) Override

Given Meridian's regulatory status under the EU AI Act (High-Risk AI Systems) and FDA 510(k) clearances, any change to the following requires a separate, explicit approval from the CMB, documented as a prerequisite before the CAB can authorize the release:
- Clinical AI Platform v3.x model weights, architecture, or feature engineering logic.
- Patient risk scoring algorithms.
- Adverse event prediction systems.
- Diagnostic imaging analysis parameters (FDA regulated).

The CMB, chaired by Dr. Aisha Okafor, mandates additional documentation including:
- Algorithmic Fairness Assessment (disparate impact analysis on protected patient demographics).
- Performance Drift Analysis on holdout datasets.
- Human-in-the-Loop Validation Protocol confirmation.

#### 5.5.4 Approval Authority Matrix

| Change Type | RFC Prerequisites | CAB Review | CMO/CMB Review | Final Approver (in ServiceNow) |
| :--- | :--- | :--- | :--- | :--- |
| Standard | Valid Template, Test Results | No | No | Michael Okonkwo (Automated) |
| Normal (Non-Clinical) | Full RFC, Test Plan, Rollback Plan | Yes | No | Michael Okonkwo |
| Normal (Clinical UI) | Full RFC + Usability Test | Yes | Yes (CMO delegate) | Michael Okonkwo + Dr. Okafor |
| Major (Infra) | Full RFC + TRB Sign-off | Yes | No | Samantha Torres |
| Major (Clinical AI) | Full RFC + TRB + Fairness Assessment | Yes | Yes (Full CMB Vote) | Samantha Torres + Dr. Okafor |
| Major (HealthPay) | Full RFC + SR 11-7 Model Risk Doc | Yes | No | Samantha Torres + Robert Liu |
| Emergency | PagerDuty Incident ID | N/A (Post-facto) | N/A (Post-facto) | On-call Incident Commander |

### 5.6 Implementation and Validation

1.  **Pre-Implementation Checklist (DoW):** In the 60 minutes before the window, the Change Implementer completes the ServiceNow "Pre-Check" task list:
    *   Confirm the rollback plan is still valid.
    *   Verify the state of the relevant monitoring dashboards (Datadog).
    *   Announce the imminent change on the `#eng-ops-announce` Slack channel.
    *   Suspend related PagerDuty alerting rules where appropriate.
2.  **Execution:** The Implementer follows the Technical Implementation Plan. If a step in the plan deviates, the Implementer pauses and contacts the Change Owner. If the deviation is high-risk, the Owner contacts the on-call Incident Commander to discuss aborting to the Rollback Plan.
3.  **Back-Out Window:** If the implementation time touches the Back-Out Window threshold, the Implementer is empowered and required to initiate the Rollback Plan immediately to restore the service definition.
4.  **Post-Implementation Validation:** Immediately upon completion:
    *   Execute the Post-Change Validation steps defined in the RFC.
    *   Monitor the Datadog dashboards for 30 minutes specifically focusing on the `prod-all-synthetic` test results.
    *   The Change Owner acknowledges the results in ServiceNow.
5.  **CMDB Update:** Within 2 hours of successful validation, the automated AWS Config / ServiceNow integration reconciliation must be confirmed, or the Implementer manually updates the CIs.

### 5.7 Emergency Change Procedure

Emergency Changes are used to resolve Critical (P1) incidents or deploy security patches for confirmed active threats (e.g., a CVE with a CVSS score > 9.0 actively exploited in the wild).

1.  **Initiation:** The on-call Incident Commander declares an emergency and creates an Emergency RFC in ServiceNow, linking the active PagerDuty incident.
2.  **Authorization (1-Hour Window):** The Incident Commander, or their superior (Samantha Torres or Rachel Kim), must approve the Emergency RFC. No CAB meeting is required. If the Emergency Change involves the Clinical AI Platform, the on-call Clinical Informatics Lead must also approve.
3.  **Execution:** The most qualified available engineer (the Implementer) executes the fix. Peer review before execution is strongly encouraged but not required; at minimum, the steps must be screen-shared or co-piloted with another engineer in a Zoom bridge.
4.  **Post-Facto Review (72-Hour PIR):**
    *   The Emergency RFC is automatically placed on the agenda for the next possible CAB meeting (even an extraordinary meeting).
    *   Full documentation (root cause, implementation steps, validation) must be completed retroactively.
    *   The CAB will determine if the fix is a permanent remediation or if a follow-up Normal RFC is required to address technical debt.

---

## 6. Controls and Safeguards

This section details the specific administrative, technical, and physical controls that enforce the Change Management policy.

### 6.1 Administrative Controls

| Control ID | Control Description | Regulatory Mapping |
| :--- | :--- | :--- |
| **CM-ADM-01** | **Segregation of Duties (SoD) Enforcement:** No single user account can approve its own Normal or Major RFC. ServiceNow workflow logic programmatically prevents RFC closure if the `sys_updated_by` for the implementation and approval match on the same ticket, unless it is an Emergency Change ratified by CISO. | SOC 2 CC8.1 (Paragraph 4), HIPAA 164.312(a)(1) |
| **CM-ADM-02** | **Annual Access Review for Approvers:** The CISO's office conducts an annual review of all users granted the `change_approver` role in ServiceNow. Validation is performed against HR JML records and current job descriptions. | SOC 2 CC6.3, HIPAA 164.308(a)(3)(ii)(B) |
| **CM-ADM-03** | **Quarterly Process Audit:** The Internal Audit function (reporting to Thomas Anderson) samples 15 Normal and 5 Major RFCs per quarter. The sample tests for evidence of testing, rollback viability, and timely CMDB updates (target: 98% compliance). A report is submitted to the AI Governance Committee. | SOC 2 CC8.1, SR 11-7 |
| **CM-ADM-04** | **Vendor Change Governance:** Any change proposed by a third-party vendor (e.g., for managed SOC services) must be submitted via Meridian’s ServiceNow, not the vendor's ticketing system. The Meridian contract owner serves as the Change Owner. | SOC 2 CC9.2 |

### 6.2 Technical Controls

| Control ID | Control Description | Regulatory Mapping |
| :--- | :--- | :--- |
| **CM-TEC-01** | **Infrastructure as Code (IaC) Pipeline:** All AWS infrastructure changes must be defined in Terraform (v1.6+) and stored in the `meridian-iac` private GitLab repository. Manual clicks in the AWS Console to modify production are prohibited (IAM policy `DenyConsoleModifyProduction` enforces this, except for `break-glass` roles). | SOC 2 CC8.1, HIPAA 164.312(b) |
| **CM-TEC-02** | **CI/CD Immutable Artifacts:** Docker container images promoted to production via the `release-prod` pipeline in GitLab CI are tagged with a timestamp and commit SHA. The `latest` tag is prohibited in production Kubernetes manifests. The manifest change itself is a Normal Change. | SOC 2 CC8.1, NIST SP 800-190 |
| **CM-TEC-03** | **Production Push Validation (LangSmith):** For Clinical AI deployments, the model artifact must pass A/B safety checks in LangSmith. An automated guardrail checks for concept drift against the baseline model before traffic can be shifted in SageMaker. If the drift score exceeds 5%, the promotion is halted and a Manual CMB Review is triggered. | EU AI Act Art. 14, NIST AI RMF (MAP 3.4) |
| **CM-TEC-04** | **Database Change Locks (Redgate / Liquibase):** Schema changes to PostgreSQL databases containing ePHI are managed via Redgate Flyway. A deployment lock is automatically applied 15 minutes before the scheduled window. All interactive sessions from non-privileged accounts are terminated. | HIPAA 164.312(c)(2) |
| **CM-TEC-05** | **Immutable Audit Trail:** ServiceNow records are configured with HIPAA-audit flags. RFC records cannot be deleted by any user, including `admin`. Modifications to closed RFCs require an "RFC Correction" form, which is a new RFC subject to full review. Audit logs are streamed in real-time to an immutable Snowflake table. | SOC 2 CC8.1, HIPAA 164.312(b) |

### 6.3 Data Integrity Safeguards

Given the dual HIPAA/SOC 2 obligations, the following safeguards specifically protect ePHI during changes:

1.  **PHI-Aware Pipelines:** CI/CD pipelines for MedInsight and Clinical AI include a "PHI Masking" stage. Staging environments only use synthetic data generators or an obfuscated subset of production data. The use of raw production data in staging is a Major Change and requires a full DPIA.
2.  **Schema Change Verification:** Before a column is dropped or a data type changed in a PHI-laden table, the Change Implementer must run the `verify-no-orphan-data` script, the output of which is attached to the RFC. Failure to attach this output results in automatic CAB rejection.
3.  **Financial Hashing Verification:** For HealthPay, changes to the financial reconciliation service must pass a "Hash Matched" test, verifying that the SHA-256 of the daily transactions pre- and post-deployment are consistent unless the change explicitly alters encryption logic. (SR 11-7, Model Validation).

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The effectiveness of the Change Management process is continuously measured. The Change Manager is responsible for publishing a monthly "State of Changes" report.

| KPI Category | Metric | Target | Measurement Method |
| :--- | :--- | :--- | :--- |
| **Compliance** | Unauthorized Changes Detected | 0 per month | AWS CloudTrail / ServiceNow reconciliation script. A change record with a `start_time` but no corresponding `RFC` is flagged. |
| **Success Rate** | Failed Change Ratio | < 5% of all Normal/Major changes | (Number of changes resulting in a rollback or P1 incident within 24 hours) / (Total Changes * 100). |
| **Agility** | Average RFC Lead Time (Normal) | < 5 business days | Time from `RFC Submission` to `Approval` in ServiceNow. |
| **Emergency Discipline** | Emergency Change Ratio | < 10% of total monthly changes | (Emergency RFC count / Total RFC count * 100). A sustained spike >15% triggers a process root cause analysis. |
| **CMDB Health** | Timely CMDB Updates | 95% compliance | Daily scan: if a CI is modified but the linked RFC is not in `Closed` status within 4 hours. |
| **Clinical Governance** | Drift Detection Halts | Zero undetected drift | LangSmith pipeline gate activation log verification. |

### 7.2 Reporting Cadence

- **Weekly Operations Review:** The Change Manager presents the FSC for the upcoming week and highlights any emergency changes from the prior week to the VP of Engineering and VP of IT Operations.
- **Monthly Service Management Review:** The "State of Changes" report (Section 7.1) is distributed to all CAB members and the CISO. The report highlights trends, notable failures, and top RFC rejectors/reasons.
- **Quarterly Business Review (QBR):** The VP of IT Operations presents a summary to the Executive Leadership Team (Dr. Sarah Chen), focusing on change throughput, audit findings, and alignment between change velocity and business priorities.
- **Annual SOC 2 / HITRUST Audit:** The Change Manager compiles the full evidence package, including a 12-month log of all RFCs, a sample of CAB minutes for a selected month, and the list of all authorized approvers.

---

## 8. Exception Handling and Escalation

### 8.1 Requesting an Exception

Situations demanding a temporary or permanent deviation from this SOP must be managed via the formal Exception process, not bypassed informally.

1.  The requestor submits an "Exception Request" via ServiceNow (`MHT-RFC-EXCEPTION`), attaching a business justification, risk assessment, and proposed compensating controls.
2.  The request is routed to the Change Manager, who assigns a severity level (Minor, Major, Critical) based on the impact on SOC 2 controls or HIPAA safeguards.
3.  **Approval Workflow:**
    *   *Minor Exceptions* (e.g., extending the back-out window by 30 mins for a single weekend window): Approved by Change Manager + Security Assessor.
    *   *Major Exceptions* (e.g., bypassing staging environment testing for a hotfix): Approved by VP of IT Operations + CISO.
    *   *Critical Exceptions* (e.g., suspending a SOC 2 control for a legacy system migration): Approved by the Chief Compliance Officer, Thomas Anderson, and the General Counsel, Maria Gonzalez.
4.  Every exception has a strict expiry date, not exceeding 12 months. A renewal requires a new request and a PIR evaluating the efficacy of the compensating controls.

### 8.2 Escalation Path

In the event of a disagreement regarding change risk assessment or approval:

1.  **Technical Dispute:** Escalate from Change Manager -> TRB (Technical Review Board) -> VP of Engineering (David Park).
2.  **Risk / Compliance Dispute:** Escalate from CAB -> CISO (Rachel Kim) + Chief Compliance Officer (Thomas Anderson). Their joint decision is final.
3.  **Clinical Safety Dispute (Stop-the-Line Authority):** Any member of the Clinical Informatics team, or the Chief Medical Officer (Dr. Priya Patel), has the absolute authority to halt a change to the Clinical AI Platform or MedInsight if they suspect a patient safety risk. This "stop-the-line" halts the deployment immediately, regardless of approvals, and triggers an extraordinary CMB review within 24 hours.

---

## 9. Training Requirements

### 9.1 Role-Based Training

All individuals involved in the Change Management process must complete mandatory training appropriate to their role. Completion is tracked via the Meridian LMS (Workday Learning) and verified by the Change Manager before granting ServiceNow `change_*` roles.

| Module Code | Module Title | Target Audience | Frequency | Duration |
| :--- | :--- | :--- | :--- | :--- |
| **CHG-101** | Change Management Awareness & Your Role | All IT Staff, Contractors | Annually | 30 min |
| **CHG-201** | RFC Submission & Impact Analysis for Change Owners | All Change Owners, SW Engineers | Annually | 60 min |
| **CHG-301** | CAB Member, Approver, & Compliance Duties | All CAB Members, CISO Delegates, CMB Members | Semi-Annually | 90 min |
| **CHG-401** | Emergency Change & Incident Command | Incident Commanders, SRE Team | Semi-Annually | 45 min (Workshop format) |

### 9.2 Training Content Updates

The training curriculum owner (Michael Okonkwo, Change Manager) is responsible for reviewing and updating the training materials within 30 days of a Major version release of this SOP. For Version 2.8, the updated SOC 2 controls and Clinical Model Board sections must be incorporated into the CHG-301 and CHG-401 modules.

### 9.3 Non-Compliance

Personnel found to have implemented unauthorized changes, deliberately bypassed CAB approval, or falsified RFC data will have their production access immediately revoked by the CISO's office. A formal incident record will be created, and the matter will be referred to HR (Senior Director, Employee Relations) for disciplinary action, up to and including termination and notification to regulatory bodies if ePHI compromise is suspected.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies and SOPs

| Document ID | Document Title | Relationship to this SOP |
| :--- | :--- | :--- |
| **SOP-ISMS-001** | Information Security Management System (ISMS) Manual | Overarching security governance framework. |
| **SOP-CISO-002** | Vulnerability & Patch Management | Defines vulnerability SLAs that often drive Emergency Changes. |
| **SOP-CISO-008** | Cryptographic Key Management | Any change to HSMs or encryption keys references this SOP. |
| **SOP-ITOP-003** | Incident & Problem Management | Input source for Emergency Changes; output consumer of PIRs. |
| **SOP-ITOP-005** | Configuration & Asset Management (CMDB) | Specifies CI naming conventions and baseline reconciliation referenced in Section 5.6.5. |
| **SOP-ENG-002** | CI/CD Pipeline & Artifact Promotion | Technical implementation of code movement, to which the gates in this SOP align. |
| **SOP-CMB-001** | Clinical AI Model Governance | Detailed Clinical Model Board operating procedures, referenced for High-Risk AI Changes. |
| **SOP-PRI-001** | Data Classification & Handling | Defines the PHI, financial, and EU Personal Data tags used in the RFC process. |
| **POL-HR-015** | Acceptable Use Policy | Sets the behavioral expectation that unauthorized changes are a violation. |

### 10.2 External Standards & Regulatory References

| Standard / Regulation | Section / Article | Relevance to this SOP |
| :--- | :--- | :--- |
| **AICPA TSC (SOC 2)** | CC8.1 | The entity authorizes, designs, develops or acquires, configures, documents, tests, approves, and implements changes to infrastructure, data, software, and procedures to meet its objectives. (Thoroughly addressed in Sections 5.3, 5.5, 6.1, 6.2). |
| **AICPA TSC (SOC 2)** | CC7.1 / CC7.2 | Interface between Incident (Emergency) detection and Change Management response (Section 5.7). |
| **HIPAA Security Rule** | 45 CFR § 164.312(a)(1) | Access Control – Segregation of duties enforced by the change workflow (Section 6.1, CM-ADM-01). |
| **HIPAA Security Rule** | 45 CFR § 164.312(b) | Audit Controls – Immutable record of changes to systems containing ePHI (Section 6.2, CM-TEC-05). |
| **HIPAA Security Rule** | 45 CFR § 164.312(c)(2) | Integrity Controls – Mechanisms to authenticate ePHI during database changes (Section 6.3.2). |
| **EU AI Act** | Art. 14, Annex IV | Technical documentation for high-risk AI systems, including change logs and drift monitoring (Section 5.5.3, CM-TEC-03). |
| **FDA 21 CFR Part 820** | Subpart C - Design Controls | Post-market surveillance requirements for FDA-cleared imaging algorithms; change control documentation (Section 5.5.3). |
| **NIST AI RMF** | MAP 3.4 / GOVERN 1.3 | AI-specific change controls including fairness objectives and transparency logging (Section 4.6, 6.2). |
| **ISO 27001:2022** | A.8.32 | Operational change control (Alignment with Meridian’s ISMS). |

---

## 11. Revision History

| Version | Date | Author | Approver | Description of Changes |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 2021-02-15 | Michael Okonkwo | Samantha Torres | Initial creation and publication of SOP for IT Operations, separating Change Management from Incident Management. |
| 2.0 | 2022-10-01 | Michael Okonkwo | David Park | Major revision: Introduced Clinical Model Board (CMB) approval flow for FDA-cleared Clinical AI v2.0 launch. Added Annual Change Freeze Calendar. Updated to SOC 2 2022 TSC alignment. |
| 2.3 | 2023-07-18 | Sarah Jenkins (InfoSec GRC) | Rachel Kim | Strengthened segregation of duties controls (CM-ADM-01), defined the Immutable Audit Trail (CM-TEC-05), and integrated the GDPR DPIA requirement for EU-west-1 changes. |
| 2.6 | 2024-03-11 | Michael Okonkwo | Samantha Torres | Post-audit corrective action revision: Moved to 4-hour CMDB update SLA. Mandated LangSmith guardrails for AI drift detection. Refined the Major Change technical review board (TRB) requirement. Clarified the Stop-the-Line authority for Clinical Informatics. |
| 2.8 | 2025-05-21 | Michael Okonkwo, Dr. Aisha Okafor | David Park | Incorporation of EU AI Act High-Risk System mandate into CMB scope (Section 5.5.3 & Controls). Redgate database change lock enforcement. Updated annual change freeze dates for 2026 cycle. Added quarterly SOC 2 evidence package review by Internal Audit (Control CM-ADM-03). |

---

**End of Document - SOP-ITOP-001**