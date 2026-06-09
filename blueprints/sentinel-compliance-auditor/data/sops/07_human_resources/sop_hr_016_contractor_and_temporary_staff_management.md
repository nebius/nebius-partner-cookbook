---
sop_id: "SOP-HR-016"
title: "Contractor and Temporary Staff Management"
business_unit: "Human Resources"
version: "5.1"
effective_date: "2024-09-17"
last_reviewed: "2025-06-27"
next_review: "2025-12-04"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# STANDARD OPERATING PROCEDURE: Contractor and Temporary Staff Management

**Document ID:** SOP-HR-016
**Business Unit:** Human Resources
**Version:** 5.1
**Effective Date:** 2024-09-17
**Last Reviewed:** 2025-06-27
**Next Review:** 2025-12-04
**Owner:** Jennifer Walsh, Chief Human Resources Officer
**Approver:** Dr. Sarah Chen, CEO
**Classification:** Internal
**Status:** Active

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the management of all Contingent Workers engaged by Meridian Health Technologies, Inc. ("Meridian" or the "Company"). The purpose of this document is to standardize the end-to-end lifecycle of non-permanent personnel—from requisition and onboarding through access management, performance oversight, and offboarding—ensuring that all engagements align with Meridian’s regulatory obligations, information security posture, and contractual commitments.

This SOP defines the controls necessary to protect Meridian’s intellectual property, safeguard Protected Health Information (PHI) and Personally Identifiable Information (PII), maintain compliance with the Health Insurance Portability and Accountability Act (HIPAA), the General Data Protection Regulation (GDPR), and SOC 2 Trust Services Criteria, and uphold the integrity of Meridian’s AI systems, financial services platforms, and SaaS infrastructure.

### 1.2 Scope

This SOP applies to all Contingent Workers providing services to or on behalf of Meridian Health Technologies, Inc., regardless of geographic location, engagement mechanism, or funding source. The scope specifically includes:

| Category | Definition | Applicable Products/Systems |
|---|---|---|
| Independent Contractors (1099-NEC) | Self-employed individuals engaged under a direct contract | Clinical AI Platform, HealthPay, MedInsight, SaaS Platform |
| Agency Contractors (W-2 to Agency) | Personnel supplied through a third-party staffing agency | All business lines and corporate functions |
| Temporary Employees | Short-duration W-2 employees engaged directly by Meridian | Typically corporate operations; limited access scenarios |
| Consultants and Advisory Contractors | Specialized subject-matter experts engaged for defined deliverables | AI governance, regulatory affairs, financial modeling |
| Vendor-Resident Contractors | Contractor personnel embedded within vendor services (e.g., managed services) | AWS support, Snowflake professional services, CrowdStrike Falcon Complete |
| Interns and Co-op Students (Contract-Based) | Academic program participants engaged via contract rather than direct hire | Engineering, Clinical AI, Data Science |
| Offshore/Nearshore Contractors | Contingent Workers operating from Meridian global offices or remote international locations | London, Berlin, Singapore, Toronto offices |

**Out of Scope:** This SOP does not apply to full-time, regular employees (see SOP-HR-001: Employee Lifecycle Management) or to third-party vendor organizations acting as separate legal entities with no embedded personnel in Meridian environments (see SOP-PROC-008: Third-Party Vendor Risk Management). Board members and Scientific Advisory Board members are governed by SOP-LEG-003: Board and Advisor Governance.

### 1.3 Geographic and Jurisdictional Applicability

This SOP applies globally. Where local labor laws, data protection regulations, or tax requirements in jurisdictions including Massachusetts, the United Kingdom, Germany, Singapore, or the Province of Ontario impose stricter requirements than those described herein, the local requirements shall prevail. The Chief Human Resources Officer and General Counsel shall jointly determine the applicable standard on a case-by-case basis.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Contingent Worker** | Any individual performing services for Meridian who is not classified as a regular full-time or part-time employee. This includes all categories enumerated in Section 1.2. |
| **Engagement Manager** | The Meridian full-time employee (typically at Director level or above) who initiates and manages the Contingent Worker relationship, serves as the primary point of accountability, and approves timesheets and deliverables. |
| **Hiring Manager** | Synonym for Engagement Manager; the operational manager responsible for day-to-day task direction. |
| **Contingent Worker File** | The centralized record maintained in Workday containing all documentation related to a Contingent Worker engagement, including contract, NDA, background check results, access request forms, and offboarding confirmation. |
| **Protected Health Information (PHI)** | Individually identifiable health information held or transmitted by Meridian in any form, as defined by HIPAA at 45 CFR § 160.103. |
| **Electronic Protected Health Information (ePHI)** | PHI that is created, stored, transmitted, or received electronically. |
| **Personally Identifiable Information (PII)** | Any information relating to an identified or identifiable natural person, consistent with GDPR Article 4(1). |
| **Principle of Least Privilege** | The information security principle that a user should be granted only the minimum access permissions necessary to perform their authorized job functions. |
| **Non-Disclosure Agreement (NDA)** | The Proprietary Information and Inventions Assignment Agreement or equivalent confidentiality instrument executed by the Contingent Worker prior to any access to Meridian systems or facilities. |
| **Right-to-Know / Right-to-Work** | Statutory verifications of identity, employment eligibility, and (where applicable) criminal background, credit history, and professional sanctions screening. |
| **Logical Access Control** | The use of authentication and authorization mechanisms within Meridian’s technology stack to enforce access policies for systems, applications, and data. |
| **Segregation of Duties (SoD)** | The control design principle that no single individual should have the ability to both initiate and approve a high-risk transaction or access combination without independent oversight. |

### 2.2 Acronyms

