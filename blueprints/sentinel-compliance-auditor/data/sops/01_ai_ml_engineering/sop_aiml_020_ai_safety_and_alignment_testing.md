---
sop_id: "SOP-AIML-020"
title: "AI Safety and Alignment Testing"
business_unit: "AI/ML Engineering"
version: "2.4"
effective_date: "2024-04-24"
last_reviewed: "2025-02-24"
next_review: "2025-08-20"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# SOP-AIML-020: AI Safety and Alignment Testing

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework, testing methodologies, and governance protocols for ensuring the safety, robustness, and behavioral alignment of all artificial intelligence and machine learning (AI/ML) models developed, deployed, or maintained by Meridian Health Technologies, Inc. ("Meridian"). The purpose of this document is to define a repeatable, auditable, and risk-proportional process to identify, assess, and mitigate technical AI safety risks before and during model deployment, ensuring that AI systems operate reliably, resist adversarial manipulation, and produce outputs aligned with their intended clinical and financial use cases.

### 1.2 Scope

This SOP applies to all AI/ML models and systems across the following business units and product lines:

| Business Unit | Products Covered | Risk Classification |
|---|---|---|
| Clinical AI Platform | Clinical decision support, diagnostic imaging analysis, patient risk scoring, adverse event prediction | Safety-Critical / High-Risk |
| HealthPay Financial Services | Credit scoring models, fraud detection, claims automation, lending algorithms | Safety-Sensitive / Regulated |
| MedInsight Analytics | Population health models, care gap identification, outcomes prediction | Safety-Sensitive |
| Meridian SaaS Platform | Infrastructure-level AI services, shared ML components | Enabling Infrastructure |

This SOP covers the following model lifecycle stages:
- Pre-training data evaluation
- Model development and fine-tuning
- Pre-deployment validation
- Production deployment
- Post-deployment continuous monitoring
- Model update and retraining cycles

### 1.3 Out of Scope

The following activities are explicitly out of scope for this SOP:
- Infrastructure security testing (see SOP-ISEC-045: Cloud Security Posture Management)
- General application penetration testing (see SOP-ISEC-012: Application Security Testing)
- Privacy compliance audits (see SOP-PRIV-008: PHI Data Protection Audits)
- Fair lending compliance testing (see SOP-HPFS-015: Fair Lending Model Validation)
- Clinical efficacy validation (see SOP-CLIN-030: Clinical Model Performance Validation)

### 1.4 Applicability

This SOP applies to the following roles:
- AI/ML Engineers (all levels)
- Data Scientists
- ML Operations (MLOps) Engineers
- AI Safety Engineers (dedicated safety team)
- Product Managers for AI products
- Clinical Informatics Specialists
- Financial Risk Analysts (HealthPay)
- Quality Assurance Engineers (AI-specialized)
- DevSecOps Engineers supporting AI pipelines

Compliance with this SOP is mandatory for all personnel engaged in AI/ML model development and operations. Non-compliance may result in disciplinary action up to and including termination, in accordance with Meridian's Code of Conduct and HR policies.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Adversarial Robustness** | The ability of an AI model to maintain correct behavior and output integrity when presented with intentionally perturbed, manipulated, or maliciously crafted inputs designed to cause misclassification or erroneous outputs. |
| **AI Alignment** | The degree to which an AI system's learned behaviors, objective functions, and generated outputs correspond to the intended operational goals, ethical constraints, and safety boundaries defined by Meridian's product and clinical requirements. |
| **Capability Boundary** | The defined, tested, and documented limits of a model's operational domain beyond which the model's behavior is unverified and potentially unsafe. |
| **Catastrophic Risk** | Any AI system failure mode that could result in patient mortality, severe patient harm, systemic financial loss exceeding $10M, or regulatory action resulting in suspension of business operations. |
| **Constitutional Constraints** | Hard-coded behavioral rules, output filters, and decision boundaries that prevent the model from generating outputs classified as harmful, discriminatory, medically contradictory, or outside the approved operational domain. |
| **Distributional Shift** | A statistically significant change in the characteristics of input data between the training distribution and the production inference distribution, measured using population stability index (PSI) > 0.25 or characteristic stability index (CSI) > 0.20. |
| **Red Teaming** | A structured adversarial testing methodology in which a designated team systematically attempts to cause the AI system to produce unsafe, misaligned, or erroneous outputs using a combination of automated tools and expert human reasoning. |
| **Safety Margin** | The quantitative distance between a model's decision boundary and the nearest known failure case, expressed as a probabilistic confidence interval threshold below which model predictions are flagged for review. |
| **Sandbox Environment** | An isolated, air-gapped computational environment with no production data access, network connectivity to production systems, or ability to affect clinical or financial operations. |

### 2.2 Acronyms

| Acronym | Full Term |
|---|---|
| AI RMF | Artificial Intelligence Risk Management Framework |
| ASAT | Automated Safety Assessment Toolkit |
| ATRL | Adversarial Test Results Ledger |
| CAR | Corrective Action Report |
| CEM | Consequence-Exploitability Matrix |
| CICD | Continuous Integration / Continuous Deployment |
| DSP | Deployment Safety Package |
| FMEA | Failure Mode and Effects Analysis |
| FPR | False Positive Rate |
| MLOps | Machine Learning Operations |
| PSI | Population Stability Index |
| RSP | Risk-Specific Safety Protocol |
| SAB | Safety Alignment Board |
| SDP | Safety Demonstration Package |
| TPS | Technical Product Specification |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| Activity / Decision | Chief AI Officer | AI Safety Engineer | AI/ML Engineer | Product Manager | MLOps Engineer | QA Engineer | CISO |
|---|---|---|---|---|---|---|---|
| Safety test plan approval | A | R | C | C | I | I | I |
| Red team exercise authorization | A | R | C | I | I | C | I |
| Model safety sign-off (pre-prod) | A | R | C | C | C | R | I |
| Adversarial robustness testing | I | R | C | I | C | A | I |
| Catastrophic risk assessment | A | R | C | C | I | I | C |
| Safety incident declaration | A | R | C | C | I | I | I |
| Production rollout approval | A | R | C | A | R | R | I |
| Emergency model rollback | I | C | R | I | A | I | C |
| Safety KPI threshold updates | A | R | C | C | I | I | I |
| Exception approval | A | C | I | R | I | I | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### 3.2 Role Descriptions

