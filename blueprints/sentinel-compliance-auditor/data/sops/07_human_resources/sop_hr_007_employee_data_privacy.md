---
sop_id: "SOP-HR-007"
title: "Employee Data Privacy"
business_unit: "Human Resources"
version: "1.8"
effective_date: "2025-03-27"
last_reviewed: "2026-06-22"
next_review: "2026-12-03"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Employee Data Privacy

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for the collection, processing, storage, transfer, and disposal of Employee Personal Data at Meridian Health Technologies, Inc. ("Meridian" or "the Company"). The purpose of this SOP is to:

- Ensure compliance with the General Data Protection Regulation (EU) 2016/679 (GDPR), the Health Insurance Portability and Accountability Act of 1996 (HIPAA), and other applicable data protection laws across all jurisdictions in which Meridian operates.
- Define the legitimate bases, purposes, and boundaries for processing Employee Personal Data.
- Operationalize the data subject rights of all Meridian employees, contractors, and applicants globally.
- Establish clear governance, accountability, and technical controls to protect Employee Personal Data from unauthorized access, alteration, disclosure, or destruction.
- Implement the principles of Privacy by Design and Default as mandated by Article 25 of GDPR across all HR systems and processes.
- Maintain alignment with Meridian's SOC 2 Type II, ISO 27001:2022, and HITRUST CSF certifications.

### 1.2 Scope

#### 1.2.1 In-Scope Entities and Individuals

This SOP applies to:

| Category | Coverage Detail |
|---|---|
| **Employees** | All full-time, part-time, and temporary employees of Meridian Health Technologies, Inc. across all global offices (Boston HQ, London, Berlin, Singapore, Toronto) and remote workers. |
| **Applicants** | All individuals who submit applications for employment, including those who are ultimately not hired. |
| **Alumni** | Former employees whose data is retained in accordance with legal and business retention requirements. |
| **Contractors and Consultants** | Independent contractors, consultants, and agency temporary workers engaged by Meridian, to the extent Meridian processes their personal data as a Data Controller. |
| **Dependents and Beneficiaries** | Spouses, domestic partners, children, and other dependents whose personal data is submitted for benefits administration, emergency contacts, or other employment-related purposes. |
| **Board Members** | Non-employee members of the Board of Directors whose personal data is processed for governance purposes. |

#### 1.2.2 In-Scope Data Categories

This SOP governs "Employee Personal Data," defined as any information relating to an identified or identifiable natural person that is processed in the context of the employment or engagement relationship. Categories are detailed in Section 5.2.

#### 1.2.3 In-Scope Systems

This SOP covers data processed in the following Meridian systems, whether hosted on-premises or in cloud environments:

| System | Purpose | Hosting |
|---|---|---|
| Workday HCM | Core HRIS, payroll, benefits, talent management | AWS us-east-1 |
| Greenhouse | Applicant tracking and recruitment | AWS us-east-1 |
| Culture Amp | Employee engagement and performance | AWS eu-west-1 |
| ADP Workforce Now | International payroll (UK, Germany) | ADP-managed |
| SAP SuccessFactors | Singapore and Canada HR operations | Azure |
| Okta | Identity and access management | AWS |
| Microsoft 365 | Email, documents, collaboration | Microsoft Cloud |
| Snowflake | HR analytics and reporting | AWS us-east-1 |
| Confluence | Policy documentation and knowledge management | AWS us-east-1 |

#### 1.2.4 Out-of-Scope

- Patient, provider, and member data governed under SOP-DS-003 (Clinical Data Privacy) and SOP-DS-005 (MedInsight Data Governance).
- Customer financial data governed under SOP-FIN-012 (HealthPay Data Protection).
- B2B vendor contacts, which are governed under SOP-LGL-004 (Third-Party Data Management).

#### 1.2.5 Jurisdictional Coverage

