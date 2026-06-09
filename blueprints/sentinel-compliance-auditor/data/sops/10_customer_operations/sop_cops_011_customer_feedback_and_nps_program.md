---
sop_id: "SOP-COPS-011"
title: "Customer Feedback and NPS Program"
business_unit: "Customer Operations"
version: "5.8"
effective_date: "2025-11-10"
last_reviewed: "2026-12-24"
next_review: "2027-06-26"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for the systematic collection, analysis, and actioning of customer feedback across all Meridian Health Technologies, Inc. product lines and service touchpoints. The Customer Feedback and Net Promoter Score (NPS) Program is designed to create a closed-loop feedback ecosystem that directly informs product development, service delivery improvements, and strategic decision-making at the executive level. This program serves as the primary mechanism through which the voice of the customer is captured, quantified, and operationalized across the organization.

The program objectives include: measuring customer loyalty and satisfaction through standardized NPS methodology; identifying at-risk accounts and triggering proactive retention interventions; surfacing product enhancement opportunities with quantified customer impact; benchmarking Meridian performance against industry standards; and demonstrating measurable improvement in customer experience metrics to the Board of Directors and external auditors as part of the SOC 2 Type II management review controls.

### 1.2 Scope

This SOP applies to all Meridian Health Technologies business units, product lines, and geographies, including the Boston headquarters and London, Berlin, Singapore, and Toronto offices. The procedures herein govern all customer feedback collection mechanisms, including but not limited to: transactional NPS surveys triggered by specific customer interactions; relationship NPS surveys measuring overall sentiment; in-product feedback widgets; structured customer interviews; and unsolicited feedback captured through Customer Operations channels.

**In-Scope Products and Platforms:**
- Clinical AI Platform (deployed across 340+ hospitals and clinics)
- HealthPay Financial Services (processing $4.2B annually)
- MedInsight Analytics (handling PHI for ~12M patients)
- Meridian SaaS Platform (multi-tenant, AWS-hosted infrastructure)

**In-Scope Customer Segments:**
- Healthcare providers (hospitals, clinics, physician groups)
- Healthcare payers (insurance companies, government programs)
- Patients utilizing patient-facing financing and payment tools
- Platform partners and integrators

**Out of Scope:**
- Employee satisfaction or internal engagement surveys (managed by Human Resources under SOP-HR-042)
- Vendor performance evaluations
- Clinical outcomes measurement and efficacy studies (managed by Clinical Affairs under SOP-CA-018)

### 1.3 Audience

All Meridian personnel who design, deploy, manage, analyze, or act upon customer feedback surveys are bound by this SOP. This includes employees in Customer Operations, Product Management, Engineering, Clinical Affairs, Marketing, Sales, and executive leadership. Third-party vendors engaged for survey administration or analytics must also comply with the requirements herein through contractual obligations.

---

## 2. Definitions and Acronyms

| Term | Definition |
|------|------------|
| **Net Promoter Score (NPS)** | A customer loyalty metric derived from the likelihood-to-recommend question measured on a 0-10 scale, calculated as %Promoters (9-10) minus %Detractors (0-6) |
| **Transactional NPS (tNPS)** | NPS survey triggered by a specific customer interaction or touchpoint (e.g., support ticket resolution, onboarding completion, feature adoption) |
| **Relationship NPS (rNPS)** | NPS survey measuring overall sentiment toward the customer relationship, typically deployed on a semi-annual or annual cadence |
| **CSAT** | Customer Satisfaction score, typically a 1-5 rating on a specific interaction |
| **CES** | Customer Effort Score, measuring ease of interaction on a 1-7 scale |
| **Detractor** | Customer providing an NPS score of 0-6; at risk of churn or negative word-of-mouth |
| **Passive** | Customer providing an NPS score of 7-8; satisfied but not loyal |
| **Promoter** | Customer providing an NPS score of 9-10; loyal enthusiast likely to refer others |
| **Closed-Loop Feedback** | Process by which customer feedback results in a direct response to the customer and systematic organizational action |
| **Feedback Taxonomy** | Standardized categorization system for open-text feedback responses |
| **Inner Loop** | Immediate response to individual customer feedback (typically within 24-72 hours for Detractors) |
| **Outer Loop** | Organizational process improvement driven by aggregate feedback trends |
| **Survey Fatigue** | Decline in response rates and quality due to excessive survey frequency |
| **Response Rate** | Percentage of delivered surveys that receive a completed response |
| **Customer Health Score** | Composite metric incorporating NPS, product adoption, support volume, and financial indicators |
| **Gainsight** | Customer success platform used for health scoring and feedback workflow automation |
| **Qualtrics** | Enterprise survey platform for NPS and CSAT survey administration |
| **Salesforce Service Cloud** | CRM platform where support interactions and case management occur |
| **Snowflake** | Enterprise data warehouse where survey responses are integrated with product usage telemetry |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

