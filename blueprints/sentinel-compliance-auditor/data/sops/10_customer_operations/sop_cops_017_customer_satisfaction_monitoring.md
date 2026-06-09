---
sop_id: "SOP-COPS-017"
title: "Customer Satisfaction Monitoring"
business_unit: "Customer Operations"
version: "5.2"
effective_date: "2024-08-08"
last_reviewed: "2025-09-24"
next_review: "2026-03-18"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Customer Satisfaction Monitoring

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for systematically monitoring, measuring, analyzing, and acting upon customer satisfaction data across all Meridian Health Technologies, Inc. ("Meridian") business lines. The purpose of this SOP is to ensure a consistent, auditable, and actionable approach to understanding customer sentiment, identifying service degradation trends, and driving continuous improvement initiatives that align with the company's commitment to service excellence and regulatory obligations.

This SOP formalizes the processes by which Customer Operations collects customer feedback, transforms it into actionable intelligence, and ensures accountability for remediation of identified issues. It directly supports Meridian's SOC 2 Trust Services Criteria related to monitoring activities and complements the organization's broader AI risk management and financial services compliance frameworks.

### 1.2 Scope

This SOP applies to all Meridian business units, products, services, and personnel who interact with external customers, including contractors and third-party service providers acting on behalf of Meridian. The scope encompasses:

| In Scope | Out of Scope |
|---|---|
| All Meridian business lines (Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, Meridian SaaS Platform) | Internal employee satisfaction surveys (see SOP-HR-042) |
| All customer types: healthcare providers, payers, patients, and channel partners | Supplier/vendor performance evaluations (see SOP-PROC-011) |
| All delivery channels: direct sales, reseller partners, platform integrations | Clinical efficacy studies (see SOP-CLIN-023) |
| All geographic markets: North America, European Union, Asia-Pacific | FDA post-market surveillance (see SOP-REG-031) |
| Production and production-like environments only | Internal development/test environment feedback |
| Third-party service providers who interact with Meridian customers on Meridian's behalf | Third-party customer satisfaction programs for non-Meridian services |

This SOP is binding upon all Full-Time Employees (FTEs), contractors, consultants, and temporary personnel (collectively "Personnel") who manage, support, or influence customer relationships.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Customer Satisfaction (CSAT)** | A quantitative measure of a customer's perceived experience with a specific interaction, product feature, or overall relationship with Meridian, typically captured via standardized survey instruments. |
| **Net Promoter Score (NPS)** | A relationship-based metric measuring customer loyalty and likelihood to recommend Meridian products or services, calculated on a 0-10 scale. |
| **Customer Effort Score (CES)** | A transactional metric measuring the ease with which a customer could accomplish a specific task or resolve an issue, typically on a 1-7 Likert scale. |
| **Sentiment Analysis** | Automated natural language processing (NLP) techniques applied to unstructured customer feedback (survey verbatims, support tickets, social media mentions) to classify emotional tone and thematic categories. |
| **Detractor** | A customer providing an NPS rating of 0-6, indicating dissatisfaction and potential churn risk. |
| **Passive** | A customer providing an NPS rating of 7-8, indicating neutral satisfaction but vulnerability to competitive offerings. |
| **Promoter** | A customer providing an NPS rating of 9-10, indicating high satisfaction and loyalty. |
| **Closed-Loop Feedback (CLF)** | The process by which Customer Operations follows up directly with individual customers who have provided feedback, particularly Detractors, to understand root causes and initiate service recovery. |
| **Service Recovery** | Specific actions taken by Meridian to remediate a negative customer experience and restore the customer's confidence. |
| **Trend Analysis** | Time-series examination of satisfaction metrics to identify statistically significant patterns, shifts, or anomalies requiring management attention. |
| **Feedback Collection Point (FCP)** | A defined touchpoint in the customer journey at which satisfaction data is systematically solicited. |
| **Sentiment Threshold Breach** | An event where any monitored metric falls outside of defined control limits for a sustained period as defined in Section 7. |

### 2.2 Acronyms

| Acronym | Expansion |
|---|---|
| **AHT** | Average Handle Time |
| **AWS** | Amazon Web Services |
| **BI** | Business Intelligence |
| **CLF** | Closed-Loop Feedback |
| **COO** | Chief Operating Officer (role delegated to VP of Customer Operations for this SOP) |
| **CRM** | Customer Relationship Management |
| **CSAT** | Customer Satisfaction |
| **CES** | Customer Effort Score |
| **DPO** | Data Protection Officer |
| **DSAR** | Data Subject Access Request |
| **FCP** | Feedback Collection Point |
| **FCR** | First Contact Resolution |
| **HIPAA** | Health Insurance Portability and Accountability Act |
| **JSON** | JavaScript Object Notation |
| **KPI** | Key Performance Indicator |
| **MTTR** | Mean Time to Recovery |
| **NLP** | Natural Language Processing |
| **NPS** | Net Promoter Score |
| **PHI** | Protected Health Information |
| **PII** | Personally Identifiable Information |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **SLA** | Service Level Agreement |
| **SOP** | Standard Operating Procedure |
| **TLS** | Transport Layer Security |
| **SOC 2** | System and Organization Controls 2 |
| **VP** | Vice President |

