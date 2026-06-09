---
sop_id: "SOP-PENG-008"
title: "Technical Debt Management"
business_unit: "Product & Engineering"
version: "3.0"
effective_date: "2024-09-22"
last_reviewed: "2025-05-10"
next_review: "2025-11-27"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Technical Debt Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for identifying, documenting, prioritizing, tracking, and remediating technical debt across all Meridian Health Technologies, Inc. product lines and supporting infrastructure. Technical debt, when left unmanaged, poses material risk to system availability, security posture, development velocity, regulatory compliance, and the company's ability to deliver safe and reliable healthcare technology solutions. This SOP defines a consistent, measurable, and governance-driven approach to ensure that technical debt is treated as a first-class engineering concern with appropriate resourcing, executive visibility, and accountability.

### 1.2 Scope

This SOP applies to all software, infrastructure, data pipelines, machine learning models, and platform components developed or operated by Meridian Health Technologies, Inc., including:

| Scope Area | Coverage |
|------------|----------|
| **Clinical AI Platform** | Decision support tools, diagnostic imaging analysis, patient risk scoring, adverse event prediction systems deployed in 340+ hospitals and clinics |
| **HealthPay Financial Services** | Payment processing, patient financing, medical lending, claims automation systems processing ~$4.2B annually |
| **MedInsight Analytics** | Population health analytics, care gap identification, outcomes prediction platform handling PHI from ~12M patients |
| **Meridian SaaS Platform** | Multi-tenant cloud infrastructure on AWS us-east-1 and eu-west-1, including all supporting services, APIs, and data stores |
| **Internal Tools & Infrastructure** | CI/CD pipelines, monitoring systems, developer tooling, corporate IT systems supporting engineering functions |
| **Machine Learning Operations** | Model training pipelines, feature stores, model serving infrastructure, experiment tracking systems |
| **Third-Party Integrations** | Vendor APIs, SDK dependencies, open-source libraries, commercial software components integrated into Meridian products |

### 1.3 Applicability

This SOP is binding upon all full-time employees, contractors, consultants, and third-party vendors who contribute to, maintain, or operate software systems within the Product & Engineering business unit. Compliance with this SOP is a condition of system access and deployment authorization.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|------|------------|
| **Technical Debt** | The implied cost of future rework caused by choosing an expedient solution today over a more robust, sustainable approach. Technical debt encompasses code quality issues, architectural compromises, outdated dependencies, inadequate testing, documentation gaps, and operational toil resulting from suboptimal design decisions. |
| **Principal** | The foundational, correct implementation that would fully resolve the debt item. Represents the ideal end-state. |
| **Interest** | The ongoing cost incurred by carrying technical debt — including increased defect rates, slower feature delivery, heightened security risk, additional operational burden, and cognitive load on engineering teams. |
| **Debt Item** | A single, atomically-tracked unit of technical debt registered in the Technical Debt Register (TDR). |
| **Debt Category** | A classification dimension used to characterize the nature of the debt (see Section 5.2.1). |
| **Debt Severity** | A measure of the potential impact if the debt remains unresolved (see Section 5.2.2). |
| **Remediation Backlog** | The prioritized queue of debt items approved for active remediation within a given planning cycle. |
| **Debt Remediation Ratio** | The proportion of engineering capacity allocated to technical debt remediation versus feature development, expressed as a percentage. Target minimum: 20%. |
| **Carrying Cost** | Quantified metric representing the cumulative operational impact of a debt item, including incident frequency, manual intervention hours, and defect correlation. |
| **Amortization Schedule** | Time-bound plan for incrementally resolving a large debt item through a series of smaller, sequenced remediation tasks. |
| **Debt Ceiling** | Maximum allowable aggregate technical debt score (ATDS) for a given system or team before remediation is mandated ahead of new feature work. |

### 2.2 Acronyms

| Acronym | Expansion |
|---------|-----------|
| ATDS | Aggregate Technical Debt Score |
| CI/CD | Continuous Integration / Continuous Deployment |
| CVE | Common Vulnerabilities and Exposures |
| EOL | End of Life |
| IVR | Issue Velocity Ratio |
| ML | Machine Learning |
| MTTR | Mean Time to Resolve |
| SLA | Service Level Agreement |
| SLO | Service Level Objective |
| SME | Subject Matter Expert |
| TDB | Technical Debt Backlog |
| TDR | Technical Debt Register |
| TDS | Technical Debt Score |
| VP | Vice President |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

