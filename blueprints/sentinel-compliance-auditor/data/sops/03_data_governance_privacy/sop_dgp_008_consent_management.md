---
sop_id: "SOP-DGP-008"
title: "Consent Management"
business_unit: "Data Governance & Privacy"
version: "3.0"
effective_date: "2024-12-06"
last_reviewed: "2025-03-18"
next_review: "2025-09-23"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Consent Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the collection, management, granularity, storage, and withdrawal of consent across Meridian Health Technologies' products and platforms. The purpose is to ensure that consent is obtained lawfully, recorded accurately, maintained with integrity, and honored promptly across all business lines, while enabling Meridian to demonstrate compliance with applicable privacy and data protection obligations.

### 1.2 Scope

This SOP applies to the following:

| Scope Area | Description |
|------------|-------------|
| **Organizational Entities** | All business units, including HealthPay Financial Services, MedInsight Analytics, and Clinical AI Systems, plus all corporate functions. |
| **Geographic Jurisdictions** | Global operations, with specific procedures for jurisdictions where consent is a legal basis for processing. |
| **Data Subjects** | Patients, health plan members, clinical trial participants, website visitors, loan applicants, and any living individual whose personal data is processed by Meridian. |
| **Processing Activities** | Any processing of personal data where consent serves as the lawful basis, including but not limited to: marketing communications, non-essential cookies and trackers, secondary use of health data for research, credit assessments, and biometric processing where applicable. |
| **Systems and Platforms** | All Meridian-owned and operated systems that collect or manage consent, including the Meridian Patient Portal, HealthPay Online Lending Platform, MedInsight Research Registry, and all public-facing websites and mobile applications. |

### 1.3 Out of Scope

The following activities are explicitly excluded from this SOP:
- Processing where consent is not the lawful basis (e.g., processing necessary for the performance of a contract, legitimate interests where properly assessed, or legal obligations).
- Employee data processing governed by employment agreements (refer to SOP-HR-014, Employee Data Processing).
- De-identified or aggregated data that cannot be re-associated with an individual.

### 1.4 Applicability to Business Associates

Any third-party vendor, contractor, or Business Associate (as defined under applicable law) that collects or manages consent on behalf of Meridian must adhere to the requirements of this SOP. Compliance with this SOP shall be contractually mandated through a Business Associate Agreement (BAA) or equivalent data processing agreement. Meridian business units engaging such third parties are responsible for ensuring the existence of an executed BAA prior to any data exchange.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|------|------------|
| **Consent** | Any freely given, specific, informed, and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her. |
| **Explicit Consent** | A heightened form of consent required for processing special categories of personal data. Explicit consent requires an express statement of consent, not merely an affirmative action. |
| **Granular Consent** | The practice of seeking separate consent for distinct processing operations, such that data subjects are able to consent to specific purposes without being forced to agree to a bundle. |
| **Consent Record** | An immutable, timestamped, and retrievable digital artifact documenting the consent event, including the data subject's identity, the specific purpose consented to, the consent text presented, and the affirmative action taken. |
| **Withdrawal of Consent** | The data subject's subsequent revocation of previously granted consent. Withdrawal must be as easy as giving consent and shall take effect prospectively. |
| **Re-consent** | The process of obtaining fresh consent when the purpose, scope, or legal conditions of the original processing materially change. |
| **Consent Repository** | The centralized, encrypted database maintained by the Data Governance & Privacy (DGP) unit, designated as the system of record for all consent events across Meridian. |
| **Data Subject** | An identified or identifiable natural person to whom personal data relates. |
| **Personal Data** | Any information relating to an identified or identifiable natural person. |
| **Special Categories of Personal Data** | Personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data processed for the purpose of uniquely identifying a natural person, data concerning health, or data concerning a natural person's sex life or sexual orientation. |
| **Business Associate (BA)** | A person or entity, other than a member of Meridian's workforce, that performs functions or activities on behalf of, or provides services to, Meridian involving the use or disclosure of Protected Health Information. |
| **Protected Health Information (PHI)** | Individually identifiable health information that is transmitted or maintained by electronic media or any other form or medium. |

