---
sop_id: "SOP-DGP-017"
title: "Privacy by Design and Default"
business_unit: "Data Governance & Privacy"
version: "5.6"
effective_date: "2025-09-06"
last_reviewed: "2026-04-24"
next_review: "2026-10-02"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "EU AI Act"
status: "Active"
---

# STANDARD OPERATING PROCEDURE
## Privacy by Design and Default
### SOP-DGP-017 | Version 5.6

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for embedding privacy and data protection into the design, development, and operation of all Meridian Health Technologies, Inc. products, services, and business processes. Privacy by Design and Default (PbD) is a foundational principle that ensures data protection is not an afterthought but a core architectural requirement, operationalized through the entire lifecycle of data processing activities.

This SOP operationalizes the principles set forth in Article 25 of the General Data Protection Regulation (GDPR), which mandates that data protection be integrated into processing activities from inception, ensuring that, by default, only personal data necessary for each specific purpose is processed. This obligation extends to the volume of data collected, the extent of processing, the period of storage, and accessibility.

### 1.2 Scope

This SOP applies universally across Meridian Health Technologies, Inc. and all its global offices (Boston, London, Berlin, Singapore, Toronto). Compliance is mandatory for all business lines and underlying platforms:

| Business Unit | Platform / Product | Key Data Types | PbD Applicability |
|---|---|---|---|
| Clinical AI Platform | AI-driven clinical decision support, diagnostic imaging (FDA 510(k)/CE Marked), patient risk scoring, adverse event prediction | PHI, genomic data, medical images | Full lifecycle (conception to decommissioning) |
| HealthPay Financial Services | Payment processing, patient financing, medical lending, claims automation | PII, financial account details, credit scores, PHI | Full lifecycle (collection to deletion) |
| MedInsight Analytics | Population health analytics, care gap identification, outcomes prediction | PHI for ~12M patients, aggregated health data | Full lifecycle (ingestion to anonymization/destruction) |
| Meridian SaaS Platform | Multi-tenant cloud infrastructure (AWS us-east-1, eu-west-1) | Metadata, access logs, configuration data | Platform-level controls, tenant isolation |

This SOP applies to:

- All employees, contractors, consultants, and third-party vendors who design, build, deploy, maintain, or manage products and services.
- All software development lifecycles (SDLC), including waterfall, Agile, DevOps, and CI/CD pipelines.
- All data processing activities, including collection, storage, use, transfer, and deletion of personal data.
- All technology stacks utilized across the organization (AWS, Azure DR, PyTorch, TensorFlow, Snowflake, Kafka, etc.).
- All new projects, significant product updates, and the integration of third-party components or acquired technologies.

### 1.3 Out of Scope

- Purely internal administrative processes that do not involve the processing of personal data (e.g., financial ledger entries without customer names).
- Isolated, non-networked legacy systems that are scheduled for decommissioning within 12 months, provided a decommissioning plan is approved by the Chief Privacy Officer, and no new data is ingested. (These systems are grandfathered under the legacy waiver SOP-DGP-025).

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Privacy by Design (PbD)** | An engineering and design philosophy where privacy and data protection controls are proactively embedded into the architecture and operational specifications of IT systems, business practices, and physical design from the initial stages. |
| **Privacy by Default** | The principle that the strictest privacy settings automatically apply once a customer acquires a new product or service, without any manual action required. No data is collected, used, or shared beyond what is strictly necessary for the specified purpose. |
| **Personal Data** | Any information relating to an identified or identifiable natural person (‘data subject’). An identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier, or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural, or social identity of that natural person (GDPR Art. 4(1)). |
| **Protected Health Information (PHI)** | Individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or medium, as defined by HIPAA. At Meridian, all PHI is also treated as a special category of personal data under GDPR. |
| **Data Protection Impact Assessment (DPIA)** | A process to systematically analyze, identify, and minimize the data protection risks of a project or processing activity, required under GDPR Art. 35 for high-risk processing. |
| **Legitimate Interests Assessment (LIA)** | A documented assessment demonstrating that a specific processing activity is necessary for the purposes of a legitimate interest, balanced against the rights and freedoms of the data subject (GDPR Art. 6(1)(f)). |
| **Data Minimization** | The principle that personal data shall be adequate, relevant, and limited to what is necessary in relation to the purposes for which they are processed (GDPR Art. 5(1)(c)). |
| **Pseudonymization** | The processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organizational measures (GDPR Art. 4(5)). |
| **Anonymization** | The irreversible process of transforming personal data so that the data subject is no longer identifiable. Once anonymized, data is no longer considered personal data and falls outside the scope of GDPR. |
| **Data Inventory** | A centralized, structured catalogue of all data assets, processing activities, and data flows maintained in the OneTrust platform. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **CPO/DPO** | Chief Privacy Officer / Data Protection Officer |
| **DPIA** | Data Protection Impact Assessment |
| **LIA** | Legitimate Interests Assessment |
| **PbD** | Privacy by Design and Default |
| **PII** | Personally Identifiable Information |
| **PHI** | Protected Health Information |
| **ROPA** | Record of Processing Activities |
| **SDLC** | Software Development Lifecycle |
| **PRB** | Privacy Review Board |
| **TIA** | Transfer Impact Assessment |
| **ISMS** | Information Security Management System (ISO 27001:2022) |
| **VPAT** | Voluntary Product Accessibility Template |

