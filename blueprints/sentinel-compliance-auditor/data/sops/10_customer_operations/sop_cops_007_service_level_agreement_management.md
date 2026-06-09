---
sop_id: "SOP-COPS-007"
title: "Service Level Agreement Management"
business_unit: "Customer Operations"
version: "4.6"
effective_date: "2025-09-28"
last_reviewed: "2026-03-07"
next_review: "2026-09-07"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Service Level Agreement Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for the definition, negotiation, implementation, monitoring, reporting, and continuous improvement of Service Level Agreements (SLAs) across all Meridian Health Technologies, Inc. business lines and product offerings. The SOP ensures that contractual commitments to customers are met consistently, that operational performance is transparently measured, and that service degradation events are managed in accordance with the organization's regulatory obligations, particularly those established under the SOC 2 Type II trust services criteria.

This document serves as the authoritative reference for all personnel involved in the SLA lifecycle, from pre-sales scoping through contract execution, operational delivery, and periodic service reviews. It codifies the processes required to demonstrate to auditors, regulators, and customers that service commitments are systematically made and kept, aligning with the Availability, Processing Integrity, and Confidentiality criteria of SOC 2.

### 1.2 Scope

This SOP applies to:

- All contractual SLAs established between Meridian Health Technologies and its customers, including healthcare provider organizations, payer entities, and channel partners
- The following Meridian business lines and their underlying technology platforms:
    - **Clinical AI Platform**: Inference API availability, model response latency, adverse event alert delivery timeliness
    - **HealthPay Financial Services**: Payment processing availability, transaction authorization latency, claims adjudication response time, lending decision turnaround
    - **MedInsight Analytics**: Dashboard availability, data refresh frequency, cohort analysis query performance
    - **Meridian SaaS Platform**: Infrastructure uptime, API gateway availability, disaster recovery (DR) failover timing, tenant environment provisioning
- Internal Operational Level Agreements (OLAs) between Meridian teams that underpin customer-facing SLAs
- Third-party vendor agreements where vendor performance directly impacts Meridian's ability to meet its customer SLAs
- All production environments hosted within AWS (us-east-1, eu-west-1) and Azure DR regions
- All personnel within Customer Operations, IT Operations, Engineering, Product Management, and Legal departments who participate in SLA definition, delivery, or management

This SOP does not apply to pre-release products governed by beta agreements or non-production environments, unless such environments are explicitly referenced in a customer's contractual uptime guarantee.

### 1.3 Regulatory Alignment

This SOP is designed to support Meridian's compliance with the following frameworks and regulations:

- **SOC 2 Type II (2025 Trust Services Criteria)**: Specifically addresses CC2.2 (Communication of Service Commitments), CC4.0 (Monitoring of Controls), A1.1 (Availability Commitments), and PI1.3 (Processing Integrity Monitoring)
- **HIPAA**: Ensures SLA-related monitoring does not compromise the privacy or security of Protected Health Information (PHI)
- **GDPR**: Requires that SLA reporting mechanisms do not expose personal data without appropriate legal basis
- **EU AI Act**: Mandates transparency commitments for high-risk AI systems, including Clinical AI Platform uptime and latency targets

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Service Level Agreement (SLA)** | A documented, contractual commitment between Meridian and a customer that defines the expected level of service, measured through specific metrics, with prescribed remedies for non-performance. |
| **Operational Level Agreement (OLA)** | An internal commitment between Meridian teams (e.g., Network Operations and Database Administration) that defines performance targets required to meet customer-facing SLAs. |
| **Underpinning Contract (UC)** | A formal agreement with a third-party vendor that defines the service levels Meridian requires to meet its own obligations. Governed by SOP-PROC-014 (Vendor Risk Management). |
| **Service Credit** | A financial remedy provided to a customer when a committed SLA is breached, typically calculated as a percentage of monthly recurring fees, applied as a credit against future invoices. |
| **Availability** | The percentage of time a service is accessible and functional, measured over a defined measurement window (e.g., monthly, quarterly, annually), excluding Planned Maintenance and Excluded Events. |
| **Planned Maintenance Window** | Pre-scheduled periods during which Meridian may perform upgrades, patches, or infrastructure changes that may impact service availability. Defined in the customer's MSA and Service Order, typically communicated 7 calendar days in advance. |
| **Emergency Maintenance** | Unscheduled maintenance required to address a critical security vulnerability, prevent imminent system failure, or respond to a Priority 1 (P1) incident. Communication to affected customers occurs concurrently with the maintenance action. |
| **Incident** | Any event that causes, or may cause, an interruption to, or a reduction in, the quality of an agreed service. Managed per SOP-IM-003 (Incident Management). |
| **Measurement Window** | The calendar period over which SLA attainment is calculated (default: calendar month). |
| **Excluded Events** | Circumstances beyond Meridian’s reasonable control that result in service degradation, as contractually defined. Examples include: customer-side network failures, force majeure events (per MSA Section 12.2), denial-of-service attacks not attributable to Meridian’s security posture. |

