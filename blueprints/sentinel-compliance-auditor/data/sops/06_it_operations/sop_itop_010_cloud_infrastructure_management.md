---
sop_id: "SOP-ITOP-010"
title: "Cloud Infrastructure Management"
business_unit: "IT Operations & Infrastructure"
version: "4.7"
effective_date: "2025-02-22"
last_reviewed: "2026-06-16"
next_review: "2026-12-26"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Cloud Infrastructure Management

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the governance framework, operational controls, and technical procedures for the secure, compliant, and cost-effective management of Meridian Health Technologies, Inc.'s multi-account cloud infrastructure. This document translates the organization's commitment to the security, availability, and confidentiality principles of SOC 2 into actionable infrastructure operations. It ensures that the underlying platform supporting the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform is managed with the rigor required by our regulatory and contractual obligations.

### 1.2 Scope
This SOP applies to:

- **Personnel:** All Meridian employees, contractors, and third-party vendors involved in the architecture, deployment, management, monitoring, and decommissioning of cloud resources, including but not limited to members of IT Operations, Platform Engineering, Security Engineering, and the Cloud Center of Excellence (CCoE).
- **Cloud Service Providers:** Amazon Web Services (AWS), designated as the primary production and development cloud provider, and Microsoft Azure, designated as the Disaster Recovery (DR) and cold-storage backup provider.
- **Technical Assets:** All AWS Accounts within the `meridian-org` AWS Organization structure. This includes, but is not limited to, compute (EC2, Lambda, ECS/EKS), storage (S3, EBS), databases (RDS, Aurora, DynamoDB, ElastiCache), networking (VPC, Transit Gateway, Route 53), AI/ML services (SageMaker, Bedrock), and security services (IAM, KMS, Security Hub, GuardDuty).
- **Data Domains:** This SOP applies to the technical infrastructure hosting all Meridian data classifications, including Public, Internal, Confidential, and Strictly Confidential data. Separate data governance policies govern the logical handling of data hosted on this infrastructure.

### 1.3 Out of Scope
- CI/CD pipeline application deployment logic (see SOP-DEVP-005).
- Development team local environment configuration.
- End-user identity and access management (see SOP-SEC-015).
- Application-level change management (see SOP-CHG-001).

---

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **AWS Organization (AWS Org)** | A central management construct for consolidating multiple AWS accounts into a hierarchical structure for unified billing, access control, and security policy application. |
| **OU (Organizational Unit)** | A logical grouping of AWS accounts within an AWS Organization, allowing for the application of Service Control Policies (SCPs). |
| **SCP (Service Control Policy)** | A JSON policy document that explicitly allows or denies API actions at the AWS account or OU level, establishing a guardrail for maximum available permissions. |
| **Landing Zone** | A pre-configured, multi-account AWS environment based on best practices, serving as a starting point for secure and scalable workload deployment. Meridian uses a custom Landing Zone built on AWS Control Tower. |
| **Terraform** | Infrastructure as Code (IaC) tool used by Meridian for declarative provisioning and management of all cloud resources across both AWS and Azure environments. |
| **CSPM** | Cloud Security Posture Management. Meridian's designated tool is Palo Alto Prisma Cloud, used for continuous monitoring and automatic remediation of misconfigurations. |
| **CWPP** | Cloud Workload Protection Platform. Meridian uses CrowdStrike Falcon for runtime threat detection and vulnerability management. |
| **Blast Radius** | The potential impact or scope of compromise if a single security control, account, or container fails. |
| **Recovery Time Objective (RTO)** | The maximum acceptable time to restore a service to operational status after a disruption. |
| **Recovery Point Objective (RPO)** | The maximum acceptable amount of data loss measured in time. |
| **Golden AMI** | A pre-configured, hardened, and patched Amazon Machine Image (AMI) from which all production EC2 instances are launched. |
| **FinOps** | Financial Operations, the practice of bringing financial accountability to the variable spend model of the cloud. |
| **Tag** | A metadata label (key-value pair) applied to an AWS resource for identification, automation, cost allocation, and access control purposes. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the responsibilities for core cloud infrastructure activities.

| Activity / Decision | VP of IT Ops (S. Torres) | VP of Engineering (D. Park) | Dir. of Cloud Ops | Cloud Security Architect | Platform Engineering Lead | FinOps Manager | Development Teams |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cloud Strategy & Vision** | A/R | A | C | C | C | I | I |
| **AWS Org Structure & OU Design** | A | R | C | C | I | I | I |
| **SCP Authoring & Approval** | I | I | R | A | C | I | I |
| **Defining Golden AMIs** | I | I | A | R | C | I | I |
| **Provisioning New Accounts** | I | I | A | C | R | I | I |
| **Implementing IaC** | I | I | A | C | R | C | I |
| **Security Group Rule Approvals** | I | I | I | A | R | I | C |
| **FinOps Tagging Compliance** | A | I | R | I | I | R | R |
| **Monthly Cost Review** | A | I | R | I | I | R | C |
| **Incident Response Coordination** | A | A | R | R | C | I | C |
| **Account Decommissioning** | I | I | A | I | R | I | I |