---

## 3. Roles and Responsibilities

The following RACI matrix (Responsible, Accountable, Consulted, Informed) defines the roles and responsibilities for the execution of this SOP.

| Activity / Deliverable | CPO/DPO (Dr. Klaus Weber) | Product Manager / Engineer (VP David Park, VP Dr. Aisha Okafor) | CISO (Rachel Kim) | Business Unit VP (Liu/ Okafor/ Chang) | General Counsel (Maria Gonzalez) | Data Governance Committee | Engineers & Developers |
|---|---|---|---|---|---|---|---|
| **SOP Policy Ownership & Updates** | A, R | C | C | I | C | I | I |
| **Embedding PbD in SDLC** | C | A | C | I | I | I | R |
| **Conducting DPIA** | A | C | C | C | C | I | R |
| **Approving Privacy Review Gates** | A | C | I | I | C | R | I |
| **Implementing Default Settings** | C | A | C | I | I | I | R |
| **Approving Data Retention Schedules** | A | C | I | R | C | I | I |
| **Vendor Privacy Assessments** | C | I | C | A | C | R | I |
| **Privacy Training Completion** | I | I | I | A (CHRO Walsh) | I | I | R |
| **Managing Data Subject Rights (DSRs)** | A | I | I | I | C | I | R (Privacy Ops) |

**Key Role Descriptions:**

- **Dr. Klaus Weber, Chief Privacy Officer / DPO:** Acts as the ultimate authority on all matters related to this SOP. Has a direct reporting line to the CEO and the Board-level AI Governance Committee. Chairs the Privacy Review Board. Veto power over any product or feature that violates PbD principles.
- **Business Unit VPs (Dr. Aisha Okafor, Robert Liu, Michael Chang):** Accountable for ensuring their respective product teams comply with PbD requirements. They must allocate sufficient budget, time, and resources for privacy engineering within their roadmaps.
- **VP of Engineering (David Park):** Accountable for the technical implementation of PbD controls across all engineering teams. This includes managing the privacy tech stack (OneTrust Integration, Vault tokenization patterns, etc.).
- **CISO (Rachel Kim):** Responsible for ensuring that the technical security controls required for data protection (encryption, access management, logging) are available, properly configured, and aligned with SOC 2 and ISO 27001 standards.
- **General Counsel (Maria Gonzalez):** Provides legal interpretation of GDPR, HIPAA, and contractual obligations. Approves high-risk processing exceptions.

---

## 4. Policy Statements

Meridian Health Technologies is committed to the following high-level policy statements, which form the non-negotiable pillars of our Privacy by Design and Default framework. A breach of these policies by any employee or contractor may result in disciplinary action, up to and including termination and legal proceedings.

### 4.1 Proactive not Reactive; Preventative not Remedial

Privacy risks shall be identified and mitigated during the design phase, not after a breach or incident occurs. Every project must commence with a clear privacy-risk assessment. The cost of remediating a privacy flaw post-deployment is a business risk that must be avoided.

### 4.2 Privacy as the Default Setting

No individual shall be required to take manual action to protect their privacy. The following default settings are mandated for all Meridian systems and products:

- **Purpose Specification:** The specific, explicit, and legitimate purpose for processing must be established and communicated at the point of collection.
- **Collection Limitation:** Only the minimum necessary personal data shall be collected. The amount of data collected must be proportionate to the service offered.
- **Use, Retention, and Disclosure Limitation:** Personal data shall not be used, retained, or disclosed for purposes other than those specified, unless a new lawful basis is established and communicated via clear privacy notice updates.
- **Storage Limitation:** Personal data shall be retained only for the duration defined in the Meridian Data Retention Schedule (SOP-DGP-022). Automated deletion mechanisms must be the default for non-archival storage.

### 4.3 Privacy Embedded into Design

Privacy must be an integral component of the core functionality — a design feature, not an add-on. The architecture of all Meridian platforms, especially the multi-tenant SaaS platform, must guarantee tenant data isolation.

### 4.4 Full Functionality — Positive-Sum, not Zero-Sum

Meridian shall accommodate business imperatives and security/privacy requirements simultaneously. The pursuit of innovation (e.g., advanced clinical AI algorithms) must proceed with robust pseudonymization and privacy engineering to avoid the false dichotomy between privacy and product utility.

### 4.5 End-to-End Security — Lifecycle Protection

All personal data must be securely protected throughout its lifecycle: from collection through processing, storage, transfer, and ultimate destruction. Strong cryptographic standards (AES-256 at rest, TLS 1.3 in transit) are non-negotiable unless a formal cryptographic exception is approved by the CISO and CPO.

### 4.6 Visibility and Transparency

Meridian’s processing activities must be transparent to data subjects, regulators, and auditors. All processing must be documented in a legally compliant, up-to-date Record of Processing Activities (ROPA) maintained in OneTrust.

### 4.7 Respect for User Privacy

The rights of the data subject (Access, Rectification, Erasure, Restriction, Portability, Objection) must be engineered into the platform. Human-factors engineering shall ensure that consent management interfaces are clear, unambiguous, and non-deceptive.

---

## 5. Detailed Procedures

This section outlines the operational procedures for integrating PbD into the Meridian product and software development lifecycle. All phases are mandatory for Major/Critical projects; Minor projects may use the abbreviated checklist.

### 5.1 Phase 0: New Initiative Ideation & Privacy Framing

Before any code is written or any Jira ticket is created for a new initiative, the Product Manager must complete the "Phase 0 – Privacy Framing Document" (Template: TMP-DGP-017-01).

**Procedure:**
1.  **Initiate Framing:** The Product Manager creates a new record in OneTrust's "Privacy by Design" module.
2.  **Define the Purpose:** Document the specific, explicit, and legitimate business purpose. Vague purposes are rejected by the OneTrust workflow engine.
3.  **Identify Data Flows:** Map out the proposed data flow (Conceptual Data Flow Diagram). Identify ingress points (e.g., HL7 ingestion, user input, API calls), storage locations (e.g., AWS S3, Snowflake), and egress points.
4.  **Lawful Basis Identification:** Select the applicable lawful basis for processing.
    - **Clinical AI (EU MDR):** The lawful basis is typically GDPR Art. 6(1)(c) (legal obligation) in conjunction with Art. 9(2)(i) (public health), given the CE marking. However, for US data, a HIPAA Business Associate Agreement (BAA) governs.
    - **HealthPay:** GDPR Art. 6(1)(b) (contractual necessity) for payment execution; Art. 6(1)(f) (legitimate interest) for fraud prevention — requires a specific LIA.
    - **MedInsight Research:** Often relies on explicit consent (Art. 9(2)(a)) or Art. 89(1) safeguards for research. If relying on legitimate interest, the LIA is mandatory.
5.  **Risk Pre-Screening:** Answer the automated risk questionnaire (derived from the European Data Protection Board guidelines for high-risk processing). If the screening flags criteria like "use of new technologies," "automated decisions with legal effects," or "large-scale special category data," the system automatically triggers a full DPIA workflow (see Section 5.3).
6.  **Assignment:** The CPO/DPO office receives notification and assigns a Privacy Analyst to the initiative within **2 business days**.

### 5.2 Phase 1: Requirements & Specification (Privacy by Default Settings)

During the Product Requirements Document (PRD) and System Design Document (SDD) phase, privacy requirements must be written as specific, testable acceptance criteria. The Privacy Analyst works with the Product Manager to specify the default settings.

