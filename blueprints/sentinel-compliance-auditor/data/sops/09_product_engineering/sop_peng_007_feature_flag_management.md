---
sop_id: "SOP-PENG-007"
title: "Feature Flag Management"
business_unit: "Product & Engineering"
version: "2.6"
effective_date: "2025-03-08"
last_reviewed: "2026-06-18"
next_review: "2026-12-27"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Feature Flag Management

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the governance framework, lifecycle management protocols, and technical controls for the use of feature flags across all products and services developed and maintained by Meridian Health Technologies, Inc. The purpose of this document is to decouple deployment from release, mitigate risk associated with changes to production systems, ensure accountability for all code paths, and maintain the integrity of systems subject to regulatory oversight.

This SOP mandates a standardized approach to feature flag creation, targeting, maintenance, and removal to prevent technical debt accumulation, reduce complexity, and ensure that all feature flag activities are fully auditable in accordance with SOC 2 Common Criteria 8.1 (Change Management) and our internal compliance obligations.

### 1.2 Scope
This SOP applies to all feature flags, circuit breakers, operational toggles, permission toggles, and experimental toggles in any environment subject to change control within Meridian Health Technologies, including:

| Environment | Scope | Applicability |
| :--- | :--- | :--- |
| **Production** | All customer-facing and internal production services | Full SOP applies |
| **Staging** | Pre-production validation environments | Full SOP applies |
| **Development** | Shared development and integration sandboxes | Sections 5.1 (Creation), 5.2 (Targeting), and 5.4 (Cleanup) only |
| **Local** | Developer workstations | Exempt, subject to SOP-PENG-002 Code Review |

**In-Scope Systems:**
- Meridian SaaS Platform (all microservices deployed on AWS us-east-1, eu-west-1)
- Clinical AI Platform (diagnostic imaging analysis, patient risk scoring, adverse event prediction)
- HealthPay Financial Services (payment processing, patient financing, lending models)
- MedInsight Analytics (population health, care gap identification)
- All internal tools capable of altering system behavior in production

**In-Scope Flag Categories:**
- **Release Toggles:** Control exposure of new functionality for trunk-based development
- **Operational Toggles:** Circuit breakers, rate limiters, and kill switches for operational control
- **Permission Toggles:** Feature access based on user, tenant, or plan attributes
- **Experiment Toggles:** A/B testing and multivariate testing configurations
- **Targeted Rollout Toggles:** Percentage-based or cohort-based progressive delivery

**Out of Scope:**
- Configuration values that do not alter control flow (use AWS Systems Manager Parameter Store or HashiCorp Vault in accordance with SOP-ISMS-012)
- Emergency hotfixes bypassing the flagging system; these require a Critical Incident per SOP-ISMS-014

### 1.3 Target Audience
This document is binding upon all employees, contractors, and third-party partners within the Product & Engineering business unit, specifically:
- All Software Engineers and Engineering Managers
- Site Reliability Engineering (SRE) team members (VP of IT Operations organization)
- Quality Assurance (QA) and Test Automation Engineers
- Product Managers authoring experiment toggles
- Customer Operations (read-only access for triage purposes)

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **Feature Flag** | A software engineering technique that turns functionality on or off at runtime without deploying new code. Represented as a conditional statement in code. |
| **Flag Configuration** | The set of rules, targeting constraints, and state (ON/OFF) that define a flag's runtime behavior stored in the feature management platform. |
| **Targeting Rule** | A logical predicate evaluated at runtime that determines which users, sessions, or requests receive a specific flag variation. |
| **Stale Flag** | A flag that has been fully rolled out to 100% (or fully removed) for more than 30 calendar days in production but whose code reference and configuration have not been removed. |
| **Kill Switch** | An operational toggle designed to immediately disable a feature or integration in response to an incident without a full deployment. |
| **Circuit Breaker** | An operational toggle that automatically (or manually) prevents cascading failures by stopping requests to a failing downstream service. |
| **Flag-Driven Development** | The practice of wrapping new or modified functionality in feature flags during the software development lifecycle within trunk-based development. |
| **Feature Management Platform** | The centralized system of record for flag configurations, evaluation, and audit logging. Meridian uses **LaunchDarkly** as the enterprise standard. |
| **Flag Evaluation** | The real-time process where the SDK determines the served variation for a specific context (user, session). |
| **Flag Bloat** | The accumulation of stale, unmaintained, or undocumented flags in the codebase, creating technical debt and security/regulatory risk. |
| **Canary Deployment** | A progressive delivery strategy using a percentage-based rollout toggle to gradually shift traffic to a new version. |
| **A/B Experiment** | A controlled experiment using an experiment toggle to compare two or more variants of a feature against defined success metrics. |
| **Flag Manifest** | The machine-readable declaration of all flags expected by a specific service version. |

