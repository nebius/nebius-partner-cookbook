---
sop_id: "SOP-DGP-019"
title: "Children's Data Protection"
business_unit: "Data Governance & Privacy"
version: "1.0"
effective_date: "2024-05-05"
last_reviewed: "2025-02-05"
next_review: "2025-08-23"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Children's Data Protection

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for the protection of children's data across all Meridian Health Technologies, Inc. ("Meridian") business lines, products, and services. The purpose of this document is to define the standardized processes by which Meridian identifies, verifies, processes, stores, and disposes of personal data relating to individuals under the age of digital consent as defined by applicable jurisdictional regulations. This SOP operationalizes the commitments set forth in the Meridian Data Privacy Policy (SOP-DGP-001) and reinforces the organization's adherence to the principles of data protection by design and by default, specifically tailored to the heightened sensitivity of pediatric health and financial information.

### 1.2 Scope

This SOP applies to all Meridian business units, including but not limited to the Clinical AI Platform, HealthPay Financial Services, and MedInsight Analytics. The scope encompasses:

- **All workforce members:** Full-time employees, part-time employees, contractors, consultants, interns, and third-party vendors who interact with Meridian systems that may process children's data.
- **All data processing activities:** Collection, recording, organization, structuring, storage, adaptation or alteration, retrieval, consultation, use, disclosure by transmission, dissemination or otherwise making available, alignment or combination, restriction, erasure, or destruction of children's data.
- **All data subjects:** Individuals under the age of 16, or the applicable age of digital consent in the data subject's jurisdiction, whose personal data is processed by Meridian, including patients, dependents on HealthPay accounts, and minors participating in clinical research facilitated by Meridian platforms.
- **All environments:** Production, staging, development, quality assurance, research sandboxes, and disaster recovery environments.
- **All deployment models:** Cloud-hosted (AWS, Azure, GCP), on-premises data center, and hybrid architectures.
- **COPPA considerations:** In the event that Meridian processes personal information from children under 13 years of age in the United States, this SOP extends to compliance with the Children's Online Privacy Protection Act (COPPA) and the implementing rule of the Federal Trade Commission (FTC).

### 1.3 Out of Scope

This SOP explicitly excludes the processing of employee dependent data for human resources benefits administration, which is governed by SOP-HR-005 (Employee Benefits Data Management). It also excludes anonymized or de-identified pediatric research datasets where re-identification is contractually and technologically impossible, which are governed by SOP-RD-003 (Anonymized Research Data Handling).

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| Age of Digital Consent | The minimum age established by a jurisdiction's data protection law at which an individual can independently consent to the processing of their personal data by an information society service. Under GDPR, the default age is 16, with Member State derogations allowing ages between 13 and 16. |
| Child / Minor | For the purposes of this SOP, an individual who has not yet attained the age of digital consent in their respective jurisdiction of residence. Meridian's global standard defines a child as any individual under the age of 16, unless a lower jurisdictional age is verified and logged by the DPO. |
| COPPA | The U.S. Children's Online Privacy Protection Act of 1998 (15 U.S.C. §§ 6501–6506), which imposes requirements on operators of websites or online services directed to children under 13 years of age, and on operators of general audience websites with actual knowledge. |
| Guardian Account | A dedicated user account type within Meridian's identity and access management (IAM) system that is linked to one or more minor dependents. The Guardian Account holder (parent or legal guardian) exercises all data subject rights on behalf of the linked minor, including consent management. |
| Minor User Account | A restricted user account within Meridian's IAM system assigned to an individual under the age of digital consent. This account type is provisioned only after verified parental consent and has default data minimization controls enforced at provisioning. |
| Personal Data of a Child | Any information relating to an identified or identifiable child. This includes, but is not limited to, clinical data, financial data associated with a HealthPay dependent account, geolocation data, persistent online identifiers (e.g., cookies, IP addresses), and biometric data used for identity verification. |
| Verified Parental Consent (VPC) | The process by which Meridian makes reasonable efforts, considering available technology, to ensure that the person providing consent for the processing of a child's data is the holder of parental responsibility. Methods include, but are not limited to, signed consent forms transmitted via encrypted channels, video-conference verification with a trained Meridian consent specialist, government-issued ID verification with facial matching, and knowledge-based authentication challenges. |
| Minor Data Lock (MDL) | A technical control automatically applied to Minor User Accounts that restricts data sharing with third-party marketing partners, disables behavioral analytics tracking, and prevents the export of raw pediatric data outside the approved clinical or financial processing environment. |

