---
sop_id: "SOP-LEGC-004"
title: "External Audit Coordination"
business_unit: "Legal & Compliance"
version: "3.7"
effective_date: "2025-12-22"
last_reviewed: "2026-02-13"
next_review: "2026-08-20"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the standardized framework and operational guidelines for coordinating, managing, and executing all external audits conducted at Meridian Health Technologies, Inc. ("Meridian" or the "Company"). The purpose of this SOP is to ensure that all external audits are conducted in a systematic, efficient, and transparent manner that demonstrates the Company's ongoing commitment to compliance, security, and operational excellence. This SOP specifically governs audits related to SOC 2 Type II, HIPAA compliance, HITRUST CSF, ISO 27001:2022, FDA 510(k) surveillance, EU MDR conformity assessments, and other regulatory or contractual audit requirements that may arise from our status as a multi-jurisdictional healthcare technology organization.

Effective audit coordination protects Meridian's certifications and accreditations, which are foundational to our market position. Failure to maintain these certifications would trigger contractual defaults with over 340 hospital clients, disrupt HealthPay's payment processing capabilities, and expose the Company to regulatory enforcement actions across multiple jurisdictions. This SOP is designed to mitigate those risks through rigorous preparation, disciplined evidence management, and structured remediation tracking.

### 1.2 Scope

This SOP applies to all external audits conducted across Meridian's four business lines—Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform—and covers all associated technology stacks, operational processes, and control environments. The scope encompasses:

**In-Scope Entities and Systems:**
- All Meridian corporate offices, including the Boston headquarters (75 Arlington Street), the Dublin EU operations center, and the Singapore APAC hub
- All production environments hosting the Meridian SaaS Platform, including Amazon Web Services (AWS) us-east-1 and eu-west-1 regions, and the Azure Government Cloud for U.S. public-sector clients
- Clinical AI Platform model training infrastructure, inference endpoints, and associated data pipelines
- HealthPay transaction processing systems, settlement engines, and merchant onboarding platforms
- MedInsight analytics clusters, data warehousing environments, and de-identification pipelines
- All corporate identity and access management systems, including Okta Workforce Identity and CyberArk Privileged Access Management
- Atlassian Jira Service Management (JSM) for audit finding tracking and remediation workflow
- Evidence collection systems: Vanta for continuous compliance monitoring, AWS Audit Manager for cloud control evidence, and the Meridian Document Vault (SharePoint Online)

**In-Scope Personnel:**
- All Legal & Compliance (L&C) personnel, including the Audit Coordination Team (ACT)
- Chief Compliance Officer (CCO) and designated Compliance Owners for each regulatory domain
- Engineering Directors and Technical Leads responsible for control implementation (DevOps, Security Engineering, Data Platform, Clinical AI/ML, HealthPay Platform)
- People Operations (HR) for personnel controls, background check evidence, and training records
- Physical Security for data center access logs, camera footage retention, and badge systems
- Any Meridian personnel who receive an audit inquiry, evidence request, or interview invitation

**Out of Scope:**
- Internal audits conducted by Meridian's Internal Audit function (governed by SOP-LEGC-001)
- Client-led vendor risk assessments and security questionnaires (governed by SOP-SEC-008)
- Penetration tests and technical security assessments procured independently (governed by SOP-SEC-012)
- Tax or financial statement audits conducted by the Finance department

### 1.3 Applicability

