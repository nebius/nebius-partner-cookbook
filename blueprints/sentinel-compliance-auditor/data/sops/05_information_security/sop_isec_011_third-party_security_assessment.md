---
sop_id: "SOP-ISEC-011"
title: "Third-Party Security Assessment"
business_unit: "Information Security"
version: "4.2"
effective_date: "2025-01-19"
last_reviewed: "2026-05-25"
next_review: "2026-11-11"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Third-Party Security Assessment

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, governance, and operational processes for assessing, tiering, onboarding, and continuously monitoring the security posture of all third-party vendors, suppliers, and service providers engaged by Meridian Health Technologies, Inc. ("Meridian"). The purpose of this SOP is to ensure that third-party relationships do not introduce unacceptable risk to Meridian's information assets, systems, or regulated data, and to provide reasonable assurance to stakeholders, auditors, and regulators that a consistent, risk-based due diligence process is applied across the vendor lifecycle.

### 1.2 Scope

This SOP applies to all third parties that access, process, store, transmit, or have the potential to impact the confidentiality, integrity, or availability of Meridian's systems and data, including but not limited to Protected Health Information (PHI), personally identifiable information (PII) subject to the General Data Protection Regulation (GDPR), payment card data, proprietary algorithms, and critical infrastructure configurations.

Specifically, this SOP covers:

| Category | Examples | Applicable Business Units |
|---|---|---|
| Cloud Service Providers | Infrastructure-as-a-Service, Platform-as-a-Service, Software-as-a-Service hosting PHI | All |
| Clinical AI Data Partners | Training data licensors, annotation services, external model validation firms | Clinical AI Platform |
| Financial Services Partners | Credit bureaus, loan origination platforms, payment gateways, collections agencies | HealthPay Financial Services |
| Professional Services | Consultants, penetration testers, auditors with logical access to Meridian assets | All |
| Subprocessors | Downstream vendors engaged by Meridian's primary vendors that handle regulated data | All |
| Hardware/Firmware Suppliers | Medical device components, IoT sensors for clinical environments | Clinical AI Platform |
| Open-Source Software Maintainers | Critical dependencies in clinical AI or financial services pipelines | Engineering |

This SOP applies to:

- All Meridian employees, contractors, and temporary personnel who initiate, manage, or renew third-party vendor relationships.
- The Information Security team, which acts as the central assessment and approval function.
- Legal, Privacy, Compliance, and Procurement teams involved in vendor contract review.

This SOP does not apply to:

- Software libraries consumed under standard open-source licenses without direct vendor relationships, which are governed by the **Secure Software Development Lifecycle Policy (SOP-SDL-004)** .
- Government-mandated data sharing not involving contractual vendor agreements, covered under **Law Enforcement Data Request Procedures (SOP-LEG-009)** .

### 1.3 Regulatory Alignment

This SOP is designed to support Meridian's obligations under multiple regulatory frameworks. The specific alignment per framework is detailed throughout the document, but summarized here:

- **SOC 2 (Service Organization Control 2):** Addresses the Common Criteria series related to logical and physical access controls, system operations, and change management. The vendor risk management program serves as a key control within Meridian's system of controls over the availability and processing integrity of the Meridian SaaS Platform.
- **HIPAA (Health Insurance Portability and Accountability Act):** Addresses the requirement to obtain satisfactory assurances via Business Associate Agreements (BAAs) and conduct due diligence on vendors handling electronic Protected Health Information (ePHI). Procedures herein support administrative safeguards related to security management and evaluation.
- **GDPR (General Data Protection Regulation):** Thoroughly addressed. Articles 28 (Processor), 30 (Records of Processing Activities), 32 (Security of Processing), 44-49 (International Data Transfers), and 46 (Appropriate Safeguards) are directly operationalized through the detailed procedures, data protection impact assessments (DPIAs), and contractual mandates described in this SOP.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
|---|---|
| **Vendor** | Any external third-party legal entity engaged by Meridian under contract. Synonymous with "Supplier," "Service Provider," and "Processor" in the GDPR context. |
| **Subprocessor** | A fourth-party entity engaged by a Meridian vendor to assist in processing regulated data, as defined under GDPR Article 28(2). |
| **BAA** | Business Associate Agreement, as required by HIPAA 45 CFR § 164.504(e). |
| **DPA** | Data Processing Agreement, as required by GDPR Article 28. |
| **SCC** | Standard Contractual Clauses, a transfer mechanism under GDPR Article 46(2)(c) for cross-border data flows. |
| **TISAX** | Trusted Information Security Assessment Exchange; a standardized automotive/manufacturing security assessment occasionally used for hardware suppliers. |
| **SIG** | Standardized Information Gathering Questionnaire, a widely-used third-party risk assessment tool maintained by Shared Assessments. |
| **CAIQ** | Consensus Assessments Initiative Questionnaire, a standardized security assessment for cloud providers published by the Cloud Security Alliance (CSA). |
| **Tier** | Risk classification assigned to a vendor (1, 2, or 3), determining the depth and frequency of the security assessment. |
| **RTO** | Recovery Time Objective: the target duration of time required to restore a service following a disruption. |
| **RPO** | Recovery Point Objective: the maximum acceptable amount of data loss measured in time. |
| **ePHI** | Electronic Protected Health Information, as defined by HIPAA. |
| **ISMS** | Information Security Management System, Meridian's overarching governance framework. |
| **VRM** | Vendor Risk Management module within Meridian's OneTrust GRC platform. |