| Role | Responsible | Accountable | Consulted | Informed |
|------|:-----------:|:-----------:|:---------:|:--------:|
| **Engineering Team Lead** | R | A | C | I |
| **Staff/Principal Engineer** | R | R | C | I |
| **Product Manager** | C | A | R | I |
| **VP of Engineering (David Park)** | I | A | C | R |
| **VP of Clinical AI Products (Dr. Aisha Okafor)** | I | A | C | R |
| **VP of Financial Services (Robert Liu)** | I | A | C | R |
| **Chief AI Officer (Dr. Marcus Rivera)** | I | A | C | R |
| **Chief Information Security Officer (Rachel Kim)** | C | C | R | I |
| **Chief Compliance Officer (Thomas Anderson)** | I | I | C | R |
| **VP of IT Operations (Samantha Torres)** | C | A | R | I |
| **Engineering Manager** | A | A | C | I |
| **Individual Contributor Engineer** | R | I | I | I |

### 3.2 Role Descriptions

#### 3.2.1 VP of Engineering (David Park)
- Serves as the organizational owner of this SOP
- Approves the annual technical debt remediation budget and capacity allocation
- Reviews and approves exceptions to the Debt Remediation Ratio (Section 6.4)
- Presents quarterly technical debt posture to the AI Governance Committee
- Authorizes major architectural remediation initiatives exceeding 2 sprint equivalents of effort

#### 3.2.2 Engineering Team Lead
- Maintains the team's Technical Debt Register
- Conducts monthly debt triage sessions with the engineering team
- Ensures debt items are documented with sufficient detail for prioritization
- Reports team ATDS and remediation progress to Engineering Manager
- Validates that at least 20% of sprint capacity is allocated to debt remediation

#### 3.2.3 Staff / Principal Engineer
- Performs architectural impact assessment for debt items affecting system design
- Proposes amortization schedules for complex, cross-cutting debt items
- Reviews and approves debt item categorization and severity scoring
- Leads quarterly system-level technical debt reviews
- Provides technical oversight for remediation implementation

#### 3.2.4 Product Manager
- Incorporates prioritized debt items into the product roadmap
- Balances feature requests against debt remediation within sprint planning
- Communicates debt-driven timeline impacts to stakeholders
- Approves acceptance criteria for debt remediation completion

#### 3.2.5 Chief Information Security Officer (Rachel Kim)
- Provides security impact assessment for debt items with security implications
- Maintains the vulnerability-to-debt mapping for CVEs affecting Meridian systems
- Escalates security-critical debt items to the VP of Engineering for immediate remediation

#### 3.2.6 Individual Contributor Engineer
- Identifies and documents technical debt encountered during development activities
- Provides effort estimates for remediation tasks
- Implements approved remediation work according to defined acceptance criteria
- Updates debt item status in the TDR upon completion of remediation tasks

---

## 4. Policy Statements

### 4.1 Commitment to Sustainable Engineering

Meridian Health Technologies, Inc. recognizes that unmanaged technical debt poses systemic risk to the reliability, security, and maintainability of healthcare-critical systems. The company commits to treating technical debt as a core engineering metric, subject to the same governance rigor as feature delivery, system availability, and security posture.

### 4.2 Minimum Remediation Allocation

All engineering teams shall allocate a minimum of **20% of total sprint capacity** to technical debt remediation. This allocation is measured as a rolling average over each calendar quarter. Teams falling below the 20% threshold for two consecutive quarters shall submit a remediation catch-up plan to the VP of Engineering for approval.

### 4.3 Debt Registration Requirement

Any technical debt item expected to require more than **4 hours of remediation effort** must be registered in the Technical Debt Register (TDR) within **5 business days** of identification. Debt items representing security vulnerabilities graded **Critical** or **High** per Meridian's vulnerability classification must be registered within **24 hours**.

### 4.4 No Net New Critical Debt

No new feature, service, or system component shall be deployed to production if it introduces technical debt classified as **Critical severity** (see Section 5.2.2) without an explicit, time-bound exception approved by the VP of Engineering. Exceptions must include a committed remediation date not exceeding **60 calendar days** from deployment.

### 4.5 Debt in Definition of Done

Resolution of identified technical debt items assigned to a given work item is a mandatory component of the team's Definition of Done. Work items introducing new debt must document such debt in the TDR before the work item is marked complete.

### 4.6 Annual System Health Assessment

All production systems shall undergo an annual technical debt health assessment conducted by the responsible engineering team, with results reported to the VP of Engineering and the Chief AI Officer. Systems exceeding the defined ATDS threshold (see Section 7.2) shall be subject to a mandatory remediation program.

### 4.7 Dependency Currency

All third-party dependencies (open-source libraries, commercial SDKs, vendor APIs) shall be maintained within **one major version** of the latest stable release for Critical and High-impact dependencies, and within two major versions for Medium-impact dependencies. Exceptions require approval from the VP of Engineering and CISO.

