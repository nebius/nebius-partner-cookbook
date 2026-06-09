---
sop_id: "SOP-AIML-001"
title: "Model Development Lifecycle"
business_unit: "AI/ML Engineering"
version: "2.1"
effective_date: "2024-05-08"
last_reviewed: "2025-12-21"
next_review: "2026-06-15"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
  - "SR 11-7"
status: "Active"
---

# Standard Operating Procedure: Model Development Lifecycle

**SOP-AIML-001 | Version 2.1**
**Effective Date:** 2024-05-08
**Owner:** Dr. Marcus Rivera, Chief AI Officer
**Classification:** Internal

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory, enterprise-wide framework governing the end-to-end lifecycle for all artificial intelligence and machine learning (AI/ML) models developed, deployed, procured, or maintained by Meridian Health Technologies, Inc. The purpose of this document is to standardize model development activities, ensure consistent application of risk management principles, maintain rigorous documentation standards, and establish clear approval mechanisms that enable innovation while safeguarding patient safety, data privacy, and regulatory compliance.

This SOP operationalizes Meridian's commitment to responsible AI development by translating the principles of the NIST AI Risk Management Framework (AI RMF 1.0) into actionable, auditable procedures. It defines the controls, artifacts, reviews, and approvals required before any model transitions from ideation to production deployment.

### 1.2 Scope

This SOP applies to all models, algorithms, and AI systems across all business units, regardless of deployment environment, development methodology, or geographic location. The scope encompasses:

**In-Scope Models:**
- All models developed by the AI/ML Engineering business unit
- Models developed by Clinical AI Products, HealthPay Financial Services, and MedInsight Analytics teams
- Third-party and vendor-supplied models integrated into Meridian products
- Open-source models that have been fine-tuned, retrained, or modified by Meridian personnel
- Foundation models and large language models (LLMs) when adapted for Meridian use cases
- Rule-based systems that produce outputs used in clinical, financial, or operational decision-making
- Models operating in development, staging, shadow, A/B testing, and production environments

**In-Scope Activities:**
- Model ideation, problem formulation, and feasibility assessment
- Data acquisition, preparation, labeling, and feature engineering
- Model selection, training, hyperparameter tuning, and evaluation
- Model validation, fairness assessment, and bias testing
- Model deployment, integration, and operationalization
- Model monitoring, maintenance, and periodic retraining
- Model decommissioning and archival

**Applicability by Business Line:**

| Business Unit | Product Line Impact | Primary Risk Classification |
|---------------|--------------------|----------------------------|
| Clinical AI Platform | Patient risk scoring, diagnostic imaging, adverse event prediction | High-Risk AI System |
| HealthPay Financial Services | Credit scoring, fraud detection, claims prediction, lending models | High-Stakes Financial Model |
| MedInsight Analytics | Population health, care gap identification, outcomes prediction | PHI-Processing Model |
| Meridian SaaS Platform | Infrastructure-level optimization, anomaly detection | Operational Model |

**Out of Scope:**
- Simple statistical analyses performed in BI tools (e.g., Tableau calculations without predictive components)
- Spreadsheet-based calculations not integrated into automated decision pipelines
- Models used exclusively for academic research with no path to production (requires waiver from Chief AI Officer)

### 1.3 Applicability to Personnel

All employees, contractors, interns, and third-party partners who design, develop, test, deploy, monitor, or approve AI/ML models must comply with this SOP. Compliance is mandatory and will be verified through the model governance review process, internal audits, and as part of SOC 2 Type II and HITRUST CSF certification assessments.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|------|------------|
| **Adverse Impact Assessment** | A structured evaluation of potential negative consequences resulting from model errors, misuse, or failure, including clinical harm, financial loss, discrimination, and reputational damage. |
| **Approval Gate** | A mandatory checkpoint in the model development lifecycle at which specified criteria must be satisfied and documented approval obtained before the model may proceed to the next phase. |
| **Bias Testing** | Quantitative evaluation of model outputs across protected demographic subgroups to identify statistically significant disparities in performance or outcomes. |
| **Concept Drift** | A change in the statistical relationship between input features and target variables over time, potentially degrading model performance. |
| **Data Drift** | A change in the distribution of input features compared to the training data distribution. |
| **Explainability** | The degree to which a model's outputs and decision-making process can be understood and articulated in human-interpretable terms appropriate to the stakeholder audience. |
| **Fairness Metrics** | Quantitative measures used to evaluate disparate treatment or disparate impact, including demographic parity, equalized odds, equal opportunity, and predictive parity, as defined in SOC-QUA-002. |
| **Foundation Model** | A large-scale model trained on broad data at scale, designed to be adapted for a range of downstream tasks through fine-tuning, prompting, or other adaptation methods. |
| **Model Card** | A standardized, structured document describing a model's intended use, training data, evaluation results, limitations, ethical considerations, and performance characteristics. Required artifact per this SOP. |
| **Model Inventory** | The centralized system of record maintained in the MLflow Model Registry containing metadata, version history, and governance status for all models across the enterprise. |
| **Model Risk Tier** | A classification level (Critical, High, Medium, Low) assigned to each model based on the severity and likelihood of harm resulting from model failure, error, or misuse. |
| **Responsible AI Review (RAIR)** | A cross-functional governance review conducted at Gate 3 to evaluate a model's alignment with Meridian's ethical AI principles, fairness standards, and risk tolerance. |
| **Shadow Deployment** | A pre-production phase in which a model processes live data and generates predictions that are logged and compared against existing systems without influencing real-world decisions. |
| **Technical Specification Document (TSD)** | A comprehensive technical document describing model architecture, training methodology, data provenance, hyperparameters, and all technical decisions made during development. |

### 2.2 Acronyms

| Acronym | Full Term |
|---------|-----------|
| AI RMF | Artificial Intelligence Risk Management Framework (NIST) |
| CAIO | Chief AI Officer |
| CISO | Chief Information Security Officer |
| CMO | Chief Medical Officer |
| CPO/DPO | Chief Privacy Officer / Data Protection Officer |
| GDPR | General Data Protection Regulation |
| HIPAA | Health Insurance Portability and Accountability Act |
| HITRUST CSF | Health Information Trust Alliance Common Security Framework |
| LLM | Large Language Model |
| MLflow | Machine Learning Lifecycle Management Platform |
| PHI | Protected Health Information |
| RAIR | Responsible AI Review |
| TSD | Technical Specification Document |
| VP | Vice President |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following RACI matrix defines accountability, responsibility, consultation, and information roles for all activities within the Model Development Lifecycle.