| Acronym | Meaning |
|---|---|
| BAA | Business Associate Agreement |
| BGC | Background Check |
| CHRO | Chief Human Resources Officer |
| CISO | Chief Information Security Officer |
| DPO | Data Protection Officer |
| EOR | Employer of Record |
| HRIS | Human Resources Information System (Workday) |
| IAM | Identity and Access Management |
| IdP | Identity Provider (Okta) |
| KBA | Knowledge-Based Authentication |
| LMS | Learning Management System (Workday Learning) |
| MFA | Multi-Factor Authentication |
| MSOW | Master Statement of Work |
| NDA | Non-Disclosure Agreement |
| RBAC | Role-Based Access Control |
| SAML | Security Assertion Markup Language |
| SoW | Statement of Work |
| SOC 2 | System and Organization Controls 2 |
| TPS | Third-Party Supplier |
| UAR | User Access Review |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

| Activity / Decision | CHRO | Engagement Manager | CISO / InfoSec | Procurement | Legal / GC | DPO | Compliance Officer |
|---|---|---|---|---|---|---|---|
| **Requisition & Budget Approval** | A | R | — | C | — | — | — |
| **Worker Classification Determination** | A | C | — | R | R | — | — |
| **NDA Execution** | — | R | — | C | A | — | — |
| **BAA Execution (if PHI Access)** | — | R | — | — | A | — | C |
| **Background Check Initiation** | I | R | — | — | — | — | — |
| **Background Check Adjudication** | A | — | — | — | C | — | I |
| **Access Request & Provisioning** | — | R | A | — | — | — | — |
| **GDPR Privacy Notice Distribution** | — | — | — | — | C | R/A | — |
| **Security Training Assignment** | I | R | A | — | — | — | C |
| **Physical Access Badge Issuance** | — | R | A | — | — | — | — |
| **Timesheet & Deliverable Approval** | — | A/R | — | — | — | — | — |
| **Performance Issue Escalation** | I | R | I | — | C | — | — |
| **Access Revocation (Offboarding)** | I | R | A/R | — | — | — | I |
| **Records Retention** | A | R | — | — | — | — | I |

**Key:** R = Responsible (does the work), A = Accountable (signs off), C = Consulted (two-way input), I = Informed (one-way notification)

### 3.2 Named Role Responsibilities

**Chief Human Resources Officer (CHRO) – Jennifer Walsh**
- Serves as the process owner for this SOP.
- Adjudicates escalated worker classification disputes.
- Approves exceptions to standard BGC requirements beyond Engagement Manager authority.
- Reviews and acts on Contingent Workforce quarterly metrics.

**Engagement Manager (varies by department)**
- Initiates requisition request in Workday via the "Create Contingent Worker Requisition" business process.
- Ensures all pre-engagement documentation is completed prior to the worker's start date.
- Submits Access Request Form (SOP-HR-016-F002) on behalf of the Contingent Worker.
- Conducts monthly review of worker access and confirms continued need.
- Initiates offboarding notification no fewer than five (5) business days prior to engagement end.

**Chief Information Security Officer (CISO) – Rachel Kim**
- Defines role-based access profiles for Contingent Workers within the IAM framework.
- Reviews and approves access requests involving ePHI, credit scoring models, or AI training pipelines.
- Monitors anomalous access patterns by Contingent Worker accounts and alerts Engagement Manager.
- Manages the technical execution of access provisioning and deprovisioning through Okta and downstream system integrations.

**Data Protection Officer (DPO) – Berlin Office (Dr. Klaus Meissner)**
- Reviews Contingent Worker engagements that will process personal data of EU data subjects.
- Ensures appropriate GDPR Article 28 (Processor) contractual clauses are in place for EU-based contractors.
- Maintains the Register of Processing Activities (ROPA) records for Contingent Worker access patterns.

**Procurement (Vendor Management Team)**
- Negotiates Master Services Agreements and Statements of Work with staffing agencies.
- Maintains the Approved Contingent Worker Supplier List.
- Audits agency compliance with insurance, labor classification, and invoicing requirements.

**Compliance Officer**
- Monitors adherence to mandatory training completion for Contingent Workers.
- Investigates and documents incidents involving Contingent Worker access violations.
- Conducts quarterly reviews of Contingent Worker access controls and reports findings to CHRO and CISO.

---

## 4. Policy Statements

### 4.1 Worker Classification

Meridian Health Technologies is committed to the accurate and defensible classification of all personnel. Contingent Workers shall be classified according to IRS common law rules (IRS Publication 15-A), applicable state law (Massachusetts M.G.L. c. 149, § 148B), and international labor standards for workers operating in Meridian’s global offices. No Contingent Worker shall be treated as a de facto employee with respect to control over work hours, methods, or tools unless the engagement is restructured as an employment relationship.

### 4.2 Confidentiality and Intellectual Property

No Contingent Worker shall access any Meridian system, network, facility, or data set without first executing an NDA. The NDA shall include explicit assignment of intellectual property rights to Meridian for all work product created during the engagement. The standard template (SOP-HR-016-T001: Contingent Worker NDA) shall be used without modification unless approved by Legal.

### 4.3 Mandatory Background Verification

All Contingent Workers must undergo and pass a BGC prior to any access to Meridian systems or facilities. Badge issuance and IAM provisioning are conditionally blocked until the BGC is adjudicated as "Clear." No exceptions.

### 4.4 Access Control: Principle of Least Privilege

Contingent Workers shall be granted the minimum access permissions required to fulfill their contracted Statement of Work. Access shall be provisioned via role-based groups in Okta, tied explicitly to documented job functions. Access to systems containing ePHI, financial data subject to SOC 2 controls, or AI model training datasets requires enhanced approval, as defined in Section 6.

### 4.5 HIPAA Business Associate Obligations

