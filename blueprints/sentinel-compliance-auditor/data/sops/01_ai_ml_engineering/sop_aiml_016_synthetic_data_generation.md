---
sop_id: "SOP-AIML-016"
title: "Synthetic Data Generation"
business_unit: "AI/ML Engineering"
version: "5.5"
effective_date: "2025-11-12"
last_reviewed: "2026-03-09"
next_review: "2026-09-05"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
  - "NIST AI RMF"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide governance framework for the generation, validation, and consumption of synthetic data within Meridian Healthcare AI. Synthetic data presents a critical capability for accelerating model development, enhancing privacy-preserving data sharing, and mitigating the risk associated with processing regulated personal data. The purpose of this SOP is to ensure that synthetic data generation (SDG) activities are conducted in a manner that demonstrably preserves the statistical utility of the source data while rigorously preventing the re-identification of natural persons, thereby operationalizing the principles of "Data Protection by Design and Default" as mandated across our regulatory landscape.

### 1.2 Scope

This SOP applies to all business units, engineering teams, data science pods, contractors, and third-party data processors engaged in the generation, provisioning, or use of synthetic data derived from datasets managed or processed by Meridian. The scope covers the entire synthetic data lifecycle: source data selection, generator training and tuning, synthetic data output validation, post-generation privacy evaluation, use case approval, and secure disposal.

Specifically, this SOP governs synthetic data derived from:
- **Health Data:** Clinical trial datasets, electronic health records (EHR), medical imaging metadata, and genomic data processed by Meridian platforms.
- **Personal Data:** Directly identifying or quasi-identifying information related to patients, healthcare providers, research subjects, and Meridian employees.
- **Financial and Operational Data:** Transactional data from Meridian’s commercial operations where individuals are identifiable.
- **Meridian Clinical AI Products:** Training, testing, and validation data sourced from products with CE marking under EU MDR.

This SOP is binding upon all personnel with access to Meridian production, staging, and research data environments, including, but not limited to, the AI/ML Engineering, Clinical Informatics, Data Platform, and Data Science divisions.

### 1.3 Applicability

| **Activity**                     | **Covered by this SOP** | **Governing Principle**                |
| -------------------------------- | ----------------------- | -------------------------------------- |
| Training a GAN on patient EHR    | Yes                     | Privacy Preservation, Utility          |
| Generating digital twins for QA  | Yes                     | Re-identification Risk Mitigation      |
| Sharing synthetic data with R&D  | Yes                     | Use Case Approval, Access Control      |
| Augmenting a rare disease cohort | Yes                     | Data Quality, Fairness (Statistical)   |
| Synthetic data derived from DICOM images | Yes             | Multi-modal Privacy Evaluation         |

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| **Term**                        | **Definition**                                                                                                                                                                                                                                                             |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Synthetic Data**              | Artificially generated data derived from a generative model trained on a real-world source dataset. It replicates the statistical properties, distributions, and correlations of the original data without containing a one-to-one mapping to specific real-world individuals. |
| **Source Data**                 | The real-world, raw dataset upon which the Generative Model is trained. Source Data will contain Personal Data and Protected Health Information (PHI) in its original state.                                                                                                  |
| **Generative Model**            | The specific AI/ML algorithm (e.g., CTGAN, TVAE, Synthpop, GANBLR) used to create Synthetic Data. The model, including its weights and biases, is itself considered a derivative artifact derived from the Source Data.                                                     |
| **Privacy Budget (ε - Epsilon)** | A formal, mathematical measure of the privacy loss associated with the release of data from a differentially private (DP) mechanism. A lower epsilon value indicates stronger privacy guarantees, representing the parameter that is calibrated to meet the defined risk threshold. |
| **Re-identification Attack**    | An attempt by an adversary to link records in a synthetic dataset back to a specific, identified or identifiable natural person in the source data. This includes, but is not limited to, membership inference, attribute inference, and linkage attacks.                     |
| **Singling Out**                | The ability to isolate the synthetic record of an individual, proving that the synthetic output has memorized traits from a single source record.                                                                                                                               |
| **Linkability**                 | The ability to link at least two records concerning the same individual across two different datasets (e.g., linking a synthetic dataset release with a previously released synthetic dataset).                                                                                  |
| **Inference**                   | The ability to deduce, with significant probability, an unknown attribute of an individual from known attributes in the synthetic dataset.                                                                                                                                     |
| **Statistical Utility Score**   | A quantitative metric measuring the degree to which the statistical properties (e.g., correlations, distributions, cardinality) of the Source Data are preserved in the Synthetic Data. Measured on a scale of 0 (no utility) to 1.0 (identical to source).                      |
| **Tier 1-3 Synthetic Data**     | Meridian’s internal risk classification. **Tier 1:** Public, non-sensitive aggregate statistics. **Tier 2:** Structured, person-level synthetic data for internal research and non-prod development. **Tier 3:** Highly sensitive synthetic data reflecting rare diseases where outlier risk is high, requiring Executive approval.          |