---

## 3. Roles and Responsibilities

The following RACI (Responsible, Accountable, Consulted, Informed) matrix defines the roles and responsibilities for the execution of this SOP.

| Role | Responsibility (RACI) | Specific Duties |
|---|---|---|
| **Chief Privacy Officer (CPO) / Data Protection Officer (DPO)** — Dr. Klaus Weber | **Accountable (A)** | Ultimate accountability for the Children's Data Protection program. Approves all exceptions to this SOP. Maintains the global Age of Digital Consent jurisdictional matrix. Reports program metrics to the Executive Risk Committee. |
| **General Counsel** — Maria Gonzalez | **Accountable (A)** for legal interpretation; **Consulted (C)** | Provides binding legal interpretation of regulatory requirements. Approves the language used in consent forms. Advises on breach notification obligations related to pediatric data incidents. Maintains inventory of relevant regulatory changes. |
| **Data Governance & Privacy Team** | **Responsible (R)** for policy maintenance, monitoring, and training | Drafts, reviews, and updates this SOP. Develops and delivers workforce training modules on children's data protection. Monitors compliance metrics and conducts privacy impact assessments. Manages the VPC intake and verification process. |
| **Engineering Leads (Clinical AI, HealthPay, MedInsight)** | **Responsible (R)** for technical implementation | Implement Minor Data Lock controls in application code. Ensure age-verification gates are integrated into user registration flows. Execute data minimization requirements in database schemas and logging configurations. Remediate vulnerabilities identified during pediatric data security scans. |
| **Product Managers** | **Consulted (C)** for feature design; **Informed (I)** of policy changes | Consult with the Data Governance & Privacy Team during the design phase of any feature targeting or likely to attract minors. Ensure that the User Interface (UI) for consent management meets accessibility standards. |
| **Chief Information Security Officer (CISO)** — Tanya Osei | **Responsible (R)** for security controls; **Informed (I)** of privacy incidents involving children | Ensures encryption standards are applied to pediatric data at rest and in transit. Configures the Data Loss Prevention (DLP) system to flag any unencrypted export of pediatric data. Coordinates incident response for any security incident involving a Minor User Account. |
| **Workforce Members (All)** | **Responsible (R)** for adherence | Complete mandatory annual training. Report any suspected unauthorized access to or processing of children's data immediately via the ServiceNow Incident Portal. |
| **Account Managers (HealthPay)** | **Responsible (R)** for BAA management | Ensure that any Business Associate (covered by a BAA) handling PHI that may include pediatric data is contractually bound to equivalent children's data protection standards. Review BAA terms annually. |
| **Third-Party Vendors / Sub-processors** | **Responsible (R)** for contractual compliance | Adhere to the security and privacy requirements detailed in Meridian's Data Processing Addendum (DPA), including specific clauses for the processing of children's data. Report any breach involving children's data to the Meridian DPO within 24 hours. |

---

## 4. Policy Statements

Meridian Health Technologies is committed to the following high-level policy statements regarding the processing of children's personal data. These statements establish the mandatory principles that guide the detailed procedures in Section 5.

- **PS-001: Lawful Basis and Consent.** Meridian shall not process the personal data of a child unless processing is based on the consent of the holder of parental responsibility for the child, which has been verified through the approved VPC process, or processing is necessary for the vital interests of the child patient in a clinical emergency context. For HealthPay services, VPC must be obtained and recorded prior to the creation of any Minor User Account or Guardian-linked dependent profile.

- **PS-002: Age Verification.** All Meridian platforms that permit direct user registration must implement an age-gating mechanism at the point of initial registration. A neutral age-gate is mandatory, which does not encourage minors to misrepresent their age. If a user indicates they are below the jurisdictional age of digital consent, the registration workflow shall redirect to the Verified Parental Consent process.

