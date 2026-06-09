---
sop_id: "SOP-ITOP-012"
title: "Release Management"
business_unit: "IT Operations & Infrastructure"
version: "5.2"
effective_date: "2025-06-23"
last_reviewed: "2026-09-13"
next_review: "2027-03-16"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Release Management

## SOP-ITOP-012, Version 5.2

**Effective Date:** 2025-06-23
**Owner:** Samantha Torres, VP of IT Operations
**Approver:** David Park, VP of Engineering

---

## 1. Purpose and Scope

### 1.1 Purpose
The purpose of this Standard Operating Procedure (SOP) is to establish a standardized, controlled, and auditable process for planning, building, testing, approving, deploying, and verifying software releases across all product lines and environments at Meridian Health Technologies, Inc. This SOP ensures that all changes to production systems are delivered in a manner that protects the confidentiality, integrity, and availability (CIA) of customer data, maintains system stability, and complies with applicable regulatory frameworks, most critically SOC 2, HIPAA, and the EU AI Act for high-risk AI systems. This document operationalizes the Change Management and System Operations criteria defined within SOC 2.

### 1.2 Scope
This SOP applies to all personnel, including employees, contractors, and third-party service providers (collectively, “Meridian Personnel”), involved in the life cycle management of any software component that is deployed to or impacts a production environment. This includes all business units and their respective technology stacks:

- **Clinical AI Platform:** All models, inference APIs, model-serving infrastructure, and clinical decision support interfaces. This includes FDA 510(k)-cleared and CE-marked devices.
- **HealthPay Financial Services:** All payment processing, lending, fraud detection, and claims automation code, including SR 11-7 governed statistical models.
- **MedInsight Analytics:** The population health platform, ETL pipelines, data warehouse schemas, and any code handling Protected Health Information (PHI) for ~12M patients.
- **Meridian SaaS Platform:** The core multi-tenant platform infrastructure-as-code (IaC), authentication services, and cross-cutting utilities hosted on AWS.
- **Internal IT Tools:** Any internal application (e.g., HR systems, intranet) deemed business-critical by the VP of IT Operations.
- **Infrastructure:** All changes to production cloud environments (AWS `us-east-1`, `eu-west-1`), disaster recovery (DR) site configuration in Azure, and container orchestration platforms.

Deployments of ephemeral, isolated feature branches to a developer sandbox for the sole purpose of unit or component testing are out of scope. All other environments (development, integration, staging, production) are in scope.

---

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **A/B Testing** | A controlled experiment to evaluate a new feature or model by exposing a subset of users to the change while a control group experiences the current version. |
| **Artifact** | An immutable, versioned package of compiled code, containers, models, and configuration files stored in a repository, ready for deployment. |
| **Blue/Green Deployment** | A deployment strategy utilizing two identical production environments (Blue/Green), where traffic is switched from one to the other after validation, enabling near-zero downtime and instant rollback. |
| **Canary Deployment** | A release strategy that incrementally shifts traffic to a new service version, starting with a small percentage of users, monitoring for errors, and expanding until it replaces the old version. |
| **CCB** | Change Control Board. The cross-functional governing body, chaired by the VP of IT Operations or delegate, responsible for authorizing releases. |
| **CI/CD** | Continuous Integration / Continuous Deployment. |
| **Deployment Window** | A pre-approved time slot during which production deployments are authorized. |
| **Feature Flag** | A software development technique to decouple deployment from release, allowing functionality to be toggled on or off in a live environment without a code change. |
| **Go-Live** | The point in time when a new feature or service is made available to its target end-users. |
| **IaC** | Infrastructure as Code (Terraform, AWS CloudFormation). |
| **Lead Time for Changes** | The median time from code commit to successful production release. |
| **Mean Time to Restore (MTTR)** | The mean duration to restore service from a failed release (rollback or forward fix). |
| **Model Drift** | The degradation of a machine learning model's predictive performance due to changes in the environment, including data and concept drift. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **Pre-Production** | The staging environment, a logical mirror of production used for final validation. |
| **Release Candidate (RC)** | A specific, immutable artifact version that has passed all pre-production validation phases and is proposed for production deployment. |
| **Release Manager** | The designated IT Operations Lead responsible for orchestrating a specific release cycle. |
| **Rollback** | The process of restoring a production system to its previously known-good state. |
| **SOX** | Sarbanes-Oxley Act, relevant to the HealthPay Financial Services line for controls over financial reporting. |
| **SRG** | Service Restoration Group, the incident response team for failed releases, led by the Release Manager. |