#### 3.2.1 Chief AI Officer (Dr. Marcus Rivera)
Serves as the ultimate accountable executive for AI safety across Meridian. Approves all safety-related policy updates, authorizes red team engagements, and holds final sign-off authority for deployment of any Safety-Critical AI model. Chairs the quarterly AI Safety Alignment Board (SAB) review.

#### 3.2.2 AI Safety Engineer
A dedicated role within the AI/ML Engineering organization responsible for executing adversarial robustness testing, conducting alignment audits, developing safety test suites, and preparing the Safety Demonstration Package (SDP) for each model release. Holds the authority to block model deployments if safety thresholds are not met.

#### 3.2.3 AI/ML Engineer
Responsible for implementing safety requirements during model development, including constitutional constraints, output filters, confidence threshold enforcement, and cooperative model training techniques. Must remediate all findings identified in safety test reports.

#### 3.2.4 Product Manager
Responsible for defining safety-aligned product requirements within the Technical Product Specification (TPS), validating that safety testing covers all intended use cases, and obtaining business approval for acceptable risk tolerance levels.

#### 3.2.5 MLOps Engineer
Responsible for implementing the automated safety testing pipeline within the CICD infrastructure, deploying safety monitoring dashboards, and executing emergency rollback procedures when safety incidents are detected in production.

#### 3.2.6 QA Engineer (AI-Specialized)
Responsible for executing deterministic test cases from the safety test plan, documenting results in the Adversarial Test Results Ledger (ATRL), and verifying that all requirements from the TPS safety section are met.

#### 3.2.7 Chief Information Security Officer (CISO)
Consulted on adversarial threat modeling, red team methodology, and any AI safety incidents that involve potential security breach vectors or data exfiltration risks.

---

## 4. Policy Statements

### 4.1 Safety-First Deployment Principle

No AI/ML model classified as Safety-Critical or Safety-Sensitive shall be deployed to any production environment, including any environment that affects patient care, clinical decision-making, financial transactions, or population health analytics, without a fully approved Safety Demonstration Package (SDP) on file in the Meridian AI Asset Registry (MLflow Enterprise instance, at `mlflow.meridian.internal`). The SDP must contain documented evidence that all required safety tests have been executed and passed according to the Risk-Specific Safety Protocol defined for that risk classification.

### 4.2 Proportional Safety Testing

AI safety testing effort and depth shall be proportional to the risk classification of the model. The following minimum testing requirements apply:

| Risk Classification | Required Testing |
|---|---|
| Safety-Critical | Full red team engagement, comprehensive adversarial robustness battery, FMEA, alignment audit, capability boundary stress testing |
| Safety-Sensitive | Targeted red team assessment, adversarial robustness spot-check, alignment spot-audit, distributional shift robustness |
| Enabling Infrastructure | Automated safety regression suite, input validation fuzzing |

### 4.3 Red Teaming Mandate

Every Safety-Critical model released to production must undergo a formal, documented red team engagement conducted by qualified personnel who were not involved in the model's development. Red team objectives, methodology, success criteria, and findings must be documented in the Adversarial Test Results Ledger (ATRL) system at `atrl.meridian.internal`.

### 4.4 Adversarial Robustness Thresholds

All Safety-Critical and Safety-Sensitive models must meet minimum adversarial robustness thresholds prior to deployment approval. Thresholds vary by model type and are defined in the model-specific safety test plan. General thresholds are defined below in Section 6.

### 4.5 Alignment Verification

All models shall undergo alignment verification testing to confirm that model behaviors, objective optimization, and generated outputs conform to the intended operational domain and do not exhibit reward hacking, specification gaming, or unintended behavioral modes. Alignment verification results must be included in the SDP.

### 4.6 Prohibition on Unverified Deployment

Under no circumstances shall a model that has failed any required safety test be promoted to production without a fully documented and approved exception (see Section 8). Production deployment of a non-compliant model constitutes a Code of Conduct violation.

### 4.7 Incident Transparency

All safety incidents, near-misses, and adversarial vulnerability discoveries shall be documented in the centralized AI Incident Register (ServiceNow module `AI_Safety_Incident`) within 24 hours of detection. The incident register shall be accessible to all AI/ML Engineering personnel to promote organizational learning.

---

## 5. Detailed Procedures

### 5.1 Safety Test Planning

#### 5.1.1 Initiation Trigger

The AI Safety testing workflow shall be initiated by any of the following events:

1. A new model enters the "Feature Complete" milestone in the ML model lifecycle (documented in Jira at `meridian.atlassian.net/aiml-projects`)
2. An existing production model undergoes a major version increment (vX.0.0 → vY.0.0)
3. A production model is retrained with a new training dataset that differs by >15% in source distribution
4. A Safety Critical model has not been tested in the preceding 180 calendar days

#### 5.1.2 Test Plan Document