| Activity | Customer Operations VP (Michael Chang) | Customer Insights Manager | Program Managers | Customer Success Managers (CSMs) | Product Managers | Engineering Leads | Executive Sponsors |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Survey Design Approval | A | R | C | C | C | I | I |
| Survey Deployment | I | A | R | I | I | I | I |
| Detractor Response | A | I | C | R | C | I | I |
| Trend Analysis | R | A | C | C | C | I | I |
| Action Planning | A | R | C | C | R | C | I |
| Product Roadmap Integration | C | C | I | I | R | A | I |
| Executive Review | R | C | I | I | I | I | A |
| Customer Data Management | A | R | I | R | I | I | I |

**Key:** R = Responsible (executor), A = Accountable (approver), C = Consulted, I = Informed

### 3.2 Detailed Role Descriptions

**Michael Chang, VP of Customer Operations (Program Owner)**
- Ultimate accountability for program effectiveness and regulatory compliance
- Approves survey frequency thresholds and audience selection criteria
- Authorizes Detractor escalation workflows and retention playbooks
- Chairs quarterly executive feedback review
- Approves annual NPS benchmark targets for executive compensation linkage

**Customer Insights Manager (Operational Lead)**
- Designs survey instruments and respondent sampling methodology
- Manages Qualtrics instance configuration and integration with Gainsight and Snowflake
- Conducts quarterly trend analysis and delivers insights reports
- Maintains the Feedback Taxonomy and ensures consistent coding of open-text responses
- Monitors response rates and survey fatigue indicators
- Coordinates with Product Management for feature-request triage

**Customer Success Managers (CSMs) — Inner Loop Owners**
- Receive real-time Detractor alerts via Gainsight within 2 hours of survey submission
- Execute Detractor outreach playbook within 24-hour SLA
- Document Detractor interactions and resolution outcomes in Gainsight Timeline
- Escalate unresolved Detractor cases with churn risk score >7 to Customer Operations leadership
- Conduct semi-annual relationship NPS review calls with strategic accounts (>$500K ARR)

**Product Managers — Outer Loop Owners**
- Review monthly aggregated feedback trends for assigned product area
- Quantify customer impact of top-requested enhancements using NPS correlation
- Present feature prioritization recommendations informed by feedback at monthly Product Council
- Respond to CSM inquiries regarding feedback-driven feature status within 5 business days

**Engineering Leads**
- Implement in-product feedback collection mechanisms per specifications
- Ensure survey triggering logic integrates with Snowflake event streams
- Support Gainsight-Qualtrics API integration maintenance

**Executive Sponsors (Robert Liu, VP of Financial Services; Clinical AI VP)**
- Review quarterly NPS trends and action plan progress
- Approve resource allocation for high-impact outer loop initiatives exceeding $100K investment
- Champion customer-centricity at Board-level discussions

---

## 4. Policy Statements

### 4.1 Survey Frequency and Fatigue Management

Meridian is committed to responsible survey practices that respect customer time and attention. No individual customer contact shall receive more than six (6) survey invitations within any rolling twelve-month period. Customer Success Managers must review individual survey history in Gainsight prior to adding any ad-hoc survey recipients to ensure compliance with this limit. The Customer Insights Manager maintains a Survey Frequency Dashboard and must flag any accounts approaching the six-survey threshold for review by the VP of Customer Operations.

### 4.2 Survey Design Standards