---

## 3. Roles and Responsibilities

The RACI (Responsible, Accountable, Consulted, Informed) matrix below defines the roles for all phases of the third-party security assessment lifecycle.

| Activity | Information Security (Vendor Risk Team) | Business Unit Relationship Owner | Legal & Privacy | Procurement | CISO (Rachel Kim) | CEO (Dr. Sarah Chen) |
|---|---|---|---|---|---|---|
| **Initiation & Business Case** | I | **R/A** | | I | | |
| **Security Questionnaire Dispatch** | **R/A** | C | | | | |
| **GDPR Art. 30 ROPA Update** | C | **R/A** | C | | | |
| **Contractual Review (Art. 28, BAA)** | C | C | **R/A** | C | | |
| **Risk Tier Determination** | **R/A** | C | C | | | |
| **Technical Security Assessment** | **R/A** | I | | | C | |
| **Final Risk Acceptance (Tier 3)** | **A** | R | | | I | |
| **Final Risk Acceptance (Tier 1 & 2)** | R | C | C | | **A** | I |
| **Exception Approval (High Risk)** | C | R | C | | **A** | **I** |
| **Ongoing Monitoring & Re-Assessment** | **R/A** | I | | | | |

**Specific Roles:**

- **Chief Information Security Officer (CISO), Rachel Kim:** Owner of this SOP. Approver of all Tier 1 vendor engagements and any risk acceptance for vendors rated "High Risk." Has unilateral authority to suspend or terminate a vendor's logical access in the event of a confirmed material breach.
- **Vendor Risk Manager (Information Security):** Responsible for the day-to-day execution of this SOP. Manages the assessment queue, reviews completed questionnaires, performs technical validation of vendor claims, and maintains the vendor risk register within OneTrust VRM.
- **Data Protection Officer (DPO), Legal Department:** Consulted on all matters related to GDPR Article 35 (DPIA) requirements triggered by a vendor engagement. Reviews and approves all international data transfer mechanisms (SCCs, Binding Corporate Rules) before contract execution.
- **Business Unit Relationship Owner:** The Meridian employee who initiates the vendor engagement. Responsible for identifying the business need, completing the initial Vendor Intake Form, and serving as the primary liaison between the vendor and Meridian's assessment teams.

---

## 4. Policy Statements

Meridian Health Technologies is committed to a risk-based approach to managing security throughout the lifecycle of all third-party relationships. The following policy statements establish mandatory requirements.

### 4.1 Mandatory Assessment
No vendor that processes, stores, or transmits Meridian regulated data, or has logical or physical access to Meridian's production networks (including the `MHT-PROD` and `MHT-CLINICAL-COMPUTE` environments), may be granted such access without first completing a security assessment commensurate with its assigned risk tier.

### 4.2 Formalized Risk Tiering
All vendors must be classified into one of three tiers based on the inherent risk of the engagement. The tiering must consider data sensitivity (GDPR special categories, ePHI, PCI), access criticality, and business impact if the vendor's services were compromised or disrupted. The tiering criteria are fully operationalized in Section 5.2.

