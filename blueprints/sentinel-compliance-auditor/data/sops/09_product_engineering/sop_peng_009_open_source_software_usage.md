---
sop_id: "SOP-PENG-009"
title: "Open Source Software Usage"
business_unit: "Product & Engineering"
version: "2.5"
effective_date: "2024-02-13"
last_reviewed: "2025-11-07"
next_review: "2026-05-21"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Open Source Software Usage

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide governance framework for the evaluation, approval, usage, contribution, and lifecycle management of Open Source Software (OSS) within Meridian Health Technologies, Inc. The purpose of this framework is to enable the strategic and secure use of OSS to accelerate product development and innovation while ensuring compliance with applicable licenses, minimizing security and operational risk, and protecting Meridian's proprietary intellectual property and the sensitive data entrusted to us by our customers and patients.

This SOP operationalizes the legal, security, and quality standards necessary to ensure that OSS components introduced into our software supply chain—particularly within our high-risk AI systems, payment platforms, and data analytics pipelines—do not introduce unacceptable legal or technical vulnerabilities.

### 1.2 Scope

This SOP applies to all OSS activities across all business units, including Product & Engineering, MedInsight Analytics, and HealthPay Financial Services. The scope encompasses:

- **All OSS Components:** Any software licensed under an Open Source Initiative (OSI)-approved license, incorporated into any Meridian product, service, platform, internal tool, infrastructure-as-code (IaC) template, or research prototype, regardless of whether it is used in development, testing, staging, or production environments.
- **All Integration Methods:** OSS integrated as a direct dependency, transitive dependency, static or dynamic-linked library, operating system package, container base image, copied source code snippet, or any other form of inclusion.
- **All Contribution Activities:** Any contribution of Meridian-developed code, documentation, or resources to an external OSS project, including bug fixes, feature enhancements, and financial sponsorship, made under the Meridian brand or by Meridian personnel.
- **All Business Units:** This SOP applies uniformly to all business units at Meridian, including but not limited to Clinical AI, Cloud Platform, HealthPay Engineering, and Data Analytics.

This Framework is subordinate to the Meridian Code of Conduct and the Master Information Security Policy (SOP-ISEC-001).

---

## 3. Roles and Responsibilities

The following RACI matrix defines the key roles and their responsibilities within the OSS governance lifecycle.

| Role | Responsibility Matrix | Description |
|---|---|---|
| **Chief Executive Officer (CEO) / Dr. Sarah Chen** | **A** (Accountable) | Holds ultimate accountability for the Information Security Program. Approves this Framework and any high-risk exceptions as escalated by the VP of Engineering or CISO. |
| **VP of Engineering / David Park** | **R, A** (Responsible, Accountable) | Process Owner. Accountable for the effective operation of this Framework, including the OSS approval tooling, SBOM generation, and the OSS Contribution Review Board. Approves OSS components for use in production systems. |
| **Chief Information Security Officer (CISO) / [Named Role]** | **C, A** (Consulted, Accountable) | Accountable for the vulnerability management and threat detection aspects of the Framework. Consulted on all security-impacting OSS components and contributions. |
| **General Counsel / [Named Role]** | **C** (Consulted)** | Consulted on the legal interpretation of all novel, unconventional, or Copyleft OSS licenses before component approval. Final legal arbiter for license compliance. |
| **OSS Review Board (OSRB)** | **R, A** (Responsible, Accountable) | A cross-functional standing body comprising senior engineers, a security architect, and a representative from Legal. Responsible for the final approval of all non-standard OSS licenses and all external contributions. |
| **Principal Engineers / Architecture Team** | **R, C** (Responsible, Consulted) | Responsible for maintaining the Approved OSS Catalog (Appendix B) by continuously reviewing and approving standard, permissive-licensed components. Consulted on architectural impact of new OSS. |
| **Engineering Managers** | **R** (Responsible) | Responsible for ensuring their teams complete the OSS Request Form (Appendix A) accurately and adhere to approved licenses. |
| **All Engineers & Developers** | **I** (Informed) | Responsible for being informed of policy requirements and procedures. Must submit all OSS requests through the designated tooling and must not introduce unapproved OSS into the codebase. |

