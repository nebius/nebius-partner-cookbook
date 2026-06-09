---
sop_id: "SOP-HR-002"
title: "Background Check and Screening"
business_unit: "Human Resources"
version: "3.0"
effective_date: "2025-01-12"
last_reviewed: "2026-08-20"
next_review: "2027-02-24"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Background Check and Screening

## 1. Purpose and Scope

### 1.1 Purpose
The purpose of this Standard Operating Procedure (SOP) is to define the standardized, global framework for conducting pre-employment and ongoing background checks and screenings at Meridian Health Technologies, Inc. This SOP establishes the operational controls, regulatory compliance mandates, and risk mitigation strategies necessary to ensure the safety, security, and integrity of Meridian's workforce, patients, proprietary data, and regulated technologies. It operationalizes Meridian’s commitment to the **SOC 2 Type II** Common Criteria, specifically the security and confidentiality trust service categories, and aligns with **NIST AI RMF** Govern and Manage functions for workforce vetting.

### 1.2 Scope
This SOP applies to all individuals formally engaged by Meridian Health Technologies, Inc., including full-time employees, part-time employees, temporary workers, contractors, consultants, and interns (collectively "Candidates" or "Workforce Members"). Its scope extends across all global offices and remote work arrangements.

The screening requirements are tiered based on role-based risk, specifically:
- **Standard Access Roles:** Positions with standard access to Meridian's enterprise systems (email, general internal tools).
- **Privileged Access Roles:** Positions with administrative access to production cloud environments (AWS, Azure), CI/CD pipelines, financial systems processing transactions under **SR 11-7**, or protected databases.
- **Regulated Function Roles:** Positions with direct access to Protected Health Information (PHI) under **HIPAA**, personal data of EU data subjects under **GDPR**, or roles directly involved in the development, deployment, or quality assurance of high-risk AI systems under the **EU AI Act**.

This SOP covers the entire screening lifecycle: initiation, data collection, analysis, adjudication, adverse action, ongoing monitoring, and record disposition.

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **Adjudication** | The formal, documented process of evaluating background check results against Meridian's pre-defined eligibility criteria to determine a candidate's suitability for employment or continued engagement. |
| **Adverse Action** | A formal decision to withdraw an offer of employment, terminate an existing Workforce Member, or reassign a Workforce Member to a role with reduced access due to failed screening results. |
| **Applicant Tracking System (ATS)** | The Meridian system of record for the recruiting and hiring lifecycle, currently **Greenhouse**. |
| **Background Screening Vendor (BSV)** | The accredited, contracted third-party provider authorized to conduct background checks, currently **HireRight, LLC**. Checks for EU candidates are sub-processed through **HireRight's EU-approved affiliate**. |
| **Disclosure and Authorization Form** | The standalone legal document, distinct from the employment application, that informs a Candidate a background check will occur and obtains their explicit authorization. |
| **EU AI Act** | Regulation (EU) 2024/1689. Meridian's clinical diagnostic imaging products are classified as high-risk AI systems, requiring rigorous personnel vetting for all development and quality assurance roles. |
| **Fully Reconciled Report** | A BSV report meeting Meridian's SOC 2 control evidence requirements: uniquely identified, verified against Candidate-provided identifiers, and marked as complete with all data sources accounted for. |
| **GDPR** | General Data Protection Regulation (Regulation (EU) 2016/679). This regulation applies to all screening activities involving EU data subjects, mandating specific legal bases, transparency, and data minimization requirements. |
| **HRIS** | Human Resources Information System; Meridian's system of record for all employee data, currently **Workday**. |
| **Pre-Adverse Action Notice** | A written notification sent to a Candidate before a final adverse decision is made, containing a copy of the background check report and a summary of their rights under applicable law. |
| **Protected Health Information (PHI)** | Individually identifiable health information held or transmitted by Meridian's clinical AI products or services. |
| **SOC 2 TSC** | Trust Services Criteria for Security, Availability, and Confidentiality as defined by **AICPA TSP Section 100**.