### 2.2 Acronyms

| **Acronym** | **Definition**                                    |
| ----------- | ------------------------------------------------- |
| **SDG**     | Synthetic Data Generation                        |
| **GAN**     | Generative Adversarial Network                   |
| **DP**      | Differential Privacy                             |
| **PIA**     | Privacy Impact Assessment                        |
| **PRA**     | Privacy Risk Assessment (synonymous with PIA)    |
| **MLOps**   | Machine Learning Operations                      |
| **DRE**     | Data Risk Evaluation                             |
| **IDMC**    | Independent Data Monitoring Committee            |
| **DSRB**    | Data Stewardship Review Board                    |

---

## 3. Roles and Responsibilities

A RACI (Responsible, Accountable, Consulted, Informed) matrix is established to eliminate ambiguity in the execution of this SOP.

| **Role**                              | **Responsibility**                                                                                                                                                                                                                                      |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Chief AI Officer (CAIO)**           | Owner of this SOP. Ultimate accountability for the governance framework. Approves all Tier 3 Synthetic Data use cases and exceptions. Provides executive sign-off on the privacy budget for regulated product releases.                                  |
| **VP of Engineering (Data & AI)**     | Accountable for the technical implementation, maintenance, and performance of the SDG platform (SynthSphere). Approves Tier 2 use cases. Ensures engineering team compliance with privacy-preserving DevOps (DevPrivOps) processes.                        |
| **Data Stewardship Review Board (DSRB)** | Consults on all use cases. Accountable for defining the statistical utility thresholds and privacy budget (ε) for each approved project. Oversees the quality assurance of source data selection and the approval of Tier 2 use cases.                 |
| **Privacy Engineering Lead**          | Responsible for executing the Privacy Risk Assessment (PRA), defining the technical privacy budget, tuning DP mechanisms, and executing adversarial robustness tests (Membership Inference, Attribute Inference). Signs off on Tier 1 privacy evaluations. |
| **ML Engineer / Data Scientist**      | Responsible for executing the SDG pipeline, tuning generators for maximum utility within the approved privacy budget, generating the statistical utility report, and documenting the entire process in the MLOps catalog.                                |
| **Data Platform Engineering**         | Responsible for implementing role-based access controls (RBAC) to the SDG environment (SynthSphere), maintaining audit logs, and ensuring data lineage tracking from source to synthetic output.                                                           |
| **Legal & Compliance Officer**        | Consulted on the legal basis for processing Source Data. Approves the re-identification risk thresholds. Maintains the legally binding definition of "anonymous data" for Meridian’s jurisdiction scope.                                                 |
| **Business Unit Owner**               | Responsible for submitting a complete Synthetic Data Use Case Request (Form SDG-101). Informed upon approval or denial. Accountable for the secure consumption and final disposal of synthetic data within their approved sandbox.                         |

### 3.1 RACI Matrix

| **Activity**                               | **CAIO** | **VP Eng** | **DSRB** | **Privacy Eng** | **ML Engineer** | **Legal** |
| ------------------------------------------ | -------- | ---------- | -------- | --------------- | --------------- | --------- |
| SDG Platform Architecture Approval         | A        | R          | C        | C               | I               | I         |
| Use Case Approval (Tier 1)                 | I        | A          | C        | R               | C               | C         |
| Use Case Approval (Tier 2)                 | C        | A          | R        | R               | C               | C         |
| Use Case Approval (Tier 3)                 | A        | R          | R        | R               | C               | C         |
| Privacy Budget Calibration                 | I        | C          | A        | R               | C               | I         |
| Synthetic Data Quality Validation          | I        | R          | R        | C               | R               | I         |
| Adversarial Robustness Testing             | I        | C          | I        | R               | A               | I         |

