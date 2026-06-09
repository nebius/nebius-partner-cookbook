---
sop_id: "SOP-AIML-005"
title: "Feature Engineering and Feature Store Operations"
business_unit: "AI/ML Engineering"
version: "1.4"
effective_date: "2025-03-26"
last_reviewed: "2026-09-20"
next_review: "2027-03-10"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "NIST AI RMF"
  - "SR 11-7"
status: "Active"
---

# STANDARD OPERATING PROCEDURE: FEATURE ENGINEERING AND FEATURE STORE OPERATIONS

**SOP-AIML-005 | Version 1.4**
**Effective Date: 2025-03-26**
**Owner: Dr. Marcus Rivera, Chief AI Officer**
**Classification: Internal**

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for feature engineering, feature pipeline management, and feature store operations at Meridian Health Technologies, Inc. The purpose of this SOP is to standardize the creation, documentation, storage, serving, and governance of features used across all machine learning models developed or deployed by the AI/ML Engineering organization. Standardized feature operations reduce duplication of effort, ensure consistency between training and inference environments, enable feature reuse across models, and mitigate data leakage risks that could compromise model validity and patient safety.

### 1.2 Scope

This SOP applies to:

- **All Business Units**: Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and internal supporting functions that develop or consume ML features.
- **All Environments**: Development, staging, pre-production, and production feature stores and pipelines hosted on AWS (us-east-1, eu-west-1) and Azure DR environments.
- **All Feature Types**: Batch features, streaming features, on-demand computed features, and externally sourced features ingested into the Meridian Feature Store.
- **All Personnel**: AI/ML Engineers, Data Engineers, ML Platform Engineers, Data Scientists, ML Operations personnel, and any contractors or third parties who interact with Meridian feature systems.

This SOP covers the full feature lifecycle: feature ideation, pipeline development, feature store registration, documentation, serving for training and inference, monitoring for drift, and deprecation.

### 1.3 Out of Scope

- Raw data ingestion and ETL/ELT pipelines managed by the Data Platform team under **SOP-DATA-012**.
- Model training orchestration, which is governed by **SOP-AIML-003**.
- Model deployment and serving infrastructure governed by **SOP-AIML-004**.

---

## 2. Definitions and Acronyms

| Term | Definition |
|------|------------|
| **Feature** | An individual measurable property or characteristic derived from raw data that serves as input to a machine learning model. |
| **Feature Group** | A logical collection of related features that share a common source, refresh cadence, and entity key. |
| **Feature Store** | The centralized repository (Meridian Feature Store, built on AWS SageMaker Feature Store and Amazon DynamoDB) that stores, versions, and serves features for training and inference. |
| **Feature Pipeline** | The end-to-end data processing workflow that ingests source data, applies transformations, and publishes features to the Feature Store. |
| **Online Store** | The low-latency feature serving layer optimized for real-time inference (<50ms p99 latency SLA). |
| **Offline Store** | The historical feature repository in Amazon S3 partitioned by date, optimized for batch training queries and point-in-time lookbacks. |
| **Point-in-Time Join** | A feature retrieval operation that joins historical feature values to training labels based on exact timestamps, preventing future-looking data leakage. |
| **Feature Spec** | The mandatory documentation artifact that defines a feature's business meaning, lineage, transformation logic, freshness SLA, and data class. |
| **Data Leakage** | The improper introduction of future or target-dependent information into training datasets, resulting in overestimated model performance. |
| **Training-Serving Skew** | The divergence between features computed during model training and features computed during inference, caused by pipeline discrepancies, data drift, or inconsistent transformation logic. |
| **Entity** | A domain object (e.g., Patient, Claim, Provider, Member) identified by a unique key that anchors a Feature Group. |
| **Feature Registry** | The catalog service within the Meridian Feature Store that indexes all registered Feature Groups, their schemas, and metadata. |
| **TFDV** | TensorFlow Data Validation, a library for analyzing and validating ML data and features. |
| **Feathr** | The open-source feature store SDK used by Meridian for feature definition and ingestion logic. |