This SOP establishes a global baseline that meets the highest applicable standard (GDPR). Where local law exceeds this baseline, the local standard applies. The EU Employee Data Protection Addendum (see Appendix A of this SOP) applies to employees in the London and Berlin offices.

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Binding Corporate Rules (BCR)** | Meridian's internal data protection policy for intra-group transfers to Singapore and Canada, approved by the Berlin Supervisory Authority (Berliner Beauftragte für Datenschutz und Informationsfreiheit) in Q1 2025. |
| **Consent** | Any freely given, specific, informed, and unambiguous indication of the data subject's wishes by which they, by a statement or by clear affirmative action, signify agreement to the processing of their personal data (GDPR Art. 4(11)). Meridian recognizes the power imbalance inherent in employment relationships and **DOES NOT** rely on employee consent as a lawful basis for routine processing. |
| **Data Controller** | The entity that determines the purposes and means of processing personal data. Meridian is the Data Controller for all Employee Personal Data covered by this SOP. |
| **Data Processor** | A third party that processes personal data on behalf of Meridian (e.g., ADP, Culture Amp, AWS). |
| **Data Protection Impact Assessment (DPIA)** | A mandatory risk assessment required under GDPR Art. 35 for processing activities likely to result in high risk to the rights and freedoms of natural persons. |
| **Employee Personal Data** | Any information relating to an identified or identifiable natural person processed in the context of employment, including but not limited to: name, identification number, location data, online identifier, or factors specific to the physical, physiological, genetic, mental, economic, cultural, or social identity of that person. |
| **Ergänzende Vertragsbedingungen (EVB-IT)** | Supplementary contractual terms for IT procurement, used in the Berlin office for local system contracts. |
| **Lawful Basis** | The legal ground for processing under GDPR Art. 6. For employee data, Meridian primarily relies on: (a) performance of the employment contract (Art. 6(1)(b)); (b) legal obligation (Art. 6(1)(c)); and (c) legitimate interests balanced against fundamental rights and freedoms (Art. 6(1)(f)). |
| **PHI (Protected Health Information)** | As defined by HIPAA, individually identifiable health information held or transmitted by a covered entity or its business associate. Employee health data within self-insured health plans may constitute PHI. |
| **Privacy by Design and Default** | The requirement under GDPR Art. 25 to implement appropriate technical and organizational measures designed to implement data protection principles and integrate necessary safeguards into processing. |
| **Right of Access (DSAR)** | The right of a data subject to obtain from the controller confirmation as to whether personal data concerning them is being processed, and access to that data and associated information (GDPR Art. 15). |
| **Sensitive Personal Data (Special Categories)** | Data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health, or data concerning a natural person's sex life or sexual orientation (GDPR Art. 9). |
| **Standard Contractual Clauses (SCCs)** | European Commission-approved model contracts for the transfer of personal data to third countries, utilized for transfers to our Toronto and Singapore offices. |
| **Subject Access Request (DSAR)** | A formal request from a data subject exercising their Right of Access. |
| **Third Country** | Any country outside the European Economic Area (EEA) that has not received an adequacy decision from the European Commission. |
| **Works Council (Betriebsrat)** | Employee representative body established at the Berlin office under the Betriebsverfassungsgesetz (BetrVG), with co-determination rights over the implementation of technical systems that monitor employee behavior or performance. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| ART | Article (of GDPR) |
| BAA | Business Associate Agreement |
| BCR | Binding Corporate Rules |
| CHRO | Chief Human Resources Officer |
| CISO | Chief Information Security Officer |
| CPO/DPO | Chief Privacy Officer / Data Protection Officer |
| DPIA | Data Protection Impact Assessment |
| DSAR | Data Subject Access Request |
| ECPA | Employee Consent and Processing Agreement |
| EEA | European Economic Area |
| EMLA | Employee Master List Assessment |
| ER | Employee Relations |
| HRIS | Human Resources Information System |
| IAM | Identity and Access Management |
| LOA | Leave of Absence |
| NIST AI RMF | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework |
| PII | Personally Identifiable Information |
| PHI | Protected Health Information |
| RACI | Responsible, Accountable, Consulted, Informed |
| RBAC | Role-Based Access Control |
| ROPA | Record of Processing Activities |
| SLA | Service Level Agreement |
| SOC 2 | System and Organization Controls 2 |
| SR 11-7 | Federal Reserve Supervisory Letter 11-7 on Model Risk Management |
| WoW | Ways of Working |

## 3. Roles and Responsibilities

The following RACI matrix establishes accountability for Employee Data Privacy activities within Meridian.

