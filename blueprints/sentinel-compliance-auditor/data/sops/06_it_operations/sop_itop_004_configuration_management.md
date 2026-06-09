---
sop_id: "SOP-ITOP-004"
title: "Configuration Management"
business_unit: "IT Operations & Infrastructure"
version: "4.2"
effective_date: "2024-12-21"
last_reviewed: "2025-08-15"
next_review: "2026-02-04"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Configuration Management

**SOP-ID:** SOP-ITOP-004
**Version:** 4.2
**Effective Date:** 2024-12-21
**Owner:** Samantha Torres, VP of IT Operations
**Approver:** David Park, VP of Engineering

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, processes, and controls for Configuration Management (CM) across all technology assets owned, operated, or utilized by Meridian Health Technologies, Inc. The purpose of this SOP is to ensure that all configuration items (CIs) within the Meridian technology estate are identified, controlled, tracked, and maintained in a known, consistent, and verifiable state throughout their lifecycle. Effective configuration management is foundational to Meridian's ability to deliver secure, reliable, and compliant services across its Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the underlying Meridian SaaS Platform.

This SOP directly supports:
- The availability and integrity commitments outlined in Meridian's SOC 2 Type II certification, ensuring that changes to production systems do not introduce unauthorized or unintended degradation.
- The security and privacy requirements of HIPAA, ensuring that configurations affecting electronic Protected Health Information (ePHI) are managed and auditable.
- The risk management and model governance requirements of SR 11-7 for HealthPay Financial Services, ensuring that model operational environments are controlled.
- The technical documentation and traceability requirements for high-risk AI systems under the EU AI Act.
- The foundational control objectives of the NIST AI Risk Management Framework (AI RMF) adopted by the Board-level AI Governance Committee.

### 1.2 Scope

This SOP applies to all configuration items that constitute, support, or interface with the products, services, and internal operations of Meridian Health Technologies. The scope encompasses the following domains, platforms, and environments:

**In-Scope Environments:**
- **Production:** All environments serving live traffic for Meridian products, hosted in AWS us-east-1 (primary) and eu-west-1 (EU data residency).
- **Staging:** Production-like environments used for pre-release validation, also hosted in AWS.
- **Disaster Recovery (DR):** Azure-based warm standby environments for critical Tier-1 services.
- **Development:** Environments used for active software development and unit testing (subject to a subset of controls).
- **Corp-IT:** Internal corporate systems supporting Meridian's 2,400 employees across Boston, London, Berlin, Singapore, and Toronto offices.

**In-Scope Configuration Items (CI Classes):**

| CI Class | Description | Examples |
|---|---|---|
| **Infrastructure (IaaS)** | Physical and virtual foundational components | AWS EC2 instances, VPCs, subnets, security groups, Azure VMs, load balancers (ALB/ELB), S3 buckets, RDS instances |
| **Platform (PaaS)** | Managed platform services | AWS SageMaker domains, Snowflake warehouses, Apache Kafka clusters (MSK), Kubernetes clusters (EKS), Pinecone indexes |
| **Application Software** | Internally developed and third-party software | Clinical AI microservices, HealthPay transaction engine, MedInsight analytics pipelines, Datadog agents, Okta agents |
| **Network** | Software-defined and physical network components | Transit Gateways, Direct Connect, VPN tunnels, Route53 zones, firewall rules, WAF configurations |
| **AI/ML Assets** | AI model artifacts, data processing pipelines, and serving infrastructure | Trained model binaries (PyTorch, TensorFlow), MLflow model registry entries, Kubeflow pipeline definitions, feature store schemas, LangSmith tracing configurations |
| **Security** | Security-specific configurations | AWS KMS keys and key policies, HashiCorp Vault secret engines, Okta application integrations, CrowdStrike Falcon policies, IAM roles and policies |
| **Endpoints** | End-user and administrator devices | MacBook Pro laptops (Jamf-managed), Linux workstations for engineering, Windows Admin Jump hosts |
| **CI/CD Toolchain** | Build and deployment systems | GitHub Actions, Jenkins pipelines, Terraform Cloud workspaces, AWS CodeDeploy configurations |

**Out of Scope:**
- Customer-managed devices or applications installed on customer premises.
- Third-party SaaS platforms where Meridian has no administrative configuration access beyond tenant settings (e.g., Salesforce, Workday tenant configurations are in scope for Corp-IT).
- One-time-use ephemeral resources in development sandboxes that are destroyed within 24 hours (these are managed under SOP-DEVSEC-002, "Ephemeral Environment Management").

### 1.3 Applicability

