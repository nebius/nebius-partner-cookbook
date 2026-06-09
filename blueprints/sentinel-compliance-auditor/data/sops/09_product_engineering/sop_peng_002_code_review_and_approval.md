---
sop_id: "SOP-PENG-002"
title: "Code Review and Approval"
business_unit: "Product & Engineering"
version: "3.3"
effective_date: "2024-10-17"
last_reviewed: "2025-06-22"
next_review: "2025-12-16"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Code Review and Approval

**SOP-ID:** SOP-PENG-002
**Version:** 3.3
**Effective Date:** 2024-10-17
**Owner:** David Park, VP of Engineering
**Approver:** Dr. Sarah Chen, CEO

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the mandatory framework for systematic code review, quality assurance, security validation, and formal approval of all software source code, configuration scripts, infrastructure-as-code (IaC) templates, and machine learning (ML) model code developed or modified for products and services offered by Meridian Health Technologies, Inc. (“Meridian”). The primary purpose is to ensure that all code artifacts entering the production software supply chain meet Meridian’s stringent requirements for security, reliability, maintainability, regulatory compliance, and alignment with the Trust Services Criteria (TSC) for Security, Availability, and Confidentiality as defined by the System and Organization Controls (SOC) 2 framework.

Adherence to this SOP directly supports Meridian’s SOC 2 Type II attestation by enforcing the change management controls necessary to prevent unauthorized or erroneous modifications to production environments. It also underpins our ISO 27001:2022 Annex A.8.25 (Secure Development Life Cycle) and A.14.2.2 (System Change Control Procedures) controls.

### 1.2 Scope
This SOP applies to all Meridian personnel, including full-time employees, contractors, temporary staff, and third-party vendors who contribute to, review, or approve code for any Meridian product, platform, or internal tool that underpins a business process within the scope of SOC 2.

**In-Scope Artifacts:**
- Application source code (Python, Java, TypeScript, Go, C++).
- Machine learning model training, evaluation, and deployment scripts (PyTorch, TensorFlow, Kubeflow Pipelines, MLflow recipes).
- IaC templates (Terraform, AWS CloudFormation, Ansible) for environments handling in-scope data.
- Database schema migration scripts (SnowSQL, Alembic).
- Container definitions and orchestration manifests (Dockerfiles, Kubernetes manifests).
- User interface components (React, Next.js).
- Configuration files for in-scope services and security tools (Okta, HashiCorp Vault, CrowdStrike policies-as-code).
- Automated test scripts where failures could lead to faulty production deployment.

**In-Scope Business Units and Platforms:**
- Clinical AI Platform
- HealthPay Financial Services
- MedInsight Analytics
- Meridian SaaS Platform (including all underlying shared services)
- Internal IT systems supporting the above (e.g., CI/CD infrastructure, ML model registry).

**Out of Scope:**
- Personal "scratch" code not intended for production systems.
- Pre-release experimentation in isolated sandbox environments, provided it never connects to production data stores or is promoted via the CI/CD pipeline without following this SOP.
- Formal mathematical derivations for novel ML algorithms prior to their translation into executable code.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **AI/ML Artifact** | A composite deliverable including source code, trained model weights (e.g., `.pth`, `.h5` files), environment specifications, and evaluation reports. |
| **Approval Matrix** | A defined set of rules specifying the minimum number and type of reviewers required for a given change based on risk profile. |
| **Author** | The individual who authored the code change and submits it for review. |
| **CD** | Continuous Deployment. The automated process of releasing approved code to production. |
| **CI** | Continuous Integration. The process of automating builds and tests upon code commit. |
| **CI/CD Pipeline** | The automated system (GitHub Actions, Argo Workflows) that builds, tests, and deploys code. |
| **Critical Hotfix** | An emergency change to remedy a Severity 0 (P0) incident causing production system unavailability or critical data corruption. |
| **CVE** | Common Vulnerabilities and Exposures. A publicly disclosed computer security flaw. |
| **IaC** | Infrastructure as Code. |
| **MR** | Merge Request (also known as Pull Request/PR). A request to merge one branch into another, which triggers the review process. |
| **Owner** | A designated senior engineer or architect responsible for a specific code domain (as defined in `CODEOWNERS` files). |
| **Reviewer** | A qualified individual responsible for inspecting a code change. |
| **SAST** | Static Application Security Testing. Automated analysis of source code for security vulnerabilities. |
| **SCA** | Software Composition Analysis. Automated analysis of third-party and open-source dependencies for known vulnerabilities and license compliance. |
| **SDLC** | Secure Development Life Cycle. |
| **SOC 2 CC8.1** | TSC Change Management control: “The entity authorizes, designs, develops or acquires, tests, and implements changes to infrastructure, data, software, and procedures to meet its objectives.” |
| **TSC** | Trust Services Criteria (SOC 2). |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for the Code Review and Approval process.

