---
sop_id: "SOP-AIML-004"
title: "Model Versioning and Registry Management"
business_unit: "AI/ML Engineering"
version: "2.8"
effective_date: "2024-09-02"
last_reviewed: "2025-01-28"
next_review: "2025-07-28"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "SR 11-7"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Model Versioning and Registry Management

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the versioning, registration, storage, and lineage tracking of all artificial intelligence and machine learning (AI/ML) models developed, deployed, or procured by Meridian Health Technologies, Inc. The purpose of this document is to ensure the integrity, reproducibility, and auditability of models throughout their lifecycle, from initial experimentation to decommissioning, thereby supporting patient safety, regulatory compliance, and operational excellence.

### 1.2 Scope
This SOP applies to all models that meet any of the following criteria:
- Operate within the Clinical AI Platform, including those with FDA 510(k) clearance and CE marking under EU MDR.
- Underpin the HealthPay Financial Services business line, including credit scoring, fraud detection, and claims automation models subject to SR 11-7.
- Process Protected Health Information (PHI) within the MedInsight Analytics platform.
- Are deployed on the Meridian SaaS Platform infrastructure (AWS us-east-1, eu-west-1).
- Are developed using Meridian’s standard ML technology stack (PyTorch, TensorFlow, SageMaker, Kubeflow, MLflow).
- Are classified as high-risk AI systems under the EU AI Act, Annex III.

This SOP applies to all employees, contractors, vendors, and third parties who develop, test, deploy, monitor, or retire models on behalf of Meridian Health Technologies. Adherence is mandatory for all AI/ML Engineering, Clinical AI Products, and Financial Services teams. Non-compliance shall be escalated per Section 8 (Exception Handling and Escalation).

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **Artifact** | Any binary file, serialized object, or configuration file that is an output of the model training or build process and is required to deploy a model for inference (e.g., model weights, serialized tokenizers, feature transformation pipelines). |
| **Baseline Model** | The current champion model in production against which new candidate models are compared. |
| **Candidate Model** | A new model version registered in the model registry that is under evaluation to become the next Champion Model. |
| **Champion Model** | The specific version of a model that is actively serving predictions in a production environment. |
| **Challenger Model** | A candidate model deployed in a shadow or A/B testing mode alongside the Champion Model to evaluate real-world performance. |
| **Data Lineage** | The complete record of the origin, movements, and transformations of the datasets used to train and evaluate a model. |
| **Environment** | A logically separated infrastructure stack. Defined stages are `sandbox`, `development`, `staging`, and `production`. |
| **MLflow** | The designated enterprise platform for model registry, experiment tracking, and artifact storage, backed by an AWS S3 bucket and PostgreSQL metadata store. |
| **Model Card** | A structured, machine-readable and human-readable document describing a model's intended use, training data, performance metrics, and known limitations. Stored as `model_card.md` in the model registry. |
| **Model Lineage** | The directed acyclic graph (DAG) of all entities and processes that produced a model, including source code, training datasets, hyperparameters, and dependent base models. |
| **Model Registry** | A centralized system (MLflow Model Registry) that manages the lifecycle of all named models, their versions, stages, and associated artifacts and metadata. |
| **Promotion** | The act of transitioning a model version from one stage to another (e.g., Staging to Production). |
| **Reproducibility** | The ability to recreate the exact model artifacts given the original source code, data, and runtime configuration. |
| **Run** | A single execution of a model training or evaluation script, represented as a unique record in the MLflow Tracking server. |

## 3. Roles and Responsibilities

This section defines the roles and responsibilities for all parties involved in model versioning and registry management. The RACI matrix below specifies the Accountable (A), Responsible (R), Consulted (C), and Informed (I) parties for key tasks.

| Task / Activity | Data Scientist / ML Engineer | Model Registry Steward | VP of AI/ML or Delegate (Dr. Okafor / Mr. Liu) | CISO (Rachel Kim) | Quality Assurance (QA) | DevOps / MLOps |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Model Registration** | R, A | I | C | I | C | I |
| **Metadata & Lineage Entry** | R | A | I | I | I | C |
| **Stage Transition Approval** | I | C | A | C | C | R |
| **Artifact Integrity Verification** | C | R | I | I | A | C |
| **Registry Audit & Compliance Check** | I | R | A | C | I | C |
| **Security Control Enforcement** | I | C | I | A, R | I | C |
| **Decommissioning Approval** | C | R | A | C | I | C |