---

## 3. Roles and Responsibilities

The following RACI matrix assigns responsibilities for activities governed by this SOP:

| Activity / Decision | VP, Customer Operations (Michael Chang) | Customer Success Managers | VP, IT Ops (Samantha Torres) | Business Unit VPs | Chief Privacy Officer / DPO (Klaus Weber) | Chief Compliance Officer (Thomas Anderson) | Customer Support Team | Product Management |
|---|---|---|---|---|---|---|---|---|
| Define CSAT strategy, KPIs, and thresholds | A | R | C | C | I | I | I | C |
| Configure and maintain survey instruments | C | C | A | I | R | I | I | I |
| Execute CSAT and NPS survey distribution | I | I | R | I | I | I | A | I |
| Monitor real-time CSAT dashboards | R | A | R | I | I | I | R | I |
| Perform monthly trend analysis | A | R | C | I | I | I | C | I |
| Initiate Closed-Loop Feedback for Detractors | I | A | I | R | I | I | R | I |
| Escalate systemic satisfaction issues | R | R | C | A | I | I | I | C |
| Implement improvement action plans | I | R | C | A | I | I | I | R |
| Review and approve SOP changes | A | C | C | C | C | R | I | I |
| Ensure GDPR compliance of feedback data | I | I | C | I | A | R | I | I |
| Respond to customer DSARs involving CSAT data | I | I | I | I | A | R | I | I |
| Verify SOC 2 control alignment | I | I | I | I | I | A | I | I |

**Key:** R = Responsible (executes the work), A = Accountable (approves/signs off), C = Consulted (provides input), I = Informed (notified of outcome)

### 3.1 Specific Role Descriptions

**Michael Chang, VP of Customer Operations (SOP Owner):** Serves as the executive accountable for the overall CSAT monitoring program. Approves metric thresholds, reviews quarterly trend reports, and authorizes structural improvements. Chairs the monthly Customer Experience Review meeting.

**Customer Success Managers:** Serve as the primary relationship owners responsible for interpreting account-level CSAT data, executing CLF workflows, and escalating systemic product or service issues. Each CSM manages a designated book of business and maintains a CSAT health scorecard per account.

**Samantha Torres, VP of IT Operations:** Accountable for the technical infrastructure supporting feedback collection, including survey platform configuration, API integrations with CRM (Salesforce), and dashboard availability. Ensures feedback data pipelines meet uptime SLAs.

**Business Unit VPs (Clinical AI: Dr. Aisha Okafor; Financial Services: Robert Liu; MedInsight Analytics: TBD; SaaS Platform: David Park):** Accountable for addressing product-specific satisfaction issues identified through CSAT monitoring. Approve product improvement roadmaps in response to persistent Detractor feedback.

**Dr. Klaus Weber, Chief Privacy Officer / DPO:** Ensures all customer feedback collection, storage, and processing activities comply with GDPR and HIPAA requirements. Reviews and approves survey instruments that may collect EU data subject personal data. Manages DSAR procedures for CSAT data.

**Thomas Anderson, Chief Compliance Officer:** Verifies alignment of CSAT monitoring activities with SOC 2 Trust Services Criteria, specifically CC7.0 (Monitoring Activities). Reviews evidence of management's monitoring activities for the annual SOC 2 audit.

---

## 4. Policy Statements

Meridian Health Technologies is committed to maintaining a rigorous, continuous customer satisfaction monitoring program as a cornerstone of its SOC 2 control environment and its mission to deliver reliable, high-quality healthcare technology services. The following policy statements govern all CSAT monitoring activities:

**PS-017-01: Universal Measurement.** All production customer interactions shall be subject to CSAT measurement at defined Feedback Collection Points. No business unit, product, or customer segment is exempt from feedback solicitation without a formal exception approved per Section 8.

**PS-017-02: Consistent Methodology.** CSAT, NPS, and CES shall be measured using standardized, version-controlled survey instruments maintained in the central survey platform (Qualtrics) and approved by the VP of Customer Operations. Survey modifications require change management approval with separation of duties ensuring the individual requesting the change is distinct from the individual implementing the change. Changes are documented in the survey change log.