| Activity / Decision | CHRO (J. Walsh) | CPO/DPO (Dr. K. Weber) | VP IT Ops (S. Torres) | CISO (R. Kim) | Legal/GC (M. Gonzalez) | VP Eng. (D. Park) | People Operations | All Employees |
|---|---|---|---|---|---|---|---|---|
| **Policy Ownership and Annual Review** | **A** | R | C | C | C | I | I | I |
| **DPIA Execution and Approval** | C | **A** | R | R | C | C | I | I |
| **Art. 30 ROPA Maintenance (HR Data)** | R | **A** | C | C | C | I | I | I |
| **DSAR Fulfillment** | I | **A** | R | R | C | C | I | I |
| **Data Breach Detection and 24hr Escalation** | I | R | **A** | R | I | R | I | R |
| **Breach Notification (72-hour DPA)** | I | **A** | I | I | R | I | I | I |
| **Role-Based Access Provisioning** | C | I | **A** | C | I | R | R | I |
| **Consent Management for Non-Mandatory Processing** | I | C | I | I | **A** | I | **R** | I |
| **Employee Data Subject Rights Awareness** | C | R | I | I | I | I | **A** | I |
| **Adherence to Privacy Policies** | I | I | I | I | I | I | I | **A** |

**Key:**
- **R (Responsible):** Performs the task.
- **A (Accountable):** Ultimately answerable for the task; sign-off authority.
- **C (Consulted):** Input sought before action.
- **I (Informed):** Kept up-to-date.

### 3.1 Specific Role Descriptions

**Chief Human Resources Officer (CHRO), Jennifer Walsh:** Serves as the business process owner for HR data. Accountable for ensuring HR strategy, third-party procurement, and internal processes align with this SOP. Owns the budget for privacy-enhancing HR technologies and training.

**Chief Privacy Officer / Data Protection Officer (CPO/DPO), Dr. Klaus Weber:** An independent, statutory role under GDPR Art. 37. Dr. Weber, based in the Berlin office, monitors compliance, advises on DPIAs, acts as the primary contact point for supervisory authorities and data subjects, and has a direct reporting line to the CEO and Audit Committee. Dr. Weber's approval is required for any new processing activity involving Special Categories of Employee Data.

**Chief Information Security Officer (CISO), Rachel Kim:** Accountable for the technical implementation of security controls protecting Employee Personal Data. Ensures encryption standards, access controls, and logging are implemented per SOC 2 and ISO 27001:2022 controls and provides the DPO with breach notification data.

**VP of IT Operations, Sarah Torres:** Responsible for operational management of HR systems, user access administration, and data lifecycle management (backups and deletion).

**VP of Engineering, Daniel Park:** Responsible for ensuring that any custom application, API endpoint, or internal tool built by Meridian's engineering team that touches HR data complies with the "Security by Design" mandates and the data minimization requirements of this SOP before deployment.

**General Counsel, Maria Gonzalez:** Advises on the legal interpretation of employment law versus data protection law, manages legal privilege claims in DSAR responses, and negotiates Data Processing Agreements (DPAs) with all HR vendors.

## 4. Policy Statements

Meridian Health Technologies commits to the following fundamental principles governing the processing of Employee Personal Data:

1.  **Lawfulness, Fairness, and Transparency:** Meridian shall process Employee Personal Data lawfully, fairly, and in a transparent manner. Every new applicant and employee shall receive a layered privacy notice (see Section 5.1.2) detailing what data is collected and why. In accordance with GDPR Art. 5(1)(a), there shall be no invisible or unexpected processing.

2.  **Purpose Limitation:** Employee Personal Data shall be collected for specified, explicit, and legitimate purposes as outlined in the Record of Processing Activities (ROPA) maintained by the DPO and shall not be further processed in a manner incompatible with those purposes. Historical data stored for archiving in the public interest under GDPR Art. 89 receives a specific derogation.

3.  **Data Minimization:** Every collection point within Workday, Greenhouse, and any integrated ATS/HRIS must be reviewed semi-annually to ensure only data adequate, relevant, and limited to what is necessary for the specific employment purpose is collected. "Nice-to-know" fields shall be removed.

4.  **Accuracy:** Employees have the right and the mechanism (Workday self-service) to rectify inaccurate personal data without undue delay. HR Business Partners shall process these rectification requests within 10 business days.

5.  **Storage Limitation:** Employee files shall not be retained indefinitely. Specific retention periods based on data category and legal necessity are established in the ROPA (see Section 5.7). Upon expiry of the retention period, data shall be securely deleted or anonymized.

6.  **Integrity and Confidentiality:** Employee Personal Data shall be processed in a manner ensuring appropriate security, including protection against unauthorized or unlawful processing and against accidental loss, destruction, or damage, using appropriate technical and organizational measures as defined in SOP-IT-014 (Information Security Controls).

