---
sop_id: "SOP-HR-004"
title: "Employee Termination and Offboarding"
business_unit: "Human Resources"
version: "3.5"
effective_date: "2025-09-28"
last_reviewed: "2026-09-18"
next_review: "2027-03-21"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Employee Termination and Offboarding
**SOP-HR-004 | Version 3.5**

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the formal framework for managing the separation of all employees from Meridian Health Technologies, Inc. The primary objectives are to protect the confidentiality, integrity, and availability of Meridian’s information assets and the sensitive data we process—including Protected Health Information (PHI), personally identifiable information (PII), proprietary algorithms, and financial data—by ensuring the timely and complete revocation of all logical and physical access rights. This SOP also defines the procedures for knowledge transfer, asset recovery, exit interviews, and adherence to legal and contractual obligations upon termination.

### 1.2 Scope
This SOP applies to all workforce members of Meridian Health Technologies, Inc. across all global offices (Boston, London, Berlin, Singapore, Toronto), business units (Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and Meridian SaaS Platform), and employment classifications. This includes full-time employees, part-time employees, temporary contractors, interns, and third-party personnel whose access to Meridian systems is directly terminated upon separation from the organization.

The scope encompasses all termination types, including voluntary resignations, involuntary terminations (with and without cause), reduction-in-force (RIF) events, contract non-renewals, and termination due to death or permanent disability. For contractors and third-party vendors, the formal notification of separation to the Meridian sponsor triggers this offboarding process.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **Access Revocation** | The technical act of disabling a user's ability to authenticate to or interact with any Meridian system, network, or facility. |
| **AM/IT** | Application Management / IT Operations, a function within the VP of IT Operations’ organization. |
| **Asset Recovery** | The process of reclaiming all Meridian-owned physical property, including laptops, mobile devices, access badges, keys, and peripherals. |
| **CISO** | Chief Information Security Officer (Rachel Kim). |
| **CPO/DPO** | Chief Privacy Officer and Data Protection Officer (Dr. Klaus Weber). |
| **Data Subject Access Request (DSAR)** | A formal request by an individual to exercise their rights under GDPR, such as access, rectification, or erasure of personal data. Refer to SOP-GDPR-003. |
| **Exit Interview** | A structured conversation conducted by Human Resources to gather feedback from a departing employee. |
| **IdP** | Identity Provider (Okta). The central system managing digital identities and authentication. |
| **ITSO** | Information Technology Security Officer, a senior member of the CISO’s team. |
| **Knowledge Transfer (KT)** | The process of a departing employee documenting and transferring their critical operational knowledge, pending tasks, and project status to a designated successor or manager. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **PII** | Personally Identifiable Information. |
| **ServiceNow** | The Meridian IT Service Management (ITSM) and HR Case Management platform used to orchestrate the offboarding workflow. |
| **SOC** | Security Operations Center, a 24/7 internal team within the CISO’s organization. |
| **Standard Separation** | A termination with at least five (5) business days of notice given by the employee or manager. |
| **Termination Date** | The final date of employment, signifying the end of the employer-employee relationship. Unless otherwise specified, the effective time for all offboarding actions is 5:00 PM on this date in the employee's local time zone. |

---

## 3. Roles and Responsibilities

The following matrix defines the Responsible (R), Accountable (A), Consulted (C), and Informed (I) parties for the core offboarding activities.

| Activity | HR Business Partner | Direct Manager | IT Service Desk (AM/IT) | InfoSec (CISO) | Payroll | Legal/Compliance |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Initiate Offboarding Case in ServiceNow | R, A | C | I | I | I | I |
| Communicate Termination to Employee | R, A | C | - | - | - | C |
| Plan and Execute Knowledge Transfer | I | R, A | - | - | - | - |
| Schedule & Conduct Exit Interview | R, A | - | - | - | - | I |
| Revoke Logical Access (Okta, SSO) | - | I | R, A | C | - | - |
| Recover Physical Assets (Laptop, Badge) | I | R, A | C | - | - | - |
| Lock Facility Access (Badge) | I | I | R, A | - | - | - |
| Secure PHI/PII Access (Audit) | - | - | C | R, A | - | C |
| Final Pay & Benefits Processing | C | I | - | - | R, A | C |
| Legal Hold Verification (Preservation) | - | I | C | C | - | R, A |

