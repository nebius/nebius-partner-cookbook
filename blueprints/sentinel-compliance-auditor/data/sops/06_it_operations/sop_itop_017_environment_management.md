---
sop_id: "SOP-ITOP-017"
title: "Environment Management"
business_unit: "IT Operations & Infrastructure"
version: "4.2"
effective_date: "2025-03-11"
last_reviewed: "2026-03-11"
next_review: "2026-09-20"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Environment Management

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the governance framework, operational procedures, and technical controls for managing all software development, testing, staging, and production environments across Meridian Health Technologies, Inc. The purpose is to ensure the confidentiality, integrity, and availability of Meridian’s systems and data throughout the software development lifecycle (SDLC), to maintain strict separation of duties and data between environments, and to demonstrate compliance with applicable regulatory and contractual obligations.

### 1.2 Scope
This SOP applies to:

- **All Environments:** Development (DEV), Integration Testing (INT), User Acceptance Testing/Staging (UAT/STAGE), Production (PROD), and Disaster Recovery (DR) environments hosted on Amazon Web Services (AWS, primary) and Microsoft Azure (DR).
- **All Business Units:** Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.
- **All Data Classifications:** including but not limited to Protected Health Information (PHI), Personally Identifiable Information (PII), Payment Card Industry (PCI) data, confidential intellectual property (including model weights and training data), and internal communications.
- **All Personnel:** Full-time employees, contractors, consultants, and third-party vendors who interact with or manage Meridian environments, including those at global offices in London, Berlin, Singapore, and Toronto.

### 1.3 Out of Scope
This SOP does not cover end-user device management (refer to SOP-ISEC-003), physical data center security (not applicable; cloud-native infrastructure governed by AWS/Azure shared responsibility models), or the content of business continuity and disaster recovery plans (refer to SOP-ITOP-022), though it governs the environment configuration to support those plans.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **AWS Account** | A logically isolated container for AWS resources, used as the primary boundary for environment separation (e.g., `meridian-prod`, `meridian-nonprod`). |
| **Baseline** | A formally reviewed and agreed-upon specification of a configuration item (e.g., an Amazon Machine Image, a database schema, a set of IaC templates) that serves as the basis for further development and can be changed only through formal change control procedures. |
| **Change Advisory Board (CAB)** | A cross-functional body responsible for reviewing and approving all significant changes to Meridian environments. |
| **CI/CD Pipeline** | Continuous Integration / Continuous Deployment pipeline, the automated series of steps used to build, test, and deploy code and infrastructure changes. |
| **Data Masking** | The process of transforming data to obscure personally identifiable or other sensitive information while preserving the data’s referential integrity and statistical distribution for development and testing. |
| **Environment Refresh** | The process of replacing a non-production environment's dataset with a more recent copy of data from a source production environment, followed by mandatory masking. |
| **Infrastructure as Code (IaC)** | The process of managing and provisioning infrastructure through machine-readable definition files (Terraform, AWS CloudFormation) rather than physical hardware configuration or interactive configuration tools. |
| **Just-In-Time (JIT) Access** | A security practice where privileged access to an environment is granted on-demand for a limited duration, rather than standing access. |
| **Non-Production Environment** | Any environment not designated as PROD. Specifically, DEV, INT, and UAT/STAGE environments. |
| **Production (PROD) Environment** | The live computing environment where authorized end-users (patients, providers, payers) interact with Meridian's operational systems and data. |
| **Segregation of Duties (SoD)** | An internal control designed to prevent error and fraud by ensuring that no single individual has the authority to perform two or more conflicting duties within a single process. |

## 3. Roles and Responsibilities

The following RACI (Responsible, Accountable, Consulted, Informed) matrix defines the roles and responsibilities for the execution of this SOP.

