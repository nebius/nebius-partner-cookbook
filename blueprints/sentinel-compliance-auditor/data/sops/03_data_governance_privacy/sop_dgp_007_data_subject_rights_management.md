---
sop_id: "SOP-DGP-007"
title: "Data Subject Rights Management"
business_unit: "Data Governance & Privacy"
version: "3.5"
effective_date: "2024-06-22"
last_reviewed: "2025-03-05"
next_review: "2025-09-11"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, governance, and operational workflows for managing Data Subject Rights (DSR) requests at Meridian Health Technologies, Inc. The purpose of this document is to ensure that Meridian processes all verifiable requests from data subjects—including patients, healthcare providers, employees, and clinical trial participants—in a consistent, auditable, and timely manner that aligns with regulatory obligations and the organization's commitment to data ethics.

This SOP operationalizes the privacy principles articulated in the Meridian Privacy Policy and the Data Governance Charter. It provides actionable procedures for intake, identity verification, fulfillment, and documentation of requests under applicable data protection frameworks, including the General Data Protection Regulation (GDPR) for European Union data subjects, the Health Insurance Portability and Accountability Act (HIPAA) for Protected Health Information (PHI), and other state-level comprehensive privacy laws where applicable.

### 1.2 Scope

#### 1.2.1 In Scope
This SOP applies to all Personal Data and Protected Health Information processed by Meridian Health Technologies across all business lines, geographic regions, and technology platforms, including but not limited to:

- **Clinical AI Platform:** Patient risk scores, diagnostic imaging data, adverse event predictions, and clinician feedback records processed by the platform, deployed in 340+ hospitals and clinics across North America and the EU.
- **HealthPay Financial Services:** Payer and patient financial data, credit scoring models, loan application data, claims adjudication records, and payment processing information.
- **MedInsight Analytics:** Population health datasets containing PHI for approximately 12 million patients, care gap analyses, and outcomes prediction models.
- **Meridian SaaS Platform:** All multi-tenant cloud infrastructure hosted on AWS (us-east-1, eu-west-1), including data stored in Snowflake, PostgreSQL, Redis, and S3 data lakes.
- **Corporate Systems:** Employee data hosted in Workday, applicant tracking systems, and internal communications platforms.
- **Third-Party Processors:** Data shared with subprocessors, Business Associates, and analytics partners where Meridian acts as a Data Controller or Business Associate.

#### 1.2.2 Data Subject Rights Addressed
This SOP provides procedures for the following rights:

| Right Category | GDPR Article | HIPAA Provision | Description |
|----------------|--------------|-----------------|-------------|
| Right of Access | Art. 15 | 45 CFR § 164.524 | Obtain confirmation of processing and a copy of personal data |
| Right to Rectification | Art. 16 | 45 CFR § 164.526 | Correct inaccurate or incomplete personal data |
| Right to Erasure | Art. 17 | N/A (covered under state laws) | Delete personal data under specific conditions |
| Right to Restrict Processing | Art. 18 | 45 CFR § 164.522 | Limit processing under certain circumstances |
| Right to Data Portability | Art. 20 | 45 CFR § 164.524 (access) | Receive data in a structured, machine-readable format |
| Right to Object | Art. 21 | N/A | Object to processing based on legitimate interests or direct marketing |
| Right to an Accounting of Disclosures | N/A | 45 CFR § 164.528 | Record of PHI disclosures made in the prior six years |

#### 1.2.3 Out of Scope
This SOP does not cover:
- Data Subject Rights under laws where Meridian is not an established entity or does not offer services (e.g., Brazil's LGPD, China's PIPL) unless explicitly adopted by the Chief Privacy Officer.
- Law enforcement or national security access requests, which are governed by SOP-LEG-012 (Law Enforcement Data Request Handling).
- Internal data access for development, testing, or analytics purposes, which is governed by SOP-IS-045 (Data Access Control and Authorization).

#### 1.2.4 Applicability
This SOP applies to all employees, contractors, and third-party vendors of Meridian Health Technologies who may receive, process, or fulfill a Data Subject Rights request. Compliance with this SOP is mandatory and is incorporated into the Meridian Code of Conduct and vendor contractual obligations.

---

## 2. Definitions and Acronyms

For the purposes of this SOP, the following definitions and acronyms apply. Capitalized terms not defined herein shall have the meaning ascribed in the Meridian Data Governance Charter or the Master Services Agreement.

### 2.1 Definitions

| Term | Definition |
|------|------------|
| **Data Subject** | An identified or identifiable natural person to whom Personal Data relates. Includes patients, employees, providers (as individuals), and website visitors. |
| **Data Subject Rights (DSR) Request** | A formal, verifiable request from a Data Subject or their authorized representative to exercise one or more rights enumerated in Section 1.2.2. |
| **Personal Data** | Any information relating to a Data Subject, as defined under GDPR Article 4(1). Includes both direct identifiers (name, email, national ID) and indirect identifiers (IP address, device ID, patient record number). |
| **Protected Health Information (PHI)** | Individually identifiable health information transmitted or maintained by a Covered Entity or Business Associate, as defined under HIPAA 45 CFR § 160.103. |
| **Controller** | The entity that determines the purposes and means of processing Personal Data. Meridian is the Controller for employee data and the MedInsight analytics platform; it is a Joint Controller with healthcare provider customers for the Clinical AI Platform. |
| **Processor** | The entity that processes Personal Data on behalf of the Controller. Meridian is a Processor for HealthPay transaction data where the payer is the Controller. |
| **Business Associate** | An entity that creates, receives, maintains, or transmits PHI on behalf of a Covered Entity. Meridian is a Business Associate for all health system customers utilizing the Clinical AI Platform. |
| **Verifiable Request** | A DSR request where the identity of the Data Subject has been confirmed to a level of assurance appropriate to the sensitivity of the data being requested, using the methods defined in Section 5.2. |
| **Manifestly Unfounded or Excessive Request** | A DSR request that is clearly abusive, repetitive, or designed to cause disruption. Determined on a case-by-case basis by the DPO and General Counsel, using objective evidence of frequency, nature, and associated costs. |
| **Data Portability Package** | A structured ZIP archive containing the Data Subject's Personal Data in JSON and CSV formats as specified in Section 5.5. |