| Role | Responsibility | RACI Designation |
| :--- | :--- | :--- |
| **Software/ML Engineer (Author)** | Writes code and tests; performs self-review; creates comprehensive MR description; fixes all findings. | Responsible, Accountable (for their code) |
| **Peer Reviewer** | Reviews code for correctness, logic, style, and test coverage; approves MR if no issues. | Responsible |
| **Code Domain Owner (`CODEOWNERS`)** | Auto-assigned reviewer for specific files/paths; ensures architectural integrity of their domain; their approval is mandatory. | Accountable, Responsible |
| **ML Architect (Dr. Aisha Okafor's team)** | For AI/ML artifacts, verifies model metrics, data lineage, bias evaluation reports, and compliance with the AI Governance Committee's requirements. | Responsible (for AI-specific review) |
| **Security Champion** | Embedded team member trained in secure coding; performs initial security triage; triggers formal InfoSec review when required. | Responsible |
| **InfoSec Team (CISO Rachel Kim)** | Performs or coordinates in-depth manual security review and penetration testing as defined by the Security Review Triggers matrix. | Responsible |
| **VP of Engineering (David Park)** | Owns this SOP; grants final exception approvals; responsible for engineering-wide compliance and resourcing tooling. | Accountable |
| **Chief Privacy Officer/DPO (Dr. Klaus Weber)** | Mandatory reviewer for any code change that affects the processing of personal data in a novel way, per GDPR Article 25 (Data Protection by Design). | Responsible |
| **Chief Compliance Officer (Thomas Anderson)** | Grants final approval for regulatory exception handling related to SR 11-7 or EU AI Act documentation requirements. | Accountable (for exceptions) |
| **VP of IT Operations (Samantha Torres)** | Reviews IaC and configuration changes for production AWS and Azure environments. | Responsible (for IaC review) |

---

## 4. Policy Statements

All code changes must adhere to the following non-negotiable policy statements, which form the foundation of Meridian’s commitment to change management excellence under SOC 2 CC8.1.

1.  **Mandatory Review:** Every change to a production-bound codebase must undergo a peer review via a Merge Request (MR) by at least one qualified reviewer. The Author and a single Reviewer cannot be the same individual.

2.  **Automated Gates:** Code may not be merged until all required automated CI/CD pipeline stages pass successfully. This includes, at a minimum, compilation, unit tests, integration tests, linting, SAST, and SCA scans. Pipeline configurations themselves are subject to this SOP.

3.  **Separation of Duties:** A strict separation is enforced between the Author who develops the change and the individual who approves and merges the MR into a protected branch. No one can approve their own MR. For all in-scope systems, the merge action is a distinct privilege granted only to designated Release Managers.

4.  **Risk-Based Approval Matrix:** All code repositories are classified into a risk-based tier system (see Section 5.4). The required number and type of reviews scale proportionally with the risk tier. High-risk AI systems (per EU AI Act) and financial models (per SR 11-7) always require the highest tier of review.

5.  **Documentation of Review:** Every code review is permanently recorded. The record must include a documented summary of the review, decisions, findings, and resolution. This serves as the audit trail of evidence for SOC 2 auditors.

6.  **Blocking Findings:** Any single "Blocking" finding (e.g., confirmed security vulnerability, critical logic error, regulatory non-compliance) that is unresolved prevents approval. Reviewers have the explicit authority to place a "Do Not Merge" label on an MR.

---

## 5. Detailed Procedures

### 5.1 Pre-Review: Author Responsibilities
Before formally submitting an MR, the Author must complete the following preparatory steps. An MR submitted without these will be immediately rejected by the Reviewer.

1.  **Branch Creation:** Create a feature, bugfix, or hotfix branch from the relevant `main` or `release/X.X.X` branch. Branch names must follow the convention: `<type>/<JIRA-TICKET>-<brief-description>` (e.g., `feature/MDN-4523-add-cache-layer`).
2.  **Self-Review:** Using tools like `git diff`, the Author must perform a thorough self-review of every changed line. This is the first and most critical defense against errors.
3.  **Run Tests Locally:** Execute all relevant unit and integration tests locally and ensure they pass before pushing code.
4.  **Update Documentation:** Update any relevant inline code comments, README files, API documentation (Swagger/OpenAPI), and architectural decision records (ADRs) affected by the change.
5.  **Create the Merge Request:** Use the standardized MR template (see below). The Author must fill all sections completely. A poorly written MR is a valid reason for immediate rejection.

**Merge Request Template (Required in GitHub/GitLab):**

```markdown
## [JIRA-ID] Summary of Change
(Briefly describe the what and why of this change. What problem does it solve?)

## Type of Change
- [ ] Bug Fix
- [ ] New Feature
- [ ] Performance Improvement
- [ ] Refactoring
- [ ] Security Patch
- [ ] IaC/Config Change
- [ ] ML Model Code/Data Pipeline

## Risk Assessment
- **Risk Tier of Repository (I-III):** [e.g., II]
- **Does this change touch PII/PHI processing?** [Yes/No. If Yes, describe. E.g., "Modifies patient search query to filter by MRN."]
- **Does this modify a trained AI model's inference pipeline?** [Yes/No]
- **Does this modify financial calculations or models?** [Yes/No]
- **Does this introduce a new dependency?** [Yes/No. If Yes, link the SCA scan.]

## Testing Performed
- **New Unit Tests Added?** [Yes/No. Link to test files.]
- **Integration Tests Executed?** [Yes/No. Describe the scenario covered.]
- **Manual Testing Steps:** (List the steps a reviewer can take to validate the change in a staging environment.)

## Security Review Checklist (Pre-filled by Author/Security Champion)
- [ ] SAST scan is clean or findings are explained and suppressed with VP Eng approval.
- [ ] SCA scan shows no critical/high CVEs in new dependencies.
- [ ] No secrets or keys are hardcoded (verified with `detect-secrets` or similar).
- [ ] Input validation and output encoding are properly implemented for user-facing changes.

## Documentation
- [ ] Swagger/OpenAPI specs updated (if applicable).
- [ ] ADR updated or created (if a significant architectural decision was made).
- [ ] READMEs updated.
```

### 5.2 Automated CI/CD Pipeline Gates
Upon MR creation or any subsequent code push, the CI/CD pipeline automatically executes. A mandatory set of gates prevents human error and enforces quality standards. The MR cannot be merged until all gates are green.

| Gate ID | Stage | Tool / Method | Pass/Fail Criteria | Blocking? |
| :--- | :--- | :--- | :--- | :--- |
| **G-01** | Lint & Format | Black, ESLint, flake8, Terraform fmt | No linting errors per Meridian’s global style guide. `terraform fmt -diff` shows no changes. | Yes |
| **G-02** | Unit & Component Tests | Pytest, Jest, Go test | >85% line coverage for new code; total project coverage cannot decrease. All tests pass. | Yes |
| **G-03** | Integration Tests | Docker Compose, LocalStack | All critical-path smoke tests in `test/integration` pass. | Yes |
| **G-04** | SAST | CodeQL (GitHub Advanced Security) | Zero high/critical findings. Medium findings require inline justification by the Author. | Yes |
| **G-05** | SCA | Snyk / Dependabot | No dependencies with a CVSS score of 7.0 or higher. Exceptions require automated InfoSec Jira ticket creation and approval (see 8.1). | Yes |
| **G-06** | Secret Detection | HashiCorp Vault Git Pre-receive hook, `detect-secrets` | Zero detected secrets. | Yes |
| **G-07** | IaC Validation | Checkov, CloudFormation Guard | Zero `FAILED` checks for policies tagged `mandatory: true`. | Yes |
| **G-08** | Container Scan | Trivy (AWS ECR-integrated) | Zero critical OS or language-specific package vulnerabilities. | Yes |
| **G-09** | AI/ML Model Evaluation | Kubeflow Pipelines, MLflow | Model performance on a hold-out dataset meets pre-defined thresholds (e.g., PRAUC > 0.85). No data drift detected vs. baseline. | For AI Repos Only |
| **G-10** | Documentation Linting | Spectral (for APIs) | API spec linting passes. No breaking changes unless major version bump. | Yes |

### 5.3 Peer Review Procedure
Once automated gates are passed, the designated human reviewers perform their review. The process is structured and time-bound to ensure thoroughness without needless bottlenecking.

1.  **Reviewer Assignment:** The `CODEOWNERS` file automatically assigns relevant Domain Owners. For all Risk Tier II and III changes, the Tech Lead or Manager must manually assign at least one additional Peer Reviewer with strong domain knowledge. The Security Champion is assigned by a CI action that parses the risk checklist.
2.  **Review Cycle SLAs:**
    - **Standard MRs:** Initial review must begin within 4 business hours.
    - **Critical Hotfix MRs:** Review must begin within 30 minutes, per the Incident Response Plan (SOP-IT-001).
    - **Review Iterations:** Each subsequent review cycle by the Reviewer on a revised MR must begin within 2 business hours.
3.  **Review Scope and Checklist:** A reviewer is not a rubber stamp. They are responsible for inspecting the full change and its effect. The core review checklist:
    - **Logic & Correctness:** Are the algorithms correct? Are edge cases handled?
    - **Security:** Is there any input that isn't validated? Could this be exploited for SSRF, SQLi, XSS? Does it follow the principle of least privilege in its API calls?
    - **Maintainability & Readability:** Is the code understandable by others on the team? Are complex sections commented?
    - **Performance:** Are there obvious performance regressions (e.g., N+1 queries, loading large objects into memory)?
    - **Test Quality:** Do the tests actually validate the behavior? Are there tests for failure modes, not just the happy path?
    - **Compliance:** For AI models, does the code enforce transparency requirements (EU AI Act, Art. 13)? For financial code, is model logic fully documented per SR 11-7?
4.  **Defect Categorization:** Reviewers must tag findings with a severity.
    - **🚫 Blocking:** Security vulnerability, data corruption risk, regulatory violation, logic error, test failure. The MR cannot progress.
    - **⚠️ Minor:** Code style nit, optional refactoring suggestion, small performance tweak. The MR can be approved with a "Resolve or Ticket" expectation.
5.  **Resolving Comments:** The Author addresses feedback and pushes new commits. The Reviewer re-reviews the delta changes and resolves the conversation thread. Only the original commenter can resolve a thread.
6.  **Approval & Merge:** Once all reviewers have approved and all automated gates are green, the Author labels the MR as `ready-to-merge`. A designated Release Manager performs the final merge, maintaining separation of duties. The MR description is automatically squashed and committed, serving as the immutable audit trail.

### 5.4 Risk-Based Approval Matrix
Before seeking approval, the Author must determine the change's risk level based on the repository’s classification and the nature of the change. This matrix defines the minimum number and roles of required reviewers.

| Risk Tier | Description / Examples | Minimum Required Reviewers | Special Approvals |
| :--- | :--- | :--- | :--- |
| **Tier I: Low** | Internal tools, static marketing websites, documentation repositories. No access to PHI/PII or production infrastructure. | **1 Peer Reviewer** | None |
| **Tier II: Standard** | The Meridian SaaS Platform, MedInsight Analytics, shared libraries, IaC for staging environments. Handles PHI/PII but is not a direct financial or high-risk clinical system. | **1 Domain Owner** + **1 Peer Reviewer** | Security Champion review if the MR template indicates PII/PHI touchpoints. |
| **Tier III: Critical** | Clinical AI Platform (all components), HealthPay Financial Services (all components), IaC for production environments, CI/CD pipeline definitions, core identity services, cryptographic modules, any code processing PHI for 12M+ patients per SOP-DATA-001. | **1 Domain Owner (Architect)** + **1 Peer Reviewer** + **1 Security Champion** + **1 ML Architect (if AI)** | <li>Formal InfoSec review for significant feature work.</li><li>DPO review if the data processing purpose changes.</li><li>VP of Engineering approval for any IaC change to production.</li> |

---

## 6. Controls and Safeguards

This section details the technical and administrative controls that enforce the procedures and policies defined in this SOP. These controls are audited annually as part of our SOC 2 Type II examination.

### 6.1 Technical Enforcement
1.  **Branch Protection Rules (GitHub):** All Tier II and Tier III repositories must have these protection rules on the `main` and `release/*` branches:
    - **Require Approvals:** Minimum number of approvals set to match the Approval Matrix (e.g., 2 for Tier II).
    - **Dismiss Stale Reviews:** When new commits are pushed.
    - **Require Status Checks:** All mandatory CI gates (G-01 through G-08) must pass.
    - **Require Conversation Resolution:** All Blocking comments must be resolved.
    - **Include Administrators:** These rules apply to all users, including repository administrators, preventing any single person from circumventing the process.
    - **Restrict Direct Pushers:** Direct pushes to these branches are disabled for everyone. Only the CI/CD system’s service account or designated Release Managers can merge, and only via an approved MR.
2.  **CI/CD Pipeline Security:** Pipeline definitions themselves (`/.github/workflows/`, `/argo/`) are stored in a Tier III repository and subject to review by the VP of IT Operations, Samantha Torres. Production deployment credentials (AWS IAM roles) are securely injected via OIDC federation with HashiCorp Vault, never stored as long-lived GitHub secrets.
3.  **Automated SAST Tuning:** The InfoSec team reviews and tunes SAST tool rulesets quarterly to minimize false positives and ensure new vulnerability classes are detected. A “false-positive repository” of approved suppressions is maintained and reviewed during each audit.
4.  **Immutable Audit Logs:** All MRs, review comments, and pipeline run logs are shipped to a write-once-read-many (WORM) Amazon S3 bucket in the `LogArchive` account, which InfoSec controls. This data is retained for seven years per SOP-DATA-RET-003.

### 6.2 Administrative Safeguards
1.  **Quarterly Compliance Audits:** The Chief Compliance Officer, Thomas Anderson, and the VP of Engineering, David Park, will jointly conduct a quarterly audit of a random sample of 60 merged MRs across all risk tiers. The audit will check for a complete review narrative, adherence to the approval matrix, and proper documentation. Results are reported to the Executive Risk Committee.
2.  **Annual SOP Review:** This SOP is reviewed annually by the owner, David Park, to incorporate lessons learned, tooling updates, and changes in regulatory requirements. The `last_reviewed` and `next_review` dates are updated accordingly.
3.  **Reviewer Capacity Planning:** Engineering managers are responsible for factoring review time into their team’s sprint capacity. A heuristic of 15-30 minutes per review for standard changes is used for planning. No engineer shall be expected to consistently review more than 4 MRs per day to prevent review fatigue.

---

## 7. Monitoring, Metrics, and Reporting

Continuous monitoring and measurement are essential to demonstrate the operating effectiveness of our change management controls (SOC 2 TSC CC8.1). The following metrics are tracked in a central Datadog dashboard and reviewed monthly by the Engineering Leadership Team.

| KPI ID | Metric Name | Description | Target | Measurement Method |
| :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | Time-to-First-Review | Median time from MR submission (with all CI gates green) to the first non-author comment or approval. | < 2 hours for Tiers I & II; < 1 hour for Tier III. | Datadog metric derived from GitHub Events API. |
| **KPI-02** | Review Cycle Time | Median time from MR submission to final merge. | < 24 hours for Standard; < 2 hours for Hotfix. | Datadog metric. |
| **KPI-03** | Review Defect Escape Rate | Percentage of Blocking bugs found in production traced back to an incorrectly approved MR. | < 0.5% of production changes per quarter. | Post-incident review process (SOP-IT-001). |
| **KPI-04** | Review Non-Compliance Rate | Percentage of merged MRs from the quarterly audit that lack a complete review narrative or adhere to the approval matrix. | 0%. A single systemic failure triggers a root cause analysis and immediate remediation plan. | Quarterly manual audit (Section 6.2). |
| **KPI-05** | CI Pipeline Failure Rate | Percentage of MRs that fail an automated gate on the initial push. | N/A (Monitoring metric). A sustained month-over-month increase > 10% triggers a review of development practices. | Datadog metric. |
| **KPI-06** | Stale MR Count | Number of open MRs with no activity for > 3 business days. | < 10 across all of Product & Engineering. | GitHub API data. |

A “Code Review Health Report” is automatically generated by Datadog and sent to the CTO’s office and all VPs every Monday. This report includes all KPIs, broken down by team, and highlights the top 5 MRs by review cycle time for process improvement discussion.

---

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Process
Situations may arise where strict adherence to this SOP is not immediately feasible (e.g., a zero-day vulnerability patch, an SCA finding with no immediate fix). All exceptions must be formally documented, approved in a time-bound manner, and tracked to closure.

1.  **Request:** The Author creates an "Exception Request" issue using the `EXCPT-TEMPLATE` in GitHub/GitLab, detailing:
    - The specific SOP section(s) for which an exception is sought.
    - The business and technical justification, including the risk of *not* merging the change.
    - The compensating controls that will be in place.
    - The plan and timeline for full remediation.
2.  **Approval:**
    - **Low-Risk Exceptions (e.g., minor style rule violation):** Approved by the Engineering Manager.
    - **Medium-Risk Exceptions (e.g., suppressing a medium-severity SAST finding):** Requires joint approval from the Engineering Manager and the Security Champion.
    - **High-Risk Exceptions (e.g., merging without an ML Architect’s approval, skipping integration tests for a production hotfix):** Requires approval from the VP of Engineering, David Park, and the Chief Compliance Officer, Thomas Anderson. For AI-specific issues, the Chief AI Officer, Dr. Marcus Rivera, is also required.
3.  **Documentation:** The approved exception ticket link must be cited in the MR description, allowing reviewers and auditors to trace the deviation.
4.  **Closure Tracking:** All high-risk exceptions are reviewed at the next monthly Engineering Leadership meeting to ensure the remediation plan is on track. The Chief Compliance Officer maintains a centralized register of all open high-risk exceptions.

### 8.2 Escalation Path for Unresolved Disagreements
If an Author and Reviewer cannot agree on a finding’s validity or severity, the following escalation path is followed sequentially until a resolution is reached:

1.  **Tech Lead / Engineering Manager:** The immediate leader tries to mediate a technical consensus.
2.  **Domain Architecture Group:** David Park or a designated architect provides a design-level ruling, which is documented on the MR.
3.  **VP of Engineering:** In the rare event of a stalemate, David Park makes the final binding decision, balancing security, business delivery, and technical integrity. This decision is final and documented for the audit trail.

---

## 9. Training Requirements

All applicable personnel must be trained on the procedures and principles defined in this SOP to ensure a consistent, high-quality code review culture.

1.  **New Hire Onboarding:**
    - **Timing:** In the first week.
    - **Content:** “Meridian Secure Development Life Cycle 101” course on the LMS (Litmos). Module 4 specifically covers SOP-PENG-002. The training includes a walkthrough of the MR template, the approval matrix, and a simulated code review exercise.
    - **Verification:** A 10-question quiz; passing score is 100%.

2.  **Annual Refresher Training:**
    - **Timing:** Annually, aligned with the company-wide compliance training cycle (Q3).
    - **Content:** Covers changes to this SOP, lessons learned from the previous year's audit findings, and a refresher on the top-3 OWASP Top 10 vulnerabilities relevant to Meridian's stack.
    - **Specialized Tracks:** A separate, mandatory module is required for ML Engineers (“AI/ML Artifact Review”) and for Release Managers (“Branch Protection and Merge Compliance”).

3.  **Triggered Training:**
    - **Mechanism:** If the Quarterly Compliance Audit (Section 6.2) reveals a team with a significant non-compliance pattern, David Park can mandate a targeted re-training session for that specific team within 5 business days.
    - **Documentation:** All training completions are tracked in the HRIS (Workday) and reported to the CISO, Rachel Kim, for inclusion in the security awareness metrics dashboard. These records are auditable evidence for our SOC 2 examinations.

---

## 10. Related Policies and References

This SOP is part of a unified, integrated governance framework. It must be read and applied in conjunction with the following internal and external references.

**Internal Meridian SOPs & Policies:**
1.  **SOP-IT-001:** Incident Management and Response Plan
2.  **SOP-IS-004:** Vulnerability Management and Remediation
3.  **SOP-DATA-001:** Data Classification and Handling Policy
4.  **SOP-DATA-RET-003:** Data Retention and Disposal Schedule
5.  **SOP-RM-001:** Model Risk Management (SR 11-7 Compliance)
6.  **SOP-CPL-010:** AI Risk Management and Human Oversight (EU AI Act Compliance)
7.  **SDLC Policy:** Meridian Secure Development Lifecycle Policy

**External Standards & Frameworks:**
1.  **AICPA TSC 2017 (SOC 2):** Specifically CC8.1 (Changes to Infrastructure, Data, Software) and CC7.1 (Detection and Monitoring of Unusual Activities).
2.  **NIST Special Publication 800-53 Rev. 5:** CM-3 (Configuration Change Control), CM-4 (Impact Analyses), SA-10 (Developer Configuration Management).
3.  **ISO 27001:2022:** Annex A.8.25 (Secure development life cycle), A.14.2.2 (System change control procedures).
4.  **OWASP Top 10 (2021):** Fundamental security concepts for code reviewers.
5.  **GDPR:** Article 25 (Data protection by design and by default).

---

## 11. Revision History

| Version | Date | Author | Description of Change |
| :--- | :--- | :--- | :--- |
| 1.0 | 2020-03-15 | Jane Doe (Former VP Eng) | Initial creation and implementation of the code review SOP. |
| 2.0 | 2022-01-18 | David Park | Major revision to incorporate automated CI/CD pipeline gates and integrate formal SAST/SCA tooling (Snyk, CodeQL). |
| 3.0 | 2023-07-10 | David Park | Introduced the Risk-Based Approval Matrix (Tiers I-III) to scale reviews for different products and added the AI/ML artifact review requirements. |
| 3.1 | 2024-02-02 | David Park | Added the formal "Exception Handling and Escalation" section and detailed the Quarterly Compliance Audit process. Clarified separation of duties requirements. |
| 3.2 | 2024-07-25 | Rachel Kim (CISO) | Updated automated security gates to include secret detection (G-06) and IaC validation (G-07). Updated Security Champion role responsibilities. |
| 3.3 | 2025-06-22 | David Park | Annual review. Updated to align with new EU AI Act obligations and refined the AI/ML pipeline gate (G-09). Updated organizational titles and roles. Clarified training requirements for specialized tracks. |