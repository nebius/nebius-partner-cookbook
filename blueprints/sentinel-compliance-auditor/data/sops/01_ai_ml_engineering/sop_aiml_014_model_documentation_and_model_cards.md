---
sop_id: "SOP-AIML-014"
title: "Model Documentation and Model Cards"
business_unit: "AI/ML Engineering"
version: "2.9"
effective_date: "2025-12-20"
last_reviewed: "2026-06-21"
next_review: "2026-12-16"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
  - "SR 11-7"
status: "Active"
---

# Standard Operating Procedure: Model Documentation and Model Cards

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for the creation, review, approval, and maintenance of model documentation within Meridian Health Technologies, Inc. ("Meridian" or "the Company"). The primary objective of this SOP is to ensure that all machine learning and artificial intelligence models developed, deployed, or procured by Meridian are accompanied by complete, accurate, standardized documentation that enables effective model risk management, promotes transparency, and satisfies applicable regulatory obligations as they relate to model risk governance.

The secondary purpose is to operationalize the production of Model Cards as the standard vehicle for communicating model characteristics to internal stakeholders, including but not limited to model validation teams, internal audit, compliance personnel, and business unit leadership. Model Cards serve as the canonical record of a model's identity, purpose, architecture, training data, performance characteristics, limitations, and intended use boundaries.

### 1.2 Scope

This SOP applies to all models, algorithms, and AI systems developed, maintained, or procured by any business unit of Meridian Health Technologies, Inc. The term "model" as used herein encompasses, but is not limited to:

- Clinical decision support algorithms deployed within the Clinical AI Platform, including diagnostic imaging analysis models, patient risk scoring engines, and adverse event prediction systems.
- Credit scoring, fraud detection, lending decision, and payment processing models operating within the HealthPay Financial Services business line.
- Population health analytics models, care gap identification algorithms, and outcomes prediction systems within the MedInsight Analytics platform.
- Any supplementary or supporting models embedded within the Meridian SaaS Platform, including but not limited to natural language processing services, recommendation engines, and data transformation pipelines.
- Third-party and vendor-supplied models that are integrated into Meridian products or used to inform business decisions affecting Meridian customers or patients.

This SOP applies to all Meridian personnel involved in the model lifecycle, including employees, contractors, consultants, and temporary staff. The scope extends across all Meridian global offices (Boston, London, Berlin, Singapore, Toronto) and applies to models deployed in any AWS region or disaster recovery environment.

### 1.3 Exclusions

The following are explicitly excluded from the scope of this SOP:

- Simple rule-based systems that do not involve statistical learning, optimization, or pattern recognition (e.g., static lookup tables, hard-coded branching logic without learned parameters). The determination of whether a system qualifies for this exclusion must be documented in writing and approved by the business unit's Model Owner.
- Spreadsheet-based calculations that are not used for credit decisions, clinical recommendations, or regulatory reporting.
- Research prototypes that have not been approved for production deployment and are not processing Production Data as defined in Section 2.1.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Accountable Executive** | The senior leader (VP-level or above) who bears ultimate accountability for all models within a given business unit. |
| **Critical Model** | A model designated as critical based on materiality assessment per SOP-RISK-003, considering factors such as financial impact, patient safety implications, regulatory capital requirements, and operational criticality. |
| **Intended Use** | The specific, bounded purpose for which a model was designed, developed, and validated, including the target population, clinical or business context, and decision framework within which the model is expected to operate safely. |
| **Material Change** | Any modification to a model's architecture, training data distribution, input features, objective function, or deployment environment that, in the judgment of the Model Owner in consultation with the Model Validation team, may materially alter the model's performance characteristics, risk profile, or suitability for its Intended Use. |
| **Model** | A quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates. For purposes of this SOP, this definition encompasses all supervised and unsupervised machine learning models, deep learning networks, natural language processing systems, and ensembles thereof. |
| **Model Card** | A structured, standardized document that provides essential information about a model's identity, intended use, architecture, training and evaluation data, performance metrics, limitations, ethical considerations, and recommended usage protocols. The Model Card template is defined in Appendix A of this SOP. |
| **Model Owner** | The named individual (Director-level or above) responsible for the end-to-end lifecycle management of a specific model or model family, including documentation, performance monitoring, and remediation. |
| **Model Validator** | An individual or team functionally independent from model development who is responsible for conducting independent validation activities, including documentation completeness checks. For SR 11-7 scoped models, the Model Validator must report to an organizational unit that is independent of the model development and business line functions. |
| **Production Data** | Data that originates from or represents actual patients, customers, transactions, or operations, as distinguished from synthetic, simulated, or test data. For HealthPay Financial Services models, Production Data includes personally identifiable information (PII) and protected financial information. |
| **SR 11-7 Model** | A model used for credit scoring, fraud detection, lending decisions, or payment processing that falls within the scope of the Federal Reserve's SR Letter 11-7 guidance on model risk management. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| AI | Artificial Intelligence |
| CIO | Chief Information Officer |
| CISO | Chief Information Security Officer |
| CMO | Chief Medical Officer |
| CPO | Chief Privacy Officer |
| DPO | Data Protection Officer |
| EDA | Exploratory Data Analysis |
| F1 | Harmonic mean of precision and recall |
| FN | False Negative |
| FP | False Positive |
| GDPR | General Data Protection Regulation |
| HIPAA | Health Insurance Portability and Accountability Act |
| KPI | Key Performance Indicator |
| ML | Machine Learning |
| MRE | Model Risk Evaluation |
| PHI | Protected Health Information |
| RACI | Responsible, Accountable, Consulted, Informed |
| ROC-AUC | Area Under the Receiver Operating Characteristic Curve |
| SLA | Service Level Agreement |
| TN | True Negative |
| TP | True Positive |
| VP | Vice President |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the responsibilities of key roles in the Model Documentation lifecycle. Each model registered in the Meridian Model Inventory System (see Section 5.2) must have these roles explicitly assigned.

| Activity / Deliverable | Model Owner | AI/ML Engineer | Model Validator | Accountable Executive | Compliance Officer | CISO / DPO |
|---|---|---|---|---|---|---|
| Author initial Model Card | A | R | C | I | I | I |
| Validate Model Card completeness | I | I | R | A | I | I |
| Approve Model Card for production | C | I | C | A | I | I |
| Update Model Card after Material Change | A | R | C | I | I | I |
| Annual Model Card review and recertification | R | C | C | A | I | I |
| Identify model as Critical per SOP-RISK-003 | R | C | C | A | I | I |
| Escalate documentation non-compliance | R | I | R | A | C | I |
| Confirm SR 11-7 documentation requirements met | A | C | R | I | C | I |
| Review data privacy statements in Model Card | C | C | I | I | I | R |
| Archive deprecated model documentation | R | C | I | A | I | I |

**R** = Responsible (performs the work) | **A** = Accountable (approves the work) | **C** = Consulted (provides input) | **I** = Informed (notified of outcome)

### 3.1 Named Role Descriptions

**Dr. Marcus Rivera, Chief AI Officer**, serves as the executive sponsor for this SOP and chairs the quarterly Model Documentation Compliance Review. The CAIO may delegate operational oversight to the VP of Engineering but retains ultimate accountability for adherence to this SOP across all business units.

**David Park, VP of Engineering**, is responsible for integrating the requirements of this SOP into the software development lifecycle (SDLC) and for ensuring that adequate tooling and automation exist to support Model Card generation and maintenance at scale.

**Accountable Executive (Business Unit Level)**: Each business unit must designate an Accountable Executive for its models:
- Clinical AI Platform: Dr. Aisha Okafor, VP of Clinical AI Products
- HealthPay Financial Services: Robert Liu, VP of Financial Services
- MedInsight Analytics: Dr. Priya Patel, Chief Medical Officer (interim)
- Meridian SaaS Platform: David Park, VP of Engineering

**Thomas Anderson, Chief Compliance Officer**, is responsible for incorporating SR 11-7 documentation requirements into the company's compliance testing program and for reporting material documentation deficiencies to the Board-level AI Governance Committee.

**Model Validation Team**: An independent team reporting to the Chief Compliance Officer with a dotted line to the CAIO. This team is responsible for conducting independent reviews of Model Cards and associated documentation for all SR 11-7 Models and Critical Models.

---

## 4. Policy Statements