---

## 3. Roles and Responsibilities

| Role | Responsible Party | Responsibilities |
|------|-------------------|------------------|
| **Feature Store Owner** | Dr. Marcus Rivera, Chief AI Officer | Approves feature store platform changes, capacity planning, and enterprise feature governance policies. |
| **Feature Store Platform Lead** | Sophia Chen, Principal ML Platform Engineer | Manages Feature Store infrastructure, platform SLAs, SDK maintenance, and store performance. Approves new Feature Group onboarding. |
| **Feature Author** | Assigned AI/ML Engineer or Data Scientist | Designs, develops, tests, and documents individual features and Feature Groups. Submits Feature Specs for review. Owns feature pipelines through staging. |
| **Feature Reviewer** | Designated Senior AI/ML Engineer (rotating assignment, 1 per squad) | Reviews Feature Specs, pipeline code, unit tests, and point-in-time validation results for completeness and leakage prevention. |
| **Data Steward** | Assigned by CDO office per data domain | Approves use of PHI/PII-derived features. Validates data classification tagging in Feature Specs. Ensures data source usage aligns with data use agreements. |
| **Model Validation Engineer** | Member of HealthPay Model Validation Squad (reporting to VP of Engineering) | Conducts validation review of features and Feature Groups used by HealthPay models per validation checklist in Section 5.6. |
| **MLOps Engineer** | Assigned MLOps team member | Manages CI/CD pipelines for feature pipelines, monitors feature drift in production, and operates feature serving infrastructure. |
| **Release Manager** | Central Release Management team | Approves production deployment of feature pipelines via change advisory board process. |

### 3.1 RACI Matrix

| Activity | Feature Author | Feature Reviewer | Platform Lead | Data Steward | Validation Engineer | MLOps Engineer |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Feature Ideation & Design | **R, A** | C | I | C | - | - |
| Feature Spec Submission | **R, A** | **R** | - | I | - | - |
| Pipeline Development & Unit Test | **R, A** | C | - | - | - | C |
| Feature Store Onboarding | C | **A** | **R** | - | - | C |
| Data Leakage Prevention Check | **R** | **A** | - | - | - | I |
| Validation Review (HealthPay only) | I | I | - | - | **R, A** | I |
| Production Deployment | I | I | **A** | - | - | **R** |
| Drift Monitoring & Alerting | I | I | - | - | - | **R, A** |

*R = Responsible (does the work), A = Accountable (approves/signs off), C = Consulted, I = Informed*

---

## 4. Policy Statements

### 4.1 Feature Store Mandate

All features used by any ML model in a production, staging, or pre-production environment MUST be registered in the Meridian Feature Store. Ad-hoc features computed in notebooks for exploratory analysis are exempt from registration but MUST NOT be used for any model validation results reported to stakeholders.

### 4.2 Feature Documentation Mandate

Every Feature Group registered in the Meridian Feature Store MUST have a completed Feature Spec, approved by a Feature Reviewer and, where applicable, a Data Steward. No feature pipeline shall be deployed to production without a signed-off Feature Spec.

### 4.3 Pipeline Definition as Code

All feature pipelines MUST be defined in code using the Meridian Feature Engineering SDK (built on Feathr) and stored in the `meridian-ml/feature-pipelines` repository. Manual, UI-driven feature creation in the AWS Console is prohibited for production features.

### 4.4 Training-Serving Consistency

The transformation logic used to generate a feature for model training MUST be identical to the logic used to generate that feature for inference. Features SHALL be defined once in the Feature Store and consumed by both training and inference serving systems from that single definition. Copy-pasting feature code between training notebooks and inference pipelines is strictly prohibited.

### 4.5 Point-in-Time Correctness

All feature pipelines supporting model training MUST implement point-in-time joins to prevent temporal data leakage. As-of timestamps MUST be used for all historical feature retrievals.

