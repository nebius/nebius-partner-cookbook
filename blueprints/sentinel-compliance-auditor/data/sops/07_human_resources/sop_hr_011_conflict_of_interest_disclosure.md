---
sop_id: "SOP-HR-011"
title: "Conflict of Interest Disclosure"
business_unit: "Human Resources"
version: "4.3"
effective_date: "2025-02-08"
last_reviewed: "2026-01-03"
next_review: "2026-07-06"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Conflict of Interest Disclosure

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish a structured, auditable framework for the identification, disclosure, review, and management of actual, potential, and perceived conflicts of interest (COI) at Meridian Health Technologies, Inc. ("Meridian" or the "Company"). Given Meridian’s position at the intersection of healthcare delivery, artificial intelligence, and financial services, the integrity of our clinical algorithms, lending decisions, and data stewardship practices must remain beyond reproach. This SOP codifies the affirmative obligation of all Covered Persons to disclose relationships, financial interests, and outside activities that may compromise—or appear to compromise—their fiduciary duties to Meridian, our patients, our provider partners, and our shareholders.

### 1.2 Scope

This SOP applies to:

- **All Employees:** Full-time, part-time, temporary, and contract employees across all Meridian offices (Boston, London, Berlin, Singapore, Toronto) and remote workers globally.
- **Board Members:** All members of the Meridian Health Technologies, Inc. Board of Directors, including the AI Governance Committee.
- **Independent Contractors and Consultants:** Individuals or entities providing services to Meridian where such services involve access to proprietary algorithms, PHI, financial models, or decision-making authority.
- **Visiting Researchers and Interns:** Affiliates with access to Meridian systems covered under the Clinical AI Platform, MedInsight Analytics, or HealthPay Financial Services.
- **Immediate Family Members:** The financial interests and outside affiliations of a Covered Person’s spouse, domestic partner, and dependent children are treated as attributable to the Covered Person for disclosure purposes.

This SOP covers conflicts arising across all four Meridian business lines, with heightened scrutiny applied to roles governed by the EU AI Act (transparency and human oversight obligations), SR 11-7 model risk management, and FDA 510(k) device requirements.

### 1.3 Exclusions

- Routine purchases of broadly diversified mutual funds or exchange-traded funds (ETFs) where the Covered Person exercises no control over individual security selection.
- Employment relationships with Meridian subsidiaries (e.g., Meridian GmbH, Meridian Singapore Pte. Ltd.) that are already disclosed via standard HR onboarding.
- Activities explicitly approved under a Technology Transfer Agreement executed by General Counsel’s office prior to the effective date of this SOP.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|----------------|------------|
| **Actual COI** | A situation where a Covered Person’s personal interests are already interfering with their Meridian responsibilities. |
| **Ad Hoc Disclosure** | A point-in-time submission triggered by a specific event (e.g., new hire, promotion, acquisition of outside interest). |
| **Annual Attestation** | The required yearly certification by every Covered Person that their disclosures are current and complete. |
| **Covered Person** | Any individual falling within Section 1.2 (Scope) of this SOP. |
| **COI Management Plan (CMP)** | A legally binding, written plan documenting risk mitigation strategies approved by the COI Review Committee. |
| **COI Review Committee (CRC)** | A cross-functional body with representatives from HR, Legal, Compliance, and relevant business unit leadership that adjudicates material disclosures. |
| **COI-Hub** | Meridian’s proprietary case management system for COI disclosure intake, review workflows, and document storage, accessed via Okta SSO at coi-hub.meridian.health. |
| **Covered Transaction** | Any proposed business dealing between Meridian and an entity in which a Covered Person has a financial interest. |
| **Financial Interest** | Any ownership interest, equity, stock options, debt instrument, royalties, consulting fees, paid speaking engagements, or other remuneration valued in aggregate above USD $1,000 annually. |
| **Immediate Family Member** | A spouse, domestic partner, or dependent child residing in the Covered Person’s household. |
| **Institutional Conflict** | A COI arising when Meridian as an entity has financial interests that may compromise research integrity or patient outcomes. |
| **Outside Activity** | Any employment, consulting, advisory role, board service, teaching appointment, or volunteer leadership position external to Meridian. |
| **PHI** | Protected Health Information as defined under HIPAA. |
| **Potential COI** | A situation where future circumstances may reasonably lead to an Actual COI. |
| **Significant Financial Interest (SFI)** | Any financial interest exceeding USD $5,000 in aggregate value or representing >0.5% ownership of a publicly traded entity. |
| **Supervisory Reviewer** | The direct manager or department head responsible for initial disclosure acknowledgment. |