**Procedure for Mandatory Default Settings:**
1.  **Consent Defaults:** If the lawful basis is consent (e.g., optional MedInsight patient-reported outcomes), the default for all processing toggles must be **OFF**. Pre-ticked checkboxes are strictly prohibited per GDPR Recital 32 & Art. 7.
2.  **Retention Defaults:** The default retention period must be the shortest operational necessity, not the longest regulatory limit. For example, if a clinical data retention law allows 20 years, but the operational need is 5 years, the system default must be 5 years with a justified, documented trigger for extension. Retention rules are coded as YAML configurations in the code repository.
3.  **Granularity of Preferences:** Privacy preference centers must not force bundled consent. "Clinical Data Processing" must be separable from "Marketing Communications" and "AI Model Training" where consent is the lawful basis.
4.  **Geo-Specific Defaults:** The platform must detect user location (by IP/geolocation API) and set defaults accordingly. EU IP addresses must default to the strictest GDPR (Art. 44) international transfer restrictions (e.g., EU-only data storage for specific buckets) unless a documented derogation applies.
5.  **Access Control Defaults (RBAC):** In MedInsight, PHI views must default to "Masked/De-identified" for all analyst roles. Unmasked views require "Break-Glass" emergency access protocol logging per SOP-ISMS-003.

### 5.3 Phase 2: Deep-Dive Privacy Risk Assessment (DPIA)

If the Phase 0 pre-screening flags high risk, a full DPIA is mandatory per GDPR Art. 35. This is a formal review process, not a generic checklist.

**Step-by-Step Procedure:**
1.  **Launch DPIA:** The Privacy Analyst initiates the DPIA template within OneTrust, linking it to the original initiative record.
2.  **Stakeholder Workshop:** The Analyst schedules a **90-minute workshop** with the following mandatory attendees: Product Manager, Lead Engineer, Data Architect, CISO (or delegate), and a representative from the Legal team.
3.  **Systematic Description:**
    - Nature and scope of processing (the "What").
    - Context of processing (the "Where" and "Why" — e.g., Clinical AI running in a hospital PACS integration).
    - Purposes (the "Why").
    - Technical and organizational measures (the "How").
4.  **Identify Assets and Vendors:** Catalogue all internal and third-party components. Confirm vendor DPAs are in place. If a vendor is unassessed, this triggers a Vendor Privacy Assessment (SOP-VMO-004).
5.  **Assess Necessity and Proportionality:**
    - Is the processing necessary for the purpose? Could a less intrusive method be used (e.g., pseudonymized data instead of directly identifiable data)? This is a critical gate. *If the Lead Engineer cannot justify the necessity of an intrusive piece of data, the requirement must be removed.*
6.  **Risk Analysis (Threat Modeling):**
    - Identify specific threats to the rights and freedoms of data subjects (e.g., loss of confidentiality, unauthorized re-identification, financial harm from HealthPay breaches).
    - Evaluate likelihood and severity using the Meridian Risk Matrix (5x5 scale: Negligible, Minor, Moderate, Significant, Severe).
7.  **Risk Mitigation:** For every identified risk categorized as "Moderate" or above, specific controls must be defined, assigned to an engineer for implementation, and linked to a test case for QA validation.
8.  **Sign-off:** The DPIA must be signed off by the Product Manager, the CPO (or delegate), and the CISO. If a "Severe" residual risk remains, the DPIA escalates to the General Counsel and the Board-level AI Governance Committee for consultation with the supervisory authority per Art. 36(1).

### 5.4 Phase 3: Privacy Architecture & Engineering Implementation

This phase translates design requirements into technical reality. VP of Engineering (David Park) is the operational gatekeeper.

**5.4.1 Encryption Standards (Art. 32 Security of Processing):**
- **At Rest:** All data stores (AWS RDS, S3 buckets, Snowflake volumes) containing personal data must use AES-256 encryption. AWS KMS keys must be managed with strict separation of duties; engineers cannot access production keys.
- **In Transit:** All API gateways (e.g., Apigee), load balancers, and internal microservice communication must enforce TLS 1.3 or mTLS.
- **Key Rotation:** All encryption keys must be automatically rotated every 180 days. Manual rotation is prohibited except during forensic investigations under the authority of the CISO.

