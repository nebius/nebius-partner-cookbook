---
sop_id: "SOP-AIML-017"
title: "Model Compression and Optimization"
business_unit: "AI/ML Engineering"
version: "2.8"
effective_date: "2024-01-24"
last_reviewed: "2025-02-02"
next_review: "2025-08-11"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Model Compression and Optimization

**SOP-AIML-017**
**Version 2.8**

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the mandatory framework for the compression and optimization of machine learning (ML) and artificial intelligence (AI) models within Meridian Health Technologies, Inc. The purpose is to ensure that all model optimization activities—including quantization, pruning, knowledge distillation, and low-rank factorization—are performed in a standardized, reproducible, and auditable manner that does not compromise patient safety, diagnostic accuracy, or regulatory compliance. This SOP mandates rigorous performance validation and stability testing post-compression to ensure functional equivalence and continued safety, particularly for high-risk AI systems under the EU AI Act.

### 1.2 Scope
This SOP applies to all AI/ML models developed, deployed, or maintained by the AI/ML Engineering business unit, and any third-party models integrated into Meridian systems. Its provisions are binding on all business lines:

- **Clinical AI Platform:** All models classified as high-risk AI systems under Annex III of the EU AI Act, including diagnostic imaging analysis, patient risk scoring, and adverse event prediction systems.
- **HealthPay Financial Services:** Models subject to SR 11-7 model risk management and SOC 2 requirements, including fraud detection, credit underwriting, and claims automation models.
- **MedInsight Analytics:** Population health models, care gap identification models, and outcomes prediction models.

This SOP governs all stages of the model optimization lifecycle: decision to compress, compression execution, functional validation, safety validation, staging deployment, production rollout, and continuous monitoring. It applies to all environments: development sandboxes (`dev-sandbox-*`), MLflow tracking server (`mlflow.meridian.internal`), staging (`stg-ml-*`), and production (`prod-ml-*`).

### 1.3 Applicability
Compliance with this SOP is mandatory for:
- AI/ML Engineers (Levels I–IV)
- Machine Learning Research Scientists
- MLOps Engineers
- Clinical AI Validation Specialists
- AI/ML Engineering Managers and Directors
- Quality Assurance (QA) personnel assigned to AI systems
- Any Meridian contractor or third-party vendor performing model optimization services

Failure to comply with this SOP shall result in escalation per Section 8, potential model rollback, and administrative review by the Chief AI Officer and VP of Engineering.

---

## 2. Definitions and Acronyms

For the purposes of this document, the following definitions apply. Additional terms are defined in the Meridian AI/ML Glossary (`SOP-AIML-001`, Appendix A).

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Calibration Data** | A representative subset of the training or validation dataset, comprising a minimum of 10,000 samples stratified across all target classes, used exclusively for computing scaling factors during quantization-aware training (QAT) and post-training quantization (PTQ). Calibration data must be logged in MLflow as an artifact named `calibration_split.parquet`. |
| **Compression Ratio** | The quotient defined as (Size of Uncompressed Model Artifact in MB) / (Size of Compressed Model Artifact in MB). Reported to three decimal places. |
| **Distillation** | A compression technique wherein a smaller "student" model is trained to mimic the output distribution (logits) of a larger, pre-trained "teacher" model, typically using a Kullback-Leibler divergence loss with a temperature parameter `T` > 1. |
| **Functional Equivalence** | A state wherein the compressed model achieves performance metrics within pre-defined absolute and relative tolerance bands (Section 5.6.3, Table 4) compared to the uncompressed baseline on a held-out gold-standard test set. |
| **Magnitude-Based Pruning** | A structured or unstructured pruning technique that removes weights with the smallest absolute magnitudes (L1-norm) from the model graph, followed by a fine-tuning period. |
| **Post-Training Quantization (PTQ)** | Quantization applied after full-precision (FP32) training is complete, converting weights and activations to lower precision (INT8, FP16) without additional training, requiring only a calibration data pass. |
| **Quantization-Aware Training (QAT)** | A training regime that simulates low-precision inference during the forward pass by inserting fake quantization nodes, allowing the optimizer to compensate for quantization error. Required for Clinical AI Platform models per Section 6.2. |
| **Sensitivity Analysis** | A layer-wise analysis that measures the impact of compression (quantization, pruning) on each layer's output distribution using KL divergence or mean-squared error, identifying layers intolerant to aggressive compression. |
| **Structured Pruning** | The removal of entire channels, filters, or attention heads from a model, resulting in hardware-friendly sparse patterns that yield inference speedups without specialized sparse kernels. |
| **Unstructured Pruning** | The zeroing-out of individual weights based on a saliency criterion, resulting in sparse weight tensors. Does not guarantee inference speedup without specialized hardware or runtimes. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **AUC-ROC** | Area Under the Receiver Operating Characteristic Curve |
| **BOPs** | Billion Operations per inference |
| **FLOPs** | Floating Point Operations |
| **FP16** | 16-bit Floating Point (IEEE 754 half-precision) |
| **FP32** | 32-bit Floating Point (IEEE 754 single-precision) |
| **INT8** | 8-bit Integer (signed quantized representation) |
| **KL** | Kullback-Leibler divergence |
| **MACs** | Multiply-Accumulate operations |
| **MSE** | Mean Squared Error |
| **ONNX** | Open Neural Network Exchange (format) |
| **QAT** | Quantization-Aware Training |
| **PTQ** | Post-Training Quantization |
| **RMSE** | Root Mean Squared Error |
| **SNR** | Signal-to-Noise Ratio (applied to activation tensors) |