*Key: R = Responsible (doer), A = Accountable (approver), C = Consulted, I = Informed*

---

## 4. Policy Statements

### 4.1 Governance and Architecture
- **4.1.1 Multi-Account Strategy:** All cloud workloads shall be segregated into multiple, purpose-built AWS accounts within a single `meridian-org` AWS Organization. This structure is mandatory to limit the blast radius of security incidents and service disruptions, and to enforce chargeback via native AWS billing boundaries. Account creation, modification, and decommissioning must be performed exclusively through the Meridian Landing Zone vending machine, driven by infrastructure as code (Terraform).
- **4.1.2 Least Privilege by Default:** All IAM roles, users, and groups shall be granted only the permissions required to perform their intended functions, based on an annual certification of need. AWS-managed policies with wildcard actions (`*`) are prohibited for use in any product account. All custom policies must adhere to a deny-by-default network and resource access model.
- **4.1.3 Infrastructure as Code (IaC) Mandate:** All production cloud infrastructure, including networking, compute, and security constructs, must be defined, modified, and destroyed using approved IaC templates (Terraform). Manual "ClickOps" changes via the AWS console are strictly prohibited for any resource in a Production or Staging OU, except during declared emergency break-glass procedures (see Section 8.4).
- **4.1.4 Immutable Infrastructure:** Workloads on the Meridian SaaS Platform shall favor an immutable infrastructure deployment pattern. Updates to EC2 instances or containers must result in the deployment of a new, fully-tested artifact from a CI/CD pipeline rather than in-place configuration changes on a running system.

### 4.2 Security and Compliance
- **4.2.1 Security Groups as Zero-Trust Boundaries:** AWS Security Groups (SGs) shall be configured with a default-deny posture, allowing only explicitly defined traffic flows that are documented in an approved Service Connectivity Request (Form-SEC-110). SGs must not be used as virtual firewalls with broad CIDR allow-lists; they should reference other security groups as sources wherever possible.
- **4.2.2 Encryption at Rest:** All data at rest within AWS services, including S3 buckets, RDS instances, EBS volumes, and DynamoDB tables, must be encrypted using the AWS Key Management Service (KMS) with customer-managed keys (CMKs). Default service-managed encryption (`aws/s3`, `aws/rds`) is acceptable only for non-production development OUs.
- **4.2.3 Encryption in Transit:** All service-to-service communication must use TLS 1.2 or higher. Application Load Balancers and API Gateways shall be configured to reject connection requests below TLS 1.2.
- **4.2.4 Regulatory Boundary:** The `eu-west-1` region is designated as the primary processing region for all workloads subject to the EU AI Act and data residency requirements, managed under the `meridian-org/geo/eu-west-1` OU. Cross-region data replication is prohibited without express approval from the Chief Privacy Officer (Dr. Klaus Weber) and VP of IT Operations.

### 4.3 Cost Management
- **4.3.1 Accountability:** Every provisioned resource must be associated with a cost center via mandatory tags. The FinOps team, led by the FinOps Manager, will perform a monthly review of cost anomalies and reserved instance/savings plan coverage.
- **4.3.2 Right-Sizing:** Performance metrics for CPU, memory, and IOPS must be reviewed quarterly to identify over-provisioned resources. Accounts running resources with an idle rate exceeding 30% for a calendar month will be flagged for remediation.

---

## 5. Detailed Procedures

This section outlines the step-by-step procedures for the lifecycle management of the Meridian cloud environment. These procedures are designed to ensure SOC 2 controls are operationalized effectively, particularly in the areas of logical access, change management, and system operations.

### 5.1 AWS Account Lifecycle Management

All new accounts are provisioned through the Meridian Landing Zone, which leverages AWS Control Tower Account Factory for Terraform (AFT). This guarantees a standardized, auditable baseline for every account.

#### 5.1.1 Procedure: Provisioning a New AWS Account