All customer-facing surveys must adhere to the Meridian Survey Design Standards maintained by Customer Operations. The standard likelihood-to-recommend question ("How likely are you to recommend [Product Name] to a colleague or peer?") must appear as the primary NPS question across all Meridian surveys to ensure metric comparability. Rating scales must not be modified without approval from the VP of Customer Operations and VP of Clinical Affairs (for clinical products). Open-text follow-up questions must use standardized prompts from the approved question bank.

### 4.3 Inner Loop Response Commitments

All Detractor (0-6 NPS) responses must receive human follow-up within 24 business hours of survey submission. Detractor follow-up must be documented in Gainsight with the outcome code, resolution status, and any resulting escalation. Escalations involving potential regulatory, legal, or safety issues must be elevated to the Chief Customer Officer within 4 hours of identification.

### 4.4 Outer Loop Transparency

Aggregate NPS results, trend analyses, and top-cited themes from open-text feedback must be published to the internal Customer Insights Dashboard accessible to all Meridian employees (subject to role-based access controls for customer-identifiable data). Quarterly NPS results, including business unit and product-line breakdown, must be presented to the Executive Leadership Team within 30 days of quarter-end.

### 4.5 Anti-Gaming and Integrity

No Meridian personnel shall influence, coach, or incent customers to provide specific NPS scores. Survey targeting must not be manipulated to exclude known Detractors or over-sample Promoters. Any suspected manipulation must be reported to the VP of Customer Operations immediately. Confirmed violations will result in disciplinary action up to and including termination per SOP-HR-029.

### 4.6 Data Quality

Survey response data must be stored in Snowflake with complete audit trail including respondent identifier, survey instrument version, timestamp, channel, triggering event (for transactional surveys), and raw score. Data exports for external reporting must include metadata sufficient to validate sample composition.

---

## 5. Detailed Procedures

### 5.1 Survey Design and Instrument Development

#### 5.1.1 Survey Type Determination

The Customer Insights Manager, in collaboration with the requesting business stakeholder, determines the appropriate survey type based on the measurement objective:

| Objective | Survey Type | Cadence |
|-----------|-------------|---------|
| Measure loyalty and benchmark competitively | rNPS | Semi-annual (Q2, Q4) |
| Evaluate specific interaction quality | tNPS | Event-triggered |
| Assess ease of specific task completion | CES | Event-triggered |
| Evaluate feature satisfaction | CSAT | Post-adoption (30-day) |

#### 5.1.2 Question Design Process

1. **Stakeholder Consultation**: Requester completes Survey Request Form (SRF) in the Customer Operations SharePoint portal, specifying measurement objective, target audience segment, triggering conditions, and desired insights.

2. **Question Bank Selection**: The Customer Insights Manager selects questions from the approved question bank catalogued in Qualtrics library. Custom questions require VP of Customer Operations approval and must be validated through cognitive testing with a minimum of 5 internal, non-customer users prior to deployment.

3. **Survey Flow Design**:
   - Question 1: Primary NPS question (required, 0-10 scale)
   - Question 2: Open-text follow-up ("What is the primary reason for your score?")
   - Question 3: Category-specific CSAT (as applicable, 1-5 scale)
   - Question 4: Open-text improvement suggestion ("What could we do to improve?")
   - Question 5: Opt-in for follow-up contact (Yes/No, with contact preference selection)

4. **Mobile Optimization**: Surveys must render correctly on mobile devices. Survey length must not exceed 5 questions to maintain mobile completion rates above 70%.

5. **Localization**: Surveys targeting customers in non-English speaking regions must be translated by an approved localization vendor. Translated instruments require back-translation validation by a native speaker not involved in the initial translation.

#### 5.1.3 Survey Review and Approval

1. Draft survey instrument is reviewed by the Customer Insights Manager within 3 business days of SRF submission.

2. For surveys targeting Clinical AI Platform customers, Clinical Affairs review is required to ensure no clinical outcome implications are inadvertently suggested.

3. VP of Customer Operations provides final approval for all net-new survey instruments or significant revisions to existing instruments. Minor revisions (text corrections, non-substantive question reordering) may be approved by the Customer Insights Manager.

4. Approved instruments are assigned a unique Survey ID and loaded into Qualtrics with the approval metadata.

