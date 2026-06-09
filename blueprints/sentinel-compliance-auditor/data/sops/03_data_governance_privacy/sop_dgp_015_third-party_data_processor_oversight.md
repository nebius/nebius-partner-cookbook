---
sop_id: "SOP-DGP-015"
title: "Third-Party Data Processor Oversight"
business_unit: "Data Governance & Privacy"
version: "1.0"
effective_date: "2024-05-18"
last_reviewed: "2025-10-28"
next_review: "2026-04-07"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
  - "SOC 2"
status: "Active"
---

# SOP-DGP-015: Third-Party Data Processor Oversight

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes a unified, risk-based governance framework for the end-to-end oversight of all Third-Party Data Processors engaged by Meridian Health Technologies ("Meridian"). The purpose of this framework is to ensure that personal data—whether protected health information (PHI), personally identifiable information (PII), or clinical trial data—is processed in conformance with contractual obligations, internal privacy commitments, and the regulatory mandates of the jurisdictions in which Meridian operates. This SOP operationalizes Meridian's duty to select, contract, monitor, and decommission processors in a manner that preserves the confidentiality, integrity, and availability of data subjects' information throughout the processing lifecycle.

### 1.2 Scope

This SOP applies to all Meridian business units, subsidiaries, and joint ventures that engage, manage, or terminate relationships with Third-Party Data Processors (defined in Section 2) who receive, store, transmit, or otherwise process personal data on behalf of Meridian. In-scope engagements include, but are not limited to:

- **Cloud-Hosted Service Providers:** Infrastructure-as-a-Service (IaaS), Platform-as-a-Service (PaaS), and Software-as-a-Service (SaaS) vendors hosting Meridian's regulated data. This includes our primary clinical data lake hosted on AWS HealthLake, our patient engagement CRM (Salesforce Health Cloud), and our analytics environments (Databricks on Azure).
- **Business Process Outsourcers:** Third parties performing medical coding, claims adjudication, customer support call centers (e.g., our TeleHealth partner, Teladoc Health), and revenue cycle management.
- **Consulting and Professional Services:** Auditors, legal firms, penetration testing teams, and management consultants granted temporary logical access to Meridian's production or staging environments.
- **Sub-Processors:** Any entity engaged downstream by a primary processor, which gains logical or physical access to Meridian-originated data as a result of the primary processing agreement.
- **Clinical Research Organizations (CROs):** Entities contracted to manage, monitor, or analyze clinical trial data on behalf of Meridian's R&D division.

### 1.3 Application

This SOP applies to all new processor engagements initiated after the effective date, and all existing processor relationships will be brought into conformance during the annual contract renewal cycle or by the next scheduled audit, whichever occurs first.

### 1.4 Out of Scope

- Direct employment relationships with Meridian staff.
- Controllers with whom Meridian shares joint controllership but does not act as a processor.
- Partnerships where Meridian is itself acting as a processor for another Controller.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **Processor** | A natural or legal person, public authority, agency, or other body which processes personal data on behalf of the Controller (Meridian). |
| **Sub-Processor** | Another processor engaged by the primary Processor to carry out specific processing activities on behalf of Meridian. |
| **Data Processing Agreement (DPA)** | The legally binding contract between Meridian (Controller) and the Processor, articulating the subject-matter, duration, nature, and purpose of processing, the type of personal data, categories of data subjects, and the obligations and rights of the Controller. |
| **Protected Health Information (PHI)** | Individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or medium, as defined by the HIPAA Privacy Rule (45 CFR § 160.103). |
| **Business Associate Agreement (BAA)** | The contract required by the HIPAA Privacy Rule between a covered entity and a business associate, establishing the permitted and required uses and disclosures of PHI. |
| **Personal Data** | Any information relating to an identified or identifiable natural person (the "Data Subject"). |
| **Data Protection Impact Assessment (DPIA)** | A process designed to systematically analyze, identify, and minimize the data protection risks of a project or plan. |
| **Transfer Impact Assessment (TIA)** | A documented assessment of the laws and practices of a third country to determine if supplementary measures are needed to ensure data subjects' rights are protected. |
| **Third-Party Risk Management (TPRM)** | The enterprise-wide program for identifying, assessing, and mitigating risks associated with external entities throughout the relationship lifecycle. |
| **Standard Contractual Clauses (SCCs)** | Standard data protection clauses adopted by the European Commission for cross-border data transfers. |
| **NIST CSF** | National Institute of Standards and Technology Cybersecurity Framework. |
| **Data Governance Council (DGC)** | Meridian's executive steering committee responsible for data strategy and policy approval. |
| **Business Owner** | The Meridian department head who initiates the engagement and is the primary beneficiary of the services. |
| **SIG Lite** | Standardized Information Gathering Lite, a risk-assessment questionnaire based on industry standards used for lower-risk vendors. |