7.  **Accountability:** Meridian, as the Data Controller, shall be responsible for and able to demonstrate compliance with all the above principles. This is achieved through auditable DPIAs, the ROPA under Art. 30, documented compliance reviews, and mandatory data protection training.

8.  **Prohibition of Solely Automated Decision-Making:** Meridian shall not subject employees to decisions based solely on automated processing, including profiling, which produces legal effects or similarly significantly affects them, unless explicitly authorized by national law, in compliance with GDPR Art. 22. Meridian's current use of Culture Amp does not constitute automated individual decision-making for the purposes of Art. 22.

9.  **Protected Health Information (PHI):** Meridian recognizes that employee health information processed in the context of our self-insured health plan is classified as PHI. Access to this data is strictly limited to the Benefits Team. Meridian shall apply the minimum necessary standard for disclosures to group health plan sponsors, though the operational specifics of this review for every instance are managed through the plan sponsor amendment rather than automated system flagging.

10.  **Transborder Data Flows:** All transfers of Employee Personal Data from the EEA to Meridian's US headquarters or to our Singapore office must be covered by the Company's Binding Corporate Rules or executed EU Standard Contractual Clauses.

## 5. Detailed Procedures

This section defines the step-by-step operational procedures to be followed by the People Operations team, managers, and support functions.

### 5.1 Transparency and Notice

#### 5.1.1 Candidate Privacy Notice

Upon application submission via Greenhouse, all candidates must:
1.  Receive an automated email from `privacy@meridian.health` containing a link to the Candidate Privacy Notice (Document HR-FRM-007a).
2.  The notice, written in clear plain English and German (for Berlin office applicants), explains:
    - Data Controller: Meridian Health Technologies, Inc., 1 Meridian Square, Boston, MA 02110, and Meridian Health Technologies GmbH, Unter den Linden 10, 10117 Berlin (for EU applicants).
    - Data Collected: CV/résumé data, cover letters, assessment results, interview notes, background check results (post-offer, where local law permits).
    - Purpose: Evaluating suitability for the specific role and potentially other future roles (with an opt-in).
    - Legal Basis: Steps prior to entering into a contract (Art. 6(1)(b)), legitimate interest in identifying suitable candidates (Art. 6(1)(f)), and explicit consent for Special Categories (Art. 9(2)(a)) where an applicant voluntarily provides health or diversity data.
    - Retention: 12 months for unsuccessful candidates; see Section 5.7.

#### 5.1.2 Employee Privacy Notice (Layered)

On day one of employment, and annually thereafter in the first week of December, all employees will receive a "Privacy at Work" notification via Workday's inbox, requiring acknowledgment. The layered notice consists of:

- **Layer 1: Infographic** — A one-page visual overview of where data sits and for what high-level purposes (payroll, performance, benefits).
- **Layer 2: Full Notice** — A hyperlinked document providing a detailed table of processing activities, retention periods, and a description of employee rights under GDPR Articles 15-21 and 77.
- **Layer 3: Policy Library** — A link to this SOP-HR-007 and the DPO's contact details.

### 5.2 Categories of Data Collected

The following table represents a mandatory list of data categories, their lawful basis, and the system of record. This must align perfectly with the Art. 30 ROPA managed by Dr. Weber.

| Data Category | Examples | Primary System | Lawful Basis (GDPR) |
|---|---|---|---|
| **Identification & Contact** | Name, DOB, SSN/SIN/NI Number, Address, Personal Email, Phone, Emergency Contacts | Workday, ADP | Contract (Art. 6(1)(b)), Legal Obligation (Art. 6(1)(c)) |
| **Recruitment Data** | CV, interview scorecards, Psychometric assessment results, offer letters | Greenhouse | Legitimate Interest (Art. 6(1)(f)), Pre-contractual steps |
| **Compensation & Benefits** | Salary, Bonus targets, Stock grants, Bank account, Insurance beneficiaries, LTD details | Workday, Fidelity NetBenefits | Contract (Art. 6(1)(b)), Legal Obligation |
| **Performance & Talent** | Goals, Performance ratings, 360 feedback, Promotion history, Succession planning flags | Workday, Culture Amp | Legitimate Interest (Art. 6(1)(f)) |
| **Time & Attendance** | PTO balances, Sick time, Clock-in/out data | Workday | Legal Obligation (Art. 6(1)(c)) |
| **System & IT Use** | User ID, Okta logs, Email metadata, Slack activity timestamps | Okta, Microsoft 365 | Legitimate Interest (Art. 6(1)(f)) — Network security, insider threat detection |
| **Sensitive / Special Categories (Art. 9)** | **Health data** (disability accommodations, LOA documentation), **Biometric data** (if used for time clocks in Berlin office), **Diversity data** (race/ethnicity, veteran status for EEOC/Voluntary monitoring) | Workday (restricted), OHM (Occupational Health Management) | Explicit Consent (Art. 9(2)(a)) or Employment Legal Obligation (Art. 9(2)(b)) |
| **Disciplinary & Grievance** | ER case notes, investigations, performance improvement plans (PIPs) | Workday (confidential), ER shared drive | Legitimate Interest (Art. 6(1)(f)), Legal Obligation |