**5.4.2 Pseudonymization and Tokenization:**
- **Meridian Vault (HashiCorp):** All direct identifiers (Name, email, Social Security Number (SSN), Medical Record Number (MRN)) must not be stored in the primary application database (e.g., PostgreSQL). Instead, the application must store a token pointing to the record locked in the Meridian Vault.
- **Pseudonymization for AI/ML:** Before Clinical AI model training datasets leave the secure production boundary and move to the research sandbox, identifiers must be replaced with pseudonyms. The pseudonymization key map must be stored in a separate, highly restricted Vault cluster controlled by the Data Governance Committee, not the AI team.

**5.4.3 Consent & Preference Management:**
Meridian uses the OneTrust platform as the central consent and preference repository. The engineering implementation must:
- Register the synchronous "Consent Check" API call in the application flow before data processing begins.
- Cache the consent status (with a TTL of no more than 1 hour) to ensure the system respects updated user preferences in near-real-time.
- Implement a mechanism for users to withdraw consent as easily as they gave it. A "Withdraw Consent" link must be visible in all user interfaces.

### 5.5 Phase 4: Privacy Review Gates (Go/No-Go)

Moving to the next SDLC phase requires passing a Privacy Review Gate. No gate can be skipped via a "fast-follow" methodology without a formal exception (Section 8).

**Gate 1: Requirements to Design (PRD → SDD)**
- *Check:* Default settings defined? DPIA initiated (if required)? Lawful basis validated?
- *Audience:* Product Manager, Privacy Analyst.
- *Tool:* OneTrust "Gate 1 Review" digital form.

**Gate 2: Design to Development (SDD → Sprint Start)**
- *Check:* Architecture reviewed for data minimization? Pseudonymization strategy documented? Threat modeling complete for high-level risks?
- *Audience:* Lead Engineer, Privacy Analyst, Security Architect.

**Gate 3: Development to Testing (Code Complete → QA)**
- *Check:* Static Application Security Testing (SAST) scans pass? OneTrust API integrations verified? Unit tests for privacy-specific functionality (e.g., consent logic) written and passing?
- *Audience:* Lead Engineer, QA Lead.

**Gate 4: Testing to Production Release (QA → Prod)**
- *Check:* Dynamic Application Security Testing (DAST) scans clear? DPIA mitigation controls validated in staging environment? Penetration test (for Major projects) confirms no PII leaks?
- *Audience:* Product Manager, Engineering Director, Privacy Analyst. **This is a hard gate. The Privacy Analyst must give explicit "Approved" status in OneTrust before the CI/CD pipeline can deploy to production.** For the Clinical AI Platform, this must include validation of privacy controls during the clinical validation phase.

### 5.6 Data Subject Rights (DSR) Engineering (GDPR Chapter III)

All business units must design their data architecture to facilitate the fulfillment of DSRs within the **strict 30-day (one-month) SLA** mandated by GDPR Art. 12(3).

**Operational Steps for Engineering:**
1.  **Access (Art. 15):** Build a capability to compile all data linked to a specific data subject UUID across all data stores (S3, RDS, Snowflake). This requires a master data management (MDM) search capability, not manual sweeps.
2.  **Rectification (Art. 16):** Users must be able to correct inaccurate data. For Clinical AI, this must follow clinical governance pathways (corrections handled formally, not simply overwritten).
3.  **Erasure (Right to be Forgotten — Art. 17):** Automated deletion scripts must be able to cascade deletion across all non-archival systems. Data stored in immutable ledgers (e.g., HealthPay blockchain components) must be addressed via irreversible pseudonymization (nulling the token) to effectively "erase" the linkage to the data subject.
4.  **Portability (Art. 20):** Data must be exportable in a structured, commonly used, and machine-readable format (JSON or CSV). APIs for portability must be available for HealthPay and Clinical AI patient portals.

The Privacy Operations team, housed under the CPO, manages intake, identity verification, and fulfillment of DSRs via a custom workflow in OneTrust. The SLA clock starts upon identity verification. Automated alerts must notify the DPO if an SLA is at risk of breach (amber alert at **Day 20**, red alert at **Day 28**).

### 5.7 Vendor and Procurement Privacy

Third-party code and SaaS vendors are a major vector for privacy breaches. Before any vendor is integrated, the procurement workflow must complete a Privacy Vendor Review.