### 4.6 Data Classification Handling

Features derived from Protected Health Information (PHI) or Personally Identifiable Information (PII) MUST be tagged accordingly in the Feature Registry. Access to these Feature Groups SHALL be restricted to authorized workloads and personnel.

---

## 5. Detailed Procedures

### 5.1 Feature Ideation and Design

#### 5.1.1 Triggering Event

Feature development is triggered by a model requirement identified in a Model Development Plan (MDP) or by an approved feature request for an existing model iteration. Feature Authors shall consult the Feature Registry before beginning development to prevent duplicate feature creation.

#### 5.1.2 Feasibility Assessment

The Feature Author shall conduct a brief feasibility assessment covering:

1. **Source Data Availability**: Confirm that the required source data exists in Meridian's data lake (AWS S3) or streaming bus (Amazon Kinesis/MSK) with the necessary latency.
2. **Freshness Requirements**: Determine whether the feature requires real-time computation (sub-second), near-real-time computation (minutes), batch daily computation, or batch weekly computation.
3. **PHI/PII Assessment**: Determine whether the source data contains PHI/PII and whether the resulting feature will retain PHI/PII characteristics.
4. **Computational Estimate**: Roughly estimate the compute resources required (Spark/EMR or AWS Glue job sizing).

The Feature Author shall document this feasibility assessment in the Feature Spec preamble section.

### 5.2 Feature Spec Creation and Review

#### 5.2.1 Feature Spec Template

Every Feature Group MUST be accompanied by a completed Feature Spec using the approved template available in the `meridian-ml/feature-specs` repository. The Feature Spec sections and required fields are:

**Section A: Administrative**
- Feature Group Name (must follow naming convention: `{domain}_{entity}_{description}_{version}`)
- Feature Author(s)
- Date of Creation
- Business Unit Sponsor
- Associated Model(s) or Use Case(s)

**Section B: Business Description**
- Business purpose of the feature group in plain language
- Intended use, limitations, and known edge cases
- Regulatory data classification: [PHI | PII | Sensitive Financial | Internal | Public]

**Section C: Technical Specification**
- Source data tables/topics (full qualified names)
- Entity key column
- Timestamp column for point-in-time joins
- Transformation logic description in prose (supplemented by code reference)
- Expected output schema (column names, data types, nullable constraints)
- Computation mode: [Batch Daily | Batch Weekly | Streaming | On-Demand Request]
- Expected data volume (rows per day, average row size)

**Section D: Freshness and SLA**
- Required freshness (end-to-end pipeline latency SLA): [<100ms | <5min | <4hr | <24hr | <72hr]
- Expected ready-by time each day (for batch features), specified in UTC
- Backfill requirements (how many days of history needed for initial training)

**Section E: Quality Expectations**
- Expected value ranges or distributional characteristics (for drift monitoring baseline)
- Known seasonal patterns or expected shifts
- Null rate expectations and acceptability thresholds

**Section F: Validation Results**
- Point-in-time join validation results summary
- Training-serving consistency test results
- Unit test coverage percentage (minimum 85% for production features)

#### 5.2.2 Feature Spec Review Process

1. Feature Author submits Feature Spec via pull request to `meridian-ml/feature-specs` tagged with `feature-spec-review`.
2. Feature Reviewer reviews within **3 business days**, using the Feature Spec Review Checklist:
   - [ ] Naming convention compliant
   - [ ] Entity key correctly identified
   - [ ] Timestamp column specified for point-in-time correctness
   - [ ] Data classification tagged
   - [ ] Transformation logic documented and consistent with pipeline code
   - [ ] Pipeline code present in corresponding PR in `meridian-ml/feature-pipelines`
   - [ ] Unit tests present and passing
   - [ ] Point-in-time validation script included and results documented
