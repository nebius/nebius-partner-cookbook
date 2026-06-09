---
sop_id: "SOP-HR-001"
title: "Employee Onboarding and Access Provisioning"
business_unit: "Human Resources"
version: "1.2"
effective_date: "2025-02-10"
last_reviewed: "2026-09-26"
next_review: "2027-03-20"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Employee Onboarding and Access Provisioning

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the standardized, auditable, and compliant process for onboarding all new employees, contractors, and contingent workers at Meridian Health Technologies, Inc. The primary objectives of this procedure are to ensure that all personnel are integrated effectively into their roles, granted timely and appropriate access to Meridian’s systems and data, and are fully apprised of their security, privacy, and compliance obligations from their first day of engagement.

This SOP is designed to operationalize Meridian’s commitment to the Security, Availability, and Confidentiality criteria of SOC 2, as well as to satisfy the Administrative Safeguards requirements of the HIPAA Security Rule. It ensures that access rights are provisioned based on the principle of least privilege and that the joiners, movers, and leavers process is controlled, repeatable, and transparent.

### 1.2 Scope

This SOP applies universally to all individuals who require authenticated access to any Meridian Health Technologies information system, data, or physical facility. This includes, but is not limited to:

- **Full-Time Employees (FTEs):** All regular, full-time staff across all global offices (Boston HQ, London, Berlin, Singapore, Toronto).
- **Part-Time Employees:** Staff working a reduced schedule who require system access.
- **Contractors and Consultants:** External personnel engaged under a Master Services Agreement (MSA) who will access Meridian systems, including those supporting the HealthPay Financial Services, Clinical AI Platform, MedInsight Analytics, and Meridian SaaS Platform.
- **Temporary Workers:** Agency-sourced short-term staff.
- **Interns:** Seasonal or fixed-term interns requiring supervised access.

**In-Scope Systems and Data Environments:**
This SOP governs access to the entire Meridian technology ecosystem, specifically including:
- **Corporate Systems:** Google Workspace, Okta Identity Platform, Slack, Jira/Confluence, Workday HRIS.
- **Production Cloud Environments:** AWS (us-east-1, eu-west-1) and Azure (DR) environments hosting the Clinical AI Platform, HealthPay, MedInsight, and SaaS Platform.
- **Data Platforms:** Snowflake (including PHI-bearing databases), PostgreSQL, Redis, Apache Kafka, Pinecone.
- **Machine Learning Operations (MLOps):** Kubeflow, MLflow, SageMaker, LangSmith.
- **Security & Observability:** CrowdStrike Falcon console, Datadog, PagerDuty, HashiCorp Vault, AWS KMS.
- **Physical Spaces:** All Meridian office locations, including secured server rooms and badge-access controlled areas.

**Out of Scope:**
This SOP does not cover the offboarding process. Temporary access elevation for incident response or the technical configuration of individual applications (managed by VP of IT Operations under SOP-IT-005) are not detailed herein.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **ABAC** | Attribute-Based Access Control. Dynamic access control method governing access based on user attributes, resource attributes, and environmental conditions. |
| **Access Review** | A periodic formal documented assessment of user entitlements and privileges to ensure they remain appropriate for the user’s current role and responsibilities. |
| **AWS** | Amazon Web Services. Primary cloud service provider. |
| **Azure** | Microsoft Azure. Secondary cloud service provider, used for Disaster Recovery. |
| **BYOD** | Bring Your Own Device. Policy allowing usage of personal devices for corporate work. |
| **CISO** | Chief Information Security Officer (Rachel Kim). |
| **CPO/DPO** | Chief Privacy Officer / Data Protection Officer (Dr. Klaus Weber). |
| **ePHI** | Electronic Protected Health Information. Any PHI that is created, stored, transmitted, or received in electronic form. |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996. |
| **HRIS** | Human Resources Information System (Workday). System of record for employee master data. |
| **IAM** | Identity and Access Management. The collective systems, policies, and processes governing digital identities and access rights. |
| **IdP** | Identity Provider (Okta). Central system for authentication and Single Sign-On (SSO). |
| **IT Ops** | IT Operations, led by VP Samantha Torres. |
| **JML** | Joiner, Mover, Leaver. Lifecycle process for identity management. |
| **Least Privilege** | Security principle of granting only the minimum necessary access rights required to perform a job function. |
| **MDM** | Mobile Device Management (Kandji). Platform for enforcing security policies on corporate and BYOD endpoints. |
| **PHI** | Protected Health Information. Individually identifiable health information held or transmitted by a covered entity or its business associate. |
| **RBAC** | Role-Based Access Control. Method of regulating access to computer or network resources based on the roles of individual users within an enterprise. |
| **SOC 2** | System and Organization Controls 2. A service organization control framework focused on Security, Availability, Processing Integrity, Confidentiality, and Privacy. |
| **SR 11-7** | Federal Reserve / OCC Supervisory Guidance on Model Risk Management. |
| **UDHR** | Universal Dining Hall Request. Internal term for a generic access request ticket. (Legacy term, still in use.) |
| **VP** | Vice President. |