**PS-017-03: Data Privacy and Consent.** All customer feedback collection shall include appropriate consent language and adhere to Meridian's Data Privacy Policy (SOP-PRIV-001). Feedback containing PHI/PII shall be identified via automated data loss prevention (DLP) scanning and quarantined per HIPAA data handling procedures. Customers in the EU shall be provided with a clear opt-out mechanism from non-essential satisfaction surveys.

**PS-017-04: Closed-Loop Accountability.** All Detractor feedback (NPS 0-6) shall trigger a mandatory Closed-Loop Feedback workflow within 1 business day of submission. Customer Success Managers shall document the root cause analysis and service recovery actions within the CRM. Open Detractor cases shall be reviewed weekly until resolution.

**PS-017-05: Transparent Reporting.** Aggregate CSAT and NPS scores shall be reported monthly to the AI Governance Committee, quarterly to the Board of Directors, and shall be made available to all customer-facing personnel via self-service dashboards.

**PS-017-06: Continuous Improvement.** Persistent negative trends in CSAT metrics shall trigger formal Root Cause Analysis (RCA) and Corrective and Preventive Action (CAPA) plans, documented and tracked to closure within 30 calendar days.

**PS-017-07: Non-Retaliation.** Meridian prohibits retaliation against any customer for providing negative feedback. Detractor feedback shall not negatively impact a customer's service level or support prioritization. Any instance of suspected retaliation shall be reported to the Chief Compliance Officer immediately.

**PS-017-08: SOC 2 Monitoring Evidence.** All CSAT monitoring activities, including dashboard reviews, alert acknowledgements, and management responses to anomalies, shall be logged and retained as audit evidence for SOC 2 CC7.0 (Monitoring Activities). Review activities shall be documented to demonstrate management's ongoing evaluation of service performance.

---

## 5. Detailed Procedures

### 5.1 Feedback Collection Point (FCP) Configuration

Customer Operations, under the technical execution of IT Operations, shall maintain the following standardized Feedback Collection Points:

| FCP ID | Trigger Event | Instrument Type | Target Population | Cadence | Survey Channel |
|---|---|---|---|---|---|
| FCP-01 | Support ticket closure (Tier 1 & Tier 2) | CSAT (1-question) + optional verbatim | All ticket requestors | Real-time, upon ticket closure | Email with embedded survey |
| FCP-02 | Support ticket closure (Tier 3 / Engineering escalation) | CES (2-question) + verbatim | All ticket requestors | Real-time, upon ticket closure | Email |
| FCP-03 | Implementation project completion | NPS (Standard) + structured feedback | Project sponsors and key stakeholders | 3 business days post-go-live | Email from CSM |
| FCP-04 | Quarterly business review (QBR) completion | Relationship NPS | Executive sponsors | 1 business day post-QBR | Personalized email from VP or CSM |
| FCP-05 | Product release adoption (major version) | CES + Feature Satisfaction | Designated customer admins | 14 calendar days post-upgrade | In-app prompt (Pendo) |
| FCP-06 | HealthPay transaction dispute resolution | CSAT (1-question) | Dispute initiators | Real-time, upon dispute closure | Email |
| FCP-07 | Annual relationship survey | Comprehensive NPS + Multi-attribute | All active customers with annual contract value > $50,000 | Annually (Q4) | Email campaign |

#### 5.1.1 Survey Instrument Configuration Procedure

**Step 1:** Customer Operations, in coordination with the relevant Business Unit, identifies the need for a new or modified survey instrument.

**Step 2:** The requestor completes the Survey Configuration Request Form (SCRF-017) in the Customer Operations SharePoint portal, specifying the target FCP, proposed question wording, rating scale, and any conditional logic.

**Step 3:** The SCRF-017 is submitted for review. The review includes approval from the VP of Customer Operations (or delegate) for content, the Chief Privacy Officer (or delegate) for privacy and consent language, and the Chief Compliance Officer for regulatory alignment.

**Step 4:** Upon approval, IT Operations personnel (distinct from the requestor and approvers) implement the configuration within the Qualtrics survey platform. A separate peer review validates the implementation against the approved SCRF-017 before deployment. This separation ensures that no single individual can both request and deploy a survey change.

**Step 5:** The implemented survey is tested in the Qualtrics lower environment against a set of test customer profiles. Test responses are verified for data flow into the Meridian Data Lake (Snowflake) and CRM.

**Step 6:** Upon successful test validation, the survey is promoted to production via a change request in ServiceNow. The deployment time and implementor are logged in the Survey Configuration Change Log.

### 5.2 Identity Verification for DSR Requests

Before processing any formal DSR (e.g., data access, deletion, rectification requests related to their own feedback data), Customer Operations must verify the requestor's identity.

**Procedure:**

**Step 1:** DSR request received via privacy@meridianhealthtech.com or through the Privacy Portal (OneTrust).