- **PS-003: Data Minimization by Default.** All systems processing children's data must operate with strict data minimization defaults. Behavioral profiling of minors for marketing purposes is strictly prohibited. Collection of special categories of data (e.g., geolocation, biometrics for non-clinical purposes) from minors is prohibited without a distinct, explicit VPC for that specific purpose.

- **PS-004: Transparency and Notice.** Any Meridian service that is likely to be accessed by a child or their guardian must provide a layered, child-appropriate privacy notice. This notice must be provided in addition to the full Meridian Privacy Notice and must explain, in age-appropriate language, what data is collected, why it is necessary for the service, and the rights of the child. PHI-related notices must align with HIPAA Notice of Privacy Practices (NPP) requirements.

- **PS-005: Security Posture.** Meridian assigns a "Critical" impact level classification to all pediatric personal data repositories. This classification mandates the highest available encryption standards, strict role-based access controls (RBAC) limited to clinical necessity, and real-time access logging that feeds the Meridian Security Information and Event Management (SIEM) system.

- **PS-006: Business Associate Agreements (BAAs).** For any processing of pediatric PHI by a Business Associate, the BAA must explicitly include clauses regarding the heightened sensitivity of minor health information. Account Managers are responsible for ensuring this clause is included in any new or renewed BAA where the service involves pediatric data processing workflows.

---

## 5. Detailed Procedures

This section outlines the step-by-step operational procedures for complying with this SOP. Deviations from these procedures must be handled per the process in Section 8.

### 5.1 Age Verification at Registration (Age-Gating)

This procedure is mandatory for all public-facing Meridian applications that include a self-service registration function, including the MedInsight patient portal, the HealthPay mobile application, and clinical trial recruitment webforms.

**Step 1: Neutral Age Gate Display**
Upon initial registration, the system must present a neutral age-gate screen. The UI must not employ design patterns that could nudge a user to misrepresent their age. The prompt asks: "Date of Birth (MM/DD/YYYY)". No default date is pre-filled.

**Step 2: Jurisdictional Age Calculation**
Upon form submission, the Meridian IAM system (Okta) calculates the user's age based on the submitted date of birth and the current UTC timestamp. It cross-references the age against the Meridian Age of Digital Consent Matrix maintained in the Governance, Risk, and Compliance (GRC) platform (OneTrust).

**Step 3A: Adult User (> Age of Consent)**
If the user's age meets or exceeds the threshold for their jurisdiction, the normal identity verification and registration workflow proceeds. The age-gate event is logged to the Okta audit trail with a transaction ID, but the date of birth is discarded for adult users after the age calculation, adhering to data minimization principles.

**Step 3B: Minor User (< Age of Consent)**
If the user's calculated age is below the jurisdictional threshold, the registration process immediately halts. The system displays a message: "Based on the date of birth provided, you are not able to create an account on your own. If you are a patient, a parent or legal guardian is required to manage your account. Please ask them to continue the registration process." The session transfers to the Verified Parental Consent workflow (Procedure 5.2). No user account is created at this stage. The submitted data (date of birth, IP address) is pseudonymized and stored in a dedicated VPC intake queue with a 14-day auto-deletion schedule if the VPC process is not initiated.

### 5.2 Verified Parental Consent (VPC) Process

**Step 1: Guardian Identity Proofing**
The adult claiming parental responsibility ("Claimant") must initiate the VPC process, linked to the Minor's pseudonymized queue entry via a unique one-time code displayed to the Minor's screen. The Claimant undergoes standard identity proofing using the Meridian Identity Verification Service (IVS) powered by Jumio. They must capture a government-issued photo ID via their mobile device or webcam.

**Step 2: Verification of Parental Relationship**
After successful ID proofing, the Claimant must establish their parental relationship to the Minor. The procedure differs based on the Meridian business unit:

- **Clinical AI / MedInsight (Clinical Data):** The Claimant must upload a legal document demonstrating parental responsibility (e.g., birth certificate, legal guardianship order, court order). Optionally, a secure video call with a Meridian Consent Specialist can be used for a live "show-and-verify" process where the Specialist visually verifies the document.
- **HealthPay (Financial/PHI Data):** The system leverages existing relationship data from the insurance eligibility transaction (270/271 X12 transaction) or plan sponsor data. If the Minor is already listed as a dependent on the Claimant's active health plan and this is electronically verifiable, the process is streamlined. If not, the document upload method above is required.

