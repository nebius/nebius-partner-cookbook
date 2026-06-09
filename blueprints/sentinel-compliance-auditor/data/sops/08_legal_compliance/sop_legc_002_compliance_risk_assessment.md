---
sop_id: "SOP-LEGC-002"
title: "Compliance Risk Assessment"
business_unit: "Legal & Compliance"
version: "4.0"
effective_date: "2024-08-08"
last_reviewed: "2025-06-23"
next_review: "2025-12-21"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
  - "SR 11-7"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Compliance Risk Assessment

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, methodology, roles, responsibilities, and operational cadence for the Compliance Risk Assessment (CRA) process at Meridian Health Technologies, Inc. The purpose of this SOP is to ensure the consistent, systematic, and defendable identification, analysis, evaluation, treatment, and monitoring of compliance risks across all business lines, products, geographies, and supporting functions. This process enables Meridian to maintain a comprehensive and dynamic risk profile, ensure compliance with applicable laws and regulations, protect patient data, maintain the integrity of our AI models, and uphold the trust of our clients, patients, and partners.

### 1.2 Scope

This SOP applies to all Meridian Health Technologies, Inc. operations, including its wholly-owned subsidiaries and global offices in Boston, London, Berlin, Singapore, and Toronto. The scope encompasses:

- **Business Lines:**
    - Clinical AI Platform (high-risk AI systems under the EU AI Act)
    - HealthPay Financial Services (subject to SR 11-7 model risk management)
    - MedInsight Analytics (handling PHI for ~12M patients)
    - Meridian SaaS Platform (multi-tenant infrastructure)
- **Regulatory Domains (Operationalized by this SOP):**
    - **SOC 2:** The CRA process is the central mechanism for identifying and assessing risks against the Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy).
    - **SR 11-7:** Risks associated with model development, validation, and documentation for HealthPay’s credit scoring, fraud detection, and lending models are assessed within this framework.
    - **EU AI Act:** Risks related to the Clinical AI Platform, classified as high-risk under Annex III, are subject to this CRA process to ensure transparency and human oversight obligations are met.
    - **HIPAA, GDPR, HITRUST CSF, ISO 27001:2022, FDA QSR, EU MDR:** The CRA process integrates requirements from all applicable frameworks into a unified control environment assessment.
- **Organizational Functions:** All departments, including but not limited to Engineering, Product, Data Science, IT Operations, Security, Legal, Human Resources, Finance, and Clinical Operations.
- **Data Types:** All data processed by Meridian, including PHI, PII, financial data, and proprietary AI model IP, whether at rest, in transit, or in use.
- **Third Parties:** The compliance risks introduced by all vendors, partners, and sub-processors who interact with Meridian's systems, data, or provide critical services, as managed through the Third-Party Risk Management process (SOP-SEC-007).