---

## 3. Roles and Responsibilities

The following RACI matrix (Responsible, Accountable, Consulted, Informed) delineates roles for all activities governed by this SOP.

| Activity | AI/ML Engineer | Clinical AI Validation Specialist | MLOps Engineer | AI/ML Engineering Manager | Chief AI Officer | Quality Assurance (QA) |
|---|---|---|---|---|---|---|
| **Compression Execution** | R | C | C | A | I | – |
| **Calibration Data Curation** | R | C | – | A | – | – |
| **Sensitivity Analysis** | R | C | – | A | – | – |
| **Compression Model Card Authoring** | R | C | – | A | I | – |
| **Functional Equivalence Testing** | C | R | C | A | I | I |
| **Clinical Safety Validation** | C | R | – | A | I | I |
| **Staging Deployment** | – | C | R | A | – | – |
| **Production Deployment Approval** | – | C | R | A | I | – |
| **Production Monitoring & Alerting** | I | I | R | A | I | C |
| **Exception Approval (Minor)** | I | I | – | R | – | – |
| **Exception Approval (Major)** | – | – | – | C | R | – |

**Named Role Assignments:**

- **R (Responsible) – AI/ML Engineer:** The individual engineer assigned to the compression task ticket in Jira (`MLOPS` project).
- **R (Responsible) – Clinical AI Validation Specialist:** A designated specialist from the Clinical AI Validation team (`clinical-ai-val@meridian.com`), assigned per project.
- **R (Responsible) – MLOps Engineer:** The engineer on-call for production deployments, rostered in PagerDuty schedule `MLOps-Prod-Deploy`.
- **A (Accountable) – AI/ML Engineering Manager:** The direct manager of the assigned AI/ML Engineer (Director-level or above).
- **A (Accountable) – Chief AI Officer:** Dr. Marcus Rivera. Ultimate accountability for all Clinical AI Platform model safety.
- **C (Consulted) – Quality Assurance:** The QA team rostered on `qa-ai-systems@meridian.com`. Must be consulted for Clinical AI Platform staging sign-off per `SOP-AIML-002`.
- **I (Informed):** Notified via automated Confluence status page updates and Jira ticket transitions.

---

## 4. Policy Statements

Meridian Health Technologies, Inc. adopts the following high-level policy commitments regarding model compression and optimization:

1. **Safety First:** No model compression technique shall be applied to any Clinical AI Platform model unless it can be conclusively demonstrated, through pre-registered validation protocols, that functional equivalence and clinical safety are maintained post-compression. This is non-negotiable.