---

## 4. Policy Statements

4.1 **Immediate Separation Protocol:** For involuntary terminations deemed high-risk by HR and the CISO—including termination for cause related to security violations, intellectual property theft, or hostile behavior—the default protocol is immediate separation. The employee's manager, with HR and Corporate Security, will escort the individual from the premises immediately following the notification meeting. All logical access will be disabled at the moment of notification, not the end of the business day.

4.2 **Zero-Trust Access Revocation:** Upon the effective termination date, a departing employee’s access to all Meridian information systems and facilities must be fully and irrevocably revoked. Re-enablement of any account requires a new hiring process and cannot occur via a simple “unlock” of a disabled account.

4.3 **Data Integrity and Intellectual Property:** All data, work product, code, documentation, and communications created or stored by the employee on Meridian systems remain the exclusive property of Meridian Health Technologies. The manager is accountable for confirming all critical data is stored on corporate-controlled systems (Google Workspace, Snowflake, GitLab, etc.) and that no Meridian data will remain on personal devices or accounts.

4.4 **Data Minimization and Purpose Limitation:** Post-termination, Meridian will retain employee personal data only for the purposes and durations defined in SOP-HR-001 (Employee Records Management) and in strict compliance with the GDPR principle of storage limitation (Art. 5(1)(e)).

4.5 **Non-Disclosure and Post-Termination Obligations:** All employees are bound by their Employee Confidentiality, Invention Assignment, and Non-Compete Agreement irrespective of their separation. HR will provide a written reminder of these continuing obligations, including non-solicitation clauses and protection of trade secrets, during the offboarding process.

4.6 **Continuous Compliance Integration:** All offboarding procedures are designed to meet the control objectives of SOC 2 Common Criteria 6.2 (Access Termination), HIPAA Administrative Safeguards § 164.308(a)(3)(ii)(C) (Termination Procedures), and the foundational principles of the NIST AI RMF. For the termination of personnel with privileges to high-risk AI systems, as classified under the EU AI Act and managed through our Clinical AI Platform, additional safeguards detailed in Section 6.3 apply.

---

## 5. Detailed Procedures

This section details the step-by-step operational workflows for employee terminations. All timelines are based on calendar days unless otherwise noted.

### 5.1 Standard Separation Workflow (5+ Days Notice)

This workflow applies when a departing employee provides at least five (5) business days of written notice or when a manager initiates an involuntary termination with a planned final date at least five (5) days in the future.

**Phase 1: Initiation and Notification (Within 24 hours of notice)**
1.  **Case Creation:** The HR Business Partner (HRBP) initiates a "Standard Offboarding" case in ServiceNow. The case captures the employee’s name, personnel number, termination date, termination type (voluntary/involuntary), and departing manager.
2.  **Manager Notification & Tasking:** ServiceNow triggers an automated task to the employee’s direct manager. The manager is required to confirm the termination date and immediately begin the Knowledge Transfer Plan and Asset Recovery Plan.
3.  **Employee Acknowledgment:** HRBP schedules the formal termination notification meeting, where the employee receives the "Separation & Post-Employment Obligations" packet, which includes information on COBRA benefits continuation, final paycheck details, and a reminder of their continuing confidentiality obligations. The employee signs an acknowledgment form, which is uploaded to their digital personnel file in Workday by the HRBP.

**Phase 2: Knowledge Transfer and Transition (T-5 Days to T-1 Day)**
4.  **Manager-Led KT Execution:** The manager creates a structured Knowledge Transfer Document (see Section 5.5) and assigns the departing employee to document critical workflows, project statuses, and key contacts within their Meridian Google Workspace shared drive.
5.  **Data Custodian Review:** By T-3 days, the departing employee must review all files in their Meridian Google Drive, local machine (if any), and any removable media, securely deleting personal files not required for the business and organizing business-critical data into designated team folders. Data stored in Snowflake, S3 buckets, or GitLab repositories must have an explicitly designated new owner.
6.  **Pending Transaction Handoff:** For personnel in HealthPay Financial Services, the manager verifies all pending financial transactions or model validation reports are transferred to a qualified successor, in alignment with SR 11-7 model ownership principles.

