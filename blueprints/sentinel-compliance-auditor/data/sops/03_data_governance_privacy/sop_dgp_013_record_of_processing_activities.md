---
sop_id: "SOP-DGP-013"
title: "Record of Processing Activities"
business_unit: "Data Governance & Privacy"
version: "2.0"
effective_date: "2024-09-26"
last_reviewed: "2025-07-21"
next_review: "2026-01-16"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Record of Processing Activities

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for creating, maintaining, reviewing, and updating Meridian Health Technologies, Inc.’s (“Meridian”) organizational and departmental Records of Processing Activities (ROPA), as mandated by Article 30 of the General Data Protection Regulation (GDPR) (Regulation (EU) 2016/679). The purpose of this document is to ensure:

- Full compliance with Article 30 obligations for both Controller and Processor records.
- Demonstrable accountability to Supervisory Authorities, specifically the Berlin Data Protection Authority (DPA) as our Lead Supervisory Authority (LSA) and other relevant EU DPAs.
- A single, authoritative, and continuously updated inventory of all personal data processing activities across Meridian’s four business lines and internal corporate functions.
- A structured mechanism to identify, assess, and mitigate privacy risks stemming from processing activities.
- A foundational dataset to support Data Protection Impact Assessments (DPIAs) per SOP-RMF-007, Cross-Border Transfer Impact Assessments (TIAs) per SOP-DGP-019, and Data Subject Rights (DSR) fulfillment per SOP-DGP-008.

### 1.2 Scope

This SOP applies to all processing of personal data conducted by or on behalf of Meridian Health Technologies, Inc., regardless of the geographic location of the data subject or the processing entity. The scope specifically includes:

- **All Business Lines:** Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.
- **All Internal Functions:** Human Resources (HR), Finance, Legal, Compliance, IT, Security, Marketing, Sales, and Procurement.
- **All Data Subject Categories:** Patients (EU and non-EU), healthcare provider staff, health plan members, Meridian employees, contractors, vendors, and website visitors.
- **All Processing Locations:** Processing occurring on AWS (primary) and Azure (DR) cloud infrastructure in regions `eu-west-1` (Ireland), `eu-west-2` (London), `eu-central-1` (Frankfurt), `us-east-1` (N. Virginia), and `us-west-2` (Oregon), as well as on-premise assets at Meridian offices.

This SOP is mandatory for all Meridian personnel, contractors, and third parties who design, implement, operate, or control processing activities. Non-compliance is subject to disciplinary action under SOP-HR-031.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **Controller** | The natural or legal person which, alone or jointly with others, determines the purposes and means of the processing of personal data (GDPR Art. 4(7)). |
| **Data Protection Impact Assessment (DPIA)** | A process to help identify and minimize the data protection risks of a project (GDPR Art. 35). Refer to SOP-RMF-007. |
| **Data Subject** | An identified or identifiable natural person to whom personal data relates. |
| **DPO** | Data Protection Officer. Dr. Klaus Weber is the appointed DPO for Meridian. |
| **Joint Controller** | Two or more controllers that jointly determine the purposes and means of processing (GDPR Art. 26). |
| **Lead Supervisory Authority (LSA)** | The supervisory authority of the main establishment of the controller in the EU. For Meridian, this is the Berlin DPA. |
| **Personal Data** | Any information relating to an identified or identifiable natural person (GDPR Art. 4(1)). |
| **Personal Data Breach** | A breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data (GDPR Art. 4(12)). Refer to SOP-SEC-015. |
| **Processing** | Any operation performed on personal data, whether or not by automated means (GDPR Art. 4(2)). |
| **Processor** | A natural or legal person which processes personal data on behalf of the controller (GDPR Art. 4(8)). |
| **ROPA** | Record of Processing Activities as required under GDPR Article 30. |
| **Special Categories of Data** | Personal data revealing racial or ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, biometric data for identification, health data, or data concerning a natural person's sex life or sexual orientation (GDPR Art. 9). |
| **Sub-Processor** | Another processor engaged by a processor to carry out specific processing activities on behalf of the controller. |
| **Third Country** | A country outside the European Economic Area (EEA) not deemed to have an adequate level of data protection by the European Commission. |
| **Transfer Impact Assessment (TIA)** | An assessment required for transfers of personal data to third countries based on Article 46 transfer tools, to verify equivalent protection. Refer to SOP-DGP-019. |

