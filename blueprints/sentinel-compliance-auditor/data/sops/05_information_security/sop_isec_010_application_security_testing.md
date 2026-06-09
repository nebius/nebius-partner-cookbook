---
sop_id: "SOP-ISEC-010"
title: "Application Security Testing"
business_unit: "Information Security"
version: "2.7"
effective_date: "2025-08-11"
last_reviewed: "2026-02-05"
next_review: "2026-08-17"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for application security testing across all software products, platforms, and services developed, deployed, or procured by Meridian Health Technologies. The purpose of this SOP is to ensure that security vulnerabilities are systematically identified, assessed, tracked, and remediated throughout the software development lifecycle (SDLC), thereby protecting the confidentiality, integrity, and availability of Meridian's information assets and the sensitive data entrusted to the organization by patients, healthcare providers, payers, and financial services customers.

### 1.2 Scope

This SOP applies to all software applications, application programming interfaces (APIs), microservices, mobile applications, and third-party software components that comprise or support the following Meridian business units and product lines:

| Business Unit | Products and Platforms in Scope |
|---|---|
| Clinical AI (Clinical AI Unit) | Diagnostic Imaging AI models, clinical decision support APIs, model serving infrastructure, model training pipelines, and associated web interfaces. |
| HealthPay (HealthPay Unit) | Payment processing platform, Patient Financing Portal, Revenue Cycle Management Dashboard, Clearinghouse Integration Engine, HealthPay Mobile App (iOS and Android), and Payment Gateway APIs. |
| Meridian Clinical Network (Clinical Network Unit) | Patient Portal (web and mobile), Provider Portal, Clinical Data Exchange APIs, HL7 FHIR Gateway, and associated backend services. |
| Corporate Systems (Information Technology Unit) | Identity and Access Management (IAM) platform, HR Portal, internal collaboration tools, and any custom-developed internal applications that process, store, or transmit Meridian Protected Health Information (MPHI) or Meridian Confidential Information (MCI). |

### 1.3 Application Security Testing Methods

The following testing methodologies are mandated under this SOP:

1.  **Static Application Security Testing (SAST):** Automated analysis of application source code, bytecode, and binary code to identify security vulnerabilities without executing the application.
2.  **Dynamic Application Security Testing (DAST):** Automated analysis of running web applications and APIs to identify security vulnerabilities observable from an external perspective.
3.  **Software Composition Analysis (SCA):** Automated identification and vulnerability analysis of all open-source and third-party software components, libraries, and frameworks integrated into Meridian products.
4.  **Interactive Application Security Testing (IAST):** Instrumentation-based analysis that observes application behavior during functional testing to identify security vulnerabilities with runtime context.
5.  **Manual Penetration Testing:** Structured, human-led security assessments conducted by qualified internal or external security professionals to identify vulnerabilities not readily discoverable by automated tools.

### 1.4 Applicability

All personnel involved in the design, development, testing, deployment, operation, and procurement of software applications at Meridian Health Technologies are required to comply with this SOP. Compliance obligations extend to:

- Meridian full-time employees and contractors within the Engineering and Product business units.
- Meridian full-time employees and contractors within the Information Security business unit.
- Third-party software development firms, independent contractors, and consultants engaged by Meridian to develop or modify software.
- Cloud service providers and managed service providers hosting or operating Meridian applications, to the extent contractually obligated by Meridian's vendor security requirements.

### 1.5 Out of Scope

The following are explicitly excluded from the scope of this SOP:

- **Infrastructure Security Testing:** Network penetration testing, cloud configuration audits, and operating system hardening assessments are covered under **SOP-ISEC-014: Infrastructure Security Testing**.
- **Physical Security Testing:** Physical penetration testing and facility security assessments are covered under **SOP-CORP-003: Physical Security Controls**.
- **Social Engineering Testing:** Phishing simulations and social engineering assessments are covered under **SOP-ISEC-005: Security Awareness and Training**.

---

## 2. Definitions and Acronyms

The following definitions and acronyms apply throughout this SOP:

| Term / Acronym | Definition |
|---|---|
| **Application Security Testing (AST)** | The collective set of automated and manual testing activities used to identify security vulnerabilities in software applications. |
| **Static Application Security Testing (SAST)** | White-box testing methodology that analyzes source code, bytecode, or compiled binaries for security flaws without executing the program. |
| **Dynamic Application Security Testing (DAST)** | Black-box testing methodology that analyzes a running application from the outside to identify exploitable vulnerabilities. |
| **Software Composition Analysis (SCA)** | Analysis of third-party and open-source components to identify known vulnerabilities (CVEs), license compliance issues, and outdated libraries. |
| **Interactive Application Security Testing (IAST)** | Security testing that instruments the application runtime to observe application behavior during automated or manual functional testing. |
| **Common Vulnerability Scoring System (CVSS)** | An open industry standard for assessing the technical severity of software vulnerabilities on a scale of 0.0 to 10.0. |
| **Common Vulnerabilities and Exposures (CVE)** | A publicly cataloged list of known cybersecurity vulnerabilities, each assigned a unique identifier. |
| **Software Bill of Materials (SBOM)** | A formal, machine-readable inventory of all components, libraries, and dependencies that comprise a software application. |
| **Meridian Protected Health Information (MPHI)** | Any individually identifiable health information processed, stored, or transmitted by Meridian systems, as defined under the Health Insurance Portability and Accountability Act (HIPAA). |
| **Personally Identifiable Information (PII)** | Any information that can be used to distinguish or trace an individual's identity, either alone or when combined with other information. |
| **Meridian Confidential Information (MCI)** | Proprietary business information, trade secrets, intellectual property, and other non-public information owned by or entrusted to Meridian. |
| **Payment Card Industry Data Security Standard (PCI DSS)** | A set of security standards designed to ensure that all companies that accept, process, store, or transmit credit card information maintain a secure environment. |
| **Remediation Service Level Agreement (SLA)** | The maximum allowable time between vulnerability discovery and confirmed remediation, based on the vulnerability's severity rating. |
| **False Positive** | A finding reported by a security testing tool that, upon manual review, is determined not to represent an actual exploitable vulnerability. |
| **Pipeline Gate** | An automated enforcement point in the CI/CD pipeline that prevents code from progressing to the next stage if security testing criteria are not met. |
| **Open Web Application Security Project (OWASP)** | A non-profit foundation that works to improve the security of software through community-led open-source projects, including the OWASP Top 10 vulnerability list. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for execution of this SOP. "R" denotes Responsible, "A" denotes Accountable, "C" denotes Consulted, and "I" denotes Informed.

| Activity / Task | Application Security Team (InfoSec) | Product Engineering Teams | Engineering Leadership (VP/Director) | Chief Information Security Officer (CISO) | Chief Technology Officer (CTO) | Internal Audit | Compliance Team |
|---|---|---|---|---|---|---|---|
| SAST Tool Configuration and Tuning | R | C | I | A | I | I | I |
| SAST Scan Execution (Pipeline) | C | R | I | I | A | I | I |
| SAST Finding Triage and Validation | R | C | I | A | I | I | I |
| DAST Scan Execution (Staging/Production) | R | C | I | A | I | I | I |
| DAST Finding Triage and Validation | R | C | I | A | I | I | I |
| SCA Scan Execution (Build) | C | R | I | I | A | I | I |
| SCA Vulnerability Remediation (Library Updates) | I | R | A | I | C | I | I |
| Vulnerability Remediation (Code Fix) | I | R | A | C | I | I | I |
| Remediation SLA Compliance | I | R | A | C | I | I | I |
| Exception Request Submission | C | R (Submitter) | A (Approver) | C | C | I | I |
| Exception Approval (≤ Medium Severity) | R | I | I | I | I | I | I |
| Exception Approval (≥ High Severity) | C | I | I | A | I | I | I |
| Quarterly AST Metrics Reporting | R | I | I | A | I | C | I |
| Tool License Management | R | I | I | A | I | I | I |
| Policy Compliance Auditing | C | C | I | I | I | R | I |

### 3.1 Named Role Assignments

| Role | Name | Title |
|---|---|---|
| SOP Owner | Rachel Kim | Chief Information Security Officer |
| SOP Approver | Dr. Sarah Chen | Chief Executive Officer |
| Application Security Lead | Marcus Thorne | Director, Application Security |
| Product Security Champion (Clinical AI) | Aisha Patel | Senior Security Engineer, Clinical AI |
| Product Security Champion (HealthPay) | David Okafor | Lead Security Architect, HealthPay |
| Product Security Champion (Clinical Network) | Maria Gonzalez | Security Engineering Manager, Clinical Network |
| VP of Engineering (HealthPay) | Kenji Tanaka | Vice President, HealthPay Engineering |
| VP of Engineering (Clinical AI) | Dr. Lena Petrov | Vice President, Clinical AI Engineering |

---

## 4. Policy Statements

Meridian Health Technologies is committed to the following policy principles governing application security testing:

### 4.1 Mandatory Testing

All applications in scope, as defined in Section 1.2, shall undergo continuous and comprehensive security testing throughout the SDLC. No application shall be promoted to a production environment without successfully passing the prescribed suite of security tests defined in Section 5 of this SOP.

### 4.2 Shift-Left Security

Meridian adopts a "shift-left" philosophy, mandating that security testing be integrated as early as possible in the development lifecycle. SAST and SCA shall be executed as automated Pipeline Gates within every feature branch build pipeline in the Meridian CI/CD platform (currently **GitHub Actions** and **Jenkins**) prior to pull request approval. This policy is designed to identify and remediate security flaws at the lowest possible cost and effort.

### 4.3 Tooling Standardization

The Information Security business unit shall provide, manage, and maintain a standardized suite of enterprise AST tools. Engineering teams are prohibited from independently procuring or deploying unapproved security testing tools without written authorization from the Application Security Lead. The current enterprise tool suite is:

| Testing Type | Enterprise Tool | Version | Deployment Model |
|---|---|---|---|
| SAST | **CodeSecure Enterprise** (formerly VeriScan) | 2025.4.x | On-premises appliance cluster; CI/CD plugin. |
| DAST | **AppScan Dynamic** (Meridian-licensed instance) | Cloud 2025.08 | SaaS, integrated with Meridian SSO. |
| SCA | **DependencyDefender Pro** | 7.3.x | CI/CD plugin; central dashboard. |
| IAST | **CodeSecure IAST Agent** | 2025.4.x | Instrumented in QA and staging environments. |
| Manual Penetration Testing | **Procured via approved vendor panel** | N/A | Annual and event-driven engagements. |

### 4.4 Risk-Based Prioritization

All identified vulnerabilities shall be prioritized for remediation based on a quantitative risk score derived from the **Common Vulnerability Scoring System (CVSS) v3.1**, adjusted for Meridian-specific environmental factors, including data classification of the affected system, exposure (internet-facing vs. internal), and exploitability maturity. The resulting Meridian Risk Score (MRS), categorized as Critical, High, Medium, Low, or Informational, shall dictate the applicable Remediation SLA.

### 4.5 Prohibition of Known-Vulnerable Components

Meridian explicitly prohibits the use of third-party and open-source software components with known, unpatched vulnerabilities rated **Critical** or **High** under the CVSS framework. SCA findings at these severity levels shall be treated as blocking issues for builds and deployments. The introduction of such components is a direct violation of this policy.

### 4.6 Segregation of Duties

The personnel responsible for developing application code shall not be the sole arbiters of the security posture of that code. The Application Security Team (InfoSec) shall have independent authority to review, validate, and, if warranted, challenge vulnerability findings, severity ratings, and remediation proposals. No vulnerability rated **Critical** or **High** may be closed or marked as "Accepted Risk" without the explicit approval of the Application Security Lead or the CISO.

### 4.7 Secure-by-Design

All new application features and significant architectural changes must be accompanied by a **Threat Modeling** exercise, conducted per **SOP-ISEC-008: Threat Modeling and Security Design Review**. The output of this exercise shall directly inform the configuration of SAST, DAST, and IAST test suites, ensuring comprehensive coverage of identified threats.

---

## 5. Detailed Procedures

This section outlines the step-by-step procedures for executing application security testing activities across the SDLC. These procedures are mandatory for all in-scope applications.

### 5.1 Security Requirements Definition (Phase: Design)

1.  **Product Manager** and **Lead Engineer** shall initiate a Security Design Review for all new applications or major feature releases by submitting a request via the **Jira Service Management (JSM) "Security Review"** project.
2.  The **Application Security Team** reviews the request and schedules a Threat Modeling workshop with the product team. The workshop shall be conducted in accordance with **SOP-ISEC-008**.
3.  Based on the identified threats, data classification (MPHI, PCI Cardholder Data, PII, MCI), and applicable regulatory requirements (SOC 2, HIPAA, PCI DSS), the Application Security Team shall produce a **Security Requirements Specification (SRS)** document.
4.  The SRS shall define specific, testable security requirements, including but not limited to:
    - Authentication mechanisms (e.g., multi-factor authentication enforcement).
    - Authorization models (e.g., Role-Based Access Control granularity).
    - Data protection requirements (e.g., encryption at rest algorithm and key management, data masking rules for PII/MPHI in logs).
    - Audit logging requirements.
    - Input validation and output encoding strategies.
5.  The SRS is provided to the product team as a Jira "Story" and must be marked as "Done" in the Definition of Done for the associated epic or release before deployment to production.

### 5.2 Software Composition Analysis (Phase: Develop, Pre-Commit)

**Objective:** Prevent the introduction of vulnerable third-party libraries.

1.  **Developer** initializes or updates a Meridian code repository. The repository must contain a valid dependency manifest (e.g., `pom.xml` for Maven, `package-lock.json` for npm, `requirements.txt` for Python, `go.sum` for Go).
2.  **Developer** installs the **DependencyDefender CLI** on their local development workstation. Configuration is provided via an internal wiki page: "DependencyDefender Local Setup".
3.  Before creating a pull request (PR) or merging code, the Developer executes the command `defender scan --path .` in the root of their project directory.
4.  DependencyDefender CLI evaluates all declared dependencies against the enterprise vulnerability database. The scan must complete with a **pass** status. A pass status is defined as zero (0) findings of **Critical** or **High** severity.
5.  If the local scan fails, the Developer must remediate the finding by upgrading the vulnerable component to a non-vulnerable version or, if no fix is available, initiating an Exception Request (see Section 8).
6.  **Pre-commit hook (enforced):** A Git pre-commit hook, installed as part of the standard Meridian developer environment bootstrap script, automatically performs a fast SCA scan of the staged changes. The commit is blocked if new Critical or High findings are introduced.

### 5.3 Static Application Security Testing (Phase: Develop, Merge Request)