---

## 4. Policy Statements

### 4.1 General Policy

4.1.1 **Privacy by Design:** All Synthetic Data Generation activities must be architected to prevent the singling out, linkability, or inference of any natural person from the synthetic output. The default approach for any SDG project must adopt a formal privacy-preserving mechanism, specifically (ε, δ)-Differential Privacy integrated into the generator’s training loop.

4.1.2 **Utility Preservation:** Meridian’s mission to advance clinical AI requires that Synthetic Data maintains high statistical utility. A trade-off analysis between utility and privacy (ε) must be documented and approved by the DSRB as defined in Section 5.4.

4.1.3 **Purpose Limitation:** Synthetic Data must not be generated for purposes incompatible with the original lawful basis for processing the Source Data. Re-purposing synthetic data for an unapproved use case is strictly prohibited.

4.1.4 **No Re-identification Attempts:** Any attempt, whether manual or automated, to re-identify individuals from Synthetic Data is a violation of Meridian’s Code of Conduct and this SOP, and may be grounds for immediate termination of employment and legal action.

### 4.2 Governance of Source Data

4.2.1 **Lawfulness of Processing:** No Source Data may be used in SDG without a documented, valid Lawful Basis for Processing. Acceptable bases include:
- **GDPR Article 6(1)(a) (Consent):** Explicit, specific, and informed consent from the data subject for the generation of synthetic derivatives.
- **GDPR Article 6(1)(f) (Legitimate Interest):** Legitimate interests pursued by Meridian, balanced against the rights and freedoms of the data subject, as documented in a Legitimate Interest Assessment (LIA) approved by Legal.
- **GDPR Article 9(2)(j):** For special categories of data (e.g., health data), processing is necessary for scientific research purposes in accordance with Article 89(1), based on Union or Member State law, with documented safeguards.

4.2.2 **Data Minimization at Source:** The Data Steward must ensure that the Source Data selected for generator training is the minimal necessary to achieve the specific, approved purpose of the synthetic data project. Direct identifiers (e.g., Name, MRN, SSN, Email, IP Address) must be removed or irrevocably pseudonymized prior to ingestion into the SDG pipeline, irrespective of the perceived privacy protections of the generator.

### 4.3 Consent and Data Subject Rights

4.3.1 **Consent Integration:** Where the processing of Source Data is based on Consent (GDPR Article 6(1)(a), 9(2)(a)), the consent management platform (OneTrust) must be programmatically queried via the Meridian Consent API (`/consent/v2/verify`) prior to any data extraction. The generator model shall be considered a downstream processing activity covered by the original consent scope.

4.3.2 **Exercising the Right to Erasure (Art. 17):** Data subjects have the right to request the erasure of their personal data. For structured Source Data, record deletion must be propagated. The effect on the Generative Model must be evaluated. If the model was trained on a record that is later erased, Meridian must, within **30 calendar days**:
1.  Delete the raw source data record from the operational database and all backups.
2.  Re-train or, where computationally infeasible to re-train immediately, mathematically unlearn the data subject’s contribution from the generative model, a process scheduled and tracked via a Jira Unlearning Ticket (Component: `SDG-Unlearn`).
3.  Re-assess the privacy budget ε and document the impact on model utility.

4.3.3 **Data Portability (Art. 20):** The generative model itself is not considered personal data and is not portable. However, the raw Source Data of the requesting data subject must be provided in a structured, commonly used, and machine-readable JSON format within **30 calendar days** of the validated request.

### 4.4 Transfer and Storage Controls

Synthetic data classified as deriving from an Article 9(1) data source will always be subject to the technical controls specified in Section 6, irrespective of its evaluated re-identification risk score, when stored or transferred across jurisdictional boundaries.

### 4.5 Prohibited Activities

The following activities are strictly prohibited:
- Use of synthetic data for operational customer communications.
- Unsupervised release of Tier 2 or Tier 3 synthetic data to public open-source repositories.
- Bypassing the SynthSphere SDG pipeline to generate synthetic data on local workstations.

---

## 5. Detailed Procedures

### 5.1 Use Case Submission and Approval Workflow

Any Meridian team seeking to generate or utilize synthetic data must follow the formal intake process. This process is designed to capture purpose, risk, and legal basis before a single compute cycle is allocated.