---

## 3. Roles and Responsibilities

A RASCI (Responsible, Accountable, Supportive, Consulted, Informed) matrix formalizes accountability. All named roles may delegate operational tasks but retain ultimate accountability.

| Activity / Deliverable | Release Manager | Product Owner / PM | Engineering Lead | QA Lead | CISO / Security | CCB / VP IT Ops | DevOps Engineer |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Release Planning & Strategy** | A/R | C | C | C | C | I | I |
| **Feature & Code Commit** | I | A | R | S | I | I | S |
| **Artifact Creation & Signing** | A | I | R | I | C | I | R |
| **Security & Compliance Scan** | I | I | C | I | A/R | I | S |
| **Pre-Prod & UAT Execution** | A | C | S | R | C | I | S |
| **Go/No-Go Decision** | C | C | C | C | C | A/R | I |
| **Production Deployment** | A | I | S | I | I | I | R |
| **Smoke & Canary Testing** | A | I | S | R | I | I | R |
| **Feature Flag Toggle (Go-Live)** | I | A | R | I | I | I | S |
| **Post-Release Monitoring** | A | C | R | I | S | I | R |
| **Rollback Execution** | A/R | C | R | I | S | C | R |

**Key Role Definitions:**

- **Vice President of IT Operations (Samantha Torres):** Executive owner of this SOP. Approves all standard maintenance windows. Acts as final escalation tier for release conflicts and major incident calls.
- **Release Manager (Rotating pool of Senior IT Ops Staff):** Orchestrates the release lifecycle for a given cycle. Creates the release timeline, chairs the Go/No-Go meeting, compiles release notes, and commands the rollback if required.
- **Product Owner / Product Manager:** Defines the business value, acceptance criteria, and user communication strategy. Owns the feature flag rollout plan.
- **Engineering Lead:** Accountable for the technical architecture and code integrity of the release. Ensures all merge requests are approved and coding standards are met.
- **QA Lead:** Accountable for test strategy, test coverage, and the thoroughness of UAT and performance testing artifacts.
- **DevOps Engineer:** Executes the deployment pipeline, manages IaC changes, and maintains CI/CD tooling (GitLab CI, ArgoCD).
- **Chief Information Security Officer (Rachel Kim) / Security Team:** Authorizes the security posture of the release. Approves penetration testing waivers and exception requests.
- **Change Control Board (CCB) / VP of Engineering (David Park):** The final authority for authorizing a production deployment. The CCB may be a one-person authority (VP of Engineering) for standard releases but convenes as a board for major releases. The CCB is chaired by the VP of IT Operations.
- **Data Protection Officer (Dr. Klaus Weber):** Consulted for any release impacting GDPR data flows, cross-border transfers, or high-risk processing activities.

---

## 4. Policy Statements

The following high-level policies govern all release activities at Meridian. Deviation from any policy requires a formal exception documented and approved per Section 8.

1.  **Segregation of Duties:** An individual who authors a code commit shall not be the sole approver of its merge request. The individual who deploys a release artifact to production shall not be the sole gatekeeper for the Go/No-Go decision.
2.  **Immutable Artifacts:** Every release candidate must be a strictly versioned, immutable artifact. No source code, configuration, or model weight shall be compiled or modified after the artifact is created. (SOC 2 CC8.1)
3.  **Separation of Deployment and Go-Live:** All releases are to be deployed in a deactivated state (via feature flags or Blue/Green switch logic) and activated only after successful post-deployment validation. Deployment is an IT activity; go-live is a Business activity.
4.  **Automated Pipeline Mandate:** All deployments to pre-production and production environments must be executed via the approved CI/CD pipeline (GitLab CI/ArgoCD). Manual `kubectl`, `aws cli`, or direct database modifications against production are strictly prohibited. (SOC 2 CC7.2)
5.  **Pre-Approved Deployment Windows:** Production deployments are restricted to the defined maintenance windows (Section 5.4). Emergency deployments are permitted but require post-hoc CCB review within 24 hours.
6.  **Zero-Data Exposure Testing:** Pre-production (staging) testing must use sanitized, synthetic, or fully-masked data. Production PHI/ePHI shall never be replicated to a non-HIPAA-compliant environment. (SOC 2 PI1.4)
7.  **Verifiable Rollback Readiness:** A documented and practiced rollback or forward-fix plan must be explicitly included in the release runbook *before* the CCB Go/No-Go meeting. If the rollback plan has not been tested in the last 90 days, the release is classified as High Risk.
8.  **Regulatory Hold (EU AI Act/Clinical):** Any change to a 510(k)-cleared algorithm, its primary use case, or a CE-marked medical device software requires mandatory consultation with the Regulatory Affairs and Quality Assurance (RA/QA) team. A “No Regulatory Impact” sign-off or an approved Change Submission to the relevant notified body (e.g., BSI) is a prerequisite for the CCB Go/No-Go for AI/ML Model releases. (SOP-REG-007 Clinical Release Addendum).