### 4.3 Contractual Mandate
No services requiring a security assessment may commence before a fully executed contract is in place that includes appropriate security and privacy schedules. This contract must include, at minimum, a HIPAA Business Associate Agreement (BAA) if the vendor will interact with ePHI, and a robust GDPR-compliant Data Processing Agreement (DPA) as specified under Article 28. The DPA must define the subject matter, duration, nature, and purpose of processing, the types of personal data, and categories of data subjects.

### 4.4 Right to Audit
Contracts with Tier 1 and Tier 2 vendors must include a "Right to Audit" clause, allowing Meridian or a nominated independent auditor to evaluate the vendor's compliance with contractual security obligations. For cloud service providers, reliance on a recognized third-party attestation (e.g., SOC 2 Type II, ISO 27001:2022) assessed annually is an acceptable alternative.

### 4.5 Subprocessor Authorization
Vendors handling Meridian personal data under GDPR must not engage any Subprocessor without prior, specific, written authorization from Meridian, as mandated by Article 28(2). A mechanism for general written authorization with a mandatory 30-day notification period for changes is the standard, but Meridian reserves the right to require specific authorization for Subprocessors handling special categories of data.

### 4.6 Breach Notification
All contractual agreements must include a clause requiring the vendor to notify Meridian's CISO and DPO of any actual or reasonably suspected security incident impacting Meridian data within 24 hours of discovery, with a detailed preliminary report within 72 hours. This aligns with the breach notification requirements under GDPR Articles 33 and 34.

---

## 5. Detailed Procedures

This section outlines the end-to-end operational procedures. The Vendor Security Assessment lifecycle consists of five distinct phases: Intake, Tiered Assessment, Remediation and Risk Acceptance, Onboarding, and Continuous Monitoring.

### 5.1 Phase 1: Intake and Pre-Screening

**5.1.1 Vendor Request Initiation**
The Business Unit Relationship Owner initiates the process by submitting a **Vendor Security Assessment Request (VSAR)** form, accessible via the OneTrust VRM self-service portal. The VSAR captures critical context:
- Vendor legal name, corporate address, and primary contact.
- Description of the intended service and business justification.
- Identification of all types of data Meridian will share or the vendor may access (schemas: GDPR Personal Data, GDPR Special Category Data, ePHI, PCI, Proprietary Algorithms).
- Anticipated logical access (e.g., VPN, API key, direct database query, access to MHT Azure Tenant Subscription `ClinicalAI-Prod`).
- Anticipated physical access, if any, to Meridian facilities.

**5.1.2 Preliminary Conflict Check**
Legal conducts a rapid conflict-of-interest check within 2 business days of VSAR submission. Simultaneously, the Information Security team checks the VRM database for any previously terminated relationships with the vendor due to security concerns.

### 5.2 Phase 2: Risk Tiering and Assessment Depth

Upon VSAR approval, the Vendor Risk Manager assigns a preliminary risk tier within 3 business days. The tiering matrix uses quantitative scoring where feasible.

**5.2.1 Inherent Risk Scoring**

| Factor | Weight | Score 1 (Low) | Score 3 (Medium) | Score 5 (High) |
|---|---|---|---|---|
| Data Sensitivity | 40% | Public/non-sensitive data | PII (non-Special Category) | ePHI, GDPR Special Category, PCI, Trade Secrets |
| Access Criticality | 30% | Isolated, non-prod access | Access to internal dev/test | Access to `MHT-PROD`, `MHT-CLINICAL-COMPUTE`, or CI/CD pipelines |
| Availability Impact | 20% | Non-critical ancillary service | Service disruption impacts non-critical workflows | Service disruption directly impacts patient safety, claims processing, or diagnostics |
| Vendor Custodial Role | 10% | Data processor, Meridian holds keys | Co-managed environment | Data controller or exclusive data steward; Meridian has limited visibility |

**Inherent Risk Score = (0.4 × Data Sensitivity) + (0.3 × Access Criticality) + (0.2 × Availability Impact) + (0.1 × Custodial Role)**

**5.2.2 Tier Assignment**