**Step 2:** The Privacy Team logs the request and assigns a unique ticket ID (DSAR-XXXX).

**Step 3:** The Privacy Team verifies the requestor's identity by matching at least two pieces of information against records in the authoritative identity source (Okta Universal Directory for users, or Salesforce for contacts): full name, email address, customer account ID, or phone number.

**Step 4:** If verification fails or is inconclusive, the Privacy Team requests additional identifying documentation from the requestor. The DSR processing clock is paused pending satisfactory verification.

**Step 5:** Once verified, the Privacy Team scopes the request to determine which Meridian systems contain the requestor's feedback data (see Data Inventory in Section 5.5).

### 5.3 Closed-Loop Feedback (CLF) Workflow

This procedure is triggered automatically upon any survey response with NPS 0-6 (Detractor) or upon any verbatim comment flagged with negative sentiment by the NLP engine, as well as any CSAT response ≤ 2 out of 5.

#### 5.3.1 Initial Response

**Step 1:** Within 4 business hours of Detractor receipt, the assigned Customer Success Manager (auto-routed by Salesforce based on account ownership) receives an email alert and a Salesforce Task with priority "High – Detractor CLF."

**Step 2:** The CSM reviews the customer's feedback, recent support ticket history, and any other relevant account context. The CSM drafts a personalized outreach, acknowledging the feedback, expressing Meridian's commitment to resolution, and proposing a follow-up call or meeting within 2 business days.

**Step 3:** The CSM sends the outreach communication, logs the communication in Salesforce against the CLF Task, and updates the Task status from "New" to "Contacted."

#### 5.3.2 Root Cause Analysis and Service Recovery

**Step 4:** The CSM conducts a discovery conversation with the customer to understand the specific drivers of dissatisfaction. The CSM documents findings in the "Root Cause Analysis" field of the CLF Task. Common root cause categories include: product bug/performance, usability/workflow friction, support response time, implementation quality, billing/invoicing error, or unmet feature expectation.

**Step 5:** The CSM defines a Service Recovery plan. Actions are documented as subtasks on the CLF Task and assigned to the appropriate teams (e.g., Engineering for a bug fix, Billing for an invoice correction, Product Management for a feature roadmap consideration).

**Step 6:** The CSM communicates the recovery plan and timeline to the customer within 3 business days of the initial outreach.

**Step 7:** The CSM tracks the recovery actions to completion, provides status updates to the customer at agreed-upon intervals, and confirms customer satisfaction with the recovery outcome.

**Step 8:** Upon customer confirmation of satisfaction, the CSM updates the CLF Task status to "Recovered – Follow-up Survey Sent" and closes the Task. The system automatically sends a follow-up transactional CSAT survey 7 days after closure.

#### 5.3.3 Escalation of Unresolved Detractors

**Step 9:** Any Detractor CLF Task remaining in "Contacted" or "In Recovery" status for more than 15 calendar days is automatically escalated to the Director of Customer Success for the relevant segment.

**Step 10:** If unresolved after 25 calendar days, the Task escalates to the VP of Customer Operations, who may engage the relevant Business Unit VP for intervention.

**Step 11:** The VP of Customer Operations reviews all Detractors aged >25 days quarterly as part of the Customer Experience Review meeting.

### 5.4 Trend Analysis and Monitoring Cadence

Customer Operations shall conduct trend analysis at the following cadences:

| Analysis Type | Frequency | Performed By | Reviewed By |
|---|---|---|---|
| Real-time anomaly detection | Continuous (automated) | Alerting platform (Datadog/PagerDuty) | IT Operations NOC |
| Weekly operational review | Weekly (Monday) | Customer Operations Analysts | Director of Customer Success |
| Monthly trend and KPI review | Monthly (first Thursday) | Customer Operations Analytics | VP of Customer Operations; shared with BU VPs |
| Quarterly executive summary | Quarterly (QBR cycle) | VP of Customer Operations | Executive Leadership Team, AI Governance Committee |
| Annual program review | Annually (December) | VP of Customer Operations | Board of Directors |

#### 5.4.1 Trend Analysis Procedure

**Step 1:** Data is automatically ingested from Qualtrics, Salesforce, Pendo, and any other approved FCP sources into the Snowflake Data Lake on a T+1 basis for batch sources and near-real-time for streaming sources (support ticket closure triggers). The ingestion pipeline performs schema validation, and any records failing validation are quarantined for manual review.

**Step 2:** On the monthly cadence, the Customer Operations Analytics team executes the "CSAT Monthly Trend Report" query package in Snowflake. The query computes for each business line and overall Meridian: mean CSAT, mean NPS, CES, response rates, Detractor/Promoter ratios, and primary sentiment themes from verbatim NLP.