**Step 3: Presentation of Consent Form**
Upon successful relationship verification, the system presents the "Guardian Consent for Minor Data Processing" form. This is an interactive electronic form that clearly spells out, in plain, legally precise language:
- The categories of data Meridian will process about the Minor (e.g., clinical vitals, diagnostic images, claims payment history).
- The specific purpose of the processing for each category.
- Which third-party sub-processors (e.g., AWS for hosting, Datadog for application performance monitoring) will have access, limited to what is strictly necessary.
- A clear "Consent Denied" button with equal prominence to the "Consent Provided" button.

**Step 4: Consent Capture and Record**
The Claimant electronically signs the form via DocuSign. The signed consent form, a unique VPC Token ID, the Claimant's verified identifier, the Minor's pseudonymized initial identifier, date/time of consent, and IP address/device fingerprint are hashed and stored immutably in the "VPC Ledger" — a purpose-built, append-only database in Meridian's AWS environment with write-once, read-many (WORM) properties. A confirmation email is sent to the Claimant’s verified email. The Minor's account is now provisioned as a "Minor User Account" linked to the "Guardian Account."

### 5.3 Processing PHI of Minors (HIPAA Considerations)

When pediatric data is Protected Health Information (PHI), specific handling procedures, consistent with SOP-PHI-005, apply.

**Step 1: Training on Pediatric PHI**
All workforce members with potential access to PHI must complete the annual "HIPAA Privacy and Security" training module. This module includes a specific fifteen-minute sub-module on the nuances of minor information, emphasizing that a parent or guardian is generally the personal representative. Training completion is tracked via the Cornerstone Learning Management System (LMS). (Note: Training is delivered on an annual basis to all relevant workforce members and is not differentiated by specific job role).

**Step 2: Business Associate Agreement (BAA) Execution**
Before any third party processes pediatric PHI on behalf of Meridian, a Business Associate Agreement (BAA) must be executed. The Meridian Legal Department uses a standard BAA template. For new engagements involving the HealthPay platform or Clinical AI model training partners with access to PHI, the Account Manager submits a request via the Legal Service Desk in Jira. Legal reviews and executes the BAA. The executed BAA is stored in the central contracts repository (iManage).

**Step 3: Honor Personal Representative Rights**
When a guardian, acting as the personal representative of a minor, exercises HIPAA rights (e.g., access, amendment), the Health Information Management (HIM) team processes the request following SOP-PHI-002. The team must first validate that the requestor is indeed the verified guardian on file for the minor in the VPC Ledger before releasing any PHI.

### 5.4 Age-Gating Upgrades and Retroactive Review

**Step 1: Scheduled Account Age-Up Review**
A nightly automated batch job ("Age-Up Processor") within Okta scans all active Minor User Accounts where the Minor's verified date of birth now indicates they have reached the age of digital consent.

**Step 2: Notification of Attained Age**
Upon detection, the following actions are triggered:
1.  The "Minor User Account" flag is removed programmatically.
2.  An automated notification is sent to the email address associated with the user's account (now an adult) and, separately, to the linked former Guardian Account email. The notification, crafted by the Privacy Team, states: "As of [Date], the account previously managed by your parent/guardian has transitioned to a standard user account. You now have full control over your privacy settings and personal data. We recommend you review our full Privacy Notice to understand your rights and our obligations regarding your data." The notification links to the Meridian Privacy Notice and the user's Privacy Settings Dashboard.

**Step 3: Retroactive Application of Adult Controls**
All Minor Data Lock (MDL) controls (marketing restriction, analytics restriction) are automatically removed. The system does not retroactively grant consent for marketing communications; it merely enables the now-adult user to opt-in independently.

### 5.5 COPPA Compliance Verification (U.S.-Specific)

When Meridian is processing data from users in the United States, and it has actual knowledge that the user is under 13, this supplementary procedure is triggered, irrespective of HIPAA status.

