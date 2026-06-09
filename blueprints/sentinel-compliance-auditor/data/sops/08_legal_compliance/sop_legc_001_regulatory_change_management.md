---
sop_id: "SOP-LEGC-001"
title: "Regulatory Change Management"
business_unit: "Legal & Compliance"
version: "2.7"
effective_date: "2025-11-27"
last_reviewed: "2026-11-04"
next_review: "2027-05-07"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "HIPAA"
  - "SOC 2"
  - "GDPR"
  - "SR 11-7"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Regulatory Change Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework and methodology by which Meridian Health Technologies, Inc. ("Meridian" or the "Company") systematically identifies, assesses, prioritizes, operationalizes, and monitors compliance with new and evolving regulatory obligations across its global operations. The purpose of this SOP is to ensure that regulatory change is managed as a controlled, auditable business process rather than an ad hoc reaction to external pressures, thereby safeguarding the Company's ability to serve healthcare providers, payers, and patients without interruption.

The Regulatory Change Management (RCM) program delivers three core outcomes:

1.  **Proactive Risk Mitigation:** Early identification of regulatory shifts that could materially impact Meridian's Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, or the Meridian SaaS Platform.
2.  **Operationalized Compliance:** Transparent translation of regulatory text into implementable technical controls, product specifications, and business processes with clear ownership and timelines.
3.  **Demonstrable Governance:** Creation of a comprehensive audit trail linking a specific regulatory obligation to a concrete change in the production environment, satisfying Board-level oversight, external auditors, and competent supervisory authorities.

### 1.2 Scope

**In-Scope Activities:**
This SOP applies to all activities, personnel, systems, and third-party relationships involved in the management of regulatory obligations affecting Meridian's products and corporate operations. This includes, but is not limited to:
- Monitoring of legislative, regulatory, and supervisory guidance developments.
- Internal assessment of applicability and materiality of regulatory changes.
- Design and implementation of compliance controls.
- Testing and validation of controls.
- Reporting on regulatory change status to management and governance bodies.

**In-Scope Entities and Personnel:**
- All full-time, part-time, and contract employees of Meridian Health Technologies globally.
- All subsidiaries and legal entities, including Meridian Europe GmbH (Berlin) and Meridian Canada, Inc. (Toronto).
- All third-party vendors, contractors, and consultants who access, process, or manage data subject to regulation, or who develop, deploy, or monitor regulated AI models or financial services.

**In-Scope Regulatory Domains:**
This SOP governs compliance activities for the following regulatory frameworks to the depth detailed in Section 5:
- EU Artificial Intelligence Act (EU AI Act)
- Health Insurance Portability and Accountability Act (HIPAA)
- Service Organization Control 2 (SOC 2)
- General Data Protection Regulation (GDPR)
- SR 11-7 (Attachment: Supervisory Guidance on Model Risk Management)
- NIST AI Risk Management Framework (NIST AI RMF 1.0)

**In-Scope Systems and Tools:**
- **Regulatory Intelligence Platform:** CUBE Global RegPlatform.
- **Data Catalog & Lineage Tool:** Alation Data Catalog, linked to the Snowflake Data Cloud.
- **Model Inventory:** Meridian internal Model Risk Management System (MRMS), custom-built on ServiceNow.
- **GRC Platform:** RSA Archer, used for control mapping, risk assessment, and issue tracking.
- **Issue Tracking:** Atlassian Jira.

**Out of Scope:**
- Management of non-regulatory internal policy changes (refer to SOP-HR-003).
- Standard product release management, except where a release is specifically triggered by a regulatory change assessed under this SOP.
- Financial audit procedures (refer to SOP-FIN-010).
- Occupational health and safety regulations.

## 2. Definitions and Acronyms

### 2.1 Definitions
For the purposes of this SOP, the following definitions apply:

| Term | Definition |
| :--- | :--- |
| **Control** | A technical, administrative, or physical safeguard designed to mitigate a specific risk and ensure compliance with a regulatory obligation. |
| **Control Owner** | The named individual (typically VP-level or above) accountable for the design, implementation, and sustained operation of a specific control. |
| **Data Lineage** | A map of the data’s journey from its origin (source system), through all transformation points (extract, transform, load processes, APIs, models), to its final consumption point (report, analytical dashboard, AI model output). |
| **Horizon Scanning** | The systematic process of identifying, filtering, and analyzing emerging regulatory publications (draft bills, consultation papers, final rules, enforcement actions) to provide early warning of forthcoming compliance obligations. |
| **Impact Assessment** | A structured multi-disciplinary analysis (legal, technical, operational) to determine the applicability, materiality, and required response to a regulatory change. |
| **Implementation Owner** | The named individual (typically Director-level or above) responsible for executing the remediation plan, often a product or engineering manager. |
| **Materiality** | An evaluation of the financial, reputational, operational, and legal risk magnitude of a regulatory change, rated as High, Medium, or Low, as defined by the risk taxonomy in SOP-RISK-001. |
| **Regulatory Change Item (RCI)** | A unique record in RSA Archer representing a single tracked regulatory change from identification to closure. |
| **Remediation Plan** | A documented plan in Jira containing specific, measurable tasks, assigned owners, and target completion dates required to achieve compliance with a new or changed regulatory obligation. |

### 2.2 Acronyms

| Acronym | Definition |
| :--- | :--- |
| AI | Artificial Intelligence |
| CCO | Chief Compliance Officer |
| DPO | Data Protection Officer |
| DUA | Data Usage Agreement |
| EC | European Commission |
| EDPB | European Data Protection Board |
| EU AI Act | European Union Artificial Intelligence Act |
| GRC | Governance, Risk, and Compliance |
| HIPAA | Health Insurance Portability and Accountability Act |
| KRI | Key Risk Indicator |
| KPI | Key Performance Indicator |
| ML | Machine Learning |
| MRI | Model Risk Inventory |
| NIST AI RMF| National Institute of Standards and Technology AI Risk Management Framework |
| OCR | Office for Civil Rights (U.S. Department of Health and Human Services) |
| PHI | Protected Health Information |
| RACI | Responsible, Accountable, Consulted, Informed |
| RCI | Regulatory Change Item |
| RCM | Regulatory Change Management |
| ROPA | Record of Processing Activities |
| SLA | Service Level Agreement |
| SR 11-7 | Supervisory and Regulation Letter 11-7, Federal Reserve Board |

---

## 3. Roles and Responsibilities

The following responsibility assignment matrix applies to all RCM activities. No single individual may be both the Control Owner and the independent Assessor for the same control without a formal conflict-of-interest waiver approved by the General Counsel.

| Role | Responsibility | Named Role(s) |
| :--- | :--- | :--- |
| **RCM Program Owner** | Accountable for the overall RCM program, its SOP, and its performance metrics. Escalation point for inter-departmental conflicts. | Thomas Anderson, Chief Compliance Officer |
| **Regulatory Horizon Scanner** | Responsible for daily monitoring of regulatory landscape, performing initial triage, logging RCIs, and configuring Alation lineage for new regulated data flows. | Maria Chen, Director of Regulatory Intelligence (Legal & Compliance) |
| **Impact Assessment Lead** | Responsible for convening the cross-functional Impact Assessment Working Group, facilitating the assessment, and documenting its outcome and risk rating in RSA Archer. | Anya Sharma, Senior Privacy & AI Counsel (Legal & Compliance) |
| **Control Owner** | Accountable for the design and continued effectiveness of a specific compliance control. Signs off on control closure. | Varies by domain. Typically VP, Data Platform (technical controls); VP, Clinical AI (model controls); VP, Security (infosec controls). |
| **Implementation Owner** | Responsible for executing the Jira-based remediation plan (i.e., engineering, product, or process changes) to meet a regulatory obligation by the target date. | Assigned per RCI; typically a Director of Engineering, Product Manager, or business process owner. |
| **Independent Assessor** | Responsible for independently testing and validating the operational effectiveness of a newly implemented control before it is closed. | Lead Auditor, Internal Audit (for non-AI controls); Head of Model Validation (for model-related controls). |
| **Data Protection Officer** | Consulted and informed on all RCIs impacting personal data. Provides guidance per GDPR Art. 39. | Dr. Lena Vogel, Meridian Europe GmbH |
| **Legal & Compliance Review Board** | Reviews and approves all Impact Assessments with a "High" materiality rating and approves any exceptions to this SOP. | Maria Gonzalez, General Counsel; Thomas Anderson, CCO; Dr. Lena Vogel, DPO |
| **Model Risk Officer** | Accountable for maintaining the Model Risk Inventory (MRI) and ensuring SR 11-7 compliance for all tracked models. | Dr. Aris Thorne, Head of AI Risk & Validation |

