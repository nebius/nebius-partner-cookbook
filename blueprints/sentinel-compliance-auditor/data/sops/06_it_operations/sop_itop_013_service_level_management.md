---
sop_id: "SOP-ITOP-013"
title: "Service Level Management"
business_unit: "IT Operations & Infrastructure"
version: "1.1"
effective_date: "2024-02-05"
last_reviewed: "2025-01-19"
next_review: "2025-07-24"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Service Level Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for defining, negotiating, monitoring, and reporting on service levels across all Meridian Health Technologies, Inc. product lines and supporting infrastructure. The purpose of this document is to ensure that IT services delivered by internal teams and external vendors meet the performance, availability, and responsiveness requirements necessary to support Meridian's business objectives, regulatory obligations, and customer commitments.

Service Level Management (SLM) at Meridian serves as the mechanism by which business expectations are translated into measurable service targets, performance is continuously tracked, and deviations are systematically addressed through structured review cycles and improvement initiatives. This SOP codifies the processes by which Meridian fulfills its availability and performance commitments under SOC 2 Common Criteria 5.1 (Management's Description of the Service Organization's System) and A1.1 (Availability of the System), while simultaneously supporting the operational resilience requirements of the EU AI Act for high-risk AI systems.

### 1.2 Scope

This SOP applies to all technology services delivered by Meridian Health Technologies, including:

| Service Domain | Components Covered | Primary Customers |
|---|---|---|
| Meridian SaaS Platform | AWS cloud infrastructure (us-east-1, eu-west-1), Azure DR environment, networking, authentication services, API gateway | Internal product teams, external customers with platform-level SLAs |
| Clinical AI Platform | AI inference endpoints, model serving infrastructure, diagnostic imaging processing pipelines, patient risk scoring services, adverse event prediction systems | 340+ hospitals and clinics, Clinical AI Products team |
| HealthPay Financial Services | Payment processing engine, claims automation, medical lending platform, credit scoring models, fraud detection systems | Healthcare providers, payers, patients, Financial Services team |
| MedInsight Analytics | Population health analytics platform, care gap identification engine, outcomes prediction services | Health systems, insurers, MedInsight Analytics team |
| Enterprise IT Services | Okta identity management, corporate networks, collaboration tools, endpoint management via CrowdStrike | All Meridian employees globally |
| Data Platform | Snowflake data warehouse, Apache Kafka streaming, PostgreSQL databases, Redis caching, Pinecone vector database | All product teams, MedInsight Analytics |

**In Scope:** All internally managed services, services managed by cloud providers where Meridian controls configuration, and services delivered by third-party vendors under contractual agreements that include service level commitments.

**Out of Scope:** Personal devices not enrolled in Meridian endpoint management, services procured outside the IT Operations procurement process without contractual SLAs, and research prototypes not yet promoted to production environments governed by Meridian's Model Risk Management framework per SR 11-7.

### 1.4 Target Audience

- IT Operations & Infrastructure personnel responsible for service delivery and monitoring
- Product Engineering teams responsible for application-level service performance
- Platform Reliability Engineering (PRE) team members
- Service Desk and Incident Management personnel
- Vendor Management and Procurement teams
- Business Unit leaders accountable for customer-facing SLAs
- Internal Audit and Compliance teams assessing SOC 2 control effectiveness

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Availability** | The percentage of time a service is accessible and operable within defined performance parameters, measured over an agreed period (typically monthly or quarterly). |
| **Business Continuity Plan (BCP)** | A documented strategy for maintaining critical business functions during and after a significant disruption. |
| **Customer Satisfaction (CSAT)** | A qualitative metric measuring customer sentiment regarding service delivery, typically collected via survey mechanisms. |
| **Disaster Recovery Plan (DRP)** | A documented strategy for restoring IT services and infrastructure following a catastrophic event. |
| **Mean Time Between Failures (MTBF)** | The average elapsed time between service interruptions or incidents for a given service component. |
| **Mean Time to Detect (MTTD)** | The average time between the onset of a service-impacting incident and its detection by monitoring systems or human reporting. |
| **Mean Time to Resolve (MTTR)** | The average time between the detection of a service-impacting incident and the full restoration of service to operational parameters. |
| **Operational Level Agreement (OLA)** | An internal agreement between Meridian support teams defining the interdependent service commitments necessary to deliver a customer-facing SLA. |
| **Service Catalog** | A centralized, maintained repository of all active IT services, their descriptions, service owners, current status, and associated SLA targets. |
| **Service Credit** | A financial remedy provided to a customer when a committed SLA target is not met, typically calculated as a percentage of recurring fees. |
| **Service Improvement Plan (SIP)** | A formally documented plan with assigned owners, milestones, and success criteria designed to remediate persistent service level breaches. |
| **Service Level Agreement (SLA)** | A formal, contractual agreement between Meridian and an external customer specifying the quantitative service level targets, measurement methodologies, and remedies for breach. |
| **Service Level Objective (SLO)** | An internal, measurable target for a specific service metric that, when aggregated, defines the overall service level expectation. |
| **Service Level Target (SLT)** | A specific, quantified performance target for a single metric within a defined measurement window. |
| **Service Review** | A periodic, structured meeting between Service Level Management, service owners, and stakeholders to evaluate performance against SLTs, discuss incidents, and track improvement initiatives. |
| **Underpinning Contract (UC)** | A formal agreement with an external vendor or cloud service provider that defines the service commitments upon which Meridian's internal and customer-facing SLAs depend. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **AMI** | Amazon Machine Image |
| **API** | Application Programming Interface |
| **AWS** | Amazon Web Services |
| **AZ** | Availability Zone |
| **BCP** | Business Continuity Plan |
| **CSP** | Cloud Service Provider |
| **CSAT** | Customer Satisfaction |
| **DRP** | Disaster Recovery Plan |
| **EBS** | Elastic Block Store |
| **EC2** | Elastic Compute Cloud |
| **EKS** | Elastic Kubernetes Service |
| **HITL** | Human-in-the-Loop |
| **ITSM** | IT Service Management |
| **KPI** | Key Performance Indicator |
| **MTBF** | Mean Time Between Failures |
| **MTTD** | Mean Time to Detect |
| **MTTR** | Mean Time to Resolve |
| **OLA** | Operational Level Agreement |
| **PRE** | Platform Reliability Engineering |
| **RDS** | Relational Database Service |
| **RPO** | Recovery Point Objective |
| **RTO** | Recovery Time Objective |
| **SIP** | Service Improvement Plan |
| **SLA** | Service Level Agreement |
| **SLM** | Service Level Management |
| **SLO** | Service Level Objective |
| **SLR** | Service Level Report |
| **SLT** | Service Level Target |
| **UC** | Underpinning Contract |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following RACI matrix defines the assignment of responsibilities for key activities within the Service Level Management process:

| Activity | VP, IT Operations (S. Torres) | VP, Engineering (D. Park) | Service Owner (Designated per service) | SLM Process Manager | PRE Team Lead | Product Manager (Designated per product) | Internal Audit |
|---|---|---|---|---|---|---|---|
| SLA Definition and Approval | A | A | R | R | C | C | I |
| SLA Negotiation (Customer-Facing) | C | C | R | R | C | R | — |
| OLA/UC Definition | A | — | R | R | R | I | — |
| Service Catalog Maintenance | A | — | C | R | I | I | I |
| Monitoring Configuration | — | — | R | C | R | C | — |
| Service Level Reporting | A | I | R | R | C | I | I |
| Service Review Facilitation | R | — | C | R | C | C | — |
| Breach Remediation | R | R | A | R | C | I | — |
| Service Improvement Plan Execution | A | A | R | C | R | C | — |
| Exception Approval | R | R | C | C | I | I | — |

**R = Responsible** (executes the work); **A = Accountable** (approves the work, ultimate answerability); **C = Consulted** (provides input before work is done); **I = Informed** (notified after work is complete)

### 3.2 Named Role Descriptions

| Role | Designated Individual / Team | Key Responsibilities |
|---|---|---|
| **Service Level Management Process Owner** | Samantha Torres, VP of IT Operations | Owns this SOP document. Approves SLA templates. Escalation point for persistent SLA breaches. Authorizes Service Improvement Plans requiring cross-functional investment. |
| **SLM Process Manager** | [Designated by VP IT Operations] | Facilitates SLA/OLA negotiation. Maintains Service Catalog. Produces monthly SLR. Facilitates quarterly service reviews. Manages SIP tracking. |
| **Service Owner** | Designated per service (must be a Manager-level or above individual within the team delivering the service) | Accountable for achieving SLTs for assigned service(s). Authors and maintains OLAs. Approves monitoring configurations. Responds to SLA breach incidents. Presents performance at service reviews. |
| **Platform Reliability Engineering (PRE) Team** | PRE Team Lead and engineering staff | Implements observability and monitoring tooling. Configures alerting mechanisms (Datadog, PagerDuty). Supports incident response for platform-level issues. Provides performance data for reporting. |
| **Product Manager** | Designated per product line | Negotiates customer-facing SLAs with commercial counterparts. Communicates customer-impacting incidents. Defines product-level availability requirements. |
| **Internal Audit** | Internal Audit Department | Periodically reviews evidence of SLA monitoring, reporting, and review cadence to assess SOC 2 control effectiveness. |
| **Customer Support Manager** | Designated per product line | Captures customer-reported service degradations not detected by automated monitoring. Feeds CSAT data into service reviews. |

---

## 4. Policy Statements

### 4.1 Service Level Commitment Policy

Meridian Health Technologies is committed to delivering IT services that meet the availability, performance, and responsiveness targets established in customer agreements and internal operating plans. All production services governed by this SOP shall have documented Service Level Targets, approved by the Service Owner and the VP of IT Operations, and reviewed no less frequently than annually. Service level commitments to external customers shall be memorialized in formal Service Level Agreements executed as part of the Master Services Agreement or equivalent contractual instrument.

### 4.2 Measurability and Transparency Policy

All SLTs shall be expressed in quantifiable, measurable terms with clearly defined measurement windows, calculation methodologies, and data sources. Service performance against SLTs shall be reported on a monthly basis via the Service Level Report, which shall be distributed to Service Owners, Product Managers, and the VP of IT Operations. Customer-facing SLA performance reports shall be prepared quarterly for distribution to customers upon request or as contractually specified.

### 4.3 Continuous Improvement Policy

Meridian shall conduct formal service reviews on a quarterly basis for all services subject to external SLAs and semi-annually for all internal services. Any service that breaches a committed SLT in two consecutive measurement periods shall require the development and execution of a formal Service Improvement Plan, approved by the VP of IT Operations and the VP of Engineering. SIPs shall include root cause analysis, corrective actions with assigned owners, implementation milestones, and criteria for closure.

### 4.4 Interdependency Management Policy

All internal support relationships that are critical to the delivery of a customer-facing SLA shall be formalized through Operational Level Agreements. All external dependencies (including AWS, Azure, and SaaS providers) that materially contribute to Meridian's ability to meet service commitments shall be governed by documented Underpinning Contracts with defined service level expectations. OLAs and UCs shall be reviewed in concert with the SLAs they support.

