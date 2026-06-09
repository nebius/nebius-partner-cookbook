---
sop_id: "SOP-AIML-011"
title: "ML Pipeline Orchestration"
business_unit: "AI/ML Engineering"
version: "2.2"
effective_date: "2024-11-10"
last_reviewed: "2025-11-24"
next_review: "2026-05-03"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: ML Pipeline Orchestration

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the end-to-end orchestration of Machine Learning (ML) pipelines at Meridian Health Technologies, Inc. The purpose of this document is to ensure that all phases of the ML lifecycle—from data ingestion and feature engineering through model training, validation, deployment, and monitoring—are executed in a standardized, repeatable, auditable, and secure manner. This SOP enforces compliance with the System and Organization Controls (SOC) 2 Type II trust services criteria and the National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF 1.0) across all business units deploying ML models into production environments.

This SOP defines the architectural principles, Directed Acyclic Graph (DAG) management standards, failure handling protocols, scheduling policies, and control mechanisms that govern the Meridian ML Platform (internally codenamed "Aether"). Given the company's regulated footprint—covering high-risk AI systems under the EU AI Act, PHI under HIPAA, and model risk under SR 11-7—rigorous pipeline governance is a critical operational and compliance requirement.

### 1.2 Scope

This SOP applies to:

- **All pipelines** that train, retrain, fine-tune, or deploy models classified as **production** or **shadow-production** within the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.
- **All environments**: development (`dev`), staging (`staging`), UAT (`uat`), production (`prod`), and disaster recovery (`dr`).
- **All personnel** involved in the design, development, deployment, and maintenance of ML pipelines, including full-time employees, contractors, and third-party vendors hosted within Meridian's AWS (us-east-1, eu-west-1) and Azure (DR) tenants.
- **All data classifications**: Public, Internal, Confidential, and Restricted (including PHI and PCI-DSS data processed by HealthPay).
- Models governed by **SOP-AIML-004 (Model Risk Management)**, **SOP-DS-007 (Data Governance for AI/ML)**, and **SOP-SEC-015 (Secure Development Lifecycle)**.

**Out of Scope:** Ad-hoc exploratory data analysis notebooks in the `sandbox` environment are not subject to this SOP unless the resulting artifacts are promoted to a production pipeline. Jupyter notebooks executed manually on local workstations are strictly prohibited from accessing production data sources.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **Aether** | Internal codename for the Meridian ML Platform, comprising Kubeflow Pipelines, MLflow, and SageMaker orchestration layers. |
| **Artifact** | Any versioned input or output of a pipeline step, including datasets, serialized models, feature stores, metrics, and explainability reports. |
| **Artifact Store** | MLflow-managed S3 bucket (`s3://meridian-ml-artifacts-{env}`) with versioning and WORM (Write Once Read Many) compliance for audit trails. |
| **Backfill** | The historical re-execution of a pipeline over a defined retrospective time window. |
| **CI/CD** | Continuous Integration / Continuous Deployment. Managed via GitHub Actions and ArgoCD. |
| **DAG** | Directed Acyclic Graph. The structural definition of pipeline components and their dependencies. |
| **Data Drift** | A change in the statistical properties of model inputs relative to the training distribution. |
| **Explainability Report** | A pipeline-generated document using SHAP/LIME, required for all high-risk models per EU AI Act Annex III. |
| **Guardrail** | A deterministic or heuristic layer that validates inputs, outputs, or intermediate states against predefined rules. |
| **KFP** | Kubeflow Pipelines. The primary orchestration engine for containerized ML workflows. |
| **MLIR** | ML Incident Report. A formal record of pipeline failures impacting patient safety or financial integrity. |
| **Pipeline Idempotency** | The property guaranteeing that re-executing a pipeline with identical inputs yields identical outputs and side effects. |
| **RTO / RPO** | Recovery Time Objective (4 hours) / Recovery Point Objective (1 hour) for critical ML pipelines. |
| **Step** | A single node within a DAG, corresponding to a containerized operation (e.g., `data-validation`, `training`). |

---

## 3. Roles and Responsibilities

