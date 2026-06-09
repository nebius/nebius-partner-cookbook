---
sop_id: "SOP-COPS-006"
title: "Complaint Resolution"
business_unit: "Customer Operations"
version: "2.1"
effective_date: "2025-01-15"
last_reviewed: "2026-08-08"
next_review: "2027-02-26"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "GDPR"
  - "SOC 2"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the centralized framework for receiving, documenting, investigating, resolving, and reporting on complaints received by Meridian Health Technologies, Inc. The purpose of this SOP is to ensure that all complaints are handled consistently, transparently, and in compliance with applicable regulatory standards, including but not limited to the General Data Protection Regulation (GDPR) and the Trust Services Criteria (TSC) for SOC 2 Type II certification. A robust complaint resolution mechanism serves as a critical feedback loop for product safety surveillance, service quality improvement, and maintaining customer trust across our Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.

### 1.2 Scope
This SOP applies to all directors, officers, full-time employees, part-time employees, contractors, and third-party service providers acting on behalf of Meridian Health Technologies, Inc. (collectively referred to as "Personnel") who may receive, process, or manage complaints from external parties.

This SOP covers complaints originating from:
- Healthcare providers and clinical staff using the Clinical AI Platform.
- Patients utilizing HealthPay Financial Services or whose data is processed by MedInsight Analytics.
- Health plan administrators and insurance partners.
- Merchants and billing departments integrated with HealthPay.
- Any individual exercising their data subject rights under GDPR or other privacy laws.

This SOP governs the entire complaint lifecycle, from intake through resolution, root cause analysis (RCA), and trend reporting. It applies irrespective of whether the complaint is received verbally, in writing, via electronic mail, through the customer portal, or via social media channels monitored by Customer Operations. It excludes internal HR grievances, which are managed under SOP-HR-014 ("Employee Relations and Grievance Policy").

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **ACR** | Adverse Complaint Report. A specific category of complaint pertaining to the Clinical AI Platform, where an alleged malfunction, inaccuracy, or design flaw is reported to have contributed to a near-miss or adverse clinical event. |
| **CAPA** | Corrective and Preventive Action. A structured process for identifying the root cause of a non-conformity and implementing actions to eliminate its recurrence. |
| **CCS** | Customer Complaint Summary. The formal record of a complaint logged in the centralized Salesforce Service Cloud (SFSC) instance. |
| **Complainant** | An individual or legal entity who submits a complaint. |
| **Complaint** | Any written, electronic, or oral communication that alleges deficiencies, errors, service failures, or misconduct related to Meridian's products, services, or data processing activities. A request to exercise a data subject right under GDPR is treated as a privacy-specific complaint under this SOP (see Section 5.5). |
| **DPIA** | Data Protection Impact Assessment. A process to help identify and minimize the data protection risks of a project. |
| **GxP** | Good Practice quality guidelines and regulations. |
| **HELD** | A software platform for managing adverse events, pharmacovigilance, and product safety. |
| **RCA** | Root Cause Analysis. |
| **SFSC** | Salesforce Service Cloud; the single Authoritative System of Record for all Meridian Customer complaints. |
| **SOC 2 TSC** | System and Organization Controls 2 Trust Services Criteria, specifically Common Criteria 3.1, 3.2, 3.3, 5.1, 5.2, and the Availability and Confidentiality criteria, as audited against annually. |
| **SOP** | Standard Operating Procedure. |
| **Triage** | The process of assessing a complaint's severity, regulatory reportability, and assignment priority. |

---

## 3. Roles and Responsibilities

A RACI (Responsible, Accountable, Consulted, Informed) matrix defines the interaction of cross-functional teams across the Complaint Resolution lifecycle.

| Activity / Decision Point | Customer Operations (Intake) | HR Ops (Triage) | VP Customer Operations (Owner) | Security Engineering | Legal & Compliance | Engineering / QA | VP of Business Unit (e.g., Clinical AI, FinSvcs) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intake & Acknowledgment** | **R/A** | I | I | I | I | I | I |
| **Initial Triage & Classification** | C | **R/A** | I | C | I | I | I |
| **GDPR Art. 15-22 Response Initiation** | I | **R** | C | C | **A** | I | I |
| **SOC 2 Logical Access Complaint Investigation** | I | C | I | **R/A** | I | C | I |
| **Clinical AI Adverse Event Assessment** | I | C | C | I | **R/A** | **R** | C |
| **Financial Error Transaction Reconciliation** | I | C | I | I | R | C | **A/R** |
| **RCA & CAPA Management** | I | R | I | R | R | **R/A** | C |
| **Complainant Close-Out Communication** | I | **R/A** | I | I | I | I | C |
| **Monthly KPI Review & Trend Analysis** | C | R | **A** | R | R | C | C |
| **Regulatory Report Filing (MDR, GDPR)** | I | R | I | I | **A** | C | C |

