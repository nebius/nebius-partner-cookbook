---
sop_id: "SOP-ISEC-002"
title: "Access Control and Identity Management"
business_unit: "Information Security"
version: "2.7"
effective_date: "2025-09-28"
last_reviewed: "2026-07-28"
next_review: "2027-01-08"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Access Control and Identity Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, policies, and operational procedures for managing digital identities and controlling access to Meridian Health Technologies, Inc. information systems, applications, and data assets. The purpose of this document is to ensure that access to protected information is granted based on the principles of least privilege, need-to-know, and segregation of duties, while maintaining the confidentiality, integrity, and availability of Meridian’s systems and the sensitive data they process.

This SOP defines the mechanisms by which Meridian enforces its commitment to protecting electronic Protected Health Information (ePHI), personally identifiable information (PII) subject to the General Data Protection Regulation (GDPR), financial data subject to SR 11-7 model risk management guidance, and intellectual property embedded within its AI models and SaaS platform.

### 1.2 Scope

This SOP applies to all workforce members, contractors, temporary workers, vendors, service providers, and any other individuals or entities granted access to Meridian Health Technologies information systems, including but not limited to:

- **Clinical AI Platform:** AI-driven clinical decision support tools, diagnostic imaging analysis, patient risk scoring, and adverse event prediction systems deployed in 340+ hospitals and clinics.
- **HealthPay Financial Services:** Payment processing, patient financing, medical lending, and claims automation systems.
- **MedInsight Analytics:** Population health analytics and care gap identification platform handling PHI from approximately 12 million patients.
- **Meridian SaaS Platform:** The multi-tenant cloud infrastructure hosted on AWS (us-east-1, eu-west-1) underlying all product offerings.
- **Corporate Systems:** Email, collaboration tools, human resources systems, financial systems, and development environments.
- **AI/ML Infrastructure:** Model training pipelines, feature stores, model registries, and inference endpoints.

This SOP covers all access control dimensions, including logical access to applications and data, physical access to facilities housing information systems, and programmatic access via APIs and service accounts. It applies to all environments (production, staging, development, disaster recovery) and all data classifications defined in the Meridian Data Classification Policy (SOP-DATA-001).

### 1.3 Applicability by Regulatory Domain

| Regulatory Framework | Applicability | System/Data Scope |
|---|---|---|
| SOC 2 (Security, Availability Criteria) | All Meridian SaaS Platform systems | Controls supporting the SOC 2 Trust Services Criteria for the Meridian SaaS Platform |
| HIPAA Security Rule (45 CFR §164.312) | All systems processing ePHI | Clinical AI Platform, MedInsight Analytics, any system with access to ePHI |
| GDPR (Art. 25, 28, 32) | All processing of personal data of EU data subjects | Systems in eu-west-1, any system handling EU personal data |
| EU AI Act (Art. 14, 15, Annex III) | High-risk AI systems | Clinical AI Platform components classified as high-risk |
| SR 11-7 / OCC 2011-12 | HealthPay Financial Services models | Credit scoring, fraud detection, lending decision models |

## 2. Definitions and Acronyms

### 2.1 Acronyms

| Acronym | Definition |
|---|---|
| ACL | Access Control List |
| AWS | Amazon Web Services |
| CI/CD | Continuous Integration / Continuous Deployment |
| CISO | Chief Information Security Officer |
| DPO | Data Protection Officer |
| ePHI | Electronic Protected Health Information |
| EKS | Amazon Elastic Kubernetes Service |
| FIM | File Integrity Monitoring |
| GDPR | General Data Protection Regulation |
| IAM | Identity and Access Management |
| IdP | Identity Provider |
| JML | Joiner-Mover-Leaver |
| KMS | AWS Key Management Service |
| MFA | Multi-Factor Authentication |
| NIST | National Institute of Standards and Technology |
| PAM | Privileged Access Management |
| PHI | Protected Health Information |
| RBAC | Role-Based Access Control |
| RTO/RPO | Recovery Time Objective / Recovery Point Objective |
| SAML | Security Assertion Markup Language |
| SCIM | System for Cross-domain Identity Management |
| SIEM | Security Information and Event Management |
| SoD | Segregation of Duties |
| SOP | Standard Operating Procedure |
| SSO | Single Sign-On |
| UAR | User Access Review |

### 2.2 Definitions

| Term | Definition |
|---|---|
| Access Control | The process of granting or denying specific requests to obtain and use information and related information processing services. |
| Authentication | The process of verifying the identity of a user, process, or device, often as a prerequisite to allowing access to resources in an information system. |
| Authorization | The process of determining whether a previously authenticated entity is permitted to access a specific resource. |
| Break-Glass Account | An emergency access account with elevated privileges, intended for use only when normal authentication or authorization mechanisms are unavailable. |
| Entitlement | An attribute associated with an identity that specifies access rights to a resource. |
| Joiner-Mover-Leaver (JML) | The lifecycle process governing how identities are provisioned (Joiner), modified due to role changes (Mover), and de-provisioned (Leaver). |
| Least Privilege | The principle that a security architecture should be designed so that each entity is granted the minimum system resources and authorizations necessary to perform its function. |
| Privileged Access | Access that provides elevated permissions beyond those of standard users, including administrative, root, or system-level access. |
| Role-Based Access Control (RBAC) | A method of regulating access to computer or network resources based on the roles of individual users within an enterprise. |
| Segregation of Duties (SoD) | The principle of dividing a single task or transaction into separate components assigned to different individuals to prevent fraud and error. |
| Service Account | A non-human account used by an application or service to interact with other applications, services, or the operating system. |
| Single Sign-On (SSO) | A session and user authentication service that permits a user to use one set of login credentials to access multiple applications. |
| User Access Review (UAR) | A periodic review process in which managers and application owners certify that user access rights are appropriate. |

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for the Access Control and Identity Management program. The matrix uses: **R**esponsible (does the work), **A**ccountable (approves/signs off), **C**onsulted (provides input), **I**nformed (kept up to date).

| Activity / Function | CISO (Rachel Kim) | Chief Privacy Officer / DPO (Dr. Klaus Weber) | VP of IT Operations (Samantha Torres) | VP of Engineering (David Park) | Business Unit VPs | Chief Compliance Officer (Thomas Anderson) | IAM Engineering Team | Data Owners | General Counsel (Maria Gonzalez) | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|---|
| IAM Strategy & Architecture | A | C | R | C | I | I | R | I | I | I |
| Policy Development & Maintenance | A | C | R | C | I | R | C | I | C | I |
| Identity Lifecycle (JML) Execution | I | I | A | R | C | I | R | C | I | I |
| Access Provisioning & Deprovisioning | I | I | I | A | C | I | R | C | I | I |
| User Access Reviews | I | I | I | I | A | R | R | R | I | I |
| Privileged Access Management | A | I | R | R | I | I | R | I | I | I |
| Multi-Factor Authentication | A | I | R | R | I | I | R | I | I | I |
| Access Control Monitoring & Alerting | A | I | R | R | I | C | R | I | I | I |
| GDPR Data Subject Access Controls | C | A | R | R | I | C | R | C | C | I |
| HIPAA ePHI Access Controls | A | C | R | R | I | R | R | R | C | I |
| SOC 2 Access Control Evidence Collection | I | I | R | R | I | A | R | I | I | I |
| Exception Approvals | A | C | C | C | R | C | I | R | C | I |
| Access Certification Audits | I | I | I | I | I | A | R | I | I | R |

