---
sop_id: "SOP-PENG-012"
title: "Software Bill of Materials"
business_unit: "Product & Engineering"
version: "5.9"
effective_date: "2024-05-15"
last_reviewed: "2025-03-23"
next_review: "2025-09-23"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Software Bill of Materials

## 1. Purpose and Scope

This Standard Operating Procedure (SOP) establishes the mandatory framework for the generation, maintenance, monitoring, and disclosure of the Software Bill of Materials (SBOM) for all software products and infrastructure developed or deployed by Meridian Health Technologies, Inc. The primary objective is to create a transparent, auditable, and automated inventory of all third-party and open-source software components that comprise our systems. This capability is fundamental to managing software supply chain risk, ensuring regulatory compliance, and maintaining the security posture that underpins trust in our Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.

This SOP applies to all software components, including source code, compiled binaries, container images, firmware, and software-as-a-service dependencies, that are part of any product or service offered by Meridian Health Technologies. The scope encompasses the entire software development lifecycle (SDLC), from initial development and CI/CD pipeline integration through production deployment, maintenance, and end-of-life decommissioning. It applies to all environments, including development, testing, staging, production, and disaster recovery (Azure DR environment).

The policy is binding upon all employees, contractors, and third-party service providers involved in the design, development, deployment, or maintenance of software for Meridian Health Technologies, with specific responsibilities assigned to the Product & Engineering, IT Operations, and Information Security functions. Adherence to this SOP is required to support our SOC 2 Type II certification, compliance with the EU AI Act for our high-risk AI systems, alignment with the NIST AI Risk Management Framework, and fulfillment of our obligations under SR 11-7 for HealthPay models.

## 2. Definitions and Acronyms

The following terms are defined for the purpose of this SOP to ensure consistent interpretation and execution.