The following RACI matrix delineates accountability for pipeline orchestration activities.

| Activity | AI/ML Engineer | ML Platform Team | Data Engineering | DevOps | CISO / Security | Compliance Officer | Business Unit VP |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Pipeline DAG Design & Implementation | **R, A** | C | C | C | I | I | I |
| Infrastructure Provisioning (K8s, GPUs) | C | **R, A** | I | R | I | I | I |
| Data Source Registration & Access Control | C | C | **R, A** | I | R | I | I |
| Security Scanning (Containers, Secrets) | I | R | I | **R, A** | C | I | I |
| SOC 2 Control Execution & Evidence | C | R | I | R | **A** | R | I |
| Model Risk Tier Classification | C | I | I | I | I | R | **A** |
| Pipeline Failure Triage (L1/L2) | R | **R, A** | R | I | I | I | I |
| Pipeline Promotion (Dev → Prod) | R | **A** | I | R | I | I | R |
| NIST AI RMF Map & Gap Analysis | C | R | I | I | C | **R, A** | C |
| EU AI Act Technical Documentation | R | C | C | I | I | **R, A** | C |
| Annual DR Test Execution | I | R | I | **R, A** | I | C | I |

**Key:**
- **R**: Responsible (executes the task)
- **A**: Accountable (approves and signs off; exactly one per row)
- **C**: Consulted
- **I**: Informed

### 3.1 Critical Named Roles

| Named Role | Individual | Responsibility |
| :--- | :--- | :--- |
| AI Governance Committee Chair | Dr. Sarah Chen, CEO | Ultimate accountability for AI-related risks. |
| Pipeline Orchestration Owner | Dr. Marcus Rivera, Chief AI Officer | Policy owner; approves exceptions to this SOP. |
| ML Platform Technical Lead | David Park, VP of Engineering | Operational health of the Aether platform; approves DAG architecture changes. |
| Security & Privacy Approver | Rachel Kim, CISO | Sign-off on container images, IAM roles, and data exfiltration controls. |
| Regulatory Compliance Approver | Thomas Anderson, CCO | Validates alignment with SOC 2, NIST AI RMF, and EU AI Act evidence collection. |

---

## 4. Policy Statements

All ML pipelines operating within Meridian Health Technologies, Inc. shall be designed, deployed, and monitored in accordance with the following policies.

### 4.1 Code-First, Declarative Design
All production pipelines must be defined as code (Python DSLs using KFP SDK v2.0+) and stored in version-controlled repositories (`git@github.com:meridian/ml-pipelines`). DAG definitions shall not be created or altered via UI-based tools in production. The pipeline definition file must include a complete `@pipeline` decorator with metadata labels for `risk_tier`, `data_classification`, and `regulatory_regime`.

### 4.2 Immutable Infrastructure
Pipeline steps shall execute on immutable, pre-built container images from the Meridian Container Registry (`meridian.jfrog.io`). The `latest` tag is forbidden in production—all production DAGs must reference images by their SHA256 digest.

### 4.3 Data Minimization
Steps must only request the minimum necessary data permissions (IAM roles scoped to `s3://meridian-data-{env}/dataset-name/`). Pipelines processing PHI must execute within the HIPAA-eligible VPC (`vpc-prod-phir`) and encrypt all data in transit (TLS 1.3) and at rest (AWS KMS CMK `arn:aws:kms:us-east-1:...:key/ml-key-prod`).

### 4.4 Comprehensive Audit Trails
Every pipeline execution must produce an immutable audit trail capturing the exact code commit hash, container image digests, input parameter values, data source snapshots (via Iceberg table snapshots), and output artifact lineage. This trail shall be stored in the MLflow Tracking Server (`mlflow.meridian.internal`) and backed up to the Compliance S3 bucket. Audit trails must be retained for a minimum of 7 years.

### 4.5 Failure as a First-Class Citizen
DAGs must explicitly define failure handlers at both the step and DAG level. Unhandled failures that result in silent data corruption or unauthorized data propagation constitute a Severity 1 (SEV1) incident per **SOP-INC-002 (Incident Response)**.

---

## 5. Detailed Procedures

