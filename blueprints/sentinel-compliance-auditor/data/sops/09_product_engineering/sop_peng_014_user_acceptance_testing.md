---
sop_id: "SOP-PENG-014"
title: "User Acceptance Testing"
business_unit: "Product & Engineering"
version: "2.7"
effective_date: "2025-10-07"
last_reviewed: "2026-03-27"
next_review: "2026-09-16"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: User Acceptance Testing

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the mandatory framework for conducting User Acceptance Testing (UAT) across all product lines at Meridian Health Technologies, Inc. UAT serves as the final empirical validation that a product release, feature, or enhancement meets the defined business requirements, satisfies end-user needs, and is fit for operational deployment within our regulated healthcare and financial services environment. This process is designed to provide reasonable assurance that changes introduced into production do not compromise data integrity, system availability, or patient safety outcomes.

### 1.2 Scope
This SOP applies to all software releases, including major, minor, and emergency hotfixes, across the following Meridian business units:

| Business Unit | Product Scope | UAT Requirement |
|---|---|---|
| Clinical AI Platform | Diagnostic imaging models, patient risk scoring algorithms, CDS hooks, adverse event predictors | Mandatory full UAT |
| HealthPay Financial Services | Payment processing, lending modules, claims automation, credit decisioning engines | Mandatory full UAT |
| MedInsight Analytics | Population health dashboards, care gap reports, outcomes prediction exports | Mandatory full UAT |
| Meridian SaaS Platform | Platform-level changes (authentication, tenancy, API gateway, core data services) | Mandatory full UAT |

This SOP applies to all employees, contractors, and third-party development partners involved in the software development lifecycle (SDLC). Exclusions are limited to infrastructure-as-code patches that do not alter application logic and pre-approved documentation-only updates.

### 1.3 Operational Context
Meridian operates in a multi-tenant cloud environment hosted primarily on AWS with Azure serving as disaster recovery infrastructure. All UAT activities must be conducted within the dedicated `meridian-uat` environment (AWS account `515234789012`, VPC `vpc-0a8b9c7d6e5f4a3b2`), which is architecturally isolated from production and development environments. UAT data sets must be synthetic, de-identified, or scrubbed of all Protected Health Information (PHI) unless a specific, logged, and approved data security waiver is obtained from the Chief Privacy Officer and CISO.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **UAT** | User Acceptance Testing — the formal process where end-users or their designated representatives validate a system against business requirements. |
| **BPO** | Business Process Owner — the operational stakeholder ultimately accountable for a business function within a product line. |
| **CDS** | Clinical Decision Support — AI-driven recommendations provided to clinicians. |
| **COAC** | Change Oversight and Approval Committee — the cross-functional governance body chaired by the CISO or delegate. |
| **CR** | Change Request — a formal request to modify any component of the production environment, initiated via Jira Service Management. |
| **DDL** | Defect Disposition Log — the centralized record of all findings during UAT, maintained within Jira. |
| **DevOps** | The consolidated Development and IT Operations function under the VP of IT Operations. |
| **DSR** | Data Security Review — the pre-UAT assessment to ensure the testing environment does not expose PHI/PII. |
| **EUC** | End-User Computing — applications developed outside formal IT, such as Excel macros or Access databases (governed under SOP-IT-029). |
| **Go/No-Go** | The formal authorization decision to proceed with or halt a production deployment. |
| **PDCA** | Plan-Do-Check-Act — the iterative management methodology for continuous improvement. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **PO** | Product Owner—Agile role representing the business stakeholder for a given product increment. |
| **SME** | Subject Matter Expert — a designated individual with specialized knowledge of the business domain. |
| **TSR** | Test Summary Report — the final artifact certifying UAT completion. |
| **VPAT** | Voluntary Product Accessibility Template — a document evaluating a product’s conformance with Section 508 accessibility standards (applicable to federal contracts). |

---

## 3. Roles and Responsibilities

The following matrix delineates the accountability model for all UAT activities. The framework follows RACI principles (Responsible, Accountable, Consulted, Informed).