All Meridian employees, contractors, and third-party service providers who are involved in or impacted by external audit activities must comply with this SOP. Compliance is mandatory and non-negotiable for personnel in designated audit coordination roles. Failure to adhere to the procedures outlined herein may result in disciplinary action up to and including termination of employment or contract, in accordance with HR Policy HR-305 and the Company's Code of Conduct.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Audit Engagement** | A formally scoped and contracted external audit activity, identified by a unique Engagement ID (format: AUD-YYYY-NNN). |
| **Audit Universe** | The complete inventory of all external audits, certifications, and attestations maintained by the Company, stored in the Compliance Calendar (Vanta). |
| **Control Owner** | The named individual accountable for the design, implementation, and operating effectiveness of a specific control. This individual is responsible for providing evidence during audits. |
| **Evidence Package** | A structured collection of documents, artifacts, screenshots, logs, and attestations compiled to demonstrate a control's operating effectiveness for a defined audit period. |
| **Finding** | A formal observation or deficiency identified by the external auditor, classified as: *Significant Deficiency*, *Material Weakness* (SOC 2), *Non-Conformity* (ISO 27001), or *Corrective Action Required* (HIPAA, HITRUST). |
| **Remediation Plan** | A documented plan, tracked in Jira JSM, that identifies the corrective actions, accountable owner, milestone dates, and evidence requirements necessary to close a Finding. |
| **Audit Liaison** | A designated Meridian employee who serves as the primary point of contact between the external audit firm and internal Meridian stakeholders. |
| **Walkthrough** | A structured demonstration where a Control Owner shows the auditor the operation of a control, typically via screen sharing of system configurations and review of a sample transaction. |
| **Population** | The complete set of items from which an auditor draws a sample for testing (e.g., all change requests for a quarter). |
| **Sample** | A subset of items selected by the auditor from a Population for detailed testing. |
| **Audit Period** | The defined timeframe covered by the audit, typically a rolling twelve-month period ending on the review date. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **ACT** | Audit Coordination Team (within Legal & Compliance) |
| **AICPA** | American Institute of Certified Public Accountants |
| **APAC** | Asia-Pacific |
| **AWS** | Amazon Web Services |
| **BAA** | Business Associate Agreement |
| **CCO** | Chief Compliance Officer |
| **CFR** | Code of Federal Regulations |
| **CISO** | Chief Information Security Officer |
| **CSF** | Common Security Framework (HITRUST) |
| **DPO** | Data Protection Officer |
| **EMR** | Electronic Medical Record |
| **EPHI** | Electronic Protected Health Information |
| **FDA** | U.S. Food and Drug Administration |
| **GC** | General Counsel |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996 |
| **HITECH** | Health Information Technology for Economic and Clinical Health Act |
| **HITRUST** | Health Information Trust Alliance |
| **IAM** | Identity and Access Management |
| **ISO** | International Organization for Standardization |
| **JSM** | Jira Service Management |
| **MDR** | Medical Device Regulation (EU 2017/745) |
| **NIST** | National Institute of Standards and Technology |
| **OCR** | Office for Civil Rights (U.S. Department of Health and Human Services) |
| **PHI** | Protected Health Information |
| **RBAC** | Role-Based Access Control |
| **RPO** | Recovery Point Objective |
| **RTO** | Recovery Time Objective |
| **SOC** | System and Organization Controls |
| **SoD** | Segregation of Duties |
| **SSAE** | Statement on Standards for Attestation Engagements |
| **SSO** | Single Sign-On |
| **TSC** | Trust Services Criteria (SOC 2) |
| **VP** | Vice President |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

The following RACI matrix defines the roles and responsibilities for all major phases of the external audit lifecycle. A RACI designation of **R** (Responsible) denotes the individual who performs the work; **A** (Accountable) denotes the individual who answers for the completion and approves the deliverable; **C** (Consulted) denotes individuals whose input is sought; **I** (Informed) denotes individuals kept apprised of progress.

| Activity / Deliverable | CCO (Thomas Anderson) | GC (Maria Gonzalez) | VP, Security (David Chen - CISO) | Director, Platform Engineering (Priya Kapoor) | ACT Lead (Jennifer Walsh) | Control Owner (Various) | DPO (Sarah Okonkwo) |
|---|---|---|---|---|---|---|---|
| **Audit Planning & Scoping** | A | C | C | I | R | C | C |
| **Auditor Selection & Contracting** | C | A | I | I | R | I | I |
| **Evidence Collection & Validation** | I | I | C | C | R | R | I |
| **Walkthrough Facilitation** | I | I | I | I | A | R | C |
| **Auditor Inquiry Response** | C | I | C | C | R | R | C |
| **Finding Triage & Remediation Planning** | A | C | R | R | R | R | C |
| **Remediation Execution** | I | I | I | I | C | R | I |
| **Audit Report Review & Acceptance** | R | A | C | I | R | I | I |
| **Regulatory Notification (HIPAA Breach, etc.)** | C | A | R | C | R | I | R |

### 3.2 Role-Specific Responsibilities

**Thomas Anderson, Chief Compliance Officer (CCO)**
- Serves as the executive sponsor for all external audits and the primary signatory for management representation letters.
- Approves the annual Audit Universe plan and prioritization for resource allocation.
- Reviews and approves all Remediation Plans for Findings classified as *Material Weakness* or *Significant Deficiency*.
- Escalates overdue or critically blocked remediations to the Executive Risk Committee.
- Designated HIPAA Security Officer under 45 CFR § 164.308(a)(2), responsible for the overall HIPAA Security Rule compliance posture and the final approval of all policies and procedures subject to audit scrutiny.

**Maria Gonzalez, General Counsel (GC)**
- Reviews and approves all Engagement Letters with external audit firms, ensuring appropriate legal protections for privileged work product, limitation of liability, and data handling terms.
- Serves as the primary legal advisor on auditor access to legally privileged information, including incident response reports and attorney-client communications.
- Authorizes the release of any final audit report to external parties, including clients and regulators, under a Non-Disclosure Agreement (NDA).

**Jennifer Walsh, Audit Coordination Team Lead (ACT Lead)**
- Manages the day-to-day operational execution of all active audit engagements, serving as the primary Audit Liaison for external audit firms.
- Maintains the master audit schedule, evidence package tracker, and the Finding repository in Jira JSM.
- Performs first-pass quality review on all evidence packages for completeness, timeliness, and adherence to evidence standards defined in Section 5.
- Coordinates logistics for all walkthroughs, interviews, and status update meetings.
- Manages auditor access to the Meridian Document Vault (SharePoint Online) evidence portal.