### 4.5 Regulatory Alignment Policy

Service Level Management activities shall be conducted in a manner that supports Meridian's compliance with SOC 2 Trust Services Criteria, particularly within the Availability and Processing Integrity categories. The SLM process shall provide demonstrable evidence of the following:

- Management has defined and communicated availability commitments (CC5.1, A1.1)
- Monitoring systems are configured to detect availability deviations
- Deviations are systematically documented, investigated, and remediated
- Customers are notified of significant service interruptions per contractual obligations

For services supporting the Clinical AI Platform, SLA commitments shall align with the operational resilience expectations established under EU MDR for medical device software and the EU AI Act for high-risk AI systems.

### 4.6 Change Management for SLA Modification Policy

Any change to an existing customer-facing SLA target or measurement methodology shall undergo formal change management review prior to customer communication. SLA modifications shall be documented and approved using the standard change management process. The approver for SLA modifications shall be the VP of IT Operations with consultation from the VP of Engineering and the relevant Product Manager. The individual proposing the change shall not be solely responsible for approving the change.

---

## 5. Detailed Procedures

### 5.1 Service Level Definition

#### 5.1.1 SLA Definition for Customer-Facing Services

This procedure applies when establishing service levels for services delivered to external paying customers under contractual agreements.

**Step 1: Service Profile Creation**
The Product Manager, in collaboration with the Service Owner, shall create a Service Profile documenting:
- Service name and description
- Business criticality classification (Tier 1: Critical, Tier 2: Business Important, Tier 3: Supportive)
- Customer base and impacted business processes
- Technical architecture overview
- Known single points of failure
- Dependency map (internal OLAs, external UCs)

**Step 2: Target Metric Selection**
Based on the Service Profile, the following standard metrics shall be evaluated for inclusion in the SLA:

| Metric | Definition | Applicability |
|---|---|---|
| Uptime Percentage | (Total minutes in measurement window – Downtime) / Total minutes × 100 | All customer-facing services |
| Response Time (95th Percentile) | API or transaction processing time within which 95% of all requests complete | Interactive services, APIs |
| Error Rate | Failed transactions / Total transactions × 100 | All transactional services |
| Latency (p99) | Maximum response time experienced by 99% of requests | Clinical AI Platform inference endpoints |
| Batch Processing Window | Time to complete scheduled batch processing jobs | MedInsight nightly analytics runs |
| Incident Response Time | Time from incident detection to initial response | All managed services |
| Incident Resolution Time | Time from incident detection to full service restoration | All managed services |

**Step 3: SLT Quantification**
For each selected metric, the Service Owner shall propose a quantitative target based on:
- Historical performance data (minimum 90 days for existing services, industry benchmarks for new services)
- Customer requirements gathered by the Product Manager
- Technical capability assessment performed by the PRE team
- Cost-benefit analysis of incremental reliability investments

Targets shall be tiered as follows for standard platform availability:

| Service Tier | Standard Uptime Target | Measurement Window | Measurement Granularity |
|---|---|---|---|
| Tier 1 (Critical) | 99.95% ("three and a half nines") | Calendar month | Minute-level |
| Tier 2 (Business Important) | 99.9% ("three nines") | Calendar month | Minute-level |
| Tier 3 (Supportive) | 99.5% | Calendar month | Hour-level |

For HealthPay Financial Services payment processing, the availability target shall be no less than 99.95% during business hours (defined as Monday-Friday, 08:00-20:00 EST, excluding US federal holidays).

For Clinical AI Platform inference endpoints supporting diagnostic workflows, the availability target shall be no less than 99.9% and the p99 latency target shall be no more than 500 milliseconds for standard inference requests.

**Step 4: Service Credit Structure Definition**
The Product Manager, in consultation with Legal and Finance, shall define a service credit schedule for SLA breaches. The standard Meridian SLA credit structure is as follows:

| Actual Performance vs. Target | Service Credit (% of Monthly Recurring Revenue) |
|---|---|
| Below target but ≥ (target – 0.1%) | 5% |
| Below (target – 0.1%) but ≥ (target – 0.5%) | 10% |
| Below (target – 0.5%) but ≥ (target – 1.0%) | 25% |
| More than 1.0% below target | 50% |

Service credits shall be capped at 50% of the monthly recurring revenue for the affected service in the measurement month. Service credits shall not constitute a customer's sole and exclusive remedy unless explicitly negotiated in the Master Services Agreement.

**Step 5: Draft SLA Creation**
The SLM Process Manager shall produce a draft SLA document using the standard Meridian SLA Template (available at `\\meridian.internal\Templates\SLM\SLA-Template-v2.3.docx`). The draft shall include: service description, metric definitions and calculation methodology, quantified targets, measurement windows, exclusions (including standard maintenance windows, force majeure, customer-caused incidents), reporting frequency, and service credit schedule.

**Step 6: SLA Review and Approval**
The draft SLA shall undergo a review cycle including:
1. Service Owner review (technical feasibility)
2. PRE Team Lead review (monitoring capability)
3. Legal review (contractual enforceability)
4. Finance review (service credit liability exposure)
5. VP of IT Operations approval

Formal approval shall be documented via the SLA Approval Form (`SOP-ITOP-013-F01`) with signatures retained in the IT Operations document repository.

#### 5.1.2 OLA Definition for Internal Support Relationships

Operational Level Agreements define the commitments between Meridian internal teams that support the delivery of customer-facing SLAs.