---

## 4. Policy Statements

Meridian Health Technologies is committed to the following high-level policy statements that govern the use of Open Source Software:

### 4.1 License Compliance

All OSS used within Meridian products or infrastructure must be governed by a valid, identifiable, and OSI-approved license. The legal obligations of every OSS license in use must be understood and met. No OSS component may be used in a manner that imposes obligations on Meridian proprietary code beyond those explicitly accepted through the formal approval process defined in Section 5. The use of components with no discernible license, or with "public domain" dedications that are not legally robust in all required jurisdictions, is prohibited.

### 4.2 Security and Risk Management

OSS shall not introduce unacceptable security risk to Meridian or its customers. All OSS components must undergo automated vulnerability scanning prior to approval and continuously thereafter as part of the CI/CD pipeline. The use of OSS components with unpatched critical- or high-severity vulnerabilities is prohibited unless a specific, time-bound exception is granted by the VP of Engineering and CISO under the controls defined in Section 8.

### 4.3 Supply Chain Integrity and SBOM

Every Meridian-managed microservice, application, and distributable software artifact must have a corresponding, machine-readable Software Bill of Materials (SBOM) that fully enumerates all OSS components and their transitive dependencies. The SBOM must be generated at build time, signed, and stored in an immutable repository. SBOM data, including component name, version, declared license, and supplier, must be available for automated ingestion by vulnerability management and compliance tooling.

### 4.4 Operational Excellence

OSS components must be actively maintained and sourced from reputable, responsive upstream communities or foundations. Components that are unmaintained, deprecated, or have reached End-of-Life (EOL) must be replaced or internally maintained. All OSS usage must be tracked in the Meridian Configuration Management Database (CMDB). Contributions back to OSS projects are encouraged but must be approved and done in alignment with Meridian's intellectual property and brand strategy.

---

## 5. Detailed Procedures

This section details the step-by-step operational procedures for the lifecycle of OSS within Meridian.

### 5.1 OSS Consumption Request and Approval

This procedure applies to any Meridian personnel wishing to introduce a new OSS component, or a new version of an OSS component with a materially changed license, into a Meridian product.

**Step 1: Discovery and Identification**
The Requestor (typically an Engineer) identifies a candidate OSS component. The Requestor must gather the following information:
- Component Name and Version
- Upstream Project URL (e.g., GitHub repository, project website)
- Declared License(s) (SPDX Identifier, e.g., MIT, Apache-2.0, GPL-3.0-only)
- Reason for Use: A brief technical justification for why this component is needed versus an existing approved alternative.

**Step 2: Initiate Request in `oss.aragon.meridian.com`**
The Requestor logs in via Okta SSO and submits the formal "OSS Component Request" form (digitally equivalent to Appendix A). The form auto-populates key data from the specified package registry (e.g., npm, PyPI, Maven Central) or SBOM ingestion.

**Step 3: Automated and Manual Review**
The request triggers the following automated checks within one (1) hour:
- **License Check:** `FOSSA` engine analyzes the full dependency tree for license compliance against the Meridian License Compliance Matrix (Appendix C). A flag is raised for any License Category 3 (Restrictive Copyleft) or 4 (Prohibited) license.
- **Vulnerability Scan:** `Wiz` and `Snyk` perform an immediate scan for known vulnerabilities (CVEs). A flag is raised if the component has any Critical or High severity CVE without an available, compatible patched version.
- **Project Health Score:** `FOSSA` calculates a project health score based on community activity, frequency of releases, and responsiveness to security issues.

**Step 4: Approver Decision**
Based on the automated checks:
- **Auto-Approval:** Components with a Category 1 (Permissive) license, zero Critical/High CVEs, and a high project health score are automatically approved by the system and added to the Approved OSS Catalog. The Requestor receives a notification.
- **Manual Review Required (OSRB):** For components flagged in Step 3, or any request for a Category 2 (Limited Copyleft) license, the request is routed to the OSRB queue for the next scheduled review. Reviews occur bi-weekly on Tuesday and Thursday. A Principal Engineer and, if the license flag requires, the General Counsel, reviews the request. They approve, approve with conditions (e.g., a specific upgrade timeline), or reject the request.

