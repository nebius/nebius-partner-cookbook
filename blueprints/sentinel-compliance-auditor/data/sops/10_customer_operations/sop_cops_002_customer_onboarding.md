---
sop_id: "SOP-COPS-002"
title: "Customer Onboarding"
business_unit: "Customer Operations"
version: "3.0"
effective_date: "2025-07-05"
last_reviewed: "2026-05-22"
next_review: "2026-11-27"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
  - "SOC 2"
status: "Active"
---

# Customer Onboarding Standard Operating Procedure
**SOP-COPS-002 | Version 3.0**
**Owner:** Michael Chang, Vice President of Customer Operations
**Business Unit:** Customer Operations

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the mandatory, controlled process for onboarding all new customers onto Meridian’s Clinical AI Platform, HealthPay Financial Services, and MedInsight Analytics products. The purpose is to ensure a consistent, scalable, compliant, and auditable onboarding experience that protects Meridian’s systems, data, and reputation, while enabling customers to derive value rapidly and securely. This SOP codifies the operational controls necessary to demonstrate compliance with the General Data Protection Regulation (GDPR), the Health Insurance Portability and Accountability Act (HIPAA), and the Security, Availability, and Confidentiality criteria of SOC 2.

### 1.2 Scope
This SOP applies to all employees, contractors, and third-party representatives within the Customer Operations, Sales Engineering, Cloud Infrastructure, Security Engineering, and Product Management business units who are involved in the onboarding lifecycle of a new, paying customer. The scope encompasses all operational domains from the receipt of a fully executed Master Services Agreement (MSA) through the final configuration validation and the handoff to the Customer Success Management (CSM) team for steady-state operations.

The procedures herein govern:
- The collection and processing of Customer Personal Data (CPD) from designated administrators.
- The capture of explicit data processing consents and Data Processing Agreement (DPA) acknowledgments.
- The technical configuration of single-tenanted and multi-tenanted logical environments within Amazon Web Services (AWS) Commercial and GovCloud partitions.
- The establishment of secure network connectivity (AWS PrivateLink, Site-to-Site VPN, or AWS Direct Connect).
- The integration with the Customer’s Identity and Access Management (IAM) fabric for federated authentication.
- The provisioning of initial Role-Based Access Control (RBAC) groups and user accounts.
- The configuration of audit logging for all access and data modification events.

### 1.3 Out of Scope
The following activities are explicitly out of scope for this SOP and are governed by their respective policies:
- Pre-sales technical demonstrations (see SOP-SALES-001).
- Ongoing customer support and help desk ticket resolution (see SOP-ITSM-003).
- Product feature design and development lifecycle (see SOP-ENG-101).
- Routine vulnerability scanning and patch management (see SOP-INFRA-012).

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **CCPA** | California Consumer Privacy Act of 2018. |
| **CPD** | Customer Personal Data; any information relating to an identified or identifiable natural person that is provided by the Customer to Meridian for the purpose of creating administrative user accounts. |
| **CSM** | Customer Success Manager; the Meridian personnel responsible for the long-term relationship post-onboarding. |
| **DPA** | Data Processing Agreement; the legally binding contract between the data controller (Customer) and the data processor (Meridian). |
| **DSAR** | Data Subject Access Request. |
| **GDPR** | Regulation (EU) 2016/679 of the European Parliament and of the Council. |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996. |
| **IAM** | Identity and Access Management. |
| **IDP** | Identity Provider; the Customer's system for federated authentication (e.g., Okta, Azure AD, PingFederate). |
| **MFA** | Multi-Factor Authentication. |
| **MSA** | Master Services Agreement. |
| **Onboarding Engineer** | The designated Meridian technical resource responsible for executing the technical configuration steps. |
| **PHI** | Protected Health Information. |
| **PI** | Personal Information. |
| **RBAC** | Role-Based Access Control. |
| **ROPA** | Record of Processing Activities. |
| **SAM** | Service Account Manager; the designated Meridian business owner for the commercial relationship. |
| **SAML** | Security Assertion Markup Language 2.0. |
| **SCIM** | System for Cross-domain Identity Management. |
| **SOC 2** | Service Organization Control 2 report, per the AICPA’s Trust Services Criteria. |
| **SSO** | Single Sign-On. |
| **TSC** | Trust Services Criteria. |