2. **Reproducibility Mandate:** All compression operations must be scripted and tracked in MLflow, with input artifacts, compression hyperparameters, output artifacts, and validation metrics immutably logged. Manual, ad-hoc compression in notebooks is prohibited outside of exploratory research branches (`feature/exploratory-*`), and results from such branches shall never be promoted to staging or production.

3. **Performance Gate Enforcement:** No compressed model shall pass the CI/CD pipeline gates in Jenkins (`jenkins.meridian.internal`) unless all performance metrics specified in Section 5.6.3 meet or exceed thresholds. A failed gate requires a documented root cause analysis (RCA) in Confluence before re-submission.

4. **Audit Trail Completeness:** Every compression event shall generate a "Compression Model Card" (Section 5.9, Appendix A) stored in the Meridian Model Registry (`registry.ml.meridian.internal`), linking the uncompressed and compressed model versions in an auditable chain.

5. **Hardware-Software Co-Design:** Target compression ratios and quantization schemas shall be dictated by the inference hardware target. For NVIDIA Triton Inference Server deployments on T4/V100/A100 GPUs, FP16 is preferred. For edge deployments on Coral TPU (Clinical AI Platform – bedside monitoring), INT8 QAT is mandatory.

6. **Continuous Monitoring:** Post-deployment, the MLOps team shall continuously monitor compressed models for data drift, concept drift, and prediction degradation, as specified in Section 7.

7. **Regulatory Compliance:** For models classified as high-risk under the EU AI Act Annex III, compression shall be treated as a "substantial modification" requiring re-evaluation of the technical documentation per Article 61. The Clinical AI Validation Specialist is the Responsible person for this re-evaluation.

---

## 5. Detailed Procedures

This section constitutes the operational core of this SOP. All ML compression workflows on Meridian systems shall adhere to the following steps. Deviation requires an approved exception (Section 8).

### 5.1 Step 0: Pre-Compression Feasibility Assessment

Before any code is written, the assigned AI/ML Engineer shall complete the "Compression Feasibility Checklist" (`SOP-AIML-017-F01`) in Confluence.

**Procedure:**
1.  Navigate to the Meridian AI/ML Confluence Space > SOP Templates > `SOP-AIML-017-F01: Compression Feasibility Checklist`.
2.  Populate the following fields:
    - **Model Registry ID:** Link to the uncompressed model in the Meridian Model Registry.
    - **Current Metrics:** Accuracy, F1-score, AUC-ROC, Inference Latency (P99, ms), Model Size (MB), MACs/FLOPs.
    - **Target Hardware:** Specify (e.g., NVIDIA T4, Coral TPU, CPU inference on x86_64).
    - **Compression Objective:** Latency reduction (< X ms P99), size reduction (< Y MB), or throughput increase (> Z queries/sec).
    - **Proposed Technique(s):** Quantization (QAT/PTQ), Pruning (Structured/Unstructured), Distillation. Justify selection based on hardware target.
    - **Risk Assessment:** Preliminary identification of layers sensitive to compression (initial KL divergence estimate if available).
3.  Schedule a 30-minute review meeting with the AI/ML Engineering Manager and (if Clinical AI Platform) the Clinical AI Validation Specialist.
4.  Upon approval, the Manager transitions the Jira ticket (`MLOPS-XXXX`) status from "To Do" to "In Progress."

### 5.2 Step 1: Environment and Artifact Preparation

**Procedure:**
1.  **Clone Repository:** `git clone git@github.meridian.com:ai-ml/model-compression.git` and checkout a new branch named `compression/<ModelRegistryID>-<Technique>` (e.g., `compression/MRM-1427-INT8-QAT`).
2.  **Activate Conda Environment:** Activate the approved, standardized compression environment:
    ```bash
    conda activate /shared/conda-envs/meridian-ml-compression-v3.1.0
    ```
    *Note: This environment contains PyTorch 2.1.0, TensorRT 8.6.1, ONNX Runtime 1.16.0, and NVIDIA's `nvidia-modelopt` library.*
