---
sop_id: "SOP-PENG-004"
title: "Software Quality Assurance"
business_unit: "Product & Engineering"
version: "3.4"
effective_date: "2025-02-23"
last_reviewed: "2026-02-18"
next_review: "2026-08-24"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Software Quality Assurance

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide Software Quality Assurance (QA) framework for Meridian Health Technologies, Inc. The purpose of this document is to define the standardized processes, methodologies, roles, responsibilities, and controls necessary to ensure that all software products, platforms, and services developed, deployed, or maintained by Meridian meet defined quality standards, functional requirements, non-functional requirements, and regulatory obligations. This SOP provides a unified approach to quality governance across all business units, ensuring patient safety, data integrity, and financial accuracy in our AI-powered healthcare fintech ecosystem.

### 1.2 Scope

This SOP applies to all software development, configuration, integration, and maintenance activities across all Meridian business lines and supporting functions:

| Business Unit | Products in Scope | Key Quality Considerations |
|---|---|---|
| Clinical AI Platform | Clinical decision support tools, diagnostic imaging analysis, patient risk scoring, adverse event prediction | Patient safety, model accuracy, EU AI Act Annex III compliance, FDA 510(k) requirements, CE marking under EU MDR |
| HealthPay Financial Services | Payment processing, patient financing, medical lending, claims automation | Financial accuracy, transaction integrity, SR 11-7 model risk management |
| MedInsight Analytics | Population health analytics, care gap identification, outcomes prediction | PHI data quality, analytical accuracy, HIPAA compliance |
| Meridian SaaS Platform | Multi-tenant cloud infrastructure, shared services, APIs, data pipelines | Platform reliability, security, performance, SOC 2 requirements |

This SOP covers the full software development lifecycle (SDLC) including requirements analysis, design, development, testing, release, and post-deployment monitoring. It applies to:

- All permanent employees, contractors, and third-party vendors engaged in software development or QA activities
- All environments (development, staging, pre-production, production) in AWS (us-east-1, eu-west-1) and Azure DR
- All software change types: new features, enhancements, bug fixes, patches, configuration changes, and emergency hotfixes
- All deployment types: cloud service updates, model updates, infrastructure-as-code changes, database schema modifications

### 1.3 Out of Scope

- Hardware quality assurance for on-premises medical devices (see SOP-MFG-001)
- Clinical validation of AI model efficacy (see SOP-CLNAI-007, Clinical AI Validation)
- Financial audit procedures (see SOP-FIN-012)
- Third-party vendor due diligence (see SOP-VEND-003)

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| Acceptance Criteria | Specific, measurable conditions that must be satisfied for a user story, feature, or requirement to be considered complete and acceptable to stakeholders. |
| Bug | A discrepancy between the actual behavior of the software and its specified or expected behavior, resulting from a coding error, design flaw, or configuration issue. |
| Code Coverage | A metric measuring the percentage of source code lines, branches, conditions, or paths exercised by automated test suites during execution. |
| Continuous Integration / Continuous Deployment (CI/CD) | A DevOps practice where code changes are automatically built, tested, and prepared for release to production through a defined pipeline. |
| Defect | A broader term encompassing bugs, design deficiencies, documentation errors, and any non-conformance to requirements or quality standards. |
| Deferred Defect | A known defect that has been formally reviewed and intentionally deferred for resolution to a future release based on risk assessment and business priority. |
| Feature Flag | A configuration-driven mechanism enabling runtime toggling of functionality without deploying new code, used for canary releases, A/B testing, and operational control. |
| Hotfix | An emergency software change deployed outside the normal release cadence to resolve a critical production issue, often bypassing standard QA procedures. |
| Non-Functional Requirement (NFR) | System quality attributes including performance, security, reliability, scalability, usability, and maintainability. |
| Regression Testing | Testing performed to verify that previously developed and tested software functionality continues to work correctly after code changes, additions, or modifications. |
| Release Candidate (RC) | A software build that has passed all required QA activities and is deemed potentially suitable for production deployment, pending final approval. |
| Severity | A classification of the impact a defect has on system operation, patient safety, financial integrity, or business operations. |
| Shift-Left Testing | The practice of moving testing activities earlier in the SDLC to identify defects sooner, reducing the cost and risk of late-stage discovery. |
| Smoke Testing | A preliminary set of tests executed on a new build to verify that critical core functionality is operational before proceeding with more extensive testing. |
| Test Case | A detailed specification of preconditions, inputs, actions, expected results, and postconditions used to verify a specific aspect of software behavior. |
| Test Suite | A collection of test cases organized by feature area, functionality, or test type, designed to be executed together. |

### 2.2 Acronyms

| Acronym | Expansion |
|---|---|
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| AWS | Amazon Web Services |
| BDD | Behavior-Driven Development |
| CI/CD | Continuous Integration / Continuous Deployment |
| CISO | Chief Information Security Officer |
| CPO | Chief Privacy Officer |
| DAST | Dynamic Application Security Testing |
| DPO | Data Protection Officer |
| EHR | Electronic Health Record |
| E2E | End-to-End Testing |
| FDA | U.S. Food and Drug Administration |
| FHIR | Fast Healthcare Interoperability Resources |
| FMEA | Failure Mode and Effects Analysis |
| GDPR | General Data Protection Regulation |
| HIPAA | Health Insurance Portability and Accountability Act |
| IaC | Infrastructure as Code |
| KPI | Key Performance Indicator |
| MAE | Mean Absolute Error |
| ML | Machine Learning |
| MLOps | Machine Learning Operations |
| MTTR | Mean Time to Resolve |
| NFR | Non-Functional Requirement |
| NIST | National Institute of Standards and Technology |
| PHI | Protected Health Information |
| QA | Quality Assurance |
| RAG | Regression Automation Grade |
| RC | Release Candidate |
| RMSE | Root Mean Square Error |
| SAST | Static Application Security Testing |
| SDLC | Software Development Lifecycle |
| SLA | Service Level Agreement |
| SLO | Service Level Objective |
| SME | Subject Matter Expert |
| SQA | Software Quality Assurance |
| TDD | Test-Driven Development |
| UI | User Interface |
| UAT | User Acceptance Testing |
| WCAG | Web Content Accessibility Guidelines |