### 5.1 Pipeline Design and Registration

This procedure governs the initial creation and promotion of a new ML pipeline.

#### 5.1.1 DAG Design Principles

Engineers must adhere to the following principles when constructing a DAG:

- **Single Responsibility:** Each step must perform one logically distinct operation (e.g., `validate_data`, `train_model`, `evaluate_bias`). Monolithic "mega-steps" are prohibited.
- **Idempotency by Default:** All steps, particularly data ingestion and feature engineering, must be idempotent. Data ingestion steps shall utilize "checkpoint" mechanisms to avoid processing the same source data window multiple times during retries. Idempotent tokens must be used where available.
- **Artifact Parity:** Every exit point of a step must produce a typed artifact registered in MLflow.
- **Guardrails as Sidecars:** Input and output validation shall run as exit-handlers or sidecar containers, never as inline code that can be bypassed by a step failure.

**Required Pipeline Metadata (`pipeline.yaml` embedded in `@pipeline` annotation):**
```yaml
pipeline_id: "diabetic-retinopathy-screening-v2"
risk_tier: "TIER_1_HIGH"
data_subject_type: "PHI"
regulatory_regimes: ["HIPAA", "EU_MDR_ANNEX_III", "SR11_7"]
slo_target_success_rate: 99.9
owner_team: "clinical-ai-screening"
```

#### 5.1.2 Step Types and Mandatory Configurations

Every pipeline DAG must include, at minimum, the following logical phases. Each phase corresponds to one or more KFP steps.

**Phase 1: Data Ingestion**
- **Tooling:** Apache Spark on KFP with Iceberg connectors; AWS Glue Data Catalog for schema registry.
- **Exit Condition:** An `DataIngestionMetrics` artifact must be emitted containing: row count, null ratio per column, schema fingerprint, and source data timestamp.
- **PHI Handling:** Steps connecting to the Electronic Health Record (EHR) FHIR endpoint must use the `meridian-ml-phi-operator` service account with temporary credentials from HashiCorp Vault.

**Phase 2: Data Validation & Drift Detection**
- **Component:** `GreatExpectationsValidator` (containerized, reference `meridian/ge-validator@sha256:...`).
- **Behavior:** The validator compares current source statistics against the baseline Expectation Suite stored in the MLflow Model Registry for that pipeline. A data drift score is calculated.
- **Exit Gate:** If the `drift_score` exceeds the configured `drift_threshold` (default: 0.25), the pipeline pauses and issues a `WARN` event to the ML Engineering Slack channel (`#ml-pipeline-alerts`), awaiting manual approval via the Aether UI console before proceeding.

**Phase 3: Feature Engineering**
- **Backend:** SageMaker Feature Store (Online and Offline stores).
- **Ingestion:** Transformed features are ingested via `PutRecord` API (Online) and bulk-load Spark job (Offline). Feature group names must follow the naming convention: `{business_unit}_{model_family}_{version}` (e.g., `clinicalai_dr_screening_v2`).
- **Lineage:** A `FeatureLineage` artifact must link each feature group to its originating Ingestion Run ID.

**Phase 4: Model Training**
- **Orchestration:** SageMaker Training Jobs submitted via KFP `Submit` step.
- **Hyperparameter Tuning:** SageMaker Automatic Model Tuning (Bayesian optimization) integrated as a sub-DAG.
- **Exit Condition:** Successful completion of the training job, with the `model.tar.gz` URI logged as an artifact.

**Phase 5: Model Evaluation & Registry**
- **Evaluation:** SageMaker Processing Job executing the `evaluation.py` script. Metrics (AUC-ROC, F1, Precision, Recall) are calculated and logged to MLflow.
- **Registry:** If metrics meet the registered "challenger" threshold defined in the Model Registry, a new `ModelVersion` is created with status `PENDING_MANUAL_APPROVAL`. This action triggers a notification to the Model Risk Committee. Registrations failing the threshold move to `ARCHIVED`.
- **Explainability:** A SHAP analysis is executed, and the resulting feature importance plot and full `SHAPExplanation` artifact are registered. This is mandatory for all Tier 1 and Tier 2 models per NIST AI RMF (Section 4.2) and EU AI Act technical documentation.