### 2.2 Acronyms

| Acronym | Meaning |
|---------|---------|
| BA | Business Associate |
| BAA | Business Associate Agreement |
| CMP | Consent Management Platform |
| DGP | Data Governance & Privacy |
| DPO | Data Protection Officer |
| PHI | Protected Health Information |
| PII | Personally Identifiable Information |
| PoAM | Plan of Action and Milestones |
| RACI | Responsible, Accountable, Consulted, Informed |
| SLA | Service Level Agreement |
| CRS | Consent Record System |
| IAM | Identity and Access Management |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| Activity | DPO (Dr. Klaus Weber) | DGP Unit | Business Unit Owner | IT Engineering | General Counsel (Maria Gonzalez) | Compliance Officer |
|----------|:--:|:--:|:--:|:--:|:--:|:--:|
| **Consent Policy Definition** | A | R | C | C | C | I |
| **Consent Collection Implementation** | I | R | A | R | I | C |
| **Consent Record Maintenance** | I | A | I | R | I | C |
| **Consent Withdrawal Execution** | I | R | A | R | I | C |
| **Re-consent Campaigns** | C | R | A | R | C | I |
| **Audit Control Monitoring** | A | R | I | I | C | I |
| **Exception Approval** | R | C | C | I | A | C |

**Legend:** R = Responsible (does the work), A = Accountable (approves, signs off), C = Consulted (input before action), I = Informed (notified after action)

### 3.2 Role Descriptions

**Dr. Klaus Weber, Chief Privacy Officer / Data Protection Officer (DPO)**
- Serves as the ultimate accountable executive for the Consent Management program.
- Approves all exceptions to this SOP that involve high-risk processing or special categories of data.
- Reports consent compliance metrics to the Executive Risk Committee quarterly.
- Oversees the centralized Consent Record System (CRS).

**Data Governance & Privacy (DGP) Unit**
- Responsible for the day-to-day operation, maintenance, and integrity of the Consent Repository.
- Designs consent collection user interfaces (UIs) and user experiences (UX) in consultation with legal counsel.
- Executes all re-consent campaigns and manages communication templates.
- Monitors consent metrics and prepares monthly compliance dashboards.

**Business Unit Owner (e.g., VP of HealthPay, VP of MedInsight)**
- Accountable for ensuring that all customer-facing products within their unit implement consent mechanisms compliant with this SOP.
- Responsible for funding any product-level engineering changes required for compliance.
- Must consult the DGP unit before launching any new processing activity requiring consent.

**IT Engineering (Platform & Security)**
- Responsible for implementing the technical consent controls in all Meridian platforms, including the CMP.
- Ensures audit logs capturing consent events are generated and stored securely.
- Engineers the withdrawal mechanisms ensuring they take effect within the mandated SLA.

**Maria Gonzalez, General Counsel**
- Approves the final wording of all consent communications to ensure enforceability.
- Approves any exceptions involving regulatory interpretation.
- Reviews and approves this SOP on each revision cycle.

**Compliance Officer**
- Informed of all consent-related audit findings and metric reports.
- Performs independent spot-checks on consent records for quality assurance.

---

## 4. Policy Statements

The following constitute the high-level policy commitments of Meridian Health Technologies regarding consent management.

**PS-01: Lawful Basis Primacy**
Where consent is selected as the lawful basis for processing personal data, Meridian shall ensure that such consent meets the standards defined in this SOP. Consent shall not be the default basis when another legitimate lawful basis is more appropriate.

**PS-02: Freely Given Consent**
Meridian shall not condition the performance of a contract, provision of a service, or determination of creditworthiness on the provision of consent unless that consent is demonstrably necessary for the specific service. Any appearance of bundling consent with service terms shall be avoided.