This SOP is binding upon all employees, contractors, consultants, and third parties who design, develop, deploy, operate, or decommission any in-scope configuration item. Functional responsibility is primarily held by the following business units:
- **IT Operations & Infrastructure** (Owner: Samantha Torres)
- **Engineering** (Approver: David Park)
- **Information Security** (CISO: Rachel Kim)
- **Clinical AI Products** (VP: Dr. Aisha Okafor)
- **Financial Services Engineering** (VP: Robert Liu)

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Configuration Item (CI)** | Any component or asset that needs to be managed in order to deliver an IT service. CIs are under the control of the Change Management process (see SOP-ITOP-001, "Change Management") and are recorded in the Configuration Management Database (CMDB). |
| **Configuration Management Database (CMDB)** | A centralized repository, implemented in ServiceNow, that stores information about the attributes, relationships, and history of all authorized CIs. |
| **Baseline** | A formally reviewed and agreed-upon specification for a CI, or group of CIs, at a specific point in time. A baseline serves as a reference for future changes and can only be altered through the formal Change Management process. |
| **Drift** | Any unauthorized or unrecorded deviation of a CI's actual state from its authorized baseline. Drift is a primary indicator of configuration control failure. |
| **Drift Detection** | The continuous or periodic process of comparing the actual state of a CI against its defined baseline in the CMDB to identify drift. |
| **Golden AMI (Amazon Machine Image)** | A pre-configured, hardened, and approved base operating system image from which all EC2 instances of a given class are launched. |
| **Trusted Source** | The authoritative system of record for a particular CI attribute. The CMDB is a consumer of data from trusted sources via automated discovery and integration. |
| **High-Risk AI System** | As defined by the EU AI Act, Annex III, a system that poses a significant risk of harm to health, safety, or fundamental rights. All products under the Clinical AI Platform business line are classified as high-risk. |
| **Technical Debt** | The implied cost of future rework caused by choosing an expedient solution now instead of a better, more robust approach. Configuration drift is a form of technical debt that must be tracked and remediated. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **CI** | Configuration Item |
| **CMDB** | Configuration Management Database |
| **CMS** | Configuration Management System (the overall ecosystem of tools, processes, and the CMDB) |
| **IaC** | Infrastructure as Code |
| **CSB** | Configuration Standards Board |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **CM** | Configuration Management |
| **SME** | Subject Matter Expert |
| **PHI/ePHI** | Protected Health Information / Electronic Protected Health Information |
| **SNS** | AWS Simple Notification Service |
| **SQS** | AWS Simple Queue Service |

---

## 3. Roles and Responsibilities

The following Responsibility Assignment Matrix (RACI) defines the key roles and their relationship to the major activities within this SOP. [R=Responsible (doer), A=Accountable (approver), C=Consulted (subject matter expert), I=Informed (kept up-to-date)]

| Activity / Process | VP of IT Ops (Torres) | VP of Eng (Park) | CISO (Kim) | Sr. CM Engineer | Product Team Lead | DevOps Engineer | Compliance Officer (Anderson) |
|---|---|---|---|---|---|---|---|
| **CM Policy & Strategy** | A/R | A | C | R | C | C | I |
| **CMDB Design & Health** | A | I | C | R | I | C | I |
| **Baseline Definition & Approval** | I | A | C | R | C | R | I |
| **Drift Detection & Remediation** | I | I | I | R | I | R | I |
| **CI Lifecycle Management** | I | I | I | A | C | R | I |
| **Automated Discovery & Integration** | A | I | I | R | I | C | I |
| **Exception Handling & Approval** | A | A | C | R | C | C | R |
| **Regulatory Audit Support** | I | I | C | R | I | I | A |

### 3.1 Role Descriptions

**VP of IT Operations (Samantha Torres):**
- Ultimate accountability for the Configuration Management process and CMDB integrity.
- Approves all high-impact baseline changes for infrastructure CIs.
- Reviews and signs off on the monthly Configuration Status Report.

**VP of Engineering (David Park):**
- Ultimate accountability for the configuration of application software and CI/CD toolchain CIs.
- Approves all high-impact baseline changes for application CIs and product architectures.
- Ensures engineering teams adhere to IaC principles and CM policies.

**Chief Information Security Officer (Rachel Kim):**
- Consults on security control configurations, including IAM policies, security group rules, and encryption key management.
- Reviews all baselines for security-sensitive CIs.
- Escalates critical exploitable configuration drift as a security incident per SOP-SEC-001, "Incident Response".

**Senior Configuration Management Engineer (CM Team):**
- Operational owner of the CMDB and the CMS ecosystem.
- Designs and maintains automated discovery integrations between ServiceNow and AWS, Azure, Datadog, and Okta.
- Creates and manages baseline definitions in the CMDB.
- Runs daily drift detection reports and orchestrates remediation workflows.
- This role resides within the IT Operations & Infrastructure business unit.

**Product Team Lead (e.g., Clinical AI, HealthPay, MedInsight):**
- Represents the product's functional and non-functional requirements during baseline definition.
- Acts as the primary point of contact for CI disputes or misclassifications related to their product.
- Accountable for ensuring their team remediates drift on application-owned CIs within SLA.

**DevOps Engineer:**
- Responsible for authoring and maintaining all IaC artifacts (Terraform, CloudFormation, Kubernetes manifests, Ansible playbooks).
- Executes planned configuration changes via the CI/CD pipeline, ensuring the actual state matches the declared IaC.
- Performs first-level triage on drift alerts for their responsible CIs.

**Chief Compliance Officer (Thomas Anderson):**
- Accountable for ensuring the CM process meets the evidence-generation requirements for SOC 2, HIPAA, ISO 27001, and HITRUST audits.
- Reviews and approves all policy-level exception requests to ensure they do not violate a regulatory mandate.

---

## 4. Policy Statements

### 4.1 Foundation Principles