---

## 3. Roles and Responsibilities

The following responsibility matrix outlines accountabilities. R = Responsible (executes), A = Accountable (approval authority), C = Consulted (provides input), I = Informed (receives status updates).

| Role / Function | New Disclosure Submission | Initial Manager Review | Materiality Determination | CMP Approval | Annual Audit |
|---|---|---|---|---|---|
| **Covered Person** | R | I | I | I | R (Attests) |
| **Supervisory Reviewer** | C | R/A | C | I | I |
| **COI-Hub System (Automated)** | I (ticketing) | I (routing) | I (risk scoring) | I (versioning) | I (dashboard) |
| **Jennifer Walsh, CHRO** | I | I | A (policy owner) | C | A |
| **Maria Gonzalez, General Counsel** | I | I | C | A (binding legal) | C |
| **Thomas Anderson, CCO** | I | I | C | A (regulatory) | A |
| **Dr. Klaus Weber, CPO/DPO** | I | I | C (EU data subjects) | A (GDPR impact) | C |
| **COI Review Committee (CRC)** | I | I | R/A | R | I |
| **Board AI Governance Committee** | I | I | C (AI product COI) | I (escalations only) | I |
| **Internal Audit** | I | I | I | I | R |

### 3.1 COI Review Committee Composition

The CRC is a standing committee that convenes monthly and on an emergency basis as needed. Voting membership includes:

- **Chair:** Chief Compliance Officer, Thomas Anderson (or designee)
- **Secretary:** Senior HR Business Partner, Global Compliance
- **Member:** Deputy General Counsel, Litigation & Employment
- **Member:** VP of Engineering, David Park (for technology-related COIs)
- **Member:** VP of Financial Services, Robert Liu (for HealthPay-related COIs)
- **Member (non-voting):** A representative from the Chief Medical Officer’s office when clinical conflicts are under review.

CRC decisions require a simple majority of voting members. In a tie, the Chair casts the deciding vote. The CRC reports aggregate findings quarterly to the Board AI Governance Committee.

---

## 4. Policy Statements

Meridian Health Technologies, Inc. is committed to the following high-level policy positions, which inform the detailed procedures in Section 5:

4.1 **Presumption of Disclosure.** Covered Persons must operate under a presumption that any external financial interest, relationship, or activity is disclosable unless explicitly excluded under Section 1.3. Ambiguity is resolved in favor of disclosure.

4.2 **No Self-Dealing.** No Covered Person may use their position at Meridian to obtain an unwarranted financial or professional advantage for themselves, an Immediate Family Member, or an associated third party.

4.3 **Clinical Neutrality.** Employees with influence over clinical AI model development or medical device design functions must not hold any SFI in entities whose products, services, or therapies are subject to Meridian’s algorithmic evaluations or FDA submissions.

4.4 **Financial Services Integrity.** Employees with influence over HealthPay Financial Services credit models or underwriting criteria must not have an ownership interest exceeding USD $2,500 in any entity originating or servicing consumer loans covered by Meridian analytics.

4.5 **No Board Service Conflicts.** Covered Persons serving on external boards of directors or advisory boards must obtain written CRC pre-approval. Approval will not be granted for organizations that directly compete with Meridian in clinical AI, medical device manufacturing, or financial services predictive modeling.

