---
sop_id: "SOP-FIN-007"
title: "Financial Model Validation"
business_unit: "Financial Services"
version: "1.3"
effective_date: "2024-05-23"
last_reviewed: "2025-12-13"
next_review: "2026-06-11"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SR 11-7"
status: "Active"
---

# Standard Operating Procedure: Financial Model Validation

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the requirements and processes for the validation of financial models utilized by Meridian Health Technologies, Inc. within the HealthPay Financial Services business unit. The purpose of this SOP is to ensure that financial models, including those used for credit scoring, patient financing, medical lending, and claims automation, are sound, properly implemented, and perform as expected, thereby supporting the integrity of financial operations and decision-making.

### 1.2 Scope

This SOP applies to all models developed, acquired, or significantly modified by the Financial Services business unit that are used for material financial decisions. This includes, but is not limited to:

| Model Category | Example Use Cases |
| :--- | :--- |
| Credit Scoring Models | Patient financing approvals, medical lending risk tiers |
| Fraud Detection Models | Claims anomaly detection, payment integrity scoring |
| Revenue Forecasting Models | Payment volume projections, delinquency rate forecasts |
| Pricing and Profitability Models | Loan product pricing, provider fee structure optimization |
| Automation Decision Models | Auto-adjudication of claims, automated payment plan assignments |

This SOP applies to all employees, contractors, and consultants within the Financial Services, Engineering, and Data Science teams who develop, deploy, monitor, or rely upon the output of financial models. It covers the entire model lifecycle, from initial development through decommissioning. The policy is applicable across all Meridian global offices where HealthPay Financial Services operates, including Boston, London, Singapore, and Toronto.

### 1.3 Exclusions

This SOP does not apply to:
- Purely clinical AI models governed under SOP-DS-014 (Clinical AI Lifecycle Management).
- General business intelligence dashboards not used for automated financial decisions.
- Third-party vendor models where Meridian acts solely as a data provider with no influence on model design or output, unless the output is used for a high-impact decision as defined in Section 5.2.1.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **Back-Testing** | The process of applying a model to historical data and comparing the predicted results to known actual outcomes. |
| **Benchmark Model** | A simpler, often rules-based or linear model used as a performance baseline for comparison against a primary model. |
| **Conceptual Soundness** | An assessment of the model's underlying theory, design logic, and the appropriateness of its methodology for the intended use case. |
| **High-Impact Decision** | A model output that directly results in an action with significant financial, legal, or health-related consequence for an individual patient. Examples include decline of a loan application, assignment to a collections pathway, or a change in a provider's settlement terms. |
| **Model** | A quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates. |
| **Model Developer** | The individual or team responsible for the initial design, coding, and documentation of a model. |
| **Model Owner** | The designated business stakeholder responsible for the model's use, performance, and governance throughout its lifecycle. Typically a Director-level or above role within Financial Services. |
| **Output Defect** | A model output that is factually incorrect, logically inconsistent, or outside pre-defined acceptable performance thresholds, requiring investigation. |
| **Overfitting** | A modeling error where a model learns the noise and random fluctuations in the training data to the extent that it negatively impacts the model's performance on new, unseen data. |
| **Performance Drift** | A degradation in a model's predictive accuracy or decisioning quality over time, as measured against defined key performance indicators. |
| **Validation** | A holistic, ongoing assessment designed to confirm that a model is performing as expected, in line with its design objectives and business use case. |
| **Validation Report** | A formal document summarizing the findings, conclusions, and recommendations from a validation exercise. |

---

## 3. Roles and Responsibilities

The following matrix defines the responsible parties for key activities within this SOP.

| Activity | Model Owner | Model Developer | Quality Review Team | Operational Analytics | VP, Financial Services | CFO |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Model Development & Initial Documentation** | C | R | I | I | I | I |
| **Pre-Deployment Validation** | A | R | C | I | I | I |
| **Annual Back-Testing** | R | C | I | A | I | I |
| **Ongoing Performance Monitoring** | A | C | C | R | I | I |
| **Validation Report Preparation** | R | C | C | I | A | I |
| **Exception Approval** | I | I | I | I | R | A |
| **Model Decommissioning** | R | C | I | I | A | I |

**Key:** R = Responsible for execution, A = Accountable (approver), C = Consulted, I = Informed

