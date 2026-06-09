---
sop_id: "SOP-LEGC-010"
title: "Policy Lifecycle Management"
business_unit: "Legal & Compliance"
version: "1.9"
effective_date: "2024-12-03"
last_reviewed: "2025-12-13"
next_review: "2026-06-03"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Policy Lifecycle Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the standardized framework for the creation, review, approval, version control, distribution, attestation, maintenance, and archival of all corporate policies, standards, and standard operating procedures at Meridian Health Technologies, Inc. The purpose of this framework is to ensure that all governing documentation is developed, maintained, and enforced in a consistent manner that meets or exceeds the requirements set forth by applicable regulations, including the Health Insurance Portability and Accountability Act (HIPAA), the General Data Protection Regulation (GDPR), the EU Artificial Intelligence Act (EU AI Act), and the voluntary frameworks of NIST AI RMF 1.0 and the Trust Services Criteria (TSC) for SOC 2 Type II certification.

The Policy Lifecycle Management program is designed to translate regulatory obligation and organizational risk appetite into actionable, auditable, and enforceable directives. This SOP serves as the meta-policy governing all other Meridian Health Technologies policies, ensuring a continuous improvement loop that reflects changes in the business environment, technology stack, threat landscape, and legal mandate.

### 1.2 Scope

This SOP applies to all policies, standards, and procedures authored by any department, business unit, or subsidiary of Meridian Health Technologies, Inc. This includes, but is not limited to, policies governing the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, the Meridian SaaS Platform, and all internal administrative functions.

The scope encompasses all documentation classified as "Internal," "Confidential," or "Public" within the Meridian policy hierarchy. It applies to all full-time employees, part-time employees, independent contractors, consultants, Board members, and third-party vendors who are required to adhere to or are governed by Meridian’s corporate policy library.

Explicitly, this SOP covers the lifecycle of documents from initial concept to final archival, including:
- The identification of a need for a new policy or a change to an existing one.
- The drafting, collaboration, and formatting of the document.
- The formal review and approval workflow.
- The publication and communication to the impacted population.
- The active acknowledgment and attestation of understanding.
- The cyclical, event-driven, and continuous review processes.
- The exception handling and waiver process.
- The enforcement and violation management.
- The final archival and destruction.

This SOP does not cover the creation of technical engineering runbooks, non-governance-related project charters, or individual job descriptions, though these documents must align with the policies governed by this SOP.

### 1.3 Policy Hierarchy

Meridian Health Technologies maintains a three-tiered governance structure. All documents in this structure are subject to the lifecycle controls in this SOP.

| Tier | Document Type | Description | Example | Max. Review Cycle |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | **Policy** | High-level, principle-based mandates reflecting management's intent and regulatory requirements. Set the "what" and "why." | Information Security Policy (SOP-ISMS-001), Data Classification & Handling Policy (SOP-DLP-005) | 12 months |
| **Tier 2** | **Standard** | Specific, measurable, mandatory controls and technical specifications that support Tier 1 policies. Set the "how much." | Encryption Standard (STD-ISMS-015), Access Control Standard (STD-ISMS-010) | 12 months |
| **Tier 3** | **Procedure (SOP)** | Detailed, step-by-step operational instructions to implement Tier 1 and 2 requirements. Set the "how." | Policy Lifecycle Management (SOP-LEGC-010), Vendor Risk Assessment Procedure (SOP-VRM-020) | 12 months |

## 2. Definitions and Acronyms

### 2.1 Definitions

- **Attestation:** The formal process by which an individual affirms, with a digital signature, that they have read, understood, and agree to comply with a specific policy or set of policies. Attestation creates an auditable, non-repudiable record.
- **Policy Author:** The individual or group designated with the responsibility for drafting or significantly revising a policy document. Typically a subject matter expert within the owning business unit.
- **Policy Owner:** The named executive or senior leader (VP or above) who is ultimately accountable for the content, accuracy, enforcement, and lifecycle management of a specific policy. The Owner is a role defined in Section 3 of this SOP.
- **Policy Steward:** The operational role, typically held by a member of the Legal & Compliance department, responsible for facilitating the lifecycle process, interpreting framework requirements, maintaining the central policy library, and tracking metrics. The Steward acts as an advisor and administrator, not a content owner.
- **Policy Library:** The centralized, access-controlled repository of record for all current, draft, and archived policies and their associated metadata, housed within the **ServiceNow GRC Policy and Compliance Management module**.
- **Trigger Event:** A significant internal or external occurrence that necessitates an immediate, out-of-cycle review of a policy. Examples include a material data breach, a major regulatory update (e.g., a new EU AI Act Annex), a significant merger or acquisition, or the introduction of a new core technology platform.
- **Zero-Day Policy:** An emergency policy or amendment enacted in response to an active, critical threat or legal imperative, requiring an expedited approval and deployment process outside the standard cycle.