**Phase 3: Separation Day Activities (Termination Date)**
7.  **Final Verification:** At 10:00 AM local time, the manager confirms in ServiceNow that all KT objectives are complete and all physical assets are accounted for and ready for return.
8.  **Exit Interview:** HRBP conducts the 30-minute Exit Interview (see Section 5.6), either in person or via secure video conference. The results are logged into the anonymous, aggregate "Meridian Voice" system, with PII removed.
9.  **Asset Return:** At 4:00 PM local time, the employee returns all Meridian property (laptop, badge, keys, YubiKey, peripherals) to their manager or local IT. For remote employees, IT will have staged a pre-paid, trackable shipping kit. The IT Service Desk logs all returned serialized assets in ServiceNow’s Configuration Management Database (CMDB).
10. **Access Revocation Execution:** At exactly 5:00 PM local time, the ServiceNow workflow triggers the automated "Mass Access Revocation" script via Okta APIs. This action:
    - Moves the Okta user account to the `Pending_Offboarding` group.
    - Clears all Okta group memberships, suspending SSO access to Google Workspace, Slack, AWS, GitLab, Snowflake, Salesforce, and all other SAML/OIDC-connected applications.
    - Commands a "Remote Wipe" signal to the Meridian Mobile Device Management (MDM) system, JAMF, for any managed iOS/Android device not yet physically returned.

**Phase 4: Post-Departure Finalization (T+1 to T+10 days)**
11. **Hard Token & Secret Rotation:** Within 24 hours (T+1), the IT Service Desk executes the rotation of any shared secrets, API keys, or service accounts the employee had access to as identified by the HashiCorp Vault audit log review.
12. **Email and Data Handling:** The employee's Google Workspace account is suspended but not deleted. An out-of-office auto-responder is set to guide senders to an alternate contact. The manager is granted delegated access to the email inbox and Google Drive for a 15-day transition period. On day T+16, the account and all associated data are automatically archived to a secure, immutable AWS S3 Glacier Deep Archive vault, with a retention period defined by the Meridian Data Retention Policy (SOP-LG-001).
13. **Final Pay & Expense Reimbursement:** Payroll processes the final paycheck, including any accrued, unused Paid Time Off (PTO) as per local statutory requirements, on the next regular payroll cycle. Outstanding expense reports must be submitted within 10 days of termination.
14. **GDPR-Specific Data Handling Notification:** The CPO/DPO’s office logs the termination date into the central Register of Processing Activities (ROPA) for employment data. The data controller (Meridian) will maintain the record of this processing activity, citing legal obligation (Art. 6(1)(c)) and legitimate interest (Art. 6(1)(f)) as the lawful bases for post-employment data processing.

### 5.2 Involuntary High-Risk Immediate Termination Workflow

This workflow is for terminations with cause involving suspected data exfiltration, security violation, or hostile intent, requiring immediate separation without prior notice.

1.  **Strategic Pre-Approval:** The HRBP, CISO (or ITSO), and a member of the Legal team convene a confidential "High-Risk Separation" call. The CISO pre-authorizes an emergency access revocation ticket. Legal confirms the justification and assesses potential data preservation needs (Legal Hold).
2.  **Coordinated Notification:** HR and a Corporate Security representative meet the employee. The notification meeting is brief and direct, and the employee is escorted to collect personal effects under supervision before being escorted from the building.
3.  **Instantaneous Revocation:** Simultaneously, at the moment the notification meeting begins, the ITSO manually executes the "Emergency Kill Switch" playbook from PagerDuty. This executes the same Okta and JAMF commands as the standard workflow but also forcefully terminates all active sessions, including VPN tunnels and AWS Console federated logins.
4.  **Forensic Preservation:** The employee's corporate laptop is immediately secured as evidence. IT serializes the device, creates a forensically sound disk image using a write-blocker, and stores the image in the InfoSec Evidence Locker (an encrypted, chain-of-custody tracked S3 bucket). A chain of custody log is initiated and maintained.
5.  **Data Exfiltration Analysis:** The Security Operations Center (SOC) performs a retrospective audit of the user's logs for the preceding 60 days, analyzing email gateway logs, Cloud Access Security Broker (CASB) alerts from Netskope, USB device usage, and high-volume downloads.

