---
sop_id: "SOP-PENG-001"
title: "Secure Software Development Lifecycle"
business_unit: "Product & Engineering"
version: "1.3"
effective_date: "2025-04-19"
last_reviewed: "2026-04-01"
next_review: "2026-10-25"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Secure Software Development Lifecycle

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) defines the mandatory, risk-based Secure Software Development Lifecycle (SSDLC) for all software products, features, platforms, and machine learning (ML) models developed, acquired, or maintained by Meridian Health Technologies, Inc. The SSDLC integrates security, privacy, and regulatory compliance into every phase of the software development process, from initial concept through architecture, development, testing, deployment, operation, and eventual decommissioning. This ensures that Meridian’s products protect the confidentiality, integrity, and availability of protected health information (PHI) and other sensitive data, comply with applicable regulations, and align with our board-approved risk appetite.

### 1.2 Scope
This SOP applies to all Meridian business units—including the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform—and to all personnel involved in the software lifecycle: full-time employees, contractors, consultants, and third-party vendors. The scope encompasses:

- **All custom-developed code** for web applications, APIs, backend services, mobile applications, and data pipelines.
- **All AI/ML model development** artifacts, including training pipelines, feature engineering code, inference endpoints, and model serialization formats.
- **All Infrastructure as Code (IaC)** used to provision and manage AWS, Azure, and on-premises resources (CloudFormation, Terraform, Ansible).
- **All third-party and open-source software** (OSS) components integrated into the Meridian technology stack.
- **Configuration files, scripts, and orchestration logic** that impact the security posture of production and pre-production environments.
- **CI/CD pipeline definitions** (Jenkinsfiles, GitLab CI YAML, GitHub Actions workflows) that automate build, test, and deployment processes.

### 1.3 Guiding Principles
All software development activities shall adhere to these core principles:

1. **Security by Design:** Security requirements are defined alongside functional requirements, not retroactively bolted on.
2. **Shift Left:** Security testing and validation occur as early as possible in the lifecycle, with developer self-service tooling.
3. **Least Privilege:** Every system component, service account, and user operates with the minimum set of permissions required.
4. **Defense in Depth:** No single security control is considered sufficient; multiple compensating controls are layered throughout the lifecycle.
5. **Privacy by Default:** PHI/PII handling is minimized by default; explicit justification is required for any collection, storage, or transmission of sensitive data.
6. **Continuous Compliance:** Regulatory obligations are continuously validated, not merely asserted at audit time.

### 1.4 Exemptions
Legacy systems in a "Maintain-Only" support state (as formally classified by the VP of Engineering) may deviate from certain phases of this SOP only if a documented risk acceptance is approved per Section 8 of this SOP. All other deviations require a formal exception.

---

## 2. Definitions and Acronyms

| Term | Definition |
|---|---|
| **SSDLC** | Secure Software Development Lifecycle — the integrated processes defined in this SOP. |
| **PHI** | Protected Health Information, as defined by the HIPAA Privacy Rule (45 CFR §160.103). |
| **ePHI** | Electronic Protected Health Information — PHI that is transmitted by or maintained in electronic media. |
| **PII** | Personally Identifiable Information — any information that can be used to distinguish or trace an individual's identity. |
| **DAST** | Dynamic Application Security Testing — testing a running application for vulnerabilities. |
| **SAST** | Static Application Security Testing — analyzing source code for vulnerabilities without executing it. |
| **SCA** | Software Composition Analysis — identifying and managing open-source and third-party component risk. |
| **IAST** | Interactive Application Security Testing — instrumentation-based testing combining SAST and DAST approaches. |
| **IaC** | Infrastructure as Code — machine-readable definition files for provisioning infrastructure. |
| **SBOM** | Software Bill of Materials — a nested inventory of all components within a software artifact. |
| **STRIDE** | Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege — a threat modeling methodology. |
| **CVSS** | Common Vulnerability Scoring System — an open industry standard for assessing the severity of vulnerabilities. |
| **CVE** | Common Vulnerabilities and Exposures — a list of publicly disclosed cybersecurity vulnerabilities. |
| **CI/CD** | Continuous Integration / Continuous Deployment — the automated pipeline that builds, tests, and deploys code. |
| **RACI** | Responsible, Accountable, Consulted, Informed — a responsibility assignment matrix. |
| **SDLC** | Software Development Lifecycle. |
| **SME** | Subject Matter Expert. |
| **TRB** | Technical Review Board — governance body that reviews architectural decisions and risk acceptances. |

---

## 3. Roles and Responsibilities

The following table defines the specific responsibilities for each Meridian role with respect to the SSDLC. All personnel are expected to understand and execute their designated responsibilities. The owner for each functional area is accountable for ensuring that their team possesses the required skills through training (see Section 9).

### 3.1 RACI Matrix

| Phase / Activity | Product Manager | Engineering Lead | Developer | Security Architect | DevOps Engineer | QA Engineer | Data Scientist | Compliance Officer |
|---|---|---|---|---|---|---|---|---|
| **Requirements** | **A** | C | I | C | I | I | I | C |
| **Threat Modeling** | I | R | C | **A** | C | I | C | I |
| **Architecture Review** | I | R | C | **A** | C | I | C | I |
| **Secure Coding (Authoring)** | I | A | **R** | C | I | I | R | I |
| **Code Review (Security)** | I | R | R | **A** | I | I | R | I |
| **SAST/SCA Scanning** | I | A | R | C | **R** | I | R | I |
| **DAST/IAST Testing** | I | A | C | C | R | **R** | C | I |
| **Penetration Testing** | I | C | C | **A** | C | C | C | C |
| **Change Management Approval** | C | R | C | C | C | I | I | I |
| **Deployment to Production** | I | A | I | C | **R** | C | I | I |
| **Post-Deploy Monitoring** | I | R | I | C | **R** | I | R | I |
| **Vulnerability Management** | I | R | R | **A** | C | I | R | I |