### 2.2 Acronyms

| Acronym | Definition |
| :--- | :--- |
| BAA | Business Associate Agreement |
| CCPA | California Consumer Privacy Act |
| CCO | Chief Compliance Officer |
| CIO | Chief Information Officer |
| CISO | Chief Information Security Officer |
| CPO/DPO | Chief Privacy Officer / Data Protection Officer |
| DPIA | Data Protection Impact Assessment |
| EEA | European Economic Area |
| EU AI Act | European Union Artificial Intelligence Act (Regulation 2024/1689) |
| GDPR | General Data Protection Regulation (EU) 2016/679 |
| GRC | Governance, Risk, and Compliance |
| HIPAA | Health Insurance Portability and Accountability Act of 1996 |
| HR | Human Resources |
| KPI | Key Performance Indicator |
| NIST AI RMF | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework 1.0 |
| OCR | Office for Civil Rights (U.S. Department of Health and Human Services) |
| PHI | Protected Health Information |
| RACI | Responsible, Accountable, Consulted, Informed |
| SOC 2 | System and Organization Controls 2 |
| TSC | Trust Services Criteria (as defined by AICPA for SOC 2) |
| VP | Vice President |

## 3. Roles and Responsibilities

A RACI matrix provides a high-level view of accountability. A detailed narrative follows for each named role, with specific regulatory implications.

| Activity / Decision | Policy Author (SME) | Policy Steward (Compliance) | Policy Owner (VP+) | Approver (e.g., GC, CCO) | Legal | CISO / CPO |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Initiation & Drafting** | R | C | A | I | C | C |
| **Regulatory Alignment Review** | C | R | I | A | C-I (GDPR/HIPAA) | C-I (Security/Privacy) |
| **Cross-Functional Stakeholder Review** | C | R | A | I | R | R |
| **Final Content Approval** | I | R | A | R | I | I |
| **Publication & Communication** | I | R | A | I | I | I |
| **Attestation Campaign Management** | I | R | I | I | I | I |
| **Exception Handling** | C | R | C | A | C | C |
| **Periodic Review & Recertification** | R | A | R | I | I | I |

### 3.1 Policy Owner (Accountable)

The Policy Owner is a senior leader (VP or above) with the organizational authority and budget to enforce the policy. Responsibilities include:
- **Strategic Alignment:** Ensures the policy supports business objectives and is aligned with the risk appetite set by the Board.
- **Resourcing:** Allocates necessary resources for policy development, implementation, and enforcement.
- **Recertification:** Formally recertifies the policy’s continued accuracy and necessity during each review cycle. This includes a written attestation appended to the policy record in ServiceNow.
- **Accountability for Enforcement:** Holds ultimate responsibility for ensuring the policy is enforced within their business unit(s), including the application of disciplinary measures as defined by SOP-HR-105 (Employee Relations and Disciplinary Action). For HIPAA, the Owner is accountable for defining appropriate sanctions for non-compliance as required by 45 CFR § 164.308(a)(1)(ii)(C). For GDPR, they support the DPO in demonstrating accountability per Art. 5(2).

### 3.2 Policy Steward (Responsible for Process)

The Policy Steward is a designated member of the Legal & Compliance team, ultimately reporting to Thomas Anderson, Chief Compliance Officer. The Steward is the operational engine of the lifecycle. Responsibilities include:
- **Program Management:** Manages the central review calendar, triggers all review activities, and organizes meetings.
- **Gatekeeper of the Library:** Maintains the integrity of the central policy library in ServiceNow. Only the Steward or a designated administrator can publish a document from "Draft" to "Published" status.
- **Quality Assurance (QA):** Performs a QA check on all documents before they enter formal review. The QA checks for proper formatting (as per this SOP), style guide compliance, versioning, and metadata completeness. The Steward does not QA content, only governance requirements.
- **Metric Tracking:** Tracks and reports on all KPIs outlined in Section 7, including attestation completion rates, on-time review percentages, and exception aging.
- **Training:** Provides initial and refresher training to all Policy Authors and Owners on this SOP.

### 3.3 Policy Author (Responsible for Content)