Any Contingent Worker whose contracted duties involve the creation, receipt, maintenance, or transmission of PHI on behalf of a Meridian Covered Entity component must be engaged under the umbrella of a fully executed Business Associate Agreement (BAA). If the Contingent Worker is an independent contractor, the BAA is executed directly between Meridian and the individual. If engaged via an agency, the BAA is executed with the agency, and the individual Contingent Worker is named as an authorized subcontractor under the BAA.

### 4.6 Secure Offboarding

Access for Contingent Workers shall be revoked within four (4) hours of the termination event (contract end, early termination, or security incident). This is a critical SOC 2 Security control. The Engagement Manager shall schedule offboarding tasks to align with this SLA.

### 4.7 GDPR Data Subject Transparency

Contingent Workers whose personal data is processed by Meridian are entitled to a privacy notice at the point of data collection. Meridian will provide a contractor privacy notice to all Contingent Workers at the time of onboarding. This notice will describe the categories of personal data collected, the purposes of processing, and the legal basis for processing. Retention of Contractor personal data shall align with the corporate data retention schedule.

### 4.8 Equal Opportunity and Non-Discrimination

Meridian applies its Equal Employment Opportunity and Anti-Harassment policies to all Contingent Workers. Any reported violation will be investigated by Human Resources and escalated to the supplier agency where applicable.

---

## 5. Detailed Procedures

### 5.1 The Requisition and Pre-Engagement Process

This procedure applies whenever a Meridian department identifies a need to engage a Contingent Worker.

#### 5.1.1 Requisition Initiation

| Step | Actor | Action | System/Tool |
|---|---|---|---|
| 1 | Engagement Manager | Logs into Workday and navigates to the "Create Contingent Worker Requisition" task. | Workday |
| 2 | Engagement Manager | Completes all required fields: job title, estimated start date, estimated end date (max 12 months for initial term), hours per week, physical location (office, remote, hybrid), business justification narrative (minimum 150 characters), budget code, and funding source. | Workday |
| 3 | Engagement Manager | Indicates whether the worker will interact with PHI, ePHI, PII of EU residents, Meridian financial systems, Clinical AI/ML training pipelines, or any system in scope for Sarbanes-Oxley (SOX) or MDR compliance. This classification dictates subsequent controls. | Workday Requisition Form |
| 4 | Engagement Manager | Selects the source: "Individual Contractor" (direct), "Agency - Approved Supplier" (from pre-vetted list), or "Agency - New Supplier" (triggers Procurement vetting). | Workday Requisition |
| 5 | Engagement Manager (Cost Center Owner) | Approves the budget allocation within Workday. If the total contract value exceeds $50,000 USD, VP-level approval is automatically routed by the system. | Workday Adaptive Planning |

#### 5.1.2 Early Worker Classification Review

Before the requisition is posted or an individual is identified, HR and Legal jointly review the role description for misclassification risk.

- **Test Applied:** Meridian uses the "ABC Test" for Massachusetts engagements and analogous tests for international offices. Key questions: Is the worker free from Meridian's direction and control to a degree that defines a true independent contractor relationship? Is the service performed outside the usual course of Meridian's business? Is the worker customarily engaged in an independent trade?
- **Outcome:** A classification memo is generated within Workday and attached to the requisition, containing the legal rationale for "Contractor" vs. "Temporary Employee" status. The CHRO reviews this memo before the requisition is approved for an external offer.

#### 5.1.3 Contingent Worker Offer and Agreement Execution

Once the requisition is approved:
1.  **For Direct Contractors:** Procurement issues the standard Meridian Independent Contractor Agreement (SOP-HR-016-T003) via DocuSign. The agreement links the SoW, NDA, and Data Protection Addendum if required.
2.  **For Agency Contractors:** A Task Order under the existing Master Services Agreement is issued to the agency. The Task Order must list the pre-identified candidate by name and stipulate that Meridian maintains the right to perform an independent background check.
3.  **Pre-Start Documentation Packet:** The following must be signed and returned via DocuSign at least 48 business hours before the scheduled start date:
    - Proprietary Information and Inventions NDA (SOP-HR-016-T001)
    - Confidentiality Agreement
    - Acceptable Use Policy for Information Technology Resources (acknowledgment receipt)
    - Code of Conduct Acknowledgment
    - If PHI access: Business Associate Agreement Addendum

### 5.2 Background Check and Adjudication Procedure

#### 5.2.1 Initiation and Consent

| Step | Actor | Action |
|---|---|---|
| 1 | HR Onboarding Coordinator | Upon receipt of the fully executed contract, initiates the BGC request within Meridian's approved BGC vendor portal (currently: Checkr). |
| 2 | Contingent Worker | Receives an email from the vendor with a link to provide personal information and electronic consent. Consent must be provided within 72 hours; failure to do so pauses the onboarding process and notifies the Engagement Manager. |
| 3 | Vendor | Executes the BGC package based on Meridian's defined packages. |

#### 5.2.2 BGC Packages

| Package Code | Description | Criteria for Use |
|---|---|---|
| **BGC-S-001** | SSN Trace, National Criminal Database, Sex Offender Registry, Global Watchlist (OFAC). | Non-sensitive, remote contractors with zero system access (e.g., content writers). Rarely used. |
| **BGC-S-002 (STANDARD)** | All of BGC-S-001, plus: 7-year County Criminal Search (Primary Counties), Federal Criminal Search. | **Default for all on-site contractors and all contractors receiving system access.** |
| **BGC-S-003 (ENHANCED)** | All of BGC-S-002, plus: Education Verification, Professional License Verification, Employment Verification (past 3 years). | Contractors with access to PHI, Clinical AI systems, or Financial systems (HealthPay). |
| **BGC-S-004 (OFFICE OF INSPECTOR GENERAL)** | All of BGC-S-003, plus: OIG List of Excluded Individuals/Entities (LEIE), GSA SAM.gov Excluded Parties, FDA Debarment List, EPLS checks. | Contractors working on any U.S. Federal healthcare program-related systems or data. Mandatory for all MedInsight contractors. |