**Key:** R = Responsible (does the work), A = Accountable (signs off, the "owner"), C = Consulted (provides input), I = Informed (kept up to date)

### 3.2 Role-Specific Mandates

**CEO (Dr. Sarah Chen):**
- Ultimate accountability for Meridian’s information security posture.
- Approves all SOPs classified "Internal" and above.
- Authorizes capital expenditures for enterprise security tooling.

**VP of Engineering (David Park):**
- Owner of this SOP and accountable for its effectiveness across all engineering teams.
- Chairs the Technical Review Board (TRB).
- Approves all Tier-2 and Tier-3 exceptions (Section 8).
- Reports on SSDLC metrics to the Executive Risk Committee quarterly.

**Director of Information Security (CISO):**
- Establishes technical security standards and secure coding guidelines referenced in Section 5.2.
- Manages the enterprise vulnerability disclosure and bug bounty program.
- Owns the risk register and tracks all risk acceptances from the SSDLC.

**Director of Cloud Infrastructure:**
- Accountable for the security of all IaC and CI/CD pipeline infrastructure.
- Enforces separation-of-duties controls for production deployments (where technically feasible with documented compensating controls).

**Engineering Leads (per product team):**
- Responsible for the security outcomes of their product.
- Conduct threat modeling sessions within the first sprint of every new feature or significant enhancement.
- Ensure that developers on their team complete mandatory secure coding training (Section 9).
- Approve change requests in the deployment process per SOP-ITOP-004 (Change Management).

**Developers (All levels):**
- Execute secure coding practices and attend required annual training.
- Run SAST and SCA tools locally or via CI pre-commit hooks; remediate all Critical/High findings before code merge.
- Participate in code reviews with a security lens, utilizing review checklists (Appendix A).
- Report any observed security concerns to the Director of Information Security via the `infosec@meridianhlt.com` distribution list within 1 business day.

**Data Scientists / ML Engineers:**
- Responsible for the security and integrity of ML model training and serving pipelines.
- Ensure model serialization formats do not introduce deserialization vulnerabilities.
- Apply input validation and rate limiting to all model inference endpoints, consistent with API security standards.

**QA Engineers:**
- Execute security-focused test cases from the SSDLC Test Case Template (Appendix B).
- Validate that all security user stories and acceptance criteria have been met before the feature is marked "Done."

**Compliance Officer (Privacy & Regulatory):**
- Provides consultation during requirements gathering for HIPAA, EU AI Act, and cross-border data transfer implications.
- Conducts periodic audits of the SSDLC process to ensure adherence.
- Acts as the designated HIPAA Privacy Officer for any process-level PHI questions.

---

## 4. Policy Statements

The following policy statements represent the mandatory, high-level commitments that govern all software development at Meridian. Violations of these policies are handled under the Code of Conduct and may result in disciplinary action.

### 4.1 General Security Policies

- **SSDLC-001:** All software changes, including emergency hotfixes, must follow the prescribed phases of the SSDLC. No code may bypass the defined security gates.
- **SSDLC-002:** Security requirements must be explicitly documented in feature tickets (Jira, ADO) using the "Security Requirements" field or a dedicated child task. Product Managers and Engineering Leads are jointly responsible for verifying these are populated during sprint planning.
- **SSDLC-003:** All production-bound code must pass an automated SAST scan with zero Critical findings and zero High findings. Any false positives must be documented, triaged by the Security Architect, and annotated in the scan output.
- **SSDLC-004:** All third-party and open-source dependencies must be continuously scanned for known vulnerabilities using SCA tooling. Libraries with Critical CVEs (CVSS ≥ 9.0) that are exploitable in the deployment context must be patched or replaced before deployment.
- **SSDLC-005:** No production credentials, API keys, tokens, or secrets may be hardcoded in source code, configuration files, IaC templates, or documentation. All secrets must be managed via HashiCorp Vault (Meridian’s authorized secrets manager) and injected at runtime.
- **SSDLC-006:** All software artifacts—compiled binaries, Docker images, ML model packages—must be cryptographically signed using Cosign or equivalent tooling before being promoted to any production registry.
- **SSDLC-007:** Threat modeling must be conducted for all new products, for significant feature additions to existing products, and at least annually for all Tier-1 (business-critical) applications. The output must be documented as a Threat Model Document (TMD) using the Meridian Threat Modeling template (Appendix C).

### 4.2 HIPAA-Specific Security Policies

In accordance with the HIPAA Security Rule (45 CFR Part 164, Subpart C), the following specific commitments apply to all systems that create, receive, maintain, or transmit ePHI. All Meridian products operate under the assumption of containing ePHI unless formally classified otherwise by the Compliance Officer.