#### 5.1.1 Procedure Steps

1.  **Requestor** completes Form `SDG-101: Synthetic Data Use Case Request` available in the Meridian ServiceNow Portal under *IT Services > Data Governance*.

    **Form SDG-101 Fields:**
    | Field ID | Field Name              | Field Type     | Description / Options                                                                                                         |
    | -------- | ----------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------- |
    | `req01`  | **Business Owner**      | User Lookup    | Must be a Director+ level.                                                                                                    |
    | `req02`  | **Project Name**        | Text           | A clear, descriptive title.                                                                                                   |
    | `req03`  | **Objective**           | Rich Text      | Detailed description of why synthetic data is needed. Specify the model under development or the research question.           |
    | `req04`  | **Source Data Asset**   | CMDB Lookup    | Select from the Data Asset Registry (e.g., `DAT-0045: NHANES-Diabetes-Cohort`). Must link to data classification tier.        |
    | `req05`  | **Lawful Basis**        | Dropdown       | `Consent`, `Legitimate Interest`, `Scientific Research (Art. 9)`. Evidence of consent or LIA ID required.                   |
    | `req06`  | **Desired Utility (`U`)**| Slider (0-1)   | Target downstream model performance metric (e.g., F1 score, AUC).                                                             |
    | `req07`  | **Target Release Tier** | Dropdown       | Tier 1 (Public), Tier 2 (Internal), Tier 3 (Highly Sensitive).                                                              |
    | `req08`  | **Consumer List**       | Group Lookup   | Active Directory groups that will access the generated data.                                                                 |
    | `req09`  | **Data Disposition**    | Dropdown       | Plan for data after project end (e.g., `Delete after 90 days`).                                                               |

2.  **Automated Validation:** Upon submission, ServiceNow triggers a scripted validator (`SOP-AIML-016-Validator`) that:
    - Checks that the `Source Data Asset` has an approved and current Data Protection Impact Assessment (DPIA) in the GRC platform, Archer.
    - Verifies the `Lawful Basis` evidence.
    - If validation fails, the request is auto-rejected and returned to the Requestor with a list of violations.

3.  **DSRB Triage:** If validation passes, the ticket is routed to the DSRB Chair. Within **5 business days**, the Chair assigns a Lead Reviewer (Privacy Engineer) and a Quality Reviewer (Data Steward). A kick-off meeting is scheduled if the project is Tier 2 or 3.

4.  **Privacy Risk Assessment (PRA):** The assigned Privacy Engineering Lead performs a detailed PRA.
    - **Tier 1:** Automated PRA is executed by the SDG platform itself. The system confirms source data is aggregate, non-personal and approves automatically.
    - **Tier 2:** Manual PRA by Privacy Eng. Lead. Defines initial privacy budget bounds (e.g., ε ∈ [1.0, 4.0]) and identifies potential vulnerability to Membership Inference Attacks.
    - **Tier 3:** Full adversarial review by the Office of the CAIO. A formal Ethical Review Board (ERB) consultation is mandatory.

5.  **Approval:** The DSRB votes via ServiceNow. Approval quorum is a simple majority (50%+1), but must include either the CAIO (for Tier 3) or the VP of Engineering (for Tier 2) as an affirmative vote. The final approved `ε` budget and minimum acceptable `Statistical Utility Score` are documented in the `SDG-101` record. The maximum processing time for a complete Tier 2 request is **15 business days**.

### 5.2 Source Data Preparation (`SynthSphere Prep`)

Following approval, the ML Engineer executes the Source Data preparation pipeline on the `SynthSphere` platform, a secured Kubernetes cluster (`meridian-ai-ml-prod`).

1.  **Data Extraction:** Run the `synth-extract` CLI tool, which queries the Meridian Data Lake (Apache Hudi tables) using a read-only service account. The tool enforces column-level access control based on the approved source asset ID.
2.  **Irrevocable Pseudonymization (Stage 1):** All direct identifiers (Cols: `pat_name`, `mrn`, `ssn_last4`, `email_addr`, `phone_num`, `exact_address`) are dropped. No reversible tokenization is permitted; only SHA-256 hashing with a securely discarded salt is permitted at this stage.
3.  **Data Quality Gate:** Execute the `synth-validate-source` script. This pipeline checks for:
    - *Missingness Rate:* ≤ 5% per feature. Features exceeding this trigger an alert to the DSRB.
    - *Record Count:* Must be ≥ **1,000** unique subjects. Training a generative model on cohorts smaller than this requires a Tier 3 exception explicitly approved by the CAIO.
    - *Leakage:* Scans for any surviving direct identifiers using a pre-trained Named Entity Recognition (NER) model. If recall > 0.0, the pipeline is hard-stopped.