**PS-03: Specific, Informed, and Unambiguous Consent**
Requests for consent shall be presented in a manner clearly distinguishable from other matters, using clear and plain language. The data subject shall be informed of the identity of the data controller (Meridian Health Technologies, or the specific legal entity), the purpose of each processing operation for which consent is sought, the types of data to be processed, and the existence of the right to withdraw consent.

**PS-04: Granularity by Default**
Where a processing operation serves multiple purposes, consent shall be sought for each distinct purpose. Data subjects shall be provided the option to consent to specific processing purposes without being forced to grant a blanket, undifferentiated consent. Pre-checked boxes or opt-out mechanisms shall not constitute valid consent.

**PS-05: Demonstrability and Record-Keeping**
Meridian shall maintain comprehensive, immutable consent records for every consent event across all platforms. Each consent record must be retrievable by data subject identifier and by time period. Consent records shall be retained for no less than seven (7) years from the date of the last processing action based on that consent, or for whatever longer period is legally required.

**PS-06: Right to Withdraw**
Data subjects shall have the right to withdraw their consent at any time. The withdrawal mechanism shall be as easy and accessible as the original consent mechanism. Withdrawal shall not affect the lawfulness of processing carried out prior to the withdrawal event. Upon receipt of a valid withdrawal request, Meridian shall cease the relevant processing within a 30-day SLA, and within 72 hours for direct marketing communications.

**PS-07: Re-consent Triggers**
Meridian shall initiate a re-consent campaign when:
- The purpose of the processing changes materially from the original purpose for which consent was granted.
- A new category of personal data is introduced to the processing activity.
- Data is to be used for a new, incompatible purpose.
- The data subject is a minor who reaches the age of majority, where original consent was granted by a parent/legal guardian.
- Changes in applicable law render the original consent no longer sufficient.

**PS-08: Consent for Special Category Data**
Any processing of special categories of personal data based on consent shall require Explicit Consent. The consent mechanism shall incorporate an additional confirmation step beyond standard consent, requiring a clear declaratory statement of explicit agreement from the data subject.

**PS-09: Audit Controls**
Meridian shall implement hardware, software, and procedural mechanisms that record and examine activity in information systems that process or contain personal data subject to consent. These audit controls shall be maintained to support the demonstrability of consent.

---

## 5. Detailed Procedures

### 5.1 Consent Collection at Point of Interaction

This procedure governs the collection of consent via digital interfaces (web, mobile app, clinical kiosk) at the first point of data collection.

#### 5.1.1 UI/UX Requirements for Digital Consent

Before deploying any consent collection mechanism, the Product Owner, in consultation with the DGP Unit, shall verify the following design requirements:

1.  **Separation from Terms of Service (ToS):**
    - Consent request elements shall be visually and structurally separated from ToS acceptance.
    - A single “I Agree to Terms and Accept” button covering both ToS and all consent purposes is strictly prohibited.

2.  **Unbundled Consent Options:**
    - Each distinct processing purpose shall be presented with its own opt-in toggle, checkbox, or equivalent affirmative action element.
    - Purposes shall not be pre-checked.

3.  **Clear Language for Each Purpose:**
    - *Example for HealthPay (Loan Application):*
        - ☐ **Credit Report Analysis:** I consent to Meridian HealthPay pulling and analyzing my consumer credit report for the purpose of assessing my loan eligibility.
        - ☐ **Marketing Communication:** I consent to receive promotional emails and offers for Meridian HealthPay products.
    - *Example for MedInsight (Research Registry):*
        - ☐ **Observational Research:** I consent to my de-identified health data being used in population health observational studies.
        - ☐ **Interventional Trial Contact:** I consent to be contacted by a MedInsight coordinator if a clinical trial matches my profile.
    - *Example for Patient Portal (Clinical AI Triage):*
        - ☐ **AI-Assisted Triage:** I consent to my reported symptoms being processed by the Meridian Clinical AI engine to suggest preliminary triage recommendations.