### 2.2 Acronyms

| Acronym | Meaning |
|---|---|
| **BA** | Business Availability (a composite metric) |
| **BCP** | Business Continuity Plan (see SOP-BCP-002) |
| **CSM** | Customer Success Manager (primary customer advocate within Meridian) |
| **DR** | Disaster Recovery |
| **MTBF** | Mean Time Between Failures |
| **MTTR** | Mean Time to Resolution (measured from Incident declaration to service restoration) |
| **OLA** | Operational Level Agreement |
| **PMW** | Planned Maintenance Window |
| **QBR** | Quarterly Business Review |
| **RPO** | Recovery Point Objective |
| **RTO** | Recovery Time Objective |
| **SLO** | Service Level Objective (an internal target, typically set higher than the customer-facing SLA) |
| **SLI** | Service Level Indicator (a specific, quantifiable measure of a service characteristic) |
| **Uptime** | The aggregate period during which the service is operational and accessible |

---

## 3. Roles and Responsibilities

The following Responsibility Assignment Matrix (RACI) details the participation of each role in the SLA management lifecycle. (R = Responsible, A = Accountable, C = Consulted, I = Informed)

| Activity / Decision | VP, Customer Ops (M. Chang) | VP, Financial Services (R. Liu) | Customer Success Manager | VP, Engineering | Legal & Contract Mgmt | Incident Commander | Service Owner (Product) |
|---|---|---|---|---|---|---|---|
| **SLA Definition & Scoping** | A | A | R | C | C | I | C |
| **Contractual SLA Final Approval** | A | A | C | C | R | I | C |
| **SLA Monitoring & Dashboard Setup** | I | I | C | C | I | I | R |
| **Monthly SLA Report Generation** | I | I | R | I | I | I | C |
| **SLA Breach Declaration** | C | C | R | I | C | R | I |
| **Customer Communication (Breach)** | C | I | R | I | C | I | C |
| **Service Credit Calculation & Approval** | A | A | R | I | C | I | I |
| **OLA Negotiation (Internal)** | C | I | R | C | I | I | C |
| **Continuous Service Improvement** | A | C | R | R | I | I | R |
| **SOC 2 Evidence Collection** | R | I | C | I | I | I | C |

### 3.1 Detailed Role Descriptions

**Michael Chang, VP of Customer Operations (SOP Owner):** Provides executive oversight of the SLA Management program. Approves the annual SLA review and is the primary signatory for material changes to standard SLA templates. Acts as the executive escalation point for persistent SLA breach disputes.

**Robert Liu, VP of Financial Services (SOP Approver):** Approves the financial governance framework for service credits. Ensures that SLA breach liabilities are accurately captured in financial reporting and that credit issuance aligns with the company's revenue recognition policies.

**Customer Success Manager (CSM):** Assigned to each customer account. Owns the operational SLA relationship, including monthly report delivery, QBR preparation, breach notification drafting (in coordination with Legal), and service credit processing. The CSM serves as the customer's primary point of contact for all SLA-related inquiries.

**VP of Engineering:** Ensures the architectural and operational capabilities of Meridian's platforms can meet or exceed committed SLAs. Owns the investment and resource allocation for reliability engineering, observability tooling (currently Datadog and PagerDuty), and capacity planning.

**Legal & Contract Management Team:** Reviews all customer-specific SLA amendments that deviate from standard templates. Advises on liability caps, contractual remedy language, and regulatory considerations (especially GDPR and CE marking requirements under EU MDR). Maintains the central repository of executed Service Orders within Salesforce.