---

## 5. Detailed Procedures

### 5.1 Technical Debt Identification

#### 5.1.1 Identification Sources

Technical debt shall be identified through the following channels:

| Identification Source | Frequency | Responsible Party | Registration Method |
|----------------------|-----------|-------------------|---------------------|
| **Development Activity** | Continuous | Individual Contributor Engineers | Jira issue linked to TDR |
| **Code Review** | Per pull request | Reviewers, Staff Engineers | Pull request comments escalated to TDR |
| **Architecture Review Board** | Monthly | Principal Engineers, VP of Engineering | Architecture debt report |
| **Incident Postmortem** | Per incident | Incident Commander, Team Lead | Postmortem action item → TDR |
| **Security Vulnerability Scan** | Weekly (automated) | CISO, DevSecOps | CrowdStrike/Jira integration → TDR |
| **Dependency Audit** | Monthly | Automated via Dependabot/Snyk | Auto-populated in TDR |
| **Performance Testing** | Per release cycle | QA, Site Reliability Engineering | Performance regression report → TDR |
| **Accessibility Audit** | Quarterly | UX Engineering | Audit findings → TDR |
| **Model Drift Monitoring** | Continuous | ML Engineering | LangSmith/Kubeflow alerts → TDR |
| **Operational Toil Tracking** | Weekly | SRE, IT Operations | Datadog incident correlation → TDR |

#### 5.1.2 Debt Identification Template

Each debt item registered in the TDR shall include the following minimum information:

```
TECHNICAL DEBT ITEM — REGISTRATION TEMPLATE

TDR-ID: [Auto-generated: TDR-{YYYY}-{####}]
Date Identified: [YYYY-MM-DD]
Identified By: [Name, Role]
System/Component: [Affected service, repository, or infrastructure component]
Debt Category: [See Section 5.2.1]
Severity: [Critical / High / Medium / Low — See Section 5.2.2]
Estimated Remediation Effort: [Story points or person-hours]
Affected SLAs/SLOs: [List any service level objectives impacted]
Regulatory Implications: [EU AI Act, HIPAA, SR 11-7, GDPR — if applicable]
CVE References: [If security-related]
Principal Definition: [Description of the correct, sustainable implementation]
Interest Manifestation: [How this debt currently creates cost/risk]
Remediation Recommendation: [Proposed approach to resolution]
Known Workarounds: [Any interim mitigations in place]
Business Impact Assessment: [Impact on users, customers, revenue, compliance]
```

#### 5.1.3 Automated Debt Detection

The following automated tooling shall be configured to identify and register debt items:

| Tool | Detection Type | Integration Point |
|------|---------------|-------------------|
| **SonarQube** | Code quality, code smells, duplication | CI/CD pipeline — Jenkins/GitHub Actions |
| **Snyk** | Open-source vulnerability scanning | Dependency resolution at build time |
| **Dependabot** | Outdated dependency alerts | GitHub repository scanning |
| **Datadog APM** | Performance degradation, increased latency | Production monitoring, weekly trend analysis |
| **LangSmith** | ML model performance drift, data quality degradation | AI tracing pipeline |
| **AWS Trusted Advisor** | Infrastructure right-sizing, idle resources | Weekly infrastructure audit |
| **Checkov / tfsec** | Infrastructure-as-code misconfigurations | Pre-commit hooks and CI/CD pipeline |

### 5.2 Debt Classification and Prioritization

#### 5.2.1 Debt Categories

All debt items shall be classified into one or more of the following categories:

| Category | Code | Description | Examples |
|----------|------|-------------|----------|
| **Architectural** | ARCH | Structural deficiencies in system design that limit scalability, maintainability, or extensibility | Monolithic service requiring decomposition; tight coupling between Clinical AI and HealthPay modules |
| **Code Quality** | CODE | Implementation-level issues including complexity, duplication, inconsistent patterns, poor readability | Methods exceeding cyclomatic complexity threshold of 15; code duplication exceeding 5% across modules |
| **Testing** | TEST | Inadequate test coverage, missing test types, flaky tests, or untestable code | Unit test coverage below 80% threshold; absence of integration tests for payment processing pipeline |
| **Security** | SEC | Vulnerabilities, weak configurations, outdated cryptographic practices, or missing security controls | Unpatched CVEs with CVSS ≥ 7.0; hardcoded credentials; missing encryption at rest for PHI data stores |
| **Dependency** | DEP | Outdated, unmaintained, or end-of-life third-party components | Python 3.8 EOL dependency; deprecated AWS SDK versions; unmaintained NPM packages |
| **Documentation** | DOC | Missing, outdated, or inadequate system documentation, runbooks, or API specifications | Undocumented API endpoints; missing incident response runbooks for new services |
| **Operational** | OPS | Manual processes, deployment friction, observability gaps, or configuration drift | Manual database migration steps; lack of synthetic monitoring for critical user journeys |
| **Data** | DATA | Data quality issues, schema deficiencies, inconsistent data models, or inadequate data governance | PHI fields lacking data classification tags; inconsistent patient identifier formats across MedInsight and Clinical AI |
| **ML/AI Specific** | MLAI | Model-related debt including training data quality, feature engineering fragility, model explainability gaps, or concept drift | Undocumented feature transformations; bias in training data not assessed; model cards not published per EU AI Act requirements |

