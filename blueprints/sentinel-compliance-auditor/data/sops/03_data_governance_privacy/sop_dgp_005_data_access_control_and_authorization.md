---
sop_id: "SOP-DGP-005"
title: "Data Access Control and Authorization"
business_unit: "Data Governance & Privacy"
version: "2.6"
effective_date: "2025-03-07"
last_reviewed: "2026-12-24"
next_review: "2027-06-13"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "HIPAA"
  - "SOC 2"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Data Access Control and Authorization

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for managing, controlling, and auditing access to Meridian Health Technologies, Inc. ("Meridian") information assets. The purpose of this document is to ensure that access to all data, systems, and applications is granted based on the principles of least privilege, need-to-know, and segregation of duties, thereby protecting the confidentiality, integrity, and availability of Protected Health Information (PHI), Personally Identifiable Information (PII), intellectual property, and critical business systems.

### 1.2 Scope

This SOP applies to all Meridian personnel, including full-time employees, contractors, temporary staff, interns, third-party vendors, and any other entity granted access to Meridian information systems. The scope encompasses:

| Category | Coverage Detail |
| :--- | :--- |
| **Data Types** | PHI (ePHI and physical records), PII, Cardholder Data (CHD), intellectual property, financial records, credentials, and business-confidential information. |
| **Environments** | Production, staging, development, and disaster recovery (DR) environments across all cloud platforms (AWS us-east-1, eu-west-1; Azure DR). |
| **Users** | All human and service accounts (machine identities) accessing Meridian resources. |
| **Locations** | All global offices (Boston, London, Berlin, Singapore, Toronto) and remote work environments. |

This SOP specifically applies to the four Meridian business lines: Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform, and addresses compliance requirements for the regulatory frameworks detailed in Section 1.3.

### 1.3 Regulatory Alignment

This SOP is the primary control document for demonstrating compliance with the following regulations and frameworks. Adherence to this SOP is mandatory for maintaining certifications and avoiding regulatory penalties.

- **HIPAA (Health Insurance Portability and Accountability Act):** Addresses the Technical Safeguards (§164.312) and Administrative Safeguards (§164.308) related to Access Control, Audit Controls, and Person/Entity Authentication.
- **SOC 2 (System and Organization Controls 2):** Addresses the Common Criteria (CC) series, specifically CC6.1 (Logical and Physical Access Controls), CC6.2 (User Access Provisioning), CC6.3 (Access Review), and P6.6 (Data Confidentiality).
- **GDPR (General Data Protection Regulation):** Addresses Article 25 (Data Protection by Design and Default), Article 32 (Security of Processing), and Article 5(1)(f) (Integrity and Confidentiality).
- **EU AI Act:** Supports requirements for data governance and security controls for high-risk AI systems as per Article 10 and Article 15.
- **SR 11-7 / OCC 2011-12:** Supports model risk management by enforcing strict access controls on model code, training data, and outputs for models used in HealthPay Financial Services.
- **NIST AI RMF:** Implements controls from the "GOVERN" and "MANAGE" functions related to third-party and internal access to AI systems.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
| :--- | :--- |
| **Access Control List (ACL)** | A list of permissions attached to an object, specifying which entities are granted or denied access. |
| **Birthright Access** | Baseline access granted to all employees of a given classification (e.g., all full-time employees receive email and SSO access). |
| **Data Owner** | A senior business leader with primary accountability for a specific data asset, responsible for classifying the data and authorizing access. |
| **Deprovisioning** | The process of removing access rights from an identity, triggered by termination, role change, or access expiry. |
| **Entitlement** | A single access right or privilege granted to a user, service account, or role. |
| **Least Privilege** | The principle that an identity is granted only the minimum necessary access to perform its required function and nothing more. |
| **Privileged Access** | Access that provides elevated rights, such as administrative, root, or system-level control over an operating system, database, or application. |
| **Role-Based Access Control (RBAC)** | A model for controlling access based on the roles that users have within the organization, where permissions are aggregated into roles. |
| **Segregation of Duties (SoD)** | A control policy that prevents a single individual from holding two conflicting responsibilities, e.g., submitting a change request and approving that same request. |
| **Service Account** | A non-human account used by an application, system, or automated process to interact with other resources. |

### 2.2 Acronyms