---

## 5. Detailed Procedures

### 5.1 Release Planning and Classification

The process begins with the Product Owner defining the scope of a release. All releases are categorized to determine the governance pathway.

**Table 5-A: Release Classification Matrix**

| Category | Impact | Examples | Governance |
| :--- | :--- | :--- | :--- |
| **Emergency / Hotfix** | Critical outage or security vulnerability in production. P0 Incident. | Zero-day Log4Shell patch, payment gateway outage fix, critical data leakage fix. | War-room protocol. VP of Engineering & CISO approval. Deployment by Release Manager & DevOps Lead (two-person rule). Post-hoc CCB documentation within 24h. |
| **Standard** | Planned feature update, performance improvement, non-critical bug fix. Low/Moderate risk. | A new UI filter on the dashboard; a standard dependency update; a minor fraud model coefficient refresh. | Standard pipeline. Release Manager-led. Electronic Go/No-Go. |
| **Major** | Significant architectural re-platforming, public API breaking changes, multi-team coordinated delivery, or a fundamental change to a regulated algorithm. | Migrating the Claims Engine from EC2 to EKS; Upgrading the Clinical AI diagnostic engine with a new 510(k)-cleared algorithm (v2.1). | Full CCB meeting required. VP of IT Operations and CISO approval mandatory. Formal UAT sign-off from Product Owner. Full DR test in scope. |
| **Infrastructure** | Changes to IaC, network topology, container orchestration nodes, or AWS Account settings. | Modifying VPC CIDR blocks; upgrading the EKS cluster controller; rotating root Certificate Authorities. | Treated as Major. All IaC changes require `terraform plan` output attached to the CCB ticket. |

### 5.2 The Meridian Release Lifecycle: The "T-7" Model

For Standard and Major releases, a standardized 7-working-day lifecycle (T-7) is enforced.

**T-7: Release Initiation**
- **Action (Product Owner):** Creates a `RELEASE` ticket in Jira with the unique Release Name (semantic version, e.g., `MedInsight-2025.07-Sprint4`). Links all in-scope User Stories and Bug tickets. Assigns the Release Manager.
- **Action (Release Manager):** Creates the Release "Epic" and a dedicated Slack channel `#rel-<release-name>`.

**T-5: Code Freeze & Artifact Vaulting**
- **Action (Engineering Lead):** All feature branches are merged into a release branch (`release/vX.Y.Z`) in GitLab. Development on new features for this release ceases. Only critical bug fixes are merged after this point.
- **Action (CI Pipeline):** On merge to the release branch, GitLab CI/Kaniko automatically builds the Docker container, tags it with the release name and Git SHA256 hash, and pushes it to the AWS ECR (Elastic Container Registry).
- **Action (DevOps):** For IaC, a `terraform plan` is executed and the output attached to the Release ticket. The immutable commit hash is recorded.

**T-4: Environment Deployment & Quality Gate 1 (Staging)**
- **Action (Release Manager):** Triggers the `deploy-to-staging` pipeline in GitLab.
- **Action (Automated Tests):** The pipeline executes the Acceptance Test Suite. Quality Gate 1 is "Green" only if:
    - 100% of Critical and High priority test cases pass.
    - Test coverage does not decrease by more than 0.5% from the previous release.
    - The Semgrep SAST scan reports zero Critical findings.