| Activity / Task | VP of IT Ops (Samantha Torres) | VP of Engineering (David Park) | Environment Manager | DevSecOps Engineer | Product Engineering Team | Compliance Officer (Thomas Anderson) | CAB | CISO (Rachel Kim) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Policy Ownership & Review** | A, R | C | R | I | I | C | I | C |
| **Architecture & IaC Design** | I | A | R | R | C | I | I | C |
| **Environment Provisioning** | I | C | A | R | I | I | I | I |
| **Data Masking Procedure** | I | I | A | R | I | C | I | C |
| **Environment Refresh Execution** | I | C | A | R | C | I | I | I |
| **Access Control Management** | I | I | R | A | I | I | I | C |
| **Access Approvals** | A | A | I | I | I | I | I | I |
| **Deployment to UAT/STAGE** | I | C | C | A | R | I | I | I |
| **Deployment to PROD** | I | A | C | R | C | I | R | C |
| **Monitoring & Alerting** | I | I | R | A | I | C | I | I |
| **Exception Management** | A | A | R | I | C | R | C | C |
| **Annual Audit Support** | R | R | R | I | C | A | I | I |

- **VP of IT Operations (Samantha Torres):** Accountable for the operational integrity of all environments and the overall execution of this SOP.
- **VP of Engineering (David Park):** Accountable for the technical architecture and the SDLC pipeline that interacts with environments.
- **Environment Manager:** A dedicated role within IT Operations responsible for orchestrating environment maintenance, refresh cycles, and baseline management.
- **DevSecOps Engineer:** Responsible for the implementation and maintenance of IaC, CI/CD pipelines, security scanning automation, and access control mechanisms.
- **CISO (Rachel Kim):** Consulted on all security-related controls, risk assessments, and exception handling.
- **Compliance Officer (Thomas Anderson):** Consulted on regulatory requirements and responsible for providing evidence during internal and external audits.

## 4. Policy Statements

The following high-level policy statements establish the minimum mandatory requirements for environment management at Meridian. All procedures and controls detailed in this SOP derive from these policies.

### 4.1 Strict Environment Segregation
- 4.1.1 Production environments must be logically and physically separated from all non-production environments. Separation must be maintained at the AWS account level: `meridian-prod` AWS Organization OU shall not share any security groups, IAM roles, or network connectivity with the `meridian-nonprod` AWS Organization OU, except via approved, JIT-only API gateways.
- 4.1.2 Production data, including all PHI, PII, and PCI data, shall never be used for development or testing purposes. All data in DEV, INT, and UAT environments must be masked or synthetically generated.
- 4.1.3 Code development, testing, and validation activities are strictly prohibited in the PROD environment. The PROD environment shall only contain compiled, verified, and CAB-approved software releases.

### 4.2 Secure by Default
- 4.2.1 All environments shall be provisioned using approved IaC templates (Terraform) from the `meridian-corp/iac-templates` repository. Manual configuration of any cloud resource is prohibited.
- 4.2.2 All inter-service communication within an environment must be whitelisted at the network and service-mesh level. Open security groups (e.g., `0.0.0.0/0` for ingress) are prohibited in all environments.
- 4.2.3 Logging and monitoring agents (Datadog, CrowdStrike Falcon) shall be embedded in the base Amazon Machine Image (AMI) and automatically enabled upon instance launch in any environment.

### 4.3 Full Traceability
- 4.3.1 Every change in a non-production environment must be traceable to an approved Jira issue. Every change in the PROD environment must be traceable to a Jira issue linked to a CAB-approved Request for Change (RFC).
- 4.3.2 The CI/CD pipeline (GitHub Actions, ArgoCD) is the sole mechanism for deploying application code and configuration changes. It must cryptographically sign all artifacts and record an immutable deployment log.
- 4.3.3 All configuration baselines for environment infrastructure must be version-controlled and subject to the same peer-review policy as application code, per SOP-SDLC-002.

## 5. Detailed Procedures

The following step-by-step procedures operationalize the policy statements above.

### 5.1 Environment Provisioning and Configuration
This procedure details the creation of a new non-production environment (e.g., a new feature-development environment). All environments follow an identical provisioning process, with specific sizing and service flags determined by an environment profile.