3.  **Retrieve Model Artifact:** Use the Meridian CLI (`mcli`) to download the uncompressed model artifact (`.pt`, `.onnx`, or TensorFlow SavedModel) from the Model Registry.
    ```bash
    mcli model pull <ModelRegistryID> --output-dir ./artifacts/baseline
    ```
4.  **Load Calibration Data (if QAT/PTQ):** Retrieve the pre-registered calibration dataset split from the Meridian Data Lake (`s3://meridian-data-lake/curated/calibration/`). Use the `calibration_split.parquet` artifact associated with the baseline model in MLflow.

### 5.3 Step 2: Sensitivity Analysis

Identify layers vulnerable to precision loss.

**Procedure:**
1.  Execute the Meridian Sensitivity Profiler (`msp`) tool against the baseline model:
    ```bash
    msp profile --model ./artifacts/baseline/model.pt --data ./calibration_split.parquet --output ./artifacts/sensitivity_report.json
    ```
2.  The profiler injects simulated INT8 quantization noise layer-by-layer and measures the KL divergence of the output activation distributions.
3.  Review `sensitivity_report.json`. Layers with a KL divergence > 0.05 are flagged as "high sensitivity." For Clinical AI Platform models, any layer exceeding this threshold MUST be excluded from aggressive PTQ and shall instead use QAT with layer-specific bit-width allocation (e.g., INT8 for tolerant layers, FP16 for sensitive layers). This exclusion list must be codified in a `sensitive_layers.json` artifact and logged to MLflow.

### 5.4 Step 3: Compression Execution

#### 5.4.1 Quantization-Aware Training (QAT)

Mandatory for Clinical AI Platform INT8 models.

1.  Load the baseline FP32 model.
2.  Apply the NVIDIA Model Optimizer QAT recipe, referencing `sensitive_layers.json` for mixed-precision configuration.
3.  Fine-tune the model on the full training dataset for a minimum of 10 epochs, with a learning rate schedule decaying from a peak LR of 1e-5. The loss function remains the original task loss (e.g., Dice loss for segmentation, Cross-Entropy for classification).
4.  Export the QAT fine-tuned model to ONNX format with INT8 quantization annotations.
    ```python
    torch.onnx.export(
        qat_model,
        dummy_input,
        "artifacts/compressed/model_int8_qat.onnx",
        opset_version=17,
        quantization_parameters=True
    )
    ```

#### 5.4.2 Post-Training Quantization (PTQ)

Acceptable for MedInsight Analytics and HealthPay models ONLY where latency requirements are stringent and Functional Equivalence testing passes (Section 5.6).

1.  Load the baseline model.
2.  Instantiate a TensorRT `IInt8Calibrator` using the calibration data loader.
3.  Build the TensorRT engine with INT8 precision.
4.  Serialize the engine (`.engine` file).

#### 5.4.3 Structured Pruning (L1-Norm)

1.  Load baseline model.
2.  Apply `torch.nn.utils.prune.ln_structured` on convolutional and linear layers. Specify the pruning dimension (`dim=0` for output channels, the most common pattern for GPU speedup).
3.  Iteratively prune (0.1%–1.0% per pruning round, known as "gradual pruning") with interleaved fine-tuning epochs (1 epoch per round) to recover accuracy.
4.  After reaching the target parameter count, permanently remove pruned weights (`prune.remove` on all modules) and export to ONNX for deployment.

#### 5.4.4 Knowledge Distillation

1.  Instantiate the pre-defined, compact "student" architecture (e.g., ResNet-18 as student for a ResNet-152 teacher for a classification task).
2.  Train the student model using a combined loss function: `Loss = α * TaskLoss(student_output, labels) + (1-α) * KLLoss(softmax(student_logits/T), softmax(teacher_logits/T)) * T^2`.
    - `T` (Temperature) = 3.0 (default, tunable hyperparameter).
    - `α` (Weighting) = 0.7 (default, tunable hyperparameter).
3.  Log `T` and `α` in MLflow.

### 5.5 Step 4: Artifact Logging

All artifacts must be logged to the MLflow Tracking Server (`mlflow.meridian.internal`).

