---
sop_id: "SOP-AIML-015"
title: "Foundation Model and Transfer Learning Usage"
business_unit: "AI/ML Engineering"
version: "2.8"
effective_date: "2024-10-02"
last_reviewed: "2025-10-17"
next_review: "2026-04-02"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Foundation Model and Transfer Learning Usage

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework governing the evaluation, selection, procurement, fine-tuning, deployment, and ongoing monitoring of foundation models and transfer learning workflows across Meridian Health Technologies, Inc. ("Meridian"). As the organization increasingly leverages large-scale pre-trained models—including large language models (LLMs), vision transformers, and multi-modal architectures—across its Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and Meridian SaaS Platform, a unified and rigorous governance framework is essential to ensure patient safety, regulatory compliance, model robustness, intellectual property protection, and alignment with Meridian's ethical AI principles.

This SOP addresses the unique risks introduced by foundation models, including but not limited to: supply chain vulnerabilities, upstream data provenance uncertainty, catastrophic forgetting during fine-tuning, open-source license contamination, emergent behaviors not present in pre-deployment testing, and regulatory obligations under the EU AI Act for high-risk AI systems that integrate pre-trained components.

### 1.2 Scope

This SOP applies to:

- **All business units** within Meridian Health Technologies, including Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.
- **All personnel** involved in the lifecycle of AI/ML models, including AI/ML Engineers, Data Scientists, MLOps Engineers, Product Managers, Clinical Domain Experts, Compliance Officers, Legal Counsel, and Procurement Specialists.
- **All foundation model types**, including but not limited to: text-based LLMs (e.g., GPT, ChatGPT, Llama families), vision transformers (ViT), diffusion models, multi-modal encoder-decoders, embedding models, and any model with parameter counts exceeding 100 million that is pre-trained on broad, uncurated datasets and intended for adaptation via transfer learning.
- **All adaptation methodologies**: full fine-tuning, parameter-efficient fine-tuning (PEFT) including LoRA, QLoRA, and adapter layers, prompt engineering, retrieval-augmented generation (RAG), reinforcement learning from human feedback (RLHF), and distillation.
- **All deployment contexts**: development, staging, production, and production-shadow environments.
- **All geographic regions** where Meridian operates, with specific attention to products deployed in the European Union and subject to the EU AI Act.

### 1.3 Out of Scope

- Models trained entirely from scratch on Meridian-curated datasets without leveraging pre-trained weights (see SOP-AIML-012, "Traditional Model Development Lifecycle").
- Simple heuristic or rule-based systems with no learned parameters.
- Third-party SaaS products where Meridian has no access to model weights or training pipelines and serves solely as an end-user (see SOP-VEND-008, "Third-Party AI Vendor Risk Management").

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|----------------|------------|
| **Foundation Model** | An AI model trained on broad data at scale, designed for adaptability across a wide range of downstream tasks. Characterized by large parameter counts (typically > 100M), emergent capabilities, and the intent to serve as a base for transfer learning. |
| **Transfer Learning** | The process of adapting a pre-trained foundation model to a specific downstream task using domain-specific data. Includes full fine-tuning, PEFT, and few-shot in-context learning. |
| **PEFT** | Parameter-Efficient Fine-Tuning. Techniques that adapt a foundation model by training only a small subset of parameters (e.g., LoRA adapters), leaving the base weights frozen. |
| **LoRA** | Low-Rank Adaptation. A specific PEFT method that injects trainable rank decomposition matrices into transformer layers. |
| **Model Card** | A structured document, aligned with NIST AI RMF and EU AI Act transparency requirements, detailing a model's intended use, training data, performance characteristics, limitations, and evaluation results. |
| **Open-Weights Model** | A model whose trained parameters are publicly released, either under permissive (e.g., Apache 2.0, MIT) or restrictive (e.g., RAIL, Llama Community License) terms. Distinct from fully open-source models. |
| **Supply Chain Risk** | The composite risk arising from dependencies on upstream model providers, training data of unknown provenance, unverified pre-processing pipelines, and latent malicious code or poisoned weights introduced during pre-training. |
| **Catastrophic Forgetting** | The tendency of a neural network to abruptly lose previously acquired knowledge upon learning new information during fine-tuning. |
| **EU AI Act** | Regulation (EU) 2024/1689 laying down harmonized rules on artificial intelligence. |
| **High-Risk AI System** | As defined in Annex III of the EU AI Act. Includes Meridian's Clinical AI decision support, diagnostic imaging analysis, and patient risk scoring products. |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework (NIST AI 100-1). |
| **RLHF** | Reinforcement Learning from Human Feedback. Training paradigm where a reward model, trained on human preference data, guides policy optimization. |
| **RAG** | Retrieval-Augmented Generation. Architecture pattern combining a retrieval system with a generative model to ground outputs in external knowledge sources. |
| **BOM** | Bill of Materials. A structured inventory of all components in an AI system, including base model, datasets, adapters, prompts, and tooling dependencies. |
| **DPO** | Data Protection Officer. Dr. Klaus Weber, Meridian's appointed DPO based in Berlin. |
| **CAIO** | Chief AI Officer. Dr. Marcus Rivera. |
| **AI-GC** | AI Governance Committee. Board-level committee established 2024, chaired by the CAIO. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines accountability for activities governed by this SOP. Roles are mapped to specific Meridian positions and teams.