**Procedure:**

1. The Service Owner of the customer-facing service shall identify all internal dependencies required for SLA delivery. Each dependency shall be mapped to the internal team that provides it.

2. The Service Owner shall initiate an OLA negotiation meeting with the leadership of each dependent internal team. At minimum, the following internal teams shall be evaluated for OLA necessity:
   - Platform Reliability Engineering (infrastructure availability)
   - Network Operations (connectivity, bandwidth)
   - Database Administration (database performance, backup/restore times)
   - Security Operations (authentication service availability)
   - Service Desk (incident routing and initial triage)

3. For each identified dependency, the OLA shall specify:
   - **Supporting Service:** The internal service being provided (e.g., "AWS us-east-1 compute infrastructure")
   - **Provider Team:** The team responsible for the supporting service
   - **Consumer Team:** The team relying on the supporting service
   - **OLA Targets:** The quantitative performance targets the provider must meet
   - **Escalation Path:** The contact sequence when OLA targets are not being met
   - **Review Cadence:** Frequency of OLA performance review

4. OLA targets shall be set such that, when all internal OLAs are simultaneously met, the customer-facing SLA target is mathematically achievable. The relationship shall be documented as: `SLA_Target ≥ (OLA1_Target × OLA2_Target × ... × OLAN_Target)` for serial dependencies, with appropriate formulas for parallel dependencies.

5. The OLA shall be documented using the standard OLA Template (`SOP-ITOP-013-F02`) and signed by the Service Owner (consumer) and the manager of the provider team. Signed OLAs shall be stored in the Service Level Management repository on the IT Operations SharePoint site.

**Example Internal OLA Targets:**

| Supporting Service | Provider Team | Standard OLA Target |
|---|---|---|
| AWS Compute Infrastructure | PRE - Infrastructure | 99.95% availability (measured at EC2/EKS node health) |
| Network Core Services | Network Operations | 99.99% availability, <2ms intra-AZ latency |
| Database Services (RDS Primary) | Database Administration | 99.95% availability, <10ms read replica lag |
| Okta Authentication Service | Identity Management | 99.9% availability, <3s login latency at p95 |
| Service Desk Incident Triage | IT Service Desk | <15 minutes mean time to first response for Sev 1 incidents |

#### 5.1.3 Underpinning Contract Management

Underpinning Contracts define the service level commitments that Meridian expects from external vendors and cloud service providers.

**Procedure:**

1. During the vendor procurement or contract renewal process, the Vendor Management lead shall collaborate with the relevant Service Owner to define required service level commitments.

2. For cloud services, Meridian shall maintain documentation of:
   - AWS Service Level Agreements applicable to Meridian workloads (EC2, RDS, EKS, S3, etc.)
   - Azure Service Level Agreements for DR environment services
   - The specific configuration choices Meridian makes (e.g., multi-AZ deployment, instance sizing) that may impact Meridian's ability to claim credits under CSP SLAs

3. UCs shall be reviewed semi-annually to ensure that CSP SLA commitments remain sufficient to support Meridian's internal OLAs and customer-facing SLAs.

4. If a CSP modifies its SLA terms, the Service Owner shall perform an impact assessment within 30 days and present findings to the VP of IT Operations.

### 5.2 Service Level Monitoring

#### 5.2.1 Monitoring Configuration

All production services governed by SLAs shall have monitoring instrumentation configured to measure performance against each SLT. The PRE team is responsible for implementing and maintaining this instrumentation.

**Step 1: Metric Instrumentation**
For each SLT, the following instrumentation shall be configured:

| Measurement Need | Primary Tool | Fallback |
|---|---|---|
| Infrastructure availability (EC2, RDS, EKS node health) | Datadog Infrastructure Monitoring | AWS CloudWatch |
| Application availability (endpoint health, API responsiveness) | Datadog APM | Custom health check endpoints probed by Route 53 Health Checks |
| Transaction latency and error rates | Datadog APM with distributed tracing | Application-level metrics exported to CloudWatch |
| Synthetic transaction success (customer-perspective health) | Datadog Synthetic Monitoring | — |
| Database query performance | Datadog Database Monitoring | RDS Performance Insights |
| End-user experience metrics (RUM) | Datadog Real User Monitoring | — |

**Step 2: SLI Definition in Datadog**
For each SLT, the PRE team shall define a Service Level Indicator (SLI) in Datadog with:
- The precise metric query matching the SLA calculation methodology
- The SLO threshold corresponding to the SLA target
- The measurement window (rolling 28-day for monthly SLAs, rolling 7-day for operational awareness)
- The error budget (1 – SLO) expressed as acceptable downtime in minutes

**Step 3: Alert Configuration**
Alerting shall be configured using Datadog monitors with PagerDuty integration. The specific alert thresholds and the escalation paths to be followed when those thresholds are triggered shall be configured according to the procedures defined within this document.

**Step 4: Synthetic Transaction Suite**
For Tier 1 services, the PRE team shall implement a synthetic transaction suite that executes critical user journeys at a minimum frequency of once every five minutes from geographically distributed probe locations. Synthetic transactions shall emulate:
- User authentication flow
- Core API transactions
- End-to-end clinical workflow (for Clinical AI Platform)
- Payment processing lifecycle (for HealthPay)

Synthetic transaction failures shall be treated with the same severity classification as customer-reported outages of equivalent scope.

#### 5.2.2 Downtime Measurement Methodology

**Definition of Downtime:**
A service is considered "down" or "unavailable" when:

1. **Customer-Facing Unavailability:** The service fails to respond to properly-formed requests within the SLT-defined latency threshold, and this failure affects >5% of attempted transactions over a rolling 5-minute window.

2. **Synthetic Check Failure:** Two or more geographically distinct synthetic monitoring probes simultaneously register a failure of a critical user journey.

3. **Internal Monitoring Confirmation:** The PRE team confirms via Datadog APM, infrastructure monitoring, and/or log analysis that the service is unable to process transactions.

**Exclusions from Downtime Calculation:**

The following shall be excluded from downtime calculations for SLA purposes:
- Planned maintenance during published maintenance windows (see Section 5.5)
- Force majeure events as defined in the governing SLA contract
- Customer-caused incidents (configuration errors, quota exhaustion on customer-managed resources)
- Third-party network transit issues outside Meridian's direct control (subject to UC review)
- Denial-of-service attacks not attributable to Meridian's failure to maintain standard network defenses

**Downtime Calculation Formula:**
`Total Downtime = SUM(Downtime_Event_Duration) for all qualifying events within the measurement window`

`Uptime Percentage = ((Total Minutes in Window – Total Downtime Minutes) / Total Minutes in Window) × 100`

All downtime events shall be documented in an incident record within the ITSM platform (ServiceNow), including start time, end time, root cause classification, and an indicator of whether the event counts against SLA measurements.

### 5.3 Service Level Breach Management

#### 5.3.1 Breach Identification and Notification

**Procedure:**

1. Upon detection of a service degradation that, if sustained, would result in an SLA breach (as determined by Datadog SLO burn rate alerts or manual observation), the PRE team shall open a Severity 1 or Severity 2 incident per SOP-SEC-009 Incident Response procedures.

2. The Service Owner shall assess, within one business day of incident resolution, whether the incident constitutes an SLA breach when measured across the full window.

3. If an SLA breach is confirmed, the Service Owner shall:
   - Notify the VP of IT Operations within 24 hours of breach confirmation
   - Notify the Product Manager within 24 hours
   - Initiate root cause analysis per Section 5.3.3

4. The Product Manager shall notify affected customers of the SLA breach per contractual notification requirements, typically within 5 business days of breach confirmation.

5. The SLM Process Manager shall record the breach in the SLA Breach Register (maintained in ServiceNow as a problem record linked to the incident).

#### 5.3.2 Service Credit Processing

When a breach results in service credit obligations to a customer:

1. The SLM Process Manager shall calculate the applicable service credit amount per the SLA credit schedule.

2. The calculation shall be documented in a Service Credit Determination form (`SOP-ITOP-013-F03`) and submitted to the VP of IT Operations for approval.

3. Upon approval, the form shall be routed to the Finance department (Accounts Receivable team) for issuance of credit memo.

4. Service credits shall be tracked in a centralized register to support trend analysis and SIP prioritization.

#### 5.3.3 Root Cause Analysis

For any confirmed SLA breach affecting a Tier 1 or Tier 2 service, a formal Root Cause Analysis (RCA) shall be conducted.

**RCA Procedure:**

1. The Service Owner shall schedule an RCA session within 5 business days of incident resolution.

2. Participants shall include: Service Owner (facilitator), PRE team representative, Product Manager, and any other teams identified as contributing factors.

3. The RCA shall employ a recognized methodology: Five Whys analysis or Ishikawa (fishbone) diagramming.

4. The RCA shall produce a documented report using the RCA Template (`SOP-ITOP-013-F04`) containing:
   - Incident timeline
   - Direct cause
   - Contributing factors
   - Root cause(s)
   - Preventative actions with assigned owners and due dates
   - Detection time analysis (MTTD assessment: was the incident detected by automated monitoring or by customer report?)
   - Resolution time analysis (MTTR assessment: barriers to faster resolution)
   - Classification as a known failure pattern vs. novel failure

5. The RCA report shall be reviewed and signed by the Service Owner and the VP of IT Operations.

6. Preventative actions shall be tracked as problem tasks in ServiceNow and reviewed at the subsequent quarterly service review.

### 5.4 Service Review Procedures

#### 5.4.1 Quarterly Service Review (QSR) — Tier 1 and Tier 2 Services

Quarterly Service Reviews are mandatory for all Tier 1 and Tier 2 services with customer-facing SLAs. The SLM Process Manager shall schedule and facilitate these reviews.

**Agenda:**

| Item | Owner | Duration |
|---|---|---|
| Review of previous QSR action items | SLM Process Manager | 10 min |
| SLA performance vs. targets for the quarter | Service Owner | 20 min |
| Incident review (Sev 1 and Sev 2 incidents) | Service Owner, PRE Team Lead | 20 min |
| Error budget consumption tracking | PRE Team Lead | 10 min |
| OLA/UC performance review | Service Owner | 15 min |
| SIP status updates (if applicable) | Service Owner | 15 min |
| Upcoming changes / risk assessment (maintenance windows, infrastructure changes, capacity planning) | Service Owner, PRE Team Lead | 20 min |
| Customer feedback summary | Product Manager | 10 min |
| New action item assignment | SLM Process Manager | 10 min |

**Materials:**
- Quarterly Service Performance Dashboard (generated from Datadog, exported as PDF)
- Incident summary report (extracted from ServiceNow)
- Error budget status report
- SIP status tracker (if applicable)
- Minutes template (`SOP-ITOP-013-F05`)

**Post-Review:**
Meeting minutes, action items, and a brief executive summary shall be distributed within 3 business days. Action items shall be entered into the ITSM system and tracked through to completion.

#### 5.4.2 Annual SLA Review

Annually, and upon any major service release or architectural change, the full SLA shall be formally reviewed.

