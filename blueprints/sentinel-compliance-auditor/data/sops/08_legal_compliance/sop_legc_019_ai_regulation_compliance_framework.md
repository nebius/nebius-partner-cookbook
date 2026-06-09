---
sop_id: "SOP-LEGC-019"
title: "AI Regulation Compliance Framework"
business_unit: "Legal & Compliance"
version: "3.6"
effective_date: "2025-04-26"
last_reviewed: "2026-09-13"
next_review: "2027-03-01"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
  - "SR 11-7"
status: "Active"
---

# Standard Operating Procedure: AI Regulation Compliance Framework

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide compliance framework for artificial intelligence (AI) and machine learning (ML) systems developed, deployed, or procured by Meridian Health Technologies, Inc. (“Meridian” or the “Company”). The purpose of this document is to operationalize Meridian’s commitment to responsible AI governance by defining standardized processes for regulatory mapping, compliance control implementation, evidence collection, and gap remediation across all business units and geographies in which Meridian operates.

This SOP translates voluntary framework adoption and mandatory regulatory obligations into auditable, repeatable procedures that ensure AI systems are developed and maintained in a manner consistent with applicable laws, regulatory guidance, and industry best practices for safety, fairness, transparency, and accountability.

### 1.2 Scope

This SOP applies to:

- **All AI/ML Systems:** Any system, model, algorithm, or application that utilizes machine learning, deep learning, natural language processing, computer vision, or related techniques to make predictions, recommendations, classifications, or decisions, or to generate content, that is used in connection with Meridian’s Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, or the Meridian SaaS Platform.
- **All Lifecycle Stages:** The full AI lifecycle, including problem formulation, data acquisition and preparation, model development and training, testing and validation, deployment, ongoing monitoring, and decommissioning.
- **All Personnel:** All full-time employees, contractors, consultants, and third-party vendors who design, develop, train, test, deploy, operate, monitor, or decommission AI systems on behalf of Meridian.
- **All Geographies:** Activities conducted in all Meridian offices, including Boston (HQ), London, Berlin, Singapore, and Toronto, and any cloud environments utilized (AWS us-east-1, eu-west-1; Azure DR).
- **Procured AI:** Third-party AI components, including foundation models, embeddings models, API-based AI services, and embedded AI features in vendor applications, that are integrated into Meridian’s product offerings or used in support of internal operations processing sensitive data.

This SOP is subsidiary to the Meridian AI Governance Charter and works in concert with the policies listed in Section 10 (Related Policies and References).

### 1.3 Out of Scope

The following are explicitly outside the scope of this SOP, though they may be addressed by other governance documents:

- Compliance assessments for non-AI software systems (see SOP-SDLC-002).
- General cybersecurity incident response procedures not specific to AI (see SOP-CISO-005).
- Employee performance evaluation criteria for personnel not directly involved in AI development.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|------|------------|
| **Accountable Executive** | The member of Meridian’s Executive Leadership Team with ultimate accountability for a specific AI system’s compliance posture. |
| **AI System** | A machine-based system that, for explicit or implicit objectives, infers from the input it receives how to generate outputs such as predictions, recommendations, or decisions that can influence physical or virtual environments. |
| **Conformity Assessment** | The process of demonstrating whether specified requirements relating to an AI system have been fulfilled. |
| **Data Drift** | A change in the statistical properties of the input data to a model over time. |
| **Explainability** | The degree to which an AI system's outputs can be understood in terms that are meaningful to a human stakeholder given the context of use. |
| **Human-in-the-Loop (HITL)** | A system design in which human operators are directly involved in the decision-making process of an AI system, with the capability to override or modify algorithmic outputs. |
| **Impact Assessment** | A structured evaluation of the potential positive and negative consequences of deploying an AI system in a specific context. |
| **Model Risk** | The potential for adverse consequences from decisions based on incorrect or misused model outputs. |
| **Model Drift** | Degradation of model predictive performance over time due to changes in the environment. |
| **Performance Threshold** | A pre-defined, quantitative metric boundary for a specific model metric (e.g., accuracy, F1 score, precision, recall) that triggers a review or intervention when breached. |
| **Responsible AI (RAI)** | Meridian’s internal program encompassing the principles of fairness, reliability & safety, privacy & security, inclusiveness, transparency, and accountability for all AI systems. |

### 2.2 Acronyms