### 3.1 Named Role Descriptions

- **Data Scientist / ML Engineer:** The individual developing the model. Responsible for creating reproducible run scripts, registering models, and documenting all parameters, metrics, and artifacts in MLflow.
- **Model Registry Steward:** A designated role within the AI/ML Engineering team responsible for the overall hygiene of the MLflow Model Registry. This steward performs periodic audits, validates model card completeness, and manages merge conflicts or registration errors. This is a rotating role with a 6-month term, currently held by a Senior MLOps Engineer appointed by David Park.
- **VP of AI/ML or Delegate:** Dr. Aisha Okafor holds this authority for all Clinical AI Platform models. Robert Liu holds this authority for all HealthPay Financial Services models. They are the ultimate approvers for promoting any model to a production stage (`production` or `champion`).
- **Chief Information Security Officer (CISO):** Rachel Kim and her team are responsible for ensuring the security of the model registry and all stored artifacts, including KMS encryption policies, IAM role permissions, and network boundary controls.
- **Quality Assurance (QA):** An independent team responsible for verifying functional correctness and performing user acceptance testing before model promotion. For SR 11-7 models, QA performs an additional review, though it is not a fully independent validation function.
- **DevOps / MLOps:** The team responsible for maintaining the MLflow infrastructure, CI/CD pipelines (Jenkins, ArgoCD), and the automated artifact promotion system.

## 4. Policy Statements

4.1. **Centralized Registry Mandate:** All models within the scope of this SOP must be registered in the Meridian Central Model Registry (MLflow), accessible at `https://mlflow.internal.meridianht.com`. Local `.pkl` files, unversioned S3 buckets, or personal development instances are strictly prohibited for any model intended for deployment beyond a local sandbox.

4.2. **Immutability:** Once a model version is registered under a given name, its artifacts and critical metadata (run ID, metrics) are immutable. Any change, including hyperparameter correction, requires the registration of a new model version. The registry enforces this technically via a write-once tag policy on the backing S3 artifact bucket (`meridian-model-artifacts-prod`).

4.3. **Semantic Versioning:** All models must adhere to a `MAJOR.MINOR.PATCH` versioning scheme, aligned with the MLflow model version integer.
    - **MAJOR:** Incremented when a model is trained on a fundamentally new data source, has a new architectural design, or an incompatible change is made to the inference API.
    - **MINOR:** Incremented when the model is retrained on an extended dataset, a new feature is added, or hyperparameters are optimized.
    - **PATCH:** Incremented for bug fixes, dependency updates that do not change model output, or a non-functional change.

4.4. **Stage Gating:** A model version cannot be promoted to a subsequent stage without meeting all defined quality, security, and documentation gates (see Section 5.5). Automated checks are enforced via the Meridian CI/CD pipeline, and manual approvals are recorded in ServiceNow (SOW-AIML).

4.5. **Lineage Completeness:** Every promotion-ready model run must have a complete, auditable lineage linking it to the exact Git commit hash of the training code, the S3 URI of the training and validation datasets, and the Docker image SHA256 digest used as the runtime environment. This satisfies SOC 2 Common Criteria 8.1 (Change Management) and 8.4 (Monitoring of Changes).

4.6. **Transparency Documentation:** All models, regardless of business unit, shall be accompanied by a Model Card. This documentation makes the model’s intended purpose, performance characteristics, and technical implementation transparent to downstream consumers, internal auditors, and serves as the basis for external transparency reporting.

## 5. Detailed Procedures

### 5.1 Model Development and Run Tracking

