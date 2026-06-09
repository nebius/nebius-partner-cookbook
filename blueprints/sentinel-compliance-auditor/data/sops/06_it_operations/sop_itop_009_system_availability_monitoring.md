---
sop_id: "SOP-ITOP-009"
title: "System Availability Monitoring"
business_unit: "IT Operations & Infrastructure"
version: "2.1"
effective_date: "2025-08-25"
last_reviewed: "2026-08-15"
next_review: "2027-02-25"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: System Availability Monitoring

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) defines the standardized framework, methodology, roles, and responsibilities for the continuous monitoring, measurement, reporting, and enforcement of system availability across all product lines and supporting infrastructure at Meridian Health Technologies, Inc. The purpose is to ensure that all customer-facing and critical internal systems meet or exceed their defined availability targets, thereby upholding contractual commitments, maintaining patient safety, and satisfying regulatory and compliance obligations.

### 1.2 Scope

This SOP applies to the following systems, platforms, and infrastructure across all Meridian global offices (Boston, London, Berlin, Singapore, Toronto) and cloud environments:

| System/Business Line | Scope Inclusion | Criticality Tier |
| --- | --- | --- |
| Meridian SaaS Platform (AWS us-east-1, eu-west-1; Azure DR) | Core infrastructure, tenant isolation, authentication services, API gateway | Tier 1 - Critical |
| Clinical AI Platform | Inference endpoints, model serving infrastructure, clinical decision support APIs, diagnostic imaging analysis pipelines | Tier 1 - Critical |
| HealthPay Financial Services | Payment processing gateway, patient financing portals, claims automation engine, lending decision APIs | Tier 1 - Critical |
| MedInsight Analytics | Population health dashboards, PHI data pipelines, care gap identification services | Tier 2 - High |
| Internal Corporate Systems | Okta IdP, internal DNS/DHCP, CI/CD pipelines (GitHub Actions, Jenkins), VPN concentrators | Tier 2 - High |
| Development/Staging Environments | Non-production AWS/Azure environments | Tier 3 - Moderate |
| Corporate LAN/WAN | Office network infrastructure at all global locations | Tier 3 - Moderate |

**Out of Scope:** End-user device availability (covered under SOP-ITOP-014: Endpoint Management), physical security systems (covered under SOP-SEC-003: Physical Security Operations), and third-party SaaS vendor availability beyond API integration points.

### 1.3 Applicability

This SOP is binding upon all personnel within the IT Operations & Infrastructure, Engineering, Security, and Compliance business units. Specific role-based obligations are detailed in Section 3. Non-compliance with this SOP may result in disciplinary action up to and including termination of employment per Meridian's Employee Handbook (HR-POL-102).

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
| --- | --- |
| **Availability** | The percentage of time a system or service is operational and accessible for its intended use, measured over a defined period. Calculated as: (Agreed Service Time - Downtime) / Agreed Service Time × 100. |
| **Agreed Service Time (AST)** | The predetermined window during which a service is expected to be available. For Tier 1 systems, AST is 24 hours × 7 days × 365 days (8,760 hours/annum). |
| **Downtime** | Any period during which a service is unavailable or fails to perform its critical functions. Includes both planned and unplanned outages. |
| **Planned Downtime** | Scheduled maintenance windows communicated to customers and stakeholders at least 72 hours in advance. Planned downtime exceeding the quarterly maintenance budget counts against SLA targets. |
| **Unplanned Downtime** | Any service interruption not communicated in advance, including incidents caused by infrastructure failures, software defects, cyber-attacks, or human error. |
| **Mean Time to Detect (MTTD)** | Average elapsed time between the onset of an incident and its detection by monitoring systems or human observation. |
| **Mean Time to Acknowledge (MTTA)** | Average elapsed time between incident detection and acknowledgment by an on-call responder. |
| **Mean Time to Resolve (MTTR)** | Average elapsed time between incident detection and full service restoration. |
| **Uptime** | The total accumulated time a service is available within the measurement period. |
| **Service Level Agreement (SLA)** | A formal, contractual commitment to customers defining availability targets and remedies for non-compliance. |
| **Service Level Objective (SLO)** | An internal, measurable target for availability that is more stringent than the external SLA to provide an operational buffer. |
| **Error Budget** | The permissible amount of downtime or errors within a given period, calculated as (1 - SLO). Once exhausted, new feature releases are frozen until availability is restored. |
| **Health Check** | An automated probe that determines the operational status of a component. Can be classified as Liveness (is it running?), Readiness (can it serve traffic?), or Functional (is it doing the right thing?). |
| **Synthetic Transaction** | A scripted, end-to-end test of a critical user workflow executed by an external monitoring agent that mimics real user behavior. |
| **High-Risk AI System** | As defined by the EU AI Act Annex III, encompassing all clinical decision support and diagnostic AI products deployed within EU member states. |
| **Protected Health Information (PHI)** | Individually identifiable health information as defined under HIPAA Privacy Rule (45 CFR § 160.103). |

### 2.2 Acronyms