### 5.2 Vulnerability Remediation and Patch Management

**Step 1: Vulnerability Alert Generation**
`Wiz` and `Snyk` continuously monitor the production and staging Kubernetes (EKS) clusters and container registries (ECR). Upon detection of a new Critical or High CVE that affects a deployed OSS component, the system automatically generates an Incident Ticket in `PagerDuty` and assigns it to the owning service team.

- **Service Level Agreement (SLA) for Remediation:**
  - **Critical Severity (CVSS >= 9.0):** Triage initiated within **4 hours**. Patched version must be deployed to production, or a compensating control (e.g., Web Application Firewall rule, network isolation) validated by the CISO, within **7 calendar days**.
  - **High Severity (CVSS 7.0 - 8.9):** Triage initiated within **24 hours**. Remediation deployed within **30 calendar days**.
  - **Medium Severity (CVSS 4.0 - 6.9):** Remediation planned in the next sprint cycle, not to exceed **90 calendar days**.
  - **Low Severity (CVSS < 4.0):** Remediation at the service team's discretion, tracked within the central vulnerability management backlog.

**Step 2: Remediation and Verification**
The assigned Engineering Manager ensures a patched version of the component is identified and integrated. The fix is tested and deployed through the standard CI/CD pipeline. The automated vulnerability scanner re-scans the environment to verify remediation. Successful remediation is noted on the Incident Ticket, and the ticket is closed.

### 5.3 OSS Contribution (Outbound) Process

Any Meridian employee wishing to contribute code, documentation, or other resources to an external OSS project must obtain prior approval.

**Step 1: Contribution Proposal**
The Contributor (Meridian employee) drafts a Contribution Proposal. This proposal must state the target project, the license it uses, the nature of the change (e.g., a bug fix for a critical production issue, a new feature for a community tool), and a declaration of any Meridian-proprietary code or logic that might be inadvertently included.

**Step 2: Submission to OSRB**
The Contributor submits the proposal through the `oss.aragon.meridian.com` portal. This triggers a review by the OSRB.

**Step 3: OSRB Review and CEO Approval**
The OSRB reviews the proposal for IP contamination risk, security best practices, and strategic alignment. For any proposed contribution that is not a trivial bug fix (i.e., fewer than 20 lines of configuration or documentation), the OSRB's approval recommendation is forwarded to the CEO (Dr. Sarah Chen) for final written approval. An approved Individual Contributor License Agreement (CLA) or Corporate CLA must be on file for the target project from the General Counsel.

### 5.4 SBOM Generation and Management

**Step 1: Build-Time Generation**
Every production-bound CI/CD pipeline (e.g., `Jenkinsfile` or `.github/workflows`) must include a mandatory stage that invokes the `Syft` tool to generate an SBOM. The pipeline must generate SBOMs in both SPDX 2.3 and CycloneDX 1.4 formats. Failure to generate an SBOM must fail the build pipeline.

**Step 2: Attestation and Storage**
The generated SBOM must be signed using Cosign with the Meridian OCI key pair. The signed SBOM artifact must be pushed to the Meridian Harbor OCI registry alongside the container image or software artifact it describes. All SBOMs are indexed by `Dependency-Track` for continuous vulnerability and license analysis.

---

## 6. Controls and Safeguards

Meridian implements a defense-in-depth strategy of administrative, technical, and physical controls to enforce this SOP.

### 6.1 Technical Controls

| Control ID | Control Description | Tool / System |
|---|---|---|
| **T-001** | **Pipeline License Gate:** The CI/CD pipeline (`Jenkins`, `GitHub Actions`) must fail a build if `FOSSA CLI` detects a license violation in the dependency tree against the Meridian License Compliance Matrix. | `FOSSA CLI`, `Jenkins` Shared Library |
| **T-002** | **Continuous Image Scanning:** The `Wiz` admission controller must prevent the deployment of any container image containing a Critical vulnerability into the `production` Kubernetes namespace. | `Wiz`, OPA Gatekeeper |
| **T-003** | **SBOM Verification:** The artifact promotion pipeline must verify the presence of a valid Meridian-signed SBOM in the Harbor registry before promoting an artifact from `staging` to `production`. | `Harbor`, Cosign |
| **T-004** | **Repository Network Isolation:** Internal OSS proxy registries (`Jfrog Artifactory`) must be the only upstream source from which Meridian CI/CD runners are allowed to pull packages. Direct public internet access from build environments is prohibited. | `Jfrog Artifactory`, AWS VPC Security Groups |