*Key: R = Responsible (does the work), A = Accountable (approves/signs off), C = Consulted, I = Informed.*

### 3.1 Named Role Assignments
- **Owner:** Michael Chang, VP of Customer Operations, is the business process owner for complaint handling and has authority over Tier 1 and Tier 2 escalations.
- **GDPR Authority:** The Meridian Data Protection Officer (DPO, currently part of the Legal & Compliance function) is the accountable party for all privacy-related complaints, including DSARs and data breach complaints.
- **Clinical AI Safety:** The Chief Medical Information Officer (CMIO) is accountable for the clinical evaluation of all ACRs in conjunction with QA.
- **Financial Services Resolution:** Robert Liu, VP of Financial Services, is the accountable executive for the resolution of complaints involving monetary errors, transaction disputes, or violations of payment card industry rules.

---

## 4. Policy Statements

Meridian Health Technologies, Inc. is committed to a customer-centric and risk-based approach to complaint handling. The following policy commitments guide all procedures defined herein:

1.  **Good Faith Principle:** All complaints are received on good faith. No complainant will face retaliatory action, service denial, or contract termination solely for submitting a complaint.
2.  **Timely Acknowledgment:** Every complaint logged in SFSC will receive an automated acknowledgment message to the Complainant’s registered email address within 24 hours of successful case creation.
3.  **Objective Investigation:** Each complaint will be investigated objectively, using documented procedures and, where necessary, by personnel independent of the subject of the complaint.
4.  **Data Confidentiality:** Complaint records contain highly sensitive personal and compliance information. Access to the SFSC Complaint object is granted based on a strict role-based access control (RBAC) model, adhering to the principle of least privilege.
5.  **Continuous Improvement:** Root Cause Analysis (RCA) findings will be translated into Corrective and Preventive Actions (CAPAs), tracked to closure, and verified for effectiveness as part of our quality management system.
6.  **Regulatory Adherence:** Meridian is committed to adhering to SOC 2 TSC for the security, availability, processing integrity, and confidentiality of customer data. This includes, but is not limited to, logical access controls, risk assessment, and system operations. For GDPR, Meridian respects and facilitates all enumerated data subject rights.

---

## 5. Detailed Procedures

This section outlines the systematic, phased approach to resolving a complaint.

### 5.1 Phase 1: Intake and Record Creation
Any Meridian Personnel receiving a complaint, regardless of channel, must direct the Complainant and the complete details to the official intake channel within four (4) business hours of receipt.

#### 5.1.1 Intake Channels
- **Primary:** Web-form on the Meridian Support Portal (support.meridian-healthtech.com).
- **Secondary:** Electronic mail directed to `complaints@meridian-healthtech.com` (generates auto-ticket).
- **Tertiary (Voice):** Call to the Customer Operations main line (1-800-MERIDIAN), where the agent will complete the web-form on the Complainant's behalf.
- **Physical Mail:** Scanned and uploaded to SFSC by the Corporate Mailroom within one business day of receipt.

#### 5.1.2 Record Creation in SFSC
Upon reception, the HR Ops Intake Team will create a Formal Customer Complaint Summary (CCS) record in SFSC. The CCS record MUST contain the following mandatory fields:

| Field | Description | Example |
| :--- | :--- | :--- |
| **CCS-ID** | Auto-generated unique identifier. Format: CCS-YYYY-NNNNN. | CCS-2026-000582 |
| **Complainant Name** | Full legal name of the individual or authorized entity representative. | Jane Doe |
| **Contact Preference** | Email, Phone, Post. Must be captured for all response timelines. | Email |
| **Complaint Source** | Dropdown: Portal, Email, Phone, Letter, Social Media, Other. | Phone |
| **Date Received** | Date and time complaint was first heard/received by any Meridian Personnel. | 2026-08-08T14:15:00Z |
| **Business Unit Impacted** | Dropdown: Clinical AI, MedInsight, HealthPay, SaaS Platform, Corporate. | Clinical AI |
| **Complaint Category** | Tier 1 pre-defined list, including 'Billing/Financial', 'Privacy/Data Subject Request', 'Clinical/Safety', 'Service/System Availability', 'Data Integrity', 'Other'. | Clinical/Safety |
| **Detailed Narrative** | Verbatim record of the complaint as stated by the Complainant, in quotes. | "The AI Model v2.3 consistently miscalculates the cardiovascular risk score for patients on Beta Blockers." |
| **Attachment(s)** | All associated screenshots, letters, or other supporting evidence. | Screenshot_20260808_1015.png |

The CCS record status must be set to "Open - Unassigned".

### 5.2 Phase 2: Triage, Criticality, and Assignment
Within four (4) business hours of a CCS record being saved as "Open - Unassigned", the HR Ops Compliance Triage Lead will perform the Triage step.

#### 5.2.1 Severity Classification
The complaint is assigned a Severity Level based on the documented definitions:

- **Severity 1 (Critical):** ACR involving patient harm, major HealthPay financial fraud impacting >50 patient accounts, a systemic data breach, or a complete Meridian SaaS Platform outage. **Required Action:** Trigger Major Incident Management (SOP-ITSM-001). VP Customer Operations and Legal notified immediately by phone and SMS.
- **Severity 2 (High):** A product non-conformance with potential but no confirmed harm, a privacy complaint requiring complex DSAR action, service unavailability impacting a single hospital department. **Required Action:** Case assigned to Senior Resolution Specialist. Department VP notified.
- **Severity 3 (Medium):** A standard service issue, documentation error, or a simple transactional complaint. **Required Action:** Case assigned to the standard resolution queue.
- **Severity 4 (Low):** A cosmetic issue, feature suggestion phrased as a complaint, or general feedback. **Required Action:** Case assigned for acknowledgment and closure, no formal investigation required.

#### 5.2.2 Assignment and SOC 2 Role Separation
The Triage Lead must verify that the assigned Resolution Specialist has no conflict of interest (e.g., was not the primary developer of the feature, nor directly involved in the event being complained about). This segregation of duties is a critical SOC 2 (TSC CC5.2) control to ensure objective investigations. The CCS record status is updated to "Open - Assigned".

### 5.3 Phase 3: Investigation
The assigned Resolution Specialist owns the investigation. The investigation methodology varies by `Complaint Category`.

#### 5.3.1 Standard Service Investigation (Non-ACR, Non-Privacy)
1.  **Engage:** Contact the Complainant within one (1) business day of assignment to confirm details, gather missing information, and set expectations for resolution.
2.  **Reproduce:** Attempt to reproduce the reported issue in a non-production Meridian sandbox environment.
3.  **Diagnose:** Use system logs in Splunk and application logs in Datadog to trace the error. Engage Engineering/QA as needed.
4.  **Validate:** If the issue is a known bug, validate it against the Known Error Database (KEDB) in ServiceNow and associate the CAPA tracker.
5.  **Document:** All investigation steps, findings, and code commits are logged in the SFSC Case Feed.

#### 5.3.2 Clinical AI Adverse Complaint Report (ACR) Investigation
1.  **Lock Case:** Upon a Category of "Clinical/Safety," the CCS record is immediately locked for read-only access to all except the Resolution Specialist, the CMIO, and the Legal & Compliance officer.
2.  **HELD Transfer:** All data is immediately transcribed to the Held platform for GxP-compliant adverse event management, creating a unique HELD ID. The HELD ID is cross-referenced back to the SFSC CCS-ID.
3.  **Clinical Review:** The CMIO performs a clinical evaluation to determine the "causality" and "seriousness" of the event. This evaluation is documented in HELD.
4.  **Product Investigation:** Quality Assurance performs a product defect investigation on the specific version of the AI model, including data drift analysis and training data integrity review. This is documented in a Product Investigation Report (PIR).