#### 5.2.2 Severity Classification

| Severity | Score | Definition | Remediation SLA (from identification) |
|----------|-------|------------|---------------------------------------|
| **Critical** | 4 | Debt that poses immediate risk to patient safety, system availability, data security, or regulatory compliance. Includes active exploits, data loss scenarios, or EU AI Act non-compliance for high-risk AI systems. | Remediation plan: 48 hours; Resolution: 30 calendar days |
| **High** | 3 | Debt that significantly degrades system reliability, creates material security exposure without active exploit, or blocks critical feature delivery. Includes debt likely to become Critical within 90 days. | Remediation plan: 5 business days; Resolution: 90 calendar days |
| **Medium** | 2 | Debt that measurably impacts developer productivity, increases operational toil, or represents a departure from best practices that will compound over time. | Resolution: within 2 planning cycles (approximately 6 months) |
| **Low** | 1 | Minor code quality issues, documentation gaps, or improvement opportunities that do not materially impact system operation or team velocity. | Resolution: addressed opportunistically within normal development activity |

#### 5.2.3 Prioritization Formula

The Technical Debt Score (TDS) for each item is calculated as:

```
TDS = (Severity Score × 3) + (Carrying Cost Factor × 2) + (Proximity Factor × 2) + (Scope Factor × 1)
```

Where:

| Factor | Weight | Scale |
|--------|--------|-------|
| **Severity Score** | ×3 | 1 (Low) to 4 (Critical) |
| **Carrying Cost Factor** | ×2 | 1 (Minimal impact) to 5 (Active business disruption) |
| **Proximity Factor** | ×2 | 1 (Distant future risk) to 5 (Degrading within current cycle) |
| **Scope Factor** | ×1 | 1 (Single component) to 5 (Cross-cutting across multiple systems) |

Maximum TDS = (4×3) + (5×2) + (5×2) + (5×1) = 12 + 10 + 10 + 5 = 37

#### 5.2.4 Triage Cadence

| Activity | Frequency | Participants | Output |
|----------|-----------|--------------|--------|
| **Team Debt Triage** | Weekly (Sprint Planning) | Engineering Team Lead, Product Manager, Team Engineers | Updated TDR with new items triaged; remediation tasks assigned to sprint |
| **Cross-Team Debt Review** | Monthly | Engineering Managers, Staff Engineers, Product Managers | Identification of cross-cutting debt; dependency coordination |
| **System-Level Architecture Debt Review** | Quarterly | Principal Engineers, VP of Engineering, relevant Team Leads | Architecture debt report; major remediation initiative proposals |
| **Executive Debt Posture Review** | Quarterly | VP of Engineering, CISO, Chief AI Officer, CTO | ATDS dashboard review; remediation budget allocation; exception approvals |

### 5.3 Tracking and Tooling

#### 5.3.1 Technical Debt Register (TDR)

The single source of truth for all technical debt items is the Technical Debt Register, implemented as a Jira project with custom fields mapping to the debt item template (Section 5.1.2). The TDR shall be configured with:

| Configuration Element | Implementation |
|----------------------|----------------|
| **Platform** | Jira Software (Cloud) — Project Key: TDR |
| **Issue Types** | Debt Item, Amortization Epic, Remediation Task |
| **Custom Fields** | Debt Category, Severity, TDS, Regulatory Impact, Affected System, Estimated Effort, Carrying Cost Factor |
| **Workflow States** | Identified → Triaged → Prioritized → In Remediation → Verification → Resolved → Closed |
| **Automation Rules** | Auto-assignment based on affected system; SLA breach notifications; weekly status digest |
| **Integration** | Datadog (incident → debt linkage); Snyk (CVE → debt item creation); GitHub (PR → debt resolution) |

#### 5.3.2 Jira Workflow Definition