### 2.2 Acronyms

| Acronym | Full Form |
|---------|-----------|
| BAA | Business Associate Agreement |
| CJIS | Criminal Justice Information Services |
| CPO | Chief Privacy Officer |
| DPO | Data Protection Officer |
| DSR | Data Subject Rights |
| DLP | Data Loss Prevention |
| EEA | European Economic Area |
| EMR | Electronic Medical Record |
| IAM | Identity and Access Management |
| JIRA | Issue Tracking System (Atlassian) |
| KBA | Knowledge-Based Authentication |
| LGPD | Lei Geral de Proteção de Dados (Brazil) |
| MFA | Multi-Factor Authentication |
| PIA | Privacy Impact Assessment |
| PIPL | Personal Information Protection Law (China) |
| ROPA | Record of Processing Activities |
| SHA | Secure Hash Algorithm |
| SSAE | Statement on Standards for Attestation Engagements |
| TLS | Transport Layer Security |

---

## 3. Roles and Responsibilities

The effective management of Data Subject Rights requires a cross-functional governance structure with clearly defined accountability. The following RACI matrix assigns Responsibility, Accountability, Consulted, and Informed roles for each phase of the DSR lifecycle.

### 3.1 DSR Governance RACI Matrix

| Activity / Decision Point | CPO / DPO | General Counsel | CISO | VP Engineering | VP Customer Ops | VP IT Ops | Business Unit Owners | DSR Triage Team |
|---------------------------|-----------|-----------------|------|----------------|-----------------|-----------|----------------------|-----------------|
| DSR Intake & Logging | I | I | I | I | R | C | I | A |
| Identity Verification | C | I | C | I | I | I | I | R |
| Request Complexity Assessment | A | C | I | C | I | I | I | R |
| Data Discovery & Collection | I | I | I | A | C | R | R | C |
| Data Redaction & Review | I | A | I | C | I | I | C | R |
| Response Package Assembly | I | I | I | C | I | R | I | A |
| Final Approval & Release | A | C | I | I | I | I | I | I |
| Denial or Extension Decisions | C | A | I | I | I | I | I | R |
| Escalation to Supervisory Authority | A | R | I | I | I | I | I | I |

**Legend:** R = Responsible (does the work), A = Accountable (approves/owns), C = Consulted (provides input), I = Informed (notified of outcome)

### 3.2 Named Role Responsibilities

#### 3.2.1 Chief Privacy Officer / Data Protection Officer (Dr. Klaus Weber)
- Serves as the primary point of contact for EU supervisory authorities and data subjects on all DSR and privacy matters.
- Holds ultimate accountability for the DSR program, including timely and compliant fulfillment.
- Approves all DSR response extensions and denials.
- Conducts the balancing test for objections to legitimate interest processing.
- Reports quarterly on DSR metrics to the AI Governance Committee and annually to the Board.
- Maintains the Record of Processing Activities (ROPA), which is referenced during data discovery.

#### 3.2.2 General Counsel (Maria Gonzalez)
- Provides legal review for complex or precedent-setting DSR requests.
- Approves all denials based on legal privilege or disproportionate effort.
- Manages any litigation or regulatory inquiries arising from DSR responses.
- Reviews and approves BAA modifications related to DSR fulfillment.

#### 3.2.3 Chief Information Security Officer (Rachel Kim)
- Ensures identity verification mechanisms meet the required authentication assurance levels.
- Validates that data extraction and transmission methods maintain the confidentiality and integrity mandated for PHI and high-risk AI system data under the EU AI Act.
- Oversees logging and monitoring of DSR processing activities for security anomalies.
- Manages DLP controls to prevent unauthorized exfiltration during DSR fulfillment.

#### 3.2.4 Vice President of Engineering (David Park)
- Maintains and enhances the automated DSR fulfillment tooling, including the Data Subject Request Portal and the integration APIs with Snowflake, PostgreSQL, and S3.
- Ensures all data stores have documented schemas and data lineage accessible to the DSR Triage Team.
- Owns the technical implementation of the "Data Portability Package" format.

#### 3.2.5 Vice President of Customer Operations (Michael Chang)
- Manages the client-facing DSR escalation path for requests originating from enterprise customers (hospitals, payers) who are Controllers.
- Ensures customer agreements and BAAs are accessible to the DSR Triage Team to clarify the Controller-Processor relationship.
- Coordinates with customers when a DSR requires joint action.

#### 3.2.6 Vice President of IT Operations (Samantha Torres)
- Provisions access and service accounts needed by the DSR Triage Team to query production databases and log repositories.
- Ensures backup and archive systems are included in the scope of data discovery searches.
- Manages the secure file transfer infrastructure for delivering response packages.