#### 5.3.3 Financial Service Complaint Investigation (HealthPay)
1.  **Transaction Reconciliation:** The Resolution Specialist extracts the complaint-specific transaction log from the core payment ledger. A three-way reconciliation is performed between the end-user report, Meridian's payment gateway log (Stripe/Cybersource), and the downstream acquirer bank report.
2.  **Forensic Analysis:** If fraud is alleged, the case is escalated to the Security Engineering team for forensic log analysis, preserving the chain of custody for all evidence.
3.  **Monetary Correction:** Any confirmed error resulting in a monetary loss for the Complainant is documented and processed for correction, subject to approval by the VP of Financial Services as per the delegation of authority matrix.

### 5.4 Phase 4: Resolution, Correction, and Closure
#### 5.4.1 Resolution Formulation
A resolution is formulated based on the investigation's root cause. The resolution is documented in a structured "Resolution Record" within the SFSC case, including:
- **Cause:** Specific technical or procedural root cause.
- **Correction:** Immediate action taken to resolve the issue for this specific Complainant (e.g., refund, account correction, workaround).
- **Corrective Action (CA):** Action to eliminate the root cause (e.g., code hotfix, server reconfiguration).
- **Preventive Action (PA):** Action to prevent recurrence across the system (e.g., new system monitoring alert, updated developer checklist, new automated test case).

#### 5.4.2 Communicating Resolution to Complainant
The Resolution Specialist communicates the outcome to the Complainant via their preferred contact method. The communication must be:
1.  **Clear:** Written in plain language, explaining the findings and the correction.
2.  **Complete:** Outlines the timeline for any corrective and preventive actions that directly affect the user.
3.  **Feedback-Oriented:** Includes a link to a feedback survey to gauge satisfaction with the complaint process.

#### 5.4.3 Case Closure
A case can only be moved to "Closed" status in SFSC by the Resolution Specialist when the following preconditions are met:
- [ ] The Resolution Record is completed and approved.
- [ ] The Complainant has been notified of the outcome (unless a silent fix for a systemic, non-critical bug that no user reported as a complaint; requires VP of Customer Operations approval).
- [ ] All linked CAPA records have been created in the Quality Management System.
- [ ] If the complaint is a GDPR DSAR, the response has been delivered (See 5.5).

### 5.5 GDPR-Specific Complaint Handling
This section addresses the handling of complaints that invoke data subject rights, specifically Articles 15-22 of the GDPR.

#### 5.5.1 Intake and Verification of Identity
When a complaint is categorized as "Privacy/Data Subject Request," the Resolution Specialist must first verify the identity of the requesting individual. A request for additional verification, such as a copy of a government-issued ID or a notarized affirmation of identity, may be requested. The case is not progressed until identity is verified to a standard of "reasonable certainty."

#### 5.5.2 Response Timelines
Once identity is verified, the DPO, acting as the Resolution Specialist, shall clarify the exact nature of the complaint (e.g., a request to access data under Art. 15, to rectify under Art. 16, to erase under Art. 17, etc.). The DPO will proceed to service the request using standard internal data mapping and retrieval tools.

The information required to respond shall be gathered and the response prepared. The resolution communication to the Complainant will be delivered, striving to meet the regulatory timeframe. Once the response is provided, the case is closed, with the closure reason set to "Data Subject Rights Fulfilled."

#### 5.5.3 DPIA Triggering
During the course of an investigation, a new processing activity or a systemic flaw may be identified that constitutes a high risk to the rights and freedoms of natural persons. In such circumstances, the DPO will initiate a Data Protection Impact Assessment (DPIA) process. The DPIA is conducted, recorded in the central DPIA register, and its findings may directly inform the preventive actions for the original complaint.

---

## 6. Controls and Safeguards

This section details the specific administrative and technical controls within the Complaint Resolution process, directly mapped to SOC 2 Trust Services Criteria (TSC) Common Criteria (CC) and Categories.

### 6.1 Control Objectives for SOC 2