---

## 4. Policy Statements

All policies herein are active, mandatory, and subject to audit by Internal Audit.

- **POL-LEGC-001-A (No Unassessed Obligation):** No new regulatory obligation that has been assessed as "Applicable" and "Material" shall be past its target compliance date without an active, Executive-approved remediation plan or risk acceptance.

- **POL-LEGC-001-B (Lineage as a Control Prerequisite):** For any regulatory obligation concerning data rights, use limitation, or data quality, documented end-to-end data lineage in Alation is a prerequisite for the creation of the associated compliance control in RSA Archer.

- **POL-LEGC-001-C (Governance Traceability):** Every implemented compliance control must be traceable from the specific Article or Section of the source regulation in RSA Archer, through the Impact Assessment and Jira remediation tasks, to a validated, operational control.

- **POL-LEGC-001-D (Mandatory Impact Assessment):** Any regulatory publication identified through Horizon Scanning that is triaged as "Potentially Applicable" to Meridian must undergo a formal, multi-disciplinary Impact Assessment. No engineering work for compliance shall commence before the Impact Assessment is completed and approved.

- **POL-LEGC-001-E (Zero Expired Exceptions):** All risk acceptances and control exceptions must have a defined expiry date. No expired exception shall remain open without a re-approval before the expiry date.

- **POL-LEGC-001-F (Model Regulatory Status):** No AI/ML model currently in production within the Clinical AI Platform may have an undefined "Regulatory Status" tag in the MRMS. The status must be actively maintained as a function of this RCM process.

---

## 5. Detailed Procedures

This section details the four core phases of the RCM lifecycle: Horizon Scanning, Impact Assessment, Implementation Planning, and Tracking & Closure.

### 5.1 Phase I: Regulatory Horizon Scanning

**Objective:** To systematically identify, capture, and perform an initial triage on all potentially relevant regulatory developments.

**5.1.1 Sources and Cadence**
The Regulatory Horizon Scanner is responsible for monitoring the configured sources detailed in the table below. This is a continuous activity, supplemented by a mandatory deep-dive review conducted every Monday morning (or next business day if a holiday).

| Source Category | Specific Source | Monitoring Freq. | Method |
| :--- | :--- | :--- | :--- |
| **EU Official Publications** | Official Journal of the European Union (EUR-Lex), EC AI Office announcements, EDPB guidance. | Daily | Automated RSS Feeds integrated into CUBE; manual review of CUBE-curated summaries. |
| **U.S. Federal** | U.S. Federal Register, HHS/OCR announcements, Federal Reserve Board (SR letters). | Daily | Manual review of Federal Register subscription and relevant agency press rooms. |
| **National Data Protection** | Berlin DPA (BlnBDI), other lead supervisory authorities for GDPR. | Weekly | Manual review of authority websites; alerts subscribed via DLA Piper’s Focus on Data newsletter. |
| **US State-Level** | Comprehensive state privacy laws (e.g., California, Colorado, Connecticut). | Weekly | CUBE RegPlatform configured for cross-referencing with Meridian customer geography. |
| **Industry Standards** | NIST, ISO/IEC JTC 1/SC 42 (AI), HITRUST CSF updates. | Monthly | Membership body notifications; manual review of standards body websites. |