| Step | Action | Role | Tool/System |
| :--- | :--- | :--- | :--- |
| 1. | **Request Submission:** The requesting Development Lead or Project Manager submits an "AWS Account Provisioning Request" via the ServiceNow portal (Form-IT-210). The form must specify: Business Unit, intended OU (`Workloads/Dev`, `Workloads/Prod`, `Sandbox`), project lifespan, estimated monthly budget, and cost center. An architectural diagram must be attached for Production accounts. | Requestor | ServiceNow |
| 2. | **Budget & Approval:** The request is routed to the designated Business Unit cost center owner for financial approval. Upon approval, it queues for the FinOps Manager for budget allocation validation. | Cost Center Owner, FinOps Manager | ServiceNow, AWS Budgets |
| 3. | **Security Review and Baseline Configuration:** The Cloud Security Architect reviews the request against standard patterns. For a deviation from standard baselines, a full security review is triggered (see SOP-SEC-023). The standard GitHub `aws-account-baseline` Terraform module is pre-loaded with the new account's parameters (name, email, OU, initial SCPs). | Cloud Security Architect | Prisma Cloud, GitHub |
| 4. | **Pull Request and IaC Apply:** A Platform Engineering member creates a PR to add the account definition (`account.tf`) to the `terraform-org-management` repository. The PR must be reviewed and approved by the Cloud Operations Director or their delegate. Merge triggers the AFT pipeline, which: a) provisions the account in the correct OU, b) establishes a trust relationship with the Identity Center, c) creates a KMS root CMK, and d) deploys baseline VPCs, standard SGs, a central logging IAM role, and AWS Config rules. | Platform Engineering, AFT Pipeline | GitHub, Terraform Cloud, AWS Control Tower |
| 5. | **Handover:** The Platform Engineer records the new account ID in the CMDB (`cmdb.meridian.internal`), creates the delegated DNS zones in Route 53, and updates the `meridian-org` network map documentation. | Platform Engineer | CMDB, Route 53 |
| 6. | **Post-Provision Validation:** The CSPM tool (Prisma Cloud) is configured to scan the new account within 1 hour of creation. Any "High" or "Critical" findings must be remediated by the Platform Engineer before the account is marked as "Ready for Workload" and released to the requesting team. | Platform Engineer, Prisma Cloud | Prisma Cloud |

**Expected SLA:** From approved request to "Ready for Workload" status: 3 business days.

#### 5.1.2 Procedure: Decommissioning an AWS Account

| Step | Action | Role | Tool/System |
| :--- | :--- | :--- | :--- |
| 1. | **Request:** Account owner submits a "Resource Decommissioning Request" (Form-IT-211) in ServiceNow. | Requestor | ServiceNow |
| 2. | **Data Sanitization (Pre-Check):** A hold is placed on account deletion. The Platform Engineer runs an automated S3Inventory report and an AWS Backup report to verify that all required data has been archived per the data retention schedule (see SOP-DATA-001). Final backups are copied to the Azure DR cold-storage account. | Platform Engineer | S3 Inventory, AWS Backup, Azure |
| 3. | **Infrastructure Teardown:** All non-logging, non-IAM resources in the account are destroyed by running a `terraform destroy` for the workload modules. The Platform Engineer confirms resource deletion via the AWS Console (read-only view). | Platform Engineer | Terraform Cloud, AWS Console |
| 4. | **Security Lockdown:** The SCP for the account is updated to `Deny: *` (all actions). All IAM users and roles are deactivated, and access keys are deleted. | Platform Engineer | AWS Organizations, IAM |
| 5. | **Quarantine and Decommission:** The account is moved to a `Suspended` OU for a minimum 30-day quarantine period. After 30 days, if no restoration request is received, the account is closed and deleted from the AWS Organization by the Cloud Operations Director. | Dir. of Cloud Ops | AWS Organizations |
| 6. | **Cascade Cleanup:** The CMDB record is archived, monitoring dashboards are torn down, and the account is removed from the cost allocation reporting scope. | Platform Engineer | CMDB, Datadog, AWS Cost Explorer |

### 5.2 Network Security Group (SG) Management

This procedure enforces a zero-trust network model and is a critical control for SOC 2 CC6.1 (Logical and Physical Access Controls) and CC6.6 (External Communications Threats).

#### 5.2.1 Procedure: Requesting a New Security Group Rule

| Step | Action | Role | Tool/System |
| :--- | :--- | :--- | :--- |
| 1. | **Service Connectivity Request (SCR):** The application developer completes a Service Connectivity Request (Form-SEC-110) in ServiceNow. The form requires: Source Resource Name/Tag, Destination Resource Name/Tag, Protocol (TCP/UDP), Port/Port Range, Business Justification, and the `app-tier` tag of both source and destination. | Developer | ServiceNow |
| 2. | **Implicit Deny Validation:** The form logic automatically queries the CMDB to verify that the source and destination are not in a pre-defined exclusion zone (e.g., a PCI-DSS account to a Non-PCI account). A critical warning is displayed if a previously blocked protocol (e.g., SMB/CIFS) is requested. | ServiceNow | CMDB |
| 3. | **Security Architect Review:** The Cloud Security Architect reviews the justification. For inter-tier communication not matching an approved Pattern of Life (POL), the request is denied by default. The Architect is responsible for ensuring the rule does not expose a vulnerability or contravene the zero-trust policy. | Cloud Security Architect | ServiceNow |
| 4. | **IaC PR Creation:** Upon approval, the Platform Engineering Lead maps the request to a Terraform module. For standard requests, a self-service Terraform module generates a PR in the `terraform-org-management` repository, adding the rule to the appropriate `<app>-sg.tf` file. The rule syntax must be: `ingress { from_port = X, to_port = Y, protocol = "tcp", security_groups = [aws_security_group.source.id] }`. CIDR-based rules (`cidr_blocks = [...]`) require an additional justification entry. | Platform Engineering | GitHub, Terraform |
| 5. | **Peer Review and Apply:** The PR requires a formal review from one senior member of Platform Engineering. The reviewer validates that the Terraform plan output shows only the expected rule change (no drift correction). Merge triggers the apply. | Senior Platform Engineer | GitHub, Terraform Cloud |
| 6. | **Post-Deploy Audit:** Within 1 hour of the change, Prisma Cloud runs a change audit and alerts the Cloud Security Architect of any newly opened ports. The new rule is logged in a central Network Connectivity Matrix (an automated Confluence page) for real-time visibility. | Prisma Cloud, Confluence | Automated System |

