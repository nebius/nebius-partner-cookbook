---
sop_id: "SOP-COPS-004"
title: "Customer Identity Verification"
business_unit: "Customer Operations"
version: "2.3"
effective_date: "2025-05-02"
last_reviewed: "2026-03-25"
next_review: "2026-09-22"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "HIPAA"
  - "SOC 2"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Customer Identity Verification

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for verifying the identity of customers, authorized users, and legal representatives who interact with Meridian Health Technologies, Inc. products, services, and protected data assets. The purpose of this SOP is to ensure that access to protected health information (PHI), personally identifiable information (PII), financial accounts, and high-risk artificial intelligence systems is granted exclusively to authenticated and authorized individuals, thereby preventing unauthorized disclosure, fraudulent transactions, social engineering compromises, and identity theft.

This SOP implements controls required by the Health Insurance Portability and Accountability Act (HIPAA) Security and Privacy Rules, the System and Organization Controls 2 (SOC 2) Trust Services Criteria for Security and Confidentiality, and the General Data Protection Regulation (GDPR) principles of data protection by design and default.

### 1.2 Scope

This SOP applies to all identity verification activities performed by or on behalf of Meridian Health Technologies, Inc., including interactions conducted through the following channels:

| Channel | Applicable Systems | Audience |
|:---|:---|:---|
| Digital Self-Service | Meridian Customer Portal (Okta SSO), MedLink Mobile App | External Customers, Providers |
| Assisted Service | Salesforce Service Cloud, Zendesk Talk | Customer Operations Agents |
| In-Person | Clinician tablet workstations, Front-desk kiosks | Clinic Staff, Patients |
| Financial Operations | Stripe Connect, NetSuite ERP | Billing Administrators, Payers |
| Enterprise Administration | Azure AD, Okta Admin Console | Internal Workforce Members |

This SOP applies to all workforce members, independent contractors, third-party administrators, and business associates who initiate, validate, or approve identity verification transactions. It governs verification of both natural persons and legal entities acting as Meridian customers.

### 1.3 Out of Scope

The following activities are explicitly excluded from this SOP and are governed by separate policies:
- Authentication of automated system-to-system API calls (see SOP-SEC-012: API Key and Service Account Management)
- Physical access verification at Meridian office locations (see SOP-FAC-003: Physical Access Controls)
- Employment eligibility verification (I-9 processing) (see SOP-HR-001: Onboarding and Offboarding)

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
|:---|:---|
| **CIV** | Customer Identity Verification – the process described by this SOP |
| **PII** | Personally Identifiable Information – information that can be used to distinguish or trace an individual's identity |
| **PHI** | Protected Health Information – individually identifiable health information as defined by HIPAA |
| **KBA** | Knowledge-Based Authentication – verification using information only the legitimate customer should know |
| **MFA** | Multi-Factor Authentication – authentication requiring two or more distinct categories of credentials |
| **IDV** | Identity Document Verification – automated or manual validation of government-issued identification |
| **Biometric Verification** | Confirmation of identity using unique biological characteristics (facial geometry, voiceprint) |
| **Liveness Detection** | Technology that verifies a biometric sample is from a live person, not a spoof artifact |
| **IRL** | Identity Risk Level – the calculated risk score (1-5) assigned to a verification attempt |
| **IdP** | Identity Provider – Okta, Meridian's central identity platform |
| **CISO** | Chief Information Security Officer |
| **DPO** | Data Protection Officer |
| **Access Request** | A formal submission for access to Meridian systems or data by or on behalf of a customer |
| **Authorized Representative** | An individual legally empowered to act on behalf of a customer (e.g., legal guardian, power of attorney) |
| **Social Engineering** | Psychological manipulation to trick individuals into divulging confidential information or performing actions |
| **Spoofing** | Presenting falsified biometric or documentary evidence to impersonate another individual |

## 3. Roles and Responsibilities

The following RACI matrix assigns accountability for all key activities within this SOP.