### 6.2 Administrative Controls

| Control ID | Control Description |
|---|---|
| **A-001** | **Segregation of Duties for Security Approval:** The individual who initiates an OSS component exception (Requestor) cannot be the same individual who approves the compensating security control. The approval must come from a Security Engineer in the CISO's office who is not a member of the requesting team. This ensures independent validation of the risk. |
| **A-002** | **Periodic Compliance Audits:** The Governance, Risk, and Compliance (GRC) function conducts a quarterly audit of 100% of active OSS components used in production against the Approved OSS Catalog and approved exceptions. |
| **A-003** | **Incident Response Plan:** Meridian maintains a detailed Incident Response Plan (SOP-SEC-015). The plan addresses scenarios specific to OSS, including major zero-day vulnerability exploitation and supply chain poisoning attacks. |

---

## 7. Monitoring, Metrics, and Reporting

To demonstrate the effectiveness of the Framework and drive continuous improvement, the VP of Engineering and CISO track and report on the following Key Performance Indicators (KPIs).

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target | Measurement Method | Reporting Cadence |
|---|---|---|---|
| **Mean Time to Acknowledge (MTTA) for Critical OSS CVE** | < 4 hours | `PagerDuty` Incident Acknowledged timestamp minus `Wiz` Alert Creation timestamp. | Weekly Operational Review |
| **Mean Time to Remediate (MTTR) for Critical OSS CVE** | < 7 calendar days | `Jira` ticket closure timestamp minus `PagerDuty` Incident Creation timestamp. | Monthly CISO Dashboard |
| **OSS License Approval Cycle Time (95th Percentile)** | < 5 business days | Time from `oss.aragon.meridian.com` ticket creation to `Approved` or `Rejected` status. | Monthly OSRB Review |
| **% of Deployed Images with a Valid, Signed SBOM** | 100% | `Dependency-Track` vs. `Kubernetes` production cluster registry scan. Anomalies reported immediately. | Weekly Platform Health Check |
| **Number of Unapproved OSS Components Detected** | 0 (Zero) | Quarterly GRC audit findings. Triage for any deviation is immediate. | Quarterly Risk Review |

### 7.2 Reporting
A formal "OSS Health & Compliance Report" is compiled by the VP of Engineering's office and presented to the CEO and Executive Leadership Team on a quarterly basis. The report includes a summary of KPIs, a catalog of active exceptions with their risk ratings, trends in OSS consumption, and a forward-looking assessment of supply chain risks.

---

## 8. Exception Handling and Escalation

Exceptions to the policies and procedures in this SOP are expected to be temporary and limited in scope. All exceptions must be formally tracked, assessed for risk, and scheduled for resolution.

**Step 1: Exception Request**
The Requestor submits an "OSS Policy Exception Request" through `oss.aragon.meridian.com`. The request must include:
- A clear description of the deviation from the policy (e.g., use of a Category 3 License, deployment of a component with a Critical CVE without a patch).
- A detailed technical and business justification for the urgency or necessity.
- A proposed compensating control (e.g., a strict AWS WAF rule pattern, dedicated network micro-segmentation) to contain the risk.
- A specific, measurable remediation plan with a firm "sunset" date to bring the component or process back into full compliance.

**Step 2: Risk Assessment**
The CISO or their delegate performs a formal risk assessment of the proposed exception.

**Step 3: Approval Authority**
The authority to approve an exception is based on the severity and duration of the risk:
- **Low / Medium Risk:** Exceptions for Medium vulnerability SLAs or for Category 2 licenses can be approved by the **VP of Engineering and CISO** jointly.
- **High / Critical Risk:** Any exception involving a Critical CVE, a Category 3 Restrictive Copyleft license, or a remediation plan exceeding 60 days, must be approved by the **Chief Executive Officer (Dr. Sarah Chen)** upon joint recommendation from the VP of Engineering, CISO, and General Counsel.

