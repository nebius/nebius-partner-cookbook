---
sop_id: "SOP-PENG-019"
title: "Platform Reliability Engineering"
business_unit: "Product & Engineering"
version: "2.2"
effective_date: "2025-03-04"
last_reviewed: "2026-10-25"
next_review: "2027-04-15"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Platform Reliability Engineering

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, principles, and operational practices for ensuring the reliability, availability, and performance of the Meridian Health Technologies, Inc. (“Meridian”) platform ecosystem. The Platform Reliability Engineering (PRE) function integrates software engineering, systems engineering, and data-driven operational practices to build and maintain trust in Meridian’s critical healthcare and financial services products.

This SOP defines how Meridian:
- Defines, measures, and enforces service level objectives (SLOs) for all production services.
- Manages operational risk through error budget policies and progressive delivery techniques.
- Conducts structured, blameless incident response and post-incident analysis.
- Continuously validates system resilience through controlled chaos engineering experiments.
- Aligns reliability practices with SOC 2, HIPAA, SR 11-7, and the EU AI Act obligations.

### 1.2 Scope

This SOP applies to all production systems, services, and data pipelines supporting Meridian’s four business lines:

| Business Line | In-Scope Systems | Key Reliability Implications |
|---|---|---|
| Clinical AI Platform | Inference APIs, model serving infrastructure, diagnostic imaging pipelines, risk scoring engines | EU AI Act high-risk classification; patient safety impact |
| HealthPay Financial Services | Payment processing gateways, medical lending platforms, claims automation, fraud detection models | SR 11-7 model risk management; financial transaction integrity |
| MedInsight Analytics | Population health data pipelines, care gap identification engines, outcomes prediction services | PHI processing at scale; data freshness SLAs |
| Meridian SaaS Platform | Multi-tenant AWS infrastructure (us-east-1, eu-west-1), authentication services, API gateway, data storage layers | SOC 2 Type II scope; foundational dependency for all products |

**In scope:** All production environments, staging environments used for reliability testing, CI/CD pipelines, observability tooling, incident management processes, and reliability governance structures.

**Out of scope:** Development sandboxes, employee productivity tools not customer-facing, internal IT systems managed by IT Operations under SOP-ITOPS-042.

### 1.3 Applicability

This SOP applies to all personnel responsible for designing, deploying, operating, or managing Meridian platform services, including:
- Product & Engineering employees and contractors
- Site Reliability Engineering (SRE) team members
- Platform Engineering team members
- Clinical AI Platform engineers
- HealthPay engineering personnel
- MedInsight Analytics engineers
- Information Security personnel involved in incident response
- IT Operations personnel managing AWS/Azure infrastructure

Compliance with this SOP is mandatory for all in-scope personnel. Non-compliance shall be addressed per the disciplinary process defined in the Meridian Employee Handbook and SOP-HR-011.

---

## 2. Definitions and Acronyms

### 2.1 Key Definitions

| Term | Definition |
|---|---|
| **Service Level Indicator (SLI)** | A carefully defined quantitative measure of some aspect of the level of service provided. SLIs are the metrics that matter most to users and are measured from the perspective of the consumer of the service. |
| **Service Level Objective (SLO)** | A target value or range of values for a service level that is measured by an SLI. SLOs define the acceptable reliability threshold for a service over a measurement window. |
| **Service Level Agreement (SLA)** | A contractual obligation with customers that specifies the availability, performance, or responsiveness commitments Meridian makes, including financial or contractual remedies for breaches. |
| **Error Budget** | The maximum amount of time a service can fail to meet its SLO before consequences are triggered. Calculated as: `Error Budget = (1 − SLO) × Measurement Window`. |
| **Error Budget Policy** | A governance mechanism that specifies how error budget consumption triggers actions: freezing feature launches, prioritizing reliability work, or escalating to leadership. |
| **Chaos Engineering** | The discipline of experimenting on a distributed system to build confidence in the system's capability to withstand turbulent conditions in production. All experiments follow a hypothesis-driven methodology. |
| **Game Day** | A scheduled, facilitated exercise where teams simulate large-scale failure scenarios to validate incident response procedures, observability, and recovery mechanisms. |
| **Incident** | An unplanned interruption to a service or reduction in the quality of service that is detectable by monitoring, alerting, or user reports. |
| **Major Incident** | An incident that meets criteria for severity level 1 (SEV1) or severity level 2 (SEV2), involving customer-facing impact, data integrity concerns, or regulatory breach potential. |
| **Blameless Postmortem** | A structured, written analysis of an incident conducted with the explicit principle of focusing on systemic causes—not individual actions—to drive improvement. No individual assignment of fault is permitted. |
| **Recovery Time Objective (RTO)** | The targeted duration of time within which a service must be restored after a disruption. |
| **Recovery Point Objective (RPO)** | The maximum targeted period in which data might be lost due to a major incident. |
| **Canary Deployment** | A deployment strategy where a new version of a service is rolled out to a small subset of users or traffic before being promoted to the full production population. |
| **Progressive Delivery** | An umbrella term for deployment strategies—including canary releases, blue-green deployments, and feature flags—that limit the blast radius of changes by incrementally increasing exposure. |
| **Runbook** | A documented, tested, and executable set of operational procedures that guide responders through detection, mitigation, and resolution of known failure modes. |

### 2.2 Acronyms

| Acronym | Expansion |
|---|---|
| SLO | Service Level Objective |
| SLI | Service Level Indicator |
| SLA | Service Level Agreement |
| PRE | Platform Reliability Engineering |
| SRE | Site Reliability Engineering |
| IMOC | Incident Management On-Call |
| EOC | Emergency Operations Center |
| RC | Root Cause (per postmortem taxonomy; used as a descriptor only, not a single cause attribution) |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| MTTR | Mean Time to Resolve |
| MTTD | Mean Time to Detect |
| SEV | Severity Level |
| IaC | Infrastructure as Code |
| EBP | Error Budget Policy |
| CE | Chaos Engineering |
| BCP | Business Continuity Plan (see SOP-BCP-003) |
| DR | Disaster Recovery |