**R = Responsible** (executes the work)
**A = Accountable** (approves; single point of accountability)
**C = Consulted** (provides input)
**I = Informed** (receives status updates)

| Activity / Decision | Model Developer | Model Owner | AI Governance Committee | CAIO | CISO | CPO/DPO | VP Eng. | CMO (Clinical) | Compliance Officer |
|---------------------|-----------------|-------------|------------------------|------|------|---------|---------|----------------|-------------------|
| Problem Formulation & Feasibility | R | A | I | C | - | - | I | C (if clinical) | - |
| Data Acquisition & Preparation | R | A | - | I | C | C | I | - | - |
| Model Training & Selection | R | A | - | I | - | - | I | - | - |
| Bias & Fairness Testing | R | C | I | A | - | - | - | C | - |
| Responsible AI Review (Gate 3) | C | C | A | R | C | C | I | C | C |
| Security Review (Gate 4) | C | C | - | I | A | C | I | - | - |
| Production Approval (Gate 5) | I | R | - | A | C | C | C | C | C |
| Model Card Completion | R | A | I | C | - | - | - | - | - |
| Post-Deployment Monitoring | R | A | I | I | I | - | I | - | - |
| Model Decommissioning | R | A | I | C | C | C | I | - | - |

### 3.2 Role Definitions

**Model Developer (Data Scientist / ML Engineer)**
- Executes technical development activities including data processing, feature engineering, model training, evaluation, and documentation
- Creates and maintains model artifacts in designated repositories (MLflow, GitHub Enterprise)
- Implements fairness testing protocols and documents results
- Responds to monitoring alerts and executes model retraining procedures
- Required qualifications: Master's degree in quantitative field with 3+ years ML experience, or PhD with 1+ years

**Model Owner (Product Manager / Technical Lead)**
- Serves as the business owner of the model throughout its lifecycle
- Defines model requirements, success criteria, and acceptable performance thresholds
- Approves model behavior changes, retraining scope, and decommissioning decisions
- Maintains current knowledge of the model's operational status and risk posture
- Required: Completion of Model Ownership Training (SOP-GOV-005) within 30 days of assignment

**AI Governance Committee**
- Chaired by the Chief AI Officer; meets bi-weekly
- Standing members: CAIO, CISO, CPO/DPO, CMO, General Counsel, VP Engineering, Chief Compliance Officer
- Reviews and approves High-Risk and Critical-tier model deployments
- Adjudicates model-related risk exceptions and policy waivers
- Reviews quarterly model monitoring reports and adverse incident summaries

**Chief AI Officer (Dr. Marcus Rivera)**
- Executive owner of the Model Development Lifecycle SOP
- Final approval authority for Critical-tier model deployments
- Reports model risk posture to the Board of Directors quarterly
- Maintains the enterprise Model Inventory and publishes quarterly governance reports

**Chief Medical Officer (Dr. Priya Patel)**
- Reviews and validates clinical appropriateness of models impacting patient care
- Defines clinical safety thresholds for Clinical AI Platform models
- Approves clinical model output format and presentation to clinicians
- Consults on model decommissioning impact to clinical workflows

**Chief Information Security Officer (Rachel Kim)**
- Conducts security architecture review for all production-bound models
- Defines model access controls, API security requirements, and data protection standards
- Approves model container images and dependency security scans
- Monitors model endpoints for security anomalies

**Chief Privacy Officer / DPO (Dr. Klaus Weber)**
- Reviews all models processing personal data for privacy compliance
- Approves data minimization strategies and retention schedules
- Ensures Data Protection Impact Assessments are completed where required
- Advises on GDPR compliance for models processing EU data subject information

---

## 4. Policy Statements

### 4.1 Foundational Policy Commitments

Meridian Health Technologies, Inc. is committed to developing and deploying AI/ML systems that are safe, effective, fair, transparent, and aligned with our ethical obligations to patients, providers, and partners. The following policy statements establish the non-negotiable requirements that govern all model development activities:

**PS-1: Human-Centered Design**
All models shall be developed with explicit consideration of the humans who will use, be affected by, or oversee the system. Problem formulation must include consultation with domain experts, end-users, and, where feasible, patient representatives. This aligns with NIST AI RMF Govern 1.1 and Map 1.1-1.3.

**PS-2: Risk-Proportional Governance**
The intensity of governance controls applied to each model shall be proportional to the model's Risk Tier classification. Higher-risk models require more extensive testing, documentation, independent review, and approval authority levels. Risk Tier assignments shall be made using the standardized methodology defined in Procedure P-01.

**PS-3: Fairness and Non-Discrimination**
All models shall undergo mandatory fairness and bias testing prior to production deployment. No model shall be deployed if it demonstrates statistically significant adverse impact against protected groups unless a documented, approved business necessity justification has been reviewed and accepted by the AI Governance Committee. This implements NIST AI RMF Map 2.3 and Measure 2.11.

**PS-4: Transparency and Explainability**
Model decisions that affect individuals shall be explainable in plain language appropriate to the recipient. Model Cards shall be created for all production models and made available to internal stakeholders and, where required by regulation, to external parties. This aligns with NIST AI RMF Govern 5.1-5.2 and Map 1.4.

**PS-5: Security and Privacy by Design**
Model development shall incorporate security and privacy controls from inception through deployment and decommissioning. All models processing PHI or personal data shall undergo a formal Data Protection Impact Assessment. Personal data minimization shall be demonstrated at each approval gate.

**PS-6: Continuous Monitoring and Improvement**
All production models shall be subject to continuous automated monitoring for performance degradation, data drift, concept drift, and fairness metrics drift. Monitoring results shall be reviewed at least monthly by the Model Owner and quarterly by the AI Governance Committee.

**PS-7: Documentation Completeness**
No model shall proceed past any Approval Gate without complete, reviewed documentation as specified in this SOP. Documentation must be maintained in the designated governance repository and linked to the model's entry in the MLflow Model Registry.

**PS-8: Third-Party Model Governance**
Third-party and vendor-supplied models are subject to the same governance requirements as internally developed models. Vendors must provide sufficient documentation, testing results, and access for Meridian to complete required evaluations.

### 4.2 Risk Tier Classification

All models shall be assigned one of the following four risk tiers using the scoring methodology defined in Procedure P-01:

| Risk Tier | Definition | Governance Intensity | Max Models per Approval Batch |
|-----------|-----------|---------------------|-------------------------------|
| **Critical** | Model failure could result in patient death, severe injury, significant financial loss (>$10M), or systemic discrimination affecting >100,000 individuals | Maximum | 1 |
| **High** | Model failure could result in patient harm, moderate financial loss ($1M-$10M), discrimination affecting 1,000-100,000 individuals, or regulatory enforcement action | Mandatory full governance | 1 |
| **Medium** | Model failure could result in inconvenience, minor financial loss (<$1M), or non-material operational disruption | Standard governance | 3 |
| **Low** | Model failure has negligible impact on individuals, finances, or operations | Streamlined governance | 5 |

**Default Risk Tier Assignments:**
- Clinical AI Platform models: Minimum High; Critical if impacting diagnosis or treatment decisions
- HealthPay Financial Services credit/lending models: High
- HealthPay Financial Services fraud detection: Medium
- MedInsight Analytics population health models: High
- SaaS Platform infrastructure models: Low

---

## 5. Detailed Procedures

### 5.1 Model Development Lifecycle Overview

The Meridian Model Development Lifecycle consists of seven sequential phases with five mandatory Approval Gates. Each phase produces specified artifacts that must be completed, reviewed, and stored in the designated governance repository before the model may proceed through the corresponding gate.

**Lifecycle Phases and Gates:**

```
Phase 1: Problem Formulation → Phase 2: Data Preparation → Gate 1: Data & Problem Approval
Phase 3: Model Development → Phase 4: Testing & Evaluation → Gate 2: Technical Review
→ Gate 3: Responsible AI Review → Phase 5: Pre-Production → Gate 4: Security & Privacy Review
→ Phase 6: Production Deployment → Gate 5: Production Approval → Phase 7: Monitoring & Maintenance
```

### 5.2 Phase 1: Problem Formulation and Feasibility Assessment

**Duration:** Target 2-4 weeks (Critical/High models); 1-2 weeks (Medium/Low models)

**Procedure P-01: Problem Formulation**

**Step 1.1: Business Case Development**
The Model Owner, in collaboration with business stakeholders, shall complete the Model Initiation Document (MID) using Form F-01-MID (found in the Governance SharePoint repository). The MID must include:

a) **Business Problem Statement**: Clear articulation of the problem to be solved, including clinical, financial, or operational context
b) **Target Population**: Description of the population(s) affected by or subject to model decisions, including demographic characteristics, geographic scope, and estimated population size
c) **Intended Use Case**: Precise description of how model outputs will be used, including decision-making workflows, human interaction points, and downstream systems
d) **Success Criteria**: Quantifiable business and technical success metrics with minimum acceptable thresholds
e) **Current State Baseline**: Description of existing process or system, including performance metrics for comparison
f) **Resource Estimate**: Estimated compute, data, personnel, and timeline requirements
g) **Initial Risk Factors**: Preliminary identification of potential harms, failure modes, and stakeholder concerns

**Step 1.2: Regulatory Classification Determination**
The Model Owner shall consult with the Compliance Officer to determine applicable regulatory classifications:

a) **EU AI Act Classification**: Determine if the model qualifies as a high-risk AI system under Annex III. Document classification rationale.
b) **FDA/Medical Device Determination**: For Clinical AI Platform models, consult with the Clinical Regulatory Affairs team to determine if FDA 510(k) clearance or CE marking under EU MDR is required.
c) **SR 11-7 Applicability**: For HealthPay models, determine if the model falls within scope of model risk management requirements.

**Step 1.3: Risk Tier Calculation**
Using the Risk Tier Scoring Matrix (Form F-02-RTS), the Model Owner shall calculate the initial Risk Tier:

**Scoring Dimensions (each scored 1-5):**

| Dimension | Weight | Scoring Criteria |
|-----------|--------|------------------|
| Harm Severity | 40% | 1=Negligible inconvenience; 3=Moderate harm treatable with intervention; 5=Irreversible catastrophic harm or death |
| Scale of Impact | 25% | 1=<100 individuals; 3=1,000-100,000 individuals; 5=>1,000,000 individuals |
| Decision Autonomy | 20% | 1=Purely advisory with strong human override; 3=Recommender with optional override; 5=Fully automated without human intervention |
| Reversibility | 10% | 1=Fully reversible instantly; 3=Reversible with moderate effort/cost; 5=Irreversible |
| Data Sensitivity | 5% | 1=Public/non-personal; 3=Personal data; 5=Special category data (health, biometric) |

**Risk Tier Thresholds:**
- Weighted score ≥ 4.0: **Critical**
- Weighted score 3.0-3.9: **High**
- Weighted score 2.0-2.9: **Medium**
- Weighted score < 2.0: **Low**

**Step 1.4: Stakeholder Identification**
The Model Owner shall identify and document:
- Primary users and their training requirements
- Affected stakeholders (including patients, providers, payers)
- Required reviewers for each Approval Gate
- External dependencies and integration teams

**Step 1.5: Feasibility Go/No-Go**
The Model Owner presents the MID and Risk Tier calculation to the CAIO for Feasibility Assessment review. The CAIO, in consultation with the CMO (for clinical models) or CFO (for financial models), makes a Go/No-Go determination within 5 business days.

**Gate 0: Feasibility Approval (applicable to Critical and High tiers only)**
- Medium and Low tier models proceed directly to Phase 2 upon Model Owner approval
- Critical and High tier models require CAIO approval before resource allocation

### 5.3 Phase 2: Data Acquisition and Preparation

**Duration:** Target 2-8 weeks depending on data complexity

**Procedure P-02: Data Governance and Preparation**

**Step 2.1: Data Source Identification and Approval**
The Model Developer shall document all data sources using Form F-03-DS (Data Source Declaration):

a) **Internal Data Sources**: Snowflake databases, data lakes, data warehouses, operational systems
b) **External Data Sources**: Third-party data providers, public datasets, partner data
c) **Synthetic Data**: Any synthetic data generation methods, including validation of statistical fidelity
d) **Data Provenance**: For each source, document origin, collection methodology, consent basis, and any usage restrictions

**Step 2.2: Data Protection Impact Assessment**
For models processing personal data (including PHI), the CPO/DPO shall complete or approve a Data Protection Impact Assessment (DPIA) using Form F-04-DPIA prior to data access being granted. The DPIA must address:

a) Purpose and necessity of data processing
b) Data minimization assessment (is each data element necessary?)
c) Privacy risks to data subjects
d) Mitigation measures implemented
e) Retention periods and anonymization strategies