| Acronym | Definition |
| --- | --- |
| AI RMF | Artificial Intelligence Risk Management Framework (NIST AI 100-1) |
| AST | Agreed Service Time |
| AWS | Amazon Web Services |
| AZ | Availability Zone |
| BCP | Business Continuity Plan |
| CCO | Chief Compliance Officer |
| CIO | Chief Information Officer (role fulfilled by VP of Engineering at Meridian) |
| CISO | Chief Information Security Officer |
| CPO/DPO | Chief Privacy Officer / Data Protection Officer |
| DR | Disaster Recovery |
| EU AI Act | European Union Artificial Intelligence Act (Regulation 2024/1689) |
| GDPR | General Data Protection Regulation (Regulation (EU) 2016/679) |
| HIPAA | Health Insurance Portability and Accountability Act |
| HITRUST | Health Information Trust Alliance Common Security Framework |
| ISO | International Organization for Standardization |
| KPI | Key Performance Indicator |
| MTTD | Mean Time to Detect |
| MTTA | Mean Time to Acknowledge |
| MTTR | Mean Time to Resolve |
| NIST | National Institute of Standards and Technology |
| NOC | Network Operations Center |
| PHI | Protected Health Information |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| SLA | Service Level Agreement |
| SLO | Service Level Objective |
| SOC 2 | System and Organization Controls 2 (AICPA Trust Services Criteria) |
| SOP | Standard Operating Procedure |
| SR 11-7 | Federal Reserve Supervisory Guidance on Model Risk Management |
| SSL/TLS | Secure Sockets Layer / Transport Layer Security |
| VPC | Virtual Private Cloud |
| VP | Vice President |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| Activity | VP of IT Ops (Samantha Torres) | Director, Infrastructure Ops | NOC Lead (Shift Supervisors) | Site Reliability Engineers (SREs) | Product Engineering Managers | CISO (Rachel Kim) | CCO (Thomas Anderson) | VP of Engineering (David Park) |
|---|---|---|---|---|---|---|---|---|
| Define SLOs & Error Budgets | A | R | C | C | C | C | I | I |
| Approve SLA targets | C | C | I | I | R | I | C | A |
| Configure monitoring probes & dashboards | I | A | C | R | I | - | - | I |
| 24/7 Monitoring & Alert Response | I | I | R | R | - | - | - | - |
| Declare Major Incident | C | R | R | C | I | I | I | I |
| Execute Incident Response Playbooks | I | C | R | R | C | I | - | - |
| Post-Incident Review (Postmortem) | A | R | R | R | R | C | I | I |
| Monthly SLA Reporting | R | A | C | C | I | I | I | C |
| Quarterly Audit Evidence Collection (SOC 2) | C | R | - | C | I | I | A | - |
| Annual SOP Review & Update | A | R | C | C | C | C | C | C |
| Approve Exception Requests | A | R | - | - | C | C | R | I |

**R = Responsible** (executes the work), **A = Accountable** (final approval authority), **C = Consulted** (provides input before action), **I = Informed** (notified after decision/action).

### 3.2 Role Descriptions

**VP of IT Operations (Samantha Torres):** Serves as the SOP Owner. Accountable for the overall effectiveness of the availability monitoring program. Approves all SLOs, error budgets, and exception requests. Provides quarterly availability reports to the Board AI Governance Committee. Holds signatory authority for SLA reporting to external customers.

**Director, Infrastructure Operations:** Reports to VP of IT Operations. Responsible for the operational execution of this SOP. Manages the Network Operations Center (NOC) team leads. Conducts quarterly reviews of monitoring coverage and tooling efficacy. Approves planned maintenance windows exceeding 30 minutes for Tier 1 systems.

**NOC Lead (Shift Supervisors):** Manage 24/7/365 monitoring shifts across Boston, London, and Singapore NOC locations. Serve as the initial escalation point for all monitoring alerts. Authorized to engage on-call SREs and declare Sev-2 incidents. Ensure shift handover documentation is complete and accurate.

**Site Reliability Engineers (SREs):** Embedded within product engineering teams. Design, implement, and maintain synthetic health checks, application performance monitoring (APM) dashboards, and alerting rules within Datadog and PagerDuty. On-call rotation (primary and secondary) for incident response. Authors of post-incident postmortems.

**Product Engineering Managers:** Responsible for ensuring their products meet defined SLOs. Consult on error budget consumption and feature freeze decisions. Provide product-specific expertise during incident triage. Accountable for resolving defects that contribute to availability degradation.

**Chief Information Security Officer (Rachel Kim):** Consults on security-related monitoring, including intrusion detection alerts that may impact availability (e.g., DDoS, ransomware). Authorizes emergency security patching that may require expedited planned downtime.

**Chief Compliance Officer (Thomas Anderson):** Accountable for ensuring availability monitoring evidence collection satisfies SOC 2 Trust Services Criteria (Availability), specifically CC5.2, A1.1, and A1.2. Approves the structure of quarterly audit reports before external auditor submission.