### 3.1 Detailed Role Descriptions

- **Model Owner (Product Director or Finance Director):** Serves as the business champion. Ensures the model meets its intended business purpose, allocates resources for validation activities, reviews and signs off on validation reports, and manages the model's lifecycle budget. The Model Owner is accountable for the model's performance in production.

- **Model Developer (Data Science Team):** Designs, codes, and conducts initial unit testing of the model. Prepares the initial model documentation, including design rationale, input data specifications, and development-test results. Assists in the remediation of defects found during back-testing.

- **Quality Review Team (QA Engineering):** Executes defined back-testing scripts, conducts A/B testing of model outputs, and documents defects in the code or logic. This team is distinct from the Model Developer but resides within the broader Engineering organization under the VP of Engineering.

- **Operational Analytics (Financial Services Operations):** Performs daily and weekly trend monitoring on model outputs. Detects and alerts on performance anomalies or drift against established baselines. This team manages the Datadog dashboards used for real-time model monitoring.

- **VP of Financial Services (Robert Liu):** Approves all model validation activities, acts as the primary escalation point for model performance issues, and has final sign-off authority for any model exceptions or risk acceptances at the business unit level.

- **Chief Financial Officer (James Thornton):** Provides final approval for all new high-impact decision models entering production and for any exceptions to this SOP. Ultimately accountable for the financial risk associated with model usage.

---

## 4. Policy Statements

1.  All financial models must undergo a documented validation process before deployment to production and before any significant change or update.

2.  Validation activities will be proportional to the materiality and complexity of the model. High-impact models are subject to more rigorous and frequent scrutiny.

3.  The Model Owner must maintain a complete and up-to-date lifecycle document for each active model, stored in the HealthPay Governance Confluence space.

4.  All models must undergo annual back-testing using an out-of-time sample of historical data not used in model development.

5.  Model performance must be monitored on an ongoing basis via operational dashboards with predefined alert thresholds. Any breach of an alert threshold must be investigated within 3 business days.

6.  A formal Validation Report must be prepared by the Model Owner and reviewed with the VP of Financial Services after each validation cycle. The report must be archived for audit purposes for a minimum of 7 years.

---

## 5. Detailed Procedures

### 5.1 Initial Model Validation (Pre-Deployment)

The goal of pre-deployment validation is to confirm that the model is fit for purpose and meets the business requirements defined by the Model Owner. This process must be completed and signed off before any model can begin scoring in a production context.

#### 5.1.1 Intake and Documentation Review

1.  The Model Developer opens a "Model Validation Request" Jira ticket in the `FIN-MODEL` project and links to the complete Model Documentation package.
2.  The Model Documentation must contain at minimum:
    - A business problem statement.
    - A detailed theory of approach and mathematical methodology.
    - A complete data dictionary of all input features and their sources.
    - Summary statistics of the training, testing, and hold-out datasets.
    - Code repository link (e.g., GitHub `meridian-healthpay/finance-models`).
    - Initial development-test results showing performance against a simple benchmark.
3.  The Model Owner reviews the documentation for completeness and conceptual soundness. If the documentation is insufficient, the request is assigned back to the developer.

#### 5.1.2 Code and Logic Review

1.  The Model Developer triggers a pull request (PR) in GitHub for the `production` branch.
2.  A Senior Engineer from the Quality Review Team, unaffiliated with the model's development, conducts a structured code review. The review checklist includes:
    - Adherence to Meridian Python/Spark coding standards (PEP-8 with team extensions).
    - Correct implementation of the mathematical logic described in the documentation.
    - Correct consumption of input data from Snowflake and Kafka streams.
    - Absence of hard-coded secrets; all credentials must be fetched from HashiCorp Vault.
    - Proper logging to Datadog with appropriate trace IDs.
3.  The reviewer logs all findings in the Jira ticket. Critical findings block production deployment.

#### 5.1.3 Pre-Deployment Back-Testing

1.  The Quality Review Team executes a back-testing script defined in the `backtesting-runbook` repository against a frozen historical dataset stored in the `s3://mht-fin-models-backtest/` bucket.
2.  The back-test must cover a period of at least 24 months and must use a dataset completely separate from the development sample (out-of-time validation).
3.  The primary performance metric is the Population Stability Index (PSI) for all input features, with a critical threshold of PSI >= 0.25. Secondary metrics (e.g., AUC, log-loss, precision/recall) are defined by the Model Owner in the business requirements.
4.  Results are automatically plotted by a SageMaker processing job and posted to the Jira ticket as artifacts.