## 3. Roles and Responsibilities

A RACI matrix defines the accountability for the core sub-processes of this SOP.

| Process Step / Task | Candidate | Recruiter | HR Operations (HR Ops) | Security Engineering | Legal & Compliance | Hiring Manager |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Policy Governance & Exception Approval** | I | I | C | C | **A/R** | I |
| **Role Tier Determination** | I | R | **A** | C | C | I |
| **Disclosure & Authorization** | **R** | **A** | C | I | I | I |
| **Initiating the BSV Process** | C | I | **A/R** | I | I | I |
| **GDPR Art. 13/14 Notice Delivery** | I | I | **A** | I | R | I |
| **SOC 2 Vendor Due Diligence (BSV)** | I | I | C | C | **A/R** | I |
| **Criminal Adjudication** | I | C | R | C | **A** | I |
| **Compliance Adjudication (OIG/GSA)** | I | I | R | I | **A** | I |
| **Final Employment Suitability Decision** | I | I | I | I | C | **A/R** |
| **Adverse Action Process Execution** | **I** | I | R | I | **A** | I |
| **Continuous Monitoring** | I | I | R | I | **A** | I |
| **Record Disposition & Deletion** | I | C | **R** | I | A | I |

**Responsible (R):** The role performing the work.
**Accountable (A):** The role ultimately answerable for the correct and thorough completion, including sign-off authority.
**Consulted (C):** Roles whose input is required.
**Informed (I):** Roles kept informed of progress and outcomes.

**Key Named Roles:**
- **Policy Exception Approver:** For exceptions to any check type, the approval chain is the Chief Human Resources Officer (CHRO) and the General Counsel.
- **SOC 2 Control Owner:** The Director of HR Operations is the control owner for SOC 2 control activity `HR-CC1.2`, "Background Verification of Personnel," and is responsible for quarterly evidence collection.
- **Data Protection Officer (DPO) Liaison:** The VP, Legal - Privacy is the internal liaison for all Data Protection Authority (DPA) queries.

## 4. Policy Statements

Meridian Health Technologies is committed to the following high-level policies governing background screening:

- **Zero Trust Alignment:** Hiring and engagement processes will verify all identity claims and trust signals before granting access to Meridian assets. No individual is exempt from the screening requirements of their designated role tier.
- **Global Consistency with Local Adaptation:** Meridian will maintain a globally consistent adjudication framework based on risk, while strictly adhering to the local data privacy and labor laws of the jurisdictions in which we operate.
- **Proportionality:** Screening requirements are tiered to be proportionate to the risk associated with the role. Roles with access to safety-critical, financial, or highly sensitive personal data will undergo enhanced vetting.
- **Transparency:** All Candidates will be provided with clear, conspicuous, and upfront notice regarding the scope and purpose of all screening activities before they occur, in accordance with the **SOC 2 CC2.2** criterion.
- **Privacy-by-Design:** Background screening processes are designed to collect the minimum personal data necessary to assess the identified risk.
- **Non-Discrimination:** Adjudication decisions will be based solely on the pre-defined, risk-based criteria outlined in this SOP. Factors such as race, religion, national origin, gender, sexual orientation, age, or disability shall play no role in adjudication.

## 5. Detailed Procedures

This section comprises the operational procedures for the background check lifecycle.

### 5.1 Tier Determination and Requisition Coding
The process begins at the job requisition stage.
1.  **HR Business Partner (HRBP):** Upon receiving a new role request, the HRBP consults with the Hiring Manager to determine the specific access requirements.
2.  **Role Tier Assignment:** The HRBP assigns one of three Role Tiers in the ATS (Greenhouse) based on the access profile:
    - **Tier 1 (Standard):** No access to PHI, production environments, or financial systems (e.g., general marketing roles).
    - **Tier 2 (Privileged):** Administrative access to AWS, CI/CD tools, or systems processing credit card transactions. Read access to PHI.
    - **Tier 3 (Regulated):** Unrestricted write/move access to PHI, deployment authority for high-risk AI medical devices, or access to source code repositories for regulated products.