## 3. Roles and Responsibilities

The following RACI matrix defines the responsibilities for the ROPA lifecycle.

| Role | RACI | Responsibility Detail |
| :--- | :---: | :--- |
| **Data Governance & Privacy Analyst** | R, A | **Responsible** for executing the ROPA update procedures, conducting interviews with processing owners, maintaining the central ROPA repository in OneTrust, performing quality assurance checks, and flagging discrepancies to the DPO. **Accountable** for the completeness and accuracy of the inventory once entered. |
| **Processing Activity Owner** (Business Unit VP/Director or Functional Head) | C, I | **Consulted** for any new, changed, or ceased processing activity within their domain (e.g., VP of Clinical AI for the model training pipeline, VP of Human Resources for employee data). Must respond to quarterly verification requests within 10 business days. **Informed** of any ROPA-derived risks or compliance gaps related to their area. |
| **Chief Privacy Officer / DPO** (Dr. Klaus Weber) | A, C, I | **Accountable** for the overall ROPA compliance program. Reviews and signs off on the Master ROPA annually. Acts as the primary point of contact for supervisory authorities regarding the ROPA. **Consulted** on borderline processing classifications (Controller vs. Processor). |
| **General Counsel** (Maria Gonzalez) | A, I | **Accountable** for approving the final interpretation of joint controllership agreements and complex data-sharing contracts mapped in the ROPA. |
| **IT & Security Architecture** (CTO Office) | C | **Consulted** on the technical accuracy of processing descriptions, system inventories, data flow mappings, cross-border data routing, and technical safeguards. |
| **Procurement & Vendor Management** | C, I | **Consulted** at contract renewal or new vendor onboarding to identify new Processor/Sub-Processor relationships for inclusion in the ROPA. |
| **Internal Audit** | I | **Informed** via the annual ROPA sign-off report and may use the ROPA as an auditee data source for ISO 27701 and internal control audits. |

## 4. Policy Statements

1. Meridian shall maintain a comprehensive, written (electronic) ROPA as a single source of truth for all personal data processing activities, pursuant to GDPR Article 30.
2. The ROPA shall be subdivided into a Master Controller ROPA (covering Meridian’s activities as a Controller or Joint Controller) and a Processor ROPA (covering activities performed by Meridian on behalf of its clients, typically via the MedInsight Analytics and SaaS Platform).
3. All processing activities, regardless of perceived risk level or data volume, shall be recorded. No processing activity is de minimis for ROPA purposes.
4. The ROPA shall be reviewed and updated on a continuous trigger basis and no less than quarterly for all active records.
5. The DPO shall make the ROPA available to the Berlin DPA upon request within 72 hours (GDPR Art. 30(4)).
6. Any new processing activity must have a corresponding ROPA entry drafted and approved *prior* to the "go-live" date of the processing. This ROPA entry serves as a prerequisite for a "Privacy by Design" sign-off.
7. A Data Protection Impact Assessment (DPIA) trigger evaluation is mandatory for any new entry in the ROPA that involves new technologies, profiling, or processing of special categories of data on a large scale. This evaluation must be documented within the ROPA itself.

## 5. Detailed Procedures

This section outlines the step-by-step procedures for the end-to-end ROPA lifecycle management. The authoritative repository for the ROPA is the **OneTrust Data Mapping module**, accessible via SSO through Okta.

### 5.1 Trigger Identification and Intake

A new ROPA entry or a significant update to an existing entry can be triggered by multiple events. All personnel are responsible for identifying and communicating such triggers.