| Acronym | Full Form |
| :--- | :--- |
| AR | Access Request |
| CI/CD | Continuous Integration / Continuous Deployment |
| CPO/DPO | Chief Privacy Officer / Data Protection Officer |
| IAM | Identity and Access Management |
| IdP | Identity Provider |
| ITSM | IT Service Management |
| JML | Joiner-Mover-Leaver |
| MFA | Multi-Factor Authentication |
| PAM | Privileged Access Management |
| PHI | Protected Health Information |
| SIEM | Security Information and Event Management |
| SOX | Sarbanes-Oxley Act |
| UAR | User Access Review |

---

## 3. Roles and Responsibilities

The following RACI matrix delineates the roles and responsibilities for data access control and authorization at Meridian.

| Activity | Data Owner | Chief Privacy Officer / DPO | InfoSec (CISO) | IT Operations (VP IT Ops) | Engineering Managers | HR (CHRO) | Compliance Officer |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Data Classification & Labeling** | A,R | C | I | I | I | I | C |
| **Access Policy Definition** | C | A,R | C | C | C | I | I |
| **Technical IAM Implementation** | I | C | C | A,R | C | I | I |
| **Access Request Approval** | A,R | C | I | I | I | I | I |
| **Access Review & Certification** | A,R | I | I | I | C | I | C |
| **Termination/Transfer Notification** | I | I | I | C | I | A,R | I |
| **Audit Log Monitoring** | I | I | A,R | I | I | I | I |
| **Third-Party Access Management** | C | A,R | C | C | I | I | I |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

**Key Named Roles:**
- **SOP Owner:** Dr. Klaus Weber, CPO / DPO
- **SOP Approver:** Maria Gonzalez, General Counsel
- **Technical IAM Owner:** VP of IT Operations
- **Privileged Access Monitor:** CISO / Security Operations Team

---

## 4. Policy Statements

### 4.1 General Principles

1.  **Least Privilege:** All identities shall be granted the absolute minimum set of permissions required to perform their verified job function. No identity shall be provided with elevated privileges by default.
2.  **Need-to-Know:** Access to data, especially PHI/PII, shall be predicated on a demonstrable business justification. Mere employment is insufficient justification.
3.  **Segregation of Duties (SoD):** In compliance with SOC 2 CC6.3, conflicting duties shall be identified and enforced. No single user shall be capable of both requesting and approving their own access, or of deploying code to production and modifying production audit logs.
4.  **Default Deny:** All access is implicitly denied. Access is explicitly granted only upon submission, justification, and approval of a formal Access Request.
5.  **Periodic Review:** All access entitlements are subject to a formal, documented review process (User Access Review) on a quarterly basis where no entitlement is grandfathered.
6.  **Data Protection by Design and Default (GDPR Art. 25):** Technical and organizational measures, such as pseudonymization and data minimization, are implemented at the system design phase to enforce data protection principles. By default, only personal data necessary for each specific purpose of the processing is accessible.

### 4.2 HIPAA-Specific Policy

In adherence to the HIPAA Security Rule, specifically §164.312(a)(1) (Access Control) and §164.308(a)(4)(i) (Information Access Management), Meridian enforces the following policy directives for all systems creating, receiving, maintaining, or transmitting electronic PHI (ePHI):

- **Unique User Identification (Required):** All users must be identified by a unique user ID. Shared or generic accounts for human users are prohibited.
- **Emergency Access Procedure (Required):** A defined, documented, and tested procedure (See SOP-DGP-005-AEP: Emergency PHI Access) exists for obtaining necessary ePHI during an emergency. The activation of this procedure triggers an immediate high-priority alert in the SIEM and a mandatory review by the CISO and CPO/DPO within 24 hours.
- **Automatic Logoff (Addressable):** Implemented. Following 15 minutes of user inactivity on any workstation or application accessing ePHI, the session is locked and requires re-authentication via MFA.
- **Encryption and Decryption (Addressable):** Implemented as a mandatory control. All ePHI at rest in AWS S3, RDS, and on endpoint devices is encrypted using AES-256. TLS 1.3 is mandatory for ePHI in transit.

---

## 5. Detailed Procedures

### 5.1 Joiner-Mover-Leaver (JML) Lifecycle

#### 5.1.1 Joiner (Onboarding)

This process ensures that new hires, contractors, or third-party users receive appropriate access from Day One without exposing Meridian to unnecessary risk.

