---
sop_id: "SOP-HR-017"
title: "Employee Data Subject Access Requests"
business_unit: "Human Resources"
version: "3.8"
effective_date: "2025-05-10"
last_reviewed: "2026-04-18"
next_review: "2026-10-14"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Employee Data Subject Access Requests

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the framework, governance, and operational processes for managing Data Subject Access Requests (DSARs) submitted by current and former employees, contractors, interns, and applicants (collectively, “Data Subjects”) of Meridian Health Technologies, Inc. and its global subsidiaries. This SOP ensures that Meridian fulfills its obligations under Articles 12, 15, and related provisions of the General Data Protection Regulation (GDPR), as well as complementary requirements under applicable state and federal laws, while maintaining the security and integrity of its data assets.

### 1.2 Scope

**In-Scope Entities and Geographies:**
- All Meridian Health Technologies, Inc. legal entities, including Meridian Health Technologies UK Ltd., Meridian Health Technologies GmbH (Berlin), Meridian Health Technologies Singapore Pte. Ltd., and Meridian Health Technologies Canada, Inc.
- All physical offices (Boston HQ, London, Berlin, Singapore, Toronto) and remote employees working in jurisdictions covered by GDPR or equivalent privacy legislation.

**In-Scope Data Subjects:**
- Current full-time and part-time employees.
- Former employees (retention period of HR records plus active DSAR window).
- Independent contractors and consultants classified as data subjects under GDPR.
- Interns, apprentices, and trainees.
- Job applicants who have submitted applications through Meridian’s Greenhouse ATS.
- Dependents and beneficiaries whose personal data is processed for benefits administration.

**In-Scope Processing Activities and Systems:**
This SOP covers all personal data processed in the context of employment, including but not limited to data held within the following Meridian systems:

| System / Platform | Data Categories |
| :--- | :--- |
| Workday (HRIS) | Core HR records, compensation, performance reviews, disciplinary records, emergency contacts, employment history, education, certifications |
| Greenhouse (ATS) | Application materials, interview notes, assessment scores, offer letters |
| ADP Workforce Now (Payroll) | Salary, bank account details, tax withholdings, benefits deductions |
| Culture Amp (Engagement/Performance) | Performance review narratives, 360-degree feedback, engagement survey responses |
| Azure Active Directory / Okta | Login timestamps, access logs, group memberships, authentication tokens |
| Slack Enterprise Grid | Direct messages, channel communications (in scope only if related to a formal HR matter) |
| Microsoft 365 (Exchange, SharePoint, OneDrive) | Emails, documents within HR and manager folders relevant to the employee |
| ServiceNow HR Service Delivery | HR case tickets, accommodation requests, leave requests |
| AWS SaaS Platform Access Logs | User access and activity timestamps for Meridian systems |
| Jira/Confluence (Engineering/IT) | Performance-related tickets, project activity metadata for performance management |

**Out-of-Scope:**
- Anonymized or pseudonymized data that cannot be re-identified by Meridian using reasonable means (per Recital 26, GDPR).
- Data processed solely in the context of Meridian's business operations where the employee is incidentally mentioned (e.g., a patient record referencing a care manager) — these are handled under the separate **SOP-PRIV-005 (Patient Data Subject Access Requests)** .
- Privileged legal communications protected by attorney-client confidentiality.
- Unstructured personal notes held by managers that are not intended for filing or shared disclosure, provided they are strictly personal and not stored on corporate systems.