## 3. Roles and Responsibilities

The following RACI matrix (Responsible, Accountable, Consulted, Informed) defines the quality-related roles and responsibilities for all personnel involved in the SDLC.

### 3.1 Responsibility Assignment Matrix

| Activity / Decision | Product & Engineering (Dev, QA, MLOps) | VP of Engineering | Product Management | CISO / Security | Clinical SMEs | Business Unit Owners | CEO |
|---|---|---|---|---|---|---|---|
| Writing and executing unit tests | R | I | C | I | I | I | I |
| Writing integration and E2E tests | R | A | C | C | C | I | I |
| Defining acceptance criteria | C | I | R / A | C | C | C | I |
| Executing manual QA testing | R | A | C | I | C | I | I |
| Approving release candidates (standard) | R | A | C | C | C | C | I |
| Approving emergency hotfix releases | R | A | C | I | I | C | I |
| Clinical AI validation (SOP-CLNAI-007) | C | A | C | I | R | I | I |
| Security-focused QA activities (SAST, DAST) | C | A | I | R | I | C | I |
| Defining and tracking QA KPIs | R | A | C | C | I | C | I |
| Granting exceptions to QA policy | C | R / A | C | C | C | C | I |
| Final product release authorization | I | A | R | C | C | C | I |

**Note**: "R" for Responsible indicates the party performing the work. For clarity, Developers are Responsible for unit tests; QA Engineers are Responsible for integration and E2E tests.

### 3.2 Detailed Role Descriptions

**3.2.1 Chief Executive Officer (CEO)**
- Ultimate accountability for product quality and patient safety
- Approves all major version updates to this SOP
- Receives quarterly quality reports and is informed of critical (Sev-1) production defects within 4 hours via the escalation path

**3.2.2 VP of Engineering (David Park)**
- Owner of this SOP and accountable for the QA program across all business units
- Approves release candidates based on QA sign-off and business readiness
- Authorizes hotfix deployments bypassing standard QA gates
- Reviews and approves all QA policy exceptions
- Chairs the monthly Quality Review Board meeting (see Monitoring, Metrics, and Reporting)

**3.2.3 Product Management**
- Responsible for defining clear, testable acceptance criteria for all features
- Accountable for prioritizing the product backlog, balancing feature work with technical debt and defect remediation
- Consults on severity classification of defects
- Participates in User Acceptance Testing (UAT) for patient-facing and provider-facing features
- Informed of all release candidate QA metrics before approving customer-facing rollout

**3.2.4 Quality Assurance Engineers (Product & Engineering)**
- Design, implement, and execute test suites across all testing levels
- Maintain the automated test framework, CI/CD pipeline integrations, and test data management
- Execute manual exploratory testing, regression testing, and UAT coordination
- Triage, classify, and document all discovered defects in Jira
- Generate per-release QA metric reports and dashboards
- Conduct shift-left testing practices, participating in sprint planning and design reviews

**3.2.5 Developers (Product & Engineering)**
- Write and execute unit tests achieving minimum code coverage thresholds
- Fix defects identified by QA and production monitoring
- Participate in code reviews, static analysis reviews, and peer testing
- Implement feature flags, logging, and monitoring hooks to support production quality observability

**3.2.6 MLOps Engineers (Product & Engineering)**
- Responsible for ML-specific QA: model performance on holdout sets, data drift detection, feature validation, shadow deployment testing
- Define and monitor ML-specific quality KPIs (RMSE, MAE, precision/recall for classifiers, data quality scores)
- Maintain model versioning and A/B testing infrastructure
- Execute FMEA analysis on AI-driven clinical decision support workflows prior to release

**3.2.7 Chief Information Security Officer (CISO)**
- Consulted on all security-related QA activities
- Responsible for defining security testing requirements and acceptable risk thresholds
- Receives SAST/DAST scan results and approves deployment where security findings are within risk tolerance
- Informed of all Sev-1 and Sev-2 security defects within 24 hours

**3.2.8 Clinical Subject Matter Experts (SMEs)**
- Consulted on clinical workflows, medical terminology accuracy, and patient safety aspects of QA testing
- Participate in clinical scenario testing for CDS products
- Review model fairness and bias testing results
- Co-author clinical validation test scripts

**3.2.9 Business Unit Owners**
- Consulted on business-critical functionality prioritization
- Informed of release QA status, known deferred defects, and risk assessments
- Participate in Go/No-Go decisions for major releases affecting their business lines

## 4. Policy Statements

### 4.1 Quality Governance

4.1.1 All software releases must pass defined QA gates prior to production deployment. No release may proceed without documented QA sign-off per the release criteria defined in Section 5.

4.1.2 Quality is a shared responsibility across all members of Product & Engineering. Every engineer, regardless of title, is expected to contribute to the quality of the products they build, test, and deploy.

4.1.3 The VP of Engineering, or their designated delegate, holds the final authority for release authorization based on a holistic assessment of QA metrics, open defects, risk posture, and business readiness.

### 4.2 QA Strategy and Approach

4.2.1 Meridian employs a risk-based, layered QA strategy incorporating the following testing levels:

| Testing Level | Primary Responsibility | Automation Expectation |
|---|---|---|
| Unit Testing | Developers | 100% automated; executed on every commit |
| Integration Testing | Developers / QA | ≥ 90% automated via CI/CD pipeline |
| System / E2E Testing | QA Engineers | ≥ 70% automated for critical paths |
| User Acceptance Testing (UAT) | Product Management, Clinical SMEs | Manual with structured scripts |
| Exploratory Testing | QA Engineers | Manual; risk-focused per release |

4.2.2 All AI/ML models deployed to production shall undergo:
- Performance evaluation against held-out test datasets
- Bias and fairness assessment (see SOP-CLNAI-008, Responsible AI)
- Shadow deployment or A/B testing for a minimum period defined in the release plan (not less than 7 calendar days for models used in clinical decision support)

4.2.3 Production emergency hotfixes may bypass standard QA gates ONLY upon documented authorization of the VP of Engineering and with mandatory post-deployment validation executed within 24 hours.

### 4.3 Test Coverage Requirements

| Code Type | Line Coverage Floor | Branch Coverage Floor |
|---|---|---|
| New business logic (Go, Java, TypeScript services) | 85% | 80% |
| New UI components (React) | 80% | 75% |
| Infrastructure-as-Code (Terraform, CloudFormation) | 90% (validation tests) | N/A |
| Data pipeline transformations | 90% | 85% |
| Critical path clinical/financial code | 95% | 90% |
| Legacy code under maintenance | No regression — improve by minimum 5% per release | Same |

Coverage thresholds are enforced via CI/CD pipeline gates. Builds that fall below the floor will fail.

### 4.4 Defect Management

4.4.1 All defects identified in production or pre-production shall be logged in Jira with at minimum: description, reproduction steps, severity classification, affected component, environment, and assigned owner.

4.4.2 Severity Classification:

| Severity | Definition | Response SLA | Examples |
|---|---|---|---|
| Sev-1 — Critical | System unavailable, patient safety risk, financial integrity compromised, PHI breach | Acknowledge ≤ 15 min; Initiate resolution ≤ 1 hr; Resolve ≤ 24 hrs (continuous effort) | Production outage; incorrect drug dosage calculation; payment processing failure; unencrypted PHI in logs |
| Sev-2 — High | Major feature broken; core workflow disrupted with viable workaround; non-critical data loss | Acknowledge ≤ 1 hr; Resolve ≤ 3 business days | Patient data incorrectly formatted but EHR integration still functions; reporting dashboard 50% broken |
| Sev-3 — Medium | Non-critical feature impaired; cosmetic issues on branded surfaces; performance degradation not violating SLOs | Resolve per sprint prioritization — recommended within 14 calendar days | UI misalignment in admin panel; slow loading on rarely used report |
| Sev-4 — Low | Minor cosmetic issues; typos not affecting clinical understanding; suggestions for improvement | Backlog prioritization | Misleading tooltip; inconsistent button styling |

4.4.3 Known defects deferred from the current release must be:
- Documented in the release notes
- Reviewed by the VP of Engineering or delegate
- Communicated to affected business unit owners
- Scheduled for resolution in a specific future release (no indefinite deferrals)

### 4.5 Quality in AI/ML Systems

Given Meridian's identity as an AI-powered healthcare platform, additional specific quality requirements apply to ML systems:
- Model reproducibility: every deployed model must be reproducible from version-controlled datasets, training code, and hyperparameters
- Concept drift monitoring: all models serving predictions in production must have defined drift monitoring and alerting thresholds
- Shadow evaluation: significant model version upgrades shall undergo shadow mode evaluation against live traffic before serving predictions

## 5. Detailed Procedures

### 5.1 QA Planning and Requirements Analysis

**5.1.1 Sprint Zero and Release Kickoff**

At the commencement of each new development initiative (new product, major feature set, or architectural refactor), the following planning activities must be completed:

| Activity | Owner | Deliverable | Timeline |
|---|---|---|---|
| Quality Risk Assessment | QA Lead + Product Manager | Risk matrix identifying high-risk areas requiring intensified testing | Within 5 business days of initiative kickoff |
| Test Strategy Document | QA Lead | Tailored testing strategy covering scope, environments, data requirements, tools, and schedule | Within 10 business days of initiative kickoff |
| Test Environment Specification | DevOps / MLOps Engineer | Environment topology, dataset requirements, integration touchpoints | Within 10 business days of initiative kickoff |
| NFR Baseline Definition | QA Lead + Architecture | Specific, measurable NFR targets (latency, throughput, uptime) | Within 10 business days of initiative kickoff |

**5.1.2 User Story Refinement — Definition of Ready**

A user story is considered "Ready for Development" only when it meets the Definition of Ready (DoR):
- [ ] Story is sized appropriately (fits within one sprint)
- [ ] Acceptance Criteria are defined, specific, and testable
- [ ] Non-functional requirements applicable to the story are specified
- [ ] Dependencies are identified and resolved
- [ ] UI/UX mockups are attached (for UI features)
- [ ] API contracts are defined (for API/integration features)
- [ ] Performance/security/compliance considerations are documented
- [ ] Clinical/regulatory SMEs have reviewed (for clinical features)

**5.1.3 Test Case Design**

For each user story or feature, QA Engineers shall design test cases covering:

- **Positive Path**: Verify the feature works as intended under normal, expected conditions
- **Negative Path**: Verify graceful handling of invalid inputs, error conditions, and edge cases
- **Boundary Conditions**: Test limits on input fields, pagination, data volumes, concurrency
- **Integration Touchpoints**: Verify interactions with dependent services, databases, and external APIs
- **Security Considerations**: Verify authentication, authorization, input sanitization (per security test cases coordinated with CISO team)
- **Accessibility**: Verify WCAG 2.1 AA compliance for patient-facing and provider-facing UI

Test cases shall be written using Behavior-Driven Development (BDD) Gherkin syntax where appropriate:

```
Feature: Patient Risk Score Calculation

  Scenario: Calculate risk score with complete patient data
    Given a patient record exists with vital signs recorded within 24 hours
    And the patient has at least 3 lab results within the reference range
    When the "Calculate Risk Score" service is invoked with the patient ID
    Then the service returns a risk score between 0.00 and 1.00
    And the response includes a confidence interval
    And the calculation metadata includes the model version used

  Scenario: Handle missing vital signs gracefully
    Given a patient record exists with no vital signs recorded within 72 hours
    When the "Calculate Risk Score" service is invoked with the patient ID
    Then the service returns a risk score of -1.0 indicating "insufficient data"
    And the response includes an error code "DATA_GAP_VITALS"
    And an event is logged to the data quality monitoring pipeline
```

Test cases shall be stored in the Test Management module of Jira (Xray plugin) and linked to their corresponding requirements/user stories.

### 5.2 Shift-Left Testing — Developer Phase

**5.2.1 Unit Testing**

All developers are required to write and maintain unit tests for their code. Unit tests must:

1. Be executable via the standard build tool for the language (e.g., `go test`, `pytest`, `jest`)
2. Mock all external dependencies (databases, APIs, file systems)
3. Execute in the CI pipeline on every commit to a feature branch
4. Pass 100% before a Pull Request (PR) can be merged

**CI Pipeline Gate for Unit Tests:**

Pipeline Stage: `unit-tests`
```yaml
# Example pipeline configuration (GitHub Actions / Jenkins / GitLab CI)
unit-test-job:
  runs-on: meridian-standard-runner
  steps:
    - checkout
    - run: make unit-tests
    - publish: test-results.xml, coverage-report.xml
  gates:
    - test-pass-rate: 100%
    - line-coverage-floor: as per Section 4.3
    - branch-coverage-floor: as per Section 4.3
    - coverage-decline-check: no file decreased > 2% from baseline
  on-failure: BLOCK_MERGE, NOTIFY_DEVELOPER
```

**5.2.2 Static Code Analysis**

All code commits must pass static analysis scans in the CI pipeline. Meridian uses SonarQube (on-premises instance at `sonarqube.internal.meridian.com`) for code quality analysis.

Quality Gate thresholds:
- No Critical or Blocker code smells introduced
- No duplicated lines density > 3% on new code
- Maintainability Rating not worse than A
- No security vulnerabilities of severity High or above (using bundled FindBugs/ESLint security rules — **note**: this does not substitute for dedicated security scanning)

**5.2.3 Code Review**

All code changes must undergo peer review before merge:

1. Developer creates Pull Request (PR) in Bitbucket
2. PR template includes checklist:
   - [ ] Unit tests included and passing
   - [ ] Acceptance criteria met (evidence in PR description)
   - [ ] SonarQube quality gate passed
   - [ ] No hardcoded secrets, credentials, or API keys
   - [ ] Logging added appropriately (no PHI in logs)
   - [ ] Feature flagged if applicable
3. Minimum one approving review from a peer developer
4. For clinical or financial code paths: additional mandatory review from a designated SME reviewer
5. QA Engineer reviews PRs for testability concerns on a sampling basis (minimum 20% of PRs per sprint reviewed by QA)

### 5.3 Integration and System Testing — QA Phase

Once a feature branch is merged to the `develop` integration branch, the QA phase begins.

**5.3.1 Integration Test Execution**

Integration tests are executed automatically via the CI/CD pipeline upon merge to `develop` and nightly against the latest `develop` build.

Integration test suites are organized by:

- **Service Domain**: e.g., `patient-service-integration`, `payment-gateway-integration`
- **Cross-Cutting Concerns**: `auth-integration`, `logging-integration`, `audit-integration`

Pipeline stage: `integration-tests`
- Execute all integration test suites
- Pass rate must be 100%; failures block promotion to staging environment
- Duration target: ≤ 30 minutes total execution time

**5.3.2 Staging Environment Deployment and Smoke Testing**

Upon successful integration tests, the build is deployed to the `staging` environment in AWS us-east-1.

Automated smoke tests are executed immediately:

| Smoke Test | Description | Failure Action |
|---|---|---|
| Health Check API | Verify all core services respond to `/health` endpoint with 200 OK within 5 seconds | Block release; page DevOps |
| Authentication Flow | Log in with a test user; obtain valid JWT token | Block release; page DevOps |
| Core API Roundtrip | Create a test patient → retrieve patient → update patient → verify FHIR resource integrity | Block release; page QA Lead |
| Database Connectivity | Verify read/write to primary Aurora cluster | Block release; page DevOps and DBA |
| Message Bus | Publish a test event; verify consumption by subscription service | Block release; page DevOps |

**5.3.3 Manual QA — Structured Exploratory Testing**

Upon passing smoke tests, QA Engineers conduct structured exploratory testing on the `staging` environment. This is not random clicking; it is a session-based, risk-focused testing activity.

**Session-Based Test Management:**

Each exploratory testing session is time-boxed and documented:

- **Session Duration**: 90 minutes (standard session)
- **Charter**: A concise mission statement for the session, e.g., "Explore the new medication reconciliation workflow focusing on drug-drug interaction alerts with incomplete patient medication history"
- **Coverage Areas**: Specific features, integrations, data scenarios, edge cases identified in QA planning
- **Output**: Session report in Jira containing:
  - Features exercised
  - Data scenarios tested
  - Defects discovered (linked as Jira bugs)
  - Observations and risk notes
  - Time spent breakdown (test execution vs. defect investigation vs. environment issues)

**Regression Test Selection:**

For each release, the QA Lead selects a regression test suite based on:

1. **Change-based**: All test cases linked to modified code modules (identified via Jira traceability and code diff analysis)
2. **Risk-based**: Critical path test cases for patient safety and financial integrity are ALWAYS executed for every release
3. **Automated Regression**: The automated regression suite (Selenium/Cypress for UI, custom Python/Go scripts for API) runs nightly against `staging`

