---
sop_id: "SOP-COPS-003"
title: "Support Ticket Management"
business_unit: "Customer Operations"
version: "5.9"
effective_date: "2025-03-28"
last_reviewed: "2026-11-14"
next_review: "2027-05-17"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Support Ticket Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the unified framework for managing all customer-initiated and internally-generated support tickets within Meridian Health Technologies, Inc. The purpose of this document is to ensure the consistent, traceable, and timely resolution of incidents, service requests, and inquiries across all four Meridian business lines: Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform. This SOP defines the complete ticket lifecycle—from intake and classification through resolution and closure—to maintain service quality, uphold contractual service level agreements (SLAs), and meet the availability and processing integrity criteria relevant to our SOC 2 Type II certification.

### 1.2 Scope

This SOP applies to:

- **All Personnel:** Full-time employees, contractors, and managed service providers within the Customer Operations, IT Operations, Engineering, Clinical AI Products, Financial Services, and MedInsight Analytics teams who handle, triage, escalate, or resolve support tickets.
- **All Systems:** The centralized service desk platform, Zendesk, which serves as the mandatory system of record for all customer-facing support interactions. Engineering-originated issues tracked in Jira Service Management must be linked to a parent Zendesk ticket when they are derived from a customer-reported issue.
- **All Ticket Types:** Incidents (unplanned service degradation or outage), Service Requests (standard pre-approved changes, access provisioning), Informational Inquiries, and Problem Investigations originating from external customers (hospitals, clinics, health systems, payers) or their designated authorized contacts.
- **All Environments:** Production, staging (pre-production validation), and customer-facing sandbox environments hosted on AWS (us-east-1, eu-west-1). Non-customer-facing internal development environments are explicitly excluded; issues therein are tracked via Jira under the purview of the Engineering DevOps playbook.

### 1.3 Exclusions

- Product defect tracking discovered internally before customer release (managed via Jira Engineering Backlog SOP-ENG-012).
- Formal data subject access requests under GDPR (managed via SOP-LEG-001, Privacy Request Handling).
- Employee internal IT issues (managed via SOP-IT-004, Internal IT Service Desk).

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **ACK** | Acknowledgement; the first response to a customer confirming receipt of their reported issue. |
| **Business Critical (TIER 1)** | A severity classification indicating a complete service outage affecting multiple customer organizations, or an incident that halts core clinical or financial workflows with no available workaround. |
| **Degraded (TIER 2)** | A severity classification indicating significant performance degradation or a feature outage where a manual, labor-intensive workaround exists. |
| **FRT** | First Response Time; the elapsed clock time between ticket submission and the first human (non-automated) acknowledgment sent to the customer. |
| **JIRA** | Jira Service Management, the Engineering-internal ticketing platform used for software defect and backlog management. All Jira tickets tied to a customer root cause MUST be linked via a Zendesk "Jira Link" field. |
| **MTTR** | Mean Time to Resolution; the average duration from ticket creation to formal resolution, tracked across a rolling 30-day window. |
| **OLA** | Operational Level Agreement; internal commitments between support tiers (e.g., Tier 2 to Engineering) that underpin external SLAs. |
| **PAR** | Periodic Access Review; a formal cadence-driven audit of logical access rights (see Section 8.3 for related process, though scheduling of reviews is not defined in this SOP). |
| **SLA** | Service Level Agreement; a contractual commitment to a customer specifying uptime targets, FRT, and Time to Resolution (TTR). |
| **TTR** | Time to Resolution; the total elapsed clock time from ticket creation until the ticket status is set to "Resolved" or "Closed." |
| **ZENDESK** | The Customer Operations service management platform, designated as the System of Record for all customer interactions, accessible via Meridian SSO. |

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