### 5.3 GDPR Exit Procedures for EU Data Subjects

This procedure applies to all employees based in our EU offices (Berlin, and Dublin data center operations), and any other employee who is an EU resident per the GDPR.

1.  **Notification of Rights Document:** In the termination packet, the employee receives a specific "GDPR Exit Data Subject Notice." This document restates their rights under GDPR Art. 13-22, with a clear focus on the right to rectification (Art. 16), the right to erasure (Art. 17, "Right to be Forgotten"), and the right to data portability (Art. 20).
2.  **DSAR Facilitation:** The departing employee is assigned a direct contact in the CPO/DPO’s office (`[email protected]`). If the employee wishes to exercise their right to data portability, they are instructed to file a formal request. The CPO’s office commits to fulfilling this specific portability request, providing a machine-readable JSON export of their core HR and payroll data, within a strict 14-day timeline, significantly under the GDPR’s one-month maximum.
3.  **Right to Erasure Decisioning:** For any request of erasure under Art. 17, the CPO/DPO's office executes a "Balancing of Interests" test within 15 business days. Meridian will erase personal data unless it is legally obligated to retain it. The employee will receive a detailed written response specifying:
    - What data will be erased, and when (within 30 days of request).
    - What data will be retained, the specific lawful basis for retention (e.g., Art. 6(1)(c) for tax law compliance), and the retention period. No blanket exemptions are applied.
4.  **Third-Party Processor Notification:** Upon an approved erasure request, the CPO/DPO instructs all relevant processors (e.g., Workday, Morgan Stanley for 401k, external payroll) to delete the data subject’s PII from their systems, in accordance with Art. 19 and the relevant Data Processing Agreement (DPA).

### 5.4 Access Revocation Technical Procedure

The IT Service Desk and Security Engineering teams use a centrally orchestrated and auditable process.

**System De-Provisioning Sequence:**
The ServiceNow workflow executes access revocation in the following priority order to eliminate network access first, preventing any cloud data egress post-authorization removal.

1.  **Priority 1: Network Access and Core Identity.**
    - **Okta:** Account moved to `offboarded_users` OU. Suspension ensures no SSO token generation.
    - **VPN (Cisco AnyConnect):** Profile and certificate explicitly revoked on Meridian’s RADIUS servers. Active sessions terminated.
    - **Meridian SaaS Platform (AWS):** IAM user’s login profile deleted. All active access keys and secrets are invalidated via a scripted AWS Lambda function within 45 seconds.
2.  **Priority 2: Communication and Collaboration.**
    - **Google Workspace:** Account suspended. OAuth tokens for third-party integrations are cleared.
    - **Slack:** Account deactivated. Sessions are invalidated.
    - **Zoom:** Account license removed.
3.  **Priority 3: Critical Data Platforms.**
    - **Snowflake:** User disabled and all active queries forced-aborted.
    - **GitLab:** User blocked, and all Personal Access Tokens (PATs) revoked.
    - **JIRA/Confluence:** Access disabled, and user is unassigned from all open tickets.
    - **Clinical/PHI Systems:** For departures of personnel with access to clinical trial data or PHI, a specific "PHI Access Revocation" review is triggered. The CISO's Deputy validates that the user is removed from all Epic, Cerner, or internal clinical data mart groups. This review is documented and signed off within 2 business hours.
4.  **Priority 4: Physical and Ancillary.**
    - **Kastle/Badge System:** Badge ID is set to "Inactive/Terminated" in the building access control system.
    - **YubiKey:** Serial number is decommissioned from the Okta policy, invalidating its hardware authentication capabilities.

### 5.5 Knowledge Transfer (KT) Template and Procedure

The responsible manager must populate and execute this plan. A failure to complete this plan by the termination date will be reported in the Chief Compliance Officer’s monthly report.