- **SSDLC-HIPAA-001 – Access Control (§164.312(a)(1)):** Every software component that accesses ePHI must implement technical access controls that enforce the principle of least privilege. Role-Based Access Control (RBAC) or Attribute-Based Access Control (ABAC) must be integrated into application logic. Each access request to ePHI must be evaluated against the requester’s authenticated identity and assigned roles. Access control decisions must be made at the API gateway layer (Apigee Edge) and at the individual microservice layer.
- **SSDLC-HIPAA-002 – Audit Controls (§164.312(b)):** All systems handling ePHI must produce tamper-resistant audit logs that capture: (1) the authenticated identity of the requester; (2) the exact type of data accessed (e.g., patient demographics, clinical notes, medication list); (3) the timestamp of access with NTP-synchronized accuracy; (4) the success or failure of the access attempt; and (5) the action taken (CREATE, READ, UPDATE, DELETE). These logs must be shipped to Meridian’s centralized SIEM (Splunk Cloud) within 60 seconds of the event, and retained for a minimum of six (6) years per HIPAA retention requirements (§164.316(b)(2)(i)).
- **SSDLC-HIPAA-003 – Integrity Controls (§164.312(c)(1)):** Electronic mechanisms must be implemented to corroborate that ePHI has not been altered or destroyed in an unauthorized manner. All ePHI-at-rest in databases and object stores must be protected with cryptographic hashing or digital signatures using SHA-256 or higher. Any unauthorized modification must be detectable via automated integrity checks run at least every 24 hours.
- **SSDLC-HIPAA-004 – Person or Entity Authentication (§164.312(d)):** Every software system must authenticate the identity of any person or entity seeking access to ePHI. Multi-Factor Authentication (MFA) enforced via Okta is mandatory for all human users accessing production systems. For machine-to-machine (service-to-service) communication, Mutual TLS (mTLS) with short-lived certificates (max 24-hour validity) issued by HashiCorp Vault’s PKI engine is required.
- **SSDLC-HIPAA-005 – Transmission Security (§164.312(e)(1)):** All ePHI transmitted over any network, including internal microservice meshes, must be encrypted in transit using TLS 1.2 or higher with strong cipher suites. In addition, internal service meshes (Istio) must be configured with mTLS to provide defense-in-depth against lateral movement. Exceptions for "internal-only, air-gapped" networks require written approval from the CISO and Compliance Officer.
- **SSDLC-HIPAA-006 – Encryption at Rest (Addressable, §164.312(a)(2)(iv)):** Meridian has implemented the addressable specification for encryption at rest as **mandatory**. All ePHI stored in databases (PostgreSQL RDS), object storage (AWS S3), and file systems (EBS volumes) must be encrypted using AES-256. Key Management Service (AWS KMS) keys must be rotated annually or upon any suspected compromise. Database Transparent Data Encryption (TDE) must be enabled for all production database instances.
- **SSDLC-HIPAA-007 – Emergency Access Procedure (§164.312(a)(2)(ii)):** All ePHI systems must be designed with a "break-glass" emergency access mechanism. This mechanism must allow a predefined, limited set of authorized personnel (e.g., on-call SRE, Incident Commander) to obtain temporary elevated access. Any invocation of this mechanism must generate a P1-priority alert to the Security Operations Center (SOC) and be reviewed forensically within 24 hours.

### 4.3 SOC 2 Trust Services Criteria Alignment

The SSDLC is the primary mechanism by which Meridian satisfies the SOC 2 Common Criteria for the Security, Availability, and Confidentiality trust service categories.

- **SSDLC-SOC2-001 – Change Management (CC8.1):** The authors of software changes are responsible for authoring the change, providing test evidence, and requesting a change approval. The designated approver (Engineering Lead) reviews the change request, including security test results, and either approves or rejects it. For changes to Tier-1 systems, a separate notification is sent to the Director of Information Security for post-approval visibility. This process ensures that all changes to production are documented and authorized but relies on the author's integrity for proper segregation.
- **SSDLC-SOC2-002 – Risk Mitigation (CC7.1-CC7.2):** The threat modeling and SAST/SCA scanning procedures described in Sections 5.2 and 5.3 are the primary risk mitigation processes used to identify, analyze, and respond to security and availability risks introduced by software.
- **SSDLC-SOC2-003 – Monitoring of Changes (CC7.3):** The deployment of software changes is monitored for anomalous behavior post-implementation. The Infrastructure and SRE teams use Datadog dashboards to observe error rates, latency, and system health. Deviations from baseline are investigated. Formal alert thresholds and defined escalation paths are currently managed through team-level operational runbooks.

---

## 5. Detailed Procedures

This section defines the mandatory operational sequence for the SSDLC. Each phase contains entry criteria, a step-by-step process, and exit criteria that must be met before the software artifact can progress to the next phase. The standard flow is: Requirements → Design → Development → Testing → Release → Operate → Decommission.

### 5.1 Requirements Phase (Phase 1)

**Entry Criteria:** A new product initiative, feature epic, or significant enhancement has been approved via the Product Investment Committee (PIC) process and is assigned to an Engineering team in Jira.

**Procedure:**

1. **Product Manager (PM)** creates the Epic-level Jira ticket and populates the "Business Requirements" and "Functional Requirements" sections of the Product Requirements Document (PRD) template.
2. **PM**, in consultation with the **Compliance Officer**, populates the "Regulatory Considerations" section of the PRD. If the feature touches ePHI or PII, this must be explicitly flagged. The specific HIPAA Security Rule provisions that apply are identified.
3. **PM** assigns a mandatory "Security Requirements" child task to the Epic. This task is owned by the **Engineering Lead** and the **Security Architect**.
4. **Engineering Lead & Security Architect** jointly author the security requirements, documenting them in the Security Requirements child task. At a minimum, they address:
   - **Authentication & Authorization Model:** How will users/services prove their identity? What access control paradigm (RBAC, ABAC) will be used?
   - **Data Classification:** Does this feature create, store, process, or transmit Confidential data (ePHI, PII, PCI, Credentials)? If yes, a Data Flow Diagram (DFD) must be initiated.
   - **Audit Logging Requirements:** What specific security-relevant events (access, modification, authN failure, privilege escalation) must be logged? What log schema is required?
   - **Encryption Requirements:** What data must be encrypted at rest and in transit? What key management is needed?
   - **Resilience/DoS Requirements:** What rate limiting, throttling, or input validation is required to maintain availability?
   - **Privacy Requirements:** If processing personal data, what data minimization or anonymization is required per GDPR/CCPA guidelines as applicable?