**Step 4: Active Management and Escalation**
All approved exceptions are placed on a central risk register monitored by the CISO. As the sunset date approaches, the `oss.aragon.meridian.com` system automatically notifies the owner and the approver. If a remediation plan fails to meet its deadline, the exception is automatically escalated to the next management level, culminating with the CEO for final risk acceptance or directive for immediate, emergency remediation.

---

## 9. Training Requirements

All Meridian personnel with responsibilities defined in this SOP must complete role-based training to ensure consistent application of the Framework.

| Role | Training Module | Frequency | Delivery Method |
|---|---|---|---|
| **All Engineers & Developers** | "OSS Fundamentals for Developers" (MOD-OSS-101). Covers license types, procedure for requesting OSS, and understanding the SBOM. | Annually | LMS (Workday Learning) |
| **Engineering Managers & Tech Leads** | "OSS Governance and Risk Management" (MOD-OSS-201). Covers the approval workflow, vulnerability SLA enforcement, and the Contribution Review Process. | Annually | Instructor-led Workshop |
| **OSRB Members & Approvers** | "Advanced OSS License and Supply Chain Risk" (MOD-OSS-301). Deep-dive on complex license interactions and supply chain threat modeling. | Semi-Annually | External Legal Counsel-led Seminar |

Completion of required training is tracked via Workday Learning. Personnel who fail to complete mandatory training by the due date will have their OSS request privileges suspended until compliance is achieved.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| Document ID | Document Title |
|---|---|
| SOP-ISEC-001 | Master Information Security Policy |
| SOP-PENG-003 | Secure Software Development Lifecycle (SDLC) |
| SOP-SEC-015 | Incident Response Plan |
| SOP-PENG-004 | CI/CD Pipeline Security and Operations |
| SOP-DATA-005 | Data Classification and Handling Standard |
| SOP-PENG-010 | AI Model and Component Provenance |

### 10.2 External References

- Meridian License Compliance Matrix (Appendix C - Internal Only)
- Meridian Approved OSS Catalog (Appendix B - Maintained on `oss.aragon.meridian.com`)
- Open Source Initiative (OSI) License List: [https://opensource.org/licenses/](https://opensource.org/licenses/)
- SPDX License List: [https://spdx.org/licenses/](https://spdx.org/licenses/)
- NIST SP 800-53, Rev. 5: Security and Privacy Controls for Information Systems (Especially CM-8, SA-10, SR-3)
- EU AI Act, Regulation (EU) 2024/1689, Articles 9, 11, 15, 17, and Annex VII.

---

## 11. Revision History

| Version | Effective Date | Author(s) | Description of Changes |
|---|---|---|---|
| 1.0 | 2021-07-19 | Sarah Chen, CEO | Initial publication establishing enterprise-wide OSS governance framework. |
| 1.2 | 2022-11-04 | David Park, VP of Eng. | Added Section 5.4 (SBOM Generation and Management). Integrated `FOSSA` and `Snyk` into the procedures. |
| 2.0 | 2023-05-15 | OSS Review Board | Major rewrite to incorporate Contribution (Outbound) Process. Separated roles of Engineer and Approver. Revised vulnerability SLAs. |
| 2.4 | 2024-02-13 | David Park, VP of Eng. | Refined Section 3 RACI matrix. Updated Section 6.1 to include new `Wiz` admission controller (T-002). Enhanced Section 7 KPI targets. Renamed SOP from "OSS Management" to "OSS Usage". |
| 2.5 | 2025-11-07 | Rachel Kim, CISO & David Park | Comprehensive update for EU AI Act alignment. Updated Section 1.2 (Scope) to explicitly reference AI systems and HealthPay. Added detailed SBOM provenance controls (T-003). Updated Section 3 to incorporate CISO as consulted role. Added Section 5.5 for AI-specific OSS governance. |
|---|---|---|---|