**Procedure:**

1. The SLM Process Manager initiates the annual review 60 days prior to the scheduled SLA renewal date.

2. The Service Owner provides a 12-month performance trend analysis.

3. The Product Manager gathers customer feedback on SLA adequacy and relevance.

4. A joint review meeting is held with: Service Owner, Product Manager, PRE Team Lead, VP of IT Operations, and Legal representative (if SLA modifications are proposed).

5. Outcomes are classified as:
   - **Renew as-is:** No changes to targets or measurement methodology
   - **Modify:** Targets adjusted (upward or, only under exceptional documented justification, downward), metrics added/removed, or measurement methodology revised
   - **Sunset:** Service being retired, SLA termination plan established

6. Any modifications shall follow the SLA Definition procedure (Section 5.1.1).

### 5.5 Planned Maintenance Window Management

**Standard Maintenance Windows:**

| Infrastructure Zone | Standard Window | Tier 1 Services | Tier 2 Services | Tier 3 Services |
|---|---|---|---|---|
| us-east-1 (Primary) | Sundays, 02:00-06:00 EST | Included, requires 14-day advance customer notice | Included, requires 7-day advance internal notice | Included, no specific notice |
| eu-west-1 (EU Clinical) | Sundays, 02:00-06:00 CET | Included, requires 14-day advance customer notice | Included, requires 7-day advance internal notice | Included, no specific notice |

Maintenance executed entirely within the standard window is excluded from SLA downtime calculations, provided the 14-day advance notice was delivered to customers.

**Emergency Maintenance:**
Maintenance required to address an active security vulnerability (CVSS 7.0+) or prevent an imminent service failure may be classified as emergency maintenance with approval from the VP of IT Operations. Emergency maintenance windows shall be communicated to customers as soon as operationally feasible; the 14-day advance notice requirement is waived. Emergency maintenance downtime is excluded from SLA calculations at the discretion of the VP of IT Operations.

### 5.6 Service Catalog Maintenance

The Service Catalog is the authoritative repository of all services governed by this SOP.

**Procedure:**

1. Upon completion of an SLA definition (Section 5.1.1), the SLM Process Manager shall create or update the corresponding Service Catalog entry in ServiceNow.

2. Each Service Catalog entry shall contain:
   - Service unique identifier and display name
   - Service classification (Tier 1, 2, or 3)
   - Service Owner (named individual)
   - Current SLA targets (all metrics)
   - Current status (Active, Deprecating, Retired)
   - Linked OLAs and UCs
   - Technical service offering details (supported regions, endpoints, authentication methods)

3. Service Owners shall review their Service Catalog entries for accuracy on a quarterly basis, no later than 7 days before each QSR.

4. The SLM Process Manager shall produce a Service Catalog health report monthly, identifying entries with expired reviews or missing required information.

---

## 6. Controls and Safeguards

### 6.1 Access Control for SLA Configuration

Modification of SLA targets, measurement methodologies, or monitoring configurations associated with customer-facing SLAs is restricted to authorized personnel.

| Action | Authorized Roles | Approval Required |
|---|---|---|
| Creation of new SLA | Service Owner, SLM Process Manager | VP of IT Operations |
| Modification of existing SLA target | Service Owner, VP of IT Operations | VP of Engineering |
| Modification of SLA measurement methodology | SLM Process Manager | Service Owner, VP of IT Operations |
| Modification of Datadog SLO/SLI configuration | PRE Team Lead, PRE engineers designated as "SLI Admin" | Service Owner |
| Modification of PagerDuty alert routing | PRE Team Lead | Service Owner |
| Deletion of SLA from Service Catalog | SLM Process Manager | VP of IT Operations, Legal |

Access controls shall be enforced via Datadog Role-Based Access Control (RBAC) groups, with the "SLI Admin" role restricted to named individuals on the PRE team. All modifications to SLA-related configurations shall produce an audit trail in Datadog Audit Logs.

### 6.2 Segregation of Duties for SLA Modifications

Modifications to customer-facing SLA targets require the involvement of two distinct roles: an initiator and an approver. The initiator (typically the Service Owner or SLM Process Manager) proposes the change with documented justification. The approver (VP of IT Operations or VP of Engineering) reviews and authorizes the change independently. The system shall be configured to enforce this workflow in the ServiceNow Change Request module.

### 6.3 Monitoring Integrity Safeguards

To protect the integrity of SLA performance data:

- Datadog monitors shall be configured with "read-only" access for users who require visibility but are not authorized to modify thresholds.
- Changes to monitoring configurations in production Datadog environments shall be made via Infrastructure-as-Code (Terraform) with pull request review required.
- Alert silencing (maintenance windows, downtime) shall be time-bounded and require justification text.
- Synthetic transaction scripts shall be version-controlled in the `meridian-health/synthetic-monitoring` GitHub repository.

### 6.4 Backup and Disaster Recovery for SLM Artifacts

All SLM documentation (SLA documents, OLA documents, UC registers, QSR minutes, SIP trackers) stored on IT Operations SharePoint shall be subject to the standard Meridian data backup and retention policies per SOP-ITOP-007 "Data Backup and Restoration." The ServiceNow instance hosting the Service Catalog and incident/problem records shall be included in the SaaS backup schedule with a Recovery Point Objective (RPO) of 4 hours.

### 6.5 Change Management for Service Modifications Impacting SLAs

Any infrastructure change, application deployment, or configuration modification that has a reasonable probability of impacting a Tier 1 service's ability to meet its SLA targets shall be governed by formal change management procedures. The change requestor shall perform an SLA impact assessment as part of the change planning documentation. The assessment shall identify:

- Which SLA metrics could be impacted
- The estimated duration of potential impact
- Mitigation actions planned
- Rollback plan

The change shall proceed only after the Service Owner reviews and acknowledges the SLA impact assessment.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators

Service Level Management process effectiveness shall be measured by the following KPIs:

| KPI | Description | Target | Measurement Source |
|---|---|---|---|
| SLA Attainment Rate | Percentage of all SLTs across all services that are met within the monthly measurement window | ≥ 99% of SLTs met | Datadog SLO Dashboard |
| Customer-Facing SLA Breach Count | Number of confirmed breaches of contractual SLA targets per quarter | ≤ 2 per quarter | ServiceNow SLA Breach Register |
| Mean Time to Detect (MTTD) | Average time from incident onset to automated detection or valid customer report, whichever is earlier | ≤ 5 minutes for Sev 1 | ServiceNow Incident records |
| Mean Time to Resolve (MTTR) | Average time from incident detection to full service restoration for Sev 1 and Sev 2 incidents | ≤ 240 minutes for Sev 1 (4 hours) | ServiceNow Incident records |
| OLA Attainment Rate | Percentage of internal OLA targets met per month | ≥ 99.5% | Datadog, internal monitoring |
| Service Review Completion | Percentage of scheduled QSRs completed within the calendar quarter | 100% | SLM Process Manager tracker |
| SIP Closure Rate | Percentage of Service Improvement Plan action items completed on or before due date | ≥ 90% | ServiceNow Problem tasks |
| Service Catalog Accuracy | Percentage of Service Catalog entries with accurate information as verified by quarterly Service Owner review | 100% | Service Catalog health report |

### 7.2 Reporting Cadence

| Report | Frequency | Audience | Medium |
|---|---|---|---|
| Monthly Service Level Report (SLR) | Monthly, by 5th business day of following month | Service Owners, Product Managers, VP IT Operations, VP Engineering | PDF generated from Datadog dashboards, distributed via email; archived on SharePoint |
| Quarterly Customer SLA Performance Report | Quarterly, within 15 business days of quarter-end | External customers (upon request or contractually specified) | PDF with executive summary, distributed by Product Manager |
| Quarterly Service Review (QSR) Pack | Per-service, prepared 5 business days before scheduled QSR | QSR attendees | PDF compilation: Datadog dashboard export, incident summary, error budget status, action item tracker |
| Semi-Annual Management Review | Semi-annual (H1, H2) | Executive Leadership Team (ELT) representative | PowerPoint presentation summarizing SLA performance across all product lines, notable breaches, SIP status, improvement initiatives proposed |

### 7.3 Dashboard Requirements

The following operational dashboards shall be maintained in Datadog:

1. **SLM Executive Dashboard:** High-level view of all SLA attainment statuses, current error budget remaining, and active incident count. Access: VP IT Operations, VP Engineering, CTO, Service Owners.

2. **Per-Service SLA Detail Dashboard:** Granular view of each SLT metric, SLO burn rate, error budget consumption trend, synthetic transaction success rate, and incident timeline for the current measurement window. Access: Service Owner, PRE team, Product Manager, SLM Process Manager.

3. **OLA Performance Dashboard:** Internal dashboard tracking OLA targets between internal teams. Access: All internal teams party to OLAs, PRE team, SLM Process Manager.

4. **UC Dependency Health Dashboard:** Aggregated view of CSP status pages (AWS Health Dashboard, Azure Status) correlated with Meridian service health. Access: PRE team, Service Owners.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Process

Situations may arise where a defined SLA target cannot be met due to circumstances beyond the Service Owner's reasonable control, or where a proposed SLA configuration deviates from the standard policies defined in this SOP.

**Procedure:**

1. The requesting party (Service Owner, Product Manager, or PRE Team Lead) shall submit a formal Exception Request using the form `SOP-ITOP-013-F06`, documenting:
   - The specific policy, procedure, or target from which deviation is requested
   - The business justification for the exception
   - The proposed alternative approach or temporary target
   - The effective period for the exception (start and end dates)
   - The risk assessment associated with the exception

2. The SLM Process Manager shall review the request for completeness and impact on dependent services, OLAs, and customer commitments.

3. For exceptions impacting customer-facing SLA targets:
   - **Approver:** VP of IT Operations and VP of Engineering (joint approval)
   - **Consultation:** Legal (if customer notification is required), Product Manager

4. For exceptions to internal OLAs or operational procedures:
   - **Approver:** VP of IT Operations
   - **Consultation:** Service Owner of dependent customer-facing service

5. Approved exceptions shall be:
   - Documented in the Exception Register (maintained on SharePoint)
   - Communicated to affected parties (internal teams, and if applicable, customers via the Product Manager)
   - Reviewed at each quarterly service review
   - Time-bounded; exceptions shall not remain open indefinitely. Extensions require re-approval.

### 8.2 Escalation Path

Escalation of service level issues shall follow this path:

| Escalation Level | Trigger | Escalation Contact | Response Expectation |
|---|---|---|---|
| Level 0 (Operational) | Standard incident management per SOP-SEC-009 | PRE On-Call, Service Desk | Per incident severity SLTs |
| Level 1 | An SLA breach is confirmed or imminent (error budget exhausted with >5 days remaining in measurement window) | Service Owner | Acknowledge within 4 business hours; convene war room if ongoing incident |
| Level 2 | Service Owner unable to resolve breach or SIP execution stalled (>2 weeks overdue on critical path item) | VP of IT Operations (S. Torres) | Respond within 1 business day; direct resource allocation |
| Level 3 | Multi-service impact, customer escalation to executive level, or regulatory concern | VP of IT Operations, VP of Engineering (D. Park), CTO | Joint assessment within 24 hours; executive communication plan |