## 3. Roles and Responsibilities

A RACI (Responsible, Accountable, Consulted, Informed) matrix defines the specific responsibilities for all stakeholders in the onboarding and access provisioning lifecycle.

| Role | Responsibility | Accountable | Consulted | Informed |
| :--- | :--- | :--- | :--- | :--- |
| **Hiring Manager** | Initiates onboarding, defines role requirements. | R, I | A | C | I |
| **HR Business Partner (HRBP)** | Processes new hire in HRIS, triggers onboarding workflow. | R, I | A | | I |
| **VP, IT Operations (Samantha Torres)** | Ensures technical infrastructure for automated provisioning is available. | | A | C, I | I |
| **IAM Team (IT Ops)** | Provisions, modifies, and revokes access; implements RBAC/ABAC; configures IAM roles. | R | A | | I |
| **CISO (Rachel Kim)** | Approves exceptional access requests; owns security risk assessment for access. | | A | C, I | I |
| **CPO/DPO (Dr. Klaus Weber)** | Approves access to data sets containing ePHI beyond role defaults. | | A | C, I | I |
| **New Hire / Worker** | Completes policy acknowledgments, activates MFA, creates workstation password. | R | A | | |
| **Compliance Manager** | Audits process adherence monthly; performs semi-annual access reviews. | | | C | R, A |

### 5.2 Phase 2: Pre-Start Day (T-14 Days)

The objective is to ensure legal, HR, and preliminary IT tasks are completed before the New Hire’s first day. Delays in this phase directly impact Time-to-Productivity KPI.

**Step 2.1: Record Generation (HRBP)**
- **Trigger:** Signed offer letter returned and background check cleared in Checkr.
- **Action:** The HRBP creates the worker profile in Workday HRIS.
- **Data Entry Requirements:**
    - Legal Name (as per government ID).
    - Business Unit (e.g., Clinical AI, MedInsight).
    - Job Title (must match approved headcount title).
    - People Manager hierarchy.
    - Work Location (City, Office/Remote).
    - Start Date.
- **Output:** Workday generates a unique Worker ID. This ID is the authoritative source attribute for all downstream IAM provisioning.

**Step 2.2: Corporate Account Provisioning (Automated)**
- **Trigger:** Workday business rule on `Worker_Status = "Active"` and `Start_Date = T-10 Days`.
- **Action:** The Okta-Workday SCIM integration automatically creates a "pre-staged" user object in Okta Universal Directory.
- **Attributes Sync:** Map `Worker_ID` to `employeeNumber`, `Job_Title` to `title`, `Manager_ID` to `managerDN`, and `Business_Unit` to `department`.
- **Group Assignment:** Script in Okta Workflows uses `department` attribute to assign the New Hire to the correct Okta base groups (e.g., `grp-all-employees`, `grp-google-workspace`, `grp-slack`). No access to production data or platforms (Snowflake, AWS) is provisioned at this stage.

**Step 2.3: Hardware Procurement and Configuration (IT Ops)**
- **Trigger:** Workday report listing hires starting in N days.
- **Action:** IT Desktop Support prepares a corporate laptop (MacBook Pro M-series standard issue).
    - Device is enrolled in Apple Business Manager and assigned to Meridian’s MDM (Kandji).
    - Zero-touch deployment profile is assigned.
    - Cryptographic disk encryption (FileVault) keys are escrowed.
    - CrowdStrike Falcon sensor, Okta Verify, and Zscaler (ZIA) agent are pre-installed.

### 5.3 Phase 3: Day One Onboarding (T+0)