| Activity / Decision Point | Customer (External) | Tier 1 Support (CS-Ops) | Tier 2 Analyst | Tier 3 Engineering | VP, Customer Ops (Michael Chang) | VP, Product Eng. | VP, Financial Services (Robert Liu) |
|---|---|---|---|---|---|---|---|
| Ticket Submission | R, A | C | | | | | |
| Triage & Initial Classification | I | R, A | | | | | |
| Tier 2 Technical Troubleshooting | I | C | R, A | C | | | |
| Code Fix / Hotfix Deployment | | C | I | R, A | | C | |
| Sev 1 Escalation Approval | | I | I | I | A | R | C |
| SLA Extension / Exception | | C | C | C | R | | A |
| Ticket Closure | C | R, A | | | | | |
| Ticket Quality Audit (Retroactive) | | I | | | R, A | | |

- **Responsible (R):** The individual(s) who perform the work to achieve the task.
- **Accountable (A):** The single individual ultimately answerable for the correct and thorough completion of the task. Must sign off on exceptions.
- **Consulted (C):** Those whose opinions are sought, typically subject matter experts.
- **Informed (I):** Those kept up-to-date on progress, often after decisions or actions are taken.

### 3.2 Role Definitions

- **Tier 1 Support Agent (CS-Ops):** Handles initial intake, FR, categorization, basic known-error lookup, and password/multifactor authentication (MFA) reset requests. Empowered to resolve account-lock issues and route tickets per the standard playbook.
- **Tier 2 Support Analyst:** Performs deep technical troubleshooting, reviews audit logs via Sumo Logic, executes database read-only queries in production (via Snowflake Read-Only Role), triages network latency issues, and initiates pre-approved emergency change requests (ECRs).
- **Tier 3 Engineering / DevOps:** Possesses logical access privileges to modify production application code and infrastructure-as-code (Terraform). They execute hotfixes and coordinate patch deployment.
- **VP, Customer Operations (Michael Chang):** Owner of this SOP, accountable for global support KPIs, SLA adherence across all tiers, and approval of permanent exceptions.
- **VP, Financial Services (Robert Liu):** Approver of this SOP, specifically to ensure alignment with HealthPay contractual obligations and financial reporting integrity.

## 4. Policy Statements

1.  **System of Record:** Zendesk is the mandatory system of record for all customer-support interactions. No verbal, email, or chat-originated request shall be acted upon without an associated Zendesk ticket. This control supports the SOC 2 principles of security and availability.
2.  **No Ticket Left Unacknowledged:** Every properly submitted ticket shall receive an automated system acknowledgment immediately. A human-crafted, actionable acknowledgment (FR) must follow within the SLA-defined FRT window.
3.  **Logical Access Controls:** Access to Zendesk and linked backend diagnostic tools (Sumo Logic, Snowflake) is provisioned based on the principle of least privilege. Tier 1 agents possess “Viewer” access to dashboards but cannot modify Tier 2/3 ticket fields. Tier 2 analysts possess read-only access to production databases. Tier 3 engineers possess time-limited write privilege elevation via Azure AD Privileged Identity Management (PIM). All ticket access is authenticated via Meridian SSO with MFA enforced.
4.  **Data Privacy:** Protected Health Information (PHI) or Personally Identifiable Information (PII) shall not be logged in Zendesk public- or private-note fields. The Zendesk instance is configured with field-level encryption for specific text fields identified in HIPAA Security Rule assessments.
5.  **Incident-Driven Response:** A ticket classified as a "Major Incident" (TIER 1) shall immediately invoke the Major Incident Management process (see Section 8.2). The Incident Commander is authorized to assemble a dedicated Slack channel (`#se-critical-<ticketID>`) and engage on-call resources, bypassing standard OLA timers.

## 5. Detailed Procedures

This section outlines the step-by-step lifecycle of a support ticket. Each agent must follow the procedures in sequence unless an emergency expedited process is invoked per Section 8.

### 5.1 Ticket Intake and Creation

Intake channels include the Meridian Customer Portal (powered by Zendesk Guide), an API endpoint for automated monitoring alerts from Datadog, and a direct email intake (`support@meridianhealthtech.com`). Inbound phone calls documented at initial contact must have a ticket created by the receiving agent.