```
[Identified] ──→ [Triaged] ──→ [Prioritized] ──→ [In Remediation] ──→ [Verification] ──→ [Resolved] ──→ [Closed]
       │               │              │                   │                  │                │
       └─── Rejected (with rationale documented)          │                  │                │
                                                          └─── Blocked       └─── Failed       └─── Reopened
```

| Transition | Required Approval | Required Fields |
|------------|------------------|-----------------|
| Identified → Triaged | Engineering Team Lead | Category, Severity, Estimated Effort |
| Triaged → Prioritized | Product Manager + Team Lead | TDS, Target Remediation Cycle |
| Prioritized → In Remediation | None (sprint commitment) | Assigned Engineer, Acceptance Criteria |
| In Remediation → Verification | Peer Reviewer | Pull Request link, Test Evidence |
| Verification → Resolved | Engineering Team Lead | Verification Results, Principal Achieved (Y/N) |
| Resolved → Closed | Automated (30-day waiting period) | No regression incidents |

#### 5.3.3 Dashboard Configuration

Real-time technical debt dashboards shall be maintained in Datadog and Jira Dashboards, displaying:

- Aggregate Technical Debt Score (ATDS) per team and per system
- Debt Remediation Ratio trend (current sprint, rolling quarter)
- Age distribution of unresolved debt items (0–30 days, 31–90 days, 91–180 days, >180 days)
- Critical and High severity debt count and aging
- Dependency currency status across all repositories
- Carrying cost trend correlated with incident data
- SLA compliance rate for debt remediation timelines

### 5.4 Remediation Planning

#### 5.4.1 Sprint Capacity Allocation

Engineering teams shall allocate capacity as follows during sprint planning:

| Allocation Category | Minimum | Maximum | Notes |
|--------------------|---------|---------|-------|
| **Technical Debt Remediation** | 20% | 50% | Mandatory minimum; may increase based on ATDS thresholds |
| **Feature Development** | 40% | 70% | New capabilities, enhancements |
| **Unplanned Work / Sustainment** | 10% | 25% | Production issues, critical patches, emergent work |

If the team ATDS exceeds the Warning Threshold (see Section 7.2), the debt allocation minimum increases to **30%** until the score returns below threshold.

#### 5.4.2 Amortization Scheduling

For debt items estimated to exceed **20 story points** or **80 person-hours** of remediation effort, an Amortization Schedule shall be created. The schedule shall:

1. Decompose the debt item into discrete, value-delivering remediation increments
2. Sequence increments to deliver measurable risk reduction at each step
3. Define intermediate acceptance criteria for each increment
4. Establish a target completion date not exceeding **2 planning cycles** for High severity items
5. Identify any interim compensating controls required during the amortization period

Amortization Schedules shall be tracked as Jira Epics (issue type: Amortization Epic) containing child Remediation Tasks linked to the parent Debt Item.

#### 5.4.3 Remediation Strategies

Teams shall select the appropriate remediation strategy based on debt characteristics:

| Strategy | Description | Applicable Scenarios |
|----------|-------------|---------------------|
| **Full Refactor** | Complete replacement of the debt-laden implementation with the principal | Architectural debt, security-critical systems, regulatory non-compliance |
| **Incremental Improvement** | Series of smaller changes applied over multiple sprints | Large-scale code quality issues, test coverage gaps |
| **Strangler Pattern** | Gradual replacement by building new functionality around the old, eventually replacing it entirely | Legacy service decomposition, platform migrations |
| **Containment** | Isolating the debt behind a clean interface to prevent propagation, with remediation deferred | Low-severity debt in stable, rarely-modified components |
| **Retirement** | Decommissioning the affected system or feature entirely | Deprecated features, redundant systems, EOL components |

#### 5.4.4 Verification and Validation

All remediated debt items shall undergo verification before being marked as Resolved:

| Verification Method | Required For | Performed By |
|--------------------|--------------|--------------|
| **Code Review** | All remediations | Peer Engineer (not the implementer) |
| **Automated Test Execution** | All code-level remediations | CI/CD Pipeline |
| **Regression Test Suite** | Architectural changes, High/Critical debt | QA Engineer |
| **Security Review** | Security debt items, dependency updates | DevSecOps / CISO representative |
| **Performance Benchmark** | Performance-related debt, infrastructure changes | SRE Engineer |
| **Architecture Review** | Architectural debt items | Staff/Principal Engineer |
| **Model Validation** | ML/AI model debt items | ML Engineering Lead |

---

## 6. Controls and Safeguards

### 6.1 Access Controls for Technical Debt Register

Access to the TDR shall be governed by the following role-based permissions:

| Role | Create | Edit | Delete | View All | Admin |
|------|:------:|:----:|:------:|:--------:|:-----:|
| Individual Contributor Engineer | ✓ | Own items | — | Team scope | — |
| Engineering Team Lead | ✓ | Team scope | Team scope | Team scope | — |
| Staff/Principal Engineer | ✓ | All | All | All | — |
| Engineering Manager | ✓ | All | — | All | — |
| Product Manager | ✓ | Team scope | — | Team scope | — |
| VP of Engineering | ✓ | All | All | All | ✓ |
| CISO | — | Security items | — | Security items | — |

### 6.2 Debt Ceiling and Enforcement

| Control Mechanism | Threshold | Enforcement Action |
|------------------|-----------|-------------------|
| **Team Debt Ceiling** | ATDS exceeds 150% of baseline | 30% sprint capacity allocation to debt; feature freeze on non-critical enhancements |
| **System Debt Ceiling** | Critical/High items exceeding 90-day SLA | VP of Engineering escalation; mandatory remediation sprint |
| **Dependency Currency Gate** | Critical dependency >2 major versions behind | Deployment block until dependency updated or exception approved |
| **Security Debt Trigger** | Any Critical CVE unresolved >48 hours | Immediate CISO escalation; incident response protocol activation |

### 6.3 Compensating Controls

When immediate remediation is not feasible, compensating controls shall be documented and implemented:

| Debt Type | Compensating Control Examples |
|-----------|------------------------------|
| **Security Vulnerability** | WAF rules, network segmentation, IP allowlisting, increased monitoring frequency |
| **Performance Degradation** | Rate limiting, increased auto-scaling thresholds, traffic shedding for non-critical paths |
| **Data Quality Issue** | Data validation middleware, automated anomaly detection, manual QA checkpoint |
| **Operational Toil** | Temporary runbooks, increased on-call tier support, automated alert suppression for known false positives |
| **Model Drift** | Shadow model deployment, automated retraining triggers, human-in-the-loop review for edge cases |

Compensating controls shall be documented in the debt item and reviewed monthly. Controls shall have defined expiration dates.

### 6.4 Exception Process

Exceptions to any policy statement in this SOP shall follow this process:

1. **Exception Request**: Submitted via Jira (TDR project, issue type: Exception) with:
   - Policy section for which exception is requested
   - Business justification
   - Risk assessment
   - Proposed compensating controls
   - Duration of exception (maximum 90 days)

2. **Review**: Reviewed by Engineering Manager and affected VP within 5 business days

3. **Approval**: Approved by VP of Engineering; CISO co-approval required for security exceptions; Chief AI Officer co-approval for Clinical AI exceptions

4. **Registration**: All active exceptions tracked in the Exception Register with monthly review

5. **Expiration**: Exceptions expire automatically; renewal requires new request with justification for extension

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators

| KPI | Definition | Target | Measurement Frequency |
|-----|-----------|--------|----------------------|
| **Debt Remediation Ratio (DRR)** | (Story points completed for debt remediation / Total story points completed) × 100 | ≥ 20% per quarter | Weekly, aggregated quarterly |
| **ATDS Trend** | Month-over-month change in Aggregate Technical Debt Score | Decreasing or stable (±5%) | Monthly |
| **Critical Debt Aging** | Average age of unresolved Critical severity items | ≤ 15 days | Weekly |
| **High Debt Aging** | Average age of unresolved High severity items | ≤ 45 days | Weekly |
| **SLA Compliance** | Percentage of debt items resolved within severity-defined SLA | ≥ 90% | Monthly |
| **Debt Backlog Growth Rate** | (New debt items registered − Debt items resolved) / Total open debt items | ≤ 5% net growth per month | Monthly |
| **Dependency Currency Score** | Percentage of dependencies within version thresholds | ≥ 85% | Monthly (automated) |
| **Debt-Driven Incidents** | Percentage of production incidents with root cause linked to a known debt item | ≤ 15% | Monthly |
| **Carrying Cost Index** | Aggregated operational hours spent on debt-related manual work | Declining quarter-over-quarter | Quarterly |

### 7.2 Aggregate Technical Debt Score (ATDS) Thresholds

| Threshold Level | Value Range | Required Action |
|-----------------|-------------|-----------------|
| **Healthy** | ≤ 100% of baseline ATDS | Standard 20% debt allocation |
| **Warning** | 101%–150% of baseline ATDS | Increase debt allocation to 30%; report to Engineering Manager |
| **Critical** | >150% of baseline ATDS | Feature freeze consideration; mandatory remediation plan submitted to VP of Engineering within 10 business days |