| Acronym | Full Form |
|---------|-----------|
| **AI** | Artificial Intelligence |
| **AI RMF** | Artificial Intelligence Risk Management Framework |
| **CISO** | Chief Information Security Officer |
| **CCO** | Chief Compliance Officer |
| **CPO** | Chief Privacy Officer |
| **DPO** | Data Protection Officer |
| **DRR** | Decision Rationale Record |
| **GAP** | Governance, Accountability, and Procedures (Internal tool) |
| **GRC** | Governance, Risk, and Compliance |
| **HITL** | Human-in-the-Loop |
| **HOR** | Human Oversight Record |
| **KPI** | Key Performance Indicator |
| **ML** | Machine Learning |
| **RAI** | Responsible AI |
| **RAI-REG** | RAI Regulation Mapping Tool (Internal system) |
| **SOP** | Standard Operating Procedure |
| **SRM** | System Risk Matrix |
| **V&V** | Verification and Validation |

---

## 3. Roles and Responsibilities

The following matrix defines the RACI assignment for each major phase of the AI Compliance Framework lifecycle. Specific role titles are referenced below the matrix.

| Activity | Chief Compliance Officer | General Counsel | CPO / DPO | CISO | BU Head (e.g., VP Clin. AI) | CAIO | Model Owner | Internal Audit |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Regulatory Mapping** | A | C | R | C | C | R | I | I |
| **Impact Assessment** | A | C | R | C | C | R | I | I |
| **Control Implementation** | C | C | C | C | A | C | R | I |
| **V&V Testing** | C | I | I | C | A | R | R | I |
| **Deployment Approval** | R | A | R | R | C | R | C | I |
| **Ongoing Monitoring** | A | I | C | R | C | R | R | I |
| **Evidence Collection** | A | C | R | R | C | R | R | I |
| **Exception Approvals** | A | R | C | C | R | C | C | C |
| **Regulatory Reporting** | A | R | R | C | I | R | I | I |
| **Training Assignment** | R | A | R | R | C | R | C | I |

### 3.2.1 Chief Compliance Officer (CCO) — Thomas Anderson
The Accountable Executive for the overall AI Compliance Framework, including the maintenance of this SOP. Responsible for maintaining the centralized evidence repository and approving all compliance KPIs.

### 3.2.2 Chief AI Officer (CAIO)
Oversees all technical activities of the framework. Responsible for ensuring mapping, testing procedures, and monitoring metrics are technically sound and executed. Serves as the bridge between the Legal & Compliance and Engineering functions.

### 3.2.3 Model Owner
A specifically designated individual within the responsible Business Unit who owns the day-to-day execution of compliance tasks for a given model. This role is documented in the Model Inventory and is responsible for submitting evidence into the RAI-REG system.

### 3.2.4 AI Ethics Board
A cross-functional governance board that reviews all impact assessments prior to new AI system deployment. Chaired by the CAIO, with voting members from Legal, Compliance, Privacy, and the relevant Business Unit.

---

## 4. Policy Statements

Meridian Health Technologies is committed to the following high-level policy principles for the governance of all AI systems:

1.  **Proportional Governance:** The intensity of governance, documentation, and oversight applied to an AI system shall be proportional to the magnitude and scope of its potential impact on individuals, clinical outcomes, and financial standing, as determined by an approved system risk matrix.
2.  **Transparency and Explainability:** All AI systems deployed in production shall have a documented level of explainability appropriate for their designated domain of use. Stakeholders, including internal decision-makers and, where appropriate, end-users, shall be informed that they are interacting with or being evaluated by an AI system.
3.  **Human Oversight:** AI systems supporting clinical or financial decisions shall incorporate meaningful human oversight capabilities. No final irreversible clinical or credit decision shall be made entirely autonomously by an AI system without documented human-in-the-loop verification, consistent with regulatory standards for medical device software and financial services model risk management.
4.  **Robustness and Safety:** All AI systems shall undergo rigorous Verification & Validation (V&V) prior to deployment, including back-testing, stress-testing, and fairness evaluation. Systems shall be continuously monitored for data drift and model degradation against pre-defined performance thresholds.
5.  **Accountability:** A named Accountable Executive and Model Owner shall be documented for every AI system in production. These individuals are responsible for the system's lifecycle compliance.
6.  **Data Governance:** All data used for the training, validation, and operation of AI systems shall be governed in accordance with Meridian’s data governance policies, with particular regard to provenance, quality, privacy, and security.
7.  **Continuous Learning:** Meridian commits to using post-market monitoring data and incident learnings to inform an iterative cycle of model improvement and framework enhancement.