#### 5.1.4 Shadow Mode Deployment (Optional)

For models replacing an existing decision process, the Model Owner may authorize a 30-day Shadow Mode deployment. In this phase, the model scores traffic in production but its decisions are logged by Kafka and not acted upon. The primary purpose is to compare live output distribution against the back-test results. A Shadow Mode Review must be completed and attached to the Jira ticket before full production activation.

#### 5.1.5 Final Approval and Activation

1.  Upon satisfactory completion of all preceding steps, the Model Owner documents the final "Go/No-Go" decision directly in the Jira ticket.
2.  The Model Owner presents a summary of findings to the VP of Financial Services during the bi-weekly HealthPay Product Operations meeting.
3.  For models classified as high-impact, the CFO must provide final electronic approval via Jira.
4.  Post-approval, the Model Owner triggers the production deployment runbook in Rundeck, which promotes the model artifact from the MLflow `Staging` registry to the `Production` registry and activates the SageMaker endpoint.

### 5.2 Ongoing Model Validation (Post-Deployment)

#### 5.2.1 Annual Back-Testing Cycle

Every active financial model must undergo a complete back-test on an annual basis. The Anniversary Date is the date of first production deployment. The Model Owner is responsible for initiating the annual cycle no later than 30 days before the Anniversary Date.

1.  **Data Extraction:** The Operational Analytics team extracts a new out-of-time historical dataset covering the most recent 12-24 months. The data is stored in the designated S3 back-testing bucket.
2.  **Execution:** The Quality Review Team re-runs the standard back-testing suite against this new dataset.
3.  **Results Analysis:** The Model Owner and Model Developer jointly review the results. The analysis must explicitly comment on:
    - Any degradation in evaluation metrics versus the prior back-test.
    - Feature drift analysis, particularly for high-importance features identified in the initial model documentation.
    - An assessment of whether the model continues to be conceptually sound for the current operating environment.
4.  **Documentation:** Results are documented in a standardized Annual Back-Test Results Template (Confluence: `FIN-MODEL/Templates/Annual-Backtest-Results`) and stored in the model's governance folder.

#### 5.2.2 Triggered Re-Validation Events

A full, out-of-cycle re-validation must be conducted if any of the following trigger events occur:

- An observed performance metric breaches a critical Datadog threshold for 5 consecutive business days.
- A significant source data system change (e.g., migration of a core claims system, introduction of a new patient management platform) that alters the semantics of a top-10 feature.
- A regulatory change that materially impacts the model's decision logic.
- A request from the Chief Compliance Officer, Chief Information Security Officer, or CFO.

The process for a triggered re-validation follows the full pre-deployment validation procedure described in Section 5.1, but its scope can be tailored to the specific trigger event, as agreed upon between the Model Owner and VP of Financial Services.

### 5.3 Model Decommissioning

When a model is no longer needed, it must be formally decommissioned.

1.  The Model Owner creates a "Model Decommissioning Request" Jira ticket.
2.  The request must include a justification and a plan to resolve any lingering dependencies (e.g., other models that consume its output as a feature).
3.  The VP of Financial Services approves the decommissioning request.
4.  Upon approval, the Engineering team will delete the SageMaker production endpoint and move the model artifact in the MLflow registry to the `Archived` state.
5.  The model's code repository is archived in GitHub.
6.  A final entry is made in the model's lifecycle document, and the document is moved to the "Decommissioned Models" section of the HealthPay Governance Confluence space.

---

## 6. Controls and Safeguards

The following administrative and technical controls are implemented to support the integrity of the model validation process.