1.  **Employee Record Creation:** HR initiates a record in Workday.
2.  **Event Trigger:** The `NewHire` event is generated in Workday and integrated with Okta (IdP) and ServiceNow (ITSM).
3.  **Manager Task Notification:** The hiring manager is automatically assigned a "Pre-Onboarding Access Request Form" task 5 business days prior to the start date.
4.  **Birthright Access Provisioning:**
    - Okta account with enforced MFA (Okta Verify Push or FIDO2 WebAuthn).
    - Meridian Google Workspace email account.
    - VPN client access (Prisma Access).
    - Enrollment in endpoint management (Jamf Pro).
5.  **Role-Based Access Request:**
    - Hiring Manager submits a ServiceNow Request Item (`AR-DATA-001`).
    - The request must specify the business justification and the target role group (e.g., `ROLE-ENG-PLATFORM-DEV-RW`, `ROLE-CLN-ONCOLOGY-RESEARCHER-RW`).
    - **Approval Chain:** Manager → Data Owner (per data classification tag).
    - **Data Owner Approval Window:** 48 hours. If no response, the request escalates to the Data Owner's direct manager.
6.  **Privileged Access:** If the role requires privileged access (e.g., `ROLE-ADM-DATABASE-DBA`), an additional form is required (`AR-PRIV-002`), justifying the specific need for `sudo`, `root`, or database `sysadmin` privileges. This requires CISO approval.
7.  **Provisioning:** Okta Group Push provisions the user into the appropriate IAM role/entitlement within the target system (AWS IAM Identity Center, GCP IAM, Snowflake RBAC model).
8.  **Verification:** The new hire must successfully log in and acknowledge receipt of the acceptable use policy. The manager confirms access efficacy on Day 2.

#### 5.1.2 Mover (Role Change)

When an internal employee transfers departments or receives a significant change in job function (promotion, lateral move), access rights must be recalculated. Access from the previous role must not accumulate ("permissions creep").

1.  **Trigger:** HR initiates a `JobChange` event in Workday.
2.  **Notification:** Workday triggers a "Role Change - Access Re-certification" task in ServiceNow assigned to both the old and new manager.
3.  **Review and Revocation:** The previous manager has 5 business days to review and submit a "Deprovision Request" for all legacy entitlements no longer required in the new role. This is a mandatory closure step.
4.  **New Access Request:** The new manager follows the standard Joiner process (Section 5.1.1, Step 5) for the new role's requirements.
5.  **Effective Date Enforcement:** All deprovisioning actions from the old role and provisioning for the new role are staged for the effective date of the transfer (HR trigger date). The change is logged and auditable.

#### 5.1.3 Leaver (Termination/Separation)

Immediate and comprehensive revocation of access is critical. Delays directly represent a violation of the Least Privilege principle and are a Class 1 security incident.

1.  **Trigger:** HR records a `Termination` event in Workday with a timestamp of effectivity.
2.  **Automated Suspension (Immediate):** Upon Workday trigger, an automated Okta workflow executes:
    - Clear user sessions.
    - Suspend Okta account.
    - Move account to a "Suspended-Former-Staff" organizational unit (OU) in Google Workspace.
3.  **Deprovisioning Actions (within 24 hours):**
    - IT Operations executes a runbook that deprovisions all access from AWS IAM, GCP IAM, Snowflake, and on-premise directory services.
    - PAM session recordings for the user are archived and access to PAM is revoked.
    - Physical access badges are deactivated.
4.  **Data Custodian Review (within 72 hours):** The departing user's manager confirms that all corporate assets and data held on local or personal drives are identified and secured. The user's data owner is consulted regarding the transfer of ownership of any critical data artifacts.
5.  **Verification:** The `Termination_Deprovisioning_Report` is automatically generated and shared with the CISO and internal audit for weekly review.

### 5.2 Access Request Workflow for Non-Standard Access

This procedure is for users who require access to a resource beyond their birthright or currently assigned role.

**ServiceNow Request Fulfillment Process:**
- **Form:** `Access Request Form (AR-EXT-003)`
- **System of Record:** ServiceNow ITSM
- **SLAs:**
    - Triage: 4 hours (business hours)
    - Manager Approval: 48 hours
    - Data Owner Approval: 72 hours
    - Technical Provisioning: 24 hours post-approval

**Workflow Steps:**
1.  **Requester** navigates to ServiceNow Service Catalog and selects "Request for Data Access."
2.  **Requester** specifies:
    - Target System (e.g., AWS S3 Bucket: `medinsight-prod-phidata`, Snowflake Schema: `CLINICAL_TRIAL_RAW`).
    - Justification: Free-form text that MUST state a specific purpose ("Need to run quarterly analysis for FDA submission 45-B for the ONCO-2025-03 cohort").
    - Duration: Temporary access or Permanent role modification. If temporary, must specify an expiry date (<90 days).