4.1.1 **Infrastructure as Code (IaC) Mandate.** All in-scope CIs in production, staging, and DR environments, covering infrastructure, platform, and security classes, SHALL be provisioned, modified, and decommissioned exclusively through a pre-approved, peer-reviewed Infrastructure as Code (IaC) pipeline. Direct manual manipulation via cloud consoles or APIs (so-called "ClickOps") is strictly prohibited for these environments and constitutes an unauthorized change, subject to immediate rollback and incident review per SOP-ITOP-001, "Change Management".

4.1.2 **Centralized Configuration Repository.** The ServiceNow CMDB SHALL serve as the single, centralized, authoritative configuration repository for all technology CIs. The CMDB is the system of record for CI attributes, relationships, and their authorized baselines. All other tools and dashboards are downstream consumers of CMDB data.

4.1.3 **Complete and Accurate Data.** All CIs within scope SHALL be registered in the CMDB with attributes populated sufficiently to support the key service management processes of Incident, Problem, Change, Availability, and Capacity Management. The completeness and accuracy targets for the CMDB are defined in Section 7.

4.1.4 **Baseline Governance.** Every CI class listed in Section 1.2 SHALL have a documented, approved, and version-controlled baseline. A CI may not be promoted to a production environment without a ratified baseline. Baselines are immutable once approved and can only be modified via an approved Change Request.

4.1.5 **Drift is an Incident.** Configuration drift is a deviation from a known-secure, known-compliant state. Any unplanned, unauthorized drift detected in a production system SHALL be treated as a P3 incident (or higher, depending on security impact) and responded to according to the incident management process defined in SOP-ITOP-003, "Incident Management". The immediate objectives are to determine the root cause, contain any potential impact, and restore the CI to its authorized baseline.

### 4.2 SOC 2-Specific Commitments

4.2.1 **Availability Management.** Configuration baselines for systems classified as Tier-1 (customer-facing, revenue-impacting) shall define the intended architecture to support availability commitments. This includes specifying the deployment across a minimum of two Availability Zones (AZs) and configuring auto-scaling policies. The baseline for Tier-1 services ensures that the infrastructure is designed to recover from common failure modes. Specific Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) are defined in architectural decision records and service level objectives, which inform the baseline configurations for disaster recovery assets in Azure.

4.2.2 **Logical Access Configuration.** IAM roles, security groups, and network ACLs are CIs under this policy. Their baselines define the principle of least privilege. Access to modify a CI's configuration must be restricted to authorized IaC pipelines and strictly limited break-glass roles. The logical access configurations are reviewed during the baseline approval process to confirm they restrict access appropriately.

### 4.3 HIPAA-Specific Commitments

4.3.1 **ePHI System Configuration.** CIs that process, store, or transmit ePHI are classified as "Type-B" (HIPAA-sensitive) CIs. Their baselines are subject to an additional mandatory review by the CISO and include mandatory security controls such as encryption at rest and in transit. Any drift on a Type-B CI is immediately escalated to a P2 incident.

4.3.2 **Breach Notification Support.** In the event of a confirmed security incident involving a Type-B CI, an accurate and current CMDB is critical to determining the scope of impact. The CMDB must provide the capability to rapidly identify all relationships between a compromised CI and datasets containing ePHI. This capability supports Meridian's legal and regulatory obligation for breach notification. The configuration management team is responsible for generating a "Data Relation Impact Assessment" from the CMDB within four hours of a request from the incident commander.

### 4.4 EU AI Act-Specific Commitments

4.4.1 **High-Risk AI System Transparency.** For CIs that are components of a high-risk AI system (Clinical AI Platform), the CMDB shall serve as a technical documentation register, recording the version and configuration of all models, data pipelines, and inference environments. This ensures traceability between a specific AI system's risk assessment (see SOP-CAI-001, "AI Risk & Impact Assessment") and its operational state.

---

## 5. Detailed Procedures

This section details the step-by-step operational procedures for the core Configuration Management processes. The CM Team, in coordination with DevOps and Engineering personnel, is responsible for executing these procedures.

### 5.1 CI Identification and Registration

The objective of this procedure is to ensure every new CI is properly identified, classified, and registered in the CMDB at the point of creation.

**Procedure ID:** CM-PROC-01
**Trigger:** Automated via IaC pipeline or manual via ServiceNow for non-IaC covered CIs.
**Target Completion:** Registration must be completed before the CI is deployed to a non-sandbox environment.

**Steps:**

1.  **CI Candidate Identification:**
    - **Automated (Primary):** The IaC pipeline (e.g., `terraform plan`) generates a list of proposed new resources. A `terraform provider` for ServiceNow parses the plan output and identifies candidate CIs that do not exist in the CMDB.
    - **Manual (Exception):** For CIs not yet managed by IaC (e.g., a legacy Corp-IT server, a physical piece of lab equipment), the asset owner submits a "New CI Registration Request" via the ServiceNow Service Catalog.

