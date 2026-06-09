---
sop_id: "SOP-DGP-020"
title: "Data Protection Officer Responsibilities"
business_unit: "Data Governance & Privacy"
version: "5.6"
effective_date: "2024-04-28"
last_reviewed: "2025-10-27"
next_review: "2026-04-17"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Data Protection Officer Responsibilities

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the formal responsibilities, authority, operational mandates, and governance framework for the Data Protection Officer (DPO) function at Meridian Health Technologies, Inc. and its wholly owned subsidiaries (collectively, “Meridian”). The document codifies the structural independence of the DPO, delineates reporting lines, specifies the minimum tasks required for regulatory compliance, and defines the resource allocation model necessary to sustain a mature privacy program across a multinational healthcare fintech enterprise.

### 1.2 Scope

This SOP applies to:

| **Scope Dimension** | **Coverage** |
|---|---|
| **Organizational Entities** | Meridian Health Technologies, Inc. (Boston HQ), Meridian Health Technologies GmbH (Berlin), Meridian HealthPay Services LLC, and all future subsidiaries |
| **Business Lines** | Clinical AI Platform (including all diagnostic imaging analysis modules, patient risk scoring engines, and adverse event prediction systems), HealthPay Financial Services (payment processing, patient financing, medical lending, and claims automation), MedInsight Analytics (population health analytics, care gap identification, and outcomes prediction) |
| **Processing Activities** | All processing of personal data relating to identified or identifiable natural persons located in the European Economic Area (EEA), United Kingdom, and Switzerland, regardless of where the processing takes place |
| **Data Subjects** | Patients, healthcare providers, clinical trial participants, payment beneficiaries, employees, contractors, and vendors whose personal data is processed by Meridian |
| **Personnel** | All employees, contractors, consultants, interim staff, and third-party service providers who design, develop, test, deploy, operate, or maintain Meridian applications that process personal data |

### 1.3 Exclusions

This SOP does not apply to:
- Processing of personal data solely for household or personal activities unrelated to Meridian's business operations.
- Data sets that have been irreversibly anonymized in accordance with the standards documented in SOP-DGP-005 (Data Anonymization and Pseudonymization Standards) and verified by the DPO.
- Paper-based records not intended for filing in a structured system (though Meridian maintains a separate Records Management Policy for such materials).

### 1.4 Compliance Obligations

Adherence to this SOP is mandatory. Non-compliance shall be subject to corrective action under the Meridian Progressive Discipline Policy (HR-EMP-012), up to and including termination of employment or contract, in addition to any civil or criminal liabilities that may arise under applicable data protection legislation.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Data Protection Officer (DPO)** | The individual formally designated by Meridian's Board of Directors to fulfill the role and responsibilities defined in Article 37, 38, and 39 of the General Data Protection Regulation (GDPR). At Meridian, this role is held by the Chief Privacy Officer. |
| **Personal Data** | Any information relating to an identified or identifiable natural person. An identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, identification number, location data, online identifier, or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural, or social identity of that natural person. |
| **Special Categories of Personal Data** | Personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health, or data concerning a natural person's sex life or sexual orientation. Meridian's Clinical AI Platform routinely processes a subset of these categories, specifically data concerning health and genetic data extracted from diagnostic imaging. |
| **Processing** | Any operation or set of operations performed on personal data, whether or not by automated means, including collection, recording, organization, structuring, storage, adaptation or alteration, retrieval, consultation, use, disclosure by transmission, dissemination or otherwise making available, alignment or combination, restriction, erasure, or destruction. |
| **Controller** | The natural or legal person, public authority, agency, or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data. Meridian is the Controller for all personal data processed within its business operations, except where it acts as a Processor under a valid Data Processing Agreement (DPA). |
| **Processor** | A natural or legal person, public authority, agency, or other body which processes personal data on behalf of the Controller. |
| **Data Subject** | The identified or identifiable natural person to whom personal data relates. |
| **Data Protection Impact Assessment (DPIA)** | A structured risk assessment designed to identify, evaluate, and mitigate the data protection risks inherent in a proposed processing operation. Required under Article 35 GDPR for processing likely to result in high risk to the rights and freedoms of natural persons. The DPO provides advice on the necessity and content of DPIAs. |
| **Personal Data Breach** | A breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data transmitted, stored, or otherwise processed. |
| **Lead Supervisory Authority (LSA)** | The supervisory authority in the Member State of Meridian's main establishment (Germany: Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit - BfDI) responsible for the cross-border processing carried out by Meridian. |
| **Independence** | The organizational and operational principle ensuring the DPO is not instructed in the exercise of their tasks, is not dismissed or penalized for performing their duties, and directly reports to the highest management level. |
| **Subsidiary** | Any legal entity in which Meridian Health Technologies, Inc. holds, directly or indirectly, more than 50% of the voting rights or has the right to appoint a majority of the board of directors. |