**Control Owners (Various - named per control)**
- Attends walkthrough meetings and demonstrates the operating effectiveness of assigned controls.
- Collects, annotates, and submits evidence packages to the ACT Lead by the defined evidence request deadline.
- Drafts Remediation Plans for any Findings associated with their controls, obtains approval from the CCO (or delegate), and executes remediation tasks on schedule.
- Proactively notifies the ACT Lead of any control failures, deviations, or significant environmental changes that may impact audit results.

**David Chen, VP Security (CISO)**
- Owns all controls within the Security domain, including IAM, vulnerability management, endpoint protection, and incident response.
- Provides technical validation of evidence artifacts that rely on security infrastructure (e.g., AWS CloudTrail logs, Okta system logs, CrowdStrike Falcon console screenshots).

**Priya Kapoor, Director of Platform Engineering**
- Owns controls within the Availability domain for the Meridian SaaS Platform and the AWS infrastructure layer.
- Ensures that recovery commitments align with platform capabilities and provides architectural context during availability walkthroughs.

**Sarah Okonkwo, Data Protection Officer (DPO - Dublin)**
- Advises on all EU MDR and GDPR evidentiary requirements impacting clinical AI products with CE marking.
- For HIPAA audits, provides consultation on patient rights management under 45 CFR § 164.524 and the documentation requirements for the designated record set.
- Coordinates European regulatory notifications if an audit reveals a notifiable personal data breach under Article 33 of the GDPR.

---

## 4. Policy Statements

Meridian Health Technologies is committed to a "no surprises" audit philosophy. The following policy statements govern all external audit activities and are binding on all personnel.

**P-001: Auditor Qualification and Independence**
All external audit firms engaged by Meridian must hold current, recognized credentials from the relevant governing body (e.g., AICPA for SOC 2 attestations) and must demonstrate independence in accordance with the applicable professional standards. No Meridian employee may hold a direct financial interest in an audit firm engaged to perform attestation services for the Company. The GC's office shall obtain an independence representation letter from each audit firm prior to engagement.

**P-002: Single Liaison Channel**
All communications between Meridian and the external audit team shall flow through the designated Audit Liaison (ACT Lead). No Control Owner, executive, or other Meridian employee shall provide unsolicited information, opinion, or commentary directly to the auditor without the prior knowledge and coordination of the ACT Lead. This policy ensures message consistency and prevents inadvertent scope expansion. Any direct inquiry received by an employee from an auditor must be forwarded to the ACT Lead and the CCO before a response is prepared.

**P-003: Truthful and Complete Representation**
Meridian does not tolerate misrepresentation or concealment of facts during an audit. All evidence submitted must be accurate, complete, and relevant for the control under test. If a control was not operating effectively during the audit period, the Control Owner must disclose the deviation to the ACT Lead, who shall, with counsel from the GC, proactively present the deviation to the auditor along with a preliminary remediation plan. Attempting to fabricate or retroactively generate evidence is a terminable offense under SOP-HR-002.

**P-004: Auditor Access and Confidentiality**
Access to Meridian systems, data, and facilities by external auditors shall be granted on a least-privilege, time-bound basis. Auditors shall sign Meridian's standard Confidentiality Agreement (Form LEGC-004-CA) prior to receiving any access to proprietary information. No auditor shall be granted unescorted physical access to any Meridian facility or unsupervised logical access to any production system.

**P-005: Finding Acceptance and Remediation**
All Findings presented by an external auditor shall be formally reviewed and either accepted or formally disputed by the CCO within ten (10) business days of receipt of the draft report. An accepted Finding shall have a corresponding Remediation Plan created in Jira JSM within fifteen (15) business days of acceptance. Target closure for all Findings is prior to the commencement of the next audit period's fieldwork, unless a longer timeframe is explicitly approved by the CCO and communicated to the auditor.

---

## 5. Detailed Procedures

The external audit lifecycle is managed in four distinct phases: Auditor Selection and Engagement, Audit Preparation and Readiness, Evidence Management and Fieldwork, and Finding Remediation and Closure. Each phase is detailed below.

### 5.1 Phase 1: Auditor Selection and Engagement

This phase initiates upon identification of an audit requirement (annually per the Compliance Calendar, or reactively due to a new regulatory mandate or client contractual requirement).

#### 5.1.1 Requirement Identification and Scoping

1.  The **ACT Lead** reviews the Compliance Calendar in Vanta and identifies upcoming audit requirements at least **six (6) months** prior to the Audit Period end date.
2.  The ACT Lead drafts a preliminary Scope Memorandum using the **Audit Scope Template (LEGC-004-T01)** in the Meridian Document Vault. The memorandum includes:
    -   Audit type (SOC 2 Type II, HIPAA, HITRUST, ISO 27001 Surveillance, etc.)
    -   Proposed Trust Services Criteria (TSC) for SOC 2 (Security, Availability—see Section 6.2, Confidentiality, Processing Integrity, Privacy)
    -   In-scope business units, systems, and geographic locations
    -   Proposed Audit Period (typically trailing 12 months)
    -   Key system and organizational changes since the last audit