| Tier | Inherent Risk Score | Definition | Assessment Depth |
|---|---|---|---|
| **Tier 1 (High)** | > 4.0 | Vendors hosting critical regulated data (ePHI, Special Category GDPR data), with privileged logical access, or upon whom business continuity is dependent. | Comprehensive: Full on-site/virtual audit, detailed SIG questionnaire, penetration test review, DPIA trigger. |
| **Tier 2 (Medium)** | 2.0 - 4.0 | Vendors with limited regulated data or access. Standard SaaS vendors hosting PII. Data processors under GDPR that are not Tier 1. | Enhanced: Standard SIG or CAIQ, SOC 2 Type II review, privacy shield/supplement review. |
| **Tier 3 (Low)** | < 2.0 | Vendors with negligible data exposure, no logical access, or provision of non-critical commodities. | Standard: Self-assessment questionnaire, policy acknowledgment. |

### 5.3 Phase 3: Risk Assessment Execution

The depth of this phase is strictly governed by the assigned Tier.

#### 5.3.1 Tier 3 (Low-Risk) Assessment

- **Questionnaire:** Vendor completes a condensed Meridian Security Self-Assessment (20 questions) covering basic administrative, physical, and technical safeguards.
- **Review:** The Vendor Risk Manager validates responses within 5 business days.
- **Outcome:** Pass/Fail. No conditional remediation; failures result in rejection of the vendor.

#### 5.3.2 Tier 2 (Medium-Risk) Assessment

The Tier 2 assessment introduces rigorous artifact collection and is the baseline for any vendor processing personal data under GDPR.

**Step 1: Standardized Information Gathering (SIG) Questionnaire**
Vendors must complete the Meridian-curated SIG questionnaire, comprising approximately 250 questions mapped to NIST SP 800-53r5, ISO 27001:2022, and specific GDPR Article 32 controls. The questionnaire is digitally delivered and tracked via OneTrust.

**Step 2: Evidence Collection**
Vendors must provide the following minimum set of artifacts:
- **SOC 2 Type II Report:** Annual or most recent report covering the Trust Services Criteria relevant to the Meridian engagement.
- **Summary of Information Security Policy:** Documented policy demonstrating alignment with ISO 27001 or equivalent.
- **Data Flow Diagram:** Detailed mapping of how Meridian data transits through the vendor's infrastructure, explicitly marking any cross-border data flows.
- **Business Continuity Plan Summary:** A document attesting to the existence of a plan that addresses service continuity.

**Step 3: Technical Review**
The Vendor Risk Manager and a designated Security Architect (for technical integrations) review the questionnaire against the submitted evidence for consistency. Specific focus areas:

- **GDPR Art. 32 Technical Measures:** Evidence of encryption at rest (e.g., AES-256) and in transit (TLS 1.2+), pseudonymization techniques used, and documented vulnerability management program. Timelines: Critical vulnerabilities must be patched within 14 days; High within 30 days, as per Meridian's **Vulnerability Management Standard (SOP-ISEC-008)** .
- **Resilience Assessment:** The vendor's Business Continuity Plan is reviewed to ensure it addresses the vendor's availability commitments to Meridian. The plan is assessed for its logical coherence in restoring service following a prolonged region-wide cloud outage.
- **Access Control Model:** The vendor's access control model must demonstrably prevent unauthorized access to Meridian data. The reviewer examines logical access controls, including multi-factor authentication enforcement and role-based access. The reviewer confirms that the vendor attests to having a robust join-mover-leaver process for their own staff.

**Step 4: Privacy Review (GDPR-specific)**
The DPO reviews the DPA, Data Flow Diagram, and Subprocessor list against GDPR requirements:

- **Article 28(3) DPA Content:** Meridian's standard DPA is the default starting point. The DPO verifies it accurately specifies processing details (Annex I of DPA).
- **Article 44-49 Transfer Mechanism:** If the vendor's Data Flow Diagram shows Meridian data transiting or being stored outside the European Economic Area (EEA), the mechanism (e.g., EU SCCs Module 2 for controller-to-processor transfers) must be fully executed by contract signature.
- **Article 28(4) Subprocessors:** The vendor's Subprocessor list is reviewed. If a Subprocessor also handles Meridian personal data, the vendor's contract with that Subprocessor must pass on equivalent data protection obligations. The DPO has 10 business days to raise an objection to a Subprocessor.
- **Article 35 DPIA:** A Data Protection Impact Assessment (DPIA) is triggered for any Tier 2 engagement using new technology or where processing, due to its nature, scope, or purposes, is likely to result in a high risk to data subjects. The Business Unit owner, in consultation with the DPO, completes the DPIA using the Meridian template **TEMPLATE-LEG-DPIA-01**, which must be signed off by the DPO.