**Trigger Events include, but are not limited to:**
1.  **New Product/Feature Launch:** A Product Manager proposes a new feature in the Clinical AI Platform that collects a new biometric marker (special Category data). This is initiated via a "Privacy by Design Review Request" in ServiceNow, which auto-creates a draft ROPA task in OneTrust.
2.  **New Vendor Engagement:** Procurement initiates a third-party risk assessment for a new marketing automation platform that will receive Meridian customer email addresses.
3.  **Internal Process Change:** HR decides to implement a new background check process for contractors that involves a new screening agency and new data categories (e.g., credit history).
4.  **M&A Activity:** Legal identifies personal data assets in a target company during due diligence.
5.  **Quarterly Verification:** A scheduled task assigned to all Processing Activity Owners (see 5.3).

**Procedure:**
1.  The **Originator** (e.g., Product Manager, Procurement Specialist, HR Business Partner) identifies a trigger event and submits a "Privacy Review Request" in ServiceNow.
2.  ServiceNow routes the request to the **Data Governance & Privacy Analyst** queue.
3.  The Analyst performs a preliminary review within 3 business days to confirm if the trigger constitutes a new or materially changed processing activity requiring a new or updated ROPA entry.
4.  If confirmed, the Analyst creates a new task in OneTrust, linking it to the ServiceNow ticket, and assigns it to the relevant Processing Activity Owner with a due date of 14 business days.

### 5.2 Information Gathering and Data Mapping

The Processing Activity Owner is responsible for providing the necessary information. The Data Governance & Privacy Analyst facilitates the collection through a structured interview or workshop.

**A. Controller ROPA Entry (GDPR Art. 30(1))**
The following fields must be populated in OneTrust for every processing activity where Meridian acts as a Controller or Joint Controller:

1.  **Record ID:** Auto-generated by OneTrust (e.g., CTL-2024-0234).
2.  **Processing Activity Name:** A unique, human-readable, and descriptive name (e.g., "Clinical AI Platform - ECG Arrhythmia Model Training on EU Patient Data," "HR - EU Employee Payroll Processing").
3.  **Controller/Joint Controller(s) and Their Contact Details:** Legal entity name(s) (e.g., "Meridian Health Technologies GmbH," "Meridian Health Technologies, Inc."), registered address. If a Joint Controller, reference the Joint Controller Agreement (Art. 26) executed and stored in DocuSign. **DPO contact details are automatically populated.**
4.  **Purpose(s) of Processing:** A granular, specific, and legitimate purpose. Must not be vague. (e.g., "Detection of atrial fibrillation patterns in de-identified ECG waveforms to improve diagnostic algorithm accuracy," not "Product improvement").
5.  **Categories of Data Subjects:**
    - Use standardized taxonomy from OneTrust: Patients (Adults, Ineligible for consent), Patients (Adults, Eligible for consent), Patients (Minors), Healthcare Professionals (HCPs), Clinical Trial Participants, Employees (Current, Former, Candidate), Contractors, Website Visitors.
6.  **Categories of Personal Data:**
    - Select all applicable categories from the OneTrust taxonomy. Must explicitly flag if any category falls under GDPR Art. 9 (Special Category) or Art. 10 (Criminal Conviction Data). Examples: Name, Contact Details, Online Identifiers (IP Address, Cookie ID), Device ID, Biometric Data (ECG waveform), Health Data (Diagnosis, Heart Rate), Financial Data (Bank Account Number), etc.