| Activity | VP, Customer Ops (Michael Chang) | VP, Financial Services (Robert Liu) | CISO | DPO | Team Lead, Customer Ops | Customer Ops Agent | Compliance Analyst | Identity Intelligence Analyst |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| SOP Ownership & Annual Review | A | C | C | C | R | I | I | I |
| Execute Standard Verification | I | I | I | I | A | R | I | I |
| Execute Elevated (IRL 4-5) Verification | I | A | C | C | R | I | I | C |
| Approve Exception Handling | A | A | C | C | R | I | I | I |
| Monitor Verification SLAs | A | I | I | I | R | C | C | I |
| Investigate Verification Failures | I | I | I | I | A | C | R | R |
| Training Assignment & Tracking | A | I | I | I | R | C | I | I |
| Reporting to Leadership | R | R | R | R | A | I | I | I |
| Technology & Vendor Evaluation | C | C | A | C | R | I | I | I |

**Key: R = Responsible (does the work), A = Accountable (signs off), C = Consulted (provides input), I = Informed (receives output)**

### 3.1 Named Role Responsibilities

- **Michael Chang, VP, Customer Operations**: Final authority on operational procedures, exception thresholds, and SLA adherence. Approves SOP revision publication.
- **Robert Liu, VP, Financial Services**: Approves all verification procedures affecting financial account access. Authorizes exceptions for high-net-value accounts.
- **CISO**: Maintains technical architecture for identity verification systems, approves biometric and document verification vendors through the Third-Party Risk Management (TPRM) process.
- **DPO**: Ensures verification methods comply with GDPR Articles 5, 25, and 32; advises on legitimate interest assessments for verification data processing.
- **Identity Intelligence Analyst**: A dedicated role within the Security Operations Center (SOC) responsible for reviewing high-risk verifications (IRL 4-5), identifying identity fraud patterns, and tuning automated risk scoring models.

## 4. Policy Commitments

Meridian Health Technologies commits to the following high-level policy statements:

1. **Least Privileged Access**: No individual shall be granted access to PHI, PII, financial accounts, or administrative functions until their identity has been verified to a level commensurate with the requested access risk, in accordance with this SOP.
2. **Proportional Verification**: Identity verification requirements shall scale proportionally with the sensitivity of the data or transaction requested. Routine portal access requires Standard Verification; access to clinical records or financial instruments requires Elevated Verification.
3. **Data Minimization**: Meridian shall collect, process, and store only the minimum identity attributes necessary to achieve verification, in compliance with GDPR Article 5(1)(c).
4. **Anti-Social Engineering**: No identity verification procedure shall be modified, bypassed, or expedited based on verbal request, urgency claims, or external pressure. All high-risk actions require independent verification through a second authorized channel.
5. **Transparency**: Customers shall be informed, through a layered Privacy Notice presented at verification initiation, what data is collected, how it is used, the legal basis for processing (GDPR Articles 12-14), and their right to lodge complaints with supervisory authorities.
6. **Automation with Human Oversight**: Automated identity verification decisions (IRL 1-3, auto-approved) shall be subject to quarterly statistical audit to detect bias; IRL 4-5 decisions require manual human review before access is granted.

## 5. Detailed Procedures

This section describes the step-by-step operational procedures for Customer Identity Verification. All times referenced are in Coordinated Universal Time (UTC) for system logs; operational SLAs are expressed in business hours (Monday–Friday, 06:00–22:00 UTC).

### 5.1 Customer Identity Verification Intake

Verification is triggered when a person attempts to:
- Register a new Meridian Customer Portal account
- Request access to PHI for a patient other than themselves
- Initiate an Authorized Representative relationship
- Access financial billing or payment instruments
- Request a password reset or MFA factor reset through assisted service channels

The intake channel determines the initial workflow:

#### 5.1.1 Digital Self-Service Intake

1. Customer navigates to the Meridian Customer Portal or MedLink Mobile App and selects "Create Account" or "Request Access."
2. The system (Okta Registration Inline Hook) presents a data collection form requiring:
   - Full legal name
   - Email address
   - Mobile phone number (for SMS-based MFA binding)
   - Residential address
   - Date of birth