5. **Security Architect** performs a preliminary risk assessment and assigns an initial "Security Impact Rating" to the feature: **Low**, **Moderate**, or **High**.
   - **Low:** Minor UI changes, no Confidential data touched, standard security features apply.
   - **Moderate:** New microservice, significant refactor, touches Confidential data.
   - **High:** New product boundary, handles ePHI, processes financial transactions, AI/ML model serving endpoint publicly exposed.
6. **Exit Criteria:** The PRD exists in Confluence and is linked to the Jira Epic. The "Regulatory Considerations" section is completed. The Jira "Security Requirements" child task is created and has initial content. The Security Impact Rating is recorded on the Epic.

---

### 5.2 Design Phase (Phase 2)

**Entry Criteria:** The Jira Epic has an assigned "Security Impact Rating" of Moderate or High. For Low-impact features, a streamlined design discussion may occur within the development sprint, but a formal Threat Model Document (TMD) is not required.

**Procedure for Moderate/High Impact Features:**

#### 5.2.1 Architectural Design Review
1. **Engineering Lead** schedules a 1-hour "Security Architecture Review" (SAR) meeting. Required attendees: Engineering Lead, Security Architect, relevant Developers, Cloud Infrastructure representative. Optional: Compliance Officer, Product Manager.
2. Before the meeting, the **Engineering Lead** posts the technical design document (which includes the context diagram and DFD) to the `#eng-security-reviews` Slack channel at least 48 hours in advance.
3. During the SAR meeting, the **Security Architect** facilitates a walkthrough of the system architecture, focusing on trust boundaries, authentication flows, data stores with ePHI, and external integrations. Specific attention is paid to the HIPAA controls identified in Section 4.2.
4. Decisions and action items from the SAR are documented in the Confluence meeting notes.

#### 5.2.2 Threat Modeling
1. Following the SAR, the **Engineering Lead** and **Security Architect** facilitate a formal threat modeling workshop using the **STRIDE** methodology. Threat modeling is conducted per Meridian SOP-RISK-001 (Risk Assessment Framework).
2. The output is a **Threat Model Document (TMD)** that contains:
   - **A Data Flow Diagram (DFD)** at Level 1 or Level 2, clearly delineating trust boundaries.
   - **A Threat Library Table** enumerating each identified threat with:
     - STRIDE category (e.g., Tampering, Information Disclosure).
     - Affected component.
     - Threat description.
     - Inherent risk (Likelihood x Impact using the Meridian 5x5 Risk Matrix).
     - Planned mitigation(s) / compensating controls.
     - Residual risk after mitigation.
   - **An Abuser Story list** capturing "misuse cases" in a format consumable by QA (e.g., "As an attacker, I want to brute-force the login API so I can gain unauthorized access").
3. The TMD must be reviewed and approved by the **Security Architect** before the development team may begin coding any Moderate or High impact component.

#### 5.2.3 Secure Design Review Checklist
The Engineering Lead must complete the following checklist as part of the final design review and attach it to the Epic.

| # | Check | Yes/No/NA | Supporting Artifact |
|---|---|---|---|
| D1 | Least Privilege access principles applied for all service accounts and users | | |
| D2 | All PHI/ePHI data stores identified on a DFD and encrypted at rest (AES-256) | | |
| D3 | mTLS configured for all inter-service communication paths | | |
| D4 | Secrets management strategy documented (HashiCorp Vault) — no hardcoded secrets | | |
| D5 | Input validation strategy defined for all external-facing APIs (allowlists, parameterized queries, etc.) | | |
| D6 | Output encoding strategy defined to prevent XSS (CSP headers, context-sensitive encoding) | | |
| D7 | Session management strategy defined with secure attributes (HTTPOnly, Secure, SameSite=Strict) | | |
| D8 | API authentication scheme documented (OAuth2.0/OIDC with Okta) | | |
| D9 | Rate-limiting and DoS protection strategy defined | | |
| D10 | Logging requirements for PHI access auditable events defined | | |

**Exit Criteria:** For Moderate/High features: SAR meeting notes are published. A TMD exists and is approved. The Design Review Checklist is completed and attached to the Epic. For Low features: a brief design note exists in the development task describing the security approach.

---

### 5.3 Development Phase (Phase 3)

**Entry Criteria:** Approved TMD (if required), completed Design Review Checklist. Developer workstations are configured as per Meridian endpoint security standards (SOP-ITOP-002).

**Procedure:**

#### 5.3.1 Secure Coding Practices
1. All Developers must adhere to the **Meridian Secure Coding Standards** (maintained in an internal Confluence space by the CISO and Security Architect). These standards are language-specific and include rules for:
   - **Java/Spring Boot:** OWASP Java Encoder for output encoding, parameterized SQL queries (no string concatenation), Spring Security configuration, CSRF token handling.
   - **Python/FastAPI:** Dependency injection for DB calls, Pydantic model validation for inputs, defusedxml for XML parsing, bandit ruleset integration into VSCode.
   - **JavaScript/React:** DOMPurify for HTML sanitization, Helmet.js for security headers, npm audit integration.
   - **IaC (Terraform/CloudFormation):** checkov/compliance scans for S3 Public Access Blocks, KMS key rotation, security group egress restrictions, IAM admin role restrictions.