1.  **Automated Inbound Processing:** Zendesk processes the inbound email or API POST. The system auto-populates the `Contact` record, sets status to `New`, and parses the `Subject` line.
2.  **Manual Intake (Phone/Walk-in):** The Tier 1 agent navigates to the Zendesk Agent Workspace and clicks `+ Add Ticket`. The agent must:
    - Search and select the correct `Requester` (Contact record). Strictly no anonymous tickets.
    - Select the `Brand`: `Clinical AI`, `HealthPay Financial`, `MedInsight`, or `Meridian SaaS Platform`.
    - Populate the `Subject` line using the standard convention: `[Feature-Area]: Concise error description`.
    - Record the verbatim customer description in the `Description` field.

### 5.2 Triage and Classification (Tier 1)

Upon creation, the ticket status automatically transitions to `Open`. The Tier 1 Triage Agent performs the following sequence within 15 minutes of receipt:

1.  **Validate Contact:** Verify the requester is an active authorized contact in the `Customer` Zendesk organization. If not, immediately assign the ticket to the `Account Management Queue` and do not proceed further.
2.  **Screen for Duplication:** Use Zendesk’s "Similar Articles & Tickets" sidebar widget to identify potential duplicates. If a duplicated issue is confirmed, link the new ticket as `Incident/Problem is caused by` the parent ticket and set status to `Closed (Duplicated)`.
3.  **Assign Severity Level:** Classify the issue per the matrix defined in Table 5.3-A. If insufficient information exists to classify definitively, default to **TIER 2** (Degraded) as a precautionary measure.
4.  **Set Priority & Route:**
    - TIER 1 (Critical): Assign to `Tier 3 - On Call Queue`. Immediately trigger Major Incident Playbook (Section 8.2).
    - TIER 2 (Degraded): Assign to `Tier 2 - Technical Analysis Queue`.
    - TIER 3 (Standard/Minor): Assign to `Tier 2 - Service Request Queue`.

**Table 5.3-A: Severity Classification Matrix**

| Severity | Definition | Example Triggers | Initial Queue Target |
|---|---|---|---|
| **TIER 1 - Business Critical** | Service is down or a critical function is unavailable across multiple customer organizations. No procedural workaround exists. The incident affects data integrity or patient safety. | - Clinical AI inference endpoint returning HTTP 503 across all regions.<br>- Customers unable to process payment batches in HealthPay.<br>- Data breach suspected. | `Tier 3 - On Call Queue` |
| **TIER 2 - Degraded** | Major feature is unavailable or performance is severely degraded. A procedural (manual) workaround exists but is commercially impractical at scale. | - Report generation in MedInsight is failing, but users can query the raw Snowflake view manually.<br>- Timeout errors on 20% of Clinical AI API calls. | `Tier 2 - Technical Analysis Queue` |
| **TIER 3 - Standard** | Partial, non-critical loss of functionality. User experience impaired but core business operations are functional. | - Dashboard widget fails to render; underlying data accessible via direct report.<br>- Single user locked out of their MFA device. | `Tier 2 - Service Request Queue` |
| **TIER 4 - Inquiry** | General questions, documentation clarifications, feature usage queries. | - "How do I export a custom cohort?"<br>- "Please provide a link to the MDR change log." | `Tier 1 - General Queue` |

5.  **Perform First Response (FR):** The Tier 1 agent sends a personalized response using a macro as the base, confirming the reported symptom, stated severity, assigned ticket number, and next expected step timeline. The macro `FR_Tier2_General` or `FR_Tier1_Critical` should be used, but the output MUST be edited to reflect the specific content of the customer's ticket. The FR is recorded as the first public comment in the ticket timeline.

### 5.3 Technical Investigation and Resolution (Tier 2)

When a ticket enters a Tier 2 Analyst queue, the status automatically shifts to `Awaiting Support` via a Zendesk trigger.