4.  **Explicit Consent Interface:**
    - For special category data, the interface shall require a two-step confirmation.
    - *Step 1:* Checkbox: “I explicitly consent to Meridian processing my genetic data [insert specific purpose here].”
    - *Step 2:* A confirmation dialog box: “You have indicated you wish to provide explicit consent for processing your genetic data for the purpose of [X]. This is an additional confirmation step. Click ‘Confirm Explicit Consent’ to proceed.”

5.  **Granular Withdrawal Access:**
    - On the same interface where consent is collected, display a link to the Consent Management Dashboard (see 5.3.1) where users can subsequently view, modify, or withdraw their preferences.

#### 5.1.2 Consent Collection Workflow (Digital)

| Step | Action | Responsible | System |
|------|--------|-------------|--------|
| 1 | Data subject accesses Meridian service requiring consent (e.g., creates HealthPay account, joins MedInsight registry). | N/A (Data Subject) | HealthPay Portal / MedInsight Portal |
| 2 | Service presents the Consent Interface as specified in 5.1.1. The interface dynamically loads the consent purposes relevant to the service context from the DGP-approved purpose catalog. | Product Owner (Implementation), DGP (Catalog) | Consent Management Platform (CMP) API |
| 3 | Data subject toggles consent options and clicks “Submit Preferences.” | N/A (Data Subject) | Frontend -> CMP API endpoint `/v1/consent/record` |
| 4 | The CMP API generates a consent event record. See schema in 5.1.3. | IT Engineering (Automated) | Consent Record System (CRS) DB |
| 5 | The CRS DB writes the event immutably and returns a `consent_receipt_id`. | IT Engineering (Automated) | CRS DB |
| 6 | The receiving frontline system (e.g., HealthPay Core) stores the `consent_receipt_id` as a reference in the data subject's profile. The frontline system shall only process data for purposes where a valid, active consent record exists. | Application Backend | HealthPay DB / MedInsight DB |
| 7 | The system sends an automated confirmation email or in-app message summarizing the granted consents, including instructions on how to withdraw. | IT Engineering (Automated) | SendGrid / In-App Messaging |

#### 5.1.3 Consent Record Schema

Each consent event record captured in the CRS must contain the following minimum elements:

| Field | Description | Required |
|-------|-------------|----------|
| `consent_receipt_id` | Universally Unique Identifier (UUIDv4) for the specific consent event. | Y |
| `data_subject_id` | Unique Meridian Customer ID linking to the data subject master record. | Y |
| `consent_purpose_id` | Unique identifier referencing the DGP purpose catalog (e.g., `PUR-023`, `PUR-089`). | Y |
| `consent_purpose_description` | The full text presented to the data subject for this purpose at the time of consent. | Y |
| `affirmative_action_type` | Enum: `TOGGLE_ON`, `CHECKBOX_CHECKED`, `EXPLICIT_DIALOG_CONFIRMED`, `SIGNATURE_CAPTURED`. | Y |
| `consent_status` | `GRANTED`, `WITHDRAWN`, or `EXPIRED`. Note: Withdrawals generate a separate event record, but status is updated on the active record. | Y |
| `consent_version` | DGP-managed version of the consent text presented (e.g., `v2.1`). | Y |
| `interface_origin` | Source system where consent was collected (e.g., `MHP-PORTAL`, `MEDINSIGHT-IOS`). | Y |
| `ip_address` | IP address of the data subject at consent time. | Y |
| `timestamp_utc` | ISO 8601 timestamp of the consent event. | Y |
| `expiry_timestamp_utc` | Null if perpetual until withdrawal. Populated for consents with a defined lifespan. | N |
| `parental_consent_flag` | Boolean indicating if the consent was collected from a legal guardian for a minor. | Y |

### 5.2 Consent Collection for Non-Digital Interactions

In limited cases, consent may be collected via paper forms, telephonic interviews, or in-person clinical encounters.

