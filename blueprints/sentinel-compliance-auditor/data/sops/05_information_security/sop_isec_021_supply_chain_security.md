---
sop_id: "SOP-ISEC-021"
title: "Supply Chain Security"
business_unit: "Information Security"
version: "5.3"
effective_date: "2025-10-07"
last_reviewed: "2026-01-02"
next_review: "2026-07-25"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Supply Chain Security

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish the framework, requirements, and operational procedures for managing supply chain security risks across Meridian Health Technologies, Inc. This SOP defines the lifecycle management of third-party software components, vendor relationships, and the integrity of the Meridian software supply chain that supports the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.

Supply chain security is foundational to Meridian's commitment to patient safety, data protection, financial integrity, and regulatory compliance. A compromise at any tier of the supply chain can cascade into clinical risk, financial loss, regulatory enforcement action, and erosion of trust among the 340+ hospitals, health systems, and millions of patients who depend on Meridian's platforms.

### 1.2 Scope

This SOP applies to:

- **All Meridian business units** including Clinical AI, HealthPay Financial Services, MedInsight Analytics, and Meridian SaaS Platform.
- **All Meridian personnel** including full-time employees, contractors, interns, and consultants who develop, deploy, operate, procure, or manage software and systems.
- **All third-party software components** integrated into Meridian products, including open-source libraries, commercial off-the-shelf (COTS) software, software-as-a-service (SaaS) APIs, container images, and machine learning model dependencies.
- **All vendors, suppliers, and service providers** that supply software, hardware, firmware, data, or services that integrate with, support, or are embedded within Meridian's technology stack.
- **All environments** including production, staging, development, testing, and disaster recovery environments across AWS (us-east-1, eu-west-1) and Azure (DR) footprints.
- **All offices and subsidiaries** in Boston (HQ), London, Berlin, Singapore, and Toronto.

### 1.3 Applicability Matrix

| Business Unit | Scope Applicability | Key Supply Chain Risks |
|---|---|---|
| Clinical AI Platform | Full scope; all ML model dependencies, medical device software components, inference engine libraries | Patient safety risk from tampered models; EU AI Act Article 15, 17 requirements |
| HealthPay Financial Services | Full scope; payment processing libraries, credit decision engines, API gateways | Financial fraud risk; SR 11-7 model integrity requirements |
| MedInsight Analytics | Full scope; analytics libraries, population health data pipelines, PHI-handling components | HIPAA compliance risk; data exfiltration through compromised dependencies |
| Meridian SaaS Platform | Full scope; core infrastructure components, orchestration tools, container base images | Availability risk; multi-tenant isolation compromise |

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| Supply Chain | The end-to-end ecosystem of people, processes, organizations, tools, and components involved in the conception, development, production, delivery, and maintenance of Meridian software products and services. |
| Software Bill of Materials (SBOM) | A formal, machine-readable inventory of all components, libraries, and modules that comprise a software artifact, including transitive dependencies, versions, licenses, and provenance data. |
| Vendor | Any external entity that provides software, hardware, firmware, data, models, or services to Meridian under a contractual agreement. |
| Critical Vendor | A vendor whose compromise or failure would materially impact Meridian's ability to deliver clinical, financial, or operational services. Designation determined by the Vendor Risk Classification Matrix (see Section 5.1.2). |
| Dependency | A software component required by another component to function as intended. Includes direct dependencies (explicitly declared) and transitive dependencies (inherited through direct dependencies). |
| Provenance | Verifiable information about the origin, chain of custody, and build process of a software artifact, sufficient to establish trust in its integrity. |
| Artifact Integrity | The property that a software artifact has not been altered in an unauthorized manner since its creation. Verifiable through cryptographic signatures and attestations. |
| Zero-Day Vulnerability | A previously unknown vulnerability for which no patch is yet available and which may be under active exploitation. |
| Open Source Software (OSS) | Software distributed under a license that grants recipients the rights to use, study, modify, and distribute the software. |
| Container Image | A lightweight, stand-alone, executable package that includes everything needed to run a piece of software, including the code, runtime, system tools, system libraries, and settings. |
| Attestation | A cryptographically signed statement asserting facts about a software artifact, such as the environment in which it was built or the results of a vulnerability scan. |
| EU AI Act | Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence. |
| High-Risk AI System | As defined in EU AI Act Article 6 and Annex III, an AI system intended to be used as a safety component of a medical device, which Meridian's Clinical AI Platform qualifies as. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| SBOM | Software Bill of Materials |
| SCA | Software Composition Analysis |
| SAST | Static Application Security Testing |
| DAST | Dynamic Application Security Testing |
| SLA | Service Level Agreement |
| KPI | Key Performance Indicator |
| TPRM | Third-Party Risk Management |
| CVE | Common Vulnerabilities and Exposures |
| CVSS | Common Vulnerability Scoring System |
| NIST | National Institute of Standards and Technology |
| NTIA | National Telecommunications and Information Administration |
| OWASP | Open Web Application Security Project |
| SLSA | Supply-chain Levels for Software Artifacts |
| Sigstore | A project for signing and verifying software artifacts |
| SPDX | Software Package Data Exchange |
| CycloneDX | OWASP CycloneDX SBOM standard |
| VEX | Vulnerability Exploitability eXchange |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| GRC | Governance, Risk, and Compliance |
| ISMS | Information Security Management System |
| CI/CD | Continuous Integration / Continuous Deployment |
| SOC 2 | System and Organization Controls 2 |

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| Activity | CISO (Rachel Kim) | VP Engineering | VP Product | Legal & Compliance | Security Architecture | DevOps Team | Procurement | Vendor Risk Manager |
|---|---|---|---|---|---|---|---|---|
| Vendor Risk Classification | A | C | I | C | R | I | C | R |
| SBOM Generation & Maintenance | A | R | I | I | C | R | I | I |
| Dependency Vulnerability Scanning | A | I | I | I | R | R | I | I |
| Critical Vulnerability Remediation | I | A | C | I | C | R | I | I |
| Vendor Contract Security Review | A | C | I | R | C | I | R | C |
| OSS License Compliance | I | A | I | R | I | I | I | I |
| Supply Chain Incident Response | R/A | R | I | C | C | R | I | C |
| SBOM Audit & Attestation | R/A | C | I | I | R | C | I | I |
| EU AI Act Article 15 Compliance (Accuracy, Robustness, Cybersecurity) | A | R | R | C | R | R | I | I |
| EU AI Act Article 17 Compliance (Quality Management System) | A | R | R | R | C | I | I | I |
| Exception Approval for Policy Deviation | R/A | C | C | C | C | I | I | I |

**Key:** R = Responsible (performs the work); A = Accountable (approves and signs off); C = Consulted (provides input); I = Informed (kept up to date)

### 3.2 Named Role Descriptions

| Role | Title/Designation | Responsibilities |
|---|---|---|
| Chief Information Security Officer (CISO) | Rachel Kim | Overall accountability for supply chain security program; approves exceptions; reports to CEO and Board on program maturity. |
| VP, Engineering | [Named Engineering Lead, as designated by CTO org] | Ensures engineering teams adhere to secure development practices, SBOM requirements, and dependency management procedures. |
| VP, Product | [Named Product Lead per product line] | Ensures product roadmaps account for dependency lifecycle management; approves timelines for remediation. |
| Director, Legal & Compliance | [Named Legal Lead] | Reviews vendor contracts for security clauses; advises on OSS license compliance; ensures GDPR Data Processing Agreements (DPAs) include supply chain security requirements. |
| Security Architecture Lead | [Named Security Architect] | Owns technical standards for SBOM generation, artifact signing, and vulnerability scanning tooling; maintains the Meridian Approved Dependency Registry. |
| Vendor Risk Manager | [Named, reports to CISO dotted line to Procurement] | Owns vendor risk assessment lifecycle; maintains the Vendor Risk Register; conducts initial and periodic vendor due diligence. |
| Procurement Manager | [Named Procurement Lead] | Ensures all software procurement requests flow through the Vendor Risk Assessment process before contract execution; maintains the master vendor inventory. |
| DevOps / Platform Engineering Lead | [Named DevOps Lead] | Implements and operates CI/CD pipeline controls for SBOM generation, artifact signing, and pre-deployment vulnerability gates. |
| Incident Response Lead | [Named IR Lead, reports to CISO] | Leads supply chain-related incident investigations; coordinates vendor notification and regulatory reporting. |