The Author is the subject matter expert (SME) who performs the actual writing and revision. Responsibilities include:
- **Research & Drafting:** Creates the initial draft and subsequent revisions using the approved **Policy Document Template (TEMPLATE-LEGC-010_Rev4.docx)** housed on the Legal & Compliance SharePoint site.
- **Technical Accuracy:** Ensures all technical controls, procedural steps, and references are correct and feasible within the current Meridian technology stack (AWS, Snowflake, Okta, etc.).
- **Incorporation of Feedback:** Integrates all feedback from the Steward, CISO, CPO/DPO, Legal, and other stakeholders.
- **Content Recertification:** Assists the Policy Owner in the recertification process by providing evidence of the policy's continued accuracy.

### 3.4 Approver

The Approver is the final authority for policy enactment, typically Maria Gonzalez, General Counsel, or Thomas Anderson, Chief Compliance Officer, depending on the policy domain. The Approver signs off to confirm that the policy aligns with all applicable laws, regulations (SOC 2 TSC, HIPAA, GDPR), and Meridian’s Code of Ethics. This role is the final control point for legal and regulatory risk.

### 3.5 Legal, CISO, and CPO/DPO (Consulted)

These roles are mandatory, non-negotiable consultants in the policy lifecycle.
- **General Counsel (Maria Gonzalez):** Must be consulted on all policies that could have contractual, litigation, or corporate law implications.
- **CISO (Rachel Kim):** Must be consulted on any policy, standard, or procedure that impacts the confidentiality, integrity, or availability of information systems and data. This is a direct requirement of the SOC 2 TSC for Control Environment (CC1.2). For policies touching PHI, this consultation fulfills the HIPAA Security Rule requirement at 45 CFR § 164.308(a)(2) for a security official.
- **CPO/DPO (Dr. Klaus Weber):** Must be consulted on any policy that impacts the processing of personal data, per GDPR Art. 39. For any policy involving processing that is likely to result in a high risk, the DPO's opinion on a mandatory DPIA must be sought and documented. This includes MedInsight Analytics policies and HealthPay models.

## 4. Policy Statements

Meridian Health Technologies, Inc. commits to the following high-level policy statements, which govern the operations defined in this SOP:

4.1 **Single Source of Truth:** The ServiceNow GRC Policy and Compliance Management module shall be the single, authoritative source of truth for all active, draft, and archived Meridian governance documents. No other ad-hoc repositories (e.g., SharePoint folders, shared drives, Confluence spaces) may be used to store the official record, though they may contain working drafts that are explicitly watermarked as "DRAFT - UNOFFICIAL COPY."

4.2 **Mandatory Review Cycle:** All Tier 1, 2, and 3 documents shall undergo a full recertification and review by the Policy Owner and Policy Steward no less than annually from their effective date. A policy whose annual review is more than 30 calendar days past due is automatically rescinded and removed from the active library until recertified.

4.3 **Attestation as a Control:** Attestation is a primary administrative control to ensure awareness and accountability. Failure to complete mandatory attestation within the specified timeframe is considered a violation of this SOP and will be treated as an indicator of non-compliance, triggering a notification to the individual’s manager and HR, as per SOP-HR-105.

4.4 **Risk-Based and Regulation-Driven Approach:** Policies shall be created and revised based on a formal risk assessment process and a continuous regulatory monitoring program, not on an ad-hoc basis. The Compliance team's annual risk assessment directly informs the policy creation and revision schedule for the following fiscal year.

4.5 **Transparent Exception Management:** A formal, audited exception process exists for instances where strict compliance is operationally prohibitive. No policy is to be knowingly violated. All exceptions must be formally requested, risk-assessed, time-bound, and approved.

## 5. Detailed Procedures

This section outlines the step-by-step operating procedures for the five core phases of the policy lifecycle. All steps are tracked within the ServiceNow GRC module.

### 5.1 Phase 1: Policy Creation and Authoring

This phase is triggered by the identification of a new regulatory or business requirement, an audit finding, or a material change in risk profile.

**Step 1.1: Request Intake and Scoping**
- **Action:** Any employee or stakeholder can initiate a request for a new policy by submitting a "Policy Change Request" (PCR) via the ServiceNow GRC Service Catalog.
- **Triage:** The Policy Steward reviews the PCR within 5 business days. The Steward schedules a scoping meeting with the requestor and the prospective Policy Owner to validate the need.
- **Outcome:** If approved, the Steward assigns the PCR, officially designates the Policy Author(s), and creates a new draft record in the ServiceNow Policy Library. The record includes pre-populated metadata fields: `sop_id`, `title`, `business_unit`, `version` (set to 0.1 draft), and `status` (set to "Drafting").