### 5.4 AI/ML Specific QA Procedures

Machine learning model quality assurance requires procedures beyond traditional software testing.

**5.4.1 Offline Model Evaluation**

Before an ML model candidate is promoted to staging for integration testing, it must pass offline evaluation:

| Metric | Threshold (Example: Patient Readmission Risk Model) | Enforcement |
|---|---|---|
| AUC-ROC on holdout test set | ≥ 0.85 | Gate; Fail = reject candidate |
| Precision at recall 0.80 | ≥ 0.65 | Gate; Fail = reject candidate |
| Fairness parity (Demographic Parity Difference) across race | ≤ 0.05 | Gate; Fail = flagged for review; SME override required |
| Calibration error (Expected Calibration Error) | ≤ 0.03 | Warning; Fail = documented risk accepted by Product |
| Prediction latency at p99 | ≤ 500ms | Gate; Fail = architecture review |

**5.4.2 Shadow Deployment Testing**

All major model version upgrades shall undergo shadow deployment. In shadow mode:

1. The new model version receives a copy of live production inference requests
2. Predictions are generated but NOT returned to users
3. Predictions are logged alongside the production model's predictions
4. Logs are analyzed daily by MLOps for a minimum of 7 calendar days for non-clinical models and 14 calendar days for clinical models
5. Discrepancy analysis: any prediction where the shadow model's output differs from the production model by > 10% (for continuous outputs) or category differs (for classifiers) is flagged for SME review

**5.5 User Acceptance Testing (UAT)**

UAT is performed on the `staging` environment.

**5.5.1 UAT Planning**

For each major or minor release, Product Management shall prepare a UAT plan containing:
- Specific workflows and scenarios to be tested by end-user representatives
- Data setup requirements (test patient records, synthetic claims data)
- Go/No-Go criteria for UAT sign-off
- Schedule: UAT window is minimum of 5 business days for major releases, 3 business days for minor releases

**5.5.2 UAT Execution**

UAT participants execute the scripted scenarios and are encouraged to perform ad-hoc workflows typical of their daily roles.

Defects found during UAT are logged in Jira with a `UAT` label and triaged by QA and Product Management:
- Sev-1 or Sev-2 UAT defects: release is blocked until resolved or VP of Engineering grants a formal risk-acceptance exception
- Sev-3 UAT defects: Product Management decides to fix or defer with documented rationale
- Sev-4 UAT defects: logged, triaged in next sprint planning

**5.5.3 UAT Sign-off**

Formal UAT sign-off requires documented approval from:
- Product Manager for the feature area
- At least one Clinical SME (for clinical features)
- Business Unit Owner (for business workflow features)

### 5.6 Release Procedures

**5.6.1 Release Candidate Validation**

A Release Candidate (RC) is a specific build artifact (container image tag, Lambda version, etc.) that has passed all QA gates and is proposed for production deployment.

**Release Candidate Validation Checklist:**

The QA Lead is responsible for generating the Release Validation Report containing this checklist prior to the Go/No-Go meeting:

| Gate | Status | Evidence |
|---|---|---|
| All unit tests passing on RC build | PASS / FAIL | CI job link |
| All integration tests passing against RC on staging | PASS / FAIL | CI job link |
| Automated regression suite pass rate ≥ 99.5% | PASS / FAIL | Test suite execution report |
| All Sev-1 and Sev-2 defects resolved or formally deferred with risk acceptance | RESOLVED / OPEN (list) | Jira query link |
| UAT Sign-off obtained (for releases with UAT requirement) | SIGNED / PENDING | UAT sign-off document |
| SonarQube Quality Gate passed (no Critical/Blocker issues) | PASS / FAIL | SonarQube project dashboard link |
| Infrastructure as Code validation tests passed | PASS / FAIL | CI job link |
| Database migration tested successfully against staging schema | PASS / FAIL | Migration test log |
| Feature flags configuration reviewed and correct | CONFIRMED | Feature flag audit report |
| Rollback procedure documented and tested | CONFIRMED | Rollback runbook link |
| Release notes prepared and reviewed | CONFIRMED | Release notes draft |

**5.6.2 Go/No-Go Decision**

The Go/No-Go meeting is chaired by the VP of Engineering or their delegate. Required attendees:

- VP of Engineering or Release Manager (Chair)
- QA Lead
- Product Manager
- Engineering Lead / Tech Lead
- MLOps representative (if ML changes included)
- Security representative (optional, required if security-impacting changes)

The QA Lead presents the Release Validation Report. The Chair facilitates the decision:

- **GO**: All mandatory gates are PASS. Release proceeds per deployment runbook.
- **CONDITIONAL GO**: All mandatory gates PASS, but one or more non-mandatory gates have issues. Chair authorizes release with documented conditions and post-deployment action items.
- **NO-GO**: One or more mandatory gates FAIL. Release is deferred. Root cause analysis for the failure is initiated.

**5.6.3 Production Deployment**

Upon GO decision, deployment to production follows the deployment runbook specific to the service. General principles:

1. **Phased Rollout**: Deploy to a limited subset of production instances/servers initially (canary deployment)
2. **Canary Monitoring**: Monitor canary instances for error rates, latency, and business metrics for a minimum observation period specified in the deployment runbook (typically 1 hour for standard changes)
3. **Full Rollout**: Upon successful canary monitoring, proceed to full deployment
4. **Feature Flag Activation**: If features are behind feature flags, activate per agreed rollout plan
5. **Post-Deployment Smoke Tests**: Immediately execute the automated production smoke test suite

### 5.7 Post-Deployment Monitoring and Production QA

Post-deployment monitoring is a critical QA function, providing real-world validation that the software behaves correctly under genuine production load and data.