1.  **Assign Owner:** A Tier 2 Team Lead must manually assign the ticket to a specific analyst. Unassigned tickets age out and trigger a "Stale Ticket" escalation alert to the `#cs-tier2-leads` Slack channel after 30 minutes.
2.  **Diagnostic Execution:** The assigned analyst initiates diagnostic procedures:
    - **Log Analysis:** Query the Meridian Log Aggregator (Sumo Logic) using the specific `trace.id` or `session.id` provided by the customer. The analyst must use the saved “Tier 2 - PHI Redaction” search library to avoid exposing raw PII/PHI in log streams.
    - **Database Review:** For MedInsight or HealthPay data integrity queries, execute read-only SQL queries against the `ANALYTICS_REPORTING` Snowflake shared view. Queries must adhere strictly to the pre-approved `Meridian_Tier2_Analyst_ReadOnly` query library. No ad-hoc `SELECT *` queries are permitted.
    - **Configuration Audit:** Check the Meridian Launchpad configuration against the customer’s baseline using the Terraform Cloud state output (read-only access).
3.  **Root Cause Analysis (RCA):** Document the probable root cause in the internal "RCA Field" on the Zendesk ticket sidebar. If the RCA points to a software defect, proceed to Section 5.4.
4.  **Propose and Execute Resolution:**
    - *Standard Changes:* Execute pre-approved Standard Change procedures (e.g., restarting a pod, clearing a Redis cache key via read-only tools). Log the change record ID in the ticket.
    - *Emergency Changes:* If a non-standard action is required (e.g., manual database update, IAM role modification), draft an Emergency Change Request (ECR) in Jira Service Management using the template `ECR_Template_Meridian`. The ECR must be linked to the Zendesk ticket, approved in Jira by an on-call Engineering manager, and executed *only* after approval.
5.  **Resolution Code Assignment:** Before resolution, the analyst sets the `Resolution_Code` field from the dropdown list:

| Code | Description | Example |
|---|---|---|
| `CONFIG_FIX` | A non-code configuration change resolved the issue. | Reverted a misconfigured feature flag in Launchpad. |
| `DATA_FIX` | Inaccurate data was corrected via ETL re-run or manual SQL. | Reprocessed payment batch `HEALTHPAY-987` due to FX conversion error. |
| `DOC_BUG` | Customer error due to erroneous or unclear documentation. | README incorrectly stated format for API date header. |
| `KNOWN_ERR` | Issue matched a published Known Error Article in the Zendesk Guide. | "Error Code 4512" Article linked in resolution notes. |
| `SOFTWARE_BUG` | Issue was a software defect requiring a code fix. | `#T3-Patch` Jira issue `MER-9876` linked for hotfix deployment. |
| `WORKAROUND` | Permanent fix is deferred; a commercially reasonable workaround was provided. | Provided manual bulk-billing import script while UI fix is in sprint. |

### 5.4 Engineering Handoff (Tier 3)

This procedure is invoked when the Resolution Code is `SOFTWARE_BUG` and the resolution is beyond the Tier 2 analyst’s authority or tools.

1.  **Create Jira Issue:** From the Zendesk ticket sidebar, click “Create Jira Issue.” Map the fields:
    - *Project:* `MER` (Meridian Core Product)
    - *Issue Type:* `Bug`
    - *Summary:* Auto-populated from Zendesk.
    - *Severity:* Mirrors Zendesk Priority (Critical/Major/Minor).
    - *Environment:* `us-east-1-prod`, `eu-west-1-prod`.
    - *Linked Zendesk Ticket:* Auto-populated.
2.  **Triage Bridge:** The Jira issue enters the Engineering `Triage (MER)` Kanban. A weekly triage meeting prioritizes bugs with “Critical” severity for the current or next sprint.
3.  **Code Fix Cycle:** The assigned engineer branches from `main`, develops the fix, commits with the linked Jira key, initiates a pull request (PR), undergoes peer review, and merges the PR upon approval. The CI/CD pipeline (Azure DevOps) deploys the artifact to the Stage environment.
4.  **Validation:** The Customer Operations QA team (a subsection of CS-Ops) validates the fix against the original reproduction steps in the `stage` environment. Upon successful validation, the Tier 2 Analyst updates the Zendesk ticket with "Fix validated in stage, scheduled for production deployment in next release window."
5.  **Production Deployment:** The on-call DevOps engineer executes the production deployment runbook via Terraform Cloud. A production runbook log is auto-attached to the Jira issue.