## 4. Policy Statements

### 4.1 General Policy Commitments

1. **Secure-by-Design Supply Chain:** Meridian shall design, implement, and maintain a software supply chain security program that integrates security controls at every stage of the software development lifecycle (SDLC), from initial coding through deployment and ongoing operations.

2. **Transparency and Traceability:** Meridian shall maintain a complete, continuously updated Software Bill of Materials (SBOM) for every software artifact deployed in production environments. SBOMs shall be generated in both SPDX 2.3 and CycloneDX 1.5 formats to ensure interoperability.

3. **Dependency Integrity:** All software dependencies, whether open-source or commercial, shall be obtained only from a Meridian-approved source. Cryptographic verification of dependency integrity shall be performed at the time of ingestion and at every subsequent build.

4. **Vendor Due Diligence:** No software vendor, service provider, or data processor shall be engaged without completing the Meridian Vendor Security Risk Assessment (VSRA) process commensurate with the vendor's risk classification.

5. **Continuous Monitoring:** Meridian shall continuously monitor its software supply chain for vulnerabilities, threats, and integrity anomalies using automated tooling integrated into the CI/CD pipeline and runtime environment.

6. **Compliance with EU AI Act:** For all components integrated into Meridian's High-Risk AI Systems, as defined under the EU AI Act, Meridian shall implement the specific supply chain accuracy, robustness, and cybersecurity requirements of Article 15, along with the quality management system requirements of Article 17.

7. **Vulnerability Remediation SLAs:** All identified vulnerabilities in the software supply chain shall be remediated according to the timelines specified in the Meridian Vulnerability Management Standard (SOP-ISEC-015) and as augmented in Section 5.4 of this SOP.

8. **Artifact Integrity Verification:** All software artifacts deployed to production shall carry a valid cryptographic signature verifiable against Meridian's internal Public Key Infrastructure (PKI) or an approved external attestation framework (Sigstore, in-toto).

9. **Least Privilege for Pipeline Systems:** CI/CD pipeline systems shall be configured with the minimum permissions necessary to perform their functions. Credentials used by pipeline systems shall be uniquely identifiable and shall never be shared across environments.

10. **No Direct-to-Production External Dependency Resolution:** Production builds shall not resolve external dependencies at build time. All dependencies shall be pre-fetched, scanned, and stored in the Meridian Internal Artifact Repository (JFrog Artifactory) prior to consumption by production builds.

### 4.2 EU AI Act Specific Policy Commitments

Meridian's Clinical AI Platform is classified as a High-Risk AI System under Annex III of the EU AI Act (Regulation 2024/1689). As such, in addition to the general policy commitments above, Meridian commits to the following supply chain security provisions specific to the AI supply chain:

1. **Article 15(1) – Accuracy, Robustness, and Cybersecurity:** Meridian shall ensure that the Clinical AI Platform, including all components sourced from third parties, achieves an appropriate level of accuracy, robustness, and cybersecurity throughout its lifecycle. Third-party AI models, training datasets, and inference components shall undergo dedicated security and integrity assessment prior to integration.

2. **Article 15(3) – Resilience Against Manipulation:** The AI supply chain shall be resilient against attempts by unauthorized third parties to alter system use or behavior. Meridian shall employ technique-level robustness testing against supply chain poisoning attacks on model weights and training data.

3. **Article 17(1)(a) – Quality Management System Integration:** Supply chain security shall be an integral component of Meridian's Quality Management System (QMS). The QMS shall document the design control and design verification procedures for all externally sourced components of High-Risk AI Systems.

4. **Article 17(1)(f) – Post-Market Monitoring:** Meridian shall maintain a post-market monitoring system that actively tracks the security posture of all third-party AI components after deployment, ensuring that newly discovered vulnerabilities are addressed in accordance with the vigilance obligations of the EU Medical Device Regulation (MDR).

5. **Article 17(4) – Conformity Presumption:** Meridian shall seek conformity with harmonised standards (where applicable) for AI supply chain security, including ISO/IEC 42001 and ETSI EN 303 645 for underlying infrastructure.

## 5. Detailed Procedures

### 5.1 Vendor Onboarding and Risk Assessment

#### 5.1.1 Vendor Identification and Intake

1. Any Meridian employee or contractor who identifies a need for a new software vendor, service provider, data provider, or open-source dependency from an unapproved external source shall initiate a **Vendor Security Intake Request** via the Meridian ServiceNow GRC portal (ServiceNow GRC > Vendor Risk > New Request).

2. The intake form shall capture, at minimum:
   - Vendor legal name and corporate identifier (D-U-N-S number or LEI, if available)
   - Product or service description
   - Business justification (why an existing approved vendor cannot meet the need)
   - Business unit and system(s) that will consume the vendor's output
   - Data classification of information that will be processed, stored, or transmitted by the vendor
   - Estimated annual spend
   - Proposed contract term

3. Upon submission, the ServiceNow workflow automatically notifies:
   - The **Vendor Risk Manager** (assignment group: `SN-ITSM-VRM`)
   - The **Procurement Manager** (assignment group: `SN-FIN-PROC`)
   - The **Director, Legal & Compliance** (for requests involving PHI or PII)

#### 5.1.2 Vendor Risk Classification and Tiering

1. The Vendor Risk Manager, with input from the requesting business unit and Security Architecture, shall assign a risk tier to the vendor within **five (5) business days** of intake submission. Classification shall follow the Meridian Vendor Risk Classification Matrix:

| Risk Tier | Criteria | Examples at Meridian | Due Diligence Depth |
|---|---|---|---|
| **Tier 1 – Critical** | - Vendor software is embedded in or directly supports a High-Risk AI System <br> - Vendor processes, stores, or transmits ePHI or financial payment data <br> - Vendor has privileged network access to Meridian infrastructure <br> - Failure or compromise of vendor directly threatens patient safety or causes regulatory action | - Foundation model provider for Clinical AI <br> - Cloud infrastructure provider (AWS, Azure) <br> - Payment processing gateway <br> - CI/CD pipeline tooling vendor | Full: On-site assessment (or virtual equivalent), penetration testing results review, SOC 2 Type II review, business continuity and disaster recovery (BC/DR) plan review |
| **Tier 2 – High** | - Vendor supplies a core business application <br> - Vendor processes confidential internal data <br> - Vendor software has elevated privileges within Meridian environments | - CRM platform vendor <br> - HRIS vendor <br> - Observability platform vendor <br> - Commercial ML library vendor | Enhanced: SOC 2 Type II review or equivalent (ISO 27001 certification), completed SIG/Lite questionnaire, incident response capability review |
| **Tier 3 – Standard** | - Vendor supplies a non-critical business tool <br> - Vendor processes limited, non-sensitive data <br> - Vendor has no privileged access | - Office productivity tool vendor <br> - Diagramming tool vendor <br> - Project management SaaS | Standard: Review of publicly available security documentation, Standardized Information Gathering (SIG) Lite questionnaire, or equivalent self-attestation |
| **Tier 4 – Low** | - Vendor supplies a utility or tool with no access to Meridian data <br> - Vendor relationship is one-time or transactional | - Font library vendor <br> - Static documentation hosting | Minimal: Review of vendor's published security posture, confirmation of no data exchange |

2. The Vendor Risk Manager shall record the tier classification, rationale, and associated risk in the **Meridian Vendor Risk Register** (stored in ServiceNow GRC, table: `vendor_risk_assessment`).