4.6 **Anti-Retaliation.** Meridian strictly prohibits retaliation against any Covered Person who makes a good-faith disclosure under this SOP. Reports of retaliation are investigated by the General Counsel’s office and, if substantiated, result in disciplinary action up to termination of the retaliator.

4.7 **Continuous Obligation.** Disclosure is not a one-time event. Covered Persons must update their disclosure in COI-Hub within 15 calendar days of any material change in circumstances.

---

## 5. Detailed Procedures

### 5.1 Initial Disclosure Upon Onboarding

**Timeline:** Completed no later than five (5) business days after the Covered Person’s start date.

**Step-by-Step:**

1.  **System Invitation:** On the Covered Person’s first day, Meridian’s Identity and Access Management (IAM) system auto-provisions an account and triggers an email invitation to `coi-hub.meridian.health`. The invitation contains a unique, time-limited link.
2.  **Okta Authentication:** The Covered Person authenticates via Okta Single Sign-On (SSO) using their Meridian corporate credentials. Multi-factor authentication (MFA) via the Meridian-approved authenticator application is mandatory.
3.  **Intake Questionnaire Completion:** COI-Hub presents the "Initial Disclosure Questionnaire" (Form HR-011-F1). This dynamic form includes the following mandatory fields:
    -   *Personal Details:* Legal name, Meridian employee ID, business unit, office location, Supervisor name.
    -   *Outside Activities:* Current external employment, consulting, board service, academic appointments, volunteer leadership roles.
    -   *Financial Interests:* List all entities in which the Covered Person or an Immediate Family Member holds, or has held in the past 12 months, any Financial Interest. For each entity, provide the entity name, relationship (self/spouse/dependent), nature of interest (equity, debt, royalty, consulting), and approximate current USD value.
    -   *Intellectual Property:* Any patents, copyrights, or trademarks held personally or by an Immediate Family Member, whether revenue-generating or not, that relate to Meridian’s current or reasonably anticipated business areas.
    -   *Covered Transactions:* Identify any past, ongoing, or proposed business transactions between Meridian and any disclosed entity.
4.  **Attestation & Submission:** The Covered Person electronically signs the attestation:
    > ` "I certify that the above disclosures are true, complete, and accurate to the best of my knowledge. I understand that I have a continuing obligation to update this disclosure within 15 calendar days of any material change." `
    Upon submission, COI-Hub generates a unique case ID (format: `COI-YYYY-MM-NNNN`) and routes the disclosure to the Supervisory Reviewer.
5.  **Supervisory Reviewer Acknowledgment:** The Supervisor receives a COI-Hub notification and has three (3) business days to review. The Supervisor does not adjudicate conflicts but must:
    -   Acknowledge receipt.
    -   Add any comments regarding known or suspected COIs not apparent on the disclosure face.
    -   Flag the disclosure as ` "Supervisor Comments Added" ` or ` "No Comments." `

### 5.2 Annual Attestation Cycle

**Timeline:** Launched globally on February 1st of each year. All Covered Persons must complete attestation by March 1st.

**Step-by-Step:**

1.  **Launch Notification:** On February 1st, COI-Hub sends a blast notification, co-signed by Jennifer Walsh, CHRO, and Thomas Anderson, CCO, to all active Covered Persons via the Meridian intranet and company-wide email.
2.  **Pre-Populated Review:** Upon login, COI-Hub presents the Covered Person with their current, previously submitted disclosures. The system asks a binary primary question:
    > ` "Have you, or has any Immediate Family Member, acquired any new Financial Interest, begun any new Outside Activity, or engaged in any new Covered Transaction within the preceding 12 months that is not currently reflected in this disclosure?" `