3. For features tagged as PHI or PII, a Data Steward is added as a mandatory reviewer.
4. For features supporting HealthPay models, a Model Validation Engineer reviews Section E (Quality Expectations) for sufficiency of drift baseline definition.
5. Upon approval, Feature Reviewer merges the PR and registers the Feature Group in the Feature Registry via the Meridian Feature Store CLI: `meridian-featurestore register --spec-path <path>`

### 5.3 Feature Pipeline Development

#### 5.3.1 Repository and Branching

All production feature pipelines SHALL reside in the `meridian-ml/feature-pipelines` repository. Feature Authors work on feature branches named `feature/{FeatureGroupName}`. Merges to `main` require an approved Feature Spec and passing CI.

#### 5.3.2 Pipeline Structure

Every feature pipeline MUST follow the canonical pipeline structure:

```
feature-pipelines/
└── {domain}/
    └── {entity}/
        └── {feature_group_name}/
            ├── pipeline.py           # Main pipeline definition using Meridian Feathr SDK
            ├── transformations.py    # Feature transformation logic (pure functions)
            ├── transformations_test.py  # Unit tests for transformation logic
            ├── pt_validation.py      # Point-in-time validation script
            ├── feature_spec.yaml     # Approved Feature Spec in machine-readable format
            └── README.md             # Quick reference
```

#### 5.3.3 Transformation Logic Standards

1. **Deterministic Transformations**: All feature transformations must be deterministic functions of their inputs. Use of non-deterministic operations (random sampling, UUID generation) within feature transformations is prohibited.
2. **Pure Functions**: Transformation code in `transformations.py` must consist of pure functions that accept DataFrames or streaming event objects and return transformed DataFrames/features. Stateful operations must use the Feature Store's built-in state management primitives and be documented.
3. **Time-Bound Operations**: Any windowed aggregation (e.g., rolling 30-day averages) must explicitly declare the window boundary using event timestamps, not processing time. Lag-based windows (e.g., "30 days before label date") must be parameterized.
4. **Null Handling**: All transformation functions must include explicit null handling logic. The Feature Author must document the intended behavior: null propagation, default value imputation, or row exclusion. Default value imputation values must be chosen with business justification and documented in the Feature Spec.
5. **Schema Enforcement**: The output schema of `transformations.py` must match the schema declared in the Feature Spec exactly. Column ordering, names, and data types are enforced by CI schema validation.

#### 5.3.4 Pipeline CI/CD

Feature pipelines use the Meridian CI/CD workflow defined in `.github/workflows/feature-pipeline-ci.yml`. The workflow stages are:

1. **Lint & Format**: Python code formatting (Black with `--line-length=100`), import sorting (isort), and linting (flake8 with project-specific rules).
2. **Unit Tests**: `pytest` execution of `transformations_test.py`. Minimum coverage: 85%.
3. **Schema Validation**: Validate that pipeline output matches registered Feature Spec schema.
4. **Point-in-Time Validation**: Execute `pt_validation.py` against a sampled historical dataset with known labels. Assert no future timestamps leak into training windows.
5. **Build**: Package pipeline as a Docker image and push to Amazon ECR.
6. **Deploy to Staging**: Deploy to staging Feature Store environment. Run for minimum 3 days of execution before production promotion.
7. **Promotion Request**: Feature Author submits a promotion request via ServiceNow change request, attaching staging execution metrics and Feature Spec approval records.

### 5.4 Feature Store Registration and Serving

#### 5.4.1 Registration Command

Upon Feature Spec approval AND successful staging deployment (minimum 3 days), the Feature Author registers the Feature Group for production serving using the CLI:

```bash
meridian-featurestore register \
  --spec-path path/to/feature_spec.yaml \
  --pipeline-arn arn:aws:sagemaker:us-east-1:{account}:pipeline/{pipeline} \
  --online-store \
  --offline-store \
  --ttl-days 400
```

The `--online-store` flag is required only if the feature will be served for real-time inference. The `--ttl-days` parameter sets offline storage retention.

#### 5.4.2 Online Store Configuration