| Role | Responsibility in UAT | RACI Designation |
|---|---|---|
| **VP of Engineering** | Overall process ownership; approves UAT strategy exceptions; escalates resource conflicts. | Accountable |
| **VP of Clinical AI Products** | Signs off on all clinical efficacy criteria for AI-driven products; reviews drift analysis reports. | Accountable (Clinical), Consulted |
| **VP of Financial Services** | Signs off on financial calculation accuracy; verifies compliance with SR 11-7 model documentation standards. | Accountable (Financial) |
| **Product Owner (PO)** | Defines acceptance criteria within user stories; assembles the UAT test suite in Zephyr Scale; serves as primary user proxy. | Responsible |
| **Business Process Owner (BPO)** | Nominated departmental representative who physically executes test scripts and attests to functional correctness. | Responsible |
| **QA Lead** | Facilitates UAT logistics; manages the DDL; runs the daily defect triage call; drafts the TSR. | Responsible |
| **DevOps Release Manager** | Deploys the build to the UAT environment; validates environment parity; confirms successful smoke test run before UAT start. | Responsible |
| **Chief Information Security Officer** | Consulted on any UAT data handling exceptions. | Consulted |
| **Chief Privacy Officer / DPO** | Approves any data security waivers for using production data in UAT. | Consulted |
| **Chief Compliance Officer** | Receives the final TSR for releases with regulatory impact. | Informed |
| **Customer Support Lead** | Informed of known issues shipped to production; assists in validating user-facing error messages. | Informed |

### 3.1 UAT Working Group
For every major release (version increment of X.Y.0), a temporary UAT Working Group shall be convened by the VP of Engineering. This group comprises the PO, BPO, QA Lead, Release Manager, and a designated SME from the affected business unit. The group disbands upon the submission of the final TSR.

---

## 4. Policy Statements

Meridian Health Technologies commits to the following high-level policies governing User Acceptance Testing:

**POL-014.1 — Entry Criteria:** No software build shall be deployed to the UAT environment unless it has successfully passed all automated integration tests, unit tests, and a QA-led functional verification cycle in the `staging` environment. The code must be frozen in a tagged release branch (`release/X.Y.Z`) within the Meridian GitHub Enterprise repository.

**POL-014.2 — Test Environment Data:** The UAT environment must not contain production PHI, live financial account numbers, or personally identifiable information (PII). All test data must be generated synthetically using the Tonic.ai platform or scrubbed via the Meridian Data Masking Utility (MDMU) v2.3+.

**POL-014.3 — Sign-Off Authority:** No product release shall proceed to production without documented, auditable sign-off from the designated Business Process Owner and the accountable VP. Electronic signatures must be captured within DocuSign and linked to the Jira release record.

**POL-014.4 — Accessibility:** All user-facing features must include at least one UAT scenario that validates basic screen reader compatibility (JAWS 2024+ or NVDA 2024+) and keyboard-only navigation.

**POL-014.5 — Clinical Safety:** For any Clinical AI Platform release affecting diagnostic recommendations, a licensed clinician (MD, DO, or equivalent) designated by the Chief Medical Officer must participate in UAT and attest to the absence of clinically significant regressions.

**POL-014.6 — Model Documentation:** For AI/ML model updates, the UAT must validate that the model’s outputs align with the documented intended use statement and that the transparency artifacts (model cards) are complete and accurate.

---

## 5. Detailed Procedures

### 5.1 Phase 0: UAT Preparation and Planning

#### 5.1.1 Initiation Trigger
UAT preparation commences as soon as the Product Owner moves the primary release epic in Jira to the `Ready for UAT` status. This action triggers an automated notification to the QA Lead and the Release Manager via Slack channel `#uat-coordination`.

#### 5.1.2 Test Plan Development
The Product Owner, in collaboration with the QA Lead, must draft a UAT Test Plan document. The plan must be completed and linked to the Jira release at least five (5) business days prior to the scheduled UAT start.

The UAT Test Plan must contain the following sections, recorded in Confluence within the `Product & Engineering > UAT` space:

1.  **Test Objectives:** A concise statement of what the release intends to achieve from a user perspective.
2.  **Scope and Out-of-Scope Items:** Clear delineation of features undergoing UAT and any associated functions explicitly excluded.
3.  **Business Process Owner Roster:** Named individuals responsible for test execution.
4.  **Test Schedule:** Daily cadence, including a mandatory daily defect triage meeting.
5.  **Test Scenarios and Scripts:** A traceability matrix linking each scenario back to a specific business requirement or user story. Scripts must use the Gherkin syntax (Given/When/Then) within Zephyr Scale.
6.  **Acceptance Criteria:** Quantifiable metrics for declaring success (e.g., "100% of Critical and High severity defects closed," "95% pass rate on core business flow scripts").
7.  **Data Requirements:** Specification of the synthetic data sets required, including volume and edge-case profiles.
8.  **Go/No-Go Decision Framework:** The explicit quorum and voting rules for the final release decision.

#### 5.1.3 Environment Provisioning
The DevOps Release Manager provisions or resets the `meridian-uat` environment. The environment configuration must mirror production in terms of database versions (PostgreSQL 16.x), Redis cache topology, Kafka broker configuration, and compute instance types. The Release Manager must execute a "smoke test" suite—a 45-minute automated script that validates all API endpoints return 200-level responses—and post the all-clear in `#uat-coordination`. This must occur at least 24 hours before BPOs are granted access.

### 5.2 Phase 1: UAT Execution

#### 5.2.1 Kick-Off Meeting
On the first day of UAT, the QA Lead conducts a mandatory 30-minute kick-off with all BPOs and SMEs. Agenda items include reviewing the test schedule, demonstrating the defect logging workflow in Jira, and confirming access credentials via Okta.

#### 5.2.2 Test Execution Protocol
BPOs execute test scripts serially within their assigned functional domain. The following rules govern execution:

- **Script Execution:** Each script step must be marked as `Pass`, `Fail`, or `Blocked` in Zephyr Scale in real-time. Screenshots must be attached for any `Fail` or `Blocked` designation.
- **Defect Logging:** When a test step fails, the BPO must immediately create a defect in Jira (Project: `UAT`, Issue Type: `Bug`). The defect must include the unique Test Script ID, the environment URL, exact steps to reproduce, expected outcome, actual outcome, and the attached screenshot.
- **Defect Severity Classification:** The BPO assigns a preliminary severity. The QA Lead re-validates and finalizes the severity during the daily triage.

| Severity | Classification Criteria | Target Remediation SLO |
|---|---|---|
| **Blocker** | Prevents execution of any further test scenarios in the functional area; system crash; data corruption; incorrect clinical score. | 4 hours |
| **Critical** | A core functional requirement is non-functional; no workaround exists; significant adverse financial or clinical impact. | 24 hours |
| **Major** | Feature fails to meet acceptance criteria but a reasonable business workaround exists. | 72 hours or must be assigned to a subsequent release |
| **Minor** | Cosmetic or layout issue; spelling error; unintended but non-impactful UX behavior. | Next release |
| **Enhancement** | A suggestion for future improvement, not a violation of current requirements. | Product Backlog |

#### 5.2.3 Daily Defect Triage
The QA Lead facilitates a mandatory 30-minute triage call at 2:00 PM Eastern Time each day. Attendees: QA Lead, PO, Release Manager, and the relevant Engineering Team Lead.

**Triage Agenda:**
1.  Review all new defects submitted in the past 24 hours.
2.  Confirm or re-assign severity for each defect.
3.  Assign the defect to a developer.
4.  Track Blocker and Critical defect aging.
5.  Update the Defect Disposition Log (DDL) in Confluence.

**Remediation Process:**
- Developer fixes the defect in the `hotfix/UAT-XYZ` branch.
- Code review by a peer or team lead is mandatory.
- A new build is promoted to UAT by the Release Manager.
- The fix is validated by the QA Lead (smoke test) and the reporting BPO (verification).

### 5.3 Phase 2: Clinical and Compliance Validation

This phase runs concurrently with Phase 1 for applicable products.

#### 5.3.1 Clinical AI Model Validation
For Clinical AI Platform releases, the Chief Medical Officer designates a Clinical SME (a board-certified physician). This SME must execute the "Clinical Validation Script Suite" (CVSS), a curated set of 50 de-identified historical cases designed to expose common failure modes like demographic bias, edge-case anatomy, and algorithmic drift. The SME must complete a Clinical Attestation Form (CAF-01, available in the Meridian QMS), which explicitly certifies whether they have observed any clinically significant performance degradation.