### 3.1 Named Role Descriptions

| Role | Specific Responsibilities |
|---|---|
| Rachel Kim, CISO | Ultimate accountability for the IAM program; approves policy; approves high-risk exceptions; chairs Access Review Steering Committee. |
| Dr. Klaus Weber, CPO/DPO | Ensures GDPR compliance for access controls affecting EU personal data; reviews Data Protection Impact Assessments (DPIAs) for new access control implementations; advises on data minimization and purpose limitation as they relate to access. |
| Samantha Torres, VP of IT Operations | Owns execution of IAM operations; manages Okta tenant and SSO infrastructure; oversees physical access control systems; manages CrowdStrike endpoint access policies. |
| David Park, VP of Engineering | Owns implementation of access controls within the Meridian SaaS Platform; manages AWS IAM, EKS RBAC, and service account governance; ensures CI/CD pipeline access controls. |
| Business Unit VPs (Dr. Aisha Okafor, Robert Liu, Michael Chang) | Perform user access reviews quarterly for their respective business units; approve standard access requests; ensure timely notification of role changes. |
| Thomas Anderson, Chief Compliance Officer | Monitors adherence to this SOP; coordinates evidence collection for audits; manages the access-related corrective action process. |
| IAM Engineering Team | Executes technical provisioning and de-provisioning; maintains Okta, AWS IAM, HashiCorp Vault configurations; implements automation for JML processes; resolves access-related incidents. |
| Data Owners | Classify data assets; define access entitlements for their data domains; approve access to sensitive data; participate in User Access Reviews. |

## 4. Policy Statements

### 4.1 Core Principles

Meridian Health Technologies, Inc. adopts the following core principles governing all access control and identity management activities:

1. **Least Privilege:** Access rights shall be limited to the minimum necessary permissions required for a user or service to perform their authorized business function.
2. **Need-to-Know:** Access to sensitive data, including ePHI and EU personal data, shall be granted only when there is a demonstrable business need.
3. **Segregation of Duties:** Conflicting duties and areas of responsibility shall be separated to reduce the risk of unauthorized or unintentional modification or misuse of organizational assets.
4. **Defense in Depth:** Access controls shall be implemented at multiple layers (network, application, data, physical) to ensure no single control failure results in unauthorized access.
5. **Default Deny:** Access shall be denied by default and explicitly granted based on business requirements, following formal approval processes.
6. **Periodic Review:** Access rights shall be reviewed at regular intervals to ensure continued appropriateness.
7. **GDPR Data Protection by Design and Default:** Per Article 25 of the GDPR, access control mechanisms shall be designed from the outset to implement data protection principles, including data minimization and purpose limitation.

### 4.2 General Policy Statements

| Policy ID | Policy Statement |
|---|---|
| ACM-001 | All human and non-human identities requiring access to Meridian information systems must be uniquely identified and authenticated before any access is granted. |
| ACM-002 | Multi-Factor Authentication (MFA) is mandatory for all human users accessing any Meridian production system, corporate application, or data store containing sensitive data. MFA shall use phishing-resistant methods (Okta Verify with push and biometric, or FIDO2 security keys) where technically feasible. |
| ACM-003 | Single Sign-On (SSO) via Okta shall be used for all corporate and production applications. Local application accounts are prohibited unless explicitly approved by the CISO. |
| ACM-004 | Role-Based Access Control (RBAC) shall be the standard model for provisioning access. Roles shall be defined based on job functions and reviewed annually by Business Unit VPs and Data Owners. |
| ACM-005 | Access rights for all workforce members shall be reviewed quarterly by their direct managers. Access to ePHI and EU personal data shall be reviewed by Data Owners on a monthly basis. |
| ACM-006 | Upon termination of employment or contract, all access rights must be revoked within 24 hours. For involuntary terminations involving elevated risk, revocation must occur within 1 hour of notification. |
| ACM-007 | Privileged accounts (administrator, root, system) shall not be used for routine, non-administrative activities. All privileged session activity must be logged and retained for a minimum of 12 months, or 36 months for systems processing ePHI, whichever is greater. |
| ACM-008 | Service accounts must be inventoried, have documented ownership, use certificate-based authentication or managed secrets where possible, and have their credentials rotated at least every 90 days. |
| ACM-009 | The Meridian SaaS Platform shall maintain availability commitments. In the event of a service disruption affecting access control systems, alternative access mechanisms shall be available to support critical business operations. |
| ACM-010 | All access control mechanisms must be designed to comply with the GDPR principles of purpose limitation, data minimization, and storage limitation. Access to personal data of EU subjects shall be restricted to explicitly authorized personnel with a lawful basis for processing. |

### 4.3 GDPR-Specific Policy Commitments

| Article Reference | Policy Commitment |
|---|---|
| Art. 25 – Data Protection by Design and by Default | Access control systems shall implement data minimization by default. Role design shall ensure that by default, only personal data necessary for each specific purpose is accessible. |
| Art. 28 – Processor Obligations | All third-party processors handling EU personal data shall contractually agree to implement access controls at least equivalent to those in this SOP. The DPO shall review processor access controls during vendor onboarding. |
| Art. 30 – Records of Processing Activities | The IAM Engineering Team shall maintain records of all logical access control mechanisms as part of the Records of Processing Activities, mapping each access role to processing purposes. |
| Art. 32 – Security of Processing | Access controls shall be implemented as technical and organizational measures to ensure a level of security appropriate to the risk, including encryption of personal data at rest and in transit, the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems. |
| Art. 33 & 34 – Notification of Personal Data Breach | Any access control failure resulting in a personal data breach shall be reported to the DPO within 2 hours of discovery. The DPO shall assess the requirement to notify the supervisory authority within 72 hours and affected data subjects without undue delay, in accordance with Articles 33 and 34. |

### 4.4 HIPAA-Specific Policy Commitments

| HIPAA Security Rule Reference | Policy Commitment |
|---|---|
| §164.312(a)(1) – Access Control | Unique user identification (Required), Emergency access procedure (Required) shall be implemented for all systems containing ePHI. |
| §164.312(a)(2)(i) – Unique User Identification | All users accessing ePHI must be assigned a unique identifier. Shared accounts for accessing ePHI are strictly prohibited. |
| §164.312(a)(2)(ii) – Emergency Access Procedure | Break-glass procedures shall be documented and tested annually for systems containing ePHI. |
| §164.312(d) – Person or Entity Authentication | Authentication mechanisms shall verify that a person or entity seeking access to ePHI is the one claimed. MFA is required for remote access to ePHI. |
| §164.308(a)(3)(ii)(B) – Workforce Clearance Procedure | Access authorization procedures shall be in place to determine that the access of a workforce member to ePHI is appropriate. |
| §164.308(a)(3)(ii)(C) – Termination Procedures | Procedures shall exist to terminate access to ePHI when the employment of a workforce member ends. |
| §164.312(b) – Audit Controls | Hardware, software, and/or procedural mechanisms that record and examine activity in information systems that contain or use ePHI shall be implemented. |
| §164.404 – Notification to Individuals | In the event of a breach of unsecured ePHI, affected individuals shall be notified. Procedures for breach response are detailed in SOP-PRIV-001 (Breach Response and Notification). |