2.  **Class and Attribute Assignment:**
    - The automated system, or a CM analyst for manual requests, assigns the CI to a specific class from the ServiceNow Common Service Data Model (CSDM) table structure, mapped to the CI Classes in Section 1.2.
    - **Mandatory Attributes:** The following core attributes must be populated for every CI:
        - `Name` (Unique identifier, e.g., `us-east-1-prd-clinicalai-ecs-cluster`)
        - `CI Class`
        - `Environment` (Production, Staging, DR, Development, Corp-IT)
        - `Data Classification` (Type-A: ePHI, Type-B: Sensitive Non-PHI, Type-C: Public)
        - `Business Service` (Maps to a product line, e.g., "MedInsight Analytics")
        - `Owner` (Responsible Team Lead, e.g., "Clinical AI Platform Team")
        - `Location` (Physical or logical, e.g., `AWS us-east-1a`, `Azure westeurope-01`)
        - `Managed By` (Automated system, e.g., "Terraform - Core Infrastructure")

3.  **Relationship Mapping:**
    - The discovery source (Terraform, AWS Config, etc.) identifies upstream and downstream relationships. Common relationships include:
        - `Runs on::Runs` (e.g., Application runs on EC2)
        - `Depends on::Used by` (e.g., EC2 depends on Security Group)
        - `Contains::Contained by` (e.g., VPC contains Subnet)
    - These relationships are automatically proposed and created in the CMDB. For manual entries, a CM analyst must map at minimum the `Contains` and `Depends on` relationships.