### 5.3 Employee Rights and DSAR Processing

Meridian must respond to all Data Subject Access Requests (DSARs) within **one month** (30 calendar days) of receipt, in accordance with GDPR Art. 12(3). This extends to two months (60 calendar days) for complex or multiple requests, but **the DPO must inform the employee of the extension within the first 30 calendar days**.

#### 5.3.1 DSAR Intake

1.  Employees may submit a DSAR verbally, via email to `privacy@meridian.health`, or by submitting a ticket through the ServiceNow "Privacy Rights Request" portal.
2.  Any Meridian employee who receives a DSAR must forward it to `privacy@meridian.health` within **4 business hours**. Failure to do so is a policy violation.
3.  Upon receipt, the DPO's office logs the request in the Jira Service Management (JSM) "DSAR-QUEUE" project with a unique ticket ID (e.g., DSAR-2026-045).

#### 5.3.2 Identity Verification

Before releasing data, the DPO must verify the requestor's identity. Acceptable methods include:
- Verification of government-issued ID via a secure Okta Verify Identity Proofing session.
- If the request comes from a known email, the DPO may ask a "gatekeeper" knowledge question (e.g., "What is your Workday Employee ID?").
- **No data shall be released** until identity is confirmed to the DPO's satisfaction.

#### 5.3.3 Data Assembly and Extraction

1.  The DPO creates a task in JSM for each system owner (e.g., VP of People Operations for Workday, VP of IT Ops for Slack logs).
2.  System owners run an export from the production system to a designated, encrypted SharePoint location (URL: `privacy_dsar_staging`).
3.  The extracted data is collected by the DPO's Analyst. The Analyst reviews the data and redacts third-party personal data (e.g., names of other employees who gave peer feedback, unless consent from that peer is obtained) and legally privileged information, consulting with the General Counsel where necessary.
4.  A DSAR Response Package is compiled, consisting of:
    - A narrative explanation of the processing.
    - The specific copies of personal data.
    - A reiteration of the employee's rights (rectification, erasure, restriction, portability, right to lodge a complaint with a supervisory authority).

#### 5.3.4 Portability Requests

For requests to exercise the right to data portability under Art. 20, the People Operations team shall provide a structured, commonly used, and machine-readable format (JSON file). This is limited to data provided by the employee processed by automated means on the basis of consent or contract.

### 5.4 New HR Technology Procurement (Privacy by Design)

Before People Operations procures or builds any new system or tool that processes Employee Personal Data, a **Privacy Threshold Assessment (PTA)** must be completed. This procedure formalizes Article 25.

1.  **Initiation:** People Operations submits a ServiceNow "HR Tech Procurement Request."
2.  **PTA Triage:** The DPO determines if the processing is likely to be "high risk." Automatic triggers for a full DPIA include:
    - Processing of Special Categories of Data (e.g., a new wellness app).
    - Systemic monitoring of employee performance or behavior (e.g., key logging or productivity tracking).
    - Processing involving new technologies (e.g., sentiment analysis using AI on employee communications).
    - AI-driven talent analytics. Meridian's NIST AI RMF Profile guides this DPIA.
3.  **DPIA Execution:** The DPO, in collaboration with the CHRO, CISO, and the requesting team, conducts a DPIA using the French CNIL's PIA methodology template, adapted to Meridian. The DPIA must:
    - Describe the processing operations.
    - Assess the necessity and proportionality of the processing.
    - Define the risks to rights and freedoms.
    - Outline the measures to mitigate those risks.
4.  **Betriebsrat Consultation:** For any tool impacting the Berlin office, the VP of People Operations, Europe (London) must initiate a Works Agreement (Betriebsvereinbarung) negotiation with the Berlin Works Council **before** global deployment. The CHRO is accountable for ensuring this step is not skipped.
5.  **DPO Sign-Off:** No purchase order or Statement of Work (SOW) can be executed for a high-risk HR tool without the DPO's digital sign-off in ServiceNow.