**KT Plan Components (Located in Meridian Internal Wiki, Template ID: T-KT-004):**
1.  **Core Responsibilities:** A prioritized list of the departing employee's ongoing responsibilities.
2.  **Project Status Overview:** A RAG (Red/Amber/Green) status update for each active project, including immediate next steps, blockers, and key stakeholder contacts.
3.  **Credentials and System Handoff:** A documented list of all non-personal, functional system accounts or shared vault paths the employee managed. The manager confirms new ownership for each.
4.  **Vendor/Partner Contacts:** A final, validated list of any external vendor or partner relationships the employee owned.
5.  **Model and Algorithm Handoff (Critical for AI/Data Science Roles):** For employees in Clinical AI or MedInsight, the KT plan includes a detailed handoff of all active Jupyter notebooks, model training pipelines (Kubeflow), feature stores, and any critical MLflow experiment tracking URLs. The departing employee must run a final, reproducible model training script in the team's dedicated SageMaker environment, witnessed by a senior engineer still on the team, to ensure all dependencies and data sources are correctly documented.

### 5.6 Exit Interview Procedure

The Exit Interview is mandatory for all voluntary resignations and involuntary not-for-cause terminations. It is facilitated by the HRBP.

1.  **Scheduling:** The HRBP schedules a private, 45-minute meeting slot as part of the ServiceNow offboarding task. Attendance is optional, but the employee is encouraged to participate.
2.  **Confidentiality Statement:** The HRBP opens the meeting by stating: *"This interview is a key source of insight for Meridian. Your responses will be anonymized and aggregated with other exits to identify trends. No identifying details will be shared with your former manager or team. This does not affect your final compensation or any reference.""*
3.  **Structured Questionnaire:** The HRBP uses the standard "Meridian Exit Questionnaire" (Form HR-EX-001), covering themes of Job Satisfaction, Management, Company Culture, Growth Opportunities, and Reason for Leaving. The HRBP takes verbatim notes.
4.  **Data Handling:** Interview notes are immediately transcribed into the "Meridian Voice" tool without the employee’s name. PII is redacted. The original notes are securely deleted after 30 days. Aggregated, non-attributable data is shared with departmental VPs on a quarterly basis for organizational improvement. Access to the raw, redacted transcript is strictly limited to the CHRO and one senior HRBP delegate, and it is purged after 18 months.

---

## 6. Controls and Safeguards

### 6.1 Access Control Controls (SOC 2)
Meridian implements logical access controls to deprovision access in a timely manner upon termination. The automated ServiceNow-to-Okta workflow ensures a centralized, scripted removal of access rights on the day of separation. User accounts are suspended, not deleted, for an archival period defined by the data retention schedule. The IT Service Desk performs an audit of the offboarding script's success status within one (1) business day of execution, logging a "Pass/Fail" event. The Security Operations Center maintains a continuous monitoring alert for any "failed deprovision" events.

A review of user access rights is conducted by the Internal Audit function as part of the annual SOX and SOC 2 audit cycles. During these reviews, a sample of terminated users from the preceding audit period is analyzed to verify that all system accounts were suspended in alignment with this SOP’s timeline.

### 6.2 PHI Breach and Security Incident Controls (HIPAA)
Any activity suggesting unauthorized access, use, or disclosure of PHI by a departing employee is treated as a potential security incident. The CISO initiates the incident response process defined in SOP-IS-001 (Information Security Incident Response). The SOC conducts a scoped forensic review of the departing employee’s account activities.

If a breach of unsecured PHI is confirmed, Legal and Privacy Officers will direct the required notifications. A risk assessment will be conducted to determine the nature and extent of the PHI involved, the individual whose PHI has been breached, and the probability of harm. Notifications will be made to affected individuals, the Secretary of HHS, and where applicable, prominent media outlets, without unreasonable delay and in accordance with the law. Workforce members receive annual training on these notification procedures as part of the mandatory HIPAA Awareness course.

### 6.3 EU AI Act High-Risk System Controls
For employees with privileged "maintainer" or "validator" access to high-risk AI systems, as documented in the Meridian AI Inventory (SOP-AI-102), additional controls are enforced post-termination:

1.  **Model Version Integrity Check:** Within 72 hours of a privileged AI engineer's departure, the VP of Clinical AI Products (Dr. Aisha Okafor) must sponsor an independent review of all code commits, model weight changes, and pipeline modifications made by the departing user in the last 30 days. This review looks for anomalies or unauthorized alterations.
2.  **Human Oversight Re-Assignment:** Any "human-in-the-loop" verification duties assigned to the departing employee in the adverse event prediction system’s workflow engine are immediately reassigned to a qualified clinician. This ensures Meridian’s continuous compliance with the EU AI Act’s human oversight obligations (Art. 14).
3.  **Log Retention:** All automatic logs generated by the high-risk AI system relating to the terminated user’s activity are retained in a WORM (Write-Once, Read-Many) compliant store for the system’s entire lifecycle, as mandated for traceability (Art. 12).