**Meridian Standard:** All Contingent Workers receiving logical or physical access to Meridian facilities or systems are subject to, at minimum, BGC-S-002. Access will not be provisioned until results are received and adjudicated as "Clear."

#### 5.2.3 Adjudication Matrix

| Finding Category | Adjudication Decision Authority | Criteria |
|---|---|---|
| **Category 0 (Clear)** | HR Onboarding Coordinator (automated) | No records found, or records found are non-disqualifying per matrix. |
| **Category 1 (Minor Offense)** | Engagement Manager + HR Business Partner | Traffic violations, non-violent misdemeanors older than 5 years, dismissed charges. Engagement Manager can approve "Clear with Notes." |
| **Category 2 (Significant Offense)** | CHRO (Jennifer Walsh) | Any felony, any crime involving dishonesty or breach of trust (fraud, embezzlement, identity theft), any violent crime, any drug-related felony, or any offense within the last 7 years. |
| **Category 3 (Exclusion)** | CHRO + CCO | OIG LEIE match, FDA debarment match, or SOX-related financial crime history. These are immediate "No Hire." |

An adjudication log entry is created in Workday with the final status, adjudicator name, and date.

### 5.3 Onboarding, Access Provisioning, and System Enrollment

This is the most tightly controlled segment of the Contingent Worker lifecycle.

#### 5.3.1 Day One (Start Date)

The Contingent Worker arrives (physically at the assigned Meridian office) or logs in remotely (via the provided temporary credentials). The Engagement Manager, or a designated HR delegate, executes the following onboarding checklist:

**Checklist ID: SOP-HR-016-C001**

| Task ID | Task Description | Responsible Party | Tool / Evidence |
|---|---|---|---|
| ONB-01 | Verify identity against government-issued photo ID. | Engagement Manager (in-person) or HR via KBA (remote video session). | Secure video call recording; copy of ID (retained securely as per SOP-LEG-001) |
| ONB-02 | Collect Right-to-Work documentation (I-9 for US, equivalent for global offices). | HR Onboarding Coordinator. | Workday Onboarding module. |
| ONB-03 | Issue Physical Access Badge (if on-site). Photo taken, badge printed. Must set an expiration date matching the contract end date. | Physical Security / Office Manager. | Lenel OnGuard badge system. |
| ONB-04 | Issue Temporary Okta Credentials. Login is restricted only to the Workday onboarding page and LMS until tasks ONB-05 and ONB-06 are complete. | IT Service Desk (automated provisioning script triggered by HR on "Start Date" in Workday). | Okta Workflow. |
| ONB-05 | **HIPAA & Security Training (Mandatory)**. Worker logs in and MUST complete: "HIPAA and You: Essentials for the Contingent Workforce" and "Meridian Information Security Awareness for Non-Employees." Modules end with a scored quiz (pass rate: 80%). | Contingent Worker. | LMS (Workday Learning). |
| ONB-06 | GDPR Privacy Acknowledgment. Worker receives a link to the "Meridian Contingent Worker Privacy Notice" (available in English, German, and French). Worker acknowledges review. | Contingent Worker. | DocuSign. |
| ONB-07 | Role-Based Access Control (RBAC) Group Assignment. Upon documented completion of ONB-05 and ONB-06, the system automatically moves the worker from the "New-Hire-Pending" Okta group to one or more pre-authorization groups based on the Access Request Form. | Automated via Okta Workflow. | Okta / Active Directory. |

#### 5.3.2 Access Request Form (SOP-HR-016-F002)

The Engagement Manager submits this form *before* the start date. The Access Request Form maps the Contractor's role to specific IAM groups. Examples from Meridian's catalog:

| Contractor Role | Okta Group | Associated Permissions | Enhanced Approval? |
|---|---|---|---|
| Clinical Data Analyst | `aws-s3-prod-medinsight-ro` | Read-Only access to S3 `medinsight-prod-phidata` | Yes - CISO |
| AI Model Auditor | `sagemaker-readonly-ai-gov` | Read-only SageMaker, no data movement | Yes - CISO |
| HealthPay QA Contractor | `jira-hp-dev-qa` | Jira access, test environment credentials only. **Explicitly excluded from `prod-payment-app`** | Yes - CISO |
| General IT Support Contractor (Desktop) | `okta-helpdesk-limited` | Okta read-only Help Desk app, limited ServiceNow ticket creation | No - IT Manager |
| Marketing Design Contractor | `adobe-cc-marketing`, `dropbox-marketing-ro` | Adobe CC license, Dropbox read-only | No - Marketing Director |
| EU Data Contractor (Berlin office) | `eu-gdpr-sandbox-data` | Access to pseudonymized-only sandbox data in EU-west-1 region. No US cross-border data transfer permitted. | Yes - DPO (Dr. Meissner) |

For requests involving enhanced approval, the Access Request Form is routed in ServiceNow to the CISO and DPO (if applicable) simultaneously. CISO target SLA for approval/rejection is two business days.

### 5.5 Ongoing Management and Monitoring

#### 5.5.1 Timesheet and Deliverable Approval

- Contingent Workers log hours in Workday via the "Contingent Worker Time Entry" module.
- Engagement Manager approves hours *weekly* before 12:00 PM Eastern Time on Monday for the preceding week.
- For deliverables-based contracts (consultants), the Engagement Manager submits a "Deliverable Acceptance" confirmation in Workday, which authorizes invoice payment.

#### 5.5.2 Periodic Access Review & Reaffirmation