### 5.2 Data Collection

#### 5.2.1 Audience Selection

Customer contact lists for survey deployment are generated from Gainsight per the following rules:

- **Active Customers**: Accounts with status "Active" or "Implementing" and with at least one logged platform interaction within the preceding 90 days
- **Contact Selection**: Primary Business Contact and Technical Contact roles, plus any additional contacts designated as "Survey Eligible" by the assigned CSM
- **Exclusion Rules**: Contacts who have opted out of research communications, contacts with open Critical (P1) support cases, and contacts who have received >5 survey invitations in the trailing 12 months are automatically suppressed
- **Minimum Sample**: Transactional surveys require a minimum eligible population of 30 contacts to proceed; smaller populations require VP approval and use of qualitative interview methods instead

#### 5.2.2 Survey Deployment Channels

| Channel | Use Case | Platform |
|---------|----------|----------|
| Email | All rNPS, most tNPS | Qualtrics Email Engine |
| In-Product Widget | Post-interaction tNPS, CES | Embedded via Gainsight PX |
| SMS | Urgent interaction follow-up (support) | Twilio integrated with Qualtrics |
| In-Person/Phone | Strategic account quarterly business reviews | CSM-administered, tablet entry |

Email remains the primary channel for relationship surveys. In-product widgets are preferred for transactional surveys to maximize context relevance and response rates.

#### 5.2.3 Deployment Schedule and Triggers

**Relationship NPS (rNPS) Deployment Calendar:**

| Cohort | Deployment Window | Close Date |
|--------|-------------------|------------|
| Cohort A: Strategic Accounts (>$500K ARR) | February 10-14, August 10-14 | February 28, August 31 |
| Cohort B: Growth Accounts ($100K-$500K ARR) | March 1-5, September 1-5 | March 21, September 21 |
| Cohort C: Standard Accounts (<$100K ARR) | March 15-19, September 15-19 | April 4, October 4 |

**Transactional NPS (tNPS) Triggers (configured in Gainsight PX):**

| Trigger Event | Survey Type | Delay Before Send |
|---------------|-------------|-------------------|
| Support ticket resolution (P2-P4) | CSAT + NPS | 2 hours |
| Onboarding milestone completion (Phase 2) | tNPS + CES | 24 hours |
| Feature adoption event (3rd use of new feature) | Feature CSAT | 7 days post-adoption |
| Quarter-end business review completion | rNPS (subset) | 48 hours |
| Renewal completed | Transactional Relationship Pulse | 5 business days |

#### 5.2.4 Survey Fielding and Monitoring

During active deployment periods, the Customer Insights Manager monitors the following metrics daily:

- **Response Rate**: Target >25% for rNPS, >15% for tNPS
- **Completion Rate**: Target >90% of started surveys completed
- **Survey Drop-off Point**: Identify questions causing abandonment

If response rate falls below 15% for any deployment after 7 days, the Customer Insights Manager sends a reminder email (maximum one reminder per deployment) and evaluates whether alternative channels or incentives are warranted.

### 5.3 Data Analysis and Interpretation

#### 5.3.1 NPS Calculation

NPS is calculated at the survey deployment level:

```
NPS = (% of respondents scoring 9-10) - (% of respondents scoring 0-6)
```

Results are reported with the margin of error at 95% confidence interval using the formula:

```
Margin of Error = 1.96 × √(p(1-p)/n)
```

_where p is the proportion and n is the sample size._

Statistical significance testing is applied when comparing NPS across time periods or segments. A minimum sample of 30 responses per segment is required for segment-level reporting.

#### 5.3.2 Open-Text Feedback Classification

All open-text responses from the "primary reason" follow-up question are classified using the Feedback Taxonomy maintained in Gainsight. The taxonomy has three hierarchy levels:

1. **Category** (e.g., Product Functionality, Support Quality, Pricing, Onboarding)
2. **Subcategory** (e.g., under Product Functionality: Bug, Missing Feature, Performance, Usability)
3. **Theme** (e.g., under Missing Feature: Clinical Workflow, Reporting, Integration, Configuration)