3.  The ACT Lead circulates the draft Scope Memorandum to the **CCO**, **CISO**, **DPO**, and relevant **VP-level stakeholders** for a five (5) business day review.
4.  The CCO approves the final Scope Memorandum. For HIPAA-specific audits, the Scope Memorandum specifically enumerates which components of the Security Rule administrative, physical, and technical safeguards (45 CFR §§ 164.308, 164.310, 164.312) and which organizational and policies and procedures requirements (45 CFR § 164.316) will be examined. For privacy components, the DPO confirms in-scope entities and patient data flows subject to 45 CFR § 164.514 (Requirements for de-identification).

#### 5.1.2 Request for Proposal (RFP) and Firm Selection

For recurring audits where an incumbent auditor is retained, proceed to Section 5.1.3. For new engagements or mandatory rotations, follow this procedure:

1.  The **ACT Lead**, in consultation with the **GC**, identifies a shortlist of qualified audit firms. The shortlist contains a minimum of three (3) firms.
2.  The ACT Lead issues a formal Request for Proposal (RFP) using **Template LEGC-004-T02**. The RFP includes:
    -   Approved Scope Memorandum
    -   Meridian's Standard Terms and Conditions for Professional Services
    -   Required credentials and relevant healthcare technology experience
    -   Proposed timeline, team composition, and fee schedule
    -   Mandatory HIPAA BAA requirement
3.  The GC's office manages all NDA execution with prospective firms before sharing any Meridian confidential information.
4.  The selection committee—comprising the **CCO**, **GC**, and **CISO**—evaluates proposals on criteria weighted as follows: Relevant Experience (40%), Proposed Methodology (30%), Cost (20%), and Team Fit / Cultural Alignment (10%).
5.  The committee's recommendation is documented in a Firm Selection Memorandum and approved by the Chief Financial Officer (CFO) if the engagement fee exceeds **$150,000**.

#### 5.1.3 Engagement Letter and Kickoff

1.  The **GC** negotiates and approves the final Engagement Letter. The Engagement Letter must include clauses for:
    -   Confidentiality of audit work papers
    -   Limitation of liability commensurate with fees
    -   Data breach notification obligations on the auditor (per HIPAA BAA)
    -   Return or destruction of Meridian data at engagement conclusion
    -   Prohibition on subcontracting without prior written consent
2.  The **CCO** signs the Engagement Letter on behalf of Meridian.
3.  The **ACT Lead** schedules a formal Kickoff Meeting within ten (10) business days of engagement execution. Attendees include the full audit team, the CCO, CISO, GC, and all primary Control Owners.
4.  At the kickoff, the ACT Lead presents the Audit Logistics Package, including:
    -   Auditor access badges and temporary Okta credentials (active for the duration of fieldwork only)
    -   Link to the dedicated SharePoint site for the engagement
    -   Communication protocols and the Single Liaison rule (P-002)
    -   Escalation contacts for access or technical issues (ACT Lead, Help Desk)

### 5.2 Phase 2: Audit Preparation and Readiness (Pre-Fieldwork)

This phase begins four (4) months before the scheduled start of fieldwork.

#### 5.2.1 Readiness Assessment

1.  The **ACT Lead**, working with the CISO's Security GRC team, executes an internal Readiness Assessment focused on all in-scope controls using Vanta's automated testing framework.
2.  The output is a **Control Readiness Report** that classifies each control as **Green** (evidence complete and compliant), **Yellow** (evidence incomplete or minor non-conformities), or **Red** (evidence missing or control failure). All Yellow and Red controls require a pre-audit remediation sprint.

#### 5.2.2 Evidence Pre-Collection and Population Generation

For SOC 2 and HIPAA audits requiring population-based sampling (e.g., user access reviews, change management approvals), the following procedure is mandatory:

1.  **Control Owners** generate and export the complete Population for each control from the system of record (e.g., Jira for change records, Okta for user account additions) for the entire Audit Period.
2.  Control Owners annotate the Population to highlight expected auditor selection criteria (e.g., changes in production, users with privileged access).
3.  For HIPAA-specific controls under 45 CFR § 164.312(b) (Audit Controls), the Control Owner for the Clinical AI Platform must provide a complete, unalterable log export demonstrating the capture of all access, modification, and deletion events involving EPHI in the MedInsight data warehouse. This log must be readable in the Meridian centralized SIEM (Sumo Logic) and must be retained for the period defined in the data retention schedule (SOP-SEC-001), which shall be no less than six (6) years per HIPAA § 164.316(b)(2)(i).

#### 5.2.3 Control Owner Training

No later than **four (4) weeks** prior to the start of fieldwork, all Control Owners must complete the mandatory "External Audit Preparedness" training module, assigned via the Workday Learning Management System (LMS). Completion is tracked, and non-completion is escalated to the CCO. Content refreshers for this training are detailed in Section 9.

---

### 5.3 Phase 3: Evidence Management and Fieldwork

This is the active audit execution phase, typically lasting four to eight weeks.

#### 5.3.1 Evidence Request Intake and Assignment