**Required artifacts:**
- `artifacts/compressed/model_compressed.<format>` (The compressed model file)
- `artifacts/sensitivity_report.json`
- `artifacts/sensitive_layers.json` (if applicable)
- `config/compression_config.yaml` (All hyperparameters used)
- `notebooks/compression_execution.ipynb` (The executed notebook or script)

**MLflow logging command:**
```bash
mlflow run . -e compression_job --experiment-name model-compression-v2 --run-name <ModelRegistryID>-compression-<Date>
```

### 5.6 Step 5: Post-Compression Functional and Performance Validation

This is the critical gate. No model proceeds without passing these tests.

#### 5.6.1 Functional Equivalence Testing (F.E.T.)

1.  **Dataset:** The held-out "Gold-Standard Test Set" (`s3://meridian-data-lake/curated/gold-test/<project_name>/`). This dataset must never have been used in training or hyperparameter tuning of the baseline or compressed models.
2.  **Execution:** The assigned AI/ML Engineer runs the Meridian `validate_equivalence.py` pipeline against both the baseline ONNX/TensorRT engine and the compressed ONNX/TensorRT engine.
3.  **Metrics Computed:**
    - Mean Absolute Error (MAE) on logits.
    - KL Divergence of output distribution.
    - Delta-Accuracy, Delta-F1, Delta-AUC-ROC (difference in task-specific metrics).
    - Latency benchmark (P50, P95, P99) on target hardware in `stg-ml-compute-02`.

#### 5.6.2 Clinical Safety Validation (Clinical AI Platform ONLY)

1.  **Executed By:** The Clinical AI Validation Specialist.
2.  **Subgroup Analysis:** The Specialist runs a pre-registered analysis plan (Jira ticket linked) that slices the Gold-Standard Test Set by protected characteristics and clinical subgroups (e.g., by age group [0-18, 19-45, 46-65, 66+], biological sex, comorbidity index). This ensures that performance does not degrade disproportionately in any specific subgroup due to compression-induced precision loss.
3.  **Sensitivity-Specificity Trade-off:** A DICE Similarity Coefficient map or AUC-ROC curve is generated for both baseline and compressed models, and overlaid, for every subgroup.

#### 5.6.3 Performance Gates (Mandatory Thresholds)

The compressed model’s performance, measured against the baseline on the Gold-Standard Test Set, must satisfy ALL applicable thresholds below. If any threshold fails, the compression attempt is immediately REJECTED.

**Table 4: Performance Gate Thresholds**

| Metric | Business Line | Absolute Tolerance | Relative Tolerance | Pass/Fail Criterion |
|---|---|---|---|---|
| **Delta-Accuracy** | All | ≤ 0.01 | ≤ 1.0% of baseline | Must Pass Both |
| **Delta-F1 Score** | Clinical AI | ≤ 0.015 | ≤ 1.5% of baseline | Must Pass Both |
| **Delta-AUC-ROC** | HealthPay | ≤ 0.005 | ≤ 0.5% of baseline | Must Pass Absolute |
| **KL Divergence (Output)** | Clinical AI | ≤ 0.020 | N/A | Must Pass |
| **KL Divergence (Output)** | MedInsight | ≤ 0.050 | N/A | Must Pass |
| **Maximum Subgroup Delta-Accuracy** | Clinical AI | ≤ 0.020 | N/A | Must Pass – No single subgroup can degrade > 2% absolute vs. baseline. |
| **Inference Latency P99** | All | N/A | ≤ 50% of baseline latency | Must Pass |

### 5.7 Step 6: Compression Model Card and Approval

1.  **Authoring:** The AI/ML Engineer authors a "Compression Model Card" (template in Appendix A of this SOP) directly in the Meridian Model Registry (`registry.ml.meridian.internal`), linking the baseline model (`ModelRegistryID-XXXX`) to the new, compressed model version (`ModelRegistryID-XXXX-v2-comp`).
2.  **The Card Documents:**
    - Compression technique, hyperparameters, and objective.
    - Sensitivity analysis summary (which layers were sensitive).
    - Full Functional Equivalence Testing results table, listing every metric against its pass/fail threshold.
    - Clinical Safety Validation summary (if applicable).
    - Target and achieved hardware benchmarks (latency, throughput, size).