#### 3.2.7 DSR Triage Team
A dedicated operational team within the Data Governance & Privacy unit, consisting of three privacy analysts (FTEs) and one part-time paralegal. The team is cross-trained on all Meridian product lines.
- Primary processor of all incoming DSR requests.
- Performs initial triage, identity verification (Level 1 and Level 2), and data collection.
- Maintains the DSR case management system (JIRA-based ticketing).

#### 3.2.8 Business Unit Owners
For each product line (Clinical AI, HealthPay, MedInsight, SaaS), the BU Owner (Dr. Aisha Okafor, Robert Liu, etc.) or their designated privacy liaison is responsible for:
- Maintaining an updated data inventory for their domain.
- Assisting the DSR Triage Team in locating data in unstructured or legacy systems.
- Identifying any contractual restrictions on data portability or deletion.

---

## 4. Policy Statements

Meridian Health Technologies is committed to honoring the rights of individuals whose data we process. The following policy statements serve as the non-negotiable principles governing all DSR activities. Any exception must follow the process in Section 8.

### 4.1 Core Principles

1. **Non-Discrimination:** Meridian shall not discriminate against any Data Subject for exercising their rights, including denial of services, differential pricing, or quality degradation, unless the service is predicated on the processing and the Data Subject has withdrawn consent where it is the sole lawful basis.
2. **Transparency:** All DSR responses will be provided in a concise, transparent, intelligible, and easily accessible form, using clear and plain language. The Meridian Privacy Policy (published at www.meridianhealth.com/privacy) will be updated at least annually to reflect the DSR process.
3. **Accuracy and Completeness:** Meridian will make commercially reasonable efforts to ensure that data provided in response to access and portability requests is a complete and accurate representation of the data held, subject to the limitations of our systems.
4. **Data Minimization in Response:** When fulfilling DSR requests, only the Personal Data of the requesting Data Subject shall be disclosed. Data of third parties, trade secrets, or internal security configurations are subject to mandatory redaction.
5. **Security of Fulfillment:** All DSR response packages shall be transmitted using encryption at rest (AES-256) and in transit (TLS 1.2 or higher). Identity verification for high-sensitivity data shall require Level 2 authentication as defined in Section 5.2.
6. **Lawful Basis Recognition:** Meridian processes Personal Data under recognized lawful bases, including consent, contractual necessity, legal obligation, vital interests, public interest, and legitimate interest as defined by Article 6 of the GDPR. The processing activity in question will dictate the permissibility of certain DSRs, particularly erasure and portability.
7. **Fee Prohibition:** Meridian will not charge a fee for the first copy of Personal Data requested in a 12-month period. For additional copies or manifestly unfounded/excessive requests (as determined in Section 8.3), a reasonable fee based on administrative costs may be assessed.

### 4.2 Special Categories of Data and High-Risk AI Systems

Given the classification of the Clinical AI Platform as a high-risk AI system under Annex III of the EU AI Act, the following supplementary policies apply to DSRs involving this system:

- **Explainability:** When a Data Subject exercises their right of access to data processed by the Clinical AI Platform, the response shall include meaningful information about the logic involved in any automated decision-making, including the significance and envisaged consequences. This shall be provided in the form of a plain-language "AI Decision Explanation" appendix, generated in collaboration with the Chief AI Officer's team.
- **Human Oversight Reference:** The response shall affirm the Data Subject's right to obtain human intervention on the part of the Controller, express their point of view, and contest the AI-generated decision, as mandated by Article 14 of the EU AI Act. For Meridian as a Processor, the response will direct the Data Subject to the healthcare provider (Controller) for this intervention.
- **Accuracy and Bias:** Meridian shall not rectify clinical predictions or risk scores unless the input data was factually inaccurate. A clinical score is a computational output; if the Data Subject believes the model is biased, this is handled as an objection under Article 21 (GDPR), not a rectification under Article 16.

### 4.3 Children's Data

For DSR requests involving data subjects under the age of 16 (or the age of digital consent in the relevant Member State), identity verification must confirm the authority of the parent or legal guardian. Requests from minors aged 13-16 regarding their own data will be assessed for the minor's capacity and maturity, in consultation with General Counsel.

---

## 5. Detailed Procedures

This section provides the step-by-step operational workflow for processing a DSR from intake to closure. All steps are tracked in the DSR module of the JIRA Service Management platform, where each request is a unique ticket with the project key "DSR-######."

### 5.1 Intake and Logging

Requests may arrive through one of the following channels:
1.  **Web Portal (Preferred):** The Meridian Data Subject Request Portal, accessible at privacy.meridianhealth.com/dsr.
2.  **Email:** DPO@meridianhealth.com and privacy@meridianhealth.com.
3.  **Physical Mail:** Meridian Health Technologies, Attn: Privacy Office / Data Protection Officer, 100 Federal Street, Boston, MA 02110, USA.
4.  **Customer Support:** Requests raised during a support call with Customer Operations must be transferred immediately to the DSR Triage Team.
5.  **Verbal Requests:** Any employee receiving a verbal DSR request must document it on behalf of the Data Subject in the portal within 2 business hours.

