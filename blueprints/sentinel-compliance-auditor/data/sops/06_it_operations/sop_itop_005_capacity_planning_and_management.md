---
sop_id: "SOP-ITOP-005"
title: "Capacity Planning and Management"
business_unit: "IT Operations & Infrastructure"
version: "4.7"
effective_date: "2024-05-13"
last_reviewed: "2025-12-15"
next_review: "2026-06-14"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Capacity Planning and Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, methodologies, roles, and responsibilities for Capacity Planning and Management across Meridian Health Technologies, Inc. The purpose of this SOP is to ensure that the IT infrastructure, platform services, and supporting technology ecosystems consistently meet the performance, availability, and scalability demands of the business while optimizing cost and resource utilization. This procedure ensures that services have the capacity to process current workloads and can scale to accommodate projected growth, new product launches, and unexpected demand spikes in a manner consistent with our regulatory and contractual commitments.

### 1.2 Scope

This SOP applies to all IT Operations & Infrastructure activities across the Meridian enterprise, encompassing the following business lines and environments:

| Environment | Business Line(s) Supported | Key Infrastructure |
| :--- | :--- | :--- |
| Production — North America | Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, Meridian SaaS Platform | AWS us-east-1, Snowflake, Apache Kafka |
| Production — European Union | Clinical AI Platform, Meridian SaaS Platform | AWS eu-west-1, Snowflake (EU instance), Pinecone |
| Production — Disaster Recovery | All business lines | Azure (DR), Azure SQL Managed Instance |
| Pre-Production (Staging/UAT) | All business lines | AWS (non-prod VPCs), isolated test environments |
| Development & Sandbox | Engineering & Data Science | AWS (dev accounts), Kubeflow, MLflow |

**In-scope resources:**
- Compute: Amazon EC2, AWS Lambda, Kubernetes (EKS) nodes, SageMaker endpoints
- Storage: Amazon S3, EBS volumes, Snowflake storage, PostgreSQL RDS instances
- Network: VPC networking, Direct Connect bandwidth, VPN throughput, load balancers (ALB/NLB), CloudFront distributions
- Data Services: Apache Kafka topics and partitions, Redis ElastiCache clusters, Pinecone vector databases
- AI/ML Infrastructure: GPU-accelerated EC2 instances (p4d, g5), LangSmith tracing infrastructure
- Software Licensing: All software licenses tied to hardware capacity or user counts

**Key regulatory alignment:** This SOP is designed to support the requirements of SOC 2 Common Criteria CC2.1 (Capacity and Demand Management), CC6.1 (Logical and Physical Access Controls), CC7.1 (Incident Detection), and CC8.1 (Change Management).

---

## 3. Roles and Responsibilities

The following RACI (Responsible, Accountable, Consulted, Informed) matrix defines the specific roles and their obligations under this SOP. Named roles are stewards of their assigned functions.

| Role | Responsibility | Actions |
| :--- | :--- | :--- |
| **VP of IT Operations** (Samantha Torres) | A | Accountable for the overall Framework, resource allocation, budget approval for capacity expansion, and executive reporting. Final authority on threshold definitions. |
| **VP of Engineering** (David Park) | A, C | Accountable for capacity requirements of the software development lifecycle, CI/CD pipeline capacity, and microservice architecture scaling. Consulted on major infrastructure changes impacting application performance. |
| **Director of Infrastructure & Cloud Operations** | R, C | Responsible for the execution of this SOP. Owns capacity dashboards, forecast models, and scaling automation. Consulted on infrastructure cost optimization. |
| **Site Reliability Engineering (SRE) Lead** | R | Responsible for performance baseline definition, service level objective (SLO) tracking, provisioning of synthetic monitoring, and automated scaling trigger configurations. |
| **Information Security Officer (ISO)** | C | Consulted on security implications of capacity-related changes, vulnerability disclosure intake triage, and incident response coordination during security-related capacity events (e.g., DDoS attack response). |
| **Data Platform Manager** | R | Responsible for capacity monitoring of Snowflake, Kafka, Redis, and PostgreSQL instances. Owner of database storage forecasting models. |
| **Engineering Leads (Platform, Clinical AI, HealthPay, MedInsight)** | C, I | Consulted on forecasted demand based on product roadmap features. Informed of all planned maintenance and scaling events affecting their services. |
| **IT Support Manager** | R, I | Responsible for capacity monitoring of internal corporate systems (Okta, VPN, Git). Informed of major production changes that may generate internal support tickets. |
| **All Personnel** | I | Informed of the obligation to report suspected capacity-related issues or security anomalies. |