3.  **Review & Sign-Offs:**
    - **Peer Review:** A second AI/ML Engineer reviews the card and code for reproducibility. (Jira transition: `In Review`).
    - **Clinical Sign-Off:** Clinical AI Validation Specialist signs off on the card. (Jira transition: `Validated`). This sign-off is the formal Article 17 AI Act Human Oversight checkpoint.
    - **Engineering Sign-Off:** AI/ML Engineering Manager approves promotion. (Jira transition: `Approved for Prod`).

### 5.8 Step 7: Deployment to Production

1.  **Promotion:** The MLOps Engineer uses a Jenkins job (`job/deploy-compressed-model`) to promote the approved compressed model artifact from the staging Model Registry stage to `Production`.
2.  **Canary Rollout:** Use an Istio `VirtualService` to split traffic: 5% to the new compressed model, 95% to the existing baseline for a period of 24 hours. The deployment dashboard (`grafana.meridian.internal/d/mlops-canary`) MUST be monitored during this window.
3.  **Full Rollout:** If no PagerDuty alerts (`alert-manager`) fire for the compressed model during the canary period, the AI/ML Manager authorizes a full traffic shift.
4.  **Decommission Old Model:** The uncompressed baseline model instance is kept in a `Retired` stage in the Model Registry for 90 days for audit trail integrity before purging, per `SOP-AIML-004` (Data Retention).

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Implementation | Applicable To |
|---|---|---|---|
| **TC-01** | **Reproducible Compression Pipeline** | All compression is executed via versioned `mlflow run` commands, not ad-hoc scripts. MLflow logs the full Conda environment snapshot. | All Models |
| **TC-02** | **CI/CD Gate Enforcement** | Jenkins pipeline (`jenkinsfile-model-compression`) programmatically enforces the Absolute and Relative Tolerance performance gates from Table 4. A failed test halts the pipeline. | Clinical AI, HealthPay |
| **TC-03** | **Immutable Golden Test Set** | The Gold-Standard Test Set (`s3://meridian-data-lake/curated/gold-test/`) has `read-only` IAM permissions for all roles except the `data-curator-admin` service account. Modifications require a break-glass process. | All Models |
| **TC-04** | **Registry Link Immutability** | Once a Compression Model Card links a `baseline` model to a `compressed` model, the link cannot be deleted or modified. A new compression run must be executed to create a new link. | All Models |
| **TC-05** | **Hardware-in-the-Loop (HIL) Testing** | Staging validation (`stg-ml-compute-02`) must use an identical hardware instance type to the production target (`prod-ml-compute-*`). | All Models |
| **TC-06** | **Automated CANCEL on PagerDuty Alert** | The Jenkins canary promotion job has a webhook listener for PagerDuty. If Meridian's `alert-manager` fires an `ml_model_*` severity `>=critical` alert during the 24-hour canary, the Jenkins job automatically reverts traffic to 100% baseline. | All Models |

### 6.2 Controls for High-Risk AI Systems (EU AI Act, Annex III)

For Clinical AI Platform models ONLY, the following enhanced controls are mandatory, fulfilling the requirements of Article 61 (Substantial Modification of High-Risk AI Systems).