---

## 3. Roles and Responsibilities

A RACI (Responsible, Accountable, Consulted, Informed) matrix is established to delineate ownership for all critical onboarding tasks. The following table provides a high-level assignment; detailed responsibilities are embedded within the procedural steps.

| Onboarding Task / Activity | Customer Operations Specialist | Onboarding Engineer | Security Engineer | SAM (Sales Acct Mgr) | Customer Admin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Initiate Onboarding Workflow** | **R/A** | I | I | C | I |
| **Collect Customer Personal Data (CPD)** | **R** | I | I | C | C |
| **GDPR Consent & DPA Capture** | **R/A** | I | C | I | C |
| **HIPAA BAA Verification** | C | I | **R/A** | C | C |
| **Logical Environment Provisioning** | I | **R/A** | C | I | I |
| **Network Connectivity Configuration** | I | R | **R/A** | I | I |
| **Federated SSO Configuration** | I | R | **R/A** | I | C |
| **Initial RBAC Group Provisioning** | I | R | C | I | **A** |
| **Security Control Validation** | I | R | **R/A** | I | I |
| **Production Handoff to CSM** | **R/A** | C | I | I | I |

---

## 4. Policy Statements

Meridian Health Technologies is committed to the following high-level policies throughout the customer onboarding lifecycle:

1.  **Data Minimization and Purpose Limitation:** Meridian will collect and process only the minimum Customer Personal Data (CPD) necessary to perform the technical onboarding tasks for which we are explicitly contracted. Such data shall not be repurposed for any other secondary use, including product development or machine learning model training, without a separate, explicit agreement.
2.  **Lawful, Fair, and Transparent Processing:** All CPD collected from Customer Administrators will be processed lawfully, fairly, and in a transparent manner, in strict accordance with GDPR Article 5(1)(a). Each data processing purpose will be clearly enumerated and tied to a specific consent field or contractual clause.
3.  **Confidentiality and Integrity:** Meridian will employ industry-standard technical and organizational measures to ensure appropriate security of CPD, including its protection against unauthorized or unlawful processing, accidental loss, destruction, or damage, using robust controls such as AES-256 encryption at rest and TLS 1.3 in transit.
4.  **Security as a Design Principle:** All provisioned environments and connectivity methods will adhere to Meridian’s "Least Privilege" architecture, configured with zero trust principles by default. No environment will exit onboarding with default administrative passwords or overly permissive security groups.
5.  **Auditability and Accountability:** Every atomic operation in the onboarding workflow is fully auditable. An immutable, chronological record of who performed what action, on which resource, and at what time shall be maintained within Meridian’s centralized SIEM and Ticketing System (ServiceNow).

---

## 5. Detailed Procedures

The onboarding lifecycle is structured into five (5) distinct, sequential phases. The Customer Operations Specialist acts as the workflow orchestrator, managing the progression of tasks in ServiceNow, using the standardized `ONB – Customer Onboarding` workflow template.

### 5.1 Phase 1: Initiation and Data Collection (Lead Time: 2 Business Days)
1.  **Trigger Event:** The Customer Operations Specialist (COS) receives an automated trigger from Salesforce upon the status of a signed MSA being set to "Closed Won."
2.  **Case Creation:** The COS creates a parent Onboarding case in ServiceNow (`ONB-XXXXX`) using SOP-COPS-002 version 3.0 template. The COS attaches the PDF copy of the executed MSA, Statement of Work (SOW), and any pre-sales technical architecture diagrams to the ServiceNow case record.
3.  **Stakeholder Identification:** The COS populates the `Onboarding Stakeholders` table in ServiceNow:
    - **Meridian:** SAM (identified from Salesforce opportunity), Onboarding Engineer (assigned from a round-robin queue in Jira Service Management), Security Engineer (from the `infosec-onboarding` distribution list).
    - **Customer:** Primary Business Sponsor, Technical Lead, and proposed Initial Administrator(s). This information is obtained via an email to the SAM within 1 business day.