**VP of Engineering (David Park):** Serves as the SOP Approver. Approves all changes to this SOP. Arbitrates disputes regarding error budget freezes and feature release priority. Provides final approval for permanent exceptions.

---

## 4. Policy Statements

### 4.1 Availability Commitment

Meridian Health Technologies is committed to delivering highly available, resilient systems that support critical healthcare and financial workflows. All Tier 1 systems shall maintain a minimum availability of 99.95%, and Tier 2 systems shall maintain a minimum availability of 99.9%, measured on a trailing 30-day and trailing 365-day basis.

### 4.2 Proactive Monitoring Mandate

All production systems shall be subject to proactive, automated health checking. No production service shall be deployed without corresponding monitoring probes (liveness, readiness, and at least one functional/synthetic check) registered in Datadog and integrated into the PagerDuty incident alerting fabric.

### 4.3 Incident Transparency

All availability incidents, regardless of severity, shall be documented, root-caused, and tracked to resolution. Incident timelines, impact assessments, and corrective actions shall be published in internal postmortems within 5 business days. A redacted summary shall be provided to affected customers upon request within 10 business days, consistent with contractual obligations.

### 4.4 Error Budget Governance

Error Budgets are the primary mechanism governing the balance between feature velocity and system stability. When a Tier 1 system's error budget is ≥80% exhausted within a calendar quarter, all non-critical feature releases for that system are automatically frozen until budget is recovered. The freeze is enforced by the VP of IT Operations with concurrence from the VP of Engineering.

### 4.5 SOC 2 Availability Controls

In alignment with the AICPA Trust Services Criteria for Availability (CC5.2, A1.1, A1.2, A1.3), Meridian implements continuous monitoring, environmental redundancy, disaster recovery planning, and capacity management controls. Evidence of control operation is collected continuously and compiled quarterly for SOC 2 Type II audit reviews.

### 4.6 EU AI Act Compliance Overlay

Availability monitoring for Clinical AI Platform components classified as high-risk AI systems under the EU AI Act shall include additional probes verifying "human oversight" interfaces (ability to override, flag, or halt AI output) are operational. Any degradation of these interfaces constitutes a Tier-1 availability incident, irrespective of the underlying model's availability.

---

## 5. Detailed Procedures

### 5.1 System Onboarding to Monitoring Framework

This procedure shall be followed for any new production system, significant feature release, or acquisition integration before go-live approval is granted.

**Responsible:** SRE Team Lead, Product Engineering Manager
**Accountable:** Director, Infrastructure Operations

**Steps:**
1. **Product Team Submission:** The Product Engineering Manager submits a completed "Monitoring Onboarding Request" form (see Appendix A: Monitoring Onboarding Template) to the SRE team via the Jira Service Management (JSM) "ITOps-Monitoring" project at least 10 business days prior to planned go-live.
2. **SLO Definition Workshop:** Within 3 business days, an SRE is assigned and schedules a 60-minute SLO Definition Workshop with the product team. The following artifacts are produced:
   - A list of all critical user journeys (CUJs).
   - The Service Level Indicator (SLI) for each CUJ (e.g., latency at p99, error rate, availability %).
   - The initial SLO target.
   - The initial Error Budget.
   - Definition of "Good" vs "Bad" events for the SLI.
3. **Dashboard & Probe Implementation:** The assigned SRE implements:
   - Datadog dashboards for golden signals (Traffic, Latency, Errors, Saturation) per CUJ.
   - Liveness probe (HTTP GET /healthz).
   - Readiness probe (HTTP GET /readyz).
   - Functional synthetic tests using Datadog Synthetic Monitoring (minimum: 3 geographically distributed locations).
   - PagerDuty service entries correlated with Datadog monitors.
4. **Alert Threshold Configuration:** Alerts are configured with the following thresholds (tunable per SLO):
   - **Warning (Sev-3):** Error budget burn rate > 1x (alerts within 1 hour).
   - **Critical (Sev-2):** Error budget burn rate > 10x (alerts within 5 minutes) or service completely unreachable for > 120 seconds.
   - **Emergency Page (Sev-1):** Error budget burn rate > 100x (immediate page) or availability of CUJ drops below 95% for any 5-minute window.
5. **Runbook Validation:** The assigned SRE creates or updates a PagerDuty Runbook Automation action for each alert type. The runbook is validated in a testing session with the NOC within 5 business days of configuration.
6. **Go-Live Gate Check:** Before the product go-live, the NOC Lead verifies that the new monitors are visible in the central NOC dashboard and that synthetic tests are passing from all designated regions. The NOC Lead signs off on the JSM ticket. The Director, Infrastructure Operations provides final approval.

**Outputs:** Configured Datadog monitors, PagerDuty service entries, validated runbooks, signed JSM approval ticket.

### 5.2 Routine Health Check Monitoring (NOC Operations)

This procedure governs the 24/7/365 real-time monitoring activities performed by the Network Operations Center.

**Responsible:** NOC Shift Engineers, NOC Lead (Shift Supervisor)
**Accountable:** NOC Lead