### 5.5 SLA Tracking and Monitoring

SLA tracking is automated through Zendesk Explore. The calculation of business hours for SLAs is based on the customer's contractual calendar, defaulting to **24x7** for all TIER 1 Clinical AI and HealthPay issues, and **8x5 (US Eastern Time)** for MedInsight Standard Tier.

1.  **SLA Clock Pause Rules:** The SLA clock pauses only when the ticket status is set to `Awaiting Customer`. Statuses of `Awaiting Engineering` or `Awaiting Vendor` are counted against our internal OLA but do NOT pause the external customer SLA clock unless explicitly communicated and acknowledged (ACK) via a customer statement "Acceptance of Delay" recorded in the public ticket comments.
2.  **SLA Breach Warning:** At 80% of the target TTR, Zendesk triggers an audible and visual alarm in the Agent Workspace. At 95%, the ticket is auto-flagged and a Slack notification is posted to `#cs-tier2-alerts`.
3.  **SLA Breach Escalation:** A breached ticket is marked with a red violation flag in the dashboard. An automated escalation email is sent to the VP of Customer Operations. The assigned agent must draft a post-mortem summary within the ticket within 4 business hours.

**Table 5.5-A: Target SLA Matrix (Default)**

| Metric | TIER 1 (Critical) | TIER 2 (Degraded) | TIER 3 (Standard) | TIER 4 (Inquiry) |
|---|---|---|---|---|
| **First Response Time (FRT)** | 1 hour | 4 hours | 8 business hours | 2 business days |
| **Time to Resolution (TTR)** | 8 hours | 3 business days | 10 business days | 15 business days |

### 5.6 Ticket Resolution and Closure

1.  **Provide Resolution Summary:** The ticket assignee posts a final public comment summarizing:
    - Root cause (in non-technical, plain language).
    - Action taken to resolve (e.g., "Deployed hotfix MER-9987 to patch the memory overflow issue").
    - Steps taken to prevent recurrence (e.g., "Added monitoring alert for memory usage threshold").
2.  **Set Status to `Resolved`:** The agent sets the status. The Zendesk ticket `Resolution` field is set to the chosen code. SLA timer stops.
3.  **Automated Customer Satisfaction Survey:** Zendesk automatically dispatches a CSAT survey (Good/Satisfactory/Bad) for TIER 2 and TIER 3 requests.
4.  **Closure Window:** The ticket remains in `Resolved` state for 72 hours (3 days). During this window, the customer can re-open the ticket with a single reply. If no reply is received, the system automatically transitions the ticket to `Closed`. Support agents are prohibited from manually overriding `Closed` to `Resolved`; a new ticket must be created and linked to the old one.

## 6. Controls and Safeguards

### 6.1 Logical Access Controls

- **Identity Provider:** All access to Zendesk, Sumo Logic, and Snowflake is federated through Azure Active Directory (Azure AD) SSO, with Multi-Factor Authentication (MFA) enforced via Conditional Access Policy `CA-Support-Apps-MFA`.
- **Role-Based Access (RBAC):**
    - *Zendesk:* Granular permissions configured via custom roles (`CS-Ops-T1`, `CS-Analyst-T2`, `CS-Lead`, `Admin`). T2 analysts cannot modify triggers, automations, or business rules.
    - *Sumo Logic:* Tier 2 holds Role `SumoAnalyst_T2` allowing search on `prod-*` indices but with a redaction policy masking PCI/HIPAA-sensitive fields.
    - *AWS Console:* Direct console access is denied to support personnel. All read-only actions proceed via a Snowflake connector proxy.
- **Access Provisioning:** Requests for access are managed via a ticket against SOP-IT-004. Provisioning executes via Terraform-managed AD Group assignments.

### 6.2 Incident Response Integration