1.  All auditor evidence requests (Requests For Evidence - RFEs) must be submitted through the designated Meridian Jira Service Management (JSM) project board ("External Audit Findings & RFEs"), not via email.
2.  The **ACT Lead** reviews each JSM ticket for clarity and completeness within **four (4) business hours** of submission. If a request is ambiguous, the ACT Lead engages the auditor for clarification, minimizing time wasted by Control Owners.
3.  Once clarified, the ACT Lead assigns the RFE ticket to the appropriate **Control Owner** and sets a due date based on the following SLA:

| RFE Priority | Auditor SLA (from ticket receipt) | Meridian Internal SLA (Owner submission) |
|---|---|---|
| **P1 - Critical / Blocking** | Not Applicable | 24 hours |
| **P2 - High (Mandatory control test)** | 5 business days | 3 business days |
| **P3 - Medium (Supporting evidence)** | 10 business days | 7 business days |
| **P4 - Low (Informational)** | 15 business days | 12 business days |

#### 5.3.2 Evidence Package Assembly and Quality Review

1.  The **Control Owner** assembles the evidence package per the guidance in the Meridian *Evidence Collection Standard (LEGC-STD-004-A)*, ensuring all artifacts are:
    -   **Relevant:** Directly demonstrates the control operation.
    -   **Complete:** Shows the full timeline, all approvals, and relevant system configurations.
    -   **Annotated:** Highlights the specific element that satisfies the control requirement. Raw screenshots are unacceptable without annotation.
    -   **Time-stamped:** Clearly within the Audit Period.
2.  The Control Owner attaches the evidence package to the JSM ticket and transitions the status to **"Peer Review"**.
3.  A designated **Peer Reviewer** (typically a Technical Lead or Engineering Manager not directly involved in the evidence creation) reviews the package for technical accuracy and annotates any gaps.
4.  The Control Owner transitions the ticket to **"ACT Review"**.
5.  The **ACT Lead** performs the final Quality Assurance (QA) check, verifying formatting, naming conventions, annotation clarity, and adherence to the non-technical requirements of the request. If evidence fails QA, the ticket is returned to the Control Owner with specific comments.
6.  Upon passing QA, the ACT Lead uploads the final package to the auditor's restricted folder in the Meridian Document Vault and transitions the JSM ticket to **"Submitted to Auditor"**.

#### 5.3.3 Walkthrough and Demonstration Facilitation

1.  The **ACT Lead** schedules all walkthroughs at least **five (5) business days** in advance and sends calendar invitations with a detailed agenda, the auditor's Zoom link, and a list of required participants.
2.  One (1) business day before the walkthrough, the ACT Lead holds a preparatory session with all Meridian participants to review:
    -   The agenda and control narrative.
    -   The "single voice" rule: The designated Control Owner answers auditor questions; other Meridian personnel should mute and use the Zoom chat for internal-only clarifications.
    -   Anticipated difficult questions and approved responses.
3.  During the walkthrough, the **ACT Lead** shares their screen to control the flow of the demonstration. The Control Owner describes their actions while the ACT Lead navigates the system.
4.  A designated Meridian scribe takes detailed meeting minutes, capturing every auditor question and the Meridian response. These minutes are stored in the engagement-specific folder in the Document Vault and are considered privileged communication subject to review by the GC's office.

---

### 5.4 Phase 4: Finding Remediation and Closure

#### 5.4.1 Management Response and Remediation Planning

1.  Upon receiving a draft Finding from the auditor, the **ACT Lead** logs it in the JSM "External Findings" project and assigns it to the relevant **Control Owner**.
2.  The Control Owner has **five (5) business days** to draft a proposed Management Response and Remediation Plan using the **Finding Remediation Template (LEGC-004-T03)** . The plan must include:
    -   A clear statement of whether Meridian accepts or disputes the Finding. Disputes must be accompanied by counter-evidence.
    -   Root cause analysis.
    -   Specific corrective actions with assigned owners.
    -   Milestone dates with measurable deliverables.
3.  For Findings classified by the auditor as significant (Material Weakness, Major Non-Conformity), the Remediation Plan must be approved by the **CCO** and **CISO** prior to submission to the auditor.
4.  The **ACT Lead** formally submits the Management Response to the auditor within the timeframe stipulated in the audit contract (typically within ten business days of draft report issuance).

#### 5.4.2 Remediation Execution and Validation

1.  The **Control Owner** executes the approved Remediation Plan, updating the JSM ticket's progress and attaching evidence of completion for each milestone.
2.  Upon completion of the plan, the Control Owner transitions the JSM ticket to **"Remediation Evidence Review"** .
3.  The **ACT Lead** and, for technical findings, the **CISO**'s delegate, review the closure evidence. If the evidence substantiates closure, the finding is substantively closed in JSM.
4.  Closure evidence is then submitted to the external auditor for validation during the subsequent audit cycle's bridge letter or interim review period.

#### 5.4.3 HIPAA-Specific Reporting Obligations

If during the course of any external audit, evidence reveals a breach of unsecured PHI as defined in 45 CFR § 164.402, the standard incident response procedure (SOP-SEC-007) is immediately triggered. The ACT Lead must immediately halt submission of that specific evidence artifact and notify the GC and DPO. The finding is then managed exclusively under breach notification protocols, which are outside the scope of this audit coordination SOP but must be resolved prior to providing a final management representation to the auditor regarding HIPAA compliance.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