1.  The Data Scientist clones the project repository from the Meridian Bitbucket instance and checks out a new feature branch (e.g., `feature/MOD-1023-optimize-xgboost`).
2.  All training and evaluation scripts must be instrumented with the Meridian MLflow tracking client library (`mlflow>=2.8.0`). The MLflow Tracking URI must be set via the standard environment variable: `MLFLOW_TRACKING_URI=https://mlflow.internal.meridianht.com`.
3.  For every run, the following must be logged via `mlflow.log_params()`:
    - `git_commit`: The full SHA1 commit hash from `git rev-parse HEAD`.
    - `training_dataset_uri`: The full S3 URI (e.g., `s3://meridian-datasets-prod/claims/diag_v2/2024-08-01.parquet`).
    - `docker_image`: The full Docker image URI with SHA256 digest.
4.  All model-specific metrics (e.g., accuracy, F1-score, RMSE, AUC-ROC) must be logged via `mlflow.log_metrics()`.
5.  The trained model artifact must be logged using `mlflow.sklearn.log_model()`, `mlflow.pytorch.log_model()`, or the appropriate flavor-specific function. A `signature` object reflecting the expected input schema must be included to enforce T-CON-03.

### 5.2 Model Registration Process

1.  Upon successful completion of a training run in `development`, the Data Scientist navigates to the Run details page in the MLflow UI.
2.  In the **Artifacts** section, the Data Scientist confirms the presence of the `model` folder, the `conda.yaml` or `requirements.txt` environment file, and the `input_example.json`.
3.  The Data Scientist clicks the **Register Model** button.
4.  A dialog box appears. The Data Scientist either selects an existing registered model name from the dropdown or enters a new name. Naming convention must follow the Business Unit prefix: `CLINICAL_<model_name>`, `FINANCIAL_<model_name>`, or `MEDINF_<model_name>` (e.g., `FINANCIAL_claims_fraud_v2`).
5.  The Data Scientist enters a rich-text description of this specific version in the **Description** field, summarizing the purpose of this run (e.g., "Retrained with Q3 2024 data to address drift; optimized learning rate.").
6.  The Data Scientist applies the tag `stage:development` using the MLflow UI.
7.  Upon registration, MLflow auto-assigns an integer version number (e.g., Version 17).

### 5.3 Artifact and Metadata Enrichment (Post-Registration)

An automated webhook in Jenkins (`meridian-ml-enrichment-pipeline`) triggers within 5 minutes of a new registration. This pipeline performs the following steps:
1.  **Lineage Graph Construction:** Queries the MLflow API to parse the Run's parameters. It retrieves the `git_commit`, `training_dataset_uri`, and `docker_image`.
2.  **S3 Artifact Signing:** Calculates and appends SHA256 checksums for all major artifacts (e.g., `model.pkl`, `tokenizer.json`) as tags (e.g., `artifact.checksum.sha256`).
3.  **Code Snapshot:** Pulls the exact Git commit from Bitbucket and stores a `.zip` archive of the training code in a secure lineage bucket (`meridian-lineage-prod`), tagging it with the Run ID.
4.  **Data Lineage Integration:** Queries an internal data catalog API (Apache Atlas) to attach business-level tags (e.g., `PHI:True`, `DataDomain:clinical_diag`) to the run if the dataset URI is registered in the catalog.
5.  The pipeline writes a JSON payload containing the full lineage data to a DynamoDB table (`model-lineage-store`) for fast audit queries.

### 5.4 Model Card Template and Completion

Each model version must have a `model_card.md` attached as an artifact. This file is generated from a standard template.

**Template Structure (`model_card_template.md`):**
```markdown
# Model Card: [Registered Model Name] - Version [Version Number]

## Model Overview
- **Registered Name:** `[e.g., CLINICAL_patient_risk_strat_v1]`
- **Version:** `[e.g., 17]`
- **Run ID:** `[e.g., 4a5b6c7d8e9f]`
- **Parent Run ID:** `[if fine-tuned]`
- **Business Unit:** `[AI/ML Engineering | Clinical AI | Financial AI]`
- **Owner:** `[Email of the Data Scientist]`

## Intended Use
- **Primary Use Case:** `[e.g., Stratify patients by risk of 30-day readmission]`
- **Intended Clinical/Operational Context:** `[e.g., A decision-support tool to flag high-risk patients for care managers. Not a primary diagnostic tool.]`

## Training Data and Lineage
- **Dataset URI:** `s3://[dataset_uri]`
- **Dataset Version:** `[e.g., claims_v2.0_2024-08-01]`
- **Data Card Reference:** `[Link to Data Card in Data Catalog]`
- **Preprocessing Steps:** `[e.g., Missing values imputed with median; categorical variables one-hot encoded; outliers clipped at 99th percentile.]`