## 3. Roles and Responsibilities

The following RACI matrix defines the engagement of each role in the Feature Flag lifecycle:

| Activity | Product Manager | Engineer | Engineering Manager | SRE | QA | Release Captain | VP of Engineering |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Flag Request & Intent Specification | **R** | C | I | I | C | I | I |
| Flag Creation & Code Integration | I | **R** | A | C | C | I | I |
| Peer Code Review (Flag Logic) | I | **R** | C | I | I | A | I |
| QA Validation & Toggle Testing | I | C | I | I | **R** | I | I |
| Production Release Coordination | I | A | I | C | I | **R** | I |
| Operational Kill Switch Trigger | I | I | I | **R** | I | I | A |
| Flag Cleanup & Debt Tracking | C | **R** | A | I | I | I | I |
| Approval of Permanent/ Long-Lived Flags | C | C | C | C | I | I | **R** |
| Audit Review & Compliance | I | I | I | I | I | C | **R** |

**Key: R = Responsible (Doer), A = Accountable (Approver), C = Consulted, I = Informed**

### 3.1 Named Responsibility Assignments

| Role | Named Lead | Core Responsibility |
| :--- | :--- | :--- |
| **VP of Engineering** | David Park | Ultimate authority for flag lifecycle policy, exception approvals, and technical debt SLAs. Acts as the SOC 2 Management Review owner for change management controls. |
| **SRE Lead** | Samantha Torres (VP of IT Operations) | Operational toggle architecture, circuit breaker thresholds, and PagerDuty escalation integration. |
| **Release Captain** | Rotating role (appointed per sprint) | Coordinates flag state transitions during release windows; manages the Release Runbook per SOP-ISMS-010. |
| **Engineering Managers** | Team-specific | Enforce flag hygiene within sprints; ensure cleanup tickets are prioritized in backlog. |
| **QA Director** | Maria Chen (Reporting to VP of Engineering) | Maintains the Toggle Testing Matrix and automated validation suite. |

## 4. Policy Statements

### 4.1 General Principles
- **MANDATORY PLATFORM:** All feature flags interacting with production traffic MUST be managed through the centralized LaunchDarkly platform. Local configuration files or environment variables are prohibited for dynamic feature control in staging or production.
- **NO PERMANENT FLAGS:** Feature flags are inherently transient. No flag may be marked as permanent without a formal exception approved by the VP of Engineering and reviewed by the Chief Information Security Officer. Even approved long-lived permission toggles must undergo annual review.
- **DEFAULT TO DARK:** Newly created flags MUST default to the OFF (disabled) state in production environments when the targeted audience is not explicitly matched. This prevents unintentional exposure of untested features.
- **AUDIT TRAIL INTEGRITY:** Every flag evaluation, configuration change, and targeting rule update MUST produce an immutable audit log. These events must be shipped to our SIEM (Splunk) and the flag’s manifest must be traceable to a specific Jira ticket and Git commit.
- **HEALTHPAY & CLINICAL AI – ENHANCED SCRUTINY:** Flags altering financial calculations (credit scoring, payment routing, interest calculations per SR 11-7) or clinical reasoning (diagnostic support, patient risk scoring per EU AI Act Annex III) require a **Second Approver** and a **Risk Assessment** per Section 5.2.3 prior to activation.

### 4.2 Lifecycle Management Commitment
Meridian Engineering commits to a "Zero Stale Flags" target. No flag shall remain in the codebase longer than 60 days after its rollout has been completed. Feature flag cleanup is tracked as a sprint-level metric and reported to the AI Governance Committee as part of technical debt oversight.