**T-3 & T-2: User Acceptance Testing (UAT) & Performance Testing**
- **Action (QE/QA Lead):** Executes the UAT script in Staging. This includes exploratory testing, negative path testing, and HIPAA data handling verification.
- **Action (DevOps Lead):** Executes the Performance & Resilience Test Suite against the Staging environment.
    - *Pass Criteria:* P95 latency < 300ms for Clinical APIs; Throughput > 1000 TPS for Payment Gateway. Chaos Engineering tests pass (e.g., simulated pod deletion, Aurora replica failure).
    - **SOC 2 PI1.5 Conformity:** A Performance Test Report is autogenerated by K6/Gatling and archived to the Meridian AWS Evidence Bucket.

**T-1: The CCB Go/No-Go Meeting**
The Release Manager presents the release evidence package to the Change Control Board. For a Standard release, this may be an asynchronous review of a dashboard. For Major releases, this is a synchronous 30-minute mandatory video conference.
(See Section 5.3 for Go/No-Go criteria).

### 5.3 Go/No-Go Criteria and Decision Matrix

No release shall proceed without formal approval. The CCB approval is a recorded, auditable artifact in the Jira RELEASE ticket. The decision is based on the absolute, non-negotiable criteria below. If any "NO-GO" criterion is true, the release is blocked.

**Table 5-B: Mandatory Go/No-Go Checklist**

| # | Criterion | Responsible Party | Status | Evidence Required (Must be attached to Jira Ticket) |
| :--- | :--- | :--- | :--- | :--- |
| **C1** | **Test Completion:** All UAT, Performance, and Security test cycles are complete. | QE Lead | ☐ Go / ☐ No-Go | Stamped Test Summary Report (.pdf) |
| **C2** | **Zero Critical/High Vulnerabilities:** The Aqua container scan and OWASP ZAP dynamic scan report zero *unresolved* Critical or High vulnerabilities. | Security Architect | ☐ Go / ☐ No-Go | Aqua/ZAP scan report (Automated link) |
| **C3** | **Rollback/Fix Plan Tested:** For Major releases, the rollback procedure has been enacted and verified in a lower environment in the last 30 days. For all releases, the plan is documented. | DevOps Lead | ☐ Go / ☐ No-Go | Log output of rollback test in `#rel-<name>` channel |
| **C4** | **Regulatory Sign-Off:** If the release impacts a 510(k) cleared device or CE-marked product, a signed RA/QA approval document is attached. | Product Owner | ☐ Go / ☐ No-Go | RA/QA Approval Form (DocuSign Envelope ID) |
| **C5** | **Operational Readiness:** Dashboards, alerts, and logging are configured in Datadog for the new service/version. On-call SRE team has acknowledged the release and its runbook. | Release Manager | ☐ Go / ☐ No-Go | Link to Datadog Dashboard; Slack acknowledgement from Incident Commander. |
| **C6** | **Data Privacy:** For any release involving new or modified PHI/ePHI processing, the Data Privacy Impact Assessment (DPIA) is approved per SOP-COMP-004. | DPO / Privacy Office | ☐ Go / ☐ No-Go for PHI | DPIA Tracker ID |

The CCB Chair (VP of IT Operations, or for Major releases, the full CCB) reviews the checklist. If all criteria are "Go", the Chair digitally approves the Jira ticket, which is the webhook trigger to unlock the production deployment pipeline for the specified Release Candidate artifact tag.

### 5.4 Production Deployment Windows & Execution

Standard maintenance windows are enforced to protect business continuity and provide predictable support.

| Category | Authorized Windows (Eastern Time) | Max Duration |
| :--- | :--- | :--- |
| **Clinical AI & Patient-Facing Apps** | Wednesdays, 02:00 AM – 04:00 AM ET | 2 hours |
| **HealthPay Financial Services** | Saturdays, 12:00 AM – 04:00 AM ET | 4 hours |
| **MedInsight Analytics** | Thursdays, 02:00 AM – 05:00 AM ET | 3 hours |
| **SaaS Platform (Shared Services)** | Tuesday/Thursday, 03:00 AM – 04:00 AM ET | 1 hour |
| **Emergency / Hotfix** | Any time. Requires explicit approval from CISO and VP Engineering. | Per incident |

**Production Deployment Procedure (Canary Strategy - Default):**