7.  **Legal Basis for Processing:**
    - Select the primary legal basis (Consent (Art. 6(1)(a)), Contract (Art. 6(1)(b)), Legal Obligation (Art. 6(1)(c)), Vital Interests (Art. 6(1)(d)), Public Task (Art. 6(1)(e)), Legitimate Interests (Art. 6(1)(f)). If Legitimate Interests is chosen, the "Legitimate Interests Assessment" (LIA) must be attached to the record. For Special Category Data, the relevant Art. 9(2) exemption must be selected. A record cannot be approved without a valid basis.
8.  **Recipient Categories:** Who the data is disclosed to (e.g., "Cloud Hosting Providers," "Payment Gateways," "Regulatory Authorities," "Affiliate Subsidiaries for CRM"). Specific Processors are captured in the Processor ROPA and linked here.
9.  **Transfers to Third Countries:** A Boolean Yes/No flag. If "Yes," the specific third country must be identified, the Article 46 transfer mechanism/safeguard cited (e.g., SCCs, BCRs), and a link to the applicable Transfer Impact Assessment (TIA) (SOP-DGP-019) must be provided.
10. **Retention Periods:** The period for which the data will be stored, or if not possible, the criteria used to determine that period (e.g., "10 years after the last patient interaction as per Medical Device Regulation requirements," "Deleted 30 days after account termination," "Cookies: 13 months"). Reference the Corporate Retention Schedule (SOP-DGP-009).
11. **Technical and Organizational Security Measures (TOMs):** A high-level description or link to the applicable security profile in OneTrust (e.g., "Encrypted at rest (AES-256) and in transit (TLS 1.3), access restricted based on RBAC, pseudonymization applied at intake, annual SOC 2 Type II audit"). This should be verified with IT Security during the mapping.
12. **DPIA Required (Y/N):** Mandatory field. If "Yes," a link to the DPIA record (SOP-RMF-007) and its outcome must be provided before the ROPA entry can be approved.

**B. Processor ROPA Entry (GDPR Art. 30(2))**
For activities where Meridian acts solely as a Processor (e.g., hosting de-identified data from pharma clients on our SaaS Platform), the Analyst works with the VP of Professional Services and relevant Client Success Manager to maintain the record. Fields include:

1.  **Name and Contact Details of the Processor (Meridian) and any Sub-Processors:** Meridian's details as the lead Processor, and a linked list of all approved Sub-Processors (e.g., AWS, Datadog).
2.  **Categories of Processing Carried Out on Behalf of Each Controller:** Grouped by Controller or Controller type (e.g., "Top 10 Pharma - Real World Data Analytics," "Hospital Group - Clinical Data Hosting").
3.  **Nature and Purpose of Processing:** The service provided (e.g., "Secure hosting and management of de-identified patient data on the MedInsight platform").
4.  **Duration of Processing:** Tied to the Master Services Agreement (MSA) with the Controller.
5.  **Transfer to a Third Country:** As per Controller ROPA.
6.  **General Description of TOMs:** As per Controller ROPA, reflecting the baseline security measures for the platform.

### 5.3 Quarterly Verification Cadence

To ensure the ROPA remains a living document, a formal verification cycle is enforced.

1.  On the first business day of each quarter (Jan, Apr, Jul, Oct), OneTrust automatically triggers a "Quarterly ROPA Verification" task to every **Processing Activity Owner** for the records they own.
2.  The email notification contains a personalized dashboard link showing a list of their active processing activities.
3.  The Owner must, within **10 business days**, for each record:
    - Confirm "No Change."
    - Flag "Minor Change" and update the relevant fields (e.g., new recipient).
    - Flag "Major Change" or "Sunsetting," which triggers a new task for the Data Governance & Privacy Analyst to re-engage via the 5.2 procedure.
4.  If an Owner fails to respond within the 10-day SLA, an automatic escalation email is sent to the Owner and their direct manager. After 15 days, the DPO is notified.
5.  A verification dashboard in OneTrust tracks completion rates by department.

### 5.4 Review and Approval Workflow

Every new or materially changed ROPA entry must pass a rigorous review gate before it is published in the Master ROPA.

1.  **Peer Review:** Upon information completion, a second Data Governance & Privacy Analyst performs a quality assurance check for logical consistency, completeness of required fields, and clear, non-vague language. This step is completed within 3 business days.
2.  **Security Alignment:** If the record involves new technical controls, system architecture, or cross-border data flows, the task is routed to the **IT Security Architecture** team for a 5-business-day review. They verify the accuracy of the stated TOMs and the technical feasibility of stated data flows.
3.  **Legal Review (Conditional):** The task is routed to **General Counsel** for review if the record involves a new Joint Controller arrangement, an untested legal basis (e.g., public interest), or has a complex data export flow requiring a TIA. Standard vendor integrations and established processing activities bypass this step.
4.  **DPO Final Sign-off:** The DPO (or delegate) performs a final review, ensuring regulatory alignment. The DPO has the authority to reject a record and send it back for remediation with specific comments. The DPO’s review must be completed within 5 business days.
5.  **Publication:** Upon DPO approval, the record status changes from "Draft" to "Active." It is then immediately part of the Master ROPA and reportable to Supervisory Authorities.

### 5.5 Annual Audit and Certification

Annually, aligned with the fiscal year-end, a comprehensive audit of the ROPA is conducted.

1.  **Internal Audit selects a statistically significant sample (n=30) of active ROPA entries, stratified across business units and risk levels.**
2.  **For each sampled entry, the Data Governance & Privacy team must provide evidence ("evidence pack") that the recorded processing matches reality. This pack includes:**
    - Screenshots of data fields in the actual application.
    - A copy of the current DPA with the Processor.
    - Confirmation from IT Security on technical controls.
    - A signed attestation from the Processing Activity Owner.
3.  **The DPO and General Counsel review the audit findings. Systemic issues (e.g., "20% of records had inaccurate retention periods") result in a Corrective Action Plan (CAP) with a binding remediation deadline.**
4.  **Upon successful audit sign-off, the DPO and General Counsel issue a joint "Annual ROPA Compliance Certificate" which is presented to the Board of Directors.**

## 6. Controls and Safeguards

To maintain the integrity, confidentiality, and availability of the ROPA, the following controls are implemented:

| Control ID | Control Description | Type | Implementation |
| :--- | :--- | :--- | :--- |
| **DGP013-C01** | **Access Control:** Access to the OneTrust ROPA module is strictly role-based. No user outside the Data Governance & Privacy team has "edit" rights. Processing Activity Owners have "comment and respond" rights only on their assigned records. | Technical | Enforced via Okta SSO groups mapped to OneTrust roles. Quarterly entitlement reviews by the DPO team. |
| **DGP013-C02** | **Audit Trail:** All activities within the ROPA module (view, create, edit, approve, reject, delete) are logged with an immutable timestamp and username. | Technical | Native OneTrust audit log feature, enabled and retained for 7 years. Ship logs to the central Splunk SIEM for monitoring. |
| **DGP013-C03** | **Segregation of Duties:** The originator of a ROPA entry cannot be the DPO final approver for the same entry. No single individual can create and approve a record end-to-end. | Administrative | Built into the OneTrust workflow configuration. |
| **DGP013-C04** | **Data Loss Prevention (DLP):** Electronic export of ROPA data is restricted to specific, authorized analysts for reporting or supervisory authority requests. All exports are watermarked and logged. | Technical | OneTrust configuration restricts bulk export to 'ROPA Administrator' role only. |
| **DGP013-C05** | **Change Management:** All modifications to the ROPA are treated as governed changes. The system auto-generates a version history for the Master ROPA upon any "Active" record's addition, change, or sunsetting. | Administrative | OneTrust versioning and effective date mechanism. |
| **DGP013-C06** | **Cross-Reference Integrity:** Automated validation rules in OneTrust prevent a ROPA entry from being set to "Active" if it references a non-existent or "Draft" Processor record or DPIA. | Technical | Custom validation rules scripted in OneTrust's Data Flow and Cross-Reference modules. |
| **DGP013-C07** | **Physical Security:** Data centers hosting OneTrust cloud infrastructure maintain SOC 2 Type II certification, a copy of which is reviewed annually by the Meridian Security team. | Physical | Evidence maintained in the Vendor Risk Management platform, Aravo. |

## 7. Monitoring, Metrics, and Reporting

The effectiveness of this SOP is measured and reported through the following Key Performance Indicators (KPIs):

| Metric / KPI | Target | Measurement Mechanism | Reporting Cadence & Audience |
| :--- | :--- | :--- | :--- |
| **ROPA Completeness Rate** | 100% of identified live processing activities have an Active ROPA record. | Semi-annual reconciliation of ROPA against a catalog of live applications, databases, and vendor contracts from CMDB and Aravo. | Quarterly, to DPO. Annually, to Board. |
| **Quarterly Verification On-Time Completion** | >95% of assigned verifications completed by Owners within the 10-business-day SLA. | OneTrust Dashboard. | Monthly, to DPO. Quarterly, to Business Unit VPs (shows red/yellow/green scores for their teams). |
| **Record Accuracy** | <5% error rate in the annual audit sample. | Annual Internal Audit "Evidence Pack" review. | Annually, to General Counsel and Board of Directors. |
| **Time-to-Approval for New Records** | Average cycle time from ServiceNow ticket creation to "Active" ROPA status is <30 business days. | OneTrust analytics calculating the duration of workflow stages. | Quarterly, to DPO for process optimization. |
| **"Sunsetting" Process Removal** | 100% of sunset applications/processes have their ROPA record status changed to "Archived" within 30 days of retirement. | Reconciliation between decommissioning records in the CMDB and OneTrust. | Quarterly, to DPO and CTO. |

A summary "State of the ROPA" report, including a heatmap of processing risk, will be presented by the DPO to the Data Ethics & Privacy Council (DEPC) on a quarterly basis.

## 8. Exception Handling and Escalation

Deviations from this standard operating procedure must be formally managed.

### 8.1 Exceptions

1.  **Emergency Processing:** In a bona fide emergency (e.g., critical vulnerability leading to a Personal Data Breach requiring urgent forensics that process data in an unregistered way), the CISO may authorize temporary processing. Within 5 business days of the emergency stabilisation, a retrospective ROPA entry must be completed, noting the emergency exception. The DPO must be informed immediately.
2.  **Short-Term Pilot/Research:** If a research team wishes to conduct a pilot with personal data lasting less than 30 days and involving fewer than 100 data subjects, a full ROPA may be temporarily deferred. A "Lightweight ROPA" (L-ROPA) form, capturing core Art. 30(1) points, must be completed instead. Any extension of the pilot beyond 30 days automatically triggers a full ROPA requirement.
3.  All exceptions must be formally logged in the ServiceNow "Exception Register" by the DPO, stating the justification, the compensating controls, and the expiration date. General Counsel must approve all exceptions exceeding 90 days.

### 8.2 Escalation Path

Any unresolved dispute on the content of a ROPA entry (e.g., a Processing Activity Owner refusing to acknowledge their responsibility, a disagreement on the legal basis) must be escalated promptly.

1.  **Level 1:** Data Governance & Privacy Analyst escalates to the DPO, providing a summary of the deadlock. Resolution within 5 business days.
2.  **Level 2:** DPO escalates to General Counsel for a joint decision on the legal interpretation. Resolution within 5 business days.
3.  **Level 3:** For business-critical conflicts, DPO and General Counsel jointly escalate to the Chief Risk Officer (CRO) and the relevant Business Unit Executive Vice President (EVP) for a risk-based business decision that is formally recorded. This decision is final.

## 9. Training Requirements

All personnel with assigned roles in this SOP must complete appropriate training.

| Training Module | Target Audience | Frequency | Delivery Method |
| :--- | :--- | :--- | :--- |
| **GDPR Foundations & ROPA Awareness** | All employees and long-term contractors. | Annually | Mandatory e-learning module in Workday Learning. Covers trigger identification and basic Art. 30 principles. |
| **ROPA Practitioner Training** | Processing Activity Owners, Privacy Champions embedded in business units. | Annually, and on role change | Instructor-led virtual session by the DPO team. Covers detailed procedures, the OneTrust interface for Owners, and the quarterly verification process. |
| **ROPA Analyst & Admin Training** | Data Governance & Privacy Analysts, DPO. | Annually, and upon major OneTrust release | Advanced, multi-day workshop including hands-on exercises, regulatory updates, and audit preparation. |
| **Targeted Remediation** | Any Processing Activity Owner who fails the quarterly verification SLA twice in a row. | Ad-hoc | 30-minute one-on-one coaching session with a Data Governance Analyst. |

Training completion is tracked in Workday Learning. Non-completion is reported to managers and counts against the individual's compliance scorecard, which impacts annual performance reviews.

## 10. Related Policies and References

This SOP is not a standalone document. It must be read and enacted in conjunction with the following internal and external references.

### 10.1 Internal Meridian SOPs and Policies

| SOP-ID / Policy | Document Title | Relationship |
| :--- | :--- | :--- |
| **SOP-RMF-007** | Data Protection Impact Assessment (DPIA) | ROPA triggers DPIA; DPIA outcome recorded in ROPA. |
| **SOP-DGP-008** | Data Subject Rights (DSR) Requests | ROPA is used to locate data for DSR fulfillment. |
| **SOP-DGP-009** | Data Retention and Disposal Schedule | ROPA dictates retention period alignment. |
| **SOP-DGP-019** | Cross-Border Data Transfer Impact Assessment | ROPA identifies transfers requiring a TIA. |
| **SOP-SEC-015** | Personal Data Breach Notification | ROPA identifies impacted controllers/processing for notification. |
| **SOP-VRM-003** | Third-Party Vendor Risk Management | Vendors identified in ROPA must be managed via this SOP. |
| **POL-DGP-001** | Data Governance and Privacy Policy | Overarching corporate policy. |
| **POL-HR-031** | Employee Standards of Conduct and Disciplinary Action | Consequences of non-compliance with this SOP. |

### 10.2 External Standards and Regulations

- **Regulation (EU) 2016/679 (General Data Protection Regulation):** In particular, but not exclusively, Articles 4, 5, 6, 9, 10, 26, 30, 35, 44-49.
- **WP29/WP248 rev.01:** Guidelines on Data Protection Officers (‘DPOs’), as endorsed by the EDPB.
- **EDPB Guidelines on Personal Data Breach Notification.**
- **ISO 27701:2019:** Security techniques — Extension to ISO 27001 and ISO 27002 for privacy information management.

## 11. Revision History

| Version | Effective Date | Author | Approver | Summary of Changes |
| :--- | :--- | :--- | :--- | :--- |
| **2.0** | 2024-09-26 | Dr. Klaus Weber, DPO | Maria Gonzalez, General Counsel | Major overhaul. Migrated procedural steps to OneTrust. Added formal quarterly verification cadence (5.3), new roles (Processing Activity Owner), detailed KPIs (7.0), and RACI matrix (3.0). Fully aligns with revised Art. 30 EDPB guidance. |
| **1.2** | 2024-04-10 | Alice Chen (Analyst) | Dr. Klaus Weber, DPO | Added §5.5 Annual Audit procedure. Updated definitions to include "Joint Controller." Clarified Processor record detail for the new MedInsight multi-tenant architecture. Updated related SOPs. |
| **1.1** | 2023-11-05 | Dr. Klaus Weber, DPO | Dr. Klaus Weber, DPO | Minor revision. Updated DPO contact details. Added reference to new SOP-DGP-019 (Cross-Border Transfer IA). Escalation path clarified in §8.2. |
| **1.0** | 2023-06-01 | Dr. Klaus Weber, DPO | Maria Gonzalez, General Counsel | Initial version. Created a formal, documented ROPA procedure from the pre-existing ad-hoc spreadsheet-based practice, in response to Berlin DPA inquiry from Q1 2023. |