This is the highest-risk day for credential compromise and access misconfiguration. All steps are mandatory, and completion triggers "Day 1 Access."

**Step 5.3.1: New Hire Orientation (HRBP)**
- **Security & Compliance Briefing:** A mandatory 2-hour session covering Meridian’s acceptable use policy, physical security, and the specific risks associated with handling clinical data and regulated financial transactions. For staff joining HealthPay, specific guidance on the Fair Credit Reporting Act (FCRA) and model risk management is delivered.

**Step 5.3.2: Identity Activation and MFA (New Hire)**
- **Action:** HRBP provides the Worker ID and a one-time activation link. The New Hire logs into the pre-staged Okta account.
- **Critical Security Step:**
    1.  Set a passphrase conforming to Meridian's Length-Based Entropy standard (minimum 16 characters).
    2.  Enroll in Okta Verify MFA (Push notification). For privileged roles (Engineering, IT, CISO Office), enrollemnt in a FIDO2 hardware security key (YubiKey) is mandatory, not optional. SMS-based MFA is strictly prohibited.
    3.  Acknowledge Employee Handbook, Data Classification Policy, and Code of Conduct digitally via Workday.

**Step 5.3.3: Role-Based Access Provisioning (RBAC)**
This is the most critical IT procedure. Access to sensitive environments like the Clinical AI Platform AWS account or MedInsight Snowflake databases must *never* be static or default. It must be role-based, time-bounded, and formally approved.

- **Action (IAM Team):** Upon successful enrollment in MFA, the "Day 1 Access" ticket in ServiceNow is actioned. The IAM team uses an Infrastructure-as-Code (Terraform) module to assign the new worker to Okta Push Groups that map to AWS IAM Roles and Snowflake roles.
- **Rule of Least Privilege:** The IAM team must execute the `meridian-iam-provisioner` CLI tool, which queries the standard role matrix (`roles-matrix.yaml`). For example, a "HealthPay Software Engineer III" will receive access to the `dev-healthpay` AWS OUs, read-access to non-production databases, and read-write access to the non-production application logs. They get *zero* access to production payment processing systems or PCI-scoped environments. That access requires a separate temporary elevation request via SOP-IT-008 ("Privileged Access Management").

#### 5.3.4 MedInsight and Clinical AI Specific Controls
Due to the extreme sensitivity of Clinical AI and MedInsight data platforms, additional attribute-based controls (ABAC) are layered on top of RBAC. Access to any Snowflake environment that hosts ePHI is not automatic. The worker's Okta profile must include the attribute `data_access_level = "PHI-APPROVED"`.

- To set this attribute, the IAM Team must verify the worker has completed *both* the general HIPAA training assignment AND the "Clinical Data Stewardship" module within the LMS.
- Even with `PHI-APPROVED` status, write-access to clinical annotation schemas or production model training data requires a specific, time-bound Jira ticket approved by the Chief Medical Officer and the CISO.

### 5.4 Phase 4: Post-Onboarding Verification (T+5 Days)

No access is assumed; it is tested.

**Step 5.4.1: Managerial Spot-Check**
The Hiring Manager is required to conduct a documented 15-minute screen-sharing session with the New Hire on Day 5. The manager must visually verify the user can access the core corporate apps (Email, Slack, Wiki) and specifically *cannot* reach sensitive areas like the production AWS bastion host or privileged Snowflake tables, unless explicitly provisioned. Results are recorded in a "N-Hire Verif" Jira ticket.

**Step 5.4.2: Automated Recertification Trigger**
On T+14 Days, the SailPoint IdentityIQ platform triggers a semi-automated "New Hire Access Attestation." The tool compares the current Okta groups against the standard blueprint for the official Job Title from Workday. Any deviation or "rogue entitlement" generates an alert for the IAM team and the Hiring Manager’s VP. This must be remediated or formally accepted as an exception within 72 hours, or the orphaned entitlement is automatically pruned by the SailPoint deprovisioning bot.

### 5.5 Templates and Forms

The following standard templates must be used. Failure to use the precise template often leads to exception handling delays.

- **FRM-003A: Access Requisition Form (Standard).** For standard role-based access requests.
- **FRM-003B: Privileged Access & Exception Request.** For admin/root roles, access to production financial systems, or any deviation from the standard Role Matrix.
- **FRM-004: Contractor Access Sponsor Agreement.** Must be signed by the Meridian Sponsor (Manager) explicitly accepting personal accountability for the contractor’s actions on Meridian systems.