### 4.1 Mandatory Documentation

Meridian Health Technologies, Inc. requires that every model deployed in a production environment or used to inform a material business decision be accompanied by a completed Model Card that has been reviewed and approved in accordance with this SOP. No model shall be promoted to production status without an approved Model Card on file in the Meridian Model Inventory System.

### 4.2 SR 11-7 Compliance

Meridian is committed to sound model risk management practices consistent with the Federal Reserve's Supervisory Guidance on Model Risk Management (SR Letter 11-7). Specifically, this SOP implements the documentation standards required by SR 11-7, which stipulates that model documentation must be sufficiently detailed to allow parties unfamiliar with the model to understand the model's functioning, limitations, and key assumptions. For SR 11-7 Models, documentation must meet the following specific requirements:

- **Conceptual Soundness Documentation (SR 11-7 Section III.A)**: Model Cards must include a comprehensive description of the theory, logic, and assumptions underlying the model design. This includes, at minimum: (a) a detailed exposition of the mathematical and statistical methodology employed; (b) justification for the choice of methodology relative to alternatives considered; (c) description of the theoretical relationship between input variables and predicted outcomes; and (d) documentation of all expert judgment or qualitative adjustments applied.
- **Data Integrity Documentation (SR 11-7 Section III.B)**: Model Cards must document the source, quality, and relevance of data used to develop and test the model. This must include: (a) provenance of all training, validation, and test datasets; (b) descriptive statistics for all input features, including counts of missing values and extreme observations; (c) data preprocessing and transformation steps applied; (d) assessment of data representativeness relative to the target population; and (e) documentation of any proxy variables used when ideal data was unavailable.
- **Model Performance Testing (SR 11-7 Section III.C)**: Model Cards must document the results of performance testing, including: (a) sensitivity analysis demonstrating model behavior across a plausible range of input values; (b) back-testing results where historical data is available; (c) benchmarking against alternative models or industry standards; (d) stability analysis assessing the sensitivity of model outputs to small perturbations in inputs; and (e) stress testing results under adverse scenarios defined in SOP-RISK-004.
- **Outcomes Analysis (SR 11-7 Section IV)**: Model Cards must contain a framework for ongoing outcomes analysis, specifying: (a) key metrics to be tracked on an ongoing basis; (b) thresholds that trigger investigation or remediation; (c) the cadence of performance monitoring (minimum monthly for Critical Models, quarterly for all other SR 11-7 Models); and (d) the responsible party for conducting and reviewing outcomes analysis.

### 4.3 Model Card Minimum Content

Every Model Card produced under this SOP shall contain, at minimum, the following sections. Detailed specifications for each section are provided in Appendix A.

1. **Model Identity and Versioning**: Unique identifier, version number, date of last training, owning business unit, and development team.
2. **Intended Use and Target Population**: Precise specification of the model's intended purpose, the population on which it is designed to operate, and the decision context in which model outputs are expected to be used.
3. **Model Architecture and Methodology**: Description of the model type, architecture, training objective, optimization algorithm, and key hyperparameters.
4. **Training and Evaluation Data**: Description of datasets used, including source, size, time period covered, and known limitations or biases.
5. **Performance Metrics**: Quantitative performance metrics on held-out test data, stratified by relevant subgroups where applicable.
6. **Fairness and Bias Assessment**: Analysis of model performance across demographic or clinically relevant subgroups, with identification of any disparate performance or outcome patterns.
7. **Limitations and Out-of-Scope Uses**: Explicit enumeration of known limitations and contexts in which the model should not be used.
8. **Ethical Considerations**: Assessment of potential societal or individual impacts, including dual-use risks and steps taken to mitigate identified concerns.
9. **Maintenance and Monitoring Plan**: Schedule for periodic review, performance monitoring, and conditions triggering unscheduled review.
10. **Regulatory Compliance Mapping**: Cross-reference to applicable regulatory requirements satisfied by this documentation.

### 4.4 Timeliness and Recertification

Model documentation must be maintained in a current and accurate state throughout the model's production lifecycle. Specifically:

- Initial Model Cards must be completed and approved prior to production deployment.
- Updates reflecting Material Changes must be completed within 30 calendar days of the change.
- Annual recertification of Model Card accuracy must be completed by the Model Owner by the anniversary date of the model's initial approval. Recertification includes: (a) verification that all performance metrics reflect current production performance; (b) review and update of limitations based on operational experience; (c) confirmation that the Intended Use statement remains accurate; and (d) documentation of any drift or degradation observed since last review.
- Deprecated or decommissioned models must have their Model Cards archived with a retirement date annotation within 15 business days of decommissioning.

---

## 5. Detailed Procedures

### 5.1 Model Onboarding and Initial Documentation

This procedure describes the steps required to document a new model entering the Meridian model ecosystem.

#### 5.1.1 Pre-Development Documentation (Phase 0)

Prior to commencing model development, the proposing team shall complete the following:

1. **Register Intent**: The Model Owner (identified by the business unit) shall submit a New Model Intent Form in the Meridian Model Inventory System. This form captures: proposed model ID, business justification, initial risk classification (per SOP-RISK-003), and designation of whether the model will process PHI or financial data.
2. **Conduct Preliminary SR 11-7 Scoping**: The Model Owner and the Model Validation team shall jointly determine whether the proposed model falls within the scope of SR 11-7 based on its intended use in credit, fraud, or lending decisions. This determination must be documented in the Model Inventory System. If the model is classified as an SR 11-7 Model, a senior validator must be assigned as a reviewer prior to any data ingestion.
3. **Document Data Sources**: The AI/ML engineering team shall document all anticipated data sources in the Data Source Registry module of the Model Inventory System, including: source name, data custodian, data classification (per SOP-DATA-005), expected volume, and known quality issues.

#### 5.1.2 Development-Phase Documentation (Phase 1)

During model development, the AI/ML team shall maintain a Development Log containing:

1. **EDA Summary**: Exploratory data analysis results, including distributions of key features, correlation matrices, identified outliers, and treatment of missing data.
2. **Feature Engineering Log**: Documentation of all feature transformations, encodings, and derived features, with justification for each.
3. **Algorithm Selection Rationale**: Written justification for the selected modeling approach, including a comparison of at least two candidate approaches (if only one is proposed, a written justification for why alternatives were not feasible is required).
4. **Hyperparameter Tuning Record**: Search space definition, optimization strategy, and final selected hyperparameters with corresponding performance on the validation set.
5. **Code Repository Reference**: Link to the version-controlled repository (GitHub Enterprise or equivalent) containing the training pipeline, tagged with the model version identifier.

The Development Log shall be maintained in a format that can be linked or appended to the final Model Card.

#### 5.1.3 Pre-Deployment Model Card Completion (Phase 2)

At least 14 calendar days prior to the scheduled production deployment date, the Model Owner shall submit a complete draft Model Card for review. The submission must include:

1. **Completed Model Card** (all sections per Appendix A populated).
2. **Independent Test Set Performance Report**: Results on a held-out test set that was not used during model development or hyperparameter optimization. The report must include, for SR 11-7 Models, the following minimum metrics:
   - Confusion matrix (TP, FP, TN, FN) and derived metrics (accuracy, precision, recall, F1 score).
   - ROC-AUC with 95% confidence interval.
   - Calibration curve (reliability diagram) for probabilistic outputs.
   - Performance stratified by at least three relevant demographic or risk-stratified subgroups.
   - Kolmogorov-Smirnov (KS) statistic for rank-ordering ability.
3. **Fairness Assessment**: For models processing individual-level data where demographic attributes are known or inferable, a fairness analysis reporting:
   - Statistical parity difference between the most- and least-favored subgroups.
   - Equal opportunity difference (true positive rate parity).
   - Average odds difference.
   - Thresholds for flagging: differences exceeding 10 percentage points require mitigation; differences exceeding 20 percentage points require escalation to the AI Governance Committee prior to deployment approval.
4. **Stability Test Results**: Sensitivity of key performance metrics (F1, AUC) to random perturbation of input features at magnitudes of 1%, 5%, and 10% of the feature's standard deviation.
5. **Data Quality Certificate**: Attestation from the Data Engineering team confirming that the training data pipeline has passed data quality checks per SOP-DATA-006, including completeness (>95% required for SR 11-7 models), consistency, and timeliness.