**5.7.1 Production Monitoring Dashboards**

Within 30 minutes of production deployment, the QA Lead and responsible Engineering Lead shall jointly review the following dashboards:

| Dashboard | Tool | Metrics Reviewed |
|---|---|---|
| Application Error Rates | Datadog | 5xx error rate vs. pre-deployment baseline; spike detection |
| Service Latency | Datadog | p50, p95, p99 latency vs. SLOs; increase vs. baseline |
| Business Metrics | Custom (Grafana) | Successful patient record updates, payment transactions processed, API calls served — verify expected throughput |
| ML Model Performance | Evidently AI | Prediction distribution shift; feature drift detection |

**5.7.2 Production Defect Handling**

Defects identified in production follow the same classification and logging process (Section 4.4). Additionally:

- **Sev-1 Defect**: Immediately initiate incident response per SOP-INC-001 (Incident Management). VP of Engineering is paged. Executive communication initiated. QA Lead participates in post-incident review.
- **Sev-2 Defect**: QA Lead opens a critical bug ticket and assigns to the appropriate engineering team within 1 hour. VP of Engineering informed.
- **Sev-3 / Sev-4 Defects**: Logged as standard bugs and prioritized in backlog refinement.

### 5.8 Defect Management Lifecycle

The standard defect lifecycle from discovery to closure:

1. **Discovery & Logging**: Defect discovered (testing, UAT, production monitoring) → logged in Jira with details per Section 4.4.1
2. **Triage**: QA Lead reviews defect within the SLA window corresponding to its severity. Triage actions:
   - Confirm severity classification
   - Attempt reproduction on `staging` or appropriate environment
   - Link to relevant requirement/user story
   - Assign to the responsible engineering team
3. **Investigation & Root Cause**: Developer investigates. Root cause documented in Jira ticket.
4. **Fix & Unit Test**: Developer implements fix in a feature branch. Unit tests (including a regression test specifically for the defect) are added and pass.
5. **Code Review & Merge**: PR reviewed per Section 5.2.3. Merged to integration branch.
6. **QA Verification**: QA Engineer verifies the fix on the `staging` environment:
   - Reproduce the original defect scenario → defect does NOT occur
   - Execute regression test suite around the affected area → no new defects
   - Verify acceptance criteria for the fix
7. **Closure**: QA Engineer closes the defect ticket in Jira with verification evidence (test run link, screenshots).

**5.8.1 Defect Triage Meetings**

Weekly Defect Triage meetings are held:
- **Attendees**: QA Lead, Engineering Managers, Product Managers
- **Agenda**:
  - Review new un-triaged defects
  - Review aged defects (> 30 days open for Sev-3; > 90 days for Sev-4)
  - Re-classify misclassified defects
  - Identify clustering patterns indicating deeper quality issues

### 5.9 Test Data Management

QA testing requires realistic, safe, and version-controlled test data.

**5.9.1 Synthetic Data Generation**

Meridian uses the Synthea synthetic patient data generation tool to create test datasets. All synthetic data must be:
- Clearly marked as synthetic in metadata
- Free of real patient identifiers (verified via automated PHI scan before import to `staging` environment)
- Representative of production data distributions (demographics, clinical conditions, lab values)

**5.9.2 Production Data for Testing (Prohibited)**

Use of live production data, including de-identified production data without explicit DPO and CISO approval, in non-production environments is **strictly prohibited**. Any approved use of production-derived data must follow the Data Classification and Handling policy (SOP-INFOSEC-005) and be explicitly documented with an expiration date.

**5.9.3 Test Data Management Repository**

QA maintains a Git repository (`meridian-qa-testdata`) of test data fixtures, SQL seed scripts, API mock recording files, and synthetic patient bundles versioned alongside the code they test.

## 6. Controls and Safeguards

### 6.1 CI/CD Pipeline Gates

All code paths to production must transit through the defined CI/CD pipeline with automated enforcement gates. The pipeline is the primary technical control ensuring QA policy adherence.

The canonical Meridian CI/CD pipeline stages and gates are:

```
Stage 1: Source Code Commit (Developer Workstation)
    └── Pre-commit hooks: lint, secrets scanning (Talisman)

Stage 2: Feature Branch CI
    └── GATE: Unit tests pass (≥ floors)
    └── GATE: SonarQube quality gate pass
    └── GATE: One peer review approval

Stage 3: Integration Branch ("develop") CI
    └── GATE: Integration tests pass (100%)
    └── GATE: Build / container image vulnerability scan (Trivy — criticals block)

Stage 4: Staging Deployment
    └── GATE: Smoke tests pass on staging
    └── GATE: (Manual) UAT sign-off for applicable releases
    └── GATE: (Manual) Go/No-Go approval per Section 5.6.2

Stage 5: Production Canary Deployment
    └── GATE: Canary monitoring metrics within SLO for observation period
    └── GATE: (Manual) Canary sign-off by Release Manager

Stage 6: Full Production Deployment
    └── GATE: Post-deployment smoke tests pass
```

### 6.2 Feature Flag Governance

Feature flags serve as a runtime safety control, enabling rapid isolation of problematic code without requiring a full deployment rollback.

- **Flag Naming Convention**: `feature.{service}.{functionality-description}`
- **Mandatory Flags**: All new high-risk features (clinical calculation changes, payment processing logic changes, new data pipeline destinations) MUST be deployed behind a feature flag
- **Flag Ownership**: Each flag has a clear owner defined in the `feature-flags.yaml` configuration file
- **Circuit Breaker**: Mission-critical service-to-service calls SHALL implement circuit breaker patterns (via Istio/Envoy or application-level resilience libraries like `resilience4j`)
- **Flag Retirement**: Feature flags must be removed from code within 2 sprints of full rollout confirmation unless there is a documented operational reason for persistence