**Step 1: Direct Notice to Parent**
Before any VPC process under 13 begins, the system provides a direct, concise notice compliant with 16 CFR § 312.4(c) to the Claimant's verified email. This notice includes a description of the specific verifiable consent method being requested.

**Step 2: Restricted Internal Access Flag**
An enhanced flag (`COPPA_PROTECTED`) is applied to the user's record in the Data Lake and clinical data systems. This flag is used by the Data Loss Prevention (DLP) and access control systems. Any query attempting to export data from a `COPPA_PROTECTED` record outside an approved, audited clinical use case is blocked by the Meridian Data Security Fabric and immediately generates a P2 Security Incident.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Name | Description | Environment |
|---|---|---|---|
| **TEC-022-01** | Age Verification Gate (AVG) | Mandatory age-gating implemented in the Okta Customer Identity Cloud (CIC) registration flows for all Meridian patient and customer portals. | All (Production, Staging) |
| **TEC-022-02** | Minor Data Lock (MDL) — Profile Restriction | IAM policy that prevents Minor User Accounts from being included in marketing automation lists, behavioral analytics cohorts, or non-clinical research datasets. Enforced by SailPoint IIQ. | All |
| **TEC-022-03** | Minor Data Lock (MDL) — API Restriction | API Gateway policy that blocks any outbound REST API call from a service handling minor data to third-party analytics, marketing, or data brokerage endpoints. Enforced by Kong API Gateway. | Production |
| **TEC-022-04** | VPC Consent Ledger | Immutable, append-only database with SHA-256 hashing to securely store the chain of VPC records. Built on Amazon QLDB. Audited quarterly by the Internal Audit team. | Production (AWS) |
| **TEC-022-05** | Pediatric PII Scanning Tool | Agent-based software (Spirion) deployed on all workstations and servers to scan for patterns indicative of a child's PII combined with parental PII (e.g., birthdate next to a guardian's SSN in text). Detects and alerts on unauthorized storage. | All |
| **TEC-022-06** | Encryption Standard — Pediatric Data | AES-256 encryption at rest for database columns tagged with `DATA_CLASS = CHILD_PHI` or `CHILD_PII`. TLS 1.3 enforced in transit. | All |
| **TEC-022-07** | `COPPA_PROTECTED` Flag & Dynamic Masking | A data-level security tag applied to users known to be under 13. Triggers dynamic data masking in analytics environments, ensuring any view of the data by non-clinical personnel masks direct identifiers. | Data Lake, Analytics |

### 6.2 Administrative Controls

| Control ID | Control Name | Description |
|---|---|---|
| **ADM-022-01** | Annual Pediatric Data Protection Audit | The Internal Audit team conducts an annual review of VPC records, age-up processing logs, and BAA clauses related to children's data. Results are reported to the Board Audit Committee. |
| **ADM-022-02** | VPC Consent Form Review | The Data Governance & Privacy Team, in consultation with General Counsel, reviews and updates the Guardian Consent Form template annually or when a significant change in processing operations occurs. |
| **ADM-022-03** | Third-Party Data Processing Addendum (DPA) | All contracts with sub-processors include a DPA that incorporates "Enhanced Requirements for Processing of Children's Data," mandating equivalent technical and organizational measures. |
| **ADM-022-04** | Incident Response Addendum | The Meridian Cybersecurity Incident Response Plan (IRP-001) contains a specific playbook for a "Confirmed Breach of Minor's Personal Data," which triggers mandatory notification to the CPO and General Counsel within 2 hours of confirmation. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Metrics

The effectiveness of this SOP is continuously monitored by the Data Governance & Privacy Team using the following quantitative metrics, displayed on the Privacy and Data Governance operational dashboard (Power BI).