#### 5.1.4 Model Card Review and Approval (Phase 3)

Upon submission of the complete package, the following review workflow is initiated:

| Review Stage | Reviewer | Timeline | Criteria |
|---|---|---|---|
| **Completeness Check** | Model Validator | 3 business days | All required fields populated; attachments present |
| **Technical Review** | Peer AI/ML Engineer (not on development team) | 5 business days | Reproducibility of reported metrics; code review of evaluation scripts |
| **SR 11-7 Compliance Review** | Senior Model Validator (if applicable) | 7 business days | Verification against SR 11-7 Sections III.A-III.C and IV |
| **Privacy & Security Review** | CISO / DPO delegate | 3 business days | Data handling compliance; PHI/PII exposure assessment |
| **Final Approval** | Accountable Executive | 3 business days | Sign-off for production deployment |

If any reviewer identifies deficiencies, the Model Owner is notified and must resubmit within the original 14-day window or request an extension. Extensions beyond 30 days from initial submission require written approval from the CAIO.

Approval is recorded in the Model Inventory System with a digital signature from the Accountable Executive.

### 5.2 Model Inventory System

The Meridian Model Inventory System (accessible at `https://model-inventory.internal.meridian.com`) serves as the system of record for all model documentation. The system maintains:

- A unique Model ID for each registered model (format: `MER-ML-[BUSINESS_UNIT]-[SEQUENTIAL]`, e.g., `MER-ML-CLIN-0147`).
- Version-controlled Model Cards with full audit trail (creation, modification, approval timestamps and actor identities).
- Automated workflow routing for review and approval per Section 5.1.4.
- Searchable metadata including business unit, model type, risk classification, SR 11-7 status, and review due dates.

All Model Cards must be stored in this system. No model may exist in production without a corresponding entry. IT Operations, under the direction of the VP of Engineering, is responsible for maintaining the availability, integrity, and backup of the Model Inventory System with a recovery time objective (RTO) of 4 hours and a recovery point objective (RPO) of 1 hour.

### 5.3 Material Change Documentation

When a Material Change (as defined in Section 2.1) is made to a model, the documentation update procedure is:

1. **Change Impact Assessment**: The Model Owner completes a Material Change Assessment Form documenting: (a) nature and rationale of the change; (b) expected impact on model performance; (c) comparison of pre- and post-change performance on a consistent test set; (d) determination of whether the change requires re-approval or supplemental approval.
2. **Model Card Revision**: Updated sections of the Model Card are drafted, with change bars indicating modifications from the previous version.
3. **Validation Scope Determination**: The Model Validator reviews the Change Impact Assessment and determines the scope of re-validation required:
   - **Minor Change**: Targeted review of affected sections; 5 business day turnaround.
   - **Significant Change**: Full re-validation of performance and fairness metrics; 10 business day turnaround.
   - **Fundamental Change**: Model treated as new; full Phase 0-3 process applies; 30 business day timeline.
4. **Re-Approval**: Updated Model Card is routed through the review workflow (Section 5.1.4) at the validation level determined above. Final approval is required from the Accountable Executive.
5. **Version Archive**: The prior version of the Model Card is archived with the effective end date recorded. Retention of archived versions is indefinite.

### 5.4 Annual Recertification Procedure

By the first business day of the model's anniversary month, the Model Inventory System generates an automated notification to the Model Owner. The procedure is:

1. **Performance Refresh**: The Model Owner, in coordination with the operations/MLOps team, shall re-execute the evaluation pipeline against the current production model using either: (a) the most recent three months of production data (for models with continuous inference), or (b) a contemporary hold-out sample drawn from production data (for batch-scored models). Metrics reported must match those in the original Model Card.
2. **Drift Assessment**: Compare current metrics to the metrics reported in the most recently approved Model Card. Thresholds:
   - ROC-AUC degradation >5 absolute percentage points: requires investigation and remediation plan within 60 days.
   - F1 score degradation >7 absolute percentage points: requires investigation and remediation plan within 60 days.
   - KS statistic below 30% for SR 11-7 credit models: immediate escalation to CCO and CAIO.