### 6.3 Environment Segregation

Strict environment segregation is a foundational control preventing accidental production impact from development/testing activities.

| Environment | Purpose | Access Control | Data Classification |
|---|---|---|---|
| `dev` | Developer sandbox; unit/integration test execution | Developer team full access | Synthetic only; NO PHI |
| `staging` | QA, UAT, performance testing | QA + Developers + SMEs read/write; deployment via CI only | Synthetic with approved production-derived de-identified data; NO PHI without CPO waiver |
| `pre-prod` (optional, as needed) | Final validation mirror of production config | Deployment via CI only; read access for QA/SMEs | Synthetic / de-identified |
| `prod` (us-east-1) | Primary production | Break-glass access for on-call; no direct developer write access | PHI (HIPAA-governed) |
| `prod-dr` (eu-west-1 Azure) | Disaster recovery | Break-glass access | PHI |

**Access Control Enforcement**:
- Production AWS accounts are isolated from non-production accounts in separate AWS Organizations
- CI/CD pipeline service accounts have least-privilege deployment roles per environment
- Developer IAM users have no `prod` write/update access by default; temporary elevated access requires a Just-in-Time Access request (via Teleport) with VP of Engineering approval

### 6.4 Test Artifact Integrity

- All test results from CI/CD pipeline stages shall be digitally signed with the pipeline's GPG key
- QA release validation reports are stored in the immutable release archive (`s3://meridian-release-artifacts/releases/{version}/qa-report-{date}.pdf`)
- Test data fixtures shall follow the same code review and version control policies as production code

## 7. Monitoring, Metrics, and Reporting

### 7.1 Quality KPIs and Dashboards

The QA program is measured and managed via a defined set of Key Performance Indicators (KPIs), visualized on a centralized Grafana dashboard (`QA Executive Dashboard`) and reviewed regularly.

| KPI | Definition | Target | Measurement Tool |
|---|---|---|---|
| **Release Stability Index** | Percentage of releases NOT requiring a hotfix within 7 calendar days of deployment | ≥ 95% | Jira + CI/CD deployment logs |
| **Defect Escape Rate** | Sev-1 and Sev-2 defects discovered in production, expressed as count per release | ≤ 1 Sev-1/2 per 4 releases | Jira (defect tickets with `environment=prod`) |
| **Regression Automation Coverage** | Percentage of critical-path test cases (as defined in risk assessment matrix) that are automated | ≥ 90% | Xray (Jira) test case coverage report |
| **Mean Time to Detect (MTTD)** | Average time from deployment of a defect-introducing change to creation of a Sev-1/2 defect ticket | ≤ 4 hours | Datadog alerts to Jira ticket time delta |
| **Mean Time to Resolve (MTTR)** | Average time from Sev-1/2 defect ticket creation to verified fix deployment | ≤ 24 hours (Sev-1), ≤ 72 hours (Sev-2) | Jira ticket history |
| **Flaky Test Rate** | Percentage of CI pipeline failures due to non-deterministic (flaky) tests rather than genuine failures | ≤ 2% | CI pipeline metrics → Grafana |
| **Code Coverage (Line)** | Across all active repositories (new code, 90-day rolling window) | ≥ 80% aggregate | SonarQube |
| **Open Defect Age** | Count of Sev-3 defects open > 30 days; Sev-4 defects open > 90 days | ≤ 10 total aged defects | Jira query |

### 7.2 Reporting Cadence

| Report | Audience | Frequency | Owner |
|---|---|---|---|
| **QA Executive Dashboard** | VP of Engineering, CEO, BU Owners | Real-time; reviewed at monthly Quality Review Board | QA Lead |
| **Per-Release QA Scorecard** | VP of Engineering, Product Management | Ad-hoc per release (part of Go/No-Go package) | QA Lead |
| **Defect Aging Report** | Engineering Managers | Weekly (sent via email Monday 09:00 ET) | QA Lead (automated Jira query) |
| **Test Automation Health Report** | QA Engineers, DevOps Engineers | Weekly (automated pipeline job output) | QA Lead |
| **Quarterly Quality Trend Report** | CEO, Leadership Team | Quarterly | VP of Engineering |

### 7.3 Quality Review Board

A monthly Quality Review Board meeting is chaired by the VP of Engineering. Standing agenda:
1. Review QA KPIs against targets — exceptions and trends
2. Review Sev-1 and Sev-2 production defects — root cause summaries and preventative actions
3. Review aged defects (> 60 days open) — escalation decisions
4. Review upcoming major releases — QA readiness
5. Continuous improvement initiatives

## 8. Exception Handling and Escalation

### 8.1 Exception Types

Situations may arise where strict adherence to this SOP is not practicable or would introduce disproportionate risk or delay. The following exception types are recognized:

| Exception Type | Definition | Approval Authority |
|---|---|---|
| **Emergency Hotfix Bypass** | Deployment of a fix for a Sev-1 production incident that bypasses standard QA gates (unit, integration, staging testing) | VP of Engineering (or delegate on-call manager) — documented post-hoc within 24 hours |
| **Coverage Threshold Waiver** | Approval to merge code not meeting code coverage floors | Engineering Manager for the team, with rationale documented; VP of Engineering for repeated waivers on same module |
| **Deferred Sev-2 Defect** | Decision to release with a known Sev-2 defect, accepting the business risk | VP of Engineering + Product Manager joint sign-off |
| **UAT Bypass** | Skipping UAT for a minor/patch release where risk assessment deems UAT non-value-add | QA Lead + Product Manager joint sign-off; BU Owner informed |
| **Staging Environment Unavailability** | QA in an alternate environment when staging is unavailable for > 4 hours | VP of Engineering; documented with timeline for staging restoration |

### 8.2 Exception Process