1.  **Initiation (DevOps):** DevOps Lead triggers the `deploy-to-production` job via GitLab, confirming the artifact tag. The job is audited and immutable — no parameters can be changed post-initiation.
2.  **Phase 1: Deploy Inactive (0% Traffic):** ArgoCD syncs the new ReplicaSet/Service version into the production Kubernetes cluster with a feature flag set to `off` or a Blue environment ready. A system health ping is sent to Datadog. **No user traffic is served.**
3.  **Phase 2: Smoke Test (Internal Traffic Only):** The pipeline auto-executes smoke tests against the new pods. This validates network connectivity, secret resolution (Vault), and database connectivity. If smoke tests fail, the pipeline HALT is automatic.
4.  **Phase 3: Canary (5% Traffic, 15-Minute Bake):** A live traffic shifting rule (Istio `VirtualService`) sends exactly 5% of real user traffic to the new version. Datadog monitors the SLO burn rate for the service.
    - **Autoblock:** If the error rate 4xx/5xx is 2x baseline, or P99 latency exceeds SLO, the canary is automatically aborted by the Istio/Argo Rollouts controller and traffic is shifted back.
5.  **Phase 4: Full Rollout (100% Traffic):** If the 15-minute bake is green, traffic is ramped to 100%. The old ReplicaSet is scaled down but not deleted (for instant rollback).
6.  **Phase 5: Deployment Complete:** The DevOps Engineer posts a completion message to `#team-devops` and `#release-<name>`.

### 5.5 Post-Deployment Go-Live & Feature Flag Toggle

Once the deployment is verified and stable, the responsibility shifts to the Product Owner for the "Go-Live" activation.

1.  **Internal Launch:** Product Owner toggles the feature flag to "ON" for Meridian internal employees (dogfooding phase). Monitors for 2 hours.
2.  **External Beta (if applicable):** Feature is enabled for a pre-selected group of users/clients.
3.  **General Availability (GA):** Product Owner activates the feature for all target users. This is executed via the LaunchDarkly feature flag tool (which maintains a full audit log of all toggle changes). *Note: The toggle UI change is a separate, governed action from the deployment.*

### 5.6 Release Notes and Artifact Documentation

The Release Manager owns the curation and publication of Release Notes. These are mandatory for all external-facing releases.

**Release Note Structure (Markdown template in `RELEASE_NOTES.md`):**

- **Header:** Product Name, Release Version, Release Date.
- **Highlights:** 1-2 sentence value-focused summary.
- **New Features:** A bulleted list of new functionality, linked to the corresponding user guides.
- **Known Issues & Limitations:** A critical transparency section, listing any defects deferred to the next sprint and any workarounds.
- **Regulatory Statements:** For Clinical AI, a section titled “Clinical Performance and Limitations” must include the AUC/ROC performance of the current version on the validation holdout set and any patient demographic subgroup analysis. This is mandatory for CE-marked Medical Device compliance.
- **Base Artifact:** The SHA256 digest of the deployed container image.

The document is published to the Meridian Customer Knowledge Base and attached to the Jira release ticket, fulfilling SOC 2 control CC7.4 (Communication of System Changes).

---

## 6. Controls and Safeguards

This section operationalizes the SOC 2 Common Criteria (COSO Principle Points) through specific technical and administrative controls.

### 6.1 Technical Controls (Automated Guards)

- **GitLab CI Branch Protection (SOC 2 CC8.1):** The `main` and `release/*` branches are protected. No direct push is allowed. Code must be merged via a Merge Request with a minimum of two approvals, one of which must be from a code owner (specified in the `CODEOWNERS` file).
- **Artifact Signing (SOC 2 CC6.1):** All container images pushed to the production-grade ECR repository (`meridian-prod-images`) are signed using AWS Signer and a key from AWS Key Management Service (KMS). The ArgoCD admission controller is configured to *only* deploy signed images from the trusted prod registry.
- **Network Security Policy (Kubernetes):** Strict `NetworkPolicy` objects are implemented. The `staging` namespace is isolated from `production`. Pods in production cannot egress to the public internet unless explicitly for a documented business need (e.g., a payment gateway API call, which must be on an allow-listed CIDR block).
- **Secrets Management:** No secrets (API keys, DB passwords) are in code or environment variables. All secrets are injected at pod runtime from HashiCorp Vault using the Kubernetes Auth Method. (SOC 2 CC6.3)
- **Database Change Control (SOC 2 CC8.2):** All schema changes (DDL scripts) are stored in a Liquibase/Flyway repository and executed by the CI/CD pipeline as an automated step *before* the application deployment. The pipeline user is the only entity with DDL grant permissions on production databases.