3. **Limitations Review**: Review the limitations section against operational incident reports (from Jira Service Management or equivalent) to identify any new limitations not captured in the existing documentation. Any incident classified as P1 or P2 (per SOP-INC-001) that involved model error or unexpected behavior MUST be documented as a new limitation or risk.
4. **Recertification Attestation**: The Model Owner submits a signed attestation confirming: (a) review of current performance against benchmarks; (b) accuracy of Intended Use statement; (c) no unreported drift; and (d) any updates made to limitations or ethical considerations.
5. **Validator Spot Check**: The Model Validation team randomly samples 20% of annual recertifications for full independent review. Models flagged for spot check are notified to the Model Owner within 5 business days of recertification submission.

### 5.5 Third-Party and Vendor Model Documentation

For models procured from third-party vendors, the Procurement team shall ensure that the vendor contract includes a requirement for delivery of documentation equivalent to a Meridian Model Card. Specifically:

1. **Pre-Procurement Assessment**: The Model Owner (assigned by the procuring business unit) shall complete a Vendor Model Assessment, evaluating the vendor's documentation against the standards of this SOP. Gaps shall be documented in a Gap Analysis Report.
2. **Contractual Requirement**: Vendor agreements must stipulate delivery of: model architecture description, training data characteristics (sufficient to assess representativeness), performance benchmarks, known limitations, and intended use boundaries. For SR 11-7 Models provided by vendors, the contract must also require annual updated performance reports benchmarked against Meridian-specific data.
3. **Internal Model Card Creation**: Within 45 calendar days of vendor model receipt, the assigned Model Owner shall produce an internal Model Card based on vendor documentation, supplemented by Meridian-led evaluation on Meridian data. Gaps shall be explicitly identified.
4. **Risk Acceptance**: Where gaps cannot be remediated, the Accountable Executive and CCO must jointly sign a Risk Acceptance Memorandum, which is filed with the Model Card and reviewed annually.

### 5.6 Deprecated Model Archiving

When a model is decommissioned:

1. The Model Owner updates the Model Card status to "Deprecated" with an effective date.
2. A final performance summary covering the model's operational period is appended.
3. All associated documentation (Model Card, validation reports, development logs) is archived to the long-term retention repository.
4. Retention period: 10 years from date of deprecation for SR 11-7 Models; 5 years for all others.
5. The Model Inventory System entry is marked as read-only, with metadata indicating archive location.

---

## 6. Controls and Safeguards

### 6.1 Access Controls

Access to Model Cards in the Model Inventory System is governed by role-based access control (RBAC):

| Role | Access Level |
|---|---|
| Model Owners | Read/Write for owned models; Read for all models |
| AI/ML Engineers | Read/Write for assigned models; Read for team models |
| Model Validators | Read for all models; Write for validation review sections |
| Compliance / Audit | Read for all models; Download capability |
| Accountable Executives | Read for business unit models; Write for approval |
| External Auditors | Read-only (time-limited, approved by CISO) |

Modification of any approved Model Card requires explicit check-out from the system, which generates an audit trail entry recording the user, timestamp, and nature of the change.

### 6.2 Segregation of Duties

Consistent with SR 11-7 principles, the following segregation requirements are enforced:

- No individual may serve as both the Model Owner and the Model Validator for the same model.
- Model Validators must be organizationally independent from model development. For SR 11-7 Models and Critical Models, the validation function reports to the Chief Compliance Officer, not to the AI/ML Engineering organization.
- Approval decisions for SR 11-7 Model Cards require signatures from both the Accountable Executive (business) and an independent validator (independent control function).

### 6.3 Audit Trail

The Model Inventory System maintains an immutable audit log recording:

- Every access to a Model Card (user, timestamp, action).
- Every modification to a Model Card (before/after snapshots).
- Every approval or rejection action.
- Every Material Change Assessment.

Audit logs are retained for the life of the model plus 7 years, consistent with Meridian's record retention policy (SOP-COMP-008).

### 6.4 Version Control

Model Cards are subject to semantic versioning:

- **Major version** (X.0): Incremented upon fundamental re-development or re-architecture.
- **Minor version** (X.Y): Incremented upon Material Change that does not constitute a fundamental change.
- **Patch version** (X.Y.Z): Incremented upon non-material updates, errata corrections, or routine recertification with no substantive changes.