#### 5.1.3 Vendor Due Diligence and Assessment

1. **Tier 1 – Critical Vendors:** The Vendor Risk Manager shall commission a full due diligence assessment within **thirty (30) calendar days** of tier assignment. This assessment shall include:
   - A Meridian-led or qualified third-party auditor-led security assessment (remote or on-site), covering the Meridian Vendor Security Assessment Standard (template: `TPRM-ASSESS-T1-v3.2.docx`).
   - Review of the vendor's most recent SOC 2 Type II report (or equivalent independent attestation). Meridian shall evaluate the Complementary User Entity Controls (CUECs) and determine whether Meridian's internal controls adequately address any stated expectations.
   - Review of the vendor's penetration testing summary report for the system(s) Meridian will consume.
   - Review of the vendor's business continuity and disaster recovery plan, including confirmation that RTO/RPO for the service are documented and align with Meridian's availability requirements. For services supporting Tier 1 clinical systems, Meridian shall validate that the vendor's published continuity commitments are logically consistent with Meridian's own service continuity expectations, as documented in the system-specific architecture runbooks.
   - Review of the vendor's vulnerability disclosure and patch management policies.
   - For vendors supplying AI components (models, training data, labeling services), a specific **AI Supply Chain Assessment** covering the items in Section 5.11.

2. **Tier 2 – High Vendors:** The Vendor Risk Manager shall commission an enhanced due diligence assessment within **twenty (20) calendar days** of tier assignment, including:
   - Completion and review of the SIG Lite questionnaire or equivalent (SIG, CAIQ, or VSAQ).
   - Review of the vendor's most recent SOC 2 Type II report or ISO 27001 certificate.
   - Confirmation of the vendor's incident notification SLA (must be ≤ 24 hours for confirmed breaches involving Meridian data).
   - Review of the vendor's data flow diagram as it pertains to Meridian data.

3. **Tier 3 – Standard Vendors:** The requestor, with support from the Vendor Risk Manager, shall complete a Standard Vendor Security Questionnaire (template: `TPRM-ASSESS-T3-v2.1.docx`) within **ten (10) calendar days**.

4. **Tier 4 – Low Vendors:** A minimal assessment confirming that no Meridian data is exchanged and that the vendor poses negligible risk. Completed within **five (5) business days**.

5. Assessment results shall be documented in the Vendor Risk Register. Any residual risks identified during the assessment shall be entered into the Meridian Risk Register (ServiceNow GRC > Risk Management) and tracked to remediation or formal acceptance by the CISO.

#### 5.1.4 Contractual Security Requirements

1. Before contract execution, the Director, Legal & Compliance shall ensure that the vendor agreement includes the **Meridian Standard Information Security Addendum** (template: `LEGAL-SEC-ADDENDUM-v4.1.docx`) appropriate to the vendor's risk tier. Key contractual requirements include:

   - **Right to Audit:** Meridian reserves the right to audit the vendor's security controls annually (or following a security incident), either directly or through an independent assessor at Meridian's discretion.
   - **Security Incident Notification:** Vendor shall notify Meridian of any confirmed security incident involving Meridian data or systems within **four (4) hours** of confirmation (Tier 1) or **twenty-four (24) hours** (Tiers 2-3).
   - **SBOM Provision:** For Tier 1 and Tier 2 software vendors, the vendor shall provide a current SBOM for their product upon request and upon any major version release.
   - **Vulnerability Disclosure:** Vendor shall disclose any Critical or High severity vulnerabilities in their product to Meridian within **seventy-two (72) hours** of internal confirmation.
   - **Data Processing Addendum (DPA):** For vendors processing personal data (including PHI), a DPA compliant with applicable data protection law (GDPR, HIPAA) shall be executed.
   - **Subprocessor Notification:** Vendor shall notify Meridian of any new subprocessor engagements at least **thirty (30) calendar days** prior to the subprocessor beginning to process Meridian data.
   - **Termination Data Handling:** Vendor shall, at Meridian's election, return or securely destroy all Meridian data within **thirty (30) calendar days** of contract termination and provide written certification of destruction.

2. No purchase order or contract for a Tier 1-3 vendor shall be approved without confirmation from the Vendor Risk Manager that the due diligence assessment has been completed and any identified risks have been accepted.

#### 5.1.5 Vendor Re-Assessment Cadence

| Tier | Re-Assessment Frequency | Trigger Events (immediate re-assessment) |
|---|---|---|
| Tier 1 | **Annually** | Merger/acquisition; major incident at vendor; vendor change of control; vendor introduces a new subprocessor for Meridian data |
| Tier 2 | **Biennially (every 2 years)** | Merger/acquisition; major incident at vendor |
| Tier 3 | **Upon contract renewal** | Major incident at vendor |
| Tier 4 | **Ad-hoc (event driven)** | Documented concern |

### 5.2 Software Bill of Materials (SBOM) Management

#### 5.2.1 SBOM Generation

1. **Mandatory SBOM Generation Points:** An SBOM shall be generated at the following stages of the software lifecycle:
   - **Build Time:** Automatically at the completion of every CI/CD pipeline build that produces a deployable artifact (binary, container image, package).
   - **Release Time:** Before a software release is promoted to production.
   - **Procurement Ingestion:** Upon receipt of any third-party commercial software, before integration into Meridian environments.
   - **Event-Driven:** Upon discovery of a new Critical/High CVE affecting a dependency, a fresh SBOM for the affected artifact shall be generated to facilitate impact analysis.

2. **SBOM Formats:** All SBOMs shall be generated in the following machine-readable formats:
   - **SPDX 2.3** (Software Package Data Exchange) – Preferred for license compliance and broader interoperability.
   - **CycloneDX 1.5** (OWASP CycloneDX) – Preferred for security vulnerability management due to richer component pedigree and VEX support.

3. **SBOM Minimum Data Elements:** Each SBOM entry for a dependency shall include, at minimum, the elements prescribed by the NTIA "Minimum Elements for a Software Bill of Materials":
   - **Supplier Name:** The name of the entity that created, defined, and identified the component.
   - **Component Name:** The name of the component as defined by the supplier.
   - **Version String:** The version identifier used by the supplier to specify the software component.
   - **Component Hash:** A cryptographic hash (SHA-256 minimum) of the component.
   - **Unique Identifier:** A globally unique identifier for the component, such as a Package URL (purl) or CPE.
   - **Relationship:** The relationship between the component and the Meridian artifact (e.g., INCLUDES, DEPENDS_ON, GENERATES).

4. **Extended Data Elements (Enriched SBOM):** For Tier 1 clinical and AI system components, Meridian shall additionally capture:
   - **Provenance Data:** Link to an in-toto attestation or SLSA provenance statement for the component.
   - **Pedigree Data:** Information regarding the lineage of the component, including upstream sources and modifications.
   - **License Identifier:** A valid SPDX License Identifier.
   - **Known Vulnerabilities:** An embedded or referenced VEX document stating the exploitability status of known CVEs in the component within the Meridian deployment context.

#### 5.2.2 SBOM Tooling

| Tool | Purpose | Integration Point |
|---|---|---|
| **Syft** (Anchore) | SBOM generation for container images | Integrated into all Dockerfile builds in GitLab CI; generates SBOM before image push |
| **CycloneDX Generator for Maven/Gradle** | SBOM generation for Java-based services (HealthPay, MedInsight) | Integrated into Maven/Gradle build plugins |
| **pip-audit with CycloneDX output** | SBOM generation for Python-based AI/ML services (Clinical AI) | Integrated into Poetry/pip build pipeline |
| **Trivy** (Aqua) | Container image vulnerability scanning integrated with SBOM generation | GitLab CI security stage; enforces policy gates |
| **Dependency-Track** (OWASP) | Centralized SBOM ingestion, analysis, and vulnerability correlation platform | Deployed on Meridian Kubernetes clusters; receives SBOMs via CI/CD webhook uploads |
| **JFrog Artifactory** | Binary repository with build-info SBOM generation | Used for all binary artifact storage; stores generated SBOMs alongside artifacts |