3. Upon form submission, the Customer Identity Risk Engine (`CIV-Risk`, Meridian custom microservice) calculates an initial Identity Risk Level (IRL) based on:
   - Geolocation IP analysis (anomaly from known residential area)
   - Email domain reputation score (using ZeroBounce API)
   - Phone carrier tenure and porting history (using Twilio Lookup API)
   - Device fingerprint hash (using ThreatMetrix)
4. The IRL score (1-5) dictates the subsequent verification path per the table below:

| IRL Score | Risk Category | Required Verification Path | Maximum SLA from Trigger |
|:---|:---|:---|:---|
| 1 | Low | Email Ownership + SMS OTP | 5 minutes (automated) |
| 2 | Moderate | Email + SMS + Knowledge-Based Authentication (KBA) | 15 minutes (automated) |
| 3 | Medium-High | Email + SMS + KBA + Identity Document Verification (IDV) | 4 business hours |
| 4 | High | All Standard + Biometric Liveness Check + Manual Review | 8 business hours |
| 5 | Critical | All Elevated + Out-of-Band (OOB) call-back + CISO consultation | 24 business hours |

#### 5.1.2 Assisted Service Intake (Contact Center)

1. Customer contacts Meridian Customer Operations via phone (Zendesk Talk) or chat (Salesforce Service Cloud Live Agent). A unique ticket (`CASE-XXXXX`) is created in Salesforce.
2. The Agent performs an initial identity screening using the **"Ask but Do Not Tell"** protocol:
   - Agent requests: Full name, Date of Birth, and the email address on file.
   - Agent **does not** confirm whether the provided information matches any existing record.
3. The Agent enters the provided data into the **CIV-Assist Console** (a custom Salesforce Lightning component integrated with the CIV-Risk engine).
4. CIV-Assist returns the IRL score and the required verification path. If the caller is already an established customer (existing record found), the Risk Engine uses a modified baseline that includes account history tenure.
5. For IRL 3-5, the Agent must explicitly inform the caller: *"For your security, this call will be recorded, and I will now guide you through enhanced verification steps, which may include uploading a government ID and completing a brief facial scan."* This disclosure meets GDPR Article 12 transparency requirements for data collection during a call.

### 5.2 Standard Verification Methods

The following procedures detail each verification method component.

#### 5.2.1 Email Ownership Verification (All IRL)

1. Upon submission of the intake form, Okta triggers a one-time passcode (OTP) via the Meridian Notification Service (AWS SES).
2. The OTP is a 6-digit numeric code valid for **10 minutes** from issuance.
3. The email body **shall never include** the customer's full name or any PII alongside the OTP. The template reads: *"Your Meridian verification code is: XXXXXX. If you did not request this, please contact support immediately."*
4. The customer enters the OTP into the verification screen.
5. After 3 incorrect attempts, the OTP is invalidated, and the attempt counter increments. After 5 invalidated OTP cycles within a 24-hour period for a single email address, the email is placed in a **Verification Quarantine** for 4 hours. The SOC is notified via SIEM alert (`CIV_EMAIL_QUARANTINE`).

#### 5.2.2 SMS OTP (Phone Binding) (All IRL)

1. A distinct 6-digit OTP is sent via the Twilio SMS Gateway to the mobile number provided.
2. Validity period is **10 minutes**, with a 3-attempt limit per single OTP.
3. The SMS text must read: *"Meridian verification code: XXXXXX. Do not share this code. Call +1-800-MERID-0 if you did not expect this."*
4. Successful validation binds the mobile number as an authorized MFA factor in the Okta Universal Directory.

#### 5.2.3 Knowledge-Based Authentication (KBA) (IRL 2-4)

1. The CIV-Risk engine queries the internal Salesforce Contact record and the Meridian Data Warehouse (`dw_cust_profile` schema) to generate 3-5 dynamic questions.
2. Question sources must be drawn from a pre-approved **KBA Question Library** maintained by the Customer Operations Team Lead. Questions may include:
   - Month and year of the most recent invoice payment amount within a stated range.
   - Name of a provider associated with a recent clinical visit (encounter date without diagnosis).
   - Street name of the previous address on file (not the full address).