#### 5.2.1 Paper Consent Forms

1.  **Form Design:** The DGP Unit shall maintain and approve the only authorized paper consent form template. Business units must request a customized form from DGP, which pre-populates the specific purposes from the purpose catalog.
2.  **Collection:** The data subject must physically initial next to each specific consent purpose they agree to, and sign and date the form’s consent declaration section. Blanket signatures without initials are invalid per this SOP.
3.  **Digitization:** The paper form must be scanned and ingested into the CRS via the `POST /v1/consent/paper` API endpoint, which triggers a manual review queue. The responsible staff member (Clinical Coordinator, Research Assistant) must upload the scan and manually key the consent purposes into the DGP validation dashboard.
4.  **Validation:** A DGP Unit member validates the manual entry against the scanned initialed form within three (3) business days. Upon validation, the records are committed immutably.
5.  **Retention:** The original paper form must be stored in a secure, locked filing cabinet in a facility with access logging. The paper form is retained for a minimum of one year following digitization, after which it may be securely shredded in accordance with SOP-OPS-002 (Secure Disposal).

### 5.3 Consent Withdrawal

This procedure governs the process when a data subject withdraws consent for one or more processing purposes.

#### 5.3.1 Self-Service Withdrawal (Consent Management Dashboard)

1.  **Access:** Data subjects can access the Consent Management Dashboard by:
    - Authenticating via the Meridian Account portal (`account.meridianhealth.com/consent`) using standard IAM credentials.
    - Clicking “My Consent Preferences” in any authenticated Meridian service or app.
    - Clicking the “Unsubscribe / Manage Preferences” link in the footer of any marketing email (applicable for Marketing consent only).
2.  **Interface:** The dashboard displays all active and inactive consents grouped by service/product line. Each consent is presented with a toggle set to `ON`.
3.  **Withdrawal Action:** The data subject toggles any `ON` toggle to `OFF` and clicks “Update My Preferences.”
4.  **Backend Processing:**
    - The CMP API receives the withdrawal call.
    - For the specific purpose, the CRS DB creates a new event record with `consent_status: WITHDRAWN`. The original record's status is also updated.
    - The CMP publishes a `CONSENT_WITHDRAWN` event to the enterprise message bus (Kafka topic: `privacy.consent.events`).
5.  **Downstream Action (Processing Cessation):**
    - **Direct Marketing (SLA: 72 Hours):** The Marketing Cloud subscriber (Braze) subscribes to `privacy.consent.events`. Upon receiving a `WITHDRAWN` event for purpose `PUR-023` (Marketing), the data subject's profile in Braze is updated to supress all marketing sends. This is executed within 72 hours.
    - **Research/Secondary Use (SLA: 30 Days):** The MedInsight Data Lake ingestion service receives the event. It must cease ingesting new data for this purpose for the subject and flag existing data for archival review within 30 days. Active processing for research cohorts must exclude this data subject at the next cohort refresh.
    - **HealthPay Processing (SLA: 30 Days):** If consent for credit analysis is withdrawn but a loan account remains active, the withdrawal applies prospectively. No further credit pulls or analyses based on consent may occur.

#### 5.3.2 Assisted Withdrawal (Customer Support)

1.  A data subject contacts the Meridian Support Center (phone, email, chat) requesting withdrawal.
2.  The Support Agent (Tier 1) verifies the data subject's identity following the IAM verification procedure (knowledge-based authentication: full name, date of birth, last four digits of SSN/NHI number).
3.  Upon verification, the Support Agent uses the “Privacy Request – Consent Withdrawal” form template in Zendesk. The agent specifies the exact purpose(s) to be withdrawn as directed by the data subject.
4.  Zendesk triggers an API call to the CMP on behalf of the verified subject, creating the withdrawal record.
5.  The DGP Unit receives a notification of the assisted withdrawal and reviews within 48 hours to confirm correct execution.

### 5.4 Consent Records Maintenance and Access