1. **Requester** identifies the need for an exception and creates an Exception Request in Jira (project `QA`, issue type `Exception`). The request shall include:
   - Specific SOP section from which deviation is requested
   - Justification for the exception
   - Risk assessment (impact if exception is granted)
   - Mitigating controls to be applied in lieu of the SOP requirement
   - Duration/scope of exception (single release, time-bound, permanent policy change requested)

2. **QA Lead** reviews and adds technical risk assessment, recommends approve/deny to the approval authority.

3. **Approval Authority** approves or denies the exception. Approval is documented in the Jira ticket.

4. **Execution**: If approved, the exception and its mitigating controls are referenced in the release validation report and deployment runbook.

5. **Closure**: The exception is reviewed post-release. If no adverse impact, exception is closed. If the exception highlights a need for permanent SOP change, a revision request is initiated (see Section 11).

### 8.3 Escalation

Quality concerns not addressed through standard channels shall be escalated:

| Level | Escalation Contact | Trigger |
|---|---|---|
| Level 1 | QA Lead | Defect triage disagreement; resource constraints impacting testing |
| Level 2 | VP of Engineering | Repeated waiver requests for same team/module; Sev-1 defect root cause indicates process failure; inability to meet release date due to quality concerns |
| Level 3 | CEO | Quality issue poses patient safety risk or material financial liability and VP of Engineering is unavailable or involved in the issue |

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Role | Required Training | Initial Delivery | Refresher Frequency |
|---|---|---|---|
| **All Product & Engineering staff** | Meridian QA Policy Overview (this SOP) | Onboarding (Week 1) | Annual |
| **Developers** | Writing Effective Unit Tests; SonarQube Usage; Secure Coding for Healthcare | Onboarding (Week 2) | Annual (Secure Coding) |
| **QA Engineers** | Advanced Test Design; Xray Test Management; Selenium/Cypress Automation Framework; FHIR Testing for Healthcare | Onboarding (Weeks 1-4) | Bi-annual |
| **MLOps Engineers** | ML Model Testing and Validation; Data Drift Detection; FMEA Methodology | Onboarding | Annual |
| **Product Managers** | Acceptance Criteria Writing; UAT Facilitation | Onboarding | Bi-annual |
| **Hiring Managers (for new joiners)** | QA Onboarding Checklist completion | N/A | Per new hire |

### 9.2 Training Tracking

- All training completion is tracked in the HRIS (Workday) Learning Management module
- QA-specific training for Product & Engineering is additionally tracked via a compliance dashboard in Confluence
- Non-compliance (overdue required training) for an individual will result in their PR merge permissions and deployment permissions being temporarily suspended in the CI/CD pipeline until training is completed

### 9.3 Continuous Improvement — Post-Incident Learning

Following any Sev-1 incident, the post-incident review shall include a specific analysis of QA process effectiveness. Where QA process gaps contributed to the incident, a targeted training or process update shall be issued within 30 days of the review conclusion.

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| Document ID | Title | Relationship to this SOP |
|---|---|---|
| SOP-PENG-001 | SDLC and Branching Strategy | Defines the development workflow and branch model this QA process operates within |
| SOP-PENG-003 | Code Review Standards | Detailed code review procedures referenced in Section 5.2.3 |
| SOP-CLNAI-007 | Clinical AI Validation | Detailed clinical efficacy validation requirements beyond standard QA |
| SOP-CLNAI-008 | Responsible AI and Algorithmic Fairness | Defines bias testing and fairness requirements for AI/ML systems |
| SOP-INFOSEC-005 | Data Classification and Handling | Governs test data usage, especially provisions related to PHI |
| SOP-DEVOPS-002 | CI/CD Pipeline Governance | Defines the pipeline infrastructure, toolchain, and platform-level gates |
| SOP-INC-001 | Incident Management | Procedures invoked upon Sev-1 production defect discovery |
| SOP-VEND-003 | Third-Party Vendor Risk Management | Due diligence for vendors whose code or services are integrated into Meridian products |

### 10.2 External Standards and Frameworks

| Standard | Reference Point |
|---|---|
| ISO/IEC 25010:2011 | Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Software product quality model |
| ISTQB Certified Tester Foundation Level Syllabus | Basis for QA Engineer training and test design methodology |
| NIST SP 800-53 Rev. 5 | Security and Privacy Controls for Information Systems (relevant to security QA controls) |
| WCAG 2.1 AA | Web Content Accessibility Guidelines (accessibility QA standard for Meridian UI) |

## 11. Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2019-05-12 | J. Miller (VP, Eng) | Initial creation. Basic QA procedures for monolithic application. |
| 2.0 | 2020-03-18 | A. Chen (QA Lead) | Major revision: migration to microservices; introduction of CI/CD pipeline QA gates; shift-left testing concepts. |
| 2.3 | 2021-09-05 | A. Chen (QA Lead) | Addition of AI/ML model QA section (5.4) following acquisition of PredictHealth ML platform. |
| 3.0 | 2023-01-15 | D. Park (VP, Eng) | Comprehensive rewrite: new RACI matrix; risk-based testing strategy; feature flag governance; environment segregation; alignment with MDR CE marking requirements. |
| 3.2 | 2024-04-10 | R. Patel (QA Lead) | Updated KPI targets; added Synthetic Data Generation procedure; revised UAT sign-off requirements to include Clinical SME. |
| 3.3 | 2024-10-28 | D. Park (VP, Eng) | Post-audit update: clarified hotfix authorization chain; tightened Sev-1 response SLAs; added Quality Review Board mandate. |
| 3.4 | 2025-02-23 | D. Park (VP, Eng) | Current version. Update defect severity definitions for fintech products; incorporate MLOps shadow deployment procedure refinements; update to new pipeline tooling references (SonarQube, Xray); revised KPIs for FY2025 targets. |