## Model Architecture and Hyperparameters
- **Algorithm Type:** `[e.g., Gradient Boosted Trees, Transformer, CNN]`
- **Primary Library:** `[e.g., XGBoost 2.0, PyTorch 2.2]`
- **Key Hyperparameters:**
  - `learning_rate`: `[e.g., 0.01]`
  - `max_depth`: `[e.g., 6]`
  - `subsample`: `[e.g., 0.8]`

## Performance Metrics
- **Evaluation Criteria:** `[e.g., AUC-ROC, LogLoss, RMSE]`
- **Holdout Validation Score:** `[e.g., 0.92 AUC]`
- **Cross-Validation (K-Fold) Mean & Std Dev:** `[e.g., 0.91 ± 0.01 AUC]`
- **Slicing Performance (Fairness):** `[e.g., AUC for Cohort A: 0.91; Cohort B: 0.90]`

## Ethical and Fairness Review
- **Review Status:** `[Passed | Pending | Not Applicable]`
- **Review Ticket ID:** `[SOW-ETH-xxxx]`

## Limitations and Known Biases
- `[e.g., Model performance degrades by 8% for patients under 18.]`
- `[e.g., The model has not been validated to predict rare disease readmissions.]`
- `[e.g., Training data is biased toward the patient demographic of the Northeastern US.]`

## Technical Documentation
- This model card, alongside the stored input schema and training code snapshot, provides comprehensive technical information on the model's operation, architecture, and data requirements to a knowledgeable human operator.
```

The model card is stored in the MLflow run's artifact root. The promotion pipeline (Section 5.5) verifies its existence and that all fields are non-null.

### 5.5 Stage Promotion Procedure

Promoting a model version is a gated, automated process. The Data Scientist initiates a promotion request via the MLflow UI by requesting a stage transition (e.g., `Development` -> `Staging`). This action triggers the `model-promotion-pipeline` in Jenkins.

**Gate 1: Documentation Verification**
- **Check:** A Python script validates the existence and schema conformity of the `model_card.md` artifact. It also checks for the presence of an `input_example.json` and a signed `conda.yaml`.
- **Failure Action:** The pipeline terminates and sends an automatic notification to the requester via Slack (`#model-registry-alerts`) and email, detailing the specific failed check.

**Gate 2: Automated Testing and Reproducibility**
- **Check:** The pipeline spins up a dedicated EC2 instance from the Docker image referenced in the run's `docker_image` parameter. It executes the `mlflow models serve` command, then runs a battery of functional tests against the local REST endpoint.
- **Reproducibility Assertion:** The pipeline compares key evaluation metrics (AUC, F1) from the original run against the result of the re-run in the staging environment. They must match within a 0.1% tolerance.
- **Security Scan:** Snyk performs a vulnerability scan on the Docker image and all Python dependencies in `conda.yaml`. Critical and High severity vulnerabilities block promotion.

**Gate 3: Business Unit Approval**
- **Clinical AI Models:** The promotion request generates a ServiceNow change request (CR) assigned to Dr. Aisha Okafor's queue. The CR includes a summary of the model card, the reproducibility test results, and link to the lineage graph. Approval is required to proceed to `staging`.
- **Financial AI Models:** Similarly, a CR is generated for Robert Liu. In addition to the standard model card, a summary report on data drift from the currently deployed champion model is attached. Approval is required.
- An approval from a qualified reviewer, which includes Dr. Okafor or her delegate, confirms that the model's transparency documentation is sufficient for its downstream use.

**Gate 4: Staging Deployment**
- Upon approval, the pipeline uses ArgoCD to deploy the challenger model to the `staging` Kubernetes cluster (`eks-staging-us-east-1`). The model is deployed with a shadow traffic configuration, mirroring 5% of production traffic.