3.  **Branching Logic:**
    -   **Branch A ("No Material Changes"):** The Covered Person reviews their existing disclosures, attests to their continued accuracy via electronic signature, and submits. This completes the annual requirement.
    -   **Branch B ("Yes, Material Changes Exist"):** The Covered Person is routed to the full Form HR-011-F1 questionnaire to detail only the new or changed items. Upon submission, the disclosure follows the standard review workflow described in Section 5.3.
4.  **Escalation for Non-Completion:** COI-Hub generates an automated non-compliance report on February 15th and February 25th. Supervisors receive escalating alerts. On March 2nd, HR Information Systems (HRIS) generates a final list of non-compliant employees for escalation per Section 8.2.

### 5.3 Standard Review Workflow for Disclosures with Material COIs

When a Covered Person discloses a Potential or Actual COI (either at onboarding, via ad hoc update, or during annual attestation), the following triage process is initiated in COI-Hub.

**Step 1: COI-Hub Risk Scoring (Automated)**
The system calculates a preliminary risk score (1-10) based on a pre-configured rubric:

| Factor | Weight | Criteria Example |
|---|---|---|
| **Interest Value** | 3 | > USD $15,000 value = 3 points; $5,000-$14,999 = 2; $1,000-$4,999 = 1. |
| **Entity Relationship** | 4 | Direct competitor to Meridian = 4 points; Supplier/Vendor to Meridian = 3; Entity regulated by Meridian’s AI output = 4. |
| **Role Influence** | 3 | Covered Person has direct decision-making power (e.g., buying authority, algorithm parameter control) over entity = 4 points; Indirect influence = 2. |

**Risk Triage Thresholds:**
-   **Risk Score 1-3 ("Low/Immaterial"):** Disclosure is auto-closed. Covered Person receives an automated "No-Conflict Determination" letter with a reminder of their continuous obligation to re-disclose if circumstances change. The CRC reviews an anonymized quarterly log of auto-closures.
-   **Risk Score 4-7 ("Moderate/Material - CRC Review Required"):** Disclosure is added to the CRC meeting agenda for the next regularly scheduled meeting.
-   **Risk Score 8-10 ("High/Critical - Immediate Review"):** COI-Hub sends an immediate high-priority alert (Slack channel `#exec-compliance-alerts` and email) to the CRC Chair (Thomas Anderson), CHRO (Jennifer Walsh), and General Counsel (Maria Gonzalez). An emergency CRC meeting is convened within 48 business hours.

**Step 2: CRC Adjudication Hearing**
The CRC reviews the scored disclosure, any Supervisor comments, and conducts a hearing if necessary. The Covered Person may be invited, or required, to attend for clarification. The CRC determines one of three outcomes:
-   **Outcome 1: No Conflict or De Minimis Conflict.** A formal "No Action Required" memorandum is issued. Rationale is documented in COI-Hub.
-   **Outcome 2: Manageable Conflict — COI Management Plan (CMP) Required.** The CRC determines that a conflict exists but can be managed through specific conditions. This triggers Section 5.4 (CMP Execution).
-   **Outcome 3: Unmanageable Conflict — Prohibition.** The CRC determines that the conflict is fundamentally incompatible with the Covered Person’s role at Meridian. The Covered Person is instructed to divest the conflicting interest or resign the conflicting outside activity within 30 calendar days. Failure to do so results in disciplinary action per the Employee Handbook, up to and including termination. A decision to mandate divestiture must receive the unanimous vote of CRC voting members plus written confirmation from General Counsel.

### 5.4 COI Management Plan (CMP) Execution

When the CRC determines a conflict is manageable, a COI Management Plan (Form HR-011-F2) is drafted. This is a binding addendum to the Covered Person’s employment terms.