3. **Strictly prohibited KBA questions:**
   - Mother's maiden name, full Social Security Numbers (any segment), full driver's license number, or full bank account numbers.
   - Information easily retrievable from social media (e.g., car model, pet name).
4. The customer must answer **at least 3 out of 4 questions correctly**.
5. The CIV-Assist screen displays questions in random order each session. Answers are not displayed to the Agent; only a PASS/FAIL indicator.
6. Three cumulative KBA failures within a 30-day period for a single identity record trigger an automatic account lock and a **High-Risk Identity Review** case routed to the Identity Intelligence Analyst queue.

#### 5.2.4 Identity Document Verification (IDV) (IRL 3-5)

1. The customer is presented (via portal or Agent-sent secure link via Mimecast Secure Messaging) with instructions to upload images of a valid, unexpired government-issued photo ID. Acceptable documents:
   - State-issued Driver's License (front and back)
   - State-issued Non-Driver ID Card (front and back)
   - Passport photo page (machine-readable zone (MRZ) visible)
2. The upload interface uses a secure Web SDK provided by the approved vendor, **Onfido**.
3. Onfido's automated checks include:
   - **Data Extraction:** Optical Character Recognition (OCR) extracts name, DOB, document number, and expiration date.
   - **Authenticity Check:** Analysis of security features (fonts, layouts, hologram presence) against known government-issued templates.
   - **Image Integrity:** Detection of digital manipulation (Photoshop artifacts, inconsistent EXIF metadata), glare, blur, or black-and-white photocopies.
4. Meridian's **Identity Matching Rule**:
   - The extracted First Name, Last Name, and Date of Birth from the ID document must match the intake form submission exactly (string comparison, case-insensitive).
   - If the ID includes a middle name or suffix that is absent from the intake form, the match succeeds only if the remaining fields match exactly and the Identity Risk Score is IRL 3; for IRL 4-5, this requires manual Agent review.
5. Onfido returns an automated decision: `CLEAR`, `CONSIDER`, or `REJECT`.
   - `CLEAR`: Onfido confidence score ≥ 85%. IRL 3 proceeds auto-approved. Logged in `tbl_civ_verification_log`.
   - `CONSIDER`: Score 60-84.9%. Case routed to a **Customer Ops Agent with IDV Specialist role** for manual review within 2 business hours.
   - `REJECT`: Score < 60% or document flagged as fraudulent. Verification attempt terminated; customer instructed to use alternate verification method; SOC notified via `IRL_REJECT_FRAUD` alert.

#### 5.2.5 Biometric Verification with Liveness Detection (IRL 4-5)

1. For transactions classified as IRL 4 or 5, the customer must complete a facial biometric scan with liveness detection.
2. The workflow uses the **Onfido Face Authenticate SDK**, deployed via the Meridian Customer Portal.
3. The user is prompted to grant camera permissions and perform **Active Liveness Challenge**:
   - The SDK displays a series of randomized instructions, e.g., "Turn your head to the left," "Read the 4-digit number on the screen," "Smile."
   - Passive liveness analysis simultaneously examines pixel-level artifacts to detect presentation attacks (e.g., printed photos, 3D silicone masks, digital deepfakes delivered via virtual camera injection).
4. The captured biometric facemap is compared against the photo extracted from the ID document submitted in Section 5.2.4 (1:1 Face Match).
5. **Biometric Data Handling (GDPR Article 9 compliance):**
   - Meridian **does not** receive or store raw biometric imagery or video. Onfido provides only a similarity score and a liveness pass/fail flag.
   - The explicit consent collected at the start of the biometric flow states precisely: *"Meridian will use facial geometry analysis to match your live face to the photo on your ID to protect your account. Meridian does not receive a photograph of your face; only a match score. Facial geometry data is processed in the EU and permanently deleted by our vendor 90 days after collection."*
   - The DPO has pre-approved this processing under the explicit consent derogation of GDPR Article 9(2)(a). Consent records are stored in the OneTrust consent management platform.
6. **Thresholds**:
   - 1:1 Face Match Similarity Score must be ≥ 0.75 (75%).
   - Liveness Check must be `PASS`.
   - If either fails, the attempt is `FAILED – Biometric Mismatch`. A mandatory manual review is required, and the customer must schedule a synchronous video verification call with a Customer Ops Team Lead.