---

## 6. Controls and Safeguards

This section details the specific technical and administrative controls implemented to meet the SOC 2 Common Criteria (CC6 series) concerning logical and physical access.

### 6.1 SOC 2 Logical Access Controls

Meridian implements a defense-in-depth IAM strategy, governed by this SOP, to satisfy the requirements of **CC6.1 (Logical Access Security)** .

| Control ID | Control Description | Mechanism | SOC 2 Criteria |
| :--- | :--- | :--- | :--- |
| **IAM-01** | Unique user IDs are assigned to all personnel. All shared/generic accounts are prohibited. | Okta Universal Directory; Workday as source of truth. | CC6.1.1 |
| **IAM-02** | Automated provisioning of access rights based on HR status (JML model). | Okta SCIM Provisioning; Terraform for AWS IAM Roles. | CC6.1.2 |
| **IAM-03** | Privileged Access Management (PAM) is enforced for administrative, root, and sensitive system access. | AWS IAM Roles with SAML trust; break-glass accounts in Azure vault; checkout via HashiCorp Vault. | CC6.3.1 |
| **IAM-04** | Multi-Factor Authentication (MFA) enforced for all external-facing resources and privileged access gates. | Okta Verify Push and FIDO2 WebAuthn for all personnel. YubiKey hardware mandatory for VIPs and Admins. | CC6.6.1 |
| **IAM-05** | Segregation of duties is enforced. No single persona can create an IAM role, approve a role, and assign a user to the role. | The IAM team (IT Ops) operates the tools, a central SoD matrix managed by VP of Risk prevents conflicting roles. | CC5.3.1 |
| **IAM-06** | Access controls protect data at rest, focusing on classification (e.g., "Highly Restricted" for raw MDR clinical data). | AWS KMS with a per-team envelope encryption strategy. ABAC conditions enforced through SCPs and IAM Condition Keys. | CC6.1.4 |

### 6.2 Non-Compliant and Exception Handling

The IAM system is configured to fail closed. If the SCIM provisioning workflow encounters an error (e.g., invalid department code, missing manager), the system will halt provisioning and log a `FATAL` error in the Okta Workflows console. Manual intervention by the IAM Team is required; no account is left in an unmanaged, partially provisioned "default" state.

---

## 7. Monitoring, Metrics, and Reporting

Formal monitoring and reporting are essential for demonstrating control effectiveness for SOC 2 Type II audits and operational excellence. The VP of IT Operations and the CHRO co-own the KPIs defined in this section. Data is aggregated in both ServiceNow dashboards and Datadog.

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target | Owner | Instrumentation |
| :--- | :--- | :--- | :--- |
| **Time to Full Productivity (TFP)** | Mean time from HRIS record creation to completion of "Day 1 Access" checklist (excluding hardware shipping constraints). | IAM Team, HR Ops | **Target:** < 4 business hours from Day One MFA enrollment. |
| **Onboarding SLA Attainment** | Percentage of hires whose access is fully provisioned per the role matrix within the 4-hour window. | IAM Team | **Target:** > 95% monthly average. ServiceNow ticket lifecycle reporting. |
| **Misprovisioned Access Incidents** | Number of incidents where a new hire reports lack of access to core tools (Workflow error) OR excessive access (e.g., default access to prod). | VP, IT Ops (Samantha Torres) | **Target:** < 2 per month. Source: ServiceNow Incident Table. |
| **SailPoint New Hire Attestation** | "Clean" rate from the T+14 automated review. A "clean" attestation means zero manual exceptions were flagged. | Hiring Manager, CISO (Rachel Kim) | **Target:** > 80% clean attestation rate. SailPoint IdentityIQ report. |

### 7.2 SOC 2 Access Review Cadence (Control CC6.3.12)

Formal, documented access reviews are conducted to ensure access remains appropriate. The reviews are conducted as follows:

- **Quarterly Privileged Access Review:** A meeting chaired by the CISO (Rachel Kim) and the VP of IT Ops (Samantha Torres) to review every human account possessing a `-PowerUser` or `Admin` role in AWS, Snowflake (`SECURITYADMIN`), or the MLOps platforms. Every entitlement must be re-justified by the user's department head. The output is a signed PDF report stored in the Compliance GRC tool (AuditBoard).
- **Semi-Annual Full Access Review:** For all users, the IAM team generates a user entitlement report per business unit. Hiring Managers must formally sign off on all direct reports' access within 10 business days via AuditBoard. Failure to attest results in an automated suspension of the unreviewed accounts on day 11.