2. **Developer IDE Configuration:** All developers must have the following IDE plugins installed and active:
   - **SonarLint** (on-the-fly code quality and security analysis).
   - **Snyk Advisor** (for open-source vulnerability insights in `package.json`/`pom.xml`/`requirements.txt`/`go.mod`).
   - **TruffleHog** (git secret scanning pre-commit hook — mandatory, installed via .gitconfig).

#### 5.3.2 Source Code Management
1. All source code is managed in Meridian's GitHub Enterprise Cloud organization (`meridianhlt`).
2. **Branch Protection Rules** are enforced on all production-bound branches (e.g., `main`, `master`, `release/*`):
   - Require a pull request (PR) with at least **one** approving review from a peer developer.
   - Require status checks to pass: `SAST (CodeQL)`, `SCA (Snyk)`, `IaC Scan (checkov)`, `Unit Tests (Jest/Pytest)`.
   - Require the PR author to be different from the PR merger for changes to Tier-1 production services; for other services, this is recommended but not enforced.
   - Require signed commits (GPG or S/MIME).
   - Dismiss stale reviews when new commits are pushed.
3. **Code Review for Security:** All PRs must include a security review. Reviewers utilize the "Security Code Review Checklist" (Appendix A). For High-impact features, the Security Architect must be added as a mandatory reviewer.

#### 5.3.3 Automated Security Scanning (CI Pipeline)
The following gates are executed in the CI pipeline (GitHub Actions) on every commit to a PR and on merges to the main branch. The pipeline configuration is managed in the shared `.github/workflows/` repository.

1. **SAST (CodeQL):**
   - **Tool:** GitHub CodeQL, with the "Extended" and "Security-and-Quality" query packs enabled.
   - **Action:** The `github/codeql-action/analyze` action runs a full analysis.
   - **Failure Condition:** The pipeline **fails** if any CodeQL finding is classified as "error" (Critical or High severity). A SARIF output is generated and uploaded as a pipeline artifact.
2. **SCA (Snyk):**
   - **Tool:** Snyk Open Source.
   - **Action:** `snyk test` is run against the project manifest.
   - **Failure Condition:** The pipeline **fails** if any vulnerability is detected with a CVSS score >= 9.0 (Critical) and there is an available fix ("Fixable" state). High-severity findings (7.0-8.9) result in a pipeline **warning** status, and a Jira task is automatically created for remediation within 30 days.
3. **IaC Scanning (checkov / tfsec):**
   - **Tool:** checkov for Terraform/CloudFormation, with the `CKV_AWS_*` and `CKV_AZURE_*` checkset.
   - **Action:** `checkov -d .` runs on all IaC directories.
   - **Failure Condition:** The pipeline **fails** on any finding configured with a severity of `CRITICAL` or `HIGH` in the checkov enterprise configuration policy. This includes public S3 buckets, unencrypted EBS volumes, and overly permissive IAM roles.
4. **Secret Scanning (TruffleHog + GitHub Secret Scanning):**
   - **Tool:** TruffleHog V3 (pre-receive hook) and GitHub Secret Scanning.
   - **Action:** Scans all commits in a push for high-entropy strings and known secret patterns.
   - **Failure Condition:** The pipeline **fails** if any secret is detected. The developer must invalidate the secret immediately via Vault and rewrite git history to scrub it before the PR can be merged.

**Exit Criteria:** The PR is approved, all required CI status checks pass, and for Moderate/High features, the Security Architect's review is approved.

---

### 5.4 Testing Phase (Phase 4)

**Entry Criteria:** All development-phase code has been merged into the `integration` or `staging` branch. The deployment to the `staging` environment is successful.

**Procedure:**

#### 5.4.1 Functional Security Testing
QA Engineers execute test cases, including specific "Abuser Stories" derived from the TMD (for applicable features). These are tagged with `@security` in the Test Management System (TestRail). Test cases include:

- **Authentication Bypass:** Attempt to access protected endpoints without a valid Bearer token.
- **Authorization Bypass (IDOR):** A Role A user attempts to access or modify a resource belonging to a Role B user or organization by guessing or manipulating resource IDs (e.g., `/api/v1/patient/{uuid}`).
- **Injection Attack (SQLi, NoSQLi):** Submit malicious payloads (`' OR '1'='1`, `$gt: ''`) to API endpoints and form fields.
- **Injection Attack (XSS):** Submit stored and reflected XSS payloads into input fields and verify CSP headers and output encoding prevent execution.
- **Rate Limiting:** Exceed the configured API rate limit and confirm a `429` (Too Many Requests) status is returned, and the appropriate security event is logged.
- **File Upload Security:** Attempt to upload malicious file types (`.exe`, `.jsp`, `.php`, files with double extensions like `malicious.pdf.exe`) and verify they are rejected or sanitized.

#### 5.4.2 Dynamic Application Security Testing (DAST)
1. The **Security Architect** schedules an automated DAST scan against the `staging` environment instance(s) using **OWASP ZAP** configured in headless CI mode.
2. The ZAP scan is configured to:
   - Spider the application using the authenticated user context with a QA-provided "User" role credential.
   - Run the active scanning ruleset for High and Critical confidence findings. Passive scans are run on every build.
3. **Analysis & Remediation:**
   - The ZAP report (XML and HTML) is published as a CI artifact.
   - The **QA Engineer** and **Security Architect** triage the report. Any **High** or **Critical** severity finding confirmed as a true positive **blocks the release**. Medium-severity findings are tracked as defects to be resolved in the next planned release.