#### 5.2.3 SBOM Storage and Exchange

1. **Storage:** Generated SBOM documents shall be stored as immutable build artifacts in the Meridian Internal Artifact Repository (JFrog Artifactory) under the repository path `sbom-repository/<team>/<artifact>/<version>/`. Retention shall match the retention policy for the associated software artifact, with a minimum retention of **seven (7) years** for medical device software artifacts.

2. **Customer Exchange:** Upon request from a qualified healthcare provider customer under a valid Business Associate Agreement (BAA) or data protection agreement, Meridian shall provide a current SBOM for the Meridian software components deployed at that customer's instance within **fourteen (14) calendar days**. SBOMs may be provided under a non-disclosure agreement (NDA) if they are deemed to contain Meridian proprietary information.

3. **Regulatory Submission:** For CE-marked clinical AI products under EU MDR, the SBOM for each release shall be maintained as part of the Technical Documentation (Annex II of EU MDR 2017/745) and shall be available to the Notified Body upon request.

### 5.3 Dependency Management

#### 5.3.1 Dependency Ingestion Workflow

1. **Approved Sources:** All dependencies shall be sourced exclusively from the **Meridian Approved Dependency Registry** (maintained in the internal developer portal, Backstage). Approved sources include:
   - Meridian Internal Artifact Repository (JFrog Artifactory) – proxies for:
     - Maven Central (Java)
     - PyPI (Python)
     - npm Registry (Node.js)
     - Docker Hub (container base images, limited to approved, pinned images)
   - Vendor-provided, cryptographically signed packages delivered via secure portal.

2. **Requesting a New Dependency:** A developer who requires a new third-party dependency (not already present in the Approved Dependency Registry) shall:
   - Submit a **Dependency Approval Request** via Backstage (Software Catalog > Dependencies > Request New).
   - Provide: package name, version range, source registry, justification, and use case.
   - The request is routed to the **Security Architecture Lead** for initial review.

3. **Approval Gate Criteria:** The Security Architecture Lead shall evaluate the dependency against the following criteria within **five (5) business days**:
   - **Maintenance Status:** The project must show evidence of active maintenance (commits within the last 90 days for OSS).
   - **Security Posture:** No known unpatched Critical CVEs in the requested version; project must have a documented vulnerability disclosure process.
   - **License Compatibility:** License must be on the Meridian Approved License List (maintained by Legal & Compliance).
   - **Provenance:** The artifact must be obtainable in a manner that supports cryptographic integrity verification (e.g., signed commits, signed releases, or checksum-provided).
   - **Transitive Dependency Risk:** The dependency's own dependencies shall not introduce an unreasonable expansion of the Meridian trust boundary. A preliminary transitive dependency scan shall be performed.

4. **Dependency Mirroring:** Upon approval, the DevOps/Platform Engineering team shall mirror the approved dependency version into the Meridian Internal Artifact Repository within **two (2) business days**. The dependency is then added to the Approved Dependency Registry.

5. **Locking Versions:** All dependencies in Meridian projects shall be pinned to exact versions using lock files (e.g., `package-lock.json`, `yarn.lock`, `Pipfile.lock`, `Gemfile.lock`, `go.sum`). Version ranges (e.g., `^1.2.3`, `~> 1.2`) are prohibited in production-bound projects.

#### 5.3.2 Dependency Scanning and Analysis

1. **Continuous Scanning:** The Meridian CI/CD pipeline (GitLab CI) shall automatically execute Software Composition Analysis (SCA) scanning on every commit to the main branch and every merge request. The pipeline shall:
   - Generate an SBOM.
   - Upload the SBOM to OWASP Dependency-Track.
   - Compare identified vulnerabilities against configured policy violation thresholds.

2. **Policy Violation Thresholds (Pipeline Gates):**

| Vulnerability Severity | Action | SLA for Remediation After Discovery |
|---|---|---|
| **Critical (CVSS ≥ 9.0)** | **Build Breaker:** Pipeline fails automatically. Artifact cannot be promoted to staging or production until vulnerability is remediated or an exception is granted by the CISO (per Section 8). | **24 hours** |
| **High (CVSS 7.0 – 8.9)** | **Build Warning with Staging Gate:** Pipeline warns but allows deployment to development/staging. Promotion to production is blocked. | **7 calendar days** |
| **Medium (CVSS 4.0 – 6.9)** | **Build Warning:** Pipeline warns. Artifact may be promoted if no Critical or High vulnerabilities exist. | **30 calendar days** (or next release, whichever is earlier) |
| **Low (CVSS 0.1 – 3.9)** | **Informational:** Logged in Dependency-Track; no immediate action required. Triaged during weekly security review. | **Next patch cycle** |

3. **Vulnerability Exploitability eXchange (VEX):** For every reported vulnerability in a dependency, the Security Architecture Lead (or delegated security engineer) shall analyze exploitability in the context of Meridian's actual use of the vulnerable component. A VEX statement shall be generated indicating one of the following:
   - **Affected:** Meridian is vulnerable to this CVE and remediation action is underway.
   - **Not Affected:** Reason must be documented (e.g., "the vulnerable function is not called by the Meridian code path," "the vulnerable feature is disabled in Meridian's configuration").
   - **Fixed:** Remediation has been applied.
   - **Under Investigation:** Analysis is in progress (must be resolved within 72 hours).

   VEX statements shall be stored in OWASP Dependency-Track alongside the associated vulnerability.

4. **Runtime Dependency Monitoring:** For Tier 1 production environments, Meridian shall deploy runtime SCA agents (Aqua Security) that continuously monitor the active dependency graph of running workloads and alert on newly disclosed vulnerabilities affecting loaded libraries.

### 5.4 Vulnerability Remediation Workflow

#### 5.4.1 Identification and Triage

1. A vulnerability in a supply chain component may be identified through:
   - Automated CI/CD SCA scanning (primary path, Section 5.3.2).
   - Runtime SCA agent alerts.
   - OWASP Dependency-Track daily digest report.
   - External notification (vendor advisory, US-CERT, ISAC, bug bounty report).
   - Manual penetration test or security research finding.

2. All identified vulnerabilities shall be triaged within the SLA times specified below:

| Identification Source | Triage SLA | Triage Action |
|---|---|---|
| Automated pipeline (build breaker) | Immediate (pipeline halts) | Developer on duty must acknowledge within 1 hour during business hours; 4 hours off-hours via on-call escalation. |
| Runtime agent alert (Critical) | 1 hour | Alert routed to Security Operations Center (SOC) for immediate investigation via PagerDuty `supply-chain-critical` service. |
| Vendor advisory (Critical/High) | 4 hours | Vendor Risk Manager reviews and notifies impacted product teams via ServiceNow Security Incident (SN-SEC-INC). |
| Dependency-Track daily digest | By 10:00 AM in the team's local time zone | Team lead assigns vulnerabilities to engineers for analysis. |

#### 5.4.2 Remediation Execution

1. **Preferred Remediation Paths (in order of preference):**
   - Apply vendor-supplied patch that remediates the specific CVE.
   - Upgrade the dependency to a non-vulnerable version.
   - Apply a vendor-supplied or community-supplied workaround or mitigation.
   - Disable the vulnerable functionality via configuration, if feasible and validated.
   - Apply compensating controls (WAF rule, network segmentation) documented and approved by Security Architecture.
   - Request a formal exception (see Section 8).

2. **Remediation Verification:**
   - After remediation, the pipeline shall be re-run to confirm the vulnerability is no longer detected.
   - For runtime mitigations, a follow-up validation scan shall be performed within **24 hours** of mitigation deployment.
   - The VEX document in Dependency-Track shall be updated to **Fixed** status with a reference to the change request or incident ticket.

### 5.5 Artifact Integrity and Provenance Verification