## 5. Detailed Procedures

### 5.1 Identity Lifecycle Management (Joiner-Mover-Leaver)

The Joiner-Mover-Leaver (JML) process governs the lifecycle of all identities within Meridian systems. All JML processes must be executed through the ServiceNow ticketing system (instance: meridian.service-now.com) to maintain an auditable record.

#### 5.1.1 Joiner Process (Onboarding)

The following procedure applies to all new workforce members (employees, contractors, interns, and vendors requiring system access):

| Step | Action | Responsible Party | System/Tool | SLA |
|---|---|---|---|---|
| 1 | Hiring manager submits a "New Hire Access Request" in ServiceNow at least 5 business days prior to start date. The request must specify: Business Unit, Job Title, Manager, Required Application Access, and any special access needs (e.g., ePHI access, admin access). | Hiring Manager | ServiceNow | T-5 Business Days |
| 2 | IAM Engineering Team receives the ticket and validates completeness. If incomplete, the ticket is returned to the hiring manager with specific instructions for correction within 1 business day. | IAM Engineering Team | ServiceNow | T+1 Business Day |
| 3 | IAM Engineering queries the RBAC matrix to determine standard role entitlements for the specified Job Title and Business Unit. Custom access requests exceeding standard role entitlements are flagged for manager and Data Owner approval. | IAM Engineering Team | RBAC Matrix (Confluence), ServiceNow | T+1 Business Day |
| 4 | For roles requiring access to ePHI or EU personal data, an additional approval is required from the relevant Data Owner and the CPO/DPO (Dr. Klaus Weber) for EU personal data. The DPO verifies the lawful basis for processing (e.g., necessity for the performance of a contract, legal obligation). | Data Owner, Dr. Klaus Weber (DPO) | ServiceNow | T+2 Business Days |
| 5 | Identity is created in Okta and assigned to the appropriate groups based on approved entitlements. Automated SCIM provisioning pushes the identity to downstream applications (Google Workspace, Slack, AWS IAM Identity Center, Jira, Confluence). | IAM Engineering Team | Okta, SCIM integrations | T+2 Business Days |
| 6 | The IAM Engineering Team creates the user account in AWS IAM Identity Center for any required AWS Console access, mapping to appropriate permission sets defined in the AWS Permission Set Catalog. | IAM Engineering Team | AWS IAM Identity Center | T+2 Business Days |
| 7 | For developer roles requiring access to CI/CD pipelines and EKS clusters, the IAM Engineering Team provisions Kubernetes RBAC bindings using the automated `meridian-k8s-rbac` pipeline in Jenkins. Pipeline execution logs are retained for audit. | IAM Engineering Team | Jenkins, EKS | T+1 Business Day after step 5 |
| 8 | On Day 1, the new workforce member receives Okta enrollment instructions via their personal email. During orientation, IT Support assists with MFA enrollment (Okta Verify, and optional FIDO2 security key registration). | IT Support, New Hire | Okta | Day 1, within 4 hours of start time |
| 9 | Access verification is performed: New hire logs into Okta dashboard and verifies access to each assigned application. Any missing access is reported as a Priority 3 incident in ServiceNow. | New Hire, Hiring Manager | Okta, ServiceNow | Day 1-2 |

**Joiner Process for Service Accounts:**

| Step | Action | Responsible Party | SLA |
|---|---|---|---|
| 1 | Engineering team lead submits "Service Account Request" in ServiceNow with: Account Name, Owning Team, Owning Manager, Purpose, Required Permissions/Scopes, Authentication Method, Credential Rotation Plan. | Engineering Team Lead | Minimum 3 business days before needed |
| 2 | IAM Engineering reviews request for least privilege alignment and SoD conflicts. | IAM Engineering Team | 2 business days |
| 3 | CISO or delegate approves all service accounts with privileged (admin/root) permissions. | Rachel Kim (CISO) or delegate | 2 business days |
| 4 | Account is provisioned with automated credential injection into HashiCorp Vault. No static credentials transmitted via email or chat. | IAM Engineering Team | 1 business day |

#### 5.1.2 Mover Process (Role Change)

When a workforce member transfers roles, departments, or receives a promotion, their access rights must be reviewed and adjusted.

| Step | Action | Responsible Party | SLA |
|---|---|---|---|
| 1 | Current manager submits "Access Change – Mover" in ServiceNow immediately upon notification of the transfer. The ticket must specify: Effective Date of Transfer, New Role/Title, New Department, Access to be Removed (from old role). | Current Manager | Within 1 business day of transfer notification |
| 2 | New manager reviews current access against the standard role entitlements for the new position and submits "New Access Request" if additional access is required. | New Manager | Within 2 business days of transfer notification |
| 3 | IAM Engineering Team processes access removal for old role entitlements that are not required in the new role. Access removal must be completed by the effective date of transfer or within 3 business days of ticket receipt, whichever is earlier. For transfers involving removal of access to ePHI or EU personal data, removal must be immediate upon role change effective date. | IAM Engineering Team | Effective Date or +3 Business Days |
| 4 | Transfer is recorded in the Okta profile attributes for the user to reflect new department/manager/role for accurate future UARs. | IAM Engineering Team | +1 Business Day |

#### 5.1.3 Leaver Process (Offboarding)

| Step | Action | Responsible Party | SLA |
|---|---|---|---|
| 1 | HR/Manager submits "Termination – Access Revocation" in ServiceNow. For voluntary terminations, this should coincide with the notice period end-date. For involuntary terminations, this is submitted immediately. The ticket Severity is set to Critical for involuntary terminations. | HR Business Partner or Manager | Immediate upon notification |
| 2 | IAM Engineering Team disables the Okta account (SUSPEND), which terminates all SSO sessions within 15 minutes. Group memberships are removed. | IAM Engineering Team | < 1 Hour (Critical), < 24 Hours (Standard) |
| 3 | AWS IAM Identity Center session is revoked. IAM user access keys and Console access are deleted. | IAM Engineering Team | < 1 Hour (Critical), < 24 Hours (Standard) |
| 4 | PAM accounts (HashiCorp Vault tokens, CyberArk sessions) are revoked. | IAM Engineering Team | < 1 Hour (Critical), < 24 Hours (Standard) |
| 5 | Any service accounts owned by the departing individual are transferred to the new designated owner identified in the termination ticket. | IAM Engineering Team, New Owner | +2 Business Days |
| 6 | After 30 days, the Okta account is fully de-provisioned. Data is retained in accordance with the Meridian Data Retention Policy (SOP-DATA-002). | IAM Engineering Team (Automated) | +30 Days |
| 7 | Confirmation of access revocation is posted in the ServiceNow ticket with a summary of all disabled/revoked accounts and attached log evidence. | IAM Engineering Team | < 24 Hours (Critical), < 2 Days (Standard) |