---

## 5. Detailed Procedures

This section outlines the step-by-step procedures for the AI Compliance Framework lifecycle, from initial system intake to ongoing monitoring and decommissioning.

### 5.1 AI System Inventory Intake

#### 5.1.1 Initiation
The Model Owner or proposing team shall initiate a new AI System Intake Request in the RAI-REG system (accessible via the Meridian intranet) whenever:
- A new internally developed AI/ML model is proposed for a use case involving Protected Health Information (PHI), financial data, or operational decisions.
- A third-party AI component is being procured for integration into a Meridian product.
- A significant architectural or retraining update is planned for an existing model.

#### 5.1.2 Intake Form Completion
The Model Owner must complete the AI System Intake Form (RAI-REG-F101), providing detailed information on:
- System name, version, and business unit.
- Intended purpose and domain context.
- Key performance indicators (KPIs) for effectiveness.
- Training data sources, provenance, and volume.
- Model architecture and primary algorithm type.

The completed Form F101 triggers an automated workflow in the RAI-REG system assigning a preliminary risk profile based on context.

### 5.2 Regulatory Obligations Mapping (NIST AI RMF Integration)

Upon intake completion, the Legal & Compliance team, in coordination with the CAIO, shall perform a comprehensive regulatory obligation mapping. This process is explicitly anchored to the NIST AI Risk Management Framework (AI RMF 1.0).

#### 5.2.1 AI RMF Core Mapping Procedure
The mapping procedure shall categorize obligations into the four core functions of the NIST AI RMF:

| AI RMF Function | Procedure Step | Responsible Role |
|-----------------|----------------|------------------|
| **GOVERN 1.0** | Map system activities to sub-categories GV-1.1 (Legal and regulatory requirements are understood and managed) through GV-5.1 (Organizational structures and policies are in place). Document the accountable executive and Model Owner per GV-1.2. | Legal & Compliance |
| **MAP 1.0** | Execute a context-based risk mapping. Determine the system's position in the Meridian System Risk Matrix (SRM). Identify potential benefits and harms relative to Map sub-categories (e.g., MP-1.1: Context is established). | Model Owner, Privacy |
| **MEASURE 1.0** | Quantify residual risks and controls. Establish the quantitative monitoring metrics for trustworthiness characteristics (e.g., accuracy, robustness, fairness) as required by Measure sub-categories (e.g., MS-1.2: Trustworthiness characteristics are defined). | CAIO, Model Owner |
| **MANAGE 1.0** | Allocate risk treatment resources and document monitoring cadence. Define incident response procedures specific to AI risks per Manage sub-categories (e.g., MN-2.3: AI risks are prioritized). | CCO, CISO |

#### 5.2.2 SR 11-7 Documentation Mapping (HealthPay Financial Services Specific)
For models within the HealthPay Financial Services business unit, a supplementary mapping against the Federal Reserve's Supervisory Letter SR 11-7 is required.

The Model Owner shall complete the "SR 11-7 Alignment Workbook" containing the following sections:
1.  **Model Design and Data:** Detailed architecture diagrams, training data composition, and feature engineering methodologies.
2.  **Model Testing:** Evidence of back-testing, benchmarking against challenger models, and sensitivity analysis.
3.  **Implementation:** Deployment pipeline logic and production run-time controls.
4.  **Documentation:** A complete compilation of all workbook sections into a searchable, archived document.
5.  **Ongoing Monitoring:** The Model Owner must document the monitoring strategy, including which statistical tests and model quality metrics will be tracked. A dashboard shall be created in the central model monitoring system (currently AWS SageMaker Model Monitor) to track these metrics.

### 5.3 Control Implementation and Evidence Collection

Upon completion of the regulatory mapping, the Model Owner is responsible for implementing the assigned controls, guided by the automated workplan generated in RAI-REG. Evidence shall be collected in a tamper-proof format.

#### 5.3.1 NIST AI RMF Control Implementation
The following controls, mapped directly to the NIST AI RMF, shall be implemented with the noted evidence and SLAs:

| NIST AI RMF Sub-Category | Required Control | Objective Evidence | Completion SLA (from mapping date) |
|--------------------------|-----------------|--------------------|------------------------------------|
| **GV-3.2: AI use cases are inventoried** | System registered in RAI-REG with unique ID. | RAI-REG Inventory Entry Screenshot | 3 business days |
| **MP-2.1: Risks are mapped** | Completeness check of risk mapping. | Signed System Risk Matrix (SRM) form | 5 business days |
| **MP-3.2: Benefits and harms are assessed** | Completion of a structured stakeholder analysis workshop. | Workshop minutes, signed-off Impact Analysis Report | 15 business days |
| **MS-1.2: Trustworthiness metrics are defined** | Quantitative thresholds for fairness (e.g., disparate impact ratio < 0.85), robustness (e.g., PSI < 0.25), and explainability (e.g., SHAP summary plot reviewed by domain expert) defined in the V&V Plan. | Approved V&V Plan document | Pre-deployment |
| **MS-2.1: Measurement for trustworthiness** | Execute V&V Plan and document results. | Completed V&V Test Report with pass/fail against thresholds | Pre-deployment |
| **MN-3.1: Incidents are managed** | Integration of model-specific failure modes into the incident response plan. | Updated Incident Response Plan document | Pre-deployment |

#### 5.3.2 Evidence Collection Hub
All objective evidence shall be stored in the RAI-REG Evidence Hub, an immutable, audited repository backed by AWS S3 with strict versioning enabled. Evidence must be tagged with the relevant SOP-ID, NIST AI RMF sub-category ID, and the AI System ID within 24 hours of generation.

### 5.4 Conformity and Impact Verification

Prior to any new model deployment or major update, the CCO (or delegate) shall facilitate a pre-deployment review, known as the AI System Conformity Review (ASCR).

#### 5.4.1 ASCR Procedure
The ASCR checklist includes:
- [ ] RAI-REG Intake Form complete and risk tier approved.
- [ ] All mandatory NIST AI RMF Map and Measure controls have objective evidence verified.
- [ ] SR 11-7 Workbook (if applicable) is complete and reviewed by the Head of Model Risk.
- [ ] V&V Test Report has been reviewed and approved by the AI Ethics Board.
- [ ] Post-deployment monitoring dashboard is active and shows healthy telemetry.
- [ ] Human Oversight training for relevant operational staff is complete.

The CCO, General Counsel, and CAIO must provide joint approval via digital signature in RAI-REG before the deployment ticket can be actioned by Engineering. The SLA for the ASCR review is 5 business days from submission of the final evidence package.

---

## 6. Controls and Safeguards

This section defines the portfolio of technical and administrative controls embedded within the AI lifecycle.

### 6.1 Administrative Controls

| Control ID | Control Description | Control Objective | Monitoring Frequency | Owner |
|------------|---------------------|-------------------|---------------------|-------|
| **AC-AI-01** | AI Ethics Board Charter | Establishes a cross-functional body to review and provide advisory opinions on high-impact AI systems consistent with NIST AI RMF function GOVERN. | Annual Review | CAIO |
| **AC-AI-02** | AI System Inventory | Maintain a complete, living inventory of all AI systems in operation, including their associated risk tiers, owners, and data sources. | Monthly Audit | CCO |
| **AC-AI-03** | Vendor AI Assurance | All procurement contracts for AI services must include a right-to-audit clause for security and fairness controls. | Per Contract Cycle | CPO, Procurement |
| **AC-AI-04** | Model Decommissioning | Establish formal procedure for the safe withdrawal of an AI model from production, including archival of documentation, termination of monitoring, and notification to stakeholders. | Event-Driven | Model Owner |

### 6.2 Technical Controls

| Control ID | Control Description | Implementation Mechanism | Applicability |
|------------|---------------------|--------------------------|---------------|
| **TC-AI-01** | Explainability Dashboard | All models impacting individuals must log inference context to the RAI-REG dashboard, allowing for retrospective analysis of feature importance using SHAP or LIME. | Clinical AI, HealthPay |
| **TC-AI-02** | Adversarial Robustness Filter | Input validation layers are required to detect and log potentially adversarial inputs or data poisoning attempts before they reach the inference engine. | All Production AI |
| **TC-AI-03** | Data Quality Gate | Automated pipeline checks for missingness, schema drift, and out-of-range values must be passed before data is ingested for model retraining. | All ML Pipelines |
| **TC-AI-04** | Immutable Logging | All predictions, decisions, and human overrides must be written to an immutable, append-only log for compliance traceability per GV-2.2. | Clinical AI, HealthPay |
| **TC-AI-05** | Bias Detection Suite | Integration of the AWS SageMaker Clarify module into the CI/CD pipeline to gate deployments that exceed pre-defined fairness thresholds (e.g., Disparate Impact Ratio outside 0.80 - 1.25). | Financial, Operational AI |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Ongoing Monitoring