**Port Opening Restrictions:** The following ports require documented VP of IT Operations approval, logged in an exception ticket:
- SSH (TCP/22): Only allowed from the Meridian Jump Host Security Group or CI/CD runner CIDR ranges.
- RDP (TCP/3389): Prohibited by default; requires an approved exception.
- Database ports (TCP/3306, 5432, 1433, 27017): Only allowed from approved application-tier SGs. Direct client access is forbidden.

### 5.3 Tagging Governance and Enforcement

Tagging is the foundational control for access management (ABAC), cost allocation, automation, and incident response. This procedure operationalizes Section 4.3.

#### 5.3.1 Mandatory Tag Schema

The following tags are mandatory for all provisioned resources. Resources missing mandatory tags are subject to automatic stoppage or termination as detailed in Section 5.3.2.

| Tag Key | Description | Allowed Values / Example | Enforcement Level |
| :--- | :--- | :--- | :--- |
| `meridian:env` | Deployment Environment | `prod`, `staging`, `uat`, `dev`, `sandbox`, `dr` | **Hard** (resource creation blocked) |
| `meridian:app-id` | Application Identifier | Mapped from CMDB (e.g., `medinsight-01`, `healthpay-api`). Cannot be free-text. | **Hard** |
| `meridian:cost-center` | Financial Accounting Code | 8-digit code (e.g., `CC-BUS-4102`) | **Hard** |
| `meridian:data-class` | Highest Data Classification Level | `public`, `internal`, `confidential`, `strictly-confidential` | **Hard** |
| `meridian:owner` | Primary Owner (Email Distro) | Team DL (e.g., `dl-plat-eng@meridian.com`). No individual emails. | **Hard** |
| `meridian:compliance` | Regulatory Framework | `hipaa`, `soc2`, `eu-ai-act`, `sr11-7`, `iso27001`, `none` (comma-separated if multiple) | **Hard** |
| `meridian:automation` | Automation Opt-In | `backup:true/false`, `snapshot:true/false`, `patch:true/false` | **Medium** (automated actions may fail if absent) |

#### 5.3.2 Procedure: Automated Tag Remediation

| Step | Action | Role | Tool/System |
| :--- | :--- | :--- | :--- |
| 1. | **Event Trigger:** AWS Config captures a `create` or `modify` event for any supported resource (e.g., EC2 instance `i-12345`). A custom AWS Config rule `require-meridian-tags` evaluates the resource's tag set. | Automated | AWS Config |
| 2. | **Tag Validation:** If a "Hard" enforcement level tag is missing, the resource is flagged as `NON_COMPLIANT`. If all "Hard" tags are present, the rule passes the resource as `COMPLIANT`. | Automated | AWS Config |
| 3. | **Grace Period Warning:** A "Soft" SNS notification is published to the resource owner's Slack channel (derived from a non-required `contact` tag or event trail) and email. The message warns: "Resource {arn} is missing mandatory tags: {missing_keys}. Self-healing in 60 minutes." | Automated | SNS, Slack, SES |
| 4. | **Hard Enforcement (Non-Prod):** After 60 minutes with no remediation, a Lambda function named `tag-enforcer` is invoked. For all accounts in the `Workloads/Dev` and `Workloads/Staging` OUs, the function calls `ec2:StopInstances` or the equivalent stop/deactivate API for the service. A final notice is sent. | Automated | Lambda, AWS APIs |
| 5. | **Hard Enforcement (Production):** For `Workloads/Prod` accounts, auto-stoppage is not applied. Instead, the resource is flagged in the weekly "Prod Compliance Dashboard" reviewed by the VPs of Engineering and IT Operations. A ticket is automatically created in the team's Jira backlog with a P3 priority. Failure to remediate within 5 business days results in escalation to the Chief Compliance Officer. | Automated, VP IT Ops | Jira, ServiceNow, Datadog Dashboard |

### 5.4 Identity and Access Management (IAM) Governance

#### 5.4.1 IAM Role Strategy

Meridian uses a strictly role-based access model, federated with Okta. No long-lived IAM user access keys are permitted. The following standard roles are pre-configured in every account by the Landing Zone:

| Role Name | Intended Principal | Permissions Boundary |
| :--- | :--- | :--- |
| `AWSAdminRole` | Platform Engineering / Break Glass | Attached to `AdministratorAccess` policy, gated by an SCP requiring MFA and blocking specific destructive actions on KMS/CloudTrail. |
| `ReadOnlyRole` | All authenticated internal users | Attached to `ReadOnlyAccess`, with explicit denies on S3 objects tagged with `data-class=strictly-confidential`. |
| `PipelineDeployRole` | GitHub Actions Runners (OIDC) | Limited to application-specific deployment actions (ECS UpdateService, Lambda UpdateFunctionCode, S3 PutObject to app-specific buckets). |
| `SecurityAuditRole` | Prisma Cloud, CrowdStrike | Limited to read-only security APIs, with specific allow-lists for automated remediation actions (e.g., `ec2:RevokeSecurityGroupIngress`). |
| `DataScientistRole` | Clinical AI Team | Grants `sagemaker:*` on resources tagged `app-id=clin-ai-*` only. No access to direct database credentials or KMS `Decrypt` except for model-encryption key. |

#### 5.4.2 Procedure: Quarterly IAM Access Review

Per SOC 2 CC6.1, 6.2, and 6.3, formal access reviews must be conducted. This procedure is the operational execution of that control.

| Step | Action | Role | Tool/System |
| :--- | :--- | :--- | :--- |
| 1. | **Campaign Initiation:** On the first business day of each fiscal quarter (Jan, Apr, Jul, Oct), the CISO (R. Kim) authorizes the IAM Governance Automation to initiate an access certification campaign. | CISO | Okta, AWS SSO |
| 2. | **Report Generation:** A script run by the IAM team exports: a) All IAM roles in each account, b) All SSO Group mappings to those roles, c) All Okta group memberships. The data is compiled into a certification report in ServiceNow, with records segmented by Business Unit. | IAM Team | Lamba, ServiceNow |
| 3. | **Manager Certification:** Each BU lead (e.g., Dr. Aisha Okafor for Clinical AI, Robert Liu for Financial Services) receives a notification to certify their team's access. They must assert one of three actions for each record: **Certify**, **Modify** (with revised role/permission), or **Revoke**. | BU Leads | ServiceNow |
| 4. | **Remediation:** For "Revoke" or "Modify" actions, ServiceNow workflows automatically create Jira tasks for the IAM Team. For Revocations, the team must remove the Okta group mapping within 2 business days. Modifications are processed with a 5-business-day SLA. | IAM Team, ServiceNow | Jira, Okta |
| 5. | **Confirmation of Completion:** The IAM Governance Automation verifies that all records are actioned. A final summary report, including attestations of completion from all BU leads, is sent to the CISO, Chief Compliance Officer, and VP of IT Operations for the quarterly review board. | IAM Governance Auto. | ServiceNow, Email |

### 5.5 Financial Operations (FinOps) Procedure

#### 5.5.1 Monthly Budget-to-Actuals Reconciliation

| Step | Action | Role | Tool/System |
| :--- | :--- | :--- | :--- |
| 1. | **Data Ingestion:** On the 3rd of each month, the FinOps Manager pulls the previous month's finalized CUR (Cost and Usage Report) from the management account's S3 bucket into the FinOps tool (CloudHealth). Cost, discount, and credit data are segmented by cost center tag. | FinOps Manager | CloudHealth, AWS S3 |
| 2. | **Variance Analysis:** An automated report identifies any account where actual spend exceeds the monthly budget by 15% or $5,000 (whichever is smaller). The FinOps Analyst annotates the variance with an identified cause (e.g., dev environment left running, unexpected scale-out, market cost increase). | FinOps Analyst | CloudHealth |
| 3. | **Rightsizing Recommendations:** The tool generates a rightsizing report for all idle EC2 instances (CPU < 5%, Network < 5 MB over 30 days), unattached EBS volumes, and underutilized RDS instances. | Automated | CloudHealth |
| 4. | **Stakeholder Review Meeting:** On the 2nd Tuesday of the month, the FinOps Manager chairs a 45-minute call with all BU leads and engineering managers whose accounts breached the budget or have significant rightsizing recommendations. Action items (e.g., resize instance `i-xyz` to `c6i.xlarge`, purchase 1-year RI, or delete the stale dev stack) are assigned in Jira with a 10-business-day resolution SLA. | FinOps Manager, BU Leads | Jira |
| 5. | **Savings Realization:** The FinOps Manager executes approved reservation (RI/SP) purchases. Purchase orders and invoices are logged in Coupa for financial tracking. The realized savings are reported in the next monthly review cycle. | FinOps Manager | AWS, Coupa |

---

## 6. Controls and Safeguards

This section details the specific, technical, and administrative controls deployed to satisfy SOC 2 Trust Services Criteria, focusing on Security, Availability, and Confidentiality.

### 6.1 Preventive Controls