| Control Activity | SOC 2 TSC Reference | Meridian Implementation Evidence |
| :--- | :--- | :--- |
| **Complaint Intake Integrity** | PI1.1: The entity obtains or generates, uses, and communicates relevant, quality information regarding the objectives related to processing. | SFSC form validation rules prevent submission of a CCS record without `Complainant Name`, `Date Received`, `Detailed Narrative`, and a `Category`. |
| **Segregation of Duties (SoD)** | CC5.2: Controls to segregate incompatible duties. | The Triage function in SFSC validates that the `Assigned To` user is not in the same role as the `Created By` user for Severity 1 & 2 complaints. This is enforced at the application workflow level. |
| **Investigation Objectivity** | PI1.4: The entity implements policies and procedures to ensure the integrity of processing. | Audit trails in SFSC and Linked Jira tickets show evidence of independent review for all ACRs and financial fraud complaints. The independent reviewer cannot be the individual who performed the initial action. |
| **Privacy and Confidentiality** | C1.1: The entity protects confidential information during its collection, use, storage, and disclosure. | The SFSC `CCS` record automatically masks the `Complainant Name` and `Contact Info` fields for all users not in the "Service Ops - Privacy" permission set. |
| **Logical Access Security** | CC6.1: The entity implements logical access security software, infrastructure, and architectures over protected information assets. | Access to SFSC is managed via Okta SSO, enforced by MFA, and provisioned based on a formally approved access request (SOP-IT-004). Access reviews are performed quarterly. |

### 6.2 Key Logical and Physical Controls
- **Audit Trail Integrity:** All fields on the SFSC `CCS` object are tracked. An immutable audit log records who changed what from what to what, and when. This data is streamed to our immutable Splunk archive. Audit logs cannot be deleted by any System Administrator for the retention period of 7 years.
- **Encryption:** All complaint data is encrypted at rest (AES-256) in Salesforce Shield and in transit (TLS 1.3).
- **Complainant Verification:** Before discussing any case-specific details, the agent must validate the complainant's identity using three-factor matching against the Customer Master Data Record: Name, Date of Birth (DOB), and last four digits of the account identifier.

---

## 7. Monitoring, Metrics, and Reporting

A robust system of monitoring ensures the complaint-handling process remains effective and identifies systemic risks early.

### 7.1 Key Performance Indicators (KPIs)
The performance of the complaint resolution process is measured against the following Service Level Objectives (SLOs). A monthly dashboard is published by the VP of Customer Operations.

| Metric | SLO (Target) | Measurement Methodology |
| :--- | :--- | :--- |
| **Customer Acknowledgment Time (All Sev)** | ≤ 24 hours from receipt | SFSC Report: `Date of Acknowledgment - Date Received` |
| **Mean Time to Triage (MTTT)** | ≤ 8 business hours | SFSC Report: `Date of Triage - Date Received` |
| **Mean Time to Resolution (MTTR) - Severity 2** | ≤ 5 business days | SFSC Report: `Date Closed - Date Assigned` |
| **Mean Time to Resolution (MTTR) - Severity 3** | ≤ 15 business days | SFSC Report: `Date Closed - Date Assigned` |
| **Complaint Rate per 1,000 Transactions** | < 0.5 | (Total Complaints / Total Platform Transactions) * 1000 |
| **Repeat Complaint Rate** | < 5% of total complaints | SFSC Report: Cases linked to a prior CAPA where the CAPA has been verified as effective. |
| **Complainant Satisfaction (CSAT)** | ≥ 85% positive | Post-closure survey data fed into Qualtrics dashboard. |

### 7.2 Reporting Cadence
- **Weekly Operational Review:** The Customer Operations Management team reviews open and aging cases (those exceeding 75% of MTTR target) every Monday at 10:00 AM ET.
- **Monthly Quality Review (MQR):** A cross-functional forum including representatives from Engineering, QA, Legal, and Customer Operations reviews all Severity 1 and 2 complaints, trend data, and CAPA status for the preceding month. The MQR is chaired by Michael Chang.
- **Quarterly Management Review (QMR):** A summary report is presented to the Executive Leadership Team (ELT) by Robert Liu, covering aggregate complaint KPIs, systemic issues, budget impacts, and major regulatory findings.

---

## 8. Exception Handling and Escalation

### 8.1 Escalation Path
Any Personnel member may raise an escalation if they believe a complaint is being misclassified, poorly investigated, or not given appropriate priority.

The formal escalation path is as follows:
1.  **Level 1:** Resolution Specialist's direct Supervisor (Customer Operations Manager).
2.  **Level 2:** VP of Customer Operations (Michael Chang). The escalator must articulate the reason for escalation in writing, referencing the CCS-ID. Michael Chang has the authority to reassign the case, adjust its severity, or authorize a deviation from standard procedures.
3.  **Level 3 (Final Escalation):** VP of Financial Services (Robert Liu) in his capacity as a Compliance Approver, for issues with material financial, legal, or reputational risk.