#### 5.1.3 Pipeline Registration (CI/CD Promotion)

1.  An ML Engineer creates a branch (`feature/<ID>-pipeline-definition`) containing the `pipeline.py` DAG definition, `container-images.yaml`, and updated Expectation Suites.
2.  A Pull Request (PR) is opened against the `main` branch. The PR triggers:
    -   Static Analysis (Pylint, Bandit, Checkov).
    -   Container vulnerability scanning (Trivy on referenced SHA digests).
    -   IAM Role drift detection (AWS IAM Access Analyzer).
3.  Approval from both the **ML Platform Technical Lead** and the **Security Approver** is required before merge.
4.  On merge to `main`, GitHub Actions compiles the `pipeline.py` to an Intermediate Representation (IR) YAML file, uploads it to S3 (`s3://meridian-artifacts/pipeline-ir/`), and ArgoCD detects the change. ArgoCD synchronizes the KFP engine, registering the new pipeline version in production.
5.  A successful registration creates an entry in the Service Catalog (`servicenow.meridian.com`) linking the pipeline ID to its runbooks.

### 5.2 DAG Management (Day-2 Operations)

#### 5.2.1 Parameterized Execution

All pipelines must be instantiable via parameter sets. These parameters must be strictly typed and validated by the KFP engine upon invocation.

**Common Parameter Schema:**
```python
from kfp.dsl import Input, Output, Dataset, Model, Markdown

@dsl.pipeline(
    name='diabetic-retinopathy-training-pipeline',
    description='End-to-end training pipeline for DR screening model v2'
)
def training_pipeline(
    # Data source window
    start_date: str = "2024-01-01",
    end_date: str = "2024-06-30",
    # Feature Store metadata
    feature_group_name: str = "clinicalai_dr_screening_v2",
    # Hyperparameter override (for retraining)
    hyperparameter_override: dict = {},
    # Model registry target stage
    target_stage: str = "Staging"
):
    ...
```

#### 5.2.2 Pipeline Triggers

Production pipelines may be triggered via the following mechanisms:

| Trigger Type | Mechanism | Authorized Pipelines | Governance |
| :--- | :--- | :--- | :--- |
| **Scheduled** | AWS CloudWatch Events → KFP CronJob | All Tier 1, Tier 2 weekly retrains; Tier 3 nightly | Schedule must be documented in `/ml-pipelines/schedules` in the repo. |
| **Event-Driven** | EventBridge Rule (e.g., `s3:ObjectCreated` in landing zone) | Data ingestion pipelines for MedInsight | Event patterns approved by Data Engineering. |
| **API-Driven** | Argo Workflow REST API call from authorized service (HealthPay Core) | Fraud detection scoring pipeline | API auth via mTLS and internal OAuth 2.0 tokens. |
| **Manual (Ad Hoc)** | Aether CLI (`meridian-ml execute --pipeline-id ...`) | Backfills, DR tests, model risk validation | Requires dual approval via ServiceNow Service Catalog REQ form. |

### 5.3 Failure Handling and Idempotency

Meridian's ML platform must treat pipeline failure not as an anomaly, but as an expected operational state. The system's reliability and compliance posture depend on graceful degradation and state consistency.

#### 5.3.1 Step-Level Retry Policies

Every KFP step must have an explicit `retry_policy` defined within the DAG.

```yaml
# Inside the step definition
retry_policy:
  type: "EXPONENTIAL_BACKOFF"
  max_retries: 3
  backoff_base_seconds: 30
  max_backoff_seconds: 600
  retryable_exit_codes: ["TRANSIENT"]
```

**Exit Code Mapping:**
- **Exit Code 0:** Success.
- **Exit Code 1:** Failure (Fatal — Data Corruption). **Do not retry.** Fail the entire DAG and immediately create a SEV1 incident.
- **Exit Code 2:** Failure (Transient — External Dependency). **Retry.** (e.g., network timeout to Vault, Spark cluster resource contention).
- **Exit Code 3:** Failure (Validation — `drift_threshold` exceeded). **Do not retry.** Follow the gate logic specified in 5.1.2 Phase 2.

