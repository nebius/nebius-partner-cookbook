---
sop_id: "SOP-AIML-013"
title: "Experiment Tracking and Reproducibility"
business_unit: "AI/ML Engineering"
version: "5.6"
effective_date: "2025-01-24"
last_reviewed: "2026-08-07"
next_review: "2027-02-20"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
  - "SR 11-7"
status: "Active"
---

# Standard Operating Procedure: Experiment Tracking and Reproducibility

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for tracking machine learning experiments and ensuring the reproducibility of results at Meridian Health Technologies, Inc. The integrity of clinical AI outputs, the safety of patient-facing financial products, and the defensibility of our analytics require a disciplined, auditable approach to the machine learning lifecycle. This document defines the processes, tools, and controls necessary to create a complete and immutable record of every experiment, ensuring that any result can be verified, reconstructed, or challenged at a future date.

The core objectives of this SOP are to:
- Define a standardized taxonomy for experiment metadata across all business lines.
- Mandate the use of centralized logging and artifact storage for all model development activities.
- Establish reproducibility tiers with specific, measurable criteria.
- Ensure data lineage is maintained from raw source data to final model output.
- Provide the evidentiary foundation for model validation, audit, and regulatory review, particularly for models subject to risk management scrutiny under applicable federal guidance.

### 1.2 Scope

This SOP applies to all employees, contractors, and third-party vendors who design, develop, train, fine-tune, or evaluate machine learning models and algorithms for any Meridian product or internal tool. The scope encompasses the following activities:

**In-Scope Activities:**
- Exploratory Data Analysis (EDA) intended to inform feature engineering for a target model.
- Development and tuning of all model types, including but not limited to: gradient-boosted trees (XGBoost, LightGBM), deep neural networks (PyTorch, TensorFlow), large language models (LLMs), and classical statistical models (e.g., logistic regression) used in production pipelines.
- Feature engineering logic, including SQL-based feature stores and real-time feature computations.
- Hyperparameter optimization runs, whether manual, grid search, or Bayesian.
- Distributed training jobs orchestrated via Kubeflow on Amazon EKS.
- Evaluation and benchmarking on hold-out, validation, and out-of-time test sets.
- Bias and fairness testing, including disaggregated performance analysis.
- Prompts and configurations for generative AI components of the Clinical AI Platform.

**Out-of-Scope Activities:**
- Purely analytical one-off queries in Snowflake that do not produce a model artifact or directly inform a production feature.
- Pre-production infrastructure deployment scripts managed via Terraform (tracked under SOP-IT-102: Infrastructure Change Management).
- Production inference operations, which are governed by SOP-AIML-025: Model Serving and Monitoring.

**Applicability Matrix:**

| Business Unit | Models in Scope | Risk Classification | Reproducibility Tier (Minimum) |
| :--- | :--- | :--- | :--- |
| Clinical AI Platform | Diagnostic imaging, adverse event prediction, patient risk scoring | High-Risk | Tier 1: Full Reproducibility |
| HealthPay Financial Services | Credit scoring, fraud detection, claims adjudication, lending | Regulated Model | Tier 1: Full Reproducibility |
| MedInsight Analytics | Population health models, care gap prediction | Internal/Client-Facing | Tier 2: Core Reproducibility |
| Meridian SaaS Platform | Platform-level operational models (e.g., cost optimization) | Operational | Tier 3: Standard Reproducibility |

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
| :--- | :--- |
| **Artifact** | Any binary file produced during an experiment, including serialized model weights (`.pkl`, `.pt`, `.onnx`), preprocessor objects, encoder mappings, evaluation charts, and training logs. |
| **Data Lineage** | The complete recorded sequence of data sources, transformations, and splits that led to the dataset used for a specific training run. |
| **Environment Capsule** | A Meridian-mandated Docker image or `conda` environment lockfile that fully specifies the software dependencies for a training run. |
| **Experiment** | A single, atomic run of a training or evaluation script with a defined set of hyperparameters, code version, and data version, producing a distinct set of artifacts and metrics. A group of Experiments constitutes a Project. |
| **Immutability** | The principle that once an Experiment record and its artifacts are logged, they cannot be overwritten or deleted, only tagged (e.g., as "deprecated" or "validated"). |
| **Non-Determinism** | Sources of randomness in training that prevent bit-for-bit reproduction, including GPU floating-point non-associativity, dataloader worker scheduling, and stochastic algorithms (dropout, etc.). |
| **Seed Binder** | A cryptographically generated UUID that is hashed to deterministically produce all random seeds for an experiment (Python `random`, NumPy, PyTorch, TensorFlow, etc.), ensuring full control over stochasticity. |
| **Reproducibility Package** | A compressed directory containing the code snapshot, environment definition, parameter file, and a pointer to the immutable dataset version required to re-execute an experiment. |