**Gate 5: Staging Verification (Soak Period)**
- A mandatory 24-hour soak period begins. A monitoring script verifies:
    - **No Model Deterioration:** The challenger model's output distribution does not statistically deviate from the Baseline Champion beyond a pre-defined threshold.
    - **Latency SLA:** Average inference latency is within 110% of the champion model's P95 latency.
    - **Error Rate:** The `5xx` error rate is below 0.1%.
- The QA team receives an automated Jira ticket (`AIML-QA-xxxx`) to perform User Acceptance Testing (UAT) against the staging endpoint. QA records their sign-off in this Jira ticket.

**Gate 6: Production Promotion and Champion Swap**
- After successful staging verification and QA sign-off, the Data Scientist submits a final promotion request from `Staging` to `Production`.
- This requires a final ServiceNow CR approval from the respective VP of AI/ML or their delegate (Okafor or Liu).
- Upon approval, the MLOps pipeline executes a zero-downtime deployment using Argo Rollouts (blue/green strategy) to replace the champion model. The old champion model version is moved to the `Archived` stage, and its artifacts remain immutable.

### 5.6 Model Retirement and Decommissioning

1.  A model is identified for decommissioning due to business need change, a superior champion model, or end-of-life.
2.  The Model Owner (Data Scientist) submits a "Model Decommissioning" request in ServiceNow.
3.  The Model Registry Steward verifies all lineage and artifacts are archived to a long-term immutable compliance store (`meridian-model-archive` Glacier Deep Archive bucket) with a 10-year retention policy.
4.  The VP of AI/ML (Okafor or Liu) and the CISO (Kim) approve the decommissioning request.
5.  The MLOps team removes the model from production, deletes its Kubernetes deployment, and moves its registry stage to `Archived`. The model name remains in the registry as a tombstone.

## 6. Controls and Safeguards

All controls in this section are designed to meet SOC 2 Common Criteria, specifically sections CC6.1 (Logical and Physical Access Controls) and CC8.1 (Change Management).

### 6.1 Access Control
- **IAM Roles (AWS):** Permissions to the `meridian-model-artifacts-prod` S3 bucket and `model-lineage-store` DynamoDB table are governed strictly by IAM roles.
    - `Role-DataScientist`: `s3:GetObject`, `s3:PutObject` on `development/*` and `staging/*` prefixes. No access to `production/*` prefix.
    - `Role-MLOpsPipeline`: `s3:GetObject`, `s3:PutObject` on all prefixes (used for promotion automation).
    - `Role-Auditor`: `s3:ListBucket`, `s3:GetObject` on all prefixes (read-only, used by the InfoSec team).
- **No Human `Production` Access:** No individual user or role has `PutObject` privileges to the `production/*` prefix in the artifact bucket. All artifact movement for production is gated by the CI/CD pipeline role.
- **MLflow Registry Authentication:** The central MLflow instance is integrated with Okta SSO and enforces Multi-Factor Authentication (MFA) for all human users.

### 6.2 Artifact Integrity
- **Cryptographic Hashing:** The enrichment pipeline (Section 5.3) generates a SHA256 checksum for every artifact > 1KB. These checksums are stored as tags on the MLflow run. The staging promotion process re-calculates the checksum and compares it against the stored value before deployment. A mismatch immediately fails the pipeline and creates a Critical PagerDuty alert for the CISO team.
- **Code Signing:** All training code commits must be signed via GPG key by the Data Scientist. The CI/CD pipeline verifies this signature against the Meridian internal keyserver.

### 6.3 Audit Logging
- **Comprehensive Trail:** All actions within the MLflow Model Registry are logged to a centralized, tamper-proof audit log in an AWS OpenSearch cluster (`meridian-audit-logs`). Log entries include the `user_arn`, `timestamp`, `action` (e.g., `create_registered_model`, `transition_model_version_stage`), `model_name`, and `version`.
- **SOC 2 CC8.1 Monitoring:** A Kibana dashboard built on this OpenSearch index visualizes all model stage transitions and is monitored by the DevOps team for anomalous activity.

### 6.4 Infrastructure Security
- **Network Isolation:** The MLflow Tracking and Registry servers reside within a private subnet in the `prod` VPC. Access is only possible through the Meridian VPN or via an internal network load balancer.
- **Encryption:** All model artifacts are encrypted at rest using AWS KMS Customer-Managed Keys (CMK) with annual automatic key rotation. Metadata in the PostgreSQL database uses AWS RDS Encryption.