**Steps (Per Shift):**
1. **Shift Handover (H-15min):** Offgoing shift lead provides a structured handover to the oncoming shift lead using the NOC Handover Template (Confluence Template ID: NOC-HANDOVER). Contents include:
   - Open PagerDuty incidents (all severities).
   - Ongoing planned maintenance windows.
   - Recently closed incidents (last 8 hours) for awareness.
   - Known degraded conditions or monitoring blind spots.
   - Upcoming scheduled on-call rotations.
2. **Dashboard Walkthrough (H+15min):** Oncoming NOC engineer performs a manual 15-minute walkthrough of the "Executive NOC Dashboard" and "SOC 2 Availability Control Dashboard" in Datadog. Any anomalous patterns (latency drift, sustained elevated error rates below alert thresholds) are logged in the NOC Daily Log (Confluence Space: NOC-DAILY-LOGS).
3. **Synthetic Test Validation (H+30min):** Verify all Tier-1 synthetic transaction tests are executing successfully from all three geographic locations (US-East, EU-West, AP-Southeast). Any failure is immediately investigated, and a ticket is logged in JSM even if the test recovered.
4. **Continuous Monitoring (Entire Shift):** NOC engineers monitor the PagerDuty incident queue and Datadog real-time dashboards.
   - **Sev-3 Alerts:** Acknowledge within 15 minutes. Triage and resolve within 4 hours. Escalate to on-call SRE if unresolved after 4 hours.
   - **Sev-2 Alerts:** Acknowledge within 5 minutes. Immediately engage on-call SRE. Escalate to Director, Infrastructure Operations if unresolved after 60 minutes.
   - **Sev-1 Alerts:** Acknowledge within 1 minute. Immediately page on-call SRE and NOC Lead. NOC Lead declares Major Incident and initiates the Critical Incident Response Plan (see SOP-ITOP-001: Incident Response Management).
5. **End-of-Shift Summary:** NOC Lead documents significant events, open issues, and monitoring status in the NOC Daily Log. If any monitored system is not at full health, a detailed status is sent to the #itops-status Slack channel.

### 5.3 Planned Maintenance Management

Procedures to ensure planned downtime is executed with minimal impact and tracked against error budgets.

**Responsible:** SRE Team, Product Engineering Manager
**Accountable:** Director, Infrastructure Operations

**Steps:**
1. **Maintenance Request:** A JSM "Planned Maintenance" ticket is submitted at least 120 hours (5 days) prior to the requested window for Tier-1 systems, and 72 hours for Tier-2 systems. The request includes:
   - System(s) affected.
   - Maintenance window start/end (UTC).
   - Expected user impact (none, degraded, unavailable).
   - Rollback plan and estimated time to rollback.
   - Total minutes of potential downtime.
2. **Impact Review:** The Director, Infrastructure Operations reviews the request against the current Error Budget status. If the requested downtime would cause the error budget to exceed 80% exhaustion for the quarter, the request is denied or deferred unless approved by the VP of IT Operations.
3. **Internal Communication:** If approved, the NOC Lead publishes the maintenance window to the Meridian-wide IT Calendar (Outlook/Exchange) and posts a notification in the #itops-planned-maintenance Slack channel no less than 72 hours prior. For maintenance expected to cause user-facing impact, the VP of Customer Operations (Michael Chang) is notified to draft customer communications.
4. **Customer Notification (If Applicable):** Customer Operations sends notifications to affected customers per contractual SLA notification requirements—minimum 48 hours for standard maintenance, 24 hours for emergency security patching.
5. **Execution:**
   - Maintenance start time: SRE places the system into "Maintenance Mode" via feature flag or load balancer configuration. Monitoring alerts for the affected system are suppressed in PagerDuty for the duration via a Maintenance Window configured in Datadog/PagerDuty.
   - SRE executes the maintenance procedure per the validated runbook.
   - Maintenance end time: System is validated (all health checks pass), removed from Maintenance Mode, and monitoring is re-enabled. SRE updates the JSM ticket with actual downtime duration.
6. **Post-Maintenance:** Actual downtime minutes are recorded and fed into the error budget calculation. Any deviations (overrun, rollback execution) are documented in the JSM ticket and flagged for the next weekly operations review.

### 5.4 SLA Measurement and Calculation

**Responsible:** Director, Infrastructure Operations
**Accountable:** VP of IT Operations

**Steps:**
1. **Data Aggregation:** On the 1st calendar day of each month, an automated script (Meridian Internal Tool: SLA-Calculator) pulls raw uptime/downtime data from Datadog and AWS CloudWatch for all Tier-1 and Tier-2 systems. Excluded from the calculation: downtime during approved maintenance windows (up to the quarterly maintenance budget), and downtime attributable to force majeure events per customer contracts.
2. **Calculation Formula:**
   - System Availability (%) = (Total AST minutes in period - (Total Unplanned Downtime minutes + Planned Downtime exceeding budget minutes)) / Total AST minutes × 100