### 6.4 Financial Model Controls (SR 11-7)
For departures within HealthPay Financial Services where the employee was an owner or co-owner of a model document in the Model Inventory (SOP-FN-008), an emergency model review is triggered. The Chief Compliance Officer ensures the model's documentation is updated to reflect the change in ownership and that the new owner is briefed on outstanding model limitations, findings, and planned re-validation schedules. This ensures continuity and compliance with model risk management standards.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
The Office of the CISO and the HR Operations team jointly review the following metrics monthly:

| KPI | Target | Measurement Method | Owner |
| :--- | :---: | :--- | :--- |
| **Mean Time to Revoke (MTTR) Logical Access** | < 60 minutes from the scheduled termination time. | Okta System Log `event: user.session.clear` timestamp minus ServiceNow termination timestamp. For emergency workflows, time is from PagerDuty incident trigger to Okta group removal. | CISO (Rachel Kim) |
| **% Offboardings with "Failed Deprovision" Alert** | 0% | Monthly pass/fail log review by AM/IT. Any failure is a severity 2 incident. | VP of IT Ops (Samantha Torres) |
| **Asset Recovery Rate** | 100% | CMDB status flag for all assets assigned to terminated employee must be "Returned" within 10 days. | VP of IT Ops (Samantha Torres) |
| **EU Data Subject Erasure Request Compliance** | 100% completed within 30-day deadline | DPMS (Data Protection Management System) case tracking. | CPO/DPO (Dr. Klaus Weber) |

### 7.2 Management Reporting
On the 10th of each month, the HR Operations Director delivers an "Offboarding Metrics & Compliance Dashboard" to the VP of HR and the CISO. This dashboard includes:
- Total terminations (voluntary, involuntary, RIF) by BU and location.
- MTTR logical access trends.
- Outstanding asset recovery cases older than 15 days.
- A summary of anonymized exit interview themes.
- Register of any exceptions granted under Section 8.

---

## 8. Exception Handling and Escalation

### 8.1 General Exceptions
Any deviation from this SOP’s timelines or procedures requires a formal exception request. For example, a manager may request delayed access revocation for a highly specialized employee on a consulting agreement to finalize critical clinical trial outputs.

**Procedure:**
1.  **Request:** The manager submits a "Termination Exception Request" form in ServiceNow, detailing the business justification, the specific controls to be relaxed, and the proposed timeframe (not to exceed 14 calendar days).
2.  **Review:** The request must be approved by the immediate manager's Vice President, the Chief Compliance Officer (Thomas Anderson), and the CISO (Rachel Kim). The CISO may apply compensating controls (e.g., placing the user in a highly restricted, monitored "quarantine" group in Okta, enabling verbose logging on all their AWS API calls).
3.  **Data Protection Review:** For any employee who had access to EU personal data, the CPO/DPO (Dr. Klaus Weber) must approve the exception to ensure it does not violate GDPR principles of purpose limitation or data minimization. No exception will be granted if it conflicts with a legally mandated data subject erasure request.

### 8.2 Escalation
- **Asset Non-Recovery:** If an employee refuses to return assets, HR escalates to Legal, who may initiate action per SOP-LG-002 (Litigation Hold & Asset Recovery). For remote employees, the local police in the employee’s jurisdiction are engaged for property reclamation, and a formal theft report is filed.
- **Suspected Data Exfiltration:** Any suspicion bypasses routine escalation. The manager or IT staff member must immediately contact the SOC via the PagerDuty "Security Incident" number, initiating the "Emergency Kill Switch" playbook.

---

## 9. Training Requirements

### 9.1 Role-Based Training Assignment
Training is assigned based on the role a workforce member holds in this process.