### 8.2 Exception Management
Any deviation from a procedural step defined in this SOP requires a formal Exception Request. The Resolution Specialist must log the exception in the `Exception Handling` custom object in SFSC, linked to the CCS record. The exception must state:
1.  The specific procedure step being deviated from.
2.  The reason for the deviation.
3.  The alternative control being applied to manage the risk.
4.  The approval signature of the Level 2 Escalation (Michael Chang).

All formally approved exceptions are reviewed at the Monthly Quality Review to identify procedures that may require a permanent revision.

---

## 9. Training Requirements

### 9.1 Initial Role-Based Training
All new Personnel in Customer Operations, Quality Assurance, and relevant Engineering functions must complete the following training *before* being granted access to SFSC or Held complaint records:

1.  **COPS-006-CBT-01:** "Complaint Resolution SOP Overview" (Computer-Based, 1.5 hrs).
2.  **COPS-006-WBT-02:** "Salesforce Service Cloud: Navigating the CCS Record" (Instructor-Led, 2 hrs).
3.  **COPS-006-CBT-03:** "Handling the Upset Customer: De-escalation, GDPR, and the Art of Objective Interviewing" (Computer-Based, 2 hrs). This module includes a specific knowledge check on distinguishing a complaint from a DSAR.
4.  **COPS-006-ILT-04:** "Clinical AI Adverse Complaint Reporting" (Instructor-Led, mandatory for Triage and Resolution Specialists handling Clinical AI, 4 hrs).

### 9.2 Recurring Annual Training
All Personnel covered by this SOP must complete the mandatory `Complaint Handling Refresher` (Course Code: COPS-006-RFR-01) annually by their initial training anniversary date. This refresher covers new regulatory guidance, process changes introduced by SOP version updates, and lessons learned from anonymized case studies.

### 9.3 Training Tracking
All training completion is automatically recorded in the HR Cornerstone LMS. Access to production SFSC is gated via a SAML attribute; personnel whose `Complaint Handling Training` record is past due are automatically placed into a "No-Access" Okta group, suspending their SFSC privileges until compliance is restored. The VP of Customer Operations reviews the departmental training compliance report monthly.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
| Document ID | Document Title |
| :--- | :--- |
| SOP-ITSM-001 | Major Incident Management Process |
| SOP-ITSM-003 | IT Service Desk and Support SOP |
| SOP-HR-014 | Employee Relations and Grievance Policy |
| SOP-IT-004 | Identity and Access Management (IAM) Procedure |
| SOP-INFRA-012 | Vulnerability and Patch Management Standard |
| SOP-QA-110 | Corrective and Preventive Action (CAPA) Management |
| SOP-QA-203 | Clinical AI Post-Market Surveillance (PMS) Plan |
| SOP-LEGAL-015 | GDPR Data Subject Access Request (DSAR) Handling |
| SOP-LEGAL-016 | Data Protection Impact Assessment (DPIA) Procedure |

### 10.2 External Standards and Regulations
- EU General Data Protection Regulation (GDPR) 2016/679, Articles 12-22, 35.
- EU Medical Device Regulation (MDR) 2017/745, Articles 83-89 on Post-Market Surveillance and Vigilance.
- AICPA TSP Section 100, 2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (TSC 100).
- ISO 10002:2018, Quality management -- Customer satisfaction -- Guidelines for complaints handling in organizations.

---

## 11. Revision History

| Version | Date | Author | Section(s) Changed | Change Summary |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 2023-03-10 | Jane Hopkins | All | Initial Release. Separated complaint handling from general support. |
| 1.1 | 2024-01-22 | Michael Chang | 5.5, 7.1 | Added dedicated GDPR complaint section; refined MTTR SLOs based on 1 year of data. |
| 2.0 | 2024-06-04 | Sarah Chen | 3, 5, 7.2 | Major Revision: Integrated Clinical AI and HealthPay business units post-acquisition. Added RACI, HELD system, and MQR forum. |
| 2.1 | 2025-01-15 | Michael Chang | 2, 9.3, 11 | Minor Revision: Updated definitions, formalized Okta-based training gating control for SOC 2, added revision history for v2.0. |
| 2.1 | 2026-08-08 | David Miller | All | Periodic Review: Confirmed roles post-reorg. No procedural changes. Next review set to Q1 2027. |