---
sop_id: "SOP-CLIN-016"
title: "Clinical Validation Study Design"
business_unit: "Clinical AI Products"
version: "1.4"
effective_date: "2025-04-28"
last_reviewed: "2026-09-23"
next_review: "2027-03-27"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Clinical Validation Study Design

## 1. Purpose and Scope

This Standard Operating Procedure (SOP) establishes the mandatory framework and methodology for the design, execution, and reporting of all clinical validation studies for AI-powered clinical decision support tools, diagnostic imaging analysis software, patient risk scoring algorithms, and adverse event prediction systems developed and deployed by Meridian Health Technologies, Inc. (hereinafter "Meridian" or "the Company").

The purpose of this SOP is to ensure that every clinical validation study produces scientifically robust, statistically sound, and regulatorily sufficient evidence of safety, efficacy, and clinical utility. This evidence base supports internal decision-making, regulatory submissions, customer assurance, and ongoing post-market surveillance activities.

**Scope of Applicability:** This SOP applies to all employees, contractors, and third-party partners involved in the design, approval, execution, analysis, or reporting of clinical validation studies for the Clinical AI Platform. Specifically, it covers:

- All algorithmic models classified as "high-risk" under the Meridian AI Risk Classification Framework (SOP-AI-001), which includes all CE-marked and FDA-cleared diagnostic and prognostic models.
- Retrospective, prospective, and in-silico validation studies.
- Studies conducted using Meridian-hosted data, partner healthcare provider data, or public benchmark datasets.
- Studies intended for regulatory submission to the U.S. Food and Drug Administration (FDA), European Union Notified Bodies under the Medical Device Regulation (MDR), or other competent authorities.
- Studies used to support marketing claims, peer-reviewed publications, or customer-facing collateral.

**Out of Scope:** This SOP does not govern early-stage exploratory research (Technology Readiness Level 1-3), algorithm training methodologies, or purely technical performance benchmarking (e.g., inference latency, which is covered under SOP-ENG-042). Financial model validation under SR 11-7 for the HealthPay Financial Services business unit is covered under SOP-FIN-022.

This SOP has been reviewed by the AI Governance Committee, Legal, Compliance, and the Chief Medical Officer. Non-compliance with this SOP may result in regulatory action, withdrawal of product certifications, and disciplinary action up to and including termination of employment.

## 2. Definitions and Acronyms

For the purposes of this document, the following definitions and acronyms apply:

| Term / Acronym | Definition |
| :--- | :--- |
| **AE** | Adverse Event. An untoward medical occurrence associated with the use of a medical device, including AI-based software. |
| **AUC-ROC** | Area Under the Receiver Operating Characteristic Curve. A primary metric for discriminatory performance. |
| **Bias Assessment** | A quantitative and qualitative evaluation of algorithmic fairness across pre-defined protected attributes and clinically relevant subpopulations. |
| **CI** | Confidence Interval. |
| **CRO** | Contract Research Organization. A third-party entity engaged to execute study activities. |
| **eCRF** | Electronic Case Report Form. The digital instrument for data collection. |
| **Endpoint** | The precisely defined quantitative or qualitative measurement used to determine study outcomes. |
| **EU AI Act** | Regulation (EU) 2024/1689 laying down harmonized rules on artificial intelligence. |
| **IDEAL Framework** | The Idea, Development, Exploration, Assessment, Long-term follow-up framework for evaluating surgical and medical device innovations, adapted for AI (IDEAL-AI). |
| **IRB/EC** | Institutional Review Board / Ethics Committee. |
| **MDR** | Medical Device Regulation (EU) 2017/745. |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework 1.0. |
| **PHI** | Protected Health Information. |
| **PPV / NPV** | Positive Predictive Value / Negative Predictive Value. |
| **Pre-specification** | The practice of documenting all study design elements, endpoints, statistical tests, and sub-group analyses prior to accessing or analyzing any study data. |
| **SAP** | Statistical Analysis Plan. The detailed technical document that describes the statistical methods to be used for the analysis of study data. |
| **SAE** | Serious Adverse Event. |
| **SOP** | Standard Operating Procedure. |
| **T&E** | Transparency and Explainability. A core requirement under the EU AI Act and a principle of the NIST AI RMF. |