### 5.5 International Data Transfers

Meridian's HR data originates globally and is consolidated in AWS us-east-1 (Workday). The transfer mechanism must be in place *before* any bulk data migration.

1.  **EEA to USA:** Data transfers from the Berlin and London offices to the US corporate offices are governed by Meridian's Binding Corporate Rules (BCR) for Processors and Controllers.
2.  **Transfers to Singapore:** Singapore is a "Third Country." Meridian uses the 2021 EU Standard Contractual Clauses (Module 2: Controller to Controller) as a transfer mechanism, supplemented by a Transfer Impact Assessment (TIA) to ensure Singaporean law does not impinge on the effectiveness of the SCCs.
3.  **Recipients Outside the EEA:** The People Operations team must, at least annually, ensure that all third-party HR systems with access to EU employee data have executed DPAs incorporating the SCCs. The DPO maintains a Transfer Register as a sub-log of the Art. 30 ROPA.

### 5.6 Internal Investigations and Employee Monitoring

When Meridian conducts investigations into employee conduct, specific privacy safeguards apply to counterbalance the Company's legitimate interests:

1.  **Authorization:** Accessing an employee's Slack messages or email metadata for an investigation requires a formal Case Initiation Form co-signed by the CHRO (or designate from Employee Relations) and the General Counsel, or her designate.
2.  **Scope of Access:** IT's access is limited to the specific mailboxes, folders, and date ranges specified in the form. A data extraction log is generated and appended to the case file.
3.  **Notification:** The subject employee will be informed of the investigation and the nature of the data accessed, but only at a time determined by Legal to be non-prejudicial to the investigation.

### 5.7 Data Retention and Destruction

Meridian retains Employee Personal Data only as long as necessary or mandated. The "End of Employment" clock starts on the effective date of termination.

| Record Category | Retention Period (Post-Employment) | Justification | Destruction Method |
|---|---|---|---|
| **Core HR File (excl. ER cases)** | **10 years** | Statute of limitations on tax and social security audits | Workday Automated Purge (or manual overwrite + encrypted deletion) |
| **Recruitment Data (Unsuccessful)** | **12 months** from application | Defense of legal claims (e.g., discrimination) | Greenhouse automatic anonymization |
| **Payroll & Tax Records** | **7 years** | IRS Section 31.3502-1, Betriebsrentengesetz (Berlin) | Encrypted deletion at storage level |
| **Special Categories (Health)** | **5 years** after last action | Local medical records laws | Secure shredding of OHM data by Occupational Health Provider |
| **Employee Relations (ER) Cases (Closed)** | **7 years** from closure | Defense against legal claims | Physical and electronic file destruction |
| **Okta and IT Usage Logs** | **1 year** | SOC 2 and insider threat detection | Automated SIEM log rotation |

**Procedure:**
1.  On the 1st day of every month, the Workday administrator runs an "End of Service + Policy" report identifying records that have passed their retention window.
2.  The report is reviewed by the DPO for any unresolved legal holds.
3.  Once cleared, the "Purge Program" script is executed, generating a destruction certificate. This certificate is stored as evidence for the Art. 30 ROPA.

### 5.8 Breach Notification Procedure (GDPR)

A "Personal Data Breach" is a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, Employee Personal Data.