### 2.2 Acronyms

| Acronym | Definition |
| :--- | :--- |
| CLIMB | Clinical & Lending Integrated Model Builder (Internal Meridian platform) |
| DVC | Data Version Control |
| FMIA | Fairness and Model Impact Assessment |
| KMS | AWS Key Management Service |
| MLIR | Machine Learning Incident Response |
| MLO | Model Lifecycle Owner |
| MMDB | Meridian Model Database (Central model inventory) |
| RMSE | Root Mean Squared Error |
| ROC-AUC | Receiver Operating Characteristic - Area Under the Curve |
| SHAP | SHapley Additive exPlanations |
| VCS | Version Control System (Git) |

## 3. Roles and Responsibilities

The following RACI matrix delineates responsibilities for all activities governed by this SOP.

| Activity / Task | AI/ML Engineer | MLO / Tech Lead | QA Validator | AI Governance (Compliance) | ML Platform Team |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Experiment Execution & Logging** | R, A | C | I | I | C |
| **Code & Environment Versioning** | R | A | I | I | C |
| **Dataset Versioning & Lineage** | R | A | R | I | C |
| **Reproducibility Package Creation** | R | C | R, A | I | I |
| **Seed Binder Generation & Control** | R | C | I | I | I |
| **Artifact Signing & Immutability** | I | I | I | R | R, A |
| **Interim Model Documentation** | C | R, A | I | R | I |
| **Tier Review & Escalation** | C | R | R | A | I |
| **Tooling & Infrastructure Maintenance** | C | C | I | I | R, A |

**Key Responsibilities:**