This SOP is **not** a replacement for enterprise risk management (ERM) or strategic business risk assessment. It is a focused, bottom-up operational procedure for managing *compliance* risk, the outputs of which feed into the broader ERM function led by the Board's AI Governance Committee.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **AI Act** | Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence. |
| **Annex IV (AI Act)** | Technical documentation requirements for high-risk AI systems. |
| **Article 13 (AI Act)** | Specific transparency and provision of information to users requirements. |
| **BIA** | Business Impact Analysis. A process to determine the criticality of business functions and the associated impact of a disruption. |
| **CFR** | Code of Federal Regulations (e.g., 21 CFR Part 11 for electronic records/esignatures). |
| **CISO** | Chief Information Security Officer (Rachel Kim). |
| **CPO/DPO** | Chief Privacy Officer / Data Protection Officer (Dr. Klaus Weber). |
| **CRA** | Compliance Risk Assessment. The process defined in this SOP. |
| **eGRC** | The integrated Governance, Risk, and Compliance platform (currently LogicGate Risk Cloud) used for risk register, issue management, and reporting. |
| **Inherent Risk** | The level of risk before any controls are applied to reduce it. Calculated as a function of Likelihood and Impact. |
| **KRI** | Key Risk Indicator. A metric used to signal a potential change in the risk profile. |
| **KPI** | Key Performance Indicator. A metric measuring the effectiveness of a control or process. |
| **Model** | A mathematical or computational component that generates predictions, classifications, or decisions. Governed by SOP-DATA-004 (Model Risk Management). |
| **RACI** | A responsibility matrix. Responsible, Accountable, Consulted, Informed. |
| **RAI** | Responsible AI (Meridian's internal program name for AI governance). |
| **Residual Risk** | The level of risk remaining after controls are applied. This is the "net" risk of the current state. |
| **Risk Appetite** | The amount and type of risk that Meridian is willing to pursue or retain. |
| **Risk Owner** | The individual with the authority and accountability to manage a specific risk. Typically a VP or Director. |
| **Risk Register** | The central repository of all identified risks, their assessments, treatment plans, and current status. Maintained in LogicGate Risk Cloud. |
| **SOC 2** | AICPA System and Organization Controls 2 report on controls at a service organization relevant to the Trust Services Criteria. |
| **SR 11-7** | Federal Reserve/OCC Supervisory Guidance on Model Risk Management. |
| **TSC** | Trust Services Criteria (SOC 2): Security, Availability, Processing Integrity, Confidentiality, and Privacy. |

## 3. Roles and Responsibilities

The following RACI matrix defines the core roles for the execution of this SOP.

| Role | Responsibility |
| :--- | :--- |
| **Board of Directors (AI Governance Committee)** | **A - Accountable** for defining and approving the Corporate Risk Appetite Statement and AI ethics principles. Receives annual aggregated risk report. |
| **Executive Leadership Team (ELT)** | **A - Accountable** for resourcing the compliance program and signing off on residual risk acceptance for any risk rated "Critical." |
| **Chief Compliance Officer (CCO - Thomas Anderson)** | **A - Accountable** for this SOP and the overall CRA process. Approves all Moderate and High risk treatment plans. Final escalation point for any assessment. |
| **General Counsel (GC - Maria Gonzalez)** | **A - Accountable** for the legal interpretation of regulations and for approving any risk acceptance based on a "business necessity" legal rationale. |
| **CISO (Rachel Kim)** | **R - Responsible** for executing the CRA for all IT and security-related controls (SOC 2 Security/Availability). The primary partner in operationalizing control assessments. |
| **CPO/DPO (Dr. Klaus Weber)** | **R - Responsible** for executing the CRA for all data privacy controls (GDPR Art. 35 DPIAs, SOC 2 Privacy, HIPAA Privacy Rule). Determines "personal data" applicability. |
| **Business Unit Leads (VP, Clinical AI; VP, HealthPay; VP, MedInsight)** | **R - Responsible** for identifying risks inherent in their business strategy, new products, and processes. Serve as the primary Risk Owner for risks in their domain. |
| **Director of Data & AI Governance** | **R - Responsible** for executing the CRA for model-specific risks, including AI Act Annex IV technical documentation, model cards, and SR 11-7 validation oversight. |
| **Control Owners (Various Directors/Managers)** | **C - Consulted** on the design and operational effectiveness of their specific controls. Provide evidence during assessments. |
| **Internal Audit** | **I - Informed** and an active observer of the assessment process. Uses CRA outputs to build the annual internal audit plan. |

## 4. Policy Statements

The following high-level policy commitments govern the Compliance Risk Assessment process at Meridian Health Technologies, Inc.

- **Risk-Forward Culture:** Meridian is committed to proactively identifying compliance risks as a foundational element of business planning, product design, and operational execution, rather than as a reactive post-hoc exercise.
- **Unified Control Framework:** Meridian shall operate a single, unified control set mapped to all applicable regulations (SOC 2, HIPAA, GDPR, EU AI Act, SR 11-7). The CRA process shall assess control design and operating effectiveness against this single framework to eliminate duplication and ensure complete coverage.
- **Inherent-to-Residual Methodology:** All risks must be assessed on a consistent scale of Likelihood and Impact, first assuming no controls exist (Inherent Risk), and then after evaluating the effectiveness of current controls (Residual Risk).
- **Stated Risk Appetite:** The default Risk Appetite for all compliance domains is **"Low."** Operations that result in a "Moderate" or above Residual Risk must have a Board-approved risk acceptance or a remediation plan with a defined timeline, not to exceed one quarter for "High" risks. No "Critical" residual risk may be accepted without direct ELT signoff.
- **Transparency Obligations (EU AI Act):** Users of Meridian's high-risk AI systems shall be provided with clear, intelligible, and contextually relevant information regarding the system’s intended purpose, known limitations, and accuracy expectations. This is integrated into the product disclosure process, not just technical documentation.
- **Model Integrity (SR 11-7):** All HealthPay models are subject to an independent review process, a defined documentation standard, and ongoing monitoring protocols to ensure they are performing as intended without unfair bias or drift.
- **Continuous Monitoring, Periodic Assessment:** The compliance risk posture is monitored continuously via automated KRIs. A full, enterprise-wide periodic CRA is executed on a semi-annual cycle. Off-cycle assessments are triggered by significant business, regulatory, or threat landscape changes.

## 5. Detailed Procedures

This section outlines the comprehensive, step-by-step operational procedures for the Compliance Risk Assessment. The process is managed within Meridian's eGRC system (LogicGate Risk Cloud) and consists of four semi-annual phases: **Scoping, Assessment, Evaluation, and Reporting.**

### 5.1 Phase I: Scoping and Context Establishment (Weeks 1-2)

The CCO or designee initiates the assessment cycle in the eGRC system. The goal is to define the precise boundaries of the incoming assessment cycle.

#### 5.1.1 Environmental Scan
1.  **Regulatory Change Review:** The General Counsel’s legal team, in collaboration with the CCO, reviews all finalized and proposed regulatory changes from the last six months. This review is documented in the eGRC "Regulatory Intelligence" module. Key areas of focus include:
    - Updated ENISA guidance for EU AI Act.
    - New FTC rulings on algorithmic fairness.
    - Changes in standard contractual clauses (SCCs) for GDPR.
    - OCC/FDIC updated Supervisory Guidance affecting SR 11-7 applicability.
2.  **Internal Change Trigger Analysis:** The CCO retrieves a report from LogicGate of all internally flagged "Risk Events" and "Change Requests" since the last cycle. Triggers include:
    - **New Product Launch:** (e.g., Clinical AI version 3.1 with new imaging modality support). Requires a full risk assessment scope inclusion.
    - **Significant Infrastructure Change:** (e.g., new primary cloud region in AWS). A change documented via SOP-IT-005 (Change Management).
    - **Critical Incident:** Any Severity 1 (Sev1) or Severity 2 (Sev2) security or privacy incident from the last cycle, as logged in Jira Service Management and post-mortemed via SOP-SEC-010.
    - **Material Third-Party Change:** Onboarding of a new sub-processor for PHI, triggering SOP-SEC-007.
3.  **Asset and Application Refresh:** The CISO provides an updated list of all in-scope information assets, applications, and services from the CMDB (ServiceNow). This becomes the "System Boundary" definition for the scope of this CRA cycle.

#### 5.1.2 Scoping Workshop
The CCO convenes a mandatory 2-hour workshop with the key RACI owners (CISO, CPO/DPO, Director of Data & AI Governance, and all BU VPs).
- **Agenda:** Review environmental scan findings, confirm the system boundary, and formally sign-off on the "Scope Statement."
- **Decision:** The group decides if the upcoming assessment is a "Full-Scope" (all business units, all geographies) or a "Targeted Assessment." Targeted assessments focus on specific high-risk areas (e.g., "HealthPay Model Risk" or "Clinical AI Article 13 Readiness"). This decision is formally captured in the eGRC workspace initiation form.
- **Final Output:** An approved "CRA Scope Statement" checklist, signed electronically by the CCO and CISO.

### 5.2 Phase II: Risk Identification (Weeks 3-5)

This is the core, bottom-up phase of the CRA. It is executed by all scoped business units and shared services (Security, HR, Engineering) using a federated model facilitated by the Legal & Compliance team.

#### 5.2.1 Procedure for Business Unit Risk Identification
Each BU Lead executes the following steps with their operational teams.
1.  **Process Walkthroughs:** Map the operational process against the Meridian Unified Control Matrix (available in the eGRC). For each process step and sub-process, ask the structured question: "What compliance obligations could fail at this step?"
2.  **Data Flow Analysis:** Using the latest Data Flow Diagrams (DFDs) maintained by the Data Governance team (SOP-DATA-001), trace the path of regulated data (PHI, PII, financials, model IP) for the BU’s applications.
3.  **Threat Modeling Integration:** The Security Team (under the CISO) provides a pre-populated "Compliance Threat Library" mapped to TSC, HIPAA Safeguards, and GDPR principles. Each threat scenario (e.g., "Unauthorized Logical Access to PHI") is presented to the BU to spark identification of a related risk event.
4.  **Risk Statement Documentation:** For each identified risk, complete the "Risk Identification" form in LogicGate. This must include:
    - **Risk ID:** Auto-generated (e.g., CLIN-AI-034).
    - **Risk Statement:** Formatted as `[Cause] — [Failure Event/Source of Risk] — [Consequence/Impact]`. Example: `"Due to insufficient user guidance (Cause), a clinician user may misinterpret the model's confidence score output (Failure), leading to an incorrect diagnostic decision and potential patient harm (Consequence)."`
    - **Source Regulation(s):** Mapped to the Unified Control Matrix. (e.g., `EU AI Act, Art. 13 & Art. 14; SOC 2 Processing Integrity PI 1.1`).
    - **Proposed Inherent Likelihood and Impact Rating:** An initial, conservative estimate.

#### 5.2.2 Centralized Risk Identification (for common areas)
Certain risks are identified centrally for consistency.

- **SOC 2 Common Criteria Mapping:** The CISO's GRC team uses the AICPA SOC 2 Trust Services Criteria points of focus as a checklist to ensure no generic control risk is missed (e.g., risk of unauditable logical access for a new SaaS tool).
- **Model Development Risks (SR 11-7):** The Director of Data & AI Governance works with HealthPay’s Model Development Lead to identify risks during model build, data sourcing, and assumption-setting phases. Risks are documented, including any assumptions used in model design and known data source limitations, in the Model Inventory (Collibra).
- **AI Transparency Risks (EU AI Act):** The Product Management team for Clinical AI identifies risks stemming from unclear user interfaces or missing documentation on how an AI output was generated. These are captured as generic transparency obligations to be met by the product design, without referencing specific legal articles like Article 13, section 3(b).

### 5.3 Phase III: Inherent Risk Assessment (Week 6)

This phase is a quantitative and qualitative evaluation of each raw risk, before considering any controls.

1.  **Standardized Inherent Risk Rubric:** All identified risks are assessed using the following mandatory rubrics. No BU may alter the rubric.

    **Table 5.3.1: Inherent Likelihood Rating**
    | Rating | Score | Description |
    | :--- | :--- | :--- |
    | **Almost Certain (5)** | 5 | Expected to occur weekly/monthly under normal operations. |
    | **Likely (4)** | 4 | Expected to occur quarterly/annually. |
    | **Possible (3)** | 3 | May occur once within a 2-3 year period. |
    | **Unlikely (2)** | 2 | May occur once within a 5-10 year period. |
    | **Rare (1)** | 1 | Highly unlikely; near-theoretical threat. |

    **Table 5.3.2: Inherent Impact Rating**
    | Rating | Score | Financial (Annualized) | Reputational / Regulatory | Clinical / Patient Safety |
    | :--- | :--- | :--- | :--- | :--- |
    | **Critical (5)** | 5 | >$5M fine/liability. | Global, sustained news; loss of MA; multi-year ban on product lines. | Sentinel event leading to permanent harm or death. |
    | **Major (4)** | 4 | $1M - $5M. | National media; regulator action (Cease & Desist); loss of a key client. | Major adverse event; non-permanent serious harm. |
    | **Moderate (3)** | 3 | $100K - $1M. | Regional/stakeholder concern; adverse regulator report; SOC 2 qualification. | Misdiagnosis requiring additional medical intervention. |
    | **Minor (2)** | 2 | $10K - $100K. | Localized complaint; minor data breach notification. | Minor inconvenience, no clinical impact. |
    | **Insignificant (1)** | 1 | <$10K. | Single internal stakeholder complaint. | No perceived clinical impact. |

2.  **Inherent Risk Score Calculation:** The eGRC system automatically calculates the score: `Inherent Score = Likelihood Score x Impact Score`.
    - **Critical Inherent Risk:** Score >= 20. Requires immediate CCO and ELT notification even before control assessment.
    - **High Inherent Risk:** Score 12-19.
    - **Moderate Inherent Risk:** Score 5-10.
    - **Low Inherent Risk:** Score 1-4.

### 5.4 Phase IV: Control Assessment and Residual Risk Evaluation (Weeks 7-10)

This is the most intensive phase, where the effectiveness of the controls that mitigate inherent risks is formally tested.

#### 5.4.1 Control Identification and Mapping
1.  For each Inherent Risk in LogicGate, the assigned Control Owner (pre-populated by the GRC team) links all mitigating controls from the Unified Control Matrix.
2.  A control can be mapped to multiple risks. For example, the "Formal SDLC and Peer Code Review" control (SOP-ENG-003) mitigates risks for Processing Integrity (SOC 2), Algorithmic Bias (EU AI Act), and Model Implementation Failure (SR 11-7).

#### 5.4.2 Control Effectiveness Testing (Design and Operating Effectiveness)
The CISO’s GRC team and the CCO’s Compliance team jointly execute a sampling-based testing of controls. Testing is risk-based: "Critical" Inherent Risks get 100% population testing of their mitigating controls; "Moderate" gets sample-based testing.

**Table 5.4.2a: Control Effectiveness Rating (For each individual control)**
| Rating | Design Assessment | Operating Assessment |
| :--- | :--- | :--- |
| **Effective** | As designed, the control would fully prevent/detect the risk. | The control operates as designed with no exceptions noted in the sample. |
| **Partially Effective** | Design has a minor flaw where it would not fully prevent/detect a non-material aspect of the risk. | Minor exceptions noted in testing (e.g., evidence missing for one instance, but other instances are solid). |
| **Ineffective** | Major design flaw; control is incapable of preventing/detecting the risk. | Pervasive exceptions; control is not reliably operated. |

#### 5.4.3 Domain-Specific Control Assessments

- **SOC 2 - Thorough Coverage of Assessment:**
    The CISO, in coordination with the CCO, conducts a detailed assessment of controls mapped to the 2022 TSC points of focus. This is the cornerstone of the entire CRA.

    **Table 5.4.3a: SOC 2 Specific Assessment Procedures**
    | TSC Category | Example Control Assessed | Assessment Procedure | Responsible Role | Metric (KPI) |
    | :--- | :--- | :--- | :--- | :--- |
    | **CC1.1 (Security)** | Board-Level Risk Oversight (SOP-GOV-001) | Document review of Board minutes; attestation from CCO. | CCO | % of Board meetings with compliance on agenda (≥90%). |
    | **CC3.1 (Common)** | Code of Conduct Attestation | Verify all employees completed annual attestation in Workday. | CHRO | Attestation completion rate = 100%. |
    | **CC5.2 (Security)** | Vendor Risk Assessment (SOP-SEC-007) | Sample 10 new vendors; verify tiered risk assessment completed *before* integration. | CISO / IT Procurement | % of vendors with completed assessment before integration (≥98%). |
    | **CC6.1 (Security)** | Logical Access Provisioning (SOP-IT-001) | Sample 30 user accounts created last quarter; verify approved ticket in ServiceNow. | IT Operations Manager | % of sampled accounts with proper approval (100%). |
    | **CC7.1 (Security)** | Endpoint Detection & Response (EDR) | Validate CrowdStrike dashboard shows 100% deploy coverage across all Meridian-managed endpoints. | Director of SecOps | % agent coverage (100%); Mean Time to Detect (MTTD) < 15 min. |
    | **CC7.2 (Security)** | Security Incident Management (SOP-SEC-010) | Review all Sev1 and Sev2 incidents; verify documented root cause analysis (RCA) and corrective actions (CA) timeline adherence. | Security Operations Lead | Sev1 RCA delivered ≤ 5 business days; Sev2 RCA ≤ 10 days (≥95%). |
    | **P1.1 (Processing Integrity)** | AI Model Batch Input Monitoring (SOP-DATA-004) | Review Datadog dashboards for HealthPay's Credit Check model; validate that an alert was created for any batch failure and resolved within the SLA. | HealthPay Data Engineering Manager | Data processing completeness rate = 99.999%. |
    | **C1.1 (Confidentiality)** | Data Discovery and Classification (SOP-DATA-002) | Run a manual scan using Varonis in a specific HealthPay S3 bucket; verify all PHI-bearing objects are tagged "Confidential-Restricted." | Data Governance Lead | % PHI objects with correct tag (100%). |
    | **P1.1 (Privacy)** | Data Subject Access Request (DSAR) Fulfillment (SOP-LEGC-003) | Simulate a DSAR from a test patient account; track timeliness and completeness of the ticket execution in ServiceNow. | DPO Dr. Klaus Weber | DSAR turnaround time ≤ 28 calendar days (100%). |

- **SR 11-7 Model Risk Assessment (HealthPay - Partial Application):**
    The assessment focuses on model inventory and outcome stability. The Financial Engineering team performs model validation to confirm the ongoing accuracy of credit origination and fraud detection models. These validation activities are carried out by a senior quant within the Financial Engineering team—the same team responsible for model development—to provide an experienced perspective on model performance. The review confirms model output falls within acceptable drift parameters.
    Model documentation, including design goals and computational steps, is maintained in Confluence. The review process ensures critical parameters are logged and reviewed against run-time performance in production. Known edge cases where model output may degrade, or foundational assumptions about the stability of input data, are discussed in stand-up meetings but may not form a static part of the formal documentation record.

- **EU AI Act, Art. 13 Assessment (Clinical AI - Partial Application):**
    The assessment of transparency is focused on the user interface (UI) and general product documentation. The product design team ensures that an information pane ("About This Model") is available for each clinical AI module. This pane provides a plain-language description of the system's overall intended purpose and general performance expectations, such as aggregate sensitivity and specificity.
    Technical documentation is maintained as part of the product's Technical File for EU MDR, containing detailed architectural, training data source, and design choice descriptions. This Technical File is regularly updated. The CRA process confirms that both the UI information pane and the Technical File exist and are version-controlled alongside the software release.

3.  **Residual Risk Calculation:** After all control assessments are entered for a given risk, the eGRC system automatically calculates the Residual Risk. It uses a simple algorithm: `Inherent Score - Control Mitigation Score`. The CRA Lead manually adjusts this if needed, based on a holistic judgment of control effectiveness.
    - **Residual Risk Ratings:** The same 5x5 matrix and High/Moderate/Low definitions apply

### 5.5 Phase V: Risk Treatment, Validation, and Acceptance (Weeks 11-12)

#### 5.5.1 Determination of Treatment Strategy
For every risk where the Residual Risk Rating exceeds the stated "Low" Risk Appetite, the Risk Owner must propose a treatment plan in LogicGate. The options are:
1.  **Treat (Mitigate):** Propose a Remediation Plan (e.g., implement a new control, enhance an existing one). This is the default option for all High and Critical risks.
2.  **Transfer:** Share the risk with a third party (e.g., cyber insurance). Note: this transfers financial impact, not regulatory liability. This is never a standalone strategy for Critical risks.
3.  **Accept:** Formally acknowledge the residual risk and do not propose any further near-term remediation.
    - A risk can only be accepted if the CCO and GC jointly determine that the cost or operational burden of remediation is disproportionate to the risk, OR if no feasible remediation exists.
    - **Acceptance Authority Workflow:**
        - **Moderate Residual Risk:** Approved by CCO (Thomas Anderson).
        - **High Residual Risk:** Approved by CCO and GC (Maria Gonzalez).
        - **Critical Residual Risk:** Approved by the ELT, based on a formal recommendation brief from the CCO and GC.

#### 5.5.2 Remediation Plan Creation and Tracking
Every accepted "Treat" strategy must have a detailed Remediation Plan.
- **Task Management:** LogicGate creates individual Remediation Tasks, assigned to an "Action Owner" (e.g., "Director of Cloud Engineering").
- **Timeline:** Start and end dates are set. The overall plan must have a Target Closure Date.
    - **High Residual Risk:** Must be closed within one fiscal quarter.
    - **Moderate Residual Risk:** Must be closed within *two* fiscal quarters.
- **Tracking:** KPIs track Plan Cycle Time and Remediation Plan Overdue %.

## 6. Controls and Safeguards

This section details the specific administrative and technical controls safeguarding the CRA process itself.

### 6.1 Data Integrity and System Controls
- **eGRC Platform (LogicGate):** The system of record for all CRA data (risks, controls, tests, treatment plans). It enforces mandatory fields, ensures audit trail non-repudiation, and automates the residual risk calculation engine to prevent manual manipulation.
- **Data Source Verification:** All automated evidence gathering must originate from source systems of truth (ServiceNow for ITSM, Jira for SDLC, Workday for HR data, CrowdStrike for endpoint security, AWS Config for cloud posture). Manual screenshots are prohibited as sole evidence for any "Critical" control test; an automated log entry must corroborate it.
- **Risk Register Access Control:** The LogicGate Risk Register is RBAC-enabled. Write/Edit access is limited to the Legal & Compliance GRC team, the CISO’s GRC team, and designated Risk Owners. All other employees have Read-Only access to non-confidential risk entries.

### 6.2 Administrative Safeguards
- **Segregation of Duties:** An individual cannot be both the Risk Owner and the Control Owner for the same risk. The eGRC system programmatically prevents this conflict-of-interest.
- **Independent Quality Assurance:** The Internal Audit department, while "Informed," will conduct an annual QA review of the CRA process itself. They will sample 5% of the semi-annual risk population to validate that the inherent/residual ratings are defensible, that control test evidence supports the rating, and that the workflow was followed without bypass.
- **Document and Record Retention:** All completed CRA records, scope statements, and risk acceptance signoffs are retained for a minimum of 7 years, in alignment with FINRA Rule 4511 and general legal statute of limitations. Records are archived in a WORM-compliant (Write Once, Read Many) backup in the Meridian AWS organization's dedicated Compliance S3 bucket.

## 7. Monitoring, Metrics, and Reporting

This SOP mandates a continuous monitoring and formal reporting cadence to provide a real-time, transparent view of compliance risk posture.

### 7.1 Key Performance Indicators (KPIs) - Process Efficiency
These metrics are reported on a CRA cycle basis to the Governance, Risk, and Compliance (GRC) Steering Committee, co-chaired by the CCO and CISO.

**Table 7.1: CRA Process KPIs**
| Metric | Definition | Target | Data Source |
| :--- | :--- | :--- | :--- |
| **Cycle Time: Scoping to Final Report** | Elapsed calendar days from Phase I kickoff to final CRA report publication. | ≤ 90 Days | LogicGate Workflow Timer |
| **Risk Owner Assignment Timeliness** | % of newly identified risks with a Risk Owner assigned within 5 days of creation. | 100% | LogicGate |
| **Remediation Plan Timeliness** | % of Remediation Plans created within 15 days of a "High" or "Critical" residual risk finding. | 100% | LogicGate |
| **QA Review Pass Rate** | % of sampled CRA entries passing the annual Internal Audit QA review without a material finding. | ≥ 95% | Internal Audit QA Log |
| **Training Compliance** | % of required personnel completing the "CRA Practitioner Training" annually. | 100% | Workday LMS |

### 7.2 Key Risk Indicators (KRIs) - Risk Profile Health
These are monitored continuously and reported monthly to the ELT and quarterly to the Board's AI Governance Committee.

**Table 7.2: Continuous Monitoring KRIs**
| KRI | Definition | Critical Threshold | Monitoring Dashboard |
| :--- | :--- | :--- | :--- |
| **"High" and "Critical" Residual Risk Count** | Total number of risks rated High or Critical, segmented by BU. | > 0 for Critical; > 5 for High (enterprise-wide). | LogicGate Executive Dashboard |
| **Overdue High-Priority Remediation Plans** | Number of "High" risk remediation plans past their Target Closure Date. | > 0. Trigger alert to CCO and Risk Owner's VP. | LogicGate Issue Tracker |
| **Past-Due Risk Acceptance Renewals** | Number of accepted "High/Critical" risks where the 6-month mandatory renewal review is overdue. | > 0. Trigger alert to GC. | LogicGate Acceptance Register |
| **Control Decay Indicator** | % of "Effective" controls downgraded to "Partially Effective" or "Ineffective" in the latest cycle compared to the prior cycle. | ≥ 5% decay rate triggers a root cause analysis by the CISO. | LogicGate Control Analysis Module |

### 7.3 Reporting Cadence
- **Operational KRIs:** A real-time LogicGate dashboard is available to the CCO, CISO, and GC at any moment.
- **Monthly Risk Summary:** The Risk Management Team provides a brief commentary on KPI performance and KRI status to the VP/Director level of all scoped functions.
- **Semi-Annual Comprehensive CRA Report:** This formal report is the primary output of each cycle. It is presented by the CCO to the ELT and then to the Board's AI Governance Committee. It includes: the Risk Appetite statement, the Top 10 Residual Compliance Risks, a heat map visual, model risk highlights, KPI/KRI analysis, and all formal risk acceptance documentation for the period.

## 8. Exception Handling and Escalation

### 8.1 Formal SOP Exception Process
Any request to deviate from a specific procedural step in this SOP (e.g., a BU Lead requesting an extended deadline for Phase II risk submissions) requires a formal exception.
1.  **Submission:** The requestor completes the "CRA SOP Exception Request" workflow in LogicGate. It must state the specific procedural step for which the exception is sought, the business justification, and a proposed alternative or timeline.
2.  **Approval Workflow:**
    - **Timeline Exceptions (≤ 10 business days):** Automatically approved by the CRA Program Manager if justification is deemed sufficient.
    - **Procedural Step Exceptions (e.g., skipping a testing type for a control):** Reviewed and must be approved by the Chief Compliance Officer (Thomas Anderson).
    - **Full Scope Exemption (e.g., a new subsidiary requesting a one-cycle deferral):** Must be reviewed by the CISO (Rachel Kim) and approved by the General Counsel (Maria Gonzalez) and the CCO jointly.
3.  All exceptions and approvals are permanently linked to the specific CRA cycle in LogicGate.

### 8.2 Escalation of Substantive Risk
The risk escalation process follows the standard incident management structure but is tied directly to thresholds found in this CRA.
- **Level 1:** Upon identification of a "Critical" Inherent Risk, the eGRC system immediately notifies the CCO and CISO. The CCO has 24 hours to brief the GC.
- **Level 2:** If a remediation plan for a "High" residual risk goes past due by 30 days, the issue is automatically escalated from the Risk Owner's queue to the CCO’s dashboard as a "Failing High-Risk Issue."
- **Level 3 (Crisis):** If a risk event materializes that is assessed as a "Major" or "Critical" Impact (e.g., an active data breach of PHI), the CRA process is paused, and the incident is managed via the **Critical Incident Response Policy (SOP-SEC-011)** . The CRA process will be used in the post-mortem phase to formally assess the new inherent risk landscape.

## 9. Training Requirements

### 9.1 Role-Based Training
All personnel involved in the CRA process must receive training appropriate to their role. Training is tracked via Workday.

**Table 9.1: CRA Training Matrix**
| Target Role(s) | Training Module | Frequency | Owner |
| :--- | :--- | :--- | :--- |
| All CRA RACI Participants (Risk Owners, Control Owners) | **LEGC-002-CRA Practitioner** — How to identify risks, the logic of the Inherent/Residual rubric, how to use LogicGate for documentation, and navigating the Unified Control Matrix. | Annually | CCO |
| Legal & Compliance GRC Team, CISO's GRC Team | **LEGC-002-CRA Advanced Operator** — Advanced LogicGate administration, control testing sampling methodology, QA process, and how to facilitate a scoping workshop. | Annually | CCO |
| General Counsel & Deputy GC | **LEGC-002-CRA Legal Interp** — Annual review of regulatory changes (HIPAA, AI Act, SR 11-7) and the legal rationale required for formal risk acceptance. | Annually | GC |
| All Meridian Employees (General Awareness) | **MHT-ALL-001 Annual Compliance & Ethics** (Module 3: "Your Role in Managing Risk") | Annually | CHRO |

### 9.2 New Role Onboarding
Any individual assigned to a RACI role in Section 3 for the first time must complete their assigned training module(s) within **30 days** of the assignment. They will have a read-only LogicGate account until training is complete.

## 10. Related Policies and References

The following Meridian SOPs and external standards are directly referenced in or are dependent upon this procedure.

### 10.1 Meridian Internal SOPs
| SOP ID | Title |
| :--- | :--- |
| SOP-GOV-001 | Corporate Governance and Board Risk Oversight |
| SOP-LEGC-001 | Code of Conduct and Ethics |
| SOP-LEGC-003 | Data Subject Rights Request (DSAR) Fulfillment |
| SOP-AI-001 | Clinical AI Product Lifecycle (from Conception to PMS) |
| SOP-AI-002 | Responsible AI (RAI) Governance and Bias Review |
| SOP-DATA-001 | Data Governance and Classification |
| SOP-DATA-002 | Data Lifecycle Management and Retention |
| SOP-DATA-004 | Model Risk Management (HealthPay Focused) |
| SOP-SEC-005 | Asset Management and CMDB Integrity |
| SOP-SEC-007 | Third-Party Security and Privacy Risk Management |
| SOP-SEC-010 | Information Security Incident Management |
| SOP-SEC-011 | Critical Incident Response and Crisis Communications |
| SOP-IT-001 | Logical Access and Identity Lifecycle Management |
| SOP-IT-005 | IT Change Management |
| SOP-ENG-003 | Secure Software Development Lifecycle (SDLC) |
| SOP-HR-001 | Employee Background Verification and Clearance |

### 10.2 External Standards and Guidance
- AICPA, *Description Criteria for a SOC 2 Examination using the Trust Services Criteria* (2022 Revision).
- OCC/Federal Reserve, *SR 11-7: Supervisory Guidance on Model Risk Management* (2011).
- Regulation (EU) 2024/1689 (Artificial Intelligence Act), specifically Title III, Chapter 2, Annexes III & IV.
- HIPAA Security and Privacy Rules (45 C.F.R. Parts 160, 162, and 164).
- ISO/IEC 27001:2013, Clause 6.1 (Actions to address risks and opportunities).
- HITRUST Common Security Framework (CSF v11).

## 11. Revision History

| Version | Effective Date | Last Reviewed | Author/Reviewer | Description of Changes |
| :--- | :--- | :--- | :--- | :--- |
| **1.0** | 2020-05-15 | 2020-05-15 | T. Anderson | Initial creation. Manual spreadsheet-based CRA process. Annual cadence. |
| **2.0** | 2021-09-01 | 2021-08-01 | T. Anderson, R. Kim | Full revision. Digitized the CRA into an eGRC prototype (Archer). Introduced Inherent/Residual methodology and semi-annual cadence. |
| **3.0** | 2022-11-01 | 2022-10-05 | T. Anderson, M. Gonzalez | Major update. Integration with new LogicGate eGRC platform. Added RACI for DPO role. Formalized SOC 2 Privacy TSC controls into the Unified Control Matrix. |
| **3.1** | 2023-07-12 | 2023-07-01 | T. Anderson | Minor revision. Updated Risk Appetite Statement to "Low" for all compliance domains to align with new Board directive. Added Section 7 KPI/KRI dashboards. |
| **4.0** | 2024-08-08 | 2025-06-23 | T. Anderson, M. Gonzalez | Comprehensive cycle review. Scope expanded to fully integrate the EU AI Act requirements for Clinical AI and new HITRUST v11 mapping. Updated controls in Section 5.4.2 for Cloud-Native architecture shifts. Major clarifications added to Model Risk (SR 11-7) and AI Transparency procedures. |