3. **Weighted Composite SLA:** The composite Meridian SaaS Platform SLA is calculated as a weighted average of component system availability, with weights assigned based on the percentage of total transaction volume served by each component.
4. **Validation:** The Director, Infrastructure Operations reviews the preliminary SLA report and validates any manually excluded downtime events against the incident record. The VP of IT Operations approves the final monthly SLA figures.
5. **Remedy Calculation:** If any external SLA has been breached, the Director creates a "SLA Breach - Customer Remedy" case in the CRM (Salesforce Service Cloud), attaching the verified SLA report. This is routed to the VP of Customer Operations (Michael Chang) and General Counsel (Maria Gonzalez) for remedy execution per customer contracts.
6. **Archival:** Finalized monthly SLA reports are exported to PDF, digitally signed by the VP of IT Operations, and archived in the internal GRC platform (Vanta) as evidence for SOC 2 TSC A1.2.

### 5.5 Post-Incident Review and Postmortem

This procedure is mandatory for all Sev-2 and Sev-1 incidents.

**Responsible:** Incident Commander (designated SRE or NOC Lead)
**Accountable:** Director, Infrastructure Operations

**Steps:**
1. **Postmortem Scheduling:** Within 24 hours of the incident resolution, the Incident Commander schedules a 90-minute blameless postmortem meeting. Required attendees: Incident Commander, responding SRE(s), NOC Lead on shift during incident, Product Engineering Manager for the affected service. Optional: CISO (for security-related outages), General Counsel (for incidents with legal/compliance implications).
2. **Timeline Construction:** Prior to the meeting, the Incident Commander drafts a minute-by-minute timeline based on Datadog logs, PagerDuty alerts, Slack communications, and change management records. The timeline is posted to the shared Confluence document for review.
3. **Postmortem Meeting (Structure):**
   - **What happened?** Review the factual timeline. Only facts, no attribution of blame.
   - **What was the impact?** Quantify downtime duration, error budget consumed, customer impact (number of affected transactions/users), and any PHI exposure risk.
   - **How was it detected?** Compare actual MTTD against target MTTD (< 5 min for Tier-1). Identify if detection was automated or manual.
   - **How was it resolved?** Trace the mitigation steps. Document MTTR.
   - **What went well?** Identify effective responses to reinforce.
   - **What can be improved?** Identify root causes and contributing factors (using "5 Whys" or similar technique).
4. **Action Item Creation:** Action items from the postmortem are logged as individual Jira tickets (type: "Postmortem Action"). Each action item has a clear owner, severity (Blocking/High/Medium/Low), and target due date. All items must be tracked to completion. The Director, Infrastructure Operations reviews outstanding action items weekly.
5. **Postmortem Publication:** The final postmortem document is published to the internal Confluence "Postmortems" space within 5 business days of incident resolution. A redacted, customer-facing version is prepared by Customer Operations and Legal for distribution upon request.
6. **Quarterly Trend Analysis:** The VP of IT Operations presents a rolling 12-month incident trend analysis (count by severity, MTTD/MTTR trends, top recurring root causes) to the Board AI Governance Committee.

---

## 6. Controls and Safeguards

Meridian implements a layered set of technical and administrative controls to ensure the integrity, reliability, and auditability of the availability monitoring system, satisfying SOC 2 Availability and Security criteria.

### 6.1 Administrative Controls