- **AI/ML Engineers (Model Developers):** Execute all procedures defined in Section 5. They own the completeness and correctness of experiment logs, ensuring every metric and artifact is captured programmatically. They must never rely on manual note-taking as a primary record.
- **Model Lifecycle Owner (MLO) / Tech Lead:** Accountable for the integrity of the entire experiment stream within their project. They review logs within the Meridian Model Database (MMDB) dashboard weekly, approve experiment promotion to the "Validated" tag, and sign off on Reproducibility Packages.
- **QA Validator:** An independent party within the AI/ML Engineering unit who performs reproducibility stress tests as described in Section 5.6. This role is distinct from the model developer.
- **AI Governance (Thomas Anderson's Compliance Team):** Performs scheduled and unscheduled audits of MMDB records against this SOP to ensure adherence for all models classified as Regulated or High-Risk. They manage the centralized evidence locker for external audits.
- **ML Platform Team:** Maintains the CLIMB platform, MMDB backend, and the DVC-backed artifact store. They enforce the technical guardrails that prevent deletion and enforce naming conventions.

## 4. Policy Statements

All Meridian personnel engaged in model development must comply with the following mandatory policies:

4.1 **Mandatory Logging.** Every Experiment, regardless of business line or perceived impact, must be logged to the centralized MMDB. A log entry must be initiated via the CLIMB SDK within the training script and completed before the compute cluster is terminated. Stale or orphaned runs must be resolved or officially abandoned within one (1) business day.

4.2 **Immutability of Records.** Once an Experiment has been logged with a `RUN_ID` and its status set to `COMPLETED`, all associated parameters, metrics, tags, and the artifact pointer are immutable. Data can be corrected only by logging a new Experiment with an explicit reference to the corrected record, following the errata process in Section 5.8.

4.3 **Deterministic Seeding.** All experiments must use the Meridian Seed Binder protocol. Individual static seeds for specific libraries are prohibited. This ensures that a single `meridian_seed_binder` value is the sole source of all downstream randomness.

4.4 **Data Versioning.** No model shall be trained on a dataset that is not registered as an immutable version in the Meridian Data Catalog and tracked via DVC. The `dataset_commit_hash` from DVC must be present in the experiment log.

4.5 **Documentation.** All models must include a model document that contains a summary of the model's intended use, a concise architecture overview, and validation metrics, logged as a markdown artifact within the MMDB.

4.6 **Prohibition of Orphaned Artifacts.** Saving model artifacts to local laptops, unmanaged EBS volumes, or personal S3 buckets is strictly prohibited. All artifacts must be written to the MMDB-managed S3 bucket via the pre-signed URL mechanism provided by the CLIMB SDK.

## 5. Detailed Procedures

### 5.1 The Reproducibility Tier Framework

Meridian classifies all models into three Tiers. The MLO is responsible for assigning the Tier at the inception of the project, subject to approval by AI Governance for High-Risk and Regulated models.

- **Tier 1: Full Reproducibility.** Required for Clinical AI and Regulated HealthPay models. Any other model that directly influences individual patient care or credit decisions. A Tier 1 model must reproduce within a 0.1% tolerance of all primary reported metrics (e.g., Accuracy, ROC-AUC, RMSE).

- **Tier 2: Core Reproducibility.** Required for MedInsight Analytics models where population-level insights are the primary output. A Tier 2 model must reproduce within a 2% tolerance on primary metrics and exact match for non-stochastic metrics like precision@k where k is a static cutoff, provided identical hardware is available.

- **Tier 3: Standard Reproducibility.** Applies to exploratory, operational, and deprecated models. The codebase, environment, and data snapshot must be preserved to allow for debugging and root cause analysis, but bit-for-bit reproduction is not required.

### 5.2 Experiment Configuration and the Seed Binder

Before initiating any training run, the experiment configuration must be codified into a single YAML file, `experiment_config.yaml`, stored at the root of the project's Git repository.

**Step 1: Generate the Seed Binder.**
Use the CLIMB SDK to generate a cryptographically secure random UUID.
```bash
climb seed generate
```
This command outputs a UUID, e.g., `a1b2c3d4-e5f6-7890-1234-567890abcdef`. This value is the `seed_binder`.

**Step 2: Complete the Configuration File.**
Populate `experiment_config.yaml` with the following mandatory fields:

```yaml
experiment:
  project_name: "patient_risk_v4"
  description: "Testing GBDT with new claims features for Tier 1 clinical validation."
  reproducibility_tier: 1
  seed_binder: "a1b2c3d4-e5f6-7890-1234-567890abcdef"

data:
  dvc_remote: "s3://meridian-dvc-clinical/patient_risk_v4"
  dataset_ref: "data/processed/training_set_v4.parquet"
  # The DVC hash of the exact dataset version must be passed at runtime
  expected_dvc_hash: "a3d8f2c"

environment:
  type: "docker"
  image: "915276534271.dkr.ecr.us-east-1.amazonaws.com/meridian/jax-pytorch-cuda:12.1-custom"
  image_digest: "sha256:b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c"

parameters:
  optimizer: "adam"
  learning_rate: 0.001
  batch_size: 128
  epochs: 50

tracking:
  mmdb_callback: true
  log_every_n_steps: 100
```

**Step 3: Programmatic Seeding in Training Code.**
At the entrypoint of the training script, the Seed Binder must be unpacked deterministically. The CLIMB SDK provides a context manager:

```python
from meridian.climb import SeedBinder, Experiment

# The SeedBinder context manager deterministically sets seeds for:
# os.environ['PYTHONHASHSEED']
# random, numpy, pytorch, tensorflow
with SeedBinder(config['experiment']['seed_binder']) as seed_map:
    # `seed_map` is a dict containing library-specific seeds for debugging
    # The actual training code goes here
    model = train_model(config)
```

Static seeds (e.g., `np.random.seed(42)`) are forbidden and will be flagged by the linter in the CI/CD pipeline.

### 5.3 Data Versioning and Data Lineage

Datasets used for Tier 1 and Tier 2 models must be immutably versioned.

**Step 1: Register the Dataset.**
Instead of a raw S3 path, point DVC to the Meridian Feature Store service.
```bash
dvc import-url s3://meridian-feature-store/patient_risk/v4/training_data.parquet
```

**Step 2: Run Data Processing Scripts with Tracking.**
The script that performs the final train/test split or any state-dependent processing (`train_test_split.py`) must log its Git commit hash and the `dvc.yaml` hash to MMDB as a separate, tagged run.

**Step 3: Capture Lineage Artifact.**
After executing the processing script, create a `lineage.txt` file and log it as an artifact to MMDB.
```text
Data Processing Script: repo:patient_risk_v4, path:scripts/train_test_split.py, commit: abc123...
Input Feature Store Tag: patient_risk/v4/training_data.parquet
Output Train Dataset DVC Hash: 6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e
Output Test Dataset DVC Hash: 7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f
Timestamp: 2025-11-15T10:30:00Z
```

### 5.4 Experiment Execution and Logging

The `Experiment` object from the CLIMB SDK orchestrates the entire training run.

**Step 1: Initialize the Experiment.**
At the beginning of the training script, initialize the experiment runner. This creates the record in MMDB with a status of `RUNNING`.

```python
from meridian.climb import Experiment

exp = Experiment(
    project_name=config['experiment']['project_name'],
    config_dict=config, # The entire config is logged as metadata
    reproducibility_tier=config['experiment']['reproducibility_tier'],
    dataset_commit_hash=data_loader.get_dvc_hash(),
    code_commit_hash=git.get_current_commit(),
)
```

**Step 2: Log Parameters and Tags.**
```python
exp.log_parameters(config['parameters'])
exp.set_tags({
    "model_family": "gradient_boosting",
    "business_unit": "clinical_ai",
    "status": "under_development"
})
```

**Step 3: Log Metrics during Training.**
Use the `exp.log_metric` and `exp.log_metrics` functions for step-level and epoch-level logging. All Tier 1 models must log a minimum of:
- Loss (Training and Validation)
- AUC-ROC or RMSE (Validation)
- Gradient norm per layer
- SHAP summary plot artifact every 10 epochs.

```python
for epoch in range(epochs):
    train_loss = train_one_epoch(...)
    val_loss, val_auc = validate(...)

    exp.log_metrics({
        "train_loss": train_loss,
        "val_loss": val_loss,
        "val_auc": val_auc
    }, step=epoch)
```

**Step 4: Log Artifacts.**
Upon training completion, log all outputs.
```python
# Log the final model
exp.log_artifact(local_path="outputs/model.pkl", artifact_path="model/final_model.pkl")

# Log the SHAP explanation plot for the test set
exp.log_artifact(local_path="outputs/shap_summary.png", artifact_path="explanations/shap_summary.png")

# Log the environment lock file
exp.log_artifact(local_path="environment.lock.yaml", artifact_path="reproducibility/")
```

**Step 5: Finalize the Run.**
```python
exp.finalize(status="COMPLETED")
```
This action triggers the immutability flag. The MMDB record can no longer be altered.

### 5.5 Artifact Management and Signing

All artifacts are stored in the Meridian Artifact Store, an S3 bucket (`s3://meridian-aiml-artifacts`) with AWS KMS managed encryption (SSE-KMS). Direct access is prohibited. All interaction must go through `climb artifact` CLI or the SDK.

**Signing Procedure (Automated):**
Upon finalization, the CLIMB backend automatically:
1.  Computes the SHA-256 hash of every artifact.
2.  Records these hashes in the MMDB Experiment record.
3.  Applies an `artifact_manifest` metadata object to the S3 object using an AWS KMS key designated for artifact signing.

To verify the integrity of a downloaded artifact, use:
```bash
climb artifact verify --run_id "patient_risk_v4_a1b2c" --artifact_path "model/final_model.pkl"
```
This command re-hashes the local file and compares it against the signed manifest stored in MMDB.

### 5.6 Reproducibility Verification Procedure

The MLO must schedule a reproducibility verification exercise with the QA Validator in the following cadences:
- **Tier 1:** Immediately prior to the Model Validation Report (MVR) sign-off, and annually thereafter.
- **Tier 2:** At the first major version release (e.g., `v2.0`).
- **Tier 3:** Not required.

**Verification Steps:**

1.  **Retrieve Package:** The QA Validator uses the `RUN_ID` to retrieve the full reproducibility package via the command:
    ```bash
    climb archive fetch --run_id "patient_risk_v4_a1b2c" --output-dir "./qa_verification/"
    ```
2.  **Re-provision Environment:** The Validator provisions an EC2 instance from the same AMI and instance type family (`p3dn.24xlarge` or equivalent `p4d`) as documented in the `config.log` parameters. They pull the exact Docker image from ECR using the recorded digest.
3.  **Execute Training:** The Validator executes the training script found in the package, without modification, against the DVC-tracked dataset.
    ```bash
    climb run reproduce --config ./qa_verification/experiment_config.yaml
    ```
4.  **Compare Metrics:** The `climb run reproduce` command automatically queries the original run's metrics from MMDB and compares them to the newly generated metrics.

**Pass/Fail Criteria:**

| Metric Type | Tier 1 Tolerance | Tier 2 Tolerance |
| :--- | :--- | :--- |
| Loss, Accuracy, RMSE | ±0.1% relative error | ±2.0% relative error |
| SHAP Feature Importance (Top-10) | Exact rank match | Top-7 of Top-10 must match |
| Non-Deterministic Ops (Dropout) | Statistical equivalence test (p>0.05) is acceptable | Not tested |

If a run fails, the MLO and QA Validator must file an ML Incident Report (MLIR) per SOP-AIML-017 (Model Incident Response) and triage the root cause.

### 5.7 Code and Environment Versioning

All code for an experiment must be committed to a Meridian-managed GitHub repository. The `code_commit_hash` is a mandatory parameter in every experiment log.

**Procedure for Environment Management:**
1.  **Pre-Approved Environments:** The ML Platform team publishes a set of pre-approved Docker images for each model family and major framework version. These are scanned for vulnerabilities monthly.
2.  **Custom Environments:** If a project requires a library outside the pre-approved set, the MLO must submit a "Custom Environment" request to the ML Platform team 5 business days in advance. The resulting Docker image must be built via the CI/CD pipeline, with the `Dockerfile` committed to the project's repository. The full image digest (`sha256:...`) is the tracked artifact, not the mutable `:latest` tag.

### 5.8 Handling Corrections and Errata

Because experiment records are immutable, errors cannot be edited. They must be corrected via an official Errata process.

**Procedure:**
1.  **Identify the Error:** The original `RUN_ID` `patient_risk_v4_a1b2c` has an incorrect metric logged due to a bug in the evaluation script.
2.  **Log an Errata Note:** The MLO or engineer logs a new tag on the original experiment via the MMDB UI or CLI:
    ```bash
    climb tag add --run_id "patient_risk_v4_a1b2c" --tag "status:errata" --note "AUROC metric incorrect due to eval bug. See corrected run patient_risk_v4_z9y8x."
    ```
3.  **Execute a Corrective Run:** Fix the evaluation script bug, commit the fix to Git, and execute a new Experiment that is a *pure evaluation run* on the original model artifact.
4.  **Link Records:** The new Experiment (`patient_risk_v4_z9y8x`) must be tagged as `"corrects:patient_risk_v4_a1b2c"`. The model documentation must reference the corrected metrics.

### 5.9 Managing Non-Determinism

For Tier 1 models, a "Statement of Non-Determinism" must be logged if bit-for-bit reproduction is mathematically impossible due to algorithmic design (e.g., attention mechanisms with race conditions in gradient computation).

**Procedure:**
1.  An engineer or MLO documents the specific operators causing non-determinism (e.g., `atomicAdd` in a custom CUDA kernel).
2.  This document is logged as a text artifact in the Experiment run.
3.  The Reproducibility Verification in Section 5.6 will then default to the "statistical equivalence" test for all metrics, not the ±0.1% tolerance. The QA Validator must use a specific seed binder that ensures a normal distribution of outcomes to perform a valid equivalence test.

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Description | Enforcement Mechanism | Scope |
| :--- | :--- | :--- | :--- |
| **TEC-013-01** | **Central Artifact Store Bucket Policy.** S3 bucket policy denies `DeleteObject` and `PutObject` (except via the CLIMB service role). Direct user `s3://` PUTs are blocked. | AWS S3 Bucket Policy and SCP | Tier 1, 2, 3 |
| **TEC-013-02** | **CLIMB SDK Environment Validation.** The `Experiment` object validates at init time that the runtime environment (Docker image digest, Python version) matches an approved list. A mismatch logs a `WARNING` tag; for Tier 1, it raises a blocking `FATAL` error. | CLIMB SDK pre-flight check | Tier 1 |
| **TEC-013-03** | **Seed Binder Linting.** A pre-commit Git hook and Jenkins CI stage statically analyze all Python files in the project for explicit calls to `random.seed()`, `np.random.seed()`, etc., outside the official `SeedBinder` context manager. Any positive hit fails the build. | CI/CD Pipeline (Jenkins) | Tier 1, 2 |
| **TEC-013-04** | **Data Drift Detection at Source.** The DVC-tracked dataset hash is compared at training time against the registered hash in the Feature Store. A mismatch immediately halts the Experiment and writes an `INVALID_DATA_SOURCE` error to MMDB. | CLIMB SDK pre-flight check | Tier 1, 2 |
| **TEC-013-05** | **Immutable MMDB Records.** The PostgreSQL database backing MMDB has row-level security. The `climb_user` role has `SELECT` and `INSERT` permissions on the experiments table but lacks `UPDATE` and `DELETE` permissions for any run status other than `INITIALIZING`. | Database Role-Based Access Control | All |

### 6.2 Administrative Controls

| Control ID | Description | Frequency | Responsible |
| :--- | :--- | :--- | :--- |
| **ADM-013-01** | **Quarterly Tier 1 Audit.** The AI Governance team selects a random sample of 5 Tier 1 experiment logs and performs a manual reproducibility test against the documented criteria. | Quarterly | AI Governance |
| **ADM-013-02** | **Monthly Tier Review.** Each MLO must review all experiments in their project area with a `COMPLETED` status but no `promoted_to` tag. An experiment older than 30 days without a tag must be explicitly closed or promoted. | Monthly | Model Lifecycle Owner |
| **ADM-013-03** | **Access Review.** The ML Platform team reviews IAM and MMDB access policies for the artifact store and experiment database. | Semi-Annually | ML Platform Team |

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The ML Platform and AI Governance teams jointly monitor the following KPIs, which are visualized on the "MLOps Health Dashboard."

| KPI | Target | Measurement Method |
| :--- | :--- | :--- |
| **Experiment Logging Compliance** | >99% | (Number of active Git repos with ≥1 commit in the last month) / (Number of active Git repos with ≥1 Experiment log in MMDB in the last month) per business unit. |
| **Reproducibility Success Rate (Tier 1)** | 100% | (Number of scheduled Tier 1 reproducibility tests that pass) / (Total number of scheduled Tier 1 tests). |
| **Orphan Experiment Closure** | < 5 per BU | Count of experiments in `RUNNING` status for more than 24 hours. |
| **Artifact Store Integrity** | 100% | Daily automated scan that re-hashes a random 1% sample of artifacts and compares against the signed manifest. |
| **Custom Environment Drift** | < 3 active exceptions | Number of active projects running on a non-standard Docker image with an open exception ticket. |

### 7.2 Reporting Cadence

- **Weekly Operations Report:** An automated report on Orphan Experiment Closure is emailed to all MLOs and David Park (VP, Engineering) every Monday at 09:00 EST.
- **Quarterly Governance Report:** The AI Governance team compiles a report including the Tier 1 audit results, logging compliance trends, and a detailed review of open exceptions. This report is presented to the AI Executive Steering Committee.
- **Annual SOP Review:** Dr. Marcus Rivera (CAIO) and David Park (VP, Engineering) conduct a full review of this SOP, its KPIs, and any related ML incident reports to determine if threshold updates are necessary.

## 8. Exception Handling and Escalation

### 8.1 Exception Types

The following circumstances are recognized as valid triggers for a formal exception request:
- **Data Immutability Exception:** A training dataset is streamed and cannot be assigned a static DVC hash. Applies to specific reinforcement learning from human feedback (RLHF) setups.
- **Non-Deterministic Hardware Exception:** Training on a heterogenous fleet of spot instances where GPU type cannot be pinned for cost reasons. Applies primarily to Tier 3 models.
- **Urgent Safety Patch:** A critical bug is found in a production model that requires an immediate hotfix model to be trained and deployed without the standard reproducibility verification (post-hoc verification is required).

### 8.2 Exception Request Procedure

1.  **File Request:** The MLO files a request in the Meridian GRC (Governance, Risk, Compliance) system, selecting the "SOP-AIML-013 Exception" form. The form requires:
    - The specific policy section for which an exception is sought (e.g., 4.4, 5.6).
    - The `RUN_ID`s or project names affected.
    - A technical justification explaining why the standard procedure is technically infeasible or presents a higher risk than the non-compliance.
    - A proposed compensating control (e.g., real-time data validation instead of DVC hashing).
    - A definitive expiry date not exceeding one quarter.
2.  **Technical Review:** David Park (VP, Engineering) or his delegate reviews the technical justification.
3.  **Compliance Approval:** Thomas Anderson (AI Governance) grants final approval, assigning a `GRC_EXCEPTION_ID`. No exception for a Tier 1 Clinical or Regulated HealthPay model involving data immutability can be approved without a compensating control that is demonstrably equivalent.

### 8.3 Emergency Patch Procedure

During a P1 Incident (declared per SOP-IT-050: Major Incident Management):
1.  The responding engineer performs an expedited experiment log.
2.  They tag the experiment `"status:emergency_patch"` and explicitly link it to the incident ticket in the MMDB tags.
3.  The MLO has 5 business days after the incident is resolved to complete a full retrospective reproducibility exercise and either certify the emergency run or retrain and replace the model following standard procedures.

## 9. Training Requirements

All personnel subject to this SOP must complete the following training:

| Module Code | Title | Audience | Frequency | Delivery Method |
| :--- | :--- | :--- | :--- | :--- |
| **T-AIML-013A** | Experiment Tracking with CLIMB SDK | All AI/ML Engineers, MLOs | Onboarding, and Annually | Self-paced course on Meridian Learn, with final project requiring logging a Tier-1 compliant experiment. |
| **T-AIML-013B** | Managing Non-Determinism in Clinical AI | Clinical AI Team, QA Validators | Annually | Live, instructor-led workshop. Covers CUDA sources of randomness and statistical equivalence testing. |
| **T-AIML-013C** | Artifact Lifecycle and Model Handover | MLOs, DevOps Leads | Annually | Self-paced course covering the handoff from Experiment to Production via MMDB tags and the CI/CD pipeline. |

**Tracking:**
Completion records are maintained in the Meridian Learn Management System (LMS) and linked to the individual's permanent HR file. The ML Platform team's weekly compliance scan (Section 7) cross-references active committers to an MMDB project with current training completion. A committer with expired T-AIML-013A training will have their push privileges to the `main` branch automatically suspended until training is renewed.

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Title | Relationship |
| :--- | :--- | :--- |
| SOP-AIML-001 | AI Model Risk Management Framework | Defines the overall governance framework into which this tracking SOP fits. |
| SOP-AIML-017 | Machine Learning Incident Response (MLIR) | Procedure to follow when a reproducibility stress test fails, indicating a potential drift or data quality incident. |
| SOP-AIML-025 | Model Serving and Monitoring | Governs the transition from a tracked, validated experiment to a production inference service. |
| SOP-DATA-011 | Data Versioning and Lineage in the Feature Store | Detailed procedure for managing the data assets tracked by DVC in this SOP. |
| SOP-IT-050 | Major Incident Management | Defines P1 and P2 incident response, referenced in the emergency patch exception process. |
| SOP-GRC-004 | Governance Exception and Waiver Management | Standard enterprise process for requesting and approving exceptions to any internal policy. |

### 10.2 External References

- The Twelve-Factor App (Methodology for environment parity applied to ML environments)
- Google Cloud AI Platform: Reproducibility Guide (Conceptual reference for environment capsules)
- DVC Official Documentation (Version 3.x, the in-use generation at Meridian)

## 11. Revision History

| Version | Date | Author | Description of Change |
| :--- | :--- | :--- | :--- |
| 1.0 | 2021-03-15 | Jane Huang | Initial release. Established basic experiment logging in MMDB and mandatory artifact storage. |
| 2.1 | 2022-07-22 | Dr. Aris Thorne | Introduced the Reproducibility Tier framework (Tier 1, 2, 3) to differentiate clinical AI from analytics. Added the Seed Binder protocol. |
| 3.4 | 2023-11-01 | Priya Patel | Major revision. Mandated DVC for all Tier 1 and 2 datasets. Migrated artifact signing from KMS symmetric to asymmetric key for enhanced non-repudiation. Added Section 5.9 Non-Determinism statement. |
| 4.8 | 2024-05-17 | Dr. Marcus Rivera | Overhauled Sections 8 and 9 in response to a critical audit finding on a stale exception. Introduced GRC system integration for exceptions and added mandatory expiration dates. Increased training rigor. |
| 5.6 | 2025-01-24 | David Park | Refined Tier 1 metric tolerance from 1% to 0.1% based on Q4-2024 reproducibility success data. Added `experiment_config.yaml` as a mandatory CI/CD stage gate. Updated MMDB integration points for CLIMB SDK v4.2. Clarified MLO role accountability. |