**Outcome:** A final report is generated with one of three designations:
- **Approved:** No critical or high-risk findings.
- **Conditionally Approved:** Remediation plan for Medium-risk findings agreed upon with timelines not exceeding 90 days. Vendor cannot onboard until the Conditional Acceptance Plan (**FORM-ISEC-011-CAP**) is co-signed.
- **Rejected:** Critical or High-risk findings where the vendor is unwilling or unable to remediate within 30 days.

#### 5.3.3 Tier 1 (High-Risk) Assessment

All Tier 2 steps apply, supplemented by the following:

- **On-Site or Deep-Dive Virtual Audit:** An Information Security team member, or a nominated independent assessor on Meridian's behalf, conducts a focused assessment of physical and environmental controls, key management ceremonies, and live operations.
- **Targeted Penetration Test:** If the vendor develops software for Meridian or hosts a custom API, Meridian may request or conduct a targeted penetration test of the specific service interface.
- **Code Security Review:** For vendors contributing critical code to the Clinical AI Platform, a static application security testing (SAST) or software composition analysis (SCA) report for their specific codebase components must be provided.
- **Resilience and Recovery Objectives Interview:** The assessment includes a detailed interview with the vendor's technical operations lead. While a well-architected business continuity plan is required, the assessment focuses on the vendor's process for declaring a disaster, the failover architecture pattern (active-active vs. active-passive), and the documented communication plan, rather than specific, numerically quantified RTO/RPO guarantees in the contract.
- **Logical Access Review:** The vendor's model for logical access control is architecturally reviewed, with a focus on how privileged roles are secured and managed. The engagement with Meridian mandates strict Role-Based Access Control (RBAC) with a quarterly review of accounts by the vendor's operations team.

### 5.4 Phase 4: Remediation and Risk Acceptance

If risk findings are identified that exceed Meridian's risk threshold, the Vendor Risk Manager enters the Remediation phase.

**5.4.1 Remediation Plan Agreement**
The vendor must submit a formal remediation plan detailing corrective actions, owners, and target dates. A deadline binding by contract is set. For Tier 1 and 2 vendors, standard remediation deadlines are:
- **Critical Findings:** 15 calendar days.
- **High Findings:** 45 calendar days.
- **Medium Findings:** 90 calendar days.

**5.4.2 Risk Acceptance**
If a finding cannot be remediated within the standard timeline, the Business Unit Relationship Owner may initiate a **Security Exception Request**, detailed in Section 8. Risk acceptance for Tier 1 vendors related to ePHI or GDPR special category data always flows to the CISO and General Counsel for joint sign-off.

### 5.5 Phase 5: Contract Finalization and Onboarding

No technical connection, API key issuance, or data transfer occurs until the Security Assessment is complete and all required contractual schedules are fully executed.

**5.5.1 Contractual Enforcement Gates**
The OneTrust VRM workflow enforces a gating mechanism:
1.  **Security Assessment:** Status must be "Approved" or "Conditionally Approved" with signed CAP.
2.  **Legal Review:** Contract main body and all schedules are finalized.
3.  **Privacy Review:** DPA/SCCs fully executed.
4.  **BAA Review:** HIPAA BAA fully executed if ePHI is in scope.
5.  **Procurement:** Final signature and Purchase Order (PO) issued.

Only upon gate satisfaction does the IT/Engineering team receive an automated ticket via ServiceNow (**SNOW-PROC-ISEC-011-ONBOARD**) to provision access.

---

## 6. Controls and Safeguards

This section articulates the specific administrative and technical controls, aligned to regulatory requirements, that constitute the Third-Party Security Assessment program.

### 6.1 Vendor Inventory and ROPA Management