#### 5.3.2 DAG-Level Failure Handlers (Exit Handlers)

A DAG-level `exit_handler` step is mandatory. This step executes **once** regardless of the DAG's ultimate success or failure state.

**Exit Handler Logic:**
1.  **If DAG Status is SUCCESS:**
    -   Send a Heartbeat metric (`pipeline.success`) to CloudWatch.
    -   Optionally trigger a downstream DAG (e.g., auto-deploy to Staging).
2.  **If DAG Status is FAILED:**
    -   Collect diagnostic artifacts: last 100 lines of logs from each failed step, DAG run ID, and status of all steps.
    -   Publish these artifacts to a dedicated triage bucket (`s3://meridian-ml-triage/`).
    -   Create a PagerDuty alert with severity based on `risk_tier`:
        -   **Tier 1:** PagerDuty Priority P1 (Critical). Escalation to on-call ML Engineer and Platform Lead within 5 minutes.
        -   **Tier 2:** PagerDuty Priority P2 (Warning). Escalation within 2 hours.
        -   **Tier 3:** No PagerDuty alert. Issue automatically logged to the `#ml-pipeline-alerts` Slack channel.

#### 5.3.3 Ensuring Idempotency

To guarantee reproducibility for SOC 2 audit evidence (CC6.1, CC6.2) and NIST AI RMF characteristics (Transparent, Reliable):

1.  **Time-Windowed Processing:** Pipelines must not rely on "current" system time. They must process data within an explicit, parameterized time window.
2.  **Output Determinism:** Training steps must seed random number generators using a derivation of the Pipeline Run ID. The seed must be logged as a parameter.
3.  **Write-Once, Read-Many (WORM):** Once a pipeline run completes successfully, its output artifacts shall be immutably versioned in the Artifact Store. Subsequent backfill runs create new versions.
4.  **Idempotency Test:** The CI/CD pipeline (Section 5.1.3) must automatically execute an idempotency test for any Tier 1 pipeline. This test runs the DAG twice with identical inputs and asserts byte-for-byte equality of all output artifacts.

---

## 6. Controls and Safeguards

The following technical and administrative controls are implemented to operationalize SOC 2 Trust Services Criteria (TSC) and NIST AI RMF functions across the pipeline lifecycle.

### 6.1 Technical Controls

| Control ID | Control Name | Description | SOC 2 Ref. | NIST AI RMF Ref. |
| :--- | :--- | :--- | :--- | :--- |
| **TC-PIPE-01** | Immutable Artifact Lineage | All pipeline runs produce a cryptographic lineage record (MLflow Run UUID) that chains input data snapshots (Iceberg), container images (digest), and output model artifacts. This record cannot be altered. | CC6.1, CC6.2 | GOVERN 4.1, MAP 5.1 |
| **TC-PIPE-02** | Least-Privilege IAM Roles | Each pipeline step executes under a distinct IAM role scoped to the minimum required permissions. Roles are temporary, generated by Vault, and valid only for the step's execution duration. | CC6.1, CC6.3, P6.4 | GOVERN 4.2 |
| **TC-PIPE-03** | Guardrails | Input and output guardrails run as sidecar containers. They validate feature schemas, data types, value ranges, and detect the presence of PII/PHI outside permitted steps using AWS Comprehend-based scanning. | CC7.1, CC7.2 | MEASURE 2.3 |
| **TC-PIPE-04** | Environment Segregation | Dev, Staging, and Production pipelines execute in physically separate AWS accounts (`meridian-ml-dev`, `meridian-ml-staging`, `meridian-ml-prod`) with zero network transitivity between dev and prod. | CC6.1, CC6.2 | GOVERN 5.1 |
| **TC-PIPE-05** | Container Image Hardening | Base images are Meridian-Hardened Linux (CentOS Stream 9). Images undergo Trivy vulnerability scanning before promotion. Images with CRITICAL or HIGH vulnerabilities are blocked. | CC7.1 | GOVERN 4.3, MANAGE 4.1 |
| **TC-PIPE-06** | Secret Rotation | All secrets (API keys, service account tokens) are managed in HashiCorp Vault and rotated every 90 days. Pipelines authenticate via short-lived Kubernetes service account tokens, not static credentials. | CC6.1, CC6.3 | GOVERN 4.2 |