**Incident Commander (rotational role):** During active P1 incidents (per SOP-IM-003), declares the precise start and end times of a service degradation event. Their time-stamped declaration within PagerDuty triggers the SLA breach determination workflow.

**Service Owner (Product-specific):** For each business line, a designated Service Owner (e.g., Director of Clinical AI) is accountable for the technical delivery of the service against its defined SLIs. They triage and approve Planned Maintenance Window requests and coordinate with the CSM on customer-impacting changes.

---

## 4. Policy Statements

Meridian Health Technologies commits to the following policy positions:

1.  **Commitment Integrity:** All external SLAs will be technically validated by the responsible Service Owner and VP of Engineering prior to being offered to a customer. No SLA will be contractually committed that the current platform architecture cannot demonstrably sustain.

2.  **Transparent Measurement:** SLA attainment will be measured using objective, automated monitoring systems (Datadog monitors, AWS CloudWatch, and custom health-check probes). Manual manipulation of SLA data is strictly prohibited and constitutes a violation of the Code of Conduct.

3.  **Uniform Remedy:** The standard remedy for a breach of an Availability SLA shall be a Service Credit calculated as a percentage of the monthly recurring fee for the impacted service, unless a customized remedy is explicitly approved by Legal and the VP of Customer Operations. The standard credit table is defined in Section 5.2.

4.  **Constructive Customer Communication:** All SLA breach notifications will be delivered to the customer's designated administrative contact within the contractually specified timeframe (standard: 5 Business Days from breach identification). Communication will include a root cause summary, corrective actions taken, and a calculation of applicable credits.

5.  **Internal Accountability:** External SLAs will be translated into internal OLAs. Teams failing to meet internal OLAs will participate in a mandatory post-incident review, documented via the Problem Management process (SOP-PM-004).

6.  **Planned Maintenance Transparency:** Planned Maintenance impacting availability will be scheduled and communicated according to the contractual terms (standard: weekly 2-hour window, Sundays 02:00-04:00 UTC). No single Planned Maintenance event will exceed 120 minutes without a customer-specific exception approval.

---

## 5. Detailed Procedures

### 5.1 SLA Definition and Contracting

The purpose of this procedure is to ensure that SLA commitments are appropriately scoped, technically feasible, approved, and accurately embedded within the customer’s Master Services Agreement (MSA) and Service Order.

**Steps:**

1.  **Pre-Sales Discovery:** The assigned Sales Representative and Solutions Architect gather the prospect’s business requirements and critical workflows. They identify the Meridian services to be purchased.

2.  **SLA Scoping Request:** The Sales Representative initiates a formal SLA Scoping Request via Jira (Project: `COPS`, Issue Type: `SLA Scoping`). The request must contain:
    -   Customer Name and proposed Service(s)
    -   Proposed Uptime target (if requested above 99.9%)
    -   Critical customer workflows and peak usage periods
    -   Any unique latency or throughput requirements

3.  **Technical Feasibility Assessment:** The Jira ticket is automatically assigned to the relevant Service Owner(s). The Service Owner has **3 Business Days** to assess the request against current platform SLOs and historical performance data (sourced from Datadog dashboards, minimum trailing 90-day data). The response will indicate: "Standard SLA Feasible," "Requires Custom SLA Engineering Review" (escalated to VP of Engineering), or "Not Feasible."

4.  **Legal & Pricing Review:** Upon a "Feasible" determination, the Contract Manager drafts the SLA schedule using the approved template clause library within Conga Composer (from Salesforce). Any deviation from standard clauses requires a markup review with Legal.

5.  **Final Order Approval:** The final Service Order, complete with the SLA schedule, is routed for approval via Salesforce CPQ workflow. Required approvers: Sales Director > VP of Financial Services (for Total Contract Value > $250,000 or custom credit terms) > Legal Counsel > VP of Customer Operations (for Uptime commitments ≥ 99.99%).

6.  **Post-Execute Setup:** Within **5 Business Days** of contract execution, the CSM creates a customer-specific SLA dashboard in Datadog (using the `SLA Dashboard Template v4.6`) and a corresponding SLA Tracker in Salesforce. They validate that all contracted SLIs are being accurately captured.

### 5.2 Service Level Objectives (SLOs) and Service Credits

The following table defines Meridian’s standard SLOs, which are set strictly higher than the contracted SLA to provide an internal buffer before customer impact. The Service Credit table represents the standard contractual remedy.