## 3. Roles and Responsibilities

The following matrix defines the accountability and consultative roles for the oversight lifecycle. A RACI model shall be applied for key process decisions.

| Role | Responsibility | RACI (Process: New Processor Onboarding) |
|---|---|---|
| **Chief Privacy Officer / DPO (Dr. Klaus Weber)** | Owner of the Processor Oversight program. Final escalation point for DPA disputes. Approves any derogations from data protection standards. | A - Accountable |
| **General Counsel (Maria Gonzalez)** | Approves all DPA legal terms. Signs off on risk acceptance for non-compliant clauses. Provides legal interpretation on cross-border data flows. | C - Consulted |
| **Chief Information Security Officer (CISO - Sarah Chen)** | Defines technical and organizational measures (TOMs) for security assessments. Manages the vendor security risk tiering matrix. Reviews SOC 2 Type II and ISO 27001 certificates. | R - Responsible (Security Assessment) |
| **VP Procurement (Raj Patel)** | Manages the commercial relationship, RFP processes, and cost negotiation. Ensures the DPA is executed before or concurrently with the Master Services Agreement (MSA). | R - Responsible (Sourcing) |
| **Data Governance Manager (Lisa Park)** | Maintains the record of processing activities (RoPA) entries for all processors. Tracks DPA renewal dates and conducts initial compliance checks on sub-processor disclosures. | R - Responsible (Administrative Tracking) |
| **Business Unit Owner (Various)** | Conducts the initial business justification. Defines the nature and purpose of processing. Acts as the primary point of contact for operational incident response. | C - Consulted |
| **Internal Audit** | Performs independent and objective reviews of the TPRM program effectiveness on a biennial basis. | I - Informed |

## 4. Policy Statements

Meridian is committed to transparent, secure, and lawful processing of personal data entrusted to us. The following high-level policy commitments govern all relationships with Third-Party Data Processors:

1.  **Accountability Principle:** Meridian remains fully accountable to Data Subjects and Supervisory Authorities for the processing carried out by its Processors. This includes the obligation to demonstrate compliance through appropriate documentation, audits, and contract clauses.
2.  **Data Minimization and Purpose Limitation:** Meridian shall engage Processors only for specified, explicit, and legitimate purposes. The data disclosed to a Processor must be adequate, relevant, and limited to what is necessary in relation to the purposes for which they are processed. Processors are contractually obligated not to process data for any secondary purpose without Meridian's explicit written consent.
3.  **Privacy by Design:** Meridian's procurement process mandates that privacy considerations be evaluated during the selection phase. A standardized Data Protection Impact Assessment (DPIA) screening questionnaire must be completed for all new high-risk processing activities prior to contracting.
4.  **Incident Response and Breach Notification:** Processors must contractually commit to notifying Meridian's Security Operations Center (SOC) without undue delay upon becoming aware of a Personal Data Breach. Meridian maintains a detailed Incident Response Plan (refer to SOP-SEC-022: Security Incident Response) which outlines the procedures for notifying Supervisory Authorities and Data Subjects. Notification to stakeholders must be executed with consideration of applicable timelines.
5.  **International Data Transfers:** Processing of personal data originating from the European Economic Area (EEA) or the United Kingdom in a third country is permitted only where the Processor provides appropriate safeguards, and on condition that enforceable data subject rights and effective legal remedies for data subjects are available. The Processor must assist Meridian in conducting a Transfer Impact Assessment (TIA). Transfers are governed by the terms laid out in the Data Processing Agreement, which contains relevant contractual data protection clauses.
6.  **Sub-Processing Chain Governance:** The establishment of a regulated sub-processing chain is mandatory. Processors must obtain Meridian's prior specific or general written authorization before engaging Sub-Processors. Where general authorization is granted, the Processor must maintain a public-facing repository of Sub-Processors and provide Meridian with a minimum 30-day advance notice of any intended changes, allowing Meridian an opportunity to object.