| Step | Action | Responsible Party | Tool/System |
| :--- | :--- | :--- | :--- |
| 1 | **Initiate Request:** Create a `REQ-ENV-XXX` Jira ticket using the "Environment Provisioning" template. Include the `environment_profile` (e.g., `dev-standard`, `stage-full`), requested TTL (Time To Live), and charge code. | Engineering Manager | Jira Service Management |
| 2 | **Profile Validation:** The Environment Manager reviews the ticket for completeness and approves/denies the request within 4 business hours. The `environment_profile` dictates the immutable specifications for instance sizes, RDS class, node count, and AWS region (`us-east-1` for North America, `eu-west-1` for EU). | Environment Manager | Jira Service Management |
| 3 | **IaC Execution:** Upon approval, a webhook triggers the `meridian-corp/iac-environments` GitHub Actions pipeline. The DevSecOps Engineer reviews the automatically generated Terraform plan and merges the PR. | DevSecOps Engineer | GitHub, Terraform Cloud |
| 4 | **Automated Provisioning:** Terraform applies the configuration, creating the new AWS account with VPC, subnets, EKS cluster, RDS instances (PostgreSQL/Aurora), Redis clusters, and Kafka topics, all based on the baseline AMI and container images. | Automation | Terraform Cloud, AWS |
| 5 | **Security Bootstrap:** The pipeline automatically enrolls the new environment into Meridian’s security fabric: CrowdStrike Falcon sensor, AWS GuardDuty, AWS Inspector, and a Datadog monitoring agent. | Automation | AWS, CrowdStrike, Datadog |
| 6 | **Service Deployment:** A baseline version of all Meridian microservices (from `meridian-api/main`, `meridian-ml-serving/main`) is deployed from the artifact repository (JFrog Artifactory) to the empty EKS cluster via ArgoCD. | Automation | Artifactory, ArgoCD |
| 7 | **Smoke Test & Handoff:** An automated suite of smoke tests runs to ensure basic service health. Upon passing, the Jira ticket is updated with environment endpoints and credentials, and ownership is handed off to the requesting Engineering Manager. | Automation | Selenium, Jira |

### 5.2 Data Masking and Sanitization (Non-Production Environments)
This is the most critical procedure for environment management, ensuring compliance with data protection requirements. This procedure is mandatory before any production-derived data can be placed into a non-production environment.

- 5.2.1 **Policy Enforcement:** The `meridian-data-pipeline` contains a functional gate. Any job attempting to copy data from a source tagged `PROD` to a destination tagged `NONPROD` will automatically fail with a fatal error unless it invokes the registered `DataMaskingService`. This service is a gRPC microservice that acts as a mandatory proxy.

- 5.2.2 **Masking Algorithm Inventory:** The `DataMaskingService` applies the following transformations based on a data classification schema defined in the `meridian-data-governance` repository:
    1.  **PHI (Protected Health Information):**
        - `patient.first_name`, `patient.last_name`: Replaced with consistent but synthetic values from a pre-approved dictionary of 1,000,000 common names, seeded by `sha256(patient.mrn)`.
        - `patient.dob`: Jittered by ±15 days, preserving age distribution to the quarter.
        - `patient.mrn`: Replaced with a UUIDv5, using the `meridian-nonprod-phi` namespace UUID (`a1b2c3d4-...`).
        - `address.line1`, `address.zip`: Replaced with geospatially-consistent but synthetic addresses. ZIP codes are retained but jittered across the same Census Block Group.
        - All other notes, procedures, and diagnosis codes are tokenized using a format-preserving encryption (FPE) key stored exclusively in AWS Secrets Manager (`nonprod/data-masking-key`).
    2.  **PII (Personally Identifiable Information):**
        - `email`: Replaced with `user+<sha256(original_email)[:8]>@meridian-test.internal`.
        - `ssn`, `drivers_license`: Overwritten with `NULL`.
    3.  **PCI (Payment Card Industry Data):**
        - All PCI data fields are replaced with token `4111111111111111` or a valid test token from Stripe's testing library, regardless of the original value's tokenization status.
    4.  **Model Weights & IP:**
        - Proprietary model weights or algorithmic source code are never included in a data refresh. They are managed separately as code artifacts.