### 6.2 Administrative Controls (Process Guards)

- **Quarterly Release Retrospective:** A blameless process review is held to improve lead time and reliability. Metrics like deployment frequency and change-failure rate are reviewed against the board-approved SLA targets.
- **Access Certification:** Access to the production deployment pipeline (GitLab CI variables, ArgoCD RBAC) is reviewed by the CISO on a quarterly basis as part of SOP-IS-003 (Access Control Review). Break-glass access credentials are stored in a PIM vault and require two-person simultaneous check-out.
- **Third-Party Integration:** Any release introducing a new third-party vendor integration (e.g., a new SMS gateway or fraud data provider) must undergo the full Vendor Security Assessment per SOP-PROC-005. The integration code must abstract the vendor via an anti-corruption layer pattern, enabling the vendor to be replaced without a fundamental system re-architecture.

---

## 7. Monitoring, Metrics, and Reporting

To ensure the continuous health of the release process, the following DORA metrics and operational health indicators are tracked.

### 7.1 Key Performance Indicators (KPIs)

A live dashboard, powered by GitLab and Datadog data, is maintained for the VP of Engineering and CTO. The SLOs are measured on a rolling 30-day window.

| Metric | Target (SLO) | Alerting Threshold |
| :--- | :--- | :--- |
| **Deployment Frequency** | > 5 Standard Deployments per week per mainline service. | N/A (metric is a trailing indicator). |
| **Lead Time for Changes** | < 1 hour for a hotfix commit to reach production. < 72 hours for a standard feature from code merge to production. | > 96 hours triggers a process-review ticket automatically. |
| **Change Failure Rate** | < 5%. (Failed release = any release requiring a rollback or a hotfix post Go-Live within 24 hours). | > 5% triggers an automatic Severity-1 Engineering Alert and halts all non-critical releases until root cause analysis is complete. |
| **Failed Deployment Recovery Time (MTTR)** | < 15 minutes (automated rollback). | > 15 minutes triggers a P2 Incident ticket for the SRE team. |
| **Environment Parity Drift** | 0. Number of configuration differences between Staging and Production detected by the "EnvDiff" Datadog job. | Any drift triggers a P3 Warning in the #team-devops channel. |

### 7.2 Reporting Cadence
- **Weekly:** Operational report on all deployments, rollbacks, and deployment windows used sent to IT Operations management.
- **Monthly:** The Release Management process health is included in the CISO’s SOC 2 monitoring meeting (review of controls CC8.1, PI1.5).
- **Quarterly:** A full service review meeting with the VP of Engineering and VP of IT Operations, covering KPI trends against targets, key process bottlenecks, and the quarterly release retrospective findings. This report is archived as SOC 2 evidence of management monitoring of the subservice organization’s (IT Ops) controls.

---

## 8. Exception Handling and Escalation

Deviations from this SOP are to be treated as risk control failures unless formally excepted.

### 8.1 Exception Request Process
If a release cannot meet a Go/No-Go criterion (e.g., a Medium CVE cannot be patched, a UAT sign-off is impossible due to a client-side environment issue), an exception may be requested. Release exceptions are not permitted for Critical CVE findings (C1 must remain "Go").

1.  The Engineering Lead or Product Owner creates an "Exception" issue in the Release Jira ticket, detailing:
    - The specific control/criterion being excepted.
    - The technical and business justification.
    - The compensating control to be put in place during the risk.
    - The remediation date and owner for the underlying issue.
2.  The Release Manager escalates the Jira ticket to the CCB with a recommendation.
3.  The CCB adjudicates. Approval must be recorded with a signed-off comment in the Jira ticket.
    - For any exception involving PHI security, the CISO must personally approve.
    - For any exception involving EU data, the DPO must approve.

### 8.2 Escalation Path for Deployment Conflicts