### 2.2 Acronyms

| Acronym | Full Text |
|---|---|
| **GDPR** | General Data Protection Regulation (Regulation (EU) 2016/679) |
| **DPO** | Data Protection Officer |
| **CPO** | Chief Privacy Officer |
| **DPIA** | Data Protection Impact Assessment |
| **DSAR** | Data Subject Access Request |
| **EDPB** | European Data Protection Board |
| **EEA** | European Economic Area |
| **EU** | European Union |
| **LSA** | Lead Supervisory Authority |
| **BfDI** | Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (German Federal Commissioner for Data Protection and Freedom of Information) |
| **PD** | Personal Data |
| **SPD** | Special Categories of Personal Data |
| **SDLC** | Software Development Lifecycle |
| **SIEM** | Security Information and Event Management (Splunk Enterprise Security, Meridian instance) |
| **GRC** | Governance, Risk, and Compliance (Archer Integrated Risk Management Suite) |
| **IRP** | Incident Response Plan |
| **SLA** | Service Level Agreement |
| **KPI** | Key Performance Indicator |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

The following matrix defines the Responsible, Accountable, Consulted, and Informed parties for the key activities governed by this SOP. The DPO is the Accountable party for the data protection advisory function but is Consulted on operational decisions made by the business.

| Activity / Decision | DPO / CPO (Dr. Klaus Weber) | General Counsel (Maria Gonzalez) | CISO (James Okonkwo) | VP Engineering - AI (Dr. Anya Sharma) | VP Engineering - HealthPay (Marcus Chen) | VP Data Governance (Susan Park) | CEO (David Thornton) |
|---|---|---|---|---|---|---|---|
| **Designation and de-designation of the DPO** | C | C | I | I | I | C | A, R |
| **Allocation of DPO budget and resources** | C | C | I | I | I | C | A, R |
| **Approval of DPIA scoping and methodology** | A, R | C | C | C | C | C | I |
| **Notification of personal data breach to LSA** | C | A, R | C, R | I | I | I | I |
| **Communication of personal data breach to affected data subjects** | C | A, R | C | C | C | C | I |
| **Responding to Data Subject Access Requests (DSARs)** | C | R | I | R (for AI systems) | R (for payment records) | A, R | I |
| **Design and implementation of security measures** | C | C | A, R | R (for AI infra) | R (for fintech infra) | C | I |
| **Conducting of internal privacy audits** | A, R | C | C | I | I | C | I |
| **Maintenance of Records of Processing Activities (Article 30)** | A, R | C | I | C | C | R | I |

---

## 4. Policy Statements

Meridian Health Technologies, Inc. commits to the following policy principles governing the role of the Data Protection Officer:

### 4.1 Principle of Independence