- 5.2.3 **Validation Job:** After the `DataMaskingService` job completes, a secondary automated validation job scans the target non-production snapshots.
    1.  **Rule-Based Scan:** Scans every field tagged as `PII` or `PHI` in the Meridian Meta-Dictionary. Any field with >0% raw content match against known patterns (e.g., valid SSN pattern, known MRN format) causes an immediate job failure and quarantines the target snapshot.
    2.  **Re-identification Risk Test:** A sample of 1,000,000 records is run against a public and private data broker API simulation. If any individual can be re-identified by linking the masked data to external datasets, the job fails.

### 5.3 Environment Refresh Cycle
Non-production UAT/STAGE environments are refreshed on a 60-day cycle (or the first Monday after a major production release, whichever is sooner) to maintain structural and statistical fidelity with PROD.

| Step | Action | Responsible Party | Expected Duration |
| :--- | :--- | :--- | :--- |
| 1 | **Change Ticket Initiation:** A standard RFC, `RFC-REFRESH-UAT-YYYYMMDD`, is auto-generated by Jira on a pre-set schedule, 14 calendar days before the refresh window. The CAB approves this as a standard change via email vote within 2 business days. | CAB Chair | 2 Days |
| 2 | **Pre-Refresh Communication:** The Environment Manager sends a "Planned Non-Production Downtime" notification to all engineering teams via Slack (`#eng-announce`) and email (`engineering-all@meridian.com`) 7 calendar days and 24 hours before the event. | Environment Manager | 15 Minutes |
| 3 | **Configuration Freeze:** 12 hours before the refresh, all deployments to the source PROD and target UAT environments are halted. A “Configuration Freeze” flag is enabled in the ArgoCD dashboard. | DevSecOps Engineer | 12 Hours |
| 4 | **Snapshot & Transfer:** An automated AWS Backup Agent triggers a snapshot of the PROD RDS instances and EBS volumes. The snapshot is encrypted with the `nonprod-backup-kms-key` and transferred cross-account to the `meridian-nonprod` OU via an isolated, AWS PrivateLink-powered S3 gateway. | Automation | approx. 4-6 Hours |
| 5 | **Data Masking Execution:** The `DataMaskingService`, hosted exclusively in a secured `meridian-tools` AWS account, detects the new snapshot and begins the full masking procedure as defined in Section 5.2.2. | Automation | approx. 12 Hours |
| 6 | **Validation:** The automated validation job (Section 5.2.3) runs. On success, a secure message is sent to the Environment Manager. On failure, the snapshot is quarantined, the entire refresh job terminates, and a P1 incident is automatically declared for the Data Engineering and Security teams. | Automation | approx. 2 Hours |
| 7 | **Environment Re-Hydration:** The validated, masked dataset is restored to the UAT RDS instances, replacing the previous dataset. EKS pods are cycled to connect to the new data source. | DevSecOps Engineer | approx. 3 Hours |
| 8 | **Post-Refresh Smoke Test & Lift Freeze:** An automated integration test suite runs. Upon successful completion, the "Configuration Freeze" flag is lifted, and a "UAT Refresh Complete" notification is sent to the teams. | Automation | approx. 1 Hour |

### 5.4 Access Controls and Lifecycle
This procedure establishes a Zero Trust, Just-in-Time (JIT) access model for all environments.

- 5.4.1 **Standing Access Prohibition:** No standing IAM user, role, or group shall have administrative or write-access (`iam:PassRole`, `ec2:*`, `s3:Put*`) to any environment, regardless of tier. The only standing permission is `ReadOnlyAccess` for the DevSecOps team's break-glass accounts, which triggers an immediate, high-severity alert in Datadog upon any API call.