### 4.3 Security & Segregation of Duties
- **SEGREGATION:** The person implementing a flag’s code logic shall not be the sole individual deploying and activating a financial or clinical toggle in production. A Release Captain or secondary engineer must confirm.
- **ACCESS CONTROL:** Access to modify production flag targeting rules is restricted via Okta SSO and LaunchDarkly Custom Roles. Only the SRE team and designated Engineering Managers have "Production Maintainer" access.

## 5. Detailed Procedures

This section outlines the operational lifecycle of a feature flag from inception to retirement, aligned with the SOC 2 change management control lifecycle.

### 5.1 Flag Creation and Registration

#### 5.1.1 Flag Naming Convention
All flags must adhere to a strict naming convention to ensure discoverability and automated classification:

**Format:** `{Team}-{Service}-{Feature}-{Type}`

**Examples:**
- `pay-lending-riskmodel-v2` (Release Toggle)
- `clinicai-diag-xray-permission` (Permission Toggle)
- `ops-api-payments-cbreaker` (Circuit Breaker)
- `analytics-dash-export-experiment` (Experiment Toggle)

**Type Suffixes:**
- Release: `-v{number}`
- Permission: `-permission`
- Operational (Kill Switch): `-killswitch`
- Operational (Circuit Breaker): `-cbreaker`
- Experiment: `-experiment`

Invalid names will be rejected by the pre-receive hook in GitHub (enforced via SOP-PENG-001).

#### 5.1.2 Jira Ticket Template
Every flag must be associated with a Jira Epic or Story using the `feature_flag_creation` issue type. The Jira ticket must include:

1.  **Flag Name:** (per convention)
2.  **Flag Type:** (Release, Experiment, Operational, Permission)
3.  **Intent & Hypothesis:** What behavior is changing and why.
4.  **Success/Observability Metrics:** Datadog dashboard link or PagerDuty alert to monitor.
5.  **Risk Assessment Link:** Required for HealthPay/Clinical AI (See 5.2.3).
6.  **Planned Rollout Percentage:** e.g., 10% > 50% > 100%.
7.  **Expected Retirement Date (ERD):** Maximum 60 days post-creation.

#### 5.1.3 Code Implementation Standard
Engineers must implement flags using the LaunchDarkly Server-Side SDK (Python/Node.js) or Client-Side SDK (React).

**Mandatory Code Pattern:**
```python
# CORRECT: Safe evaluation with fallback
import ldclient
user = {"key": session.user_id, "custom": {"tenant": session.tenant_id}}
flag_value = ldclient.get().variation("pay-lending-riskmodel-v2", user, False)

if flag_value:
    execute_v2_risk_model()
else:
    execute_v1_risk_model()
```

**Prohibitions:**
- Hard-coding flag values to `True` in any non-local environment.
- Wrapping vast swaths of code in a single flag (prefers modular, narrow toggles).
- Catching generic exceptions inside the flag evaluation block without logging the flag evaluation error.

### 5.2 Targeting and Progressive Rollout

#### 5.2.1 Rollout Strategy
Meridian adopts a progressive delivery model:

| Stage | Target Audience | Duration (Minimum) | Monitoring Gate |
| :--- | :--- | :--- | :--- |
| 1. Internal Alpha | `employee-id` rule / Meridian internal tenant | Immediate | 5xx errors > 0.1%, Latency p99 < 500ms |
| 2. Canary (10%) | Random 10% of external users | 2 hours | 5xx errors stable, Business metrics neutral |
| 3. Beta (50%) | Random 50% of external users | 4 hours | No new PagerDuty Sev2 alerts |
| 4. Full Rollout | 100% of intended audience | Continuous monitoring for 24 hours | Stable dashboard baseline |

**Exception:** For operational kill switches or circuit breakers (ops-*), immediate 100% rollout is permitted if triggered by a PagerDuty Sev1 incident.

#### 5.2.2 Percentage Rollout Integrity
When using percentage-based rollouts for the MedInsight Analytics or HealthPay Financial Services platforms, the flag evaluation MUST be sticky. The default attribute for sticky bucketing is `user.key`. Random assignment must be deterministic per user to ensure a consistent user experience.