**5.1.2 Triage and Logging**
Within two (2) business days of an identified regulatory publication, the Regulatory Horizon Scanner will create a preliminary RCI record in RSA Archer with the following details:
- **RCI-ID:** Auto-generated (e.g., RCI-2026-047).
- **Source Reference:** Direct, persistent hyperlink to the publication (e.g., `EUR-Lex:32024R1689`).
- **Title:** Formal title of the publication.
- **Summary:** A 100-200 word executive summary of the publication's purpose and scope.
- **Triage Decision:** Selection of one of three initial states using the RCM Decision Tree (Appendix A):

| Triage State | Definition | Next Step |
| :--- | :--- | :--- |
| **Not Applicable** | The regulation clearly and inarguably does not apply to Meridian's business model, geographies, or data. | Record closed with justification. |
| **Potentially Applicable** | The regulation may apply, and further analysis is required. This is the default state for any ambiguous item. | **Escalate to Phase II: Impact Assessment.** |
| **Applicable & Urgent** | The regulation (e.g., an emergency enforcement ruling) directly impacts current Meridian operations with an immediate compliance date. | Escalate directly to the CCO and General Counsel within 4 hours of identification. |

### 5.2 Phase II: Impact Assessment

**Objective:** To perform a cross-functional, authoritative assessment of an RCI’s applicability, materiality, and the operational gap to compliance.

**5.2.1 Triggering and Convening**
Upon an RCI entering the "Potentially Applicable" state, the Impact Assessment Lead has five (5) business days to convene the Impact Assessment Working Group. The core group comprises:
- Impact Assessment Lead (Legal & Compliance Counsel, Chair).
- Head of Product for the impacted business unit (e.g., Product Director for Clinical AI).
- Chief Architect or designated senior engineer.
- A representative from the Security & Privacy Engineering team.
- A representative from the Data Governance team.
- The DPO (if personal data is involved).

**5.2.2 The Impact Assessment Procedure**
The Working Group will use the "Meridian Impact Assessment Template" (F-LEGC-001) stored in Archer. The assessment is a structured, evidence-based process with a target completion time of ten (10) business days from the first meeting.

The procedure is as follows:
1.  **Applicability Confirmation:** The group confirms the RCI applies to Meridian. This is a binary decision (Yes/No). If No, the RCI is closed with a detailed legal rationale.
2.  **Operational Gap Analysis:** For an applicable RCI, the group identifies the current state of Meridian's operations (people, process, technology) versus the target state required by the regulation. A gap is recorded for each unmet obligation.
3.  **Materiality Scoring:** Each identified gap is scored independently for Financial Impact, Reputational Impact, and Operational Disruption likelihood using the company-wide 5x5 risk matrix in SOP-RISK-001. The highest individual score determines the overall RCI Materiality (High, Medium, Low).
4.  **Business Unit & System Scoping:** The assessment explicitly names:
    - **Impacted Platforms:** (e.g., Clinical AI Platform, Snowflake Data Cloud).
    - **Impacted Data Domains:** (e.g., MRI Training Data, Consumer Health Insights).
    - **Required Lineage:** New or modified Alation data lineage that must be documented.
    - **Proposed Control Owners:** (e.g., VP, Clinical AI for model performance obligations).
5.  **Draft Remediation Mandate:** The assessment outlines the key deliverables for a compliant state, which will serve as the basis for the implementation plan.
6.  **Sign-off:** The completed Impact Assessment Form must be electronically signed in Archer by the Impact Assessment Lead, all contributing Working Group members, and for all items scored Medium or High, the General Counsel.