**Step 3:** Results are compared against the thresholds defined in Section 7.2. For each metric breaching a threshold, the report automatically generates a Variance Note.

**Step 4:** The draft report is reviewed by the Director of Customer Success for narrative commentary on drivers, notable customer verbatims, and a summary of the month's CLF activities. The narrative specifically addresses any metric below the "Action Required" threshold.

**Step 5:** The final report is published to the Customer Operations SharePoint site, distributed via email to the Stakeholder Distribution List (as defined in Section 7.3), and presented at the Monthly Customer Experience Review meeting.

**Step 6:** The reviewed and approved report, along with the meeting minutes documenting management's review of the data, is archived in the Compliance Document Repository as evidence for SOC 2 CC7.0 management review controls.

### 5.5 CSAT Data Inventory and Lifecycle

Meridian maintains the following systems that process customer satisfaction data:

| System | Data Stored | Retention Period | Data Disposal Method | DSAR Location |
|---|---|---|---|---|
| Qualtrics | Survey responses, contact lists, survey definitions | 5 years post-collection | Automated purge per data retention schedule | Qualtrics "Data Subject Request" export tool |
| Salesforce (CRM) | CSAT scores (account/contact level), CLF Tasks, recovery actions | Duration of customer relationship + 7 years | Manual deletion by Salesforce Admin upon verified request | Salesforce "Data Export" contact-level |
| Snowflake (Data Lake) | Aggregated survey data, NLP sentiment scores, trend reports | 7 years | Table partition drop per retention policy | Snowflake data export for contact identifiers |
| Tableau (BI Dashboards) | Cached aggregate data only; no raw PII | Refreshed with each dashboard load (no persistent cache of PII) | N/A (no raw data stored) | N/A (no PII stored) |
| Pendo (In-App Feedback) | In-app CES responses, user GUID | 3 years | Automated deletion per retention schedule | Pendo user export API |

Data subjects exercising their right to erasure (GDPR Art. 17) or right to access (GDPR Art. 15) concerning their satisfaction feedback data shall follow the DSR procedure defined in SOP-PRIV-001. The DPO shall coordinate with IT Operations to extract the relevant data from the above-listed systems within the GDPR-mandated 30-calendar-day timeline.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Applicable System(s) |
|---|---|---|
| TC-017-01 | **Encryption in Transit:** All survey data transmitted between the customer's browser/device and Meridian servers shall be encrypted using TLS 1.2 or higher. | Qualtrics, Pendo, Salesforce API Gateway |
| TC-017-02 | **Encryption at Rest:** All CSAT databases and data warehouses shall employ AES-256 encryption at rest. | Snowflake, Salesforce, Qualtrics platform |
| TC-017-03 | **Role-Based Access Control (RBAC):** Access to raw survey data containing PII or PHI shall be restricted to personnel with a documented business need. RBAC groups defined in Okta shall govern access to Qualtrics and Snowflake. | Okta, Qualtrics, Snowflake |
| TC-017-04 | **Automated PII/PHI Redaction:** NLP pipelines processing verbatim feedback shall employ an automated redaction filter to identify and mask potential PHI/PII before the text is stored in the unstructured data repository. Flagged text is quarantined for manual review by the Privacy Team. | AWS Comprehend Medical (Clinical AI feedback), custom regex pipeline (general) |
| TC-017-05 | **API Authentication:** All inter-system integrations (e.g., Qualtrics-to-Snowflake, Salesforce-to-Qualtrics) shall use OAuth 2.0 mutual authentication with short-lived tokens. | API Gateway (Mulesoft) |
| TC-017-06 | **Audit Logging:** Immutable audit logs shall capture all access, modification, export, and deletion events for CSAT data in all systems of record. Logs shall be shipped to Splunk for centralized monitoring. | All systems in Section 5.5 |
| TC-017-07 | **Immutability:** Once a survey response is recorded, the raw response record in Qualtrics shall be immutable. Corrections shall be appended as a separate administrative note, not an overwrite of the original data. | Qualtrics |

### 6.2 Administrative Controls