For features requiring online serving (<50ms p99 latency):

- Features are materialized to Amazon DynamoDB tables.
- DynamoDB throughput is configured per Feature Group based on estimated request volume documented in the Feature Spec.
- Online store TTL (DynamoDB TTL attribute) MUST be set for features with finite freshness windows. For daily batch features, set TTL to 48 hours to ensure stale data is expired.
- For streaming features, DynamoDB Streams is enabled with a Lambda processor that updates the online store on each source event.

#### 5.4.3 Offline Store Configuration

For batch training:

- Features are stored in Amazon S3 at `s3://meridian-featurestore-offline/{domain}/{entity}/{feature_group_name}/` partitioned by event date (`YYYY/MM/DD`).
- Data format: Apache Parquet with Snappy compression.
- Feature retrieval for training uses the Meridian Feature Store SDK's `get_historical_features()` method, which accepts a training event DataFrame with entity keys and event timestamps performing a point-in-time correct join automatically.

### 5.5 Data Leakage Prevention Procedures

Data leakage prevention is a mandatory part of the feature development lifecycle. The following procedures must be executed prior to production registration.

#### 5.5.1 Temporal Leakage Check

The Feature Author must create and execute a `pt_validation.py` script that:

1. Loads a labeled training dataset (entity key + label timestamp + label value).
2. Retrieves historical feature values using `get_historical_features()` with the exact label timestamps.
3. For each feature, computes the Pearson correlation between feature value and time delta to the training label. Flags any correlation > 0.05 as potential temporal leakage.
4. Generates a time-travel dataset by shifting the retrieval timestamp artificially forward by 1 day, 7 days, and 30 days. Asserts that features that should not contain future information (e.g., "next month's predicted admissions") are NULL or missing at future timestamps.

Results from `pt_validation.py` are stored as artifacts in the CI pipeline and attached to the Feature Spec PR.

#### 5.5.2 Feature Partitioning Check

For batch features computed daily:

- Batch jobs partition output by the "effective date" equal to the source data timestamp ceiling truncated to day boundary, NOT the job execution date.
- Partition columns: `event_date`, NOT `processing_date`.
- CI tests assert that `processing_date` is not used as an input to any transformation function.

#### 5.5.3 Label-Aware Feature Exclusion

For features that could inadvertently encode the target variable:

- The Feature Author must provide a Label-Leakage Assessment in the Feature Spec (Section F, item 4), listing each feature and its independence rationale.
- For HealthPay models specifically, a Model Validation Engineer verifies that no feature is derived directly from, or is a proxy for, the claim outcome status that would be known only after the fact.

### 5.6 Validation Procedures

#### 5.6.1 HealthPay-Specific Validation

For feature groups that support HealthPay Financial Services models, the following additional validation steps are performed:

1. **Validation Review**: A Model Validation Engineer from the HealthPay Model Validation Squad reviews the Feature Spec, pipeline code, and pt_validation results. This validator is a member of the AI/ML Engineering organization but is not a member of the Feature Author's immediate squad. The validator is selected from a rotating assigned pool to ensure a second set of eyes on each feature group.

2. **Validation Checklist**, items include:
   - Transformation logic review and reproducibility
   - Unit test coverage verification (>85%)
   - Point-in-time validation results review
   - Feature Spec completeness verification
   - Online-offline consistency check execution
   - Manual spot-check of 50 rows from offline store vs. computed values

3. **Validation Documentation**: The Validation Engineer attaches a signed-off "Feature Validation Summary" document to the Feature Spec PR before the PR can be merged for HealthPay-bound features.

4. **Model Inventory Registration**: Upon validation approval, the Feature Group is added to the HealthPay Model Inventory (maintained in `meridian-ml/model-inventory`), recording which feature groups are associated with which HealthPay models.

### 5.7 Feature Deprecation

When a feature is no longer needed or is being replaced:

1. The Feature Author or designated maintainer files a Feature Deprecation Notice via pull request to the Feature Spec, adding `status: deprecated` and a deprecation effective date at least **90 days** in the future.
2. The Feature Author identifies all downstream models consuming the feature via the Feature Registry dependency graph, notifying the model product managers.
3. After the effective date, the Feature Author removes the online store materialization via CLI: `meridian-featurestore deregister-online {feature_group_name}`.
4. Offline store data is retained for auditability per the data retention schedule (**SOP-DATA-014**), but no new partitions are created.

---

## 6. Controls and Safeguards

### 6.1 Access Controls

| Resource | Access Control Mechanism | Permissions |
|----------|--------------------------|-------------|
| Feature Store Offline (S3) | AWS IAM + S3 bucket policies | Read: `ml-training-role`, `ml-inference-role`; Write: `feature-pipeline-role` only |
| Feature Store Online (DynamoDB) | AWS IAM + DynamoDB fine-grained access | Read: `ml-inference-role`; Write: `feature-pipeline-role` only |
| Feature Registry (DynamoDB metadata table) | AWS IAM | Read: all ML roles; Write: Feature Store Platform Lead IAM role only |
| Feature Pipeline CI/CD | GitHub branch protection + CODEOWNERS | `main` branch: requires PR approval from Feature Reviewer + Platform Lead for infra changes |
| PHI/PII Feature Groups | Additional IAM condition tag `data-classification=phi` | Access restricted to roles with explicit PHI-approved tag |

### 6.2 Pipeline Execution Controls

- All production feature pipeline executions MUST be triggered through AWS Step Functions state machines, not ad-hoc notebooks or manual CLI invocations.
- AWS Step Functions execution logs are retained in Amazon CloudWatch Logs for minimum **365 days**.
- Failed pipeline executions for PHI-tagged features trigger automatic notifications to the Data Steward via Amazon SNS.
- Backfill executions (>7 days of historical data) require a change request approved by the Feature Store Platform Lead.

### 6.3 Encryption Controls

- Feature Store offline S3 buckets enforce AES-256 server-side encryption via bucket policy (deny `s3:PutObject` without `x-amz-server-side-encryption: AES256`).
- DynamoDB online store tables are encrypted at rest using AWS-owned KMS keys by default.
- Data in transit: All interactions with Feature Store SDK communicate over TLS 1.2+.

### 6.4 Feature Drift Controls

Automated drift detection is configured for production feature groups with an expected value range or distribution documented in the Feature Spec. Drift detection runs daily comparing the previous day's published feature values against the documented baseline.

- **Statistical Distance Metric**: Population Stability Index (PSI) computed daily for each feature column within a Feature Group.
- **Alerting Threshold**: PSI > 0.25 triggers a P3 alert (ServiceNow incident). PSI > 0.40 triggers a P2 alert.
- **Response SLA**: Acknowledge P3 within 4 business hours; P2 within 2 business hours.
- **Retraining Trigger**: PSI sustained > 0.25 for 7 consecutive days triggers a model retraining evaluation per **SOP-AIML-006**.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Feature Store Operational Metrics

| Metric | Definition | Target | Alert Threshold |
|--------|------------|--------|-----------------|
| Online Store Latency p99 | 99th percentile latency for feature retrieval from DynamoDB | <50ms | >75ms for 15 min sustained |
| Online Store Availability | Percentage of successful feature retrieval requests (HTTP 200) | 99.95% monthly | <99.9% for rolling 60-min window |
| Offline Store Partition Completeness | Percentage of daily partitions successfully created by 09:00 UTC | 99.5% | <98% for 3 consecutive days |
| Feature Freshness | Time elapsed between source data availability and feature availability in online store | Varies per Feature Spec | Exceeding declared SLA for >1hr |
| Pipeline Failure Rate | Percentage of feature pipeline executions resulting in failure | <2% | >5% for rolling 7-day window |
| Feature Drift Incidence | Number of Feature Groups with active drift alerts (PSI > 0.25) | — | Individual alert per group |