### 5.2 Authentication Management

#### 5.2.1 Multi-Factor Authentication (MFA) Enrollment

MFA enrollment is mandatory and enforced programmatically via Okta. The procedure for initial enrollment and recovery is as follows:

| Step | Action | Details |
|---|---|---|
| 1 | During Day 1 onboarding, IT Support guides the new workforce member to `meridian.okta.com` enrollment page. | User navigates to enrollment page from a managed device in the corporate office, or via a temporary enrollment link sent to their personal email. |
| 2 | User sets initial password adhering to the Meridian Password Standard: minimum 16 characters, must not be a known compromised password (checked against Have I Been Pwned API via Okta). | Password complexity enforced by Okta policy "Meridian-Standard-Policy." |
| 3 | User enrolls a primary MFA factor: Okta Verify (Push) on their Meridian-managed mobile device. This is the mandatory primary factor. | Okta Verify enrollment requires scanning a QR code presented during enrollment. |
| 4 | User is strongly encouraged, but not required, to enroll a secondary MFA factor: FIDO2 security key (YubiKey 5 Series). For users with Privileged Access (admin roles covered under PAM), FIDO2 enrollment is mandatory. | Security keys are provisioned by IT Support during onboarding for privileged users. |
| 5 | User enrolls Okta Verify as a backup factor on a secondary device if available. | Optional, recommended for users who travel frequently. |
| 6 | IT Support validates successful MFA enrollment by having the user perform a complete sign-out and sign-in cycle using Okta Verify push. | Validation step logged in the ServiceNow onboarding ticket. |

#### 5.2.2 Single Sign-On (SSO) Configuration

All internal and external applications must be integrated with Okta SSO using SAML 2.0 or OpenID Connect (OIDC).

**Procedure for New Application Integration:**

| Step | Action | Responsible | SLA |
|---|---|---|---|
| 1 | Business Unit or Engineering submits "New SSO Integration Request" via ServiceNow, providing: Application Name, Vendor, Purpose, Data Classification of data stored/processed, URL, Preferred Protocol (SAML/OIDC), Application Owner (individual, not team). | Application Owner Designate | N/A |
| 2 | IAM Engineering performs security review: Does the application support SAML 2.0 or OIDC? Does it support Just-In-Time (JIT) provisioning with SCIM? Does it enforce MFA via IdP? Does it process ePHI or EU personal data? | IAM Engineering Team | 5 Business Days |
| 3 | If the application processes EU personal data, Dr. Klaus Weber (DPO) is consulted to ensure integration aligns with Data Protection Impact Assessment (DPIA) findings and processor agreements (Art. 28). | Dr. Klaus Weber (DPO) | Variable |
| 4 | A new "Application" entry is created in Okta with the appropriate Sign-On tab configuration. Attribute mappings are defined (email, firstName, lastName, groups, etc.). Assignment is scoped to the appropriate Okta groups derived from the RBAC matrix. | IAM Engineering Team | 2 Business Days |
| 5 | Application Owner performs User Acceptance Testing (UAT) in the Meridian staging Okta tenant (`meridian-staging.okta.com`) before the integration is promoted to production. Test cases must include: successful authentication, incorrect password handling, MFA challenge, session timeout, logout/termination behavior. | Application Owner | 5 Business Days |
| 6 | Upon successful UAT sign-off recorded in ServiceNow, the integration is promoted to the production Okta tenant. | IAM Engineering Team | 1 Business Day |

**Local Accounts Exception Procedure:** If an application demonstrably cannot support SSO (legacy systems, some industrial/medical device controllers), a Local Account Exception must be filed. This requires documented justification, compensating controls (e.g., network segmentation restricting access to a jump host with SSO), mandatory MFA via a proxy if feasible, and CISO approval. Exception is valid for 12 months, after which re-evaluation is mandatory.

### 5.3 Authorization Management

#### 5.3.1 Role-Based Access Control (RBAC) Framework

Meridian uses a hybrid RBAC model consisting of:

- **Foundational Roles:** Defined by HR system data (Job Title, Department, Location, Employment Type). These map to broad entitlements (e.g., "All FTEs get Google Workspace and Slack").
- **Functional Roles:** Curated sets of entitlements grouped by job function. Defined and maintained by Business Unit VPs and Data Owners in the RBAC Matrix (maintained as a controlled document in Confluence, page: "Meridian RBAC Matrix - Current").
- **Data-Scoped Roles:** Functional roles combined with a data scope limitation (e.g., "MedInsight_Clinician – EU Region Only").

**Entitlement Granting for Sensitive Data (ePHI, EU Personal Data, PCI):**

| Data Category | Role Approval (Beyond Manager) | Access Review Frequency | Additional Controls |
|---|---|---|---|
| ePHI (Clinical AI, MedInsight) | Data Owner Approval (e.g., VP of Clinical Informatics for Clinical AI data) | Monthly | Specific HIPAA training completion required before access granted; access logged directly to SIEM. |
| EU Personal Data (eu-west-1 systems) | DPO (Dr. Klaus Weber) Consultation, Data Owner Approval | Monthly | Access restricted to explicitly documented lawful bases; cross-border access controls enforced via AWS IAM Conditions (SourceIP restricted to EU or approved geographies). |
| Financial Data (HealthPay) | VP of Finance or Delegate | Quarterly | SoD checks run automatically before provisioning; access logged. |
| AI Model Weights & Training Data | VP of AI/ML Engineering (Dr. Patel, CTO office) | Quarterly | Access restricted to specific CI/CD service accounts and named ML Engineers; model registry access via controlled AWS IAM roles. |

**Segregation of Duties (SoD) Rules Matrix:**

| Conflicting Role Set 1 | Conflicting Role Set 2 | SoD Enforcement Mechanism |
|---|---|---|
| Application Developer (write access to source code in production CI/CD) | Application Deployer (approve production deployments) | Okta Group membership enforced; Membership in both groups triggers ServiceNow incident and access is blocked until resolved. |
| System Administrator (AWS `AdministratorAccess` or equivalent) | Security Auditor (read access to audit logs) | AWS IAM Permission Boundary prevents Administrator role from modifying CloudTrail or S3 access logs configuration for audit trails. |
| Payment System Configuration (HealthPay Admin) | Payment System Financial Reconciliation | Custom authorization check in HealthPay application preventing users with Config role from accessing financial settlement screens. |

#### 5.3.2 User Access Review (UAR) Procedure

User Access Reviews are conducted to ensure access rights remain appropriate over time. The UAR cycle is defined by data sensitivity:

| Review Type | Frequency | Scope | Reviewer | Approver |
|---|---|---|---|---|
| **Managerial UAR** | Quarterly | All non-privileged access for direct reports | Manager (via ServiceNow GRC: "Access Certification" module) | Next-Level Manager |
| **Sensitive Data UAR** | Monthly | Access to ePHI, EU Personal Data, Cardholder Data | Data Owner (via ServiceNow GRC) | Business Unit VP and DPO (for EU data) |
| **Privileged Access UAR** | Monthly | All accounts with administrative, root, or elevated privileges | IAM Engineering Team Lead, with CISO oversight | CISO (Rachel Kim) |
| **Service Account UAR** | Quarterly | All active service accounts | Owning Manager, Engineering Team Lead | VP of Engineering (David Park) |
| **Vendor/Third-Party UAR** | Quarterly | All external user accounts with Meridian system access | Relationship Owner (Business), Vendor Manager (Procurement) | Business Unit VP |

**Managerial UAR Step-by-Step:**

| Step | Action | Responsible | Timeline |
|---|---|---|---|
| 1 | IAM Engineering triggers the quarterly UAR campaign in ServiceNow GRC. Campaign includes list of all active users with their manager associations and current entitlements. | IAM Engineering Team | First Monday of February, May, August, November |
| 2 | Managers receive a ServiceNow notification with a link to their "Access Certification" task list. The list shows each direct report and their active entitlements. Managers must select "Approve" or "Revoke" for each entitlement. "Approve" certifies the access is still needed for the role. | Manager | 10 business days to complete |
| 3 | If a manager does not complete the review within 10 business days, a first reminder is sent via ServiceNow. If not completed within 15 business days, the CISO and relevant Business Unit VP are notified. Access for unreviewed users may be temporarily restricted until review is completed at the CISO's discretion. | IAM Engineering Team, CISO | Day 10, Day 15 |
| 4 | For entitlements marked "Revoke," IAM Engineering creates a "Revocation Task" and executes access removal within 2 business days. Revocation is confirmed via the ServiceNow ticket. | IAM Engineering Team | 2 business days after certification |
| 5 | A UAR Summary Report is generated by the IAM Engineering Team Lead and shared with the CISO, Chief Compliance Officer, and Internal Audit. The report summarizes: total entitlements reviewed, total revoked, stale accounts identified, and any overdue certifications. | IAM Engineering Team Lead | 5 business days after campaign closure |

**Privileged Access UAR (Monthly):**

This review specifically examines all accounts in the Okta `Privileged_Access_*` groups, AWS IAM `AdministratorAccess` and PowerUser roles, EKS `cluster-admin` bindings, and accounts stored in CyberArk PAM.

The IAM Engineering Team Lead manually reviews each account, validates: (1) The named owner is still active and in a role requiring the privilege; (2) The privilege is strictly required for current duties; (3) Account has been used within the last 30 days (dormant privileged accounts are disabled immediately pending investigation); (4) Associated MFA is valid (FIDO2 key serial number matches records).

### 5.4 Privileged Access Management (PAM)

#### 5.4.1 PAM Architecture

Meridian uses a layered PAM approach:

| Layer | System | Purpose |
|---|---|---|
| Identity Provider | Okta | Group-based access to privileged SSO applications (AWS IAM Identity Center, CyberArk). MFA enforcement, session policy. |
| Privileged Session Management | CyberArk Privileged Access Manager (PAM) | Vaulting and rotating credentials for shared privileged accounts (e.g., break-glass, legacy systems); recording and auditing sessions for critical systems. |
| Cloud Infrastructure | AWS IAM, AWS KMS, AWS Secrets Manager | Fine-grained IAM Roles for AWS administration; AWS Systems Manager Session Manager for shell access to EC2 instances (no long-lived SSH keys). Service account secrets managed via Secrets Manager with automatic rotation. |
| Container Orchestration | Amazon EKS RBAC with IAM Roles for Service Accounts (IRSA) | Pod-level IAM roles; cluster access restricted to approved CI/CD pipeline roles and named SREs via `aws eks update-kubeconfig`. |
| Secrets Management | HashiCorp Vault Enterprise | Dynamic secrets for databases; API key generation for service-to-service communication; encryption as a service. |

#### 5.4.2 Privileged Session Procedure

Requests for temporary privileged access (e.g., SRE requiring emergency `cluster-admin` access) follow this procedure:

| Step | Action | Tool | SLA |
|---|---|---|---|
| 1 | User submits "Temporary Privileged Access Request" in ServiceNow, specifying: System, Reason, Duration (maximum 8 hours, default 2), Justification linked to an Incident or Change ticket. | ServiceNow | N/A |
| 2 | Automated approval workflow triggers. For production systems, approval must come from: (1) Direct Manager; (2) VP of Engineering (David Park) or CISO (Rachel Kim). | ServiceNow, PagerDuty for urgency | 15-minute response SLA for P1 incidents |
| 3 | Upon approval, IAM Engineering provisions a time-bound Okta group membership (e.g., `Temp-EKS-Admin-Ticket12345`) with an expiration set per the request duration plus 1-hour buffer. User adds themselves to the group via Okta self-service (if configured) or IAM Engineering executes. | Okta | 10 minutes |
| 4 | User accesses the system. All commands in the privileged session are logged via CyberArk (if vaulted) or AWS CloudTrail (for AWS API) or EKS Audit Logs forwarded to Splunk (SIEM). | CyberArk / Splunk | Continuous |
| 5 | At expiration, Okta group membership is automatically removed, revoking the temporary privilege. IAM Engineering verifies revocation in a post-action review of the daily "Expired Temporary Access" report. | Okta, ServiceNow | End of business day |

#### 5.4.3 Break-Glass Access

Break-glass accounts are pre-configured emergency accounts for use when normal authentication or authorization mechanisms fail. They are used for disaster recovery scenarios affecting the identity provider itself.

- **Okta Break-Glass:** Two administrative accounts (`breakglass-admin-01`, `breakglass-admin-02`) exist outside the SSO flow, authenticated via separate FIDO2 keys stored in a dual-control safe. Use requires simultaneous action by two separate authorized individuals (VP of IT Operations Samantha Torres and CISO Rachel Kim, or their designated alternates).
- **AWS Root User:** The AWS Organization root user credentials are stored in a physical safe with dual-access control. No access keys exist. MFA is a hardware TOTP token stored in a separate safe. Use requires a documented incident ("Break-Glass Activation – AWS Root") with CEO (Dr. Sarah Chen) approval. All root activity triggers a critical alert in Splunk.

### 5.5 Physical Access Control (Brief – Full SOP: SOP-PHYS-001)

Physical access to Meridian data centers (co-location facilities), corporate offices, and secure hardware storage locations is managed through a separate policy (SOP-PHYS-001). Logical access controls detailed in this SOP function as compensating controls for physical access, ensuring that even with physical proximity to hardware, access to data is governed by the IAM framework. Integration points include:

- Physical access system (Kisi) synchronization with Okta for automated deactivation upon termination.
- Quarterly joint review of physical and logical access logs by VP of IT Operations (Samantha Torres) and CISO (Rachel Kim).
- Visitor logs are correlated with sensitive area access badges to identify tailgating or unauthorized access.

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Implementation Detail |
|---|---|---|
| AC-ADM-01 | Acceptable Use Policy Acknowledgment | All users must acknowledge the Meridian Acceptable Use Policy (SOP-ISEC-001) before being granted network access. Acknowledgment is tracked in Okta Workflows. |
| AC-ADM-02 | Background Checks | All workforce members undergo a background check commensurate with their role and data access level, per HR Policy HR-003. |
| AC-ADM-03 | Non-Disclosure Agreements (NDAs) | All users (employees, contractors, third parties) must sign an NDA before gaining access to non-public information. |
| AC-ADM-04 | Access Reviews (UAR) | Performed per Section 5.3.2 of this SOP. |
| AC-ADM-05 | Policy Compliance Monitoring | The Chief Compliance Officer (Thomas Anderson) monitors adherence to this SOP. |

### 6.2 Technical Controls

| Control ID | Control Description | Technology / Tool | Configuration Standard |
|---|---|---|---|
| AC-TECH-01 | Unique Identifier (UID) Enforcement | Okta, AWS IAM, EKS RBAC | All human accounts must map to a unique HR record. Service accounts must have a unique `svc-` prefix identifier. |
| AC-TECH-02 | Password Management | Okta, HashiCorp Vault | Okta policy enforces: 16+ characters, complexity, breached password detection. Service account secrets managed in Vault with 90-day rotation. |
| AC-TECH-03 | Multi-Factor Authentication | Okta Verify (Push), FIDO2 (YubiKey) | Enforced via Okta Sign-On Policy: "Meridian-MFA-Required" applies to all production and corporate apps. |
| AC-TECH-04 | Session Management | Okta, AWS | Idle session timeout: 15 minutes (corporate), 30 minutes (clinical/PHI systems). Absolute session timeout: 8 hours. |
| AC-TECH-05 | Audit Logging | AWS CloudTrail, Amazon EKS Audit Logs, Okta System Log, Splunk | All access events (successful/failed authentication, authorization decisions, privilege escalation, account modifications) logged centrally to Splunk. Logs immutable for duration defined in SOP-SIEM-001. |
| AC-TECH-06 | Network Segmentation | AWS VPCs, Security Groups, NACLs, Palo Alto Next-Gen Firewalls | ePHI systems in isolated VPCs; EU personal data in eu-west-1 VPCs logically separated. Access between tiers governed by least-privilege Security Groups. |
| AC-TECH-07 | Database Access Monitoring | AWS RDS, Amazon Redshift, Imperva SecureSphere | Database activity monitoring (DAM) agents log all queries to databases containing sensitive data. Alerting on anomalous query patterns (e.g., `SELECT *` on PHI tables). |
| AC-TECH-08 | File Integrity Monitoring (FIM) | AWS Config, Tripwire | Monitors critical system files, access control configurations (Okta policies, AWS IAM Policies, Security Groups) for unauthorized changes. |
| AC-TECH-09 | Endpoint Access Control | CrowdStrike Falcon | All Meridian-managed endpoints enforce full-disk encryption, local firewall rules, and USB mass storage device restrictions. |
| AC-TECH-10 | Encryption of Access Credentials | HashiCorp Vault, AWS KMS | All secrets are encrypted at rest and in transit. Transmission of unencrypted credentials via email, chat, or ticketing systems is prohibited and monitored via DLP controls in Google Workspace. |

### 6.3 Access Control List (ACL) Template

For application-level ACLs managed outside the Okta/AWS IAM framework (e.g., legacy applications), each system must maintain a documented ACL in the following format, stored in the Confluence "System Access Controls" space:

| Application: [Name] | Owner: [Name/Role] | Effective Date: [Date] | Last Reviewed: [Date] |
|---|---|---|---|
| **User/Group** | **Role/Permission Set** | **Data Scope** | **Justification (Business Need)** | **Reviewer** |

### 6.4 Availability Commitments for Access Control Systems

Meridian maintains availability commitments for the access control infrastructure itself. In the event of an Okta service disruption, Meridian relies on the availability commitments of its SaaS providers. For internally managed systems (AWS IAM, EKS RBAC), the IAM Engineering Team maintains an Incident Response Runbook for "IAM Service Degradation" scenarios. The runbook includes procedures for fallback to local authentication on critical network infrastructure and emergency access procedures. Recovery objectives are addressed as part of business continuity planning; refer to SOP-BCP-001. For systems under the SOC 2 scope, Meridian commits to maintaining operational availability, ensuring that access control mechanisms are functioning to enforce the defined policies.

### 6.5 Access Control for GDPR-Compliant Processing

The following additional controls are implemented specifically for systems and data subject to the GDPR:

- **IP-Based Access Restrictions:** Access to environments processing EU personal data (eu-west-1) is restricted to users whose source IP is within an approved geography (European Economic Area, or a specific Meridian office via VPN), enforced via AWS IAM Conditions (`aws:SourceIp`).
- **Purpose-Based Access Profiles:** Each RBAC functional role is mapped to one or more specific, documented processing purposes defined in the Records of Processing Activities (Art. 30). Access is denied if no valid purpose exists. This mapping is reviewed quarterly by the DPO.
- **Data Minimization Dashboards:** Data Owners receive a monthly automated report from the Data Governance platform (Collibra) showing the volume of personal data accessible by each role. Any role with access volume exceeding a defined threshold triggers a review by the DPO to ensure proportionality (Art. 5(1)(c)).
- **Right to Restriction of Processing (Art. 18):** When a data subject exercises their right to restriction, the DPO initiates a "Data Restriction Flag" procedure. A flag is added to the user record in Okta, propagated via SCIM to source systems (MedInsight, Clinical AI datastore), dynamically revoking normal access and leaving only storage access until the restriction is lifted.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Continuous Monitoring

| Monitoring Activity | Tool | Alert Threshold / Trigger | Respondent |
|---|---|---|---|
| Failed Authentication Spike | Splunk (Okta System Log) | > 10 failed logins for a single user in 5 minutes, or > 50 across the enterprise in 1 minute. | SOC Tier 1 Analyst |
| MFA Fatigue / Push Bombing | Okta, Splunk | > 3 Okta Verify Push challenges denied by a single user in 1 minute. User account is temporarily suspended and event investigated. | IAM Engineering Team |
| Privilege Escalation | Splunk (AWS CloudTrail, EKS Audit) | Any action matching the pattern `AttachUserPolicy`, `CreatePolicyVersion`, `AddUserToGroup` for `AdministratorAccess` or equivalent. | SOC Tier 2 Analyst, CISO notified immediately |
| Break-Glass Account Usage | Splunk (Okta System Log) | Any successful authentication to break-glass accounts. Triggers P1 Security Incident automatically. | CISO, VP of IT Operations, IR Lead |
| Service Account Anomaly | Splunk | API calls from a service account at abnormal times (outside 0600-2000 ET) or from an unexpected IP range. | Engineering Team Lead |
| Disabled Account Re-Activation | Okta, Splunk | Any re-activation of a suspended/deactivated account. | IAM Engineering Team Lead |
| User Access Review Overdue | ServiceNow GRC | Any UAR task not completed within 15 days of issuance. CISO and Compliance Officer notified. | CISO (Rachel Kim), Thomas Anderson (Compliance) |