**CMP Components:**
1.  **Summary of Disclosed Conflict:** A plain-language statement of the specific financial interest, relationship, or activity giving rise to the conflict.
2.  **Mitigation Controls:** A detailed list of specific, measurable controls. Examples include:
    -   *Recusal:* The Covered Person must recuse themselves from any procurement decision, model design meeting, hiring decision, or contract negotiation involving the specified external entity. Recusals are documented in meeting minutes and recorded in COI-Hub.
    -   *Divestiture Schedule (partial or phased):* A mandated schedule for reducing ownership below the SFI threshold over a period not to exceed 12 months.
    -   *Disclosure:* A requirement to proactively disclose the relationship to external stakeholders (e.g., an academic journal, a regulatory body like an FDA Institutional Review Board) where Meridian work is being published or reviewed.
    -   *Monitoring:* Assignment of a "CMP Monitor" — typically the Covered Person’s immediate Supervisor or a designated Compliance Officer — who conducts quarterly spot-checks to verify adherence to recusal instructions.
3.  **Breach Consequences:** A non-negotiable clause stating that breach of the CMP constitutes insubordination and grounds for immediate termination for cause.
4.  **Signatures:** The CMP must be electronically signed in COI-Hub (via DocuSign integration) by the Covered Person, the Supervisor, the CRC Chair, and the General Counsel.

Once executed, COI-Hub stores the CMP and adds it to the Covered Person’s permanent compliance record. The system generates quarterly reminders to the CMP Monitor to file a "CMP Adherence Report" consisting of a simple binary certification (` "Compliant" ` / ` "Non-Compliant" `).

### 5.5 Disclosure for Board Members and Executive Leadership

Members of the Board of Directors and Meridian’s C-Suite (Executive Leadership Team) are subject to an enhanced disclosure process, managed directly by the General Counsel’s office rather than the standard COI-Hub auto-routing.

- **Annual Questionnaire (Enhanced):** In addition to the standard Form HR-011-F1, these individuals complete an "Executive Interests Supplement" disclosing all compensated and uncompensated fiduciary positions (trustee, executor, director), any interest in real property leased to or from Meridian, and all gifts received during the preceding year valued above USD $250.
- **Independent Review:** Director disclosures are reviewed annually by independent outside counsel retained by the Board’s Nominating and Governance Committee. Executive disclosures are reviewed directly by the Chief Compliance Officer, with a summary report provided to the Board’s Audit Committee.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

- **Segregation of Duties:** The COI-Hub system administrators in the IT division are strictly prohibited from accessing the *content* of disclosures. Their access is limited to system configuration, uptime, and technical logs. Disclosures are encrypted at rest. Maria Gonzalez (General Counsel) is the designated "Legal Data Custodian" with sole authority to grant content-level administrative access in COI-Hub for a specific, auditable legal purpose (e.g., discovery, whistleblower investigation).
- **Mandatory 2-Person Review:** No single CRC member may unilaterally close a disclosure that has been scored as material (Risk Score ≥4). All such closures require a minimum of two signatories in COI-Hub — one from Legal/Compliance and one from HR.
- **Physical Document Handling:** Printed copies of CMPs or disclosures are prohibited. All COI records are maintained exclusively in the immutable, append-only ledger in COI-Hub. If a physical copy is generated for a legal proceeding, it must be watermarked `"CONTROLLED DOCUMENT"` and logged in the system by the Legal Data Custodian.

### 6.2 Technical Controls

- **Access Control:** Access to COI-Hub is governed exclusively via Okta SSO with mandatory MFA. Role-based access control (RBAC) is enforced: "Covered Person" (view/edit own disclosures), "Supervisory Reviewer" (view/edit subordinate disclosures, add comments), "CRC Member" (view all, vote, generate reports), "Legal Data Custodian" (full access for legal holds and e-discovery).
- **Audit Trail:** COI-Hub maintains an immutable, time-stamped, SOC-compliant audit log of all actions. Every disclosure view, edit, comment addition, risk score calculation, and status change is logged with the authenticated user ID, timestamp, IP address, the field changed, and the previous versus new value.
- **Encryption:** All COI data in transit is encrypted via TLS 1.3. Data at rest is encrypted using AES-256 encryption. The encryption key management is performed by the Meridian Information Security team, with access to keys restricted independently from COI-Hub application administrators.