Baseline ATDS is established during the annual system health assessment and represents the aggregate TDS for all open debt items normalized against system complexity and team size.

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Medium | Owner |
|--------|----------|-----------|--------|-------|
| **Team Debt Dashboard** | Engineering Team, Product Manager | Real-time (continuous) | Jira Dashboard / Datadog | Engineering Team Lead |
| **Monthly Debt Report** | Engineering Managers, VP of Engineering | Monthly | Email digest + Confluence | Engineering Managers |
| **Quarterly Engineering Health Review** | VP of Engineering, Chief AI Officer, CISO, CEO | Quarterly | Slide deck + live review | VP of Engineering |
| **Annual System Health Assessment** | AI Governance Committee, Board | Annually | Formal report | VP of Engineering + Principal Engineers |
| **Regulatory Audit Support** | External Auditors (SOC 2, HITRUST, ISO 27001) | As required per audit cycle | Evidence package from TDR | Chief Compliance Officer |

### 7.4 Automated Alerts

| Alert | Trigger Condition | Notification Channel | Recipients |
|-------|------------------|---------------------|------------|
| **Critical Debt SLA Breach** | Critical debt item unresolved >48 hours | PagerDuty (High Urgency) | Engineering Team Lead, VP of Engineering, CISO |
| **High Debt SLA Warning** | High debt item approaching SLA deadline (within 7 days) | Slack (#eng-debt-alerts) | Engineering Team Lead, Product Manager |
| **Team DRR Below Threshold** | Rolling quarter DRR < 20% | Email + Slack | Engineering Manager, VP of Engineering |
| **ATDS Critical Threshold** | System ATDS > 150% baseline | PagerDuty (Medium Urgency) | VP of Engineering, System Team Lead |
| **Critical CVE Identified** | New CVE with CVSS ≥ 9.0 affecting deployed component | PagerDuty (Critical) | CISO, VP of Engineering, DevSecOps Lead |
| **Dependency EOL Warning** | Dependency approaching vendor EOL within 90 days | Slack (#eng-debt-alerts) | Affected team leads, Staff Engineers |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

| Exception Type | Description | Maximum Duration | Approval Authority |
|---------------|-------------|-----------------|-------------------|
| **Remediation Deferral** | Extending remediation SLA for non-Critical debt | 90 days | VP of Engineering |
| **Debt Introduction** | Deploying feature that creates Critical debt | 60 days (remediation committed) | VP of Engineering |
| **DRR Waiver** | Sprint/quarter operating below 20% DRR | 1 quarter | VP of Engineering + Chief AI Officer |
| **Dependency Exception** | Running dependency outside version policy | 180 days | VP of Engineering + CISO |
| **Debt Ceiling Override** | Continuing feature work while ATDS exceeds Critical threshold | 1 sprint (2 weeks) | VP of Engineering + CEO |

### 8.2 Escalation Path

```
Level 1: Engineering Team Lead
    ↓ (No resolution within 5 business days, or Critical severity)
Level 2: Engineering Manager + affected Product Manager
    ↓ (No resolution within 5 additional business days, or security involvement)
Level 3: VP of Engineering + CISO (if security) / Chief AI Officer (if AI)
    ↓ (No resolution, or material business risk)
Level 4: CEO (Dr. Sarah Chen) — final decision authority
```

### 8.3 Emergency Remediation Protocol

When a debt item is directly linked to a Severity 1 (Sev1) production incident:

1. The incident response process takes precedence (per SOP-INC-001 Incident Management)
2. During postmortem, the debt item is elevated to **Critical** severity regardless of prior classification
3. A remediation plan must be presented during the postmortem review
4. If no remediation plan is approved within **5 business days** of the incident, the VP of Engineering convenes an emergency architecture review
5. Feature development on the affected system may be paused at the discretion of the VP of Engineering

---

## 9. Training Requirements

### 9.1 Training Curriculum

| Training Module | Target Audience | Duration | Frequency |
|-----------------|----------------|----------|-----------|
| **SOP-PENG-008: Technical Debt Management Awareness** | All Product & Engineering personnel | 90 minutes | Initial (onboarding) + Annual refresher |
| **TDR Tooling and Workflow Training** | All Individual Contributor Engineers, Team Leads | 60 minutes | Initial + On tooling changes |
| **Debt Identification and Classification Workshop** | Engineering Team Leads, Staff Engineers | 120 minutes (interactive) | Initial + Biennial refresh |
| **Architectural Debt and System Design Review** | Staff Engineers, Principal Engineers | Half-day | Annual |
| **Technical Debt for Product Managers** | Product Managers, Product Directors | 90 minutes | Initial + Annual |

### 9.2 Training Tracking

Training completion shall be tracked in Meridian's Learning Management System (Workday Learning). Completion records shall include:

- Learner name and role
- Module completed
- Date of completion
- Assessment score (if applicable, passing threshold: 80%)

Compliance with training requirements shall be reviewed quarterly by Engineering Managers. Personnel who have not completed required training within **30 days** of assignment shall have their deployment privileges temporarily suspended until training is completed.

### 9.3 Onboarding Requirements

New engineering personnel shall complete the following within their first **10 business days**:

1. SOP-PENG-008 Technical Debt Management Awareness module
2. TDR Tooling and Workflow Training
3. Shadow at least one team debt triage session
4. Review their team's current debt backlog in the TDR

Completion shall be validated by the Engineering Team Lead and recorded in the new hire's onboarding checklist.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|--------|-------|-------------|
| SOP-PENG-001 | Software Development Lifecycle | Defines Definition of Done; debt identification during development |
| SOP-PENG-004 | Code Review Standards | Mandates code review debt flagging process |
| SOP-PENG-012 | Dependency Management Policy | Defines detailed dependency version policies and update procedures |
| SOP-INC-001 | Incident Management | Defines postmortem-driven debt identification |
| SOP-SEC-003 | Vulnerability Management | Defines CVE-to-debt registration workflow |
| SOP-ARCH-001 | Architecture Review Board Charter | Defines architectural debt governance |
| SOP-ML-005 | ML Model Lifecycle Management | Defines AI-specific debt categories and model drift procedures |
| SOP-QA-002 | Quality Gates and Release Readiness | Defines testing debt thresholds for production deployment |

### 10.2 External Standards and Frameworks

| Reference | Description | Applicable Sections |
|-----------|-------------|---------------------|
| ISO 25010:2011 | Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models | Maintainability, Reliability, Security characteristics |
| NIST SP 800-64 | Security Considerations in the SDLC | Security debt identification |
| OWASP Top 10:2021 | Web Application Security Risks | Security debt categorization |
| Technical Debt Quadrant (Martin Fowler) | Deliberate/Prudent × Reckless/Prudent classification framework | Debt categorization reference |
| IEEE Std 1061-1998 | Software Quality Metrics Methodology | TDS metric design reference |

### 10.3 Internal Tools Referenced

| Tool | Purpose | Owner |
|------|---------|-------|
| Jira Software Cloud (Project: TDR) | Technical Debt Register and Workflow | Product & Engineering |
| Confluence | Documentation and Runbooks | Product & Engineering |
| SonarQube (Enterprise Edition) | Static Code Analysis and Quality Gates | DevSecOps |
| Snyk | Open-Source Vulnerability Scanning | DevSecOps |
| Datadog APM + Logs | Observability and Performance Monitoring | SRE / IT Operations |
| PagerDuty | Incident Alerting and On-Call | IT Operations |
| LangSmith | AI Pipeline Monitoring and Drift Detection | ML Engineering |
| GitHub Advanced Security | Code Scanning and Secret Detection | DevSecOps |
| Workday Learning | Training Tracking | Human Resources |

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
|---------|------|--------|------------------------|
| 1.0 | 2021-03-15 | David Park | Initial publication. Established foundational debt management framework with annual debt reviews and basic categorization. |
| 2.0 | 2022-08-12 | David Park, with contributions from Staff Engineering group | Introduced TDS prioritization formula; added ML/AI-specific debt category; lowered minimum DRR from 15% to 20%; added dependency currency policy. |
| 2.5 | 2023-02-28 | Engineering Process Improvement Team | Added amortization scheduling procedures; expanded verification and validation section; added compensating controls framework. |
| 3.0 | 2024-09-22 | David Park, with review by Chief AI Officer and CISO | Major revision: added EU AI Act, SOC 2, and MDR regulatory alignment; introduced ML/AI debt category (MLAI); added model drift identification source; expanded roles to include AI governance; added emergency remediation protocol; updated all tooling references to current stack (LangSmith, Snyk, GitHub Advanced Security); increased minimum DRR to 20% with enforcement escalation. |
| 4.0 | 2025-11-24 | David Park | Current version. Comprehensive restructure for operational clarity: added detailed Jira workflow; expanded KPI definitions with MTTR targets for SLA compliance; introduced debt ceiling enforcement mechanism; added automated alert configuration table; revised exception handling to include duration limits and multi-party approval requirements; aligned training requirements with updated onboarding timeline. |

---

**Document Control:** This document is maintained in the Meridian Policy Repository (Confluence Space: ENG-POL). All changes to this SOP shall follow the Engineering Change Management process. Printed copies are uncontrolled. Verify version currency against the repository before use.

---

*Approved: Dr. Sarah Chen, CEO — 2025-11-24*