| Activity | Accountable (A) | Responsible (R) | Consulted (C) | Informed (I) |
|----------|-----------------|-----------------|---------------|--------------|
| Foundation Model Selection & Approval | CAIO | AI/ML Engineering Lead | AI-GC, General Counsel, CISO | VP of relevant Business Unit |
| Model Card Completion & Maintenance | AI/ML Engineering Lead | Model Developer | Clinical Domain Expert, Compliance Officer | CAIO |
| Pre-Deployment Safety & Bias Evaluation | VP of Clinical AI Products | MLOps Validation Team | Dr. Priya Patel (CMO), General Counsel | AI-GC |
| Open-Weights License Compliance Review | General Counsel | IP Legal Counsel | OSS Program Office | CAIO, CISO |
| Supply Chain Risk Assessment | CISO | Security Architecture Team | AI/ML Engineering Lead | CAIO, CCO |
| EU AI Act Conformity Assessment | CCO | Regulatory Affairs Specialist | DPO, CAIO, General Counsel | AI-GC, CEO |
| Fine-Tuning Data Governance | Chief Privacy Officer / DPO | Data Governance Lead | CISO, Clinical Domain Expert | CCO |
| Production Monitoring & Drift Detection | VP of Engineering | MLOps Platform Team | AI/ML Engineering Lead | VP of relevant Business Unit |
| Post-Market Surveillance (EU AI Act) | CCO | Clinical Safety Team | VP of Clinical AI Products, DPO | AI-GC |
| Model Deprovisioning & Decommissioning | VP of IT Operations | IT Asset Management | CISO, DPO | CAIO |
| Training & Certification | CHRO | L&D Program Manager | CAIO, CCO | All AI/ML Personnel |
| Exception Approval | CAIO | Requester's VP | General Counsel, CCO | AI-GC |

### 3.1 Key Governance Bodies

- **AI Governance Committee (AI-GC)**: Chaired by CAIO Dr. Marcus Rivera. Meets bi-weekly. Reviews and approves all foundation model usage for high-risk applications, exceptions, and significant model updates.
- **Model Review Board (MRB)**: Sub-committee of AI-GC. Convenes weekly to review model cards, risk assessments, and pre-deployment evaluation reports for models entering production.
- **Open-Source Program Office (OSPO)**: Reports to VP of Engineering. Maintains the approved license inventory, conducts license compatibility analysis, and manages open-source contributions in compliance with this SOP.

---

## 4. Policy Statements

### 4.1 Risk-Based Classification

All foundation model usage at Meridian shall be classified into one of three risk tiers based on the deployment context and potential for patient harm, financial impact, or regulatory consequence. The tier determines the rigor of governance, evaluation, and monitoring required.

| Risk Tier | Criteria | Example Use Cases | Governance Level |
|-----------|----------|-------------------|------------------|
| **Tier 1: High-Risk** | Clinical decision support, diagnostic output, patient risk scoring, credit decisions for medical lending. Subject to EU AI Act Annex III. | Fine-tuned LLM for radiology report impression generation; foundation model-based ICD-10 coding; patient deterioration prediction. | **Maximum**: AI-GC approval, full conformity assessment, mandatory model card, continuous monitoring, human-in-the-loop. |
| **Tier 2: Moderate-Risk** | Operational or administrative workflows with indirect impact on patient care or financial outcomes. | Clinical trial matching assistant; prior authorization summarization; customer service chatbot for payment inquiries. | **Standard**: MRB approval, model card, pre-deployment evaluation, automated monitoring with human oversight available. |
| **Tier 3: Low-Risk** | Internal productivity tools, research exploration, prototyping with no production data exposure. | Code generation assistant for internal development; literature summarization for research; synthetic data generation (non-PHI). | **Lightweight**: Team lead approval, basic usage logging, prohibition on PHI exposure. |

