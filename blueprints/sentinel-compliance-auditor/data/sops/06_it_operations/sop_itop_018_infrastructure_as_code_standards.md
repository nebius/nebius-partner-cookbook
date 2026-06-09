---
sop_id: "SOP-ITOP-018"
title: "Infrastructure as Code Standards"
business_unit: "IT Operations & Infrastructure"
version: "4.7"
effective_date: "2024-02-17"
last_reviewed: "2025-02-01"
next_review: "2025-08-10"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide standards, governance framework, and operational procedures for managing Infrastructure as Code (IaC) at Meridian Health Technologies, Inc. The purpose of this document is to ensure that all cloud infrastructure provisioning, configuration management, and deployment activities are performed in a consistent, repeatable, and auditable manner that supports the reliability, scalability, and security posture of the Meridian SaaS Platform.

IaC is the foundational layer upon which all Meridian business lines operate—the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the underlying Meridian SaaS Platform. Inconsistent infrastructure management introduces configuration drift, deployment failures, and potential security vulnerabilities that could impact patient care delivery, financial transaction integrity, and the confidentiality of protected health information (PHI).

This SOP codifies the toolchain, workflows, review requirements, state management practices, and drift remediation procedures that govern how infrastructure code is authored, tested, versioned, and deployed across all Meridian environments.

### 1.2 Scope

This SOP applies to:

| **In Scope** | **Out of Scope** |
|---|---|
| All AWS (us-east-1, eu-west-1) production and non-production accounts | Azure DR environment (governed by SOP-ITOP-022) |
| All Azure (DR) environments where IaC is used for disaster recovery orchestration | On-premises network hardware at Meridian corporate offices |
| Infrastructure code repositories in Meridian's GitHub Enterprise instance | Application code deployments (governed by SOP-ENG-042) |
| Configuration management code, modules, and playbooks | CI/CD pipeline definitions, except where they orchestrate IaC execution |
| State files, lock files, and backend storage configurations | |
| All contractors, vendors, and third parties with access to Meridian IaC repositories | |

### 1.3 Applicability

All Meridian personnel, contractors, and third-party service providers involved in the authoring, reviewing, testing, deploying, or maintaining of infrastructure code must comply with this SOP. Compliance is mandatory and non-negotiable. Non-compliance shall be addressed through the exception and escalation process outlined in Section 8.

This SOP applies to all Meridian environments classified as Production, Staging, QA, Development, and Sandbox. The specific controls applicable to each environment tier are defined in Section 6.

---

## 2. Definitions and Acronyms