### 5.3 Phase III: Implementation Planning and Execution

**Objective:** To translate the approved Impact Assessment into a tracked, SLA-governed project plan executable by product and engineering teams.

**5.3.1 The Remediation Kick-Off**
Within five (5) business days of the Impact Assessment’s sign-off, the Implementation Owner, in consultation with the Control Owner, must host a formal Remediation Kick-Off meeting. The output is a structured "Remediation Plan" Epics in Jira, linked to the RCI-ID in Archer.

Each Jira Epic must decompose the mandate into discrete, assignable tasks, each with a "Regulatory_Compliance" label. No task may be longer than a two-week sprint cycle.

**5.3.2 SLA Framework for Implementation**
The target completion date for the final task in the Remediation Plan is governed by the materiality of the RCI, as measured from the Remediation Kick-Off date:

| Materiality | Target Remediation Completion | Escalation Threshold (from now) | Required Approval for Delay |
| :--- | :--- | :--- | :--- |
| **High** | 60 calendar days | 75 calendar days from Kick-Off | Chief Executive Officer or Chief Product Officer |
| **Medium** | 90 calendar days | 110 calendar days from Kick-Off | Chief Compliance Officer |
| **Low** | Incorporation into next normal product planning cycle, not to exceed 6 months. | 7 months from Kick-Off | Business Unit General Manager |

**5.3.3 Data Lineage Documentation (Alation)**
For any RCI where the Impact Assessment requires a new or modified data lineage, the following procedure applies:
1.  The Data Governance representative will create a "Data Source to Consumption" lineage ticket in Jira, linked to the main RCI Epic.
2.  The Chief Data Architect is responsible for ensuring the lineage is correctly modeled in Alation, including:
    - **Technical Lineage:** Column-level flow from source databases (e.g., Cerner EHR extracts) through Snowflake schemas to the target object (e.g., an ML feature set or a dashboard view).
    - **Business Lineage:** A clear, plain-English description of the business transformation (e.g., "Patient admission data is blended with clinical lab data to create the 'Readmission Risk Score' input table.").
    - **Governance Tags:** All tables and columns must have stewardship, classification (per SOP-IS-004), and regulatory obligation tags (e.g., `reg:EU-AI-Act Art-10`, `reg:HIPAA §164.314`) correctly applied.
3.  The lineage is deemed complete only when it is verified by the Independent Assessor.

### 5.4 Phase IV: Control Validation, Tracking, and Closure

**Objective:** To provide an independent, auditable verification that a remediation is complete and the resulting control is operationally effective, and then to formally close the regulatory change lifecycle.

**5.4.1 Control Validation Testing**
Upon the Implementation Owner setting all tasks in a Jira Remediation Epic to "Done," the Control Owner must request the Independent Assessor to conduct a Control Validation Test (CVT). The test design and timing depend on the Control Type. The RCI is tracked via an "RCM Status Dashboard" in Archer.

| Control Type | Validation Method | Responsible Assessor | Evidence |
| :--- | :--- | :--- | :--- |
| **Technical/Automated** | A scripted or tool-based control execution test designed to prove the control operates as designed. | Information Security or Data Platform Engineering Lead. | Test script output, system log screenshots. |
| **Administrative/Manual** | A test of design and an operating effectiveness sample test of the procedure over a 30-day operational period. | Internal Audit Lead Auditor. | Documented procedure, sample set of executed logs, approval artifacts. |
| **AI Model Performance** | A silent production run comparing model outputs pre- and post-change against an accepted validation dataset, including fairness metrics. | Head of Model Validation. | Model Validation Report, MRMS system logs. |

**5.4.2 Closure**
An RCI can only be moved to "Closed" status in Archer upon successful upload of the following final evidence package:
1.  The signed Impact Assessment (F-LEGC-001).
2.  The Jira Epic, where every user story and technical task is in a "Done" status.
3.  The verified Alation lineage diagram (a permalink to the Alation view).
4.  The signed Control Validation Test report confirming the control is "Operating Effectively."