---

## 3. Roles and Responsibilities

The following RACI matrix defines accountability, responsibility, consultation, and information roles for Platform Reliability Engineering activities.

**Legend:**  
- **R** = Responsible (performs the work)  
- **A** = Accountable (signs off, owns outcome)  
- **C** = Consulted (provides input)  
- **I** = Informed (receives output)

| Activity / Deliverable | VP of Engineering (David Park) | SRE Team Lead | Service Team Lead | CISO (Rachel Kim) | CCO (Thomas Anderson) | VP Product Line | Engineering Team |
|---|---|---|---|---|---|---|---|
| SLO Definition & Approval | A | R | R | C | C | C | I |
| SLI Instrumentation | I | A | R | C | I | I | R |
| Error Budget Governance | A | R | R | I | C | I | I |
| Incident Response (SEV1/SEV2) | I | A | R | C | I | I | R |
| Blameless Postmortem Authoring | I | A | R | I | I | I | R |
| Postmortem Review & Acceptance | A | R | R | C | I | C | I |
| Chaos Engineering Approval | A | R | C | C | I | C | R |
| Game Day Execution | I | A | R | C | I | C | R |
| Observability Architecture | A | R | R | C | I | I | R |
| Capacity Planning | A | R | C | I | I | I | R |

### 3.1 Specific Role Descriptions

**VP of Engineering (David Park):** Serves as the executive sponsor for platform reliability. Holds ultimate accountability for SLO attainment, error budget governance, and reliability investment prioritization. Approves SLO changes, error budget policy modifications, and chaos experiment scopes that may impact production customer traffic. Chairs the quarterly Reliability Review.

**SRE Team Lead:** Owns the PRE program and this SOP. Responsible for operationalizing SLO frameworks, maintaining observability platforms (Datadog, PagerDuty, LangSmith), facilitating postmortems, managing the incident on-call rotation, and driving reliability improvement initiatives. Acts as incident commander for all SEV1 incidents until relieved.

**Service Team Lead (per product area):** Accountable for service-specific reliability, including SLO compliance, error budget adherence, postmortem action item completion, and runbook accuracy. Must approve all production deployments per SOP-CICD-008.

**Chief Information Security Officer (Rachel Kim):** Consulted on all incidents involving potential security events, data exfiltration, or access control anomalies. Co-approves chaos experiments with security implications. Owns the security incident response playbook (see SOP-IS-015).

**Chief Compliance Officer (Thomas Anderson):** Informed of any incident with regulatory reporting obligations (HIPAA breach notification, GDPR Article 33/34, EU AI Act serious incident reporting). Consulted on SLO definitions that map to customer SLA commitments.

**VP Product Line:** Consulted during SLO definition to ensure alignment with customer expectations and contractual commitments. Informed of error budget exhaustion events that delay feature delivery.

**Engineering Team Members:** Execute technical reliability work: instrumenting SLIs, responding to pages, writing postmortems, implementing remediation items, designing and running chaos experiments, and maintaining runbooks.

---

## 4. Policy Statements

### 4.1 General Reliability Principles

Meridian commits to the following reliability engineering principles:

1. **Reliability is a Feature:** Service reliability is a first-class product requirement, not an operational afterthought. Reliability targets are defined before features are launched and are continuously measured throughout a service's lifecycle.

2. **Data-Driven Operations:** All operational decisions—from SLO targets to error budget burn-down rates to chaos experiment scope—shall be grounded in empirical measurement, not intuition or anecdote.

3. **Blameless Culture:** Meridian operates a blameless post-incident analysis culture. Incidents are understood as emergent properties of complex socio-technical systems. Postmortems shall identify contributing factors across process, tooling, system design, and organizational context—not assign individual fault.

4. **Progressive Delivery:** All changes to production systems shall employ progressive delivery techniques—canary releases, blue-green deployments, or feature flags—to minimize change-induced incident risk and blast radius.

5. **Error Budgets as Decision Framework:** Error budgets govern the tension between feature velocity and reliability investment. When error budgets are exhausted or critically low, feature delivery must be paused in favor of reliability improvements.

6. **Reliability Shared Responsibility:** While SRE provides reliability tooling and frameworks, each service team is responsible for the reliability of the services they own. Reliability is never outsourced to a central team.

### 4.2 SLO and Error Budget Policy

All production services carrying customer-facing traffic, processing PHI, or handling financial transactions shall have:

- A minimum of two (2) SLIs defined and instrumented.
- A documented, achievable SLO for each SLI over a rolling 28-day measurement window.
- An error budget policy that triggers progressive actions at 50%, 75%, and 100% budget consumption thresholds.
- A quarterly SLO review to determine if targets remain appropriate given evolving customer expectations and system capabilities.

**Default SLOs by Criticality Tier:**

| Criticality Tier | Example Services | Default Availability SLO | Default Latency SLO (p99) |
|---|---|---|---|
| Tier 1 — Critical | Payment processing, Clinical inference API, Auth service | 99.95% | ≤ 500ms |
| Tier 2 — High | Claims automation, Population health dashboards | 99.9% | ≤ 1000ms |
| Tier 3 — Standard | Reporting services, Internal tooling APIs | 99.5% | ≤ 2000ms |

Tier classifications shall be reviewed and approved by the service team lead and VP of Engineering during the service onboarding process and at each quarterly SLO review.

### 4.3 Incident Management Policy