### 7.2 Key Performance Indicators (KPIs) and Metrics

The IAM Engineering Team Lead reports the following KPIs to the CISO on a monthly basis. These metrics are also included in the quarterly Information Security Management Review presentation to the CEO.

| Metric | Target | Measurement Method | Reporting Cadence |
|---|---|---|---|
| Average Time to Provision (Joiner) | < 3 Business Days | ServiceNow ticket lifecycle duration, from submission to verified access. | Monthly |
| Average Time to Deprovision (Standard Leaver) | < 24 Hours | ServiceNow ticket lifecycle duration (Step 1 to Step 7). | Monthly |
| Average Time to Deprovision (Critical Leaver) | < 1 Hour | ServiceNow ticket lifecycle duration for tickets marked Critical. | Monthly |
| Privileged Account Review Completion | 100% Monthly | Percentage of privileged accounts reviewed vs. total privileged accounts. | Monthly |
| User Access Review - Overall Campaign Completion | > 95% within 15 days | ServiceNow GRC campaign dashboard. | Quarterly |
| Orphaned Accounts | 0 | Automated reconciliation (Okta <-> Workday) daily. Count of accounts with no matching active HR record. | Monthly |
| Service Account with Expired Credentials | < 5% | HashiCorp Vault and AWS Secrets Manager lease expiration reports. | Weekly |
| MFA Enrollment Rate | 100% Human Users | Okta policy compliance report. | Weekly |
| Access-Related Policy Exceptions (Open) | < 10 | ServiceNow Exception Register. | Monthly |
| Mean Time to Resolve (MTTR) Access-Related Incidents | < 4 Hours (P1/P2) | Splunk Incident Review. | Monthly |

### 7.3 Dashboards

The following dashboards are maintained for real-time visibility:

- **IAM Operations Dashboard (Splunk):** Real-time view of authentication volumes, failure rates, geo-location of authentications, top applications by access volume.
- **Access Review Dashboard (ServiceNow GRC):** Current UAR campaign progress, overdue certifications, upcoming recertification deadlines.
- **Privileged Access Dashboard (CyberArk, AWS IAM):** List of all active privileged sessions, recent privilege escalations approved, privileged account inventory with last-used timestamp.

## 8. Exception Handling and Escalation

### 8.1 Exception Request Procedure

Instances requiring deviation from the standards defined in this SOP must follow a formal exception process. Exceptions are granted for a specified period (maximum 12 months) and must be renewed if the deviation persists.

| Step | Action | Responsible Party |
|---|---|---|
| 1 | Requestor submits a "Policy Exception Request" via ServiceNow (form: `Policy Exception`). The form requires: SOP ID (SOP-ISEC-002), Specific Control ID being excepted, Detailed Business Justification, Proposed Compensating Control(s), Risk Assessment (Impact and Likelihood), Duration Requested. | Requestor (Individual or Team Lead) |
| 2 | The immediate manager of the requestor reviews the business justification and approves/rejects. If approved, the ticket is routed for risk assessment. | Direct Manager |
| 3 | CISO (Rachel Kim) or delegate performs risk assessment. For exceptions involving ePHI or systems under HIPAA, the Chief Compliance Officer (Thomas Anderson) must also review. For exceptions involving EU personal data, the DPO (Dr. Klaus Weber) must review and approve, verifying that the exception does not violate GDPR principles (Art. 25, Art. 32) and that an adequate level of protection is maintained. | CISO (Rachel Kim), Compliance (Thomas Anderson), DPO (Dr. Klaus Weber) |
| 4 | If the residual risk is deemed High (as per Meridian Risk Management Framework), approval by the CEO (Dr. Sarah Chen) is required. | CEO (Dr. Sarah Chen) |
| 5 | Approved exceptions are registered in the "Access Control Exception Register" (Confluence), tracked, and assigned a remediation date when the exception expires. Compensating controls are implemented and verified by IAM Engineering. | IAM Engineering Team |
| 6 | Expired exceptions not renewed, or where remediation has closed the gap, are formally closed. Compensating controls are decommissioned if no longer needed. | IAM Engineering Team |

### 8.2 Access-Related Incident Escalation

| Severity | Definition | Escalation Path |
|---|---|---|
| **P1 - Critical** | Confirmed unauthorized privileged access (e.g., root compromise, Okta admin account takeover), break-glass activation not during DR test, active widespread credential stuffing attack bypassing MFA. | Immediate notification to CISO (Rachel Kim) via PagerDuty. CISO activates the Incident Response Plan (SOP-IR-001) and notifies CEO, DPO, and General Counsel. |
| **P2 - High** | Suspected unauthorized access to ePHI or EU personal data, MFA bypass detected on a standard user account, successful phishing attack leading to credential compromise. | SOC Analyst escalates to IAM Engineering Team Lead and relevant Data Owner. SOC Manager notifies CISO and DPO within 1 hour. Incident response initiated per SOP-IR-001. |
| **P3 - Medium** | Account lockout affecting a clinical user during business hours, access provisioning error granting slightly elevated permissions, MFA token loss/replacement. | ServiceNow incident ticket assigned to IAM Engineering queue. Resolved within 4 business hours or next business day. |
| **P4 - Low** | Routine access troubleshooting, password reset, group membership adjustment requests. | Standard ServiceNow Fulfillment within 2 business days. |

### 8.3 Breach Notification (GDPR and HIPAA)

Any access control failure that results in a personal data breach triggers the Meridian Breach Response and Notification Policy (SOP-PRIV-001). Specifically:

- **GDPR (Art. 33 & 34):** The DPO (Dr. Klaus Weber) must be informed within 2 hours of confirmed breach. The DPO is responsible for assessing risk to data subjects and making the notification to the competent supervisory authority within 72 hours, and communicating to affected data subjects without undue delay if the breach is likely to result in a high risk to their rights and freedoms.
- **HIPAA (§164.400 et seq.):** The Chief Compliance Officer (Thomas Anderson) is responsible for determining if a breach of unsecured PHI has occurred. All workforce members must immediately report any suspected impermissible access, use, or disclosure of PHI to their manager and the Privacy Officer. The notification process, including notifications to affected individuals, the Secretary of HHS, and the media (if applicable), is to be executed as detailed in SOP-PRIV-001.

## 9. Training Requirements

### 9.1 General User Training

All workforce members granted access to Meridian information systems must complete the following training:

| Training Module | Content | Frequency | Delivery Platform | Tracking |
|---|---|---|---|---|
| Information Security Awareness | Overview of security policies, password hygiene, social engineering awareness, clean desk policy, reporting security incidents. | Annually | Litmos LMS | Completion recorded in Workday; non-completion triggers access suspension after 30-day grace period. |
| Privacy and Data Protection (GDPR & HIPAA) | Identifying PHI and PII, GDPR principles, HIPAA Privacy and Security Rules, Minimum Necessary Standard, Breach Reporting Obligations. | Annually | Litmos LMS | Completion mandatory for all users with data access. |
| Role-Based Access Training (ePHI Access) | Specific procedures for accessing and handling ePHI, clinical data workflows, de-identification standards, emergency access procedures. | Annually, plus upon role change granting ePHI access. | Instructor-led or via Litmos LMS (clinical track). | Must be completed before ePHI access is provisioned. |