### 6.3 Data Privacy

The storage and processing of Conflict of Interest disclosures for EU-based employees (Meridian GmbH) is governed by an existing Data Protection Impact Assessment (DPIA) on file with Dr. Klaus Weber’s office. Legal basis for processing is Meridian’s legitimate interest in maintaining institutional integrity, balanced against the employee’s privacy rights. All Covered Persons are informed of data processing via a Privacy Notice displayed at login.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The CHRO, in partnership with the CCO, monitors the following metrics to evaluate the effectiveness of this SOP:

| KPI | Target | Measurement Method |
|---|---|---|
| **Annual Attestation Completion Rate** | 100% of active Covered Persons by March 1st. | COI-Hub compliance dashboard. |
| **Ad Hoc Disclosure Timeliness** | 95% of ad hoc disclosures submitted within 15 days of triggering event. | Self-reported date of event vs. COI-Hub submission timestamp. |
| **CRC Meeting Cadence Adherence** | 12 monthly meetings held per year. | Meeting minutes filed in COI-Hub. |
| **CMP Adherence Rate** | 100% of quarterly monitor reports filed on time; <5% of reports flagging "Non-Compliant." | COI-Hub CMP monitor report dashboard. |
| **Average CRC Case Resolution Time** | ≤ 30 calendar days from disclosure submission to final outcome memo for Moderately scored cases. | COI-Hub case lifecycle analytics. |

### 7.2 Reporting Cadence

- **Monthly Compliance Snapshot:** COI-Hub generates an automated, non-editable report summarizing total active disclosures by risk score, open CMPs, and late attestations. This is emailed to the CHRO and CCO on the 5th of each month.
- **Quarterly Aggregate Report:** The CRC Secretary prepares a sanitized, aggregate report for the Board AI Governance Committee. This report focuses on volume trends, risk score distributions by business unit, and any thematic concerns (e.g., "a significant rise in disclosures related to competing AI startups from Clinical AI Platform staff"). No individually identifiable data is presented without a prior determination by General Counsel.

---

## 8. Exception Handling and Escalation

### 8.1 Policy Exception Requests

A Covered Person may request an exception to a specific provision of this SOP (e.g., an extension of the 15-day ad hoc disclosure window due to documented medical incapacitation). The process is:
1.  Covered Person submits request through COI-Hub, selecting "Request Policy Exception."
2.  Request must include rationale and, if applicable, supporting documentation.
3.  Request is routed to the CRC Chair and CHRO for joint review.
4.  Decision is issued within 5 business days. All exceptions are approved on an individual, time-limited basis. A standing exception may not be granted.

### 8.2 Escalation for Non-Compliance

Failure to comply with the disclosure or CMP adherence requirements is escalated as follows:

- **First Instance (Late Submission/Missed Deadline):** COI-Hub sends an automated delinquency notice to the Covered Person, with a cc: to their Supervisor. The notice grants a 5-business-day grace period to cure the non-compliance. A copy is placed in the employee’s general HR file, but does not constitute a formal disciplinary action.
- **Second Instance (or Failure to Cure after First Instance):** The CRC Secretary issues a "Formal Compliance Warning" via email. The Supervisor is instructed to conduct a documented coaching conversation. A summary memo is uploaded to COI-Hub and the employee’s HR file.
- **Third Instance or Flagrant Violation (e.g., intentional non-disclosure of a Critical conflict):** The matter is referred directly to the General Counsel, Maria Gonzalez, for a joint investigation with the CHRO. Sanctions follow the Employee Handbook corrective action framework up to and including termination. For Board members, the Nominating and Governance Committee of the Board handles the process.

---

## 9. Training Requirements

### 9.1 Initial Training