4.  **Dispatch of Customer Data Collection Form (CDCF):** The COS dispatches the encrypted ServiceNow `CDCF_FORM_V3.0` to the Customer’s Technical Lead. The form is bound to the `ONB-XXXXX` case. The form is designed with strict data minimization and GDPR adherence as a primary architectural control. The form sections are:
    - **Section A: Administrator Account Details:**
        - Field: `Administrator First Name` (Data Purpose: user account identity)
        - Field: `Administrator Last Name` (Data Purpose: user account identity)
        - Field: `Administrator Corporate Email` (Data Purpose: authentication principal, communication)
        - Field: `Administrator Corporate Phone` (Data Purpose: multi-factor authentication setup, urgent technical communication)
    - **Section B: Technical Environment Specification:**
        - Field: `Desired Data Residency Region` (Dropdown: `us-east-2`, `eu-west-1`, `ap-southeast-2`, etc.)
        - Field: `Connectivity Method Preference` (Dropdown: `PrivateLink`, `VPN`, `Direct Connect`)

### 5.2 Phase 2: GDPR Consent and Legal Processing (Lead Time: Immediate upon CDCF receipt)
This phase operationalizes Articles 6, 7, 12, 13, 14, and 30 of the GDPR. Upon submission of the CDCF by the Customer Administrator, an automated workflow orchestrates the consent capture process.

1.  **Consent Request Dispatch:** The Meridian Data Privacy Tool (OneTrust) dispatches a specific, granular, and unbundled consent form to the email address provided in Section A. The form, linked to the `ONB-XXXXX` case ID, is structured as follows:
    - **Consent Record A (Mandatory - Contractual Necessity):**
        - *Purpose:* "Creation and maintenance of your user profile as an [Product Name] platform administrator."
        - *Processing Activity:* "Storage of First Name, Last Name, Corporate Email in the Meridian platform database."
        - *Legal Basis per Art. 6(1)(b):* "Processing necessary for the performance of a contract to which the data subject is party."
    - **Consent Record B (Mandatory - Legal Obligation):**
        - *Purpose:* "Processing of Corporate Email for mandatory security notifications and breach communications."
        - *Processing Activity:* "Use of Email by the Meridian CISO automated notification system."
        - *Legal Basis per Art. 6(1)(c):* "Processing necessary for compliance with a legal obligation to which the controller is subject."
    - **Consent Record C (Conditional - Legitimate Interest):**
        - *Purpose:* "To receive targeted onboarding guidance and product feature best-practices based on your assigned Meridian SAM's analysis."
        - *Processing Activity:* "Profiling of platform usage by Meridian Product Management to suggest workflow optimizations."
        - *Legal Basis per Art. 6(1)(f):* "Processing necessary for the purposes of the legitimate interests pursued by the controller."
        - *Opt-Out Mechanism:* "You have the right to object to this processing. A clear 'Reject' button is presented."
    - **Consent Record D (Optional - Explicit Consent):**
        - *Purpose:* "Receipt of Meridian quarterly product newsletter and updates."
        - *Processing Activity:* "Storage of email in the Marketo marketing automation platform."
        - *Legal Basis per Art. 6(1)(a) & Recital 32:* "Explicit consent of the data subject."
        - *Withdrawal Mechanism:* "Consent may be withdrawn at any time via a link in the footer of every communication."
2.  **Data Subject Rights Acknowledgment:** The OneTrust form explicitly presents the data subject with a plain-language list of their rights as established under GDPR Chapter 3 (Articles 12-23), including the right to access (Art. 15), rectification (Art. 16), erasure (Art. 17), restriction of processing (Art. 18), data portability (Art. 20), and the right to object (Art. 21). It provides the direct email address for the Meridian Data Protection Officer (DPO): `dpo@meridianhealthtech.com`.
3.  **Record of Processing Activities (ROPA) Update:** Upon successful submission of the consent form, the `GDPR_Consent_Log` table in ServiceNow is automatically updated. The Meridian Data Privacy Officer (DPO) is responsible for ensuring this automated feed correctly populates Article 30 Records of Processing Activities on a monthly review cycle.
4.  **DPA Acceptance:** The CDCF includes a mandatory "Click-to-Accept" button for the Meridian Standard Data Processing Agreement (DPA), incorporating the current Standard Contractual Clauses (SCCs) for cross-border data transfers. The metadata (timestamp, IP address, user-agent, Meridian DPA version number) is recorded and immutably stored in the `Legal_Acceptance_Log` in ServiceNow. The COS is explicitly blocked from proceeding to Phase 3 if the DPA acceptance record is NULL.
5.  **Right of Erasure (Art. 17) Operational Procedure:** If a Customer Administrator exercises their right of erasure during onboarding, the COS will log a `DSAR_ERASURE` task. This will automatically trigger the Meridian Data Engineering team to delete the specified CPD from all active systems, backups, and logs within a strict 30-calendar-day Service Level Agreement (SLA), a detailed report of erasure actions being sent to the DPO and data subject.