| Control ID | Control Description | Control Type | Implementation |
| :--- | :--- | :--- | :--- |
| **FIN-CTRL-01** | **Separation of Duties:** The Quality Review Team conducting code review and back-testing must not report to the Director of Data Science. The team reports to the VP of Engineering to ensure independence from model developers. | Administrative | Organizational Chart; Jira Permission Scheme |
| **FIN-CTRL-02** | **Immutable Back-Test Data:** All datasets used for formal back-testing are stored in a write-once-read-many (WORM) S3 bucket. Once created, datasets cannot be overwritten or deleted for 7 years. | Technical | AWS S3 Object Lock in Compliance Mode |
| **FIN-CTRL-03** | **Model Registry Access Control:** Promotion of a model to the `Production` registry in MLflow requires a multi-person authorization: one from the Model Owner group and one from the Quality Review Team group. | Technical | MLflow Auth Plugin integrated with Okta SSO |
| **FIN-CTRL-04** | **Production Endpoint Change Logging:** All changes to production SageMaker endpoint configurations are logged to AWS CloudTrail. A Datadog monitor generates a P1 alert if an endpoint configuration change is not accompanied by a corresponding approved Jira ticket ID in the change metadata. | Technical | AWS CloudTrail; Datadog Custom Monitor |
| **FIN-CTRL-05** | **Ethical Fairness Check:** Prior to initial deployment, a fairness assessment across protected attributes (specifically race, ethnicity, sex, and age) must be performed using the `fairlearn` package. The results must be documented and signed off by the Chief Privacy Officer/DPO. | Administrative | Custom SageMaker Processing Job; Confluence Documentation |
| **FIN-CTRL-06** | **Offline Output Validation:** For models that generate offline outputs (e.g., daily reporting files), a checksum (SHA-256) of every generated file is calculated and compared against a known-good checksum before delivery to the downstream system. | Technical | AWS Lambda function triggered on S3 `PUT` events |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Ongoing Performance Monitoring

The Operational Analytics team is responsible for maintaining real-time monitoring dashboards in Datadog for all active models. Dashboard panels are created from the `meridian.financial.models.*` standard metric namespace.

**Tier 1 Metrics (Real-time Alerting):**

| Metric | Alert Threshold | Alert Type | Responder |
| :--- | :--- | :--- | :--- |
| `inference_latency_p99` | > 500ms for a 5-min window | P2 - High Latency | DevOps On-Call |
| `error_rate` | > 1% of all requests | P1 - Service Degradation | DevOps On-Call |
| `output_distribution_psi` | >= 0.30 versus 7-day rolling baseline | P3 - Data Drift Warning | Operational Analytics |

**Tier 2 Metrics (Weekly Review):**

- Volume-weighted average default rate for credit models vs. predicted rate.
- Approval rate and average approved amount by risk tier.
- Claims auto-adjudication rate (for automation models).

### 7.2 Validation Reporting

The culmination of each validation event (initial, annual, or triggered) is a formal Validation Report. The report must contain the following sections:

1.  **Executive Summary:** A non-technical synthesis for management.
2.  **Model Overview:** Description of purpose, methodology, and scope of use.
3.  **Validation Scope:** Description of the activities performed and their timing.
4.  **Findings and Results:**
    - Conceptual soundness review.
    - Data quality review.
    - Back-testing and benchmarking results.
    - Fairness assessment results (for initial validations).
    - Code review summary.
5.  **Limitations and Assumptions:** Explicit statement of the model's known weaknesses or constraints.
6.  **Recommendations and Action Items:** A clear list of remedial actions, with owners and due dates.
7.  **Overall Assessment:** A clear statement of whether the model is fit for its intended purpose.
8.  **Sign-off:** Electronic signatures of the Model Owner and VP of Financial Services.

### 7.3 Management Reporting Cadence

| Report | Audience | Frequency | Medium |
| :--- | :--- | :--- | :--- |
| Model Health Dashboard Briefing | VP of Financial Services, Director of Operations | Weekly | Datadog Dashboard Screen-share |
| HealthPay Model Portfolio Summary | CFO, Chief Risk Officer (if any) | Quarterly | Formal Confluence Report |
| Annual Model Validation Summary | Audit Committee, AI Governance Committee | Annually | Board Presentation Slide Deck |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling Process

A formal exception to any clause of this SOP must be requested in writing if strict adherence is not feasible or will cause undue operational impact without commensurate risk reduction.

1.  **Request:** The Model Owner submits a "Model Validation Exception Request" using the template in the HealthPay Jira Service Management portal.
2.  **Risk Assessment:** The request must articulate the specific policy clause from which the exception is sought, the business justification, the compensating controls to be applied, and the duration for which the exception is needed.
3.  **Approval Authority:**
    - Exceptions related to a delay in annual back-testing (up to 60 days) can be approved by the VP of Financial Services.
    - Exceptions related to a pre-deployment code review for a non-high-impact model can be approved by the VP of Financial Services.
    - All other exceptions, and any exception for a high-impact model, must be approved by the CFO.