The General Counsel is Accountable for the final closure of high-materiality RCIs.

---

## 6. Controls and Safeguards

The Meridian RCM program relies on a multi-layered set of administrative and technical controls to ensure its integrity.

### 6.1 Administrative Controls

| Control ID | Control Activity | Applied Control Standard | Owner | Frequency |
| :--- | :--- | :--- | :--- | :--- |
| **AC-01** | RCM Policy Review | This SOP (SOP-LEGC-001) is reviewed annually. | Thomas Anderson, CCO | Annual (or on material regulatory change) |
| **AC-02** | Horizon Scanning Validation | A retrospective analysis compares Meridian's RCI list to a leading external law firm's quarterly regulatory update. | Maria Chen, Dir. Reg. Intel. | Quarterly |
| **AC-03** | RCM Training | All roles identified in Section 3 must complete the "Regulatory Change 101" training module. | VP, Human Resources | On-assignment, Annually |
| **AC-04** | Vendor Regulatory Review | All new high-risk vendors are assessed for their own regulatory compliance posture. | VP, Procurement | On-vendor onboarding, Annual |
| **AC-05** | Audit Trail Integrity | No user in Archer or Jira has the ability to delete a record. All changes are logged in an immutable audit trail that is backed up daily. | CTO | Continuous |

### 6.2 Technical Controls

| Control ID | Control Activity | Technical Implementation | Owner | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Automated Data Classification | Default PHI/PII classification labels are auto-applied upon data ingestion into Snowflake using regex-based pattern matching. | VP, Data Platform | Quarterly scan for untagged sensitive columns. |
| **TC-02** | Policy-As-Code | Controls related to data locality (e.g., EU data stays in AWS Frankfurt) are enforced via OPA/Kyverno policy engines. | CISO | Bi-annual penetration test. |
| **TC-03** | Immutable Lineage Log | Alation lineage and metadata changes are written to an append-only log. | VP, Data Platform | Monthly audit log review. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) – Process Efficiency
These metrics measure the performance of the RCM process itself. They are to be aggregated and rendered in a live PowerBI dashboard fed from the Archer data lake.

| KPI ID | Metric | Target | Measurement Method | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | Horizon Scanning Timeliness | 95% of RCIs created within 2 business days of publication. | (RCI Creation Date - Publication Date) <= 2 Business Days. | Maria Chen |
| **KPI-02** | Impact Assessment Agility | 90% of Impact Assessments complete within 10 business days. | (Assessment Sign-off Date - Phase II Trigger Date) <= 10 Business Days. | Anya Sharma |
| **KPI-03** | Remediation Plan On-Time Rate | 90% of medium-criticality RCI Epics complete by target date. | (Final Task Date <= Epic Target Date). | Thomas Anderson |
| **KPI-04** | RCI Closure Efficiency | Average age of an RCI from "Identified" to "Closed" shall be < 120 days for Medium-criticality items. | (Closure Date - Creation Date) for RCI population. | Thomas Anderson |

### 7.2 Key Risk Indicators (KRIs) – Control Effectiveness
These metrics measure residual risk that may require management escalation.

| KRI ID | Metric | Risk Appetite Threshold | Escalation Path |
| :--- | :--- | :--- | :--- |
| **KRI-01** | Expired Exceptions | Zero. Any expired exception is an automatic escalation. | CCO → General Counsel → Audit Committee |
| **KRI-02** | High-Materiality RCI Overdue | Any single RCI past its SLA target. | CCO → General Counsel → CEO |
| **KRI-03** | Untracked Model Deployments | MRMS inventory does not match > 3% of production instances. | Head of AI Risk → CTO → Risk Committee |