### 5.3 Authorized Representative Verification

When a person claims to act on behalf of a Meridian customer (e.g., family caregiver, legal guardian, power of attorney), verification covers both the representative's identity and their legal authority.

1. The Authorized Representative undergoes Standard Verification for their own identity (IRL commensurate with Patient's data sensitivity).
2. The Representative must upload **Legal Authorization Documents** through the Meridian Document Vault (`SOP-DOC-002: Document Management`):
   - Valid, court-issued guardianship or conservatorship order.
   - Durable Power of Attorney for Healthcare, conforming to applicable state law.
   - Completed Meridian `FORM-CIV-AUTH-001` (Authorized Representative Attestation), notarized or electronically signed under penalty of perjury.
3. A **Legal Documentation Specialist** (within Compliance) reviews uploaded documents within **24 business hours**. They verify:
   - Document authenticity against court docket searches where digitally accessible.
   - The specific permissions granted exactly match the access requested (e.g., "access to billing history" vs. "full clinical record authority").
4. Approval is recorded in Salesforce with the Legal Documentation Specialist's electronic signature. The Authorized Representative's Okta profile is updated with a bounded `auth_rep_scope` attribute limiting access.

### 5.4 Social Engineering Prevention and Verification Out-of-Band

All Meridian Customer Operations Agents and workforce members processing verification requests must act as a human firewall against social engineering. The following mandatory procedure applies to any interaction where urgency, emotional distress, or authority is invoked to shortcut verification.

#### 5.4.1 Universal Out-of-Band Callback (IRL 4-5, Escalations)

1. If the verification attempt reaches IRL 4 or 5, or if a Standard Interaction is escalated by an Agent due to suspicious behavior, the Agent **must not proceed** with verification on the current communication channel.
2. The Agent informs the caller: *"For your account's protection, I am required to verify this request through an independent channel. I will contact you using the phone number registered to the account. This will happen in the next 60 minutes. If you cannot receive that call, you may schedule an in-person appointment at any Meridian clinic."*
3. The Agent places the interaction on "Pending - OOB Callback" status.
4. An independent **Verification Callback Specialist** (a separate Agent not involved in the original interaction, or a Team Lead) retrie the case and initiates an outbound call using the phone number on record (not any new number provided by the caller).
5. The Callback Specialist conducts a simplified verification (confirming last transaction date, reason for original contact). Only upon successful callback verification does the original request proceed.

#### 5.4.2 Red Flag Indicators

Agents must be trained to recognize and report the following Red Flag Indicators (RFIs) immediately to their Team Lead and via the `Report Phishing` button in the CIV-Assist console (which creates a `SEC-INC` case).

| Category | Red Flag Indicator |
|:---|:---|
| **Verbal Cues** | Caller exhibits extreme urgency ("my mother is dying, release records NOW"), uses overly technical jargon, excessive flattery or intimidation, name-dropping Meridian executives. |
| **Information Mismatch** | Caller provides correct account number but wrong date of birth; caller knows the patient's provider but cannot name the clinic location. |
| **Caller ID Spoofing** | Incoming call displays a Meridian internal number or the customer's own number. |
| **Environmental Cues** | Background noise suggesting a call center environment (many voices, keystroke clicking), poor audio quality consistent with VoIP spoofing. |
| **Request Anomaly** | Request for an unusual change right after an account update (SIM swap + password reset); request for records of a high-profile individual with no prior history. |

#### 5.4.3 Procedure Following a Reported Social Engineering Attempt

1. Agent reports the attempt via CIV-Assist, tagging it as `Suspected Social Engineering`.
2. The SOC Identity Intelligence Analyst receives a real-time SIEM alert.
3. The Analyst places the targeted identity record into a **"Compromised - Verification Suspended"** state in Okta. No further verification transactions are permitted on that record.
4. The Analyst initiates a forensic review, examining all events for that identity record for the prior 7 days.
5. The Analyst contacts the legitimate customer (using the OOB callback procedure) to notify them of the potential compromise and re-establish identity trust.
6. The incident is recorded and tracked per `SOP-SEC-001: Incident Response`.

## 6. Controls and Safeguards

Meridian implements a multi-layered defense strategy of administrative, technical, and physical controls to secure the Identity Verification process.

### 6.1 Administrative Controls

| Control ID | Control Description | Relevant Framework Mapping |
|:---|:---|:---|
| **AC-CIV-01** | **Background Checks**: All personnel with access to CIV systems shall undergo a criminal background check prior to access, renewed biennially. | SOC 2 CC1.1, HIPAA §164.308(a)(3)(ii)(B) |
| **AC-CIV-02** | **Least Privilege Access Reviews**: The VP of Customer Operations and CISO shall review all role-based access to CIV systems quarterly, certifying that access lists are correct. | SOC 2 CC6.3 |
| **AC-CIV-03** | **Segregation of Duties**: No single Agent may both perform a high-risk (IRL 4-5) verification and approve an exception for the same transaction. The CIV-Assist system enforces a maker-checker workflow. | SOC 2 CC6.3 |
| **AC-CIV-04** | **Third-Party Oversight**: The Identity Document and Biometric vendor (Onfido) shall be subject to Meridian's TPRM program, including annual SOC 2 Type II report review and a bi-annual security audit right exercise. | HIPAA §164.308(b)(1), GDPR Art. 28 |
| **AC-CIV-05** | **Data Retention Schedule**: Raw intake form data for denied/abandoned verifications shall be retained for 60 days for abuse analysis and then purged. Completed verification records shall be retained for the duration of the customer relationship plus 7 years. | GDPR Art. 5(1)(e), SOC 2 P6.5 |

### 6.2 Technical Controls

| Control ID | Control Description | Implementation System |
|:---|:---|:---|
| **TC-CIV-01** | **Encryption in Transit (TLS 1.3+)** | AWS Application Load Balancer terminating HTTPS for all CIV APIs; Mimecast for ID upload Secure Messaging. Strong ciphers enforced via AWS WAF rule. |
| **TC-CIV-02** | **Encryption at Rest (AES-256)** | All CIV data stored in `tbl_civ` within AWS RDS Aurora with AWS KMS-managed encryption keys. Document images stored in S3 bucket `meridian-civ-docs-prod` with default SSE-KMS encryption. |
| **TC-CIV-03** | **Automated Logging** | All verification attempt details (IRL, timestamp, channel, result, Operator ID) logged to `tbl_civ_verification_log` with `PROV_WRITE` privilege only. Logs ship to Splunk Cloud for SIEM correlation and immutable storage in AWS S3 Glacier Vault. |
| **TC-CIV-04** | **Rate Limiting** | The CIV-Risk API Gateway (AWS API Gateway) enforces: 10 requests/min per IP, 20 requests/hour per email, 5 KBA failures/24h per identity record. |
| **TC-CIV-05** | **Presentation Attack Detection (PAD)** | Onfido SDK includes ISO 30107-3 compliant passive and active liveness detection to prevent deepfakes, silicone masks, and 2D photo spoofs. |
| **TC-CIV-06** | **Dynamic KBA Question Store** | KBA questions and answers are not stored in plaintext. Answers are salted and hashed (SHA-256). The CIV-Assist app retrieves an ephemeral token to validate user input without exposing the answer. |

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs)