| Term / Acronym | Definition |
| :--- | :--- |
| **SBOM** | Software Bill of Materials: A formal, structured record of the components, libraries, and modules that are contained in or used to build a piece of software, including their supply chain relationships. |
| **Component** | A distinct unit of software, including open-source libraries, commercial third-party components, and internally-developed shared modules. |
| **Dependency** | A software component that is directly or transitively required by another component for its proper function. |
| **Provenance** | The documented chain of custody and origin of a software component, including its source repository, build process, and publisher. |
| **VEX** | Vulnerability Exploitability eXchange: A companion artifact to an SBOM that provides a statement on whether a product is affected by a specific vulnerability in a component. |
| **SPDX** | Software Package Data Exchange: An open standard (ISO/IEC 5962:2021) for communicating SBOM information, adopted as the primary format by Meridian. |
| **CycloneDX** | A lightweight SBOM standard designed for use in application security contexts, accepted as a secondary format. |
| **NTIA Minimum Elements** | The U.S. National Telecommunications and Information Administration’s baseline set of data fields required in an SBOM. |
| **SCA** | Software Composition Analysis: The practice of using automated tools to identify, inventory, and analyze open-source and third-party components in a codebase. |
| **CVE** | Common Vulnerabilities and Exposures: A public list of known cybersecurity vulnerabilities. |
| **CVSS** | Common Vulnerability Scoring System: A framework for rating the severity of security vulnerabilities. |
| **CI/CD Pipeline** | Continuous Integration / Continuous Delivery Pipeline: The automated series of steps that build, test, and deploy software. (GitHub Actions is Meridian's standard). |
| **Container Image** | A lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings. |
| **ECR** | Amazon Elastic Container Registry: The managed AWS service Meridian uses to store, manage, and deploy Docker container images. |

## 3. Roles and Responsibilities

The following RACI matrix delineates the roles and responsibilities for the execution of this SOP. All named roles are Meridian employees; the Chief AI Officer acts as the accountable party for AI-specific dependencies.

| Activity | VP, Engineering (Owner) | DevSecOps Lead | Product Dev Teams | InfoSec (CISO) | Clinical Safety Lead | Chief AI Officer |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SBOM Policy & Tooling** | A | R | I | C | I | C |
| **SBOM Generation (Pipeline)** | I | R/A | C (Script Owner) | I | - | A (AI Components) |
| **SBOM Quality Validation** | I | R | I | I | I | - |
| **Vulnerability Correlation & Triage** | I | R | C | A | I | C |
| **SBOM Publication & Disclosure** | A | R | I | I | C | I |
| **Exception Approval** | A | R (Proposer) | I | C | C | C |
| **Dependency Lifecycle Management** | I | R | A | I | - | - |

**Specific Role Descriptions:**

- **Vice President of Engineering (David Park):** Acts as the Owner of this SOP. Holds ultimate responsibility for the SBOM program’s effectiveness and continuous improvement. Approves all exceptions to this policy.
- **DevSecOps Lead (Sarah Chen):** Responsible for the hands-on implementation, maintenance, and operation of all SBOM generation and validation tooling within the CI/CD pipeline. Manages the inventory of approved base images and orchestrates the vulnerability correlation engine.
- **Product Development Teams:** All engineering teams are responsible for integrating SBOM generation into their build scripts and for the accuracy of the dependency manifest. They are the first responders for remediating vulnerabilities in their codebases.
- **Chief Information Security Officer (CISO, Mark Liu):** Acts as the primary consumer of vulnerability correlation data. Responsible for setting the risk thresholds that dictate automated pipeline actions and for overseeing the Customer Disclosure process in accordance with SOP-SEC-045 (Vulnerability Disclosure).
- **Clinical Safety Lead (Dr. Aris Thorne):** Consults on the risk classification of vulnerabilities impacting Tier 0 Life Safety systems and provides guidance on VEX statements for clinical systems per SOP-REG-011 (Medical Device Cybersecurity).
- **Chief AI Officer (Dr. Evelyn Reed):** Accountable for ensuring that the provenance of all machine learning libraries, model architectures, and training framework dependencies is captured in the SBOM, aligning with the NIST AI RMF Model Cards procedure (SOP-AIG-020).

## 4. Policy Statements

Meridian Health Technologies commits to the following high-level policy obligations. These statements are the governing principles under which the detailed procedures in Section 5 are enacted.

**4.1. Universal SBOM Generation.** Every software artifact released into a production environment or delivered to a customer MUST have a corresponding, validated SBOM generated at the time of build. No artifact is exempt. This applies to all container images, mobile applications, desktop applications, and firmware.

**4.2. Standardized Data Formats.** All SBOMs MUST be generated in both ISO/IEC 5962:2021 (SPDX 2.3) and OWASP CycloneDX 1.4 formats to ensure interoperability with internal vulnerability scanners (Wiz, Prisma Cloud) and external customer systems. The data MUST, at a minimum, satisfy all NTIA Minimum Elements for an SBOM, including Data Fields, Automation Support, and Practices and Processes.

**4.3. Machine-Readable and Human-Consumable.** The authoritative copy of an SBOM is the machine-readable SPDX 2.3 tag-value format stored as an immutable artifact alongside the associated container image in Amazon ECR. A human-readable summary report MUST be auto-generated and linked in the release notes for any customer-facing product release.

**4.4. Proactive Vulnerability Correlation.** The SBOM is not a static document. All components listed in every SBOM MUST be continuously scanned against the National Vulnerability Database (NVD) and other trusted security advisories (e.g., GitHub Advisory Database, PyPA Advisory Database) for the entire supported lifecycle of the product. This process is executed by our designated Application Security Posture Management (ASPM) platform, Wiz.

**4.5. Integrity and Provenance.** The SBOM generation process MUST be an automated, immutable step in the CI/CD pipeline (GitHub Actions). A digital signature MUST be attached to each SBOM document using Sigstore (Cosign), linking the artifact’s provenance attestation to the build pipeline context.

**4.6. Risk Classification Commitment.** A risk classification for high-risk AI systems is established, which considers the nature, intended purpose, and software composition of the clinical system to guide the intensity of the SBOM dependency lifecycle management and manual review processes.

## 5. Detailed Procedures

This section outlines the mandatory step-by-step operational procedures for SBOM lifecycle management.

### 5.1. SBOM Generation Automation (CI/CD Integration)

Every CI/CD pipeline (GitHub Actions workflow) in every source code repository MUST include a mandatory, parameterized job for SBOM generation. This job cannot be skipped or manually bypassed for any build that produces an artifact destined for a production environment.

**Step 1.1: Trigger and Context Collection.**
The SBOM generation job is triggered by the same event that initiates a production build (e.g., a tag push matching `v*.*.*` or a merge to a `main` or `release/*` branch). The workflow MUST capture the following context at job start:
- Git commit sha (`GITHUB_SHA`)
- Build timestamp in ISO 8601 UTC format
- Build environment identifier (e.g., `ci-prod-us-east-1`)
- Builder identity: the Meridian service account `svc-sbom-gen` MUST be used.

**Step 1.2: Image and Filesystem Scanning.**
The job MUST run two parallel scanning methods:
1.  **Source Repository Scan:** Execute `syft scan dir:${GITHUB_WORKSPACE} -o spdx-json=$(mktemp) -o cyclonedx-json=$(mktemp)` to catalog all source-level dependencies identified by package manifest files (e.g., `package-lock.json`, `pom.xml`, `requirements.txt`).
2.  **Container Image Scan:** Simultaneously, for the built container image (e.g., `123456789012.dkr.ecr.us-east-1.amazonaws.com/clinical-ai/service-name:${GITHUB_SHA}`), execute `syft scan ${IMAGE_URI} --catalogers all -o spdx-json=$(mktemp) -o cyclonedx-json=$(mktemp)`. This catalogs all operating-system-level packages (dpkg, RPM), language libraries, and binaries within the running image.

**Step 1.3: SBOM Merge and Enrichment.**
Use the open-source tool, `spdx/tools-golang`, to merge the two SPDX documents (source and image) into a single, comprehensive SBOM document that accurately reflects the complete runtime context. The following `syft` command MUST be the standard invocation, with output files captured as workflow artifacts:
```bash
syft scan ${IMAGE_URI} \
  --output spdx-json=./artifacts/${IMAGE_NAME}-${VERSION_TAG}.spdx.json \
  --output cyclonedx-json=./artifacts/${IMAGE_NAME}-${VERSION_TAG}.cyclonedx.json \
  --output table=./artifacts/${IMAGE_NAME}-${VERSION_TAG}.summary.txt
```

**Step 1.4: NTIA Minimum Elements Validation.**
The pipeline MUST execute a validation script (`ntia-conformance-checker`) against the generated SPDX JSON artifact. This script verifies the presence of all required fields as defined in the NTIA Minimum Elements. The build pipeline MUST fail if this validation does not pass. A `FAIL` result blocks artifact promotion. The specific checks are:
- **Supplier Name:** MUST be "Meridian Health Technologies, Inc."
- **Component Name:** MUST resolve from the package manifest.
- **Version String:** MUST not be null or empty.
- **Unique Identifier:** MUST use the Package URL (purl) format as the primary identifier.
- **Dependency Relationship:** MUST state each component’ direct upstream and downstream relationships.
- **Author:** MUST be set to `svc-sbom-gen@meridian.tech`.

### 5.2. SBOM Attestation and Storage

Once validated, the SBOM artifacts must be made immutable and persistently linked to the deployable artifact.

**Step 2.1: Cryptographic Signing.**
All three validated SBOM artifacts (SPDX, CycloneDX, Summary) MUST be signed using Cosign via the Sigstore standard, leveraging Meridian’s internal OIDC provider for keyless signing. The signing identity (e.g., `https://github.com/Meridian/clinical-ai/.github/workflows/release.yml@refs/tags/v4.7.0`) MUST be embedded in the attestation.
```bash
cosign sign-blob \
  --oidc-issuer "https://gh-oidc.meridian.tech" \
  --identity-token ${{ steps.auth.outputs.token }} \
  --output-signature ./artifacts/${IMAGE_NAME}-${VERSION_TAG}.spdx.json.sig \
  ./artifacts/${IMAGE_NAME}-${VERSION_TAG}.spdx.json
```

**Step 2.2: ECR Artifact Association.**
The signed SBOM artifacts MUST be immutably attached to the container image in Amazon ECR. This is not a tag; it is an artifact association using the `aws ecr put-image` command with the `--image-manifest` and `--artifact-media-type` parameters. The MIME type `application/spdx+json` MUST be used for the SPDX document.
```bash
# Simplified example using a custom script to handle ECR artifact association
python3 ./scripts/ecr_sbom_associate.py \
  --repository ${IMAGE_NAME} \
  --image-tag ${VERSION_TAG} \
  --sbom-file ./artifacts/${IMAGE_NAME}-${VERSION_TAG}.spdx.json \
  --media-type "application/spdx+json"
```

### 5.3. Continuous Dependency Tracking, Vulnerability Correlation, and Risk Classification

This procedure defines the closed-loop system for correlating components with known vulnerabilities.

**Step 3.1: Continuous Monitoring.**
Upon successful ECR push, the Wiz runtime sensor automatically discovers the new image and parses all attached SBOMs. Wiz creates an internal inventory of every component, mapping it to its purl. This inventory is continuously cross-referenced against Meridian’s configured advisory feeds, including NVD, OSV, and any vendor-specific advisory we subscribe to (e.g., AWS Security Bulletins).

**Step 3.2: Vulnerability Correlation and Automated Notification.**
When a new CVE is published that affects a component in any active SBOM, Wiz opens a prioritized ticket in Jira within 1 hour of publication. The ticket is automatically assigned to the owning Product Development Team (based on ECR repository metadata) and the DevSecOps Lead. The ticket MUST contain:
- Affected CVE ID and CVSS v3.1 score.
- A link to the affected SBOM artifact in the Meridian artifact store.
- The exact dependency path (transitive or direct) to the vulnerable component.
- A contextual risk score (Meridian Composite Score) based on CVSS, network reachability, runtime profile (is it deployed on a public-facing ALB?), and evidence of exploitability (from Wiz).
- A "Suggested Fix" link if a newer, non-vulnerable version of the component is available in the Wiz database.

**Step 3.3: AI System Risk Classification.**
For components identified as part of Clinical AI Tier 0 or Tier 1 systems, the automatic Jira ticket is cross-linked to a Quality Management System (QMS) investigation record in our eQMS (Qualio). The Clinical Safety Lead, in coordination with the Chief AI Officer, reviews the risk classification of the system based on its purpose and the nature of the incorporated AI software. This review is to categorize the system as high-risk or non-high-risk in the context of the EU AI Act, using a pre-defined qualitative assessment workflow within Qualio. This classification determines the mandatory remediation timeline detailed in Section 5.4.

### 5.4. Vulnerability Remediation and Quality System Management

This procedure details the mandatory remediation SLAs based on severity and system risk classification.

**Step 4.1: Remediation Triage.**
Within 24 business hours of a Critical or High severity Jira ticket creation (CVSS ≥ 7.0), the owning Product Development Team, DevSecOps Lead, and Information Security representative MUST triage the vulnerability and select a Remediation Plan from the following options:
1.  **Upgrade:** Bump the vulnerable component to the minimum patched version. This is the default and required path.
2.  **Remove/Replace:** Remove the vulnerable component entirely or replace it with a functionally equivalent, non-vulnerable alternative.
3.  **Mitigation:** Deploy an infrastructure or configuration-based mitigation (e.g., WAF rule, network ACL, disabling the vulnerable feature via configuration) that demonstrably renders the vulnerability unexploitable.
4.  **Risk Acceptance:** Formally accept the risk of the vulnerability. This requires an exception (per Section 8) signed by both the CISO and VP of Engineering.

**Step 4.2: Mandatory Remediation Timelines (SLAs).**
The following SLAs are measured from the time the Jira ticket is created by the Wiz system. The VP of Engineering reports compliance against these SLAs monthly to the CEO.

| Risk Classification | CVSS Score Range | Tier 0 / High-Risk | Tier 1 / Non-High-Risk | All Other Tiers |
| :--- | :--- | :--- | :--- | :--- |
| **Critical** | 9.0 - 10.0 | **48 hours** | **5 business days** | **10 business days** |
| **High** | 7.0 - 8.9 | **5 business days** | **10 business days** | **30 calendar days** |
| **Medium** | 4.0 - 6.9 | **30 calendar days** | **45 calendar days** | **60 calendar days** |
| **Low** | 0.1 - 3.9 | Next Sprint | Next Sprint | `Backlog` Priority |

**Step 4.3: Remediation Verification.**
The remediation MUST be verified by an automated CI/CD step that re-generates the SBOM for the patched artifact and confirms the previously vulnerable component’s purl is no longer present, or is present at the patched version. The Wiz sensor MUST re-scan the new artifact and automatically close the associated Jira ticket upon confirmation that the CVE no longer affects the new build.

**Step 4.4: VEX Generation for AI Systems.**
For any vulnerability in a high-risk AI system that results in a "Risk Acceptance" disposition, the DevSecOps Lead MUST generate a VEX document per the CSAF standard. This VEX is cryptographically signed and published alongside the product artifacts in ECR. The VEX states the CVE ID, the affected component, the affected version, and the status as "known_not_affected" with a detailed justification of the compensating control or why the vulnerable code path is not reachable. The quality management system for high-risk systems is updated to record this action, ensuring a traceable log of decisions.

### 5.5. Customer Disclosure Process

The disclosure of SBOM and vulnerability information to customers is a controlled, formal process managed by the VP of Engineering's office, in coordination with the Clinical Safety Lead and Legal.

**Step 5.1: Approved Artifacts for Disclosure.**
Only the machine-readable CycloneDX JSON v1.4 format is approved for external customer disclosure, as its security-focused lineage is preferred by our partners. The SPDX JSON format is accessible only under NDA. The human-readable summary report (SBOM Summary) is generated automatically for every Major and Minor release and is linked in the official Release Notes in our customer portal.

**Step 5.2: Proactive Customer SBOM Notification.**
For each Major and Minor release of a customer-deployed product, the designated Customer Success Manager (CSM) MUST attach the SBOM Summary and CycloneDX JSON artifact to the release notification to the customer’s designated security contact in the Meridian Customer Trust Center (Safebase).

**Step 5.3: Critical CVE Disclosure SLA.**
Upon confirmation of a Critical (CVSS ≥ 9.0) vulnerability in a component used in a customer-deployed product, the VP of Engineering's office MUST:
1.  **Immediate Internal Escalation:** Create a Severity-1 incident (per SOP-SEC-045) and notify the CISO and Clinical Safety Lead.
2.  **Customer Notification:** Within 24 hours of internal triage confirming exploitability, the customer’s security contact MUST be notified via email through the Safebase portal. This notification includes the CVE, a VEX statement (affected / not affected), and the Meridian remediation plan.

**Step 5.4: SBOM Artifact Integrity for Customers.**
Every customer-facing SBOM (CycloneDX JSON) is signed with a Sigstore signature. The Meridian Trust Center page provides a documented, static public signing key and detailed verification instructions. Customers and regulators are instructed to validate the artifact's provenance and integrity independently using the Meridian public key before any review.

## 6. Controls and Safeguards

The following technical and administrative controls are implemented to enforce this SOP and protect the SBOM process from tampering.

| Control ID | Control Description | Type | Enforcement Mechanism | Coverage |
| :--- | :--- | :--- | :--- | :--- |
| **CTL-PENG-012-01** | The SBOM generation CI job step is marked as `required` in the GitHub branch protection rules for `main` and `release/*` branches. | Technical | GitHub Branch Protection Rulesets enforced via GitHub Org-wide policy (Terraform-managed). | ALL repositories. |
| **CTL-PENG-012-02** | The service account (`svc-sbom-gen`) used for build and attestation has the principle of least privilege; it cannot push images, only tag them. | Technical | AWS IAM Roles enforced via Terraform; access key rotation every 90 days. | CI/CD Pipeline |
| **CTL-PENG-012-03** | All SBOM artifacts and their signatures are stored immutably. ECR artifact lifecycle policies prevent deletion for 1825 days (5 years) from the date of creation. | Technical | AWS ECR Artifact Lifecycle Policy. | Production ECR Registry |
| **CTL-PENG-012-04** | Any manual change to the SBOM artifacts post-generation is prohibited. The VP of Engineering must approve an emergency break-glass process for CI pipeline logic changes. | Administrative | Change Management Policy (SOP-GOV-001). | Process |
| **CTL-PENG-012-05** | Only approved, hardened base images from the "Meridian Gold Image" registry can be referenced in a `Dockerfile FROM` instruction. | Technical | Dockerfile linting with a custom `Dockerfile-linter` that checks the source registry against a managed allowlist in our policy library. | CI/CD Pipeline |
| **CTL-PENG-012-06** | The SCA tooling (syft, Wiz sensor) configuration is managed as code and deployed from a central, audited repository. | Administrative | Infrastructure as Code (IaC) management via Terraform, with peer-reviewed merges required. | Configuration Management |

## 7. Monitoring, Metrics, and Reporting

The effectiveness of this SBOM program is continuously monitored through a defined set of Key Performance Indicators (KPIs) and reported on a regular cadence.

### 7.1. Key Metrics and KPIs

| KPI Name | Definition | Target | Measurement Tool |
| :--- | :--- | :--- | :--- |
| **SBOM Coverage Rate** | Percentage of production artifacts with an associated, signed SBOM that passes NTIA validation. | **100%** | Wiz Cloud Security Platform |
| **Mean Time to Remediate (MTTR) - Critical** | Average time from a Critical CVE publication to a verified fix deployed in production for Tier 0 systems. | ≤ **36 hours** | Jira / PagerDuty |
| **Mean Time to Notify (MTTN)** | Average time from Critical CVE publication to customer security contact notification via Safebase. | ≤ **18 hours** | Safebase Audit Logs |
| **Vulnerability Reopen Rate** | Percentage of automatically closed Jira tickets that are reopened by Wiz due to a failed or incomplete fix. | < **5%** | Jira |
| **Unscanned Artifact Age** | The age of the oldest ECR image in a production repository without an associated SBOM. | **0 hours** | Wiz Cloud Security Platform |
| **Dependency Freshness** | Percentage of Tier 0 & 1 system dependencies that are no more than 1 major version behind the latest stable release. | > **90%** | Renovate Dashboard |

### 7.2. Dashboards and Reporting Cadence

1.  **Operational Dashboard:** A real-time Grafana dashboard, "SBOM & Dependency Health," is maintained by the DevSecOps Lead. It displays the current state of coverage, vulnerability remediation SLAs, and MTTR metrics. This is displayed on a wall monitor in the Engineering and Security Operations Center (ESOC).
2.  **Monthly Executive Report:** The VP of Engineering delivers an "SBOM Program Status Report" to the CEO and CISO by the 5th business day of each month. This report provides a snapshot of the KPIs above, a trending analysis of the vulnerability landscape, and a summary of all granted exceptions and accepted risks.
3.  **Quarterly Audit Review:** The Internal Audit and Compliance team pulls a full dataset of SBOM coverage and SLA adherence for all Tier 1 and Tier 2 systems to serve as evidence for the quarterly SOC 2 control effectiveness review (per SOP-GOV-002).

## 8. Exception Handling and Escalation

Deviations from the procedures defined in this SOP must be handled through a formal, time-bound exception process.

**8.1. Exception Criteria.** An exception may be requested if, and only if, full compliance is demonstrably impossible due to a specific, proven technical limitation (e.g., a proprietary third-party binary for which source scanning tools yield no useful data). Lack of time or resources is not valid grounds for an exception.

**8.2. Exception Request Procedure.**
1.  The responsible Product Development Team Lead submits a formal "SBOP Exception Request" via the Internal Service Management Jira project (`JIRA-SM-SOP`), using the `sop_exception` issue type.
2.  The request MUST detail: the specific artifact in scope, the specific procedure section from which the exception is sought, a detailed technical justification, a proposed compensating control, and a sunset date. The maximum sunset date for any exception is 90 days from the request date.
3.  The DevSecOps Lead reviews the technical justification and the proposed compensating control and makes a "Recommend" or "Reject" recommendation in the Jira ticket.
4.  The Chief Information Security Officer (CISO) reviews the risk profile.
5.  For Clinical AI Tier 0 systems, the Clinical Safety Lead reviews and records the exception in the QMS (Qualio) for quality system management purposes.
6.  Final approval or rejection is made by the VP of Engineering. If approved, the compensating control must be implemented and verified by the InfoSec team within 48 hours.

**8.3. Escalation.** If a Critical vulnerability (CVSS ≥ 9.0) is identified for which no viable upgrade, mitigation, or replacement path exists, the risk acceptance cannot be approved at the standard level. It is immediately escalated to a panel consisting of the CISO, VP of Engineering, CEO, and Clinical Safety Lead. This panel must meet within 8 business hours of escalation to determine a path forward, bypassing standard change management.

## 9. Training Requirements

All personnel defined in the Roles and Responsibilities matrix must complete mandatory training on this SOP and the tools it governs.

**9.1. Training Modules.**
- **Module: PENG-012-FUNDAMENTALS (Mandatory for All Engineering & IT:)** Annual online training covering the purpose of an SBOM, the Meridian disclosure policy, and the prohibition against bypassing CI pipeline checks. Tracked via Workday.
- **Module: PENG-012-OPERATIONS (Mandatory for DevSecOps and Security:)** Quarterly hands-on workshop covering the operation of the CI/CD job, SBOM validation scripts, and the Wiz vulnerability correlation engine.
- **Module: PENG-012-DISCLOSURE (Mandatory for CSMs and Legal:)** Annual role-based training on the customer disclosure process, the contents of the Trust Center page, and the non-disclosure implications of SPDX vs. CycloneDX.

**9.2. Tracking and Remediation.** The Learning Management System (LMS, Skillsoft) tracks the assignment, completion, and expiration of all training. A report of non-compliance is sent to the VP of Engineering and the CISO monthly. Access to CI/CD production resources is automatically suspended for any individual whose required training has lapsed by more than 15 days.

## 10. Related Policies and References

This SOP is one component of a comprehensive governance framework. It must be read and enforced in conjunction with the following internal and external documents.

| Document ID | Document Title | Relationship |
| :--- | :--- | :--- |
| **SOP-SEC-045** | Vulnerability Management and Disclosure | Defines the overall vulnerability lifecycle; SBOM data feeds into this process. |
| **SOP-GOV-001** | Change Management & Release Governance | Governs the process for introducing new tools and modifying pipeline logic. |
| **SOP-AIG-020** | AI Model Provenance, Transparency, and Risk Management | Defines the standards for tracking AI-specific dependencies and model cards. |
| **SOP-REG-011** | Medical Device Cybersecurity and Post-Market Surveillance | Mandates clinical safety oversight for vulnerabilities in medical device software. |
| **SOP-INF-030** | Container Image Lifecycle Management | Policy for base image selection, approval, and lifecycle. |
| **NIST SP 800-218** | NIST Secure Software Development Framework (SSDF) v1.1 | Reference framework for our software development lifecycle practices. |
| **ISO/IEC 5962:2021** | Software Package Data Exchange (SPDX) v2.3 | The adopted international standard for the primary SBOM format. |
| **The Minimum Elements For a Software Bill of Materials (SBOM)** | National Telecommunications and Information Administration (NTIA) | Defines the foundational data fields required in our SBOMs. |

## 11. Revision History

| Version | Date | Author | Description of Change |
| :--- | :--- | :--- | :--- |
| 5.9 | 2025-03-23 | S. Chen (DevSecOps Lead) | Refined CI/CD pipeline scripts to use `syft` v0.97.1 for improved Ruby dependency detection. Updated ECR artifact lifecycle to 5 years per legal hold order. |
| 5.8 | 2024-11-15 | M. Liu (CISO) | Added Section 5.5.4, Customer Artifact Integrity. Updated SLAs for Tiers 0 and 1 to align with the new Customer Security Agreement template. |
| 5.7 | 2024-09-01 | D. Park (VP Eng) | Formalized QMS integration (Qualio) and the role of the Chief AI Officer in the RACI matrix. Introduced the Meridian Composite Score concept. |
| 5.6 | 2024-06-10 | A. Thorne (Clinical Safety) | Updated Section 5.4 with specific VEX generation requirements for critical clinical CVEs. Adjusted Critical MTTR SLA from 24h to 48h after triage review. |
| 5.5 | 2024-05-01 | S. Chen (DevSecOps Lead) | Migrated SCA tooling from Trivy to Syft as the primary SBOM generator. Updated all CI pipeline code examples. Mandated NTIA conformance validator. |