4.  **Schema Documentation:** Output a `schema-v5.json` file describing each feature’s logical type, statistical type (Gaussian, categorical, ordinal), bounds, and missing rate. This is committed to the `synthsphere-artifacts` Git repository.

### 5.3 Generator Training and Tuning

This procedure is executed within a dedicated MLflow experiment (`meridian-sdg-v3`) to ensure full reproducibility.

1.  **Model Selection:** Based on the `schema-v5.json`, the platform’s AutoML component (`sdg-automl`) selects an appropriate base architecture from the approved model registry:
    - Tabular, mixed-types: `CTGAN` or `TVAE`.
    - Time-series, event-driven: `TimeGAN` or DoppelGANger.
    - Multi-modal (Image + Metadata): Conditional diffusion models.
    The ML Engineer *may* override this, but must document the rationale in MLflow.

2.  **Privacy Integration (DP-SGD):** The `dp-pipeline` library must be invoked to wrap the generator's optimizer with a Differentially Private Stochastic Gradient Descent (DP-SGD) mechanism. This is non-negotiable for Tier 2 and Tier 3 data. The engine utilizes the `opacus` library with a Moments Accountant.
    - **Clipping Threshold (`C`):** Set to the median of the gradient norms in the first 10 training batches, capped at 1.0.
    - **Noise Multiplier (`σ`):** Calibrated automatically by the `dp-pipeline` based on the approved privacy budget `ε` and `δ = 1/N`, where N is the source dataset size.

3.  **Training Run:** Launch the training job on GPU-backed nodes. MLflow logs all hyperparameters, ε, δ, the model artifact, and the training environment fingerprint.

### 5.4 Synthetic Data Validation and Release Gate

This is the most critical control point. No synthetic dataset leaves the `SynthSphere` sandbox without passing the validation gate. This gate is a combination of automated scripts and a manual sign-off.

#### 5.4.1 Privacy Validation Gate (Automated)

The `synth-privacy-auditor` script, based on the open-source library `SDMetrics`, is executed on a 100,000-record sample of the generated synthetic data.

| **Test Category**            | **Specific Test**             | **Threshold (Tier 2)**           | **Threshold (Tier 3)**             | **Pass/Fail Action**                                                                    |
| ---------------------------- | ----------------------------- | -------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------- |
| **Singling Out**             | Cardinality Match             | No column has exact cardinality match | No column has exact match      | **FAIL:** Auto-block. Tune DP noise multiplier (`σ`).                                   |
| **Attribute Inference**      | Categorical Inference Attack  | AUC ≤ 0.70                       | AUC ≤ 0.60                         | **FAIL:** Reduce `C` or increase `σ`. Re-train.                                     |
| **Linkability (Inter-Table)**| Synthetic Fingerprint         | Dataset Hash ≠ Source Hash       | Dataset Hash ≠ Source Hash         | **PASS:** Informational only.                                                           |
| **Membership Inference**     | Black-box Attack (Shadow Model)| Recall for "In" vs "Out" ≤ 0.65  | Recall ≤ 0.55                      | **WARNING:** Manual review by Privacy Engineer required. Must prove `ε` budget was met. |

If the `synth-privacy-auditor` returns a **FAIL** state, the release gate is locked. The ML Engineer must modify DP parameters and re-train. An automated report is generated and saved to the `synthetic-data-metrics` S3 bucket.

#### 5.4.2 Utility Validation Gate (Automated)

Following a privacy PASS, the `synth-utility-auditor` script runs, measuring the statistical distance between the source data and the synthetic output.