### 5.3 Phase 3: Technical Environment Configuration (Lead Time: 5 Business Days)
Upon successful DPA acceptance, the ServiceNow workflow advances to the "Provisioning" state, assigning a `ProvisionRequest` task to the designated Onboarding Engineer.

1.  **Infrastructure as Code (IaC) Execution:** The Onboarding Engineer executes the `meridian-tenant-provisioner` IaC pipeline from AWS CodeCommit. The pipeline is parameterized with the `ONB-XXXXX` case ID, the desired AWS region, and the product SKU. The pipeline provisions:
    - A new isolated AWS Organization Unit (OU) within the Meridian Control Tower Landing Zone.
    - Product-specific AWS accounts (e.g., `prod-clinicalai-cust123`, `prod-medinsight-cust123`).
    - Base networking infrastructure: VPCs, private/public subnets, AWS Transit Gateway attachments.
    - **HIPAA Control:** A standard set of AWS Config Rules that automatically monitor and report on PHI environmental controls. The base Config rule `PHI_STORAGE_BUCKET_ENCRYPTED` is deployed to verify all designated S3 buckets are encrypted with `AES-256-CMK`. AWS CloudTrail is configured for all accounts with Organization Trail, logging to a central, immutable S3 bucket. The Onboarding Engineer validates these controls are active before proceeding.
2.  **Network Connectivity Provisioning:**
    - **AWS PrivateLink (Default Option):** The Onboarding Engineer creates an Endpoint Service for the Meridian SaaS console and APIs, registering these behind a Network Load Balancer (NLB) in the service account. The Customer is required to create an Interface VPC Endpoint in their AWS account, granting Meridian’s service account access via an endpoint policy. The Customer’s AWS Account ID is a required, validated parameter.
    - **Site-to-Site VPN (Alternate Option):** A `tgw-vpn-attachment` stack is provisioned. The Onboarding Engineer works with the Customer's Network Administrator to establish IKEv2 Phase 1 and Phase 2 parameters using Certificate-based Mutual Authentication. Pre-Shared Key (PSK) option is strictly prohibited.
3.  **MedInsight Analytics Data Loader Configuration (If Applicable):** For MedInsight customers, a dedicated AWS DMS (Database Migration Service) replication instance is provisioned. An AWS Glue Crawler role is established with an initial restrictive IAM policy scoped to the Customer’s designated data landing zone S3 bucket only.

### 5.4 Phase 4: Federated Access & RBAC Configuration
1.  **SAML/SCIM Federation Setup:** The Onboarding Engineer and Security Engineer collaborate with the Customer’s IdP Administrator. Meridian supports SAML 2.0-based SSO integration and optional SCIM 2.0 for automated user lifecycle management.
    - **SOC 2 Control:** A formal technical integration document (`FED-INTEGRATION-CHKLST_v2.1`) is completed, capturing Entity ID, ACS URL, and certificate thumbprints. Meridian requires SAML assertions to include a mandated `urn:oid:1.3.6.1.4.1.5923.1.1.1.6` (eduPersonPrincipalName) or equivalent persistent, non-reassignable attribute that uniquely identifies the principal. The connection is tested against a non-production staging environment before being promoted to production.
2.  **Provisioning of Initial RBAC Groups:** The COS provides the Onboarding Engineer with a structured, pre-approved `Default RBAC Matrix` based on the purchased products.
    - `GRP-PA-GLOBAL-ADMIN` (PA: Platform Administrator)
    - `GRP-PA-CLINICIAN-READER`
    - `GRP-PA-FINANCE-REPORTER`
    - `GRP-PA-INTEGRATOR-API`
    The Onboarding Engineer maps these Meridian groups to the SAML assertion attributes provided during federation. The initial administrative users, designated in the CDCF, are assigned to the `GRP-PA-GLOBAL-ADMIN` group upon first successful SSO login.