#### 5.5.1 Code Signing

1. **Code Signing Certificate:** Meridian maintains an internal Code Signing Certificate Authority (CA) within the Meridian PKI (managed by the Identity and Access Management team). This CA issues code signing certificates to CI/CD pipeline service accounts.

2. **Signing Points:**
   - **Git Commits:** All commits to Meridian repositories shall be signed with the committer's PGP key or S/MIME certificate. GitHub Enterprise branch protection rules shall enforce signed commits on `main` and `release/*` branches.
   - **Build Artifacts:** All released binaries, packages, and container images shall be cryptographically signed at build time using the CI/CD pipeline's code signing certificate. Signing shall utilize Cosign (Sigstore project) for container images and GPG for binaries.
   - **Container Base Images:** Only signed container images from trusted publishers shall be pulled. Image pull policies shall enforce signature verification using Cosign (keyless signing with OIDC, pinned to Meridian's GitHub organization).

3. **Verification at Deployment:** The Meridian deployment orchestrator (ArgoCD) shall verify the signature of every container image and Helm chart before admitting it to a production Kubernetes cluster. Deployment of unsigned artifacts shall be rejected, and an alert shall be generated to the SOC (`supply-chain-unsigned-artifact`).

#### 5.5.2 SLSA Compliance

Meridian adopts the Supply-chain Levels for Software Artifacts (SLSA) framework and commits to the following compliance levels:

| SLSA Level | Requirement | Meridian Implementation Status |
|---|---|---|
| **SLSA Level 3** (for Tier 1 & 2 systems) | - **Source:** Version-controlled history with strong authentication of committers. Two-person review. <br> - **Build:** Hardened build platform (GitLab CI on isolated runners). Builds are hermetic (no network access during build except to approved internal mirrors). Provenance attestation signed by the pipeline. <br> - **Provenance:** Non-falsifiable provenance attestation that can be verified by downstream consumers. | Required for all Clinical AI Platform and HealthPay Financial Services builds. |
| **SLSA Level 2** (for all other systems) | - **Source:** Version-controlled history. Authenticated builds. <br> - **Build:** Builds run on managed CI/CD platform with build steps defined in code. Provenance exists but may not be fully hermetic. | Minimum required for MedInsight and SaaS Platform builds. |

### 5.6 Open Source Software (OSS) Governance

#### 5.6.1 OSS License Compliance

1. All OSS licenses for dependencies shall be detected automatically by the SCA tooling (Dependency-Track) and mapped against the **Meridian Approved OSS License List**. The current Approved License List (version 4.2, maintained by Legal & Compliance) is available at the internal GRC Confluence space.

2. Dependencies with licenses classified as **Prohibited** (e.g., AGPL-v3 for internal-facing services where it imposes unacceptable obligations; or any license that restricts Meridian's ability to distribute its software in compliance with regulatory requirements) shall not be integrated into Meridian products without a Legal & Compliance exception approved by the General Counsel.

3. Dependencies with licenses classified as **Review Required** (e.g., GPL-2.0, LGPL-3.0) shall undergo a legal review before approval. The review shall be completed within **ten (10) business days** of the dependency approval request.

#### 5.6.2 OSS Contribution Policy

1. Meridian employees are encouraged to contribute back to the OSS projects that Meridian depends on, subject to VP-level approval.

2. Any Meridian-proprietary code contributed to an external OSS project shall be reviewed and approved by both the contributor's manager and the Director, Legal & Compliance to ensure no inadvertent disclosure of Meridian intellectual property or security-sensitive implementation details.

3. Contributions must not include Meridian internal hostnames, IP addresses, API keys, or other environment-specific information.

### 5.7 CI/CD Pipeline Security

#### 5.7.1 Pipeline Configuration as Code

1. All CI/CD pipeline definitions (GitLab CI `.gitlab-ci.yml` files) shall be stored in version control alongside the application code they build and deploy.

2. Modifications to pipeline definitions shall undergo the same peer review process as application code (merge request with at least one approving reviewer).

3. Shared pipeline templates (used across multiple projects) shall be maintained in a dedicated `meridian-pipeline-templates` repository with restricted merge permissions to the DevOps and Security Architecture teams.

#### 5.7.2 Pipeline Hardening

1. **Runner Isolation:** CI/CD build jobs for Tier 1 and Tier 2 projects shall execute on isolated, ephemeral runners (Kubernetes executor pods) that are destroyed after job completion. Runners shall not retain state across jobs.

2. **No Persistent Secrets on Runners:** All secrets (API keys, signing keys, deployment tokens) used by pipeline jobs shall be injected via the GitLab CI secrets integration (HashiCorp Vault backend) at job execution time. Secrets shall never be hardcoded in pipeline definition files or stored as project-level CI/CD variables in plaintext.

3. **Dependency Caching:** Where dependency caching is used to improve build performance, cached dependencies shall be stored in a dedicated, access-controlled object storage bucket (AWS S3 with SSE-KMS encryption). Caches shall be invalidated and rebuilt at least **weekly** to mitigate cache poisoning risks.

4. **Network Egress Control:** For Tier 1 builds achieving SLSA Level 3 hermeticity, build jobs shall run in a network-restricted environment that permits egress only to the Meridian Internal Artifact Repository (for dependencies) and Meridian container registries (for base images). No public internet egress is permitted during the build phase.

### 5.8 Container Image Governance

#### 5.8.1 Base Image Policy

1. **Approved Base Images:** All Meridian containerized applications shall be built from an approved set of hardened, minimal base images. The current approved list (maintained by Security Architecture in the Backstage Software Catalog) includes:
   - Meridian Hardened Alpine (based on `alpine:3.19`, minimal packages, scanned at build)
   - Meridian Hardened Distroless (Java-based services, Python-based AI services)
   - AWS ECR Public Images (only for AWS-provided tools, e.g., `aws-cli`)

2. **Base Image Updating:** Container base images shall be rebuilt at least **monthly** to incorporate underlying OS security patches. Pipeline automation (Renovate bot configured by DevOps) shall automatically open merge requests to update base image tags when new patches are available.

3. **Image Layer Minimization:** Container images shall be built using multi-stage builds to minimize the final image layer count and size. The final image shall not include build tools, compilers, or development dependencies.

### 5.9 Hardware and Firmware Supply Chain

#### 5.9.1 Hardware Procurement

1. All server, network, and storage hardware deployed in Meridian data centers or shipped to Meridian offices shall be procured through authorized Meridian hardware vendors via the Procurement team.

2. Hardware shipments shall be inspected upon receipt for evidence of tampering. Tampered hardware shall not be deployed, and the CISO and head of Corporate Security shall be notified immediately.

#### 5.9.2 Firmware Integrity

1. For all Meridian-managed infrastructure (on-premises servers, network appliances), firmware versions shall be maintained at the latest vendor-recommended stable release.

2. Firmware updates shall be applied during scheduled maintenance windows and shall be verified by comparing the vendor-provided cryptographic hash against the downloaded firmware image before application.

### 5.10 AI/ML Supply Chain Security (EU AI Act Compliance)

This section addresses the specific supply chain security requirements for Meridian's Clinical AI Platform, classified as a High-Risk AI System. These procedures satisfy the Article 15 robustness and Article 17 quality management system requirements of the EU AI Act.

#### 5.11.1 Model Provenance and Integrity

1. **Model Card Requirement:** Every externally sourced AI model (foundation model, fine-tuned model) integrated into the Clinical AI Platform shall be accompanied by a **Model Card** that documents:
   - Model architecture and training methodology.
   - Training data provenance, including the data source, date of acquisition, and any data preprocessing steps.
   - Known limitations, biases, and ethical considerations.
   - Performance benchmarks on relevant clinical tasks.
   - Security testing performed on the model (adversarial robustness, data poisoning resistance).

2. **Model Integrity Verification:** All model weights ingested into the Meridian ML Pipeline (MLflow, deployed on Meridian Kubernetes) shall be cryptographically verified:
   - Models shall be distributed with a strong cryptographic hash (SHA3-256 minimum).
   - The hash shall be verified by the ML pipeline ingestion step before the model is registered in the Meridian MLflow Model Registry.
   - Any hash mismatch shall halt ingestion and generate an automatic security incident in ServiceNow.

3. **Model Scanning:** Before deployment to Clinical AI production, models shall undergo:
   - **Malicious Code Scanning:** Scanning of serialized model formats (pickle, Keras SavedModel, ONNX) for embedded malicious code using Meridian's ML model scanning service.
   - **Backdoor/Trigger Detection:** Automated testing for hidden backdoor triggers using the Meridian Model Integrity Test Suite, which applies a battery of inputs designed to trigger anomalous behavior.

#### 5.11.2 Training Data Pipeline Security

1. **Data Source Validation:** The Meridian Data Engineering team (for internally sourced data) or the Vendor Risk Manager (for externally sourced data) shall validate each data source for the AI training pipeline:
   - **Source Identity:** Confirmation of the identity and trustworthiness of the data provider.
   - **Source Integrity:** Confirmation that data has been received without unauthorized modification (verified via checksums or digital signatures).
   - **Consent and Use Rights:** Confirmation that data was collected and is being used in compliance with patient consent terms and applicable regulations.

2. **Data Poisoning Defense:** The AI/ML pipeline shall incorporate technical controls against data poisoning attacks:
   - **Outlier Detection:** Automated statistical outlier detection on ingested datasets; outlier triggers a review by a data scientist before the data enters the training set.
   - **Label Integrity Verification:** For supervised learning tasks, a random sample of 5% of labels shall be verified by a qualified clinician annotator (for externally labeled data).
   - **Differential Privacy Auditing:** Where differential privacy techniques are employed for training, the privacy budget (epsilon) shall be logged and audited per run.

#### 5.11.3 AI Component Vulnerability Management

1. **AI-Specific Vulnerability Database:** In addition to the general CVE/NVD feeds in Dependency-Track, Meridian subscribes to AI-specific vulnerability feeds, including:
   - MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems).
   - AVID (AI Vulnerability Database).
   - Vendor-specific advisories for foundation models used.

2. **AI Component SBOM Extension:** The SBOM for the Clinical AI Platform (extending the standard CycloneDX) shall include:
   - Model name, version, supplier.
   - Model architecture identifier.
   - Training data provenance reference (link to the Meridian Data Catalog record for the dataset).
   - Associated Model Card reference.

3. **Post-Market Monitoring (Article 17(1)(f)):** Meridian shall actively monitor the performance and security of deployed AI models in production:
   - **Model Drift Monitoring:** Automated statistical monitoring of model input distributions and output confidence scores against baseline; significant drift alerts routed to the Clinical AI ML team.
   - **Adversarial Input Monitoring:** Deployment of input anomaly detection (using a separate, simpler classifier) that flags inputs potentially crafted to deceive the primary model.
   - **Feedback Loop Integration:** User-reported (clinician) feedback on model behavior shall be collated, reviewed by the Clinical Safety Officer, and fed back into the model improvement and risk assessment process.

#### 5.11.4 Documentation for Regulatory Conformity

1. The Quality Management System (QMS) documentation (maintained in the Meridian Document Management System, Arena PLM) shall include specific supply chain security artifacts for the Clinical AI Platform:
   - **Supplier Qualification Records:** For every third-party AI component supplier, documented evidence of qualification (assessment results, certifications reviewed).
   - **Component Acceptance Criteria:** Defined criteria that an externally sourced AI component must meet before integration (accuracy threshold, robustness test results, absence of Critical vulnerabilities).
   - **Integration Verification Records:** Test records proving that each component was verified against its acceptance criteria before integration.
   - **Continuous Monitoring Logs:** Aggregated logs from runtime monitoring systems, demonstrating ongoing compliance.

2. These documents shall be maintained in the Technical Documentation file, which shall be available to the Notified Body (for CE marking) and to competent authorities upon request under Article 21 of the EU AI Act.

### 5.12 Incident Response – Supply Chain Events

#### 5.12.1 Detection and Declaration

A supply chain security incident is declared when there is credible evidence of:
- A compromised third-party software component deployed in a Meridian environment.
- A compromised vendor system that may have exposed Meridian data or allowed lateral movement.
- A successful software supply chain attack (e.g., dependency confusion, typosquatting, malicious package submission to an upstream registry).
- A hardware or firmware supply chain compromise.

Detection sources include automated pipeline alerts, vendor notifications, threat intelligence feeds, and bug bounty reports.

#### 5.12.2 Response Procedure

1. **Containment (Immediate, within first hour):**
   - The Incident Response Lead, upon declaration, shall direct the isolation of the affected system(s). For a compromised dependency, this may involve halting all CI/CD pipelines that reference the affected artifact and cordoning off affected Kubernetes nodes.
   - The compromised artifact or vendor connection shall be severed. If a specific dependency version is confirmed malicious, that version shall be immediately removed from the Meridian Internal Artifact Repository.

2. **Investigation (Ongoing):**
   - The Incident Response team, with Security Architecture and affected engineering teams, shall determine the scope of the compromise: which Meridian systems ran the compromised component, what data those systems had access to, and whether any indicators of compromise (IoCs) suggest lateral movement or data exfiltration.
   - The SBOM for affected systems shall be used to map the blast radius of the compromised component across all Meridian deployments.

3. **Notification (within applicable SLAs):**
   - **Legal & Compliance:** Notified immediately for assessment of regulatory breach notification obligations.
   - **Affected Customers:** Notified according to contractual SLA (generally within 72 hours for Tier 1 systems, per BAA terms).
   - **EU AI Act Competent Authority:** If the incident affects the Clinical AI Platform and presents a risk to health or safety of persons, the relevant market surveillance authority shall be notified in accordance with Article 73 of the EU AI Act.

4. **Remediation and Recovery:**
   - Replace the compromised component with a verified clean version or an alternative.
   - Rotate any credentials or secrets that may have been accessible to the compromised component.
   - Rebuild affected systems from known-good states.

5. **Post-Incident Review:**
   - Within **fifteen (15) calendar days** of incident closure, a formal post-incident review (PIR) shall be conducted. The PIR shall identify root causes, evaluate the effectiveness of existing supply chain controls, and recommend improvements.

## 6. Controls and Safeguards

### 6.1 Preventative Controls

| Control ID | Control Description | Implementation Details |
|---|---|---|
| **SC-PRE-01** | Dependency Approval Gate | New dependencies require formal approval via Backstage; approval includes automated and manual security review. |
| **SC-PRE-02** | Pipeline Vulnerability Gate (Build Breaker) | Critical CVEs in dependencies automatically fail the CI/CD pipeline, preventing artifact progression to staging/production. |
| **SC-PRE-03** | Artifact Code Signing | All production artifacts cryptographically signed; unsigned artifacts rejected by deployment orchestrator (ArgoCD). |
| **SC-PRE-04** | Hermetic Builds (Tier 1) | Tier 1 builds execute in network-isolated environments; all dependencies pre-fetched from internal repository. |
| **SC-PRE-05** | Branch Protection & Signed Commits | GitHub branch protection enforces mandatory peer review and signed commits on main and release branches. |
| **SC-PRE-06** | Vendor Security Assessment | All Tier 1-3 vendors undergo security assessment before contract execution; documented in ServiceNow GRC. |
| **SC-PRE-07** | Approved Base Image Policy | Only Meridian Hardened Alpine and Distroless base images permitted for production containers. |
| **SC-PRE-08** | Model Weight Verification | All AI model weights verified by cryptographic hash comparison before MLflow registration. |
| **SC-PRE-09** | Malicious Model Scanner | Serialized models scanned for embedded malicious code; integration with ClamAV and YARA rules. |

### 6.2 Detective Controls

| Control ID | Control Description | Implementation Details |
|---|---|---|
| **SC-DET-01** | Continuous SCA Scanning (Pipeline & Runtime) | Syft/Trivy in CI/CD; Aqua Security runtime SCA agents on Tier 1 Kubernetes clusters. |
| **SC-DET-02** | OWASP Dependency-Track Centralized Dashboard | All project SBOMs ingested and correlated against NVD, GitHub Advisory, and OSV.dev databases; daily digest to Security Architecture. |
| **SC-DET-03** | CI/CD Pipeline Audit Logging | All pipeline execution logs shipped to centralized SIEM (Splunk); alerts on non-standard pipeline modifications. |
| **SC-DET-04** | AI Model Drift Monitoring | Statistical monitoring of model inputs and outputs against baseline; automated alert threshold triggered at ±2 sigma deviation. |
| **SC-DET-05** | Vendor Compliance Monitoring | Annual check of vendor SOC 2/ISO 27001 status; automated alert if certificate expires or is revoked (via ServiceNow GRC). |
| **SC-DET-06** | Dependency Confusion Detection | Meridian Internal Artifact Repository configured to strictly scope internal packages; external registries monitored for packages with names matching Meridian's internal naming prefix. |

### 6.3 Corrective Controls

| Control ID | Control Description | Implementation Details |
|---|---|---|
| **SC-COR-01** | Dependency Rollback Procedure | Documented procedure for reverting to a previously validated dependency version; rollback can be initiated from Dependency-Track. |
| **SC-COR-02** | Automated Base Image Rebuild Pipeline | Renovate bot opens automated MRs for base image updates; pipeline rebuilds and re-scans base images monthly. |
| **SC-COR-03** | Vendor Incident Notification Process | Defined notification flow from vendor to Meridian SOC to affected product teams; documented in Meridian Incident Response Plan (SOP-ISEC-012). |
| **SC-COR-04** | Compromised Artifact Purge | Ability to immediately revoke a specific artifact version from JFrog Artifactory and trigger a Kubernetes webhook to evict running containers referencing that artifact. |

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | Metric | Target | Measurement Method | Reporting Cadence |
|---|---|---|---|---|
| **SC-KPI-01** | Mean Time to Remediate (MTTR) Critical Supply Chain Vulnerabilities | ≤ 24 hours | Dependency-Track calculates time from CVE disclosure to VEX status "Fixed." | Weekly operations report; Monthly ISMS review |
| **SC-KPI-02** | Mean Time to Remediate (MTTR) High Supply Chain Vulnerabilities | ≤ 7 calendar days | Dependency-Track VEX status transition time. | Weekly operations report; Monthly ISMS review |
| **SC-KPI-03** | Percentage of Production Artifacts with Valid SBOM | 100% | Jenkins/GitLab CI reports; audit by comparing artifact count to SBOM count in JFrog `sbom-repository`. | Weekly automated check; Monthly ISMS review |
| **SC-KPI-04** | Percentage of Artifacts Signed | 100% (Tier 1), ≥ 98% (all tiers) | ArgoCD admission controller metrics; Cosign verification logs in SIEM. | Weekly automated check; Monthly ISMS review |
| **SC-KPI-05** | Vendor Risk Assessment Completion Timeliness | ≥ 95% within SLA per tier | ServiceNow GRC `vendor_risk_assessment` table; time from intake to assessment completion. | Monthly Vendor Risk report |
| **SC-KPI-06** | Number of Exceptions Open for Supply Chain Controls | Trend toward zero | ServiceNow Exception Management module; count of open, non-expired exceptions related to SOP-ISEC-021. | Monthly ISMS review |
| **SC-KPI-07** | AI Model Integrity Verification Failures | 0 | MLflow Model Registry audit logs; counter increments on hash mismatch. | Immediate alert on non-zero; weekly zero-count confirmation |
| **SC-KPI-08** | Dependency-Track Unreviewed CVE Backlog | 0 for > 30 days | Dependency-Track "Portfolio" view filtered by "Unreviewed" and age > 30 days. | Weekly Security Architecture review |

### 7.2 Dashboard and Reporting Tools

| Dashboard | Location / Tool | Audience |
|---|---|---|
| **Supply Chain Security – CISO View** | Splunk Dashboard (pre-built from Dependency-Track + pipeline logs) | CISO, Security Leadership |
| **Dependency-Track Portfolio** | OWASP Dependency-Track Web UI | Security Architecture, Engineering Leads |
| **Vendor Risk Management Dashboard** | ServiceNow GRC > Vendor Risk > Dashboard | Vendor Risk Manager, CISO, Procurement |
| **SBOM Compliance Report** | JFrog Artifactory + custom Python reporting script (runs daily) | DevOps, Security Architecture |
| **AI Model Supply Chain Health** | MLflow + custom Streamlit dashboard | Clinical AI Engineering Lead, Security Architecture |

### 7.3 Reporting Cadence

| Report | Frequency | Audience | Content |
|---|---|---|---|
| **Supply Chain Security Metrics Report** | Monthly | CISO, CTO, VP Engineering | All KPIs; trend analysis; open exceptions summary; upcoming vendor re-assessments. |
| **Vendor Risk Quarterly Report** | Quarterly | Executive Leadership Team (CEO, CFO, CTO, CISO, General Counsel) | Tier 1 vendor status; significant new vendor onboardings; high-risk vendor findings. |
| **Technical Documentation (Article 11 EU AI Act) Update** | Per major release | Notified Body, QMS Manager | SBOM, AI component provenance, model card updates, vulnerability handling records. |
| **Board of Directors Cybersecurity Report** | Bi-annually | Board of Directors, Audit Committee | Executive summary of supply chain security posture; notable incidents; resource needs. |

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

Meridian recognizes that in certain circumstances, full compliance with this SOP may not be immediately achievable (e.g., a legacy system dependency cannot be upgraded due to incompatibility, or a critical vendor has an unexpired contract that predates current requirements). In such cases, a formal exception shall be required.

1. **Submission:** The requestor (typically the Engineering Manager or Product Manager) shall submit an **Information Security Policy Exception Request** through the ServiceNow GRC portal (ServiceNow GRC > Exceptions > Request New). The request shall include:
   - The specific SOP control(s) from which the exception is sought.
   - The system(s), vendor(s), or dependency/dependencies affected.
   - The business justification for the non-compliance.
   - A detailed description of compensating controls that will be implemented to reduce residual risk.
   - The proposed duration of the exception (maximum initial duration: **ninety (90) days**).

2. **Risk Assessment:** The Security Architecture Lead shall conduct a risk assessment of the requested exception, evaluating the effectiveness of compensating controls and the overall residual risk to Meridian.

3. **Approval Authority:**

| Risk Level of Exception | Approval Authority |
|---|---|
| **Critical Residual Risk** (e.g., unpatched Critical CVE in a Tier 1 clinical system dependency) | CISO (Rachel Kim) and VP, Clinical AI Engineering |
| **High Residual Risk** | CISO (Rachel Kim) |
| **Medium Residual Risk** | Security Architecture Lead |
| **Low Residual Risk** | Security Architecture Lead |

4. **Tracking and Expiration:** All approved exceptions shall be tracked in the ServiceNow Exception Management module. The exception owner shall be automatically reminded **thirty (30) days**, **seven (7) days**, and **one (1) day** before expiration. Exceptions that are not renewed through the same process shall automatically expire, and the system shall return to compliance within the remediation window associated with the underlying finding.

5. **Renewal:** An exception may be renewed for a maximum of one (1) additional period of ninety (90) days, subject to re-approval by the original authority. Beyond 180 total days, renewal requires CEO (Dr. Sarah Chen) approval and shall be reported to the Board Audit Committee.

### 8.2 Escalation Path

Events within the supply chain security domain shall be escalated according to the following path:

| Level | Event Trigger | Notification / Escalation Action |
|---|---|---|
| **Level 1 – Operational** | Pipeline build breaker due to Critical CVE; vendor certificate renewal failure. | Automated alert to responsible engineering team via Slack channel (`#sec-supply-chain-alerts`) and email. Team Lead has 24 hours to acknowledge. |
| **Level 2 – Management** | Level 1 event not acknowledged within SLA; vendor security incident reported; exception request denied and appealed. | Escalated to VP, Engineering and CISO via PagerDuty high-priority page. |
| **Level 3 – Executive** | Active supply chain attack confirmed; significant data breach involving supply chain vector; regulatory enforcement inquiry received. | Immediate escalation to the Meridian Incident Response Plan (SOP-ISEC-012) executive notification tree: CISO → CTO → CEO → General Counsel. |
| **Level 4 – Board/Regulatory** | Material business impact confirmed; mandatory regulatory notification triggered. | CEO notifies Board Chair; General Counsel manages regulatory engagement. |

## 9. Training Requirements

### 9.1 Role-Based Training

| Target Audience | Training Module | Required Frequency | Delivery Method |
|---|---|---|---|
| **All Engineering Staff** | SEC-101: Secure Software Supply Chain Fundamentals | Annually | Meridian LMS (Absorb); includes knowledge check assessment. Passing score ≥ 80%. |
| **All Engineering Staff** | SEC-102: Secure Dependency Management (practical lab covering SBOM generation, Dependency-Track, VEX authoring) | Annually | Instructor-led virtual workshop (2 hours); hands-on lab environment. |
| **DevOps / Platform Engineers** | SEC-201: Pipeline Security Hardening & SLSA Implementation | Annually | Advanced instructor-led workshop; exam-based certification required for pipeline admin access. |
| **Security Architecture Team** | SEC-301: Advanced Supply Chain Threats and Incident Response | Bi-annually | External training (e.g., SANS SEC522 or equivalent) or internal red-team exercise. |
| **Vendor Risk Managers & Procurement** | SEC-401: Vendor Security Assessment Methodology | Annually | On-demand LMS course; updated with each version of the Meridian VSRA template. |
| **Clinical AI Engineers** | SEC-501: AI Supply Chain Security (model provenance, poisoning defense, EU AI Act requirements) | Annually, plus per-major-release refresher | Instructor-led, developed jointly by Security Architecture and Clinical AI product team. |
| **All Employees** | SEC-AWARE: General Security Awareness, including module on recognizing supply chain social engineering and reporting suspicious vendor communications. | Annually | Meridian LMS; mandatory completion tracked, non-completion flagged to HR. |

### 9.2 Training Tracking and Compliance

1. Training completion records shall be maintained in the Meridian LMS (Absorb).
2. The CISO's office shall conduct a quarterly audit of training completion rates. Any individual who has not completed required training within **thirty (30) days** of their due date shall:
   - Be placed on a "Watch List" and receive a written reminder from their manager.
   - Have their access to specific tooling (pipeline configuration, deployment approval) revoked until training is completed (for SEC-201 and SEC-301, which gate privileged technical access).
3. New hires in engineering, security, and procurement roles shall complete the relevant supply chain security training modules within their first **thirty (30) days** of employment, as part of the standard onboarding curriculum.

## 10. Related Policies and References

### 10.1 Meridian Internal SOPs

| SOP ID | Title | Relationship to This SOP |
|---|---|---|
| SOP-ISEC-012 | Incident Response Plan | Governs incident declaration and response; invoked in Section 5.12. |
| SOP-ISEC-015 | Vulnerability Management Standard | Defines vulnerability remediation SLAs; referenced in Section 5.4. |
| SOP-ISEC-003 | Third-Party Risk Management Framework | Foundational framework for vendor risk assessment; this SOP operationalizes the software supply chain aspects. |
| SOP-ISEC-018 | Identity and Access Management | Governs PKI and code signing certificates used for artifact signing. |
| SOP-ISEC-022 | Secure Software Development Lifecycle (SSDLC) | Governs general SDLC security; this SOP provides detailed supply chain-specific procedures. |
| SOP-ISEC-030 | AI System Security and Compliance | Covers broader AI security; Section 5.11 of this SOP focuses specifically on AI supply chain aspects. |
| SOP-CO-005 | Procurement and Vendor Contracting | Defines the business process for procurement that triggers the security review in Section 5.1. |
| SOP-QMS-001 | Quality Management System – Clinical AI | Documents the QMS for MDR and EU AI Act compliance, referencing supply chain artifacts generated by this SOP. |

### 10.2 External Standards and Frameworks

| Standard / Framework | Identifier | Applicability at Meridian |
|---|---|---|
| NIST Special Publication 800-53, Revision 5 | Supply Chain Risk Management (SR) family | Core reference for supply chain controls |
| NIST Special Publication 800-161, Revision 1 | Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations | Used for Meridian's control mapping |
| NIST Special Publication 800-218 | Secure Software Development Framework (SSDF) v1.1 | Maps to Meridian SSDLC (SOP-ISEC-022) and this SOP |
| OWASP Top 10 CI/CD Security Risks | N/A | Used as a threat model input for Section 5.7 |
| SLSA (Supply-chain Levels for Software Artifacts) | SLSA v1.0 | Defined compliance levels in Section 5.5.2 |
| EU AI Act (Regulation 2024/1689) | Article 15, Article 17, Annex III | Binding for the Clinical AI Platform; Section 5.11 |
| ISO/IEC 27001:2022 | Annex A, Controls 5.19-5.22 (Supplier Security) | Referenced for ISMS scope; Meridian pursues ISO 27001 certification |
| SOC 2 Common Criteria | CC5.2, CC6.1, CC7.1, CC7.2, CC8.1 | Relevant for Meridian SaaS Platform audit scope |

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| 1.0 | 2021-03-15 | R. Kim | Dr. S. Chen | Initial release. Established foundational SBOM and vendor risk assessment procedures. |
| 2.0 | 2022-06-01 | R. Kim | Dr. S. Chen | Major revision: Added CI/CD pipeline security controls; introduced Dependency-Track for centralized SCA; added container image governance. |
| 3.0 | 2023-02-10 | Security Architecture Lead | R. Kim | Added artifact signing requirements (Cosign); introduced SLSA Level 2 requirement for all projects; expanded OSS governance. |
| 4.0 | 2024-08-15 | R. Kim, Director Legal & Compliance | Dr. S. Chen | Pre-EU AI Act readiness release. Added Section 5.11 AI/ML Supply Chain Security; updated SBOM to require NTIA minimum elements plus enrichment for clinical systems; introduced VEX requirements. |
| 5.0 | 2025-01-20 | R. Kim | Dr. S. Chen | Comprehensive revision to align with EU AI Act obligations effective date (progressive enforcement). Expanded AI-specific controls; added Article 15 and Article 17 mapping; refined RACI matrix; added AI-specific KPIs. |
| 5.1 | 2025-05-07 | Security Architecture Lead | R. Kim | Minor revision: Updated SBOM format requirements to CycloneDX 1.5; revised Approved Base Image list; updated SLA for dependency approval to 5 business days. |
| 5.2 | 2025-08-12 | R. Kim | Dr. S. Chen | Incorporated lessons learned from Q2 2025 tabletop exercise; adjusted incident escalation path; refined vulnerability remediation SLAs to clarify distinction between critical clinical AI components and general SaaS components. |
| 5.3 | 2025-10-07 | R. Kim | Dr. S. Chen | Current version. Updated to reflect EU AI Act enforcement commencement; added explicit Article 17(1)(f) post-market monitoring procedures; updated Vendor Risk Classification Matrix to align with updated regulatory guidance; extended SBOM retention for medical device software to 7 years. |

---

**Document Control:** This SOP is controlled by the Meridian Information Security Management System (ISMS). Any printed copy is uncontrolled unless stamped "CONTROLLED COPY." The authoritative version is maintained in the Meridian Policy Management System (Confluence Data Center).