This SOP applies to DSARs received on or after the effective date. Pending DSARs will be transitioned to this version’s process map within 10 business days.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **Data Subject Access Request (DSAR)** | A formal request made by a Data Subject to access their personal data, as provided under Article 15 of the GDPR, and complementary rights under Articles 13-22. |
| **Personal Data** | Any information relating to an identified or identifiable natural person (Article 4(1) GDPR). |
| **Data Subject** | The identified or identifiable natural person to whom personal data relates. In this SOP, the employee, former employee, contractor, or applicant. |
| **Controller** | The entity which, alone or jointly, determines the purposes and means of the processing of personal data. For HR data, Meridian is the Controller. |
| **Processor** | An entity that processes personal data on behalf of the Controller. Examples: ADP (Payroll), Culture Amp (Performance). |
| **Profiling** | Any form of automated processing of personal data evaluating personal aspects relating to a natural person, in particular to analyze or predict performance at work, economic situation, health, personal preferences, reliability, or behavior (Article 4(4) GDPR). |
| **DSAR Portal** | Meridian’s self-service platform hosted on OneTrust DSAR, located at privacy.meridianhealth.com. |
| **DSAR Triage Team** | The cross-functional team responsible for initial intake, validation, and assignment of DSARs. |
| **Identity Verification (IDV)** | The process of confirming a requester’s identity to a level of high assurance before releasing personal data. |
| **Manifestly Unfounded** | A request where the Data Subject has no genuine interest in accessing their data, or the request is malicious in intent, with no basis in fact (e.g., a request made to cause disruption). |
| **Manifestly Excessive** | A request that is clearly unreasonable based on objective evidence, such as repetitive identical requests within short intervals, despite being informed of the previous response. |
| **OneTrust** | Meridian’s enterprise privacy management platform used for DSAR workflow automation, data discovery, redaction, and secure response delivery. |
| **DPO** | Data Protection Officer (a designated role, currently outsourced to TrustArc DPO Services, acting as Meridian’s statutory DPO per Article 37). |
| **ROPA** | Record of Processing Activities. |
| **SLA** | Service Level Agreement. |

---

## 3. Roles and Responsibilities

The following RACI matrix assigns responsibility for activities critical to the DSAR lifecycle.

| Activity / Task | Data Subject | CHRO (Jennifer Walsh) | DPO (TrustArc) | DSAR Triage Team (HR Operations) | Legal (Privacy – GC Office) | IT / Information Security (CISO: Daniel Park) | HR Business Partner | External Processor (e.g., ADP) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DSAR Intake & Acknowledgment** | R | I | C | R, A | I | I | I | I |
| **Identity Verification (IDV)** | C | I | I | R, A | I | R (Tool Support) | I | I |
| **Request Validation (Scope)** | I | C | C | R | R, A | I | I | I |
| **Data Discovery & Collection** | I | I | I | R | C | R | C | R |
| **Manual Review & Redaction** | I | I | I | R | R (Third-party data) | I | R | C |
| **Applying Exemptions** | I | A | C | R | R (A for Legal Privilege) | I | I | I |
| **Final Response Preparation & Send** | I | A | C | R | I | I | I | I |
| **Escalation / Dispute Resolution** | I | A | R, C | I | C | I | I | I |
| **Metrics & Reporting** | I | R | A | I | I | I | I | I |

**Named Role Details:**

- **Chief Human Resources Officer (Jennifer Walsh):** Owner of this SOP. Provides executive sign-off on disputed exemptions exceeding standard parameters. Responsible for oversight of HR data schemas and ensuring Workday data mapping is current for DSAR fulfillment.
- **Data Protection Officer (via TrustArc DPO Services):** Provides advisory consultation on complex Article 15 interpretations. Mandatory escalation point for requests involving cross-border data transfer information or sensitive data under Article 9. Co-signs off on any refusal to act based on Article 12(5).
- **DSAR Triage Team:** A designated sub-team within HR Operations. Current lead: Sarah Jenkins, Manager, HRIS & People Analytics. Team members: 2 dedicated HR Operations Specialists. Responsible for day-to-day execution.
- **Legal Counsel, Privacy & Employment (Alicia Voss):** Reviews all redactions invoking third-party privacy. Sole authority to invoke legal privilege exemptions.
- **Chief Information Security Officer (Daniel Park):** Ensures IT systems can support forensic, complete data searches. Accountable for the secure transfer technology (OneTrust Secure Link).

---

## 4. Policy Statements

Meridian Health Technologies commits to the following high-level policy principles in the execution of all Employee DSARs:

1. **Lawfulness, Fairness, and Transparency:** All personal data collected and processed for HR purposes is cataloged in the HR ROPA, available on the employee intranet. Data Subjects will not be reprimanded, coerced, or disadvantaged for exercising their access rights.
2. **Purpose Limitation:** Data collected for employment purposes will not be repurposed for non-compatible uses without specific notification as per Article 5(1)(b).
3. **Data Minimization:** The response process will adhere strictly to Article 15. Where Meridian relies on Article 15(4) (adversely affecting the rights and freedoms of others), redactions will be minimally invasive.
4. **Accuracy:** DSARs provide an avenue for employees to verify the accuracy of their data. Any identified inaccuracies will be rectified within 5 business days per **SOP-HR-018 (Rectification and Erasure)** .
5. **Storage Limitation:** Meridian maintains a strict HR data retention schedule. Data held beyond the schedule due to legal hold, DSAR fulfillment, or statutory obligation will be flagged to prevent accidental deletion before request completion.
6. **Security:** All DSAR responses will be transmitted exclusively through the OneTrust Secure Link portal with Two-Factor Authentication (TFA) and AES-256 encryption at rest and in transit.
7. **Accountability:** All decisions regarding scope, exemptions, and extensions will be fully documented in OneTrust with an audit trail capturing the date, time, actor, and justification.
8. **Non-Discrimination:** No employee or applicant will be subject to adverse employment action as a consequence of submitting a DSAR. Any such action is a violation of the Meridian Code of Conduct and will be subject to disciplinary action, up to and including termination.

---

## 5. Detailed Procedures

The DSAR lifecycle is governed by strict, measurable SLAs. The default statutory timeline for a substantive response is **30 calendar days** from the day after receipt of the request (or successful IDV). Where complexity warrants, the timeline may be extended by a maximum aggregate of an additional two months (60 calendar days total).

### 5.1 Intake and Recording

All requests, regardless of channel, must be centrally logged.

1. **Authorized Channels:**
    - **Primary:** DSAR Portal (`privacy.meridianhealth.com`). This is the only self-service channel.
    - **Secondary:** Direct email to `dpo@meridianhealth.com` (monitored by DPO and HR Operations).
    - **Tertiary (Verbal):** An employee may verbally express a desire to make a DSAR to their HR Business Partner or Manager. This must be captured on a standard “Verbal DSAR Intake Form” (Form HR-017-VRB) and emailed to `dsar_hr@meridianhealth.com` within 4 business hours.

2. **Acknowledgment of Receipt:**
    - Upon receipt via written channel, the DSAR Triage Team will send an automated acknowledgment via OneTrust within **24 hours** (excluding weekends/holidays). The acknowledgment includes:
        - Case reference number (e.g., `DSAR-EMP-2026-04-15-001`).
        - Link to the Meridian Employee Privacy Notice.
        - A statement that the statutory clock does not start until IDV is completed.
        - Clear instructions for IDV (see Section 5.2).

### 5.2 Identity Verification (IDV)

It is critical to prevent unauthorized disclosure. Identity must be verified to a "Reasonable Certainty" standard.

1. **Self-Service (Portal):** Employees authenticated via Okta Single Sign-On (SSO) are considered verified for simple requests (standard Workday extract). If a former employee or applicant, or a current employee with deactivated Okta, submits a request, IDV is required.

2. **IDV Matrix:**
    Meridian uses a tiered IDV approach:
    - **Tier 1 (Low Sensitivity):** Confirmation of name, address, DOB, and last four digits of employee ID. If matched to Workday, IDV is passed.
    - **Tier 2 (Medium Sensitivity – Request involves performance reviews, Slack/email content):** Tier 1 plus one additional government-issued ID (scanned, provided via OneTrust secure upload). HR Triage visually matches the ID to HR file photo. ID is not retained; a case note “ID Verified via [Document Type]” is logged.
    - **Tier 3 (High Sensitivity – Request involves special categories of data, health records, or request is for a former employee long departed):** Tier 2 plus a recorded video call verification with a DSAR Triage specialist.

3. **Outcome:** IDV must be completed within **5 calendar days** of request receipt. If the employee fails to provide required ID within this period, a reminder is sent. After 15 calendar days of inactivity, the request is closed as “Withdrawn – Failed IDV,” with a closure note sent to the non-corporate email on file.

4. **Statutory Clock Start:** The 30-day clock begins the day after successful Tiered IDV is completed and recorded in OneTrust.

### 5.3 Scoping and Clarification

The DSAR Triage Team leads the scoping phase.

1. **Initial Scoping Meeting:** Within 2 business days of clock start, the Triage Team holds a 15-minute scoping meeting. The aim is to clarify the request’s scope. Is the Data Subject looking for everything, or a specific slice? (e.g., “All my performance reviews for 2024,” “My payroll data,” “Emails my manager sent to HR about my maternity leave request”).