| **Term/Acronym** | **Definition** |
|---|---|
| **IaC (Infrastructure as Code)** | The practice of managing and provisioning computing infrastructure through machine-readable definition files, rather than through physical hardware configuration or interactive configuration tools. |
| **Terraform** | HashiCorp's open-source infrastructure as code software tool, used by Meridian for provisioning and managing cloud resources across AWS and Azure. |
| **Ansible** | Red Hat's open-source automation platform used for configuration management, application deployment, and intra-service orchestration. |
| **Packer** | HashiCorp's open-source tool for creating identical machine images for multiple platforms from a single source template. Used by Meridian for Amazon Machine Image (AMI) and Azure Managed Image generation. |
| **State File** | A Terraform-specific artifact (terraform.tfstate) that maps real-world resources to the configuration, tracks metadata, and enables management of infrastructure through declarative code. |
| **State Locking** | A mechanism that prevents concurrent operations on the same state file, avoiding race conditions and state corruption. Meridian implements this via DynamoDB (AWS) and Azure Blob Storage leases. |
| **Backend** | The destination system where Terraform state files are stored. Meridian uses S3 (AWS) with DynamoDB locking and Azure Blob Storage with native locking. |
| **Module** | A self-contained package of IaC configurations that can be reused, versioned, and shared across teams. |
| **Provider** | A plugin that Terraform uses to interact with cloud providers, SaaS providers, and other APIs. Meridian-approved providers are listed in Appendix A. |
| **Plan** | The output of `terraform plan`: a diff between the current (or intended) state and the desired configuration. Plans must be reviewed before application. |
| **Workspace** | A logical separation of state files for the same configuration. Meridian uses Terraform Cloud Workspaces for environment segregation. |
| **Configuration Drift** | The deviation between the actual state of infrastructure and the expected state defined in IaC, typically arising from manual console changes. |
| **GitOps** | The paradigm of using Git repositories as the single source of truth for declarative infrastructure and application configurations. |
| **Pull Request (PR)** | A GitHub mechanism for proposing and reviewing code changes before merging into protected branches. |
| **Protected Branch** | A Git branch (e.g., main, production) that requires pull requests, status checks, and specific reviewer approvals before merging. |
| **Terragrunt** | A thin wrapper around Terraform that provides extra tools for keeping configurations DRY (Don't Repeat Yourself), managing remote state, and handling multi-account deployments. |
| **Sentinel** | HashiCorp's policy-as-code framework embedded in Terraform Cloud/Enterprise for enforcing guardrails before infrastructure provisioning. |
| **RACI** | A responsibility assignment matrix: Responsible, Accountable, Consulted, Informed. |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| **Role** | **Authoring IaC** | **Code Review** | **State Management** | **Deployment Approval** | **Drift Remediation** | **Exception Approval** |
|---|---|---|---|---|---|---|
| Infrastructure Engineer (ITOps) | **R** | **R** | **R** | | **R** | |
| Senior Infrastructure Engineer (ITOps) | **R** | **R** | **R** | **R** | **R** | |
| Cloud Architect (Platform Engineering) | **R** | **R** | | | | |
| DevOps Engineer (Business Units) | **R** | | | | | |
| VP of IT Operations | | | | **A** | | **A** |
| VP of Engineering | | | | **A** | | **A** |
| Security Engineer (InfoSec) | | **R** | | | | |
| Compliance Officer | | | | | | **A** |
| Data Protection Officer (DPO) | | | | | | **I** |
| Service Owners (Clinical IA, HealthPay, MedInsight) | **I** | **I** | **I** | **I** | **I** | **I** |

### 3.2 Role Definitions

**Infrastructure Engineer (ITOps)**
The primary author and maintainer of IaC configurations. Responsible for writing conformant Terraform and Ansible code, testing plans in sandbox environments, submitting pull requests, applying approved plans, and executing drift remediation runbooks. Must hold Meridian IaC Competency Certification (see Section 9).

**Senior Infrastructure Engineer (ITOps)**
Provides technical review of IaC pull requests. Approves or rejects deployment plans based on conformance to this SOP, architecture standards, and security best practices. Serves as first escalation point for drift incidents. Acts as backup for state management operations.

**Cloud Architect (Platform Engineering)**
Designs the IaC module architecture, provider strategy, and workspace hierarchy. Maintains the Meridian IaC Module Registry. Ensures that IaC patterns align with Meridian's Well-Architected Framework assessment criteria.

**DevOps Engineer (Business Units)**
Contributes IaC code specific to their business unit's application infrastructure. Must adhere to this SOP's coding standards and review process. Cannot approve their own pull requests.

**VP of IT Operations (Samantha Torres)**
Serves as final approver for production deployments exceeding defined blast radius thresholds (see Section 5.8). Accountable for overall IaC governance and this SOP's maintenance.

**VP of Engineering (David Park)**
Approves this SOP and any subsequent revisions. Accountable for ensuring IaC standards align with Meridian's engineering excellence objectives.

**Security Engineer (InfoSec)**
Reviews IaC code for security vulnerabilities, hardcoded secrets, overly permissive IAM policies, and non-conformance to SOP-SEC-007 (Security Groups and Network Controls). Can block merges via Sentinel policy overrides.

**Compliance Officer**
Audits IaC deployment logs and PR records for evidence of compliance control effectiveness. Approves exceptions related to regulatory carve-outs.

**Data Protection Officer (DPO)**
Consulted on IaC changes that may impact data residency, encryption boundary, or PHI/PII processing environments. Must be informed of any production IaC changes affecting eu-west-1.

---

## 4. Policy Statements

### 4.1 Source of Truth
The Meridian IaC repository in GitHub Enterprise is the single source of truth for all cloud infrastructure configuration. No resource may be provisioned, modified, or decommissioned outside of the IaC pipeline except under a declared incident response per SOP-IR-001.

### 4.2 Immutable Infrastructure
Meridian adopts an immutable infrastructure philosophy. Configuration changes shall result in the provisioning of new resources or instances rather than in-place modification of existing running systems. Exceptions: Stateful data stores (RDS, DynamoDB) and transient non-production environments where in-place updates are explicitly designated.

### 4.3 Idempotency
All Meridian IaC configurations must be idempotent. Repeated application of the same configuration shall produce the same result without error. This includes the ability to `terraform apply` multiple times in succession without unintended side effects.

### 4.4 Declarative Paradigm
Meridian exclusively uses declarative IaC tools (Terraform, Ansible in declarative mode). Imperative scripts (CLI commands, AWS CloudFormation not routed through IaC pipeline) are prohibited in production and staging environments.

### 4.5 Infrastructure Lifecycle Management
Every cloud resource provisioned via IaC must be tracked through its entire lifecycle: provisioned, modified, decommissioned. Decommissioning must be performed via the same IaC pipeline and not via console `destroy` operations on unattached resources.

### 4.6 Secret Management
No secrets, passwords, API keys, certificates, or any other sensitive data may be hardcoded in IaC configurations. All secrets must be retrieved at runtime from AWS Secrets Manager or Azure Key Vault, referenced via data sources with output suppression.

### 4.7 Module Reusability
All repeatable infrastructure patterns must be codified as versioned Terraform modules in the Meridian IaC Module Registry. Copy-paste duplication of non-module code is prohibited beyond a two-environment threshold.

---

## 5. Detailed Procedures

### 5.1 IaC Toolchain Selection

The Meridian IaC ecosystem is a curated toolchain. Selection is governed by use case and architectural domain:

| **Domain** | **Primary Tool** | **Version Floor** | **Purpose** |
|---|---|---|---|
| AWS Resource Provisioning | Terraform (HashiCorp) | 1.6.x | Create, update, delete AWS resources |
| AWS AMI Generation | Packer (HashiCorp) | 1.9.x | Build golden images for EC2 launch configurations |
| Azure Resource Provisioning | Terraform (HashiCorp) | 1.6.x | Manage DR footprint in Azure paired regions |
| Azure Managed Images | Packer (HashiCorp) | 1.9.x | DR image generation |
| Operating System Configuration | Ansible (Red Hat) | 9.x (AWX) | Post-provision hardening and baseline configuration |
| Infrastructure Orchestration | Terragrunt (Gruntwork) | 0.54.x | DRY configurations, remote state orchestration, multi-account |

Deviation from these approved tools requires an exception per Section 8.

### 5.2 Repository Structure and Branching Strategy

#### 5.2.1 Monorepo Structure
Meridian employs a monorepo strategy for all IaC, housed in `github.meridian.com/infra/meridian-iac`. The directory hierarchy follows this convention:

```
meridian-iac/
├── terraform/
│   ├── global/              # Route53 zones, IAM, Organizations
│   ├── accounts/
│   │   ├── production-aws/
│   │   │   ├── us-east-1/
│   │   │   │   ├── networking/
│   │   │   │   ├── compute/
│   │   │   │   ├── databases/
│   │   │   │   └── terraform.tfvars
│   │   │   └── eu-west-1/
│   │   ├── staging-aws/
│   │   ├── development-aws/
│   │   └── sandbox-aws/
│   └── modules/
│       ├── meridian-vpc/
│       ├── meridian-eks/
│       ├── meridian-rds-ph/
│       └── meridian-healthpay-fargate/
├── packer/
│   ├── meridian-ec2-bastion/
│   ├── meridian-eks-nodegroup/
│   └── meridian-healthpay-app/
├── ansible/
│   ├── roles/
│   └── playbooks/
└── terragrunt/
    └── *.hcl
```

#### 5.2.2 Branching Strategy
Meridian employs a trunk-based branching model with short-lived feature branches:

| **Branch** | **Purpose** | **Protection** |
|---|---|---|
| `main` | Production and staging configurations. Merges to `main` must pass CI/CD checks and trigger stage deployment. | Protected. Requires 2 approvals, passing status checks, and linear history. |
| `feat/<SOP-ID>-<ticket>` | Feature development for new infrastructure components. | None. Must be deleted after merge. |
| `fix/<SOP-ID>-<ticket>` | Bug fix branches. | None. Must be deleted after merge. |
| `drift/<detector-run-id>` | Automated drift remediation branches. | None. Must be deleted after merge. |
| `hotfix/<incident-id>` | Emergency production fixes (per SOP-IR-001). | Temporarily unprotected (time-boxed to 4 hours). |

Branches must be prefixed with the SOP-ID or incident ID that authorizes the change.

### 5.3 Infrastructure Code Authoring Standards

#### 5.3.1 Language and Style
All Terraform code must be written in HashiCorp Configuration Language (HCL2). Terraform JSON syntax (`*.tf.json`) is prohibited due to reduced readability.

#### 5.3.2 Resource Naming Convention
All resources must follow the Meridian Resource Naming Convention:

```
meridian-{environment}-{region-abbrev}-{service}-{resource-type}-{ordinal}
```

**Example:** `meridian-prod-use1-clinicalai-eks-cluster-01`

#### 5.3.3 Tagging Requirements
All taggable resources must include the following mandatory tags:

| **Tag Key** | **Value Source** | **Example** |
|---|---|---|
| `Environment` | Workspace variable `var.environment` | `production` |
| `BusinessUnit` | Hardcoded per module | `HealthPay` |
| `SOP-Version` | Hardcoded per deployment | `SOP-ITOP-018:v4.7` |
| `CostCenter` | Hardcoded per service owner | `CC-HEALTHPAY-001` |
| `DataClassification` | Per Meridian Data Classification Policy (SOP-INFOSEC-002) | `PHI`, `PCI`, `PII`, `Internal`, `Public` |
| `ManagedBy` | Hardcoded | `Terraform` |
| `ReviewTicket` | Variable populated from CI/CD pipeline | `JIRA-ITOP-2945` |

#### 5.3.4 Variable and Output Definitions
All variables must be explicitly declared with descriptions and type constraints:

```hcl
variable "environment" {
  description = "Deployment environment (production, staging, qa, development, sandbox)"
  type        = string

  validation {
    condition     = contains(["production", "staging", "qa", "development", "sandbox"], var.environment)
    error_message = "Environment must be one of the allowed values."
  }
}
```

All outputs must be explicitly declared with descriptions. Outputs containing sensitive data (ARNs with account IDs, endpoint URLs with tokens) must be flagged with `sensitive = true`.

#### 5.3.5 Provider Configuration
Provider configurations must be version-constrained using pessimistic constraint operators:

```hcl
provider "aws" {
  region  = var.aws_region
  version = "~> 5.0"
  assume_role {
    role_arn = "arn:aws:iam::${var.account_id}:role/TerraformExecutionRole"
  }
}
```

### 5.4 Code Review Workflow

The code review workflow is the critical control gate between authoring and deployment. The process is as follows:

1. **Author Creates Feature Branch:**
   Infrastructure Engineer branches from `main` using the convention `feat/SOP-ITOP-018-{JIRA-ID}`.

2. **Author Commits Changes:**
   Commits must be granular and well-annotated. Squash commits from messy local history before pushing.

3. **Author Opens Pull Request:**
   Pull request description must use the Meridian IaC PR Template:

   ```
   ## Change Description
   [Describe the infrastructure change]

   ## Blast Radius
   [Which environments, accounts, regions, resources are affected?]

   ## Plan Output (Terraform)
   <details>
   <summary>terraform plan</summary>
   [Paste plan output]
   </details>

   ## Pre-Deployment Checklist
   - [ ] Plan output has been appended above
   - [ ] Sentinel policy checks passed
   - [ ] All variables have descriptions
   - [ ] Mandatory tags are included
   - [ ] No hardcoded secrets
   - [ ] Outputs do not leak sensitive data
   - [ ] Module versions are pinned
   - [ ] Rollback plan is documented in PR comments

   ## Deployment Approval Request
   [Request specific approval by tagging approvers]
   ```

4. **Automated Checks Execute:**
   Upon PR creation, the CI pipeline (GitHub Actions workflow `iac-pr-checks.yml`) runs:
   - `terraform fmt -check -recursive`
   - `terraform validate` (per module)
   - `tflint` (with Meridian custom ruleset)
   - `checkov` (static analysis for security misconfigurations)
   - Sentinel policy checks (via Terraform Cloud run triggers)

   All automated checks must pass before merge.

5. **Peer Review Required:**
   - **Non-Production Changes:** Minimum 1 Senior Infrastructure Engineer approval.
   - **Production Changes:** Minimum 2 approvals: 1 Senior Infrastructure Engineer + 1 of (VP of IT Operations, VP of Engineering, Security Engineer).
   - **Module Registry Changes:** 1 Senior Infrastructure Engineer + 1 Cloud Architect.

6. **Reviewer Responsibilities:**
   Reviewers must verify:
   - Resource naming convention compliance
   - Mandatory tags are included
   - No hardcoded secrets (using `gitleaks` pre-commit hook locally, validated in CI)
   - IAM policies follow least privilege
   - Security groups do not contain overly permissive ingress rules
   - Plan output does not delete production resources unintentionally
   - State locking backend is correctly configured

7. **Approval and Merge:**
   Once approvals are granted and all checks pass, the author squashes and merges the PR. The `main` branch head SHA is recorded in the deployment metadata.

### 5.5 State Management

#### 5.5.1 Backend Configuration
Meridian uses a centralized remote backend for all Terraform state:

| **Cloud Provider** | **Backend** | **Locking Mechanism** | **Encryption** |
|---|---|---|---|
| AWS | S3 bucket `meridian-terraform-state-{account}-{region}` | DynamoDB table `meridian-terraform-locks` | SSE-KMS with Meridian KMS CMK `arn:aws:kms:...:key/meridian-tfstate` |
| Azure | Azure Blob Storage container `meridian-tfstate-{subscription}` | Native Azure blob lease | Azure Storage Service Encryption with Microsoft-managed keys |

The S3 bucket and DynamoDB table are provisioned via a "bootstrap" Terraform configuration that exists outside the main monorepo (managed by Infrastructure Engineering team and accessed via temporary credentials).

#### 5.5.2 State File Isolation
State files must be strict, one-to-one mappings: one state file per environment, per region, per service component. Monolithic state files spanning multiple environments or services are prohibited.

**Example mapping:**
- `production-aws-us-east-1-networking.tfstate`
- `production-aws-us-east-1-clinicalai-compute.tfstate`
- `production-aws-eu-west-1-medinsight-db.tfstate`

#### 5.5.3 State Locking Enforcement
State locking is enforced by the backend and must not be bypassed. If an engineer encounters a stale lock (held by a disconnected Terraform Cloud run), they must escalate via the Infrastructure Ops Slack channel (#infra-alerts) for manual lock release. Force-unlock commands (`terraform force-unlock`) require the approval of the VP of IT Operations, except during incident response.

#### 5.5.4 State Backup and Recovery
S3 buckets are configured with versioning enabled. Azure Storage containers have soft delete enabled (retention: 7 days). State recovery from a prior version is an incident-level activity, requiring the approval of the VP of IT Operations. The procedure for state recovery from S3 versioned objects is documented in the Infrastructure Operations Runbook (Confluence: "Terraform State Recovery").

### 5.6 Plan and Apply Workflow

1. **Trigger:** Merge to `main` triggers the Terraform Cloud run workflow for the appropriate workspace.

2. **Speculative Plan:** Terraform Cloud automatically runs `terraform plan`. The plan output is posted as a comment on the merged PR and stored as a run artifact in Terraform Cloud.

3. **Plan Review:** The Infrastructure Engineer who authored the change (or the on-call engineer if the author is unavailable) must review the final plan within Terraform Cloud's UI. This is a secondary check beyond the PR review.

4. **Cost Estimation:** Infracost integration runs against the plan and posts an estimated monthly cost change. For changes exceeding +$500/month, the VP of IT Operations must approve the apply.

5. **Apply Approval:** For **production environments**, the `terraform apply` requires manual confirmation in Terraform Cloud by a user with the Production Apply role. This user must be different from the author. For **non-production environments**, the apply proceeds automatically after a successful plan.

6. **Apply Execution:** The apply runs in Terraform Cloud with state locking engaged. The run log is streamed to Splunk (`index=meridian_iac`) for SIEM audit purposes.

7. **Post-Apply Health Check:** Within 5 minutes of apply completion, the engineer must execute the Meridian Post-Deployment Smoke Test suite (`meridian-smoke-tests` GitHub Action workflow) against the modified environment. Test results must be logged in the deployment's JIRA ticket.

### 5.7 Drift Detection and Remediation

Drift between the actual state of cloud resources and the desired state defined in IaC is a critical risk. Drift undermines the IaC source-of-truth principle and can mask security misconfigurations.

#### 5.7.1 Drift Detection Mechanism
Meridian operates a scheduled drift detection pipeline using the `terraform plan -detailed-exitcode` command executed via a nightly GitHub Actions workflow (`drift-detection-nightly.yml`). This workflow iterates over all workspaces in Terraform Cloud, runs a plan, and interprets the exit code:

| **Exit Code** | **Meaning** | **Action** |
|---|---|---|
| 0 | No changes. Infrastructure matches configuration. | No action. |
| 1 | Error during execution. | Alert to #infra-alerts Slack channel. |
| 2 | Changes detected (drift or unapplied configuration). | Alert, log to Splunk, open JIRA ticket. |

#### 5.7.2 Drift Triage
Detected drift follows this triage process:

1. **Initial Assessment:** The Infrastructure Ops on-call engineer examines the plan output to distinguish between **unapplied configuration drift** (a legitimate IaC change was merged but not yet applied—this is normal and should resolve within the next apply cycle) and **rogue resource drift** (a resource was modified outside IaC—this is an incident precursor).

2. **Severity Classification:**

| **Drift Type** | **Severity** | **Response SLA** |
|---|---|---|
| Unapplied configuration (apply pending) | Informational | Resolve within 24 hours |
| Manual console change, non-security-impacting (e.g., tag modification) | Low | Remediate within 5 business days |
| Manual console change, security-impacting (e.g., security group rule, IAM policy) | Medium | Remediate within 24 hours |
| Resource created/deleted outside IaC | High | Remediate within 4 hours; consider SOP-IR-001 incident declaration |

3. **Notification:** Drift incidents are automatically posted to the #infra-drift Slack channel with plan output attached.

#### 5.7.3 Remediation Process
For **Rogue Resource Drift**:

1. Engineer opens a `drift/<run-id>` branch from `main`.
2. Engineer imports the changed resource into the applicable Terraform module using `terraform import`.
3. Engineer runs `terraform plan` and verifies the imported resource matches the desired configuration. If manual adjustments are needed (to revert to known-good configuration), they are made in this branch.
4. Engineer opens a pull request per Section 5.4, noting in the PR description that this is a drift remediation.
5. Upon merge and apply, the drifted state is reconciled.

If drift remediation involves reverting a security group rule to a known-good state, the Security Engineer must co-approve the PR.

### 5.8 Resource Provisioning Thresholds (Blast Radius Controls)

To prevent widespread impact from a misapplied `terraform apply`, Meridian enforces the following deployment gating thresholds:

| **Impact Category** | **Threshold** | **Required Approvals** |
|---|---|---|
| New resource provisioning (any environment) | None | Standard PR review |
| Modification of existing non-production resource | None | Standard PR review |
| Modification of existing production resource, single availability zone | 1 AZ | Senior Infra Engineer |
| Modification of existing production resource, multi-AZ | ≥2 AZs | Senior Infra Engineer + VP of IT Operations |
| Deletion of any production resource | >0 resources | Senior Infra Engineer + VP of IT Operations |
| Modification of AWS Organization-level SCP or IAM | Account-wide | Senior Infra Engineer + Security Engineer |
| Modification of Route53 top-level domain zone | Domain-wide | Senior Infra Engineer + Cloud Architect |

Thresholds are validated programmatically by a Sentinel policy in Terraform Cloud that parses the `terraform plan` JSON output to count impacted resources by environment tag.

### 5.9 Module Registry Management

The Meridian IaC Module Registry (`github.meridian.com/infra/meridian-modules`) is the catalog of reusable, versioned modules.

**Submitting a new module:**
1. Author writes the module following the Meridian Module Template (includes example usage, variable descriptions, output descriptions, and integration tests).
2. Author opens a PR to the Module Registry repository.
3. Automated checks run: `terraform fmt`, `terraform validate`, `terraform-docs` (for README generation).
4. Review required: 1 Senior Infra Engineer + 1 Cloud Architect.
5. Upon merge, a semantic version tag (`git tag v1.2.3`) is applied via GitHub Actions.

**Consuming a module:**
All module references must be pinned to a semantic version tag, not a branch or `HEAD`:

```hcl
module "vpc" {
  source = "git::https://github.meridian.com/infra/meridian-modules.git//terraform/aws/meridian-vpc?ref=v3.1.0"
  # inputs...
}
```

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| **Control ID** | **Control Description** | **Implementation** | **Enforcement Point** |
|---|---|---|---|
| IaC-TC-01 | All IaC must be stored in GitHub Enterprise, no local-only configurations | GitHub Enterprise organization policy; local git hooks validation | Pre-commit hook |
| IaC-TC-02 | Sensitive variables must be marked `sensitive = true` and written to Terraform Cloud as sensitive workspace variables | Terraform Cloud variable configuration | Manual review during workspace setup; checkov scan for variables file |
| IaC-TC-03 | All Terraform operations (`plan`, `apply`, `destroy`) must be executed via Terraform Cloud or the CI/CD pipeline | Terraform Cloud run triggers; IAM policies deny direct Terraform execution from workstations to production accounts | AWS IAM / Azure RBAC |
| IaC-TC-04 | `terraform apply` in production must require two-person approval (one to author/review, one to approve apply) | Terraform Cloud Sentinel policy: `enforce-prod-apply-approval.sentinel` | Apply gate |
| IaC-TC-05 | No manual `terraform destroy` | Terraform Cloud Sentinel policy: `block-destroy-command.sentinel` (except in sandbox) | Plan gate |
| IaC-TC-06 | GitHub protected branches on `main`, `production/*` | GitHub branch protection rules: require PR, require approvals, require status checks, linear history | Merge gate |
| IaC-TC-07 | All secrets retrieved from AWS Secrets Manager / Azure Key Vault at apply time | Terraform `data.aws_secretsmanager_secret_version` / `data.azurerm_key_vault_secret` | Code review |
| IaC-TC-08 | Infrastructure drift detection runs nightly on all production workspaces | GitHub Actions scheduled workflow `drift-detection-nightly.yml` | Scheduled at 02:00 ET daily |

### 6.2 Administrative Controls

| **Control ID** | **Control Description** |
|---|---|
| IaC-AC-01 | All Infrastructure Engineers must complete annual IaC Competency Certification (see Section 9). |
| IaC-AC-02 | Access to the Meridian IaC GitHub repository is based on role-based access control (RBAC) managed via GitHub Teams synced to Okta. |
| IaC-AC-03 | Terraform Cloud membership and team assignment are governed by Okta group membership. |
| IaC-AC-04 | Quarterly IaC governance reviews are conducted by the VP of IT Operations and VP of Engineering to assess adherence to this SOP. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| **KPI ID** | **Metric** | **Target** | **Measurement Method** |
|---|---|---|---|
| IaC-KPI-01 | Mean Time to Deploy (MTTD): Time from PR merge to successful `terraform apply` completion | < 15 minutes for non-production; < 60 minutes for production (allowing for manual approval) | Terraform Cloud run timestamps; Splunk dashboard |
| IaC-KPI-02 | Drift Detection Rate: Number of resources showing unexpected `terraform plan` changes per nightly scan | < 5 resources per production account | Drift detection workflow summary; JIRA tickets |
| IaC-KPI-03 | Drift Remediation Time: Time from drift detection to reconciliation | Severity-based SLA per Section 5.7.2 | JIRA ticket lifecycle |
| IaC-KPI-04 | IaC Code Review Throughput: PRs merged per week | >15 per week aggregate across all IaC repositories | GitHub repository insights |
| IaC-KPI-05 | Failed Apply Rate: Percentage of `terraform apply` runs that result in error | < 2% | Terraform Cloud audit logs |
| IaC-KPI-06 | Module Registry Adoption: Percentage of new resource declarations using approved modules | > 90% | Sentinel policy telemetry |

### 7.2 Dashboards

- **Splunk Dashboard: "IaC Operations Overview"** (`meridian_iac` index): Displays apply run frequency, success/failure rate, average deployment time, drift occurrences. Accessible to all Infrastructure Ops personnel.
- **Grafana Dashboard: "Meridian IaC Pipeline Health"**: Real-time metrics from the GitHub Actions CI/CD pipeline: check run durations, failure categorization, queue depth. Accessible to Platform Engineering and SRE.

### 7.3 Reporting Cadence

| **Report** | **Audience** | **Frequency** | **Contents** |
|---|---|---|---|
| IaC Operations Weekly Digest | Infrastructure Engineers, SREs | Weekly (Monday AM) | Drift incidents, apply failures, module registry updates, upcoming maintenance |
| IaC Compliance Quarterly Report | VP of IT Operations, VP of Engineering, Compliance Officer | Quarterly | Adherence KPIs, exception counts, training completion rates, policy review reminders |
| IaC Incident Postmortem (per SOP-IR-001) | All IaC personnel, CTO | Per incident | Root cause analysis, timeline, remediation actions, IaC policy amendments |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Definition
An exception is any deviation from the policies and procedures defined in this SOP, requested in advance or identified post-hoc. Typical exceptions include:
- Use of a tool not on the approved toolchain list (e.g., AWS CDK for a pilot project).
- Manual console provisioning for a time-critical production fix where the IaC pipeline is unavailable.
- Deployment without full PR review due to incident response.
- Bypassing state locking due to a Terraform Cloud outage.

### 8.2 Exception Request Process

1. **Requestor Opens JIRA Ticket:** Ticket type: "IaC Exception Request". Fields:
   - **Summary:** Brief title (e.g., "Exception: Manual us-east-1 networking fix for INC-12345")
   - **Description:** Detailed explanation, justification, blast radius, timeline.
   - **SOP Section:** Which section of SOP-ITOP-018 is being excepted.
   - **Proposed Duration:** Start and end date/time for the exception window.
   - **Mitigation Plan:** What steps will be taken to minimize risk during the exception.

2. **Initial Approval:** Requestor's immediate manager (for Infrastructure Ops: Senior Infrastructure Engineer; for business unit DevOps: Director of Engineering).

3. **Technical Review:** VP of IT Operations or delegate assesses the blast radius and technical risk.

4. **Security Review:** If the exception involves a production security configuration (firewall rule, IAM policy), a Security Engineer must approve.

5. **Compliance Review:** If the exception impacts a regulated workload (PHI, PCI), the Compliance Officer must approve.

6. **Final Approval:**
   - **Non-Production, low-risk:** VP of IT Operations or delegate.
   - **Production, any risk level:** VP of IT Operations + VP of Engineering.
   - **Regulatory impact:** Above + Compliance Officer.

7. **Exception Logging:** Approved exceptions are logged in the "Meridian IaC Exception Register" (Confluence, administered by the VP of IT Operations' office).

8. **Time-Boxing and Expiration:** All exceptions are time-boxed. Upon expiration, the exception is closed. If the exception must be extended, a new request must be filed, with an explanation for the extension.

### 8.3 Emergency Escalation Path (Incident)

During a declared incident per SOP-IR-001:

1. Incident Commander (IC) verbally briefs VP of IT Operations (or on-call for IT Ops).
2. IC is authorized to bypass standard IaC workflows (manual apply, console changes) for the duration of incident response.
3. All manual changes must be logged in the incident channel (#incident-command) and retroactively codified as follow-up remediation items.
4. Within 24 hours of incident closure, the IC files a retrospective exception record summarizing all IaC policy deviations that occurred during the incident.

---

## 9. Training Requirements

### 9.1 Meridian IaC Competency Certification (MIaC-CC)

All personnel with access to Meridian IaC repositories must hold a current MIaC-CC. This certification is valid for 12 months and requires recertification.

**Certification Curriculum:**
- **Module 1:** IaC Philosophy at Meridian (Declarative paradigm, immutable infrastructure)
- **Module 2:** Terraform Advanced Practices (State management, workspaces, modules, Sentinel policies)
- **Module 3:** Meridian IaC Coding Standards (Naming conventions, tagging, variable/output specification)
- **Module 4:** Code Review and Deployment Workflow (Section 5.4 and 5.6)
- **Module 5:** Drift Detection and Remediation (Section 5.7)
- **Module 6:** Hands-On Lab: Authoring, reviewing, and deploying a non-production change.

**Assessment:** Online written exam (75% pass mark) + practical lab exercise reviewed by a Senior Infrastructure Engineer.

### 9.2 Supplemental Training

- **Ansible Configuration Workshop:** Biannual, 2-day workshop for engineers managing OS-level configuration. Covers Meridian Ansible playbook standards and integration with Packer AMIs.
- **Terraform Cloud Administration:** Annual, 1-day workshop for Senior Infrastructure Engineers covering workspace management, policy-as-code, and run triggers.
- **IaC Security Champions:** Quarterly brown-bag session led by InfoSec, covering recent IaC-related CVEs, misconfiguration patterns, and `checkov` rule updates.

### 9.3 Training Tracking
All IaC training completions are recorded in Workday Learning (LMS). Access to IaC repositories is gated on active certification status. GitHub team membership is automatically reconciled with Workday via the Okta integration. Expired certification triggers a 14-day grace period; if not renewed, GitHub access is automatically revoked.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| **SOP-ID** | **Title** | **Relationship** |
|---|---|---|
| SOP-INFOSEC-001 | Information Security Policy Framework | Parent security policy |
| SOP-INFOSEC-002 | Data Classification and Handling | Governs tagging schema |
| SOP-INFOSEC-007 | Cloud Security Groups and Network Controls | Governs security group IaC patterns |
| SOP-ENG-042 | CI/CD Pipeline Standards | Governs GitHub Actions workflows used for IaC |
| SOP-IR-001 | Incident Response | Governs emergency IaC exceptions |
| SOP-ITOP-022 | Disaster Recovery and Business Continuity | Governs Azure DR IaC configurations |
| SOP-ITOP-025 | Cloud Account Lifecycle Management | Governs AWS/Azure account provisioning and decommissioning |
| SOP-QA-005 | Infrastructure Testing Standards | Governs smoke test and integration test suites |

### 10.2 External Standards and Frameworks

| **Reference** | **Title** | **Applicability** |
|---|---|---|
| HashiCorp | Terraform Recommended Practices | Provider versioning, state file structure |
| AWS | AWS Well-Architected Framework - Operational Excellence Pillar | IaC as fundamental to operational excellence |
| CIS Benchmarks | CIS AWS Foundations Benchmark | Security group, IAM, logging IaC patterns |
| Gruntwork | Infrastructure Cookbook | Terragrunt patterns and module design |

### 10.3 Internal Resources

- **Meridian IaC Module Registry:** `github.meridian.com/infra/meridian-modules`
- **Meridian IaC Monorepo:** `github.meridian.com/infra/meridian-iac`
- **IaC Operations Runbooks:** Confluence Space "ITOps Runbooks"
- **IaC Exception Register:** Confluence "IaC Exception Register"
- **Terraform Cloud Organization:** `app.terraform.io/meridian`
- **Splunk Index:** `meridian_iac`
- **Slack Channels:** `#infra-alerts` (monitoring), `#infra-drift` (drift notifications), `#infra-iac-changes` (automated changelog)

---

## 11. Revision History

| **Version** | **Effective Date** | **Author** | **Description of Changes** |
|---|---|---|---|
| 1.0 | 2019-06-10 | M. Chen, Infrastructure Architect | Initial release. Established Terraform as the IaC standard, defined initial monorepo structure. |
| 2.3 | 2020-11-15 | J. Ramirez, Senior Infrastructure Engineer | Introduced Terragrunt for DRY configurations. Added mandatory tagging requirements. Formalized code review PR template. |
| 3.1 | 2021-08-22 | A. Patel, Cloud Architect | Migrated from Jenkins CI to GitHub Actions. Added drift detection nightly workflow. Introduced Packer for AMI generation. |
| 4.0 | 2023-04-03 | S. Torres, VP of IT Operations | Major revision: Introduced RACI matrix, formal exception handling process, blast radius controls, module registry standards. Aligned with new business unit structure (Clinical AI, HealthPay, MedInsight). Added Azure support for DR. |
| 4.5 | 2023-09-20 | K. Nguyen, Senior Infrastructure Engineer | Updated Terraform version floor to 1.6.x. Added Sentinel policy enforcement details. Refined drift severity classification and remediation SLAs. |
| 4.6 | 2023-12-05 | L. Schmidt, DevOps Engineer (HealthPay) | Minor revision: Added PCI-compliant tagging examples for HealthPay cardholder data environment resources. Updated branch naming examples. |
| 4.7 | 2024-02-17 | S. Torres, VP of IT Operations | Annual review. Updated training curriculum. Added KPI for module registry adoption. Updated Infracost integration details. Clarified state locking enforcement and stale lock resolution. No structural changes. |