- A Major Incident declared per this SOP invokes the formal incident response procedures outlined in **SOP-SEC-001 (Information Security Incident Response Plan)**.
- Tabletop exercises are not scheduled within the scope of this Customer Operations SOP; coordination for enterprise-wide simulation, if required, falls under the purview of the CISO per SOP-SEC-001.

### 6.3 Data Integrity Safeguards

- **Audit Trail:** Every Zendesk ticket event (creation, assignment, public comment, state change) generates an immutable audit log entry, synchronized hourly to the `meridian_compliance.soc2_ticket_audit` Snowflake table for long-term archiving.
- **Egress Filtering:** The Zendesk API is configured via whitelist to only accept requests from the Meridian corporate IP range and approved third-party plugin sources (e.g., Jira Service Management native connector).

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The Customer Operations unit is measured against the following service quality and efficiency metrics, displayed via the real-time Zendesk Explore dashboard `COPS_Executive_Dashboard`.

| Metric Category | KPI Definition | Target | Monitoring Cadence |
|---|---|---|---|
| **Service Level** | SLA Adherence Rate (Tier 1-3) | ≥ 99.5% Monthly (Critical), ≥ 95% (Degraded) | Weekly Review |
| **Responsiveness** | Mean FRT (All Tiers) | < 2 hours (Critical), < 12 hours (Standard) | Daily Snapshot |
| **Productivity** | Ticket Volume per Tier 1 Agent | ≥ 25 tickets per week | Bi-Weekly |
| **Effectiveness** | Tickets Resolved within Target TTR | 90% | Monthly Ops Review |
| **Quality** | CSAT Score (Avg) | ≥ 4.5 / 5.0 | Weekly QA Scoring |

### 7.2 Ticket Quality Audits

The Customer Operations QA Lead conducts a weekly random audit of 5% of tickets closed in the previous rolling seven days. The audit is scored against a rubric based on: (1) Accurate Severity Classification, (2) Adherence to FR procedure, (3) Clear, non-jargon resolution summary, (4) Correct resolution code assignment. Scores are logged in the Zendesk QA (Klaus) integration. Consecutive audit failures trigger a retraining requirement per Section 9.

### 7.3 Reporting

- **Daily Snapshots:** A fully automated Zendesk Explore dashboard is reviewed by the Shift Lead at the start of each working block.
- **Weekly Operations Review:** Michael Chang (VP CS-Ops) receives a PDF Summary Report auto-exported from Zendesk every Monday at 08:00 EST, including high-age tickets (>5 days open) and a top-ten list of recurring issue codes.
- **Monthly Business Review (MBR):** A consolidated report containing MTTR, CSAT scores, and tier-split volume is presented to Robert Liu (VP Financial Services) for the financial product lines, analyzing the support cost-to-revenue ratio for HealthPay.

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Handling

Exceptions to the standard procedures defined herein (e.g., a request to bypass Tier 2 and directly hand-off to Engineering for a non-critical issue) must be authorized.

1.  **Document Request:** The requesting person adds an internal note "EXCEPTION REQUEST" detailing the procedure step being bypassed and the justification.
2.  **VP/Designate Approval:** An exception for priority routing requires the approval of the Customer Operations Shift Lead. An exception for an SLA commitment pause requires the VP, Customer Operations (or delegate, Director level or above). Approval is denoted in a subsequent internal note.
3.  **Flagging:** The ticket is tagged with the `exception-approved` Zendesk ticket tag. A monthly audit of tickets carrying this tag is reviewed by the VP of Customer Operations.

### 8.2 Escalation (Major Incident)

Functional or hierarchical escalation triggers are strictly defined.

- **Functional Escalation (Technical):** When a Tier 2 analyst hits a 2-hour troubleshooting wall, the ticket is escalated to `Tier 3 - Engineering Funnel`. This is a “warm handover” and must be accompanied by a documented handover note summarizing the technical bridge-up.
- **Hierarchical Escalation (Management):**
    - **Step 1:** Customer requests manager via ticket reply. Zendesk trigger alerts via Slack `#cs-management-escalation`.
    - **Step 2:** Tier 2 Team Lead assumes ownership and provides a management bridge.
    - **Step 3:** If the customer is unsatisfied, the ticket is assigned to Michael Chang, VP, Customer Operations, for direct executive engagement.