The AI Safety Engineer, in consultation with the Product Manager and the responsible AI/ML Engineer, shall produce a **Model Safety Test Plan** (template: `T-MSTP-001` in Confluence at `confluence.meridian.internal/aiml/safety-templates`). The plan shall contain:

- Model identifier (MLflow run ID and model registry name)
- Risk classification (Safety-Critical, Safety-Sensitive, or Enabling Infrastructure)
- Model use case summary
- Intended operational domain specification
- Known limitations from previous testing cycles
- Specific safety properties to be verified
- Testing methodology for each safety property
- Quantitative pass/fail criteria for each test
- Required reviewers and approvers
- Estimated testing duration and resource requirements

#### 5.1.3 Approval Workflow

| Step | Actor | Action |
|---|---|---|
| 1 | AI Safety Engineer | Drafts test plan, submits via Confluence Approval Workflow |
| 2 | Product Manager | Reviews for use case alignment within 3 business days |
| 3 | AI/ML Engineer | Reviews for technical accuracy within 3 business days |
| 4 | AI Safety Engineer | Incorporates feedback, resubmits if necessary |
| 5 | Chief AI Officer (or delegate) | Final approval |

### 5.2 Sandbox Environment Provisioning

#### 5.2.1 Environment Requirements

The AI Safety Engineer shall submit an environment provisioning request through the Meridian MLOps Platform portal (`mlops.meridian.internal/sandbox/provision`). The sandbox environment must meet the following specifications:

| Requirement | Specification |
|---|---|
| Compute | Minimum 4x NVIDIA A100-80GB or equivalent; GPU cluster `meridian-safety-gpu-pool` |
| Storage | 5TB SSD ephemeral; persistent artifact storage on `s3://meridian-safety-artifacts` |
| Networking | Air-gapped from production; restricted egress to approved artifact registries only |
| Data Access | Only synthetic and de-identified data; no PHI/PII datasets |
| Duration | Auto-terminated after 72 hours unless extended by exception ticket |
| Container Registry | `meridian-ecr-safety.dkr.ecr.us-east-1.internal/safety-sandbox/*` |

#### 5.2.2 Data Preparation

Training and testing datasets shall be prepared according to the following rules:

- PHI-identified data prohibited in sandbox environments
- Synthetic data generation using `meridian-synthetic-data-generator` v3.2+
- De-identified data sourced from Meridian Data Lake (`meridian-datalake/safety-curated/*`) with Data Governance ticket approval
- Adversarial sample sets loaded from the Meridian Adversarial Sample Repository (`s3://meridian-adversarial-samples/{model_type}/`)

### 5.3 Adversarial Robustness Testing

#### 5.3.1 White-Box Gradient-Based Attacks

For models where the AI Safety Engineer has access to model weights and gradients (i.e., models developed internally at Meridian), white-box adversarial testing shall be executed using the Automated Safety Assessment Toolkit (ASAT) at `asat.meridian.internal`.

**Procedure:**

1. **Model Loading:**
   - Load the model from MLflow registry using the safety testing service account (`svc-meridian-safety`)
   - Verify model hash against the registry to ensure integrity
   - Log the model hash and loading timestamp to the ATRL

2. **ASAT Configuration:**
   - Configure ASAT with model-specific parameters from the Safety Test Plan
   - For clinical imaging models: configure perturbation bounds ε ∈ {0.001, 0.005, 0.01, 0.05, 0.10} measured in L∞ norm relative to image intensity range
   - For tabular clinical risk models: configure per-feature perturbation budgets as defined in `SOP-AIML-020-Appendix-A`
   - For financial models: configure perturbation budgets compliant with model risk tier definitions

3. **Attack Execution:**
   - Execute Projected Gradient Descent (PGD) attacks with 40, 100, and 200 iteration steps
   - Execute C&W (Carlini-Wagner) L2 attacks with confidence parameter κ ∈ {0, 5, 10, 20}
   - Execute AutoAttack ensemble for comprehensive evaluation
   - For models with non-differentiable components, execute Square Attack (black-box score-based)
   - Each attack configuration tested on minimum 10,000 samples from the evaluation set

4. **Results Recording:**
   - Record robust accuracy at each perturbation magnitude
   - Record per-class worst-case degradation
   - Flag any perturbation magnitude where accuracy drops below threshold in Table 6.1
   - Write all results to ATRL using the API at `atrl.meridian.internal/api/v2/results`

#### 5.3.2 Black-Box Decision-Based Attacks

For models where internal personnel do not have access to model weights (e.g., third-party vendor models, API-wrapped models), black-box decision-based testing shall be conducted.

**Procedure:**

1. **API Access Configuration:**
   - Provision API access to the model endpoint in the sandbox environment
   - Configure rate limiting identical to production constraints
   - Verify model endpoint health before testing

2. **Attack Execution:**
   - Execute HopSkipJumpAttack adapted for the model input modality
   - Execute Boundary Attack with 50,000 query budget
   - For text-based models, execute TextFooler and BERT-Attack variants
   - For tabular models, execute LowProFool adapted to feature constraints

3. **Query Efficiency Measurement:**
   - Record mean queries to successful adversarial example
   - Flag models where median queries-to-breach < 1,000 as high-risk

#### 5.3.3 Physical-World Robustness (Clinical Imaging Models Only)

Clinical imaging models (diagnostic imaging, triage classification) shall undergo robustness testing against physically realizable perturbations:

1. **Synthetic Corruption Test Suite:**
   - Apply medical-imaging-specific corruptions from the Meridian Clinical Imaging Corruption Library (`meridian-cicl`):
     - Motion blur (kernel sizes 3, 5, 7, 9 pixels)
     - Gaussian noise (σ ∈ {0.01, 0.05, 0.10, 0.15} relative intensity)
     - Contrast variation (±15%, ±30%)
     - Brightness variation (±10%, ±25%)
     - Rotation (±3°, ±5°, ±10°)
     - Cropping (5%, 10% margin)
   - Test 10,000 images per corruption type and severity combination

2. **Acceptance Criteria:**
   - AUC-ROC must not degrade >5% absolute under any single corruption
   - Sensitivity at operating point must not degrade >8% absolute

### 5.4 Red Teaming Exercise

#### 5.4.1 Red Team Composition

Each red team engagement shall be staffed by:
- A Lead Red Team Operator (AI Safety Engineer with adversarial ML specialization)
- 2-3 Red Team Operators (personnel not involved in model development; may include security engineers, clinical subject matter experts, or external consultants under NDA)
- A Red Team Scribe (documents findings in real-time)

#### 5.4.2 Red Team Objectives

The Meridian AI Safety Red Team operating under this SOP shall pursue the following objectives, documented in the Engagement Plan before execution:

| Objective Category | Example Objectives |
|---|---|
| Behavioral Elicitation | Identify inputs that cause the model to produce outputs outside the approved operational domain; induce the model to violate its constitutional constraints |
| Safety Bypass | Craft input sequences that cause the model to ignore safety filters or confidence thresholds; exploit sequential decision-making vulnerabilities |
| Adversarial Goal Hijacking | Cause the model to optimize for an unintended objective function through carefully constructed multi-turn interactions |
| Data Extraction | Attempt to extract training data, membership inference, or model architecture details beyond what is publicly documented |
| Capability Overestimation | Identify scenarios where the model confidently produces incorrect outputs (high confidence, low accuracy region) |

#### 5.4.3 Red Team Methodology

1. **Engagement Kickoff (Day 0):**
   - Lead Operator briefs team on model architecture, training methodology, and intended use case
   - Constraints and boundaries of the engagement defined (no production impact, no data exfiltration beyond sandbox)
   - Threat model documented from an adversarial perspective

2. **Open Exploration Phase (Days 1-3):**
   - Unstructured, creative exploration of model behavior
   - Operators encouraged to use intuition, domain expertise, and manual prompt engineering
   - All anomalous behaviors logged to shared findings board

3. **Systematic Exploitation Phase (Days 4-5):**
   - Most promising attack vectors from open exploration are systematized
   - Automated tooling developed to scale successful attack patterns
   - Documentation of reproducibility and exploitability for each finding

4. **Reporting Phase (Days 6-7):**
   - Findings triaged using the Consequence-Exploitability Matrix (CEM) (see Section 6.3)
   - Red Team Final Report drafted, including:
     - Executive summary
     - All findings with CEM scores
     - Successfully demonstrated attack narratives
     - Recommended mitigations
     - Testing limitations and suggestions for next engagement

#### 5.4.4 Red Team Output Handling

All red team findings rated as "High" or "Critical" on the CEM must be addressed with either a code fix, architectural change, or documented risk acceptance (requiring Chief AI Officer sign-off) before model deployment approval can proceed.

### 5.5 Alignment Verification

#### 5.5.1 Specification Alignment Testing

Verify that the model's learned behavior aligns with the Technical Product Specification (TPS) for all documented functional requirements:

1. **Behavioral Test Suite Construction:**
   - Translate each TPS functional requirement into 50-200 behavioral test cases
   - Include positive test cases (model should produce X given Y)
   - Include negative test cases (model should NOT produce Z)
   - Include boundary test cases (inputs at the edge of the operational domain)

2. **Automated Execution:**
   - Behavioral test suite executed via the Meridian Alignment Test Harness (MATH) at `math.meridian.internal`
   - Test results recorded with pass/fail/skip status
   - Aggregate behavioral compliance score computed

3. **Minimum Compliance Threshold:**
   - Safety-Critical models: ≥98% behavioral test pass rate
   - Safety-Sensitive models: ≥95% behavioral test pass rate
   - Any failing test case must be individually triaged and documented

#### 5.5.2 Reward Hacking Detection

For models trained using reinforcement learning (RL), preference optimization, or other reward-signal-based methods:

1. **Reward Model Audit:**
   - Analyze the learned reward model (if explicit) or implicit reward landscape
   - Identify any states where reward diverges from true desirability
   - Flag any exploitable reward model vulnerabilities

2. **Policy Behavior Under Distributional Shift:**
   - Evaluate the trained policy on 20 systematically shifted evaluation distributions
   - Measure whether the policy begins to exploit reward model misspecification
   - Flag any policy that achieves high reward yet low true utility on ≥3/20 shifted distributions

#### 5.5.3 Constitutional Constraint Verification

Validate that all constitutional constraints (output filters, decision boundaries, safety classifiers) are effective:

1. **Constraint Exhaustion Test:**
   - Generate 50,000 inputs designed to approach but not cross each constraint boundary
   - Verify that the constraint triggers correctly at the defined boundary
   - Measure false positive rate (FPR) of constraints; FPR >5% triggers investigation

2. **Constraint Composition Test:**
   - Test interactions between multiple constraints applied simultaneously
   - Identify any conflicting constraints producing undefined behavior
   - Verify constraint priority order matches specification

### 5.6 Capability Boundary Verification

#### 5.6.1 Out-of-Distribution Testing

1. **Synthetic OOD Generation:**
   - Using the Meridian Distributional Shift Engine (`meridian-dse`), generate 100 distributionally shifted versions of the evaluation dataset
   - Shift parameters: covariate shift, label shift, concept drift, each at 3 severity levels (mild, moderate, severe)