3.  **System-of-Record Coding:** The Greenhouse requisition is coded with the Tier designation. This code triggers the appropriate screening package in the integration between Greenhouse and the Background Screening Vendor (BSV), HireRight.

### 5.2 Authorization and Notice
No background check will be initiated before a Candidate receives and acknowledges a legally compliant authorization.
1.  **Disclosure:** Upon offer acceptance, the Recruier triggers an automated task in Greenhouse. This sends the Candidate a standalone, plain-language **Disclosure and Authorization Form**. This form details:
    - The categories of information to be collected (criminal history, education, employment, professional credentials/licensing, driving record [if applicable], and credit history [for specific regulated financial roles only]).
    - The purpose of the collection (making a suitability determination).
    - The legal basis for processing. For US roles, this is a permissible purpose under the Fair Credit Reporting Act (FCRA). For EU roles, the specific Article 6(1)(b) (necessity to enter contract) and Article 9(2)(b) conditions for special category data, as processed by the BSV, are stated.
    - A **GDPR-Specific Notice** (Tier 3, EU Residents): A supplemental notice is provided detailing the data controller (Meridian), the data processor (HireRight EU Affiliate), the specific categories of personal data processed, and a summary of data subject rights (access, rectification, erasure) with instructions on how to exercise them via email to `dataprotection@meridiantech.com`. This document also clarifies the retention periods for screening data.
2.  **Candidate Acknowledgment:** The Candidate must electronically sign the Disclosure and Authorization Form within the Greenhouse portal. This constitutes explicit, informed consent. A copy is automatically archived to the Candidate’s secure profile.

### 5.3 Check Execution and Types
Upon authorization, the BSV process is automatically initiated.

| Screening Component | Tier 1 (Standard) | Tier 2 (Privileged) | Tier 3 (Regulated) | Search Scope & Notes |
| :--- | :---: | :---: | :---: | :--- |
| **ID Verification & Trace** | Mandatory | Mandatory | Mandatory | Validates SSN/Tax ID against credit bureau header data. Validates residency history. |
| **Criminal Background Check** | 7-Year County (Primary) | 7-Year Federal & County | **Global Sanctions, 7-Year Federal, County, & Int'l (if applicable)** | Tier 3 requires a global sanctions and watchlist search (e.g., OFAC, EU Consolidated Sanctions List) and a check in any non-US jurisdiction of prior residency beyond 6 months. |
| **Employment Verification** | Last 3 employers | Last 7 years | Last 10 years | Gaps exceeding 30 days are flagged. |
| **Education Verification** | Highest Degree | All post-secondary | All degrees and certifications | Professional licensure (e.g., Medical Physics, Radiology) is verified against issuing bodies. |
| **Healthcare Sanctions Check** | OIG/GSA Exclusions | OIG/GSA Exclusions | OIG/GSA, State Med. Boards, FDA Debarment | Mandatory for any role with potential access to clinical data or products. |
| **Credit Report** | N/A | For Finance roles only | For specific C-suite or fiduciary roles | Performed strictly where credit history is a bona fide occupational necessity. |
| **MVR (Motor Vehicle Report)** | N/A | Where driving is essential | Where driving is essential | Essential function must be documented in job description. |

### 5.4 Adjudication Procedure
The HR Operations (HR Ops) team is responsible for the formal adjudication process.
1.  **Report Receipt:** HR Ops receives a Fully Reconciled Report from the BSV directly into the case management module of Workday.
2.  **Initial Review:** An HR Ops Coordinator reviews the report for completeness and potential flags using the Adjudication Criteria Matrix below. The goal is to confirm the record meets Meridian's predetermined standards, not to conduct an open-ended ethical review.
3.  **Adjudication Criteria Matrix:**