### 8.3 Periodic Access Reviews (Exception)

In accordance with SOC 2 logical access control requirements, a manual procedural guideline exists to review Zendesk and Sumo Logic user lists to ensure terminated employees are removed and permissions remain aligned with roles. Access review activities are performed on an ad-hoc basis during internal audit preparation or when a significant access-related incident occurs.

## 9. Training Requirements

### 9.1 Initial Onboarding

All new support staff must complete the following within their first week of employment, prior to being granted unescorted access to production tickets:

- **SOP-COPS-003-OL (Online Course):** A two-hour video-based micro-learning covering the full ticket lifecycle, accessible via Workday Learning.
- **Knowledge Check:** A 30-question multiple-choice exam with a mandatory 90% passing score. The exam focuses on Severity Classification, SLA targets, and PHI/PII redaction rules.
- **Simulated Ticket Lab:** An instructor-led session using the Zendesk Sandbox environment where agents handle three scripted, realistic scenarios (one TIER 2 Degraded, one TIER 4 Inquiry, one Irate Customer Escalation).

### 9.2 Ongoing Refresher Training

- **Quarterly "Lunch & Learn":** The CS-Ops team conducts a mandatory 60-minute session reviewing 2-3 complex resolved tickets from the prior quarter.
- **SLA Breach Remediation:** Any agent who individually causes an SLA breach due to procedural error (not a force majeure event) is assigned a micro-course “SLA Clock Management” within Workday, to be completed within 5 business days.

### 9.3 Training Records

Completion records are automatically logged in the individual’s Workday profile. The VP, Customer Operations reviews a compliance report of all team training statuses quarterly. An agent with delinquent training is restricted from Tier 2 queue assignments until the requirements are fulfilled.

## 10. Related Policies and References

| Reference ID | Document Title | Relationship |
|---|---|---|
| **SOP-SEC-001** | Information Security Incident Response Plan | Major Incident escalation invokes IRP. |
| **SOP-IT-004** | Internal IT Service Desk | User access and hardware provisioning for agents. |
| **SOP-ENG-012** | Engineering Defect and Backlog Management | Defines the downstream Jira workflow for bugs created from Zendesk. |
| **SOP-LEG-001** | Privacy Request Handling (GDPR/CCPA) | Process for identifying and routing Data Subject Access Requests (DSARs) mistakenly submitted to Support. |
| **MSA-001** | Master Services Agreement (Template) | Base contractual obligation for SLA commitments and definitions. |
| **SEC-CONTROLS-005** | Logical Access Control Standard | Details of Azure AD role assignment and PIM elevation, referenced by Section 6.1. |

## 11. Revision History

| Version | Date | Author(s) | Description of Changes |
|---|---|---|---|
| 5.9 | 2025-03-28 | M. Chang, A. Gutierrez | Major update: Consolidated SLA matrix; Updated Triage classification to reflect new HealthPay release; Updated Section 8 for hierarchical escalation path due to organizational realignment. |
| 5.8 | 2024-11-15 | A. Gutierrez | Updated Section 5.4 Engineering Handoff to incorporate Azure DevOps CI/CD pipeline replacing Jenkins. Updated related documentation links. |
| 5.7 | 2024-06-10 | M. Chang, P. Okafor | Revised KPIs in Section 7.1 to reflect new 24x7 Clinical AI contractual obligations. Introduced TIER 1 classification granularity. |
| 5.5 | 2023-09-05 | A. Gutierrez | Introduced Sumo Logic diagnostic procedures (Section 5.3). Removed legacy BMC Remedy references. |
| 5.2 | 2023-02-20 | M. Chang | Annual SOP review. Refined Resolution Codes (Table added). Aligned roles with new org chart. |