---

## 4. Policy Statements

### 4.1 Capacity Governance

Meridian IT Operations shall maintain a formal, documented Capacity Plan covering all in-scope production environments. The Capacity Plan must be reviewed and updated quarterly, or upon major product launch, whichever comes first.

### 4.2 Proactive Monitoring and Alerting

All in-scope production resources must be instrumented with automated monitoring and configured with alerts based on the performance baselines and thresholds defined in Section 5. Monitoring must be continuous and generate an incident ticket for any critical threshold breach.

### 4.3 Right-Sizing

Resources shall be provisioned and maintained using a "right-sizing" principle—allocating sufficient headroom to handle anticipated peak loads plus a defined safety buffer, without gross over-provisioning that leads to unjustifiable cost. This principle is enforced via the thresholds in Section 5.

### 4.4 Change Management Integration

Any change to production infrastructure that alters compute, memory, storage, or network capacity (including horizontal scaling events, vertical instance type changes, database read-replica promotion, or Kafka partition expansion) must be authorized via a Change Request in the ServiceNow Change Management module. The Change Request must identify the capacity impact and be approved per SOP-CHG-001. The implementer and approver must not be the same individual to maintain segregation of duties.

### 4.5 Incident Response Integration

A capacity-related performance degradation that breaches a defined Service Level Objective (SLO) must be declared an incident and managed under the Incident Management Procedure (SOP-ISEC-002). The Incident Commander shall assess and document the capacity-related root cause. Although an incident response plan has been documented to address capacity-driven outages, regular tabletop exercises to rehearse response procedures are not currently scheduled.

### 4.6 Third-Party and Vendor Management

Third-party services hosting or processing Meridian data must provide capacity and availability metrics or API access equivalent to Meridian's internal standards, as stipulated in the vendor contract.

---

## 5. Detailed Procedures

This section defines the operational procedures for the capacity lifecycle. All procedures assume a starting point within the ServiceNow Change Management module for audit trail purposes.

### 5.1 Baseline Establishment and Maintenance

A performance baseline is a documented, time-bound representation of expected resource behavior under normal operational load. Baselines are essential to determine what constitutes a deviation.

**Procedure:**
1.  **SRE Lead** queries Datadog for a 30-day rolling window of performance metrics for each in-scope resource defined in the Capacity Management Database (CMDB).
2.  Metrics collected include: CPU utilization (%), Memory utilization (%), Disk I/O (IOPS, throughput), Network throughput (Mbps, PPS), Request latency (p50, p95, p99), Error rate, Kafka consumer lag, DB connection pool utilization.
3.  The data is statistically analyzed to remove outliers (top/bottom 5th percentile).
4.  The 95th percentile (p95) of the remaining dataset for each metric is defined as the **Performance Baseline** for that resource.
5.  Baselines are documented in the IT Operations Confluence space ("Capacity Management") and tagged in Datadog as `baseline:true`.

### 5.2 Capacity Monitoring and Threshold Triggers

Monitoring is the continuous comparison of real-time metrics against defined thresholds anchored to the baseline.

**Procedure:**
1.  **Director of Infrastructure & Cloud Operations**, in consultation with the **VP of IT Operations**, defines three capacity tiers for each production resource type. These thresholds are configured as Datadog Monitors with automated alerting.

| Tier | Threshold Formula | Alert Mechanism | Action Trigger |
| :--- | :--- | :--- | :--- |
| **Tier 1 — Warning** | P95 utilization ≥ Baseline * 1.5 for 1 hour | ServiceNow Alert (Priority 4 — Low), Slack #infra-alerts | Capacity Review scheduled within current sprint. No immediate action. |
| **Tier 2 — Critical** | P95 utilization ≥ Baseline * 2.0 for 15 minutes | ServiceNow Incident (Priority 2 — High), PagerDuty escalation to SRE on-call | Immediate investigation. Scaling action to be executed within 2 hours of triage, per below procedures. |
| **Tier 3 — Emergency** | P95 utilization ≥ Baseline * 3.0 for 5 minutes OR any service SLO breach | ServiceNow Incident (Priority 1 — Critical), PagerDuty page to VP of IT Operations & SRE Lead | Immediate emergency war room convened. All hands on deck. Scaling action or load shedding executed immediately to restore SLO. |

2.  **SRE Team** will also configure "dead man's switch" alerts: if a critical endpoint's synthetic check fails from ≥ 3 geographic PoPs simultaneously, a P1 Incident is automatically generated.
3.  Kafka consumer lag is monitored separately. Lag > 10,000 messages for > 10 minutes triggers a Critical (P2) Incident, as it indicates processing capacity is outmatched.