#### 5.2.3 Enhanced Scrutiny for Regulated Models
For any flag altering a model governed by SR 11-7 (credit/fraud scoring) or the EU AI Act (Clinical AI diagnostics), the Engineer must complete the **"Regulated Model Toggle Risk Assessment"** (see Appendix A). The Risk Assessment must be approved by:
1.  **Engineer’s Manager**
2.  **Chief AI Officer** (Dr. Marcus Rivera) or **Chief Medical Officer** (Dr. Priya Patel) delegate.

This approval must be attached to the Jira ticket before the flag is activated in production. The flag will be tagged in LaunchDarkly with the `regulated-model` tag, enforcing a mandatory 30-minute "cool-off" period before any percentage change takes effect, allowing independent monitoring review.

### 5.3 Flag Operation and Monitoring

#### 5.3.1 Real-Time Observability
All flag evaluations must be exported from LaunchDarkly to Datadog via the native integration. Engineers must annotate deployment events in Datadog with the flag name.

**Critical Thresholds for Automated Circuit Breakers:**
Meridian SRE team maintains an automatic guardrail for `pay-*` and `clinicai-*` flags:
If a newly activated feature flag correlates with a 5% increase in the service’s p99 latency or a 1% increase in error rate within 5 minutes, the LaunchDarkly Relay Proxy will automatically receive a "rollback" command to set the flag to `False` for all traffic. SRE will be paged via PagerDuty.

#### 5.3.2 User Inbox Notifications
If a feature flag change materially alters the UI for a provider or patient, the release must be registered with the Customer Operations team (VP: Michael Chang) 48 business hours in advance. This allows the creation of a "What’s New" in-app notification or a proactive support chat banner.

### 5.4 Flag Cleanup and Retirement

#### 5.4.1 The "Two-Week Rule"
Once a flag is activated at 100% for its intended audience (and not just an experiment), the Jira ticket status transitions to `Pending Cleanup`. The Engineer has a standard SLA of **14 calendar days** to:
1.  Remove the flag evaluation code from the codebase.
2.  Remove all conditional branches, leaving only the new code path.
3.  Create a Pull Request tagged with `flag-cleanup`.
4.  Delete the flag configuration from LaunchDarkly.

#### 5.4.2 Stale Flag Escalation
If a flag exists beyond its ERD:
- **Day 30 (Stale):** LaunchDarkly Code References feature automatically creates a "Stale Flag" Slack notification to the Engineering Manager and Jira task.
- **Day 45:** The flag is added to the "Flag Bloat" report reviewed at the weekly E-Staff Operations meeting.
- **Day 60:** The flag configuration is **forcibly archived** by the SRE team, even if code remains. If the code is still live, this will cause the default (FALSE) path to execute, potentially disabling the feature. This is intended as a forcing function to prevent unmaintained dead code.

#### 5.4.3 Physical Code Removal
Mere removal from LaunchDarkly is insufficient. The Engineer must use the **LaunchDarkly Code References** feature (integrated with GitHub) to locate every instance of the flag in the source code. Unused flags in code are treated as dead code vulnerabilities and flagged by CrowdStrike Falcon in SAST mode.

### 5.5 Emergency Kill Switch
In the event of a Sev1 incident related to a feature:
1.  The Incident Commander (SRE) identifies the feature flag.
2.  SRE executes the "Kill Switch" action in the LaunchDarkly dashboard or invokes the `meridian-cli kill-switch --target {flag_key}`.
3.  A Priority 1 Jira ticket is retroactively created to document the reason for the kill.
4.  The underlying code is not automatically cleaned up, but the flag is placed in a "Disabled-Permanent" state, locking the targeting to FALSE. Standard cleanup procedures resume post-mortem.

## 6. Controls and Safeguards

This section maps Meridian’s technical and administrative controls directly to the applicable SOC 2 Trust Services Criteria: **CC8.1 (Change Management)** .

### 6.1 Access Control Matrix (SOC 2 Control 8.1 a)
Access to modify feature flags in production is strictly restricted and enforced via Okta SAML integration and LaunchDarkly Custom Roles.