The current approved version is the only version considered authoritative. Access to previous versions is read-only and available for audit and comparison.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators

The following KPIs shall be tracked and reported monthly to the CAIO and quarterly to the AI Governance Committee:

| KPI | Target | Measurement Method |
|---|---|---|
| **On-Time Initial Documentation** | ≥95% of models approved prior to production deployment | Automated flag in Model Inventory System; violations reported monthly |
| **Material Change Update Timeliness** | ≥90% updated within 30 calendar days | Tracked by change event timestamp vs. revised approval timestamp |
| **Annual Recertification On-Time Rate** | ≥95% completed by anniversary date | System-generated due dates vs. completion dates |
| **SR 11-7 Documentation Conformance** | 100% of SR 11-7 models have all required sections fully populated | Quarterly audit by Model Validation team; sample of 100% of SR 11-7 models |
| **Documentation Defect Rate** | <5% of spot-checked cards have identified gaps | Independent review by CCO designee; random sample of 10% of all active Model Cards quarterly |
| **Post-Deployment Documentation Completeness** | <2% of production models lacking approved Model Card | Reconciliation of Model Inventory System vs. production model registry |

### 7.2 Reporting Cadence

| Report | Frequency | Audience | Prepared By |
|---|---|---|---|
| Documentation Compliance Dashboard | Monthly | CAIO, Accountable Executives | Model Validation Team |
| SR 11-7 Conformance Report | Quarterly | CCO, CAIO, Board AI Governance Committee | Compliance Officer |
| Annual DSR Process Effectiveness Review | Annually | CCO, CAIO, CPO | Privacy Office |
| Exception Tracking Log | Continuous | CAIO, Accountable Executives | Model Inventory System (automated) |

### 7.3 Escalation Triggers

Automated alerts are generated by the Model Inventory System under the following conditions:

- A model enters production without an approved Model Card (alert to CAIO and Accountable Executive; response required within 24 hours).
- Annual recertification is 15 days overdue (alert to Model Owner and Accountable Executive).
- Annual recertification is 30 days overdue (alert to CAIO; Model Owner status changed to "Non-Compliant").
- Post-deployment reconciliation detects a production model with no Model Inventory entry (alert to CAIO and CISO for immediate investigation).

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

In circumstances where strict compliance with a provision of this SOP is infeasible, a formal exception request may be submitted. The process is:

1. **Initiation**: The Model Owner submits a Documentation Exception Request (Form DER-014, available in the Compliance Portal) specifying: (a) the specific SOP provision for which exception is sought; (b) the rationale for non-compliance; (c) the proposed alternative control or compensating measure; (d) the duration for which the exception is needed; and (e) an assessment of risk associated with the exception.
2. **Risk Assessment**: The Model Validation team evaluates the exception's impact on model risk and documentation integrity.
3. **Approval Authority**:
   - Exceptions for non-SR-11-7 models with duration ≤60 days: Accountable Executive and CAIO.
   - Exceptions for SR 11-7 models or duration >60 days: Accountable Executive, CAIO, and CCO.
   - Exceptions exceeding 90 days: Must be escalated to the Board AI Governance Committee.
4. **Tracking**: All approved exceptions are logged in the Exception Tracking module of the Model Inventory System, visible to auditors and regulators upon request. Expired exceptions without resolution trigger automatic escalation.
5. **Review**: All open exceptions are reviewed at the quarterly AI Governance Committee meeting. Recurring exceptions for the same model or business unit trigger a root-cause analysis requirement.

### 8.2 Escalation Path

For issues that cannot be resolved at the operational level:

1. **Level 1**: Model Owner and Model Validator cannot reconcile a documentation dispute → escalate to Accountable Executive.
2. **Level 2**: Accountable Executive cannot resolve within 5 business days → escalate to CAIO and CCO jointly.
3. **Level 3**: CAIO and CCO cannot reach agreement within 10 business days → escalate to CEO or designated executive committee member for binding resolution.
4. **Level 4 (Regulatory)**: Any documentation issue that may impact regulatory compliance, particularly SR 11-7 obligations, must be escalated to the CCO within 24 hours of identification, regardless of other resolution efforts.

---

## 9. Training Requirements