### 7.3 Reporting Cadence

- **Weekly Operations Sync:** HRIS-to-Okta sync failures and KPI exceptions are reviewed.
- **Monthly CISO Dashboard:** A "Access Governance Dashboard" is presented to the CISO, aggregating TFP, misprovisioned incidents, and privileged user count vs. approval.
- **Quarterly Audit Committee:** The CHRO presents the aggregate Onboarding KPIs and a summary of the quarterly privileged access review to the Audit Committee.

---

## 8. Exception Handling and Escalation

Standard requests that fall outside the pre-defined Role Matrix must follow a controlled, auditable exception process. This process is designed to prevent "access creep" by ensuring exceptions are time-bound and reviewed.

### 8.1 Conditions Requiring an Exception
An exception is required when:
1.  A new hire’s required access does not match the curated roles in the `roles-matrix.yaml` file for their Job Title (e.g., a MedInsight Data Scientist requires read-access to raw HL7 data, a privilege normally reserved for the Clinical Integration Engineering team).
2.  A contractor requires access to a system scoped under SOC 2 Confidentiality controls without being a full-time Meridian employee in the HRIS.
3.  A non-privileged user requires temporary administrative access for a specific, time-bounded break-fix activity.

### 8.2 Procedure for Requesting an Exception
1.  **Submit Form FRM-003B:** The Hiring Manager must complete the "Privileged Access & Exception Request" form in ServiceNow Jira, providing a formal business justification, a risk acknowledgment, and a specific end-date for the privileged access.
2.  **Risk Review by CISO Office:** The request is automatically routed to the Security Architecture team. They must complete a "Access Risk Scoring" within 24 hours, classifying the request as Low, Medium, High, or Critical risk based on the combination of data sensitivity (PHI/Payment) and access privilege (Read/Write/Admin).
3.  **Approval Escalation:**
    - **Low/Medium Risk:** Approved by the Head of IAM and the CISO (or her delegate).
    - **High Risk:** Requires explicit written approval from the CISO (Rachel Kim) and the Chief Privacy Officer (Dr. Klaus Weber).
    - **Critical Risk (Production Admin/Payment System Access):** Final approval mandatory from the CEO (Dr. Sarah Chen), COO, and CISO.
4.  **Implementation:** If approved, the IAM team implements the exact privileges using a new, time-bound Okta group or AWS IAM role that automatically expires on the end-date specified in the ticket.

### 8.3 Escalation Matrix for Provisioning Failures
If automated provisioning fails, the issue must be escalated to resolve Time to Productivity (TFP) as follows:
- **Severity 1 (Total Failure):** Multiple users unable to log in. Immediate page to IAM Lead and VP IT Ops (Samantha Torres). Resolution target: 1 hour.
- **Severity 2 (Application Failure):** Single app SCIM provisioning fails (e.g., Slack). Ticket is routed to Enterprise Applications queue. Resolution target: 4 SLA hours.
- **Severity 3 (Attribute Misset):** User in a wrong group, getting a "blocked" message from a non-critical system. Standard Service Desk queue. Resolution target: 1 business day.

---

## 9. Training Requirements

Training is a foundational control for SOC 2 and for ensuring personnel understand their responsibilities in safeguarding Meridian’s data. Completion of all mandatory training is a prerequisite for obtaining full, unrestricted access to Meridian’s production data environments.

### 9.1 Mandatory Onboarding Training Path

All new personnel must complete the following Learning Path in the Workday Learning Management System (LMS) within **14 calendar days** of their start date. Failure to complete the training will result in an automated suspension of access to the Clinical AI and MedInsight platforms via an LMS-Attribute-Integration script in Okta.