3.  **Access Validation:** The COS validates that the designated Customer Administrators can successfully authenticate via SSO, access their Meridian console, and perform actions commensurate with their `GRP-PA-GLOBAL-ADMIN` privileges.

### 5.5 Phase 5: Final Validation and Handoff
1.  **Control Implementation Checklist:** The Onboarding Engineer completes the `Control_Implementation_Checklist` in ServiceNow. This is a SOC 2 operational control artifact. The checklist must evidence:
    - Completion of AWS CloudTrail and VPC Flow Log enablement.
    - Configuration of GuardDuty threat detection service across all provisioned accounts.
    - Confirmation of AWS Backup vault policies and a successful initial snapshot.
    - Verification that all CloudWatch alarms required by the incident response runbook are in an "OK" state.
2.  **Incident Response Plan Integration:** The new environment’s ARNs and identifiers are programmatically registered into the Meridian centralized On-Call Incident Management Platform (PagerDuty). The COS explicitly provides the Customer’s Technical Lead with the designated email (`incident-notification@meridianhealth.io`) and portal URL for reporting security events. A document outlining the incident response process is attached to the case.
3.  **Security Incident Notification Procedure:** In the event of a confirmed security incident involving the loss or unauthorized access of Customer Data, the Meridian SOC Commander will immediately declare a `SEV-1` incident. The SAM will serve as the primary customer communication liaison. The SOC Commander will provide a preliminary notification to the Customer via the contact details in the CDCF within four (4) hours of incident confirmation, adhering to breach notification obligations as defined in the MSA.
4.  **Transition to Steady State (Handoff to CSM):** The COS conducts a formal, 30-minute "Production Handoff" call with the CSM, SAM, and the Customer’s Technical Lead. During this call, the COS reviews the completed `Control_Implementation_Checklist`, confirms the environment is fully operational, and formally closes the `ONB-XXXXX` ServiceNow case. The CSM then takes ownership of the relationship per SOP-CSM-001.

---

## 6. Controls and Safeguards

Meridian implements a layered defense strategy of technical and administrative controls to safeguard the onboarding process.

### 6.1 Data Protection Controls
- **Encryption at Rest:** All CPD and Customer Data is encrypted at rest by default using AES-256. AWS Key Management Service (KMS) Customer Managed Keys (CMKs) with enforced annual rotation are used for all S3 buckets, RDS instances, and EBS volumes. No data is stored in plaintext.
- **Encryption in Transit:** All communication between the Customer and the Meridian Platform is encrypted using TLS 1.3. Internal micro-service communication is authenticated via mutual TLS (mTLS) within the service mesh.
- **Data Minimization Schema:** The CDCF (`CDCF_FORM_V3.0`) is a locked, auditable template. The form creator role is restricted to the Director of Customer Operations and the DPO. Any addition of a data field to this form requires a formal Privacy Impact Assessment (PIA) review and DPO approval ticket in ServiceNow.
- **Access Reviews:** User access to the production AWS environments is governed by a quarterly access review process. A designated Security Engineer audits all IAM roles and policies against the Meridian Access Certification Matrix. The results are reported to the CISO.

### 6.2 Identity and Access Controls
- **Multi-Factor Authentication (MFA):** All Meridian Personnel must use hardware-based (U2F/FIDO2) or time-based one-time password (TOTP) software tokens to access Meridian’s management plane, regardless of network location.
- **Privileged Access Management (PAM):** Direct SSH or RDP access to any production system by an Onboarding Engineer is prohibited. All administrative actions are routed through an audited, proxy-based Privileged Access Management (PAM) gateway (CyberArk) that implements session recording and keystroke logging.
- **Segregation of Duties for Change Management:** All promotions from the non-production staging environment to the production environment are executed via a formal Request for Change (RFC) ticket in ServiceNow. The RFC must be submitted by the Onboarding Engineer. The approval must be granted by a different individual – a designated Lead Engineer or Security Engineer – before the IaC pipeline will execute the `deploy-production` playbook. This provides segregation between implementation and authorization. The pipeline is programmatically prevented from accepting the approval if the submitter and approver are the same Person Unique Identifier (PUID).