### 6.2 Administrative Controls

| Control ID | Control Name | Description | Frequency | SOC 2 Ref. | NIST AI RMF Ref. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AC-PIPE-01** | Pipeline Access Review | The CISO reviews all IAM roles and KFP user RBAC mappings. | Quarterly | CC6.1, CC6.2 | GOVERN 4.2 |
| **AC-PIPE-02** | SOC 2 Control Evidence Collection | The Compliance Officer extracts MLflow audit trails for the defined review period to demonstrate adherence to CC6.1 (Logical Access), CC7.1 (Change Management), and PI1.1 (Processing Integrity). | Semi-Annual (before audit) | All SOC 2 CC-Series | GOVERN 5.2 |
| **AC-PIPE-03** | NIST AI RMF Map & Gap | The Compliance Officer updates the Meridian "AI Trust Map," linking pipeline controls to NIST AI RMF sub-categories (e.g., `GOVERN 4.2`, `MAP 5.1`, `MEASURE 2.13`). Gaps identified are entered as risk items in Archer GRC. | Synchronized with NIST AI RMF updates (current: v1.0) | N/A | ALL (Functions: GOVERN, MAP, MEASURE, MANAGE) |
| **AC-PIPE-04** | Pipeline Design Review | A cross-functional Architecture Review Board (ARB) consisting of the ML Platform Lead, CISO, and a Data Engineering Lead reviews DAG designs for new Tier 1 pipelines. | Per New Pipeline (Tier 1) | CC7.1, CC7.2 | GOVERN 4.1, MANAGE 4.2 |
| **AC-PIPE-05** | Model Risk Tiering | The Model Risk Committee (Chair: Dr. Rivera) formally assigns `risk_tier` classifications. A `TIER_1_HIGH` classification mandates additional explainability and bias monitoring. | Annual & Trigger-based | N/A | GOVERN 5.1 |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The Operations team shall track the following measurable metrics to ensure the health and integrity of the orchestration layer. These KPIs are integrated into the centralized Grafana dashboard "Meridian ML Platform Health."

| KPI ID | Metric | Target/SLA | Measurement Tool | Responsible Party |
| :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | Tier 1 Pipeline Success Rate | ≥ 99.9% (monthly) | CloudWatch Alarms, Grafana | ML Platform Team |
| **KPI-02** | Cross-Account Promotion Failure Rate | ≤ 1% of promotions | GitHub Actions / ArgoCD Logs | DevOps |
| **KPI-03** | Vulnerability Drift Time | Zero CRITICAL vulns for > 24 hours | JFrog Xray | CISO (Rachel Kim) |
| **KPI-04** | Mean Time To Detect (MTTD) for SEV1 | ≤ 5 minutes from failure | PagerDuty, Prometheus AlertManager | SRE |
| **KPI-05** | Mean Time To Resolve (MTTR) for SEV1 | ≤ 4 hours | ServiceNow | Dr. Marcus Rivera |
| **KPI-06** | Idempotency Test Pass Rate | 100% (blocking CI gate) | Custom GitHub Action Runner | ML Engineers |
| **KPI-07** | Audit Record Completeness | 100% of runs have matching MLflow and S3 artifacts | MLflow Audit API | Compliance Officer |

### 7.2 Dashboards

| Dashboard Name | Scope | Primary Consumers |
| :--- | :--- | :--- |
| **Aether - Global Platform Health** | Aggregate KPI-01, KPI-03, KPI-04 across all production pipelines in `prod` accounts. | ML Platform Team, SRE, VP of Engineering |
| **Aether - Pipeline Run Details** | Per-pipeline DAG execution graphs, step durations, artifact links to MLflow. | AI/ML Engineers |
| **Aether - Compliance Audit** | Control-specific dashboard showing lineage completeness, vulnerability scans, IAM role usage (for RBAC reviews). | CISO, Compliance Officer, Internal Audit |