1.  **Trigger:** A purchase order for software or services that will touch personal data.
2.  **Assessment:** The Business Unit VP sends a Vendor Privacy Questionnaire (based on the Standard Data Protection Clauses). The vendor must provide their DPA, SOC 2 Type II report, and ISO 27001 certificate.
3.  **Review:** The Data Governance Committee reviews the vendor's data handling practices. For high-risk vendors (e.g., an AI model provider ingesting PHI), a joint DPIA may be required with the vendor.
4.  **Contracting:** The Data Processing Agreement (DPA) must be signed before any data is shared. The DPA must incorporate the Standard Contractual Clauses (SCCs) for international transfers, as approved in V5.3 of the Meridian Template Legal Agreements.

---

## 6. Controls and Safeguards

Meridian implements a multi-layered defense model of technical and administrative controls to enforce this SOP.

### 6.1 Technical Controls

| Control Category | Specific Control | Tool / System | Standard |
|---|---|---|---|
| **Encryption** | Envelope encryption for S3, RDS, DynamoDB. Transparent Data Encryption (TDE) on all SQL databases. | AWS KMS, HashiCorp Vault | AES-256-GCM |
| **Access Control** | Principle of Least Privilege. Role-based access (RBAC) with quarterly recertification. Just-in-time (JIT) access for privileged roles. | Okta (SSO, MFA, Lifecycle Management), Teleport (session recordings) | Zero Trust Architecture |
| **Data Loss Prevention (DLP)** | Pattern-based scanning for PII/PHI on endpoints, email, and SaaS transfers. Blocking policy for unencrypted PII in emails to external domains. | CrowdStrike Falcon, Microsoft Purview | Block exfiltration of 10+ matched PII records |
| **Pseudonymization** | Tokenization for names, SSNs, MRNs via API call. Secure lookup kept in isolated Vault cluster. | HashiCorp Vault (Transform Engine) | NIST SP 800-38G |
| **Audit Logging** | Immutable logs for all access to, modification, or deletion of personal data. Logs must be tamper-proof. | Splunk Enterprise (immutable buckets in S3) | SOC 2 CC3.1, CC3.2 |
| **Tenant Isolation** | Strict logical separation in the SaaS platform enforced via IAM Policies (Attribute-Based Access Control — ABAC). Physical separation for isolated hosting clients. | AWS Organizations, IAM Policies, Service Control Policies (SCPs) | Prevent cross-tenant data access |
| **Automated Deletion** | Cron jobs/Step Functions to delete data based on retention policies. No "soft-delete" permitted beyond 30-day recovery grace period. | Python scripts in AWS Lambda, triggered by CloudWatch Events | Automated enforcement of SOP-DGP-022 |

### 6.2 Administrative Controls

| Control | Description | Cadence |
|---|---|---|
| **Privacy Review Board (PRB)** | A standing body chaired by the CPO/DPO. Reviews high-risk DPIAs, exceptions, and major architectural changes. Membership: CPO, CISO, Chief Architect, Chief Medical Officer, a rotating Business Unit VP. | Bi-weekly |
| **Privacy Champions Network** | A designated senior engineer or architect from each Business Unit who acts as the privacy subject matter expert inside the scrum teams. They triage privacy issues before they reach the PRB. | Monthly Champion sync |
| **Policy Acknowledgment** | All staff must formally acknowledge this SOP and the Acceptable Use Policy annually. Non-acknowledgment results in immediate suspension of system access. | Annually (enforced via Okta HRIS integration) |
| **Data Inventory & Classification** | Automated scanning and manual registration in OneTrust to maintain a 100% up-to-date data map. Every data store must be classified (Public, Internal, Confidential, Restricted). | Continuous scanning / Monthly review |

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness of this PbD program is measured through a set of Key Performance Indicators (KPIs), presented on a real-time executive dashboard and reviewed formally.

### 7.1 KPI Dashboard (Powered by OneTrust Analytics & Splunk)

The CPO’s office maintains a dashboard accessible to the Leadership Team.