**Step 1.2: Authoring and Initial Draft**
- **Action:** The Policy Author downloads the latest **Policy Document Template (TEMPLATE-LEGC-010_Rev4.docx)** . They draft the policy content, guided by the scope outlined in the PCR. The Author is responsible for ensuring all "THOROUGH" requirements for SOC 2, HIPAA, and GDPR are addressed with specific, auditable controls, not just principle statements.

**Step 1.3: Initial QA Check (Governance Gate)**
- **Action:** The Author submits the completed draft to the Policy Steward. The Steward performs the initial QA check against the following gate criteria:
    1.  Template formatting and metadata (YAML frontmatter) are correct.
    2.  Sections 1-11 are present as required by this SOP.
    3.  The regulatory mapping table (see Section 6.5) is completed and accurate.
    4.  A draft RACI for the new policy's subject matter is included in Section 3.
    5.  Specific, named roles (e.g., "VP of IT Operations") are referenced instead of generic titles (e.g., "IT Staff").
- **Gate Decision:** If the draft fails QA, it is returned to the Author via ServiceNow with specific feedback. If it passes, the Steward changes the status to "In Review" and initiates the formal review workflow.

### 5.2 Phase 2: Multidisciplinary Review and Approval

This phase ensures that the policy is feasible, technically accurate, and legally sound. The Policy Steward manages a 30-calendar-day review clock.

**Step 2.1: Stakeholder Review**
- **Action:** The ServiceNow workflow auto-generates review tasks for the mandated consultation list based on the policy's regulatory triggers:
    - **Legal Review** (always required): Maria Gonzalez or her delegate reviews for legal risk, contractual consistency, and litigation posture.
    - **Information Security Review** (triggered by terms like "PHI," "Security," "Access Control," "AWS"): Rachel Kim, CISO, or delegate reviews for alignment with the NIST AI RMF, SOC 2 TSC, and HIPAA Security Rule.
    - **Privacy Review** (triggered by "Personal Data," "EU," "Patient," "Marketing"): Dr. Klaus Weber, CPO/DPO, reviews for GDPR Art. 25 (Data Protection by Design and Default), Art. 5 (Principles), and Art. 35 (DPIA) triggers.
    - **AI Governance Review** (triggered by "Model," "Algorithm," "Training Data," "Inference"): Dr. Marcus Rivera, Chief AI Officer, reviews for alignment with the EU AI Act high-risk classification obligations for the Clinical AI Platform, including human oversight mechanisms.
- **Timeline:** All reviewers have a 15-calendar-day SLA to provide feedback. Feedback is documented directly within the ServiceNow review task, with line-item references to the draft document.

**Step 2.2: Feedback Reconciliation**
- **Action:** The Policy Author integrates all feedback. Disagreements are escalated by the Steward to the Policy Owner and the dissenting reviewer for resolution. The Approver breaks any ties.

**Step 2.3: Final Approval**
- **Action:** After all feedback is resolved, the Steward submits the final draft to the designated Approver. The Approver is typically Maria Gonzalez (General Counsel) for legal/privacy policies and Thomas Anderson (CCO) for compliance/SOC 2/HIPAA policies.
- **Approval Action:** The Approver's digital signature in ServiceNow is the final legal act of policy enactment. Upon signature, the Steward changes the `version` to `1.0`, the `status` to `Published`, and sets the `effective_date` as the date of publication.

### 5.3 Phase 3: Publication, Distribution, and Acknowledgment

This phase operationalizes the policy across the organization.

**Step 3.1: Publication to the Central Library**
- **Action:** The Steward publishes the final, signed PDF (generated from the .docx template) to the central ServiceNow Policy Library. The HTML version is made available on the internal `governance.meridianhealth.com` portal. An auto-generated communication is pushed to the Slack `#policy-updates` channel.

**Step 3.2: Targeted Distribution**
- **Action:** The Policy Owner and Steward collaborate to define the target audience for the policy. This audience list is populated by pulling data from Workday based on department, role, and management level.
- **Action:** An official "Policy Release Notice" email, using the `Legal-Compliance@meridianhealth.com` sender address, is distributed to the target audience. The email clearly states the policy's purpose, key changes (if a revision), effective date, and action required (attestation). The email links directly to the policy on the central portal.