Post-deployment, the Model Owner is responsible for continuous monitoring of model performance and drift. For all models, monitoring must be established under the framework defined in the V&V Plan and SR 11-7 Alignment Workbook.

### 7.2 Key Performance Indicators (KPIs)

The following KPIs shall be tracked on the Company’s centralized AI Compliance Dashboard (built on Tableau), overseen by the CCO:

| KPI ID | KPI Title | Measurement Metric | Target | Reporting Cadence |
|--------|-----------|--------------------|--------|-------------------|
| **KPI-01** | Inventory Compliance | (Number of AI systems with complete RAI-REG profiles / Total number of active AI systems) * 100 | 100% | Monthly |
| **KPI-02** | Control Attestation Lateness | Average days past the SLA completion date for mandatory control evidence | < 5 days | Monthly |
| **KPI-03** | ASCR Cycle Time | Median time from ASCR submission to joint approval decision | < 10 business days | Quarterly |
| **KPI-04** | Model Drift Alert Rate | Number of models breaching drift thresholds (PSI > 0.25 or KS statistic > 0.125) in a given month | < 15% of active models | Monthly |
| **KPI-05** | Open High-Risk Exception Count | Number of active exceptions for high-risk tier models that are past their remediation date | 0 | Weekly (internal), Monthly (Board) |
| **KPI-06** | Training Compliance Rate | (Number of active AI personnel who have completed required annual RA training / Total active AI personnel) * 100 | 100% | Quarterly |

### 7.3 Reporting Cadence

- **Weekly Operations Report:** The CCO’s office shall review a "Red-Amber-Green" status report for all high-risk AI systems, focusing on open exceptions (Section 8) and model drift alerts.
- **Monthly Management Report:** A consolidated KPI report is distributed to the Executive Leadership Team, detailing overall framework health and any systemic gaps identified.
- **Quarterly Business Review (QBR):** A formal, written review of the AI Compliance Framework is presented to the Audit Committee of the Board of Directors. The QBR includes a deep dive on a specific framework component (e.g., deep dive on MAP function performance), open internal audit findings, and the forward annual work plan.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling Procedure

Specific circumstances may temporarily prevent full compliance with a procedural or technical control defined in this SOP. Where a control cannot be met by its SLA, a formal exception must be requested.

**Process:**
1.  **Identification:** The Model Owner or CAIO identifies the specific control (e.g., TC-AI-05 Bias Detection Suite execution) that cannot be met for a specific model by the required date.
2.  **Documentation:** The requester completes an AI Compliance Exception Form (RAI-REG-F103) in the RAI-REG system. The form must document:
    - The specific control requiring an exception.
    - The objective reason for the non-compliance.
    - A detailed compensatory control to be put in place.
    - A specific remediation plan with a date (not to exceed 90 days from the approval date).
3.  **Approval Workflow:** RAI-REG automatically routes the exception based on risk tier:
    - **Low & Medium Risk Models:** Approval by the CAIO.
    - **High Risk Models:** Approval by the CAIO and the Chief Compliance Officer.
    - **Critical Risk Models:** Approval by the AI Ethics Board (full voting quorum required, with signature from the General Counsel).
4.  **Tracking and Closure:** All approved exceptions are visible on the KPI dashboard as "Open, On-Time" or "Open, Past-Due." The Model Owner must upload evidence of remediation by the committed date. Past-due exceptions are automatically escalated to the relevant Business Unit Head and the CCO.

### 8.2 Incident Escalation Matrix

For AI-related incidents involving potential patient or consumer harm, a biased decision leading to regulatory scrutiny, or a significant operational outage, the following matrix applies:

| Severity Level | Definition | Notification Timeline | Escalation Path |
|----------------|------------|-----------------------|-----------------|
| **L1 - Critical** | Active harm, regulatory notification triggered, or critical clinical system outage. | Immediate (within 30 min) | CISO -> CCO -> General Counsel -> CEO |
| **L2 - Major** | Significant bias event, model failure affecting >100 transactions, data breach. | Within 2 hours | CISO -> CCO -> BU Head |
| **L3 - Minor** | Isolated erroneous prediction, non-critical model outage, drift alert. | Within 24 hours | Model Owner -> CAIO |

---