- 5.4.2 **Just-in-Time (JIT) Access Request:**
    1.  **Initiation:** A Requestor submits an access request via the `meridian-access-bot` in Slack: `/access env:UAT resource:rds-analytics role:read-only duration:3h justification: "Debugging slow query in ticket PROJ-4562"`.
    2.  **Automated Risk Scoring:** The `meridian-access-bot` evaluates the request's risk score based on the `(Role_Privilege x Environment_Sensitivity)`. Access to DEV `read-write` is low risk; access to UAT `write` on PHI-scoped services is high risk.
    3.  **Approval Workflow:**
        - **Low Risk:** Automatically approved.
        - **Medium Risk:** Approval required from the Requestor’s direct Manager.
        - **High Risk:** Dual approval required from Manager and an Environment Manager.
        - **Critical Risk (e.g., PROD write):** Dual approval required from the relevant VP (Engineering/IT Ops) and the CISO (Rachel Kim). This triggers a synchronous change window.
    4.  **Federation & Provisioning:** Upon approval, the pipeline creates a temporary, scoped-down IAM role for the Requestor’s identity provider (Okta) group. The role’s trust policy is updated to allow the Requestor to assume it for the exact duration specified.
    5.  **Audit & Auto-Revocation:** All actions taken via the assumed role are streamed to AWS CloudTrail and Datadog. At the end of the duration, a scheduled job automatically revokes the trust policy, effectively cutting access. The Requestor receives a Slack notification: "Your access to `UAT:rds-analytics` has expired."

### 5.5 Code Promotion and Deployment Procedure
This enforces the SDLC promotion path: DEV → INT → UAT/STAGE → PROD.

| Environment | Entry Gate | Deployment Trigger | Validation | Approver |
| :--- | :--- | :--- | :--- | :--- |
| **DEV** | Feature branch merge to `develop` | Automatic on commit | Unit Tests, Linting | Automation |
| **INT** | Release branch creation (`release/vX.Y.Z`) | Automatic on branch creation | Integration Tests, SAST (SonarQube), SCA (Snyk) | DevOps Lead |
| **UAT/STAGE** | Release branch merge to `main` | Manual trigger by QA Lead in GitHub | Full Regression Suite, DAST (Invicti), Masking Validation, Performance Tests (LoadRunner) | QA Lead & Product Manager |
| **PROD** | Successful UAT validation | Manual trigger by DevSecOps Engineer via GitHub Deployments API, only during a pre-defined Change Window (Tue/Thu, 00:00-04:00 ET) | Canary Deployment, PROD Smoke Test, Automated Rollback Triggers | CAB & VP of Engineering |

- 5.5.1 **Artifact Promotion:** Artifacts (Docker images, IaC templates) must be promoted through the pipeline, not rebuilt. The SHA256 digest of the container image tested in UAT must be the exact same digest deployed to PROD. This is enforced by an admission controller in the PROD-EKS cluster that rejects any image digest not co-signed by the QA lead and the GitHub Actions pipeline attestation.

- 5.5.2 **Secrets Management:** The CI/CD pipeline never packages secrets (database passwords, API keys) with code artifacts. All secrets, including those for PROD, INT, and UAT, are fetched at runtime from AWS Secrets Manager or HashiCorp Vault based on the agent's declared environment context. A misconfigured agent that, for example, attempts to fetch PROD secrets while running in an INT cluster will fail a mutual TLS (mTLS) authentication challenge orchestrated by an environment-specific `meridian-envoy` proxy.

## 6. Controls and Safeguards

This section defines the specific technical and administrative controls implemented to meet SOC 2 CC7.1 and CC7.2 criteria and related internal security standards.

### 6.1 Technical Controls