### 7.3 Reporting Cadence

- **Daily:** Automated Slack digest to `#ml-pipeline-operations` with 24-hour statistics on KPIs 01, 04, and 05.
- **Weekly:** ML Platform Team stand-up reviews open pipeline defects and ServiceNow Incident Tickets.
- **Monthly:** The ML Platform Technical Lead prepares a "State of Aether" slide deck for the Chief AI Officer, including SLA adherence (KPIs 01-05) and an exception log review.
- **Quarterly:** Formal SOC 2 control execution and evidence logwalk with the Compliance Officer and CISO. The VP of Engineering presents a quarterly infrastructure review to the AI Governance Committee.
- **Trigger-Based:** A post mortem is mandatory for any Tier 1 pipeline failure that violates its SLO (SOP-AIML-004). The resulting document must map the failure to a control gap against the NIST AI RMF (MEASURE 2.13).

---

## 8. Exception Handling and Escalation

### 8.1 Operational Escalation Path

Pipeline failure response shall follow a tiered model aligned with the Severity levels defined in **SOP-ITSM-001 (IT Service Management)**.

1.  **Automated Triage (Level 0):** The pipeline executes its retry policy (see 5.3.1). For transient errors, the system handles recovery.
2.  **On-Call Alert (Level 1):** If retries are exhausted without success, the DAG exit handler publishes a PagerDuty alert to `on-call-ml-eng@meridian.com`. The on-call engineer acknowledges it within 5 minutes (SEV1) or 30 minutes (SEV2) and begins triage in the `#incident-response` Slack channel.
3.  **Platform SME Engagement (Level 2):** If the on-call engineer cannot resolve the issue within 1 hour (SEV1), or if the issue relates to KFP engine health or an AWS service failure, the ML Platform Lead is engaged.
4.  **Executive Notification (Level 3):** If the issue persists beyond the MTTR SLA (4 hours for SEV1), the VP of Engineering (David Park) and Chief AI Officer (Dr. Marcus Rivera) are notified and assume authority.

### 8.2 Exception Process

Exceptions to the mandatory controls outlined in this document must be formally requested, justified, and approved prior to implementation.

**Exception Request Process:**
1.  **Initiation:** The requestor (any role) submits a ServiceNow "Policy Exception" ticket, attaching a completed **"SOP-AIML-011 Exception Request Template"** (Form ID: `MER-FORM-011`).
2.  **Justification:** The form must include:
    -   Specific Control ID (e.g., `TC-PIPE-02`) being excepted.
    -   Detailed technical justification for why compliance is not currently feasible.
    -   Proposed compensating control with equivalent security or compliance value.
    -   Explicit risk acceptance statement for the duration of the exception.
3.  **Review & Approval:**
    -   **Technical Review:** ML Platform Technical Lead and CISO review for technical soundness.
    -   **Compliance Review:** Compliance Officer (Thomas Anderson) reviews for regulatory impact.
    -   **Final Approval:**
        -   Pipeline exceptions (TC controls): **Chief AI Officer (Dr. Marcus Rivera)**.
        -   Security exceptions (IAM, secrets): **CISO (Rachel Kim)**.
4.  **Sunsetting:** All exceptions must have a defined expiration date, not to exceed 90 days. Exceptions may be renewed via the same full review process. An active exception log is maintained in ServiceNow and reviewed at the monthly pipeline review.

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Training Module | AI/ML Engineers | ML Platform Team | DevOps | Compliance Officer |
| :--- | :---: | :---: | :---: | :---: |
| **SOP-AIML-011 Awareness & Fundamentals** | **R** (Annual) | **R** (Annual) | **R** (Annual) | **R** (Annual) |
| **Kubeflow Pipelines Deep Dive** | **R** (Version-update) | **R** (Version-update) | I | I |
| **Writing Secure ML Pipelines (SDLC)** | **R** (Biannual) | **R** (Biannual) | **R** (Biannual) | I |
| **SOC 2 & AI RMF Evidence Collection** | I | **R** (Before Audit) | I | **R** (Before Audit) |
| **Incident Response & SEV1 Triage** | **R** (Annual Drill) | **R** (Annual Drill) | **R** (Annual Drill) | I |