| Metric | KPI Target | Measurement Tool | Reporting Owner |
|---|---|---|---|
| **Privacy Review Gate Cycle Time** | Mean time to close Gate 4 (Dev to Prod) < 72 hours for Minor projects, < 5 Business Days for Major. | OneTrust | CPO |
| **DPIA Completion Timeliness** | 95% of DPIAs completed before project reaches Gate 2 (Design to Dev). | OneTrust | CPO |
| **Data Subject Request (DSR) SLA Compliance** | 99.5% of DSRs fulfilled within the 30-day GDPR window. | OneTrust (DSR Module) | Privacy Ops Lead |
| **Data Minimization Score** | Percentage of databases storing "Restricted" data where pseudonymization is active. Target > 95% for new builds. | Vault Audit Logs, OneTrust Data Inventory | CISO |
| **Vendor Privacy Compliance** | No active vendor processing personal data with an expired or missing DPA. Target: 100%. | OneTrust Vendor Risk Module | VP, Procurement |
| **Retention Compliance** | 0% of data past its defined retention limit without a legal hold. | Automated S3 lifecycle policy logs, Snowflake retention scripts | Data Governance Lead |
| **Training Completion Rate** | 100% of employees in scope (engineering, product, BI) completed mandatory PbD training. | Workday Learning | CHRO (Walsh) |

### 7.2 Reporting Cadence

| Report | Audience | Frequency | Format |
|---|---|---|---|
| **CPO Weekly Operations Report** | CPO, DGC | Weekly (Monday AM) | Automated email digest with breach-of-SLA alerts |
| **Privacy Program QBR** | CEO, Board AI Governance Committee | Quarterly | Formal slide deck, deep dive into 2-3 recent major DPIAs |
| **Annual GDPR Compliance Review** | Board of Directors, Auditors | Annually | Comprehensive report, audit findings, maturity scoring |

---

## 8. Exception Handling and Escalation

Privacy is not a barrier to business, but a risk discipline. Deviations from this SOP must be managed formally.

### 8.1 Exception Process

1.  **Identification:** The requesting party (e.g., a Product Manager needing to release a feature without passing Gate 4 due to market pressure) identifies the specific requirement of this SOP they cannot meet.
2.  **Formal Request:** Submit a "Privacy by Design Exception Request" form (TMP-DGP-017-02), which details:
    - The specific clause from which the exception is sought.
    - The compelling business justification.
    - A detailed risk assessment of the proposed non-compliant course of action.
    - Proposed compensating controls and a remediation plan with a fixed deadline (not to exceed 90 days).
3.  **Approval Workflow (via OneTrust):**
    - For **Minor Risk** exceptions (e.g., delay in a UX privacy notice update by 1 sprint): Approval by the Privacy Analyst and the Business Unit VP.
    - For **Moderate Risk** exceptions (e.g., temporary use of a pseudonymized dataset without a full DPIA): Approval escalates to the CPO.
    - For **Significant/Severe Risk** exceptions (e.g., bypassing encryption, releasing without consent defaults): Must be approved by the CPO *and* General Counsel. If it involves potential non-compliance with a specific GDPR Article, the General Counsel may mandate notification to the Supervisory Authority.
4.  **Escalation:** If an exception request is denied, the decision is final unless appealed to the CEO or Board AI Governance Committee. The CPO retains the absolute right to refuse any exception that constitutes an unacceptable risk to the rights and freedoms of Meridian’s data subjects.

### 8.2 Emergency Protocol

In a critical production incident requiring a hotfix that temporarily breaches a PbD control to restore service, the Incident Commander (per SOP-ISMS-001) and the CPO (or on-call delegate) have joint authority to approve a 24-hour emergency bypass. A post-incident review and a formal exception request (retrospective) must be filed within 72 hours.

---

## 9. Training Requirements

Meridian ensures that all personnel are competent to apply these PbD principles.

### 9.1 Role-Based Training Curriculum

| Role | Training Module | Provider | Frequency | Tracking System |
|---|---|---|---|---|
| **All Staff** | Global Data Protection & Privacy Essentials (includes GDPR Art. 25 overview) | Workday Learning | Annually | Workday |
| **Engineers & Architects** | Privacy Engineering & Secure Coding (PbD in SDLC, Vault patterns, DLP avoidance) | Safecode / internal DevSecOps portal | Annually | DevSecOps Portal (LMS Integration) |
| **Product Managers** | Privacy by Design for Product Owners (Risk ID, DPIA initiation, DSR requirements) | CPO Office / Online Workshop | At hire; biennial refresh | Workday |
| **Clinical AI & MedInsight Analysts** | Handling PHI for Research and Development (Art. 89, Anonymization vs. Pseudonymization protocols) | CPO & Legal | At hire; annual refresher | Workday |
| **Senior Leadership (VPs+)** | Executive Privacy Accountability Briefing | CPO/DPO (Dr. Klaus Weber) in person | Annually (Q1) | Signed Attendance Record |