| Role | Required Training | Frequency | Tracking Method |
| :--- | :--- | :---: | :--- |
| **All People Managers** | "Responsible Offboarding: KT & Asset Management" (Course LM-OFF-101) | Annually | Cornerstone LMS Completion Record |
| **HR Business Partners** | "Mastering the Termination Workflow" (Course HR-OFF-201) and "EU Data Privacy in Offboarding" (Course GDPR-201) | Annually | Cornerstone LMS Completion Record, plus a mandatory 1-hour workshop during the HR quarterly summit. |
| **IT Service Desk (AM/IT)** | "Access Revocation Protocols & SOX Compliance" (Course IT-OFF-301) and "Chain of Custody & Forensic Evidence Handling" | Semi-annually | Cornerstone LMS and a pass/fail practical test on a sandboxed ServiceNow instance. |
| **Information Security (CISO Office)** | "Digital Forensics for High-Risk Separations" internal lab exercise. | Annually | Internal lab completion form signed by the ITSO. |
| **Legal & Compliance** | "Litigation Hold in the Offboarding Context" (Course LG-OFF-401) | Annually | Cornerstone LMS Completion Record |

### 9.2 Annual Workforce Awareness
All workforce members complete the mandatory "HIPAA & Protecting Meridian Data" awareness training annually, which includes a module on reporting un-cooperative offboarding by an outgoing colleague as a potential security concern. Role-specific data privacy training is offered to teams like Clinical AI, who are encouraged but not required to attend quarterly data stewardship roundtables hosted by the CPO/DPO's office.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies
| Document ID | Document Title |
| :--- | :--- |
| SOP-HR-001 | Employee Records Management & Retention |
| SOP-LG-001 | Data Retention and Archiving Policy |
| SOP-LG-002 | Litigation Hold & Asset Recovery |
| SOP-IS-001 | Information Security Incident Response Plan |
| SOP-IS-006 | Access Management and Provisioning |
| SOP-IS-010 | Asset Management and Acceptable Use |
| SOP-AI-102 | High-Risk AI System Inventory and Oversight |
| SOP-FN-008 | Financial Model Documentation & Inventory |
| SOP-GDPR-003 | Data Subject Access Request (DSAR) Handling |

### 10.2 External Standards and Regulations
- **SOC 2 TSC 2017:** Common Criteria 6.2 (Access Termination), 6.3 (Addressing Risks from External Parties)
- **HIPAA:** 45 CFR § 164.308(a)(3)(ii)(C) (Termination Procedures), § 164.410 (Notification Requirements)
- **GDPR:** Art. 5 (Principles), Art. 6 (Lawfulness), Art. 12-14 (Transparency & Modalities), Art. 16 (Rectification), Art. 17 (Erasure), Art. 19 (Notification Obligation), Art. 20 (Portability)
- **EU AI Act:** Art. 12 (Record-Keeping), Art. 14 (Human Oversight)
- **Federal Reserve SR 11-7:** Guidance on Model Risk Management

---

## 11. Revision History

| Version | Date | Author/Reviewer | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 3.5 | 2026-09-18 | J. Walsh, R. Kim | Replaced manual deprovisioning checklist with automated Okta "Mass Access Revocation" script. Updated RACI to reflect new automation. Added specific timelines for AI model handoff KT. |
| 3.4 | 2026-04-05 | K. Weber (CPO/DPO) | Major revision to Section 6.3 and 6.4. Added specific EU AI Act controls for privileged AI engineers. Clarified the GDPR "Balancing of Interests" test for Art. 17 erasure requests and introduced the <14-day portability service level. Updated KT template for data science roles (Kubeflow, MLflow). |
| 3.3 | 2025-12-10 | R. Kim (CISO) | Incorporated Netskope CASB alerts into the "Data Exfiltration Analysis" procedure for immediate separations. Formalized the forensic chain of custody process. Updated KPI table to include emergency workflow MTTR metric. |
| 3.2 | 2025-10-15 | J. Walsh | Updated asset recovery process for distributed workforce. Added pre-paid, trackable shipping kit procedure. Clarified final PTO payout language for multi-state compliance. |
| 3.1 | 2025-08-01 | T. Anderson (Chief Compliance Officer) | Integrated new ServiceNow module for case management. Triggered automated tasks for manager KT and asset plans. Added Section 5.4 for SR 11-7 model ownership handoff requirements. |