### 6.3 Operational Controls
- **Ticketing System:** Every step from initiation to handoff is tracked within the ServiceNow `ONB-XXXXX` case. The workflow engine enforces mandatory fields and sequential completion gates.
- **Change Management:** The `meridian-tenant-provisioner` IaC pipeline is version-controlled and subject to a code review process. A peer code review approval is required before a Pull Request (PR) from a feature branch, representing the Onboarding Engineer's change, can be merged into the `main` branch.
- **Incident Response:** The incident response plan, referenced in Section 5.5, details the process for containment, eradication, and recovery. It identifies the Security Engineering Director as the Incident Commander for any event involving unauthorized access. The plan details playbooks for common attack vectors, including DDoS, ransomware, and data exfiltration, and references the Customer-specific notification procedures.

---

## 7. Metrics, Monitoring, and Reporting

The effectiveness and compliance of the Customer Onboarding process are measured against a set of defined Key Performance Indicators (KPIs) and monitored via a real-time operational dashboard in Tableau (`ONB_Executive_Dashboard_v3`).

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | Metric Name | Definition | Target | Measurement Period |
| :--- | :--- | :--- | :--- | :--- |
| **KPI-ONB-01** | **Median Time to Onboard** | The median number of business hours from Phase 1 initiation (MSA signed) to Phase 5 handoff (ServiceNow case closure). | ≤ 65 Bus. Hours | Rolling 90-day |
| **KPI-ONB-02** | **GDPR Consent Capture SLI** | The percentage of ServiceNow cases where the OneTrust consent form timestamp is successfully recorded within 4 hours of CDCF receipt. | **≥ 99.5%** | Instantaneous |
| **KPI-ONB-03** | **DSAR Response Compliance** | The percentage of Article 17 (Right to Erasure) DSARs fulfilled within the mandated SLA during the onboarding window. | **100.0%** | Per-DSAR |
| **KPI-ONB-04** | **Infra Provisioning Success** | The percentage of IaC pipeline executions that succeed on the first attempt without manual intervention. | ≥ 95.0% | Monthly |
| **KPI-ONB-05** | **Handoff Satisfaction (CSAT)** | A post-handoff CSAT survey sent to the Customer Technical Lead. The CSAT score is the average score of three questions on a 1-5 Likert scale. | Average Score ≥ 4.4 | Monthly |

### 7.2 Reporting Cadence
- The Director of Customer Operations reviews the `ONB_Executive_Dashboard` every Monday at 09:00 ET.
- A formal Monthly Customer Operations Review is presented to the VP of Customer Operations, VP of Financial Services, and the CISO. This review includes a deep-dive on all KPI exceptions and an analysis of all customer-reported issues during the onboarding phase.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types
An exception is defined as any deviation from the procedural steps or automated guardrails defined in Section 5. Common exception types include:
- **Technical Exception:** Customer requires a connectivity method or infrastructure topology not supported by the standard IaC pipeline (e.g., a non-AWS cloud connection).
- **Operational Exception:** Customer requests a non-standard RBAC group with granular permissions that deviate from the Default RBAC Matrix.
- **Legal Exception:** A prospective EU customer’s DPO requests negotiation of a specific contractual clause outside the Standard DPA.

### 8.2 Exception Handling Process
1.  **Identification:** The COS or Onboarding Engineer identifies the exception and creates a ServiceNow case task of type `Risk/Exception` associated with the parent `ONB-XXXXX`.
2.  **Documentation:** The requestor documents the exact nature of the exception, the business justification, and the proposed mitigating control within the `Exception_Description` field.
3.  **Technical Assessment:** The Onboarding Engineer provides a technical impact assessment.
4.  **Security Review:** A Security Engineer adds a threat analysis of the proposed exception.
5.  **Data Privacy Review:** If the exception involves a change to the CDCF data schema or a deviation in data processing location, the Meridian DPO is a required approver.

### 8.3 Approval Matrix
The approval authority for an onboarding exception is determined by its cumulative risk score, calculated in ServiceNow.