**Step 3.3: Attestation Campaign**
- **Action:** Simultaneously, an automated attestation campaign is launched via the ServiceNow GRC module integrated with Okta for SSO. The campaign is configured with the following parameters:
    - **Target Audience:** Derived from the distribution list.
    - **Attestation Text:** A dynamic text block that pulls the policy title, version, and a statement: "I confirm that I have read, understood, and will comply with the requirements of [Policy Title] v[X.X]. I understand that failure to comply may result in disciplinary action, up to and including termination of employment."
    - **Deadline:** 14 calendar days from the campaign launch.
    - **Reminders:** Auto-reminders at 7 days, 3 days, and 1 day before the deadline.
    - **Non-Compliance Action:** On day 15, the individual's record is flagged in ServiceNow, and their direct manager and HR Business Partner are automatically notified via a "Policy Attestation Non-Compliance" incident ticket for immediate follow-up. This is an auditable control for SOC 2 CC1.4.

### 5.4 Phase 4: Maintenance and Continuous Monitoring

The policy is not static after publication.

**Step 4.1: Scheduled Annual Review**
- **Action:** 90 days before the `next_review` date, ServiceNow automatically creates a "Scheduled Policy Review" task for the Policy Steward. The Steward contacts the Policy Owner 60 days before the deadline to initiate the process.
- **Action:** The Author, under the Owner's direction, conducts a complete review for continued accuracy and relevance. The Owner submits a signed "Policy Recertification Statement" confirming the policy's validity with or without changes.
- **Outcome A (No Change):** The `last_reviewed` date is updated to the current date, and the `next_review` date is set to one year from that date. Version number does not change.
- **Outcome B (Minor Change):** A request for a minor revision (e.g., fixing broken links, updating role titles, grammatical fixes) is submitted and approved by the Steward and Owner. The version number is incremented (e.g., 1.0 -> 1.1). This does not trigger a full re-attestation campaign but an acknowledgment notice.
- **Outcome C (Major Change):** A material change to a policy's requirements, scope, or controls triggers a full lifecycle review (Phase 1-3), a new version number (e.g., 1.1 -> 2.0), and a mandatory, full-attestation campaign for all impacted users.

**Step 4.3: Trigger Event Review**
- **Action:** Within 5 business days of a declared Trigger Event (e.g., a reportable HIPAA breach, an OCR inquiry, a new GDPR adequacy decision, a critical zero-day vulnerability in the Meridian SaaS stack), the CCO or GC can declare a "Zero-Day Policy" state.
- **Expedited Procedure:** The standard 30-day review clock in Phase 2 is compressed to 5 business days. Approval authority for a Zero-Day Policy amendment is elevated to the CEO and the CCO jointly. The amendment is published and an immediate, emergency attestation campaign with a 48-hour SLA is launched.

### 5.5 Phase 5: Archival, Rescission, and Violation Handling

**Step 5.1: Policy Rescission and Archival**
- **Action:** A policy can be rescinded if it becomes obsolete, is consolidated into another policy, or its purpose ceases. The Policy Owner, with approval from the CCO, makes this decision.
- **Action:** The Steward changes the policy's status in ServiceNow to "Rescinded" and moves it to the Archive folder. The `effective_until_date` is set to the date of rescission. The record and all its historical documents (including attestation records) are retained in the archive in a read-only, immutable format for a minimum of 7 years from the date of rescission to meet legal hold requirements for potential litigation and regulatory investigation (SOC 2 CC6.1, HIPAA § 164.316(b)(2)(i), GDPR Art. 24).

**Step 5.2: Violation and Enforcement Process**
- **Action:** A suspected policy violation must be reported to `Legal-Compliance@meridianhealth.com` or via the ServiceNow Incident Reporting hotline (anonymous option available per SOP-HR-020). Whistleblower protections apply per SOP-HR-020.
- **Action:** The CCO (Thomas Anderson) or delegate opens a confidential investigation. The investigation gathers evidence, conducts interviews, and determines the scope and impact of the violation. This process is strictly confidential.
- **Action:** Based on the investigation findings, the CCO presents a report to a panel consisting of the Policy Owner, a representative from Legal, and a senior HR representative (CHRO or delegate).
- **Outcome:**
    - **Determination of Sanction:** Sanctions are determined based on the severity, frequency, and intent of the violation. The range of sanctions, as defined in SOP-HR-105, includes verbal warning, formal written warning, mandatory retraining, suspension without pay, and termination.
    - **Regulatory Notification:** If the violation constitutes a reportable breach (e.g., a breach of unsecured PHI under HIPAA, a personal data breach under GDPR Art. 33), the General Counsel and the CPO/DPO will manage the regulatory notification process independently of and concurrently with the internal disciplinary process.
    - **Control Remediation:** The Policy Owner and CISO are responsible for implementing any new technical or administrative controls required to prevent recurrence. This becomes a Risk Treatment Plan item in the ServiceNow GRC risk register.