| Metric ID | Metric Description | Target | Measurement Tool | Reporting Cadence |
|---|---|---|---|---|
| M-019-01 | **VPC Process Completion Rate:** Percentage of guardian-initiated VPC processes successfully completed. | > 90% | Okta CIC logs + VPC Ledger | Monthly |
| M-019-02 | **VPC Time-to-Completion:** Median time from submission of ID to completion of signed consent form. | < 15 minutes | Okta CIC logs + VPC Ledger | Monthly |
| M-019-03 | **Age-Up Processor Success Rate:** Percentage of accounts successfully transitioned nightly batch job without error. | 99.95% | Okta Admin logs | Weekly |
| M-019-04 | **DLP Blocks on `COPPA_PROTECTED` Data:** Number of blocked attempts to export `COPPA_PROTECTED` records to unauthorized destinations. Zero false positives is the target; each true positive is a P2 incident. | 0 true positives | Meridian Data Security Fabric dashboard | Real-time alerting; Weekly tally |
| M-019-05 | **Minor Data Stale Account Rate:** Number of Minor User Accounts linked to a Guardian Account where the Minor has reached the "age-up" threshold, but no transition notification has been successfully delivered. | < 5 per month | Age-Up Processor logs | Monthly |
| M-019-06 | **Annual Workforce Training Completion:** Percentage of workforce with potential minor data access who have completed the annual training. | 100% by December 1st | Cornerstone LMS | Quarterly, starting Q3 |

### 7.2 Reporting

The Chief Privacy Officer (DPO) provides a quarterly "Children's Data Protection Status Report" to the Data Governance Steering Committee. This report includes a summary of all metrics in Section 7.1, any exceptions approved under Section 8, and an update on relevant jurisdictional regulatory changes. A redacted summary of this report, suitable for external consumption, is made available to customers upon request during their annual SOC 2+ audit cycle.

---

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Request Process

Any requested deviation from the procedures in Section 5 or the controls in Section 6 must be processed through the Data Governance Exception Management Workflow.

**Step 1: Exception Request Submission (Jira Service Desk)**
The individual requesting the exception (e.g., a Clinical AI Product Manager launching a de-identified pediatric study where full VPC is technically impossible) submits a "Children's Data Protection Exception" ticket in the Jira Service Desk (`DG-EXCP` project). The request must include:
- Description of the specific procedure or control for which an exception is sought.
- Justification and business rationale for the temporary or permanent deviation.
- Comprehensive risk assessment describing potential privacy impacts to minors.
- Proposed compensating controls that will be implemented to reduce risk to an acceptable level.
- Start and end date for the exception (exceptions cannot be permanent; max 1 year).

**Step 2: Privacy Team Risk Assessment**
The Data Governance & Privacy Team (DG&P) triages the ticket. They perform an independent risk assessment and categorize the risk as Low, Medium, High, or Critical using the Meridian Privacy Risk Scoring Matrix (SOP-DGP-001-R1).

**Step 3: Approval Authority**
Exception approval is tiered based on residual risk:
- **Low/Medium Risk:** Requires approval from the Chief Privacy Officer (Dr. Klaus Weber) or their delegate.
- **High Risk:** Requires joint approval from the CPO and the Chief Information Security Officer (Tanya Osei).
- **Critical Risk:** Exception is denied. If a business-critical need persists, it must be escalated to the CEO for a final risk acceptance decision, with a documented report to the Board of Directors.

**Step 4: Tracking and Review**
All approved exceptions are logged in the GRC platform (OneTrust). A compensating controls audit is scheduled for the halfway point of the exception's duration. The exception owner must submit a renewal request no less than 30 days before the expiration date, requiring a fresh risk assessment.

### 8.2 Emergency Pediatric Data Access Escalation

In a clinical emergency where a minor's vital interests are at stake and immediate processing of data is necessary to provide critical care, the "break-glass" procedure in SOP-EME-001 (Emergency Data Access) can be invoked. The attending physician must log the emergency access within 1 hour of invocation into the ServiceNow Incident Portal. The access event is automatically flagged for a post-hoc review by the Privacy Team. No advance exception is required.

---

## 9. Training Requirements

To ensure all workforce members understand their responsibilities under this SOP, Meridian has established the following mandatory training curriculum.