## 9. Training Requirements

### 9.1 Training Curriculum

Meridian maintains a tiered training curriculum to ensure all personnel understand their duties under this SOP and the broader AI Governance Charter.

**Level 1: AI Compliance Fundamentals (Mandatory for ALL personnel within scope)**
- **Topics:** Meridian's AI Principles, roles defined in this SOP, introduction to the RAI-REG tool, methods for reporting an AI incident or concern, regulatory landscape overview.
- **Format:** 45-minute asynchronous e-learning module on Workday Learning.
- **Frequency:** Annually. Must be completed within 30 days of hire for new employees.

**Level 2: AI Development Lifecycle Compliance (Mandatory for all Model Owners, Data Scientists, ML Engineers, and CAIO team)**
- **Topics:** Deep-dive into SOP-LEGC-019 procedures, NIST AI RMF Core application, V&V planning and execution, evidence collection in RAI-REG, SR 11-7 documentation responsibilities (where applicable).
- **Format:** 4-hour instructor-led workshop (in-person or synchronous virtual), with a required practical assessment.
- **Frequency:** Annually.

**Level 3: Executive AI Oversight (Mandatory for all Executive Leadership Team members and AI Ethics Board members)**
- **Topics:** Strategic AI risk management, governance model evolution, Board-level reporting requirements, high-profile industry case studies.
- **Format:** 2-hour executive briefing, delivered semi-annually by external counsel and the CAIO.
- **Frequency:** Every 6 months.

Training completion is tracked in Workday Learning and automatically fed into the KPI dashboard via an API. The CCO is responsible for reporting on quarterly training compliance rates (KPI-06) and enforcing a 15-day grace period for overdue training before formal notification to the non-compliant employee's manager.

---

## 10. Related Policies and References

### 10.1 Internal Policies

| Document ID | Document Title | Relationship to this SOP |
|-------------|----------------|--------------------------|
| SOP-GOV-001 | Meridian AI Governance Charter | Foundational governance document |
| SOP-CISO-005 | AI Security Incident Response Protocol | Defines technical response steps for AI incidents referenced in Section 8.2 |
| SOP-PRIV-012 | Data Protection Impact Assessment (DPIA) Procedure | Required input for AI impact assessments |
| SOP-SDLC-002 | Secure Software Development Lifecycle Policy | Governs non-AI development and serves as the basis for DevSecOps pipeline controls |
| SOP-MDR-025 | Medical Device Software Maintenance | Governs post-market surveillance for Clinical AI regulated as MDSW |
| SOP-MRMS-011 | Model Risk Management Standards (SR 11-7) | Detailed technical standards for financial model documentation and monitoring |
| SOP-VEND-004 | Third-Party AI Procurement & Vendor Risk Assessment | Required procedure for procured AI, referenced in Section 5.1.1 |

### 10.2 External Standards and Regulations

| Standard/Regulation | Reference Point |
|---------------------|-----------------|
| NIST AI RMF 1.0 | Framework Architecture and Core Functions |
| Federal Reserve SR 11-7 / OCC 2011-12 | Supervisory Guidance on Model Risk Management |
| NIST SP 800-53 Rev. 5 | Security and Privacy Controls for Information Systems |
| HIPAA Security Rule | Technical safeguards for protected health information |

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
|---------|----------------|-----------|--------------------|
| 1.0 | 2023-01-15 | Thomas Anderson | Initial publication establishing foundational AI governance and SR 11-7 alignment. |
| 2.0 | 2023-08-01 | Thomas Anderson, Rachel Kim | Major revision: Integrated NIST AI RMF 1.0 core functions into mapping and control procedures. Added detailed HITL logging requirements. |
| 3.2 | 2024-03-10 | Thomas Anderson, Dr. Klaus Weber | Updated scope to include Generative AI and procured third-party foundational models. Expanded roles matrix to include CAIO. Introduced AI Ethics Board governance. |
| 3.5 | 2025-01-20 | Thomas Anderson, Maria Gonzalez | Comprehensive annual review. Updated KPI thresholds and streamlined evidence collection SLAs based on operational data. Added L3 severity to incident matrix. |
| 3.6 | 2025-04-26 | Thomas Anderson, Maria Gonzalez, Dr. Klaus Weber | Full review and update for alignment with the EU Artificial Intelligence Act. Incorporated expanded impact assessment procedures, revised regulatory mapping, and added new technical controls for high-risk systems. Expanded definitions lexicon. |