- **AC-01 – Mandatory QAT:** Post-Training Quantization (PTQ) without fine-tuning is PROHIBITED for high-risk classification, detection, and segmentation models. The Quantization-Aware Training (QAT) procedure (Section 5.4.1) is mandatory to allow the optimizer to compensate for quantization error.
- **AC-02 – Article 61 Technical Documentation Update:** Before production deployment approval, the Clinical AI Validation Specialist must author a "Substantial Modification Memo" in the Meridian QMS (`qms.meridian.internal`), explicitly referencing SOP-AIML-017 and the Compression Model Card. This memo updates the EU AI Act technical documentation file (`TECH-DOC-XXXX`), detailing the modification rationale, risk analysis, and validation evidence.
- **AC-03 – Article 17 Human Oversight Checkpoint:** The "Clinical Sign-Off" gate in Section 5.7 is the codified Article 17 human oversight measure. This sign-off cannot be delegated to an automated system. The sign-off user authenticates via Okta MFA with a hardware token (YubiKey).
- **AC-04 – Article 62 Record-Keeping:** All logs from the compression pipeline (MLflow run ID, Jenkins build ID, Jira ticket ID, validation results, sign-off timestamps) shall be automatically aggregated and stored in the Meridian AI Audit Trail system (`audit.ai.meridian.internal`), an append-only log retained for a minimum of 10 years per EU MDR requirements.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | Metric | Target | Measurement Tool | Reporting Cadence |
|---|---|---|---|---|
| **KPI-01** | **Compression Success Rate** | > 90% of initiated compression jobs pass F.E.T. gates on first attempt. | MLflow / Jenkins aggregate | Monthly |
| **KPI-02** | **Mean Time to Compress (MTTC)** | From Jira "In Progress" to "Approved for Prod": < 14 calendar days for QAT; < 5 calendar days for PTQ. | Jira / Confluence | Monthly |
| **KPI-03** | **Post-Deployment Metric Stability** | Compressed model's primary metric (e.g., F1, AUC) does not drift > 2% absolute from staging validation value in the first 30 days post-deployment. | Production model monitoring dashboards (Evidently AI) | Continuous; reported weekly |
| **KPI-04** | **Latency Reduction Achievement** | > 95% of projects achieve their pre-stated latency reduction objective (Section 5.1). | Jenkins / MLflow | Monthly |
| **KPI-05** | **High-Risk Model Re-Validation Timeliness** | Article 61 memo (AC-02) filed within 5 business days of Clinical Sign-Off. | QMS dashboard | Monthly |

### 7.2 Dashboards

- **Operational:** The "Model Compression Operations" Grafana dashboard (`grafana.meridian.internal/d/aiml-compression-ops`) displays real-time pipeline status, compression job queue length, and compression success/failure rates.
- **Performance:** The "Compressed Model Performance" dashboard, generated per model by Evidently AI, overlays the primary metric (e.g., F1-score) and latency P99 of the compressed model against the baseline, updated hourly.
- **Audit:** The AI Audit Trail dashboard provides a read-only, time-sorted view of all artifacts, sign-offs, and logs for every compressed model.

### 7.3 Reporting

The AI/ML Engineering Manager shall present a monthly "Model Optimization and Safety Report" to the Chief AI Officer, summarizing the KPIs above, any PagerDuty alerts from compressed models, the exception log (Section 8), and a summary of upcoming compression plans for the next quarter.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Criteria
An exception to any mandatory procedure in this SOP may be requested under the following, limited circumstances:
- **Technical Infeasibility:** A specific compression technique mandated for a hardware target cannot be applied due to unsupported model operations in the ONNX export or TensorRT build graph.
- **Business Criticality:** A P0 customer-facing issue requires an immediate, temporary deployment of an uncompressed or partially-compressed model patch, bypassing the full validation pipeline.

### 8.2 Exception Request Procedure
1.  The requestor (AI/ML Engineer) files an "Exception Request" issue in the `MLOPS` Jira project, issue type `Exception`.
2.  The issue must detail:
    - **SOP Section ID:** The specific section for which the exception is sought.
    - **Rationale:** A detailed technical or business justification.
    - **Risk Assessment:** An analysis of the risks of deviating from the SOP.
    - **Mitigation Plan:** Proposed alternative controls and a timeline to revert the exception and achieve full compliance.
3.  **Exception Approval Matrix:**
    - **Minor Exception:** Waives a documentation/process step without impacting functional safety or model performance. Approved by the AI/ML Engineering Manager.
    - **Major Exception:** Waives or modifies a technical validation gate (e.g., bypassing a performance gate, skipping Clinical Safety Validation). MUST be approved by the Chief AI Officer (Dr. Marcus Rivera) and the VP of Engineering (David Park).