- **Control VEND-01 (GDPR Art. 30):** A centralized, up-to-date record of all vendors processing personal data subject to GDPR is maintained in the OneTrust VRM module. This serves as a sub-component of the Meridian Records of Processing Activities (ROPA). For each vendor, the record contains: name and contact details of the processor, categories of processing carried out, and a reference to the executed transfer mechanism (e.g., SCCs).
- **Control VEND-02 (SOC 2):** An inventory of all vendors supporting the Meridian SaaS Platform is maintained. For each, the type of service, contractual availability commitment, and the vendor's notification process for planned downtime or service outage are documented.

### 6.2 Access Controls and Minimum Necessary Access

- **Control VEND-03 (Access Control):** Vendor access to Meridian systems is granted using a dedicated, named account per authorized individual; shared vendor accounts are prohibited. Access is granted via Meridian's Identity Governance and Administration (IGA) platform (SailPoint) and must use Multi-Factor Authentication (MFA).
- **Control VEND-04 (HIPAA Minimum Necessary):** The access provisioning ticket, as per the service catalog, requires the Meridian Business Unit Owner to specify the exact job role of the vendor's user. The IGA team then provisions access based on a pre-defined Role Profile scoped to facilitate the principle of least privilege as technically feasible within the target application. The role profile is designed to give the minimum necessary access to perform the contracted services.
- **Control VEND-05 (Privileged Access Management):** Any vendor access requiring elevated privileges (e.g., `sudo`, SQL `sysadmin`) must be brokered through the CyberArk Privileged Access Manager. Such sessions are recorded and audited post-hoc by the Information Security team upon access revocation or quarterly for active accounts.

### 6.3 Audit Controls and Logging

- **Control VEND-06 (HIPAA Audit Controls):** All vendor activity within Meridian's production environment housing ePHI is captured by SIEM solutions (Splunk). Meridian's Splunk forwarders are configured to collect all authentication, authorization, and data access events. Log integrity is maintained.
- **Control VEND-07 (Monitoring):** A dedicated Meridian Security Operations Center (SOC) analyst reviews high-fidelity alerts generated from vendor-related activities. For Tier 1 vendors, a weekly summary report of all vendor actions is generated and reviewed by the SOC Lead.

### 6.4 Vendor Resilience and Incident Response

- **Control VEND-08 (Incident Response Integration):** Tier 1 and Tier 2 vendor incident response contact lists are maintained and tested during annual cross-functional tabletop exercises. The vendor's incident notification obligations, aligning with GDPR Article 33, are embedded in every Tier 1/Tier 2 contract.
- **Control VEND-09 (Vendor Service Level Monitoring):** Meridian's Application Performance Monitoring (APM) tool (Dynatrace) synthetically monitors critical Tier 1 vendor service endpoints from within Meridian's network. The monitoring is configured to alert on availability drops below the vendor's documented Service Level Agreements (SLAs), triggering a breach notification to the Vendor Risk Manager and Business Unit Relationship Owner.

### 6.5 Privacy and Data Protection Specific Controls

- **Control VEND-10 (GDPR Art. 28(8) Audit Rights):** Meridian retains the right to audit the vendor, either through its own internal audit team or a qualified independent third party, upon 30 days' notice. This right is invoked at least every 36 months for Tier 1 processors and ad-hoc in response to a material security incident.
- **Control VEND-11 (GDPR Art. 28(3)(e) Data Subject Rights):** The contractually agreed DPA explicitly obligates the vendor, in its role as a processor, to assist Meridian, the controller, in fulfilling its obligations to respond to Data Subject Access Requests (DSARs), rectifications, erasures, and restrictions of processing. A specific 7-calendar-day SLA is mandated for the vendor to provide all necessary information to Meridian's Privacy team upon a DSAR request routed to the vendor's data.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Ongoing Vendor Performance Monitoring

Continuous monitoring is conducted on a risk-tier cadence:

| Tier | Continuous Monitoring Cadence (Automated) | Manual Artifact Review Cycle |
|---|---|---|
| Tier 1 | Daily (endpoint health, API availability) | **Every 6 months**, plus triggered by material business, technical, or security changes in the vendor's environment. |
| Tier 2 | Weekly (availability check) | **Annually**. The Vendor Risk Manager reviews the vendor's latest SOC 2 report bridge letter or equivalent. |
| Tier 3 | None | **Biennially** or upon contract renewal (whichever is sooner). A re-confirmation of the self-assessment questionnaire is requested. |