**Meridian SaaS Platform (AWS us-east-1 Primary Region)**

| Metric | Internal SLO (OPS target) | Standard Contractual SLA | Measurement |
|---|---|---|---|
| Core Application Availability | 99.99% | 99.90% | Monthly uptime (minutes) |
| API Gateway Availability | 99.99% | 99.90% | Monthly successful HTTP 200 responses vs. total valid requests |
| Tenant Provisioning (New) | < 4 Hours | < 8 Business Hours | Time from signed order to active environment |

**Clinical AI Platform**

| Metric | Internal SLO | Standard Contractual SLA | Measurement |
|---|---|---|---|
| Inference API Availability | 99.95% | 99.50% | Monthly uptime |
| P95 Inference Latency (single model) | < 200ms | < 500ms | Client-side timer in SDK, aggregate dashboard |
| Adverse Event Alert Delivery | 99.99% event delivery < 60 sec | 99.90% delivery < 5 min | Alert generation timestamp to customer webhook acknowledgment |

**HealthPay Financial Services**

| Metric | Internal SLO | Standard Contractual SLA | Measurement |
|---|---|---|---|
| Payment Gateway Availability | 99.99% | 99.95% | Monthly uptime |
| P95 Auth Latency | < 0.8 sec | < 2.0 sec | Gateway timestamp to issuer response |
| Claims Adjudication API | 99.95% | 99.50% | Monthly uptime |

**Standard Service Credit Schedule (Availability Breaches)**

| Monthly Uptime Percentage | Service Credit (% of Monthly Fee) |
|---|---|
| ≥ 99.90% (meets SLA) | 0% |
| 99.89% – 99.00% | 5% |
| 98.99% – 97.00% | 15% |
| 96.99% – 95.00% | 25% |
| Below 95.00% | 40% (Customer may also have right to terminate for material breach, per MSA) |

### 5.3 Planned Maintenance Communication

Maintenance that requires service interruption is managed through the following procedure:

1.  **Maintenance Request:** Engineering submits a Change Request (per SOP-CM-008) including a clear statement of expected customer impact.
2.  **CSM Impact Review:** The CSM, upon receiving the approved change notice **10 days** prior to the proposed window, reviews the list of impacted customers.
3.  **Customer Notification:** The CSM issues a formal Planned Maintenance Notice via the customer's registered email. The notice includes:
    -   Start and End Time (in UTC and Customer's local TZ)
    -   Description of the work (e.g., "Database Instance Upgrade to v16")
    -   Expected impact (e.g., "Dashboard analytics will be in read-only mode; all transaction services remain fully operational")
    -   Link to the Meridian Trust Center status page for real-time updates
4.  **Exemption Handling:** If a customer objects that the window conflicts with a business-critical event (e.g., annual open enrollment), the CSM will facilitate negotiation of an alternative window with the Service Owner. The VP of Customer Operations is the escalation point for unresolvable disputes.

### 5.4 Breach Identification and Declaration

This procedure is triggered when a monitoring alert indicates a threshold breach or an Incident Commander declares a service degradation event whose duration pushes a metric below the contractual SLA.

1.  **Automated Threshold Alert:** A Datadog monitor transitions to a `CRITICAL` or `ALERT` state when a metric threshold (defined at the SLO level) is crossed.
2.  **Incident Commander Validation:** The on-call Incident Commander (IC) acknowledges the alert in PagerDuty. They verify the alert is not a false-positive monitoring artifact. The time the IC declares a "Confirmed Service Degradation" in the PagerDuty incident log is recorded as the `SLA_Impact_Start_Time`.
3.  **Incident Resolution:** Per SOP-IM-003, the IC drives the incident to resolution. The moment the IC declares the incident `Resolved` and confirms the service is fully operational (validated via synthetic health checks), PagerDuty records the `SLA_Impact_End_Time`.
4.  **Automated SLA Breach Calculation:** Within **1 hour** of incident resolution, the Meridian Integration Hub (MuleSoft) queries the PagerDuty API for the incident timeline. It computes the total downtime minutes for the Measurement Window and determines if any customer’s contractual SLA was breached. If a breach is calculated, it automatically generates an **SLA Breach Record** in Salesforce, attached to the relevant Customer Account.
5.  **CSM Review and Submission:** The assigned CSM receives a Slack notification (`#slabreach-alerts` channel) of a new record. The CSM reviews the incident postmortem notes and technical details within **1 Business Day**. They update the SLA Breach Record with a customer-ready summary and submit it for approval to the VP of Customer Operations and Legal.

### 5.5 Customer Communication and Remediation

1.  **Draft Communication:** Upon submitting the SLA Breach Record for approval, the CSM generates a draft Customer SLA Breach Notification using the standard `SLA-Breach-Notification` Salesforce email template.
2.  **Approval:** The notification must be approved by Legal (if it contains admissions of fault or customized language) or the VP of Customer Operations (for standard financial remediation).
3.  **Delivery:** The approved notification is sent to the customer’s designated administrative and executive contacts no later than **5 Business Days** from the `SLA_Impact_End_Time`.
4.  **Service Credit Issuance:** The CSM creates a Service Credit memo attached to the customer’s Account record. Finance applies the credit against the next billing cycle. A confirmation of the credit application is sent to the customer.

### 5.6 Quarterly Service Review (QSR)

Each CSM conducts a formal Quarterly Service Review for assigned customers with an Annual Contract Value (ACV) exceeding $50,000.

1.  **Report Generation:** The CSM uses the Meridian Analytics Platform (MAP) to pull the "QSR Pack" for the quarter. This standardized report includes:
    -   SLA Performance Dashboard (actual vs. target for each contracted metric).
    -   Incident Volume and Trend Analysis (total, Mean Time to Acknowledge, Mean Time to Resolve).
    -   Planned Maintenance Summary.
    -   Open Problem Management cases (SOP-PM-004) impacting the customer.
2.  **Internal Pre-Brief:** The CSM, Service Owner, and Lead Engineer meet internally to review the data and align on key messages, upcoming capacity plans, and any unresolved pain points.
3.  **Customer Presentation:** The CSM presents the QSR via a scheduled video conference. A PDF copy of the presentation and underlying data is provided to the customer within **24 hours** of the meeting.
4.  **Action Logging:** Any follow-up action items, service improvement requests, or feature requests raised during the QSR are logged as Jira tasks and tracked through to completion.

---

## 6. Controls and Safeguards

The following controls are implemented to ensure the integrity, availability, and confidentiality of the SLA Management process, directly supporting SOC 2 criteria.

### 6.1 Administrative Controls

| Control ID | Control Description | SOC 2 Criteria Mapping |
|---|---|---|
| **SLA-AC-01** | **Annual SLA/SLO Review:** The VP of Customer Operations and VP of Engineering will conduct a formal review of all standard SLOs and SLAs against a trailing 12-month performance dataset. Findings and adjustments are documented in the SOP-COPS-007 revision history. | CC2.2, CC4.0 |
| **SLA-AC-02** | **Segregation of Duties:** Personnel who create SLA performance dashboards are distinct from personnel who approve financial credits and those who resolve incidents. Datadog dashboard edit permissions are restricted to the Observability Team and VP of Engineering designees, not CSMs. | CC4.0 |
| **SLA-AC-03** | **Vendor SLA Pass-Through:** All underpinning contracts with critical vendors (AWS, MuleSoft, PagerDuty) must include SLAs that are at least as stringent as those Meridian offers its own customers. The VP of Engineering reviews these annually. The primary AWS Business Support plan (sub-60-second P1 response) underpins our cloud SLAs. | CC9.1, CC9.2 |
| **SLA-AC-04** | **QSR Mandate:** Completion of quarterly service reviews for qualifying accounts is a mandatory performance objective for CSM roles. Compliance is tracked through Salesforce activity records. | CC2.1 |

### 6.2 Technical Controls

| Control ID | Control Description | SOC 2 Criteria Mapping |
|---|---|---|
| **SLA-TC-01** | **Automated Uptime Monitoring:** Global, high-frequency synthetic tests (every 30 seconds from three geographically diverse AWS regions) simulate customer login and critical-path transactions (e.g., submission of a sample payment or inference job). Failures are the primary data source for uptime calculation. | A1.1, PI1.3 |
| **SLA-TC-02** | **Immutable Metric Logs:** Raw metric data feeding SLA calculations is streamed from Datadog to an immutable, append-only Amazon S3 bucket with WORM (Write Once, Read Many) policy enabled. Logs are retained for a minimum of 3 years. This ensures the integrity of the single source of truth for SLA data. | PI1.3, CC6.1 |
| **SLA-TC-03** | **PII/PHI Redaction in Reports:** The QSR report generation pipeline (`MAP -> Salesforce`) includes a mandatory redaction script. No PHI (as defined under HIPAA) or PII (as defined under GDPR) is permissible in SLA Performance Dashboards or QSR presentations. The Incident postmortem data is a sanitized subset of the full incident log. | C1.2, P1.1 |
| **SLA-TC-04** | **Change-Impact Correlation:** A dashboard correlates approved Change Requests (SOP-CM-008) with service degradation events. This control allows for rapid determination of whether a breach was caused by a routine, authorized change, aiding root cause analysis and customer communication. | CC8.2 |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The VP of Customer Operations will review the following program-level KPIs on a monthly operational review call:

| KPI | Target | Measurement Tool | Owner |
|---|---|---|---|
| **Aggregate SLA Attainment (% of contracts meeting all SLAs each month)** | ≥ 99.5% | Salesforce (Aggregate of SLA Breach Records) | Michael Chang |
| **SLA Breach Notification Timeliness (% sent within 5 Business Days)** | 100% | Salesforce Report `SLA-COPS-007-Notification` | Michael Chang |
| **Service Credit Processing Time (Mean hours from breach record approval to memo issuance)** | < 8 Business Hours | Finance / Salesforce | Robert Liu |
| **OLA Attainment (% of internal teams meeting their OLAs)** | ≥ 95.0% | Jira / Datadog SLO Dashboard `Internal-OLAs` | VP of Engineering |
| **QSR Completion Rate (% of eligible accounts with documented, completed QSRs in quarter)** | 100% | Salesforce | Michael Chang |

### 7.2 Real-Time Dashboards

- **Executive SLA Dashboard:** A high-level Datadog Screenboard showing live health status (Green/Yellow/Red) for all major production services against their SLOs. Displayed on the IT Operations Command Center monitor.
- **Customer-Facing Status Page:** Powered by Atlassian Statuspage, displaying current service status and scheduled maintenances for all public-facing Meridian services.
- **CSM SLA Compliance Dashboard:** A Salesforce-native dashboard showing, per CSM, the list of their assigned accounts with a traffic-light status for each contracted SLA metric.

### 7.3 Periodic Reports

| Report | Frequency | Audience | Owner | Content |
|---|---|---|---|---|
| **Monthly SLA Performance Brief** | Monthly | CEO, CFO, VP of Engineering | Michael Chang | Summary of all SLA breaches, service credits issued, KPI status, and material OLA misses. |
| **Quarterly Service Review (QSR) Pack** | Quarterly | Individual Customers | CSM | Full QSR presentation (see Section 5.6). |
| **Annual SLA / SOP-COPS-007 Review Report** | Annually | Audit Committee, External SOC Auditors | Michael Chang | Trailing 12-month performance, proposed SLA/SLO changes, control self-assessment results, and summary of any exceptions. |

---

## 8. Exception Handling and Escalation

### 8.1 Service Credit Exception

A customer may request a form of remediation other than a service credit (e.g., a period of free service for a new feature). The assigned CSM assesses the request and drafts a proposed alternative. Approval authority follows a tiered model:

- **Value < $5,000 USD equivalent:** CSM Manager and Service Owner approval.
- **Value $5,000 - $50,000 USD equivalent:** VP of Customer Operations and VP of Financial Services joint approval.
- **Value > $50,000 USD equivalent:** C-Suite (CEO or CFO) approval.

All exceptions are documented within the Salesforce SLA Breach Record and reported on the annual review report.

### 8.2 Excluded Event Determination

If a service degradation event is suspected to be caused by an Excluded Event (e.g., a massive customer-side network configuration error or a documented force majeure), the Incident Commander follows the standard incident timeline. The CSM, with Legal counsel, determines the applicability of contractual exclusions. This determination must be made and communicated to the customer within the standard 5-Business Day notification window. A contested determination is escalated to the VP of Customer Operations and General Counsel for final decision.

### 8.3 Escalation Path for Customer Service Disputes

If a customer disputes the reported SLA metrics, severity assessment, or remediation:

1.  **Level 1 (Operational):** CSM works with the Service Owner and Observability team to re-validate raw data from the S3 immutable log. The CSM responds to the customer within **3 Business Days** of dispute lodgement.
2.  **Level 2 (Management):** If the customer remains unsatisfied, the VP of Customer Operations (Michael Chang) engages directly with the customer's executive sponsor. A formal written response will be provided within **5 Business Days**.
3.  **Level 3 (Executive):** The dispute is tabled at an executive meeting between the Meridian CEO and the customer’s executive leadership.

---

## 9. Training Requirements

All personnel assigned to a role identified in the Section 3 RACI matrix must complete the specified training.

| Role(s) | Training Module | Delivery Method | Frequency | Compliance Tracking |
|---|---|---|---|---|
| All Roles | `COPS-007: SLA Foundations and Policy Overview` | LMS (Workday Learning) CBT | On Assignment, Annually thereafter | Workday Learning Record |
| CSM, Incident Commander | `SLA-WORKSHOP: Breach Handling and Customer Communication` | Live Virtual Workshop led by VP of Customer Ops or delegate | Semi-Annually (Q2, Q4) | Salesforce Trail Tracker |
| Service Owners (Product) | `SLA-DASH: SLA Dashboard Customization and SLO Alert Tuning` | Technical Lab Walkthrough with Observability Team | On Assignment, on change | Jira Training Record |
| All Engineers (OLA-impacted) | `SRE-101: OLA Responsibility and Service Reliability Fundamentals` | LMS CBT | On Assignment, Annually | Workday Learning Record |

The VP of Customer Operations is responsible for ensuring training content is reviewed and updated annually, with any material changes communicated within 30 days of a new SOP revision taking effect. A 100% training compliance rate is a standing objective for this program.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| SOP-IM-003 | Incident Management | Governs the incident lifecycle whose timeline directly triggers SLA breach workflows. |
| SOP-PM-004 | Problem Management | Governs the root cause analysis for recurring issues that undermine SLA attainment. |
| SOP-CM-008 | Change Management | Governs the approval and communication of changes that require Planned Maintenance Windows. |
| SOP-SEC-015 | Information Security Incident Response | For SLA-impacting security incidents, this procedure runs in parallel, governing breach disclosure. |
| SOP-PROC-014 | Vendor Risk Management | Governs the establishment and monitoring of Underpinning Contracts with third-parties. |
| SOP-BCP-002 | Business Continuity Planning | Defines RPOs and RTOs for Disaster Recovery, which underpin our high-uptime SLAs. |

### 10.2 External References

-   **AICPA 2025 Trust Services Criteria** (TSP Section 100), specifically Availability (A), Processing Integrity (PI), and the Common Criteria for Communication and Information (CC2.2, CC4.0, CC6.1)
-   **EU MDR 2017/745, Annex I, Chapter II, 17.3** – Requirements related to reliability for CE-marked Clinical AI software
-   Meridian Health Technologies Master Services Agreement (MSA) v9.3, Section 10 ("Service Levels and Credits")

---

## 11. Revision History

| Version | Date | Author / Editor | Change Description |
|---|---|---|---|
| 4.0 | 2025-01-15 | Sarah Jenkins, Sr. CSM | Major revision for SOC 2 Type II alignment. Restructured document into formal procedure sections, added detailed technical and administrative controls, and a new KPI framework. |
| 4.2 | 2025-04-22 | Michael Chang | Post-audit corrective actions. Clarified excluded event handling, added specific AWS S3 WORM control detail, and modified standard Service Credit table percentages for better alignment with financial risk appetite. |
| 4.3 | 2025-06-10 | David Chen, Legal | Updated standard notification templates to ensure compliance with revised EU MDR post-market surveillance language. No procedural changes. |
| 4.5 | 2025-08-18 | Lisa Park, VP of Engineering | Complete technical refresh of Section 6. Updated internal SLOs to reflect 99.99% architecture enhancements. Added MuleSoft Integration Hub workflow for automated breach calculation. |
| 4.6 | 2025-09-28 | Michael Chang | Final annual review. Updated RACI for new rotational Incident Commander role. Added QSR thresholds, new `SLA-SCOPING` Jira workflow detail, and mandatory training compliance targets. Approved for 2026 audit cycle. |