2. **Scope Clarification Email:** If the request is broad (e.g., "Give me all my data"), Meridian will, under Article 12(2), seek to specify the request by providing a structured list of HR data categories and processing activities, as listed in Section 1.2. The Data Subject is entitled to a comprehensive response, but this assists with efficient triage.

3. **OneTrust Data Discovery:** The scoped request is formally launched in OneTrust. The system sends automated data discovery tasks to:
    - System Owner: Workday (HRIS Manager)
    - System Owner: ADP (Payroll Manager)
    - System Owner: Greenhouse (Talent Acquisition Director)
    - Etc., per the specific data map.
    - Discovery tasks include specific folder paths on SharePoint: `HR > Employee_Records > [Employee_ID]`, `HR > Performance > [Employee_ID]`.

4. **Discovery SLA:** All named System Owners must complete data pulls and confirm completeness within **7 calendar days** of receiving the automated task. Failure results in escalation per Section 8.

### 5.4 Data Collection and Assembly

The HR Operations Specialist assigned to the DSAR is the central point of collection.

1. **Collation:** Raw data is collected from all system owners into a secure OneTrust staging area. Data formats:
    - Structured data (Workday Report, ADP Payroll History) exported as `.csv` or `.xlsx`.
    - Unstructured data (emails, Slack logs, manager notes) exported as `.pst` or `.pdf` bundles.
    - A manifest of all collected data objects is generated.

2. **Metadata Preservation:** All original metadata (creation date, author, system of record) must be preserved and provided to the Data Subject as part of the response, as this information is itself personal data if it relates to the Data Subject.

### 5.5 Review, Redaction, and Privilege

This is the most critical and time-intensive step. No data must leave Meridian that would adversely affect the rights and freedoms of others (GDPR Art. 15(4)), reveal a trade secret, or breach legal privilege.

1. **Initial Automated Review:** Tools in OneTrust are used to flag high-confidence third-party data (e.g., Social Security Numbers, images of non-requesting individuals) for automatic redaction.

2. **Manual Line-by-Line Review:** The assigned HR Operations Specialist performs a manual review of all unstructured content using the following mandatory framework:

    | Review Lens | Guiding Question | Action |
    | :--- | :--- | :--- |
    | **Third-Party Data** | Does this document/email contain the personal data of a colleague, client, or patient? | Redact colleague names, contact details, and identifying attributes unless they are a direct work-related contact. Redact all patient data per HIPAA. Redact minor bystander information. |
    | **Legal Privilege** | Was this communication authored by or for the purpose of seeking legal advice from Meridian Legal Counsel? | Flag for Legal Counsel Voss. Must not be disclosed. |
    | **Confidential Business Information (Trade Secrets)** | Does the content expose proprietary algorithms, code that is a trade secret, or strategic company metrics not related to the employee? | e.g., internal M&A strategy, unreleased AI model details, system passwords. Redact. |
    | **Management’s Unrecorded Deliberations** | Is this a draft or a mind-map for making a management decision (e.g., preliminary succession planning notes)? | Recital 60 consideration. Redact if not filed and strictly for internal deliberation, but log decision carefully. |
    | **Mental Health or Harms Data** | Would disclosure of certain health or sensitive third-party data cause serious harm to any person? | Consult with DPO and Chief Medical Officer before disclosure. |

3. **Redaction Log:** Every redaction is recorded in a Redaction Log (template `HR-017-LOG`), including:
    - Document/Data Object Name.
    - Page/Line number.
    - Reason for Redaction (citing specific GDPR Article, Recital, or national law).
    - Reviewer Name and Date.

    The Redaction Log itself is a disclosable part of the response as it shows Meridian’s process, but it may be redacted if the log itself contains third-party data.

### 5.6 Profiling, Automated Decision-Making, and Logic

Under Article 15(1)(h), the Data Subject has the right to know about the existence of automated decision-making, including profiling.