**Step 2.3: Data Quality Assessment**
The Model Developer shall perform and document a Data Quality Assessment including:

a) **Completeness**: Percentage of missing values per feature; handling strategy for missing data
b) **Accuracy**: Validation against source systems; identification of known data quality issues
c) **Consistency**: Cross-field validation rules; temporal consistency checks
d) **Representativeness**: Comparison of dataset demographics to target population demographics
e) **Temporal Relevance**: Age of data; recency relative to current conditions

**Quantitative Thresholds:**
- Missing value rate >20% on any critical feature: Requires documented justification and mitigation
- Population representativeness deviation >15% on any protected demographic dimension: Requires bias mitigation plan

**Step 2.4: Data Labeling Procedures**
For supervised learning models, the Model Developer shall document labeling methodology:

a) **Label Source**: Human annotation, system logs, clinical outcomes, claims data, etc.
b) **Labeler Qualifications**: For human-labeled data, qualifications of annotators
c) **Inter-Rater Reliability**: Cohen's Kappa or equivalent metric; minimum threshold of 0.7 required
d) **Label Quality Audit**: Plan for ongoing label quality verification

**Step 2.5: Feature Engineering Documentation**
All features shall be documented in the Feature Registry (maintained in MLflow) with:

a) Feature name, description, and data type
b) Source data and transformation logic
c) Business or clinical rationale for inclusion
d) Known correlations with protected attributes (race, ethnicity, gender, age, disability status)
e) Missing value treatment methodology

**Step 2.6: Data Splitting Strategy**
The Model Developer shall define and document:

a) **Split Methodology**: Temporal, stratified, group-aware, or random splitting
b) **Split Ratios**: Train/Validation/Test proportions with justification
c) **Stratification Variables**: Variables used to ensure representative distributions
d) **Leakage Prevention**: Measures taken to prevent data leakage between splits

**Gate 1: Data and Problem Approval**

**Required Artifacts (stored in Governance SharePoint and referenced in MLflow):**
1. Model Initiation Document (F-01-MID) — Final version
2. Risk Tier Scoring Matrix (F-02-RTS) — Approved
3. Data Source Declaration (F-03-DS) — For all sources
4. Data Protection Impact Assessment (F-04-DPIA) — If applicable
5. Data Quality Assessment Report
6. Feature Registry Entries

**Approval Authorities:**
- Critical/High tier: CAIO + CPO/DPO
- Medium tier: Model Owner + Data Governance Lead
- Low tier: Model Owner only

### 5.4 Phase 3: Model Development

**Duration:** Target 4-12 weeks

**Procedure P-03: Model Training and Selection**

**Step 3.1: Development Environment**
All model development shall occur within Meridian's governed ML infrastructure:

a) **Primary Environment**: AWS SageMaker within the Meridian ML VPC (us-east-1 or eu-west-1)
b) **Experiment Tracking**: All experiments logged in MLflow with immutable run IDs
c) **Code Repository**: GitHub Enterprise with branch protection rules; all code must undergo peer review
d) **Data Access**: PHI-accessible environments require PAM elevation via Okta + HashiCorp Vault

**Step 3.2: Baseline Model Establishment**
The Model Developer shall establish a baseline model (simple heuristic, rule-based system, or simple ML model) against which more complex models will be compared. The baseline must be documented in the Technical Specification Document.

**Step 3.3: Model Selection and Experimentation**
The Model Developer shall:

a) Define candidate model architectures with justification for each
b) Document hyperparameter search strategy (grid search, Bayesian optimization, etc.)
c) Log all experiments with hyperparameters, metrics, and artifacts to MLflow
d) Maintain an experiment log with timestamp, rationale, and outcome for each experiment
e) For foundation model fine-tuning: Document base model selection criteria, fine-tuning dataset, adapter method, and compute requirements

**Step 3.4: Training Governance**
For all training runs intended as candidates for production:

a) **Random Seed Documentation**: All random seeds must be set and documented for reproducibility
b) **Compute Utilization**: Track and log compute resource consumption for environmental impact reporting
c) **Training Data Version**: Pin training data version using DVC (Data Version Control) or Snowflake time-travel
d) **Model Checkpointing**: Save model checkpoints at regular intervals with validation metrics

**Step 3.5: Environmental Impact Statement**
For models trained on >100 GPU-hours, the Model Developer shall complete an Environmental Impact Statement documenting:

a) Estimated carbon emissions (using AWS Customer Carbon Footprint Tool or equivalent)
b) Justification of compute requirements relative to model benefits
c) Consideration of more efficient alternatives

**Step 3.6: Model Packaging**
Model packages must follow Meridian standardization:

a) **Container Format**: Docker container with approved base image (see SOC-SEC-015)
b) **Model Serialization**: Standardized format (ONNX, PyTorch JIT, TensorFlow SavedModel)
c) **Inference Code**: Include preprocessing, inference, and postprocessing logic
d) **Dependency Manifest**: Complete list of dependencies with pinned versions
e) **Model Signature**: Input/output schema defined in MLflow model signature

### 5.5 Phase 4: Testing and Evaluation

**Duration:** Target 3-6 weeks

**Procedure P-04: Model Testing Framework**

**Step 4.1: Technical Performance Evaluation**
The Model Developer shall evaluate model performance using a comprehensive test suite:

**Classification Models Metrics (minimum):**

| Metric | Required For | Minimum Threshold |
|--------|--------------|-------------------|
| AUROC | All classifiers | ≥0.70 (critical/high: ≥0.80) |
| Precision (PPV) | All classifiers | ≥0.50 at operating point |
| Recall (Sensitivity) | All classifiers | ≥0.50 at operating point |
| F1 Score | Imbalanced datasets | ≥0.60 |
| Calibration Error (ECE) | All classifiers | ≤0.10 |
| Negative Predictive Value | Clinical models | Report required |

**Regression Models Metrics (minimum):**

| Metric | Required For | Threshold |
|--------|--------------|-----------|
| MAE | All regression | Context-dependent |
| RMSE | All regression | Context-dependent |
| R-squared | All regression | Report required |
| Mean Absolute Percentage Error | Financial models | ≤15% |

**Step 4.2: Fairness and Bias Testing**
All models shall undergo mandatory fairness testing per the Meridian Fairness Testing Framework (SOP-QUA-002) using the following procedure:

**a) Protected Attribute Identification**
Identify all protected attributes present in or inferable from the dataset, including proxy variables:
- Race and ethnicity
- Gender identity and sex
- Age (especially for clinical models)
- Disability status
- Socioeconomic indicators (zip code, income proxies)
- Primary language
- Geographic location (rural/urban disparities)