| Training Module ID | Module Name | Audience | Frequency | Delivery Method | Success Criterion |
|---|---|---|---|---|---|
| TR-PRV-001 | Meridian Global Data Privacy Essentials | All Workforce Members | **Annual** (before March 1st) | Cornerstone LMS (Online) | Score ≥ 80% on final quiz |
| TR-PRV-019 | Children's Data Protection and VPC Process | Data Governance & Privacy Team, Engineering Leads for Clinical AI & HealthPay, HIM Team, Account Managers | **Annual** (Quarterly cohorts) | Instructor-led (Virtual) + LMS | Complete VPC simulation; score 100% on post-simulation quiz |
| TR-SEC-005 | HIPAA Security and Privacy for Pediatric PHI | All workforce members with access to PHI (including clinical, HIM, and HealthPay teams) | **Annual** (before May 1st) | Cornerstone LMS (Online) | Score ≥ 85% on final quiz |
| TR-ENG-012 | Secure Development: Pediatric Data Minimization | All software engineers and QA testers | **Annual** (within 30 days of hire, then annually) | Secure Code Warrior (Gamified) | Complete "Minor Data Lock" coding challenge |

**Training Tracking:** Completion of all training is tracked in Cornerstone LMS. Managers receive monthly compliance dashboards. Non-completion of required training by the deadline results in temporary suspension of access to systems processing children's data and constitutes a violation of Meridian policy, subject to progressive discipline per SOP-HR-008 (Employee Conduct and Discipline). Training records are retained for a minimum of six years.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Document Title | Relationship |
|---|---|---|
| SOP-DGP-001 | Meridian Data Privacy Policy | Overarching governance policy from which this SOP inherits authority. |
| SOP-PHI-005 | Protected Health Information (PHI) Handling and Access | Provides the general HIPAA handling procedures that are augmented by the pediatric-specific procedures in this document. |
| SOP-INF-001 | Information Security Policy | Defines the security controls mandated for "Critical" impact level systems, applicable to pediatric data. |
| SOP-IDM-003 | Identity and Access Management (IAM) Standards | Defines the Okta IAM standards for account types, including Guardian and Minor User Accounts. |
| SOP-HR-008 | Employee Conduct and Progressive Discipline | Governs the consequences of non-compliance with workforce training requirements. |
| SOP-EME-001 | Emergency Data Access ("Break-Glass") | Procedure invoked for emergency clinical access to minor data without prior consent. |
| IRP-001 | Cybersecurity Incident Response Plan | Contains the playbook for a pediatric data breach. |

### 10.2 External Regulations and Standards

- **General Data Protection Regulation (GDPR) (EU) 2016/679:** Specifically Article 8, which governs the conditions applicable to a child's consent in relation to information society services.
- **Health Insurance Portability and Accountability Act (HIPAA) of 1996, as amended by the HITECH Act:** Specifically 45 CFR § 160 and § 164 (the Privacy and Security Rules) as they relate to the rights of minors and personal representatives.
- **Children's Online Privacy Protection Act (COPPA) of 1998:** 15 U.S.C. §§ 6501–6506, and the FTC's COPPA Rule, 16 CFR Part 312, governing the online collection of personal information from children under 13.
- **NIST Special Publication 800-53, Revision 5:** Applied to security and privacy controls for the VPC Consent Ledger system and Minor User Account management.

---

## 11. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 0.1 | 2024-03-10 | J. Chen, Privacy Analyst | Initial draft created for DPO and Legal review. |
| 0.2 | 2024-04-02 | Dr. K. Weber, CPO | Incorporated legal feedback. Added detailed VPC process flow and COPPA supplementary procedures. Expanded Roles matrix. |
| 0.3 | 2024-04-18 | T. Osei, CISO | Reviewed and added specific technical controls (MDL, COPPA flag, DLP rules) to Section 6. Adjusted incident response thresholds. |
| 0.4 | 2024-04-28 | M. Gonzalez, General Counsel | Final legal and regulatory review. Approved language for consent forms and notifications. |
| 1.0 | 2024-05-05 | Dr. K. Weber, CPO | Final version approved by General Counsel. Effective date set. Published to PolicyTech corporate repository. |
| 1.1 | 2025-02-05 | L. Patel, Sr. Privacy Manager | Scheduled review. Updated jurisdictional Age of Consent Matrix link to version 3.0. Clarified the annual BAA review expectation. No procedural changes required. |