### 5.3 Forecasting and Demand Management

Forecasting transforms business activities into resource requirements.

**Procedure:**
1.  **Quarterly Forecasting Cycle:**
    - **Input:** The **VP of Product Management** provides a rolling 4-quarter roadmap with anticipated user growth, new feature launch dates, and targeted transaction volumes (e.g., "HealthPay to process 20,000 claims/hour by Q1 2026").
    - **Modeling:** **SRE Lead** uses the roadmap inputs to build a predictive model in the internal capacity planning tool (Akkadian Pro).
    - **Output:** A **Quarterly Capacity Forecast Report** detailing projected Tier 1/2 threshold breach dates for all constrained resources.
2.  **Annual Budgeting:**
    - The **VP of IT Operations** and **Director of Infrastructure & Cloud Operations** compile the quarterly forecasts into an Annual Infrastructure Budget Request.
    - This request includes all anticipated step-function cost increases (e.g., new Direct Connect links, large Reserved Instance purchases, new Kafka cluster provisioning).

### 5.4 Scaling Procedures

Scaling is the execution of a pre-defined runbook to add capacity. Meridian uses an "Infrastructure as Code" (IaC) model; all scaling is performed by modifying Terraform modules or Helm values files, reviewed via pull request (PR), and applied via CI/CD (GitHub Actions).

#### 5.4.1 Horizontal Scaling (Adding more instances/pods)

This is the preferred method for stateless services (web front-ends, APIs, some Kafka consumers).

- **Trigger:** Tier 2 Critical alert, or manually initiated by an Engineer based on the forecast.
- **Runbook `run-scale-out-h-001`:**
    1.  SRE confirms the service is healthy and can handle connections from new instances.
    2.  SRE creates a Git branch: `capacity/SOP-ITOP-005/scale-[service]-[date]`.
    3.  SRE modifies the `desired_count` or `replica_count` variable in the Terraform module or Helm chart `values-prod.yaml` file. For a Critical alert, the default action is to double the current count (min 2, max 20). For a manual forecast-based scaling, the target count is calculated from the model.
    4.  SRE opens a Pull Request. The code auto-runs `terraform plan` or `helm diff` and attaches the output.
    5.  **Approval:** The PR requires an Approval from a **peer SRE or the Director of Infra & Cloud Ops**. The author cannot approve their own PR, enforcing segregation of duties for the change.
    6.  After approval, merging the PR auto-applies the change in the target environment.
    7.  SRE validates the new instances are registered with the load balancer (ALB healthy host count) and that the metric threshold has subsided.
    8.  SRE updates the ServiceNow Incident/Alert record with the action taken and closes it.

#### 5.4.2 Vertical Scaling (Increasing instance size)

Used for stateful services (databases, ElastiCache, large JVM-based apps) or GPU-bound ML endpoints.

- **Trigger:** Tier 2 Critical alert where horizontal scaling is impossible or ineffective, or a forecast-driven upgrade.
- **Runbook `run-scale-up-v-001`:**
    1.  SRE identifies the next larger, cost-effective instance type from the approved AWS Service Catalog.
    2.  SRE creates a Git branch.
    3.  SRE modifies the `instance_type` variable for the target resource.
    4.  **Maintenance Window**: SRE checks the PR description box: "Requires Maintenance Window." This triggers a secondary validation in the CI/CD pipeline that will not auto-merge immediately.
    5.  SRE creates a Change Request (CHG) in ServiceNow, attaching the PR link. The CHG must include a rollback plan and a communication notification to stakeholders per the maintenance window schedule.
    6.  **Approval:** The CHG requires approval from the **Director of Infrastructure & Cloud Operations** and acknowledgment from the **VP of Engineering**.
    7.  At the scheduled time, the Director approves the PR, which auto-applies. The instance restarts and resumes operation.

### 5.5 Capacity Recovery

Following a capacity-related incident, a formal review is mandatory.
1.  Within 5 business days of a P1 or P2 capacity incident closure, the **SRE Lead** schedules a "Post-Incident Review" (PIR).
2.  The PIR blamelessly analyzes the timeline, the monitoring (was the baseline right?), the alerting (did it fire in time?), and the procedure execution.
3.  A clear action item list is created in Jira to address any gaps (e.g., baseline adjustment, new synthetic check, runbook correction).

---

## 6. Controls and Safeguards

### 6.1 Identity and Access Management for Capacity Tools