| Category | Standard Adjudication Criteria (All Tiers) | Tier 3 Enhanced Criteria |
| :--- | :--- | :--- |
| **Criminal History** | **Automatic Disqualification (5 years):** Felony convictions for violence, sexual assault, robbery, or arson.<br>**Review & Evaluation (5 years):** Felony theft, fraud, forgery, or cybercrimes evaluated against role duties. Misdemeanor convictions reviewed over a 3-year period. | **Zero Tolerance (Lifetime):** Any conviction for fraud, theft, or breach of fiduciary duty. All felonies (regardless of time) require review by General Counsel. |
| **Employment/Education** | Minor discrepancies (dates +/- 6 months) documented. Pattern of fabrication or material omission results in denial. | All discrepancies, regardless of materiality, require a formal "Letter of Clarification and Response" from the Senior Director of HR and VP, Quality & Regulatory. |
| **Sanctions Watchlist** | Match on OFAC SDN List or EU Consolidated Sanctions List is an automatic, non-negotiable disqualification and immediate legal escalation. | Match on any OIG, GSA, FDA Debarment, or State Licensing Board exclusion list is an automatic disqualification for clinical, development, and QA roles. |

4.  **Final Determination:** For a "Clear" or "Low-Risk Discrepancy" report, the HR Ops Coordinator marks the case as `Approved - Cleared for Hire` in Workday.
5.  **Escalation for Review:** For any discrepancy falling into the "Review & Evaluation" category, the HR Ops Coordinator prepares a non-judgmental case summary, redacting any prohibited information (e.g., arrests not leading to conviction). The case is escalated to the **Adjudication Committee**, a standing body comprised of:
    - Director, HR Operations
    - Director, Corporate Security
    - Associate General Counsel, Employment Law
6.  The Adjudication Committee conducts an individualized assessment evaluating the nature and gravity of the event, the time passed, and the nature of the job sought. The Committee's decision is documented on the `HR-002-Adjudication Review Form` and uploaded to the Workday case.

### 5.5 Adverse Action Procedure
If the Adjudication Committee’s pre-decision is to rescind an offer or reassign/terminate a Workforce Member based on the background check, the following Adverse Action process is strictly followed.
1.  **Pre-Adverse Action Notice:** HR Ops sends the Candidate a comprehensive Pre-Adverse Action packet via secure email link and trackable courier to their last known address. The packet includes:
    - A copy of the Complete Background Check Report.
    - A copy of “A Summary of Your Rights Under the Fair Credit Reporting Act.”
    - A letter stating the intent to take adverse action and identifying the specific disqualifying report items (the "Adverse Factors").
    - A waiting period of at minimum ten (10) business days is provided from the confirmed delivery of the notice for the Candidate to respond and dispute the completeness or accuracy of the report with the BSV.
2.  **Dispute and Investigation:** If the Candidate provides direct evidence that a report item is factually incorrect, HR Ops places the adjudication on hold and immediately instructs the BSV to reinvestigate. The BSV must complete this reinvestigation and report back to Meridian within seven (7) business days.
3.  **Final Adverse Action Notice:** If no successful dispute is made, or upon confirmation of accuracy after reinvestigation, HR Ops sends a "Final Adverse Action Notice." This letter reiterates:
    - The final decision.
    - The specific disqualifying information and its source (the BSV).
    - A statement that the BSV did not make the decision and cannot explain its nature.
    - A notice of the Candidate’s ongoing right to obtain a free copy of their report from the BSV within sixty (60) days.
4.  **Record Retention:** The entire Adverse Action record, including all notices, correspondence, and the Adjudication Committee's rationale, is retained for seven (7) years from the date of the final decision, in accordance with Meridian's Record Retention Schedule (REF-HR-001).