### 7.3 Reporting Cadence
- **Continuous Monitoring:** The live RCM Status Dashboard in Archer is available to all impacted Control and Implementation Owners.
- **Monthly Report:** The CCO generates a "RCM Monthly Status Report" summarizing KPI and KRI status, open High/Medium RCIs, and upcoming horizon milestones. This is distributed to the Legal & Compliance Review Board.
- **Quarterly Review:** The CCO presents a formal review of the RCM program to the Risk Committee of the Board of Directors, including the status of all High-materiality items and any open exceptions.

---

## 8. Exception Handling and Escalation

### 8.1 Requesting a Procedure Exception
Any deviation from the timeline SLAs or the mandated steps of this SOP requires a formal exception. The process is as follows:
1.  The **Requestor** (e.g., Implementation Owner) submits a request through the "Regulatory Exception" workflow in RSA Archer, including:
    - The specific procedural step or SLA from which an exception is requested (e.g., Extension of Medium-criticality deadline beyond 90-day SLA).
    - The compelling business rationale (e.g., "Requires downtime in a critical clinical system only available during a scheduled window in Q3.").
    - A proposed compensatory control (e.g., manual review of model outputs on a daily basis until automated control is deployed).
    - A new proposed completion date.
2.  The **CCO** reviews the request for completeness and risk context.
3.  The request is then routed for approval based on materiality:

| Materiality Level | Approval Authority | Maximum Extension Period |
| :--- | :--- | :--- |
| **Low** | Business Unit General Manager | 3 months, renewable once. |
| **Medium** | Chief Compliance Officer | 30 calendar days, no renewal. |
| **High** | Legal & Compliance Review Board (quorum of 3) | 30 calendar days, no renewal. |

### 8.2 Escalation Path for Conflict Resolution
If a Control Owner and an Implementation Owner are in fundamental disagreement on the scope or feasibility of a required remediation, the following escalation path is followed, with the issue resolved by the first capable decision-maker:
1.  Thomas Anderson, Chief Compliance Officer
2.  Maria Gonzalez, General Counsel
3.  Chief Executive Officer

All escalation decisions and their rationale are documented in the RCI record in Archer.

---

## 9. Training Requirements

The effectiveness of this SOP depends on an informed workforce. All personnel assigned a role in Section 3 must complete targeted training regardless of their seniority or prior experience.

### 9.1 Training Curriculum
The Meridian Learning Management System (LMS, powered by Workday Learning) will assign the following mandatory curriculum based on persona:

| Persona | Required Courses | Frequency |
| :--- | :--- | :--- |
| **All Staff** | RCM-101: "Our Shared Responsibility for Regulatory Compliance" — a 30-minute awareness course covering the RCM lifecycle at a high level and how to raise a concern. | On hiring; Annually thereafter. |
| **RCM Core Roles (Section 3)** | RCM-201: "Executing Regulatory Change at Meridian" — a 3-hour deep-dive workshop combining SOP-LEGC-001 with hands-on exercises in completing the Impact Assessment and building a Jira Remediation Plan. | On assignment to role; refresher required upon any revision to this SOP or after 18 months in role. |
| **Engineers and Architects** | RCM-301: "Building Compliance Lineage" — a 90-minute technical training on tagging data sources in Alation and constructing technical lineage. | On assignment to role; Every 12 months. |

### 9.2 Training Compliance
The VP, Human Resources is the Control Owner for the "RCM Training Compliance" metric. A quarterly report must be generated from Workday showing a 98% or higher completion rate for required courses among active, assigned personnel. Any shortfall must be addressed with individual corrective action within 14 days.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- **SOP-IS-004:** Data Classification and Handling Policy
- **SOP-IS-007:** Vendor Risk Management
- **SOP-RISK-001:** Enterprise Risk Management Framework and Taxonomy
- **SOP-LEGC-002:** EU AI Act Conformity Assessment and Post-Market Monitoring
- **SOP-LEGC-004:** HIPAA Privacy Rule Compliance for Protected Health Information
- **SOP-MODEL-001:** Model Risk Management and the MRMS Lifecycle
- **SOP-SEC-002:** Identity and Access Management
- **SOP-ENG-002:** Secure Software Development Lifecycle