Automated monitoring is executed via Meridian's security ratings platform (BitSight), which continuously analyzes externally observable security posture (e.g., botnet infections, open ports, patching cadence). A 50-point drop in a Tier 1 vendor's BitSight rating automatically triggers an immediate Out-of-Cycle Review.

### 7.2 Key Performance and Risk Indicators (KPIs/KRIs)

Reported monthly to the CISO and quarterly to the Audit Committee:

| Metric | Target | Current (Placeholder) | Regulatory Alignment |
|---|---|---|---|
| **Vendor Risk Due Diligence Completion** | >95% of active Tier 1 and Tier 2 vendors assessed within policy timelines. | 97% | SOC 2 CC4.2 |
| **High-Risk Vendors by Tier** | ≤10% of all active Tier 1 and Tier 2 vendors rated "High Risk". | 8% | General ISMS |
| **Overdue Remediation Actions** | <8 overdue high/critical remediation tasks at any time. | 3 | GDPR Art. 32 |
| **Vendors Without Executed DPA/SCCs** | 0 for vendors processing EU personal data. | 0 | GDPR Art. 28, 46 |
| **Security Exception Aging** | All exceptions reviewed within their approved validity period (max 12 months). | 100% reviewed. 2 Exceptions past 9 months old. | SOC 2 CC8.1 |

### 7.3 Reporting Cadence

- **Monthly:** Operational KRI dashboard shared with VP of Security Operations.
- **Quarterly:** "State of Third-Party Risk" report from CISO to the Executive Risk Committee, summarizing new Tier 1 assessments, high-risk vendor details, and exception status.
- **Annually:** Summary report of the entire program, performance against KPIs, and results of control testing provided to external SOC 2 auditors.

---

## 8. Exception Handling and Escalation

### 8.1 Security Exception Requests

Any situation where a vendor cannot meet a mandatory procedural or technical control requirement before the contract effective date necessitates a formal Security Exception.

**Procedure:**
1.  **Initiation:** The Business Unit Relationship Owner completes a **Third-Party Security Control Exception Request** form (**FORM-ISEC-011-EXCP**), documenting:
    - The specific policy or control requirement being waived.
    - The business justification for the exception.
    - A compensating control, if applicable.
    - The proposed expiration date for the exception (maximum validity: **12 months**).
2.  **Security Review:** The Vendor Risk Manager assesses the risk, documenting the potential impact and likelihood. A formal risk score is added to the VRM tool.
3.  **DPO Consultation (GDPR Data):** Any exception involving a vendor processing personal data subject to GDPR requires mandatory review and sign-off from the Data Protection Officer.
4.  **Approval Authority:**
    - **Tier 3 Vendor, Low-Risk Finding:** Approved by the Vendor Risk Manager and Legal.
    - **Tier 2 Vendor, Medium-Risk Finding:** Approved by the Head of Information Security Operations.
    - **Tier 1 Vendor, or any "High Risk" Finding:** Approved jointly by the CISO (Rachel Kim) and the General Counsel.

### 8.2 Escalation Path for Vendor Breach or Failure

If a vendor fails to meet their contractual security obligations, or a material breach of Meridian data occurs, the following escalation path is immediately invoked:

1.  **Immediate Action (Hour 0-2):** The Security Operations Center (SOC) Lead, upon confirmation, immediately suspends all logical network access for the implicated vendor accounts in Meridian's perimeter firewalls and the IAM platform.
2.  **Crisis Team Activation (Hour 1-3):** SOC Lead invokes the **Incident Response SOP (SOP-ISEC-007)** and escalates to the CISO. The CISO activates a Virtual Tiger Team consisting of the CISO, Vendor Risk Manager, Business Unit Relationship Owner, VP of Legal (DPO), and VP of Corporate Communications.
3.  **Executive Reporting (Hour 3-6):** The CISO briefs the CEO (Dr. Sarah Chen) on the estimated impact and containment status.
4.  **Regulatory Compliance (Hour 6-48):** The DPO evaluates and executes external notification obligations as per GDPR Article 33 (72-hour supervisory authority notification) and Article 34 (data subject notification), coordinating with the vendor to extract a detailed forensics timeline.

---

## 9. Training Requirements

### 9.1 Role-Based Training

All personnel assigned a role in this SOP must complete targeted training. Completion is tracked within Meridian's Litmos Learning Management System (LMS).