Contingent Worker access is subject to a periodic review model. Every 90 days from the start date, the Engagement Manager receives an automated email from ServiceNow containing a full dump of the Contingent Worker's current effective access rights (SaaS apps, IAM groups, AD groups, and badge access). The Engagement Manager MUST confirm in ServiceNow that each entitlement remains necessary for the current phase of the SoW. If a worker's role has shifted, the Engagement Manager is expected to proactively request removal of obsolete access. The system flags non-response after seven days and escalates to the CISO's office.

#### 5.5.3 Contract Renewals and Extensions

Initial Contingent Worker engagements are limited to 12 months. Extensions beyond 12 months (up to a maximum of 24 months total tenure) require:
1.  Updated SoW with new milestones.
2.  Re-execution of BGC if more than 180 days have elapsed since the original adjudication.
3.  Re-affirmation of training (if mandatory training like HIPAA has changed).
4.  VP-level approval from the business unit and acknowledgment from CHRO regarding co-employment risk assessment.

### 5.6 Offboarding and Access Revocation Procedure

The critical offboarding control must be executed to meet the SOC 2 Security criterion for timely access removal.

#### 5.6.1 Planned Offboarding

| Timeline | Actor | Action |
|---|---|---|
| T minus 5 Business Days | Engagement Manager | Initiates the Offboarding Business Process in Workday. Specifies last day of engagement and final hour (e.g., 3:00 PM EST). |
| T minus 3 Business Days | Contingent Worker | Receives automated checklist for knowledge transfer, return of Meridian equipment inventory list, and final timesheet submission instructions. |
| T minus 1 Business Day | IT Service Desk | Pre-stages the deprovisioning script. Script is set to run automatically at the specified final hour on the final day. |
| **T + 0 (Scheduled Revocation)** | **Okta IAM (Automated)** | **At the specified time:** 1) User is moved from standard Okta groups to `deprovisioned-users` OU. 2) Session tokens are invalidated; active sessions terminated. 3) Account is suspended; not deleted, per records retention needs. |
| T + 0 | Physical Security | Badge access to Meridian offices is automatically deactivated at the specified time via Lenel OnGuard scheduling. |
| T + 1 Business Day | Engagement Manager | Confirms in Workday that all Meridian physical assets (laptop, badge, YubiKey) have been returned and that the final invoice/timesheet has been processed. |
| T + 30 Days | HR Onboarding Coordinator | Archives Contingent Worker File. Retention: 7 years from separation date. |

#### 5.6.2 Emergency / Immediate Offboarding

In the event of a security incident, violation of the Code of Conduct, or other serious cause:
1.  Engagement Manager, CISO, or CHRO escalates to the Meridian Security Operations Center (SOC) via PagerDuty.
2.  **Target SLA for Access Termination: Under four (4) hours from escalation.** The SOC, under CISO authority, executes the "Contingent Worker Emergency Disable" playbook which runs a script to:
    - Disable Okta account (SAML session termination across all SSO apps).
    - Suspend AWS IAM user / remove from all IAM groups.
    - Force-remove from Snowflake.
    - Immediately deactivate badge in Lenel.
3.  A Post-Incident Review ticket is opened in ServiceNow, documenting the timeline.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Control Objective |
|---|---|---|
| **AC-HR-016-01** | All Contingent Workers must sign an NDA prior to system access. | Protect Meridian Proprietary Information and Trade Secrets. |
| **AC-HR-016-02** | Background checks (BGC-S-002 minimum) adjudication prior to start date. | Mitigate insider threat and meet HIPAA §164.308(a)(2) standard for personnel security. |
| **AC-HR-016-03** | Standardized Access Request Form (SOP-HR-016-F002) maps role to RBAC groups. | Prevent over-provisioning, enforce least privilege. |
| **AC-HR-016-04** | Enhanced CISO/DPO approval for PHI, financial, and AI model access requests. | Satisfy HIPAA Minimum Necessary Rule (§164.514(b)), SOC 2 CC6.1 access authorization. |
| **AC-HR-016-05** | Segregation of Duties (SoD) check automated in Okta workflows. A Contingent Worker cannot be a member of both a "development" group and a "production deployment" group. | SOC 2 CC5.3, compliance with SOX-adjacent financial controls. |
| **AC-HR-016-06** | Contractors and Temporary staff are explicitly excluded from the Okta group `okta-global-administrators` and `aws-prod-admin`. | SOC 2 logical access control, HIPAA §164.312(a)(1). |
| **AC-HR-016-07** | Workday onboarding workflow has a hard-stop conditional step: task "Access Badge Issuance" and "Production Okta Group Assignment" cannot proceed until the BGC step is `status = Clear`. | Technical enforcement of mandatory background screening policy. |
| **AC-HR-016-08** | Physical access badges for Contingent Workers are visually distinct (a yellow vertical stripe) from employee badges (solid blue). Expiry date is prominently printed. | SOC 2 CC6.1 (security awareness), facilitates visual identification. |

### 6.2 Technical Controls