3.  **Submission:** Ticket is routed to the Identity Management queue.
4.  **Approvals:**
    - **Stage 1 (Manager):** Validates that the task is indeed assigned to the user.
    - **Stage 2 (Data Owner):** Validates the justification against data classification and compliance requirements. For PHI data, the justification is strictly scrutinized for minimum necessary (HIPAA §164.514(b)).
5.  **Fulfillment:** Okta/Cloud IAM team provisions access. Provisioning scripts add the user to the specified IAM group/role. A ticket comment is posted detailing the precise access granted.
6.  **Closure:** Requester validates and confirms access. If access is not confirmed within 48 hours of provisioning, it is automatically revoked.

### 5.3 User Access Review (UAR) Procedure

Performed quarterly, this procedure systematically validates all active user access rights, satisfying HIPAA §164.308(a)(4)(ii)(B), SOC 2 CC6.3, and GDPR Art. 5(1)(d) (Accuracy).

1.  **Scheduling:** Automated campaign launched on March 1, June 1, September 1, December 1 via Veza (access intelligence platform).
2.  **Data Aggregation:** Veza pulls identity data from Okta and entitlements from target systems (AWS, GCP, Snowflake, Salesforce, Workday). An access review dataset is created, showing every user and their effective permissions.
3.  **Reviewer Assignment:** Veza sends email notifications to Data Owners and Engineering Managers.
    - Data Owners review access to PHI/PII data assets.
    - Managers review their team members' total access footprint.
4.  **Reviewer Action:** For each entitlement, the reviewer must select one of the following:
    - **Approve:** I certify this access is required for this user's current role.
    - **Revoke:** This access is no longer necessary.
    - **Modify:** The level of access is incorrect (e.g., Read access is needed, but Read-Write was granted).
5.  **Dispute and Challenge Mechanism:** Users who contest a revocation have 72 hours to provide a written business justification for retention. If justified, the Data Owner can re-approve. A record of all contested and re-approved decisions is maintained and highlighted in the final UAR report.
6.  **Remediation:** All Revoke and Modify decisions are aggregated. IT Operations creates a batch de-provisioning ticket to execute changes within 10 business days.
7.  **Certification:** The CPO/DPO reviews the final UAR report, attesting to 100% completion. This attestation is a mandatory compliance artifact for SOC 2 Type II and HIPAA audits.

### 5.4 Privileged Access Management (PAM)

All users requiring administrative or root-level access must comply with this workflow, distinct from standard access due to the elevated risk profile.

1.  **Justification:** The user requests creation of a privileged account. This is a distinct form (`AR-PRIV-002`) requiring extensive justification.
2.  **Approval:** Requires Manager, Data Owner, and CISO approval.
3.  **Onboarding to PAM:** The account is created in CyberArk PAM. The user never possesses the password; they authenticate via CyberArk, which injects credentials into the session.
4.  **Account Types:**
    - **Standing Privileged Account:** For roles requiring constant administrative access (e.g., Database Administrators). Subject to monthly password rotation via CyberArk.
    - **Just-in-Time (JIT) Access:** For intermittent needs (e.g., a developer needing `root` for a 2-hour maintenance window). Access is requested and approved for a specific, time-bound window, after which it auto-expires.
5.  **Session Monitoring:** All PAM sessions are recorded in full (keystrokes and screen capture). The CISO’s Security Operations team reviews 10% of PAM recordings randomly each week.
6.  **Emergency Access (Break Glass):** A specific CyberArk `EmergencyAccess` group exists for break-glass scenarios. Activating this provides 30 minutes of unrestricted `Domain Admin` equivalent access. Access triggers an immediate Critical (P1) alert to SOC and an email to the entire Executive Leadership Team. Full session recording is mandatory.

### 5.5 Third-Party Access Management

Vendors, contractors, and partners accessing Meridian systems must follow this procedure, ensuring compliance with SOC 2 CC6.1 and GDPR Art. 28 (Processor).