### 4.2 General Policy Commitments

1. **Human Oversight**: All Tier 1 and Tier 2 foundation model systems shall maintain meaningful human oversight capability, as required by EU AI Act Article 14. Override mechanisms must be accessible, documented, and tested quarterly.
2. **Transparency**: Every deployed foundation model shall have a publicly accessible Model Card (Tier 1) or internal Model Card (Tier 2) compliant with NIST AI RMF Map, Measure, Manage functions and EU AI Act Article 13 transparency requirements.
3. **Data Minimization**: Fine-tuning shall only use the minimum necessary personally identifiable information (PII) or protected health information (PHI). De-identification and tokenization must be applied prior to any data entering a fine-tuning pipeline, unless a specific, approved exception is granted by the DPO.
4. **Supply Chain Integrity**: All foundation model weights, tokenizers, and associated dependencies shall be validated via cryptographic hash verification against published provider manifests before integration. Any discrepancy shall trigger an immediate quarantine and security investigation.
5. **License Compliance**: No foundation model shall be used in any Meridian product without a completed license compatibility analysis conducted by the General Counsel's office. Copyleft, non-commercial, and restrictive AI licenses (e.g., RAIL-M) require explicit AI-GC approval.
6. **Continuous Monitoring**: All production foundation models shall be instrumented for automated monitoring of performance drift, data drift, fairness metrics, and safety-critical outputs.
7. **Prohibition on Autonomous Clinical Decisions**: As per EU AI Act Article 14(5), Meridian shall not deploy any foundation model-based system that makes clinical decisions without the ability for a qualified clinician to review, override, and document the rationale for deviation.

---

## 5. Detailed Procedures

### 5.1 Foundation Model Selection and Procurement

#### 5.1.1 Need Identification and Justification

The proposing team shall complete Form-SOP-AIML-015-01, "Foundation Model Usage Request," documenting:
- Business justification and problem statement.
- Preliminary risk tier classification.
- Anticipated data types for fine-tuning and inference.
- Expected latency, throughput, and availability requirements.
- Make-vs-buy analysis (why an existing foundation model vs. training from scratch).

The form shall be submitted via Jira Service Management to the "AI/ML Intake" queue for initial triage by the AI/ML Engineering Lead within three (3) business days.

#### 5.1.2 Candidate Model Screening

The AI/ML Engineering Lead, in collaboration with the proposing team, shall generate a shortlist of candidate foundation models. Screening criteria include:

| Criterion | Evaluation Method | Threshold / Requirement |
|-----------|-------------------|-------------------------|
| License Compatibility | Legal review by General Counsel | Must be compatible with Meridian's commercial product licensing and distribution model. |
| Model Provenance | Provider documentation review | Training data sources, methodology, and governance practices must be documented. Unknown provenance models are prohibited for Tier 1 and Tier 2. |
| Performance Baselines | Review of published benchmarks | Benchmarks must be on recognized, independently verifiable datasets. Meridian shall reproduce key benchmarks internally. |
| Security Posture | CISO vulnerability scan of model format | Pickle-based serialization formats (e.g., legacy PyTorch) require sandboxed loading. Safetensors or equivalent is strongly preferred. |
| EU AI Act Readiness | Provider conformity documentation | For Tier 1, preference given to providers who supply CE-marked foundation models or comprehensive conformity assessment packages. |
| Data Residency | Infrastructure architecture review | Fine-tuning and inference must occur within Meridian-controlled environments in approved AWS regions (us-east-1, eu-west-1). |
| Provider Stability | Financial and organizational assessment | Provider must demonstrate at least 24 months of sustained operations or have escrow provisions. |

#### 5.1.3 Deep Technical Evaluation

For Tier 1 and Tier 2 use cases, a mandatory deep technical evaluation shall be conducted, taking no more than fifteen (15) business days. The evaluation includes:

1. **Reproducibility Check**: Download weights using checksum verification; run five (5) sample inferences from public benchmarks to confirm consistency with published results. Log results in MLflow.
2. **Red-Teaming and Adversarial Testing**: The Security Architecture Team, in partnership with the AI/ML team, shall conduct structured adversarial testing, including:
   - Prompt injection and jailbreaking attempts (for LLMs).
   - Adversarial perturbation attacks (for vision models).
   - Data extraction and membership inference attempts.
   - Output toxicity and bias probes using LangSmith tracing.
3. **Fairness Evaluation**: Using MedInsight Analytics' de-identified demographic datasets, evaluate model outputs for differential performance across protected characteristics (race, ethnicity, gender, age). Disparate impact ratios shall be calculated and must fall within [0.8, 1.25] for all groups.
4. **Alignment Assessment**: Evaluate model refusal behaviors, helpfulness, harmlessness, and honesty (HHH) characteristics using internal alignment benchmarks.
5. **Operational Feasibility**: Benchmark inference latency, GPU memory requirements, and throughput in the Meridian AWS environment using representative workloads.

#### 5.1.4 Approval Gates

| Risk Tier | Approval Gate | Documentation Required | Approving Body | SLA |
|-----------|---------------|------------------------|----------------|-----|
| Tier 3 | Single gate | Form-SOP-AIML-015-01 | AI/ML Engineering Lead | 3 business days |
| Tier 2 | Two-gate | Form-SOP-AIML-015-01 + Technical Evaluation Report + License Analysis | Gate 1: AI/ML Engineering Lead; Gate 2: Model Review Board | 15 business days |
| Tier 1 | Three-gate | All Tier 2 docs + EU AI Act Pre-Assessment + Clinical Safety Review | Gate 1: MRB; Gate 2: CMO; Gate 3: AI-GC | 30 business days |

### 5.2 Fine-Tuning and Adaptation Procedures

#### 5.2.1 Environment Preparation

All fine-tuning operations shall be conducted in isolated, monitored environments:
- **Tier 1**: Dedicated AWS SageMaker instances within Meridian's private VPC, with enhanced monitoring enabled. Access requires multi-factor authentication (MFA) and is logged to Datadog.
- **Tier 2**: Isolated SageMaker project within the ML Platform VPC, with standard monitoring.
- **Tier 3**: Permitted on local workstations or development environments, with mandatory containerization.