**Reference Definitions (from Regulation and Standards):**

- **Clinical Validation (per MDR Annex I, Section 15.1.2):** The process of establishing that the device, when used in the intended patient population and by the intended users, yields the specified clinical outcomes with the required clinical performance and safety.
- **Model Drift (per NIST AI RMF: Map 1.6):** A change in model behavior over time due to changes in the input data distribution, the relationship between inputs and outputs, or external application context.

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for all clinical validation studies.

**R:** Responsible (executes the task) | **A:** Accountable (approves the task) | **C:** Consulted (provides input) | **I:** Informed (receives status updates)

| Activity / Task | Clinical AI Lead (Sponsor) | Biostats & Data Science | Clinical Ops & Site Mgmt | Regulatory Affairs | Chief Medical Officer | CISO & Privacy | Quality Assurance |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Study Concept & Feasibility** | A/R | C | C | C | I | I | I |
| **Drafting Study Protocol** | A | R | C | C | C | C | C |
| **Statistical Analysis Plan (SAP)** | C | A/R | I | C | I | I | C |
| **IRB/EC Submission & Approval** | I | I | A/R | C | I | C | I |
| **Data Extraction & De-identification** | I | C | R | I | I | A/R | C |
| **Study Execution & Monitoring** | R | C | A | I | I | I | C |
| **Final Analysis & Reporting** | C | A/R | C | C | I | I | C |
| **Regulatory Submission Package** | C | C | I | A/R | C | I | C |
| **Go/No-Go Publication Decision** | C | C | C | C | A/R | I | C |

**Specific Role Responsibilities:**

- **VP of Clinical AI Products (Dr. Aisha Okafor):** Serves as the Executive Sponsor for all validation studies. Owns the strategic alignment of studies with product roadmaps and the overall SOP.
- **Clinical AI Lead (Study Sponsor):** A designated physician or clinical scientist responsible for the scientific integrity of a specific study. Approves the protocol and final study report.
- **VP of Engineering (David Park):** Accountable for ensuring the technical team provides a frozen, production-identical version of the model for retrospective validation. No changes to the model architecture or weights are permitted once the validation dataset is locked.
- **Chief Medical Officer (Dr. Priya Patel):** Provides final medical sign-off on all study protocols and final reports intended for regulatory submission or high-stakes external publication.
- **Chief Privacy Officer / DPO (Dr. Klaus Weber):** Reviews all data flows for GDPR and HIPAA compliance. Responsible for the Data Protection Impact Assessment (DPIA) template approval, as referenced in SOP-PRI-009.
- **Quality Assurance (QA):** An independent team within the Compliance department. Audits study documentation against this SOP and Good Clinical Practice (GCP) principles. Maintains the repository of approved exceptions.

## 4. Policy Statements

Meridian Health Technologies is committed to generating clinical evidence that meets the highest standards of scientific rigor, ethical conduct, and regulatory compliance. The following high-level policies govern all clinical validation activities:

1.  **Pre-registration and Pre-specification Mandate:** All confirmatory clinical validation studies (Phase 3 within the IDEAL-AI framework) intended for regulatory submission or pivotal marketing claims must be pre-registered on a publicly accessible registry (e.g., ClinicalTrials.gov, the ISRCTN registry) prior to first patient data access. The protocol, SAP, and primary/secondary endpoints must be time-stamped and locked in a version-controlled, audit-trailed system of record (Meridian's Veeva Vault eTMF) before analysis.
2.  **Patient-Centric and Ethical Design:** All studies must prioritize patient safety and welfare. Study designs must minimize patient burden where feasible, such as utilizing existing de-identified data sources for retrospective foundational studies. Informed consent waivers must be approved by an IRB/EC and Dr. Weber's office.
3.  **Population Representativeness:** Study cohorts must reflect the intended use population. Protocols must include a mandatory "Population Description" section that explicitly compares study demographics to the target indication epidemiology, identifying and justifying any under-representation.
4.  **Independent Validation:** For all high-risk models, a final locked validation dataset, unseen during model development, must be maintained with a strict technical and procedural "firewall" between the model development team and the team executing the validation analysis. The validation analysis code must itself be independently reviewed.
5.  **Transparency and Explainability (T&E):** The final study report must include a chapter on model behavior, detailing subgroup performance, known failure modes, and the output of the appropriate explainability method (e.g., SHAP, LIME, Grad-CAM, attention maps) as defined in the study-specific T&E Plan.
6.  **Quality Management System:** All documentation artifacts generated under this SOP, including protocols, deviations, and final reports, shall be retained within Meridian's Quality Management System (QMS) according to the records retention schedule. The validation process itself serves as evidence of conformity with the quality management principles referenced in SOP-QA-001.

## 5. Detailed Procedures

This section outlines the end-to-end workflow for a clinical validation study, from initial concept to final archival. Each sub-section corresponds to a critical stage gate in the process.

### 5.1 Study Concept and Feasibility Assessment (Stage Gate 0)

The process begins with a Study Concept Document (SCD), using the MER-CLIN-016-F01 template, drafted by the Clinical AI Lead. The SCD is a lightweight but essential proposal that must address:

- **Clinical Question (PICOTS format):** Population, Intervention, Comparator, Outcome, Timing, Setting.
- **Business and Regulatory Rationale:** Why is this study necessary? E.g., "To support a Class III 510(k) submission for a new pulmonary embolism (PE) detection algorithm on CT angiograms."
- **Proposed IDEAL Phase:** (Phase 1: In silico, Phase 2b: Early Clinical, Phase 3: Confirmatory).
- **Initial Feasibility Query:** A formal query ticket (MER-DATA-001) to the Clinical Data Operations team to estimate available cohort volume against preliminary inclusion/exclusion criteria. Data Operations commits to a 10-business-day SLA for a feasibility count response.
- **Competitor Landscape** (brief summary).

The SCD is reviewed at a bi-weekly Portfolio Prioritization Committee (chaired by the VP of Clinical AI Products). At this stage, the concept is approved, rejected, or placed on hold based on strategic fit and resource capacity.

### 5.2 Protocol Development and Finalization

Upon approval of the SCD, the Biostatistics and Data Science team leads the authoring of the full Study Protocol.

**5.2.1 Study Protocol Sections (MER-CLIN-016-F02):**
The protocol is a comprehensive document and must contain the following sections as a minimum:

1.  **Title Page and Administrative Signatures:** VP of Clinical AI, Biostats Lead, CMO, Data Privacy Office.
2.  **Synopsis:** A structured, one-page summary.
3.  **Introduction and Scientific Background:** Literature review, preliminary Meridian data.
4.  **Study Objectives, Endpoints:**
    - **Primary Endpoint:** Must be singular, clinically meaningful, and pre-specified. E.g., "Sensitivity of the PE Detection Algorithm for detecting central pulmonary emboli, as adjudicated by an independent panel of three thoracic radiologists using the consensus standard of truth, with a non-inferiority margin of -5% compared to standard-of-care multi-detector CT interpretation."
    - **Secondary Endpoints:** (Limit to 3-5). E.g., Specificity, False Positive Rate, time-to-diagnosis, AUC-ROC.
    - **Exploratory Endpoints:** E.g., Subgroup analysis by BMI, presence of motion artifacts.
5.  **Study Design and Methodology:**
    - Description of design (Retrospective cohort, Prospective observational, etc.).
    - A detailed T&E Plan subsection, specifying the explainability method, how it will be evaluated, and the clinical user interface for displaying transparent outputs.
6.  **Study Population:**
    - **Inclusion/Exclusion Criteria:** Explicit ICD-10/SNOMED CT codes or natural language definitions if using unstructured data.
    - **Ethical Considerations:** Informed consent plan, IRB submission strategy.
7.  **Model and Comparator:**
    - Frozen model version ID (from MLflow/Git commit hash).
    - Hardware specification (CPU/GPU, memory) for inference.
    - Comparator definition (standard of care, other AI models, human readers).
8.  **Data Collection and Management:**
    - Data sources, linkage methodology, eCRF design.
    - De-identification procedure per SOP-PRI-009.
9.  **Statistical Analysis Plan (SAP) Outline:** A high-level summary of the planned analysis. The full, detailed SAP is a separate, time-stamped-controlled document (MER-CLIN-016-F04).
10. **Safety and Adverse Event Reporting:** Plan for soliciting and unsolicited AE monitoring.
11. **Study Governance and Committees:** E.g., Independent Data Monitoring Committee (IDMC) if applicable.
12. **Timeline and Budget.**

**5.2.2 Protocol Review and Lock:**
The complete draft protocol undergoes a formal review. The Biostats Lead circulates the protocol via Veeva Vault to the RACI-defined "Responsible" and "Consulted" roles with a mandatory 10-business-day review period. All comments must be logged as dispositioned Veeva comments. Once all comments are resolved, the document is versioned as "v1.0 (LOCKED — FOR STUDY EXECUTION)" and digitally signed by the Approvers (CMO, Clinical AI Lead, Biostats Lead). A Veeva workflow automatically generates a read-only PDF and restricts further editing.

### 5.3 Sample Size Justification and Power Analysis

A formal power analysis is mandatory for all confirmatory studies. This analysis must be a prominent section within the SAP.

- **Methodology:** The Biostatistics team will use the `MeridianPower.jl` library (a validated internal Julia package) or equivalent validated software (e.g., SAS PROC POWER, PASS). R scripts are permitted but must be code-reviewed by a second biostatistician not involved in the script's authorship.
- **Parameters:** The analysis must clearly state all parameters: Significance level (alpha, typically 0.05 one-sided or two-sided), Target Power (not lower than 0.80, typically 0.90), Effect Size (e.g., superiority margin, non-inferiority margin), Expected Outcome Variance.
- **Justification for Effect Size:** The chosen effect size must be clinically justified. For non-inferiority studies, this is intrinsically linked to the performance of the comparator and what constitutes a clinically acceptable degradation.
- **Attrition and Missing Data:** The sample size must be inflated by a pre-specified attrition rate (e.g., 15%) to account for missing or corrupted data.

**Example:** For a non-inferiority study evaluating sensitivity, the hypothesis is:
H0: Sensitivity_AI - Sensitivity_SoC <= -NI_margin
H1: Sensitivity_AI - Sensitivity_SoC > -NI_margin
If SoC sensitivity is 95% and we set an NI margin of -5%, with 90% power and one-sided alpha of 0.025, the required sample size is calculated and documented.

### 5.4 Data Management, Governance, and Lock

A detailed Data Management Plan (DMP) (MER-CLIN-016-F03) is authored by Clinical Data Operations, referencing all data sources.

**5.4.1 Data Access and De-identification:**
The IT Data Services team executes a standard data request (MER-IT-101), extracting raw data from the Meridian Clinical Data Lake (AWS S3-based, queried via AWS Athena). Per SOP-PRI-009, all direct and indirect identifiers must be stripped. The de-identified dataset is then placed in a dedicated, project-specific, access-controlled "Study Staging" bucket.

**5.4.2 Dataset Lock and Model Freeze:**
A critical control point. The "Validation Dataset" is a specific subset of data entirely unseen during model development and tuning.
1.  **Biostats:** Defines the inclusion/exclusion coding queries.
2.  **Data Ops:** Queries the Staging bucket to create the final analytical cohort (final row count).
3.  **Engineering (Dr. Jane Smith's team):** Freezes the model code and trained weights into a containerized, version-tagged image and deploys it as a locked inference API endpoint. The endpoint is configured with full logging of every inference request and response.
4.  **Joint Lock Sign-off:** A meeting between Biostats Lead, Data Ops Lead, and VP of Engineering. They verbally confirm and digitally sign an attestation in Veeva Vault: "The Validation Dataset (N=[row count]) and the Model Version [ID] are now locked. No further exclusions, data manipulation, or model code changes are permitted prior to the primary, unblinded analysis."

### 5.5 Statistical Analysis Plan (SAP) Execution

Following dataset lock, the Biostatistics team executes the SAP.

**5.5.1 Interim Analysis Plan:**
If an interim analysis is specified in the protocol (for prospective studies with an IDMC), this is executed by an independent, unblinded statistician. No other member of the study team may access unblinded data. The IDMC makes a formal recommendation to the Study Sponsor (continue, pause, or stop).

**5.5.2 Final Analysis Workflow:**
1.  **Analysis Code Execution:** The primary analysis script (in R, Python, or Julia) is executed in a locked, version-controlled compute environment (Meridian's Posit Workbench instance).
2.  **Bias and Fairness Assessment (Ref: NIST AI RMF Map 1.6):** This is a non-negotiable sub-analysis. Model performance metrics (sensitivity, specificity, PPV) are computed and reported for pre-defined subpopulations. These subpopulations are identified based on protected attributes (where permissible and lawful to analyze) and clinically relevant characteristics (e.g., age decile, sex, race/ethnicity, comorbidity status, scanner manufacturer). Any subpopulation with a metric point estimate difference >10% from the reference population, or with a statistically significant difference (p<0.05), must be highlighted in the report as a critical fairness finding.
3.  **Output Generation:** A standard set of publication-ready tables and figures is generated using a corporate-branded reporting library (`MeridianReports.jl`), output to PDF and interactive HTML dashboards.

### 5.6 Study Report, Archiving, and Dissemination

The Biostats and Clinical AI Lead co-author the Clinical Study Report (CSR), using the approved CSR template (MER-CLIN-016-F05).

**CSR Core Sections:**
- Abstract and Executive Summary.
- Detailed Demographics and Baseline Characteristics Table.
- Primary Endpoint Analysis: Includes pre-specified analysis, supporting exploratory analyses, forest plots for subgroup analyses.
- Safety Reporting: Full listing and summary of AEs/SAEs.
- Model Performance and Behavior Chapter: Includes T&E results, failure mode analysis (e.g., heatmaps of true positives, false positives, false negatives), and the bias/fairness assessment report.
- Conclusions: A clear statement of whether the study met its primary endpoint and the model's suitability for its intended use.

**Archival:** The final, signed CSR is uploaded to Veeva Vault eTMF as a final archival record. The locked dataset, analysis scripts, and model inference endpoint are archived for a minimum of 15 years in Meridian's AWS Glacier Deep Archive, governed by SOP-IT-003 (Data Retention).

## 6. Controls and Safeguards

The following technical and administrative controls are implemented to enforce the policies of this SOP.

### 6.1 Technical Controls
| Control ID | Control Description | Implementation System | Metric / Evidence |
| :--- | :--- | :--- | :--- |
| **TC-01** | **Model Version Freeze:** Once a study is initiated, the model artifact is tagged with an immutable version, and its checksum is recorded in the protocol. The artifact is placed in a read-only storage bucket with a bucket policy that denies any `PutObject` or `DeleteObject` action. | AWS S3 with Object Lock (Governance mode), SageMaker Model Registry | Timestamp and checksum of model `tar.gz` artifact, IAM policy log showing no privileged `s3:PutObject` actions during study window. |
| **TC-02** | **Data Firewall:** Access to the locked validation dataset is managed via a dedicated IAM role. This IAM role is denied access to all development/training data buckets. The role is only assumed by the Biostats team during the formal analysis phase. | AWS IAM, S3 Bucket Policy | Quarterly IAM access advisor reports reviewed by the Data Privacy Office. Audit trail logs of all data access. |
| **TC-03** | **Reproducible Compute Environment:** The SAP is executed within a Docker container image that is itself versioned and stored in a private Amazon ECR repository. This container includes specific versions of all scientific computing libraries. | AWS ECS/AWS Batch running on Meridian's private EC2 cluster. | Container image SHA256 hash recorded in the final CSR. |
| **TC-04** | **Audit Trail Integrity:** All digital signatures, workflow transitions, and document access within the electronic Trial Master File (eTMF) are logged to an append-only audit trail. | Veeva Vault eTMF | Monthly audit trail reports reviewed by QA, specifically looking for any SOX-type conflicts (e.g., same person locking protocol and approving final report for confirmatory studies). |

### 6.2 Administrative Controls
- **Change Control for Locked Artifacts:** Any deviation after the joint lock sign-off triggers the formal exception process (Section 8). A minor change (e.g., clarifying data extraction logic that doesn't change the cohort) requires QA and Clinical AI Lead approval. A major change (e.g., adding a new endpoint, changing the model) requires CMO approval and may require protocol re-finalization.
- **Independent Biostatistics Review:** For all pivotal confirmatory studies, the SAP and final analysis code are reviewed by a biostatistician from the QA department who is independent of the Clinical AI product team.
- **Supplier Management:** If a CRO is engaged to execute portions of this SOP, a Meridian Clinical AI Lead retains accountability. The CRO's QMS must be audited by Meridian QA against this SOP prior to contract start and annually thereafter. All CRO data access is managed through dedicated, time-bound IAM roles.

## 7. Monitoring, Metrics, and Reporting

The effectiveness of this SOP is continuously monitored through a set of Key Performance Indicators (KPIs). These metrics are not merely observed but acted upon through a formal governance cadence.

### 7.1 Key Performance Indicators (KPIs)

| KPI # | Metric | Target | Measurement Methodology | Data Source |
| :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | **SOP Compliance Rate** | 100% per study | % of studies where the final, signed protocol and all key artifacts (Dataset Lock Sign-off, CSR) are present and correctly versioned in Veeva prior to release of results. | Veeva Vault eTMF, QA Audit Reports |
| **KPI-02** | **Pre-registration Timeliness** | >95% on time | % of confirmatory studies registered on ClinicalTrials.gov BEFORE the first data extraction query is run against the production data lake. | ClinicalTrials.gov timestamp vs. AWS Athena access log timestamp. |
| **KPI-03** | **Primary Endpoint Pre-specification Adherence** | 100% adherence | Qualitative audit. All reported primary endpoints in the final CSR must be an exact, word-for-word match for the primary endpoint in the locked protocol version. | Veeva Vault (Locked Protocol vs. Final CSR) |
| **KPI-04** | **Bias Assessment Completeness** | 100% | % of finalized CSRs that contain the mandated chapter on population representativeness and subpopulation bias/fairness assessment, including a quantitative analysis against the pre-defined attributes. | Manual review by the AI Ethics and Fairness Lead (part of QA). |
| **KPI-05** | **Study Cycle Time** | Reduce by 10% YoY | Time in weeks from SCD Stage Gate 0 Approval to Final CSR Archival. Monitored for specific study phases (retrospective, prospective). | Veeva Vault workflow timestamps |

### 7.2 Governance and Reporting Cadence

**A. Operational Dashboard (Daily/Weekly):** A Microsoft PowerBI operational dashboard, ingesting data via the Veeva Vault API and Jira, will display for the VP of Clinical AI Products and her direct reports:
- All active validation studies, their current phase gate, and status (GREEN, YELLOW, RED).
- Real-time enrollment metrics for prospective studies, benchmarked against the planned enrollment curve.
- Protocol deviation count per study.

**B. Monthly Quality Review (Monthly):** A 60-minute meeting chaired by the VP of Clinical AI Products with QA, Biostats, and Regulatory Affairs leads. The agenda is focused on KPI-01 (Compliance), KPI-03 (Endpoint Adherence), and trends in exception requests (Section 8). Minutes are formally distributed.

**C. AI Governance Committee Quarterly Report:** A summary slide deck is presented to the AI Governance Committee, chaired by the Chief Medical Officer. This report focuses on aggregate KPIs and strategic themes (e.g., "All our Class III validation studies for 2025 had successful primary endpoints"). This report provides evidence for NIST AI RMF Govern 1.1, demonstrating organizational commitment and accountability structures.

## 8. Exception Handling and Escalation

A core principle of this SOP is pre-specification and lock. Deviations from the locked protocol or SAP are a serious matter and must be managed through a formal, transparent process, not through informal workarounds.

### 8.1 Protocol Deviation

A protocol deviation is any departure from the approved, locked study protocol. Deviations are categorized as follows:

- **Minor Deviation:** A departure that does not affect the scientific integrity of the study, the rights/safety of patients, or the integrity of the study data. *Example: A follow-up patient visit occurred 2 days outside the protocol-specified window; a single lab value is missing from an otherwise complete record.*
- **Major Deviation:** A departure that could significantly impact the completeness, accuracy, and/or reliability of the study data, or that may affect a patient's rights or safety. *Example: Failure to execute a safety monitoring follow-up, enrolling a patient who does not meet all key inclusion criteria, the Biostats team inadvertently using an unlocked, non-validated version of a data query.*

### 8.2 Exception Handling Procedure

1.  **Immediate Identification and Documentation:** Any team member identifying a potential deviation must immediately document it in Veeva Vault using the "Clinical Study Incident & Deviation" form (MER-QA-016). This freezes the record with a unique ID.
2.  **Immediate Containment:** The Study Sponsor (Clinical AI Lead) and the Biostats Lead are jointly responsible for determining an immediate containment action. For a major deviation involving data, this may mean immediately halting the analysis.
3.  **Root Cause Analysis (RCA):** For all Major Deviations, the Study Sponsor must convene a cross-functional RCA meeting (Biostats, Data Ops, Engineering, QA) within five business days. The output is a CAPA (Corrective and Preventive Action) plan documented in the same Veeva record.
4.  **Approval and Escalation Matrix:**
    - **Minor Deviation:** Approved by the Clinical AI Lead (Study Sponsor) and logged in the study's eTMF. No further escalation.
    - **Major Deviation:** The CAPA plan must be Approved by the VP of Clinical AI Products (Dr. Aisha Okafor) AND the Chief Medical Officer (Dr. Priya Patel). The deviation and its resolution are documented in the final CSR, likely as an important sensitivity analysis evaluating the impact of the deviation.
    - **Critical Deviation (affects patient safety, or could render study unusable for regulatory submission):** Immediate escalation to the CMO (Dr. Patel) and the Chief Compliance Officer. A high-risk review board is convened.

All exception records are reviewed monthly as part of the Quality Review (Section 7.2.B) to identify systemic process failures.

## 9. Training Requirements

All personnel identified in the Roles and Responsibilities matrix (Section 3) must be qualified by training to execute their assigned tasks under this SOP.

**9.1 Required Training Courses:**
The Meridian Learning Management System (LMS), "MeridianLearn," will host the following mandatory curricula:

- **Training Assignment Group CLIN-VAL-ALL:** This applies to all individuals in "Responsible" and "Accountable" roles.
    - **M-DOC-016:** Reading and acknowledging this SOP (SOP-CLIN-016). Frequency: Upon initial assignment and annually upon new version release.
    - **M-GCP-101:** Principles of Good Clinical Practice (ICH E6(R3)). Frequency: Every 3 years.
    - **M-NIST-001:** Principles of the NIST AI RMF for Clinical Validation. Frequency: Annually.

- **Training Assignment Group CLIN-VAL-BIOSTATS:** This applies specifically to the Biostats & Data Science team.
    - **M-TECH-041:** Standardized Validation Analysis using `MeridianPower.jl` and `MeridianReports.jl`. Frequency: Annually.

- **Training Assignment Group CLIN-VAL-EXEC:** This applies to approvers and executive sponsors.
    - **M-REG-102:** Regulatory Expectations for Real-World Evidence and AI/ML-Based Medical Devices. Frequency: Every 2 years.

**9.2 Training Tracking and Remediation:**
Upon assigning a training curriculum in MeridianLearn, a 90-day completion deadline is set. 30, 60, and 90-day automated reminder emails are sent. Failure to complete training by the 90th day triggers a mandatory suspension of the employee's access to Clinical Data Lake and Veeva Vault study workspaces by an automated IAM policy integration, as well as an escalation notification to their manager and the QA department. Re-activation is immediate upon course completion.

**9.3 Role-qualification:**
Being assigned a training curriculum is necessary but not sufficient. The VP of Clinical AI Products, in consultation with QA, maintains a delegation of authority log within Veeva Vault. Each role on a specific study (e.g., "Study Sponsor," "Biostats Lead") must have a named, trained individual formally delegated to that log before undertaking any study activities governed by this SOP.

## 10. Related Policies and References

This SOP is part of Meridian's integrated Quality Management System and must be read and applied in conjunction with the following:

**Internal Meridian Documents:**

- **SOP-AI-001:** AI Risk Classification and Lifecycle Management Framework
- **SOP-AI-007:** Management of Model Drift and Post-Market Surveillance Plan
- **SOP-AI-010:** Transparency and Explainability (T&E) Plan Template
- **SOP-PRI-009:** De-identification and Anonymization of Protected Health Information
- **SOP-IT-003:** Data Retention and Archival Policy for Regulated Assets
- **SOP-ENG-042:** Technical Performance Benchmarking of AI Models
- **SOP-QA-001:** Document Management and Control within the Electronic Quality Management System (eQMS)
- **SOP-REG-008:** Preparation and Submission of EU MDR Technical Documentation
- **MER-CLIN-016-F01:** Study Concept Document (SCD) Template
- **MER-CLIN-016-F02:** Clinical Study Protocol Template
- **MER-CLIN-016-F04:** Detailed Statistical Analysis Plan (SAP) Template
- **MER-CLIN-016-F05:** Final Clinical Study Report (CSR) Template
- **MER-CLIN-016-W01:** Study Dataset Lock and Model Freeze Attestation Workflow

**External Standards and Regulations:**

- **Regulation (EU) 2024/1689:** European Union Artificial Intelligence Act. Relevant, as a guiding risk-based framework.
- **Regulation (EU) 2017/745:** Medical Device Regulation (MDR), specifically Annex I (General Safety and Performance Requirements), Section 15.1.2 on Clinical Validation.
- **NIST AI 100-1:** Artificial Intelligence Risk Management Framework (AI RMF 1.0). The functions **Map** (Context, 1.6), **Measure** (Identify and Apply, 2.6), and **Manage** (Prioritize and Act, 3.5) are directly operationalized in the bias assessment, drift monitoring, and exception handling procedures of this document.
- **ICH E6(R3):** Guideline for Good Clinical Practice.
- IDEAL Collaborative. (2019). IDEAL framework for surgical innovation 2.0: IDEAL-AI extension.
- **Declaration of Helsinki:** Ethical Principles for Medical Research Involving Human Subjects.

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **1.4** | **2025-04-28** | Dr. Aisha Okafor, J. Henderson (Reg) | **Current Version.** Major update to Section 5 (Detailed Procedures) to incorporate the revised IDEAL-AI stage gate model. Formalized the joint lock sign-off workflow (MER-CLIN-016-W01) in Veeva. Updated all template form IDs. Added the mandatory `MeridianPower.jl` library specification in Section 5.3. |
| **1.3** | **2024-11-15** | Dr. Aisha Okafor | Minor update to Section 7 (Metrics) to add KPI-04 (Bias Assessment Completeness) and adjust reporting cadence for the AI Governance Committee. Updated roles post re-organization of Biostats and Data Science teams under a single director. |
| **1.2** | **2024-03-01** | Dr. Aisha Okafor, B. Chen (CISO) | Substantial update to Section 6 (Controls and Safeguards) to reflect the migration to a fully containerized and locked inference environment (TC-01) and the introduction of IAM-based Data Firewalls (TC-02). Updated Section 8 (Escalation) with the critical deviation path. |
| **1.1** | **2023-07-12** | Dr. Aisha Okafor | Updated Section 3 (Roles) to include newly created role of Chief Privacy Officer post-MDR readiness program launch. Updated cross-references to new Privacy SOP (SOP-PRI-009). |
| **1.0** | **2023-01-21** | Dr. Aisha Okafor, Dr. Priya Patel | Initial release. Separated clinical validation from general algorithm testing policy. Established pre-registration mandate and detailed SAP requirements. |