#### 5.3.2 Financial Controls Validation
For HealthPay Financial Services releases, the VP of Financial Services designates a Financial SME. This SME must execute the "Financial Accuracy Script Suite" (FASS), validating APR calculations, loan amortization schedules, late fee assessments, and journal entry mappings. The SME must sign the Financial Accuracy Sign-Off document (FIN-ATTEST-02).

### 5.4 Phase 3: Sign-Off and Deployment Approval

#### 5.4.1 Test Summary Report (TSR)
Within 24 hours of UAT completion, the QA Lead drafts the TSR. The TSR is a structured document embedded in Confluence, drawing live data from the Jira query.

**TSR Mandatory Content:**
- **Execution Summary:** Total scripts planned vs. executed; pass/fail/blocked percentages.
- **Defect Summary:** Total defects found, broken down by severity; total fixed and verified; total deferred.
- **Open Risk Register:** Any open Major or lower defects being accepted for the release, with a written risk acceptance justification from the BPO.
- **Deployment Recommendation:** A draft statement recommending "Go" or "No-Go."

#### 5.4.2 Formal Sign-Off
The TSR is routed via DocuSign in the following sequence:
1.  **Business Process Owner(s):** Acknowledges functional correctness.
2.  **VP of Clinical AI Products or VP of Financial Services:** Acknowledges domain-specific validation.
3.  **QA Lead:** Certifies the integrity of the testing process.
4.  **VP of Engineering:** Final approval and authorization to proceed to the Change Oversight and Approval Committee (COAC) for final release scheduling.

A release is declared "UAT Approved" only upon completion of all signatures. The final, signed TSR is archived in the `Meridian QMS Document Registry` as a mandatory record per SOP-QUAL-002.

---

## 6. Controls and Safeguards

The following controls are embedded within the UAT process to ensure integrity and auditability.

### 6.1 Access Control
- Access to the `meridian-uat` environment is governed by an Okta group (`uat-testers`). Membership in this group is temporary and automatically expires 72 hours after the linked Jira release is marked `Released`.
- Multi-factor Authentication (MFA) via Okta Verify is mandatory for all UAT users.

### 6.2 Change Management Integration
- No deployment to UAT occurs without a corresponding Jira release record.
- The DevOps CI/CD pipeline (GitHub Actions + ArgoCD) has a hard-coded guardrail that prevents deployment to the `production` account from any branch not merged to `main` and validated against the status of the UAT release record.

### 6.3 Audit Trail
- All Jira defects, status changes, and comments are immutable and timestamped.
- DocuSign completion certificates are stored with the TSR.
- Environment access logs from AWS CloudTrail and Okta are retained for 3 years.

### 6.4 Data Integrity
- An automated Data Security Review (DSR) scanner runs nightly in the UAT environment. It uses a regex-based PHI detection module (coupled with a Named Entity Recognition model) to flag potential data contamination. Any positive hit generates a P1 security incident in PagerDuty and suspends the UAT environment until cleared by the CISO.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
The VP of Engineering reports on UAT process health at the monthly Engineering Leadership review.

| KPI | Target | Data Source |
|---|---|---|
| **UAT Duration Variance** | Actual duration ≤ Planned duration ± 15% | Jira (Planned Start/End vs. Actual) |
| **Defect Escape Rate** | Critical defects reported in production within 30 days of release must be < 1 per quarter | PagerDuty Incidents tagged `post-release` |
| **Requirements Traceability** | 100% of UAT scripts must have a linked business requirement | Zephyr Scale → Jira Links |
| **Sign-Off Cycle Time** | Average time from TSR generation to final VP signature must be < 48 hours | DocuSign Envelope History |
| **UAT Participation Rate** | 95% of assigned BPOs must complete their assigned scripts | Zephyr Scale Assignment Matrix |

### 7.2 Dashboards
A real-time UAT Health Dashboard is maintained in Datadog, pulling data from the Jira API. The dashboard displays:
- Open defect count by severity.
- Blocked test script counter.
- "Time in UAT" clock for active releases.
- Per-BPO script execution progress bar.

A link to the live dashboard is pinned in the `#uat-coordination` Slack channel.

---

## 8. Exception Handling and Escalation