## 5. Detailed Procedures

This section outlines the procedural lifecycle of Processor Oversight, from initial selection through decommissioning.

### 5.1 Processor Selection and Initial Risk Tiering

Before any data transfer occurs, the potential Processor must be evaluated against Meridian's security and privacy posture. The Business Owner shall initiate a "New Vendor Request" within the Coupa Risk Assess platform.

1.  **Business Justification:** The Business Owner submits a Business Justification detailing the services required, the categories of data to be processed (e.g., PII, PHI, Clinical Trial Data), the volume of data subjects, and the anticipated geographic locations of processing.
2.  **Inherent Risk Scoring:** The TPRM module in Coupa automatically calculates an Inherent Risk Score (1-5) based on the Business Justification. Factors increasing risk include:
    - Processing of Special Category Data or PHI (+2 Risk Factor).
    - Processing Sensitive PII (SSN, Financial Data) (+1 Risk Factor).
    - Hosting outside Meridian's Azure tenant (+2 Risk Factor).
    - Direct logical access to Meridian systems (+3 Risk Factor).
3.  **Due Diligence Execution:** Based on the Inherent Risk Tier, the following is triggered:
    - **Tier 1 (Low Risk):** Automated NDA execution. Procurement sends a self-attestation questionnaire (SIG Lite).
    - **Tier 2 (Medium Risk):** TPRM initiates a formal RFI. CISO reviews SOC 2 Type II reports and penetration test summaries. DPO reviews privacy notice and DPA baseline.
    - **Tier 3 (High/Critical Risk):** Full RFP process involving Legal, CISO, and DPO. Mandatory onsite assessment or detailed virtual audit (via Teams/Webex) of the vendor's control environment. This is mandatory for any processor handling PHI or acting as a Cloud Service Provider for regulated workloads.

### 5.2 Data Processing Agreement (DPA) Execution

No personal data shall be exchanged until the DPA is fully executed. Meridian uses a standard DPA template (maintained by Legal in iManage) which serves as the baseline.

1.  **Template Selection:** Based on the data jurisdiction, select the appropriate baseline template:
    - **Global Template:** Used for most processors. Includes GDPR, CCPA, and general privacy clauses.
    - **HIPAA / BAA Template:** Required when PHI is present. This addendum is appended to the Global Template.