### 6.2 Administrative Controls
- **Annual BSV Audit:** Meridian’s Vendor Risk Management team shall conduct an annual audit of HireRight to verify its compliance with SOC 2 TSC, Meridian’s MSA, and the GDPR Controller-Processor clauses. This audit reviews HireRight’s own SOC 2 Type II report for its consumer reporting platform.
- **Segregation of Duties:** The Recruiter role cannot access the raw BSV report. Only the HR Ops and Legal & Compliance teams have permission to view and adjudicate the detailed criminal history components, creating a logical segregation from the hiring decision-maker.
- **Minimum Necessary Access:** Access to Workday cases containing background check reports is restricted to the HR Operations - Background Screening Specialists, the Legal - Employment Law group, and the General Counsel. Hiring Managers only receive a binary notification (`Eligible` or `Not Eligible`) with the `Not Eligible` status accompanied by a notice to contact HR Ops for a regulatory notification (e.g., Section 5.5 Step 1 action).

## 6. Controls and Safeguards

In alignment with SOC 2 TSC **(CC6.1 Logical and Physical Access Controls)** and **(P6.7 Retention of Personal Information)**, the following specific technical and administrative controls are implemented:

### 6.1 Technical Controls
- **ATS-to-BSV Integration (API Gateway):** The workflow trigger from Greenhouse to HireRight is mediated through a secured, authenticated REST API (Application Programming Interface). We employ mutual Transport Layer Security (mTLS), ensuring bi-directional certificate-based authentication between Meridian’s VPC and HireRight’s platform. This control, mapped to **SOC 2 A1.2**, ensures only the authorized service principal can initiate a screening request.
- **Data Encryption:** BSV report data, stored as a structured document in the Candidate’s Workday profile, is encrypted at rest using AWS Key Management Service (KMS) with a Customer Managed Key (CMK). Annual key rotation is automated. Data in transit is always encrypted via TLS 1.2 or higher.
- **System-of-Record Access Control (RBAC):** Access to the "Background Check & Adverse Action" business object in Workday is governed by the following least-privilege security groups:

| Security Group | Workday Domain Access | Permissions |
| :--- | :--- | :--- |
| **HR_Ops_BSV_Specialist** | `Worker Data: Background Check` | `Get` and `Put` permission on screening results. `View` permission on the full `Background Check Report` sub-object. |
| **Legal_Employment_Counsel** | `Worker Data: Background Check` | `View`-only permission on the full `Background Check Report` sub-object. No modification rights. |
| **Recruiter_Standard** | `Candidate Data: Basic` | `View` permission on the top-level adjudication status field (`Clear`, `Review Required`, `Not Eligible`). Explicitly denied access to the report sub-object. |

### 6.2 Data Minimization and Retention
- **Targeted Screening:** The BSV integration is designed with "Check Types by Role Tier" logic, programmatically enforcing that only the authorized screening components per Table 5.3 are requested. For instance, the credit report API call is disabled by default for Tier 1 profiles.
- **Deletion Schedule:** A control to govern the lifecycle of personal data is enforced. All raw background check reports and associated adjudication notes are purged from the Workday system according to a specific deletion policy, unless subject to a legal hold. For a successful hire, the raw BSV report (`Background Check Report` object) is automatically purged three (3) years from the date of first employment. Only the adjudication metadata (final status, date, verifier) persists for the term of employment plus seven years.
- **Data Privacy by Design:** The system architecture is configured such that the Hiring Manager dashboard displays only a `Screening: In Progress / Complete` status indicator. No substantive or derogatory data is visible.

## 7. Monitoring, Metrics, and Reporting

To demonstrate control effectiveness for **SOC 2 CC4.1 (Monitoring of Controls)**, CHRO Jennifer Walsh and the GRC team monitor the following KPIs on a monthly cadence via an automated ServiceNow Performance Analytics dashboard.