#### 6.1.1 Non-Disclosure Agreements
All external auditor personnel assigned to a Meridian engagement must execute the Meridian Standard NDA (Form LEGC-004-CA) prior to receiving credentials. The executed NDA is stored in the Legal Contract Repository (Ironclad) and linked to the engagement record in Vanta.

#### 6.1.2 Background Checks
Meridian reserves the right to request that its audit firms perform and attest to the completion of background checks for all individuals who will have unescorted access to Meridian facilities or logical access to production systems. The request must be made during RFP negotiations.

#### 6.1.3 Audit Trail Integrity
All Meridian-generated evidence, system logs, and access reports provided to auditors must be generated in a manner that ensures their integrity. No raw log data may be provided to auditors in an editable format (e.g., .csv, .xlsx) unless accompanied by a cryptographic hash (SHA-256) generated at the time of export. This safeguard directly supports the HIPAA § 164.312(b) requirement for mechanisms that record and examine activity in information systems that contain or use EPHI.

### 6.2 SOC 2 Availability Controls

Meridian maintains a comprehensive Availability commitment architecture designed to ensure the Meridian SaaS Platform meets its service delivery objectives. The Company's availability strategy is built on the following control pillars:

#### 6.2.1 Environmental Protections and Redundancy
All production systems operate in a multi-Availability Zone (AZ) configuration within AWS us-east-1 and eu-west-1 regions. Core platform components, including the application load balancers, compute auto-scaling groups, and the primary Aurora PostgreSQL database cluster, are deployed with redundancy across AZs. The Company maintains documented failover procedures that describe the operational steps required to restore service in a secondary region in the event of a catastrophic primary region failure.

#### 6.2.2 Monitoring and Incident Response
Availability monitoring is performed continuously through Datadog synthetics and CloudWatch alarms. A dedicated Site Reliability Engineering (SRE) rotation provides 24/7/365 response coverage. Incident response is executed according to SOP-SEC-007 (Incident Response), which defines Severity 1 (SEV1) as a critical platform outage impacting all tenants. During a SEV1 event, the CISO and VP of Engineering are mobilized, and the primary objective is to restore service functionality as expeditiously as the nature of the incident permits, with a general organizational posture of restoring critical services within hours and non-critical services within days.

#### 6.2.3 Capacity Management and Backups
The SRE team performs monthly capacity planning reviews against forecasted demand. Database backups are performed via AWS Backup service, with continuous point-in-time recovery (PITR) enabled for the primary Aurora cluster. Backup integrity is validated through a quarterly restoration test to an isolated recovery environment. For the HealthPay Financial Services system, a supplementary backup process writes transaction ledgers to an immutable, WORM-compliant S3 bucket every fifteen (15) minutes.

### 6.3 Logical Access Controls for Audit Evidence

#### 6.3.1 Access Control to the Document Vault
Access to the Meridian Document Vault (SharePoint Online) audit engagement sites is governed by RBAC. Access is provisioned by the IT Service Desk upon approval of a formal Access Request ticket submitted by the ACT Lead. The following roles exist:

| SharePoint Role | Permissions | Assigned Personnel |
|---|---|---|
| **Audit Owner** | Full Control | ACT Lead, CCO |
| **Audit Contributor** | Contribute (Read, Write, Delete own files) | Control Owners, designated scribes |
| **Audit Reader** | Read Only | Internal Audit, GC observers |
| **External Auditor** | Restricted Read Only (to specific folder) | External audit team members |

Access is provisioned for the duration of the audit engagement plus thirty (30) days for follow-up, after which all external auditor accounts are disabled. Access for internal roles is reviewed upon change of assignment or role.

### 6.4 HIPAA Administrative, Physical, and Technical Safeguards

In preparation for any HIPAA-focused audit, the evidence package for the following mandatory controls, organized by citation, must be pre-staged by the respective Control Owner.