- All incidents with customer-facing impact shall be declared and managed through the defined severity framework within 5 minutes of initial detection.
- SEV1 incidents require page-out and assembly of the incident response team within 15 minutes.
- Incident Commanders shall be drawn from a trained pool of SRE and senior engineering staff. No person shall serve as Incident Commander without completing MER-PRE-101 training.
- All major incidents (SEV1, SEV2) require a written, blameless postmortem completed within 5 business days of incident resolution.
- Postmortem action items shall be tracked to completion in Meridian's work tracking system (Jira) with a maximum allowed open duration of 90 days unless a risk exception is approved.

### 4.4 Chaos Engineering Policy

- Chaos experiments in production environments may only be conducted after written approval from the VP of Engineering and CISO (for security-relevant experiments).
- All chaos experiments must follow the Chaos Experiment Protocol detailed in Section 5.6.
- Experiments shall be conducted during business hours with the full experiment team present unless a specific overnight window is approved for critical-path testing.
- No chaos experiment may be run against Tier 1 Critical services during the last 5 business days of any fiscal quarter or during calendar year-end processing periods (December 15–January 5 for HealthPay systems).
- All experiments must include a pre-declared abort condition and rollback plan.

### 4.5 Regulatory Alignment

- Platform reliability practices shall support SOC 2 Common Criteria for Availability (CC5.1–CC5.3). Availability commitments are maintained per customer contracts, with monitoring and incident response procedures designed to detect and remediate availability degradation. Customer availability commitments are documented in individual service agreements.
- For EU AI Act compliance, any incident affecting the accuracy, reliability, or availability of high-risk AI systems (Clinical AI Platform) that could present a risk to health, safety, or fundamental rights shall be reported per the serious incident reporting protocol in SOP-AI-017.
- For SR 11-7 alignment, HealthPay model-serving infrastructure reliability incidents and error budget consumption shall be reported to the AI Governance Committee quarterly, as model availability directly impacts model risk.

---

## 5. Detailed Procedures

### 5.1 Service Level Indicator (SLI) Definition and Instrumentation

All service teams shall follow this procedure to define, instrument, and maintain SLIs for their services.

#### 5.1.1 SLI Identification Workshop

1. The service team lead schedules a 2-hour SLI identification workshop with the SRE team lead, product manager, and at least two senior engineers from the service team.
2. Using the workshop template (Appendix A: SLI Definition Canvas), the team identifies:
   - **User journeys** served by the system and their criticality.
   - **Key metrics** from the user's perspective, not the system's internal view.
   - **Measurement boundaries** (what is included and excluded from the SLI).
3. The team categorizes candidate SLIs by the "VALET" framework:
   - **V**olume: Throughput, requests per second.
   - **A**vailability: Uptime, successful response rate.
   - **L**atency: Response time distribution (p50, p95, p99).
   - **E**rrors: Error rate categorized by error class.
   - **T**ickets: Customer support tickets generated.

#### 5.1.2 SLI Instrumentation Implementation

1. Engineering team implements measurement instrumentation using Datadog custom metrics, APM traces, and synthetic monitoring checks as applicable.
2. For each SLI, the team configures:
   - **Data source:** (Datadog APM, CloudWatch, ping checks, application logs, etc.)
   - **Aggregation method:** (Average, percentile, ratio, count per window)
   - **Measurement interval:** (Default: 1 minute)
   - **Query logic** used to compute the SLI from raw data.
3. SRE team lead validates that SLI instrumentation correctly represents user experience by running a 7-day soak period comparing SLI values against independent observations.
4. SLI definitions are registered in the Meridian Service Catalog (Backstage) with the following metadata:
   - SLI name and unique identifier
   - Owning team
   - Criticality tier
   - Measurement query
   - Associated SLO(s)
   - Last validated date

#### 5.1.3 SLI Validation Cadence

1. Every calendar quarter, service team lead reviews active SLIs to ensure they remain representative of user experience.
2. Changes to SLI definitions require SRE team lead approval and are logged in the Meridian Service Catalog with a revision note.
3. Retired SLIs shall be marked as deprecated in the Service Catalog but retained for historical reporting purposes for a minimum of 12 months.

### 5.2 Service Level Objective (SLO) Definition and Governance

#### 5.2.1 SLO Definition Procedure

1. For each active SLI, the service team lead and SRE team lead jointly propose an SLO target value for a rolling 28-day measurement window.
2. The SLO target must be consistent with the minimum thresholds defined by the Criticality Tier table in Section 4.2.
3. The proposal is documented in the SLO Approval Form (Appendix B) and includes:
   - SLI identifier
   - Proposed SLO value (e.g., "99.9% availability")
   - Measurement window (always 28 days rolling for standard SLOs)
   - Error budget calculation: `Error Budget (minutes) = (1 − SLO) × 28 days × 24 hours × 60 minutes`
   - Customer SLA mapping (if applicable)
4. VP of Engineering and VP Product Line review and approve the SLO within 10 business days of submission.
5. Upon approval, SLO is configured as an alert threshold in Datadog and linked to the relevant PagerDuty service.
6. SLOs are publicly displayed on the Meridian Reliability Dashboard (accessible to all Product & Engineering staff) and linked from the Backstage Service Catalog.

#### 5.2.2 Quarterly SLO Review

1. During the first week of each calendar quarter, SRE team lead exports the previous quarter's SLO attainment data for all Tier 1 and Tier 2 services.
2. Service team lead schedules a 1-hour SLO review meeting with SRE team lead to assess:
   - Actual SLO attainment vs. target.
   - Error budget consumption trends.
   - Whether the SLO target remains appropriate given product evolution.
3. Recommended SLO adjustments are documented and submitted per the SLO Definition Procedure (Section 5.2.1).
4. No SLO shall be loosened (i.e., made less stringent) without:
   - Written justification, including customer impact analysis.
   - VP of Engineering approval.
   - 30-day notice to affected customers if the SLO maps to an SLA.