### 8.3 Exception Log and Review
All approved exceptions are logged in the `MLOPS` Jira project and linked to the model in the Model Registry. The monthly "Model Optimization and Safety Report" (Section 7.3) includes a log and status update for all active exceptions. No exception shall remain active for more than 90 days without re-approval.

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum

| Role | Training Module(s) | Frequency | Assessment |
|---|---|---|---|
| **AI/ML Engineer** | `TRAIN-AIML-017-ENG`: Model Compression Techniques and Meridian Tooling | Annually | Practical: Successfully execute a compression and validation pipeline on a provided reference model in a sandbox environment. Score > 90% on automated pipeline checks. |
| **Clinical AI Validation Specialist** | `TRAIN-AIML-017-CLIN`: Clinical Safety Validation for Compressed Models & EU AI Act Substantial Modification. | Annually | Written exam on Article 17 and 61 requirements and Clinical Safety Validation protocol. Score > 80%. |
| **MLOps Engineer** | `TRAIN-AIML-017-OPS`: Deployment and Canary Rollout for Optimized Models. | Annually | Practical: Successful execution of a mock canary rollout and automated rollback scenario. |

### 9.2 Training Tracking
All training completions and assessment scores are recorded in the Meridian Learning Management System (LMS), `meridian-learning`. Non-compliance will be flagged in Workday. Personnel with expired training are prohibited from participating in any phase of the compression lifecycle; their Jira account will be temporarily removed from the `ML-Compression-Approved` user group, preventing pipeline executions.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- `SOP-AIML-001`: AI/ML Model Development Lifecycle
- `SOP-AIML-002`: Model Validation and Staging for Clinical AI
- `SOP-AIML-004`: ML Data and Model Artifact Retention Policy
- `SOP-AIML-008`: Feature Store and Data Lake Access Control
- `SOP-AIML-012`: Use of MLflow for Experiment Tracking and Registry
- `SOP-AIML-022`: Production Model Monitoring and Incident Response
- `SOP-REG-005`: EU AI Act High-Risk System Conformity Assessment Procedure
- `SOP-SEC-101`: Secrets Management for ML Pipelines

### 10.2 External Regulatory References (Mandatory Reading)
- **Regulation (EU) 2024/1689** (The EU AI Act). Specifically: Article 2 (Scope), Article 6 (High-Risk Classification), Article 17 (Human Oversight), Article 61 (Substantial Modification of AI Systems), Article 62 (Record Keeping).

### 10.3 External Technical References
- Nagel, M., et al. "A White Paper on Neural Network Quantization." *arXiv:2106.08295* (Meridian-recommended reference).
- NVIDIA TensorRT Developer Guide (Version 8.6.x).
- ONNX Runtime Quantization Documentation.

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| **2.8** | 2025-02-02 | A. Sharma (Sr. ML Eng.) | D. Park (VP Eng.) | Minor revision: Updated MLflow links to new internal URI (`mlflow.meridian.internal`). Updated conda environment to `v3.1.0` for TensorRT 8.6.1 compatibility. No procedural changes. |
| **2.7** | 2024-11-15 | Dr. M. Rivera (CAIO) | D. Park (VP Eng.) | Major revision: Added full EU AI Act controls (AC-01 through AC-04) in Section 6.2. Added Clinical Safety Validation role to RACI. Added Subgroup Analysis requirements (Section 5.6.2) post-audit finding. |
| **2.6** | 2024-06-10 | K. Jensen (MLOps Lead) | D. Park (VP Eng.) | Added Section 5.8.2 Canary Rollout procedure using Istio. Updated Section 7.2 with Evidently AI dashboard links. Changed monitoring reporting from quarterly to monthly. |
| **2.5** | 2024-02-20 | A. Sharma (Sr. ML Eng.) | Dr. M. Rivera (CAIO) | First major release after pilot. Formalized Performance Gates (Table 4) with quantitative thresholds established from 6-month pilot. Mandated QAT for Clinical AI (Section 5.4.1). |
| **1.0** | 2023-09-01 | J. Doe (ML Eng.) | D. Park (VP Eng.) | Initial draft for pilot program. Basic procedures for PTQ and pruning. |