| Metric (KPI) | Target | SOC 2 Control Mapping | Calculation Method | Reporting Cadence |
| :--- | :---: | :--- | :--- | :--- |
| **Cycle Time: Authorization to Adjudication** | ≤ 5 business days for 95% of completions | A1.2 (Processing Timeliness) | Timestamp(`Authorization Signed`) to Timestamp(`Final Adjudication Status Set`). Excludes Candidate disputes. | Monthly |
| **Adverse Action Compliance Rate** | 100% | C1.1 (Policy Adherence) | (# of Pre-Adverse Actions with confirmed delivery + wait period observed) / (Total # of final adverse actions). | Monthly, Quarterly SOC 2 Evidence |
| **Candidate Satisfaction Score (Post-Screening)** | ≥ 4.0 out of 5.0 | P9.1 (Customer Commitments) | Automated Qualtrics survey sent 1 day after final notification. Measures clarity of communication and professionalism. | Monthly |
| **Vendor Compliance (HireRight SLA)** | 99.5% Uptime & On-time reports | D3.2 (Vendor Performance) | Automated monitoring of HireRight API SLA reports against contractual obligation. | Quarterly |
| **Disposition Timeliness for Data Requests** | 80% acknowledged within 5 business days | GDPR Art. 12 | Number of formal data subject access or deletion requests related to screening data acknowledged within five days / total number of screening-related DSARs. | Monthly |

**Reporting Cadence:**
- **Monthly:** Operational KPIs are reviewed by the Director, HR Operations and the VP, Legal - Privacy.
- **Quarterly:** A formal SOC 2 Controls Evidence Package is compiled by the GRC Analyst, including the KPI dashboard screenshots, audit of exception records, and a sample of ten successfully adjudicated cases showing adherence to the Segregation of Duties control. This package is presented to the CISO for review before external auditor consumption.

## 8. Exception Handling and Escalation

### 8.1 Policy Exceptions
Deviations from this SOP are permitted only under extraordinary circumstances and require a formal, documented exception.
1.  **Request:** The Hiring Manager or HRBP submits a "Background Screening Exception Request" through the ServiceNow GRC portal. The request must include a compelling business justification, the specific procedure step to be excepted, and a risk mitigation plan for the duration of the exception.
2.  **Risk Assessment:** The Director, Corporate Security conducts a risk assessment and documents the potential vulnerability introduced by the exception (e.g., permitting a Tier 3 hire to start with a limited access profile pending the international criminal check).
3.  **Approval Matrix:**

| Exception Type | Required Approval Level | Max Duration |
| :--- | :--- | :---: |
| Delay in Check Completion (e.g., Int'l jurisdiction delay) | Chief Information Security Officer (CISO) & CHRO | 30 calendar days |
| Waiver of a Tier 2 or 3 Check Component | General Counsel & CISO | Not Renewable |
| Waiver for CEO or Board-Level Candidate | Meridian Board of Directors, Audit Committee Chair | One-time, defined |

All approved exceptions are tracked in the centralized GRC tool. Upon expiration, the mitigation is terminated, and the standard procedure is enforced. If the exception was temporary, full compliance is verified by Security Engineering before the "clear for hire" status is fully provisioned.

### 8.2 Incident Escalation
Any Personnel member who becomes aware of a potential compromise or bypass of the screening process (e.g., an offer letter extended without a completed check, a hiring manager accessing a raw report) must immediately report the incident via the `soc-incident@meridiantech.com` hotline. This triggers the Security Incident Response Plan (SOP-SEC-004), classifying it as a “Privacy and Employment Control Failure” with a severity of P2 (High) and requiring a root cause analysis within 72 hours. Access breach notifications will be coordinated with stakeholders according to our internal breach notification plan.

## 9. Training Requirements

Effective implementation of this SOP requires documented and verified training. All roles with responsibilities defined in Section 3 must complete the following mandatory training.

| Training Module | Audience | Delivery Method | Frequency | Assessment |
| :--- | :--- | :--- | :--- | :--- |
| **SOP-HR-002-OVW: Policy Overview & Roles** | All Recruiters, HRBPs, HR Ops, Hiring Managers | Computer-Based Training (CBT), Meridian LMS | Annually, and on policy version change ≥ 0.5 | 10-question knowledge check, 100% pass required. |
| **SOP-HR-002-ADJ: Adjudication & Adverse Action** | HR Ops - Background Screening Specialists, Legal - Employment Counsel | Instructor-Led Workshop (4 hours) | Biennially | Simulated adjudication case; scored rubric (≥ 90%). |
| **SOC 2 Evidence Collection for HR Controls** | Director, HR Operations, GRC Manager | Peer-led walkthrough | Annually | Successful collection and upload of 1 quarter's evidence into the audit portal. |
| **GDPR & Candidate Privacy for Recruiters** | Recruiters, HR Ops for EMEA | Instructor-Led (by Legal-Privacy) | Annually | Hypothetical scenario exercise; remediation required for errors. |

Compliance records for all training are maintained in the Meridian Learning Management System (Cornerstone) and are monitored monthly by the HR Compliance team. Non-completion of mandatory training by the due date is an automatic trigger for disciplinary review and can lead to temporary suspension of access to the Greenhouse and Workday systems.

## 10. Related Policies and References

This SOP is one component of Meridian’s integrated policy and control environment. The following related internal and external documents provide essential context and complementary requirements.

### Internal Meridian Policies
- **SOP-HR-001:** Global Onboarding and Offboarding (Defines account provisioning tied to screening completion).
- **SOP-SEC-003:** Identity and Access Management (Defines RBAC for privileged access, tied to Tier 2 clearances).
- **SOP-SEC-004:** Security Incident Response Plan (Governs the response to any data breach involving screening data).
- **SOP-PRI-001:** Data Protection and Privacy Policy (Defines data subject rights handling procedures).
- **PL-HR-005:** Employee Disciplinary Action Policy (Covers falsification of application data discovered post-hire).

### External Standards and References
- **AICPA TSP Section 100:** 2017 Trust Services Criteria for Security, Availability, and Confidentiality (Specifically CC1.1, CC6.1, CC1.5, P6.7).
- **Regulation (EU) 2016/679:** General Data Protection Regulation (GDPR). Article 6 (Lawful Basis), Article 9 (Special Categories), Articles 13/14 (Transparency).
- **HIPAA Privacy Rule (45 CFR § 160 and Subparts A and E of Part 164):** Access control requirements and business associate vetting for roles with PHI access are addressed in the adjudication of OIG/GSA checks, but the review is focused on criminal history, not a separate minimum necessary access review for the screening data itself.
- **NIST SP 800-53 Rev. 5:** PS-3 (Personnel Screening), PS-2 (Position Risk Designation).

## 11. Revision History

| Version | Date | Author | Description of Change |
| :--- | :--- | :--- | :--- |
| 1.0 | 2022-03-15 | M. Evans, Dir. HR Ops | Initial document creation. Combined legacy US and UK screening procedures into a single global SOP. Established Tier 1-3 risk framework. |
| 1.5 | 2023-01-10 | J. Walsh, CHRO | Minor revision to incorporate feedback from first SOC 2 Type II audit. Added KPI dashboard details and clarified Segregation of Duties matrix (Section 6.1). |
| 2.0 | 2024-05-22 | L. Chen, Assoc. General Counsel | Major revision to integrate EU AI Act regulatory requirements into Tier 3 Regulated role adjudication criteria. Updated Adverse Action wait period to 10 business days. |
| 2.1 | 2024-11-01 | H. Rodriguez, GRC Manager | Minor revision to update BSV name from "Sterling" to "HireRight" after corporate change in vendor. Updated all related links and API endpoint references. |
| 3.0 | 2025-01-12 | J. Walsh, CHRO | Major revision, full policy rewrite. Strengthened SOC 2 controls for evidence collection, added detailed RBAC table for Workday, and redesigned GDPR-specific notices as a standalone workflow step in the ATS. |