### 8.1 Scope Exceptions
Requests to waive UAT entirely for a release must be submitted in writing via Jira by the sponsoring VP to the COAC. Approved waivers are limited to emergency hotfixes where the risk of not deploying outweighs the risk of incomplete testing, and such hotfixes are still subject to a condensed, 4-hour SME validation window before production deployment.

### 8.2 Data Waivers
In the exceedingly rare event that synthetic data does not adequately represent a complex production anomaly, the BPO may request a waiver to test with a masked subset of production data. This requires the joint approval of the Chief Privacy Officer and the CISO and must be executed within the `meridian-pci` isolated VPC, not the standard UAT environment. A full post-test data destruction certificate must be generated.

### 8.3 Sign-Off Deadlock
If a BPO withholds sign-off, the matter is escalated first to the PO for mediation. If unresolved within 24 hours, it escalates to the VP of Engineering and the relevant domain VP (Clinical AI or Financial Services). The CEO is the final authority for any irrevocable deadlock regarding release safety or compliance posture.

---

## 9. Training Requirements

### 9.1 Initial Training
All employees and contractors designated as BPOs or UAT SMEs must complete training course **TRN-UAT-101: Principles of User Acceptance Testing at Meridian** prior to being granted access to the UAT environment. This course is hosted in Workday Learning. The curriculum covers:
- Meridian’s SDLC and where UAT fits.
- How to write and execute Gherkin test scripts in Zephyr Scale.
- Defect logging standards and severity definitions.
- Data privacy obligations and the prohibition on PHI in UAT.

### 9.2 Refresher Training
Refresher training is required annually, typically within 30 days of the employee's hire date anniversary. The QA Lead for each business unit is responsible for tracking compliance and reporting training gaps to the VP of Engineering during the monthly metrics review.

### 9.3 Role-Specific Training
- **Clinical BPOs:** Must additionally complete **TRN-CLN-205: Clinical AI Validation Standards**, covering bias inspection and drift interpretation.
- **Financial BPOs:** Must additionally complete **TRN-FIN-301: Financial Controls Testing**, covering audit standards and the Meridian lending calculation engine.

---

## 10. Related Policies and References

This SOP operates within a larger governance ecosystem. The following documents are binding:

| Reference ID | Document Title |
|---|---|
| SOP-SDLC-001 | Meridian Secure Software Development Lifecycle |
| SOP-QUAL-002 | Quality Management System and Document Control |
| SOP-CM-003 | Change Management and Release Governance |
| SOP-INFO-005 | Protection of PHI in Non-Production Environments |
| SOP-IT-029 | Governance of End-User Computing Applications |
| SOP-AI-041 | AI Model Risk Management and Validation |
| FRM-CLN-01 | Clinical Attestation Form (CAF-01) Template |
| FRM-FIN-02 | Financial Accuracy Sign-Off (FIN-ATTEST-02) Template |
| NIST AI RMF 1.0 | NIST Artificial Intelligence Risk Management Framework |
| EU AI Act | Regulation (EU) 2024/1689 |

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 1.0 | 2019-03-15 | J. Park (QA Manager) | Initial document creation. UAT defined for HealthPay MVP. |
| 1.5 | 2020-08-22 | J. Park | Added clinical data handling section post-ClinicAI pilot. |
| 2.0 | 2022-02-10 | A. Vance (Sr. QA Lead) | Major rewrite to align with SOC 2 Type II and ISO 27001 audit findings. Introduced formal RACI matrix and TSR template. |
| 2.4 | 2023-11-01 | A. Vance | Integrated EU AI Act readiness for Clinical AI; added Clinical SME sign-off; added accessibility testing mandate. |
| 2.5 | 2024-06-18 | D. Park (VP of Eng) | Updated severity classification SLAs; integrated Datadog dashboard requirement; moved data masking to Tonic.ai. |
| 2.6 | 2025-03-05 | L. Chen (Acting QA Lead) | Clarified cloud environment IDs; added MFA mandate for UAT access; updated training codes to new Workday catalog. |
| 2.7 | 2025-10-07 | D. Park (VP of Eng) | Incorporated financial model validation attestation for SR 11-7 alignment; refined exception delegation limits for Data Waivers; adjusted defect severity SLOs. |