Failure to complete mandatory training results in a 30-day suspension of access to restricted systems, enforced by Okta integration with the LMS. Repeated delinquency is grounds for formal HR performance review.

### 9.2 Phishing and Social Engineering
Given that privacy breaches are often caused by human error, mandatory quarterly simulated phishing exercises are conducted. Users who repeatedly click on simulated PHI-exfiltration emails are automatically enrolled in remedial privacy training.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title |
|---|---|
| SOP-ISMS-001 | Information Security Incident Response |
| SOP-ISMS-003 | Access Control Policy and Break-Glass Procedures |
| SOP-DGP-022 | Data Retention and Decommission Schedule |
| SOP-DGP-025 | Legacy System Waiver and Decommissioning |
| SOP-DGP-019 | Data Subject Rights Request Handling Standard |
| SOP-VMO-004 | Third-Party Vendor Security and Privacy Risk Assessment |
| SOP-CAI-041 | Clinical AI Model Development and Data Governance |
| SOP-SDD-001 | Secure Software Development Lifecycle |

### 10.2 External Legal and Regulatory References

- **Regulation (EU) 2016/679 (General Data Protection Regulation)**
    - Art. 5: Principles relating to processing of personal data
    - Art. 6: Lawfulness of processing
    - Art. 7: Conditions for consent
    - Art. 12: Transparent information, communication and modalities for the exercise of the rights of the data subject
    - Art. 15-20: Data Subject Rights (Access, Rectification, Erasure, Restriction, Portability)
    - Art. 25: Data protection by design and by default
    - Art. 32: Security of processing
    - Art. 35: Data protection impact assessment
    - Art. 36: Prior consultation
    - Art. 44-46: General principle for transfers, Transfers on the basis of an adequacy decision, subject to appropriate safeguards
- **Health Insurance Portability and Accountability Act (HIPAA) of 1996:** Privacy and Security Rules.
- **ISO 27701:2019:** Extension to ISO 27001 and ISO 27002 for privacy information management.
- **NIST Privacy Framework Version 1.0:** A tool for improving privacy through enterprise risk management.

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| 5.6 | 2026-04-24 | Dr. Klaus Weber (CPO) | Maria Gonzalez (GC) | **Major Review.** Updated Section 5.4.2 (Pseudonymization) to mandate new `vault-internal` vs `vault-ai` split for Clinical AI sandbox. Updated Section 7 metrics to reflect new vendor management module in OneTrust. Revised training module for Analysts on Art. 89. General language tightening for clarity. |
| 5.5 | 2025-11-15 | Dr. Klaus Weber (CPO) | Maria Gonzalez (GC) | **Minor Review.** Adjusted Phase 0 pre-screening questions to incorporate CE-marked MDR product launch learnings. Updated RBAC language in Section 5.2. Added 4-hour escalation SLAs for Privacy Ops in DSR Section 5.6. |
| 5.4 | 2025-09-06 | Dr. Klaus Weber (CPO) | Maria Gonzalez (GC) | **Comprehensive Update.** Full integration of the new OneTrust Privacy by Design module, replacing legacy Jira ticket workflows. Mandated new Data Inventory linking procedure. Updated the entire Gate review process (Section 5.5) to align with the new CI/CD pipeline architecture led by VP Engineering David Park. |
| 5.3 | 2024-12-02 | Privacy Program Manager | Dr. Klaus Weber (CPO) | **Organizational Update.** Updated RACI matrix to reflect the formation of the Data Governance Committee. Clarified roles of Privacy Champions in Section 6.2. |
| 5.2 | 2024-04-15 | Privacy Program Manager | Dr. Klaus Weber (CPO) | **Regulatory Alignment.** Updated cross-border data transfer controls (Section 5.6.4) post-Schrems II to align with the new EU SCCs adopted by Meridian Legal. Updated references to SOP-DGP-019. |

---

**End of Document: SOP-DGP-017**