4.  **Tagging Verification:**
    - No CI can be registered without verifying that it complies with the mandatory AWS/Azure tagging policy. The service will flag the `terraform plan` and fail the CI/CD pipeline if tags are missing.
    - **Mandatory Tags:** `meridian:env`, `meridian:service`, `meridian:owner`, `meridian:data-class`, `meridian:sop-itop-004`.
    - **Tagging Violation Result:** Pipeline halt and automated notification to the service owner via Slack (#eng-alerts).

5.  **CMDB Record Creation:**
    - Upon successful validation, the ServiceNow API creates the CI record with a unique `sys_id`.
    - The CI status is set to `Ordered` (if pending provisioning) and automatically updates to `In Use` upon successful deployment health checks, as confirmed by a Datadog monitor event.

### 5.2 Baseline Creation and Approval

A baseline defines the "golden" configuration for a CI or group of CIs. No CI may be in a `Production` status without an approved baseline.

**Procedure ID:** CM-PROC-02
**Trigger:** Introduction of a new CI class or a major version change to an existing service.
**Target Completion:** Must be completed and approved before a Change Request authorizing the initial production deployment is approved.

**Steps:**

1.  **Baseline Proposal Drafting:**
    - A Product Team Lead or Senior Engineer drafts a "Configuration Baseline Proposal" using the standard template in the Meridian Engineering Knowledge Base (Confluence space: `CM-Baselines`).
    - The proposal must include:
        - **CI Class & Name:** The logical grouping the baseline applies to (e.g., "Clinical AI Inference Web-Server").
        - **IaC Module & Version:** The exact Git commit hash of the Terraform module or equivalent.
        - **Golden Image/AMI ID:** The specific, hardened AMI ID generated by the Packer pipeline.
        - **Core Configuration Spec:** CPU, Memory, Instance Type, Auto-scaling minimum/maximum/desired counts.
        - **Security Controls:** IAM Instance Profile, attached Security Group IDs, disk encryption key ARN.
        - **Observability Configuration:** Specific Datadog monitor IDs to be applied.

2.  **Automated Security and Compliance Scan:**
    - The proposal must be attached to a draft Change Request. Upon submission, Jenkins triggers an automated baseline compliance scan. The scan performs:
        - **IaC Static Analysis:** Checkov, tfsec, or CloudFormation Guard scan against Meridian's custom policy packs.
        - **Image Vulnerability Scan:** AWS Inspector or CrowdStrike Falcon Cloud Security scan of the proposed Golden AMI.
        - **HIPAA Boundary Check:** If `meridian:data-class=type-a`, an automated check asserts that the Subnet CIDR is within an approved HIPAA-enforced VPC.

3.  **Configuration Standards Board (CSB) Review (Conditional):**
    - A CSB review is triggered if any of the following are true:
        - The CI is a new class, never before deployed.
        - The baseline represents a significant architectural shift (e.g., moving from EC2 to ECS Fargate).
        - The automated compliance scan fails with a severity of `HIGH` or `CRITICAL` and a waiver is sought.
    - The CSB is a virtual standing committee, including the VP of IT Ops (or delegate), CISO (or delegate), a Principal Architect from Engineering, and the Chief Compliance Officer (or delegate). They meet ad-hoc via a scheduled 1-hour session within two business days of a request.

4.  **Baseline Approval:**
    - The Change Request (and implicitly the baseline) is approved by the VP of Engineering (or delegate) and, if a security-sensitive CI, the CISO (or delegate).
    - This approval confirms the baseline is the new authorized state.

5.  **CMDB Basline Registration:**
    - Upon approval, the CM engineer registers the baseline in the ServiceNow `cmdb_baseline` table.
    - Key details recorded: `Baseline Name` (matches proposal), `Approved IaC Version`, `Date Approved`, `Approver`, `Applies to CIs`.
    - The baseline is now active.

### 5.3 Drift Detection and Remediation

Continuous drift detection is the primary control for ensuring the integrity of the configuration state.

**Procedure ID:** CM-PROC-03
**Trigger:** Scheduled, event-driven, and user-initiated.

**5.3.1 Scheduled Reconciliation (Daily)**

**Time:** 08:00 UTC and 20:00 UTC daily.
**Scope:** All Production, Staging, and Corp-IT (critical servers) CI classes.

1.  **Automated Discovery Import:** The ServiceNow IRE (Identification and Reconciliation Engine) processes the latest full-load exports from:
    - **AWS Config:** AWS resource configurations and relationships.
    - **Azure Resource Graph:** Azure resource configurations.
    - **CrowdStrike:** Server and endpoint OS-level configurations.
    - **Okta:** Application and user-to-application access mappings.

2.  **Reconciliation Job Execution:** A scheduled job compares each discovered CI against its authorized baseline in the CMDB. The comparison logic is:
    ```python
    # Simplified logic
    if actual_state[attribute] != baseline_state[attribute]:
       if attribute in ["SecurityGroupIds", "IAMInstanceProfile", "EncryptionKeyArn"]:
           severity = "CRITICAL"
       elif attribute in ["InstanceType", "SubnetId"]:
           severity = "HIGH"
       else:
           severity = "MEDIUM"
       generate_drift_incident(ci_id, attribute, actual_value, baseline_value, severity)
    ```

3.  **Automated Self-Healing (Limited Scope):**
    - For select non-destructive attributes in stateless auto-scaling groups (e.g., a non-compliant tag), the system will automatically trigger a "repave" of the affected instances without human intervention.
    - The self-healing scope is limited to CIs tagged with `meridian:auto-remediate=true`. This tag is currently only applied to development and staging web server ASGs.
    - All self-healing actions are logged to the CI's history and generate an informational ticket in ServiceNow.

**5.3.2 Event-Driven Drift Detection (Real-Time)**

1.  **CloudTrail/Activity Log Interception:** An AWS EventBridge (or Azure Event Grid) rule intercepts every `Create`, `Modify`, and `Delete` API call for in-scope resource types.
2.  **IaC Pipeline Correlation:** The EventBridge rule calls a custom Lambda function, "ConfigGuard". The function checks the `userIdentity` of the API call.
    - **Authorized (Terraform Role):** The change is correlated with an in-progress or recently completed Terraform Cloud run. No alert.
    - **Authorized (Break-Glass Role):** Validated against an open, pre-approved emergency change request in ServiceNow. A `P2` incident is automatically generated for the security team to monitor and the CM team to update the baseline post-incident.
    - **Unauthorized (Any other identity):** The change is immediately flagged as a `CRITICAL` severity configuration drift incident. ConfigGuard simultaneously publishes the alert to Datadog, PagerDuty, and Slack (#sec-alerts), and attempts to tag the modified resource with `meridian:status=quarantined`.

**5.3.3 Drift Remediation**

1.  **Incident Assignment:** The drift incident ticket is automatically routed to the service owner listed on the CI record in the CMDB.
2.  **Root Cause Analysis (RCA):** The owning team has one hour for `CRITICAL` and four hours for `HIGH` severity drift to determine a root cause and document it in the incident ticket. Common causes include:
    - Unauthorized manual command execution (Dev/prod parity issue, break-glass misuse).
    - Cross-service impact from a related, approved change on a dependent CI.
    - Discovery source error or latency (false positive).
3.  **Remediation Path Selection:**
    - **Path A (IaC Realignment):** If the drifted state is actually the desired new state (e.g., an emergency fix that must be backported), the team initiates an Emergency Change Request to update the IaC baseline. Upon baseline approval, the CMDB is updated, and the drift is resolved by updating the target state, not the actual state.
    - **Path B (State Reversion):** If the drift is unauthorized and undesired, the team must revert the CI to its authorized state by re-running the latest approved IaC pipeline. This is the mandatory default path.
4.  **Closure Verification:** The incident cannot be closed until a final automated reconciliation scan confirms zero drift for the affected CI. This is enforced by the ServiceNow workflow.

### 5.4 CI Modification (Planned Change)

This procedure describes the CM-specific steps within the broader Change Management process (SOP-ITOP-001).

**Procedure ID:** CM-PROC-04
**Trigger:** An approved Change Request that modifies the configuration of an existing CI or its relationship.

1.  **Change Impact Analysis:** The change requester uses the ServiceNow "CI Impact Analyzer" tool to visualize all upstream and downstream relationships from the target CI. This report is a mandatory attachment to the Change Request.
2.  **IaC Artifact Update:** A developer creates a feature branch and updates the relevant Terraform module, Ansible role, or Kubernetes manifest.
3.  **Pre-Deployment CM Validation (CI/CD Gate):** The CI pipeline performs a `terraform plan` and a `checkov` scan. As part of the plan, the ServiceNow provider `diff` is displayed and must be reviewed by the approving tech lead.
4.  **Execution & CMDB Update:** Upon merge to `main` and successful `terraform apply`, the ServiceNow provider automatically updates the CI record attributes to reflect the new authorized state. The `Last Modified By`, `Modified Time`, and `Related Change Request` fields are updated.
5.  **Post-Deployment Baseline Update:** If the change is permanent, the change request task list includes a mandatory task to update the parent baseline record in the CMDB to reflect the new minor or patch version.

### 5.5 CI Decommissioning

Unmanaged, orphaned CIs create security blind spots and pollute the CMDB.

**Procedure ID:** CM-PROC-05
**Trigger:** Approved Change Request to decommission a service.

1.  **Dependency Analysis:** A comprehensive report identifying all consuming services and dependent CIs is generated from the CMDB.
2.  **Client Deprovisioning:** All dependent CIs are updated (e.g., removal of security group rules referencing the target, updating service discovery records).
3.  **Resource Destruction:** The `terraform destroy` command is executed via the pipeline.
4.  **CMDB Record Retirement:** The CI record is not deleted. Its status is changed to `Retired`. Its `Retired Date` and `Destruction Evidence` (link to Terraform apply log) attributes are populated. This preserves an immutable audit log for compliance purposes. Data residency requirements for logs are automatically enforced based on the `Location` attribute.

---

## 6. Controls and Safeguards

This section outlines the specific technical, administrative, and procedural controls established to enforce this SOP.

### 6.1 Technical Controls

| Control ID | Control Name | Description | Tool/Implementation |
|---|---|---|---|
| CM-TC-01 | IaC Pipeline Enforcement | The CI/CD pipeline is the exclusive gate for all production configuration changes. | Jenkins/Terraform Cloud; GitHub branch protection rules (`main` branch); AWS SCPs denying manual EC2, RDS, S3 creation in production accounts. |
| CM-TC-02 | Service Control Policies (SCPs) | AWS SCPs applied at the Organizational Unit (OU) level prevent non-IaC roles from creating, modifying, or deleting core infrastructure CIs. | AWS Organizations SCPs for `prod` and `staging` OUs. Exempts specified break-glass roles audited by CloudTrail. |
| CM-TC-03 | Automated Discovery & Reconciliation | Scheduled, automated import of live configuration data from all platforms to reconcile with the CMDB. | ServiceNow IRE integration with AWS Config, Azure Resource Graph, Okta, CrowdStrike. |
| CM-TC-04 | Real-time Drift Guarding | Event-driven control that detects and alerts on any out-of-band configuration change. | ConfigGuard (custom Lambda), AWS EventBridge, Azure Event Grid. |
| CM-TC-05 | Immutable Image Pipeline | All server images are built from a single, version-controlled pipeline and are immutable after creation. No in-place patching on production servers. | Packer builds Golden AMIs. Code in `meridian/golden-images` GitHub repo. |
| CM-TC-06 | Secret Management | Application secrets, passwords, and API keys are never stored in IaC code, configuration files, or the CMDB. All secrets are externalized. | HashiCorp Vault; AWS Secrets Manager. CI/CD pipelines inject secret references, not values. |

### 6.2 Administrative Controls

| Control ID | Control Name | Description |
|---|---|---|
| CM-AC-01 | Configuration Standards Board (CSB) | A cross-functional governance board reviews and approves all new CI class baselines and high-impact architectural changes. |
| CM-AC-02 | Mandatory Tagging Policy | All billable AWS/Azure resources must adhere to the mandatory tagging schema. Provisioning is blocked without compliance. |
| CM-AC-03 | Segregation of Duties | A person cannot both authorize a baseline change (Approver) and execute the implementation (DevOps). The ServiceNow Change module enforces this. |
| CM-AC-04 | Break-Glass Procedure Review | All use of break-glass roles is reviewed by the CISO in a weekly security operations sync. The configuration changes performed are reconciled against the CMDB as a condition of closing the emergency change. |
| CM-AC-05 | Configuration Access Review | The CMDB stores and correlates the roles with permission to modify logical controls (security groups, IAM policies). These configured relationships are reviewed by the asset owner during baseline approval to ensure appropriate access. |

### 6.3 Physical Controls

Not directly applicable. Physical hardware is limited to Meridian's Boston and Berlin corporate offices (network switches, access control systems). These are treated as Corp-IT CIs and their configuration (firmware versions, ACLs) is managed under this SOP via a manual registration and reconciliation procedure due to the absence of a fully automated IaC pipeline for these devices.

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness of the Configuration Management process is tracked through a set of Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs). These are visualized on a centralized Datadog dashboard, "CM-Health-Dashboard."

### 7.1 Key Performance Indicators (KPIs)

| KPI | Description | Target | Measurement Method |
|---|---|---|---|
| **CMDB Completeness** | Percentage of discovered production CIs that have a corresponding, complete CI record (all mandatory attributes populated). | ≥ 99% | Daily reconciliation job: `(CIs with full records / Total Discovered CIs) * 100` |
| **CMDB Accuracy** | Percentage of CIs where the recorded attributes in the CMDB match the discovered state (i.e., zero known drift for approved baselines). | ≥ 98% | Daily reconciliation job: `(CIs with zero drift / Total Audited CIs) * 100` |
| **Mean Time to Detect (MTTD) Drift** | The average elapsed time between an unauthorized configuration drift event occurring and its detection. | ≤ 15 minutes (for production) | PagerDuty analytics from ConfigGuard alerts minus CloudTrail event time. |
| **Mean Time to Remediate (MTTR) Drift** | The average elapsed time from drift detection to the restoration of the authorized baseline. | CRITICAL: 4 hours; HIGH: 24 hours; MEDIUM: 72 hours | ServiceNow incident lifecycle analytics, filtered by CI drift incidents. |
| **IaC Adoption Rate** | Percentage of changes to production that are executed via an approved IaC pipeline. | 100% | AWS CloudTrail/Config analysis: `Change Events from authorized pipeline roles / Total Change Events`. Any non-pipeline change is a missed target. |

### 7.2 Key Risk Indicators (KRIs)

| KRI | Warning Threshold | Critical Threshold | Escalation |
|---|---|---|---|
| **Unauthorized Change Rate** | ≥ 5 unauthorized changes/day across all production | ≥ 1 unauthorized change on a HIPAA-sensitive CI (Type-A) | Warning triggers an email to the VP of IT Ops. Critical triggers a P2 incident and a call with the CISO. |
| **Accumulated Drift (Technical Debt)** | ≥ 10 drift incidents open > 72 hours | ≥ 1 drift incident > 7 days | Included in the weekly CM Operations report to VPs. Critical triggers an immediate exception review. |
| **CMDB Sync Lag** | Last successful full reconciliation from a trusted source is > 2 hours old | Last successful full reconciliation is > 6 hours old | Warning triggers a ticket to the CM Tools team. Critical triggers a P3 incident for the CM team. |

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Owner | Content Summary |
|---|---|---|---|---|
| **CM Health Dashboard** | All Engineering, IT, and Security staff | Real-time | CM Team | Live KPI, KRI, and drift incident counts. Serves as a single pane of glass. |
| **Drift Incident Triage Report** | Service Owners (Product Team Leads) | Daily (Automated Email) | ServiceNow | Lists all open drift incidents for their team's CIs, sorted by severity and age. |
| **Weekly CM Operations Report** | VP of IT Ops, VP of Engineering | Weekly | Senior CM Engineer | KPI/KRI trends, chronic drift offenders, process improvement suggestions. |
| **Monthly Configuration Status Report** | CISO, CCO, AI Governance Committee | Monthly | VP of IT Ops | Consolidated report on CMDB health, high-severity drift events, audit evidence requests, and exception register. This report is a key input into the annual SOC 2 and ISO 27001 management reviews. |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

A formal, auditable exception is required whenever an individual or team is unable to conform to a specific policy statement, procedure, or control defined in this SOP. A temporary expedient cannot be used under the guise of an exception. All exceptions carry risk and must be rigorously managed.

**Procedure:**

1.  **Initiation:** The requestor submits a "Configuration Management Exception Request" via the ServiceNow Service Catalog.
    - The request must state the specific policy, procedure, or control from which exception is sought (e.g., "Exception to 5.3.3 Path B state reversion for prod ELB `app-lb-prod-01`").
    - **Business Justification:** A detailed, compelling business or technical reason must be provided, explaining why conformance is not possible.
    - **Risk and Impact Assessment:** The requestor must identify the security, compliance, and operational risks introduced by the exception.
    - **Proposed Start and End Date:** No exception is permanent. A sunset date, not to exceed 90 days, must be proposed.
    - **Compensating Controls:** The requestor must propose any compensating controls to mitigate the temporary elevated risk.

2.  **Technical Review:** The Senior CM Engineer reviews the request for technical feasibility and completeness. This review includes an automated scan to model the configuration drift the exception will introduce, highlighting the CI relationships that will be impacted. The report is attached to the exception ticket.

3.  **Risk Approval:** The request is routed based on the residual risk level:
    - **Low/Medium Risk:** Approval from the VP of IT Operations (or delegate) is required.
    - **High/Critical Risk:** Consecutive approval from the CISO (Rachel Kim) and the Chief Compliance Officer (Thomas Anderson) is required. Any exception on a HIPAA-sensitive (Type-A) CI is automatically classified as High Risk.

4.  **State Recording:** Upon approval, the CMDB CI record is annotated with a clear "Exception Active" banner and a link to the exception ticket. This ensures the drift will be known, logged, and excluded from the daily accuracy KPI to avoid a false-positive drift incident.

5.  **Expiration and Closure:** Five business days before the agreed sunset date, ServiceNow automatically notifies the requestor and the approver. The exception cannot be extended; it must be closed. A new exception request may be submitted, and it will undergo a more stringent review due to the precedent of non-conformance.

### 8.2 Escalation Path for Drift Incidents

If drift is not being remediated within SLA, the following automated escalation path is activated in ServiceNow, driven by the incident's age and the CI's data classification:

- **Step 1: Service Owner (0 hours).** Incident is assigned.
- **Step 2: Senior DevOps Manager (Breach by 2 hours for CRITICAL, 12 hours for HIGH).** Notified of the delay.
- **Step 3: VP of Engineering (Breach by 4 hours for CRITICAL, 24 hours for HIGH).** The incident is escalated to the VP level for immediate management attention.

---

## 9. Training Requirements

Effective Configuration Management depends on the competence of all personnel involved in the lifecycle of a CI. Meridian provides both role-based and general awareness training.

### 9.1 Training Programs

| Training Module ID | Module Name | Target Audience | Mode of Delivery | Frequency | Duration |
|---|---|---|---|---|---|
| CM-TRN-101 | Configuration Management Awareness | All Engineering, IT, and Product staff | Online (Absorb LMS) | Annual | 30 min |
| CM-TRN-201 | Authoring Secure IaC Baselines | DevOps Engineers, Senior Engineers, Architects | Instructor-led workshop | On-hire, then bi-annual refresher | 8 hours |
| CM-TRN-202 | CMDB Data Stewardship & Operations | IT Operations Analysts, CM Team | Online (Absorb LMS) | Annual | 2 hours |
| CM-TRN-301 | Break-Glass & Emergency Change | IT Operations, Security Engineers | Simulation-based assessment | Annual | 4 hours |

### 9.2 Training Content Summaries

- **CM-TRN-101 (Awareness):** Covers the definition of drift, its link to incidents and HIPAA compliance, the "no manual changes" policy, and how to properly initiate a configuration change. This is included in the annual workforce training cycle, which covers general security and operational compliance topics. An acknowledgment of completion is required and tracked.
- **CM-TRN-201 (IaC Authoring):** In-depth, hands-on training on using Terraform or CloudFormation to encode Meridian baselines, the mandatory tagging schema, implementing automated Checkov policies, and the baseline approval process. A practical examination requires the developer to successfully provision a compliant, baselined microservice in a sandbox environment.
- **CM-TRN-301 (Break-Glass):** Covers the strictest procedure for emergency access. A scenario-based simulation requires the trainee to respond to a simulated critical service outage, use a break-glass role, and then correctly follow post-action reconciliation and RCA procedures.

### 9.3 Training Tracking and Enforcement

- All training completion records are stored in the Absorb Learning Management System (LMS) and are linked to the employee's HR record in Workday.
- The CM-TRN-201 and CM-TRN-301 modules are **role-based gates for privileged access**. The CI/CD pipeline will deny a deployment authorization prompt to any user whose required training is past its expiration date.
- Training compliance metrics are reported quarterly to department VPs as part of the organizational scorecard.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Documents

This SOP must not be read in isolation. It is integrated with the following internal policies and standards:

| Document ID | Document Title | Relationship to This SOP |
|---|---|---|
| SOP-ITOP-001 | Change Management | Defines the overarching process for all changes. CM changes are a specific class of change managed under that process. |
| SOP-ITOP-003 | Incident Management | Defines the Severity levels (P1-P5), the incident lifecycle, and the response playbooks that govern drift remediation. |
| SOP-SEC-001 | Security Incident Response | Governs the escalation of exploitable configuration drift (e.g., an open security group) as a security incident. |
| SOP-CAI-001 | AI Risk & Impact Assessment | Configuration records in the CMDB serve as the technical evidence for the risk assessments of high-risk AI systems it covers. |
| SOP-DEVSEC-002 | Ephemeral Environment Management | Governs the 24-hour lifecycle of sandbox resources, which are explicitly exempted from CMDB registration. |
| POL-CORP-007 | Data Classification and Handling Policy | Defines the Type-A, B, C data classifications that are a mandatory CI attribute and drive access and encryption requirements. |
| ENG-STD-009 | IaC Coding and Review Standards | Defines the specific rules for Checkov policies, Terraform modularization, and peer-review requirements referenced in the procedures. |

### 10.2 External References

| Standard | Reference | Relevant Sections |
|---|---|---|
| **SOC 2** | AICPA TSC 2017 (Revised) | CC6.1 (Logical Access), CC7.1 (Change Detection), CC7.2 (System Monitoring), A1.2 (Infrastructure Availability) |
| **HIPAA** | 45 CFR § 164.312 (Technical Safeguards) | § 164.312(b) (Audit Controls), § 164.312(c)(1) (Integrity Controls), § 164.312(e)(1) (Transmission Security) |
| **ISO 27001:2022** | Clause A.8.9 (Configuration Management) | Complete control statement requiring lifecycle management, baselines, and drift control. |
| **EU AI Act** | Regulation (EU) 2024/1689 | Article 11 (Technical Documentation), Article 17 (Quality Management System) |
| **SR 11-7** | FRB/OCC Guidance on Model Risk Management | Model operational environment stability and control is a key validation checkpoint. |

---

## 11. Revision History

| Version | Date | Author | Description of Changes | Approver |
|---|---|---|---|---|
| 3.8 | 2023-09-15 | J. Ramirez, Sr. CM Engineer | Major restructure to align with CSDM 4.0 model. Introduced CI Class table and mandatory tagging policy. | D. Park |
| 3.9 | 2024-02-20 | J. Ramirez, Sr. CM Engineer | Non-substantive update: updated references to new VP of Engineering approver, David Park. | D. Park |
| 4.0 | 2024-06-11 | M. Chen, DevOps Manager | Added entire Section 5.3.2 Event-Driven Drift Detection via ConfigGuard. Introduced real-time drift KPI targets. Updated IaC Adoption Rate KPI to 100%. | S. Torres |
| 4.1 | 2024-11-18 | A. Baker, CISO Delegate | Added mandatory CISO review for all security-sensitive CI baselines (Section 5.2). Updated technical controls to reference new CrowdStrike Falcon Cloud Security module. | S. Torres |
| **4.2** | **2025-11-24** | **Samantha Torres, VP IT Ops** | **Major revision. Expanded scope to formally include AI/ML Assets as a new CI Class for EU AI Act compliance. Added full RACI matrix. Added procedure CM-PROC-05 for CI decommissioning. Updated training module frequencies and content. Integrated LangSmith tracing configurations. This version approved by the CEO as part of cross-functional governance review.** | **Dr. S. Chen, CEO** |