| Control ID | System / Tool | Control Description |
|---|---|---|
| **TC-HR-016-01** | Okta Workflows & Lifecycle Management | Automated deprovisioning of Contingent Worker accounts based on the `endDate` attribute in Workday. Attribute synced via Workday-to-Okta SCIM integration every 15 minutes. |
| **TC-HR-016-02** | Okta ThreatInsight | Monitors login attempts from Contingent Worker accounts for impossible-travel, suspicious IPs, and credential stuffing attempts. Anomalous login triggers immediate MFA challenge and notification to SOC. |
| **TC-HR-016-03** | AWS IAM Conditions | All Contingent Worker IAM policies in AWS include a `aws:PrincipalTag/workerType = "Contingent"` condition key. S3 bucket policies for PHI buckets (`medinsight-prod-phidata`) use this tag to enforce additional safeguards, such as mandatory object-level logging and CloudTrail data events. |
| **TC-HR-016-04** | Purview Information Protection (Microsoft 365) | Sensitivity labels (`HIPAA Protected`, `Meridian Confidential`) automatically encrypt emails and documents. Contingent Worker accounts cannot decrypt content with these labels unless they are members of the authorized group for the specific engagement; access is validated via Entra ID Conditional Access. |
| **TC-HR-016-05** | Entra ID (Azure AD) Conditional Access | Policy `CA-016-Contractor-Base` mandates: Compliant device (Intune enrolled) OR defined IP range (Zscaler ZIA), MFA strength = Phishing-resistant (YubiKey), and Session Risk = Medium-low max. |
| **TC-HR-016-06** | ServiceNow Access Request Catalog | Provides a front-end for the Access Request Form. Workflows enforce RBAC mapping and required approvals (CISO, DPO). All access requests, approvals, and provisioning actions are audited and stored in the ServiceNow audit log. |

### 6.3 Physical Safeguards

| Control ID | Control Description |
|---|---|
| **PS-HR-016-01** | Contingent Worker badges allow access only to designated work areas and common areas. Access to Data Center cages (MPOE rooms), PHI file storage rooms, and HR records rooms is denied by default. Any exception requires a physical access request approved by both CISO and Physical Security Manager, with a strict time-bound window. |
| **PS-HR-016-02** | Access logs from Lenel OnGuard for all Contingent Worker badges are reviewed quarterly by Physical Security and retained for one year. Logs containing PHI location access are reviewed monthly. |
| **PS-HR-016-03** | A clean desk policy, enforced by weekly random walkthroughs by the Office Manager, applies universally and is emphasized during Contingent Worker onboarding. |

### 6.4 SOC 2 Specific Controls Mapping

Controls in this SOP are designed to meet the following SOC 2 Trust Services Criteria (as of the 2017 framework, TSC 100).

| SOC 2 Criteria | Relevant Controls in SOP-HR-016 |
|---|---|
| **CC6.1 (Logical and Physical Access Controls)** | AC-HR-016-03, AC-HR-016-06, TC-HR-016-01, TC-HR-016-03, PS-HR-016-01. The provisioning process ensures Contingent Workers are onboarded to precise groups; an RBAC model is formally described. |
| **CC6.3 (Information Asset Handling)** | TC-HR-016-04 (Purview sensitivity labels). Controls exist to protect information assets based on classification during use by external parties. |
| **CC7.1 (Incident Detection)** | TC-HR-016-02 (Okta ThreatInsight). Security event monitoring is in place for anomalous activity on contingent accounts, and procedures for security incident response exist. |
| **CC7.4 (Incident Response)** | Section 5.6.2 (Emergency Offboarding). An incident response playbook exists and personnel are designated to respond. |
| **CC9.2 (Risk Mitigation)** | AC-HR-016-02 (Mandatory BGCs). The entity assesses and mitigates risks associated with relationships with external users. |

### 6.5 HIPAA Specific Controls Mapping (Thorough Coverage)

Engagements involving access to PHI/ePHI are subject to the following heightened controls, directly addressing the HIPAA Security Rule (45 CFR Part 160 and Subparts A and C of Part 164) and HIPAA Privacy Rule (45 CFR Part 160 and Subparts A and E of Part 164).

| HIPAA Citation | Requirement | Meridian Control Implementation | Responsible Role |
|---|---|---|---|
| **§164.308(a)(2) - Workforce Security** | Implement procedures to ensure that members of its workforce have appropriate access to ePHI. | AC-HR-016-03, AC-HR-016-04. Background checks are enhanced to BGC-S-003, including OIG exclusion list check, prior to any PHI access provisioning. | CHRO, CISO |
| **§164.308(a)(3)(i) - Access Authorization** | Implement policies for granting access to ePHI. | The Access Request Form for PHI access roles requires a mandatory field identifying the specific PHI data sets and the purpose of access (consistent with the Minimum Necessary Rule §164.514(b)). | CISO, DPO |
| **§164.308(a)(3)(ii)(A) - Access Establishment** | Establish a record of the access privileges granted. | Access provisioning logs from Okta and ServiceNow are centrally ingested into Splunk and linked to the worker's record in the HRIS. An immutable record of granted access is maintained. | CISO |
| **§164.308(a)(4)(i) - Information Access Management** | Isolating healthcare clearinghouse functions. | MedInsight Contractors are placed in a dedicated OU, with logical network segmentation (via VPC and security groups) isolating the MedInsight platform from the rest of Meridian's corporate LAN. | CISO, VP of Engineering |
| **§164.308(a)(5)(ii)(C) - Log-in Monitoring** | Procedures for monitoring attempted log-ins. | A Meridian SOC, powered by Splunk SIEM, monitors all Okta log-in attempts for Contingent Workers with PHI access (`phiusers` Okta group). Five failed MFA attempts within 10 minutes generates a P2-Security Event alert with an SLA of 30 minutes for analyst triage. | CISO, SOC Manager |
| **§164.312(a)(1) - Access Control** | Technical Access Controls: Unique User Identification, Emergency Access Procedure. | Contingent Workers are given unique, role-based Okta accounts. Emergency Access (e.g., "break glass" for a critical production issue) requires a uniquely auditable 'Emergency' Okta account, the password for which is vaulted in HashiCorp Vault and requires dual-approval (SOC + CISO on-call) to release. | CISO |
| **§164.312(b) - Audit Controls** | Implement hardware, software, and procedural mechanisms to record and examine activity in information systems that contain or use ePHI. | AWS CloudTrail and VPC Flow Logs are enabled on all ePHI containers. A proprietary SIEM use case, titled "Contractor PHI Exfiltration Detection," monitors for data exfiltration patterns (e.g., unusual data volume via `aws s3 cp`). | CISO |
| **§164.312(e)(1) - Transmission Security** | Guard against unauthorized access to ePHI transmitted over an electronic communications network. | Zscaler Private Access (ZPA) provides Zero Trust Network Access. Regardless of physical location, Contingent Workers must connect via the Zscaler Client Connector; ePHI traffic is never transmitted in cleartext. TLS 1.2 minimum enforced. | CISO, Network Operations |
| **§164.514(b) - Minimum Necessary Rule** | Reasonable efforts to limit PHI to the minimum necessary to accomplish the intended purpose. | RBAC groups for PHI access are strictly scoped (e.g., `db-medinsight-readonly-deid` for teams only needing de-identified data). Automated scans in Snowflake check granted privileges monthly and revoke any broad `SELECT *` grants on raw PHI tables that are not explicitly approved. | CISO, Compliance Officer |