| Target Audience | Training Module | Frequency | Delivery Method |
|---|---|---|---|
| All Meridian Employees | Vendor Engagement Awareness | Annually, upon hire | 10-minute eLearning module (Litmos) |
| Business Unit Relationship Owners | Managing Third-Party Security Risk | Annually | 45-minute Instructor-Led (Virtual) |
| Information Security Team Members | Conducting a Third-Party Technical Assessment (Advanced SIG & Audit) | Annually | 2-hour hands-on workshop |
| Legal and Procurement | Contractual Privacy & Security Controls for Third Parties (Art. 28, SCCs, DPIA) | Annually | 1-hour Instructor-Led brief by DPO |

### 9.2 New-Hire Requirements
The "Vendor Engagement Awareness" module, part of the mandatory new-hire security curriculum, must be completed within 10 calendar days of an employee's start date. This module educates all staff on the prohibition of circumventing the TPSA process—specifically, the act of engaging a service that can access Meridian data using only a corporate credit card without a VSAR, colloquially termed "Shadow IT Vending."

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP-ID | Document Title | Relationship to This SOP |
|---|---|---|
| SOP-ISEC-007 | Security Incident Response Procedure | Defines steps to take during a vendor data breach. |
| SOP-PRIV-003 | Data Protection Impact Assessment (DPIA) Process | Procedure for handling the trigger events identified in this SOP. |
| SOP-SDL-004 | Secure Software Development Lifecycle (SSDLC) Policy | Governs security of open-source libraries not covered by this TPSA. |
| SOP-ISEC-003 | Access Management and Identity Governance Policy | Defines policies for provisioning logical access for vendors. |
| SOP-LEG-001 | Contract Management and Review Policy | Procedure for the legal lifecycle of a vendor agreement. |
| SOP-ISEC-008 | Vulnerability Management Standard | Establishes the patching timelines referenced in our vendor expectations. |

### 10.2 External Standards and Frameworks Referenced

- **ISO/IEC 27001:2022** — Information Security Management System
- **ISO/IEC 27036:2023** — Cybersecurity — Supplier Relationships
- **NIST Special Publication 800-53 Revision 5** — Security and Privacy Controls for Information Systems and Organizations
- **NIST Cybersecurity Framework (CSF) 2.0** — Govern and Identity pillars
- **CSA Enterprise Architecture & CAIQ v4.0.2** — Standardized questionnaire used for cloud vendor assessments
- **Shared Assessments SIG 2025** — Deep-dive risk assessment questionnaire

---

## 11. Revision History

| Version | Effective Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| 1.0 | 2021-06-01 | M. Ito, Dir. GRC | A. Vargas, CISO | Initial publication of formal Third-Party Security Assessment process. Mandated for all cloud and data-processing vendors. |
| 2.1 | 2022-11-15 | M. Ito, Dir. GRC | R. Kim, CISO (Interim) | Minor revision. Added TIAX framework for hardware suppliers. Updated SIG questionnaire version to 2022.4. |
| 3.0 | 2023-08-30 | R. Kim, CISO | Dr. A. Bell, CEO | Major revision. Introduced OneTrust VRM as the mandatory system of record. Created formal Tiering matrix with inherent risk scoring replacing subjective categorization. |
| 4.0 | 2025-01-19 | R. Kim, CISO | Dr. S. Chen, CEO | Full rewrite. Aligned to ISO 27001:2022 and updated GDPR Art. 28/46 requirements. Added detailed RACI, new KPI framework, and 12-month exception limit. Integrated with new Meridian ServiceNow onboarding workflow gate. |
| 4.1 | 2025-09-18 | B. Chang, Vendor Risk Mgr. | R. Kim, CISO | Periodic review update. Refined Tier 2 evidence list to accept ISO 27001 in lieu of SOC 2 for non-US data centers. Updated cross-references for new DPIA template (TEMPLATE-LEG-DPIA-01). |
| 4.2 | 2026-05-25 | R. Kim, CISO | Dr. S. Chen, CEO | Annual update. Enhanced ongoing monitoring section (7.1) to include BitSight integration. Updated escalation path in Section 8.2 with specific hourly triggers for new regulatory notification mandates. Minor clarifications to DPO responsibilities during exception handling. Updated external standards references to latest NIST revision. |