| Training Module | Duration | Intended Audience | Recurrence |
| :--- | :--- | :--- | :--- |
| **MT-ST-003: Meridian Information Security & Data Classification** | 90 mins | All Personnel | Annual |
| **MT-CC-001: Code of Conduct & Ethical Use of Clinical AI** | 60 mins | All Personnel | Annual |
| **MT-PR-002: Global Data Privacy & Practitioner Responsibility** | 75 mins | Personnel handling ePHI or PII | Annual |
| **MT-FIN-101: HealthPay SR 11-7 & Model Risk Foundations** | 120 mins | HealthPay BU Personnel only | Annual |
| **MT-ENG-201: Secure Development & OWASP Top 10** | 90 mins | Engineering & ML Ops Personnel only | Annual |

### 9.2 Role-Specific Path Requirements

Upon completion of the core learning path, the LMS will assign pre-requisite modules based on the worker’s Okta `department` and `title` attribute.

- **Clinical AI Engineers:** MT-ENG-201 + MT-CL-400 "Deploying Clinical Models Safely."
- **HealthPay Developers:** MT-ENG-201 + MT-FIN-101.
- **HR Personnel:** MT-HR-500 "Handling EEO and Personnel Data in Workday."

### 9.3 Training Tracking and Reporting

The LMS reports training completion status daily to the CISO’s compliance dashboard. The Compliance Manager is specifically responsible (RACI: Responsible) for running a monthly report on all personnel who have active access to "PHI-APPROVED" data sources but have any outstanding training. This report is sent to the relevant VP and the CISO with a mandated 7-day cure period. At day 8, the IAM team is formally tasked to suspend the user's sensitive data access until the training is complete.

---

## 10. Related Policies and References

This SOP does not stand alone. It must be interpreted and executed in concert with all other relevant Meridian policies. The user is responsible for following the most recent version of any referenced document.

**Meridian Internal Policies and SOPs:**

| Document ID | Title | Relationship to This SOP |
| :--- | :--- | :--- |
| **SOP-HR-002** | Employee Offboarding and Access Revocation | Defines the leaver process, the mirror of this joiner SOP. |
| **SOP-IT-005** | Application and Infrastructure Change Management | Governs the IT change controls used to update IAM Terraform modules. |
| **SOP-IT-008** | Privileged Access Management (PAM) and Break-Glass | Provides the detailed procedure for temporary elevated access covered conceptually in Section 8. |
| **SOP-CL-001** | Clinical AI Model Development Lifecycle | Defines the specific data annotation, training, and validation environments provisioned under this SOP. |
| **POL-IS-001** | Information Security and Acceptable Use Policy | Master policy document that this SOP’s controls aim to operationalize. |
| **POL-HR-004** | Global Employee Handbook | Contains the core employment terms, including policy on personal use of corporate assets. |

**External Regulatory and Framework References:**

- **HIPAA Security Rule (45 CFR Part 164, Subpart C):** This SOP implements the Administrative Safeguards requirements, including Assigned Security Responsibility (§ 164.308(a)(2)), Workforce Security (§ 164.308(a)(3)), and Information Access Management (§ 164.308(a)(4)).
- **SOC 2 TSC 2017:** This SOP is a key control artifact for the Common Criteria series CC5.x (Control Activities), CC6.1 (Logical Access), and CC6.3 (Restricted Access).
- **SR 11-7 / OCC 2011-12:** For HealthPay personnel, the rigorous access controls and training requirements of this SOP are critical components of the Model Risk Management framework.
- **NIST Special Publication 800-53 (Rev. 5):** Informative reference for the RBAC and ABAC control families (AC-2, AC-3) implemented in our IAM architecture.

---

## 11. Revision History

A controlled document. Any changes must go through the formal Change Review Board (CRB) and be acknowledged by the Owner and Approver.

| Version | Date | Author/Editor | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **0.5** | 2024-11-15 | Sarah Jenkins, HR Ops Lead | Initial draft for cross-functional review. |
| **1.0** | 2025-02-10 | Jennifer Walsh, CHRO | Initial approved version. Formalized JML process from legacy checklists to unified Workday-Okta flow. |
| **1.1** | 2025-09-01 | Ian Cartwright, Sec. Arch. | Added SailPoint IdentityIQ attestation procedure in Section 7. Added formal SOC 2 control IDs to Section 6 tables. Removed all references to decommissioned Active Directory bridge. |
| **1.2** | 2026-09-26 | Jennifer Walsh, CHRO & Rachel Kim, CISO | Major update to Section 8 (Exception Handling) adding formal Risk Classification tiers and CEO approval for Critical risk. Refined RACI matrix. Updated Related Policies table. Full annual review and update cycle complete. |