| Control ID | Control Description | SOC 2 Criterion | Implementation Detail |
| :--- | :--- | :--- | :--- |
| **CTL-CLD-001** | **Service Control Policies (SCPs)** | CC6.1, CC6.3 | SCPs are applied at the OU level to deny actions that would undermine controls. Key SCPs include: <ul><li>**deny-iam-changes:** In `Workloads/Prod`, denies `iam:CreateUser`, `iam:PutUserPolicy`, `iam:CreateAccessKey` to all non-admin roles, enforcing the roles-based, keyless model.</li><li>**deny-regions-except:** Denies all actions outside `us-east-1`, `us-west-2`, and `eu-west-1` (where applicable by compliance tag).</li><li>**deny-cloudtrail-stop:** Denies `cloudtrail:StopLogging` and `cloudtrail:DeleteTrail` globally.</li></ul> |
| **CTL-CLD-002** | **AWS Control Tower Guardrails** | CC6.1, CC6.6 | Preventative and Detective Guardrails are enabled. <ul><li>**Preventive:** `Disallow RDP Access` via NACL, `Disallow direct internet access to RDS`. Managed by the Landing Zone Admin.</li><li>**Detective:** `Detect whether public write access to S3 buckets is enabled`, `Detect whether unrestricted ingress SSH access is allowed`.</li></ul>Continuous drift-monitoring by Control Tower automatically remediates non-compliant baselines. |
| **CTL-CLD-003** | **Golden AMI Pipeline** | CC7.1, CC7.2 | A monthly, hardened AMI is created by the Platform Engineering team using HashiCorp Packer. The pipeline: a) Pulls the latest official Amazon Linux 2023 AMI, b) Applies all Critical/CVSS > 7 patches, c) Installs the CrowdStrike Falcon agent, the Datadog agent, and the `cis-benchmark-hardening` Ansible playbook, d) Scans the image with Prisma Cloud Twistlock, e) Publishes the AMI as a private image, tagged `golden-base-YYYY-MM`. All EC2 launch templates in production must reference the latest monthly Golden AMI. |
| **CTL-CLD-004** | **IAM Permissions Boundaries** | CC6.1 | A mandatory, non-modifiable permissions boundary policy, `meridian-restricted-boundary`, is attached to all developer-facing roles in product accounts. This boundary sets a hard limit on IAM role creation, S3 bucket policy modification, and CloudTrail/KMS tampering, regardless of the attached IAM policies. |

### 6.2 Detective Controls

| Control ID | Control Description | SOC 2 Criterion | Implementation Detail |
| :--- | :--- | :--- | :--- |
| **CTL-CLD-010** | **AWS CloudTrail (Management & Data Events)** | CC7.1, CC7.2 (CC6.1-6.8) | An organization-wide CloudTrail is active in the `Audit` account. <ul><li>**Management Events:** Enabled for Read/Write on all accounts, sent to a central S3 bucket.</li><li>**Data Events:** Enabled for all S3 buckets tagged `compliance=soc2` and all Lambda invocations.</li><li>**Integrity:** CloudTrail Log File Validation is enabled, and logs are immediately forwarded to the SIEM (Splunk) via a central EventBridge Bus.</li></ul> |
| **CTL-CLD-011** | **Prisma Cloud CSPM (Real-Time)** | CC6.1, CC6.6, CC7.2 | Prisma Cloud performs continuous configuration scanning. It ingests AWS Config data and evaluates 500+ pre-built and custom policies against every account. Critical/High alerts are routed to the Security Operations Center (SOC) Slack channel (`#secops-high`) and create a P1 incident if not acknowledged in 15 minutes. |
| **CTL-CLD-012** | **AWS GuardDuty** | CC7.2, CC7.3 | GuardDuty is enabled for all accounts. Findings are centralized to the `Security` account. A Lambda-based auto-remediation playbook is linked to specific findings: <ul><li>**UnauthorizedAccess:EC2/MaliciousIPCaller:** Automatically triggers a `RevokeSecurityGroupIngress` on the impacted security group and adds the IP to a blocklist in Network Firewall.</li><li>**CryptoCurrency:EC2/BitcoinTool:** Automatically tags the EC2 instance and notifies the SOC for immediate containment.</li></ul> |
| **CTL-CLD-013** | **Resource Configuration Drift Detection** | CC7.1, CC7.2 | Terraform Cloud's "Drift Detection" feature is scheduled to run every 24 hours on all production workspaces. Drift detection identifies any deviation between the Terraform state and the real-world resource state. A weekly "Drift Remediation" meeting is held by the Platform Engineering team to reconcile any non-emergency deviations. |

### 6.3 Corrective Controls