The Customer Operations Team Lead and the Compliance Analyst shall jointly review the CIV Executive Dashboard (`dash_civ_exec`) daily. The following quantitative thresholds apply:

| Metric | Type | Target | Alert Threshold | Measurement Period |
|:---|:---|:---|:---|:---|
| **Verification Attempts – Total Volume** | KPI | Report only | N/A | Daily |
| **Auto-Verified Rate (IRL 1-3 auto-pass)** | KPI | ≥ 85% of low-risk attempts | N/A | Weekly rolling |
| **Manual Review (CONSIDER) SLA Adherence** | KPI | ≥ 95% within 2 business hours | < 90% compliance for 2 consecutive hours | Real-time |
| **Out-of-Band Callback SLA Adherence** | KPI | ≥ 98% within 60 minutes | < 95% | Real-time |
| **IRL 5 (Critical) Time-to-Resolution** | KPI | ≤ 24 business hours | Any instance > 24 hours | Per-instance |
| **Document Verification Fraud Rate (REJECT/Manual-Confirmed-Fraud)** | KRI | < 0.5% of IDV attempts | > 0.75% month-over-month increase | Monthly |
| **Biometric Mismatch Rate** | KRI | < 1.5% of biometric attempts | > 2.0% in a rolling 7-day window | Weekly |
| **KBA Failure Rate (>3 cumulative)** | KRI | < 0.2% of active customer base | > 0.3% | Monthly |