Classification is initially performed by the Qualtrics Text iQ natural language processing engine with supervised machine learning models trained on a minimum of 5,000 previously human-coded responses. Classifications with <80% confidence score are routed to the Customer Insights team for manual review within 5 business days.

#### 5.3.3 Segmentation Analysis

Results are disaggregated across the following standard segmentation dimensions:

- **Product Line**: Clinical AI Platform, HealthPay, MedInsight, Platform/Infrastructure
- **Customer Segment**: Hospital (>500 beds), Hospital (<500 beds), Clinic/Ambulatory, Payer, Patient-Facing
- **ARR Tier**: Strategic (>$500K), Growth ($100K-$500K), Standard (<$100K)
- **Tenure**: New (<6 months), Growing (6-24 months), Established (>24 months)
- **Geography**: North America, Europe, APAC

Correlation analysis identifies the key drivers of NPS movement. Product usage telemetry data from Snowflake is joined with NPS responses to quantify the relationship between feature adoption and loyalty scores.

#### 5.3.4 Quarterly Trend Report Structure

The standard quarterly report includes:

1. Executive Summary (1-page dashboard view)
2. Overall NPS and Trend (trailing 8 quarters)
3. Product Line NPS Comparison
4. Segment Deep-Dives (for any segment with >50 responses)
5. Top 10 Themes from Open-Text Feedback (with sample verbatim quotes, de-identified)
6. Detractor Recovery Rate and Time-to-Response metrics
7. Action Plan Progress Update (from prior quarter commitments)
8. Recommendations for Next Quarter

### 5.4 Action Planning — Inner Loop

#### 5.4.1 Detractor Alert and Response Workflow

```
Survey Submitted (NPS 0-6)
    → Gainsight creates "Detractor Alert" Timeline entry [immediate]
    → Email notification to assigned CSM + CSM Manager [immediate]
    → CSM reviews survey response, account health score, and recent interaction history [within 2 hours]
    → CSM executes Detractor Outreach Playbook: [within 24 hours]
        1. Call or email customer (prefer call for accounts >$100K ARR)
        2. Acknowledge feedback directly, thank customer for honesty
        3. Probe for root cause: "Help us understand what led to this score"
        4. Document in Gainsight with Detractor Response Template
        5. Assess and classify: Solvable now | Escalation needed | Churn risk
        6. If churn risk: Create "At-Risk Account" flag, notify VP Customer Operations
    → CSM logs resolution outcome, customer response, and follow-up commitments [within 72 hours]
    → Customer Operations monitors Detractor case closure rate weekly
```

#### 5.4.2 Promoter Engagement

Promoters (NPS 9-10) are engaged through:
- Automated thank-you email with request for testimonial or case study participation
- Referral program invitation (HealthPay product line only, where referral program exists)
- Invitation to Customer Advisory Board (if meeting CAB membership criteria per SOP-PROD-034)

#### 5.4.3 Passive Monitoring

Passives (NPS 7-8) receive no immediate reactive outreach but are included in analysis identifying accounts approaching Detractor territory. CSMs review Passive trends during quarterly business reviews.

### 5.5 Action Planning — Outer Loop

#### 5.5.1 Feedback-to-Product Integration

The Customer Insights Manager prepares a monthly "Voice of Customer Input for Product" package delivered to Product Management by the 10th of each month. This package includes:

- Top 20 requested features/enhancements from open-text feedback, with frequency counts and associated NPS impact estimation
- Product area CSAT trending
- Verbatim excerpts related to product-specific feedback (de-identified)
- Detractor volume and primary cited reasons by product area

Product Managers review the package and update the "Feedback Status" field in the Product Backlog (maintained in Aha! roadmapping tool) for each tracked feedback item:
- **Under Consideration**: Acknowledged, not yet prioritized
- **Planned**: Committed to roadmap, target release specified
- **In Development**: Engineering work active
- **Delivered**: Released to customers
- **Declined**: Will not pursue, rationale documented

Status updates are communicated back to the originating CSM within 5 business days of status change.

#### 5.5.2 Cross-Functional Action Planning Workshops

Quarterly, within 2 weeks of the quarterly NPS report publication, the Customer Insights Manager facilitates a 4-hour cross-functional workshop. Required attendees:

- VP of Customer Operations (Chair)
- Customer Insights Manager (Facilitator)
- Product Management Leads for each product line
- Engineering Directors for each product line
- Head of Support
- Head of Professional Services (Onboarding)
- Marketing Director
- Two rotating CSMs (nominated quarterly for frontline perspective)

Workshop agenda:
1. Review quarterly results (30 min)
2. Deep-dive on top 3 Detractor themes (60 min)
3. Ideation and solution generation (90 min)
4. Prioritization: Impact vs. Effort matrix voting (30 min)
5. Action Plan commitment: Owner, deliverable, timeline (30 min)

Workshop output is a formal Action Plan document, approved by the VP of Customer Operations and published to the company wiki within 5 business days.

---

## 6. Controls and Safeguards

### 6.1 Access Controls

Survey response data in Snowflake is subject to role-based access controls:

| Role | Access Level |
|------|--------------|
| Customer Insights Team | Full access (all fields, all respondents) |
| Customer Success Managers | Account-level access (own portfolio only, contact-identifiable) |
| Product Managers | Aggregated, de-identified views (minimum 10 respondents per aggregation cell) |
| Engineering | Aggregated, de-identified views (no verbatim text access without approval) |
| Executive Leadership | Aggregated with account-level drill-down capability |
| Sales | Aggregated NPS trend, no individual response access |
| All Other Employees | Dashboard-level aggregate views only |

### 6.2 Data Storage and Retention

Survey response data is stored in Snowflake with the following retention schedule:

- Raw survey responses (identifiable): 7 years from collection date
- Aggregated, de-identified analytics: Indefinite (for longitudinal trend analysis)
- Gainsight Timeline entries: Duration of customer relationship + 3 years post-offboarding
- Qualtrics survey instrument versions: Indefinite (for audit of methodology changes)

### 6.3 Data Integrity Controls

- Qualtrics survey completion events are written to Snowflake via the Qualtrics REST API connector within 15 minutes of submission
- Daily reconciliation between Qualtrics raw response counts and Snowflake load counts is performed by the Data Engineering team; discrepancies >2% trigger investigation within 24 hours
- Survey instrument version ID is captured with every response to enable longitudinal analysis with methodology change awareness
- IP address and submission timestamp are captured for duplicate detection; submissions from the same IP with identical scores within 5 minutes trigger deduplication review

### 6.4 Customer Communication Preferences

Customers may manage their research communication preferences through the Preference Center (linked in every survey invitation email). Opt-out requests are processed within 24 hours through integration between the Preference Center and Gainsight contact records. Surveys sent to contacts with "Research Communications: Opted Out" status constitute a compliance violation and must be reported to the VP of Customer Operations.

### 6.5 Vendor Management

Third-party survey administration platforms (currently Qualtrics) must maintain SOC 2 Type II certification. Annual vendor risk assessments are conducted by the Information Security team. Contract terms must include incident notification within 24 hours of data breach discovery.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Program Health KPIs

| Metric | Target | Measurement Frequency | Owner |
|--------|--------|----------------------|-------|
| Relationship NPS Response Rate | >30% | Per deployment | Customer Insights Mgr |
| Transactional NPS Response Rate | >18% | Monthly | Customer Insights Mgr |
| Detractor Follow-up SLA (24 hrs) | >95% compliance | Weekly | Customer Operations VP |
| Survey Fatigue Incidents | 0 incidents (no contact >6 surveys/12mo) | Monthly | Customer Insights Mgr |
| Feedback Taxonomy Classification Accuracy | >85% automated | Quarterly audit (250 random samples) | Customer Insights Mgr |
| Inner Loop Case Closure (Detractor) | >90% closed within 72 hours | Weekly | Customer Operations VP |

### 7.2 Program Dashboards

**Executive NPS Dashboard** (Tableau, updated weekly)
- Visible to: C-Suite, VPs, Directors
- Content: Overall NPS trend, product-line NPS, segment NPS, NPS by region, Detractor volume trend, response rate trend
- Refresh: Weekly (Monday 08:00 ET)