A HIPAA Workforce Clearance Checklist (SOP-HR-016-F003) must be completed and attested to by the Engagement Manager and CISO before a Contingent Worker's PHI access is activated. This checklist is subject to review by the HIPAA Privacy Officer during periodic audits.

---

## 7. Monitoring, Metrics, and Reporting

Continuous oversight of the Contingent Worker population is essential for security, cost control, and compliance.

### 7.1 Key Performance Indicators (KPIs)

| Metric ID | Metric Description | Target | Measurement Method | Reporting Cadence |
|---|---|---|---|---|
| **KPI-016-01** | Average Cycle Time: Requisition Creation to Worker Start Date | < 15 business days | Workday Report: Calculated field from requisition `createdDate` to worker `startDate`. | Monthly |
| **KPI-016-02** | BGC Clearance Rate (Overall) and Adjudication Time | < 5 business days for BGC-S-002 completion. Clearance rate > 95%. | Checkr Vendor Portal API export. | Monthly |
| **KPI-016-03** | **Access Revocation SLA Compliance (Critical)** | 100% compliance to 4-hour SLA for emergency offboarding; 100% for scheduled revocation at time-stamp. | Splunk SIEM correlation of Workday termination event timestamps vs. Okta account suspension timestamps. | Weekly Operations Review |
| **KPI-016-04** | Overdue Access Reaffirmations | Zero overdue. Engagement Manager must confirm access in ServiceNow within the 90-day cycle window. | ServiceNow dashboard: "Contractor Access Tasks - Past Due." | Bi-Weekly |
| **KPI-016-05** | Contractor Tenure Analysis | No Contractor tenure should exceed 24 months. Exception rate monitored (< 2% of population). | Workday Headcount Report, filtered by Worker Type = Contingent. | Quarterly |
| **KPI-016-06** | Mandatory Training Completion | 100% completion of HIPAA Essentials and Information Security Awareness within 24 hours of start. | LMS (Workday Learning) auto-report. | Real-time dashboard; weekly compliance review. |
| **KPI-016-07** | PHI Access Compliance Audit | Zero instances of PHI access without fully-executed BAA. | Monthly automated reconciliation between Okta `phiusers` group membership and DocuSign BAA completion records. | Monthly |

### 7.2 Reporting

**Monthly Contingent Workforce Dashboard:**
Distributed to the CHRO, VP of Procurement, and CISO. Contains headcount by business unit, new starts and separations, cycle time, BGC status, training compliance, active tenure analysis, and budget vs. actual spend. Built in PowerBI, sourced from Workday and ServiceNow data cubes.

**Quarterly Access and Security Review:**
Conducted by the Compliance Officer and CISO. This manual, targeted review examines:
- A random sample of 15% of all active Contingent Worker accounts, validating actual group memberships against the approved Access Request Form on file.
- A review of all emergency offboarding events for the quarter.
- An analysis of SoD violations by role.

---

## 8. Exception Handling and Escalation

### 8.1 General Principle

Exceptions to this SOP must be rare, justified by a demonstrable business need, and subject to rigorous risk assessment and time-bound review.

### 8.2 Exception Request Workflow

1.  **Initiator:** Engagement Manager drafts an Exception Request in ServiceNow, selecting "SOP-HR-016 Exception" from the catalog.
2.  **Justification:** The request must include:
    - Specific section of the SOP for which an exception is sought (e.g., 5.2.3 - BGC Adjudication).
    - Detailed, fact-specific business justification for the exception.
    - Description of compensating controls to be implemented if available.
    - Proposed end date for the exception (must be specific date, not "ongoing").
3.  **Approval Chain:**
    - *Exceptions related to BGC:* Routed to CHRO (Jennifer Walsh) for approval. Legal is consulted.
    - *Exceptions related to Access Control (least privilege, access duration):* Routed to CISO (Rachel Kim) and Chief Compliance Officer.
    - *Exceptions related to Worker Classification:* Routed to General Counsel and CHRO for joint approval. No single-party approval is permitted.
4.  **Registration:** All approved exceptions are logged in a centralized SOP Exception Register, maintained by the Compliance team, and reviewed during the quarterly access review.

### 8.3 Escalation Paths for Performance and Conduct Issues

| Issue Type | Procedure |
|---|---|
| **Performance Issue (Quality/Deliverable)** | Engagement Manager addresses directly with the Contingent Worker (and the agency handler, if applicable). A Performance Improvement Plan (PIP) for contractors is documented via email. Escalation to Procurement for contract enforcement. |
| **Code of Conduct Violation (Minor)** | Engagement Manager, in consultation with HR Business Partner, issues a written warning. A copy is sent to the agency and placed in the Contingent Worker File. |
| **Security Policy Violation / Suspected Data Breach** | CISO is immediately escalated via PagerDuty. The Security Incident Response Plan (SOP-SEC-001) is invoked simultaneously. Immediate access suspension is required as in Section 5.6.2. |
| **Suspect Fraud or Criminal Activity** | General Counsel and CHRO are immediately notified. No direct engagement with the worker before Legal consultation. Law enforcement is engaged by Legal as appropriate. |