1. **Profiling Assessment:**
    - **Culture Amp Insights:** If the employee’s engagement survey scores were used in a group profiling context (e.g., “flight risk” algorithm combining performance and survey data), the response must provide meaningful information about the logic involved (e.g., “An algorithm weighted your performance improvement plan status at 0.6 and recent survey sentiment at 0.4 to generate a retention risk score.”).
    - **Greenhouse AI Sift:** For applicants, if the AI sift feature (Meridian’s Pilot project in Q2 2025) was used, the response MUST include the fact of automated decision-making, provide meaningful information about the logic involved, and the significance and envisaged consequences. (Reference **SOP-TA-004**).
    - **No Profiling:** If no such processing occurred, the response explicitly states: “Meridian did not subject your personal data to any automated individual decision-making processes or profiling as defined under Article 4(4).”

### 5.7 Response Preparation and Secure Delivery

1. **Response Package Compilation:** The final response package is compiled in a structured, electronic format.
    - **Index:** A clear table of contents.
    - **Cover Letter:** Plain-language explanation of the processing activities, purposes, data categories, and legal basis under Article 6 and, where relevant, Article 9.
    - **Data:** Structured data in `.xlsx`, unredacted text in searchable `.pdf`.
    - **Redaction Log:** HR-017-LOG.
    - **Rights Statement:** Information on the right to rectification (Article 16), erasure (Article 17), restriction (Article 18), and the right to lodge a complaint with a supervisory authority.

2. **Quality Assurance (QA) Review:** A second HR Operations team member, not the primary assembler, performs a QA review against a standard checklist (`Template HR-017-QA`). QA verifies:
    - IDV was correctly passed.
    - No glaring unredacted third-party data remains.
    - The response correctly addresses the scope of the request.
    - All required Art. 15(1)(a)-(h) elements are addressed in the cover letter.

3. **Delivery Mechanism:**
    - The portal at `privacy.meridianhealth.com` alerts the Data Subject that their response is ready.
    - The link is to a OneTrust Secure Link that requires re-authentication via Okta (current employees) or a newly set up One-Time-Password (former employees) to download.
    - The file is a `.zip` archive, AES-256 encrypted. The password is transmitted via SMS to the number on file.
    - **Under no circumstances** will a raw, unencrypted `.csv` or `.zip` be sent via standard email.

### 5.8 Request Closure and Record Retention

Once the Data Subject downloads the file or the secure link expires (5 days after sending, with one reminder sent at Day 3), the request is closed.

1. **Closure Status:**
    - **Completed:** Data delivered.
    - **Withdrawn:** Data Subject formally withdraws.
    - **Rejected (Unfounded/Excessive):** Formal refusal letter sent with appeal instructions.

2. **Records Retention:** The full DSAR case file (including data collected, redaction log, correspondence, but NOT the final extracted data archive) is retained as a DSAR Processing Record for **6 years** from the date of closure, per Article 5(2) accountability requirements.

---

## 6. Controls and Safeguards

The following technical and organizational controls are implemented to ensure the confidentiality, integrity, and availability of the DSAR process.

### 6.1 Technical Controls

- **OneTrust Discovery Connectors:** API-based data pulls ensure data is not manually exported to unsecured local machines by system owners. The Workday and ADP connectors pull directly into the OneTrust staging environment.
- **Advanced Encryption Standard:** All data in transit (TLS 1.3) and at rest (AES-256).
- **Data Loss Prevention (DLP):** Meridian’s DLP solution (Microsoft Purview) is configured with rule sets to detect and block bulk transfers of HR data. Policy `DLP-HR-01` prevents exfiltration. OneTrust service accounts are whitelisted.
- **Access Restriction:** Access to the `DSAR Staging` area in OneTrust is restricted to the DSAR Triage Team, DPO, and Privacy Legal Counsel via role-based access control (RBAC).
- **Audit Trail:** Immutable audit logs track every action: Login, View Task, Edit Redaction, Generate Report, Send. Logs are shipped to Sumo Logic SIEM and retained for 10 years.

### 6.2 Administrative Controls