#### Procedure for Intake:
1.  **Acknowledge Receipt:** Within 24 hours of receipt, the DSR Triage Team sends an automated acknowledgment via the same channel (or email if channel is verbal/physical). The acknowledgment includes the assigned DSR-ID.
2.  **Log in JIRA:** The triage analyst creates a DSR ticket with the following required fields:
    - **DSR-ID:** Auto-generated (e.g., DSR-2025-0384)
    - **Date Received:** Timestamp of original receipt
    - **Channel:** [Portal, Email, Mail, Phone, In-Person]
    - **Data Subject Identifier:** Name, email, or user ID provided
    - **Jurisdiction:** [EEA, US-HIPAA, California, Other]
    - **Request Type(s):** [Access, Rectification, Erasure, Restriction, Portability, Objection, Accounting of Disclosures] (Multiple allowed)
    - **Status:** [Awaiting Verification]
    - **Priority:** [Standard, High] (High priority assigned to requests invoking statutory deadlines or involving sensitive data)
3.  **Initial Screening:** The triage analyst performs a keyword search for "lawsuit," "legal action," "supervisory authority," or "regulatory complaint." If found, the ticket is immediately escalated to the General Counsel, and the statutory timeline is strictly prioritized.

### 5.2 Identity Verification

Identity verification is mandatory to prevent unauthorized disclosure of Personal Data. The level of verification must be proportionate to the sensitivity of the data requested and the risk of harm from unauthorized disclosure.

#### 5.2.1 Verification Levels

| Verification Level | Method | Applicable Data Types |
|--------------------|--------|-----------------------|
| **Level 1 (Basic)** | Match of 2 data elements already on file (e.g., name + email, name + date of birth), plus confirmation via a magic link to the known email address. | General account information, marketing preferences, non-sensitive SaaS platform logs. |
| **Level 2 (Enhanced)** | Level 1, plus a government-issued photo ID, verified by a secure third-party KBA service (e.g., LexisNexis InstantID) OR a live video verification call with a DSR analyst. | PHI, financial records, HealthPay loan application data, Clinical AI Platform input data (e.g., lab results, images), employee HR records. |
| **Level 3 (Authorized Representative)** | Level 2 for the Data Subject, plus a notarized Power of Attorney or a signed authorization form compliant with HIPAA 45 CFR § 164.508 for PHI. | Any request made by a person other than the Data Subject (legal guardian, attorney, family member). |

#### Procedure for Verification:
1.  **Assess Required Level:** The DSR Triage Team assigns the Verification Level based on the systems implicated by the request. A request for "all my data" triggers Level 2 verification by default.
2.  **Issue Challenge:** The system sends the verification request to the Data Subject. For Level 2, the email contains a link to the secure ID upload portal powered by the HashiCorp Vault-backed document store.
3.  **Time Limit for Verification:** The Data Subject has 30 calendar days to complete verification. The statutory response timeline (Section 5.8) is paused until verification is complete. If verification is not completed within 30 days, the request is automatically closed, and the Data Subject is notified. The ticket is updated to "Closed – Verification Timeout."
4.  **Verification Review:** A DSR analyst reviews the submitted ID or KBA result. The ID image is checked for tampering; the name is matched against the Data Subject identifier in the request. The ID image is permanently deleted from the portal within 72 hours of verification, retaining only a SHA-256 hash of the document in the JIRA ticket audit log.
5.  **Verification Failure:** If verification fails, the Data Subject is given two additional attempts. After three total failures, the request is escalated to the DPO for a manual review and determination, which may include denial of the request.

### 5.3 Request Interpretation and Clarification

Before launching data discovery, the DSR Triage Team must ensure the request's scope is clearly understood.

1.  **Review Scope:** The analyst determines if the request is specific ("all my payment history in HealthPay from 2023") or broad ("all data you have on me").
2.  **Clarification Interview:** If a broad request could return an unreasonably large volume of data (estimated >10GB or >5,000 pages when printed), the analyst contacts the Data Subject within 5 business days of verification to offer a clarification discussion. The goal is to narrow the scope to relevant systems or timeframes.
3.  **Documentation:** The clarification conversation notes are attached to the JIRA ticket. If the Data Subject insists on a full broad request, a note is added regarding the potential for extended processing time as per Section 5.8.

### 5.4 Data Discovery and Collection

This is the most resource-intensive phase. The DSR Triage Team executes data discovery queries across the Meridian data landscape.

#### 5.4.1 System Discovery Matrix
The following table maps common data categories to the systems to be queried. This matrix is maintained by the VP of Engineering and reviewed for accuracy by each Business Unit Owner quarterly.

| Data Category | System of Record | Query Responsibility | Notes / Complexity |
|---------------|------------------|----------------------|---------------------|
| User Profile & Account | Okta (IAM), Meridian SaaS identity service | VP IT Ops (automated) | Low complexity; API call retrieves profile. |
| Clinical AI Input Data | Snowflake (Clinical Data Warehouse) | DSR Triage Team (SQL query) | High complexity; requires patient ID mapping. Must exclude raw image files (DICOM) exceeding 500MB without specific scope clarification. |
| Clinical AI Algorithm Output | SageMaker Model Registry logs, MLflow | VP of Clinical AI Products (Dr. Aisha Okafor) | High complexity. Output provided as structured JSON with the AI Decision Explanation appendix. |
| HealthPay Transactions | PostgreSQL (Transactions cluster), Apache Kafka (event stream archive) | DSR Triage Team (SQL query) | Medium complexity. Must filter by `user_id` and exclude data that would reveal another individual's financial details. |
| HealthPay Credit Models | Snowflake (Analytical sandbox) | VP of Financial Services (Robert Liu) | High complexity. Raw model features are considered trade secrets; only the input data and final score are provided. Feature importance is provided in the Explainability appendix. |
| MedInsight PHI | Snowflake (PHI vault, encrypted at column level) | DSR Triage Team (SQL query) | High complexity. Requires a dedicated service account with KMS-decrypt permissions, provisioned only for the duration of the DSR fulfillment window. |
| Call Recordings | AWS S3 (Recordings bucket), Genesys Cloud | VP Customer Ops (automated) | Low complexity. Recordings for the given user ID are assembled. |
| Email Logs | Microsoft 365 Compliance Center | CISO (eDiscovery tool) | Low complexity. Requires an eDiscovery case for the specific user. |
| Website Tracking | Segment, Adobe Analytics | VP Engineering | Low complexity. Typically a simple export of the anonymous ID resolved to the known user ID. |