2. **Performance Boundary Mapping:**
   - Measure model performance (primary metric defined in TPS) across all 100 shifted distributions
   - Identify the performance contour where model degrades below the TPS-defined minimum acceptable performance threshold
   - Document this contour as the verified capability boundary

3. **Boundary Enforcement:**
   - Implement an input distribution guard model that detects inputs outside the capability boundary
   - Guard model FPR ≤1%, recall ≥95% on OOD samples at the capability boundary

#### 5.6.2 Edge Case Stress Testing

1. **Edge Case Library:**
   - Curate a library of 10,000 known edge cases from Meridian's operational history, published literature, and domain expert input
   - Each edge case labeled with expected safe behavior

2. **Automated Execution:**
   - Run all edge cases through the model
   - Log any case where the model output does not match expected safe behavior

3. **Edge Case Coverage Requirement:**
   - Safety-Critical models must achieve ≥99.5% safe behavior on the edge case library
   - Any failures must be addressed or documented as known limitations

### 5.7 Safety Demonstration Package (SDP) Assembly

#### 5.7.1 SDP Contents

The Safety Demonstration Package shall be assembled as a single version-controlled artifact and must contain:

| Document | Description | Template |
|---|---|---|
| SDP Cover Sheet | Metadata, model identifier, risk classification, sign-off block | `T-SDP-001` |
| Safety Test Plan | Reference to approved test plan | `T-MSTP-001` |
| Adversarial Robustness Results | Full ASAT output and analysis | Auto-generated from ASAT |
| Red Team Final Report | Complete red team findings and CEM scores | `T-RTR-001` |
| Alignment Verification Report | Behavioral compliance score, reward audit, constitutional constraint verification | `T-AVR-001` |
| Capability Boundary Report | OOD performance mapping, edge case results | `T-CBR-001` |
| Known Limitations Disclosure | Dated and signed disclosure of all known safety limitations not fully mitigated | `T-KLD-001` |
| Deployment Safety Checklist | Pre-deployment checklist with pass/fail status | `T-DSC-001` |

#### 5.7.2 SDP Submission and Review