**Operational Feedback Dashboard** (Gainsight, updated near-real-time)
- Visible to: Customer Success team, Support team, Product Managers
- Content: Individual Detractor alerts, Detractor case status, open-text feedback stream, response rate by CSM portfolio
- Refresh: Near-real-time (alert delay <15 minutes from survey submission)

**Product Feedback Backlog Dashboard** (Aha!, updated bi-weekly)
- Visible to: Product, Engineering, Customer Operations
- Content: Top customer-requested items, status, associated NPS impact, CSM inquiries
- Refresh: Bi-weekly per Product Manager updates

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Delivery |
|--------|----------|-----------|----------|
| NPS Pulse (1-page summary) | Executive Leadership Team | Monthly | Email + dashboard link |
| Quarterly NPS Deep-Dive Report | Executive Leadership Team, Board | Quarterly | Board deck section + standalone report |
| Product Feedback Package | Product Management | Monthly | Confluence page |
| Detractor Case Analysis | Customer Operations VP | Weekly | Gainsight dashboard review |
| rNPS Deployment Summary | All Customer-Facing Staff | Per deployment (2x/year) | All-hands presentation + internal blog post |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types and Approval Authority

| Exception Type | Example | Approval Required |
|----------------|---------|-------------------|
| Survey Frequency | Customer requests additional survey touchpoints | Customer Insights Manager |
| Instrument Deviation | Business unit requests non-standard question | VP of Customer Operations |
| Deployment Timing | Off-cycle rNPS for M&A-integrated accounts | VP of Customer Operations |
| Response Rate Waiver | Segment with <30 responses; proceed to report with caveats | Customer Insights Manager (documented) |
| Detractor SLA Extension | Customer contact unreachable despite 3 attempts in 24 hours | CSM Manager (documented in Gainsight) |
| Data Access Exception | Non-standard access to identifiable response data | VP of Customer Operations + Information Security |

### 8.2 Escalation Paths

**Operational Escalation (Inner Loop Failure):**
- CSM unable to close Detractor case within 72 hours → Escalate to CSM Manager
- CSM Manager unable to resolve within additional 48 hours → Escalate to Director, Customer Success
- Director unable to resolve (account at material churn risk) → Escalate to VP Customer Operations + Account Executive

**Strategic Escalation (Outer Loop Impasse):**
- Action Plan task unowned or deadline at risk → Customer Insights Manager flags to VP Customer Operations
- Product commitment not progressing → Product Manager escalates to VP Product
- Cross-functional disagreement on prioritization → VP Customer Operations + VP Product jointly resolve

**Safety or Regulatory Concern:**
- Survey response indicates patient safety issue, clinical adverse event, or potential regulatory non-compliance → Immediately (within 1 hour) notify Chief Medical Officer and Chief Compliance Officer per SOP-CA-052

### 8.3 Exception Logging

All exceptions must be logged in the Customer Operations Exception Register (SharePoint list) with: exception type, date raised, requestor, justification, approval decision, approver name, and date resolved. Quarterly exception log review is conducted by the VP of Customer Operations.

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Training Module | Audience | Initial Timing | Refresher Cadence | Delivery Method |
|-----------------|----------|----------------|-------------------|-----------------|
| SOP-COPS-011 Overview | All customer-facing staff | Within 30 days of hire or SOP effective date | Annual | LMS e-Learning (30 min) |
| NPS Survey Design & Administration | Customer Insights Team, Product Managers requesting surveys | Prior to Qualtrics access provisioning | Bi-annual | Instructor-led workshop (4 hours) |
| Detractor Response & Inner Loop | All CSMs, Support Team Leads | Within first 2 weeks of role | Quarterly role-play exercises | Instructor-led with simulation (2 hours) |
| Feedback Taxonomy Coding | Customer Insights Team | Within 30 days of assignment | Annual calibration session | Virtual calibration session (2 hours) |
| Qualtrics Technical Administration | Customer Insights technical admin(s) | Prior to admin access grant | Per Qualtrics major release | Vendor-provided training + internal documentation |
| Executive Interpretation | C-Suite, VPs | Prior to first review cycle | Annual | Executive briefing by Customer Insights Manager (30 min) |

### 9.2 Training Completion Tracking