- **Mandatory QA Review:** 100% QA review by a second qualified HR Operations member on all responses involving unstructured data (emails, chat). This is a “two-person integrity” model.
- **Clean Desk Policy:** While processing, a clean desk policy is enforced. Printed documents (which are highly discouraged) must be shredded in cross-cut shredders immediately after QA sign-off.
- **NDA and Confidentiality:** All individuals in the RACI matrix are bound by specific data protection clauses in their employment contracts and the general Employee Handbook.
- **Processor Management:** External processors participating in data pulls (ADP, Culture Amp) are governed by strict Data Processing Agreements (DPAs) that bind them to assist Meridian in fulfilling DSARs within 10 calendar days.

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness and compliance of this process are continuously monitored.

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target | Measurement Method |
| :--- | :---: | :--- |
| **Timeliness: Response within 30 days** | ≥ 98% of non-complex requests | OneTrust DSAR Workflow Report |
| **Timeliness: Response within 60 days** | 100% (where Article 12(3) extension applied) | OneTrust DSAR Workflow Report |
| **Timeliness: IDV Completion** | ≤ 5 calendar days | HR Operations Manual Tracker |
| **Timeliness: Acknowledgment (within 24h)** | 100% | OneTrust Workflow |
| **Quality: Post-completion QA Audit Score** | ≥ 95% compliance score | Quarterly DSAR Quality Audit (by DPO) |
| **Request Volume** | Count per month | OneTrust DSAR Dashboard |
| **Invalid/Unexercised Requests** | Rate, monitored for abuse | OneTrust DSAR Dashboard |

### 7.2 Reporting Cadence

- **Monthly DSAR Operations Dashboard:** Sent to CHRO, DPO, and HR Operations Lead. Includes volume by workforce type (employee, applicant, former), mean time to respond (MTTR), cycle time per stage, and reasons for extensions/exemptions.
- **Quarterly Data Protection Business Review:** A formal review chaired by the DPO with CHRO, CISO, and General Counsel. Reviews process adherence, audit outcomes, root cause analysis of any breached SLA, regulatory updates, and technology roadmap (e.g., automated unstructured data redaction AI pilot). A formal Red-Amber-Green (RAG) status is assigned to the overall DSAR process health.

---

## 8. Exception Handling and Escalation

Strict adherence to the 30-day timeline is required.

### 8.1 Standard Extension (Article 12(3))

- **Authorized Grounds:** Request is complex OR the Data Subject has made multiple related requests. “Complex” is defined as a DSAR requiring data from ≥5 distinct systems or manual review of ≥1,000 unstructured data items.
- **Procedure:** The case must be flagged "Extension Required" in OneTrust. The DSAR Triage Lead must draft a formal notification to the Data Subject within the first 30-day window, citing the reasons for delay and informing them of their right to lodge a complaint with the applicable supervisory authority (e.g., UK ICO, Berlin DPA). This is sent via the portal.
- **Approval:** No formal approval needed; DPO is notified via automated OneTrust report.

### 8.2 Denial (Manifestly Unfounded or Excessive – Article 12(5))

A request may be refused only on objective, documented grounds.

1. **Definition Triggers:**
    - **Excessive:** Fourth identical DSAR from the same employee in a 12-month period, with no significant change in circumstances or processing.
    - **Unfounded:** A request clearly made to harass (e.g., a formal DSAR followed by a message “I’m going to make your life miserable with these until you pay me X”).

2. **Escalation Path:**
    - DSAR Triage Lead documents the evidence of excessiveness/unfoundedness in the case log.
    - **Escalation to:** DPO (TrustArc) and Legal Counsel (Alicia Voss).
    - **Decision Authority:** Joint decision, documented. They assess Meridian’s ability to demonstrate the intent or disproportionate burden.
    - **CHRO Notification:** Jennifer Walsh is informed for awareness before any refusal is sent.
    - **Response to Data Subject:** A formal letter is sent citing the reasons, informing the right to appeal within Meridian, and the right to complain to the applicable Data Protection Authority.

### 8.3 Emergency Data Breach Escalation

If during DSAR processing a significant unrelated data breach is discovered (e.g., an HR file incorrectly mapped containing a thousand SSNs), the DSAR process pauses for that item. The CISO is immediately contacted under **SOP-SEC-003 (Incident Response Plan)** . The DSAR clock continues running; an extension may be needed exclusively on the grounds of security investigation, but the remainder of the DSAR continues.

---

## 9. Training Requirements

All personnel assigned responsibilities in this SOP must be competent and aware.