### 8.3 Force Majeure and Service Exemption

Events qualifying as force majeure under governing SLAs shall be documented with evidence of the triggering event. The VP of IT Operations, in consultation with Legal, shall make the determination that an event qualifies for force majeure exclusion from SLA calculations. This determination shall be documented and retained with the SLA performance records for the relevant period.

---

## 9. Training Requirements

### 9.1 Required Training

All personnel assigned to roles defined in Section 3 of this SOP shall complete Service Level Management training appropriate to their role.

| Training Module | Target Audience | Frequency | Delivery Method |
|---|---|---|---|
| SLM Fundamentals | All Service Owners, Product Managers, PRE team members, SLM Process Manager | Initial upon role assignment; refresher every 24 months | Meridian Learning Management System (LMS) e-learning module |
| SLA Definition Workshop | Service Owners, Product Managers newly assigned to services with customer-facing SLAs | Initial upon role assignment | Instructor-led (SLM Process Manager) |
| Datadog SLO/SLI Configuration | PRE team members designated as "SLI Admin" | Initial upon access grant; refresher upon major Datadog feature releases | Instructor-led (Datadog-certified PRE team lead) |
| Service Review Facilitation | SLM Process Manager, Service Owners | Once (initial) | Shadowing experienced facilitator for 1 QSR cycle |
| Incident Response Integration | Service Owners, PRE On-Call | Annual review | SOP-SEC-009 training curriculum |

### 9.2 Training Tracking

Training completion shall be tracked in the Meridian Learning Management System (Workday Learning). The SLM Process Manager shall maintain a Training Compliance Report reviewed quarterly. Personnel who have not completed required training within 60 days of role assignment shall not be granted approver or configuration access to SLA-related systems.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Documents

| Document ID | Title | Relationship |
|---|---|---|
| SOP-ITOP-001 | IT Service Management Framework | Parent governance framework for all ITIL-derived processes |
| SOP-ITOP-007 | Data Backup and Restoration | Defines backup RPO/RTO applied to SLM documentation repositories |
| SOP-SEC-009 | Incident Response and Breach Notification | Defines incident severity classification, response procedures, and customer notification obligations referenced herein |
| SOP-VM-022 | Vendor Offboarding and Contract Termination | Governs UC termination when vendor contracts end |
| SOP-ITOP-010 | Availability and Capacity Management | Defines capacity planning inputs to SLA target setting |
| SOP-RM-004 | Technology Risk Register | Captures risks identified through SLA breach trend analysis |
| SOP-ITOP-005 | Change Management | Defines the change approval workflow referenced in Section 6.5 |

### 10.2 External Standards and Frameworks

| Standard | Relevance |
|---|---|
| SOC 2 Trust Services Criteria (CC5.1, A1.1, PI1.3) | Availability and processing integrity commitments. This SOP provides evidence of management's defined availability commitments and systematic monitoring of performance against those commitments. |
| ITIL 4 — Service Level Management Practice | Industry best practice framework informing the structure of this SOP |
| ISO/IEC 20000-1:2018 — Service Management System Requirements | International standard for IT service management |
| EU AI Act (Regulation 2024/1689) | Operational resilience requirements for high-risk AI systems provided via Clinical AI Platform |
| EU Medical Device Regulation (2017/745) | Requirements for post-market surveillance of clinical software, supported by availability monitoring and incident management |
| SR 11-7 (FRB/OCC Guidance on Model Risk Management) | Applied to HealthPay credit scoring models and their operational service levels |

---

## 11. Revision History

| Version | Date | Author | Description of Change | Approver |
|---|---|---|---|---|
| 1.0 | 2023-06-15 | Michael Chen, IT Service Management Lead | Initial publication. Established SLM framework for Tier 1-3 services. Defined standard SLA template, QSR cadence, and SLA breach management process. | David Park, VP of Engineering |
| 1.0 (Errata) | 2023-09-11 | Samantha Torres, VP of IT Operations | Minor correction to Section 5.1.1 Step 3: Availability targets table added missing Tier 3 row. No procedural changes. | David Park, VP of Engineering |
| 1.0 (Errata) | 2023-12-19 | Elena Rossi, SLM Process Manager | Updated Section 7.1 KPI targets for MTTD and MTTR to reflect PRE team reorganization. Updated escalation contacts in Section 8.2. | Samantha Torres, VP of IT Operations |
| 1.1 | 2024-02-05 | Samantha Torres, VP of IT Operations | **Major Revision:** (1) Expanded scope to formally include Clinical AI Platform and HealthPay Financial Services with specific SLTs. (2) Added Section 5.1.3 Underpinning Contract Management to address CSP dependency management. (3) Revised Section 5.2.1 to add Datadog Synthetic Monitoring requirements for Tier 1 services. (4) Added Section 6.2 Segregation of Duties for SLA Modifications. (5) Updated Section 2 definitions to align with EU AI Act and EU MDR terminology. (6) Updated Section 10 cross-references. (7) Updated Section 3 RACI to include Internal Audit role. | David Park, VP of Engineering |

---

**END OF DOCUMENT**

*This document is classified as "Internal" per Meridian Health Technologies Data Classification Policy. Distribution is restricted to Meridian employees and authorized contractors with a legitimate business need. Do not distribute externally without authorization from the document owner or the Legal department.*