### 7.2 Dashboards

Metric dashboards are available in Amazon CloudWatch:

- **Feature Store Operations Dashboard**: Online store latency, availability, and request volume per Feature Group.
- **Pipeline Health Dashboard**: Per-pipeline success/failure rates, execution durations, and data volume trends.
- **Feature Freshness Dashboard**: Per-Feature Group freshness lag relative to declared SLA.

Dashboards are linked from the Meridian ML Platform wiki homepage.

### 7.3 Weekly Review Cadence

The AI/ML Platform team conducts a weekly review every Monday at 10:00 AM Pacific of:

- All pipeline failures from the previous 7 days
- Any open drift alerts
- Upcoming feature deprecations
- Platform capacity trends (DynamoDB provisioned throughput utilization, S3 storage growth)

Review minutes are posted to the #ml-platform-weekly Slack channel.

### 7.4 Monthly Reporting

The Feature Store Platform Lead distributes a monthly Feature Store Operations Report to the AI/ML Engineering organization summarizing:

- Feature Store adoption metrics (total registered Feature Groups, new registrations, deprecations)
- SLA adherence (online store latency, offline partition completeness)
- Major incidents (P1/P2) and corrective actions
- Drift alert trends

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

The following situations require an approved exception:

| Exception Type | Example Scenario | Approval Required |
|----------------|------------------|-------------------|
| **Feature Store Bypass** | A model team requests to use features not registered in the Feature Store for a limited production run | Feature Store Platform Lead + Chief AI Officer |
| **Documentation Waiver** | A feature group is needed urgently and the full Feature Spec is delayed | Feature Reviewer + Platform Lead; must be resolved within 14 calendar days |
| **SLA Exception** | A feature group requires a freshness SLA not supported by current batch pipeline infrastructure (<15 min batch, but not streaming-eligible) | Platform Lead; architectural review required |
| **Retention Override** | Offline feature data must be retained longer than standard 400 days for regulatory reasons | Data Steward + Platform Lead |
| **Non-Standard Transformation** | A feature requires stateful or non-deterministic transformation | Feature Reviewer + Platform Lead + Chief AI Officer |

### 8.2 Exception Request Process

1. Feature Author or Team Lead submits an Exception Request using the form in the `meridian-ml/exceptions` repository (`exception_request_template.md`).
2. The request describes:
   - The exception type and scope
   - Justification (why standard procedure cannot be followed)
   - Mitigating controls proposed
   - Expiration date of the exception
3. Required approvers are assigned automatically via CODEOWNERS.
4. Approved exceptions are registered in the Exception Log (`meridian-ml/exceptions/exception-log.md`), tracked by expiration date.
5. Upon expiration, the Exception Owner (Feature Author) must either renew with updated justification or bring the feature into compliance.

### 8.3 Escalation Path

For issues not resolvable through standard exception handling:

| Level | Escalation Contact | When to Escalate |
|-------|-------------------|------------------|
| L1: Feature Author | Feature Reviewer | Pipeline failure unresolved after 1 business day of debugging |
| L2: Feature Reviewer | Feature Store Platform Lead | Platform-level issue (e.g., DynamoDB throttling, S3 access denied across multiple pipelines) |
| L3: Platform Lead | Chief AI Officer | Risk to model safety, regulatory concern, or significant SLA breach affecting production models |
| Emergency | AI/ML On-Call (PagerDuty rotation) | Online store outage or PHI exposure incident |

---

## 9. Training Requirements

### 9.1 Required Training

