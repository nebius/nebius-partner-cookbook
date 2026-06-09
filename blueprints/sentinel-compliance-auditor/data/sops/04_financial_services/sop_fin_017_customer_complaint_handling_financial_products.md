---
sop_id: "SOP-FIN-017"
title: "Customer Complaint Handling — Financial Products"
business_unit: "Financial Services"
version: "3.2"
effective_date: "2024-06-12"
last_reviewed: "2025-10-05"
next_review: "2026-04-14"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "GDPR"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Customer Complaint Handling — Financial Products

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the formal, auditable framework for the intake, triage, investigation, resolution, and regulatory reporting of customer complaints related to the financial products and services offered by Meridian Health Technologies, Inc. (“Meridian” or the “Company”) through its HealthPay Financial Services business unit. The purpose of this SOP is to ensure that all complaints are handled consistently, fairly, transparently, and in full compliance with applicable regulatory obligations, contractual commitments, and internal control requirements as defined by SOC 2 criteria.

This procedure operationalizes the Company’s commitment to treating customers fairly, identifying and remediating systemic issues, and maintaining the integrity of the ~$4.2B in annual transactions processed by the HealthPay platform.

### 1.2 Scope

#### 1.2.1 In-Scope Products and Services
This SOP applies to all complaints, however received, pertaining to the following HealthPay Financial Services products and lines of business:
- **Patient Financing & Medical Lending:** Complaints concerning loan origination, APR disclosures, repayment schedules, credit reporting, and collections activity.
- **Payment Processing & Disbursements:** Complaints related to unauthorized transactions, duplicate charges, merchant settlement delays, refund processing, and point-of-service integration failures.
- **Claims Automation:** Complaints arising from claim adjudication errors, incorrect payer-patient responsibility assignments, and automated explanation of benefits (EOB) generation.
- **Provider Portal & API:** Complaints regarding data accuracy, platform availability, and transactional integrity for integrated provider partners.

#### 1.2.2 In-Scope Complainants
- **Patients/Consumers:** Individuals financing healthcare services, making payments, or receiving refunds.
- **Healthcare Providers:** Hospitals, clinics, and medical groups using the HealthPay processing network or claims automation services.
- **Payer Organizations:** Health plans and insurers leveraging claims automation and fraud detection products.
- **Authorized Representatives:** Any legally recognized agent acting on behalf of the above categories.

#### 1.2.3 Out of Scope
- Clinical decision support or diagnostic inaccuracies (refer to SOP-CAI-004, *Adverse Event and Clinical Safety Reporting*).
- General product feature requests without a monetary harm or service-level failure element.
- Internal operational incidents without an associated customer-facing impact (refer to SOP-IT-081, *Incident Management and Response*).
- Complaints related solely to the Meridian employment relationship (refer to *Employee Handbook, Article XIV*).