| Control ID | Control Description | Implementation Detail | SOC 2 Criteria |
| :--- | :--- | :--- | :--- |
| **TEC-ENV-001** | **Network Micro-Segmentation** | All environments run on separate AWS accounts within distinct Organizational Units (OUs). Inter-account network connectivity is blocked by default via Service Control Policies (SCPs). Approved paths (e.g., PROD-to-DR replication) use dedicated, mutually authenticated mTLS tunnels over AWS PrivateLink, with flows logged to Datadog. | CC6.1, CC6.6 |
| **TEC-ENV-002** | **Immutable Infrastructure** | All configuration changes must be made in Terraform. AWS Console write-access is denied via IAM policies, even during JIT access. Any drift between the Terraform state and reality triggers a `Critical Non-Compliance` alarm in Datadog, and the resource is scheduled for automatic remediation (re-alignment with IaC) within 1 hour. | CC7.1, CC7.2 |
| **TEC-ENV-003** | **Production Bastion Host** | There are no open SSH ports in PROD. A single, hardened, session-managed AWS Systems Manager (SSM) Bastion Host is the only approved mechanism for interactive troubleshooting in PROD. All SSM sessions are recorded, with the command-level logs streamed to the SIEM (Splunk). | CC6.1, CC6.2 |
| **TEC-ENV-004** | **Automated Drift Detection** | An AWS Config rule, deployed organization-wide, runs continuously to detect any resource not provisioned or managed by Terraform Cloud. A custom AWS Lambda function, `meridian-config-rule-evaluator`, aggregates these findings and posts a compliance score to a centralized dashboard. | CC7.1 |
| **TEC-ENV-005** | **Cryptographic Component Attestation** | The CI/CD pipeline (GitHub Actions) uses Sigstore Cosign to sign each container image and its associated SBOM (Software Bill of Materials). The admission controller in each EKS cluster (`meridian-policy-controller`) validates this signature before allowing the pod to schedule. PROD clusters reject any non-attested images. | CC7.1, CC7.2 |
| **TEC-ENV-006** | **PHI Environment Fingerprinting** | A dedicated agent in every Kubernetes worker node fingerprints the operating environment by checking its AWS Account ID, OU membership, and a specific, immutable resource tag (`data-classification`). Any workload tagged as `PHI-eligible` that attempts to schedule on a non-PROD worker node with an unmasked `PHI-eligible` volume is forcefully evicted by the `meridian-policy-controller`. | CC6.1 |

### 6.2 Administrative Controls

| Control ID | Control Description | Implementation Detail | SOC 2 Criteria |
| :--- | :--- | :--- | :--- |
| **ADM-ENV-001** | **Quarterly Access Re-Certification** | On the first business day of each quarter, the CISO (Rachel Kim) and VP of IT Ops (Samantha Torres) must receive a report from the `meridian-access-bot` listing all user and service accounts with any standing permissions to non-development environments. The report owner (Environment Manager) must attest that all accounts are still necessary and appropriately scoped. Non-attested accounts are automatically terminated after 14 days. | CC6.1, CC6.2 |
| **ADM-ENV-002** | **Annual Penetration Testing** | A SOC 2 Type II-certified external firm performs an annual, gray-box penetration test focusing on environment escalation paths (e.g., can access to a DEV service compromise a PROD service?). The VP of Engineering (David Park) is the Responsible party for all remediation items, which must be tracked in Jira as SIRs (Security Incident Reports) with a criticality-adjusted SLA (maximum 90 days for High findings). | CC7.4, CC7.5 |
| **ADM-ENV-003** | **Formal Change Management for PROD** | All PROD deployments are governed by a strict RFC process. The RFC must include a risk assessment (Business Impact, Technical Complexity, Back-Out Plan), a deployment runbook, and explicit approval from the CAB. No single individual may approve and execute a PROD deployment (SoD enforcement). | CC7.1, CC7.2 |
| **ADM-ENV-004** | **Vendor Security Assessments** | Any third-party vendor with tools integrated into our SDLC pipeline (e.g., Snyk, SonarQube, HashiCorp) must complete Meridian’s Third-Party Risk Management questionnaire, including evidence of their own SOC 2 Type II certificate, before the contract is fully executed and the tool is integrated into any environment. | CC9.2 |

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs)
Metrics are visualized on the central `IT Operations - Environment Health` Datadog dashboard, with read-only access for all Engineering personnel.

| Metric ID | Metric Name | Target | Measurement Period | Escalation Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **KPI-017-01** | **Environment Provisioning Lead Time** | < 8 hours from approved Jira ticket to Environment Ready | Monthly Average | > 12 Hour Avg for 2 consecutive weeks |
| **KPI-017-02** | **Refresh Cycle Success Rate** | 100% | Per Refresh | Any Failure |
| **KPI-017-03** | **Mean Time to Detect (MTTD)** | < 5 minutes for P1/P2 events | Real-time | > 10 Minutes |
| **KPI-017-04** | **Data Masking Validation Pass Rate** | > 99.9% | Per Job Run | < 99.9% |
| **KRI-017-01** | **PROD Deployments Outside Change Window** | 0 | Monthly Rolling | > 0 |
| **KRI-017-02** | **Configuration Drift Instances (Unremediated)** | 0 | Weekly | > 0 (Immediate P3 Incident) |
| **KRI-017-03** | **Cross-Environment Access Attempts** | 0 | Continuous | > 0 (Immediate P2 Security Incident) |