| Control ID | Control Description | SOC 2 Criterion | Implementation Detail |
| :--- | :--- | :--- | :--- |
| **CTL-CLD-020** | **Auto-Remediation Playbooks** | CC6.6, CC7.2 | AWS Systems Manager (SSM) Automation Documents are linked to specific Security Hub findings. Examples: <ul><li>`Remediate-S3BlockPublicAccess`: Re-applies account-level `BlockPublicAccess` if an account-level control is disabled.</li><li>`Remediate-SGRule-OverlyPermissive`: Removes a security group rule that has a source of `0.0.0.0/0` for ports other than 80/443.</li></ul>All auto-remediation actions are logged to the SIEM and Slack with full before/after context. |
| **CTL-CLD-021** | **Disaster Recovery (Azure Cold Site)** | A1.2, A1.3 | The Meridian SaaS Platform, deployed in AWS `us-east-1`, has a 4-hour RTO and a 1-hour RPO target. Critical application AMIs, Terraform state, and nightly Aurora snapshots are replicated via an immutable, air-gapped mechanism to an Azure cold storage account in the `Azure-US-East` region. The DR Plan (SOP-DR-003) details the controlled failover procedure, invoked only with the joint authorization of the CEO, CISO, and VP of Engineering. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Metrics

The following KPIs are reviewed in the monthly Cloud Operations Scorecard to measure the effectiveness of this SOP and associated controls.

| Category | Metric (KPI) | Target | Measurement Tool | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **Security Posture** | Mean Time to Remediate (MTTR) for Critical CSPM Findings | < 24 hours | Prisma Cloud | Cloud Security Architect |
| **Security Posture** | % of EC2 Instances Launched from Latest Golden AMI | 100% (Prod), 95% (Staging) | AWS Config / CMDB | Platform Engineering Lead |
| **IAM Hygiene** | % of Over-Privileged IAM Roles (High/Risk Score from IAM Access Analyzer) | < 2% in Production | AWS IAM Access Analyzer, Splunk | IAM Team |
| **Operations** | Drift Detection Reconciliation Rate (Terraform) | > 98% of detected drift reconciled within 7 days | Terraform Cloud | Dir. of Cloud Ops |
| **Network** | Number of Security Group Rules with `0.0.0.0/0` CIDR Source | 0 (for ports < 1024) | Prisma Cloud | Cloud Security Architect |
| **Cost Management** | % Variance of Actual Spend vs. Forecasted Budget | < 10% aggregate | CloudHealth | FinOps Manager |
| **Cost Management** | Effective Savings Rate (from Reservations/Savings Plans) | > 25% discount on eligible compute | CloudHealth | FinOps Manager |

### 7.2 Reporting Cadence

- **Daily:** An automated email from Prisma Cloud summarizing net-new "High" and "Critical" posture findings is sent to the `dl-cspm-ops@meridian.com` list. A Datadog dashboard showing real-time resource health, count, and cost anomalies is displayed on the IT Ops NOC screens.
- **Weekly (Every Monday):** The "FinOps Weekly Snapshot" report is distributed, highlighting accounts with a predicted monthly overrun. The "Weekly Cloud Change" report, auto-generated from Jira and Terraform Cloud, is sent to the VP of IT Operations.
- **Monthly (3rd Tuesday):** The formal "Cloud Operations Scorecard" meeting is held with Samantha Torres (VP IT Ops, Chair), David Park (VP Eng), the Director of Cloud Ops, and the CISO. Deviations from KPI targets are reviewed, root cause analyses are presented, and corrective actions are assigned.
- **Quarterly:** A formal SOC 2 Controls Effectiveness report is compiled, referencing aggregated KPI data, findings from the quarterly access review, and results from the latest penetration test. This report is presented to the Audit Committee.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process
Deviations from the policies and procedures in this document require a formal, time-bound exception. Exceptions are not permanent waivers but risk-accepted allowances with specific expiration dates.

1.  **Submit Formal Request:** The requestor completes the "Cloud Policy Exception Request" form in ServiceNow (Form-IT-800). The form requires:
    - The specific policy section for which an exception is sought.
    - A detailed technical justification explaining why compliance is not possible.
    - A compensating control description detailing what alternative measures will mitigate the resultant risk.
    - The requested duration of the exception (maximum 90 days).
2.  **Risk Assessment:** The Cloud Security Architect performs a formal risk assessment, assigning a "Residual Risk Score." Scores of "High" or "Critical" automatically require additional sign-off.
3.  **Business Justification Validation:** The relevant Business Unit lead must validate the critical business need driving the exception request.
4.  **Approval:** All exceptions require approval from:
    - VP of IT Operations (S. Torres)
    - CISO (R. Kim) for security-related exceptions (e.g., an overly permissive SG).
    - CTO for architecture-level exceptions.

### 8.2 Exception Tracking and Expiry
Approved exceptions are tracked in a central ServiceNow register. The register is reviewed by the VP of IT Operations weekly. 14 days and 7 days before an exception expires, automated alerts are sent to the requestor and approver via ServiceNow and email. The exception cannot be "renewed" without going through the full, new request process again, including a re-evaluation of the need for a permanent, compliant architectural solution.

### 8.3 Escalation Path for Out-of-Policy Drift
If the automated drift detection (Section 6.2, CTL-CLD-013) discovers a manually applied production change, the `tag-enforcer` Lambda in the `Audit` account performs the following escalation chain:

1.  **T+0 min (Detection):** The "ClickOps Alert" fires in the `#prod-drift-critical` Slack channel, tagging the Platform Engineering Lead and the Director of Cloud Ops. A P2 ticket is created automatically.
2.  **T+60 min (No Acknowledgment):** The VP of Engineering (D. Park) is tagged and notified via text message (PagerDuty).
3.  **T+240 min (No Remediation/Rollback Plan):** The Chief Information Security Officer (R. Kim) and VP of IT Operations (S. Torres) are directly paged for an on-call incident bridge.

### 8.4 Break-Glass Procedure for Emergency Access
A privileged role, `BreakGlassRole`, exists in each production account, gated by an SCP that requires both an MFA token from a hardware security key and the completion of an emergency access form on the PagerDuty incident. Logging for actions performed by this role is streamed in real-time to the CISO's Slack channel and the Compliance team. Any account where `BreakGlassRole` is used is quarantined for 24 hours post-incident for a full forensic audit.

---

## 9. Training Requirements

| Training Module | Target Audience | Frequency | Delivery Method | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **MND-INF-101: Cloud Security & Shared Responsibility** | All personnel with AWS access | Annually | LMS (LearnUpon) | Completion status fed to Okta. Access keys are suspended 7 days post-expiry. |
| **MND-INF-102: IaC & Terraform Fundamentals** | All members of IT Ops, Platform Engineering, and Security Engineering | Once, within 90 days of hire | Instructor-led Workshop | Tracked in Jira Learning Path. |
| **MND-INF-103: SOC 2 Controls and the Practitioner** | BU Leads, Engineering Managers, all Senior Engineers | Quarterly Lunch & Learn, content refreshed based on previous quarter's control deficiencies | Live (Virtual/In-Person) | Attendance recorded in LMS by the CCoE. |
| **MND-INF-104: FinOps for Engineers** | All developers tagged as `cost-center-owner` | Annually | Self-paced eLearning (AWS Skill Builder) | Certification of completion uploaded to HR Profile. |
| **MND-INF-105: Tagging Hygiene Workshop** | All Cloud Users | On-Demand (Prerequisite for Dev Sandbox access) | Self-paced LMS with a hands-on lab | Completion auto-requests the developer's first sandbox account. |

Compliance with mandatory training is a condition of continued access to the Meridian AWS Organization. The VP of IT Operations will review training completion rates monthly.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- **SOP-SEC-015:** Identity and Access Management for Federated Users
- **SOP-SEC-023:** Security Architecture Review Process
- **SOP-CHG-001:** Standard IT Change Management Process
- **SOP-DEVP-005:** CI/CD Pipeline and Infrastructure as Code Management
- **SOP-DATA-002:** Data Lifecycle and Retention Policy
- **SOP-DR-003:** IT Disaster Recovery and Business Continuity Plan
- **SOP-VEN-001:** Third-Party Vendor Risk Management Program

### 10.2 External Standards and References
- **AWS Well-Architected Framework:** Security Pillar, Operational Excellence Pillar, Cost Optimization Pillar.
- **AWS Control Tower Documentation:** Account Factory for Terraform (AFT), Guardrail Reference.
- **CIS AWS Foundations Benchmark:** Version 3.0.0, used as a baseline for CSPM policies.
- **NIST SP 800-53 Rev. 5:** Control Families AC, AU, CM, IR, SC, SI. Mapped internally to all controls in Section 6.

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
| :--- | :--- | :--- | :--- | :--- |
| 4.7 | 2026-06-16 | J. Mbeki, Cloud Ops | S. Torres | Minor update: Added control CTL-CLD-004 (Boundaries). Updated KPI targets for Q3 2026 SOC 2 readiness. Clarified Golden AMI pipeline scanner from Clair to Prisma Cloud Twistlock. Standardized tagging schema documentation. |
| 4.6 | 2025-11-15 | L. Chen, Platform Eng | D. Park | Major revision: Migrated from a multi-org to a single-org, multi-OU Landing Zone structure. Formalized Break Glass (8.4) procedure. Changed IaC tool from CloudFormation to Terraform across all procedures. Added detailed FinOps procedure in Section 5.5. |
| 4.5 | 2025-07-02 | J. Mbeki, Cloud Ops | S. Torres | Updated RTO/RPO targets in Section 6.3. Added the explicit prohibition on manual console changes in Production (4.1.3). Integrated the new ServiceNow request forms. |
| 4.4 | 2025-04-11 | A. Rodriguez, CCoE | D. Park | Rewritten Section 5.2 on Security Group management for a zero-trust model. Introduced the mandatory tag schema in Section 5.3. Updated names of all roles to reflect title changes from the Q1 reorganization. |
| 4.0 | 2025-02-22 | S. Patel, Sec Arch  | S. Torres | Foundational re-write and re-certification for EU AI Act readiness. Introduced the `meridian:compliance` tag, designated the `eu-west-1` OU, and added Prisma Cloud as a named CSPM tool. Formalized the SOC 2 controls table in Section 6. |