### 10.2 External References
- Regulation (EU) 2024/1689 (Artificial Intelligence Act)
- Health Insurance Portability and Accountability Act of 1996 (HIPAA) and implementing regulations, 45 C.F.R. Parts 160, 162, and 164.
- General Data Protection Regulation (Regulation (EU) 2016/679)
- Board of Governors of the Federal Reserve System, SR Letter 11-7: "Supervisory Guidance on Model Risk Management"
- National Institute of Standards and Technology, AI Risk Management Framework 1.0 (NIST AI 100-1)
- AICPA, Trust Services Criteria for SOC 2 examinations

### 10.3 Key Templates and Forms
- **F-LEGC-001:** Impact Assessment Template (in RSA Archer)
- **F-LEGC-002:** Exception and Risk Acceptance Request Form (in RSA Archer)

---

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **1.0** | 2023-05-15 | T. Anderson, A. Sharma | Initial release of the RCM SOP, aligning with the launch of the Clinical AI Platform CE marking process. |
| **1.5** | 2024-02-22 | M. Chen, A. Sharma | Major revision to add the Horizon Scanning procedure (Section 5.1), formalize the Archer-based logging schema, and incorporate SR 11-7 alignment following the Model Validation team expansion. |
| **2.0** | 2024-08-30 | T. Anderson, A. Sharma, D. Vogel | Substantial rewrite to operationalize EU AI Act obligations (Art. 9, 10, 15, 17, 43) ahead of the February 2025 applicability dates for high-risk systems. Added explicit Alation lineage SLA (Section 5.3.3) and the Model Validation Test. |
| **2.3** | 2025-03-11 | T. Anderson | Streamlined the Impact Assessment roles; added the KRI dashboard framework in Section 7 following a series of overdue medium-criticality items. |
| **2.5** | 2025-09-01 | M. Chen | Post-HITRUST audit adjustment: strengthened the controls in Section 6 for identity and access management of the Archer and Jira tools. Updated HIPAA procedures to align with OCR guidance on pixel-tracking technologies. |
| **2.7** | 2025-11-27 | T. Anderson, D. Vogel | Refined NIST AI RMF integration points. Updated international data transfer procedures and privacy notice requirements in the context of the Clinical AI Platform expansion into new therapeutic areas. Updated CISO review cadence. |

---

**APPENDIX A: RCM Decision Tree (Referenced in Section 5.1.2)**

**[Start]**
1.  Is the regulatory publication from a jurisdiction where Meridian has operations, customers, or data subjects?
    - **No** → [Not Applicable. Close with geographic limitation rationale.]
    - **Yes** → Go to Step 2.
2.  Does the content of the publication regulate an activity, technology, or data type (e.g., PHI, personal data, training data, ML model) that Meridian directly produces, uses, or manages?
    - **No** → [Not Applicable. Close with scope limitation rationale.]
    - **Yes** → Go to Step 3.
3.  Does the publication create a new obligation, or does it materially alter an existing obligation that would change an implemented compliance control?
    - **No** → [Record for information only. Log as "Monitoring" in Archer.]
    - **Yes** → Go to Step 4.
4.  Is the effective date of the new obligation within the next 3, 6, or 12 months?
    - **12+ months** → [Record as "Potentially Applicable — Watch." Set a reminder to reassess in 6 months.]
    - **3-12 months** → [Log as **"Potentially Applicable"**. Escalate to Phase II within 5 business days.]
    - **< 3 months** → [Log as **"Applicable & Urgent"**. Immediate escalation to the CCO and General Counsel.]
    - **Effective Date Past** → [Log as **"Non-Compliance Suspected"**. Immediate escalation per the Incident Response Plan (SOP-SEC-001).]
---
**[End of Document]**