The CRS is the system of record. All consent and withdrawal events are stored immutably.

- **Immutability:** CRS records are write-once. Updates to `consent_status` are technically new records that supersede the prior status. No record of a consent event can be deleted.
- **Access Control:** Direct database read access is restricted to the DGP Unit. All other system queries must occur via the CMP API with role-based access.
- **Retrieval for Compliance:** An authorized DGP officer can query all consent records for a given `data_subject_id` to reconstruct a timeline of consents and withdrawals. This must be used to respond to regulatory inquiries.

### 5.5 Re-Consent Procedure

When a re-consent trigger is identified (per PS-07), the DGP Unit executes a re-consent campaign.

#### 5.5.1 Trigger Identification and Validation

1.  A Business Unit Owner identifies a material change or a DGP review flags a change in law.
2.  The DGP Unit reviews the existing consent purpose text and determines that it is no longer sufficient, formally documenting the re-consent trigger in a “Re-Consent Determination Memo.”
3.  Maria Gonzalez, General Counsel, reviews and approves the memo.

#### 5.5.2 Campaign Execution Workflow

| Step | Action | Responsible | Timeline |
|------|--------|-------------|----------|
| 1 | DGP defines the target cohort: a query in the CRS for all data subjects with `consent_purpose_id = X` AND `consent_status = GRANTED`. | DGP Analyst | Day 0-2 |
| 2 | DGP drafts the re-consent communication (email template, in-app message, and paper letter if required). The communication must clearly explain the material change and present the new consent language. | DGP, General Counsel (review) | Day 2-5 |
| 3 | Campaign is executed via the approved customer communication channel. | DGP, Marketing Operations | Day 5 |
| 4 | Data subjects are given a 45-day window to provide new consent. Reminder notices are sent at Day 15 and Day 35. | Automated via CMP | Day 15, Day 35 |
| 5 | At the end of the 45-day window, the DGP generates a report showing: (a) subjects who re-consented, (b) subjects who explicitly denied, (c) non-responders. | DGP Analyst | Day 46 |
| 6 | For non-responders and denials, the DGP updates the consent status to `EXPIRED` in the CRS. The relevant processing ceases per the cessation SLA (5.3.1, step 5). | DGP Analyst, Engineering | Day 46-50 |
| 7 | A final re-consent outcome report is archived with the Re-Consent Determination Memo. | DGP | Day 51 |

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

- **Data Protection by Design:** Any new product, service, or processing activity that will rely on consent must undergo a Privacy Threshold Assessment (PTA) managed by the DGP Unit. The PTA will determine if a more detailed assessment is required and will specify consent requirements.
- **BAA Requirement:** For any processing activity involving PHI managed by a third party that requires consent, a BAA must be executed before data is shared. The BAA will incorporate the consent requirements defined herein.
- **Segregation of Duties:** The personnel responsible for designing consent interfaces (DGP) are separate from the personnel implementing them (Engineering) and the personnel auditing them (Compliance). No single individual can both manage consent records and audit them.

### 6.2 Technical Controls

| Control | Implementation | Description |
|---------|----------------|-------------|
| **Audit Controls** | Implemented via the CRS and application-level logging. | All consent actions (grant, withdraw, update) generate an immutable log entry with timestamp, user ID, action, and success/failure status. |
| **Encryption** | AES-256 at rest, TLS 1.3 in transit. | All consent records in the CRS database are encrypted at rest. API communication mandatorily uses TLS 1.3. |
| **Data Integrity** | Hash-chain within the CRS. | Each new consent record includes a cryptographic hash of the previous record for the same data subject, ensuring an unbreakable audit trail. |
| **Access Control** | Meridian IAM (Okta) integrated with RBAC. | Only authorized DGP members have read/write access to the CRS. Support agents have a proxy write capability for withdrawals via the trusted Zendesk integration. |
| **Intrusion Detection** | Meridian SOC standard IDS/IPS. | All traffic to the CMP API is monitored for anomalies. Any mass consent withdrawal event triggers an immediate P1 alert to the SOC and DPO. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The DGP Unit tracks and reports the following metrics monthly:

| KPI | Definition | Target | Escalation Threshold |
|-----|------------|--------|----------------------|
| **Consent Capture Rate** | % of new accounts that successfully have a consent record created vs. total new accounts needing consent. | > 99.5% | < 99% |
| **Withdrawal Timeliness – Marketing** | % of marketing consent withdrawals processed within the 72-hour SLA. | 100% | < 100% (Zero Tolerance) |
| **Withdrawal Timeliness – General** | % of all other processing withdrawals effected within the 30-day SLA. | > 95% | < 90% |
| **Re-consent Completion Rate** | % of targeted data subjects in a re-consent campaign who actively respond (grant or deny). | > 60% | < 40% |
| **Consent Record Integrity** | Automated weekly check: % of records with all required schema fields populated and valid. | 100% | < 99.9% |
| **Data Subject Dashboard Access** | % uptime of the self-service Consent Management Dashboard. | 99.9% | < 99.5% |

### 7.2 Reporting Cadence

| Report | Recipient | Frequency |
|--------|-----------|-----------|
| **Consent Operations Dashboard** | DGP Unit, Chief Privacy Officer | Real-time (Grafana dashboard) |
| **Consent Compliance Summary** | Chief Privacy Officer, Compliance Officer, General Counsel | Monthly |
| **KPI Compliance Pack** | Executive Risk Committee | Quarterly |
| **Re-consent Campaign Outcome Report** | Relevant Business Unit Owner, DPO, General Counsel | Per campaign (within 10 business days of completion) |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

Exceptions to this SOP are categorized as:

- **Technical Exception:** A system bug prevents consent from being properly recorded or honored. (e.g., CMP API outage, CRS write failure).
- **Process Exception:** A required process step cannot be completed due to an operational impediment (e.g., paper form digitization backlog exceeds 5 business days).
- **Policy Exception:** A business need arises to deviate from a policy statement (e.g., a request to bundle consent purposes for a specific, time-limited campaign, which is otherwise prohibited by PS-04).

### 8.2 Exception Request Process

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Requestor documents the exception using the “Consent Management Exception Request” form on the DGP SharePoint portal. The form requires: the policy statement being excepted, the specific system or data affected, the business justification, compensating controls proposed, and the requested duration of the exception. | Requestor (usually Business Unit Owner or VP of Engineering) |
| 2 | DGP Unit performs an initial impact assessment, evaluating privacy risk and compliance impact. | DGP Analyst |
| 3 | DGP Unit Lead, Dr. Klaus Weber, reviews the assessment. For Technical and Process Exceptions with a duration < 30 days, the DPO can approve directly. | Chief Privacy Officer / DPO |
| 4 | For all Policy Exceptions, or any exception with a duration > 30 days, the request and DPO recommendation are forwarded to Maria Gonzalez, General Counsel, for final approval. | General Counsel |
| 5 | If approved, the exception is logged in the “SOP Exception Register” with a unique exception ID, expiration date, and required review milestones. | DGP Unit |
| 6 | Upon expiration, the requestor must either certify compliance restoration or submit a renewal request, which follows the full process again. | Requestor |

### 8.3 Emergency Process

For a P1 incident where consent is being systematically violated (e.g., a faulty withdrawal implementation means marketing sends continue despite opt-out), the Chief Privacy Officer has the authority to order an emergency halt to the offending processing activity verbally, confirmed in writing within 4 hours. The full exception documentation process is completed retroactively.

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Role | Course | Frequency | Verification |
|------|--------|-----------|--------------|
| **All Employees** | Privacy Awareness 101 | Annually | Completion recorded in Workday LMS. <95% completion rate triggers escalation to CHRO. |
| **DGP Unit** | Advanced Consent Management (DGP-201) | Bi-annually | Score > 80% on post-training assessment. |
| **Product Owners & Managers** | Privacy by Design & Consent UX (DGP-202) | Annually | Completion recorded in Workday LMS. |
| **Software Engineers (Frontend & Backend)** | Implementing Consent Controls (ENG-305) | Annually | Completion recorded in Workday LMS; engineering managers verify via code review checklists. |
| **Customer Support (Tier 1-3)** | Handling Privacy Requests (SUP-410) | Quarterly | Simulated call/chat exercises with QA score > 85%. |