| Tier | Escalation Point | Trigger |
| :--- | :--- | :--- |
| **Tier 1** | **Release Manager** | Any procedural blockage (e.g., test environment not ready). |
| **Tier 2** | **Samantha Torres, VP of IT Operations** | Two conflicting emergency releases vie for the same window; need to authorize a deployment outside the standard window. |
| **Tier 3** | **David Park, VP of Engineering & Rachel Kim, CISO** | A decision to deploy to production with a known High vulnerability is being contemplated (Emergency Exception). This requires VP-level dual authorization. |

---

## 9. Training Requirements

The effectiveness of this SOP is dependent on the proficiency of the personnel who execute it.

| Target Audience | Training Module | Frequency | Owner |
| :--- | :--- | :--- | :--- |
| **All Engineering, QA, DevOps** | `REL-101: Release Management Fundamentals` (45-min online, mandatory quiz). Covers versioning, artifact creation, roles, and RACI. | Annually, plus within 30 days of hire. | HR/L&D via Workday. |
| **Release Managers & DevOps** | `REL-201: Advanced Deployment & Incident Command` (Half-day instructor-led workshop). Covers runbook creation, helm charts, ArgoCD dashboards, and rollback command-line execution. | Annually. | VP of IT Operations. |
| **Product Owners / Managers** | `REL-301: Feature Flag Governance and Go-Live`. Covers LaunchDarkly best practices and customer communication policy. | On Role Assignment. | Product SVP. |
| **CCB Members** | `REL-401: CCB Duties & Compliance Adjudication`. Covers SOC 2 and regulatory (HIPAA/MDR) implications of Go/No-Go decisions. | Biannually. | CISO & VP of Engineering. |

All training records are tracked in Meridian’s Learning Management System (Workday). SOC 2 auditors will sample completed training records for personnel associated with audit-period releases. An expired training certification automatically revokes the person's role assignment in the CI/CD pipeline RBAC until re-certification.

---

## 10. Related Policies and References

- **SOP-IS-003:** Access Control Policy & Review
- **SOP-IS-014:** Incident Response & Management
- **SOP-IS-008:** Vulnerability and Patch Management
- **SOP-COMP-004:** Data Privacy Impact Assessment (DPIA)
- **SOP-ENG-001:** Software Development Life Cycle (SDLC)
- **SOP-DATA-002:** Production Data Handling and Masking
- **SOP-PROC-005:** Third-Party Vendor Risk Management
- **SOP-REG-007:** Clinical AI/ML Regulatory Release Addendum (510(k)/MDR specific)
- **SOC 2 Common Criteria:** CC6.1 (Logical Access Security), CC6.3 (Encryption), CC7.2 (System Monitoring), CC7.4 (Communication of System Changes/Release Notes), CC8.1 (Change Authorization), CC8.2 (Testing of Changes), PI1.4 (Data Integrity), PI1.5 (Processing Integrity).
- **AWS Well-Architected Framework (Operational Excellence Pillar)**
- **EU MDR 2017/745 Annex I (General Safety and Performance Requirements)**
- **PCI DSS v4.0 (Relevant for HealthPay)**

---

## 11. Revision History

| Version | Effective Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **1.0** | 2021-10-05 | Michael Kent | Initial document creation. Manual deployment process. |
| **3.1** | 2023-04-12 | Sarah Chen | Major revision to integrate full CI/CD automation via GitLab/ArgoCD. Introduction of the T-7 lifecycle model. Removal of manual FTP-based releases. |
| **4.4** | 2024-11-01 | Samantha Torres | Addition of RA/QA gate for Clinical AI releases (MDR/IVDR compliance). New Section 5.6 on regulated release notes. Updated classification matrix for CE-marked devices. |
| **5.0** | 2025-06-23 | Samantha Torres | Complete rewrite for SOC 2 Type II Audit. Introduced RASCI matrix. Formalized Go/No-Go criteria with digital evidence map. Aligned metrics with DORA standards. Integrated new `meridian-prod-images` AWS Signer and LaunchDarkly governance. |
| **5.1** | 2026-01-10 | Samantha Torres | Minor update to clarify Environment Parity Drift KPI and remediation of false positives from the `EnvDiff` tool. Added A/B testing definition. |
| **5.2** | 2026-09-13 | Samantha Torres | Annual review. Updated exception process for Medium CVEs. Added DPO role to RASCI matrix for GDPR. Updated rollback MTTR SLO from < 30 min to < 15 min following Blue/Green implementation. |

---
**End of Document — SOP-ITOP-012**