#### 5.4.2 Discovery Procedure:
1.  **Ticket Assignment:** The DSR Triage Team Lead creates sub-tasks in the JIRA ticket for each responsible team based on the scope.
2.  **Service Account Provisioning:** For systems requiring manual querying, the DSR analyst requests a time-limited (24-hour), read-only service account from IT Operations. All actions by this account are logged to a dedicated CloudTrail bucket.
3.  **Query Execution:** The responsible party executes the pre-approved queries documented in the Meridian DSR Playbook (Confluence, restricted access). Ad-hoc queries require DPO approval.
4.  **Data Staging:** All collected raw data is placed in a single, encrypted S3 bucket path (`s3://meridian-dsr-eu-west-1/temp/DSR-######/`) in the jurisdiction's home region. No data crosses regions (EU data stays in eu-west-1; US data stays in us-east-1).

### 5.5 Data Review, Redaction, and Assembly

Once data is collected, it must be reviewed to ensure it does not compromise third-party rights, trade secrets, or system security.

#### 5.5.1 Redaction Rules
The DSR Triage Team applies the following mandatory redactions:
1.  **Third-Party Personal Data:** Any data that would directly identify another individual who is not a joint account holder (e.g., a doctor's notes about a family member, an email address in a CC field). This is replaced with `[Redacted - Third-Party Data]`.
2.  **Internal Confidential Identifiers:** Database row IDs, internal IP addresses, host container names, and cryptographic salts are redacted. Replaced with `[Redacted - Internal System Identifier]`.
3.  **Trade Secrets:** Proprietary algorithm weights, model feature engineering code, and fraud detection thresholds are redacted. Replaced with `[Redacted - Trade Secret / Confidential Business Information]`. This redaction is logged and subject to review by the DPO.
4.  **Legal Privilege:** Communications clearly marked as "Attorney-Client Privileged" or "Attorney Work Product" are withheld in entirety.
5.  **Security Risk Data:** Current password hashes, MFA secret seeds, and full credit card numbers (beyond the last four digits) are redacted. Replaced with `[Redacted - Security Information]`.

#### 5.5.2 Data Portability Package Assembly
For portability requests, data is assembled into a structured format:
- **Container:** A password-protected, AES-256 encrypted ZIP archive.
- **Password:** A complex, unique password for each request, delivered in a separate communication channel (e.g., if the package is emailed, the password is sent via SMS to the verified mobile number).
- **Internal Structure:**
    - `/profile/` : JSON file with user profile attributes.
    - `/clinical/` : Structured JSON and CSV files for lab results, vitals, encounters. DICOM images included if specified.
    - `/financial/` : JSON files for transactions, CSV for loan history.
    - `/activity_logs/` : CSV of significant system access events.
    - `/ai_explanations/` : PDF documents with plain-language explanations of any automated decisions.
    - `/manifest.json` : An index of all files in the package, with schema descriptions.

### 5.6 Approval and Release

The final response package must be approved before release to the Data Subject.

1.  **Peer Review:** All redaction decisions are reviewed by a second DSR Triage Team analyst.
2.  **Data Protection Officer Review:** The DPO reviews and approves any DSR response that involves:
    - Denial of a request in whole or in part.
    - Redaction of data under the "Trade Secret" rule.
    - Requests from former employees or active litigants.
    - Requests from prominent public figures or media representatives.
3.  **Secure Delivery:**
    - The response letter and any generated PDFs are delivered via encrypted email or a secure download link from the portal.
    - The Data Portability Package download link is valid for 7 days. The Data Subject must re-authenticate (Level 1) to download it.
    - No PHI or personal data may be sent as an unencrypted email attachment under any circumstances.

### 5.7 Request Closure and Follow-up

1.  **Confirmation of Receipt:** Seven days after delivery, the system sends an automated follow-up email asking the Data Subject to confirm receipt of the data and whether they have follow-up questions.
2.  **Closure Approval:** If no response is received within 14 days, the ticket is auto-closed. The analyst confirms closure.
3.  **Data Purge from Staging:** Within 14 days of ticket closure, all data in the temporary staging S3 bucket (`s3://meridian-dsr-eu-west-1/temp/DSR-######/`) is permanently deleted. A deletion log is appended to the ticket.

### 5.8 Response Timelines and Service Level Agreements (SLAs)

Meridian aims to process requests efficiently. The following SLAs are established:

| Request Complexity | Description | Target Fulfillment Timeline | Statutory Reference |
|--------------------|-------------|-----------------------------|---------------------|
| **Standard** | Single-system, low-data-volume request. | Within 30 calendar days of verified receipt. | GDPR Art. 12(3), HIPAA 45 CFR § 164.524(b)(2) |
| **Complex** | Multi-system, high-volume, or requiring manual clinical review. | Within 60 calendar days of verified receipt. Requires a notice of extension sent within the first 30 days. | GDPR Art. 12(3) |
| **Accountings of Disclosures** | Historical list required by HIPAA. | Within 60 calendar days of verified receipt. | HIPAA 45 CFR § 164.528(c)(2) |
| **Verification** | Time taken for the Data Subject to prove their identity. | Pauses the SLA clock. Data Subject has 30 days to verify. | N/A |
| **Rectification** | Correcting inaccurate data. | Within 30 calendar days. Extension of 30 days permitted for complex records. | GDPR Art. 16; HIPAA 45 CFR § 164.526 |

#### Extension Notification:
If an extension is required, the Data Subject must be informed within the first 30 days of the verified request, along with the reasons for the delay and their right to lodge a complaint with a supervisory authority.

### 5.9 Specific Procedures by Right

#### 5.9.1 Right to Access (Art. 15 GDPR / 45 CFR § 164.524)
- **Procedure:** A copy of the Personal Data undergoing processing is provided, along with the following metadata: purposes of processing, categories of personal data, recipients or categories of recipient, retention period, rights to rectification/erasure/restriction, right to complain, source of data, and existence of automated decision-making. This is delivered as a "Personal Data Report."
- **Clinical AI Consideration:** The report includes the "AI Decision Explanation" appendix, explaining the logic and impact of any automated clinical risk scoring.

#### 5.9.2 Right to Rectification (Art. 16 GDPR / 45 CFR § 164.526)
- **Procedure:** Upon verification of inaccuracy or incompleteness, the DSR team identifies the authoritative system of record and coordinates an update. Meridian will also notify any third-party recipients to whom the inaccurate data was disclosed, where feasible and not disproportionate.
- **Limitation:** Meridian will not alter clinical opinions or medical diagnoses made by a licensed physician unless demonstrably factual errors (e.g., wrong patient, wrong date) are identified. This is documented as a "statement of disagreement" when the Data Subject disagrees with a clinical finding.

#### 5.9.3 Right to Erasure ("Right to be Forgotten") (Art. 17 GDPR)
- **Procedure:** The Data Subject must be in one of the grounds (e.g., data no longer necessary, consent withdrawn, objection upheld). The DSR team will permanently hard-delete data from the primary system, replication clusters, and online backups. A tombstone record of the DSR-ID, the identity hash, and the date of deletion is kept in a dedicated, immutable ledger for audit purposes.
- **Exception Handling:** Deletion from offline, long-term, immutable backup archives (e.g., AWS S3 Glacier Deep Archive with vault lock) is technically impossible within the SLA timeframe. In such cases, data is placed in a "restricted processing" state: it will not be restored for any operational use and will be permanently expunged at the end of its retention period. This limitation is communicated to the Data Subject in the response.

#### 5.9.4 Right to Restrict Processing (Art. 18 GDPR / 45 CFR § 164.522)
- **Procedure:** The DSR team flags the data record in all active systems as "Restricted." This flag prevents any processing except storage, unless consent is re-obtained, for legal claims, or for the protection of another person's rights.
- **Technical Implementation:** An attribute `processing_state = RESTRICTED` is set at the core identity level in the Meridian SaaS Platform, propagating to Snowflake, PostgreSQL, and operational caches via Kafka.

#### 5.9.5 Right to Data Portability (Art. 20 GDPR)
- **Procedure:** Applicable only when the processing is based on consent or a contract, and the processing is carried out by automated means. The "Data Portability Package" (Section 5.5.2) is provided. Meridian will not translate proprietary clinical formats to a competitor's format but will use established standards (FHIR R4, CSV, JSON) to the extent feasible.

#### 5.9.6 Right to Object (Art. 21 GDPR)
- **Procedure:** The Data Subject can object to processing based on legitimate interests (Article 21(1)) or for direct marketing (Article 21(2)). For direct marketing objections, processing ceases immediately. For legitimate interest objections, the DPO conducts a "balancing test." Processing is suspended pending the outcome of this assessment, which must be completed within 14 business days. The Data Subject is informed of the result and their right to escalate.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

- **Policy Communication:** This SOP is published on the corporate intranet (Atlas) and all employees are required to acknowledge it annually as part of the mandatory Privacy & Security Awareness Training.
- **Segregation of Duties:** No single analyst has the security permissions to both collect raw data from production systems and approve the final DSR response package for release.
- **Background Checks:** All members of the DSR Triage Team undergo enhanced background checks, including a financial history review for any role in handling financial data portability requests.
- **Confidentiality Agreement:** A specific DSR Confidentiality and Non-Disclosure Agreement is signed by all individuals with access to the DSR staging environment, above and beyond the standard employee NDA.

### 6.2 Technical Controls

| Control Category | Description | Implemented Via |
|------------------|-------------|-----------------|
| **Access Control** | Access to DSR data stores is based on the principle of least privilege and time-bound access. | Okta IAM with Just-In-Time access provisioning in HashiCorp Vault. Service accounts automatically expire after 24 hours. |
| **Encryption** | Data used during DSR fulfillment is encrypted at rest and in transit. | AWS KMS with CMK for S3 (AES-256), TLS 1.2 enforced for all API calls and data transfers. |
| **Audit Logging** | All access, querying, and manipulation of data for DSR fulfillment are logged centrally. | AWS CloudTrail, Snowflake Access History, PostgreSQL pgAudit, Datadog Log Management. |
| **Data Loss Prevention** | Prevent unauthorized exfiltration of staging data via email or external drives. | CrowdStrike Falcon DLP module active on all endpoints of DSR Triage Team members. |
| **Network Segmentation** | DSR staging environment is logically isolated from Development and QA environments. | AWS VPC with specific subnet for DSR operations, security groups restrict ingress/egress traffic. |
| **Anonymization for Audit** | Training data and internal audits must use de-identified or synthetic data, never real DSR data. | AWS Lake Formation data filters for training read-only roles. |

### 6.3 Physical Controls
- DSR Triage Team workstations are in a secure, access-controlled area of the Boston HQ with badged entry.
- All records are electronic; physical mail DSRs are digitized within one business day, and the paper originals are securely shredded.

---

## 7. Monitoring, Metrics, and Reporting

The performance and compliance of the DSR program are under continuous monitoring by the DPO and are subject to review by the AI Governance Committee and the Board.

### 7.1 Key Performance Indicators (KPIs)

The following KPIs are tracked in a live Datadog dashboard, drawing data from the JIRA DSR project:

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| **DSR Volume** | N/A (Tracking) | Total number of DSRs by month, by type, and by jurisdiction. |
| **Timeliness SLA Adherence** | >95% of requests fulfilled within statutory or extended timeline. | `(Requests completed on time / Total completed requests) * 100` |
| **Verification Drop-off Rate** | <20% | `(Requests abandoned during verification / Total requests received) * 100` |
| **Mean Time to Fulfillment (MTTF)** | <21 calendar days for Standard, <45 for Complex | Average calendar days from verification to response delivery. |
| **Overturn Rate** | <2% | Requests where Meridian's denial or redaction was successfully challenged and overturned by a supervisory authority or court. |
| **Customer Satisfaction (CSAT)** | >4.0/5.0 | Post-fulfillment survey sent with the 7-day confirmation email. |

### 7.2 Reporting Cadence

| Report Type | Audience | Frequency | Content |
|-------------|----------|-----------|---------|
| **Operational DSR Dashboard** | DSR Triage Team, VP Engineering, VP Customer Ops | Real-time | Live counts, aged tickets, bottleneck alerts. |
| **Monthly Privacy Metrics** | CPO/DPO | Monthly | KPI performance, trends, notable request highlights, resource utilization. |
| **Quarterly DSR Governance Report** | AI Governance Committee, C-Suite | Quarterly | Compliance trends, emerging regulatory risks, adequacy of controls, tooling roadmap updates. |
| **Annual Board Report** | Board of Directors | Annually | Program maturity, benchmark against industry peers, budget review, material risks identified. |

---

## 8. Exception Handling and Escalation

### 8.1 General Escalation Path

1.  **Level 1 - DSR Triage Team Lead:** Operational issues (e.g., system unavailability, data source mapping ambiguity, minor technical hurdles).
2.  **Level 2 - Data Protection Officer (Dr. Klaus Weber):** Unclear scope, potential refusal of repetitive requests, complex redaction involving trade secrets, disputes with Business Associates.
3.  **Level 3 - General Counsel (Maria Gonzalez):** Any denial of a request, involvement of litigation, requests from regulatory bodies (e.g., an EU Supervisory Authority directly), or law enforcement.

### 8.2 Exception Requests for Denial or Extension

Any plan to deny a DSR request (in whole or part) or to extend the timeline beyond the initial 30+30 day period requires the following:
1.  **Formal Documentation:** The DPO drafts a memo explaining the legal and factual basis for the exception, citing the specific regulatory article. This is stored in the JIRA ticket.
2.  **Legal Review and Approval:** The General Counsel reviews and signs off, digitally.
3.  **Notification to Data Subject:** A formal denial letter is sent, clearly stating the reasons, the Data Subject's right to complain to a supervisory authority, and the right to seek a judicial remedy. The letter is tracked, and a read receipt is requested.

### 8.3 Manifestly Unfounded or Excessive Requests
To classify a request under this exemption, the following cumulative criteria must be met:
- The request is repetitive (more than two identical requests in a 12-month period).
- The request is clearly malicious, vexatious, or solely intended to disrupt operations.
- Evidence of the above points must be documented and approved by both the DPO and General Counsel.
If approved, Meridian may charge a reasonable fee based on administrative costs or refuse to act on the request. This decision must be justified in writing to the Data Subject.

### 8.4 Data Breach During DSR Fulfillment
If a security incident occurs during the DSR process (e.g., mis-delivery of a Data Portability Package, unauthorized access to the staging S3 bucket):
1.  Immediately pause all DSR processing for the affected request.
2.  Declare a security incident per SOP-IS-015 (Security Incident Response Protocol).
3.  The CISO and DPO will jointly assess whether the incident constitutes a notifiable personal data breach under GDPR Article 34 or HIPAA § 164.404. If so, the DPO is responsible for notification to supervisory authorities and affected data subjects, with the notification documenting the DSR-ID as the source of the breach.

---

## 9. Training Requirements

All personnel involved in the DSR lifecycle must be trained in the specific procedures and sensitivities of handling Data Subject Rights.

### 9.1 Role-Based Training Matrix

| Role | Training Module | Frequency | Method | Record Keeping |
|------|-----------------|-----------|--------|----------------|
| All Meridian Employees | Data Privacy Essentials & DSR Recognition (DGP-101) | Annually | LMS (Workday Learning) | Completion tracked in Workday, flagged in annual compliance audit. |
| DSR Triage Team (Privacy Analysts) | Advanced DSR Management & Fulfillment (DGP-201) | On hire, then Semi-Annually | Instructor-led training by DPO & GC in Boston; practical exercise with a synthetic dataset. | 90% or higher score on post-course exam required. |
| DSR Triage Team | DSR Clinical & Financial Data Handling (DGP-202) | Annually | Instructor-led, includes a review of updated data models for Clinical AI and HealthPay. | Sign-off by DPO and BU Owner. |
| Engineering and IT Operations | Secure DSR Data Staging and Disposal (DGP-203) | On role assignment, then Annually | Technical workshop with the CISO's security engineers. | Hands-on lab completion recorded in Jira Training project. |
| Customer Operations | Frontline DSR Intake (DGP-204) | Quarterly refresh | Micro-learning video and 5-question quiz in LMS. | Completion tracked in Workday. |
| General Counsel, Privacy Team | DSR Legal Update & Regulatory Trends (DGP-205) | As needed (minimum annually) | Presentation by external counsel or regulatory invitee. | Attendance sheet and summary notes filed. |

### 9.2 Training Effectiveness
The effectiveness of training is measured by:
- A reduction in Level 1 intake errors (e.g., missed DSR requests in Customer Ops calls).
- Post-training exam scores.
- Analysis of exceptions and errors during the DSR fulfillment process, fed back into the annual training update.

---

## 10. Related Policies and References

This SOP is an integral component of the Meridian Health Technologies Data Governance and Privacy Framework. It must be read in conjunction with the following internal documents and external standards.

### 10.1 Internal Meridian Policies

| SOP ID | Document Title | Relationship to This SOP |
|--------|----------------|--------------------------|
| SOP-DGP-001 | Data Governance Charter | Foundational governance principles for all data processing. |
| SOP-DGP-003 | Record of Processing Activities (ROPA) Management | The ROPA is the authoritative source for data discovery in Section 5.4. |
| SOP-DGP-005 | Privacy Impact Assessment (PIA) Process | DSRs for high-risk AI systems may trigger a supplementary PIA. |
| SOP-IS-015 | Security Incident Response Protocol | Governs the response to data breaches during DSR fulfillment (Section 8.4). |
| SOP-IS-045 | Data Access Control and Authorization | Governs the provisioning of the service accounts in Section 5.4.2. |
| SOP-LEG-012 | Law Enforcement Data Request Handling | Governs separate, non-DSR requests for data from government/law enforcement. |
| SOP-RMS-009 | Model Risk Management Policy (SR 11-7) | Governs the management of credit and fraud models in HealthPay, including their explainability outputs for DSRs. |
| SOP-VRM-001 | Vendor Risk and Third-Party Due Diligence | Governs the oversight of third-party services used in DSR fulfillment (e.g., KBA provider). |
| Pol-HR-015 | Employee Privacy Notice | Policy governing employee data processed by HR, subject to employee DSRs. |

### 10.2 External Standards and Regulations

- **REG (EU) 2016/679:** General Data Protection Regulation (GDPR)
- **REG (EU) 2024/1689:** European Union Artificial Intelligence Act (EU AI Act)
- **45 CFR Part 160 and 164:** HIPAA Privacy and Security Rules
- **NIST Special Publication 800-53 Rev. 5:** Security and Privacy Controls for Information Systems and Organizations
- **NIST AI RMF 1.0:** Artificial Intelligence Risk Management Framework
- **ISO 27001:2022 & ISO 27701:2019:** Information Security and Privacy Information Management Systems
- **SOC 2 Trust Services Criteria (Security, Confidentiality, Privacy):** 2022 edition

---

## 11. Revision History

| Version | Date | Author | Change Description | Approvals |
|---------|------|--------|-------------------|-----------|
| 1.0 | 2020-11-15 | J. Walsh (former CPO) | Initial creation. Established foundational DSR workflow for GDPR and CCPA compliance. | J. Walsh, M. Gonzalez |
| 2.0 | 2022-01-20 | K. Weber | Major revision. Incorporated HIPAA accounting of disclosures, added JIRA-based ticketing procedure, and defined the KBA process for identity verification. | K. Weber, M. Gonzalez |
| 2.5 | 2023-04-10 | K. Weber | Updated scope to include HealthPay data, defined the "Data Portability Package" format (JSON/CSV), and added the initial redaction rules for third-party data. | K. Weber, M. Gonzalez, R. Liu |
| 3.0 | 2023-11-01 | K. Weber | Full integration of EU AI Act requirements. Added "AI Decision Explanation" appendix protocol, Clinical AI redaction rules, and defined the role of the Chief AI Officer in DSR fulfillment. Added new Section 7 on KPIs. | K. Weber, M. Gonzalez, M. Rivera |
| 3.4 | 2024-04-17 | K. Weber | Annual review. Updated identity verification to mandate video verification option, refined SLAs for complex requests, and added new data discovery sources (e.g., Kafka archives). | K. Weber, M. Gonzalez |
| 3.5 | 2024-06-22 | K. Weber | Incorporated post-FDA clearance and CE marking operational changes for Clinical AI. Tightened physical control requirements. Clarified the procedure for handling objections to legitimate interests. This version is effective as of the date above. | K. Weber, M. Gonzalez, R. Kim |

**End of Document - SOP-DGP-007 v3.5**