All training completions are recorded in the Meridian Learning Management System (Workday Learning). Completion reports are generated monthly by the Customer Operations Training Coordinator. Non-compliance (>30 days past due for initial training or >60 days past due for refresher) is escalated to the trainee's manager and HR Business Partner.

### 9.3 Training Effectiveness Assessment

Training effectiveness is assessed through:
- Post-training knowledge checks (minimum score 80% required; 2 retake attempts permitted before instructor intervention)
- Field audit of Detractor response quality: Monthly random sample of 10 Detractor cases audited by Customer Insights Manager for adherence to playbook
- Annual survey design calibration: Review of all surveys fielded in prior 12 months for compliance with design standards

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|--------|-------|--------------|
| SOP-COPS-008 | Customer Health Score and Churn Prediction | Input data source for Detractor risk scoring |
| SOP-COPS-014 | Customer Onboarding Program | Onboarding milestone triggers tNPS deployment |
| SOP-COPS-017 | Customer Support Case Management | Support case closure triggers CSAT/tNPS deployment |
| SOP-SEC-022 | Data Classification and Handling Standards | Governs survey response data classification |
| SOP-SEC-031 | Third-Party Vendor Security Assessment | Applies to survey platform vendors |
| SOP-PROD-034 | Customer Advisory Board Program | Promoter engagement feeds CAB nomination |
| SOP-CA-018 | Clinical Customer Experience Measurement | Delineates clinical outcomes from satisfaction measurement |
| SOP-CA-052 | Adverse Event Reporting and Escalation | Governs safety-signal response from feedback |
| SOP-HR-029 | Employee Disciplinary Procedures | Referenced for anti-gaming enforcement |
| SOP-MKT-019 | Customer Reference and Case Study Program | Promoter follow-up feeds reference pipeline |
| SOP-PLAT-045 | Analytics Data Governance | Governs Snowflake data modeling and access control standards |

### 10.2 External References

| Reference | Description |
|-----------|-------------|
| Qualtrics Platform Security Whitepaper (v2025.3) | Technical controls for survey data in transit and at rest |
| Gainsight Administration Guide (v6.12) | Customer health score configuration and Timeline standards |
| NICE Satmetrix NPS Benchmark Reports (Industry: Healthcare IT, 2025) | External benchmarking reference for target-setting |
| SOC 2 Trust Services Criteria (CC2.2, CC2.3) | Control activities related to customer feedback as management review input |

---

## 11. Revision History

| Version | Date | Author | Change Description | Approved By |
|---------|------|--------|-------------------|-------------|
| 1.0 | 2019-03-15 | Sarah Chen, Customer Insights Manager | Initial document creation; established foundational NPS program | Michael Chang |
| 2.3 | 2020-06-22 | Michael Chang, VP Customer Operations | Major revision: Added inner loop/outer loop framework, Detractor response SLAs, feedback taxonomy introduction | Michael Chang |
| 3.1 | 2021-09-14 | David Okonkwo, Customer Insights Manager | Incorporated Qualtrics platform migration from SurveyMonkey; added Section 6 Controls; updated roles post-reorganization | Robert Liu |
| 4.4 | 2023-01-31 | David Okonkwo, Customer Insights Manager | Added HealthPay product line to scope after 2022 acquisition integration; updated training requirements for expanded CSM team; introduced CES metric | Robert Liu |
| 5.0 | 2024-05-15 | Priya Patel, Director of Customer Insights | Comprehensive rewrite: introduced Snowflake data integration; added gainsight PX triggers and feedback taxonomy automation; expanded from 9 to 12 sections; aligned with 2024 organizational structure | Michael Chang |
| 5.5 | 2025-03-20 | Priya Patel, Director of Customer Insights | Minor revision: updated Detractor SLA from 48hrs to 24hrs; added CE marking survey implications for EU customers; refined segment definitions per executive request | Michael Chang |
| 5.8 | 2025-11-10 | Priya Patel, Director of Customer Insights | Current version: revised Section 5.2 audience exclusion rules for active support cases; updated Gainsight integration specifications for v6.12; added Section 9 training effectiveness assessment; updated referenced SOPs to current versions | Robert Liu |