#### 5.4.3 Penetration Testing (Mandatory Annual or Triggered)
1. An external, CREST-accredited penetration testing vendor is engaged annually to perform a comprehensive test of all Tier-1 production applications.
2. A "pen-test triggered" event occurs when a new, externally-facing Tier-1 application or major API boundary is released. The **Director of Information Security** determines if the change warrants an ad-hoc test.
3. Findings are managed through the vulnerability management process (SOP-ITOP-005).

**Exit Criteria:** All `@security` QA test cases pass. The ZAP DAST report contains zero Critical and zero High true-positive findings. The Penetration Test report (if applicable) contains zero Critical unmitigated findings.

---

### 5.5 Release / Deployment Phase (Phase 5)

**Entry Criteria:** All Phase 4 testing gates are green. An approved Change Request (CR) exists in the ITSM system (ServiceNow). The artifact to be deployed has been cryptographically signed.

**Procedure:**

1. **Change Request Creation:** The **Engineering Lead** or designated **DevOps Engineer** creates a Standard Change Request in ServiceNow, providing:
   - Description of the change.
   - The Jira Epic/Issue IDs being released.
   - Rollback plan and estimated rollback time.
   - Evidence of all SSDLC gate approvals (links to passing CI pipeline runs, TMD approval, DRC checklist, QA sign-off, ZAP report).
2. **Change Approval:** The Change Request is routed for approval. The approver for the Engineering team (Engineering Lead) reviews the provided evidence and approves the change. For Tier-1 services, the Director of Cloud Infrastructure is also notified of the pending change.
3. **Production Deployment:** The approved release is executed via the CI/CD pipeline (GitHub Actions → ArgoCD for Kubernetes or CodeDeploy for EC2/ECS). The deployment strategy (Blue/Green, Rolling, or Canary) is specified in the service's deployment manifest.
4. **Smoke Test / Canary Analysis:** Immediately after deployment, the **DevOps Engineer** performs a production smoke test against a health-check endpoint. Monitoring dashboards (Datadog) are actively observed for 15 minutes for any anomaly (spike in 5xx errors, latency increase >20%, sudden drop in traffic).
5. **Failed Deployment & Rollback:** If the smoke test fails or a critical anomaly is detected, the **DevOps Engineer** initiates the rollback plan documented in the Change Request. The rollback must be executed via the CI/CD pipeline's rollback command. A post-mortem is scheduled per Meridian incident response SOP (SOP-ITOP-001).

**Exit Criteria:** The deployment is successful. Production monitoring shows nominal health. The Change Request is closed in ServiceNow.

---

### 5.6 Operations / Post-Deployment Phase (Phase 6)

**Entry Criteria:** A production system is running.

**Procedure:**

1. **Continuous Vulnerability Scanning:** All production container images and running infrastructure are continuously scanned by Meridian's cloud security posture management (CSPM) platform (Wiz).
   - **Container Vulnerabilities:** Newly discovered Critical or High CVEs in running images generate an automatic ticket in the Engineering team's backlog. The SLA for remediation is per the table below.
   - **Misconfigurations:** Wiz detects configuration drift from the approved IaC baseline (e.g., an S3 bucket policy made less restrictive by a manual change). An alert is sent to the `#cloud-security-alerts` Slack channel.
2. **Dependency Monitoring:** Snyk monitors all deployed application manifests and notifies the owning Engineering Lead of newly published Critical CVEs in dependencies.
3. **Vulnerability Remediation SLA:**

| CVE Severity (CVSS v3.1) | Internal Remediation SLA (from notification) | Regulatory Overlay (if ePHI system) |
|---|---|---|
| Critical (9.0-10.0) | **72 hours** | 48 hours, plus HIPAA incident report consideration per §164.308(a)(6) |
| High (7.0-8.9) | **14 calendar days** | 7 calendar days |
| Medium (4.0-6.9) | **30 calendar days** | 21 calendar days |
| Low (0.1-3.9) | **90 calendar days** | Best effort — next planned release |

4. **Bug Bounty / VDP:** Meridian operates a Vulnerability Disclosure Program (VDP) managed by the CISO’s office. Valid reports from external researchers are triaged and injected into the SSDLC at Phase 5 (as a blocker) or Phase 6 (as a vulnerability ticket) based on the affected component's position in the lifecycle.

**Exit Criteria:** The system is decommissioned (Phase 7).

---

### 5.7 Decommissioning Phase (Phase 7)

**Procedure:**

1. **Data Sanitization:** Before an ePHI-storing system is decommissioned, a Data Sanitization Plan is authored by the Engineering Lead and approved by the Compliance Officer, ensuring alignment with NIST SP 800-88 Rev. 1 guidelines for media sanitization (for the cloud, this is cryptographic erasure of the KMS key or an AWS-native wipe procedure).
2. **Artifact Archival:** The final source code tag, SBOM, container image, IaC snapshot, and monitoring logs are archived in an immutable, read-only AWS S3 bucket (`meridian-compliance-archive`) with a retention period of six (6) years.
3. **Configuration Clean-up:** All DNS records, load balancer configurations, firewall rules, and identity provider (Okta) application registrations related to the system are removed from the live configuration.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