| Control ID | Control Description |
|---|---|
| AC-017-01 | **Segregation of Duties for Survey Changes:** Survey configuration changes shall require separate individuals for (a) requesting the change, (b) approving the change, and (c) implementing the change. The survey change log shall record the identities of all three parties. Individuals with Qualtrics system administrator privileges are prohibited from approving their own changes; an independent approver as per the SCRF-017 workflow is required. |
| AC-017-02 | **Background Check Requirement:** All personnel with Administrator or equivalent access to Qualtrics, Salesforce CSAT objects, or the Snowflake CSAT schema shall have successfully completed a criminal background check prior to access provisioning, renewed every 3 years per SOP-HR-003. |
| AC-017-03 | **Quarterly Access Review:** The VP of IT Operations shall conduct a quarterly review of all user accounts with privileged access to CSAT systems, revoking any accounts no longer requiring such access. Evidence of the review shall be documented in ServiceNow and retained for SOC 2 audit. |
| AC-017-04 | **Confidentiality Agreement:** All Customer Operations, IT Operations, and analytics personnel with access to identifiable customer feedback data shall sign a confidentiality addendum as part of their employment or contractor agreement. |
| AC-017-05 | **Data Minimization:** Survey instruments shall be designed to collect only the minimum necessary personal data to achieve the purpose of the survey. Collection of demographic data beyond business-relevant attributes requires DPO approval. |
| AC-017-06 | **Survey Fatigue Management:** Customer contacts shall not receive more than one survey per 7 calendar days, enforced by the Qualtrics contact frequency ruleset. Customers who have unsubscribed or opted out of surveys shall be suppressed from all non-transactional survey distributions. |

### 6.3 Physical and Environmental Controls

Access to data centers and physical infrastructure hosting Meridian CSAT data is governed by Meridian's cloud-first strategy. All CSAT systems are hosted in SOC 2 Type II certified cloud environments (AWS, Salesforce). Physical and environmental controls are the responsibility of these subservice organizations, as assessed through Meridian's vendor risk management program (SOP-VRM-005).

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following KPIs are measured and reported through the Customer Operations Business Intelligence (BI) dashboards:

| KPI ID | Metric | Calculation | Target | Review Frequency |
|---|---|---|---|---|
| KPI-017-01 | Overall Customer Satisfaction (CSAT) | Mean score of all FCP-01, FCP-02, FCP-06 responses | ≥ 4.2 / 5.0 | Weekly |
| KPI-017-02 | Net Promoter Score (NPS) | % Promoters - % Detractors (FCP-03, FCP-04, FCP-07) | ≥ 45 | Monthly |
| KPI-017-03 | Customer Effort Score (CES) | Mean score of FCP-02, FCP-05 responses | ≤ 2.5 / 7.0 (lower is easier) | Monthly |
| KPI-017-04 | Survey Response Rate | (Completed surveys / Delivered surveys) * 100 | ≥ 18% overall | Monthly |
| KPI-017-05 | Detractor Recovery Rate | (% of Detractors recovered to Passive or Promoter within 90 days) | ≥ 60% | Quarterly |
| KPI-017-06 | CLF Initial Contact SLA | (% of Detractor CLF Tasks with "Contacted" status within 1 business day) | ≥ 95% | Weekly |
| KPI-017-07 | Time to Detractor Resolution | Mean calendar days from Detractor receipt to CLF Task closure as "Recovered" | ≤ 18 calendar days | Monthly |
| KPI-017-08 | Sentiment Polarity | Mean NLP sentiment score of all verbatim comments (-1.0 to +1.0) | ≥ +0.30 | Monthly |

### 7.2 Alert Thresholds and Breach Criteria

Monitored thresholds represent a baseline for investigation. Sustained breach of any threshold shall trigger the Escalation procedure in Section 8.2.

| Metric | Warning Threshold (Monitor & Investigate) | Critical Threshold (Escalate & CAPA Required) | Duration Requirement for Breach |
|---|---|---|---|
| Overall CSAT | < 4.0 for 1 week | < 3.5 for 2 consecutive weeks | Sustained (non-transient) |
| Overall NPS | < 30 | < 15 | 1 calendar quarter |
| CES | > 3.5 / 7.0 | > 4.5 / 7.0 | 1 calendar month |
| Survey Response Rate | < 10% | < 5% | 1 calendar quarter |
| CLF Initial Contact SLA | < 90% | < 75% | 1 calendar month |
| Detractor Recovery Rate | < 50% | < 30% | Rolling 6 months |
| Per-Business Unit CSAT Variance | > 0.3 points below corporate average | > 0.6 points below corporate average | 2 consecutive months |

### 7.3 Dashboards and Reporting

**CSAT Executive Dashboard (Tableau):** A real-time, read-only dashboard displaying current CSAT, NPS, CES, response rates, and Detractor/Promoter ratio by business line, updated hourly. Accessible to Directors and above. The dashboard shall include data for the prior rolling 12 months. A footer note shall indicate the last data refresh timestamp. Dashboard users are trained to manually review for anomalies; automated anomaly detection is under evaluation. The dashboard does not currently include a configurable alert mechanism for proactive threshold notifications.

**CSAT Analyst Workbench (Snowflake + JupyterHub):** An interactive analytics environment for the Customer Operations Analytics team to perform deep-dive trend analysis, cohort analysis, and ad-hoc reporting.

**Monthly Trend Report (PDF):** A formal report per Section 5.4.1, distributed by the 10th calendar day of the following month.