### 7.2 Reporting Cadence

| Recipient Audience | Report Contents | Frequency | Delivery Method |
|:---|:---|:---|:---|
| **Customer Operations Agents** | Individual error queue status, personal SLA adherence | Weekly, Mon 09:00 UTC | Salesforce Dashboard |
| **Team Lead, Customer Ops** | Full operational dashboard; agent-level KPIs; IRL distribution; open exceptions | Daily | CIV Executive Dashboard (Tableau) |
| **Michael Chang (VP), Robert Liu (VP)** | Executive summary; YoY volume trend; Top 3 KRI breaches; exception analysis; regulatory update | Monthly, 5th business day | PDF Report, email with DPO/CISO cc |
| **Board of Directors Audit Committee** | Annual SOC 2 control attestation summary; material fraud attempts; CIV process maturity score | Annually, Q4 | Formal Board Paper |

## 8. Exception Handling and Escalation

### 8.1 General Exception Principles

Deviations from the identity verification procedures defined in this SOP are strongly discouraged. However, Meridian recognizes that rigid policy adherence may, in rare edge cases, preclude legitimate customer access (e.g., natural disaster preventing ID upload, disability preventing biometric liveness). All exceptions must be:
- **Risk-Assessed:** CISO or delegate must produce a written risk acceptance.
- **Time-Bound:** Exception approval is valid for a single defined transaction or a maximum of 7 calendar days.
- **Logged:** All exception details recorded in the `CIV Exception Register` (Salesforce custom object `CIV_Exception__c`).
- **Compensating Controls Applied:** At minimum, the out-of-band callback procedure plus a video confirmation call shall be applied.

### 8.2 Exception Approval Matrix

| Requested Deviation | Approver | Max Validity |
|:---|:---|:---|
| Waive IDV for identity re-verification after a validated, locked-account incident | Team Lead, Customer Ops | 48 hours |
| Waive Biometric requirement due to documented ADA disability | Michael Chang, VP Customer Ops (or delegate Director) | Perpetual, with annual review |
| Accept alternative non-US identification documents (GDPR cross-border case) | DPO + Team Lead, Customer Ops | 30 days |
| Bypass OOB callback due to verified lack of working phone number for customer | Robert Liu, VP Financial Services (if financial access requested) | 7 days, non-renewable |
| Emergency access to PHI without complete verification (life-threatening situation per HIPAA §164.510) | On-call Physician Executive + CISO | Single transaction; must be reviewed within 72 hours by Privacy Board |

### 8.3 Escalation Path

1. Agent identifies a case that cannot proceed via standard procedures.
2. Agent documents the blocking point in the Salesforce case, attaches evidence, and changes case status to `Pending Exception`.
3. Agent assigns the case to their immediate Team Lead.
4. Team Lead has **2 business hours** to either resolve (using their delegated approval authority) or escalate to the VP, Customer Ops or the DPO, as the matrix dictates.
5. For any exception involving a potential GDPR data subject access request or HIPAA Privacy Rule matter, the DPO must be concurrently notified via email to `dpo-alert@meridian.health`.

## 9. Training Requirements

All workforce members involved in identity verification must complete training to ensure their actions align with Meridian's security and privacy commitments.