| Citation | Safeguard Description | Control Owner | Key Evidence Artifact(s) |
|---|---|---|---|
| **45 CFR § 164.308(a)(1)(ii)(A)** | Risk Analysis (Administrative) | CISO | Current Asset Inventory, Threat Catalog, Vanta Risk Register with calculated risk scores and treatment plans. |
| **45 CFR § 164.308(a)(2)** | Assigned Security Responsibility | CCO | Formal appointment letter for the HIPAA Security Officer, published organizational chart reflecting dotted-line reporting to the Board's Audit Committee. |
| **45 CFR § 164.308(a)(3)(ii)(A)** | Authorization and/or Supervision of Workforce Members with Access to EPHI | Manager, People Operations | Signed Employee Handbook acknowledgments, documented quarterly supervisor reviews for Clinical AI staff. |
| **45 CFR § 164.308(a)(4)(i)** | Information Access Management: Isolating Healthcare Clearinghouse Functions | VP, HealthPay Platform | Network segmentation diagrams showing the logical isolation of HealthPay transaction processors from general corporate IT. |
| **45 CFR § 164.310(a)(1)** | Facility Access Controls (Physical) | Director, Physical Security | Access card reader logs for the Boston HQ data hall for the Audit Period, reviewed quarterly by a security supervisor. |
| **45 CFR § 164.310(d)(1)** | Device and Media Controls (Disposal and Re-use) | Director, IT Operations | Certificates of Destruction from Iron Mountain for decommissioned hard drives, asset disposal records from Jira. |
| **45 CFR § 164.312(a)(1)** | Unique User Identification (Technical) | Director, Identity & Access Mgmt. | Okta account import report showing a unique, non-shared User ID for every human and service account with PHI access. |
| **45 CFR § 164.312(b)** | Audit Controls (Technical) | Director, Security Engineering | Sumo Logic dashboard for Clinical AI Platform EPHI access events, configured to alert on any event indicating export or bulk download. |
| **45 CFR § 164.312(e)(1)** | Transmission Security | VP, Network Engineering | Architecture diagrams proving TLS 1.3 encryption for all EPHI data in transit across public networks; validated by Qualys SSL Labs scan reports. |
| **45 CFR § 164.316(b)(2)(i)** | Time Limit (Documentation Retention) | ACT Lead | Documented retention policy with a minimum six-year retention, and Vanta control showing automated archival of audit logs to AWS S3 Glacier Deep Archive. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The performance of the external audit coordination process is continuously measured against the following KPIs. These are reviewed monthly by the ACT Lead and quarterly by the CCO.

| KPI ID | Metric | Target | Measurement Method |
|---|---|---|---|
| **KPI-LEGC-04-1** | Audit Timeliness: Percentage of audits completed with the final report delivered by the contractual date. | 100% | Contract vs. actual report delivery date. |
| **KPI-LEGC-04-2** | Evidence Submission SLA Adherence: Percentage of RFEs submitted to the auditor by the Meridian internal SLA deadline. | ≥ 95% | JSM data, calculated monthly. |
| **KPI-LEGC-04-3** | Evidence First-Pass Quality: Percentage of evidence packages that pass the ACT Lead QA review without requiring rework. | ≥ 85% | JSM QA review status tracking. |
| **KPI-LEGC-04-4** | Finding Remediation On-Time: Percentage of Remediation Plan milestones completed on or before the scheduled date. | ≥ 90% | JSM milestone tracking. |
| **KPI-LEGC-04-5** | Overdue Findings: Number of Findings past their target closure date without an approved extension. | 0 | JSM overdue report, reviewed weekly. |

### 7.2 Reporting Cadence

| Report Name | Audience | Frequency | Contents | Owner |
|---|---|---|---|---|
| **Active Audit Status Report** | CCO, CISO, VP Engineering | Weekly (during active fieldwork) | RFE status, upcoming walkthroughs, blockers, auditor sentiment. | ACT Lead |
| **Finding Remediation Tracker** | CCO, GC, Control Owners | Bi-weekly | Open Findings, overdue milestones, remediation progress %. | ACT Lead |
| **Audit Universe Quarterly Summary** | Executive Risk Committee | Quarterly | Status of all planned audits, closed audits, Findings trending, resource utilization. | CCO |
| **Annual Compliance Assessment** | Board of Directors Audit Committee | Annually | Summary of all audit results, major Findings, remediation effectiveness, and the forward 18-month audit schedule. | CCO & GC |

### 7.3 Dashboards

A real-time dashboard shall be maintained in Jira JSM and is accessible to all Control Owners, the CCO, and the CISO. The dashboard displays:
- A list of all active open RFEs, sorted by due date and priority.
- A burndown chart of open Findings over the current fiscal quarter.
- A pie chart of Finding severity (Material Weakness, Significant Deficiency, Other).
- The current status of each active Remediation Plan.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling

Deviations from the procedures or SLAs defined in this SOP require a formal exception. An exception is defined as any instance where an SLA is breached, a required piece of evidence cannot be produced, or a procedural step must be bypassed.

#### 8.1.1 Procedure for Requesting an Exception

1.  The **Control Owner** or **ACT Lead** identifies the need for an exception and creates an "Exception Request" issue type in the External Audit Findings JSM project.
2.  The request must include:
    -   The specific procedure or SLA from which the deviation is sought.
    -   A clear business justification for the deviation.
    -   An assessment of the risk created by the deviation and any compensating controls that will be put in place during the exception period.
    -   A proposed duration for the exception, not to exceed one (1) audit cycle.
3.  The ticket is routed for approval as defined in the table below.

| Exception Type | Approver |
|---|---|
| Extension to an internal RFE SLA (less than 5 business days) | ACT Lead |
| Extension to an internal RFE SLA (greater than 5 business days) | CCO |
| Inability to produce required HIPAA evidence artifact | CCO and CISO (joint) |
| Deviation from a policy statement (P-001 through P-005) | Maria Gonzalez, GC |
| Request to bypass the internal Peer Review step for an evidence artifact | ACT Lead (for P4 artifacts only) |

### 8.2 Escalation