### 9.2 Training Content Requirements

**Course: Advanced Consent Management (DGP-201)**
- Detailed walkthrough of the CRS schema and immutability model.
- Procedure practice: Running a manual re-consent campaign.
- Procedure practice: Responding to an assisted withdrawal request.
- Case study: A regulator requests demonstration of consent for a specific data subject. The trainee must query the CRS, assemble the evidence pack, and explain the audit trail.

### 9.3 Tracking and Non-Compliance

All training is tracked via the Workday Learning Management System (LMS). Role-holders failing to complete mandatory training within the required calendar window shall be flagged as non-compliant. System access shall be suspended for any individual whose training is more than 30 days past due until the training is completed.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|--------|-------|--------------|
| SOP-DGP-001 | Data Classification and Handling | Defines how personal data categories are classified, critical for consent granularity. |
| SOP-DGP-003 | Records of Processing Activities (RoPA) | The central RoPA links each processing activity to its lawful basis, including consent. Consent records must reconcile with RoPA entries. |
| SOP-SEC-012 | Access Control and Identity Management | Governs the IAM system used to authenticate data subjects for the Consent Dashboard. |
| SOP-SEC-019 | Audit Logging and Monitoring | Defines the technical standards for the audit logs referenced in Sections 5 and 6. |
| SOP-RES-005 | Secondary Use of Data for Research | Specifies how MedInsight data may be used; depends on valid consent records managed herein. |
| SOP-MKT-002 | Electronic Marketing Communications | References consent requirements for email/SMS sends and the mandatory suppression upon withdrawal. |
| SOP-VEN-004 | Third Party Vendor Risk Management | Governs the BAA inventory and the requirements for third parties handling consent-related data. |

### 10.2 External Standards and References

| Reference ID | Description |
|--------------|-------------|
| ISO/IEC 27701:2019 | Security techniques — Extension to ISO/IEC 27001 and ISO/IEC 27002 for privacy information management. |
| NIST Privacy Framework v1.0 | A voluntary tool to help Meridian identify and manage privacy risk. |
| ICO Consent Guidance | UK Information Commissioner's Office detailed guidance on consent, used as a best-practice benchmark. |

---

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
|---------|------|-----------|-------------------|
| 0.1 (Draft) | 2021-03-10 | Dr. A. Sharma (former DPO) | Initial draft for review. |
| 1.0 | 2021-05-15 | Dr. A. Sharma, M. Gonzalez | First approved version. Established foundational consent collection for HealthPay launch. |
| 2.0 | 2022-11-20 | K. Weber, DGP Unit | Major revision: Introduced Granular Consent (PS-04) and the centralized Consent Record System (CRS) schema. Updated re-consent procedure for MedInsight expansion. |
| 2.1 | 2023-07-18 | K. Weber | Minor revision: Updated consent withdrawal SLAs from 45 days to 30 days. Added explicit parental consent flag to CRS schema. |
| 2.2 | 2024-03-05 | DGP Unit, M. Gonzalez | Clarification of explicit consent UI pattern (two-step confirmation). Addition of Section 9 training matrix. Updated RACI to include Compliance Officer as Informed. |
| 3.0 | 2024-12-06 | K. Weber | Comprehensive rewrite: Updated scope to cover all business units. Aligned definitions and procedures with new CMP. Enhanced controls and safeguards section with technical specifics. Extended re-consent window to 45 days. |