The DPO shall perform their duties and tasks with complete autonomy and independence. The DPO shall not receive any instructions regarding the exercise of their tasks from any officer, employee, or contractor of Meridian. The DPO shall not be dismissed or penalized by Meridian for performing their duties. Any attempt to influence the DPO's professional judgment is a violation of this SOP and shall be reported immediately to the Chair of the Audit Committee of the Board of Directors via the whistleblower mechanism (ETH-001).

### 4.2 Direct Reporting Line to the Highest Management Level

The DPO reports directly to the Chief Executive Officer (CEO) of Meridian Health Technologies, Inc. and has an unfettered access line to the Chair of the Board's Audit Committee. The DPO shall have a dotted-line reporting relationship to the General Counsel for administrative purposes (HR, expense approval, travel) only. Under no circumstances shall the General Counsel or any other officer direct, override, or influence the DPO's professional legal opinions on data protection matters.

### 4.3 Conflicting Roles Prohibited

The DPO shall hold no other position within Meridian that determines the purposes and means of processing personal data. This is strictly enforced.
- **Prohibited Roles for DPO**: CEO, Chief Operating Officer, VP Engineering (any unit), VP Product Management, Chief Marketing Officer, VP Data Governance (in their operational capacity for data strategy).
- **Permitted Concurrent Roles**: Chief Privacy Officer (CPO, as this is functionally the DPO role), oversight chair of the Ethics & Compliance Committee. The DPO may provide operational advice on privacy engineering but shall not assume product management duties.

### 4.4 Accessibility