## 6. Controls and Safeguards

Meridian implements a multi-layered control framework to safeguard the policy lifecycle process itself. These controls are designed to meet specific regulatory articles and SOC 2 criteria.

### 6.1 Administrative Controls

| Control ID | Control Description | Mechanism | SOC 2 TSC Reference | HIPAA Reference | GDPR Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ADM-01** | **Segregation of Duties** | The Policy Steward cannot approve content. The Approver cannot publish. ServiceNow workflow enforces separation. | CC5.1 (Control Activities) | § 164.308(a)(3)(ii)(B) (Information Access Management) | Art. 25(1) (Data Protection by Design) |
| **ADM-02** | **Management Oversight** | Quarterly review of policy lifecycle KPIs with the Chief Risk Officer and policy dashboard review during the Audit Committee meeting. | CC2.1 (Communication & Information) | § 164.308(a)(1)(ii)(B) (Risk Management) | Art. 24(2) (Responsibility of Controller) |
| **ADM-03** | **Formal Disciplinary Process** | A sanctioned, company-wide, HR-driven disciplinary process for non-compliance. Referenced in all attestation campaigns. | CC1.2 (Code of Conduct) | § 164.308(a)(1)(ii)(C) | Art. 83 (Penalties) |
| **ADM-04** | **Vendor Policy Flow-down** | Master Services Agreement (MSA) clauses require critical vendors to acknowledge and flow-down key Meridian policies (e.g., Data Handling). Managed by Vendor Risk Management (SOP-VRM-020). | CC9.2 (Vendor Risk Management) | § 164.308(b)(1); BAA | Art. 28(3) (Controller-Processor Contract) |

### 6.2 Technical Controls

| Control ID | Control Description | Mechanism / System | SOC 2 TSC Reference |
| :--- | :--- | :--- | :--- |
| **TEC-01** | **Centralized Library & Version Control** | All policies are stored with full version history, digital signatures, and audit trails in ServiceNow GRC. No policy can be distributed outside this system's approval workflow. | CC6.1 (Logical and Physical Access Controls) |
| **TEC-02** | **Role-Based Access Control (RBAC)** | Permissions are strictly controlled in ServiceNow: Authors can edit drafts; Owners can approve; Stewards can publish/archive; all others have read-only access to Published documents. Access logs are reviewed monthly by CISO. | CC6.1, CC6.3 |
| **TEC-03** | **Immutable Audit Trail** | Every action in the ServiceNow Policy Module (creation, edit, review, approval, acknowledgment) is logged with a timestamp, user ID, and a non-repudiable hash. These logs are ingested into Splunk and retained for 7 years. | CC7.1, CC7.2 |
| **TEC-04** | **Automated Attestation Workflow** | ServiceNow-OKTA integration pushes mandatory attestations. A direct API query between ServiceNow and the HRMS (Workday) confirms employment status and role. | CC5.2, CC6.1 |

### 6.3 Physical Controls

- An air-gapped, offline backup of the entire ServiceNow instance, including policy records, is stored in a secure, access-controlled vault in the Meridian Boston datacenter. This backup is refreshed bi-annually and tested for data integrity as part of the disaster recovery plan (SOP-IT-050).

### 6.4 Version Control and Standard Naming Convention

All documents adhere to the following naming convention, enforced by the ServiceNow form:
`[Document Type Code]-[Business Unit Code]-[NNN]`
- **Document Type:** SOP (Standard Op. Procedure), POL (Policy), STD (Standard).
- **Business Unit:** LEGC (Legal & Compliance), ISMS (InfoSec), HRMS (Human Resources), PRIV (Privacy), MGAI (AI Governance).
- **NNN:** Sequential three-digit number assigned by the Steward.

Example: `STD-ISMS-015` is the Encryption Standard, owned by Information Security.

### 6.5 Regulatory Cross-Mapping (Excerpt)

The Policy Steward maintains a full, auditable matrix mapping every active policy to the precise regulation it supports. This matrix is reviewed quarterly.

| Meridian SOP/Policy ID | Title | Primary SOC 2 TSC | Primary HIPAA Rule | Primary GDPR Article(s) | EU AI Act |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SOP-LEGC-010** | Policy Lifecycle Mgmt | CC1.1, CC5.1, CC6.1, CC7.1 | § 164.308(a)(1)(ii)(A-D), § 164.316(b)(2)(i) | Art. 5(2), 24, 25, 39 | Art. 17 |
| POL-ISMS-001 | Information Security Policy | CC1.2, CC4.1, CC5.2 | § 164.308(a)(1)(i) | Art. 32 | N/A |
| SOP-DLP-005 | Data Classification Policy | CC1.1, CC6.1 | § 164.310(c), § 164.312(e)(1) | Art. 5(1)(c) | Art. 10 |
| SOP-AIM-001 | AI Model Lifecycle Policy | N/A | N/A | Art. 35 | Art. 9, 10, 14, 17 |