### 9.1 Initial Training

All personnel assigned to roles defined in Section 3 of this SOP shall complete the following training within 30 days of role assignment:

| Training Module | Target Audience | Duration | Delivery Method |
|---|---|---|---|
| SOP-AIML-014 Awareness and Compliance | All Model Owners, AI/ML Engineers, Validators | 2 hours | LMS (Workday Learning) |
| SR 11-7 Documentation Standards | Model Owners and Validators for SR 11-7 models | 3 hours | Instructor-led (quarterly sessions) |
| Model Card Authoring Workshop | AI/ML Engineers | 4 hours | Hands-on workshop with sample datasets |
| Bias Detection and Fairness Analysis | All AI/ML Engineers | 2 hours | LMS + case study exercise |
| Model Inventory System Usage | All users | 1.5 hours | System walkthrough + sandbox exercise |

### 9.2 Annual Refresher Training

All individuals with active Model Owner responsibilities or validation duties must complete an annual refresher covering:

- Updates to this SOP (if version has changed since last training).
- Lessons learned from documentation deficiencies identified during audits.
- Changes to regulatory requirements affecting SR 11-7 compliance.

Refresher training must be completed by December 15 of each calendar year. Completion rates are tracked and reported to the CAIO.

### 9.3 Training Records

Training completion is recorded in Workday Learning and linked to the individual's compliance profile. The CCO's office conducts quarterly reconciliation to identify any individuals with overdue training and notifies their managers.

---

## 10. Related Policies and References

### 10.1 Internal SOPs and Policies

| Document ID | Title | Relationship |
|---|---|---|
| SOP-RISK-003 | Model Risk Classification and Materiality Assessment | Defines criteria for Critical Model designation |
| SOP-RISK-004 | Model Stress Testing and Scenario Analysis | Defines adverse scenarios for stress testing documentation |
| SOP-DATA-005 | Data Classification and Handling | Governs data classification referenced in documentation |
| SOP-DATA-006 | Data Quality Management | Defines data quality checks for training pipelines |
| SOP-MLOPS-002 | Model Deployment and Lifecycle Management | Governs production deployment gating |
| SOP-COMP-008 | Records Retention and Archiving | Defines retention periods for documentation |
| SOP-INC-001 | Incident Management and Response | Incident classification used in limitations review |
| SOP-VALD-001 | Independent Model Validation | Validation standards and procedures |

### 10.2 External References

- Board of Governors of the Federal Reserve System, SR Letter 11-7: "Supervisory Guidance on Model Risk Management" (April 4, 2011)
- Federal Reserve SR Letter 11-7 Attachment: "Guidance on Model Risk Management"
- Meridian Health Technologies Model Risk Management Policy (CORP-POL-011)

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2020-03-15 | J. Martinez | Initial publication establishing basic Model Card framework. |
| 2.4 | 2021-08-12 | K. Chen | Added Material Change definition; expanded Third-Party section; updated templates in Appendix A. |
| 2.6 | 2023-02-28 | L. Osei | Comprehensive update: integrated SR 11-7 specific requirements; added fairness metrics; expanded validation procedures for SR 11-7 models; updated RACI to include Compliance Officer for SR 11-7 models. |
| 2.7 | 2024-05-17 | M. Rivera | Revised scoring thresholds; added KS statistic monitoring; updated segregation of duties language; introduced annual recertification spot check; clarified training requirements for SR 11-7 documentation. |
| 2.8 | 2025-06-10 | M. Rivera, T. Anderson | Added Section 4.5 timeliness and recertification policy; updated Section 5.6 archiving retention periods; refined KPI targets; added escalation path in Section 8.2; minor corrections to definitions. |
| 2.9 | 2025-12-20 | M. Rivera, D. Park | Incorporated feedback from 2025 internal audit: strengthened exception handling controls; added 24-hour alert for undocumented production models; expanded training requirements matrix; reorganized Section 5 for clarity; updated thresholds for drift assessment; this version approved following full review by AI Governance Committee. |

---

**END OF DOCUMENT**

*© Meridian Health Technologies, Inc. This document contains proprietary and confidential information. Unauthorized reproduction or distribution is prohibited. Access is restricted to authorized personnel per the classification designation.*