**Quarterly Board Report:** A 2-page executive summary prepared by the VP of Customer Operations, including trended NPS, top 3 drivers of satisfaction and dissatisfaction from verbatim analysis, and a summary of systemic improvement initiatives.

### 7.4 SOC 2 Monitoring Evidence

In alignment with SOC 2 CC7.0 (Monitoring Activities), the following evidence artifacts are generated and retained:

1.  **Scheduled Review Logs:** Dated, timestamped logs of all scheduled dashboard reviews performed by Customer Operations, including name of reviewer and any observations noted. These are captured via a mandatory "Review Acknowledgement" checkbox on the Monthly Trend Report cover page.
2.  **Anomaly Investigation Records:** ServiceNow Incidents created in response to any detected anomaly or sustained negative trend, with documented root cause analysis and remediation steps.
3.  **CLF Case Audit Trail:** Complete Salesforce audit trail for each CLF Task, documenting all status changes, communications, and recovery actions.
4.  **Annual Program Effectiveness Review:** A memo prepared by the VP of Customer Operations, presented to the Compliance Officer, attesting to the continued effectiveness of the CSAT monitoring program as a management monitoring control.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Requests

Requests for exceptions to any provision of this SOP shall be submitted via the Policy Exception Request process in ServiceNow (SOP-COMP-002).

**Procedure:**

**Step 1:** Requestor completes the ServiceNow "Policy Exception Request" form, specifying the SOP ID (SOP-COPS-017), the specific policy statement or procedure step for which exception is sought, the business justification, the scope of impact (e.g., specific customer, product, time period), and any compensating controls proposed.

**Step 2:** The request is routed for sequential approval:
-   **First-Line Approver:** Requestor's direct manager
-   **Second-Line Approver (Business Unit Owner):** VP of Customer Operations (Michael Chang)
-   **Final Approver (Risk Acceptance):** Chief Compliance Officer (Thomas Anderson)

**Step 3:** The Compliance Officer evaluates the aggregate risk posture of all active exceptions and may impose a sunset clause (maximum 12-month validity) and mandatory compensating controls.

**Step 4:** Approved exceptions are logged in the Policy Exception Register (ServiceNow). The register is reviewed by the Compliance Officer quarterly. Expired exceptions where the underlying condition has not been remediated require a new exception request.

### 8.2 Escalation Procedures

Escalation triggers and their prescribed paths are defined below.

| Trigger Condition | Escalation Level 1 (within 24 business hours) | Escalation Level 2 (if Level 1 unresolved for 5 business days) | Escalation Level 3 (if Level 2 unresolved for 10 business days) |
|---|---|---|---|
| Critical Threshold Breach (Section 7.2) | VP of Customer Operations + Relevant BU VP | Chief Compliance Officer + Chief Privacy Officer | CEO (or COO delegate) |
| Detractor CLF Task > 15 days without resolution | Director of Customer Success | VP of Customer Operations | Relevant BU VP + VP of Customer Operations |
| Suspected PHI/PII in feedback verbatim | IT Operations (for quarantine) + DPO | Chief Information Security Officer (CISO) | Chief Compliance Officer |
| Customer complaint alleging retaliation | Chief Compliance Officer | CEO | Board of Directors (Audit Committee Chair) |
| Inability to meet CLF SLA for > 5% of Detractors in a week | VP of Customer Operations | Chief Operating Officer (COO delegate) | CEO |

### 8.3 Escalation Communication

All escalations shall be communicated via email to the prescribed distribution lists with the subject line format: `ESCALATION: [Trigger Category] – [Brief Description] – [Priority: High]`. The communication shall include the incident summary, CSAT data involved, impacted customers, current status, and action requested of the escalation recipient.

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum

All personnel assigned responsibilities under this SOP shall complete the following training:

| Training Module ID | Module Name | Target Audience | Delivery Method | Frequency | Competency Assessment |
|---|---|---|---|---|---|
| TRN-COPS-017-01 | CSAT Program Fundamentals | All customer-facing personnel (CSMs, Support, Sales, Professional Services) | LMS (Workday Learning) eLearning (45 min) | Within 30 days of hire; Annual refresher | Post-course quiz; 85% passing score |
| TRN-COPS-017-02 | Closed-Loop Feedback Execution | Customer Success Managers, Support Team Leads | Instructor-led virtual workshop (2 hours) | Within 30 days of hire; Biennial refresher | Simulated CLF scenario; manager sign-off |
| TRN-COPS-017-03 | CSAT Data Privacy & GDPR | All personnel with access to raw CSAT data | LMS eLearning (30 min) | Annual | Post-course quiz; 90% passing score; mandatory for access provisioning |
| TRN-COPS-017-04 | Dashboard Interpretation & Anomaly Detection | Customer Operations Analysts, CSM Managers | Instructor-led (1 hour) | Within 30 days of role assignment | Practical exercise: analyze a sample monthly report |
| TRN-COPS-017-05 | Exception and Escalation Procedures | VP, Directors, Compliance Team | Job aid document + recorded briefing | As needed upon SOP revision | Acknowledgement of comprehension form |