## 7. Monitoring, Metrics, and Reporting

The effectiveness of the policy lifecycle program is measured through a defined set of KPIs. The CCO (Thomas Anderson) is responsible for monitoring and reporting on these metrics.

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target / SLA | Measurement Method |
| :--- | :--- | :--- |
| **Policy Recertification Timeliness** | 95% of policies recertified on or before their `next_review` date. | ServiceNow GRC Policy Dashboard. |
| **Attestation Completion Rate** | 100% completion within 14 calendars of campaign launch. | ServiceNow Campaign Analytics. |
| **Overdue Policy Rate** | 0% of active policies with a `next_review` date older than 30 days. Zero tolerance. | ServiceNow automated report, weekly. |
| **Policy Acknowledgment Time** | Mean time-to-acknowledge < 48 hours from campaign launch. | ServiceNow Campaign Analytics. |
| **Draft Review Cycle Time** | 80% of drafts move from "In Review" to "Published" status within 30 calendars. | ServiceNow workflow cycle time report. |
| **Exception Aging** | 90% of open, non-permanent exceptions are less than 90 days old. All exceptions are reviewed at least semi-annually. | ServiceNow Exception Management Module. |

### 7.2 Reporting Cadence

| Report | Audience | Frequency | Content |
| :--- | :--- | :--- | :--- |
| **Operational KPI Dashboard** | Thomas Anderson (CCO), Policy Owners | Monthly (automated report) | Real-time tracking of all Section 7.1 KPIs; drill-down to specific overdue items and non-compliant users. |
| **Compliance & Risk Report** | Compliance Steering Committee (CCO, GC, CFO, CISO, CPO/DPO) | Quarterly | Summary of KPI trends, open exceptions, trigger events, upcoming regulatory changes, and the 12-month policy review forecast. |
| **Governance & Audit Update** | Board of Directors, Audit Committee Chair | Annually (Q4) | Executive-level summary of program health, significant policy changes, independent audit findings (e.g., SOC 2 Type II, ISO 27001), and program maturity roadmap. |

## 8. Exception Handling and Escalation

This section describes the process for requesting a formal, documented exemption from a specific policy mandate.

### 8.1 Exception Request Process

1.  **Initiation:** An employee or their manager identifies a legitimate business need that cannot be met without a deviation from a specific policy control. The manager submits a "Policy Exception Request" from the ServiceNow GRC portal. The request must include:
    - Specific policy ID and the clause from which the exception is sought.
    - Detailed business justification and operational need.
    - A compensating control analysis: What alternative safeguards will be implemented to reduce the inherent risk to an acceptable level?
    - Proposed duration (start and end date). Permanent exceptions are disallowed.

2.  **Risk Assessment:**
    - **CISO Review (Rachel Kim):** For any exception touching technical controls, systems, or data. The CISO provides a formal, documented risk rating (High, Medium, Low) and an opinion on the acceptable compensating controls.
    - **CPO/DPO Review (Dr. Klaus Weber):** For any exception impacting personal data processing. A Data Protection Impact Assessment (DPIA) light-review is triggered to ensure the exception does not cross GDPR Art. 35 thresholds.

3.  **Approval Authority:** Based on the risk rating and duration, the exception is routed for approval.
    | Risk Rating | Max. Duration | Business Justification Approver | CISO or CPO Sign-Off Required |
    | :--- | :--- | :--- | :--- |
    | **Low** | 12 Months | Policy Owner & Policy Steward | Not mandatory, but consulted |
    | **Medium** | 6 Months | Policy Owner & Thomas Anderson (CCO) | Mandatory |
    | **High** | 90 Days | Thomas Anderson (CCO) & Maria Gonzalez (GC) | Mandatory |

4.  **Tracking and Closure:** Approved exceptions are logged in the ServiceNow GRC module. The system auto-generates a task for the CISO 10 days before the exception's expiration. The requestor must either resubmit for an exception renewal or demonstrate that the non-compliant condition has been fully remediated. No exception expires silently; failure to close or renew results in an automatic escalation to the CCO.

## 9. Training Requirements

All Meridian personnel with a designated role in this SOP must undergo specific, auditable training.