1.  **Detection and Containment (0-4 hours):** Any employee recognizing a breach (e.g., phishing success, lost laptop) must immediately notify the SOC at `soc@meridian.health`. CISO Rachel Kim's team immediately initiates containment.
2.  **Evaluation and Escalation (4-24 hours):** The CISO assesses risk using the Meridian Breach Risk Matrix. If there is a risk to the rights and freedoms of employees, the CISO escalates to the DPO, Dr. Weber, within 24 hours of detection.
3.  **Supervisory Authority Notification (within 72 hours):** Dr. Weber, as DPO, is responsible for notifying the relevant supervisory authority (e.g., Berlin Commissioner for Data Protection) within 72 hours of Meridian becoming aware of the breach, as mandated by Art. 33. The notification includes the nature of the breach, categories of data, records affected, and mitigation measures.
4.  **Data Subject Notification (without undue delay):** If the breach is likely to result in high risk (identity theft, financial loss), the DPO and General Counsel determine the content of a communication to affected employees, sent "without undue delay" (Art. 34). A dedicated hotline is established.
5.  **Breach Register:** The DPO maintains a master Breach Register (stored in Jira) detailing all incidents, even those not requiring notification.

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control | Implementation Detail | Tool / System |
|---|---|---|
| **Encryption at Rest** | All HR data storage volumes (EBS, S3 buckets) must be encrypted with AES-256. | AWS Key Management Service (KMS) |
| **Encryption in Transit** | All data communication must use TLS 1.3. Internal application-to-application traffic between Workday and M365 must be encrypted. | Service Mesh / VPC Peering Policies |
| **Access Control (RBAC)** | Role-Based Access Control (RBAC) implemented in Workday, Greenhouse, and Culture Amp. Access is segmented into granular security groups (e.g., `HR_BP_NorthAmerica`, `GB_Recruiter`, `DE_Payroll_Admin`). | Okta / Workday Security Configuration |
| **Multi-Factor Authentication (MFA)** | Mandatory phishing-resistant MFA (Okta FastPass / YubiKey) for all HR system access from managed devices. SMS-based MFA is deprecated for HR data. | Okta Verify |
| **Automated Anonymization** | Greenhouse anonymizes candidate records on a rolling 13-month schedule for unsuccessful applicants who do not opt-in to retention. | Greenhouse |
| **Data Loss Prevention (DLP)** | Microsoft 365 DLP policies block the transmission of Sensitive Data (SSN/SIN patterns, NI numbers) from Meridian workstations to unmanaged external recipients. | Microsoft Purview Information Protection |
| **Audit Logging** | All access, modification, and export actions for Special Categories of data must generate an immutable audit log sent to the SIEM. Retention: Minimum 3 years. | Splunk / AWS CloudTrail |

### 6.2 Administrative Controls

- **Bi-Annual Access Review:** Every April and October, the VP of IT Ops and the CHRO will conduct a formal Access Review. This involves reviewing all user accounts with access to Workday's "Compensation" and "Benefits" domains. Any inappropriate privileges found constitute a "Finding" and must be remediated within 3 business days.
- **Clean Desk Policy:** Hard copies of Employee files must be stored in locked Verifile cabinets with digital access PINs. A monthly physical check is performed in Boston and Berlin offices.
- **SOP Alignment:** This policy is intrinsically linked to SOP-DS-001 (Data Classification and Handling) and SOP-IT-014 (Information Security Controls). All HR staff are "Data Guardians" within the Meridian Data Governance Framework.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The DPO and CHRO report on the following KPIs quarterly to the Risk and Compliance Committee, chaired by Dr. Sarah Chen.

| KPI | Target | Measurement Tool |
|---|---|---|
| **DSAR Compliance Rate** (requests closed within 30-day deadline) | **100%** | Jira Service Management Dashboard |
| **DPIA Completion Before Procurement Go-Live** | **100%** | ServiceNow HR Tech Procurement vs. Jira DPIA Register |
| **Bi-Annual Access Review Completion** | **100% by April 15 and Oct 15** | Confirmed sign-off by CHRO and DPO |
| **Privacy Training Completion (Active Employees)** | **>95%** | Culture Amp / Workday Learning |
| **Mean Time to Notify (MTTN) — Breach to DPO** | **< 4 hours** | SOC Incident Response Ticket linkage |

### 7.2 Reporting Cadence

| Report Type | Audience | Frequency | Owner |
|---|---|---|---|
| **DSAR Fulfillment KPIs** | CHRO, DPO | Monthly | DPO Office (J. Walsh copied) |
| **Retention & Destruction Reporting** | DPO, VP IT Ops | Monthly (1st of month) | S. Torres |
| **HR Privacy Audit & Access Review** | CHRO, DPO, CISO | Bi-Annual (April & October) | S. Torres / R. Kim |
| **Comprehensive Data Privacy Review** | CEO, Board Audit Committee | Annually (December) | Dr. K. Weber |

## 8. Exception Handling and Escalation

Deviations from this SOP must be handled through a formal exception process; operating outside the policy without a registered exception is a direct violation subject to disciplinary action up to and including termination, as defined in SOP-LGL-002 (Employee Code of Conduct).

### 8.1 Exception Request Procedure