### 9.2 Training Tracking

All mandatory role-based training is assigned and tracked within the Meridian **Skillsoft LMS**. The "SOP-AIML-011 Awareness" module is prerequisite to gaining write access to the `meridian/ml-pipelines` GitHub repository. Completion reports are generated quarterly by the HR Systems team and provided to the Compliance Officer for inclusion in the SOC 2 annual evidence package. Incomplete mandatory training for 30 days results in escalation to the individual's manager and a 7-day remediation window before conditional access revocation.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
| :--- | :--- | :--- |
| SOP-AIML-004 | Model Risk Management | Defines model tiering (`risk_tier`) and approval workflow triggers referenced here. |
| SOP-DS-007 | Data Governance for AI/ML | Defines data classification labels and access patterns enforced by pipeline IAM roles. |
| SOP-SEC-015 | Secure Development Lifecycle (SDLC) for AI | Governs code scanning and container build process enforced in CI/CD. |
| SOP-INC-002 | Incident Response and Escalation | Defines SEV definitions, PagerDuty rotations, and the Incident Commander role. |
| SOP-ITSM-001 | IT Service Management | Governance of the ServiceNow catalog for Exception and REQ forms. |
| SOP-GDPR-001 | GDPR & Data Subject Rights | Governs the inclusion of a "Right to be Forgotten" sweep step in relevant pipelines. |

### 10.2 External Standards

- **AICPA TSP Section 100, 2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (SOC 2):** Specifically Common Criteria Series `CC6.1` through `CC6.8` (Logical and Physical Access Controls), `CC7.1` through `CC7.5` (System Operations), `CC8.1` (Change Management), and `PI1.1-PI1.5` (Processing Integrity).
- **NIST AI RMF 1.0 (AI 100-1):** Core functions mapped: GOVERN 4.1-4.3 (Organizational Culture), GOVERN 5.1-5.2 (Policies), MAP 5.1 (Data/Process context), MEASURE 2.3 (Model Evaluation), MEASURE 2.13 (Impact Assessment), MANAGE 4.1-4.3 (Risk Treatment).
- **EU Artificial Intelligence Act (EU AI Act) Annex III (High-Risk Systems):** Technical Documentation and record-keeping requirements for medical diagnostic pipelines.
- **OCC SR 11-7 / FRB SR 12-11:** Model Risk Management guidance applicable to HealthPay credit risk models.

---

## 11. Revision History

| Version | Date | Author(s) | Revision Summary |
| :--- | :--- | :--- | :--- |
| 1.0 | 2022-04-15 | Dr. Marcus Rivera, Alice Chen (ML Platform) | Initial release. Focused exclusively on Kubeflow and CI/CD integration. |
| 1.1 | 2022-11-02 | David Park | Added Data Drift detection gate and `exit_handler` logic for Tier 1 models. Updated MTTR SLA to 4 hours based on SEV1 post mortem (INC-2022-084). |
| 2.0 | 2023-06-18 | Dr. Marcus Rivera, Thomas Anderson (CCO) | Major revision. Introduced formal RACI matrix. Integrated SOC 2 control mapping and NIST AI RMF v1.0 Map & Gap procedure (AC-PIPE-03). |
| 2.1 | 2024-03-01 | Rachel Kim (CISO) | Enhanced technical controls (TC-PIPE series). Mandated mutable-free tags in production. Introduced Immutable Artifact Lineage (TC-PIPE-01). Refined IAM role rotation to 90-day Vault-based. |
| 2.2 | 2024-11-10 | Dr. Marcus Rivera | Post-EU MDR CE marking update. Added mandatory Explainability Report step for all EU-bound Tier 1 and Tier 2 models in DAG phase 5. Updated regulatory mapping for EU AI Act Annex III. Formalized quarterly Pipeline Access Review (AC-PIPE-01). Bumped KFP SDK requirement to v2.0+. Expiration date pushed to 2026. |