**b) Subgroup Analysis**
Compute performance metrics for each protected subgroup individually. Document any subgroup with sample size <100 as "insufficient data for reliable assessment."

**c) Disparity Metrics Calculation**
Calculate the following disparity metrics:

| Disparity Metric | Formula | Acceptable Threshold |
|------------------|---------|----------------------|
| Demographic Parity Difference | \|P(positive \| group A) - P(positive \| group B)\| | ≤0.10 |
| Equalized Odds Difference | Max of TPR and FPR differences across groups | ≤0.10 |
| Disparate Impact Ratio | P(positive \| group A) / P(positive \| group B) | ≥0.80 and ≤1.25 |

**d) Bias Mitigation**
If any disparity metric exceeds acceptable thresholds:
1. Document the finding in the Bias Assessment Report
2. Implement bias mitigation techniques (reweighting, resampling, adversarial debiasing, post-processing adjustment)
3. Re-evaluate after mitigation
4. If disparities persist, escalate to AI Governance Committee for determination

**Step 4.3: Robustness and Stress Testing**

**a) Input Perturbation Testing**
Evaluate model stability by introducing controlled perturbations to input data:
- Gaussian noise at multiple standard deviations (0.01σ, 0.05σ, 0.10σ)
- Missing feature simulation (random feature dropout at 5%, 10%, 20%)
- Boundary value testing at feature distribution extremes
- Adversarial example testing for neural network models

**b) Subpopulation Shift Testing**
Evaluate model performance on subsets of the test data representing plausible deployment distribution shifts:
- Temporal subsets (most recent period)
- Demographic subsets
- Clinical severity subsets

**Step 4.4: Explainability Assessment**
All models classified as Critical or High Risk Tier must undergo formal explainability assessment:

**a) Global Explainability**: Feature importance using SHAP values, permutation importance, or model-appropriate methods. Top 20 features must be documented in the Model Card.

**b) Local Explainability**: For models making decisions affecting individuals, individual prediction explanations must be available using LIME, SHAP, or integrated gradients.

**c) Clinical Plausibility Review**: For Clinical AI Platform models, a board-certified physician from the Clinical AI Products team shall review feature importance rankings and individual explanations for clinical plausibility. Any clinically implausible features must be investigated and resolved.

**Step 4.5: Comparative Evaluation**
Compare model performance against:
a) The established baseline model
b) The current production model (if applicable)
c) Any vendor-supplied benchmark models

**Gate 2: Technical Review**

**Required Artifacts:**
1. Technical Specification Document (Form F-05-TSD)
2. Model Evaluation Report with all metrics
3. Bias Assessment Report (Form F-06-BAR)
4. Explainability Report (Critical/High only)
5. Robustness Testing Results
6. MLflow Experiment Registry with all experiment runs

**Review Panel:**
- Critical/High: Senior ML Engineer (not on development team) + Clinical reviewer (if applicable)
- Medium: Peer ML Engineer review
- Low: Self-assessment with documented checklist

**Approval Criteria:**
- All quantitative thresholds met or documented exceptions approved
- Fairness metrics within acceptable thresholds
- Explainability analysis completed
- Code review completed with no critical findings unresolved

### 5.6 Pre-Production Phase

**Duration:** Target 2-4 weeks

**Procedure P-05: Responsible AI Review and Pre-Production Preparation**

**5.6.1 Gate 3: Responsible AI Review (RAIR)**

The Responsible AI Review is a mandatory cross-functional governance review applicable to all Critical and High tier models, and required by policy for Medium tier models processing PHI or making decisions about individuals.

**RAIR Panel Composition:**

| Role | Required For |
|------|--------------|
| AI Ethics Lead (Chair) | All RAIRs |
| CAIO or delegate | All RAIRs |
| CPO/DPO or delegate | Models processing personal data |
| CISO or delegate | All RAIRs |
| CMO or clinical delegate | Clinical models |
| General Counsel or delegate | All RAIRs |
| Model Owner | All RAIRs |
| Independent Reviewer (external to project) | Critical tier |

**RAIR Assessment Domains (aligned with NIST AI RMF Govern categories):**

**Domain 1: Beneficial Use and Value Alignment**
- Does the model align with Meridian's mission and ethical principles?
- Have potential dual-use concerns been identified and addressed?
- Is the intended use case clearly specified with boundaries?

**Domain 2: Fairness and Equity**
- Have fairness metrics been adequately evaluated across all relevant subgroups?
- Do any disparities remain, and if so, is the business justification documented?
- Have affected communities been considered in the impact assessment?

**Domain 3: Transparency and Explainability**
- Is the Model Card complete and accurate?
- Are explanations available at appropriate levels for different stakeholders?
- Have limitations been clearly communicated?

**Domain 4: Accountability and Oversight**
- Are roles and responsibilities clearly defined for all lifecycle phases?
- Is there a clear escalation path for concerns?
- Is the monitoring plan sufficient?

**Domain 5: Privacy and Data Protection**
- Has data minimization been demonstrated?
- Are consent mechanisms appropriate?
- Are retention and deletion procedures defined?

**Domain 6: Safety and Robustness**
- Have failure modes been systematically identified and assessed?
- Are safeguards proportional to the risk tier?
- Is the model resilient to edge cases and adversarial inputs?

**RAIR Outcome and Voting:**
Each domain is scored by the panel on a scale of 1-5:
- 5: Exemplary; exceeds requirements
- 4: Meets all requirements
- 3: Meets minimum requirements with minor concerns
- 2: Significant concerns requiring remediation
- 1: Unacceptable; do not proceed

**RAIR Decision Rules:**
- Any domain score of 1: Model rejected; cannot proceed without fundamental redesign
- Any domain score of 2: Conditional approval with mandatory remediation plan and timeline
- All domains ≥3 : Approved to proceed
- Average score ≥4: Approved with commendation

The RAIR outcome and domain scores are documented in Form F-07-RAIR and stored in the model's governance record.

**5.6.2 Shadow Deployment**

For Critical and High tier models, a shadow deployment phase of minimum duration is required:

| Risk Tier | Minimum Shadow Duration | Minimum Inference Volume |
|-----------|------------------------|--------------------------|
| Critical | 30 days | 10,000 inferences |
| High | 14 days | 5,000 inferences |
| Medium | Recommended but not required | N/A |