All newly onboarded Covered Persons must successfully complete the "Meridian Integrity Foundations" course within the first 10 business days of employment. The course is delivered via the Learning Management System (LMS), accessible via `learn.meridian.health`. Module 4 of this course, titled "Conflict of Interest: Our Shared Responsibility," is specific to this SOP. A passing score of 85% on the end-of-module quiz is mandatory. Failure to complete the training within the 10-day window results in automated system alerts to the Supervisor and HR Business Partner, and a "Not In Good Standing" flag in the HRIS until completion.

### 9.2 Annual Refresher Training

Coinciding with the Annual Attestation cycle launch on February 1st, all active Covered Persons are assigned an updated "Annual COI Refresher" course in the LMS. This course highlights any SOP revision history from the prior year and walks through current CMP precedent scenarios (anonymized). Completion of the refresher training is a prerequisite for submitting the Annual Attestation in COI-Hub.

### 9.3 Targeted Role-Based Training

- **CRC Members:** Must attend a 2-hour live, instructor-led training session facilitated by the General Counsel’s office annually, focusing on implicit bias in adjudication and advanced regulatory risk assessment (including SR 11-7 and EU AI Act implications).
- **Engineering and Clinical Product Leads (Directors and above):** Participate in a semi-annual "AI Ethics and Integrity" seminar, co-hosted by the CTO’s office and the CCO’s office, where conflicts of interest in model development and data procurement are a primary case study topic.

### 9.4 Training Tracking

All training completions, quiz scores, and workshop attendance records are stored in the LMS and fed via API to the COI-Hub compliance record for each Covered Person. The CRC Secretary validates that every individual on the CRC roster has completed their targeted training prior to their participation in any adjudication hearing.

---

## 10. Related Policies and References

This SOP is an integral component of the Meridian Health Technologies compliance and ethics framework. All Covered Persons should, at a minimum, be familiar with the following cross-referenced documents.

| Reference | SOP-ID / Document | Description |
|---|---|---|
| **Employee Handbook** | SOP-HR-001 | Comprehensive workplace policies, including corrective action framework. |
| **Code of Business Conduct and Ethics** | SOP-LEG-002 | Foundational ethical principles governing all Meridian business operations. |
| **Data Privacy and Protection Policy (GDPR)** | SOP-LEG-045 | Handling of personal data for EU-based Covered Persons; managed by DPO Klaus Weber. |
| **Algorithmic Transparency and Model Governance** | SOP-ENG-088 | Governs development and clinical validation of AI/ML models, including model developer COI provisions. |
| **Supplier and Vendor Integrity** | SOP-FIN-024 | Procurement integrity rules where COI disclosures are cross-referenced during vendor selection. |
| **Anti-Retaliation and Whistleblower Protection** | SOP-LEG-009 | Confidential reporting channels and protection from retaliation for good-faith reports. |
| **Information Security Policy** | SOP-IT-003 | Encryption standards, access control, and acceptable use policies underlying COI-Hub. |

---

## 11. Revision History

| Version | Date | Author / Owner | Summary of Changes |
|---|---|---|---|
| 4.3 | 2026-01-03 | Jennifer Walsh, CHRO | Refined annual attestation launch date. Updated CRC membership (Robert Liu replacing former VP of Lending). Clarified CMP quarterly monitoring report obligations. |
| 4.2 | 2025-08-15 | Jennifer Walsh, CHRO | Incorporated EU AI Act transparency obligations into Section 1.2 (Scope). Updated escalation contacts. |
| 4.1 | 2025-06-01 | Maria Gonzalez, General Counsel | Revised Section 5.5 (Board Member Enhanced Process). Added new "AI Ethics and Integrity" training for clinical product leads. |
| 4.0 | 2025-02-01 | Jennifer Walsh, CHRO | Major revision. Migrated all disclosure workflows from manual paper/email to new COI-Hub system. Introduced automated risk scoring (Section 5.3). |
| 3.1 | 2024-04-10 | Thomas Anderson, CCO | Updated "Outside Activity" definition to specifically capture advisory roles post-CE marking activities. Minor formatting edits. |