The following triggers mandate an immediate escalation via the JSM "Escalation" workflow, which automatically notifies the CCO and logs the event for the next quarterly Executive Risk Committee review:

-   **Auditor Dispute:** An external auditor formally disputes a Management Response.
-   **Dead Letter:** An RFE ticket has been awaiting a Control Owner response for more than 72 hours past its internal SLA deadline.
-   **Control Failure:** Evidence provided for a control reveals a systemic failure, not just a single missed instance.
-   **Discovery of PHI Breach:** As noted in Section 5.4.3.
-   **Attempted Fraud/Concealment:** Any suspicion of evidence fabrication.

---

## 9. Training Requirements

### 9.1 Mandatory Training Modules

All personnel with designated roles in the RACI matrix (Section 3.1) must complete the following training. Completion is tracked via the Workday LMS. Non-completion within the required timeframe results in revocation of system access relevant to audit coordination and a formal notification to the individual's direct manager.

| Training Name (Workday ID) | Target Audience | Frequency | Content |
|---|---|---|---|
| **External Audit Preparedness (SEC-AUD-101)** | All Control Owners, Peer Reviewers, ACT members | Annually (before start of FY audit season) | This SOP, Evidence Collection Standard, how to conduct a walkthrough, handling difficult auditor questions. |
| **HIPAA for Engineers (CMPL-HIPAA-201)** | All Control Owners for systems touching EPHI | Annually | Practical application of the Security Rule, PHI vs. de-identified data, incident recognition and reporting. |
| **Audit Liaison and Communications (CMPL-AUD-301)** | ACT Team, CCO direct reports | Bi-annually | Advanced communications techniques, managing auditor relationships, responding to preliminary findings. |

### 9.2 Role-Based Training Verification

Prior to the commencement of any audit fieldwork, the **ACT Lead** must pull a training compliance report from Workday. Any in-scope personnel not 100% compliant with their assigned training modules are flagged to the CCO. The CCO has the authority to replace a non-compliant Control Owner for the duration of the audit engagement.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP-ID | Document Title | Relationship to This SOP |
|---|---|---|
| SOP-LEGC-001 | Internal Audit Program | Defines the internal audit function; external audit findings may be fed into internal audit planning. |
| SOP-LEGC-002 | HIPAA Privacy and Security Compliance Program | Foundational HIPAA governance document; this SOP operationalizes the audit component. |
| SOP-SEC-001 | Information Security Policy | Defines the overarching security controls tested during SOC 2 and ISO 27001 audits. |
| SOP-SEC-007 | Incident Response Procedure | Triggered by any audit discovery of a breach or critical security event. |
| SOP-SEC-008 | Third-Party Risk Management | Governs client questionnaires, which are separate from but informed by external audit results. |
| SOP-PLAT-001 | Change Management Policy | Defines the change control processes examined during audits for Processing Integrity. |
| SOP-HR-002 | Employee Code of Conduct and Disciplinary Action | Referenced for consequences of evidence fabrication or misrepresentation. |
| SOP-PEOP-001 | Employee Background Check Policy | Evidence source for personnel controls audited under SOC 2 and HIPAA. |

### 10.2 External Standards and Regulations

-   **AICPA:** *SSAE No. 22, AT-C Section 205 and 320* (SOC 2 examinations)
-   **U.S. Dept. of Health and Human Services:** *45 CFR Part 160 and Part 164, Subparts A, C, and E* (HIPAA Security and Privacy Rules)
-   **HITRUST Alliance:** *HITRUST CSF v11.2*
-   **ISO/IEC:** *27001:2022 Information Security Management Systems - Requirements*
-   **FDA:** *21 CFR Part 820* (Quality System Regulation)
-   **European Union:** *Regulation (EU) 2017/745* (Medical Device Regulation)

---

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
|---|---|---|---|
| 1.0 | 2019-03-15 | J. Miller (former CCO) | Initial document created in response to first SOC 2 Type I engagement. |
| 2.1 | 2020-09-22 | T. Anderson | Major revision to incorporate Findings remediation workflow and the JSM-based RFE process. Introduced the formal "ACT" role. |
| 2.5 | 2021-05-07 | M. Gonzalez | Legal review and update following auditor access dispute; strengthened P-003 (Truthful Representation) and added GC oversight to Phase 1. |
| 3.0 | 2022-11-15 | J. Walsh, T. Anderson | Complete redraft to align with Vanta implementation and automated evidence collection. Added detailed HIPAA safeguards table (Section 6.4). Introduced KPIs. |
| 3.3 | 2024-01-10 | D. Chen | Updated Section 6.2 Availability Controls and IAM references for Okta SSO migration. |
| 3.5 | 2024-09-30 | J. Walsh | Added EU MDR CE marking audit stream and DPO role. Updated RACI. |
| 3.7 | 2025-12-22 | J. Walsh, T. Anderson, M. Gonzalez | Annual review. Updated for HealthPay WORM backup procedure. Refined SLA targets based on FY25 KPI data. Added Section 5.4.3 HIPAA Breach Discovery Protocol. Added Section 9.2 Training Verification pre-audit checkpoint. Current version. |