- **Column Shapes:** Kullback-Leibler (KL) Divergence. Median KL must be < 0.1. Features with KL > 0.3 are flagged as "Low Fidelity".
- **Pairwise Correlations:** Difference in correlation matrices. Root Mean Square Error (RMSE) must be < 0.15.
- **Boundary Adherence:** Synthesized values must not violate the legal boundaries established in `schema-v5.json` (e.g., negative age, impossible lab result values).
- **Target Utility (`U`):** The user-defined utility metric from `SDG-101` (`req06`) is calculated (e.g., comparing an AUC of a classifier trained on real vs. synthetic data). The difference between Real-Utility and Synthetic-Utility must be ≤ 10%. If the Privacy Gate reduces utility below this, the DSRB is consulted to re-baseline the project scope, a process mediated by the trade-off chart.

#### 5.4.3 Final Release Approval (Manual Sign-off)

1.  The Privacy Engineering Lead reviews the combined Gate Report (Privacy + Utility). If the report meets all automated thresholds, they attach a "PRIVACY-SIGN-OFF" to the `SDG-101` ticket.
2.  The Data Steward reviews the Utility Report and confirms the "Fitness-for-Purpose" of the data for the approved research question.
3.  The VP of Engineering (or CAIO for Tier 3) performs the final release. The `synth-release` CLI command moves the validated synthetic `Parquet` files from the sandbox bucket to a securely scoped, read-only output bucket (e.g., `s3://meridian-sdg-release/SDG-101-847/`).

### 5.5 Post-Generation Decommissioning

The lifecycle of synthetic data is finite. The disposition plan in `req09` of `SDG-101` is programmatically enforced.
- **Retention:** An S3 lifecycle policy is automatically applied to the release bucket, matching the approved retention period.
- **Destruction:** After the retention period, data is irrevocably deleted using S3 Object Lock deletion.
- **Model Retention:** The generative model artifact in MLflow is retained for audit and potential "unlearning" purposes but its serving endpoints are decommissioned.

---

## 6. Controls and Safeguards

### 6.1 Technical Access Controls

| **Control ID** | **Description**                                                           | **Implementation**                                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TAC-016-01** | **SynthSphere Environment Isolation**                                     | The entire SDG stack operates in a dedicated AWS Virtual Private Cloud (VPC), `vpc-synth-prod`, with no public internet ingress. Egress is limited to Meridian’s internal artifact store and approved package mirrors via a NAT Gateway with strict allowlisting. |
| **TAC-016-02** | **Role-Based Access to Pipeline**                                         | Access governed by AD groups synced to AWS IAM. (`GRP-SDG-Engineer` for training, `GRP-SDG-Auditor` for validation read-only, `GRP-SDG-Release-Manager` for data promotion). Principle of Least Privilege is enforced via IaC (Terraform). |
| **TAC-016-03** | **Immutable Audit Logging**                                              | All CLI commands (`synth-extract`, `synth-release`), API calls to the Consent API, and access to output S3 buckets are logged to AWS CloudTrail. Logs are streamed in real-time to a Sumo Logic `audit-immutability` index, which is read-only. |
| **TAC-016-04** | **Differential Privacy Engine**                                           | The `dp-pipeline` library is a mandatory dependency for any generator serving Tier 2/3 data. Its inclusion is enforced server-side. A non-DP model will fail the `synth-privacy-auditor` Membership Inference test.                      |

### 6.2 Administrative Controls

- **Annual Re-certification:** All personnel in the `GRP-SDG-Engineer` AD group must re-attest to this SOP annually. Failure to complete the SOP-AIML-016 attestation in Workday within 30 days of assignment will result in suspension of SynthSphere access.
- **Third-Party Audits:** The Office of the CAIO will commission an independent audit of the SDG pipeline by an external Qualified Security Assessor (QSA) every **24 months**. The audit will include a full code review of the `dp-pipeline` and `synth-privacy-auditor`.
- **Segregation of Duties:** The person who trains the model must not be the same person who approves the final release for Tier 3 data. This is enforced through ServiceNow workflow rules.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The efficacy of this SOP is measured through a series of quantitative KPIs, displayed on the CAIO Executive Dashboard (Tableau).