| Control ID | Control Description | SOC 2 Mapping | Frequency | Owner |
|---|---|---|---|---|
| **AC-MON-01** | Independent Review of Monitoring Configuration: The Director, Infrastructure Operations performs a quarterly review of all Tier-1 Datadog monitor configurations, synthetic test scripts, and PagerDuty escalation policies to ensure alignment with approved SLOs. Deviations are documented in a Jira ticket. | CC5.2, A1.1 | Quarterly | Dir., Infra Ops |
| **AC-MON-02** | Annual SOP Attestation: All NOC engineers, SREs, and Engineering Managers must formally attest via Okta Workflows that they have read, understood, and will comply with the current version of this SOP. Attestation records are stored in the GRC platform. | CC1.2, A1.1 | Annually (or upon revision) | CCO (Thomas Anderson) |
| **AC-MON-03** | Segregation of Duties: The NOC team (monitoring) is organizationally and logically separate from SREs (system configuration). NOC engineers do not have IAM permissions to modify production infrastructure or suppress Datadog monitors. SREs cannot modify PagerDuty user contact methods. | CC5.2, A1.1 | Continuous | CISO (Rachel Kim) |
| **AC-MON-04** | Quarterly SLA Report Review & Approval: The final monthly SLA report for the third month of each fiscal quarter is compiled into a Quarterly SLA Compliance Report. This report is reviewed and formally approved via DocuSign by the VP of IT Operations (Samantha Torres), VP of Engineering (David Park), and CCO (Thomas Anderson) before submission to external auditors. | A1.2, A1.3 | Quarterly | VP, IT Ops |
| **AC-MON-05** | Third-Party Uptime Validation: An independent, external uptime monitoring service (StatusHub.io, configured under Meridian's enterprise account) performs continuous HTTP and SSL/TLS health checks against Meridian's public-facing endpoints. Discrepancies between internal and external uptime reports greater than 0.01% are formally investigated. | A1.1 | Per-Incident | Dir., Infra Ops |

### 6.2 Technical Controls

| Control ID | Control Description | Implementation Detail |
|---|---|---|
| **TC-MON-01** | Synthetic Transaction Georedundancy | Datadog Synthetic tests execute from AWS regions us-east-1 (N. Virginia), eu-west-1 (Ireland), and ap-southeast-1 (Singapore) to validate availability from all Meridian operating regions. |
| **TC-MON-02** | Monitor-As-Code (MaC) | All Datadog monitors, synthetic tests, and PagerDuty service configurations are defined in Terraform (m-iac) and stored in the `meridian/itops-monitoring` private GitHub repository. Changes require Pull Request review and approval from an SRE team lead before `terraform apply`. This ensures version control and audit trail integrity. |
| **TC-MON-03** | Out-of-Band Alerting Path | In addition to PagerDuty (primary), all Tier-1 Sev-1 alerting rules push a simultaneous, low-tech alert to a dedicated, on-call-only Slack channel (#pagerduty-emergency) and, if unacknowledged in 5 minutes, trigger an automated outbound call via PagerDuty to the dedicated NOC emergency contact number. |
| **TC-MON-04** | Silent Monitor / Shadow Alerting | All new or modified alert thresholds are deployed in "Shadow Mode" (evaluating but not triggering pages) for a minimum of 72 hours to validate signal quality, reduce false positives, and ensure thresholds are calibrated before operational activation. |
| **TC-MON-05** | PagerDuty Escalation Policy Enforcement | Escalation policies are enforced via Terraform. Any manual override of an escalation policy from the PagerDuty UI triggers an alert to the CISO (Rachel Kim) and is logged as a security event in Splunk. Overrides self-expire after 60 minutes. |
| **TC-MON-06** | Monitoring Data Encryption at Rest | All Datadog log archives, APM traces, and metric data, which may contain metadata correlated with PHI access patterns, are encrypted at rest using AES-256 via AWS KMS customer-managed keys (`alias/meridian-datadog-archive-key`). Log forwarding to our SIEM is via TLS 1.3. |
| **TC-MON-07** | AI Human-Override Probe | For all Clinical AI Platform services in the EU environment, a specific synthetic probe validates the `/override` API endpoint returns HTTP 200. Failure of this probe triggers a Sev-1 alert, as this constitutes a loss of the human oversight mechanism required under EU AI Act Article 14. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

These metrics are continuously tracked and reported monthly. Any indicator trending negatively for two consecutive reporting periods triggers a mandatory Corrective Action Plan (CAP) owned by the Director, Infrastructure Operations.

| KPI ID | Metric | Tier-1 Target | Tier-2 Target | Measurement Tool |
|---|---|---|---|---|
| **KPI-AVAIL-01** | System Uptime | ≥ 99.95% (rolling 30d) | ≥ 99.90% (rolling 30d) | Datadog SLA-Calculator |
| **KPI-DETECT-01** | Mean Time to Detect (MTTD) — Automated | < 2 minutes | < 5 minutes | PagerDuty Analytics |
| **KPI-DETECT-02** | Mean Time to Detect (MTTD) — Manual | < 15 minutes | < 30 minutes | Incident Postmortem |
| **KPI-ACK-01** | Mean Time to Acknowledge (MTTA) | < 1 minute (Sev-1); < 5 min (Sev-2) | < 15 min | PagerDuty Analytics |
| **KPI-RESOLVE-01** | Mean Time to Resolve (MTTR) | < 60 minutes | < 240 minutes | PagerDuty Analytics, Incident Record |
| **KPI-ALERT-01** | False Positive Alert Rate | < 2% of all alerts | < 5% | Datadog -> PagerDuty correlation |
| **KPI-POSTMORT-01**| Postmortem Completion SLA | 5 business days for Sev-1/Sev-2 | N/A | Jira (Postmortem Action Items) |

### 7.2 Reporting Cadence

| Report Name | Audience | Content | Frequency | Owner |
|---|---|---|---|---|
| **Daily NOC Health Digest** | VP, IT Ops; Dir, Infra Ops; CISO; SRE Leads | Summary of last 24h: open incidents, critical alerts, upcoming maintenance. | Daily (08:00 UTC) | NOC Lead |
| **Weekly Operations Review Deck** | VP, IT Ops; Dir, Infra Ops; VP of Engineering (David Park) | Trailing 7-day uptime, incident review, error budget consumption, CAP status. | Weekly (Monday, 10:00 ET) | Dir., Infra Ops |
| **Monthly SLA Compliance Report** | VP of Customer Operations (Michael Chang); Legal; Compliance | Verified uptime for customer-facing SLAs, breach notifications, remedy status. | Monthly (by 5th business day) | VP, IT Ops (Samantha Torres) |
| **Quarterly SOC 2 Availability Evidence Package** | External Auditors (via CCO) | Finalized Monthly SLA Reports, Quarterly Monitoring Review sign-off (AC-MON-01), Postmortem completion records. | Quarterly (by 10th business day after quarter-end) | CCO (Thomas Anderson) |
| **Semi-Annual Board Report** | Board of Directors, AI Governance Committee | Executive summary of availability KPIs, significant incidents, error budget health, and progress on monitoring maturity. | Semi-Annually (Q2, Q4) | VP, IT Ops (Samantha Torres) |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

Any request for temporary or permanent deviation from the standards defined in this SOP must be formally documented, risk-assessed, and approved.

**Procedure:**
1. **Submission:** The requestor submits a "Policy Exception Request" ticket in Jira Service Management (Project: "GRC-Exceptions"). The submission includes:
   - Specific SOP section(s) from which deviation is requested.
   - Business justification for the exception.
   - Scope and duration of the exception (temporary exceptions cannot exceed 90 days without re-approval).
   - Compensating controls proposed to mitigate risk during the exception period.
2. **Risk Assessment:** Within 5 business days, the CISO (Rachel Kim) and CCO (Thomas Anderson) complete a joint risk assessment, documenting the residual risk level (Low/Medium/High/Critical).
3. **Approval Authority:**
   - **Low/Medium Risk, Temporary (≤30 days):** Approved by Director, Infrastructure Operations.
   - **Medium Risk, Temporary (>30 days), or any High Risk:** Approved jointly by VP of IT Operations (Samantha Torres) and VP of Engineering (David Park).
   - **Critical Risk or Permanent Exception:** Approved jointly by VP of IT Operations, VP of Engineering, CISO, and CCO.
4. **Registration:** Approved exceptions are logged in the "Active Exceptions Register" in the GRC platform (Vanta). The register is reviewed quarterly by the CCO.
5. **Expiration and Renewal:** The requestor is notified 14 days before an exception expires. If an exception needs renewal, a new request with an updated justification must be submitted. No more than two consecutive renewals are permitted for a single exception before a permanent fix must be scheduled on the engineering roadmap.

### 8.2 Escalation Matrix

| Issue | Primary Contact | Escalation (if unresolved in SLA) | Final Escalation |
|---|---|---|---|
| Unacknowledged Sev-1 Page (MTTA >1 min) | On-call SRE | NOC Lead → Director, Infra Ops | VP, IT Ops (Samantha Torres) |
| Error Budget Exhaustion | Director, Infra Ops | VP, IT Ops | VP of Engineering (David Park); Board AI Committee |
| Monitoring Tool Outage (e.g., Datadog unavailable) | NOC Lead (initiates manual monitoring per runbooks) | Director, Infra Ops | VP, IT Ops; CISO |
| Customer Dispute over SLA Claim | VP, IT Ops | VP of Customer Operations (Michael Chang) | General Counsel (Maria Gonzalez) |
| Refusal to Comply with Postmortem Action | Director, Infra Ops | VP, IT Ops | VP of Engineering (David Park); CCO for compliance risk |

---

## 9. Training Requirements

All personnel assigned to roles in Section 3 with responsibilities under this SOP must complete mandatory training.

### 9.1 Training Curriculum

| Training Module | Method | Duration | Target Audience | Owner |
|---|---|---|---|---|
| **SOP-ITOP-009 Awareness & Attestation** | Self-paced eLearning (LMS) + Okta Attestation | 30 mins | All NOC, SRE, Eng Managers, Compliance | Dir., Infra Ops |
| **Datadog Monitoring Operations Bootcamp** | Instructor-led (virtual/lab) | 4 hours | New NOC Engineers, New SREs | SRE Team Lead |
| **Practical Incident Response & PagerDuty Drill** | Simulated incident (live-fire drill) | 2 hours | All NOC, SRE (annual refresher) | NOC Lead |
| **Blameless Postmortem Facilitation** | Workshop | 2 hours | Incident Commanders, SRE Leads | Dir., Infra Ops |

### 9.2 Training Frequency and Tracking

- **Onboarding:** All training modules must be completed within the first 5 business days of assignment. System access (Datadog, PagerDuty, Jira) is gated on completion.
- **Annual Refresher:** The "Practical Incident Response & PagerDuty Drill" must be completed annually by all NOC and SRE staff.
- **Just-in-Time Training:** When a new synthetic test tool or monitoring capability is introduced, a short (30-minute) targeted training session is delivered to the NOC team by the SRE team.
- **Tracking:** Training completion records are mandatory evidence for SOC 2 (TSC CC1.2). Records are stored in the Learning Management System (Workday Learning) and automatically synchronized to the GRC platform (Vanta) via API.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs & Policies

| Document ID | Title | Relationship |
|---|---|---|
| **SOP-ITOP-001** | Incident Response Management | Defines Major Incident declaration, war room procedures, and communications playbooks referenced in §5.2 and §5.5. |
| **SOP-ITOP-005** | Change Management for Production Systems | Governs the approval and rollback of changes that may impact availability. Planned maintenance (§5.3) must comply with this SOP. |
| **SOP-BCP-001** | Business Continuity & Disaster Recovery Plan | Defines RTO/RPO for all tiers. DR failover tests are executed per this plan; availability during failover is governed by this SOP. |
| **SOP-SEC-007** | Security Incident Response Plan | For availability incidents caused by security events (e.g., DDoS), this plan is activated in parallel. |
| **SOP-ITOP-014** | Endpoint Management | Out of scope for this SOP, but referenced for completeness in §1.2. |
| **HR-POL-102** | Employee Handbook & Disciplinary Policy | Referenced for non-compliance consequences. |
| **SOP-PRIV-003** | PHI Breach Notification | If an availability incident involves confirmed or suspected PHI access disruption or exposure, this SOP is activated by the CISO. |

### 10.2 External Standards & Regulatory References

| Standard/Regulation | Relevant Articles/Sections | Applicability |
|---|---|---|
| **AICPA SOC 2 TSC (2017)** | CC1.2, CC5.2, A1.1, A1.2, A1.3 | Core control framework for the Meridian SaaS Platform. |
| **ISO/IEC 27001:2022** | A.5.29 (Information security during disruption), A.8.8, A.8.16 | Informational reference mapping; Meridian's ISMS is aligned but certification is in-progress. |
| **NIST AI 100-1 (AI RMF)** | Govern 2.0, Map 2.2 | AI system monitoring overlay referenced in §4.6. |
| **EU AI Act (Regulation 2024/1689)** | Article 14 (Human Oversight), Article 15 (Accuracy, Robustness, Cybersecurity) | Applies to Clinical AI Platform availability monitoring. |
| **HIPAA Security Rule** | 45 CFR § 164.308(a)(7) (Contingency Plan), § 164.312(b) (Audit Controls) | Indirect applicability; PHI data pipeline monitoring is included. |
| **FedRAMP (SRG rev.5)** | CA-7 (Continuous Monitoring), CP-8 (Telecommunications Services) | Reference only; Meridian holds Moderate ATO for government-cloud offering (covered under subsidiary SOP, aligned with this SOP). |

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
|---|---|---|---|
| **1.0** | 2023-03-15 | J. Miller (Prev. Dir., Infra Ops) | Initial release. Established foundational monitoring and SLA framework. |
| **1.1** | 2023-09-22 | L. Chen (SRE Lead) | Minor revision. Added synthetic transaction georedundancy (§6.2 TC-MON-01). Updated PagerDuty escalation policies for new Singapore NOC. |
| **1.2** | 2024-02-10 | M. Okonkwo (GRC Analyst) | Revised Section 6 to align with SOC 2 Type II audit feedback. Added AC-MON-02 (Annual SOP Attestation) control. Updated reporting cadence table. |
| **2.0** | 2025-01-20 | Samantha Torres (VP, IT Ops) | Major revision. Added EU AI Act compliance overlay (§4.6, TC-MON-07). Integrated Error Budget governance framework. Migrated to Monitor-as-Code with Terraform. Established Board AI Governance Committee reporting. |
| **2.1** | 2025-08-25 | Samantha Torres (VP, IT Ops) & David Park (VP of Engineering) | Post-DR Test revision. Recalibrated MTTA thresholds for Sev-1/Sev-2. Updated Azure DR inclusion in scope table. Revised exception renewal limits. Annual review completed. |

---

**APPENDIX A: Monitoring Onboarding Request (Form Template)**

| Field | Instructions |
|---|---|
| **Product/Service Name** | Official name as it appears in the service catalog. |
| **Criticality Tier** | Tier 1 (Critical), Tier 2 (High), or Tier 3 (Moderate) based on Business Impact Analysis. |
| **Go-Live Date** | Target date for production launch (YYYY-MM-DD). Must be ≥10 business days from ticket submission. |
| **Primary Engineering Contact** | Product Engineering Manager name, email, Slack handle. |
| **Critical User Journeys (CUJs)** | List of user-facing journeys that define "available" for this system. (e.g., "Clinician runs inference on chest X-ray," "Patient submits payment"). |
| **Expected Peak Traffic** | Requests per second (RPS) during peak window. |
| **Environment URLs** | List all production endpoints (URLs, ports). |
| **Authentication Requirements** | Does the synthetic test agent need to authenticate? (Yes/No). If Yes, attach a securely shared test credential via 1Password. |
| **Custom Health Check endpoints** | Any non-standard health check endpoints? Provide paths (e.g., `/api/v2/status/database`). |
| **Known Fragile Dependencies** | Any downstream dependencies known to be unstable that SRE should be aware of for runbook planning? |
| **Human-Override Interface** | (For AI Systems only per EU AI Act) Provide the API path for the human override endpoint. |

*Form submitted via Jira Service Management ("ITOps-Monitoring" project) with this content in the Description field. Submitter must sign the ticket to certify information is accurate.*