4.  **Registration and Tracking:** All approved exceptions are logged in a central register maintained by the Chief Compliance Officer and reviewed quarterly. No exception may be granted for a period exceeding 12 months without a full re-approval.

### 8.2 Escalation Path for Unresolved Model Defects

When a model defect is identified that cannot be resolved by the Model Owner and Quality Review Team within the expected timeframe, the following escalation path is activated:

1.  **Week 1:** Issue identified and owned by the Model Owner. A remediation plan is documented in the associated Jira ticket.
2.  **Week 2 (Escalation 1):** If remediation is not complete, the VP of Financial Services is notified and joins the remediation stand-up. The model may continue to run if compensating manual reviews are put in place.
3.  **Week 3 (Escalation 2):** If the defect remains unresolved, the VP of Financial Services will escalate to the CFO with a recommendation to either continue with heightened manual controls or to temporarily suspend the model's use in production. The CFO makes the final decision.

---

## 9. Training Requirements

All personnel identified in the Roles and Responsibilities matrix (Section 3) must complete role-appropriate training prior to engaging in any model validation activity.

| Role(s) | Required Training | Frequency | Delivery Method | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| Model Developers, Quality Review Team, Operational Analytics | `FIN-101: Financial Model Development & Validation Standards` | Annually | LMS (Workday Learning) | Automated via Workday |
| Model Owners | `FIN-201: Model Ownership & Governance Responsibilities` | Annually | LMS (Workday Learning) | Automated via Workday |
| All Finance and Data Science Staff | `COR-105: Ethical Use of Data & AI` | Annually | LMS (Workday Learning) | Automated via Workday |
| VP, Financial Services; CFO | `EXC-301: Executive Model Risk Overview` | Bi-annually | In-person workshop | Attendance roster signed by GC |

New hire onboarding must include the relevant foundational training within the first 30 days of employment. Failure to complete annual refresher training will result in the suspension of system access privileges for the associated validation tools (e.g., MLflow, SageMaker, back-testing S3 buckets) until compliance is achieved.

---

## 10. Related Policies and References

This SOP is one component of Meridian Health Technologies' integrated governance framework. It should be read and applied in conjunction with the following:

**Internal Meridian Policies:**

| Policy ID | Policy Title |
| :--- | :--- |
| SOP-DS-002 | Algorithmic Change Management |
| SOP-ENG-005 | Machine Learning Lifecycle Management |
| SOP-SEC-010 | Access Control and Identity Management |
| SOP-SEC-012 | Cryptographic Key Management with HashiCorp Vault |
| SOP-QA-004 | Code Review and Quality Assurance for Production Systems |
| SOP-CMP-003 | Complaint and Dispute Handling for Automated Decisions |
| SOP-CPO-001 | Data Protection Impact Assessment (DPIA) Procedure |

**External Standards and References:**

| Document | Description |
| :--- | :--- |
| NIST AI 100-1 | Artificial Intelligence Risk Management Framework |
| HITRUST CSF v11 | Common Security Framework, Control Maturity Scoring |
| ISO 27001:2022 | Annex A Controls, specifically A.8.25 (Secure Development Life Cycle) |

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2022-09-18 | Sarah Jenkins (Former Dir. of Ops) | Initial version of the policy. Defined pre-deployment validation and annual back-testing requirements. |
| 1.1 | 2023-04-05 | Michael Chen (Data Science Lead) | Added Section 5.1.4 (Shadow Mode Deployment); clarified role of QA Engineering in code review; updated the code review checklist. |
| 1.2 | 2023-11-15 | Robert Liu (VP, Fin. Services) | Introduced formal model decommissioning procedure (Section 5.3); added ethical fairness check control (FIN-CTRL-05); aligned terminology with the new global AI governance framework. |
| 1.3 | 2024-05-23 | Anya Sharma (Compliance Analyst) | Comprehensive annual review. Updated roles to reflect the new Operational Analytics team; added WORM bucket control (FIN-CTRL-02); clarified CFO approval authority for high-impact models; updated all cross-referenced SOP IDs. |