- Access to Datadog dashboards is granted based on role, with `read-only` for all engineering, `power-user` (manage monitors) for SRE, and `admin` for VP IT Ops and Director of Infra & Cloud Ops.
- Access to Terraform state files in S3 is restricted to the CI/CD service account, which is gated by GitHub Environments requiring specific approver groups.
- Direct AWS Console access ("break glass") for making manual capacity changes requires PagerDuty incident context and is logged directly to CloudTrail with a Security Hub auto-remediation check. Any manual console change triggers a high-severity finding that the Information Security Officer must close within 24 hours.

### 6.2 Segregation of Duties

The Infrastructure as Code (Git-based) model inherently provides a technical segregation layer. This is enforced by:
- **GitHub Branch Protection Rules:** The `main` branch of all infrastructure repositories is locked. No direct commits are permitted.
- **CODEOWNERS File:** A `CODEOWNERS` file designates the `@meridian/sre-team` as the required reviewer for all capacity-related changes.
- **Restricted Approvals:** The author of a Pull Request cannot approve it. For changes classified as `risk: high` (e.g., vertical scaling of a production database), two approvals are required: one from an SRE peer and one from the Director of Infrastructure & Cloud Operations.
- **ServiceNow Enforcement:** The Change Management module is configured so that the *Assigned To* (implementer) and *Approver* fields must contain different user IDs. The system enforces this by blocking save functionality, not merely a warning.

### 6.3 Automated Cost Safeguards

- An AWS Budget Action is configured. If projected monthly spend exceeds the approved Operations Budget by 15%, an automatic alert is sent to the VP of IT Operations. If it exceeds by 25%, a cost-control policy is activated that automatically terminates any EC2 instance tagged with `environment: sandbox` to prevent uncontrolled spending from non-production capacity.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The success of the Capacity Management process is measured by the following KPIs, reported in the monthly IT Operations Scorecard:

| KPI | Target | Measurement Tool |
| :--- | :--- | :--- |
| **SLO Compliance** (% of SLI compliance periods where the objective is met) | > 99.9% | Datadog SLO Dashboard |
| **Capacity Overhead** (Average CPU/Memory headroom across prod fleet during peak hour) | 30% - 50% | Datadog, Custom Datadog Metric |
| **Forecast Accuracy** (Variance between forecasted and actual peak load) | ± 15% | Akkadian Pro vs. Datadog Actuals |
| **Incidents from Capacity Exhaustion** (Number of P1/P2 incidents attributed to capacity) | 0 | ServiceNow Incident Module |
| **Mean Time to Scale Out (MTTSO)** (Time from Tier-2 alert to healthy new instance serving traffic) | < 15 minutes (automated) | Datadog Event Log to ServiceNow Alert Closure |

### 7.2 Reporting Cadence

| Report | Audience | Frequency | Method |
| :--- | :--- | :--- | :--- |
| **Real-time Capacity Dashboard** | SRE, IT Ops | Continuous | Datadog Screenboard, wall-mounted display in NetOps Center |
| **Weekly Capacity Brief** | Director of Infra & Cloud Ops, Engineering Leads | Weekly (Every Monday) | Auto-generated PDF from Datadog, delivered to Slack #ops-leads |
| **Monthly IT Operations Scorecard** | VP of IT Operations, VP of Engineering, CTO | Monthly | Formal presentation deck, review of KPI trends |
| **Quarterly Capacity Forecast & Review** | CTO, CFO, VP of Product | Quarterly | Formal capacity plan document review against product roadmap and budget |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Definition

An exception is any situation where a procedure in this SOP cannot be followed. Common examples include:
- An emergency security patch that must be deployed, and the change management system is integrated but the full CAB approval latency poses an unacceptable risk of exploitation.
- A sudden, unforeseen business demand spike (e.g., a partner launching a mobile app that skyrockets our HealthPay transaction volume) that requires the purchase of hardware or contract negotiation outside the normal budget cycle.

### 8.2 Exception Process

1.  **Initiator:** Any person identifying the need for an exception submits an "Exception Request" in ServiceNow, referencing the specific SOP section, the justification, and a proposed compensating control or timeline.
2.  **Risk Assessment:** The **Information Security Officer (ISO)** is automatically added as a viewer and performs a documented risk assessment, adding their findings to the ServiceNow ticket within 1 business day.
3.  **Business Justification:** The relevant **Business Unit Lead** (e.g., VP of Product for partner-driven demand) must document the business necessity and impact of not granting the exception.
4.  **Approval Chain:**
    - **Low/Medium Risk (Temporary, < 1 month):** Approved by **VP of IT Operations**.
    - **High Risk or Permanent Exception:** Approved by **VP of IT Operations**, **ISO**, and **VP of Engineering**. The **CTO** is informed.