- **Background Checks:** All personnel with access to Meridian source code repositories and production systems undergo background verification as a condition of employment per SOP-HR-001.
- **Confidentiality Agreements:** All employees, contractors, and interns sign an Intellectual Property and Confidentiality Agreement (IPCA) upon their start date. The IPCA explicitly covers the security and confidentiality of software code, designs, and security documentation.
- **Disciplinary Process:** Non-compliance with this SOP is subject to progressive disciplinary action, up to and including termination of employment and/or contract, in accordance with Meridian’s Employee Handbook.

### 6.2 Technical Controls

- **Integrated Development Environment (IDE) Controls:** Developer workstations are managed via Jamf and enforce disk encryption, screen lock timeout, and mandatory installation of approved security plugins.
- **Version Control System (VCS) Controls:** Branch protection rules enforced on GitHub Enterprise Cloud (detailed in Section 5.3.2). All pushes are via SSH or HTTPS with PAT.
- **CI/CD Pipeline Security:** Pipeline definitions are stored in a separate, restricted repository. Secrets used by pipelines are stored in HashiCorp Vault and injected ephemerally using the Vault-Action GitHub Action.
- **Artifact Registry & Signing:** All container images are stored in the Meridian Private ECR Gallery. Image signing is performed with Cosign keys stored in KMS. Meridian’s container admission controller (Conaisseur) enforces that only signed images from the Meridian ECR can be scheduled on production nodes.

### 6.3 Physical and Environmental Controls
(No physical controls are applicable to the SaaS development process itself; these are addressed in SOP-FAC-001 for Meridian office locations, which are not data centers.)

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Monitoring
The effectiveness of the SSDLC is continuously monitored via automated dashboards (Grafana, sourced from Datadog and Snyk APIs) and manual control audits. The Security Operations Center (SOC) monitors the SIEM (Splunk) for any security events related to the CI/CD pipeline (e.g., unauthorized admin access, secret leakage alerts).

### 7.2 Key Performance Indicators (KPIs) and Service Level Objectives (SLOs)

These metrics are measured monthly and reported to the Engineering Leadership Team. The Director of Information Security (CISO) is accountable for the accuracy and timeliness of the report.

| # | Metric / KPI | Target / SLO | Measurement Method | Owner |
|---|---|---|---|---|
| K1 | **Critical/High SAST findings at merge** | 0 | CodeQL Dashboard | CISO |
| K2 | **Mean Time to Remediate (MTTR) Critical CVE in running images** | ≤ 72 hours | Wiz / ServiceNow report | CISO |
| K3 | **Mean Time to Remediate (MTTR) High CVE in running images** | ≤ 14 days | Wiz / ServiceNow report | CISO |
| K4 | **Threat Model Coverage (% of Tier-1 apps with TMD <12 m/o)** | 100% | Manual audit of TMD registry | VP of Engineering |
| K5 | **Secure Code Review Compliance (% of PRs with security checklist)** | 95% | GitHub API report | Engineering Leads |
| K6 | **Time from Code-Commit to Prod (Lead Time for Changes)** | N/A (Tracking only) | Jenkins / GitHub Actions | Director of Platform |
| K7 | **Percentage of releases requiring rollback** | < 5% of all releases | ServiceNow | Director of Platform |

### 7.3 Reporting Cadence

- **Operational Dashboards:** Datadog/Grafana dashboards are real-time and available 24/7 to Engineering and Operations teams.
- **Monthly SSDLC KPI Report:** Compiled by the CISO’s office and distributed to the VP of Engineering and all Engineering Leads. Highlights KPIs K1-K7, exception status, and any open critical vulnerabilities beyond SLA.
- **Quarterly Executive Risk Report:** A consolidated report containing the monthly SSDLC KPIs, a summary of open risk acceptances, and a forecast of upcoming High-Impact features is presented by the VP of Engineering to the CEO and the Executive Risk Committee.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types and Tiers
Deviations from the mandatory procedures or policies defined in this SOP must be handled through the formal exception process. Violations without an approved exception constitute a policy violation.

| Tier | Definition | Approval Authority | Max Validity Period |
|---|---|---|---|
| **Tier 1** | Minor procedural deviation (e.g., missing document link, training completed 1 day late). No direct risk to data confidentiality or integrity. | Engineering Lead | 30 days, non-renewable |
| **Tier 2** | Temporary deviation from a security gate (e.g., emergency hotfix bypassing DAST scan), deployment with a known High CVE with a documented compensating control. | Director of Information Security & VP of Engineering | 90 days, renewable once upon detailed re-review |
| **Tier 3** | Exception to a core policy statement (e.g., deploying a system handling ePHI without TLS 1.2 for a legacy integration). Represents a material risk. | CEO (Dr. Sarah Chen), upon recommendation of CISO and Compliance Officer | 180 days, renewable once with CEO approval |

### 8.2 Exception Process
1. **Submission:** The requestor completes the "SSDLC Exception Request" form in ServiceNow. For Tier 2 and Tier 3, this must include:
   - The specific SOP section or policy statement from which deviation is sought.
   - The technical or business justification.
   - A risk assessment describing the inherent risk and any compensating controls to be put in place.
   - A remediation plan with a target date for eliminating the deviation.
2. **Review:** The Security Architect reviews the request and makes a recommendation to the approval authority.
3. **Approval/Rejection:** The approval authority approves or rejects the request.
4. **Tracking:** All approved exceptions are logged in the Meridian Risk Register managed by the CISO. Their expiration date is tracked, and the requestor is automatically notified 14 days and 7 days before expiry.