| Training Module | Audience | Frequency | Delivery Method |
|-----------------|----------|-----------|-----------------|
| SOP-AIML-005 Familiarization | All AI/ML Engineers, Data Scientists | Onboarding + annual refresher | Self-paced Confluence course + quiz (score ≥80% required) |
| Feature Store SDK Workshop | Feature Authors | Onboarding | 2-hour instructor-led hands-on lab |
| Data Leakage Prevention in Healthcare ML | All personnel developing features for Clinical AI Platform | Onboarding + annual | Online module with case studies |
| PHI/PII Feature Handling | Any personnel tagging features with PHI/PII classification | Onboarding + biennial | Compliance-led live training |
| HealthPay Feature Validation | HealthPay Model Validation Engineers | Onboarding + annual | Procedure walkthrough |

### 9.2 Training Tracking

Completion of training is tracked in the Meridian Learning Management System (LMS). Feature Authors who have not completed required training shall have their PR merge permissions temporarily suspended by the Platform Lead until training is completed.

### 9.3 SOP Familiarization Quiz

The annual SOP-AIML-005 refresher quiz covers:

- Feature Spec requirements
- Pipeline development standards
- Feature Store registration steps
- Data leakage prevention procedures

A minimum score of 80% is required. Two retake attempts are allowed before mandatory 1:1 remediation with the Feature Store Platform Lead.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|--------|-------|--------------|
| **SOP-AIML-001** | Machine Learning Development Lifecycle | Governs overall ML project phases; feature engineering is a sub-phase. |
| **SOP-AIML-003** | Model Training and Experiment Tracking | Consumes offline Feature Store; defines training data assembly procedures. |
| **SOP-AIML-004** | Model Deployment and Serving | Consumes online Feature Store; defines inference pipeline requirements. |
| **SOP-AIML-006** | Model Monitoring and Drift Response | References feature drift monitoring outputs; defines retraining decision framework. |
| **SOP-DATA-012** | Data Ingestion and ETL Operations | Defines upstream data pipeline standards that feed feature pipelines. |
| **SOP-DATA-014** | Data Retention and Archival | Governs retention of offline feature data. |
| **SOP-SEC-008** | Data Classification and Access Controls | Governs PHI/PII tagging and IAM policy alignment. |
| **SOP-COMP-003** | Model Inventory and Regulatory Documentation | References HealthPay Model Inventory and validation documentation. |

### 10.2 External References

| Reference | Version | Applicability |
|-----------|---------|---------------|
| AWS SageMaker Feature Store Developer Guide | Latest | Meridian Feature Store is built on SageMaker Feature Store |
| Feathr Documentation (Open Source) | v0.8+ | Base SDK used by Meridian Feature Engineering SDK |
| TensorFlow Data Validation (TFDV) Guide | v1.10+ | Used for schema validation in CI pipeline |
| Apache Parquet Specification | 2.0+ | Offline store data format |

---

## 11. Revision History

| Version | Date | Author | Description of Changes | Approver |
|---------|------|--------|------------------------|----------|
| 1.0 | 2023-05-15 | Dr. Marcus Rivera | Initial release. Established Feature Store mandate, pipeline standards, and data leakage prevention procedures. | David Park |
| 1.1 | 2023-11-02 | Sophia Chen | Added online store TTL configuration requirements (Section 5.4.2). Updated Feature Store CLI commands. Added drift detection thresholds. | David Park |
| 1.2 | 2024-03-18 | Sophia Chen | Updated Feature Spec template to include Section E (Quality Expectations). Incorporated HealthPay validation procedures per regulatory feedback. | David Park |
| 1.3 | 2024-08-07 | Dr. Marcus Rivera | Added feature deprecation lifecycle (Section 5.7). Updated exception handling process. Refined RACI matrix. Added streaming feature support details. | David Park |
| 1.4 | 2025-03-26 | Dr. Marcus Rivera | Major revision. Restructured pipeline CI/CD stages. Added `pt_validation.py` mandatory scripts. Updated Data Steward review requirements for PHI/PII. Standardized Feature Spec naming convention. Updated training requirements with LMS tracking integration. | David Park |

---

**END OF DOCUMENT**

*© 2025 Meridian Health Technologies, Inc. All rights reserved. This document is classified as Internal. Distribution outside authorized business units requires approval from the document owner.*