During shadow deployment:
a) Model processes production data but outputs are not used in decision-making
b) Performance metrics are collected and compared against production model
c) Data drift metrics are monitored in real-time
d) At completion, Shadow Deployment Evaluation Report (Form F-08-SER) is generated

**5.6.3 Gate 4: Security and Privacy Review**

**Required Activities:**
a) **Container Security Scan**: All model containers scanned with CrowdStrike Falcon; zero critical or high vulnerabilities allowed
b) **Dependency Audit**: All dependencies reviewed; known vulnerabilities must be patched or risk-accepted by CISO
c) **API Security Review**: Model inference API reviewed for authentication, authorization, rate limiting, input validation
d) **Data Flow Analysis**: End-to-end data flow documented and reviewed for PHI/PII exposure
e) **Access Control Verification**: Principle of least privilege verified; all access justified and time-bound
f) **DPIA Verification**: CPO/DPO verifies DPIA recommendations have been implemented

**Approval Authority**: CISO (security) + CPO/DPO (privacy)

### 5.7 Phase 6: Production Deployment

**Procedure P-06: Production Deployment**

**5.7.1 Deployment Strategy Selection**
The Model Owner, in consultation with the VP of Engineering, shall select and document the deployment strategy:

| Strategy | Description | Required For |
|----------|-------------|--------------|
| Canary Deployment | Gradual traffic shifting (5% → 25% → 50% → 100%) with monitoring gates | Critical tier |
| Blue-Green Deployment | Parallel environments with instant cutover | High tier |
| Rolling Deployment | Incremental instance replacement | Medium tier |
| Direct Deployment | Direct replacement of existing model | Low tier |

**5.7.2 Deployment Checklist (Form F-09-DLC)**
Prior to deployment, the following must be verified and documented:

- [ ] All previous gate approvals obtained and documented
- [ ] Model serialized and versioned in MLflow Model Registry: `models:/[model_name]/[version]`
- [ ] Model container image built and tagged: `meridian-ml/[model_name]:[version]`
- [ ] Container image passed security scan
- [ ] Inference endpoint configured with appropriate instance type and auto-scaling
- [ ] Monitoring instrumentation enabled (performance, drift, fairness)
- [ ] Logging configured with appropriate retention policy
- [ ] Alerting thresholds configured in Datadog
- [ ] Rollback plan documented and tested
- [ ] On-call rotation updated to include model support
- [ ] Runbook created with troubleshooting procedures
- [ ] Model Card published to internal Model Catalog
- [ ] Stakeholders notified of deployment schedule

**5.7.3 Gate 5: Production Approval**

**Approval Authorities by Tier:**

| Risk Tier | Approver | Additional Sign-off |
|-----------|----------|---------------------|
| Critical | CAIO | CMO (clinical) or CFO (financial) |
| High | CAIO | None |
| Medium | VP of Engineering or delegate | None |
| Low | Model Owner | None |

**Production Go-Live Protocol:**
1. Model Developer initiates deployment according to selected strategy
2. For initial traffic (canary phase), monitor all metrics for minimum 2 hours before traffic increase
3. At each traffic increment gate, verify all metrics within expected ranges
4. If any alert fires during deployment, halt traffic increase and investigate
5. Upon reaching full traffic, Model Owner sends deployment confirmation notification

### 5.8 Phase 7: Monitoring and Maintenance

**Procedure P-07: Continuous Monitoring**

**5.8.1 Monitoring Infrastructure**
All production models are monitored through the centralized Meridian Model Monitoring Platform (Datadog + MLflow integration with LangSmith for AI tracing). Monitoring dashboards are configured automatically upon model registration.

**5.8.2 Model Performance Monitoring**
The following metrics are monitored continuously with automated alerting:

| Metric Category | Specific Metrics | Monitoring Frequency | Alert Threshold |
|-----------------|------------------|---------------------|-----------------|
| Model Performance | Accuracy, AUROC, F1, MAE, etc. (model-specific) | Per inference batch; aggregated hourly | 10% degradation from deployment baseline |
| Data Drift | PSI, KS statistic, Jensen-Shannon distance per feature | Daily | PSI > 0.25 on top 10 features |
| Concept Drift | Proxy metrics (e.g., outcome rate changes) | Daily | 15% change from baseline |
| Prediction Distribution | Mean, variance, quantile distribution | Hourly | 3σ deviation from 30-day rolling baseline |
| Fairness Metrics Drift | Disparate impact, equal opportunity difference | Weekly | Any metric crossing acceptable threshold |
| Infrastructure | Latency (p50, p95, p99), throughput, error rate | Real-time | Latency p99 > 2x SLA; error rate > 0.5% |
| Data Quality | Null rate, schema violations, range violations | Per batch | Any change from deployment baseline |

**5.8.3 Alert Response Protocol**

**Alert Severity Levels:**

| Severity | Definition | Response Time | Escalation |
|----------|-----------|---------------|------------|
| P1 - Critical | Model producing harmful or dangerous outputs; security incident; PHI exposure | 15 minutes | PagerDuty → On-call ML Engineer → CAIO |
| P2 - High | Performance degradation exceeding threshold; fairness metric violation | 2 hours | PagerDuty → On-call ML Engineer → Model Owner |
| P3 - Medium | Drift detected; non-critical metric degradation | 24 hours | Jira ticket assignment |
| P4 - Low | Informational anomalies; investigation recommended | 5 business days | Dashboard annotation |

**5.8.4 Periodic Model Retraining**

**Retraining Triggers:**
Models shall be evaluated for retraining based on:
a) **Scheduled Retraining**: Per the schedule defined in the Model Card (minimum: quarterly for Critical/High; semi-annually for Medium)
b) **Triggered Retraining**: When automated monitoring detects sustained degradation
c) **Ad-hoc Retraining**: When the Model Owner identifies need due to changed conditions

**Retraining Procedure:**
1. Initiate Retraining Request (Form F-10-RTR)
2. If retraining scope is limited to data refresh (same features, architecture, hyperparameters):
   - Follow streamlined re-validation path
   - Requires Gate 2 Technical Review only
3. If retraining involves model architecture changes, feature changes, or hyperparameter re-tuning:
   - Full governance path from Phase 3
4. Retrained model must beat current production model on test sets before deployment
5. Side-by-side comparison report required

**5.8.5 Quarterly Model Review**
Each production model shall undergo a formal quarterly review led by the Model Owner:

**Review Topics:**
a) Performance metrics trending over quarter
b) Drift analysis findings and trends
c) Fairness metrics over time
d) Incident summary (alerts, investigations, resolutions)
e) Usage statistics and business impact
f) Compute cost and environmental impact
g) Recommendation: Continue, Retrain, Retire, or Reassess Risk Tier

**Quarterly Review Report** (Form F-11-QRR) is submitted to the AI Governance Committee for Critical and High tier models.

**5.8.6 Model Decommissioning**
Models shall be decommissioned when:
a) Model performance cannot be restored to acceptable levels
b) Business need has ended
c) Model is replaced by a superior alternative
d) Regulatory requirements necessitate retirement

**Decommissioning Procedure:**
1. Model Owner submits Decommissioning Request (Form F-12-DR)
2. Impact assessment: downstream systems, dependent processes, data retention requirements
3. Decommissioning plan: data archival, model artifact archival, communication plan
4. Approval by original production approval authority
5. Implementation: traffic cessation, infrastructure teardown, archival
6. Model status updated to "Decommissioned" in MLflow Registry
7. Model Card archived with decommissioning date and rationale

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

**TC-01: Development Environment Isolation**
All model development environments are logically isolated from production environments. PHI-accessible development environments require additional controls:
- Multi-factor authentication via Okta with hardware token option
- Session recording enabled via AWS CloudTrail
- Data exfiltration prevention via CrowdStrike DLP policies
- Just-in-time access provisioning via HashiCorp Vault (4-hour maximum session)

**TC-02: Model Registry Access Control**
The MLflow Model Registry implements role-based access control:
- Model Developers: Read/write for owned models in development
- Model Owners: Read/write for owned models; promote to staging
- AI Governance Committee: Read all models; approve production promotions
- All others: Read-only access based on need-to-know

**TC-03: Model Artifact Integrity**
All model artifacts are immutably stored with cryptographic hashing:
- Model weights SHA-256 hash computed and stored in registry
- Training data version hash recorded
- Container image digest (SHA-256) used for deployment
- Artifact lineage maintained in MLflow for full reproducibility

**TC-04: Automated Testing Pipeline**
A CI/CD pipeline in GitHub Actions enforces:
- Unit tests for preprocessing and inference code (minimum 80% coverage)
- Integration tests for model endpoint
- Automated fairness metric computation
- Automated model card validation (required fields populated)
- Pipeline must pass before merge to main branch

**TC-05: Inference API Authentication**
All model inference endpoints require:
- Mutual TLS for service-to-service communication
- API key + OAuth 2.0 for external clients
- Rate limiting per API key
- Request/response logging for audit trail
- Input validation against model signature schema

**TC-06: Data Protection During Inference**
- PHI in request payloads encrypted in transit (TLS 1.3 minimum)
- Inference logs sanitized: PHI fields redacted or tokenized
- Request payloads not persisted unless explicitly approved for monitoring
- Data retention for inference logs: 30 days default (extended with CPO approval)

### 6.2 Administrative Controls

**AC-01: Segregation of Duties**
The following roles must be held by different individuals for Critical and High tier models:
- Model Developer and Model Approver
- Model Developer and RAIR Panel Chair
- Model Owner and Independent Reviewer

**AC-02: Model Inventory Management**
The CAIO maintains the enterprise Model Inventory as the system of record. The inventory is:
- Reviewed for accuracy quarterly
- Audited against production deployments semi-annually
- Reported to Board of Directors annually
- Includes: model name, version, risk tier, status, owner, last review date, next review date

**AC-03: Vendor Model Governance**
Third-party models are subject to:
- Vendor risk assessment prior to procurement
- Documentation requirements equivalent to internal models
- Contractual right to audit model performance and fairness
- Annual recertification of vendor model compliance
- Inclusion in Model Inventory with vendor designation

**AC-04: Policy Exception Management**
Policy exceptions follow the Exception Handling process defined in Section 8. All exceptions are time-bound (maximum 12 months) and tracked in the Exceptions Register.

**AC-05: Record Retention**
Model governance documentation retention:
- Model Cards: 7 years after decommissioning
- Training data references: 7 years after decommissioning
- Evaluation reports: 7 years after decommissioning
- Approval records: Permanent
- Monitoring logs: 2 years (per SOC 2 requirements)
- Inference audit logs: Per data retention policy (SOP-DATA-007)

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The AI/ML Engineering organization reports the following KPIs to measure model governance effectiveness:

| KPI | Target | Measurement Period | Owner |
|-----|--------|-------------------|-------|
| Model Governance Compliance Rate | ≥95% of models with all required approvals | Quarterly | CAIO |
| Time-to-Approval (Critical/High) | ≤90 days from Phase 1 start to Gate 5 | Quarterly | CAIO |
| Production Model Monitoring Coverage | 100% of production models | Continuous | VP Engineering |
| Alert Response SLA Compliance | P1: 100% within 15 min; P2: 95% within 2 hours | Monthly | VP IT Operations |
| Fairness Metric Violations | Zero sustained violations (resolved within 30 days) | Quarterly | CAIO |
| Model Retraining Timeliness | ≥90% completed within scheduled window | Quarterly | VP Engineering |
| Model Incident Count | Trending downward quarter-over-quarter | Quarterly | AI Governance Committee |
| Bias Assessment Completion | 100% of production models | Quarterly | CAIO |
| Documentation Completeness | ≥98% of required fields in Model Cards | Monthly | AI Governance Committee |

### 7.2 Dashboards and Reporting

**Automated Dashboards (Datadog):**
- **Model Operations Dashboard**: Real-time performance, drift, and infrastructure metrics for all production models
- **Fairness Monitoring Dashboard**: Fairness metrics by model, time, and protected attribute; with alert overlays
- **Governance Compliance Dashboard**: Model lifecycle status, approval gate completion, upcoming reviews, expiring exceptions

**Scheduled Reports:**

| Report | Frequency | Audience | Content |
|--------|-----------|----------|---------|
| Model Operations Summary | Weekly | Model Owners, VP Engineering | Alert summary, performance trends, incident log |
| Quarterly Model Review Report | Quarterly | AI Governance Committee | Per-model review summaries, KPI trends, exception status |
| Board AI Risk Report | Quarterly | Board of Directors | Executive summary, critical risks, regulatory updates, incident highlights |
| Annual Model Governance Report | Annual | Board of Directors, External Auditors | Comprehensive governance assessment, policy effectiveness, improvement recommendations |

### 7.3 Audit and Assurance