| Role / Audience | Training Module | Delivery Method | Frequency | Learning Management System (LMS) Record |
| :--- | :--- | :--- | :---: | :--- |
| **DSAR Triage Team & HR Ops** | `LMS-DSAR-201: Advanced DSAR Handling & Redaction` | Instructor-Led (Alicia Voss / TrustArc) | Annual | Cornerstone LMS |
| **DSAR Triage Team & HR Ops** | `LMS-DSAR-202: Redaction Best Practices Using Adobe Pro & OneTrust` | Hands-on Workshop | Annual | Cornerstone LMS |
| **HR Business Partners** | `LMS-DSAR-101: Recognizing a DSAR and Intake Protocol` | eLearning (15 min) | Annual | Cornerstone LMS |
| **Managers / All People Leaders** | `LMS-DSAR-100: DSAR Awareness – The Right to Access` | eLearning (10 min) | New Hire Onboarding | Cornerstone LMS |
| **IT System Owners** | `LMS-DSAR-203: Technical Discovery Obligations for SysAdmins` | Live Technical Briefing | Biannual | Cornerstone LMS |

**Tracking and Remediation:** Completion rates are reported quarterly. Non-compliance with training by the deadline results in escalating reminders, and after 30 days of non-compliance, an email to the employee’s manager. Repeated failure is a performance issue.

**Phishing and Social Engineering Tests:** Quarterly, the Information Security team sends targeted phishing simulations mimicking DSAR portal notifications. Click-through rates are reported to the CISO and CHRO as part of the DSAR security health metric.

---

## 10. Related Policies and References

| SOP / Policy ID | Document Title | Relationship |
| :--- | :--- | :--- |
| **SOP-PRIV-005** | Patient Data Subject Access Requests | Process for patient/care personal data; distinct from HR. |
| **SOP-HR-018** | Employee Data Rectification and Erasure | Handles linked requests under Arts. 16-17 that often follow a DSAR. |
| **SOP-HR-015** | Employee Records Retention and Disposal | Defines the retention schedules referenced herein. |
| **SOP-SEC-003** | Information Security Incident Response | Activated if a breach is discovered during DSAR processing. |
| **SOP-LGL-001** | Legal Hold and eDiscovery | Priority handling if data is under legal preservation obligation. |
| **POL-CORP-001** | Global Data Protection Policy | Umbrella corporate policy for GDPR compliance. |
| **TEMP-HR-017-QA** | DSAR QA Checklist | Standard template for the mandatory QA review (Section 5.7.2). |
| **TEMP-HR-017-LOG** | DSAR Redaction Log | Mandatory log for all manual redactions. |
| **External Reference** | EU General Data Protection Regulation 2016/679, Arts 12, 15, 4, 5, 9, 14, 23 |
| **External Reference** | ICO Right of Access Detailed Guidance 2025 |

---

## 11. Revision History

| Version | Effective Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **3.8** | 2025-05-10 | Sarah Jenkins, HRIS Manager | **Major Revision.** Complete process re-engineering for OneTrust migration. Retired legacy SFTP manual process. Added detailed RACI, refined scope for contractors and Greenhouse ATS. Added Section 5.6 Profiling requirements. Updated timelines to match latest ICO guidance. |
| **3.5** | 2024-11-01 | Alicia Voss, Legal Counsel | **Technical Correction.** Retrofitted scope to align with the EU-U.S. Data Privacy Framework (DPF) requirements for HR data, specifically regarding access requests made by EU citizens in US context. Updated appeal language. |
| **3.2** | 2024-06-15 | Sarah Jenkins, HRIS Manager | **Process Enhancement.** Added formal QA step (Section 5.7.2). Implemented the DSAR Redaction Log (TEMP-HR-017-LOG) as a mandatory output. Updated response package format to include Rights Statement. |
| **3.0** | 2024-01-22 | Jennifer Walsh, CHRO | **Policy Overhaul.** Extended scope to all international subsidiaries post-Brexit and Schrems III alignment. Formal adoption of the 30-day clock. Added definitions for profiling. Replaced legal hold procedure reference. |
| **2.1** | 2023-09-05 | Daniel Park, CISO | Minor amendment. Added explicit encryption standards (TLS 1.3, AES-256) and delivery mechanism restrictions after security audit finding on a DSAR sent via unaudited email in Q3 2023. |