### 9.2 Training Compliance Tracking

Training completion records are maintained within Workday Learning. The VP of Customer Operations shall receive a monthly training compliance report. Any personnel in a role requiring training who are delinquent by more than 15 calendar days past the due date shall have their access to CSAT data systems temporarily suspended by IT Operations until training is completed.

### 9.3 SOP Awareness

Upon each revision of this SOP, a summary of changes notification shall be distributed to all affected personnel via the Meridian Policy Update Newsletter. Receipt and acknowledgement of the updated SOP is tracked within the Qualys Policy Compliance module.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Document Title | Relationship to SOP-COPS-017 |
|---|---|---|
| SOP-PRIV-001 | Data Privacy and Protection Policy | Governs handling of PII/PHI in CSAT data; DSAR procedures |
| SOP-COMP-002 | Policy Exception and Management Process | Governs the exception handling workflow defined in Section 8.1 |
| SOP-HR-003 | Pre-Employment Background Screening | Governs background checks required under AC-017-02 |
| SOP-SEC-012 | Access Control and User Access Review | Governs RBAC principles and quarterly access reviews |
| SOP-VRM-005 | Vendor Risk Management | Governs assessment of subservice organizations hosting CSAT systems |
| SOP-REG-031 | Post-Market Surveillance (MDR) | Related clinical feedback processes for EU MDR compliance |
| SOP-CLIN-023 | Clinical Complaint Handling | Governs clinical feedback distinct from general CSAT |
| SOP-CHG-008 | IT Change Management | Governs technical changes to survey infrastructure |
| SOP-DATA-009 | Data Retention and Disposal | Governs CSAT data lifecycle timelines |

### 10.2 External Standards and Regulatory References

| Reference | Description | Applicable Section(s) |
|---|---|---|
| SOC 2 TSC CC7.0 (2017) | Trust Services Criteria: Monitoring Activities | Sections 4, 5.4, 7.4 |
| SOC 2 TSC P5.2 (2017) | Trust Services Criteria: Notice of Privacy Practices | Section 4 (PS-017-03) |
| SOC 2 TSC CC6.1 (2017) | Trust Services Criteria: Logical and Physical Access Controls | Section 6.1 |
| GDPR Art. 6, 7, 15, 17, 21 | Lawfulness, Consent, Right of Access, Right to Erasure, Right to Object | Sections 4, 5.2, 5.5, 9.1 |
| GDPR Art. 35 | Data Protection Impact Assessment (DPIA) | Trigger for material changes to CSAT data processing |
| HIPAA Privacy Rule 45 CFR §164.508 | Uses and Disclosures of PHI | Section 4 (PS-017-03) |

---

## 11. Revision History

| Version | Effective Date | Author(s) | Description of Changes |
|---|---|---|---|
| 5.2 | 2024-08-08 | Michael Chang, VP of Customer Ops; Thomas Anderson, CCO | Minor revision: Updated NPS target from 50 to 45 to reflect post-MDR recalibration. Clarified sunset clause procedure in Exception Handling (Section 8.1, Step 3). Added Pendo as an FCP channel (FCP-05). Updated role titles for organizational changes. SOC 2 CC7.0 evidence alignment reviewed. |
| 5.1 | 2024-02-15 | Michael Chang; Dr. Klaus Weber (DPO) | Revised consent language in FCP-04 and FCP-07 for EU customers per updated EDPB guidelines. Added explicit DSAR handling in Section 5.2. Introduced TRN-COPS-017-05 (Escalation training) in response to internal audit finding #2024-AUD-11. |
| 5.0 | 2023-10-12 | Michael Chang; Samantha Torres (VP IT Ops) | Major rewrite for SOC 2 readiness. Introduced formal RACI, KPIs with thresholds, CLF workflow, and Qualtrics-to-Snowflake data pipeline definition. Transitioned from annual-only survey to multi-FCP model. |
| 4.0 | 2022-05-03 | Previous VP, Customer Success | Introduced NPS methodology and standard survey instruments. Established basic CLF concept. |
| 3.1 | 2021-01-20 | Customer Operations Director | Updated to include MedInsight Analytics business line in scope following acquisition integration. |

---

**END OF DOCUMENT**

*This document is the property of Meridian Health Technologies, Inc. Dissemination, distribution, or reproduction outside of authorized channels is prohibited. Document classification: Internal.*