| Role | Environment | Permissions | Segregation Control |
| :--- | :--- | :--- | :--- |
| **Software Engineer** | Development/Test | Creator, Editor | Can create flags but cannot toggle Production flags to ON without Release Captain approval. |
| **Engineering Manager** | Production | Production Maintainer | Can toggle flags ON/OFF. Cannot modify RBAC permissions. |
| **SRE** | Production | Admin | Full control. Can create operational toggles on the fly. Actions alert the Security team. |
| **Release Captain** | Production | Approver | Must approve all percentage-increase requests for regulated models via Jira workflow. |
| **Customer Ops** | Production | Reader | Read-only access to flag status for triage. Cannot modify. |

**Quarterly Access Review:** The CISO (Rachel Kim) and VP of Engineering (David Park) will review LaunchDarkly user access lists every quarter against active HR records.

### 6.2 Segregation of Duties
The standard SDLC requires a Pull Request for the code, but a separate approved Jira ticket for the configuration change in LaunchDarkly. This binary artifact (code) vs. configuration (flag) split ensures that a single compromised developer account cannot unilaterally introduce and activate malicious code.

### 6.3 Immutable Audit Trail (SOC 2 Control 8.1 c & e)
LaunchDarkly is configured to stream all audit events to Splunk via the Event Relay in real-time. The following events are classified as High Severity in Splunk and trigger immediate alerts to the SOC:
- `featureflag.changed` (Production Environment)
- `featureflag.deleted` (Production Environment)
- `role.permissions.updated`
- `featureflag.evaluation.mismatch` (when SDK returns an unexpected default value)

Audit logs are retained in a Write-Once-Read-Many (WORM) compliant Amazon S3 bucket for 7 years to meet compliance requirements with HIPAA and FDA’s 21 CFR Part 820 for Design History Files.

### 6.4 Testing Controls
Prior to production activation, QA must execute the "Toggle Testing Matrix" in a staging environment:
1.  **Test State A (Flag OFF):** Validation that baseline functionality remains untouched.
2.  **Test State B (Flag ON):** Validation that new functionality works.
3.  **Test Toggle Ramp:** Validation that switching back to OFF (Rollback) does not corrupt data.
4.  **Test Target Unmatched:** Validation that unmapped users (null user keys) receive the default `False` variation.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
The SRE and QA teams track the following metrics via a centralized Datadog dashboard titled **"Feature Flag Health & Hygiene"**:

| Metric | Target | Measurement Method |
| :--- | :--- | :--- |
| **Mean Time to Cleanup (MTTC)** | < 14 days after roll-out to 100% | Jira timestamp (Status: Done minus Status: Pending Cleanup) |
| **Stale Flag Ratio** | 0 in Production | LaunchDarkly Code References + ERD Overdue Report |
| **Flag-Related Incidents** | 0 Sev1/2 incidents per month | PagerDuty incident tagging (#feature-flag) |
| **Audit Event Loss Rate** | < 0.01% | Reconciliation between LaunchDarkly Event Stream and Splunk Index |

### 7.2 Reporting Cadence
- **Daily:** Automated Slack digest to the `#eng-flag-bot` channel listing flags approaching their ERD (7-day warning).
- **Weekly:** Engineering Managers review the "Flag Bloat" report during the sprint review.
- **Monthly:** The VP of Engineering reviews the Feature Flag Hygiene Dashboard with the CTO and CISO. This review is documented as part of the SOC 2 Management Review evidence package.
- **Quarterly:** The AI Governance Committee reviews all long-lived permission toggles to ensure they remain necessary and compliant with the EU AI Act.

## 8. Exception Handling and Escalation

### 8.1 Flag Exception Request
Requests for deviations from this SOP (e.g., a permission flag expected to live longer than 12 months, or a kill switch needed without a matching Jira ticket in an emergency) must be submitted via the `[SOP-PENG-007] Exception Request` form in Jira Service Management (JSM).

**Approval Escalation Path:**
- **Level 1 (Standard Exceptions):** Approval by VP of Engineering (David Park).
- **Level 2 (Regulated Exceptions crossing finance/clinical streams):** Co-approval by VP of Engineering and Chief Compliance Officer (Thomas Anderson), with notification to the Chief AI Officer (Dr. Marcus Rivera).

### 8.2 Emergency Dispensation
In the event of a production outage (Sev1), the SRE Incident Commander is authorized to bypass the standard 4-stage rollout procedure to toggle a kill switch for the duration of the incident. A retrospective exception request must be filed within the next business cycle (24 hours). Failure to file the retro will trigger the "Audit Exception" count on the monthly KPIs.

## 9. Training Requirements

### 9.1 Mandatory Training
All personnel within the Product & Engineering division must complete the following:

| Training Module | Assigned To | Frequency | Platform |
| :--- | :--- | :--- | :--- |
| **SOP-PENG-007 Awareness** | All Engineers, SRE, QA, Product | Annually (Q1) | Docebo (LMS) |
| **LaunchDarkly Power User** | SRE, Engineering Managers | Annually | LaunchDarkly Academy + Practical Lab |
| **EU AI Act & Clinical Switches** | Clinical AI Platform Engineers | Semi-Annually | In-person lecture by Chief Medical Officer (Dr. Priya Patel) |
| **SR 11-7 Model Risk Refresher** | HealthPay Engineers | Annually | Online module provided by General Counsel (Maria Gonzalez) |

### 9.2 Training Compliance
The Chief Human Resources Officer (Jennifer Walsh) is responsible for tracking completion rates. 100% completion is required for any engineer prior to gaining deployment access. Non-compliance for 30+ days post-deadline will result in revocation of write-access to production systems until remediated.

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Document Name | Relationship |
| :--- | :--- | :--- |
| SOP-ISMS-010 | Production Change Management | Parent policy governing all production changes, including flag-driven releases. |
| SOP-ISMS-012 | Configuration and Secrets Management | Defines management of static config vs. dynamic flags. |
| SOP-ISMS-014 | Critical Incident Response | Defines the Sev1 response process referenced by emergency kill switches. |
| SOP-PENG-001 | Source Code Management | Governs the GitHub branching strategy and pre-receive hooks. |
| SOP-CLIN-001 | AI Model Deployment and Rollback | Specific rollback procedures for EU AI Act Annex III models. |
| SOP-FIN-002 | HealthPay Lending Model Governance | SR 11-7 risk management framework for financial models. |

### 10.2 External Standards

| Standard | Reference Section | Relevance |
| :--- | :--- | :--- |
| **SOC 2 (2024 TSC)** | CC8.1 Change Management & CC7.1 Detection of Anomalies | Central control objective for this SOP. |
| **EU AI Act** | Article 26 (Obligations of deployers) & Article 18 (Technical documentation) | Required for traceability of changes to high-risk AI systems. |
| **SR 11-7** | Attachment A: Model Development, Implementation, and Use | Applies to flags altering financial models. |
| **NIST AI RMF** | MAP 4.2: Evaluate & Prioritize Risks | Framework used for the Enhanced Risk Assessment procedure. |

## 11. Revision History

| Version | Date | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2021-01-15 | David Park | Initial SOP release, foundational LaunchDarkly governance. |
| 1.5 | 2022-06-10 | Sarah Jenkins (SRE) | Added Circuit Breaker section (Ops toggles) and Datadog integration specs. |
| 2.0 | 2023-11-01 | David Park | Major revision: Mandated Flag ERD (Expected Retirement Date), defined Stale Flag Escalation. |
| 2.4 | 2024-08-20 | Dr. Marcus Rivera | Updated per EU AI Act readiness: Added Enhanced Scrutiny procedures for Clinical AI and the regulated-model tag. |
| 2.6 | 2025-03-08 | David Park, Dr. Klaus Weber | SOC 2 Type II 2025 annual review. Updated access control matrix to align with Okta RBAC changes. Added "Zero Stale Flags" KPI for management review. |

## Appendix A: Regulated Model Toggle Risk Assessment (Template)

This form must be completed in Jira and approved before the flag targeting expands beyond employees.

- **Flag Key:** `[pay/clinicai]-[service]-[feature]`
- **Model Affected:** (Link to Model Card in MLflow)
- **Regulation Triggered:** [EU AI Act / SR 11-7 / FDA 510(k)]
- **Change Description:** (Qualitative description of the algorithmic change)
- **Behavioral Impact Analysis:** If the flag is ON, what human oversight is present? How does this alter the clinician’s or credit officer’s workflow?
- **Rollback Procedure:** How is a corrupted state reversed? (Flag OFF only, or data migration script needed?)
- **Risk Owner Sign-Off:** *[Name / Email]*