1.  **Onboarding:** The sponsoring Meridian employee (the "Sponsor") submits a "Third-Party AR" (`AR-EXT-003`).
2.  **Documentation:** The request must include:
    - Contract/SOW number.
    - Valid copy of the Vendor's SOC 2 Type II or ISO 27001 certification, or a completed Meridian Vendor Security Assessment (VSA) rated "Low Risk" or mitigated to "Low Risk."
    - A list of IP addresses from which access will originate (e.g., the vendor's corporate network).
3.  **Account Provisioning:** Accounts are created with a naming prefix `EXT_` (e.g., `EXT_JDoe_PWConsulting`). MFA is mandatory.
4.  **Access Boundaries:** Access is scoped to the absolute minimum environment (e.g., `dev-vpc` only, not `prod-vpc`). Network access is granted only from the pre-registered IP addresses via a Security Group rule, enforced by Infrastructure as Code (Terraform).
5.  **Monitoring:** All activity by `EXT_` accounts is routed to a dedicated SIEM index with a high-fidelity alert rule for "Data Exfiltration - Volume > 100MB."
6.  **Quarterly Third-Party Review:** The Sponsor and CPO/DPO review all active third-party accounts. Any Sponsor failing to validate the ongoing business need results in immediate account suspension. This review is critical for GDPR Art. 32 ongoing confidentiality assurance.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Regulatory Mapping |
| :--- | :--- | :--- |
| **ADM-001** | Formal Data Classification Procedure. All corporate data shall be classified as Public, Internal, Confidential, or Restricted. PHI, PII, and ePHI are classified as Restricted. | SOC 2 P6.6, GDPR Art. 32 |
| **ADM-002** | Employee Access Policy Acknowledgment. Annually, all employees must re-sign the Information Security and Data Privacy Policy document. | HIPAA §164.308(a)(5)(i) |
| **ADM-003** | Access Review (Section 5.3) must be completed with 100% of entitlements reviewed by the Data Owner every quarter. | SOC 2 CC6.3 |
| **ADM-004** | SoD conflict matrix review. The matrix is reviewed by Internal Audit and updated during the annual SOP review cycle. | SOC 2 CC6.3 |

### 6.2 Technical Controls

| Control ID | Control Description | Implementation Detail |
| :--- | :--- | :--- |
| **TEC-001** | Centralized IdP | Okta Workforce Identity. SAML/OIDC integration for all internal apps. |
| **TEC-002** | MFA Enforcement | Okta Verify with Push, FIDO2 WebAuthn (YubiKey). Phishing-resistant MFA mandatory for all privileged roles. |
| **TEC-003** | Automated Deprovisioning | ServiceNow-to-Okta-to-AWS/Cloud IAM automated integration. Deprovisioning SLAs are measured and reported on monthly. |
| **TEC-004** | Database Activity Monitoring (DAM) | Imperva SecureSphere for all RDS ePHI instances. Alerts on suspicious queries (e.g., `SELECT *` on full patient table). |
| **TEC-005** | Cloud Infrastructure Entitlement Management (CIEM) | Wiz for detection of unused and overly permissive cloud identities, with automated "Revoke Unused After 90 Days" policy in production. |
| **TEC-006** | Endpoint Data Loss Prevention (DLP) | Forcepoint DLP on all managed endpoints. Policy blocks USB mass storage writes and quarantines emails containing >3 PHI record patterns. |
| **TEC-007** | Encryption | AWS KMS (CMK) managed keys for S3 and RDS. SSE-KMS enforced via SCP at the Organization level. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The effectiveness of this SOP is measured against the following KPIs, reported to the Data Governance Steering Committee monthly.

| Metric | Target | Measurement Tool | Responsible Owner |
| :--- | :--- | :--- | :--- |
| **Access Request Triage Time (P1)** | < 4 hours 99% | ServiceNow Dashboard | IT Operations |
| **Deprovisioning Execution Time** | < 1 hour 100% (Target: automated) | Okta/Wiz reconciliation | InfoSec | |
| **Quarterly UAR Completion** | 100% of Applications/Data | Veza Report | CPO/DPO |
| **SoD Violations Detected** | 0 High, < 3 Low per quarter | Internal Audit Tool | Compliance Officer |
| **Unused Privileged Accounts >30 days** | 0 | CyberArk Report | CISO |
| **EXT_ Account Re-certification** | 100% on time | CPO/DPO Quarterly Review | CPO/DPO |

### 7.2 Reporting Cadence

- **Monthly Operations Review:** IT Operations and InfoSec review tactical metrics (deprovisioning times, AR SLAs).
- **Quarterly Governance Review:** The Data Governance Committee (chaired by CPO/DPO) reviews the UAR, policy exceptions, and high-risk events.
- **Annual Executive Review:** The Board of Directors and Executive Leadership review the state of data access governance, informed by internal audit and external audit findings.

---

## 8. Exception Handling and Escalation

### 8.1 Policy Exceptions

Any deviation from the procedures defined in this SOP requires a formal, documented exception.

1.  **Request Initiation:** The requesting party (or their manager) submits a "Data Access Policy Exception" form in ServiceNow.
2.  **Justification:** The request must detail the specific control from which deviation is sought, a compelling business justification, the scope of affected systems/data, and a compensating control to maintain risk within appetite.
3.  **Risk Assessment:** The CISO and CPO/DPO jointly assess the risk of the exception.
4.  **Approval Authority:**
    - Exceptions with a duration of < 30 days and Low risk: CPO/DPO.
    - Exceptions up to 1 year or Medium risk: CISO + CPO/DPO.
    - Any exception affecting PHI processing, or any exception granted for > 1 year: Requires CISO, CPO/DPO, and General Counsel approval.
5.  **Expiration and Review:** No exception is granted for longer than 12 months. At expiry, the request must be re-submitted with updated justification and compensating controls.

### 8.2 Breach or Potential Breach

If an unauthorized access to PHI/PII is suspected or confirmed, the **SOP-DGP-003: Personal Data Breach Notification and Response** procedure immediately takes precedence. The incident must be reported via the `ISIRT` (Information Security Incident Response Team) hotline within 1 hour of awareness, as per GDPR Art. 33 notification timelines.

---

## 9. Training Requirements

### 9.1 Role-Based Training

| Training Module | Target Audience | Frequency | Delivery Method |
| :--- | :--- | :--- | :--- |
| **DSR-101: Data Security and Privacy Essentials** | All Personnel | Annually | Workday LMS |
| **DSR-201: Access Request Procedures for Managers** | People Managers, Data Owners | Semi-Annually | Instructor-led (virtual) |
| **DSR-301: Privileged User Code of Conduct** | All PAM Account Holders | Quarterly | Workday LMS + Phishing Simulation |
| **DSR-401: CPO/DPO Access Governance Oversight** | Data Governance Committee | Annually | Live Board Session |

Completion of DSR-101 is mandatory before a user's provisioned IT accounts are activated. Failure to complete refresher training within 30 days of assignment triggers an automatic account suspension.

---

## 10. Related Policies and References

### 10.1 Internal SOPs and Policies

- **SOP-DGP-001:** Data Classification and Handling Policy
- **SOP-DGP-002:** Encryption and Key Management Standard
- **SOP-DGP-003:** Personal Data Breach Notification and Response
- **SOP-DGP-004:** Vendor and Third-Party Risk Management
- **SOP-DGP-005-AEP:** Appendix - Emergency PHI Access Procedure
- **SOP-IS-001:** Identity and Access Management (IAM) Technical Standards (Okta)
- **SOP-HR-004:** Employee Onboarding and Offboarding (Workday)

### 10.2 External References

- NIST Special Publication 800-53, Revision 5: Access Control (AC) family.
- NIST Special Publication 800-63B: Digital Identity Guidelines: Authentication and Lifecycle Management.
- HHS Office for Civil Rights: Guidance on HIPAA and Cloud Computing.
- Cloud Security Alliance (CSA): Cloud Controls Matrix (CCM) v4.0, IAM Control Domain.

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2021-05-15 | Dr. Klaus Weber | Initial creation. Alignment with GDPR and early HIPAA review. |
| 2.0 | 2022-09-01 | Alice Chen (former CISO) | Major revision: Added comprehensive SOC 2 controls, introduced Veza for UAR automation, formalized third-party access procedure. |
| 2.2 | 2023-03-20 | Dr. Klaus Weber | Updated risk scoring matrix to 5-tier system. Added Section 8 on Exceptions. |
| 2.5 | 2024-08-02 | Dr. Klaus Weber | Added EU AI Act and SR 11-7 regulatory mappings in Section 1.3. Enhanced PAM Just-in-Time workflows. |
| 2.6 | 2025-03-07 | Dr. Klaus Weber | Annual review. Updated named roles to reflect current org structure. Mandated Phishing-resistant MFA for all privileged accounts. Updated SIEM thresholds for third-party access. |
| 3.0 | *Draft* | Dr. Klaus Weber | *Planned for 2027: Integration of AI-based access request justification analysis and predictive least-privilege.* |