Data for fine-tuning shall undergo the following pre-processing pipeline:
1. **Data Cataloging**: Register the dataset in Alation (Meridian's data catalog), tagging with data classification, provenance, and retention policy.
2. **De-identification**: If the dataset contains PII/PHI, execute the Meridian De-identification Service (MDS) pipeline. Validate de-identification success using the MDS validation suite. Tokenization mapping shall be stored separately in the encrypted PHI vault.
3. **Bias Audit**: Use the Fairness Indicators library to profile the dataset for representation imbalances across demographic dimensions.
4. **Data Splitting**: Stratified split into training (70%), validation (15%), and held-out test (15%) sets. The test set shall remain immutable and never be used during hyperparameter tuning.
5. **Data Versioning**: Commit datasets to DVC (Data Version Control) with Git-backed metadata.

#### 5.2.2 Fine-Tuning Execution (PEFT Preferred)

Meridian's default fine-tuning strategy for foundation models is Parameter-Efficient Fine-Tuning (PEFT) using LoRA or QLoRA adapters. Full fine-tuning requires explicit justification and AI-GC approval for Tier 1, MRB approval for Tier 2, due to elevated catastrophic forgetting and overfitting risks.

**PEFT Workflow Steps:**
1. Load base model weights in the defined training environment. Verify SHA-256 checksum against the approved provider manifest.
2. Initialize LoRA adapters with rank `r=8` to `r=64` (Tier 1 default: `r=16`; Tier 2 default: `r=32`), alpha scaling factor, and target modules appropriate for the architecture.
3. Train adapters on the Meridian-specific dataset using supervised fine-tuning (SFT) loss.
4. Log all training runs to MLflow, including hyperparameters, loss curves, and evaluation metrics.
5. Upon training completion, save adapter weights separately from base model weights. Store in the Meridian Hugging Face Model Hub (private instance) with versioned tags.
6. Merge adapters to base weights only for deployment packaging, preserving the unmerged base and adapter pair for auditability.

**Full Fine-Tuning (Exception Only) Additional Steps:**
1. Establish a baseline evaluation suite on the pre-trained model (pre-fine-tuning).
2. Implement Elastic Weight Consolidation (EWC) or experience replay to mitigate catastrophic forgetting.
3. Run the full evaluation suite post-fine-tuning, comparing against baseline. Degradation > 5% on any pre-existing capability metric requires remediation or rollback.

#### 5.2.3 RLHF Procedure (Tier 1 and Tier 2 Only)

When reinforcement learning from human feedback is employed:
1. **Reward Model Training**: Deploy a separate reward model trained on Meridian's clinical preference data. Preference data collection must follow the IRB-approved clinical annotation protocol (SOP-CLIN-027).
2. **Annotation Workforce Qualification**: Human labelers must hold relevant clinical credentials for Tier 1 (e.g., board-certified radiologist for imaging tasks) or domain expertise for Tier 2.
3. **Policy Optimization**: Use Proximal Policy Optimization (PPO) with a KL-divergence penalty to prevent reward hacking and policy collapse. Log KL-divergence in real-time to Datadog.
4. **Safety Filtering**: Before RLHF, integrate the Meridian Safety Filter (MSF) to intercept and log policy outputs that violate content safety thresholds.

### 5.3 Model Evaluation and Validation

#### 5.3.1 Pre-Deployment Evaluation Suite

All Tier 1 and Tier 2 models must pass the following evaluation gates:

| Evaluation Category | Metrics | Threshold (Tier 1) | Threshold (Tier 2) | Tool |
|---------------------|---------|--------------------|--------------------|------|
| Task Performance | Accuracy, F1, BLEU, ROUGE, etc. (task-dependent) | Must exceed current production baseline or clinically meaningful threshold defined by CMO | Must exceed heuristic baseline or previous model version | SageMaker Clarify, Custom Eval Harness |
| Fairness | Equal Opportunity Difference (EOD), Demographic Parity Difference (DPD) | EOD and DPD magnitude < 0.1 for all groups | EOD and DPD magnitude < 0.15 for all groups | SageMaker Clarify, Fairlearn |
| Robustness | Performance under synthetic perturbations, adversarial examples | < 10% degradation under PGD attack (ε=0.01) | < 15% degradation under PGD attack (ε=0.01) | Adversarial Robustness Toolbox (ART), LangSmith |
| Calibration | Expected Calibration Error (ECE) | ECE < 0.05 | ECE < 0.10 | NetCal, Custom Eval |
| Safety | Toxicity score, refusal accuracy for harmful prompts | Toxicity < 0.001; Refusal > 99% | Toxicity < 0.01; Refusal > 95% | Meridian Safety Filter, Perspective API (offline) |
| Clinical Safety | Sensitivity, Specificity for critical conditions | 95% CI lower bound must meet clinical threshold | N/A (if non-clinical) | Custom Clinical Eval Set |
| Latency | P50, P95, P99 inference time | Must meet SLA defined in deployment specification | Must meet SLA defined in deployment specification | Datadog, Locust |

#### 5.3.2 Model Card Generation

Upon successful evaluation, a Model Card shall be generated using the Meridian Model Card Generator (MMCG) tool, which produces output compliant with the Hugging Face Model Card specification, NIST AI RMF, and EU AI Act Annex IV. The Model Card includes:
- Model name, version, and unique identifier (BOM hash).
- Intended use and prohibited use cases.
- Training data summary with provenance and demographic composition.
- Evaluation results from 5.3.1, with confidence intervals.
- Known limitations and failure modes.
- Ethical considerations and fairness evaluation.
- Recommended post-market surveillance plan.

### 5.4 Deployment and Integration

#### 5.4.1 Packaging and Registration

1. Package model artifacts (merged weights or base weights + adapter) into a Docker container using the Meridian Model Serving Template.
2. Register the container in Amazon ECR with a semantic version tag (`major.minor.patch`) and a corresponding Git commit hash tag.
3. Register the Model Card and all evaluation artifacts in the Meridian Model Registry (MLflow). Attach the BOM.

#### 5.4.2 Canary and Shadow Deployment

All Tier 1 models must undergo:
- **Shadow Mode (minimum 14 days)**: Model inferences are executed in parallel with the current production system but not served to users. Logs are compared; statistically significant differences (p < 0.05) in outcomes trigger investigation.
- **Canary Deployment (minimum 7 days)**: Traffic is incrementally shifted (5% → 25% → 50% → 100%) with automated rollback triggers if monitoring alerts fire.

Tier 2 models require a shortened canary window (minimum 3 days).

#### 5.4.3 Decommissioning

When a foundation model is retired:
1. Archive model artifacts, training data references, and evaluation results in the Meridian Compliance Archive (AWS Glacier) with a retention period aligned to the associated product's record retention schedule (minimum 10 years for clinical systems).
2. Deregister model containers from ECR.
3. Mark model as "DEPRECATED" in the Model Registry.
4. Issue a decommissioning notice to the DPO if the model processed EU resident data.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Applicable Tiers | Implementation |
|------------|---------------------|-----------------|----------------|
| TC-01 | Incoming model weight checksum verification | Tier 1, Tier 2, Tier 3 | HashiCorp Vault-secured script validating SHA-256 prior to any model loading |
| TC-02 | Sandboxed model loading for untrusted formats | Tier 1, Tier 2 | GVisor runtime isolation for any model loaded from pickle or other unserialized formats |
| TC-03 | Automated bias detection in training data | Tier 1, Tier 2 | SageMaker Clarify pre-processing bias metrics computed and logged to Datadog |
| TC-04 | Adversarial robustness gates | Tier 1, Tier 2 | ART library integrated into CI/CD pipeline; failure blocks deployment |
| TC-05 | Content safety filtering | Tier 1, Tier 2 (LLMs) | Meridian Safety Filter (MSF) deployed as a sidecar proxy for all LLM inference endpoints |
| TC-06 | PII/PHI redaction in prompts and completions | Tier 1, Tier 2 | Amazon Comprehend Medical + custom regex post-processing pipeline |
| TC-07 | Differential privacy for fine-tuning | Tier 1 (optional for Tier 2) | Opacus library integration; ε ≤ 8.0, δ ≤ 1e-5 |
| TC-08 | Model weight encryption at rest | Tier 1, Tier 2 | AWS KMS envelope encryption; keys rotated every 90 days |
| TC-09 | Inference air-gapping for highest sensitivity | Tier 1 (clinical imaging) | Private VPC, no internet egress; AWS PrivateLink for service access |

### 6.2 Administrative Controls

| Control ID | Control Description | Applicable Tiers | Implementation |
|------------|---------------------|-----------------|----------------|
| AC-01 | AI-GC approval for all Tier 1 deployments | Tier 1 | Bi-weekly review board; quorum of 4 required |
| AC-02 | Dual-party review for model evaluation results | Tier 1, Tier 2 | Independent sign-off by MLOps Validation Lead and Clinical/domain expert |
| AC-03 | Annual third-party audits | All | External audit firm with AI/ML expertise; includes penetration testing of model APIs |
| AC-04 | Mandatory training completion before access | All | E-learning course (SOP-AIML-015-TRN) assigned via Workday; completion tracked |
| AC-05 | Model inventory and register | All | MLflow Model Registry synced to Meridian Asset Management (ServiceNow CMDB) |

### 6.3 EU AI Act Conformity Controls

Per EU AI Act, specifically Articles 9, 11, 13, 14, 15, 17, and 61, the following additional controls apply to all high-risk AI systems (Tier 1):

- **Article 9 – Risk Management System**: Risks are identified, estimated, and evaluated in Form-SOP-AIML-015-02 (EU AI Act Risk Assessment). Residual risk must be deemed acceptable by the AI-GC.
- **Article 11 – Technical Documentation**: Maintained in Meridian's electronic Quality Management System (eQMS – Qualio), organized per Annex IV structure.
- **Article 13 – Transparency**: Model Cards are published on Meridian's public-facing developer portal for all Tier 1 models.
- **Article 14 – Human Oversight**: Override mechanisms documented in user interface and tested quarterly by the Clinical Safety Team.
- **Article 15 – Accuracy, Robustness, Cybersecurity**: Satisfied via controls TC-04, TC-08, TC-09, and the evaluation regime in Section 5.3.
- **Article 17 – Quality Management System**: This SOP is a controlled document within Meridian's ISO 13485:2016 and ISO 27001:2022 certified QMS.
- **Article 61 – Post-Market Monitoring**: Active collection and analysis of real-world performance data, with serious incident reporting to Notified Body within 15 days.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators

The following KPIs shall be tracked continuously and reviewed quarterly by the AI-GC.

| Metric ID | Metric Name | Description | Target | Measurement Method |
|-----------|-------------|-------------|--------|-------------------|
| KPI-01 | Model Drift Rate | Percentage of deployed models with PSI > 0.2 or embedding drift > threshold within the reporting period | < 5% of Tier 1 models | Datadog drift monitors |
| KPI-02 | Fairness Threshold Compliance | Percentage of Tier 1 models with all fairness metrics within approved thresholds | 100% | SageMaker Clarify automated checks |
| KPI-03 | Mean Time to Detect (MTTD) Critical Anomaly | Time from critical safety or performance anomaly onset to PagerDuty alert trigger | < 5 minutes | PagerDuty analytics |
| KPI-04 | Model Evaluation Pass Rate | Percentage of model candidates passing pre-deployment evaluation suite on first attempt | > 60% | MLflow Model Registry |
| KPI-05 | Training Completion Rate | Percentage of AI/ML personnel current on SOP-AIML-015-TRN | > 95% | Workday LMS |
| KPI-06 | EU AI Act Serious Incident Reports | Number of reportable serious incidents under Art. 61 | 0 | Qualio Incident Management |
| KPI-07 | Open-Source License Violations | Number of license violations detected in post-deployment audits | 0 | FOSSA, quarterly scans |
| KPI-08 | Model Inventory Accuracy | Percentage of production models registered in MLflow with complete metadata | 100% | Monthly reconciliation with live endpoints |

### 7.2 Dashboards

- **Operational Dashboard (Datadog)**: Real-time model health, latency, error rates, drift indicators, and safety filter trigger rates. Accessible to MLOps and AI/ML Engineering teams.
- **Governance Dashboard (Tableau)**: Aggregated KPIs, risk tier distributions, exception status, training compliance. Published to AI-GC and executive leadership monthly.
- **EU AI Act Compliance Dashboard (Qualio)**: Conformity assessment status, post-market surveillance log, serious incident tracker. Accessible to CCO, DPO, and regulatory affairs.

### 7.3 Reporting Cadence

| Report | Frequency | Audience | Content |
|--------|-----------|----------|---------|
| Daily Model Health Check | Daily (automated) | MLOps Team, AI/ML Engineering Lead | Critical alerts, drift warnings, error rate anomalies |
| Weekly Operations Summary | Weekly | VP of Engineering, CAIO | Key incidents, deployments, evaluation pass/fail summary |
| Quarterly AI Governance Report | Quarterly | AI-GC, Board of Directors | Full KPI review, risk register update, exception log, regulatory horizon scan |
| Annual EU AI Act Compliance Report | Annually | Notified Body, Competent Authority | Conformity assessment updates, post-market surveillance summary, serious incident log |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

Any deviation from the procedures defined in this SOP requires a formal exception request via Form-SOP-AIML-015-03 ("SOP Exception Request"). The form shall include:
- Specific section(s) of the SOP for which an exception is sought.
- Justification and risk analysis.
- Proposed compensating controls.
- Duration of the exception (maximum 90 days for Tier 1; 180 days for Tier 2/3).
- Impact assessment on patient safety or financial risk.

### 8.2 Exception Approval Matrix

| Risk Tier | Exception Scope | Approver(s) Required | Maximum Duration |
|-----------|-----------------|---------------------|------------------|
| Tier 3 | Any | AI/ML Engineering Lead | 180 days |
| Tier 2 | Non-safety-critical | Model Review Board Chair | 180 days |
| Tier 2 | Safety-adjacent | CAIO | 90 days |
| Tier 1 | Non-safety-critical | CAIO + General Counsel | 90 days |
| Tier 1 | Safety-critical | AI-GC (full quorum) | 90 days, renewable once |

### 8.3 Escalation Path

If a critical risk is identified outside the normal exception workflow (e.g., model exhibiting dangerous emergent behavior), the following escalation path shall be followed:
1. **Immediate**: MLOps engineer on call triggers PagerDuty "SEV-1" alert and disables the affected model endpoint.
2. **Within 1 hour**: Incident commander (Designated MLOps Lead) assembles the Critical Incident Response Team (CIRT) including CAIO, CISO, and CMO.
3. **Within 4 hours**: A preliminary incident report is drafted in Qualio.
4. **Within 24 hours**: If the model is EU AI Act high-risk and the incident meets serious incident criteria, the CCO initiates the Article 61 notification to the Notified Body.
5. **Within 72 hours**: Root cause analysis (RCA) is initiated; results are presented to AI-GC within 14 days.

---

## 9. Training Requirements

### 9.1 Required Training Modules

All personnel governed by this SOP must complete the following training, tracked and managed via Workday Learning.

| Training Code | Title | Description | Frequency | Required For |
|---------------|-------|-------------|-----------|--------------|
| SOP-AIML-015-TRN | Foundation Model Governance and Safety | Overview of SOP, risk tiers, evaluation requirements, and incident reporting. Includes EU AI Act fundamentals and NIST AI RMF awareness. | Annually | All AI/ML personnel, Product Managers, Clinical domain experts |
| SOP-AIML-015-ADV | Advanced Foundation Model Risk Management | Deep dive into adversarial testing, fairness evaluation, PEFT techniques, and supply chain security. | Annually | AI/ML Engineers, MLOps Engineers, Security Architecture Team |
| EU-AIACT-101 | EU AI Act Practitioner Training | Legal requirements for high-risk AI, conformity assessment, post-market surveillance. | Bi-annually | AI/ML Leadership, Compliance Officers, Clinical Safety Team |
| NIST-RMF-101 | NIST AI RMF Workshop | Practical application of Map, Measure, Manage, Govern functions. | Annually | All AI/ML personnel |

### 9.2 Training Compliance Tracking
- HR's Learning & Development team issues monthly compliance reports to VPs.
- Personnel with lapsed training (>30 days past due) shall have their model registry and deployment tool access suspended until training is completed.
- New hires must complete SOP-AIML-015-TRN within their first 14 days of employment.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| SOP-AIML-012 | Traditional Model Development Lifecycle | Predecessor process for non-foundation-model AI development |
| SOP-AIML-010 | AI Model Risk Management Framework | Overall risk management umbrella for AI systems |
| SOP-SEC-023 | AI Supply Chain Security | Detailed third-party component vetting procedures |
| SOP-VEND-008 | Third-Party AI Vendor Risk Management | Vendor-specific governance, overlapping for proprietary model provider assessment |
| SOP-DATA-005 | Data Classification and Handling | Data governance policies for training data |
| SOP-DATA-011 | PHI De-identification Standards | Detailed de-identification pipeline requirements |
| SOP-CLIN-027 | Clinical Annotation and RLHF Data Collection | Human preference data gathering for clinical AI |
| POL-ETHICS-001 | Meridian AI Ethics Charter | Foundational ethical principles guiding all AI development |
| POL-EU-AIACT-001 | EU AI Act Compliance Policy | High-risk system governance and conformity assessment obligations |

### 10.2 External Standards and Regulations

| Reference | Version / Date | Applicability |
|-----------|----------------|---------------|
| EU AI Act (Regulation 2024/1689) | 2024 | High-risk AI system governance, all Tier 1 use cases |
| NIST AI RMF (AI 100-1) | January 2023 | Entire SOP framework |
| NIST AI RMF Generative AI Profile (AI 600-1) | July 2024 | Foundation model-specific risk dimensions |
| ISO/IEC 42001:2023 | 2023 | AI management system requirements |
| ISO/IEC 22989:2022 | 2022 | AI terminology and concepts |
| ISO 13485:2016 | 2016 | Medical device quality management (clinical AI products) |
| ISO 27001:2022 | 2022 | Information security management |
| COSO Enterprise Risk Management | 2017 | Risk management framework alignment |
| Hugging Face Model Card Specification | v1.0 | Model Card format standard |

---

## 11. Revision History

| Version | Effective Date | Author | Change Summary |
|---------|----------------|--------|----------------|
| 1.0 | 2022-05-15 | Dr. Sarah Chen (initial draft) | Initial release, covering general ML model governance. |
| 1.5 | 2023-01-20 | Dr. Marcus Rivera | Added foundation model-specific provisions; introduced risk tiers. |
| 2.0 | 2023-08-01 | Dr. Marcus Rivera, Legal | Major revision: integrated EU AI Act requirements (post-adoption); introduced model card mandate and post-market surveillance. |
| 2.5 | 2024-03-15 | David Park, MLOps Lead | Added PEFT preference, canary deployment, differential privacy controls, and expanded KPI dashboard. |
| 2.8 | 2024-10-02 | Dr. Marcus Rivera | Current version: refined NIST AI RMF alignment (GenAI Profile); updated OSPO role; expanded supply chain controls; updated training requirements for EU AI Act conformity. |