5.  **Tracking:** All approved exceptions are reviewed monthly. If the root cause leading to the exception is not addressed within the approved time, the exception is escalated to the CTO for resolution.

### 8.3 Escalation of Unresolved Capacity Issues

If a capacity threshold breach (Tier 2 or 3) persists for > 4 hours and the standard runbooks have been exhausted:
1.  The **SRE Lead** declares a "Systematic Capacity Event" and escalates verbally and via a Priority 1 ServiceNow ticket to the **VP of IT Operations** and **CTO**.
2.  The **CTO** is empowered to authorize emergency spend, override standard change management lead times for critical fixes, or make decisions regarding graceful degradation of non-critical services to preserve core clinical and payment functions (e.g., temporarily disabling complex reporting dashboards to free database resources for transaction processing).

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

All training must be completed within the first 2 weeks of employment or reassignment to a role. Annual refresher training compliance is tracked via Workday Learning.

| Role | Training Module | Annual Refresher | Delivery Method |
| :--- | :--- | :--- | :--- |
| **SRE, Cloud Engineers** | MOD-CAP-101: SRE Capacity Runbooks & IaC Scaling | Yes | Online (Workday) + Hands-on Lab (Quarterly) |
| **IT Support Managers** | MOD-CAP-201: Internal System Monitoring & Reporting | Yes | Online (Workday) |
| **Engineering Leads, Directors** | MOD-CAP-301: Capacity Forecasting & Business Demand Translation | Yes | Online (Workday) |
| **Information Security Officer & Team** | MOD-CAP-401: Secure Capacity Management & Incident Coordination | Yes | Instructor-led Workshop (Annual) |

### 9.2 SOP Awareness

This SOP document is reviewed as part of the standard New Hire Onboarding plan for all IT Operations and Engineering personnel. An acknowledgment of "Read and Understood" is recorded in Workday for each version of this SOP. Upon publication of a new version, all personnel with responsibilities herein have 10 business days to complete the review and acknowledgment.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Policy Name | Relationship |
| :--- | :--- | :--- |
| SOP-CHG-001 | Change Management Policy | Governs all changes executed via scaling procedures. |
| SOP-ISEC-002 | Incident Response Procedure | Governs response to Tier 2 and Tier 3 capacity events. |
| SOP-ARCH-001 | Architecture Review Process | New products must be assessed against capacity planning prior to launch. |
| SOP-DATA-004 | Database Operations and Management | Contains database-specific capacity and backup standards. |
| SOP-HR-101 | Onboarding and Offboarding | Ensures training assignments and access reviews are tied to the employment lifecycle. |

### 10.2 External Standards and References

- **SOC 2**: Trust Services Criteria (TSC) CC2.1 (Capacity & Demand), CC6.1 (Access Controls), CC7.1 (Incident Detection), CC8.1 (Change Management).
- **AWS Well-Architected Framework**: Performance Efficiency Pillar.
- **ITIL 4**: Capacity and Performance Management Practice.

---

## 11. Revision History

| Version | Date | Author | Authorized By | Description of Change |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 2019-02-10 | James Parkins (Former Dir. Infra) | Elara Vance (Former VP Eng) | Initial creation of standalone Capacity Management SOP. |
| 2.1 | 2020-06-22 | Maria Jensen (SRE Lead) | Elara Vance (Former VP Eng) | Major revision: Integration with AWS Infrastructure. Added forecast modeling section. |
| 3.4 | 2022-01-15 | Liam O'Connell (SRE) | Samantha Torres | Updated to reflect migration to EKS, added Kafka and Snowflake monitoring. Introduced RACI matrix. |
| 4.1 | 2023-08-30 | Priya Sharma (SRE Lead) | Samantha Torres | Integrated Azure DR capacity monitoring. Refined Tier 1-3 thresholds. Aligned change approval flow with updated SOP-CHG-001. |
| 4.5 | 2024-03-10 | Kai Nakamura (SRE) | Samantha Torres, David Park | Pre-audit review. Added explicit SOC 2 TSC mapping to Procedure. Hardened segregation of duties in IaC/PR flow. Updated roles after re-org. |
| **4.7** | **2025-12-15** | **Elena Rossi (SRE)** | **Samantha Torres, David Park** | **Annual comprehensive review. Updated GPU instance types for Clinical AI inference fleet. Revised Kafka lag alert thresholds. Added cost control safeguard (AWS Budget Action). Cleaned up formatting for Workday integration.** |