1.  **Initiation:** The requesting party (e.g., a VP wanting to bypass data minimization to collect a new data field) submits a Policy Exception Request through ServiceNow.
2.  **Risk Assessment:** The CISO and DPO jointly conduct a risk assessment and document the compensating controls required.
3.  **Approval Matrix:**
    - **Low Risk:** (e.g., extending a minor retention date by 30 days) — Approved by DPO and CHRO.
    - **Medium Risk:** (e.g., temporary emergency access to PHI for an unauthorized role) — Approved by DPO, CHRO, and CISO.
    - **High Risk:** (e.g., use of a non-approved SaaS tool processing Special Categories of data) — Approved by CEO or Audit Committee, upon recommendation from the DPO.
4.  **Time-Bound:** All exceptions are time-bounded and registered in the Jira Exception Register for quarterly review. No permanent exceptions are granted unless the SOP itself is formally revised.

## 9. Training Requirements

A privacy-aware workforce is a foundational administrative control. Training is tailored by role.

| Training Module | Target Audience | Frequency | Delivery Method | Tracking |
|---|---|---|---|---|
| **META-001: Global Data Privacy & Ethics** | All employees globally on Day 1 and annually on anniversary | Annual | Workday Learning (SCORM 1.2) | Completion Rate in Workday |
| **META-002: GDPR at Work (EU Focused)** | Berlin & London office staff, all People Operations globally | Annual | In-person (Berlin) / Zoom (London) / eLearning | DPO Training Register |
| **META-003: HIPAA Privacy for Employers** | US Benefits Specialists, Self-Insured Plan Team, relevant ER team | Annual | Zoom Webinar by outside counsel | Compliance Team Register |
| **META-004: DSAR Handling & Data Security** | People Operations, IT Support, SOC Team | Bi-Annual | Dr. Weber's Direct Briefings | Attendance Log (DocuSign) |

Non-compliance with mandatory training results in automated notification to the employee's manager and restricted access to HR systems after a 30-day grace period.

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Document Name | Relationship |
|---|---|---|
| SOP-PR-001 | Meridian Global Data Protection Policy (Umbrella) | Foundational Policy |
| SOP-DS-001 | Data Classification and Handling | Controls for what constitutes "Confidential" and "Restricted" |
| SOP-IT-014 | Information Security Controls | Technical safeguards detailed; Encryption standard A.10.1.1 |
| SOP-LGL-002 | Employee Code of Conduct and Disciplinary Action | Defines consequences for privacy violation |
| SOP-LGL-004 | Third-Party Data Management (Vendor DPAs) | Required HR vendor contract standards |
| SOP-DS-003 | Clinical Data Privacy | Contrasting policy for patient data |
| SOP-BCP-001 | Business Continuity and Disaster Recovery | Data availability and backup verification for HR systems |

### 10.2 External Standards and Legal References

- Regulation (EU) 2016/679 (General Data Protection Regulation)
- Health Insurance Portability and Accountability Act (HIPAA) of 1996
- NIST Special Publication 800-53, Revision 5: Security and Privacy Controls for Information Systems and Organizations
- NIST AI 100-1: Artificial Intelligence Risk Management Framework
- ISO/IEC 27001:2022, Annex A.5.34 (Privacy and protection of PII)
- SOC 2 TSC 2017 CC6.1 (Logical and Physical Access Controls)
- Meridian Health Technologies Binding Corporate Rules (BCR), as approved 15 Feb 2025.

## 11. Revision History

| Version | Date | Author / Owner | Summary of Changes |
|---|---|---|---|
| 1.0 | 2022-01-25 | J. Walsh | Initial Policy Creation and ROPA alignment. |
| 1.4 | 2023-06-01 | Dr. K. Weber | Major revision: Operationalized DSAR timelines (30-day mandate); Added Art. 30 ROPA linkage; Introduced DPIA mandatory triggers for AI profiling. |
| 1.6 | 2024-09-15 | J. Walsh / S. Torres | Updated the International Data Transfer section to reflect the new EU-US Data Privacy Framework adequacy decision; Added Okta AMFA requirement; Updated retention for payroll records to 7 years based on Texas workforce audit. |
| 1.7 | 2025-03-20 | Dr. K. Weber | Revised DPIA process post-CE certification. Added NIST AI RMF reference for HR analytics tools. Replaced "Annual" with specific Bi-Annual access calendar dates. |
| 1.8 | 2026-06-22 | J. Walsh | Merged feedback from Works Council Agreement (BV-ID: 2026-04-BE1). Strengthened language on pseudonymization in Culture Amp. Clarified exception timelines; introduced automated Greenhouse anonymization flag. Updated role titles post-restructure. |