### 8.3 Escalation Path
If an issue cannot be resolved or an exception cannot be approved at the current Tier level:
- The developer escalates to their **Engineering Lead**.
- The Engineering Lead escalates to the **Security Architect** and **VP of Engineering**.
- The VP of Engineering escalates to the **CEO** and the **Executive Risk Committee**.

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Role | Required Training(s) | Frequency | Delivery Method | Tracking |
|---|---|---|---|---|
| **All Developers (incl. Data Scientists, QA)** | Meridian Secure Coding Standards (by language) | Annually | LMS (WorkRamp) + Live lab via Secure Code Warrior platform | HR system (Workday) |
| **All Developers** | OWASP Top 10 Awareness (2024 edition) | Annually | LMS (WorkRamp) | Workday |
| **All Engineering Leads & Architects** | Threat Modeling with STRIDE | Every 24 months | Instructor-led Workshop (2-day) | Confluence certification register |
| **DevOps & SRE Engineers** | Secure CI/CD Pipeline Management & IaC security | Annually | LMS (WorkRamp) + Practical exam | Workday |
| **All New Hires (Engineering)** | SOP-PENG-001 SSDLC Onboarding Module | Once, within first 10 business days | LMS (WorkRamp) | Workday |
| **HIPAA-Regulated System Personnel** | HIPAA for Engineers (Privacy & Security Rule) | Annually | LMS (WorkRamp) | Workday |
| **All Engineering Personnel** | Reporting a Security Incident (SOP-ITOP-001) | Annually | LMS (WorkRamp) | Workday |

### 9.2 Training Compliance and Consequences
- **New Hire Compliance:** Completion of the SSDLC Onboarding Module is a condition of the probationary period.
- **Annual Training Compliance:** All annual training must be completed by the end of Q4 (December 31st). The compliance rate is reported to management in January. Employees who have not completed mandatory training by the deadline will have their access to source code repositories temporarily suspended until completion is verified by their manager and the CISO's office.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| `SOP-ITOP-001` | Security Incident Response Plan | Defines the process invoked by security events from CI/CD or production monitoring |
| `SOP-ITOP-002` | Endpoint Security Standards | Mandates the secure configuration of developer workstations |
| `SOP-ITOP-004` | Change Management Policy | Defines the overall change management authority and categories this SOP plugs into |
| `SOP-ITOP-005` | Vulnerability Management Program | Governs the lifecycle of identified vulnerabilities, fed from SSDLC scanning |
| `SOP-RISK-001` | Risk Assessment Framework | Contains the Meridian Risk Matrix and the formal Threat Model Document template |
| `SOP-CMPL-001` | HIPAA Privacy and Security Compliance | Defines the overarching HIPAA program under which this SOP operates |
| `SOP-DATA-001` | Data Classification and Handling | Defines the formal data classification scheme (Public, Internal, Confidential, Restricted) |
| `SOP-ML-001` | Machine Learning Model Lifecycle | Specifics for ML model training, evaluation, and serving which must also follow this SSDLC |

### 10.2 External Standards and Frameworks

- NIST Special Publication 800-53, Revision 5: "Security and Privacy Controls for Information Systems and Organizations."
- NIST Special Publication 800-88, Revision 1: "Guidelines for Media Sanitization."
- OWASP Top 10 (2024): Web Application Security Risks.
- OWASP Top 10 for Large Language Model Applications (2025).
- OWASP Application Security Verification Standard (ASVS) 4.0.3, Level 2.
- MITRE ATT&CK Framework (Enterprise).

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
|---|---|---|---|
| 1.0 | 2023-10-10 | Jane Smith (CISO) | Initial release. Established base SSDLC framework, HIPAA controls, and CI/CD security gates. |
| 1.1 | 2024-04-15 | David Park, VP of Engineering | Revised Section 5.3 to mandate CodeQL. Expanded Section 9 (Training) to include Secure Code Warrior platform. Updated RACI matrix in Section 3. |
| 1.2 | 2024-09-20 | Alex Kim, Security Architect | Incorporated ML model development into scope (Section 1.2). Added IaC scanning gate to Section 5.3.3. Updated Section 7 KPIs to add MTTR for CVEs. |
| 1.3 | 2025-04-19 | David Park, VP of Engineering | Major revision. Updated External Standards to 2024/2025 OWASP editions. Added Artifact Signing policy (SSDLC-006). Refined DRC checklist in Section 5.2.3. Clarified Change Management flow for SOC 2 CC8.1 alignment. Updated HIPAA references for audit logging retention period. |
| 1.4 | *Draft* | TBD | Planned integration of formal SBOM generation (CycloneDX format) into CI phase per FDA/EU MDR requirements. Refinement of AI/ML threat model templates. |

---

**Appendix A: Security Code Review Checklist** *(Referenced in Section 5.3.2)*

**For Every PR:**
- [ ] **Secrets Check:** Ensure no hardcoded credentials, API keys, or connection strings.
- [ ] **Input Validation:** Is all external input (query params, body, headers) validated against an allowlist?
- [ ] **Output Encoding:** Is output contextually encoded (HTML, JS, URL) to prevent XSS?
- [ ] **SQL Queries:** Are all DB queries parameterized? (No string concatenation).
- [ ] **Error Handling:** Do error messages reveal stack traces or sensitive system info in the response?
- [ ] **Logging:** Are sensitive data (ePHI, PII, auth tokens) correctly masked in log statements?

**For ePHI/High-Impact Features:**
- [ ] **Authentication:** Is the endpoint protected with a valid OAuth2.0 scope?
- [ ] **Authorization:** Is access verified against the requested resource’s ownership? (IDOR check).
- [ ] **Audit Log:** Is an audit log event generated for every Create, Read, Update, and Delete of ePHI? Does it follow the Meridian Audit Log Schema?