### 7.2 Reporting Cadence
- **Weekly Operational Report:** The Environment Manager generates an automated report from Jira/Datadog, summarizing RFC approval rates, refresh cycle status, lead times, and any unremediated drifts. Shared with David Park and Samantha Torres.
- **Monthly Management Review (MMR):** A formal MMR covering all environment management metrics—including KPIs, KRIs, exception statuses, and change management trends—is presented to the CISO and CTO. This is recorded as evidence for SOC 2 management review controls.
- **Quarterly Audit Review:** The Compliance Officer (Thomas Anderson) extracts an immutable evidence pack from the systems (Jira audit logs, Datadog dashboards, Terraform state history) to provide external auditors, demonstrating the operating effectiveness of the controls within this SOP.

## 8. Exception Handling and Escalation

### 8.1 Exception Handling
Any request to deviate from a policy statement or procedural step in this SOP must be handled through the formal Risk Exception Process.

| Step | Action | Responsible Party | Timeline |
| :--- | :--- | :--- | :--- |
| 1 | **Initiate Exception Ticket:** Using the `SEC-EXCP` Jira issue type, the Requestor details the specific section (e.g., 5.1.2), the justified business need, the scope of the deviation (which systems, data), compensating controls, and a requested expiration date (maximum 90 days). | Requestor | N/A |
| 2 | **Technical and Business Assessment:** Sandra Torres (IT Ops VP) assesses the operational impact and proposed compensating controls. The Compliance Officer (Thomas Anderson) evaluates the regulatory impact against applicable frameworks. | VP IT Ops, Compliance Officer | 5 Business Days |
| 3 | **CISO Review:** Rachel Kim reviews the cumulative risk profile of the request. She may require additional, real-time compensating technical controls or a shortened expiration date. | CISO | 2 Business Days |
| 4 | **Approval & Tracking:** If approved, the exception is logged in the `Environment Exceptions Register`, a Google Sheet linked from the main Datadog dashboard. The ticket is linked to the Register entry. | Compliance Officer | N/A |
| 5 | **Expiration and Re-Review:** 5 business days before the Jira ticket’s due date, an automated notification is sent to the Requestor and the CISO team. The exception must be formally re-reviewed and re-approved if needed, or it lapses, requiring the Requestor to return to compliance immediately. | Automation | 5 Days Before Expiry |

### 8.2 Escalation Paths
- **Operational Escalation:** For a failed refresh cycle or provisioning delay beyond SLA, the incident is escalated to the VP of IT Ops (Samantha Torres) and a war-room is initiated.
- **Security Escalation:** Any confirmed instance of PROD data in a non-prod environment (masking failure), unauthorized PROD access, or a detected configuration drift that introduces a new vulnerability triggers the **Information Security Incident Response Plan (SOP-ISEC-001)**. The CISO (Rachel Kim) is the first point of contact, and the incident is managed on a separate, secure out-of-band communication channel.

## 9. Training Requirements

Meridian IT personnel and Engineering staff involved in environment management, SDLC, or who have privileged access to any non-development environment must complete the following training.

| Training Module | Target Audience | Frequency | Delivery Method | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **ENV-MGMT-101: Environment Management Principles** | All IT Ops, DevSecOps, Senior Engineers | Onboarding, then Annually | LMS (Workday) Course & Assessment | VP of IT Ops |
| **ENV-SEC-201: Secure SDLC & PHI Isolation** | All Engineering, QA, Product (as applicable) | Onboarding, then Annually | LMS Course & Live Workshop for `main` branch committers | CISO Office |
| **ENV-TOOLS-301: Practical IaC & JIT Workshop** | IT Ops, DevSecOps | Onboarding & Bi-Annually | Hands-on lab in a dedicated training AWS sandbox account | Environment Manager |