| **Metric ID**      | **KPI**                                   | **Target**     | **Measurement Method**                                                                                              |
| ------------------ | ----------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------- |
| **MET-016-01**     | **Mean Time to Approve (MTTA)**           | ≤ 15 Days      | Time from `SDG-101` submission to DSRB approval, measured in ServiceNow.                                              |
| **MET-016-02**     | **First-Pass Privacy Gate Yield**         | ≥ 85%          | Percentage of Tier 2 generator training runs that pass the automated `synth-privacy-auditor` on the first attempt.    |
| **MET-016-03**     | **Utility Divergence (Target U vs. Actual)** | ≤ 10% Absolute | Measured by comparing `req06` in `SDG-101` with the final utility score in `synth-utility-auditor`.                 |
| **MET-016-04**     | **Right to Erasure SLA Compliance**       | 100%           | Percentage of Art. 17 requests where the source record is deleted and model unlearning is initiated within 30 days.    |
| **MET-016-05**     | **Consent Check Latency**                 | < 50ms         | Average API response time for the pre-extraction OneTrust consent verification call.                                  |

### 7.2 Reporting Cadence

- **Weekly Operational Review:** The MLOps team reviews failed validation gates (`synth-privacy-auditor` FAIL logs) to identify model drift or tuning errors.
- **Monthly Program Review:** The VP of Engineering presents a roll-up of metrics (MET-016-01 through MET-016-05) to the Data Stewardship Review Board. This review includes a state of all open exceptions.
- **Quarterly Executive Review:** The CAIO delivers a report to the Chief Compliance Officer summarizing the organization’s synthetic data risk posture, Art. 17 compliance, and results from any internal privacy sweeps.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

Deviations from the procedures specified in this SOP, particularly concerning the use of non-DP generators or the release of data failing a validation gate, require a formal exception. Operational necessity does not justify bypassing controls.

1.  **Submission:** Requestor completes Form `SDG-E01: SDG Exception Request` on ServiceNow, linking the original `SDG-101` ticket. The form requires a detailed justification, a compensating control plan, and the proposed timeframe for resolution.
2.  **Risk Evaluation:** The Privacy Engineering Lead performs an expedited risk assessment, quantifying the increased re-identification risk on a scale of LOW, MEDIUM, HIGH, CRITICAL.
3.  **Approval Matrix:**
    | **Risk Level** | **Approver**                                    | **Max Validity** |
    | -------------- | ----------------------------------------------- | ---------------- |
    | LOW            | Privacy Engineering Lead                        | 12 Months        |
    | MEDIUM         | VP of Engineering, Data Stewardship Review Board| 6 Months         |
    | HIGH           | Chief AI Officer, Chief Compliance Officer      | 90 Days          |
    | CRITICAL       | Chief Executive Officer, General Counsel        | 30 Days          |

4.  **Tracking:** All active exceptions are tracked in the ServiceNow "Exception Register" and reviewed at each Monthly Program Review. A compensating control (e.g., enhanced manual review, restricted access to a smaller consumer list) is mandatory for any approved exception.

### 8.2 Escalation Protocol

- **Violation Detection:** Any engineer who discovers evidence of a prohibited activity (e.g., an unauthorized re-identification attempt) must immediately escalate to their Director and the Privacy Engineering Lead via the `dsrb-escalation@meridian.com` distribution list.
- **Incident Response:** The escalation triggers the *Meridian Incident Response Plan* (IRP-001). The SDG Environment is quarantined, access keys for the implicated user are revoked, and a forensic snapshot of the affected data buckets is taken within 1 hour.

### 8.3 Ethical Review Board (ERB) Veto

The Meridian Ethical Review Board retains an unconditional right to revoke any synthetic data use case approval or exception if, upon review, the activity is deemed to pose an unacceptable reputational or ethical risk to the company or patient populations, irrespective of its technical compliance with this SOP.

---

## 9. Training Requirements

### 9.1 Required Training Modules

All personnel in roles defined in Section 3 must complete the following training curricula, tracked via the Workday Learning Management System (LMS).

| **Role Group**                        | **Course Code**      | **Course Title**                                             | **Frequency** | **Passing Score** |
| ------------------------------------- | -------------------- | ------------------------------------------------------------ | ------------- | ----------------- |
| ML Engineers, Data Scientists         | `AIML-016-TECH-01`   | Technical Execution of SOP-AIML-016                          | Annually      | 85%               |
| ML Engineers, Data Scientists         | `AIML-016-DP-01`     | Principles of Differential Privacy & Utility Trade-offs      | Semi-Annually | 90%               |
| Business Owners, Product Managers     | `AIML-016-GOV-01`    | Data Governance for Non-Engineers: Synthetic Data & You      | Annually      | 80%               |
| Privacy Engineers, DSRB Members       | `AIML-016-ADV-04`    | Advanced Adversarial Robustness and Attack Vectors           | Annually      | 95%               |
| All Access-Holders (Mandaory)         | `SEC-AIML-PHI-101`   | Security Hygiene & Handling of Regulated Data Artifacts      | Annually      | 90%               |