**Internal Audits:**
- Model governance process audit: Semi-annual by Internal Audit team
- Artifact completeness spot check: Monthly by AI Governance Committee secretariat
- Access control review: Quarterly by CISO team

**External Audits:**
- SOC 2 Type II: Annual; model governance controls in scope
- HITRUST CSF: Annual; AI/ML controls validated
- ISO 27001:2022: Annual surveillance audit; ML infrastructure controls in scope

---

## 8. Exception Handling and Escalation

### 8.1 Policy Exceptions

**8.1.1 Exception Types**
Exceptions to this SOP may be requested for:
a) **Process Deviation**: Request to skip or modify a lifecycle phase or gate
b) **Threshold Deviation**: Request to deploy a model not meeting quantitative thresholds
c) **Role Exception**: Request to permit role consolidation normally prohibited by segregation of duties
d) **Timeline Exception**: Request to accelerate governance timeline
e) **Documentation Deferral**: Request to defer documentation completion post-deployment (Critical/High models not eligible)

**8.1.2 Exception Request Procedure**
1. Model Owner completes Exception Request Form (Form F-13-ER) including:
   - Exception type and scope
   - Business justification
   - Risk assessment and mitigation
   - Proposed expiration date
   - Alternative controls to be implemented
2. Exception reviewed by CAIO within 3 business days
3. For Critical and High tier models, AI Governance Committee approval required
4. Approved exceptions entered into Exceptions Register
5. Exception expiration tracked; renewal requires new request

**8.1.3 Exception Limits**
- Maximum exception duration: 12 months
- Maximum concurrent exceptions per model: 2
- Exceptions for fairness threshold deviations: Maximum 6 months, must include bias monitoring plan

### 8.2 Escalation Path

**Technical Issues:**
Model Developer → Model Owner → VP Engineering → CAIO

**Risk Concerns:**
Any employee → Model Owner → AI Governance Committee → CAIO → CEO

**Fairness/Ethics Concerns:**
Any employee → AI Ethics Lead (confidential channel available) → AI Governance Committee → Chief Compliance Officer → Board AI Ethics Subcommittee

**Urgent Production Incidents:**
Per PagerDuty escalation policy (SOP-ITOPS-012)

---

## 9. Training Requirements

### 9.1 Required Training Programs

| Training Module | Required For | Frequency | Delivery Method | Tracking |
|-----------------|--------------|-----------|-----------------|----------|
| SOP-AIML-001 Awareness Training | All AI/ML Engineering, Data Science, and ML Operations personnel | Upon hire; annually thereafter | LMS (Workday Learning) | HRIS completion records |
| Model Ownership Training (SOP-GOV-005) | All Model Owners | Before assuming Model Owner role; biennially | Instructor-led (virtual) | AI Governance Committee records |
| Fairness and Bias in AI | All Model Developers | Annually | LMS + Workshop | HRIS completion records |
| Responsible AI Principles | All employees involved in model lifecycle | Upon hire | LMS | HRIS completion records |
| Clinical AI Safety (for clinical models) | Model Developers and Owners of clinical models | Annually | CMO-led workshop | CMO office records |

### 9.2 Training Compliance
- Training completion rate of ≥95% required organizationally; tracked quarterly
- Individuals with overdue training lose model development access until training completed
- Training effectiveness assessed through post-training assessments; pass rate ≥80% required

---

## 10. Related Policies and References

### 10.1 Internal Policies and SOPs

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| SOP-GOV-001 | AI Governance Framework | Parent governance policy |
| SOP-GOV-005 | Model Ownership and Accountability | Defines Model Owner responsibilities |
| SOP-QUA-002 | Fairness Testing Framework | Detailed bias and fairness testing procedures |
| SOP-SEC-015 | ML Infrastructure Security Standards | Container security, access control standards |
| SOP-DATA-007 | Data Retention and Disposal Policy | Inference log retention requirements |
| SOP-PRI-003 | Data Protection Impact Assessment | DPIA procedure and templates |
| SOP-CLIN-008 | Clinical AI Validation Requirements | Clinical model validation standards |
| SOP-FIN-012 | Financial Model Risk Management | HealthPay-specific model controls |
| SOP-ITOPS-012 | Incident Response and Escalation | Production incident handling |
| SOP-VEND-004 | Third-Party AI Procurement | Vendor model governance |

### 10.2 External Standards and Frameworks

| Standard | Reference |
|----------|-----------|
| NIST AI Risk Management Framework 1.0 | Govern, Map, Measure, Manage functions |
| NIST SP 800-53 Rev. 5 | Security and privacy controls for information systems |
| ISO/IEC 42001:2023 | AI Management System |
| ISO/IEC 23894:2023 | AI Risk Management |
| HITRUST CSF v11 | Information risk management framework |
| SOC 2 TSC 2017 | Trust Services Criteria (Security, Availability, Confidentiality) |

---

## 11. Revision History

| Version | Date | Author | Changes | Approver |
|---------|------|--------|---------|----------|
| 1.0 | 2022-03-15 | Dr. Sarah Chen (initial CAIO) | Initial creation; established baseline MDLC | Dr. Sarah Chen |
| 1.1 | 2023-01-20 | Dr. Marcus Rivera | Added Risk Tier classification matrix; introduced RAIR process; updated NIST AI RMF references | Dr. Marcus Rivera |
| 1.2 | 2023-08-10 | Dr. Marcus Rivera | Expanded fairness testing requirements; added Environmental Impact Statement for large models; incorporated HITRUST CSF alignment | David Park |
| 2.0 | 2024-05-08 | Dr. Marcus Rivera | Major revision: Foundation model provisions, shadow deployment requirements, expanded monitoring framework, new templates and forms, updated role definitions, alignment with NIST AI RMF 1.0 Govern/Map/Measure/Manage structure | David Park |
| 2.1 | 2025-12-21 | AI Governance Committee Secretariat | Annual review: Updated alert thresholds based on operational data; added LLM-specific evaluation criteria; revised RAIR domain scoring; added P4 severity level for alerts; updated KPI targets; incorporated lessons learned from 2025 production incidents | Dr. Marcus Rivera |

---

**Document Classification: Internal**
**Distribution: All AI/ML Engineering, AI Governance Committee, Model Owners**
**© 2024-2025 Meridian Health Technologies, Inc. All rights reserved.**

*This document contains proprietary information of Meridian Health Technologies, Inc. Reproduction, distribution, or disclosure without prior written consent is prohibited. This document is uncontrolled when printed. Refer to the Meridian Policy Portal for the current approved version.*