| Training Module | Assigned Roles | Frequency | Delivery Platform | Minimum Passing Score |
|:---|:---|:---|:---|:---|
| **CIV-101: Identity Verification Fundamentals** | All Customer Operations Agents, Team Leads | Annually, plus on-hire day 1 | Workday Learning | 85% |
| **CIV-201: Advanced Social Engineering Defense** | All Customer Operations Agents, Team Leads, SOC Analysts | Semi-annually (Mar & Sep) | Workday Learning + Simulated Phishing (KnowBe4) | 90% |
| **CIV-202: Biometric & IDV Processing (GDPR)** | Team Leads, Legal Documentation Specialists, DPO | Annually | Workday Learning | 90% |
| **CIV-REF: Annual Refresher & SOP Amendment Acknowledgment** | All above roles | Within 14 days of any SOP revision | DocuSign CLM (acknowledgment) | Affirmation of Review |

All training completion records must be stored in Workday and are auditable. Non-completion of mandatory training by the assigned due date will result in temporary revocation of access to CIV systems, managed via an automated integration between Workday and Okta.

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP-ID | Title | Relationship |
|:---|:---|:---|
| SOP-SEC-001 | Incident Response | Governs response to confirmed identity theft or credential compromise. |
| SOP-SEC-012 | API Key and Service Account Management | Covers authentication for non-human identities interacting with CIV data. |
| SOP-DATA-002 | Data Classification and Handling | Defines PHI and PII classification and labeling applied to CIV data. |
| SOP-COPS-003 | Customer Communication and Notification | Governs the mandatory breach notification language sent to customers if their CIV data is compromised. |
| SOP-HR-007 | Disciplinary Action for Policy Violations | Outlines consequences, up to termination, for intentional circumvention of CIV controls. |
| SOP-DOC-002 | Document Management | Governs the storage of uploaded identity and legal authorization documents. |
| SOP-FAC-003 | Physical Access Controls | Controls access to Meridian facilities where in-person identity verification may occur. |

### 10.2 External Standards and Regulations

- **HIPAA Security Rule (45 CFR Part 160, 162, and 164)**: Specifically §164.312(d) Person or Entity Authentication; §164.308(a)(3)(ii)(A) Workforce Security; §164.308(a)(4)(i) Information Access Management.
- **SOC 2 Trust Services Criteria (2017 TSC, AICPA)**: CC6.1 (Logical and Physical Access Controls), P6.2 (Privacy – Collection), P6.4 (Privacy – Use and Retention).
- **GDPR (Regulation (EU) 2016/679)**: Article 5 (Principles), Article 9 (Special categories of data), Article 25 (Data protection by design), Article 32 (Security).
- **NIST SP 800-63A** (Digital Identity Guidelines, Enrollment and Identity Proofing): Guidance for Identity Assurance Levels (IAL) mapped to Meridian IRL scores.

## 11. Revision History

| Version | Date | Author | Description of Change |
|:---|:---|:---|:---|
| 1.0 | 2023-09-15 | Sarah Jenkins, CISO | Initial publication replacing legacy `CUST-VER-001` policy memo. Established IRL framework. |
| 2.0 | 2024-01-22 | Marcus Thorne, Principal Compliance Analyst | Major revision: Integrated Onfido IDV/Biometric vendor following TPRM approval. Added Section 5.2.4-5.2.5. Raised minimum face match threshold to 0.75. |
| 2.1 | 2024-06-10 | Anita Desai, DPO | GDPR alignment update: Added explicit consent disclosure for biometrics, revised data retention for denied verifications to 60 days, added Section 3.1 DPO Role. |
| 2.2 | 2024-11-08 | Michael Chang, VP Cust Ops | Post-incident revision following successful deepfake attempt on VP's account. Added Active Liveness Challenge, IRL 5 OOB Callback requirement, and Section 5.4.1 Universal OOB Procedure. |
| 2.3 | 2025-05-02 | Michael Chang, VP Cust Ops | Comprehensive annual review. Updated roles for new org structure. Added Red Flag Indicators table (5.4.2) and Authorized Representative workflow (5.3). Aligned all SLAs to business hours. Approved by Robert Liu. |

---
**END OF DOCUMENT**

*This is a controlled document. When printed, it is considered uncontrolled and for reference only. Always access the official version via the Meridian Policy Portal (sharepoint.internal/ops-policies).*