## 7. Monitoring, Metrics, and Reporting

The MLOps team, led by the senior engineer reporting to David Park, is responsible for the implementation and maintenance of all monitoring dashboards.

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target | Measurement Tool | Reporting Cadence |
| :--- | :---: | :--- | :--- |
| **Registry Adoption Rate** (% of in-scope models in MLflow) | 100% | Quarterly manual audit against deployment manifests | Quarterly to CTO, CISO |
| **Model Card Completeness** (% of `production` models with all `model_card.md` fields non-null) | ≥ 99% | Automated script querying MLflow API | Weekly to VP of Engineering |
| **Reproducibility Gate Success Rate** | ≥ 95% | Jenkins pipeline `model_gateway` Prometheus metric `gate_reproducibility_success_total` / `gate_reproducibility_total` | Weekly |
| **Mean Time to Promotion (MTTP)** (from `dev` registration to `production`) | ≤ 7 calendar days | Calculated from audit log timestamps per model | Monthly to Chief AI Officer |
| **Security Vulnerability SLA Compliance** (Critical vulns patched before promotion) | 100% | Snyk scan results parsed from pipeline logs | Weekly to CISO |

### 7.2 Dashboards
A central Grafana dashboard, `SOP-AIML-004 Compliance Overview`, shall display the following panels:
- **Model Inventory by Stage:** A donut chart showing the count of model versions in each lifecycle stage.
- **Promotion Trend:** A time-series chart of promotions to `production` per week.
- **Registry Health:** A gauge showing the percentage of registered models that have been logged to (i.e., not stale) in the last 90 days.
- **Audit Log Volume:** A counter of all registry transactions over the last 24 hours, with an anomaly detection graph to spot deviations.

### 7.3 Reporting
The owner of this SOP (Dr. Marcus Rivera) is responsible for compiling a monthly Model Operations Report. This report is distributed to the CTO, all VPs of AI/ML, and the CISO. It summarizes the KPIs, lists all models promoted to `production` and `archived` in that period, and tracks open exceptions.

## 8. Exception Handling and Escalation

### 8.1 Exception Types
Meridian recognizes two types of exceptions to this SOP:
- **Technical Exception:** A technical limitation preventing strict compliance (e.g., an unsupported model flavor that cannot be fully packaged via the standard CI/CD pipeline).
- **Business Time-Critical Exception:** An urgent business need that requires an expedited promotion, bypassing some soak period gates (e.g., a critical zero-day model fix).

### 8.2 Exception Approval Process
1.  **Request Submission:** The Data Scientist submits an Exception Request via ServiceNow, selecting the relevant SOP (SOP-AIML-004), the policy statement in question, and the rationale.
2.  **Risk Assessment:** The Model Registry Steward and a member of the InfoSec team conduct a joint risk assessment within 1 business day, documenting the residual risk in the ServiceNow ticket.
3.  **Approval Matrix:**
    - **Promotion Gate Bypass:** Requires approval from the specific VP (Dr. Aisha Okafor or Robert Liu) and the CISO (Rachel Kim).
    - **Documentation Gap (e.g., incomplete Model Card):** Can be conditionally approved by the Director of AI/ML Engineering, with a mandatory remediation plan and deadline (no more than 30 days).
4.  **Tracking:** All active exceptions are tracked on the central ServiceNow dashboard and reviewed monthly. An exception that misses its remediation deadline is escalated to the Chief Technology Officer.

### 8.3 Escalation Path
- **Violation Detection:** Any automated gate failure or manual audit finding.
- **Level 1 Support:** Model Registry Steward. Handles technical troubleshooting, minor clarifications.
- **Level 2 Escalation:** VP of AI/ML (Okafor/Liu). Handles non-compliance for their respective business units, resource bottlenecks, and exception approvals.
- **Level 3 Escalation:** Chief AI Officer (Dr. Marcus Rivera). Responsible for cross-functional conflict resolution, SOP policy interpretations, and major regulatory risk decisions.

## 9. Training Requirements

### 9.1 Mandatory Training
All personnel defined in Section 3.1 (Roles and Responsibilities) must complete the following training modules:

| Module Title | Delivery Method | Provider | Frequency | Target Audience |
| :--- | :--- | :--- | :--- | :--- |
| **MLflow Registry Operations** | eLearning (LMS) & Hands-on Lab | AI/ML Platform Team | Annual + Onboarding | All Data Scientists, ML Engineers, MLOps |
| **Model Card Authoring and Ethical Review** | Instructor-Led Workshop | AI Ethics Committee | Bi-Annual | All Data Scientists, QA Team Leads |
| **SOC 2 Change Management for AI** | eLearning (LMS) | GRC Team (CISO Org) | Annual | MLOps, DevOps, Data Scientists |
| **SOP-AIML-004 Procedure Walkthrough** | Recorded Webinar & Quiz | SOP Owner (Rivera's delegate) | On Version Change > Minor | All personnel within scope |

### 9.2 Training Tracking
All training completion is tracked via the corporate Learning Management System (LMS), `MeridianLearn`. The Model Registry Steward has delegated access to run a monthly compliance report from the LMS for all assigned, in-scope personnel. Non-completion 90 days after assignment triggers an automatic escalation to the individual's manager and the owner of this SOP. Access to the production MLflow instance is technically dependent on an Active, compliant training status. An automated Okta integration will suspend a user's MLflow-production-group membership if their mandatory training status lapses by 10 days.

## 10. Related Policies and References

### 10.1 Internal Meridian Health SOPs

| SOP ID | Title | Relationship to this SOP |
| :--- | :--- | :--- |
| **SOP-CISO-002** | Data Encryption and Key Management | Governs the KMS keys used for artifact encryption (Section 6.4). |
| **SOP-SWENG-001** | Source Code Management and Branching | Defines the Git commit and tagging standards referenced in Section 5.1. |
| **SOP-AIML-001** | AI/ML Model Development Lifecycle | High-level SDLC for ML. This SOP executes the versioning phase of that lifecycle. |
| **SOP-AIML-005** | Model Monitoring and Drift Detection | Dictates the operational triggers for retraining a champion model, leading to new versions in this registry. |
| **SOP-QA-010** | User Acceptance Testing for Deployed Services | Governs the QA team's UAT procedures referenced in Gate 5 (Section 5.5). |
| **SOP-HR-015** | Employee Training and Compliance Tracking | Governs the LMS platform and mandatory training enforcement policy (Section 9). |

### 10.2 External Standards and Regulations

- **ISO/IEC 42001:2023** — Information technology — Artificial intelligence — Management system. Section A.8.1 (Operational planning and control).
- **EU AI Act** — Regulation (EU) 2024/1689, specifically Annex IV on technical documentation and Title VIII on transparency obligations.
- **SR 11-7** — Federal Reserve Board guidance on Model Risk Management.
- **SOC 2 Common Criteria** — Sections CC6.1 (Logical Access), CC8.1 (Change Management), and CC5.2 (Control Monitoring), as defined by the AICPA 2017 Trust Services Criteria.

## 11. Revision History

| Version | Date | Author | Description of Changes |
| :--- | :---: | :--- | :--- |
| 1.0 | 2022-06-15 | Dr. Aisha Okafor | Initial creation. Model Registry established on a legacy internal tool. |
| 1.5 | 2023-01-20 | David Park (VP, Eng) | Migrated registry to MLflow. Added semantic versioning policy. |
| 2.0 | 2023-08-01 | Dr. Marcus Rivera | Major rewrite. Added mandatory Model Cards, automated CI/CD promotion gates, and RACI matrix. Aligned with EU AI Act draft. |
| 2.3 | 2024-01-05 | Rachel Kim (CISO) | Enhanced Section 6 (Controls and Safeguards) with specific IAM roles and KMS policies for SOC 2 CC6.1 audit. |
| 2.6 | 2024-05-12 | Dr. Marcus Rivera | Added Financial AI Model specifics (SR 11-7), updated model card template, split QA from independent validation. |
| 2.8 | 2024-09-02 | Dr. Marcus Rivera | Finalized CE marking alignment. Updated promotion gates and soak period. Added GPG code signing requirement. Current version. |