- **Competency Verification:** All LMS courses must conclude with a mandatory assessment requiring a score of 80% or higher to pass. The DevSecOps practical workshop is pass/fail based on successfully provisioning a standard web service from Terraform and accessing it through a JIT access request.
- **Training Tracking:** Completion records are automatically recorded in Workday. The Compliance Officer (Thomas Anderson) pulls a training compliance report for all assigned personnel quarterly. The VP of IT Operations is responsible for enforcing training compliance, with non-completion after 30 days of assignment resulting in temporary suspension of access to non-production environments until the training is completed.

## 10. Related Policies and References

This SOP is part of Meridian’s integrated policy framework and should be read in conjunction with the following internal and external documents.

| SOP-ID / Ref | Title | Relationship |
| :--- | :--- | :--- |
| **SOP-ISEC-002** | Access Management and Identity Governance | Defines the Okta master user identities and JIT approval groups referenced in this SOP's access procedures. |
| **SOP-SDLC-002** | Secure Software Development Lifecycle | Defines the code branching strategy, SAST/DAST requirements, and artifact signing policy that feeds into our deployment procedures. |
| **SOP-ITOP-022** | Disaster Recovery & Business Continuity | Governs the PROD-to-DR replication procedures and DR environment activation, which are a special case of environment refresh. |
| **SOP-ISEC-001** | Information Security Incident Response | The mandatory escalation procedure invoked by Section 8.2 of this SOP. |
| **SOP-PRIV-009** | Data Classification and Handling | Defines the data classification schema (PHI, PII, PCI) that the `DataMaskingService` relies upon. |
| **MERIDIAN-TMP-017-A** | Environment Provisioning Request Template | The formal Jira template referenced in procedure 5.1. |
| **MERIDIAN-TMP-017-B** | Request for Change (RFC) Template | The formal Jira template required for all PROD deployments and environment modifications. |
| **SOC 2 TSC 2017** | Trust Services Criteria (CC6 Series, CC7 Series) | The core framework for the logical and physical access controls, system operations, and change management controls detailed throughout this SOP. |
| **NIST SP 800-53 Rev. 5** | Security and Privacy Controls | Informative reference for control language, particularly from the CM (Configuration Management) and AC (Access Control) families. |

## 11. Revision History

| Version | Date | Author / Editor | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2021-05-20 | Sarah Jenkins (Former VP IT Ops) | Initial document creation. Established core environment separation and deployment procedures. |
| 2.0 | 2022-10-12 | Kevin Park (DevSecOps) | Major revision. Introduced IaC-based provisioning and the `DataMaskingService` proxy model. Formalized refresh cycle. Shifted from static IAM users to JIT access model. |
| 3.0 | 2023-08-01 | Aisha Chen (Compliance Officer) | Update in response to SOC 2 Type II audit findings. Added detailed Controls and Safeguards section (Section 6). Formalized Key Performance Indicators (KPIs) and the Monthly Management Review (MMR) reporting cadence. Refined exception handling to include mandatory expiration. |
| 4.0 | 2024-05-15 | Samantha Torres (VP IT Ops) | Updated to align with HealthPay PCI compliance requirements. Added `meridian-policy-controller` for EKS admission control. Expanded Section 5.4 on access controls to include Critical Risk dual-approval flow. Architectural update to Azure DR. |
| 4.1 | 2024-11-01 | Liam O'Brien (DevSecOps) | Minor revision. Updated the list of approved IaC module versions to `v2.3.x`. Added `meridian-envoy` proxy for mTLS secret fetch validation in Section 5.5.2. Refined Datadog dashboard links for the new environment health monitor. |
| 4.2 | 2025-03-11 | Samantha Torres (VP IT Ops) | Bi-annual review. Updated roles to reflect organizational changes (David Park as Approver). Incorporated NIST SP 800-53 Rev 5 references. Revised KPI-017-01 lead time target down to 8 hours, reflecting pipeline optimization. Clarified the vendor risk assessment process. No structural changes. |