**Objective:** Identify security flaws in custom-written code before it is merged into the main branch.

1.  **Developer** creates a Pull Request (PR) in **Azure DevOps** (for Clinical Network and Corporate Systems) or **GitHub Enterprise** (for Clinical AI and HealthPay) targeting the `main`, `develop`, or a release branch.
2.  The PR creation automatically triggers the `meridian-sast-scan` pipeline job, defined in a centrally maintained pipeline template library. This job executes a **CodeSecure Enterprise** scan on the diff of the source code changes introduced by the PR.
3.  The SAST tool analyzes the code against its comprehensive, Meridian-specific ruleset, which includes rules for the OWASP Top 10, SANS Top 25, and custom rules developed by the Application Security Team (e.g., rules specific to Meridian's internal cryptographic libraries).
4.  Upon completion, the SAST pipeline job posts a status check to the PR. The status check is a **Pipeline Gate**.
    - **Pass:** The scan report contains zero (0) new findings of **Critical**, **High**, or **Medium** severity compared to the target branch.
    - **Fail:** The scan report contains one or more new findings of **Critical**, **High**, or **Medium** severity. The findings are automatically posted as comments on the PR, linked to detailed finding information in the **CodeSecure Central Dashboard**.
5.  On a **Fail** status, the Developer must triage all new findings.
    - **False Positive:** The Developer marks the finding as "Not a Bug" in CodeSecure, providing a mandatory justification note.
    - **True Positive:** The Developer remediates the vulnerability in the code and pushes a new commit. The SAST pipeline job re-executes automatically.
6.  A designated **Product Security Champion** for the business unit must review and approve the SAST pass status. This approval is a mandatory condition for branch policy to allow the PR to be merged. Merging without this approval requires an explicit override from the Application Security Lead.

### 5.4 Dynamic Application Security Testing in Lower Environments (Phase: Test)

**Objective:** Identify runtime vulnerabilities in an integrated environment.

1.  Following a successful deployment to the **QA** or **Integration** environment, the CD pipeline triggers a DAST scan.
2.  The pipeline job invokes the **AppScan Dynamic** API to initiate a pre-configured "Full Scan" on the application's staging URL. The scan configuration is stored as an AppScan template, managed by the Application Security Team.
3.  The Application Security Team is responsible for ensuring the DAST scan configuration is updated for new API endpoints and significant UI workflow changes. Product teams notify the AppSec team of such changes via a dedicated `#ask-appsec` Slack channel at least **two business days** before the planned deployment.
4.  The DAST scan executes a comprehensive crawl and audit, including authenticated scanning. A functional testing account with pre-configured roles and data, created per **SOP-ISEC-005**, is used.
5.  Upon completion, if the scan discovers any **Critical** or **High** severity findings, the automated release orchestration platform (**Octopus Deploy**) is prevented from promoting the release to the **Staging** environment.

### 5.5 Interactive Application Security Testing (Phase: Test)

**Objective:** Provide high-fidelity vulnerability detection during quality assurance (QA) testing.

1.  The QA environment deployment pipeline automatically instruments the application with the **CodeSecure IAST Agent**.
2.  As the **QA Team** executes manual and automated functional tests (e.g., Selenium scripts), the IAST agent passively observes application behavior, data flow, and control flow.
3.  Identified vulnerabilities (e.g., SQL Injection, Second-Order XSS, insecure deserialization) are reported in real-time to the **CodeSecure Central Dashboard**, correlated with the specific functional test case that triggered the finding.
4.  Findings are treated with the same authority as SAST findings. The QA team is trained to recognize and escalate IAST findings, which are automatically tagged with the business unit and application name.

### 5.6 Dynamic Application Security Testing in Pre-Production (Phase: Staging)

**Objective:** Final validation of runtime security posture in a production-like environment before go-live.

1.  This scan is a mandatory step in the production deployment runbook.
2.  The **Release Manager** or the responsible **DevOps Engineer** triggers the "Pre-Prod DAST scan" against the **Staging** environment URL using AppScan Dynamic. This scan is identical in configuration to the QA scan but targets the staging endpoint.
3.  The scan must complete with a **pass** status, defined as zero (0) un-remediated findings of **Critical** or **High** severity. All such findings must be either fixed or accompanied by an approved Exception (see Section 8) before the production deployment can proceed. The **VP of Engineering** for the business unit is accountable for this sign-off.

### 5.7 Manual Penetration Testing (Phase: Production & Major Releases)

**Objective:** Identify business logic flaws and complex, multi-step vulnerabilities that evade automated tools.

1.  The Application Security Team manages an annual, independent penetration testing engagement for all core product platforms (Clinical AI APIs, HealthPay Platform, Patient Portal). This is a key control for SOC 2 and PCI DSS compliance.
2.  Additionally, a point-in-time manual penetration test is mandated for any **Major Release**, defined as a release incrementing the major version number (e.g., v1.x to v2.0) or any release introducing a fundamentally new, high-risk feature such as a new payment rail or clinical data exchange protocol.
3.  The **Product Security Champion** initiates the procurement process with an approved vendor from the Meridian Vendor Security Panel, drafting a Statement of Work (SOW) that defines scope, test types, and rules of engagement.
4.  The Application Security Lead approves the SOW. Testing is conducted against the production environment or a staging environment certified by Engineering as a 1:1 replica of production.
5.  The vendor delivers a final report. All findings from this report are ingested into the corporate vulnerability management system for tracking and remediation according to the SLAs defined in Section 5.9.

### 5.8 Triage and Remediation Workflow

This workflow applies to all verified true-positive vulnerabilities from any source.

1.  **Finding Ingest:** All validated, non-false-positive findings from SAST, DAST, SCA, IAST, and Manual PenTests are automatically or manually ingested into the **Vulnerability Response System (VRS)**, Meridian's system of record for vulnerability management, currently **ServiceNow Security Operations (SecOps) module**. Each finding generates a unique **Vulnerability Response Task (VRT)**.
2.  **Auto-Assignment:** The VRS assigns the VRT to the **Product Engineering Lead** for the affected application based on asset tags. The assignment includes the full technical details, the calculated Meridian Risk Score (MRS), and the applicable Remediation SLA deadline.
3.  **Triage:** The assigned Engineering Lead has **5 business days** to triage the finding. Triage actions include:
    - **Confirm:** Accept the finding and propose a remediation plan with a target date within the SLA.
    - **False Positive Challenge:** Propose that the finding is a false positive. This must be substantiated with a detailed technical rationale, which is submitted back to the **Application Security Team** for review and final adjudication.
4.  **Remediation:** The Engineering Lead assigns the VRT to a specific Engineer for implementation. The fix is developed, code-reviewed, and tested.
5.  **Validation Rescan:** Upon deploying the fix to the target environment, the Engineer or a DevOps pipeline triggers a targeted re-scan using the same tool that originated the finding. A successful re-scan that does not reproduce the finding is the sole acceptable condition for closing the VRT in ServiceNow.

### 5.9 Remediation Service Level Agreements (SLAs)

All remediation efforts shall be governed by the following SLAs, measured from the timestamp of the initial finding creation in the VRS to the timestamp of the successful closure validation rescan.

| Meridian Risk Score (MRS) | CVSS v3.1 Score Range | Severity Label | Remediation SLA (Production / Internet-Facing Systems) | Remediation SLA (Internal / Non-Critical Systems) |
|---|---|---|---|---|
| 9.0 - 10.0 | 9.0 - 10.0 | **Critical** | **48 hours** | **7 calendar days** |
| 7.0 - 8.9 | 7.0 - 8.9 | **High** | **14 calendar days** | **30 calendar days** |
| 4.0 - 6.9 | 4.0 - 6.9 | **Medium** | **90 calendar days** | **180 calendar days** |
| 0.1 - 3.9 | 0.1 - 3.9 | **Low** | **Next major release** | **Next major release or 365 days, whichever is earlier** |
| 0.0 | N/A | **Informational** | No SLA; reviewed for next major release. | No SLA; reviewed for next major release. |

**Note on SLA Breaches:** Any breach of a Critical or High severity Remediation SLA triggers an automatic escalation to the CISO and the relevant VP of Engineering, as detailed in Section 18.1.

---

## 6. Controls and Safeguards

This section delineates the specific technical and administrative controls implemented to satisfy the requirements of this SOP and the relevant trust services criteria from the SOC 2 framework, particularly within the **Common Criteria (CC) Series** and the **Logical and Physical Access Controls (CC6 Series)** . For HIPAA, controls address the Technical Safeguards of the Security Rule, though full operationalization of the Minimum Necessary Standard is addressed in the access provisioning SOP and is out of scope for the granularity of this testing policy.

### 6.1 SOC 2 Controls

The following detailed controls are established to demonstrate the operating effectiveness of application security testing, aligned with the **SOC 2 Security Category (CC Series), Logical and Physical Access Controls (CC6 Series), and System Operations (CC7 Series)** .

| Control ID | Control Description | Testing Frequency | Responsible Role | Related Tool / Evidence |
|---|---|---|---|---|
| **CC6.1-AST-01** | Logical access to application source code repositories (GitHub Enterprise, Azure DevOps) is restricted based on a documented, role-based access control (RBAC) model. Multi-factor authentication (MFA) is mandated for all user access. | Daily (Automated) | IAM System, VP Engineering | Identity Provider (Okta) logs, repository access audit trails. |
| **CC6.1-AST-02** | The code commit process requires a unique, traceable user ID. Shared, group, or generic accounts are prohibited for code commits. The `GIT_AUTHOR_NAME` and `GIT_COMMITTER_EMAIL` must map to a valid Meridian identity. | Per Commit (Automated Pre-Receive Hook) | DevOps Lead, InfoSec | Git commit log, pipeline hook violation log. |
| **CC6.3-AST-01** | The CI/CD pipeline (GitHub Actions, Jenkins) enforces a mandatory SAST Pipeline Gate (as described in 5.3) before any code merge to a protected branch. The status "pass" is required. | Per Pull Request (Automated) | Product Security Champion | CI/CD pipeline execution logs, Pull Request status check records. |
| **CC6.3-AST-02** | The CD pipeline enforces a mandatory SCA Pipeline Gate before any container image or deployment artifact is stored in the corporate artifact repository (JFrog Artifactory). A pass status (zero Critical or High CVEs) is required. | Per Build (Automated) | DevOps Lead | Artifactory plugin logs, pipeline execution logs. |
| **CC7.1-AST-01** | Detection of anomalous or malicious activity is achieved via a Web Application Firewall (WAF) placed in front of all production internet-facing applications. The WAF is configured in "blocking" mode for OWASP Top 10 rule categories. | Continuous | Security Operations Center (SOC) Lead, Infrastructure Team | AWS WAF logs, Datadog monitors, #soc-alerts Slack channel logs. |
| **CC7.1-AST-02** | The Runtime Application Self-Protection (RASP) agent is deployed on all Java-based HealthPay payment APIs. The RASP agent is configured to "monitor" mode for SQL Injection and Command Injection, logging detections to Datadog SIEM. | Continuous | Application Security Lead | RASP agent dashboard, Datadog SIEM alerts. |
| **CC7.2-AST-01** | The Application Security Team monitors Threat Intelligence feeds (e.g., CISA Known Exploited Vulnerabilities, vendor security advisories) for critical vulnerabilities in Meridian's technology stack. Upon such notification, an emergency scan and remediation process is initiated outside the regular SLA cadence. | Continuous | Application Security Lead | ServiceNow SecOps Incident record. |
| **CC7.3-AST-01** | Quarterly vulnerability assessments, including authenticated DAST and full-infrastructure SAST, are performed on all production systems. The report is reviewed by the CISO and CTO. | Quarterly | Application Security Lead | Formal assessment report PDF, meeting minutes from Quarterly Security Review. |
| **CC7.4-AST-01** | Security incidents suspected to originate from an application-layer vulnerability are managed per **SOP-ISEC-002: Incident Response**. The Incident Response Team engages the Application Security Team for forensic analysis and root cause identification. | Event-driven | CISO, SOC Lead | Incident ticket in ServiceNow SIR module, Post-mortem report. |
| **CC7.5-AST-01** | For each major incident, a root cause analysis (RCA) is performed. If the root cause was a missed application vulnerability, the RCA must include a formal plan to update SAST/DAST rulesets or manual testing procedures to prevent recurrence. | Post-Incident | VP of Engineering (system owner), AppSec Lead | RCA document, updated SAST custom rule, updated test plan. |

### 6.2 HIPAA Controls

For applications processing Electronic Protected Health Information (ePHI), the following controls derived from **45 CFR Part 164, Subpart C - Security Standards for the Protection of Electronic Protected Health Information**, are implemented through this SOP.

- **Audit Controls (§ 164.312(b)):** All Meridian applications handling ePHI shall use the standard Meridian audit logging framework, which captures create, read, update, and delete (CRUD) actions on ePHI data objects. Application logs must include the Meridian User ID, timestamp, action type, and the unique identifier of the accessed data object. The Application Security Team's DAST test plan shall include test cases to verify the presence and correct functioning of these audit log mechanisms. The exact mechanism and format for log generation is specified here, but the specific, granular system-level log events captured and the mandated minimum retention period for such logs are defined in the Data Retention Schedule managed by the Compliance Team.
- **Person or Entity Authentication (§ 164.312(d)):** SAST test suites shall be configured with rules to detect hard-coded credentials, weak password complexity validation, and bypassable authentication logic. Review of authentication mechanisms is a mandatory phase in the Threat Modeling process (see 5.1) for all ePHI-handling applications.
- **Access Controls (§ 164.312(a)):** This SOP mandates that all applications implement Role-Based Access Control (RBAC) for restricting access to ePHI. DAST and manual penetration tests must include detailed, role-based test cases to verify that horizontal and vertical privilege escalation is not possible. The assignment of those roles and the implementation of the "Minimum Necessary" standard—ensuring a user's assigned role provides access only to the specific ePHI required to do their job—is a function of the identity governance and role engineering process defined in the Access Management Policy. Security testing can verify that the technical RBAC enforcement matches the intended role, but the policy governing the definition of those roles themselves is external to this SOP.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Monitoring

The Application Security Team shall maintain continuous monitoring over the health and operational status of all enterprise AST tools via a dedicated Datadog dashboard. Monitored metrics include scan queue depth, job failure rate, license utilization, and server resource consumption.

### 7.2 Critical Metrics and Key Performance Indicators (KPIs)

The following metrics shall be captured, calculated, and reported to measure the effectiveness of the Application Security Testing program. These KPIs are reviewed monthly by the Application Security Lead and quarterly by the CISO, CTO, and the Governance, Risk, and Compliance (GRC) Committee.

| KPI Category | Metric Name | Definition and Calculation Method | Target | Reporting Cadence |
|---|---|---|---|---|
| **Coverage** | SAST Pipeline Adoption Rate | `(Number of actively developed repositories with passing SAST Pipeline Gate) / (Total number of actively developed repositories)` | 100% for Tier 1 & 2 apps; 95% Tier 3 | Monthly |
| **Coverage** | SCA Scan Rate | `(Total production artifacts scanned by SCA at build) / (Total production artifacts built)` | 100% | Monthly |
| **Efficiency** | Mean Time to Remediate (MTTR) by Severity | `(Sum of time from VRT creation to VRT closure for resolved findings) / (Number of resolved findings)`, grouped by severity (Critical, High, Medium). | ≤ 75% of SLA threshold | Monthly |
| **Efficiency** | False Positive Rate (SAST) | `(Number of findings marked "False Positive" by Dev and confirmed by AppSec) / (Total number of SAST findings)` | < 15% | Monthly |
| **Efficiency** | Stale Vulnerability Rate | `(Number of unresolved, non-excepted Vulnerabilities past their SLA deadline) / (Total number of unresolved Vulnerabilities)` | 0% for Critical/High; < 2% for Medium | Weekly (via automated report) |
| **Effectiveness** | Penetration Test Finding Remediation Rate | `(Number of Critical/High findings from the last Annual Pen Test that have been resolved) / (Total number of Critical/High findings from the last Annual Pen Test)` | 100% | Annually |
| **Effectiveness** | Mean Time to Detect (MTTD) via DAST/IAST vs. External Report | Time difference between vulnerability identification by Meridian's internal DAST/IAST and the first external vulnerability report from Bug Bounty program or security researcher. | Zero; all Critical/High vulns must be found first by Meridian's tools. | Event-driven |

### 7.3 Reporting

1.  **Technical Vulnerability Report:** An automated, weekly report generated from the VRS (ServiceNow SecOps) detailing all new, open, and overdue vulnerabilities, grouped by business unit and application owner. Delivered to all VP of Engineering and Director of Engineering.
2.  **Monthly AST Operations Report:** A formal memo from the Application Security Lead to the CISO, summarizing tool health, KPI dashboards, SLA breach summaries, and remediation progress against quarterly goals.
3.  **Quarterly Business Review (QBR):** A presentation delivered by the CISO to the CEO, CTO, and General Counsel. This includes a summary of SOC 2 control attestation status, the overall risk posture from an application security perspective, a summary of exceptions granted, and status of the annual penetration test.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

Situations may arise where a vulnerability finding cannot be fully remediated within its prescribed SLA or where a remediation is technically infeasible (e.g., a Critical vulnerability in a deeply embedded, non-updatable third-party component of a medical device software package). In such cases, a formal Exception Request is required.

1.  **Submission:** The **Product Engineering Lead** submits an Exception Request via the **ServiceNow Service Catalog "Security Exception Request"** form. The request must include:
    - The unique identifier of the related Vulnerability Response Task (VRT).
    - A detailed technical justification for why a standard remediation cannot be performed.
    - A proposed compensating control, with specific, verifiable details. This could be a WAF rule, a RASP rule, a network micro-segmentation policy, or a highly specific, documented operational monitoring procedure.
    - The proposed duration of the exception (must not exceed one year).

2.  **Risk Assessment:** The **Application Security Lead** performs a risk assessment of the compensating control's effectiveness against the original vulnerability. The assessment includes a review of the CVSS v3.1 score, resulting in a new, residual risk score (Adjusted MRS).

3.  **Approval Authority:**
    - Exceptions for vulnerabilities with a residual risk rating of **Low** or **Medium**: Reviewed and approved by the **Application Security Lead**.
    - Exceptions for vulnerabilities with a residual risk rating of **High**: Reviewed by the Application Security Lead and approved by the **Chief Information Security Officer (CISO)**.
    - Exceptions for vulnerabilities with a residual risk rating of **Critical**: Reviewed by the CISO and approved jointly by the **Chief Executive Officer (CEO)** and the **Chief Medical Officer (CMO)** (if the system impacts patient safety).

4.  **Tracking:** All approved exceptions are tracked in a central Compliance Exceptions Register. The exception has a mandatory expiration date. The owner is automatically notified 30 days, 14 days, and 7 days before expiration to either renew (with improved justifications) or close out the exception.

### 8.2 Escalation for SLA Breach

In the event of a non-excepted vulnerability breaching its defined SLA:

1.  **Day of Breach (Critical/High):** An automated email is sent from the VRS to the **Product Engineering Lead** and their direct **VP of Engineering**, with a copy to the **Application Security Lead** and CISO. This creates a high-priority task.
2.  **One Business Day Post-Breach (Critical/High) - Unresolved:** The VRS automatically generates a formal risk acceptance memo and emails it to the **Chief Technology Officer (CTO)** , **Chief Information Officer (CIO)** , and CISO. The VP of Engineering for the owning business unit must present a remediation or exception plan to the CISO within one additional business day.
3.  **Medium Severity Breach:** A weekly report of all Medium-severity SLA breaches is sent to the **VP of Engineering** and **Application Security Lead**.

---

## 9. Training Requirements

### 9.1 Role-Based Training

All personnel identified in the RACI matrix (Section 3) must complete the following security training, managed and tracked via the Meridian Learning Management System (LMS), **Workday Learning**.

| Training Module Code | Module Name | Audience | Frequency | Duration |
|---|---|---|---|---|
| **SEC-T-101** | Meridian Secure Coding Standards & OWASP Top 10 | All Software Engineers, DevOps Engineers, QA Engineers | Annually | 4 hours |
| **SEC-T-201** | AST Tooling for Engineers (SAST, SCA, DAST) | All Software Engineers, DevOps Engineers | Annually | 2 hours |
| **SEC-T-301** | Advanced Application Security for Champions | All Product Security Champions | Annually | 8 hours |
| **SEC-T-401** | Application Security for Non-Engineering Roles | Product Managers, Scrum Masters, Engineering Directors | Bi-annually | 1 hour |
| **SEC-T-501** | Threat Modeling Practitioner Workshop | Product Security Champions, Principal Engineers, Architects | Once; refresher required on major change to SOP-ISEC-008 | 16 hours (2-day workshop) |

### 9.2 Compliance Tracking

Module completion status is tracked in Workday Learning. The Application Security Team shall produce a monthly compliance report, distributed to all VPs and Directors of Engineering. Any individual with overdue, mandatory training shall have their access to Meridian source code repositories temporarily suspended until compliance is achieved. This process is automated via Okta group membership integration with Workday.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Document Title | Relationship |
|---|---|---|
| **SOP-COMP-005** | Meridian Code of Conduct and Ethics | Overarching employee obligation to protect company assets. |
| **SOP-ISEC-002** | Incident Response Plan | Procedure for responding to security incidents, including those from AST findings. |
| **SOP-ISEC-003** | Vulnerability Management Lifecycle | The broader process for managing all vulnerabilities, to which this SOP feeds findings. |
| **SOP-ISEC-004** | Information Classification and Handling | Defines MPHI, PII, and MCI, which inform the risk scores in this SOP. |
| **SOP-ISEC-005** | Identity and Access Management | Specifies the creation and management of functional testing accounts for DAST. |
| **SOP-ISEC-008** | Threat Modeling and Secure Design Review | Mandates the process that generates the security requirements in Section 5.1 of this SOP. |
| **SOP-ISEC-014** | Infrastructure Security Testing | Covers security testing for cloud and network infrastructure, out of scope for this SOP. |
| **SOP-ISEC-015** | Third-Party Vendor Security Management | Policy for assessing the security of software procured from external vendors. |
| **SOP-ENG-003** | Software Development Lifecycle (SDLC) Policy | Overarching engineering policy into which these security testing procedures integrate. |

### 10.2 External Standards and Regulatory References

- **AICPA SOC 2® for Service Organizations: Relevant to the Security, Availability, and Confidentiality Trust Services Criteria (TSC) 2017 (with 2022 revision considerations).** Specifically used to inform controls in Section 6.1.
- **ISO/IEC 27001:2022, Annex A, Control 8.25 (Secure Development Lifecycle) and 8.29 (Security Testing in Development and Acceptance).**
- **NIST Special Publication 800-53, Revision 5: Security and Privacy Controls for Information Systems and Organizations.**
- **Open Web Application Security Project (OWASP) Application Security Verification Standard (ASVS) V4.0.3.**
- **PCI DSS v4.0, Requirements 6.2.2, 6.3.2, and 11.3.2.**
- **45 CFR § 164.312 - Technical Safeguards (HIPAA Security Rule).**

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
|---|---|---|---|
| 1.0 | 2023-01-15 | Rachel Kim, Marcus Thorne | Initial policy creation. Established SAST and Manual Pentest requirements. |
| 1.5 | 2023-08-22 | Rachel Kim | Updated to incorporate HealthPay PCI DSS scope. Added DAST requirement for all internet-facing apps. Introduced Remediation SLAs table. |
| 2.0 | 2024-05-10 | Rachel Kim | Major revision. Added SCA and IAST requirements. Shifted policy framework to align with SOC 2 CC6 Series controls. Formalized RACI matrix and roles. |
| 2.5 | 2025-02-20 | Marcus Thorne | Updated for new Clinical AI product line (EU MDR scope). Changed enterprise SAST tool from Fortify to CodeSecure. Refined triage workflow. Added Threat Modeling integration. |
| **2.7** | **2025-08-11** | **Rachel Kim** | **Refined IAST procedures. Added specific MFA control (CC6.1-AST-01). Updated Exception Handling to include CMO approval for patient safety-related exceptions. Clarified HIPAA Audit Control and Access Control language. Annual review completed.** |