### 5.3 Error Budget Governance

#### 5.3.1 Error Budget Calculation and Monitoring

1. Error budget is calculated automatically by the Datadog SLO monitoring module for each active SLO.
2. The calculation follows Meridian's standard formula:  
   `Remaining Error Budget (%) = 100 × (1 − (Compliance Period Bad Minutes / (Compliance Period Total Minutes × (1 − SLO))))`
3. SRE team maintains a centralized error budget dashboard showing current burn status for all Tier 1 and Tier 2 services.

#### 5.3.2 Error Budget Policy (EBP) Threshold Actions

The following progressive actions shall be automatically communicated via PagerDuty notification and documented in the quarterly Reliability Review:

| Burn Threshold | Trigger Action | Responsible Role |
|---|---|---|
| **50% consumed** within 28-day window or projected exhaustion within 14 days | SRE team lead notifies service team lead; voluntary feature freeze on non-urgent deployments; reliability backlog items prioritized | Service Team Lead |
| **75% consumed** within 28-day window | Mandatory freeze on all feature deployments; service team dedicates minimum 50% of sprint capacity to reliability backlog items; VP of Engineering notified | VP of Engineering |
| **100% consumed** (error budget exhausted) | Immediate feature freeze for remainder of measurement window; 100% of service team capacity redirected to reliability backlog until budget recovers above 50%; executive escalation to CEO; applicable SLA customer notifications per contractual obligations | VP of Engineering & VP Product Line |

#### 5.3.3 Error Budget Override

1. The VP of Engineering may authorize a one-time override to continue feature deployments during error budget exhaustion under the following conditions:
   - Override is justified by a documented critical business need (e.g., regulatory mandate, critical customer commitment, patient safety enhancement).
   - Override is time-bound (maximum: 14 days).
   - Override requires co-approval from the Chief Compliance Officer if the system processes PHI or financial data.
2. All overrides are logged in the Exception Register (Appendix C) and reviewed at the next Reliability Review.
3. No more than two (2) overrides per service per calendar year are permitted.

### 5.4 Incident Management

#### 5.4.1 Severity Classification

All incidents shall be classified within 5 minutes of declaration per the following matrix:

| Severity | Definition | Examples | Response |
|---|---|---|---|
| **SEV1** | Complete outage or severe degradation of Tier 1 service(s); customer-facing impact; potential PHI exposure or financial transaction failure; data loss | Payment processing offline, Inference API returning 5xx errors for all requests | Page-out; assemble IMOC within 15 min; EOC channel opened in Slack (#incident-sev1); CEO notification within 30 min |
| **SEV2** | Degraded functionality of Tier 1 or outage of Tier 2 service(s); significant latency; non-critical customer impact; error budget burn acceleration | MedInsight dashboards loading >30 seconds, claims processing delayed, synthetic checks failing intermittently | Page-out; IMOC assembled within 30 min; VP of Engineering notified |
| **SEV3** | Minor service degradation; limited customer impact; Tier 3 service issues | Internal tooling unavailable, non-production environment issues affecting release pipeline | Create Jira issue; addressed within business hours; no page-out |
| **SEV4** | No customer impact; informational | Cosmetic UI bug, low-priority log anomaly | Jira backlog; no immediate action |

#### 5.4.2 SEV1 Incident Response Procedure

**Step 1: Detection and Declaration (Target: ≤ 5 minutes from detection)**
1. Monitoring system (Datadog) triggers PagerDuty alerting the primary on-call SRE.
2. On-call SRE acknowledges page within 2 minutes and performs initial triage using the Incident Triage Runbook (Appendix D).
3. If triage confirms Tier 1 service disruption criteria, on-call SRE declares SEV1 by typing `/incident declare sev1` in the Slack #incident-response channel, which triggers a PagerDuty page-out to the full IMOC roster.

**Step 2: IMOC Assembly (Target: ≤ 15 minutes from page-out)**
1. Incident Commander (IC) is the SRE team lead or, if unavailable, the most senior SRE on-call.
2. The IC opens the Emergency Operations Center (EOC) virtual war room — Google Meet link published in #incident-response.
3. The following roles shall be filled:
   - **Incident Commander (IC):** Runs the incident, delegates tasks, maintains timeline.
   - **Operations Lead (OL):** Executes diagnostic commands, applies mitigations, restarts services.
   - **Communications Lead (CL):** Manages stakeholder updates, customer communications, external notifications.
   - **Scribe:** Maintains the incident timeline document (shared Google Doc, template at Appendix E).
4. IC confirms quorum: at minimum, IC + OL must be present. If key roles are unfilled after 15 minutes, IC escalates to VP of Engineering.

**Step 3: Mitigation (No time limit; execution is continuous until service restored)**
1. IC establishes the incident timeline and logs all actions in the shared timeline document.
2. OL follows the relevant runbook. If no runbook matches the failure mode, OL performs systematic diagnostic procedures:
   - **Observability:** Check Datadog dashboards for correlated anomalies.
   - **Recent Changes:** Review deployment logs for last 24 hours (SOP-CICD-008 mandates deployment changelog).
   - **Infrastructure:** Run `terraform plan` on affected environment to detect configuration drift.
   - **Dependencies:** Check status of upstream services (auth, database, networking).
3. IC enforces the 30-minute update cadence: CL posts status to #incident-sev1 Slack channel every 30 minutes.
4. If mitigation is not achieved within 60 minutes, IC escalates to VP of Engineering to summon additional resources.
5. No root cause analysis is conducted during the incident; focus is exclusively on restoring service.

**Step 4: Resolution and Verification**
1. OL declares service restored when monitoring shows SLIs returning to normal ranges for 5 consecutive minutes.
2. IC verifies restoration by confirming with the CL that customer-facing symptoms have ceased.
3. IC announces incident resolution in #incident-response and closes the EOC.
4. IC sets a 24-hour "incident watch" status in the monitoring system, during which alert thresholds are tightened for the affected service.

**Step 5: Post-Incident**
1. Within 24 hours, IC assigns a Postmortem Owner (any engineer who participated in the response; not the IC).
2. IC schedules the postmortem review meeting for within 5 business days.

#### 5.4.3 Blameless Postmortem Procedure

**Step 1: Drafting (Completed ≤ 3 business days post-resolution)**
1. Postmortem Owner authors the postmortem using the Postmortem Template (Appendix F).
2. The postmortem must include:
   - **Incident Summary:** Date, duration, severity, services affected, customers impacted.
   - **Detection:** How the incident was discovered (monitoring alert, user report, etc.) and MTTD.
   - **Response:** Timeline of key actions from detection to resolution, reconstructed from the incident timeline document, Slack logs, and PagerDuty records.
   - **Contributing Factors:** A structured analysis of system conditions that contributed to the incident. The Contributing Factor taxonomy includes:
     - Process/Procedure gaps
     - System Design/Architecture limitations
     - Observability/Monitoring gaps
     - Testing/Validation gaps
     - Deployment/Change management issues
     - External dependency failures
     - Human factors (cognitive load, tooling usability, training gaps — described contextually, never as "person made a mistake")
   - **Impact:** Quantified where possible (number of users, transactions lost, error budget consumed).
   - **Mitigations Applied During Incident:** What was done; whether it was effective.
   - **Action Items:** Specific, assignable, time-bound improvements. Each action item must reference a contributing factor. Each action item must have a single assignee and a due date ≤ 90 days from postmortem acceptance unless exception-approved.

**Step 2: Review (Completed ≤ 5 business days post-resolution)**
1. Postmortem Owner schedules a 60-minute postmortem review meeting. Required attendees:
   - All engineers who participated in the incident response.
   - SRE team lead.
   - Service team lead.
   - CISO representative (if security-relevant incident).
2. During the meeting, Postmortem Owner presents the postmortem and facilitates discussion. The tone is explicitly blameless; the meeting facilitator shall intervene if blame language is used.
3. The group ratifies action items and due dates.

**Step 3: Acceptance and Distribution**
1. Postmortem is published to the Meridian Postmortem Register (Confluence space, access-restricted to Product & Engineering personnel).
2. Action items are created as Jira tasks linked to the postmortem document.
3. A summary (excluding sensitive details) is shared in the #eng-all Slack channel within 1 business day of postmortem acceptance.

**Step 4: Action Item Tracking**
1. The SRE team lead reviews open postmortem action items monthly. Items past due without a risk exception are escalated to VP of Engineering.
2. Postmortem action item completion rate is a KPI tracked per Section 7.

### 5.5 Progressive Delivery Controls

All production deployments shall employ progressive delivery mechanisms to limit the blast radius of defective changes. This procedure defines the standard deployment promotion pipeline.

#### 5.5.1 Canary Deployment Procedure

1. Service team creates a deployment artifact and deploys to the **staging** environment. A suite of integration tests and reliability smoke tests must pass before promotion.
2. Upon staging validation, the service team deploys to the **canary** production subset. The canary receives 5% of production traffic for a minimum observation period:
   - Tier 1 services: 30 minutes
   - Tier 2 services: 15 minutes
   - Tier 3 services: 5 minutes
3. During the canary observation period, the service team monitors:
   - Error rate vs. canary baseline (previous stable version).
   - Latency distribution (p50, p95, p99) vs. baseline.
   - Error budget burn rate — any statistically significant acceleration triggers automatic canary abort.
4. If no anomalies are detected, canary is promoted to full production (100% traffic).
5. Canary deployment metadata is logged in the deployment changelog (automated via CI/CD pipeline integration with Datadog event API).

#### 5.5.2 Feature Flag Governance

1. All feature flags in production shall use the Meridian feature flag platform (LaunchDarkly enterprise tier).
2. Feature flags must have:
   - A named owner (engineer responsible for flag hygiene).
   - A target removal date (maximum: 60 days post-launch unless a permanent operational flag is approved by the service team lead).
   - A kill-switch mechanism accessible to SRE on-call without code changes.
3. Flag removal backlog is reviewed quarterly by the SRE team lead. Flags past their removal date are flagged to the owner; if unresolved within 14 days, they are escalated to VP of Engineering.

### 5.6 Chaos Engineering Protocol

This protocol governs all chaos engineering experiments conducted in Meridian production or staging environments.

#### 5.6.1 Experiment Design Phase

1. The experiment proposer (any engineer) completes the Chaos Experiment Proposal (Appendix G), including:
   - **Hypothesis:** A specific, testable statement. Example: "If the primary read replica of the Aurora cluster is terminated, the application will automatically fail over to the secondary replica within 30 seconds and user-facing latency will remain below the p99 SLO threshold."
   - **System Under Test:** Specific services, components, and dependencies.
   - **Experiment Type:** (e.g., resource stress, network partition, dependency failure, AZ failure simulation).
   - **Steady State Metrics:** Pre-experiment measurements establishing the normal operating baseline.
   - **Blast Radius:** Quantified scope of impact (e.g., "5% of traffic to the payment API in us-east-1").
   - **Abort Conditions:** Objective triggers requiring immediate experiment termination (e.g., "SEV1 alert fires, error budget burn rate exceeds 2x baseline, or p99 latency exceeds 2 seconds for 1 minute").
   - **Rollback Plan:** Step-by-step instructions to restore steady state.
   - **Timing:** Proposed date, time, expected duration (maximum experiment window: 2 hours).

#### 5.6.2 Experiment Approval

1. Experiment proposer submits the completed proposal to the SRE team lead for review at least 5 business days before the proposed experiment date.
2. SRE team lead evaluates:
   - Hypothesis clarity and testability.
   - Blast radius appropriateness (experiments must start with minimal blast radius and expand iteratively).
   - Abort condition sufficiency.
   - Conflict with other scheduled changes.
3. For experiments in production targeting Tier 1 or Tier 2 services, VP of Engineering approval is required.
4. For experiments with security implications (network segmentation, IAM policy changes, credential rotation), CISO consultation and approval is required.
5. Approved experiments are added to the Chaos Experiment Calendar, visible to all Product & Engineering.

#### 5.6.3 Experiment Execution

1. **Pre-flight Check (T-15 minutes):**
   - Experiment team (minimum: proposer, SRE team lead or delegate) verifies that all observability dashboards are functioning.
   - Abort command or kill-switch mechanism is tested (dry-run if possible).
   - Communication channel (#chaos-eng Slack channel) is opened and all relevant service teams are notified.
2. **Steady State Verification (T-5 minutes):**
   - Experiment team captures baseline SLI values and confirms system is operating within normal parameters.
3. **Experiment Initiation (T=0):**
   - Proposer introduces the failure condition per the experiment design.
4. **Continuous Monitoring:**
   - Team monitors Datadog dashboards, PagerDuty, and user-facing telemetry for the experiment duration.
   - IC for the experiment maintains a live timeline document.
5. **Abort or Completion:**
   - If any abort condition is met, the experiment is immediately terminated, rollback plan executed, and an incident is declared per Section 5.4.
   - If the experiment reaches its planned conclusion, the proposer verifies steady state is restored, then declares the experiment complete.

#### 5.6.4 Experiment Post-Analysis

1. Within 5 business days, the experiment proposer publishes a Chaos Experiment Report summarizing:
   - Hypothesis validation (proven, disproven, or inconclusive).
   - Observations and anomalies.
   - System weaknesses discovered.
   - Recommended reliability backlog items.
2. Discovered weaknesses that could lead to SEV1 incidents shall be added to the reliability backlog with Critical priority and tracked per Section 5.3 error budget governance.

### 5.7 Game Day Procedure

Game Days are larger-scale facilitated exercises simulating complex, cross-service failure scenarios. Game Days are mandatory for all Tier 1 and Tier 2 service teams and shall be conducted at least once per calendar year.

#### 5.7.1 Game Day Planning (8 weeks prior)

1. SRE team lead designates a Game Day Facilitator.
2. Facilitator forms a Game Day Planning Committee with representatives from all participating service teams, plus CISO and Compliance representation as needed.
3. The committee designs the Game Day scenario, which must:
   - Involve at least three (3) Meridian services.
   - Include a simulated failure injection (controlled by the Facilitator, not automated chaos tooling, to allow pacing and safe abort).
   - Exercise the incident response chain (detection → page → IMOC assembly → diagnosis → mitigation).
   - Have a "game clock" schedule not to exceed 4 hours.
4. VP of Engineering approves the scenario 4 weeks prior.

#### 5.7.2 Game Day Execution

1. All participants assemble in a designated space (physical or virtual war room).
2. Facilitator briefs participants on rules of engagement: no pre-staging of responses, all runbooks may be used, real observability tooling is exercised.
3. Facilitator injects the initial failure per the scenario script.
4. Response teams operate exactly as they would for a real incident.
5. Facilitator acts as the "voice of God," answering questions about system state that real operators would be able to determine.
6. Facilitator manages the game clock and may accelerate or decelerate to maintain scenario pace.
7. At scenario conclusion, Facilitator declares Game Day ended and leads an immediate "hot wash" debrief.

#### 5.7.3 Game Day Post-Analysis

1. Within 10 business days, the Facilitator publishes a Game Day Report summarizing:
   - Scenario narrative and timeline.
   - Performance against MTTD and MTTR targets.
   - Gaps identified in runbooks, observability, escalation paths, or team coordination.
   - Recommended improvements prioritized by severity.
2. All gaps rated "Critical" or "High" shall generate Jira action items owned by the relevant service team lead, tracked as reliability backlog items.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control | Implementation | Purpose |
|---|---|---|
| **Monitoring and Alerting** | Datadog APM, infrastructure monitoring, synthetic checks for all Tier 1 and Tier 2 endpoints; PagerDuty for alerting, escalation policies with 5-minute acknowledgment SLAs | Ensure rapid MTTD for all service degradations |
| **SLI/SLO Measurement** | Datadog SLO module querying APM metrics; Backstage Service Catalog integration for SLO definition registration | Ensure consistent, auditable reliability measurement per Section 5.1–5.2 |
| **Progressive Delivery** | LaunchDarkly feature flags, Argo Rollouts for canary deployments; CI/CD pipeline integration with Datadog for automated canary analysis | Limit blast radius of production changes per Section 5.5 |
| **Infrastructure as Code** | Terraform Enterprise for all AWS/Azure infrastructure; GitHub for IaC source with branch protection requiring peer review | Ensure reproducible, auditable infrastructure provisioning |
| **Secrets Management** | HashiCorp Vault for all service credentials, API keys, certificates; no secrets in source code or configuration files | Prevent credential exposure; support rotation during incidents |
| **Logical Access Controls** | AWS IAM roles per service, principle of least privilege; separate production and non-production AWS accounts; Okta SSO for human access, IAM roles for machine access | Enforce least-privilege access to production infrastructure |
| **Network Segmentation** | VPC isolation per environment (prod, staging, dev); security groups restricting inter-service communication to authorized ports only | Prevent lateral movement and unauthorized cross-environment access |
| **Audit Logging** | AWS CloudTrail enabled in all accounts; Datadog Log Management aggregating application logs; immutable log storage in S3 with versioning | Provide forensic evidence during post-incident analysis |
| **Runbook Management** | All runbooks stored in a versioned Git repository, rendered in Confluence; must include last-validated date; stale runbooks (>180 days without validation) flagged for review | Ensure incident responders have accurate, current procedures |

### 6.2 Administrative Controls

| Control | Implementation | Purpose |
|---|---|---|
| **On-Call Rotation** | PagerDuty schedules with mandatory primary/secondary; escalation chain defined per service; no individual on-call for >2 consecutive weeks | Prevent alert fatigue; maintain response readiness |
| **Deployment Freeze Windows** | All Tier 1 services: no non-emergency deployments during fiscal quarter-end close (last 5 business days of quarter), calendar year-end (December 15–January 5 for HealthPay), or during SEV1 incidents | Reduce change-induced risk during sensitive periods |
| **Change Advisory** | All Tier 1 production changes require peer review via pull request; changes during freeze windows require VP of Engineering approval | Ensure changes are reviewed and intentional |
| **Capacity Planning** | Monthly capacity review automated via Datadog forecasting dashboards; capacity alerts at 70% utilization; auto-scaling policies for compute | Prevent capacity-triggered incidents |
| **Access to Production** | Production access by engineering personnel is authenticated via Okta SSO with multi-factor authentication (MFA); access logged in CloudTrail; break-glass emergency accounts monitored with real-time alerting to CISO | Maintain auditable control over production changes |

### 6.3 Availability Commitments and Recovery Planning

Meridian maintains availability commitments to customers per contractual agreements and service-level objectives defined under Section 5.2. In the event of a service disruption, incident management procedures per Section 5.4 are invoked to restore service as rapidly as possible. Service teams shall maintain current runbooks describing restoration procedures for known failure modes.

System backups are managed per the Meridian Data Protection SOP (SOP-DP-012) and include the following retention and frequency standards:

| Data Class | Backup Frequency | Retention Period |
|---|---|---|
| PHI Data Stores (Aurora, RDS) | Continuous (point-in-time recovery) + daily snapshot | 30 days (snapshots), 7 days (transaction logs) |
| Financial Transaction Logs | Hourly | 90 days |
| Application Configuration (IaC state) | On every Terraform apply | Indefinite (versioned S3) |
| Observability Data (metrics, logs) | Streaming, no separate backup | 30 days (Datadog retention) |

Meridian's Business Continuity Plan (SOP-BCP-003) and Disaster Recovery procedures (SOP-DR-007) address major outage scenarios requiring full-site failover or recovery.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Reliability Metrics

The following metrics are tracked continuously and reported at cadences defined below.

| Metric | Definition | Target | Measurement Tool |
|---|---|---|---|
| **SLO Attainment** | Percentage of SLOs meeting target over rolling 28-day window | ≥95% of Tier 1 SLOs | Datadog SLO module |
| **Mean Time to Detect (MTTD)** | Time from incident start to first alert acknowledgment, measured across all SEV1/SEV2 incidents | ≤ 5 minutes for SEV1 | PagerDuty analytics |
| **Mean Time to Resolve (MTTR)** | Time from incident start to service restoration (not incident closure) | ≤ 60 minutes for SEV1 (average rolling 6-month) | PagerDuty + incident timeline docs |
| **Error Budget Consumption Rate** | Percentage of error budget consumed per week, aggregated by service tier | No Tier 1 service exceeding 25% burn per week | Datadog error budget dashboard |
| **Postmortem Action Item Completion** | Percentage of action items completed by due date | ≥ 90% | Jira filtered by `postmortem-action-item` label |
| **Change Failure Rate** | Percentage of production deployments causing service degradation (SEV2+) | ≤ 5% | CI/CD pipeline + incident register |
| **On-Call Alert Noise** | Ratio of actionable alerts to total alerts | ≥ 70% actionable | PagerDuty analytics |

### 7.2 Reliability Dashboards

The following dashboards shall be maintained and accessible to all Product & Engineering staff:

1. **Executive Reliability Dashboard:** SLO attainment, error budget status, and MTTR trends aggregated across all tiers. Updated live via Datadog dashboard; reviewed at quarterly Reliability Review.
2. **Service Reliability Dashboard:** Per-service SLI graphs, error budget burn-down charts, incident history. Available in Datadog per service.
3. **Incident Metrics Dashboard:** MTTD, MTTR, incident frequency, and postmortem action item tracking. Maintained by SRE team lead, reviewed monthly.

### 7.3 Reporting Cadence

| Report | Frequency | Audience | Owner |
|---|---|---|---|
| **Weekly On-Call Handoff** | Weekly (Monday, 10:00 EST) | SRE team, service team leads | SRE on-call engineer |
| **Monthly Reliability Report** | Monthly (first Friday) | VP of Engineering, service team leads, CISO | SRE team lead |
| **Quarterly Reliability Review** | Quarterly (second week of quarter) | CEO, VP of Engineering, VPs of Product Lines, CISO, CCO | David Park (VP of Engineering) |
| **Annual SOC 2 Reliability Assessment** | Annually (aligned with audit cycle) | External auditors, CISO, CCO | David Park & Thomas Anderson |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Procedure

Deviations from the requirements of this SOP require a formal Exception Request:

1. Requestor (service team lead or higher) completes the Exception Request Form (Appendix H), documenting:
   - SOP section from which exception is sought.
   - Specific requirement being excepted.
   - Justification (technical, business, or compliance rationale).
   - Proposed compensating controls to mitigate reliability risk.
   - Requested duration of exception (maximum: one quarter, renewable).
2. Exception Request is submitted to VP of Engineering (David Park) for review.
3. For exceptions impacting PHI-processing systems or financial systems, Chief Compliance Officer (Thomas Anderson) consultation is required.
4. VP of Engineering renders decision within 5 business days. All decisions are documented in the Exception Register maintained by the SRE team lead.
5. Approved exceptions are tracked with automatic expiration. The SRE team lead notifies the requestor 14 days prior to expiration. Extensions require a new Exception Request.

### 8.2 Escalation Path for Unresolved Reliability Issues

Any engineer observing a reliability risk that is not being addressed through normal channels may escalate per the following path:

1. **Service Team Lead** — First point of escalation for service-specific issues.
2. **SRE Team Lead** — For issues impacting multiple services or concerning observability/alerting gaps.
3. **VP of Engineering (David Park)** — For issues involving error budget exhaustion risk, deployment freeze violations, or unresolved postmortem action items.
4. **Chief Executive Officer (Dr. Sarah Chen)** — For issues presenting immediate patient safety, financial integrity, or regulatory compliance risk.

Escalation is considered a professional responsibility, not an adversarial act. Meridian policy prohibits retaliation for good-faith reliability escalations.

---

## 9. Training Requirements

### 9.1 Required Training Modules

| Training Module | Code | Audience | Frequency | Delivery Method |
|---|---|---|---|---|
| **Incident Commander Training** | MER-PRE-101 | All SRE team members, service team leads, any engineer on-call for Tier 1 services | Annual; required before first on-call shift | Instructor-led (SRE team lead); 4 hours |
| **Blameless Postmortem Facilitation** | MER-PRE-102 | All engineering managers, SRE team, any personnel who may author or review postmortems | Annual | E-learning module (LMS); 2 hours |
| **Chaos Engineering Certification** | MER-PRE-103 | Engineers authorized to design and execute chaos experiments | One-time, with annual refresher (1 hour) | Instructor-led + hands-on lab; 8 hours |
| **Observability and Alerting** | MER-PRE-104 | All Product & Engineering personnel | Onboarding, then annual refresher | E-learning (LMS); 1.5 hours |
| **PRE SOP Awareness** | MER-PRE-105 | All Product & Engineering personnel | Onboarding, then annual | E-learning (LMS); 1 hour |

### 9.2 Training Tracking and Compliance

1. All required training is tracked in Meridian's Learning Management System (LMS).
2. Service team leads are responsible for ensuring their team members complete required training by assigned due dates.
3. Non-completion of mandatory training by the due date shall result in temporary revocation of relevant access (e.g., PagerDuty responder role suspended if MER-PRE-101 not current).
4. SRE team lead reports quarterly training compliance rates in the Monthly Reliability Report.

---

## 10. Related Policies and References

### 10.1 Internal SOPs and Policies

| Reference | Title | Relationship |
|---|---|---|
| SOP-BCP-003 | Business Continuity Planning | Cross-reference for major outage recovery |
| SOP-DR-007 | Disaster Recovery Procedures | Cross-reference for region-level failover scenarios |
| SOP-CICD-008 | Continuous Integration and Delivery | Deployment pipeline controls referenced in Section 5.5 |
| SOP-IS-015 | Information Security Incident Response | Security-specific incident handling; consulted during incidents with security implications |
| SOP-AI-017 | AI System Incident Reporting | EU AI Act serious incident reporting for Clinical AI Platform incidents |
| SOP-DP-012 | Data Protection and Backup Policy | Backup management referenced in Section 6.3 |
| SOP-CHG-004 | Change Management | Production change approval alignment |
| SOP-HR-011 | Employee Disciplinary Procedures | Consequences of non-compliance |
| SOP-ITOPS-042 | IT Operations Management | Separates internal IT reliability from customer-facing platform reliability |
| SOP-MR-023 | Model Risk Management for HealthPay | SR 11-7 alignment for model-serving reliability |

### 10.2 Industry Standards and References

| Standard | Reference |
|---|---|
| Google SRE Book (Site Reliability Engineering) | Foundational SRE principles adapted for Meridian |
| SOC 2 Trust Services Criteria (CC5.1–CC5.3, Availability) | Control framework alignment |
| CHAOS Community | Chaos experiment design principles |
| AICPA TSP Section 100 | Basis for SOC 2 audit alignment |
| NIST SP 800-53 (IR-4: Incident Handling) | Incident management framework reference |
| ISO 22301:2019 (Business Continuity) | Business continuity alignment |

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2023-01-15 | David Park, VP of Engineering | Initial creation of Platform Reliability Engineering SOP. Established SLO framework, incident management, and basic chaos engineering governance. |
| 1.1 | 2023-06-22 | Sarah Lin, SRE Team Lead | Added Progressive Delivery controls (Section 5.5). Updated incident classification matrix to include SEV4. Revised training requirements to include MER-PRE-105. |
| 1.2 | 2024-01-10 | Marcus Okonkwo, SRE Engineer | Incorporated EU AI Act serious incident reporting alignment. Added Game Day procedure (Section 5.7). Updated chaos engineering protocol with CISO co-approval requirement for security-relevant experiments. |
| 2.0 | 2024-08-05 | Sarah Lin, SRE Team Lead | Major revision: restructured SLO framework with tier-based defaults; introduced quantitative error budget policy thresholds; updated Observability section to reflect Datadog migration; added Section 6.3 Availability Commitments and Recovery Planning. |
| 2.1 | 2025-01-17 | David Park, VP of Engineering | Post-audit revision: added Section 1.3 applicability statement; clarified logical access controls; updated reporting cadences for regulatory alignment; incorporated Compliance consultation for PHI/financial exception requests. |
| 2.2 | 2025-03-04 | David Park, VP of Engineering | Current version. Annual review completed. Updated role titles (Sarah Lin transitioned, SRE Team Lead role updated). Added quarterly SLO review procedure. Updated related policies references. No material threshold changes. Approved by Dr. Sarah Chen. |

---

*This document is classified as Internal. Distribution is limited to Meridian Health Technologies, Inc. personnel and authorized contractors under non-disclosure obligations. Unauthorized external distribution is prohibited per SOP-IS-020.*