| Role(s) | Training Title | Method | Frequency | Initial Assignment |
| :--- | :--- | :--- | :--- | :--- |
| **Policy Owners & Authors** | POLICY-AUTH-101: Authoring Effective Governance & Regulatory Mapping | Instructor-led (virtual) by Compliance Team | Annually (as refresher) | Within 30 days of role assignment |
| **Policy Stewards** | POLICY-STEW-201: Advanced GRC Administration and Audit Prep | External certified GRC professional training (e.g., ServiceNow Admin, CISA prep) | Annually | Before grant of admin privileges to ServiceNow Library |
| **All Approvers & Senior Mgmt** | CORPORATE-LEGAL-101: Legal & Regulatory Obligations for Control Oversight | e-Learning (Workday LMS) + annual live town hall with GC | Annually | Within 30 days of promotion/hire |

### 9.1 Training Tracking and Remediation

- All training completions and assessment scores are automatically recorded in the individual's Workday Learning profile. A score of 90% or higher on the POLICY-AUTH-101 assessment is required to pass. Failure results in mandatory, assigned retraining within 15 days. The Policy Steward tracks a 100% completion KPI for all assigned roles each calendar year.

## 10. Related Policies and References

This SOP does not exist in isolation. The following internal and external documents form the broader governance ecosystem.

### 10.1 Internal Meridian Policies and Standards

- **SOP-HR-105:** Employee Relations and Disciplinary Action (Sanction Guidelines)
- **SOP-HR-020:** Whistleblower and Non-Retaliation Policy (Reporting Violations)
- **SOP-ISMS-001:** Information Security Management System (ISMS) Policy
- **SOP-VRM-020:** Third-Party Vendor Risk Management
- **STD-ISMS-010:** Access Control Standard
- **POL-DLP-005:** Data Classification & Handling Policy
- **POL-AI-01:** AI Governance and Ethics Charter (EU AI Act Compliance)
- **SOP-IT-050:** IT Disaster Recovery and Business Continuity Plan

### 10.2 External Standards and Regulatory References

- **AICPA Trust Services Criteria (TSC):** For SOC 2 Type II examinations. Specifically CC1.1 (Control Environment), CC5.1 (Control Activities), CC7.1 (Information & Communication), and CC9.2 (Risk Mitigation).
- **Health Insurance Portability and Accountability Act (HIPAA):** 45 CFR Part 164, Subparts C (Security) and D (Notification). Specifically § 164.308 (Admin Safeguards), § 164.316 (Policies & Procedures).
- **General Data Protection Regulation (GDPR):** (EU) 2016/679. Specifically Art. 5, 24, 25, 28, 30, 32, 33, 35, and 39.
- **NIST SP 800-53 Rev. 5:** Control Family PM-1 (Program Management) and AU-1 (Audit and Accountability), used as supplementary guidance for SOC 2 controls.
- **ISO 27001:2022:** Annex A, Clause 5.1 (Leadership and commitment).

### 10.3 Templates and Forms

- **TEMPLATE-LEGC-010_Rev4.docx:** Authorized Policy Document Template (available on Compliance SharePoint).
- ServiceNow GRC Forms:
    - `PCR_Form_001`: Policy Change Request
    - `EXCEPTION_Form_001`: Policy Exception Request
    - `ATTS_Campaign_001`: Attestation Campaign Configuration

## 11. Revision History

| Version | Date | Author | Change Summary |
| :--- | :--- | :--- | :--- |
| 1.0 | 2022-05-10 | Sarah Jenkins (Former CCO) | Initial creation and implementation of formal policy lifecycle program. |
| 1.4 | 2023-02-15 | Marcus Thorne (GRC Analyst) | Major update to integrate the new ServiceNow GRC module; retired Confluence-based library. Added Phase 5 details on archiving. |
| 1.6 | 2023-11-20 | Thomas Anderson (Current CCO) | Post-SOC 2 Type II audit revision. Strengthened QA gate in Section 5.1; added KPI for overdue policy rate; updated exception approval matrix to add CISO sign-off. |
| 1.8 | 2024-07-08 | Thomas Anderson & Dr. Klaus Weber | GDPR and EU AI Act alignment update. Added mandatory CPO/DPO review trigger; included CAIO review for AI-related policies; updated definitions for "Zero-Day Policy." |
| 1.9 | 2024-12-03 | Thomas Anderson & Maria Gonzalez | Comprehensive annual review. Formalized new CAIO role responsibilities; updated regulatory mapping for EU AI Act, Art. 9 & 10; updated template reference to Rev4; minor grammar fixes to attestation text. No structural changes. |