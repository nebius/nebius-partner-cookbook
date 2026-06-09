---
sop_id: "SOP-LEGC-011"
title: "Regulatory Inquiry Response"
business_unit: "Legal & Compliance"
version: "4.5"
effective_date: "2025-06-06"
last_reviewed: "2026-05-16"
next_review: "2026-11-07"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "HIPAA"
  - "GDPR"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Regulatory Inquiry Response

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish a standardized, auditable, and defensible framework for the intake, triage, management, response, and closure of all regulatory inquiries directed to Meridian Health Technologies, Inc. ("Meridian") by governmental authorities, regulatory bodies, and supervisory agencies. This SOP ensures that Meridian responds to all inquiries in a timely, accurate, and legally privileged manner, while maintaining compliance with applicable data protection, financial services, and artificial intelligence regulations across all operating jurisdictions. This framework is designed to protect the company from legal and financial penalties, preserve corporate reputation, and ensure that all communications are coordinated through the appropriate legal and compliance channels to maintain attorney-client privilege and work product doctrine protections where applicable.

### 1.2 Scope

This SOP applies to all regulatory inquiries received by Meridian Health Technologies, Inc., including its global offices in London, Berlin, Singapore, and Toronto. The scope encompasses all five categories of regulatory contact:

**In-Scope Inquiries:**
- Formal subpoenas, civil investigative demands (CIDs), and court orders
- Information requests from the U.S. Department of Health and Human Services (HHS) Office for Civil Rights (OCR)
- Data protection authority (DPA) inquiries under the General Data Protection Regulation (GDPR) from EU/EEA supervisory authorities
- Federal Reserve and Consumer Financial Protection Bureau (CFPB) inquiries related to HealthPay Financial Services
- U.S. Food and Drug Administration (FDA) inquiries related to clinical AI products
- National Institute of Standards and Technology (NIST) voluntary compliance verification requests
- State attorneys general inquiries
- Sectoral regulator inquiries in the UK (Information Commissioner's Office, Financial Conduct Authority), Germany (BfDI, BaFin), Singapore (PDPC, MAS), and Canada (OPC, OSFI)
- Notified Body inquiries under EU Medical Device Regulation (MDR) for CE-marked clinical AI products

**Out-of-Scope:**
- Routine customer complaints not escalated to a regulatory body
- Internal audit findings without external regulatory notification
- Commercial contract disputes not involving a regulatory authority
- Standard business license renewals and routine tax filings

**Applicability:** All employees, contractors, consultants, and third-party service providers who may receive correspondence from regulatory authorities must comply with this SOP. The procedures herein are binding on all business units, including Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.

### 1.3 Regulatory Context

Meridian operates in a multi-jurisdictional regulatory environment. This SOP provides the procedural backbone for compliance with the EU AI Act, GDPR, and related frameworks. For HealthPay Financial Services, this SOP integrates with SR 11-7 model risk management response protocols.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Attorney-Client Privilege** | Legal doctrine protecting confidential communications between Meridian legal counsel and Meridian personnel for the purpose of seeking or rendering legal advice. |
| **Data Protection Authority (DPA)** | Any EU/EEA supervisory authority with competence over GDPR enforcement, including but not limited to the Irish Data Protection Commission (lead authority for Meridian's cross-border processing), the Berlin Commissioner for Data Protection and Freedom of Information (BlnBDI), and the UK Information Commissioner's Office (ICO). |
| **Document Hold Notice** | A legally binding internal directive instructing identified custodians to preserve all potentially relevant documents, data, and records in anticipation of or response to a regulatory inquiry. |
| **Inquiry Coordinator** | The designated Legal & Compliance professional assigned to manage the day-to-day logistics of a specific regulatory inquiry response. |
| **Inquiry Triage Committee** | Cross-functional decision-making body responsible for classifying the severity, urgency, and legal privilege status of incoming inquiries. |
| **Legal Hold** | Synonymous with Document Hold Notice. |
| **Lead Supervisory Authority (LSA)** | Under GDPR Article 56, the DPA of Meridian's main establishment (Ireland) with primary responsibility for cross-border processing matters. |
| **Notified Body** | An organization designated by an EU member state to assess conformity of medical devices (including certain AI-based clinical products) under the EU MDR before CE marking. |
| **Regulatory Inquiry** | Any written or oral communication from a governmental or regulatory authority requesting information, documentation, testimony, or other responsive action from Meridian. |
| **Responsive Documents** | All records, in any format, that fall within the scope of the inquiry's document request parameters. |
| **Work Product Doctrine** | Legal protection shielding materials prepared in anticipation of litigation or regulatory proceedings from disclosure. |

### 2.2 Acronyms

| Acronym | Full Term |
|---|---|
| BfDI | Bundesbeauftragter für den Datenschutz und die Informationsfreiheit (German Federal Data Protection Commissioner) |
| CID | Civil Investigative Demand |
| CFPB | Consumer Financial Protection Bureau |
| DPA | Data Protection Authority |
| EDRM | Electronic Discovery Reference Model |
| EU AI Act | European Union Artificial Intelligence Act (Regulation 2024/1689) |
| FCA | Financial Conduct Authority (UK) |
| GDPR | General Data Protection Regulation (Regulation (EU) 2016/679) |
| HHS OCR | U.S. Department of Health and Human Services Office for Civil Rights |
| ICO | UK Information Commissioner's Office |
| MAS | Monetary Authority of Singapore |
| MDR | EU Medical Device Regulation (Regulation (EU) 2017/745) |
| OPC | Office of the Privacy Commissioner of Canada |
| OSFI | Office of the Superintendent of Financial Institutions (Canada) |
| PDPC | Personal Data Protection Commission (Singapore) |
| SR 11-7 | Federal Reserve Supervisory Guidance on Model Risk Management |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix: Regulatory Inquiry Response

| Role | Receive & Log | Triage | Investigation | Response Drafting | Final Approval | Communication to Regulator |
|---|---|---|---|---|---|---|
| **General Counsel (Maria Gonzalez)** | - | A | C | C | R | A/I |
| **Chief Compliance Officer (Thomas Anderson)** | - | R | A | R | A | C |
| **Chief Privacy Officer (Dr. Elena Vasquez)** | - | C | R | R | C | C |
| **VP, Regulatory Affairs - AI (Dr. Marcus Chen)** | - | C | R | R | C | C |
| **Head of HealthPay Compliance (Sarah Okonkwo)** | - | C | R | R | C | C |
| **Director, Information Security (James Liu)** | C | C | R | C | I | - |
| **Inquiry Coordinator (Assigned per inquiry)** | R | R | R | R | I | R |
| **Legal Counsel - EU (Berlin Office)** | C | C | R | R | C | C (EU DPAs only) |
| **Document Custodians (All Employees)** | I | - | C | - | - | - |
| **External Counsel (Gibson Dunn / Fieldfisher)** | - | C | R | R | C | I |
| **CEO (Dr. Rachel Park)** | - | I | - | - | A (High Risk) | - |

**Key:** R = Responsible; A = Accountable; C = Consulted; I = Informed

### 3.2 Role Descriptions

**Thomas Anderson, Chief Compliance Officer (SOP Owner):** Ultimate accountability for the maintenance of this SOP and the operational integrity of the inquiry response process. Directly responsible for initial triage determination within two (2) business hours of inquiry receipt. Serves as the primary liaison to external regulatory bodies for non-EU matters unless otherwise delegated. Approves all responses classified as "Medium Risk." Must be a qualified attorney licensed in at least one U.S. jurisdiction (currently New York).

**Maria Gonzalez, General Counsel (Approver):** Holds final signing authority for all "High Risk" and "Critical" inquiry responses. Approves all privilege designations and retains the sole authority to waive attorney-client privilege or work product protection. Directly manages relationships with retained external law firms and manages litigation holds. Must be immediately notified of any inquiry accompanied by a civil penalty or criminal referral.

**Dr. Elena Vasquez, Chief Privacy Officer:** Accountable for GDPR DPA inquiry responses originating from EU/EEA supervisory authorities. Coordinates with the Data Protection Officer (DPO) in the Berlin office. Must ensure GDPR response timelines (per Article 58) are met. Consults on all data access, portability, or deletion-related inquiries.

**Dr. Marcus Chen, VP, Regulatory Affairs - AI:** Responsible for providing technical documentation for inquiries related to the Clinical AI Platform. Maintains the EU AI Act technical documentation repository. Coordinates with the Notified Body (TÜV SÜD) on MDR-related inquiries. Ensures AI transparency documentation is prepared, particularly for inquiries from EU market surveillance authorities under the EU AI Act.

**Sarah Okonkwo, Head of HealthPay Compliance:** Consults on all inquiries related to the HealthPay Financial Services business unit, including Federal Reserve, CFPB, FCA, and MAS matters. Ensures SR 11-7 model documentation availability. Maintains licensing records for cross-border financial services.

**Legal Counsel - EU (Berlin Office):** Serves as the statutory representative for GDPR Article 27 purposes. Handles direct communications with the Berlin DPA (BlnBDI) and the UK ICO. Drafts GDPR-specific responses under privilege where applicable under local law.

**External Counsel:** Retained on an inquiry-by-inquiry basis. Gibson Dunn & Crutcher serves as primary U.S. regulatory defense counsel. Fieldfisher LLP serves as primary EU/UK regulatory defense counsel. Engagement requires a specific limited-scope engagement letter executed by the General Counsel.

---

## 4. Policy Statements

### 4.1 Foundational Policy Commitments

**POL-011-001: Mandatory Reporting.** Any employee, contractor, or agent of Meridian who receives a communication from a regulatory authority, whether by mail, email, telephone, facsimile, or personal service, must immediately (within sixty (60) minutes of receipt) forward the communication in its entirety to the Legal & Compliance department at regulatory-inquiry@meridian-health.ai. Failure to report a regulatory inquiry is a Category 1 compliance violation subject to disciplinary action, up to and including termination for cause and, where applicable, referral to law enforcement for obstruction. Physical documents must be hand-delivered or securely couriered to the Legal & Compliance office at 400 Meridian Drive, Suite 1200, Boston, MA 02210 within four (4) hours.

**POL-011-002: No Direct Response.** No employee is authorized to respond substantively to any regulatory inquiry without the express written authorization of the General Counsel or Chief Compliance Officer. Acknowledgement of receipt, if required by law, must be drafted by the Legal & Compliance department and may only confirm that the inquiry was received and is under review. Any unauthorized communication with a regulatory authority shall be immediately reported to the Chief Compliance Officer for corrective action and potential privilege waiver assessment.

**POL-011-003: Privilege Preservation.** Meridian asserts attorney-client privilege and work product doctrine protection over all investigatory materials, internal communications analyzing regulatory requirements, draft responses, and communications with external counsel related to regulatory inquiries. All responsive document collections and internal investigation files shall be managed within the established Privilege Zone in the iManage Work document management system (iManage Privilege Workspace: "MHT-REG-PRIVILEGED"), accessible only to the Legal & Compliance team and designated external counsel.

**POL-011-004: Data Protection by Design in Investigations.** All personal data collected, accessed, or processed during a regulatory inquiry investigation shall be processed in accordance with GDPR Article 25 (Data Protection by Design and by Default). Internal investigation teams shall use pseudonymization techniques where feasible and shall strictly limit access to personal data to personnel with a demonstrable need-to-know for the specific inquiry.

**POL-011-005: EU AI Act Cooperation.** Meridian commits to cooperating fully with market surveillance authorities designated under the EU AI Act. Upon receipt of an inquiry, Meridian shall prepare to provide, within commercially reasonable timelines, the technical documentation demonstrating compliance with obligations for high-risk AI systems (Clinical AI Platform products classified as high-risk under Annex III of the EU AI Act). Meridian shall identify a point of contact for AI regulatory matters within five (5) business days of inquiry receipt.

### 4.2 Specific Policy Commitments

**POL-011-006: GDPR DPA Cooperation.** Meridian shall cooperate in good faith with all Data Protection Authorities exercising their investigatory powers under GDPR Article 58. Meridian shall respond to DPA information requests within the timelines specified by the requesting authority, typically thirty (30) calendar days from formal notification, unless an extension is formally negotiated through the Lead Supervisory Authority mechanism under Article 60.

**POL-011-007: SR 11-7 Documentation Availability.** For inquiries related to HealthPay Financial Services model risk, Meridian shall maintain ready-access to all model development documentation, validation reports, and governance committee minutes as required by SR 11-7, and shall produce these records within the timelines specified by the inquiring regulator.

---

## 5. Detailed Procedures

### 5.1 Inquiry Intake, Logging, and Acknowledgement

**Step 1: Receipt and Timestamping (Target: 30 minutes)**
Upon delivery of a regulatory communication to the Legal & Compliance department (via the regulatory-inquiry@meridian-health.ai inbox or physical delivery), the Inquiry Coordinator on duty (rotating schedule, available 24/7/365) shall:
1.  Timestamp the communication in the Meridian Regulatory Inquiry Tracking System (RITS), a Power Platform application maintained by the Compliance Technology team.
2.  Assign a unique Inquiry Tracking Number in the format: `REG-YYYY-NNNN` (e.g., `REG-2025-00173`).
3.  Scan all physical documents into secure, access-controlled PDF files stored directly into the iManage Privilege Workspace.
4.  If the inquiry was served by a process server or law enforcement agent on-site at a Meridian facility, the Head of Global Security (Vincent Rossi) must be notified immediately via the Security Operations Center (SOC) hotline.

**Step 2: Immediate Notification (Target: 30 minutes from logging)**
The Inquiry Coordinator sends a "High Priority - Confidential" notification via Microsoft Teams and email to the Inquiry Triage Committee distribution list. The notification must include:
- Inquiry Tracking Number
- Sender (Regulatory Body and specific individual, if known)
- Date and method of receipt
- Summary of stated subject matter
- Attached copy of the original inquiry

### 5.2 Inquiry Triage and Classification

**Step 3: Classification (Target: 4 business hours from notification)**
The Inquiry Triage Committee convenes (virtually or in-person, as needed). The Committee classifies the inquiry along two axes: **Risk Level** and **Regulatory Domain**.

**Table 5-1: Risk Level Classification Matrix**

| Risk Level | Criteria | Example |
|---|---|---|
| **Critical** | Inquiry accompanied by search warrant, dawn raid, criminal referral, imminent threat of asset seizure, or involving allegations of systemic fraud. CEO and Board must be informed immediately. | FBI search warrant executed at Meridian headquarters. |
| **High** | Formal subpoena, CID, OCR investigation with potential civil monetary penalties, DPA investigation under GDPR Article 58(2) corrective powers (including a potential ban on processing), or FDA Warning Letter. | HHS OCR investigation into a reported data breach involving >50,000 individuals. |
| **Medium** | Standard DPA Article 58(1) inquiry, state AG inquiry, formal notice of an announced regulatory audit, or a request for information related to a routine supervisory review. | Federal Reserve annual model risk questionnaire. |
| **Low** | Voluntary industry data request, requests for publicly available information, or inquiries that can be satisfied by referencing published transparency reports. | NIST RFI on AI risk management practices. |

**Step 4: Conflict Check and External Counsel Engagement (Target: 24 hours from triage)**
The General Counsel determines if external counsel is required, based on Risk Level (mandatory for all Critical and High inquiries) or specialized jurisdictional expertise. The Engagement Letter is executed, and Meridian's Matter Number is communicated.

### 5.3 Scoping and Document Hold Issuance

**Step 5: Scoping Meeting (Target: 48 hours from triage)**
The Inquiry Coordinator schedules a scoping meeting. Attendees include the General Counsel (or designate), Chief Compliance Officer, the relevant Business Unit Compliance Lead, the Chief Privacy Officer (for GDPR inquiries), and external counsel. Agenda items:
1.  Analyze the specific questions and document requests.
2.  Identify preliminary Meridian systems and data sources likely to contain responsive information. Systems reviewed include: Salesforce CRM, Workday HRIS, Azure DevOps (code repositories), Snowflake (data warehouse), Microsoft 365 (Exchange Online, SharePoint, Teams), iManage Work, and Epic EHR (for clinical support data, if applicable).
3.  Identify preliminary custodians (employees whose data may be responsive).
4.  Define a preliminary date range.
5.  Determine if any subject matter expert interviews are immediately needed.

**Step 6: Issuance of Document Hold Notice (Target: Immediately upon custodian identification)**
The Inquiry Coordinator, under direction of the General Counsel, issues a legally-binding Document Hold Notice through the Onit Legal Hold Management Platform. The notice must:
- Be addressed to all identified custodians and their direct managers.
- Describe the subject matter of the inquiry broadly to avoid inadvertent spoliation.
- Instruct custodians to suspend all routine deletion policies (e.g., email auto-archive, ephemeral chat log deletion) for the specified date range.
- Include a mandatory "Acknowledgment of Compliance" that each custodian must digitally sign within forty-eight (48) hours of issuance. Non-acknowledgement is auto-escalated to the custodian's manager and then to the VP of Human Resources.

### 5.4 Collection, Processing, and Review

**Step 7: Data Collection (Target: 5 business days from Hold Notice)**
The IT Forensics team, working under the direction of the Director of Information Security, executes data collection. Collection follows a strict chain-of-custody protocol logged in the Forensics Lab Investigation Notebook (FLIN) system.
- **Microsoft 365:** Mailboxes, OneDrive, and Teams chats are collected using Microsoft Purview eDiscovery (Premium). Export is loaded into the Relativity review platform.
- **Structured Data (Snowflake):** Queries are built to extract relevant transaction records, model inputs/outputs, and audit logs. Results are exported to CSV and loaded into Relativity.
- **Epic / Clinical Systems:** Extraction follows a defined, auditable SQL script validated by the VP of Clinical Informatics.

**Step 8: Processing and Data Reduction (Target: 3 business days from collection)**
The eDiscovery team processes collected data in RelativityOne. Processing includes:
- De-duplication at the family level.
- De-NISTing (removing known system files).
- Email threading.
- Text extraction for all documents.

**Step 9: GDPR Data Protection Impact Assessment (DPIA) for Review Data (Mandatory for all EU inquiries)**
Before substantive document review begins, the EU Legal Counsel, in conjunction with the Data Protection Officer, conducts a DPIA (GDPR Article 35) on the data set to be reviewed. This DPIA documents:
- A systematic description of the review process.
- The necessity and proportionality of processing personal data of data subjects (employees, customers, patients) within the review set for the purposes of responding to the regulatory inquiry.
- An assessment of the risks to the rights and freedoms of data subjects whose personal data is incidentally contained within the reviewed documents.
- The controls established to mitigate these risks, including: strict role-based access controls (RBAC) in Relativity, automatic redaction suggestions for PII using Relativity's pre-trained models, and a prohibition on exporting sensitive personal data from the review platform.

**Step 10: Document Review and Privilege Logging (Iterative, timeline agreed with regulator)**
A tiered review workflow is established in Relativity:
1.  **First-Level Review (Contract Attorneys):** Cull for relevance using an approved coding panel. Tag for potential privilege, PII, and key issues.
2.  **Second-Level Review (Meridian Associate Counsel):** Confirm relevance and privilege calls. All potentially privileged documents are moved to a separate, encrypted privilege log volume.
3.  **Third-Level Review (General Counsel / External Counsel Partner):** Final sign-off on all responsive, non-privileged productions. Draft a detailed Privilege Log for any withheld documents using the agreed format.

### 5.5 Response Drafting, Approval, and Production

**Step 11: Narrative Response Drafting (Target: First draft 10 business days before deadline)**
The Inquiry Coordinator leads the drafting of the narrative response and transmittal letter. Drafting follows a collaborative model using Co-Author in Microsoft Word within the secure Matter Workspace. All factual assertions must be sourced (footnoted to a Bates-numbered document or interview record).

**Step 12: Multi-Stage Approval Workflow (Target: Final draft 5 business days before deadline)**
Responses flow through an automated approval workflow in the Power Automate-based Compliance Review Board (CRB) system.

**Table 5-2: Approval Workflow by Risk Level**

| Risk Level | Required Approvers |
|---|---|
| **Low** | Inquiry Coordinator, Chief Compliance Officer |
| **Medium** | Inquiry Coordinator, Chief Compliance Officer, Relevant Business Unit Lead (e.g., VP AI, Head of HealthPay) |
| **High** | All Medium approvers + Chief Privacy Officer, General Counsel. External counsel review is mandatory. |
| **Critical** | All High approvers + Chief Executive Officer. Board of Directors notification occurs prior to submission. |

**Step 13: Document Production (Target: 1 business day before deadline)**
Responsive, non-privileged documents are produced in a defensible, load-ready format. Productions are Bates-stamped (`MHT-REG-[Tracking No.]-[#####]`). The production is accompanied by a Transmittal Letter signed by the General Counsel. Electronic productions are transmitted via the agreed-upon secure file transfer method (typically a secure SFTP portal managed by the regulator). Physical productions are hand-delivered via bonded courier.

### 5.6 Inquiry Closure and Recordkeeping

**Step 14: Closure (Target: 30 days after final communication)**
Upon receipt of a closure letter, "no action" notice, or settlement agreement, the Inquiry Coordinator:
1.  Updates the RITS record to "Closed."
2.  Archives the full Matter Workspace in iManage as a static, read-only record.
3.  Reviews the Document Hold Notice and formally releases custodians from their preservation obligations via a "Release of Hold Notice" in Onit.

**Step 15: Recordkeeping and Retention:**
- **Closed Inquiry Files:** Retained for a period of ten (10) years from the date of closure, per Meridian's Corporate Record Retention Schedule (SOP-CORP-008), unless a longer retention period is mandated by a specific regulatory or court order.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

**CONT-011-01: Need-to-Know Access.** Access to the Meridian Regulatory Inquiry Tracking System (RITS) is restricted to named members of the Legal & Compliance department, designated executive leadership, and specifically authorized support staff. Access rights are reviewed quarterly by the Director of Legal Operations.

**CONT-011-02: Segregation of Duties.** Under no circumstances may the individual serving as the Inquiry Coordinator for a specific matter also serve as the final approver for the response on that same matter. This function must be separated.

**CONT-011-03: External Counsel Protocol.** All communications with external counsel shall include the legend: "Attorney-Client Communication: Privileged and Confidential, Protected by the Work Product Doctrine."

**CONT-011-04: GDPR Article 28 Processor Agreements.** Any external eDiscovery vendor, forensic consultant, or expert engaged for an inquiry response who will process personal data originating from the EU/EEA must have a valid GDPR Article 28 Data Processing Agreement (DPA) in place, reviewed within the last twelve months.

### 6.2 Technical Controls

**CONT-011-05: iManage Privilege Workspace.** The "MHT-REG-PRIVILEGED" workspace in iManage Work is configured with mandatory 2-Factor Authentication (2FA), automatic 256-bit AES encryption at rest, and a full, immutable audit trail recording every user action (view, edit, share, download).

**CONT-011-06: RelativityOne Access.** Meridian's RelativityOne instance is configured with Active Directory Federation Services (ADFS) for SSO, enforcing Meridian's central password policy. Firewall rules restrict access to the review platform to authorized internal IP ranges and the dedicated VPN pool for external review teams.

**CONT-011-07: Data Loss Prevention (DLP).** A specific DLP policy ("DLP-LEGAL-01") is applied to the Legal & Compliance user group. This policy blocks the unauthorized exfiltration of documents containing the Bates prefix `MHT-REG-` or the keyword "Privileged and Confidential Attorney Work Product" via email, USB, or non-approved cloud storage services.

### 6.3 Quality Assurance Controls (Related to EU AI Act Inquiries)

**CONT-011-08: Technical Documentation Generation.** For inquiries under the EU AI Act, the VP of Regulatory Affairs - AI will generate a Technical Documentation Package. This automated report compiles details on the AI system's intended purpose, algorithmic logic, performance metrics, and training data provenance as stored in the Meridian Model Registry (MLflow). The quality assurance of this report is a manual review performed by the AI Governance Board. The report provides technical information but is generated based on the model metadata available at the time; the scope is limited to data points actively tracked in MLflow, which covers primary development and validation records.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

**Table 7-1: Regulatory Inquiry Response KPIs**

| Metric | Target | Measurement Method | Owner |
|---|---|---|---|
| **Intake-to-Triage Time** | < 4 business hours from receipt | RITS Timestamp Delta | Chief Compliance Officer |
| **Hold Notice Issuance Time** | < 24 hours from custodian identification | Onit Legal Hold Platform Audit Log | General Counsel |
| **Response Timeliness** | 100% production before the regulator's deadline | RITS Deadline vs. Production Date | Chief Compliance Officer |
| **Custodian Hold Acknowledgement** | >99% within 48 hours of issuance | Onit Acknowledgment Report | Director of Legal Operations |
| **Privilege Log Accuracy** | <1% successful challenge rate on privilege designations post-production | External Counsel Feedback Loop | General Counsel |
| **GDPR Consultation Compliance** | 100% of GDPR inquiries involving personal data have a DPIA filed before review | DPIA Log in OneTrust | Chief Privacy Officer / DPO |

### 7.2 Reporting Cadence

- **Weekly Operational Metrics:** An automated dashboard in Power BI, sourced from RITS and Onit, is published every Monday at 08:00 EST to the Legal & Compliance team and the Chief Privacy Officer. This dashboard tracks all in-flight inquiries, upcoming deadlines, and YTD KPI performance against targets.

- **Quarterly Regulatory Landscape Report:** The Chief Compliance Officer presents a consolidated report to the Audit Committee of the Board of Directors. This report summarizes all inquiries received in the quarter, response outcomes, aggregate metrics, significant matters, and a forward-looking analysis of emerging regulatory risks.

- **Annual SOP Effectiveness Review:** As part of the annual review cycle (see Section 12), the Chief Compliance Officer conducts a formal effectiveness review, sampling a minimum of five (5) closed inquiries (or all, if less) to test procedural adherence and identify opportunities for continuous improvement.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling

Any deviation from the prescribed procedures of this SOP requires a formal, documented exception. This is critical for the defensibility of the inquiry response process.

**Step 1: Identification and Documentation.** The individual requesting the deviation (e.g., a request to use an alternate eDiscovery vendor, a request to extend an internal deadline) must complete a Request for Exception (RFE) form in the Meridian Compliance GRC Platform.

**Step 2: Assessment by Inquiry Coordinator.** The Inquiry Coordinator assesses the RFE against the specific risks it introduces (legal, technical, and operational risk).

**Step 3: Approval Matrix.** The RFE is routed for approval based on the matrix below:

**Table 8-1: Exception Approval Matrix**

| Impact of Exception | Approver |
|---|---|
| Procedural delay that will NOT cause a missed regulatory deadline | Director of Legal Operations |
| Any deviation involving a new third-party vendor or technology | Chief Compliance Officer |
| Any deviation that may increase the risk of a missed deadline | General Counsel |

All approved exceptions must be logged in RITS and attached to the specific inquiry record.

### 8.2 Escalation Pathway

If a dispute arises between business units regarding the content of a response, or if an unresolvable resource constraint threatens the ability to meet a regulatory deadline, the following escalation pathway must be followed:

1.  **Level 1:** Inquiry Coordinator to Director of Legal Operations.
2.  **Level 2:** Director of Legal Operations to Chief Compliance Officer.
3.  **Level 3:** Chief Compliance Officer to General Counsel.
4.  **Final Level:** General Counsel to the Chief Executive Officer for binding resolution.

Documentation of each escalation level, including the resolution, must be appended to the matter file in iManage.

---

## 9. Training Requirements

### 9.1 Annual Role-Based Training

All personnel identified in the RACI matrix (Section 3) must complete the following mandatory training:

**TRN-011-01: Inquiry Response Foundations.**
- **Audience:** All roles in the RACI matrix.
- **Modality:** Self-paced eLearning module in Workday Learning.
- **Frequency:** Annually, within ninety (90) days of the effective date of a new version of this SOP.
- **Key Topics:** Overview of SOP changes; a refresher on the intake and immediate notification procedures.

**TRN-011-02: Tabletop Exercise: Critical Inquiry Simulation.**
- **Audience:** Inquiry Triage Committee, General Counsel, CCO, CPO, CEO, Director of Information Security. (Other roles attend biennially).
- **Modality:** Facilitated tabletop exercise run by an external crisis management consultant.
- **Frequency:** Annually for the core crisis team.
- **Objective:** Practice the triage, coordination, and high-pressure decision-making required for a Critical-level inquiry, such as a simulated dawn raid or a cross-border GDPR investigation.

**TRN-011-03: Advanced eDiscovery and Privilege Workshop.**
- **Audience:** Legal & Compliance associates, Director of Legal Operations, IT Forensics Team.
- **Modality:** Instructor-led training by retained external counsel.
- **Frequency:** Biennially.
- **Objective:** Deep dive into privilege log drafting, defensible collection protocols, and recent case law updates on privilege waiver.

### 9.2 General Employee Awareness

All Meridian employees must complete the "If You Receive a Regulatory Inquiry" micro-course (15 minutes) as part of their annual Code of Conduct training, which covers the mandatory reporting obligation.

### 9.3 Training Tracking

Completion of all role-based training is tracked in Workday Learning. The Director of Legal Operations is responsible for generating a monthly compliance report on training completion. Non-completion of mandatory training within the specified grace period constitutes a compliance violation and is referred to Human Resources for remediation.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Document Title | Relationship to This SOP |
|---|---|---|
| SOP-LEGC-008 | Corporate Record Retention Schedule | Defines retention periods for inquiry records post-closure. |
| SOP-LEGC-006 | Attorney-Client Privilege Management | Governs day-to-day privilege classification and management; referenced by the privilege controls in this SOP. |
| SOP-INFOSEC-023 | Forensics and eDiscovery Protocol | Technical procedures for the collection of electronically stored information (ESI); referenced in Procedure 5.4. |
| SOP-HR-004 | Employee Disciplinary Policy | Defines the classifications and consequences for compliance violations referenced in Policy Section 4.1. |
| SOP-PRIV-003 | Data Subject Rights Request Handling | (See Section 9 for training cross-references). |
| SOP-PRIV-007 | Data Protection Impact Assessment (DPIA) Procedure | Mandatory DPIA process referenced in Section 5.4. |
| SOP-AI-015 | EU AI Act High-Risk System Documentation | Governs the ongoing technical documentation for AI systems, which is used to generate the response package in Control 6.3. |

### 10.2 External References

- **GDPR (Regulation (EU) 2016/679):** Foundational text for all data protection inquiries, specifically Articles 25 (DPbD), 27 (EU Representative), 28 (Processor), 30 (RoPA), 35 (DPIA), 37-39 (DPO), 56 (LSA), 58 (Powers), 60 (Cooperation), 60-63 (Consistency), 83 (Fines).
- **EU AI Act (Regulation 2024/1689):** For inquiries related to AI systems.
- **EU MDR (Regulation (EU) 2017/745):** For inquiries related to CE-marked clinical products, specifically Annex IX (Conformity Assessment).
- **HIPAA Regulations (45 CFR Parts 160, 164):** Foundational text for U.S. healthcare data privacy and security inquiries.
- **SR 11-7 / Attachment:** Federal Reserve Guidance on Model Risk Management.

---

## 12. Revision History

This section documents all substantive changes to this SOP. Minor typographical corrections not affecting procedural meaning are not logged here but are tracked in the iManage document version history.

**Table 12-1: Revision History Log**

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 1.0 | 2021-03-15 | Thomas Anderson | Initial Release. Established basic intake and response framework for HHS OCR and FDA inquiries only. |
| 2.0 | 2022-08-01 | Thomas Anderson | Major revision. Expanded scope to include GDPR DPA inquiries. Added RACI matrix and detailed eDiscovery procedures. Integrated external counsel management process. |
| 3.0 | 2023-11-20 | Amelia Chen (Sr. Legal Counsel) | Revised to integrate the launch of HealthPay Financial Services. Added policies and procedures for financial services regulators (CFPB, Fed). Introduced the triage classification matrix. |
| 4.0 | 2024-08-15 | Thomas Anderson | Comprehensive refresh to align with the EU AI Act effective date. Added the VP of AI role to RACI. Incorporated the Onit Legal Hold tool and RelativityOne platform into technical controls and procedures. SOP-ID standardized from "INQ-01" to "SOP-LEGC-011". |
| 4.2 | 2025-01-10 | Thomas Anderson | Interim update. Refined escalation pathway and updated external counsel panel. Added clarity to AI Technical Documentation controls following first-generation market feedback from EU MSAs. |
| 4.4 | 2025-04-22 | Maria Gonzalez (GC) | Approved update to Critical triage criteria post-NIST consultation. Updated training requirements for the Crisis Simulation Tabletop. |
| 4.5 | 2026-05-16 | Thomas Anderson | Scheduled biennial comprehensive review. Updated risk classification criteria, clarified scoping procedures, and incorporated lessons learned from the Q4 2025-Issue. Confirmed GDPR alignment. |