| Calculated Risk Score | Approver Role(s) |
| :--- | :--- |
| **Low ( < 2.5 )** | Director of Customer Operations |
| **Medium ( 2.5 – 3.4 )** | VP of Customer Operations + Security Engineering Director |
| **High ( ≥ 3.5 )** | VP of Customer Operations + CISO + DPO (if data privacy related) |

The `ONB` workflow is blocked from proceeding until all required approvals per the exception risk matrix are captured in ServiceNow.

---

## 9. Training Requirements

All Personnel assigned to the roles defined in Section 3.0 are required to complete specific, measurable training before being granted access to any production system or ServiceNow workflow to onboard a customer.

### 9.1 Initial Onboarding
A prospective Onboarding Engineer or Customer Operations Specialist has a 90-calendar-day probationary period. Before independently working on a live `ONB-XXXXX` case, the trainee must:
1.  **SOP-COPS-002 Certification:** Obtain the "SOP-COPS-002 v3.0 Certified" badge in Workday Learning by passing an online, proctored quiz with a score of 100% on questions related to GDPR consent capture procedure (Phase 2) and the RBAC configuration procedure (Phase 4).
2.  **Shadowed Onboarding Completion:** Successfully shadow a Senior Onboarding Engineer for a minimum of two (2) complete full-cycle customer onboardings from Phase 1 to Phase 5, with the Senior Engineer logging the successful shadowing tasks in ServiceNow.
3.  **Secure Coding Training:** Complete the annual "Meridian Secure Coding & Infrastructure Best Practices" course, covering IaC pipeline security, least-privilege IAM policy creation, and data handling best practices.

### 9.2 Annual Re-Certification
All active Onboarding personnel must re-certify annually by:
- Re-taking and passing the `SOP-COPS-002 v3.0 Certified` quiz, which receives a mandatory annual update reflecting procedural changes.
- Viewing and acknowledging the updated Meridian Information Security and Data Protection Policy.

Non-compliance with training requirements will result in the automatic revocation of access to the `meridian-tenant-provisioner` pipeline and the ServiceNow Onboarding workflow modules.

---

## 10. Related Policies and References

| Document Identifier | Document Title |
| :--- | :--- |
| **SOP-ITSM-003** | IT Service Management and Incident Handling |
| **SOP-INFRA-012** | Infrastructure Vulnerability and Patch Management |
| **SOP-SEC-101** | Information Security Policy |
| **SOP-LEG-004** | Data Privacy and Data Protection Impact Assessment (DPIA) Process |
| **MSA-TEMPLATE_v4.1** | Standard Master Services Agreement Template |
| **DPA-TEMPLATE_v3.0** | Standard Data Processing Agreement & SCCs |
| **RBAC-MATRIX_v2.0** | Meridian Platform Default Role-Based Access Control Matrix |
| **ISO 27001:2022** | Information security, cybersecurity and privacy protection |
| **AICPA TSC 100** | 2017 Trust Services Criteria for Security, Availability, and Confidentiality |

---

## 11. Revision History

| Version | Date | Author | Description of Change |
| :--- | :--- | :--- | :--- |
| **1.0** | 2024-08-15 | J. Stanton | Initial document creation and approval. Basic workflow for Clinical AI Platform on US East only. |
| **2.0** | 2025-01-10 | M. Chang | Major revision to incorporate HealthPay Financial Services and MedInsight Analytics products. Added multi-region provisioning pipeline logic. Transitioned CDCF to ServiceNow. |
| **2.1** | 2025-09-22 | A. Kapoor | Minor revision. Updated DPA references to version 3.0 incorporating new EU SCCs. Updated DPO contact email. |
| **2.5** | 2026-02-14 | M. Chang | Refactored Phase 2 for alignment with AWS GovCloud onboarding requirements. Added Phase 4 RBAC Matrix integration. Added KPI-ONB-03 for DSAR response. |
| **3.0** | 2026-05-22 | M. Chang, R. Liu | Comprehensive rewrite for multi-tenant architecture. Added detailed SOC 2 and GDPR operational controls. Introduced automated consent orchestration via OneTrust integration. Enhanced Section 6 controls on PAM and IaC segregation of duties. |