---

## 9. Training Requirements

### 9.1 Mandatory New Contingent Worker Training Curriculum

All Contingent Workers, regardless of role or location, must complete the following mandatory training modules within the first 24 hours of their system access being provisioned. Failure to complete results in automatic revocation of accounts.

| Module ID | Module Title | Description | Duration |
|---|---|---|---|
| **SOP-HR-016-TRN-001** | HIPAA and You: Essentials for the Contingent Workforce | HIPAA Privacy and Security Rule basics, PHI/ePHI identification, sanctions for violations, reporting processes. | 45 minutes |
| **SOP-HR-016-TRN-002** | Meridian Information Security Awareness for Non-Employees | Acceptable Use, clean desk, phishing and social engineering identification (with interactive simulation), MFA requirements, incident reporting (how to reach the SOC). | 30 minutes |
| **SOP-HR-016-TRN-003** | Code of Conduct and Business Ethics | Anti-harassment, non-discrimination, gifts and entertainment, conflicts of interest, IP protection. | 20 minutes |

### 9.2 Annual Refresher Training

For Contingent Workers with engagements extending beyond 12 months, the same training modules must be retaken and passed within 30 days of the second year commencement. Engagement Manager is responsible for verification.

### 9.3 Role-Specific Training

| Role Category | Additional Training | Responsible Manager |
|---|---|---|
| **Clinical Data Analysts (MedInsight)** | "AI and Data Ethics: Bias and Responsible Handling of Clinical Data" (SOP-ETH-003-TRN-001). Annual completion. | CTO / VP of MedInsight |
| **HealthPay Financial QA** | "PCI DSS and Financial Data Handling for Non-Employees." Annual completion. | VP of HealthPay Engineering |
| **Workers in Berlin office** | "GDPR Essentials: Data Handling in the EU." Completion tracked by DPO. | DPO (Dr. Meissner) |

### 9.4 Systems for Tracking

Workday Learning (LMS) is the system of record for all Contingent Worker training. Completion records are automatically synced to the worker's profile in Workday and tied to the access provisioning workflow—training status is checked before annual contract extensions are approved by HR.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Document Title |
|---|---|
| SOP-HR-001 | Employee Lifecycle Management |
| SOP-PROC-008 | Third-Party Vendor Risk Management |
| SOP-SEC-001 | Security Incident Response Plan |
| SOP-SEC-002 | Information Security Acceptable Use Policy |
| SOP-SEC-005 | Identity and Access Management (IAM) Policy |
| SOP-SEC-009 | Incident Detection and Response Protocol |
| SOP-LEG-001 | Legal Hold and Records Retention Policy |
| SOP-LEG-002 | Proprietary Information and Inventions Agreement |
| SOP-LEG-003 | Board and Advisor Governance |
| SOP-PRI-003 | Global Data Protection and Privacy Policy |
| SOP-ETH-003 | AI and Clinical Data Ethics Framework |

### 10.2 External References and Regulatory Standards

| Reference ID | Document / Standard |
|---|---|
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996, Privacy Rule (45 CFR Part 160 and Subparts A and E of Part 164), Security Rule (45 CFR Part 160 and Subparts A and C of Part 164). |
| **GDPR** | Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (General Data Protection Regulation). |
| **SOC 2** | AICPA Trust Services Criteria for Security (Common Criteria), TSP Section 100. |
| **PCI DSS** | Payment Card Industry Data Security Standard v4.0, applicable to HealthPay systems and personnel. |
| **IRS Publication 15-A** | Employer's Supplemental Tax Guide (Worker classification). |
| **M.G.L. c. 149, § 148B** | Massachusetts Independent Contractor Law. |

### 10.3 Key Forms and Templates

| Form / Template ID | Document Title | Location |
|---|---|---|
| SOP-HR-016-F001 | Contingent Worker Requisition | Workday |
| SOP-HR-016-F002 | Access Request Form | ServiceNow Catalog |
| SOP-HR-016-F003 | HIPAA Workforce Clearance Checklist | ServiceNow / DocuSign |
| SOP-HR-016-T001 | Contingent Worker NDA Template | DocuSign |
| SOP-HR-016-T002 | Agency Master Services Agreement Template | Conga CLM |
| SOP-HR-016-T003 | Independent Contractor Agreement Template | DocuSign |

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
|---|---|---|---|
| 2.0 | 2020-03-14 | HR Compliance Team | Initial formalization. Moved from distributed email process to centralized Workday workflow for requisitions. BGC became mandatory. |
| 3.0 | 2021-01-20 | Jennifer Walsh (CHRO) | Full rewrite to align with new Okta IAM and RBAC provisioning processes post-merger. Introduced role-based Access Request Form (F002). |
| 4.0 | 2023-06-10 | CISO Office, HR, Legal | Major update for SOC 2 Type II and HIPAA audit readiness. Added Sections 5.3.2 (Enhanced Access), 6.4 and 6.5 (Controls Detail), HIPAA Clearance Checklist. Codified 4-hour offboarding SLA. Added GDPR privacy notice requirement for EU contractors. |
| 5.0 | 2024-07-01 | HR Policy, CISO | Annual review. Strengthened AI/ML system access controls. Added Purview Information Protection and Conditional Access technical controls. Updated BGC package definitions to include FDA debarment. |
| 5.1 | 2024-09-17 | Jennifer Walsh (CHRO) | Minor revision. Updated Section 7.1 KPI targets to reflect 2024 data. Corrected cross-reference errors (SOP-SEC-009). Added clarification on offshore/nearshore worker classification in Section 1.2. Reapproved. |