#### 1.2.4 Geographic Applicability
This SOP applies globally to all operational offices, including Boston (Headquarters), London, Berlin, Singapore, and Toronto, with additional country-specific requirements to be observed as communicated by the Office of General Counsel. For complaints involving personal data of European Economic Area (EEA) data subjects, the requirements of the General Data Protection Regulation (GDPR) apply as detailed herein.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **Complaint** | Any expression of dissatisfaction, whether oral or written, and whether justified or not, from or on behalf of a customer about the provision of, or failure to provide, a financial product or service. The expression must relate to an actual or potential monetary impact, data integrity issue, or regulatory non-compliance. |
| **Complainant** | The individual or entity lodging the complaint. |
| **Root Cause Analysis (RCA)** | A systematic problem-solving methodology, aligned with SOC 2 CC7.2, used to identify the underlying processes, control failures, or design flaws that allowed the event giving rise to the complaint to occur. |
| **Financial Materiality** | A classification threshold defined as a complaint involving a monetary impact or potential impact of ≥ $500 USD or equivalent, or any amount related to suspected fraud or identity theft. |
| **High-Risk Complaint** | A complaint that alleges (a) violation of federal or state lending laws, (b) systemic unauthorized access to financial data, (c) discriminatory lending practices, (d) an event that is immediately reportable to a regulatory body, or (e) potential litigation. |
| **Service Level Agreement (SLA)** | The contractually defined, measurable commitment for acknowledgement, investigation, and resolution timeframes. |
| **HealthPay Platform (HPP)** | The core financial services processing system, including the patient financing portal (MyHealthPay), provider portal (HealthPay Connect), and the back-office case management system. |
| **CASEMGR** | The centralized complaint and case management application within the HealthPay Platform used for logging, tracking, and reporting all in-scope complaints. |
| **GDPR** | General Data Protection Regulation (EU 2016/679). |
| **SOC 2** | AICPA Trust Services Criteria for Service Organizations. |
| **CCx.y** | Reference to a specific SOC 2 Common Criteria point of focus (e.g., CC7.2 addresses management's detection and monitoring of processing deviations). |
| **PII** | Personally Identifiable Information. |
| **PHI** | Protected Health Information. |
| **KPI** | Key Performance Indicator. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the accountability and authority for all roles involved in this SOP.

| Role | Responsibility (RACI) | Specific Duties |
| :--- | :--- | :--- |
| **VP of Financial Services (Robert Liu)** | **A - Accountable** | Ultimate ownership of the complaint management process. Approves all SOP revisions, major process deviations, and systemic remediation plans. Chairs the monthly Complaints Governance Forum. |
| **Director of Financial Operations** | **A - Accountable (Operational)** | Day-to-day oversight of the Complaint Handling Unit. Approves complaint closure for all High-Risk complaints. Authorizes binding goodwill compensation up to $5,000. |
| **Complaint Handling Unit (CHU)** | **R - Responsible** | Centralized intake, triage, and case ownership. Performs Level 1 and Level 2 investigations. Communicates directly with complainants. Drafts responses and manages CASEMGR records. |
| **Compliance Officer, Financial Services** | **R - Responsible** | Conducts regulatory impact assessment for all High-Risk complaints. Manages regulatory filing obligations (e.g., state/federal reporting). Validates that resolutions meet regulatory standards. |
| **Chief Privacy Officer / DPO (Dr. Klaus Weber)** | **C - Consulted** | Mandatory consultation on any complaint involving an allegation of a personal data breach, a request for data erasure/deletion, or a formal data subject access request (DSAR) lodged within a complaint. |
| **Information Security Team (CISO: Rachel Kim)** | **C - Consulted** | Mandatory consultation on complaints alleging unauthorized account access, credential compromise, or security control failure. Performs forensic analysis when required. |
| **VP of Customer Operations (Michael Chang)** | **I - Informed** | Receives weekly trend reports on complaint volume and sentiment. |
| **General Counsel (Maria Gonzalez)** | **I - Informed** | Informed of all High-Risk complaints within 24 hours of classification, and immediately upon receipt of any formal legal complaint or summons. |
| **Customer Support Tier 1** | **I - Informed** | Receives updated knowledge base articles from CHU to prevent recurrence. |

---

## 4. Policy Statements

Meridian Health Technologies is committed to operating a transparent, accessible, and timely complaint handling mechanism that meets or exceeds the requirements of applicable regulatory bodies and the AICPA Trust Services Criteria for SOC 2.

1.  **Accessibility:** The complaint process shall be barrier-free. Mechanisms for submitting complaints are published on the HealthPay website, within the mobile application, on all periodic statements, and in provider service agreements.
2.  **No Retaliation:** No complainant shall be subject to adverse treatment, fee imposition, or service discrimination as a consequence of having lodged a complaint in good faith.
3.  **Timeliness:** All complaints shall be acknowledged and resolved according to the strict SLAs defined in this SOP. Where resolution is anticipated to exceed the SLA, the Complainant must receive a detailed holding communication explaining the reason for the delay and a revised resolution date.
4.  **Objectivity and Fairness:** Each complaint shall be investigated on its merits. All investigations shall be conducted by personnel not directly involved in the subject matter of the complaint.
5.  **Data Integrity and Confidentiality:** All complaint records shall be treated as confidential. PHI and PII contained in complaint files shall be handled per HIPAA and SOC 2 CC6.1 (Logical and Physical Access Controls).
6.  **Continuous Improvement:** Complaint root cause analysis shall be a formal input into the risk assessment process, product management lifecycle, and internal controls testing required under SOC 2 CC8.1.
7.  **Regulatory Compliance:** For complaints originating from European data subjects, a specific privacy notice applies. This notice explains to the complainant who is collecting their data, the purposes of the processing, and who it will be shared with. All complaints involving cross-border transfer of data are acknowledged.

---

## 5. Detailed Procedures

This section details the end-to-end lifecycle of a customer complaint within the HealthPay Financial Services unit.

### 5.1 Intake and Triage

All complaints, regardless of entry channel, must be logged in CASEMGR within **4 business hours** of receipt.

#### 5.1.1 Intake Channels and Logging
- **Electronic (Web Form & Email):** Complaints submitted via `healthpay.meridian.com/complaints` or `complaints@meridianhealthfin.com` are automatically ingested into the CASEMGR queue via API. The system parses the sender email, date stamp, and raw body text.
- **Voice (Call Center):** A Tier 1 agent creates a CASEMGR record *while the caller is on the line*. The agent must read back the summarized complaint to the caller to confirm accuracy before submission.
- **Written (Physical Mail):** Received by the Boston HQ mailroom. Scanned and uploaded to CASEMGR by the Office Management team within the 4-hour SLA. Tracking is backdated to the physical postmark date.
- **Regulatory (Direct Referral):** Complaints forwarded directly from the Consumer Financial Protection Bureau (CFPB), State Attorney General offices, or the Better Business Bureau (BBB) bypass Tier 1 and are auto-flagged as **High-Risk** in CASEMGR.

#### 5.1.2 Triage Protocol
Upon logging, a CHU Intake Specialist assigns the complaint attributes in CASEMGR using the following decision tree:

1.  **Complainant Identity Validation:** Verify the customer record in the HealthPay core ledger. Flag as "Identity Unverified" and *do not disclose financial data* if identity cannot be confirmed. For EU residents, do not initiate identity verification that is disproportionate to the nature of the complaint.
2.  **Product Line Categorization:** Patient Financing (MED-LOAN), Payment Processing (MDR-PAY), Claims Automation (CLM-AUTO).
3.  **Materiality Assessment:**
    - **Financial Materiality:** Is the direct monetary impact ≥ $500?
    - **Regulatory Materiality:** Does the complaint invoke regulatory non-compliance (lending violations, privacy)?
    - **If any materiality factor is YES, flag as High-Risk.**
4.  **Data Privacy Nexus:** Does the complaint include a DSAR, a request for erasure, or an allegation of a data breach?
    - If YES, the CASEMGR record triggers an automatic parallel notification to the Office of the DPO (`dpo@meridianhealth.com`) with the subject line `[Action Required] GDPR-CASE-{ID}`. The CHU continues processing the financial complaint; the DPO independently manages the data subject rights request.

### 5.2 Acknowledgement and Initial Communication

- **Standard Complaints:** An automated acknowledgement email is sent from CASEMGR within **24 hours** of receipt. This email includes the unique CASEMGR ID, the assigned investigator's first name, and a link to the Meridian HealthPay *Customer Complaints Privacy Notice*.
- **High-Risk Complaints:** A personalized acknowledgement is sent by the Director of Financial Operations within **24 hours**. This communication includes direct contact details for the assigned case manager and a statement that the matter is undergoing an expedited regulatory review.

### 5.3 Investigation Process

The investigation is the evidentiary phase and must be completed per the SLA schedule defined in Section 6.1. The assigned CHU Investigator follows these steps:

#### 5.3.1 Evidence Collection
The investigator assembles a case file within CASEMGR containing:
- **Ledger Extract:** Transaction logs, chargeback records, loan amortization schedules.
- **Platform Audit Logs:** Records from Splunk and DataDog capturing the user session, API calls, and system state at the time of the reported issue. This is critical for CC7.2 evidence.
- **Communication History:** All prior emails, support tickets (Zendesk), and call recordings related to the incident.
- **Dispute Documentation:** If applicable, relevant ACH/dispute filings with our acquiring bank.

#### 5.3.2 Root Cause Analysis (RCA)
For all High-Risk complaints and any standard complaint where the investigator determines Meridian is in error, an RCA must be documented using the "5 Whys" methodology in the CASEMGR "Root Cause" tab. Example:
1.  *Why was the patient’s APR 22% instead of 12%?* (The underwriting engine’s promotional flag wasn’t applied.)
2.  *Why wasn’t the flag applied?* (The batch upload from the Marketing module failed.)
3.  *Why did the batch upload fail?* (A schema change was made in the Marketing module without testing the downstream HealthPay integration.)

The RCA output is a formal "Corrective Action Preventative Action" (CAPA) ticket assigned to the product and engineering owners.

#### 5.3.3 Resolution Determination
Based on the RCA, the CHU Investigator, in collaboration with Financial Compliance, drafts a resolution plan. This may include:
- **Monetary Remedy:** Principal correction, interest/fee reversal, ex-gratia/goodwill compensation.
- **Non-Monetary Remedy:** Credit bureau correction letter, formal apology, process walk-through with the provider.
- **Systemic Fix Confirmation:** Verification that the assigned CAPA ticket has been accepted into an engineering sprint.

### 5.4 Resolution Letter and Closure

The final resolution letter (a "Final Action Letter") must be drafted on Meridian letterhead, signed by the Director of Financial Operations, and transmitted via the channel requested by the complainant.

1.  **Content Requirements (per SOC 2 CC7.4):**
    - Plain-language summary of the complainant’s concern.
    - Detailed findings of the investigation.
    - An unambiguous statement of the remediation action taken (or a clear justification for no action).
    - The specific monetary adjustments, including the timeline for the Complainant to see the credit in their account.
    - Contact details for the relevant Ombudsman or Regulator (e.g., CFPB in the U.S., Financial Ombudsman Service for complaints arising from UK operations).
2.  **Complainant Acknowledgement:**
    - For monetary remedies, the CHU must seek explicit written confirmation (email accepted) from the Complainant that the resolution is satisfactory before the case is closed in CASEMGR.
3.  **Case Closure in CASEMGR:**
    - A case is formally closed only when all remediation tasks (monetary and non-monetary) are marked "Complete" in CASEMGR. Closed cases are locked against further editing, with an immutable audit trail maintained.

---

## 6. Controls and Safeguards

This section defines the administrative and technical controls established to assure the integrity of the complaint handling process. These controls are designed, implemented, and monitored to satisfy the SOC 2 Common Criteria (CC) series.

### 6.1 Service Level Agreement (SLA) Controls
The following time-to-respond and time-to-resolve thresholds are hard-coded into the CASEMGR SLA clock and monitored by the Director of Financial Operations.

| Complaint Class | Acknowledgement SLA | Resolution Target | Escalation Trigger |
| :--- | :--- | :--- | :--- |
| **Standard (Non-material)** | ≤ 24 hours | 10 Business Days | Not resolved by Day 9; auto-notification to CHU Manager. |
| **High-Risk (Material)** | ≤ 24 hours (personalized) | 5 Business Days | Not resolved by Day 4; auto-notification to VP, Financial Services, and General Counsel. |
| **Privacy/GDPR Nexus** | ≤ 24 hours (dual-track) | Per complaint; 30 calendar days for the parallel DSAR track. | Independent tracking by the DPO’s office; separate from financial resolution SLA. |

### 6.2 Access Control (CC6.1)
- Logical access to CASEMGR is role-based and enforced via Okta SSO with MFA.
- **Segregation of Duties:** An investigator cannot self-approve a monetary remedy ≥ $100. The maker-checker control is strictly enforced within the CASEMGR workflow rules.
- Access to raw database records for investigation purposes is via a temporary-read-only elevation, which is logged and reviewed weekly by the CISO’s designated delegate.

### 6.3 Monitoring of Deviations (CC7.2)
- The Meridian Security Information and Event Management (SIEM) system ingests CASEMGR audit logs and SLA breaches in real-time. Anomalies—such as an account modifying multiple complaint records—generate a P2 security incident ticket automatically.
- Daily reconciliation of intake channels ensures no complaint is lost or omitted from the CASEMGR log.

### 6.4 Root Cause Remediation Chain (CC8.1)
- Each RCA that identifies a systemic control failure generates a CAPA ticket in Jira (`project: FINRISK`).
- The VP of Financial Services presents open FINRISK CAPA items at the quarterly SOC 2 Management Review meeting.
- A CAPA cannot be closed without a verifiable change to the production environment, a revised standard operating procedure, or a demonstrable system reconfiguration.

---

## 7. Monitoring, Metrics, and Reporting

Complaint data is treated as a Key Risk Indicator (KRI) for the financial services business unit. Metrics are auditable for SOC 2 CC9.2 and Management Review processes.

### 7.1 Key Performance Indicators (KPIs)
Metrics dashboards are hosted in Tableau, sourcing directly from CASEMGR and Workday.

| KPI | Target | Calculation |
| :--- | :--- | :--- |
| **C-SAT (Complaint Satisfaction)** | ≥ 90% | % of "Satisfied" ratings from post-resolution surveys. |
| **SLA Adherence** | 100% for High-Risk; ≥ 98% for Standard. | (Cases resolved ≤ Target) / Total Cases Closed. |
| **Mean Time to Resolution (MTTR)** | ≤ 5 Days for High-Risk. | Sum of time (days) from receipt to closure for High-Risk / Total High-Risk closed. |
| **Overturn Rate (Control Failure)** | < 1.5% | Number of complaints determined to be "In Error" by Meridian / Total Complaints Received. |
| **Repeat Complaint Rate** | ≤ 2% | Complaints from the same account on the same subject within 90 days. |

### 7.2 Reporting Cadence
- **Operational Dashboard (Weekly):** VP of Financial Services and CHU Manager review volume, channel distribution, and real-time SLA breach notifications.
- **Management Review Slide Deck (Monthly):** Director of Financial Operations prepares a trend analysis, including top 5 RCA findings, for the VP of Financial Services and CISO. This is a direct input into the SOC 2 CC9.2 Management Review risk assessment.
- **Quarterly Business Review (QBR) Deck:** A sanitized, aggregate report, including the Overturn Rate and systemic remediation status, is presented to the Chief Financial Officer (James Thornton) and General Counsel (Maria Gonzalez).

---

## 8. Exception Handling and Escalation

### 8.1 Deviation from SLA (Timing Exception)
If an investigation is unavoidably delayed (e.g., awaiting data from an external acquiring bank), the CHU Investigator must:
1.  Document the rationale and expected revised date in CASEMGR.
2.  Obtain approval from the Director of Financial Operations.
3.  Send a holding communication to the Complainant detailing the reason for delay and the next expected contact date.

No SLA deviation is permitted purely on the grounds of "high volume."

### 8.2 Goodwill Compensation Exceeding Authority
A goodwill payment exceeding $5,000 must be presented to the VP of Financial Services (Robert Liu) for approval, with a business justification memorandum attached. Any goodwill payment associated with a High-Risk complaint over $1,000 must also be reviewed by the Financial Compliance Officer.

### 8.3 Litigation Hold
Upon receipt of a formal legal notice, subpoena, or summons, the CHU Manager immediately:
1.  Transfers the CASEMGR record to "Legal Hold" status, removing it from the standard active queue.
2.  Notifies General Counsel (Maria Gonzalez) and the CISO (Rachel Kim) to initiate a litigation hold on all associated data, overriding standard data retention protocols.

---

## 9. Training Requirements

All personnel assigned to roles within this SOP must complete mandatory training before being granted access to CASEMGR and annually thereafter.

| Training Module | Target Audience | Delivery Method | Frequency | Tracking System |
| :--- | :--- | :--- | :--- | :--- |
| **FIN-101: Complaint Sensitivity & Customer Fairness** | All CHU, Tier 1 Support | Meridian LMS (Absorb) | Onboarding & Annual | Workday Learning |
| **FIN-201: Advanced Investigation & RCA Writing** | CHU Investigators, Financial Compliance | Instructor-led Workshop | Initial & Bi-annual | Workday Learning |
| **REG-202: Fair Lending & UDAAP for Complaint Handling** | All CHU, Director of Financial Ops | Meridian LMS (Absorb) | Annual | Workday Learning |
| **GDPR-GEN: Handling Personal Data Requests** | CHU, DPO Office Staff | Instructor-led Workshop (DPO) | Annual | Workday Learning |

**Training Non-Compliance:** An individual with lapsed training for > 30 days will have their CASEMGR access automatically suspended by a Workday-IAM integration workflow until the training is recompleted.

---

## 10. Related Policies and References

| Policy/Reference ID | Title | Relationship |
| :--- | :--- | :--- |
| **SOP-FIN-017** | *This Document* | Master record for financial complaints. |
| **SOP-CAI-004** | *Adverse Event and Clinical Safety Reporting* | Procedure for complaints with a clinical nexus. |
| **SOP-IT-081** | *Incident Management and Response* | Governs the parallel TIER-1 security incident lifecycle for data breach complaints. |
| **SOP-LEG-002** | *Litigation Hold and Legal Response* | Mandatory process triggered upon legal escalation. |
| **POL-DATA-001** | *Data Retention and Disposal Policy* | Defines the 7-year retention lifecycle for complaint records in CASEMGR. |
| **POL-COMP-003** | *Code of Conduct and Ethics* | Foundational commitment to fair dealing. |
| **EXTERNAL** | *AICPA TSC Section 100, 2017* | SOC 2 Trust Services Criteria (Common Criteria CC6.1, CC7.2, CC7.4, CC8.1, CC9.2). |

---

## 11. Revision History

| Version | Date | Author | Revision Description | Approver |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 2022-03-15 | Sarah Jenkins (Former VP, FS Ops) | Initial policy creation. Complaint handling for patient financing only. | John Mitchell (Former CFO) |
| 2.0 | 2023-01-20 | Robert Liu | Major revision: Expanded scope to all HealthPay Financial Products (Payments, Claims). Introduced CASEMGR logging. | James Thornton |
| 3.0 | 2023-11-10 | CHU Process Manager | Redefined Materiality thresholds. Added formal RCA and CAPA procedures to meet SOC 2 CC8.1. | James Thornton |
| 3.1 | 2024-02-28 | Office of the DPO | Integrated parallel DSAR processing track for EU data subjects. Added Data Privacy Nexus definitions. | Dr. Klaus Weber & James Thornton |
| 3.2 | 2024-06-12 | Robert Liu | Refined High-Risk escalation triggers. Updated role to General Counsel. Removed stand-alone UK appendix; folded into global process. Updated training module list. | James Thornton |