2.  **Key Clause Negotiation (Mandatory):** The following clauses are non-negotiable unless a formal Risk Acceptance is signed by the CISO and DPO:
    - Processing instructions (nature and purpose).
    - Confidentiality commitments for persons authorized to process.
    - Technical and Organizational Measures (TOMs).
    - Sub-Processor engagement terms.
    - Audit rights (including virtual and, for Tier 3, on-site physical access with 30 days' notice).
    - Data Breach Notification protocols.
    - Termination and data return/deletion procedures.
3.  **Contract Review Workflow:** The DPA draft is routed in Coupa:
    - **Step 1:** Legal review (Maria Gonzalez's team).
    - **Step 2:** CISO sign-off on TOMs (Sarah Chen).
    - **Step 3:** DPO approval (Dr. Klaus Weber).
    - **Step 4:** Procurement final execution via DocuSign.

### 5.3 Audit and Monitoring (Ongoing Governance)

Processor oversight does not end at contract execution. A continuous monitoring lifecycle is observed.

- **Annual Re-Assessment:** Every processor undergoes an automated Inherent Risk re-scoring on the anniversary of the contract. The DPA is reviewed to ensure it matches the evolving processing reality.
- **Remote Audit Evidence Collection:** For Tier 2 and 3 processors, Meridian collects evidence of control effectiveness biannually. This includes:
    - Latest SOC 2 Type II / ISO 27001 certificate upload.
    - Summary of penetration testing results with remediation plans.
    - Access control lists and encryption validation logs.
- **Performance Scorecard:** The Business Owner completes a quarterly Processor Performance Scorecard in Coupa. Metrics tracked include SLA adherence, responsiveness to security inquiries, and transparency regarding sub-processor changes.

### 5.4 Sub-Processor Authorization and Management

Meridian strictly controls the sub-processing chain to prevent data sprawl.

1.  **Authorization Request:** The Processor submits a "Sub-Processor Addition Request" via the Meridian Third-Party Portal (hosted on OneTrust).
2.  **Objection Window:** Meridian has a 15-business-day window to object to the addition. Legal and CISO review the Sub-Processor.
3.  **Objection Basis:** Meridian may object if:
    - The Sub-Processor is a direct competitor as identified by Market Intelligence.
    - The Sub-Processor is located in a jurisdiction deemed inadequate (necessitating a new TIA).
    - The Sub-Processor's security posture is insufficient (e.g., lacks ISO 27001 certification for a critical data flow).
4.  **Back-to-Back Flow-Down:** The primary Processor's DPA mandates that a "back-to-back" DPA (substantially identical data protection terms) is in place with the Sub-Processor. Meridian retains the right to audit the flow-down contract.

### 5.5 Terminating the Processing Relationship

When transitioning away from a processor, data reclamation and secure destruction are critical.

1.  **Data Extraction:** The Business Owner coordinates with IT to extract all Meridian data from the Processor's environment in a usable, machine-readable format (JSON or CSV, as agreed in the DPA).
2.  **Verification of Deletion:** The Processor must provide a Certificate of Destruction (CoD) signed by their CISO or a qualified third-party shredding/logical wiping vendor.
3.  **Logical Access Revocation:** Meridian's Identity and Access Management (IAM) team must revoke all VPN credentials and API keys within 4 hours of contract termination.
4.  **RoPA Update:** The Data Governance Manager updates the Record of Processing Activities (RoPA) to mark the processing activity as "Terminated."

---

### 5.6 Detailed Operational Workflow: DPA Renewal and Amendment

This sub-process addresses modifications to existing DPAs.

1.  **Trigger Event:** The OneTrust platform generates an automated ticket 90 days before DPA expiration to the Legal and Privacy teams, copying the Business Owner.
2.  **Amendment Initiation:** If the processing scope changes mid-contract (e.g., a new product feature requiring new analytics), the Business Owner must submit an "Amendment Request" detailing the change.
3.  **Impact Assessment (Mini-DPIA):** The DPO office (Privacy Analyst) conducts a Mini-DPIA to assess whether the new scope increases risk or alters the legal basis.
4.  **Legal Modification:** Legal drafts the two-way amendment document.
5.  **Execution & Archival:** Both parties sign via DocuSign; the executed document is stored in ContractWorks and linked in Coupa.

### 5.7 Handling Incidents Originating at the Processor

When a security incident occurs at a Processor, the Business Owner and CISO must coordinate a response to assess blast radius to Meridian data.

1.  **Notification Intake:** The Meridian SOC monitors a dedicated processor incident mailbox (`processor-alerts@meridian.com`). Alerts are auto-triaged.
2.  **Severity Assessment:** The CISO determines if the Meridian Incident Response Plan (IRP) must be activated. Criteria: confirmed breach of confidentiality, integrity loss of PHI, or ransomware impacting shared infrastructure.
3.  **Joint Forensics:** Where contractually permitted and commercially reasonable, Meridian may deploy its Incident Response retainer (CrowdStrike Services) to interface with the Processor's IR team.

## 6. Controls and Safeguards

### 6.1 Administrative Controls

- **DPA Deviation Register:** A centralized risk register (in ServiceNow GRC) is maintained by the DPO, tracking all instances where a Processor contract deviates from Meridian's standard DPA baseline. Each entry must be validated annually.
- **Privacy Notices:** Meridian maintains a series of layered external privacy notices (hosted on the public-facing website `www.meridian.com/privacy`) informing data subjects about the categories of processors we use. These notices cover the primary purposes of data sharing.
- **Segregation of Duties:** The TPRM platform (LogicGate) is configured with rule-based permissions to prevent a single individual from both initiating a vendor assessment and approving the final risk acceptance.
- **Access Controls:** Meridian's Logical Access Management Policy (SOP-IT-004) governs access to all internal systems containing Processor assessment data. Access is role-based (RBAC) and reviewed quarterly.

### 6.2 Technical Controls

- **Data Discovery and Classification:** The Varonis Data Security Platform is configured with pattern-matching rules to detect and classify Processor-specific contract metadata and PHI at rest in Meridian's OneDrive and SharePoint tenant.
- **API Gateway Throttling:** Azure API Management (APIM) enforces strict rate-limiting on all outbound API connections to Processors to prevent accidental bulk data leakage.
- **DLP Configuration:** Endpoint Data Loss Prevention (DLP) policies (Microsoft Purview) are tuned to block uploads to non-approved SaaS domains. "Approved Processor Tenant IDs" are whitelisted.
- **Encryption in Transit:** Meridian policy enforces TLS 1.2+ for all data streams. Legacy processors must be granted a formal technical exception.

### 6.3 Risk Acceptance and Mitigation

If a Processor cannot meet a mandatory technical control (e.g., they only support TLS 1.1), the following safeguards must be implemented before proceeding:
- **Compensating Control:** A documented compensating control is required (e.g., IPsec VPN tunnel with AES-256 instead of public TLS).
- **Time Limit:** The Risk Acceptance must have a sunset clause (no longer than 12 months).
- **Sign-off:** Risk Acceptance must be co-signed by the CISO and DPO.

## 7. Monitoring, Metrics, and Reporting

The effectiveness of the Processor Oversight program is measured via a defined set of Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs), presented monthly to the Data Governance Council.

### 7.1 Key Metrics Dashboard

| Metric | Target | Calculation Logic |
|---|---|---|
| **DPA Coverage Ratio** | 99.5% | (Count of Active Processors with Executed DPAs) / (Total Count of Active Processors) |
| **Overdue Assessments** | < 5% | (Tier 2/3 Processors past due for Annual Re-assessment) / (Total Tier 2/3 Processors) |
| **Sub-Processor Compliance** | 100% | Confirmation that the latest Sub-Processor list matches the vendor's public registry (checked biannually) |
| **Risk Posture Trending** | Decreasing Y-o-Y | Aggregate Inherent Risk Score vs. Residual Risk Score across the portfolio |
| **Incident Response Time** | < 1 Hour ACK | Time from SOC receiving Processor notice to acknowledgment of receipt by DPO |
| **Data Return Compliance** | 100% | Terminated contracts with verified Certificate of Destruction |

### 7.2 Reporting Cadence

- **Monthly TPRM Operations Call:** Procurement, Legal Operations, and the DPO Analyst discuss active RFPs and amendment statuses.
- **Quarterly Business Review (QBR):** The CISO and DPO present the Processor Performance Scorecard to the Business Unit VPs.
- **Annual Privacy Reporting:** The DPO aggregates annual Processor assurance metrics for the Supervisory Authority (where required) and Meridian's Corporate Responsibility Report.

## 8. Exception Handling and Escalation

Deviation from this SOP is managed through a structured exception process, not ad-hoc approval.

### 8.1 Exception Request Procedure

1.  **Initiation:** The Business Owner initiates an "SOP Deviation Request" (SDR) in ServiceNow, specifying the precise clause of SOP-DGP-015 being deviated from, the compensating control, and the technical justification.
2.  **Impact Analysis:** The DPO and CISO teams jointly assess the increased residual risk.
3.  **Approval Matrix:**
    - **Low Impact Exceptions:** (e.g., 5-day delay in certificate upload) Approved by the Data Governance Manager.
    - **Medium Impact Exceptions:** (e.g., alternative audit mechanism) Approved by the DPO and CISO.
    - **High Impact Exceptions:** (e.g., waiving DPA clause for a strategic partner) Escalated to the Data Governance Council Executive Committee (GC, CEO, CISO).

### 8.2 Escalation Path for Critical Non-Compliance

If a critical Tier 3 Processor refuses to comply with mandatory audit rights or security remediation (e.g., refuses to patch a critical 9.8 CVSS vulnerability within 30 days), the following escalation path is followed:

1.  **Operational Escalation:** DPO and VP Procurement notify the Processor's executive contact in writing of the material breach of contract.
2.  **Service Suspension:** If not remediated in 15 days, Business Owner enacts a temporary suspension of new data flows into the processor environment. Read access may be maintained for business continuity.
3.  **Contract Termination:** Legal (Maria Gonzalez) initiates the termination for convenience clause in the MSA. Data extraction and destruction procedures (Section 5.5) begin immediately.

## 9. Training Requirements

### 9.1 Role-Based Curriculum

Meridian's Learning Management System (LMS, SAP SuccessFactors) automatically assigns privacy and security training modules based on the user's role mapped against this SOP.

| Target Audience | Training Module(s) | Frequency |
|---|---|---|
| Procurement Team | "Privacy in Sourcing: The Art of the DPA" | Annually |
| Legal Counsel (Commercial) | "Handling SCCs and Cross-Border Litigation"; "HIPAA BAA Masterclass" | Annually |
| Business Unit Owners / Product Managers | "TPRM Essentials: It Starts with You" | Annually |
| DPO Office & IT Security Auditors | "Advanced Third-Party Audit Techniques" (cert. prep) | Biennially |

### 9.2 Awareness Validation

All users assigned a curriculum must pass a short knowledge-check quiz (Pass Threshold: 80%). Failure requires re-training within 30 days. Quarterly phishing simulations, specifically themed around "Fake Sub-Processor Requests," are distributed enterprise-wide by the Security Awareness team.

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

- **SOP-SEC-022:** Security Incident Response Plan.
- **SOP-IT-004:** Logical Access Management and Entitlement Review.
- **SOP-DGP-002:** Records of Processing Activities (RoPA) Maintenance.
- **SOP-DGP-010:** Data Protection Impact Assessment (DPIA) Standard.
- **SOP-RMC-008:** Enterprise Third-Party Risk Management (TPRM) Framework.
- **SOP-DGP-022:** Cross-Border Data Transfer Protocol.

### 10.2 Regulatory and External References

- Regulation (EU) 2016/679 (General Data Protection Regulation).
- Health Insurance Portability and Accountability Act of 1996 (HIPAA) Privacy, Security, and Breach Notification Rules.
- AICPA TSC 2017 (Trust Services Criteria for SOC 2).
- NIST Special Publication 800-53, Rev. 5.
- ISO/IEC 27701:2019 (Privacy Information Management System).

## 11. Document Revision History

| Version | Date | Author(s) | Description of Changes |
|---|---|---|---|
| 0.1 | 2024-03-10 | Dr. Klaus Weber (DPO), Lisa Park (Governance) | Initial Draft. Consolidated prior "Security Vendor" and "Privacy Processor" procedures. |
| 0.2 | 2024-04-05 | Sarah Chen (CISO) | Added Technical Controls section. Revised Risk Tiering Matrix to align with NIST CSF 2.0. |
| 0.3 | 2024-04-28 | Maria Gonzalez (General Counsel) | Legal review of DPA clauses and International Data Transfer sections. Added Sub-Processor Objection legal language. |
| 1.0 | 2024-05-18 | Dr. Klaus Weber (DPO) | Approved Version 1.0. Effective Date established. Replaced legacy policy "Vendor Privacy Management 2.1." |
| 1.1 | 2025-10-28 | Lisa Park (Data Governance Manager) | Routine annual review. Updated Roles table to reflect new CISO appointment (Sarah Chen). Updated escalation path names. No substantive policy changes. |