1. AI Safety Engineer uploads complete SDP to the Meridian AI Asset Registry
2. Automated completeness check verifies all required artifacts present
3. Manual review by at minimum two qualified reviewers (from AI Safety Engineering and the product's QA Engineering team)
4. Reviewers may request additional testing or information within 5 business days
5. Approved SDP authorizes deployment for 180 days or until next major model update, whichever occurs first

---

## 6. Controls and Safeguards

### 6.1 Quantitative Safety Thresholds

| Model Type | Metric | Threshold |
|---|---|---|
| Clinical Diagnostic Imaging | Robust Accuracy (ε=0.01 L∞) | ≥90% of nominal accuracy |
| Clinical Diagnostic Imaging | Robust Accuracy (ε=0.05 L∞) | ≥75% of nominal accuracy |
| Clinical Risk Prediction | Robust AUC-ROC (max-feature perturbation=0.10) | ≥0.85 |
| Clinical Risk Prediction | Calibration Error Under Attack (ECE) | ≤0.08 |
| Financial Credit Scoring | Robust KS Statistic (ε=0.05 per feature) | ≥30 |
| Financial Fraud Detection | Robust Precision@100 (ε=0.05 per feature) | ≥0.85 |
| All Safety-Critical | Speculative Output Rate (undefined behavior) | ≤0.1% |
| All Safety-Critical | Constitutional Constraint Bypass Rate | 0% (any bypass = critical finding) |

### 6.2 Technical Safeguards

| Safeguard ID | Safeguard | Implementation Detail |
|---|---|---|
| TS-001 | Output Confidence Threshold | All Safety-Critical model predictions with confidence ≤0.85 routed to human-in-the-loop queue; threshold adjustable per model in MLflow serving configuration |
| TS-002 | Input Distribution Guard | Secondary lightweight model deployed inline before primary model; classifies input as in-distribution or OOD; OOD inputs blocked with error code `SAFETY_OOD_001` |
| TS-003 | Maximum Inference Rate Limiter | Per-model rate limiting enforced at API Gateway (`kong.meridian.internal`); prevents attacker from executing high-query-budget black-box attacks; rate limits defined per model endpoint |
| TS-004 | Output Sanitization Pipeline | Post-inference output filter validates all outputs against schema and content constraints; outputs failing validation replaced with safe fallback response |
| TS-005 | Sandbox Network Isolation | Sandbox environments provisioned in isolated VPC (`vpc-meridian-safety-sandbox`) with no peering to production VPCs; egress-only to approved artifact registries; all traffic logged |
| TS-006 | Model Hash Verification | SHA-512 hash of serialized model computed at registration, deployment, and post-deployment daily; mismatch triggers automatic rollback to last verified hash |

### 6.3 Consequence-Exploitability Matrix (CEM)

Used to triage red team and adversarial testing findings:

| | **Exploitability: Low** | **Exploitability: Medium** | **Exploitability: High** |
|---|---|---|---|
| **Consequence: Critical** | **HIGH** - Must address before deploy | **CRITICAL** - Block deployment | **CRITICAL** - Block deployment |
| **Consequence: Major** | **MEDIUM** - Address within 30 days | **HIGH** - Must address before deploy | **CRITICAL** - Block deployment |
| **Consequence: Moderate** | **LOW** - Track in backlog | **MEDIUM** - Address within 30 days | **HIGH** - Must address before deploy |
| **Consequence: Minor** | **INFO** - Document | **LOW** - Track in backlog | **MEDIUM** - Address within 30 days |

**Consequence Definitions:**
- **Critical:** Patient mortality or severe harm plausible; or systemic financial loss >$10M
- **Major:** Patient moderate harm plausible; or systemic financial loss $1M-$10M
- **Moderate:** Patient minor/inconvenience harm; or financial loss $100K-$1M
- **Minor:** No patient impact plausible; financial loss <$100K

**Exploitability Definitions:**
- **High:** Exploit achievable with publicly available tools and minimal expertise
- **Medium:** Exploit requires moderate expertise or specific domain knowledge
- **Low:** Exploit requires expert-level skills or insider access

### 6.4 Administrative Safeguards

| Safeguard ID | Safeguard | Implementation Detail |
|---|---|---|
| AS-001 | Segregation of Duties | Personnel who developed the model may NOT serve as the AI Safety Engineer for that model's safety evaluation; enforced by role assignment in Jira projects |
| AS-002 | SDP Approval Workflow | Four-eyes principle: SDP must be approved by AI Safety Engineer AND either QA Engineer or Product Manager; Chief AI Officer approval additionally required for Safety-Critical models |
| AS-003 | Safety Incident Reporting | All personnel empowered and required to report safety concerns via ServiceNow `AI_Safety_Incident` module; anonymous reporting enabled; no retaliation policy enforced per Meridian Whistleblower Policy |
| AS-004 | Quarterly Safety Review | AI Safety Alignment Board (SAB) convenes quarterly to review all open safety findings, incident trends, and threshold adequacy; chaired by Chief AI Officer; minutes published to Confluence |

### 6.5 Data Controls

| Control ID | Control Description |
|---|---|
| DC-001 | PHI/PII datasets prohibited in sandbox environments; violation triggers immediate sandbox termination and security incident report |
| DC-002 | All adversarial test datasets versioned in `s3://meridian-adversarial-samples/` with read-only access except for AI Safety Engineer role |
| DC-003 | Model outputs produced during safety testing auto-purged from sandbox storage within 24 hours of sandbox termination |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | KPI Name | Measurement | Target | Reporting Cadence |
|---|---|---|---|---|
| KPI-01 | Safety Test Coverage | % of deployed models with current SDP | 100% | Monthly |
| KPI-02 | Red Team Engagement Cadence | Days since last red team per Safety-Critical model | ≤180 days | Monthly |
| KPI-03 | Critical Finding Resolution Time | Median days from CRITICAL finding to verified remediation | ≤14 days | Weekly |
| KPI-04 | HIGH Finding Resolution Time | Median days from HIGH finding to verified remediation | ≤30 days | Monthly |
| KPI-05 | Production Safety Incident Rate | Incidents per Safety-Critical model per quarter | ≤0 | Monthly |
| KPI-06 | Input Distribution Shift Alerts | Models with PSI >0.25 unresolved after 7 days | 0 | Weekly |
| KPI-07 | Adversarial Robustness Regression | Models with ≥5% robust accuracy degradation vs. previous version | 0 | Per-release |
| KPI-08 | SDP Review Cycle Time | Median calendar days from SDP submission to approval decision | ≤10 days | Monthly |

### 7.2 Safety Monitoring Dashboards

The MLOps team shall maintain the following dashboards in the Meridian AI Observability Platform (Grafana instance at `grafana.meridian.internal/ai-safety`):

| Dashboard Name | Content | Refresh Rate | Access |
|---|---|---|---|
| Safety Test Execution Status | Current test runs, pass/fail rates, blocked deployments | Real-time | AI/ML Engineering, QA |
| Adversarial Robustness Trends | Robust accuracy vs. perturbation magnitude over model versions | Daily | AI/ML Engineering |
| Production Safety Monitor | Input PSI, output confidence distributions, anomaly detection alerts | Real-time | MLOps, AI Safety |
| Safety Incident Overview | Open incidents, MTTR, incident severity distribution | Real-time | All AI/ML personnel |
| SDP Compliance Tracker | Models with valid SDP, approaching expiration, expired SDPs | Daily | AI Safety, Chief AI Officer |

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Delivery Method |
|---|---|---|---|
| Weekly Safety Status | AI Safety Team, MLOps Lead | Weekly (Monday 10AM) | Automated email from ATRL |
| Monthly Safety Metrics | Chief AI Officer, VP Engineering, Product Management | Monthly (1st business day) | Grafana snapshot + narrative summary |
| Quarterly Safety Review | AI Safety Alignment Board | Quarterly | Formal presentation with trend analysis |
| Annual AI Safety Report | Board of Directors (via CTO) | Annual | 20-30 page comprehensive report |

### 7.4 Alert Thresholds

The following conditions shall trigger automated alerts to the on-call MLOps engineer and AI Safety Engineer:

| Alert ID | Condition | Severity | Response SLA |
|---|---|---|---|
| ALERT-01 | Production model PSI >0.30 sustained for >1 hour | SEV-2 | Acknowledge 15 min, mitigate 4 hours |
| ALERT-02 | Production model output confidence distribution shifts by >2σ | SEV-3 | Acknowledge 1 hour, investigate 24 hours |
| ALERT-03 | Constitutional constraint bypass detected in production | SEV-1 | Acknowledge 5 min, model offline 15 min |
| ALERT-04 | Input distribution guard trigger rate >5% | SEV-3 | Acknowledge 1 hour, investigate 24 hours |
| ALERT-05 | SDP expiration within 7 days for Safety-Critical model | SEV-3 | Renew SDP within 7 days |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

| Exception Type | Description | Approver |
|---|---|---|
| E-001: Safety Test Deferral | Defer specific safety tests to post-deployment window | Chief AI Officer |
| E-002: Threshold Relaxation | Accept relaxed quantitative safety threshold | Chief AI Officer + VP Engineering |
| E-003: Red Team Waiver | Deploy Safety-Critical model without full red team engagement | Chief AI Officer + CISO |
| E-004: Partial SDP Acceptance | Deploy with incomplete SDP, missing artifacts documented and timeline for completion committed | Chief AI Officer |
| E-005: Known Vulnerability Acceptance | Accept a known safety vulnerability with compensating controls | Chief AI Officer + Product VP |

### 8.2 Exception Request Procedure

1. **Initiator:** AI/ML Engineer or Product Manager identifies need for exception
2. **Documentation:** Exception request documented via ServiceNow form `AI_Safety_Exception` containing:
   - Exception type (from Table 8.1)
   - Model identifier and risk classification
   - Specific requirement being excepted
   - Business justification and urgency
   - Proposed compensating controls
   - Proposed remediation timeline and plan
3. **Risk Assessment:** AI Safety Engineer evaluates the exception, prepares a risk assessment memo documenting the residual safety risk
4. **Approval Chain:**
   - AI Safety Engineer recommendation (Approve/Deny/Approve with Conditions)
   - Product Manager concurrence
   - Approver per Table 8.1
5. **Conditions and Tracking:** If approved, conditions tracked in Jira as blocker issues linked to the model release epic; exception expiration date set (not to exceed 90 days)
6. **Closure:** Exception closed when conditions met or exception expires; expired exceptions trigger automatic escalation to VP Engineering

### 8.3 Emergency Rollback Procedure

In the event of a confirmed safety incident in production:

1. **Incident Declaration:** Any personnel observing AI behavior reasonably believed to constitute a safety incident shall immediately declare a SEV-1 incident via PagerDuty (`pagerduty.meridian.internal/ai-safety`)
2. **Model Takedown:** On-call MLOps Engineer shall, within 15 minutes of incident declaration:
   - Route 100% of traffic away from the affected model to the safe fallback
   - If no safe fallback exists, take the affected endpoint offline completely
   - Post incident notification to `#ai-safety-incidents` Slack channel
3. **Containment:** AI Safety Engineer shall, within 2 hours:
   - Confirm the incident scope and affected traffic volume
   - Capture all relevant logs and inputs for forensic analysis
   - Determine if patient or financial impact has occurred
4. **Recovery:** Model restored to service only after:
   - Root cause identified and documented
   - Remediation verified in sandbox
   - Updated SDP with root cause analysis approved
   - Chief AI Officer authorizes restoration in writing

### 8.4 Escalation Path

| Level | If unresolved within | Escalate to |
|---|---|---|
| AI Safety Engineer | N/A (initial handler) | Lead AI Safety Engineer |
| Lead AI Safety Engineer | 24 hours | Chief AI Officer |
| Chief AI Officer | 5 business days | CTO |
| CTO | 5 business days | CEO and Board Risk Committee |

---

## 9. Training Requirements

### 9.1 Required Training Modules

| Training Code | Module Name | Target Audience | Frequency | Duration |
|---|---|---|---|---|
| T-AISAF-101 | AI Safety Foundations at Meridian | All personnel in AI/ML Engineering, Product, QA | Within 30 days of hire; annual refresher | 4 hours |
| T-AISAF-201 | Adversarial Robustness Testing Practitioner | AI Safety Engineers, QA Engineers (AI-specialized) | Initial certification; recertification biennial | 16 hours + practical exam |
| T-AISAF-202 | Red Team Operations Methodology | AI Safety Engineers designated as Red Team Operators | Initial certification; recertification biennial | 24 hours + supervised engagement |
| T-AISAF-301 | Safety-Critical Model Development | All AI/ML Engineers developing Safety-Critical models | Prior to first Safety-Critical project | 8 hours |
| T-AISAF-401 | AI Safety for Product Managers | All Product Managers for AI products | Annual | 3 hours |

### 9.2 Training Delivery

All training modules shall be delivered through the Meridian Learning Management System (LMS) at `lms.meridian.internal`. Training content is maintained by the AI Safety Engineering team, reviewed annually for currency, and updated as needed when:
- New attack techniques are published in academic literature
- Meridian experiences a safety incident revealing a training gap
- Regulatory requirements change

### 9.3 Training Compliance Tracking

| Metric | Target | Measurement |
|---|---|---|
| Training compliance rate (overdue rate) | <5% personnel overdue | LMS dashboard reported monthly |
| T-AISAF-201 certification rate (qualified personnel) | 100% of AI Safety Engineers certified | HR skills database |
| Annual refresher completion | ≥95% within 60 days of assignment | LMS dashboard |

### 9.4 Competency Verification

Personnel in safety-critical roles must demonstrate competency through:
1. Passing score (≥80%) on written examination
2. For T-AISAF-201 and T-AISAF-202: successful completion of a practical assessment (scored red team exercise or adversarial test suite execution on a provided sandbox model)
3. Supervised safety evaluation on a real Meridian model under mentorship (applies to new AI Safety Engineers)

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| SOP-AIML-010 | AI/ML Model Lifecycle Management | Defines lifecycle gates where safety testing is required |
| SOP-AIML-015 | Model Registry and Versioning | Defines registry structure where SDPs are stored |
| SOP-AIML-025 | AI/ML Incident Response | Defines incident response procedures; referenced by Section 8.3 |
| SOP-CLIN-030 | Clinical Model Validation | Defines clinical efficacy validation; safety testing is prerequisite |
| SOP-HPFS-015 | Fair Lending Model Validation | Defines fairness testing for financial models; complementary to safety |
| SOP-ISEC-012 | Application Security Testing | Defines general security testing; AI red teaming is complementary |
| SOP-ISEC-045 | Cloud Security Posture Management | Defines infrastructure security for sandbox environments |
| SOP-PRIV-008 | PHI Data Protection Audits | Defines data handling rules for sandbox environments |
| SOP-MLOPS-005 | Deployment Pipeline Governance | Defines deployment approval gates that consume SDP approval status |
| SOP-GRC-010 | Model Risk Management Framework | Defines overall model risk governance; safety risk is a component |

### 10.2 External Standards and Frameworks

| Reference | Title | Applicability |
|---|---|---|
| NIST AI 100-1 | Artificial Intelligence Risk Management Framework | Framework for AI risk categorization and management |
| ISO/IEC 42001:2023 | Artificial Intelligence Management Systems | International standard for AI governance (informative reference) |
| MITRE ATLAS | Adversarial Threat Landscape for Artificial-Intelligence Systems | Threat taxonomy referenced for red team planning |
| OWASP ML Top 10 | Machine Learning Security Risks | Risk catalog referenced for threat modeling |

### 10.3 Meridian Internal Tools and Systems

| System | Purpose | URL |
|---|---|---|
| MLflow Enterprise | Model registry and artifact storage (SDP storage) | `mlflow.meridian.internal` |
| ASAT | Automated Safety Assessment Toolkit (adversarial robustness) | `asat.meridian.internal` |
| ATRL | Adversarial Test Results Ledger (findings database) | `atrl.meridian.internal` |
| MATH | Meridian Alignment Test Harness (behavioral testing) | `math.meridian.internal` |
| Grafana AI Safety Dashboards | Safety monitoring dashboards | `grafana.meridian.internal/ai-safety` |
| ServiceNow - AI Safety Incident | Safety incident reporting and tracking | `servicenow.meridian.internal/ai_safety` |
| Confluence - AI Safety Templates | Safety test plan and report templates | `confluence.meridian.internal/aiml/safety-templates` |
| MLOps Platform Portal | Sandbox provisioning | `mlops.meridian.internal/sandbox/provision` |
| LMS | Training delivery and tracking | `lms.meridian.internal` |

### 10.4 Forms and Templates

| Form/Template ID | Name | Location |
|---|---|---|
| T-MSTP-001 | Model Safety Test Plan Template | Confluence templates |
| T-SDP-001 | Safety Demonstration Package Cover Sheet | Confluence templates |
| T-RTR-001 | Red Team Final Report Template | Confluence templates |
| T-AVR-001 | Alignment Verification Report Template | Confluence templates |
| T-CBR-001 | Capability Boundary Report Template | Confluence templates |
| T-KLD-001 | Known Limitations Disclosure Template | Confluence templates |
| T-DSC-001 | Deployment Safety Checklist Template | Confluence templates |

---

## 11. Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2022-06-15 | Dr. Marcus Rivera | Initial release. Established foundational safety testing framework for Clinical AI Platform models only. |
| 1.1 | 2022-11-08 | Sarah Chen, AI Safety Engineer | Added Section 5.3.3 Physical-World Robustness Testing for clinical imaging models. Minor corrections to adversarial threshold values. |
| 2.0 | 2023-03-20 | Dr. Marcus Rivera | Major revision: expanded scope to include HealthPay Financial Services and MedInsight Analytics. Introduced risk-proportional testing tiers. Added red teaming mandate (Section 5.4). Updated CEM matrix. Added training requirements (Section 9). |
| 2.1 | 2023-08-01 | James Okonkwo, Lead AI Safety Engineer | Incorporated lessons learned from Q2 2023 red team exercises. Refined adversarial robustness thresholds. Added Section 5.6 Capability Boundary Verification. Updated KPI targets. |
| 2.2 | 2023-11-15 | Dr. Marcus Rivera | Updated to align with NIST AI RMF 1.0 release. Added AI risk categorization references. Revised quarterly review requirements. Added Section 4.5 Alignment Verification mandate. Minor formatting updates across all sections. |
| 2.3 | 2024-01-22 | Sarah Chen, AI Safety Engineer | Corrected several typographical errors. Updated sandbox environment provisioning specifications to reflect new GPU cluster `meridian-safety-gpu-pool`. Updated Confluence template links. No substantive procedural changes. |
| 2.4 | 2024-04-24 | Dr. Marcus Rivera | Current version. Added alignment verification specification detail (Section 5.5). Refined red team methodology with structured phases. Added MLOps Engineer responsibilities for sandbox provisioning and alert response. Updated related SOP cross-references. Expanded reporting cadence requirements. Updated CEM exploitability definitions. |

---

**Document Control**

This document is maintained in the Meridian Policy Management System (ServiceNow Policy module). The controlled master copy is the electronic version accessible at `servicenow.meridian.internal/policy/SOP-AIML-020`. Printed copies are uncontrolled and valid only on the day of printing.

For questions regarding this SOP, contact the AI Safety Engineering team at `ai-safety-engineering@meridian.internal` or via Slack channel `#ai-safety-sop`.

**Approval Signatures**

| Role | Name | Signature | Date |
|---|---|---|---|
| SOP Owner | Dr. Marcus Rivera, Chief AI Officer | *Electronic signature on file* | 2024-04-24 |
| Approver | David Park, VP of Engineering | *Electronic signature on file* | 2024-04-24 |

---

*End of Document — SOP-AIML-020 v2.4*