### 9.2 Non-Compliance

Access to the `SynthSphere` environment is controlled by AD group membership (`GRP-SDG-Engineer`). A nightly automated script queries the Workday LMS API. Any user whose required training is **expired by more than 7 calendar days** is automatically removed from the `GRP-SDG-Engineer` group, revoking their access. Reinstatement requires manual completion and a Director approval.

---

## 10. Related Policies and References

### 10.1 Internal Policies

| **SOP ID**      | **Title**                                                                 |
| --------------- | ------------------------------------------------------------------------- |
| `SOP-GDPR-001`  | EU General Data Protection Regulation (GDPR) General Compliance Framework |
| `SOP-DP-003`    | Differential Privacy Implementation Standard                             |
| `SOP-ISMS-005`  | Access Control Policy & RBAC Procedure                                   |
| `SOP-MLOPS-009` | ML Model Lifecycle Management & MLOps Standards                          |
| `SOP-IRP-001`   | Meridian Incident Response Plan                                          |
| `SOP-DM-011`    | Data Retention, Archiving, and Secure Disposal Policy                    |
| `POL-HR-007`    | Employee Code of Conduct and Acceptable Use Policy                       |
| `FORM-SDG-101`  | Synthetic Data Use Case Request Form                                     |
| `FORM-SDG-E01`  | SDG Exception Request Form                                               |

### 10.2 External References

| **Reference**                           | **Identifier**                                                                                                                      |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Regulation (EU) 2016/679                | General Data Protection Regulation (GDPR)                                                                                          |
| ISO/IEC 27001:2022                      | Information security, cybersecurity and privacy protection                                                                          |
| ISO/IEC 20889:2018                      | Privacy enhancing data de-identification terminology and classification of techniques                                              |
| Meridian Ethics Charter, v3.0           | Ethical principles governing the use of AI/ML at Meridian                                                                          |

---

## 11. Revision History

| **Version** | **Date**       | **Author**                    | **Description of Change**                                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | -------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1.0**     | 2022-04-01     | Dr. A. Sharma (ex-CAIO)       | Initial creation. Established basic GAN usage guidelines.                                                                                                                                                                                                                                                                                                                                       |
| **2.1**     | 2023-06-15     | Privacy Engineering (J. Diaz) | Added initial Privacy Validation Gate (Singling Out check only). Formalized roles of DSRB and CAIO. Created `SDG-101` form.                                                                                                                                                                                                                                                                      |
| **3.2**     | 2024-01-22     | MLOps (K. Ito)                | Full integration of SynthSphere platform. Retired local-workstation SDG. Implemented `synth-privacy-auditor` v1.0 with automated attribute inference and linkability checks. Added DP-SGD requirements for all Tier 3 data.                                                                                                                                                                  |
| **4.4**     | 2024-09-05     | Legal & Compliance            | Major revision. Harmonized procedure with Consent API following external GDPR audit. Refined Lawful Basis for Processing (Art. 6 & 9) guidance. Added Art. 17 unlearning requirements and KPIs. Integrated `dp-pipeline` library as mandatory. Introduced the ERB veto power in Section 8.3.                                                                                                |
| **5.0**     | 2025-07-08     | Business Operations           | Enhanced ServiceNow workflow automation. Replaced static PDF forms with ServiceNow Catalog Items. Added Section 7 Monitoring & Metrics dashboard. Clarified RACI for Tier 1, 2, and 3 data releases. Formalized the generator unlearning ticket protocol.                                                                                                                                     |
| **5.5**     | **2025-11-12** | **Dr. Marcus Rivera (CAIO)**  | **(Current Version)** Comprehensive re-write to incorporate EU MDR compliance for clinical products. Recalibrated validation gate thresholds (Privacy and Utility) based on 12-month adversarial robustness benchmark study. Added detailed data quality gate during source preparation, formalized S3 lifecycle controls, and mandated third-party audit process. Updated training curricula codes. |