### 9.2 Specialized Role Training

| Role | Training Module | Frequency | Trainer/Provider |
|---|---|---|---|
| IAM Engineering Team | Okta Certified Professional / AWS Certified Security Specialty; Internal Meridian SOP-ISEC-002 Training; Hands-on Break-Glass Drill. | On initial team assignment; SOP refresher annually; Break-Glass Drill Annually. | External Certifications + Internal Training by IAM Engineering Team Lead. |
| Data Owners | "Data Owner Responsibilities under SOP-ISEC-002": conducting access reviews, classifying data, approving access requests. | Annually, prior to Q4 access review campaign. | Chief Compliance Officer (Thomas Anderson). |
| Managers & VPs | "Manager Responsibilities for Access Review": how to complete the UAR in ServiceNow GRC, importance of accurate review, implications of rubber-stamping. | Annually, prior to Q1 access review campaign. | CISO (Rachel Kim) or delegate. |
| Developers/DevOps | "Secure CI/CD and Service Account Management": managing secrets in Vault, avoiding hardcoded credentials, Kubernetes RBAC, least privilege in pipeline design. | On initial access to CI/CD, plus annual refresher. | VP of Engineering (David Park), IAM Engineering Team. |

### 9.3 GDPR-Specific Training

Pursuant to Article 39 of the GDPR, the DPO (Dr. Klaus Weber) shall ensure that all personnel involved in processing operations of EU personal data are informed of their obligations. The DPO conducts a semi-annual "GDPR Data Protection Deep Dive" session, mandatory for Data Owners of systems containing EU personal data and all IAM Engineering Team members. The session covers recent EDPB guidelines on access controls, enforcement actions related to access management failures, and changes to this SOP derived from regulatory updates.

## 10. Related Policies and References

### 10.1 Meridian Internal Policies

| SOP ID | Document Title | Relationship |
|---|---|---|
| SOP-ISEC-001 | Acceptable Use of Information Assets | Defines acceptable behavior for users granted access under this SOP. |
| SOP-ISEC-003 | Incident Response | Procedure followed when an access control incident is detected. |
| SOP-ISEC-004 | Encryption and Key Management | Governs the encryption of credentials and access tokens managed by this SOP. |
| SOP-ISEC-005 | Change Management | All changes to IAM configurations (Okta policies, AWS IAM Policies) must follow the Change Management procedure. |
| SOP-ISEC-006 | Logging and SIEM Monitoring | Details the logging standards and Splunk alerting framework referenced in monitoring procedures. |
| SOP-DATA-001 | Data Classification and Handling | Defines data sensitivity levels driving access control stringency. |
| SOP-DATA-002 | Data Retention and Disposal | Defines retention periods for access logs and identity data. |
| SOP-PRIV-001 | Breach Response and Notification | Detailed procedure for breach notification obligations referenced in escalation section. |
| SOP-BCP-001 | Business Continuity and Disaster Recovery Plan | Addresses availability of access control systems during a disaster. |
| SOP-PHYS-001 | Physical Security | Companion policy for physical access to Meridian facilities. |
| SOP-VEND-001 | Vendor Risk Management | Defines access control requirements for third-party vendors. |

### 10.2 External Standards and Regulatory References

| Reference | Description |
|---|---|
| NIST SP 800-53 Rev. 5 | Security and Privacy Controls for Information Systems and Organizations (AC Family: Access Control). |
| NIST SP 800-63B | Digital Identity Guidelines – Authentication and Lifecycle Management. |
| ISO/IEC 27001:2022 | Information Security, Cybersecurity, and Privacy Protection – A.5.15, A.5.18, A.5.3, A.8.2, A.8.3, A.8.4. |
| HIPAA Security Rule | 45 CFR Part 164, Subpart C – Security Standards for the Protection of Electronic Protected Health Information. |
| GDPR | Regulation (EU) 2016/679, specifically Art. 5, 24, 25, 28, 30, 32, 33, 34, 39. |
| EU AI Act | Regulation (EU) 2024/1689, specifically Art. 14 (Human Oversight), Art. 15 (Accuracy, Robustness, and Cybersecurity) for high-risk AI systems. |
| SR 11-7 / OCC 2011-12 | Supervisory Guidance on Model Risk Management. |
| SOC 2 | AICPA TSC 2017 (2022 Revision), CC6.1, CC6.2, CC6.3. |

## 11. Revision History

| Version | Date | Author(s) | Description of Changes |
|---|---|---|---|
| 2.7 | 2025-09-28 | Rachel Kim, IAM Engineering Team | **Current Version:** Major revision. Updated PAM architecture to incorporate HashiCorp Vault dynamic secrets; Added detailed GDPR purpose-based access profiles and IP restriction controls per EDPB guidance; Added new Section 7.3 for Dashboards; Revised Leaver SLA to differentiate Critical (1-hour) vs. Standard (24-hour) per HR integration improvements; Added AI Model weights to RBAC data categories; Updated related SOP references. |
| 2.6 | 2026-07-28 | IAM Engineering Team, Thomas Anderson (Compliance) | **Last Reviewed:** Annual review cycle. Updated ServiceNow ticket templates; updated AWS Permission Set names; incorporated feedback from Q2 2026 internal audit finding related to break-glass procedure documentation; added specifics for EKS RBAC bindings in CI/CD pipeline; moved RACI matrix from prose to table format per policy documentation standards; updated Vendor UAR reviewer from "Regional Manager" to "Relationship Owner." |
| 2.5 | 2025-11-14 | Rachel Kim (CISO), Dr. Klaus Weber (DPO) | Emergency revision: Addressed cross-border data transfer controls for EU personal data following EU-US Data Privacy Framework update; strengthened Data Owner approval requirements for ePHI access provisioning; integrated new CyberArk PAM deployment details. |
| 2.4 | 2025-08-01 | Information Security Policy Team | Minor revision: Updated Okta enrollment procedure steps to reflect new Okta Verify Push experience; expanded SoD table to include Payment System Configuration roles for HealthPay; updated MFA policy statement to mandate phishing-resistant methods for privileged users; clarified that break-glass account credentials are not stored in Vault but in physical safes. |
| 2.3 | 2025-04-15 | IAM Engineering Team, VP of IT Operations (Samantha Torres) | Updated to include procedure for decommissioning legacy SSH bastion host and migrating to AWS Systems Manager Session Manager for all administrative shell access; added ServiceNow GRC campaign IDs for UAR automation; expanded Service Account management to include IRSA model for EKS. |
| 2.2 | 2025-01-20 | IAM Engineering Team, David Park (VP Engineering) | First major revision of 2025. Migrated all access control policy statements out of individual system runbooks and into this central SOP. Full alignment of JML process with Workday HRIS integration. Expanded RBAC matrix to formally define "Foundational" and "Functional" roles. |

---