The DPO shall be easily accessible to all Meridian employees, data subjects, and supervisory authorities. Contact details for the DPO (name, postal address (Berlin office), dedicated email: dpo@meridiantech.com, encrypted contact form: https://privacy.meridiantech.com/contact-dpo) shall be published on Meridian's website, in all privacy notices, and on Meridian's internal intranet (MeridianNet).

### 4.5 Secrecy and Confidentiality

The DPO and their staff are bound by secrecy and confidentiality concerning the performance of their tasks, in accordance with Article 38(5) GDPR. All communications with data subjects, employees, or supervisory authorities involving personal data or organizational vulnerabilities shall be protected by attorney-client privilege where legally permissible and shall be encrypted in transit (TLS 1.2+) and at rest (AES-256).

---

## 5. Detailed Procedures

This section operationalizes the mandatory tasks of the Data Protection Officer. All tasks are assigned a unique Task ID for traceability.

### 5.1 Task Management and Case Handling

The DPO manages all incoming inquiries, consultations, and incident reports through the Meridian Privacy Case Management System (PCMS), an encrypted, access-controlled module within the ServiceNow platform, configured with strict access control lists (ACLs) granting full access exclusively to the DPO and authorized DPO Staff (currently two Senior Privacy Analysts).

**Procedure for Case Intake and Triage:**

1.  **Ingestion**: Inquiries arrive via email (dpo@meridiantech.com), the encrypted web form, internal ServiceNow tickets routed from Legal/Compliance, or direct verbal instruction (which must be immediately transcribed to a PCMS case by DPO Staff).
2.  **Registration**: Within 2 business hours of receipt during Meridian's core business hours (09:00-17:00 CET / 03:00-11:00 EST), a new case is created in PCMS with a unique ID (format: DPO-YYYY-NNNN). The case captures the source, date/time, a summary of the matter, the urgency (Standard, High, Critical), and the relevant regulation.
3.  **Triage and Assignment**: The DPO or designated Senior Privacy Analyst reviews the case.
    - **Data Subject Access Requests (DSARs)**: Assigned to the DSAR Fulfillment Team (Legal) with DPO oversight.
    - **Data Breach Notifications**: Immediately escalated to the CISO and General Counsel as per SOP-SEC-015 (Incident Response).
    - **DPIA Consultations**: Assigned to the DPO for substantive review.
    - **General Advice**: Triaged to the appropriate Privacy Analyst for a first draft, reviewed by the DPO before release.
4.  **Acknowledgment**: The originator receives an automated acknowledgment stating the case ID and the expected timeline for a substantive response, in accordance with the SLAs in Section 6.

### 5.2 Task: Informing and Advising Meridian and its Employees (Article 39(1)(a))

The DPO has a formal, documented advisory role. All processing activities presenting "high risk" to data subjects—a determination made solely by the DPO—require a mandatory, documented consultation with the DPO prior to initiation.

**Procedure for Mandatory Prior Consultation:**

1.  **Initiative Identification**: Any Product Owner, Engineering Director, or business sponsor initiating a new project, feature, or product iteration that involves the collection or novel use of personal data (especially SPD) must file a "Privacy Gate Review Request" (Form DPO-101) through the Privacy Review module in Jira Align, tagged to the `privacy-consultation` workflow.
2.  **Threshold Assessment**: The DPO reviews Form DPO-101 within 5 business days.
    - If the DPO determines the activity does *not* present a high risk, the DPO issues a "Cleared – No High Risk" advisory memo, which is attached to the Jira Epic. No further DPIA is mandated by the DPO.
    - If the DPO determines the activity presents a high risk (e.g., profiling for creditworthiness in HealthPay, large-scale processing of genomic data from the Clinical AI Platform, systematic monitoring of employee keystrokes), the DPO issues a "Mandatory DPIA Order" (Form DPO-102). This triggers the procedure in Section 5.3.
3.  **Advisory Documentation**: All advice provided by the DPO, including interpretations of the law and risk assessments, shall be documented in a formal "DPO Advisory Memorandum" (Template: TEMP-DPO-001). Memoranda are stored, indexed, and immutably logged in the PCMS. Advice is binding on the business unless overruled in writing by the CEO, who shall record their reasons in a "Management Risk Acceptance Letter" (Form DPO-200) that is countersigned by the DPO acknowledging the override, and filed in the Corporate Risk Register.

### 5.3 Task: Monitoring Compliance, including DPIAs (Article 39(1)(b), (c))

The DPO is tasked with monitoring compliance with applicable data protection law and Meridian's internal policies, including the assignment of responsibilities, awareness-raising, staff training, and related audits. The most critical operational tool for this task is the Data Protection Impact Assessment (DPIA).

**Procedure for Conducting a Mandatory DPIA (triggered by Form DPO-102):**

1.  **DPIA Team Assembly**: The responsible Product Owner must assemble a cross-functional DPIA Team including: the Product Owner (Lead), a Senior Engineer, a representative from Data Governance, a representative from Legal, and the DPO (or their Senior Analyst designee) as an advisor.
2.  **System Description**: The team documents the nature, scope, context, and purposes of the processing; the functional architecture; the data flows (using Microsoft Visio diagrams stored in the project's Confluence space); the categories of data subjects and personal data; and the data retention periods.
3.  **Necessity and Proportionality Assessment**: The team documents a detailed assessment of whether the collection of each data element is necessary and proportionate to the defined purpose. The DPO reviews this assessment for legal sufficiency. **Note: Data minimization requirements are addressed in SOP-SEC-013 (Secure Development Lifecycle), but the DPIA must explicitly reconfirm them.**
4.  **Risk Identification and Analysis**: The team identifies risks to the rights and freedoms of data subjects arising from the processing, including:
    - Illegitimate access, alteration, loss, unavailability.
    - Unintended re-identification of pseudonymized data.
    - Inability to exercise data subject rights.
    - Discrimination, identity theft, financial loss, reputational damage.
    The DPIA utilizes Meridian's standard risk matrix (Likelihood x Impact, Scale 1-5) documented in SOP-RM-001 (Risk Management Framework).
5.  **Mitigation Measures**: The team defines specific technical and organizational measures to address each identified risk. Examples include: differential privacy for analytics queries (Clinical AI), tokenization of primary account numbers (HealthPay), strict Attribute-Based Access Control (ABAC) policies, pseudonymization, encryption, and contractual controls on processors.
6.  **DPO Review and Opinion**: The DPO reviews the completed DPIA draft. The DPO provides a formal opinion which may be:
    - **Favorable**: No residual high risk. Processing may proceed.
    - **Favorable with Recommendations**: Low/Medium residual risk. Processing may proceed, with documented recommendations for improvement tracked as Jira Tasks.
    - **Unfavorable**: High residual risk remains. Processing shall NOT proceed. The DPO shall immediately escalate the matter to the CEO and the relevant Supervisory Authority (BfDI), a step outlined in Section 8.
7.  **Sign-off and Living Document**: The DPIA is signed off by the Product Owner, the General Counsel (or delegate), and the DPO. The DPIA is a "living document" stored in the PCMS. The DPO is responsible for triggering a formal review of the DPIA at least annually, or immediately upon a significant change to the processing activity.

### 5.4 Task: Cooperation with the Supervisory Authority and Acting as Contact Point (Article 39(1)(d), (e))

The DPO serves as the single point of contact for the Lead Supervisory Authority (BfDI) and any other relevant supervisory authorities for all matters relating to the processing of personal data.

**Procedure for Managing Supervisory Authority Communications:**

1.  **Inbound Communication**: Any communication from a supervisory authority received by any officer or employee of Meridian must be forwarded, unread, to the DPO within 1 business hour of receipt.
2.  **Log and Assess**: The DPO logs the communication in the PCMS as a "Supervisory Authority Matter."
3.  **Response Preparation**: The DPO drafts the response, gathering necessary information from across the business. All internal stakeholders are obligated to respond to a DPO's data request related to a supervisory matter with the highest priority, within 24 hours or sooner if the DPO specifies a shorter deadline.
4.  **Executive Approval and Submission**: The final response must be approved by the General Counsel. The DPO submits the response. A copy is maintained in the PCMS.
5.  **Proactive Cooperation**: The DPO shall proactively consult with the BfDI on matters specified in Article 36(1) (prior consultation when a DPIA indicates high risk and no sufficient mitigation is found). Such consultation shall be conducted in writing and co-signed by the CEO.

### 5.5 Role-Specific Tasks: Independence and Resourcing

**Procedure for Annual Resource Review:**

1.  **Justification Memo**: By October 1 of each fiscal year, the DPO shall prepare a "DPO Annual Resource Justification Memo" for the CEO and the Board Audit Committee. The memo details:
    - Past year's case load, DPIA volume, and supervisory activity.
    - Projected needs for the upcoming year (staff, external counsel budget, technology tools like enhanced privacy-enhancing technologies (PETs) for the AI platform, training budget).
    - A statement affirming the DPO's continued structural independence, reporting any events that threatened this independence.
2.  **Approval**: The CEO reviews and approves the budget. Failure to approve a budget sufficient to meet regulatory tasks triggers the DPO's obligation to formally note this in their annual report and may trigger a direct report to the supervisory authority concerning Meridian's inability to resource its compliance function.

### 5.6 Task: Record Keeping for DPO Operations

The DPO must maintain secure, confidential records of their own operations, separate from any broader corporate records.

- **Case Files**: All PCMS cases, DPO Advisory Memoranda, DPIA reviews, and correspondence with authorities are retained for the duration of the DPO's tenure plus 5 years.
- **Conflict of Interest Log**: The DPO maintains a personal log of any instances where their advice was overruled by management, documenting the matter, the DPO's advice, the decision taken by management, and the management rationale as captured in Form DPO-200. This log is the DPO's "safe file" and is not stored on Meridian's shared drives but in a DPO-controlled, encrypted repository for use only in the event of a regulatory investigation.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Control Owner | Frequency |
|---|---|---|---|
| **ADMIN-DPO-01** | Formal designation letter for the DPO, outlining role, independence, and reporting lines, is reviewed and re-signed annually by the CEO and the DPO. | CEO / DPO | Annual |
| **ADMIN-DPO-02** | The DPO's position description (HR-JD-0541) is reviewed to ensure it contains no conflicting operational duties (e.g., determining processing purposes). | VP HR (Rebecca Holt) / DPO | Annual |
| **ADMIN-DPO-03** | An independence audit is conducted by an external law firm (currently, 'DataLex Partners') to verify the DPO has not received instructions, has not been dismissed, and has no conflicting roles. The report is delivered to the Board Audit Committee. | Board Audit Committee | Biennial |
| **ADMIN-DPO-04** | All formal DPO advice that is overruled by management must be documented in a Management Risk Acceptance Letter (Form DPO-200), signed by the officer overriding and the DPO. This is logged in the Corporate Risk Register. | CEO / Overriding Officer / DPO | Event-driven |

### 6.2 Technical Controls

| Control ID | Control Description | Tool / System |
|---|---|---|
| **TECH-DPO-01** | Access to the PCMS is restricted by role-based access control (RBAC) with multi-factor authentication (MFA). All access and actions are logged immutably to a dedicated Splunk index. | ServiceNow PCMS, Meridian Okta IAM, Splunk |
| **TECH-DPO-02** | All DPO communications with data subjects, employees, and authorities are encrypted using TLS 1.2+ in transit. Stored case files are encrypted at rest using AES-256. | Microsoft 365 DLP, Azure Key Vault |
| **TECH-DPO-03** | The DPO's case management email account (dpo@meridiantech.com) is excluded from standard corporate eDiscovery holds and retention policies and is subject to a 10-year litigation hold with strict custodial access controlled by the DPO. | Microsoft 365 Legal Hold, Purview |
| **TECH-DPO-04** | For secure internal whistleblowing and confidential consultation, the DPO maintains a dedicated Signal Messenger account for encrypted voice and text, registered to a DPO-controlled device. | Signal Private Messenger |

### 6.3 Resourcing Safeguards

Meridian commits to the following minimum resources for the DPO function:

- **Personnel**: DPO (1 FTE), Senior Privacy Analysts (2 FTE), Administrative Assistant (0.5 FTE).
- **External Legal Budget**: An annual, ring-fenced budget of €250,000 for specialized external data protection counsel, available to the DPO without any further approval required from the Legal department.
- **Technology Budget**: An annual budget of €75,000 for discrete software or services needed by the DPO's office.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The performance of the DPO function is measured not on business outcomes, but on the timeliness and completeness of its mandatory processes.

| KPI ID | KPI Description | Target | Measurement Tool |
|---|---|---|---|
| **DPO-KPI-01** | Average time from initial Privacy Gate Review Request to issuance of DPO Advisory Memorandum for non-high-risk processing. | ≤ 5 Business Days | PCMS Dashboard |
| **DPO-KPI-02** | Average time for DPO to provide formal opinion on a completed DPIA from date of receipt. | ≤ 10 Business Days | PCMS Dashboard |
| **DPO-KPI-03** | Percentage of supervisory authority inquiries acknowledged within 1 business hour and substantively responded to within the authority's stated deadline (or 30 calendar days if none). | 100% | PCMS Dashboard, Email Logs |
| **DPO-KPI-04** | Number of instances where DPO advice was formally overruled (as per Control ADMIN-DPO-04). | (Metric for Board Risk Committee) | Form DPO-200 Log |
| **DPO-KPI-05** | Average time to log a newly received data subject complaint and provide an initial acknowledgment. | ≤ 4 Business Hours | PCMS Dashboard |
| **DPO-KPI-06** | Annual DPIA review cycle compliance (percentage of active DPIAs reviewed within 12 months of their last review). | ≥ 95% | PCMS Calendar/Workflow |

### 7.2 Reporting Cadence

| Report Title | Audience | Frequency | Content |
|---|---|---|---|
| **DPO Quarterly Operational Report** | CEO, General Counsel, CISO, VP Data Governance | Quarterly | Case volumes by type, DPIA status, DSAR metrics, training completion rates, breach notification statistics, supervisory authority interactions, and resource utilization. |
| **DPO Annual Independence and Activity Report** | Board of Directors (Audit Committee), CEO | Annual | Full year operational metrics, a formal statement of independence, review of any management overrides, regulatory horizon scanning, and resource requirements for the upcoming fiscal year. This report is produced by the DPO and is unedited by management. |

The dashboards in the PCMS are accessible in real-time by the CEO and the Board Audit Committee Chair.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling for Advisory Override

Any decision by a business leader to deviate from a documented DPO advisory (i.e., to assume a risk acknowledged by the DPO) follows this formal exception process:

1.  **Request**: The business leader (e.g., VP Engineering) drafts a Management Risk Acceptance Letter (Form DPO-200) in the PCMS. The letter must state:
    - The specific DPO advice being overruled.
    - The detailed business rationale for the override.
    - The proposed compensating controls, if any.
    - The specific period the risk acceptance is requested for.
2.  **DPO Review**: The DPO reviews the request. The DPO may note their continuing objection on the form itself.
3.  **Executive Approval**: The CEO, or their formally delegated officer (limited to General Counsel or COO), must sign the Form DPO-200, definitively accepting the risk on behalf of the corporation.
4.  **Registration**: The fully executed Form DPO-200 is logged by the General Counsel in the Corporate Risk Register and a copy is stored in the DPO's sealed "safe file."

### 8.2 Mandatory Escalation to CEO and Board

The DPO has the authority and obligation to bypass management and escalate directly to the Board Audit Committee, immediately and in writing, under the following conditions:
- A risk acceptance involves a demonstrable, immediate threat of significant harm to data subjects.
- The DPO has a reasonable belief that a criminal offense has occurred or is being planned in respect of data processing.
- The independence of the DPO's role is materially compromised.

### 8.3 Escalation to Supervisory Authority (BfDI)

In accordance with Article 36, if a DPIA indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk, the DPO shall formally advise the CEO. If the CEO decides to proceed regardless, the DPO shall consult the Lead Supervisory Authority (BfDI) prior to the processing commencing. The DPO shall not be instructed on the content of this consultation. This is an absolute, non-delegable duty.

---

## 9. Training Requirements

### 9.1 DPO and DPO Staff Training

The DPO and their staff must maintain expert knowledge of data protection law and practice.

| Training Module | Provider/Source | Frequency | Record |
|---|---|---|---|
| **GDPR Masterclass & Annual Legal Update** | International Association of Privacy Professionals (IAPP) / Bird & Bird LLP | Annual | IAPP CIPP/E / CIPM certification or Annual CPE record filed with HR |
| **EU Digital and AI Regulation Horizon-Scanning** | Fieldfisher LLP | Bi-annual | Certificate of Completion |
| **Meridian Clinical AI Data Ethics Training** | Internal, developed by Ethics & Compliance and Clinical AI | Annual | Meridian LMS (Cornerstone) transcript |
| **Meridian HealthPay Financial Privacy (PCI DSS / PSD2 Context)** | Internal, developed by HealthPay Security | Annual | Meridian LMS transcript |

### 9.2 Organization-Wide Training Monitored by DPO

The DPO is responsible for advising on, but not administering, organization-wide training. The administration is handled by the HR Learning & Development department, who report completion metrics to the DPO quarterly.

| Target Audience | Training Module | Frequency | SLA for Completion |
|---|---|---|---|
| All Employees & Contractors | Meridian Data Protection Essentials | On-hire, then Annual | 95% completion within 30 days of assignment |
| Engineers (All Business Units) | Privacy by Design and Secure Coding (SOP-SEC-013) | Annual | 100% completion required for system access |
| Marketing & Sales | Privacy in Direct Marketing and Sales | Annual | 95% completion within 30 days |
| HR & Finance | Handling Employee and Dependent Personal Data | On-hire, then Biennial | 100% completion |

### 9.3 Compliance Monitoring

The DPO receives a monthly automated report from the Meridian LMS (Cornerstone) directly to the PCMS, listing all outstanding training assignments and non-compliance percentages by department. The DPO shall escalate persistent non-compliance (individuals or teams >30 days overdue) directly to the relevant VP and the VP of HR for disciplinary action under HR-EMP-012.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP-ID | Title | Relationship |
|---|---|---|
| SOP-SEC-015 | Information Security Incident Response Plan | Defines the Personal Data Breach notification process timeline into which the DPO's tasks fit. |
| SOP-SEC-013 | Secure Software Development Lifecycle (SSDLC) | Mandates the privacy-by-design principles the DPO monitors. |
| SOP-DGP-005 | Data Anonymization and Pseudonymization Standards | Technical standard against which the DPO assesses risk mitigation. |
| SOP-DGP-010 | Data Subject Access Request (DSAR) Fulfillment | Operational procedure for the DSAR task the DPO cooperates on. |
| SOP-RM-001 | Enterprise Risk Management Framework | Contains the risk matrix used in the DPIA procedure. |
| HR-EMP-012 | Progressive Discipline Policy | Mechanism for addressing non-compliance with this SOP. |
| SOP-VDR-003 | Third-Party Vendor Security and Data Protection Assessment | The DPO is a key stakeholder in reviewing assessments for processors handling SPD. |

### 10.2 External References

| Reference ID | Document | Source |
|---|---|---|
| EXT-LEG-001 | Regulation (EU) 2016/679 (General Data Protection Regulation) | European Parliament and Council |
| EXT-LEG-002 | Directive 95/46/EC (repealed, for legacy context) | European Parliament and Council |
| EXT-GUID-001 | Guidelines on Data Protection Officers ('DPOs') - WP243 rev.01 | European Data Protection Board (EDPB), formerly Article 29 Working Party |
| EXT-GUID-002 | Guidelines on Data Protection Impact Assessment (DPIA) - WP248 rev.01 | EDPB |
| EXT-GUID-003 | Guidelines on Personal data breach notification under Regulation 2016/679 - WP250 rev.01 | EDPB |

---

## 11. Revision History

| Version | Effective Date | Last Reviewed | Author | Summary of Changes |
|---|---|---|---|---|
| 5.6 | 2024-04-28 | 2025-10-27 | Dr. Klaus Weber, DPO | Full periodic review. Updated case handling procedures to reflect new ServiceNow PCMS module implemented Q2 2025. Added Control TECH-DPO-04 (Signal Messenger). Updated training SLA to 30 days. No changes to independence provisions. |
| 5.5 | 2024-04-15 | 2024-01-10 | Dr. Klaus Weber, DPO | Minor revision. Updated contact details and web form link. Adjusted DPIA review cycle to align with new Product Lifecycle Management (PLM) timeline. |
| 5.4 | 2023-10-01 | 2023-08-15 | Dr. Klaus Weber, DPO | Post-audit change. Implemented Biennial external independence audit (ADMIN-DPO-03) as a direct Board requirement. Formalized the "safe file" procedure in 5.6. |
| 5.3 | 2023-05-12 | 2023-05-01 | Susan Park (VP Data Governance, Acting) | Technical edit. Updated all references from "VP Security" to "CISO" following organizational restructuring. Clarified RACI for breach notification to align with the newly ratified SOP-SEC-015 v3.0. |
| 5.2 | 2022-11-01 | 2022-10-20 | Dr. Klaus Weber, DPO | Major revision. Integrated responsibilities for the newly acquired Berlin-based GmbH (EU establishment). Designated BfDI as LSA. Formalized DPO's role in DPIA sign-off. Added detailed procedure for prior consultation. Increased external legal budget to €250,000. |

**End of Document**