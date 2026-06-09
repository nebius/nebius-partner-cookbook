---
sop_id: "SOP-PENG-011"
title: "CI/CD Pipeline Security"
business_unit: "Product & Engineering"
version: "3.8"
effective_date: "2025-04-17"
last_reviewed: "2026-07-18"
next_review: "2027-01-28"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: CI/CD Pipeline Security

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory security requirements, controls, and operational procedures governing the Continuous Integration and Continuous Deployment (CI/CD) pipelines at Meridian Health Technologies, Inc. The purpose of this document is to ensure that all software artifacts deployed across the Meridian SaaS Platform, Clinical AI Platform, HealthPay Financial Services, and MedInsight Analytics are built, tested, and released through secure, auditable, and tamper-evident pipelines that preserve the confidentiality, integrity, and availability of the systems and the protected data they process.

This SOP defines the minimum security baseline for all pipeline stages—from source code commit through production deployment—and implements controls required under the SOC 2 Type II Trust Services Criteria, specifically within the Security and Availability categories. It operationalizes the principles of the NIST AI Risk Management Framework as applied to the software supply chain for high-risk AI systems.

### 1.2 Scope

This SOP applies to:

- **All Meridian Engineering Teams** developing, maintaining, or operating software deployed to production, staging, or any environment containing non-public data.
- **All CI/CD Pipelines** managed through GitHub Actions, Jenkins, AWS CodePipeline, and ArgoCD, including pipelines that produce container images, machine learning model artifacts, infrastructure-as-code templates, and mobile application binaries.
- **All Artifact Repositories** including AWS Elastic Container Registry (ECR), PyPI mirror (Artifactory), and Meridian's internal Helm chart repository.
- **All Infrastructure-as-Code (IaC)** provisioning paths managed through Terraform Cloud and AWS CloudFormation.
- **Third-Party Integrations** that receive, process, or deploy Meridian-built code or artifacts.
- **Model Deployment Pipelines** for Clinical AI Platform components classified as high-risk AI systems under the EU AI Act, including those subject to FDA 510(k) or CE-marked releases.

This SOP does **not** apply to:

- Legacy on-premises systems decommissioned by memorandum SOP-ITOP-045.
- Research and development sandbox environments with no connectivity to production data stores (governed separately under SOP-PENG-022).
- Desktop productivity software managed by IT Operations.

### 1.3 Target Audience

All Engineering, DevOps, MLOps, Security Engineering, and Quality Assurance personnel. Additionally, this SOP is binding on Product Managers approving production releases and Compliance personnel conducting pipeline audits.

---

## 2. Definitions and Acronyms

| Term | Definition |
|---|---|
| **Artifact** | Any build output intended for deployment, including container images, compiled binaries, Python wheels, ML model serialization files, Helm charts, and Terraform plans. |
| **Artifact Signing** | Cryptographic signing of an artifact using a Meridian-managed private key such that its integrity and provenance can be verified at deployment time. |
| **Attestation** | A cryptographically signed statement about an artifact, such as an in-toto attestation documenting the build process, materials, and compliance checks. |
| **CI/CD Pipeline** | The automated sequence of stages that takes source code from version control to a deployable artifact and optionally through to production release. |
| **Deployment Approval** | A formal, auditable authorization step required prior to advancing an artifact to a production environment, recorded in the pipeline execution log and ServiceNow change management. |
| **Hardened Runner** | A CI/CD execution environment (e.g., GitHub Actions runner, Jenkins agent) that has been configured to a defined security baseline including read-only filesystems, no outbound internet access except to approved endpoints, and ephemeral lifecycles. |
| **Immutable Artifact** | An artifact that, once built and signed, is never modified. Any configuration changes result in a new artifact with a new unique version identifier. |
| **Pipeline Integrity** | The property that all stages of the pipeline execute as defined, without unauthorized modification, and produce verifiable outputs. |
| **Provenance** | Metadata describing the origin, build process, and chain of custody of an artifact, sufficient to reconstruct the exact inputs and environment that produced it. |
| **Secret** | Any credential, token, key, password, or certificate used to authenticate to internal or external systems. |
| **SLSA** | Supply-chain Levels for Software Artifacts. A framework adopted by Meridian for measuring and improving supply chain integrity. |
| **Software Bill of Materials (SBOM)** | A machine-readable inventory of all components, libraries, and dependencies included in an artifact. |

| Acronym | Full Name |
|---|---|
| **CD** | Continuous Deployment |
| **CI** | Continuous Integration |
| **DAST** | Dynamic Application Security Testing |
| **IaC** | Infrastructure-as-Code |
| **OWASP** | Open Web Application Security Project |
| **SAST** | Static Application Security Testing |
| **SCA** | Software Composition Analysis |
| **SCM** | Source Code Management |
| **SLSA** | Supply-chain Levels for Software Artifacts |
| **SBOM** | Software Bill of Materials |
| **VCS** | Version Control System |

---

## 3. Roles and Responsibilities

The following responsibility assignment matrix governs all activities described in this SOP. Responsibilities are defined as:

- **R** (Responsible): The party who performs the work.
- **A** (Accountable): The party ultimately answerable for the correct and thorough completion of the task. Only one "A" per task.
- **C** (Consulted): The party whose input is sought, typically through two-way communication.
- **I** (Informed): The party kept up-to-date on progress, typically through one-way reporting.

| Activity / Responsibility | VP of Engineering | DevOps Lead | Security Engineering | Engineering Team Lead | Software Engineer | Compliance Officer | Product Manager |
|---|---|---|---|---|---|---|---|
| Overall SOP governance and enforcement | A | R | C | I | I | I | I |
| Pipeline infrastructure provisioning | I | A / R | C | I | I | I | I |
| Hardened runner configurations | I | R | A / R | I | I | I | I |
| Secret management and rotation | I | R | A | C | I | I | I |
| SAST / SCA tool integration | I | R | A | R | C | I | I |
| Container image signing | I | A | R | I | R | I | I |
| SBOM generation and validation | I | R | A | R | C | I | I |
| Deployment approval for production | C | R | C | R | I | I | A |
| Emergency break-glass process | I | A | C | R | I | I | C |
| Audit log review and retention | I | R | A | I | I | R | I |
| Vulnerability remediation SLAs | A | R | C | R | R | I | I |
| Pipeline compliance evidence collection | I | R | I | I | I | A | I |

### 3.1 Named Role Assignments

| Role | Default Assignee |
|---|---|
| **VP of Engineering** | David Park |
| **DevOps Lead** | Maria Okonkwo |
| **Security Engineering Lead** | Rajesh Thakur |
| **Compliance Officer** | Allison Vance |
| **Clinical AI Platform Lead** | Dr. Wei Zhang |

---

## 4. Policy Statements

### 4.1 Pipeline Integrity Policy

All CI/CD pipelines must operate on a principle of zero trust: no pipeline stage shall trust inputs from a prior stage without cryptographic verification. Every production artifact must have verifiable provenance linking it back to a specific, approved source commit, a known build environment, and a successful set of compliance checks. Meridian mandates SLSA Level 3 compliance for all production artifact pipelines effective Q2 2025.

### 4.2 Secret Management Policy

Secrets must never be stored in plaintext in source code, configuration files, build scripts, Dockerfiles, pipeline definition files, or log output. All secrets shall be stored in HashiCorp Vault with access granted exclusively to defined pipeline identities through short-lived, auto-rotated credentials. Long-lived static credentials are prohibited for production pipeline access.

### 4.3 Artifact Signing Policy

Every artifact promoted to a production environment must be cryptographically signed using a Meridian-managed code-signing key stored in AWS Key Management Service (KMS). The signature must cover the complete artifact digest and associated provenance metadata. Unsigned artifacts are rejected at deployment by the admission controller.

### 4.4 Deployment Approval Policy

No artifact may be deployed to a production environment without an approved change request in ServiceNow, linked to the specific artifact version, and approved by the designated Product Manager and Engineering Team Lead. This approval must be validated programmatically by the deployment pipeline before execution.

### 4.5 Pipeline Isolation Policy

Pipelines handling code for separately regulated workloads (e.g., Clinical AI Platform vs. HealthPay) must execute on logically isolated runner pools with distinct IAM roles, VPC subnets, and logging streams. Shared runners are prohibited for such multi-tenant scenarios.

### 4.6 Dependency Management Policy

All third-party and open-source dependencies must be continuously monitored for known vulnerabilities through SCA tooling integrated into the CI pipeline. Builds introducing dependencies with Critical or High severity vulnerabilities as defined by CVSS v3.1 score ≥ 7.0 shall be blocked from deployment unless a formal exception is approved under Section 8.

---

## 5. Detailed Procedures

### 5.1 Pipeline Configuration and Hardening

#### 5.1.1 CI/CD Toolchain Architecture

Meridian operates a unified CI/CD architecture composed of the following components:

1. **Source Control**: GitHub Enterprise Cloud (primary SCM), with branch protection rules enforced on all production-intended repositories.
2. **CI Orchestration**: GitHub Actions for standard application pipelines; Jenkins (self-hosted, hardened) for regulated Clinical AI Platform pipelines requiring isolated execution environments.
3. **Artifact Registry**: AWS Elastic Container Registry (ECR) for container images; JFrog Artifactory for language-specific packages and Helm charts.
4. **CD Orchestration**: ArgoCD (deployed within each Kubernetes cluster) for GitOps-based deployment; AWS CodePipeline for serverless and infrastructure deployment workflows.
5. **Secrets Backend**: HashiCorp Vault (Enterprise, HA mode, deployed in dedicated management VPC).
6. **Code Signing**: AWS KMS asymmetric keys (RSA 4096-bit) dedicated to artifact signing, with key policies restricting usage to specific pipeline IAM roles.

#### 5.1.2 GitHub Branch Protection Standards

Every production-intended repository must have the following branch protection rules applied to the `main` (or `master`) branch:

| Protection Rule | Configuration | Mandatory |
|---|---|---|
| Require pull request reviews before merging | Minimum 1 approval from CODEOWNERS | Yes |
| Dismiss stale pull request approvals when new commits are pushed | Enabled | Yes |
| Require status checks to pass before merging | See required checks list below | Yes |
| Require conversation resolution before merging | Enabled | Yes |
| Require signed commits | Enabled (GPG or S/MIME) | Yes |
| Require linear history | Enabled | Yes |
| Do not allow bypassing the above settings | Applied to administrators | Yes |
| Restrict pushes to specific actors | `main` branch push restricted to `devops-admins` team only | Yes |

**Required Status Checks** (must all pass before merge):

1. `SAST-scan` (SonarQube Enterprise Edition)
2. `SCA-scan` (Snyk with Meridian policy ruleset)
3. `container-build-and-sign` (custom Meridian action)
4. `unit-tests` (language-specific framework)
5. `integration-tests` (environment-specific)
6. `sbom-generate` (Syft/Grype integration)
7. `secret-scan` (TruffleHog or GitGuardian)
8. `license-compliance` (FOSSA)

#### 5.1.3 Hardened Runner Configuration

All self-hosted runners (Jenkins agents, GitHub Actions self-hosted runners) must be deployed using the Meridian Hardened Runner Baseline defined in this section.

**Infrastructure Requirements:**

```
Runner Configuration Baseline:
├── Compute: EC2 c5.xlarge (or equivalent) with Nitro Enclave for attested execution
├── AMI: meridian-hardened-runner-ami-2025-q2 (build SOP-PENG-011a)
├── Disk: EBS root volume, encrypted with KMS CMK, delete on termination
├── Lifecycle: Ephemeral; destroyed after each pipeline execution
├── Networking: Private subnet, no public IP, egress via VPC endpoints only
├── IAM Role: Runner-specific, least-privilege policy
└── Logging: CloudWatch Agent shipping to dedicated log group
```

**Hardening Controls Applied at Provisioning:**

1. **Read-only root filesystem**: The runner's root volume is mounted read-only; writable directories (`/tmp`, `/var/lib/docker`, `/home/runner`) are backed by ephemeral instance store volumes formatted at launch.
2. **No outbound internet**: All outbound traffic restricted via security group rules to VPC endpoints for AWS services, GitHub Enterprise API endpoints, and approved package registries (Artifactory proxy). Direct public internet access is blocked.
3. **Container runtime security**: Docker daemon configured with `userns-remap`, `no-new-privileges=true`, AppArmor profiles enabled, and `--icc=false` to disable inter-container communication.
4. **Seccomp profile**: Custom seccomp profile applied, blocking unprivileged `clone`, `mount`, `ptrace` syscalls.
5. **Runtime monitoring**: Falco daemon running in detection mode, alerting Security Engineering on suspicious syscalls.

**Runner Lifecycle:**

```
Provisioning:
  1. Scaling event triggers (GitHub webhook or Jenkins job queue depth threshold)
  2. EC2 instance launched from hardened AMI
  3. User-data script registers runner with orchestrator
  4. Runner marked "online" in orchestrator pool

Execution:
  5. Pipeline job assigned to runner
  6. Runner clones repository, executes pipeline stages
  7. All output logged to centralized CloudWatch log group
  8. Artifacts pushed to registry (runner identity authenticated via Vault-issued token)

Destruction:
  9. Runner reports completion to orchestrator
  10. Orchestrator initiates runner deregistration
  11. EC2 instance terminated (termination protection disabled at launch)
  12. CloudWatch log stream preserved for 365-day retention
```

#### 5.1.4 Pipeline Definition Security

**CI/CD Configuration Files:**

- All pipeline definition files (`.github/workflows/*.yml`, `Jenkinsfile`, `argo-rollouts/*.yaml`) must be stored within the repository they govern and are subject to the same branch protection and code review requirements as application code.
- Pipeline definition changes must be reviewed by a member of the DevOps team in addition to the standard CODEOWNERS review.
- Inline scripts in pipeline definitions are prohibited. All scripts must reside in a `scripts/` or `ci/` directory with explicit review history.

**Self-Hosted Jenkins Security:**

- Jenkins authentication integrated with Okta SSO, enforcing MFA for all human users.
- Project-based matrix authorization enabled; `Job/Configure` permission restricted to `devops-admins` group.
- Script Console access disabled for all users except the root emergency account (stored in Vault, break-glass only).
- All Jenkins plugins pinned to known-good versions with SHA-256 checksums verified at installation.

### 5.2 Secret Management Procedures

#### 5.2.1 Secret Storage Hierarchy

All production secrets are classified into tiers and stored accordingly:

| Secret Tier | Examples | Storage Location | Access Method | Max TTL |
|---|---|---|---|---|
| **Tier 0** | Root CA keys, Vault unseal keys | FIPS 140-2 Level 3 HSM | Physical access, quorum | Indefinite (rotation every 90d) |
| **Tier 1** | AWS root credentials, Code-signing keys | AWS KMS + Vault transit | Pipeline IAM roles only | 24 hours |
| **Tier 2** | Database passwords, API keys | Vault KV v2 (versioned) | Vault agent injection | 7 days (auto-rotated) |
| **Tier 3** | Deploy tokens, registry credentials | Vault KV v2 | Pipeline secret references | 24 hours (ephemeral) |

#### 5.2.2 Pipeline-to-Vault Authentication

Pipelines authenticate to Vault using the following chain:

1. **Runner identity**: Each pipeline execution receives an AWS IAM role credential via EC2 instance metadata (IMDSv2 enforced, hop limit = 1).
2. **Vault AWS auth method**: IAM role bound to Vault roles with specific policies attached. The Vault role definition requires the IAM role ARN be present in the `bound_iam_principal_arn` parameter.
3. **Secret retrieval**: Pipeline stages request specific secrets by Vault path using the `vault-agent` sidecar (Kubernetes contexts) or `vault` CLI (Jenkins/GitHub Actions non-Kubernetes contexts). Secrets are written to a tmpfs mount that is destroyed on pipeline completion.

**Example Vault Policy for Pipeline Role (HealthPay-API-Build):**

```hcl
path "secret/data/healthpay/production/database" {
  capabilities = ["read"]
}
path "secret/data/shared/registry/ecr" {
  capabilities = ["read"]
}
path "auth/token/renew-self" {
  capabilities = ["update"]
}
```

#### 5.2.3 Secret Scanning in Pipelines

All pipelines must execute a secret scanning stage as the **first step after checkout**. The secret scanning stage:

1. Runs `trufflehog` (open-source) against the complete git history of the checked-out commit and any uncommitted changes.
2. Runs `git-secrets` against AWS-specific credential patterns.
3. Scans all files in the workspace for patterns matching Meridian's custom secret format regex.
4. **Blocks the pipeline on any positive detection**, logging an event to the Security Incident Response channel (#security-incidents in Slack) and generating a SecOps ticket.
5. If a valid secret is detected, the compromised secret is immediately rotated by the Secret Rotation automation (see SOP-SEC-003), and the commit author's credentials are revoked pending incident investigation.

#### 5.2.4 Secret Rotation Schedule

| Secret Category | Rotation Interval | Automation Status |
|---|---|---|
| Database credentials (Tier 2) | 7 days | Fully automated via Vault dynamic secrets |
| API keys for internal services | 30 days | Automated rotation, manual propagation window |
| AWS IAM access keys for service accounts | 90 days | Automated via Vault AWS secrets engine |
| Code-signing keys (Tier 1) | 180 days | Semi-automated; manual verification step required |
| TLS certificates for internal endpoints | 90 days | Automated via cert-manager and Let's Encrypt (internal CA) |

### 5.3 Artifact Integrity and Signing

#### 5.3.1 Container Image Build and Signing Procedure

**Step 1: Deterministic Build**

All production container images must be built using the Meridian standard `Dockerfile.build` template, which enforces:

- Base images pinned by SHA-256 digest (e.g., `FROM python:3.11-slim@sha256:a1b2c3...`)
- `--no-cache` flag set
- Build timestamp set to SOURCE_DATE_EPOCH for reproducibility
- Build executed within hardened runner environment

**Step 2: SBOM Generation**

Simultaneously with the image build, an SBOM is generated using Syft with the following configuration:

```
syft packages <image-name> \
  --output spdx-json \
  --file sbom-<image-tag>.spdx.json
```

**Step 3: Vulnerability Scan**

The generated SBOM is scanned with Grype against the Meridian vulnerability policy:

- Maximum allowable Critical vulnerabilities: 0
- Maximum allowable High vulnerabilities (CVSS ≥ 7.0): 0
- Maximum allowable Medium vulnerabilities (CVSS 4.0-6.9): 5 (requires documented remediation plan in Jira)

Images failing vulnerability thresholds are not signed and cannot be promoted.

**Step 4: Image Signing with Cosign**

The validated image is signed using Cosign with the Meridian code-signing key:

```bash
cosign sign \
  --key awskms:///arn:aws:kms:us-east-1:123456789012:key/mrk-abc123 \
  --tlog-upload=true \
  --annotations "meridian.sop=SOP-PENG-011" \
  --annotations "meridian.team=${TEAM}" \
  --annotations "meridian.git-commit=${GITHUB_SHA}" \
  ${ECR_REGISTRY}/${REPOSITORY}:${IMAGE_TAG}
```

**Step 5: In-Toto Attestation Generation**

A build attestation is generated using in-toto layout:

```json
{
  "subject": [
    {
      "name": "healthpay-api",
      "digest": {
        "sha256": "abc123..."
      }
    }
  ],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "builder": {
      "id": "https://github.com/Meridian-HealthTech/hardened-runner@v2.1"
    },
    "buildType": "https://meridian.dev/deployments/github-actions@v1",
    "materials": [
      {
        "uri": "git+https://github.com/Meridian-HealthTech/healthpay-api.git",
        "digest": {
          "sha1": "def456..."
        }
      }
    ]
  }
}
```

This attestation is stored in the Rekor transparency log and linked to the artifact in Artifactory.

**Step 6: Registry Push and Retention**

The signed image and its `cosign.sig` and `cosign.att` tags are pushed to ECR. ECR tag immutability is enforced. Images are retained per the following schedule:

| Environment | Retention Policy |
|---|---|
| Production | Indefinite (all versions) |
| Staging | Last 90 days (rolling) |
| Development / Feature branches | Last 7 days |

#### 5.3.2 Artifact Verification at Deployment

ArgoCD (or equivalent deployment controller) is configured with an admission webhook that:

1. Validates the `cosign` signature against the Meridian trust root before scheduling any pod.
2. Checks that the Rekor entry exists and contains the expected builder identity.
3. Verifies the in-toto attestation chain of custody.
4. Rejects deployment if verification fails, logging a CRITICAL event to Splunk.

**Admission Controller Policy (OPA/Rego snippet):**

```rego
deny[msg] {
  input.request.operation == "CREATE"
  artifact := input.request.object.spec.containers[_].image
  not verified_by_cosign(artifact, trusted_key)
  msg := sprintf("unsigned image rejected: %s", [artifact])
}
```

### 5.4 Deployment Approval and Release Management

#### 5.4.1 Standard Release Path

The path to production deployment consists of the following gates, each enforced programmatically in the pipeline:

| Gate | Stage | Action | Evidence Required |
|---|---|---|---|
| **G1** | Merge to `main` | All status checks pass | CI pipeline completion log with all 8 checks green |
| **G2** | Build and Sign | Artifact produced and signed | Cosign signature verification, SBOM attestation uploaded |
| **G3** | Staging Deployment | Deploy to staging, automated smoke tests | All staging integration tests pass; DAST scan clean |
| **G4** | Change Approval | ServiceNow CHG record approved | CHG-XXXXXXXXX record linked in deployment metadata |
| **G5** | Approval Gate | Product Manager + Engineering Lead approve promotion | Digital approval recorded in pipeline, timestamped |
| **G6** | Production Deployment | Rolling deployment, canary 5% → 100% | Prometheus metrics within SLO; no Sev1/PagerDuty alerts triggered |

**Gate G5 Details:**

The deployment approval is a manual pipeline gate configured in ArgoCD Rollouts (`argo-rollouts` Notification controller). Approval is requested via:

1. **ServiceNow Change Record** created automatically by the pipeline upon staging deployment success.
2. **Microsoft Teams Adaptive Card** sent to the `Change-Approval-Board` channel, requesting approval from two authorized approvers.
3. Approvals are digitally signed with the approver's Okta identity and recorded in the pipeline execution history, the Rekor transparency log, and ServiceNow.

**Authorized Approver Pool (per Business Unit):**

| Business Unit | Approver Pool |
|---|---|
| HealthPay Financial Services | David Park + Director of Risk |
| Clinical AI Platform | Dr. Wei Zhang + Director of Clinical Compliance |
| MedInsight Analytics | Maria Okonkwo + Director of Data Platform |
| Meridian SaaS Platform (shared) | David Park + Rajesh Thakur |
| Mobile Applications | Mobile Engineering Lead + Director of Product |

#### 5.4.2 Canary Deployment Procedure

All production deployments use a graduated canary release strategy defined as ArgoCD Rollout objects:

**Stage 1: Canary (5%) — Duration: 5 minutes**
- Deploy new image version to 5% of pods.
- Monitor: 5xx error rate, p99 latency, CPU/Memory usage, crash-loop events.
- If any metric exceeds defined SLO, automatic rollback to stable version.

**Stage 2: Canary (25%) — Duration: 10 minutes**
- Expand to 25% of pods.
- Monitor: All previous metrics plus business-specific KPIs (e.g., payment transaction success rate for HealthPay).
- Manual approval prompt sent to Release Manager if proceeding.

**Stage 3: Canary (100%) — Duration: Gradual over 15 minutes**
- Progressive rollout to full fleet.

**Rollback Trigger:**
If ANY of the following conditions are met, ArgoCD Rollouts automatically rolls back:
- `5xx` error rate > 1% of traffic
- `p99` latency > 200% of baseline (measured over 24h rolling window)
- Any PagerDuty alert triggers with severity ≤ Sev2
- Manual rollback command issued by any member of the `devops-admins` group

**Rollback Artifact:**
Rollback deploys the immediate prior version (artifact digests tracked in deployment history). No new build is triggered.

### 5.5 Software Supply Chain Integrity (SLSA Compliance)

Meridian's SLSA compliance implementation covers four levels. This SOP codifies SLSA Level 3 across all production pipelines.

**SLSA Level 3 Controls Mapped to SOP Procedures:**

| SLSA Requirement | SOP Procedure Mapping |
|---|---|
| **Source**: Version controlled, verified history | Section 5.1.2, Branch Protection |
| **Source**: Two-person review | CODEOWNERS review requirement (G1) |
| **Build**: Scripted build process | Pipeline definition in repository (Section 5.1.4) |
| **Build**: Build as code | GitHub Actions YAML / Jenkinsfile reviewed |
| **Build**: Ephemeral environments | Hardened runner lifecycle, ephemeral instances (Section 5.1.3) |
| **Build**: Isolated builds | Isolated runner pools for multi-tenant (Section 4.5) |
| **Provenance**: Non-falsifiable attestation | In-toto attestation, Rekor transparency log (Section 5.3.1) |
| **Provenance**: Build service authenticated | Runner identity via IAM → Vault → Signing Key (Section 5.2.2) |
| **Provenance**: Complete and auditable | All attestations stored in Rekor, indexed by artifact digest |
| **Common**: Cryptographic verification | Admission controller verification (Section 5.3.2) |

### 5.6 Pipeline Audit Logging and Forensics

#### 5.6.1 Audit Log Sources

All pipeline events are captured across the following log streams:

| Source | Data Captured | Retention | Query Interface |
|---|---|---|---|
| GitHub Audit Log (Org-level) | Repository events, branch protection changes, admin actions | 3 years | Splunk index `github_audit` |
| Jenkins Job History | Job execution, parameter changes, approval events | 365 days | Jenkins REST API → Splunk `jenkins_jobs` |
| ArgoCD API Server | Deployment requests, sync status, rollback events | 90 days in-cluster; 3 years in Splunk | Splunk `argocd_prod` |
| Cosign Attestations (Rekor) | Signature events, TLOG entries | Indefinite (public ledger) | Rekor API |
| AWS CloudTrail | IAM role assumption, KMS usage, ECR push/pull | 3 years | Splunk `cloudtrail_all` |
| Vault Audit Logs | Secret access, token creation, policy changes | 3 years | Vault syslog → Splunk `vault_prod` |
| Hardened Runner CloudWatch | Pipeline execution logs, security events (Falco) | 365 days | CloudWatch Insights |

#### 5.6.2 Pipeline Forensics Query Templates

Security Engineering has published the following Splunk query templates for incident investigation:

**Query 1: Trace an artifact from production back to source commit**
```splunk
index=argocd_prod AND "image="<artifact_digest>
| join type=inner [ search index=vault_prod "cosign_sign" ]
| join type=inner [ search index=jenkins_jobs build_number ]
| join type=inner [ search index=github_audit repo=<repo_name> commit=<sha> ]
| table _time, repo, commit_author, reviewer, build_id, cosign_attestation, deploy_timestamp
```

**Query 2: Identify all deployments by an individual**
```splunk
( index=jenkins_jobs OR index=argocd_prod OR index=github_audit )
| where triggered_by="<username>" OR approved_by="<username>" OR commit_author="<username>"
| stats count by source, repository, artifact_version, environment, _time
```

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | SOC 2 TSC Mapping | Implementation Evidence |
|---|---|---|---|
| **PENG-011-AC01** | Formal CI/CD security policy is documented, approved, and reviewed annually | CC1.1, CC1.2 | This SOP, version-controlled with approval record |
| **PENG-011-AC02** | Pipeline access is granted based on role, reviewed quarterly | CC1.3, CC1.4 | Quarterly access review reports (ServiceNow), deviation logged in SecOps Jira |
| **PENG-011-AC03** | Security responsibilities for pipeline management are formally defined | CC1.5 | RACI matrix (Section 3) |
| **PENG-011-AC04** | Background checks required for personnel with administrative pipeline access | CC2.1 | HR compliance report, verified semi-annually |
| **PENG-011-AC05** | Pipeline security risks are assessed in the enterprise risk registry | CC3.1 | GRC tool (Archer) entry "CI/CD Pipeline Compromise," risk owner: VP Engineering |
| **PENG-011-AC06** | Annual third-party penetration test includes CI/CD pipeline attack surface | CC3.2 | Penetration test scope document, findings tracked to remediation |
| **PENG-011-AC07** | Segregation of duties enforced: developer cannot approve their own production deployment | CC5.1 | Programmatic enforcement in ServiceNow approval workflow |
| **PENG-011-AC08** | Code-signing keys managed under dual control | CC5.2 | KMS key policy requires two distinct IAM principals for key material access |

### 6.2 Technical Controls

| Control ID | Control Description | SOC 2 TSC Mapping | Technology Stack |
|---|---|---|---|
| **PENG-011-TC01** | All code changes require a pull request with at least one approval from a different individual | CC6.1, CC7.1 | GitHub branch protection rules |
| **PENG-011-TC02** | SAST scanning runs on every commit; Critical/High findings block merge | CC7.1 | SonarQube Quality Gate `meridian-standard` |
| **PENG-011-TC03** | SCA scanning scans all dependencies; Critical/High CVEs block build | CC7.1 | Snyk CLI with `--severity-threshold=high` and meridian policy |
| **PENG-011-TC04** | Secrets detection scan runs on every pipeline execution | CC6.1, CC6.6 | TruffleHog + GitGuardian integrated |
| **PENG-011-TC05** | Build environments are ephemeral and hardened | CC6.1, CC7.2 | Custom AMI, seccomp profile (Section 5.1.3) |
| **PENG-011-TC06** | Production artifacts are cryptographically signed | CC6.1, CC7.1 | Cosign + AWS KMS (RSA-4096) |
| **PENG-011-TC07** | Signed artifacts are verified at deployment admission | CC6.1, CC7.1 | OPA Gatekeeper + Cosign verification webhook |
| **PENG-011-TC08** | Deployment approval is programmatically enforced | CC5.1, CC6.1 | ArgoCD Rollouts + ServiceNow Integration |
| **PENG-011-TC09** | Network egress from CI runners is restricted to approved endpoints | CC6.1, CC6.6 | Security groups + VPC endpoints; no public internet |
| **PENG-011-TC10** | SBOM generated, stored, and continuously monitored for all production artifacts | CC7.1 | Syft (SBOM) + Grype (vuln scan) + Dependency-Track (monitoring) |
| **PENG-011-TC11** | Pipeline audit logs centralized and retained for ≥ 3 years | CC4.1, CC7.2 | Splunk index retention policy (Section 5.6.1) |
| **PENG-011-TC12** | Log integrity safeguarded with append-only Splunk indexes and tamper-evident HEC tokens | CC7.2 | Splunk Indexer Clustering with data integrity verification |

### 6.3 SOC 2 Trust Services Criteria Mapping Summary

This SOP directly implements controls addressing the following SOC 2 TSC 2017 criteria within the **Security** and **Availability** categories:

| TSC Criteria | Description | SOP Reference |
|---|---|---|
| **CC1.1** | The entity has defined organizational structures, reporting lines, and authority. | Section 3 (Roles), Section 5.4 (Approval authority) |
| **CC1.2** | Responsibility for internal control is assigned. | RACI Matrix, Gate G5 approver list |
| **CC1.3** | Segregation of duties exists. | Code review vs. deployment approval; dual control for keys |
| **CC2.1** | Background checks performed. | AC04 |
| **CC3.1** | Risk assessment for supply chain. | AC05, Section 5.5 (SLSA compliance) |
| **CC3.2** | External penetration testing scope. | AC06 |
| **CC4.1** | Monitoring of pipeline security events. | Section 7, AC07 |
| **CC5.1** | Access restriction and management. | Secret management (Section 5.2), IAM roles |
| **CC5.2** | Dual control for sensitive operations. | AC08, Vault unseal, KMS key operations |
| **CC6.1** | Logical access security measures. | Branch protection, Pipeline isolation, Secret scanning, SBOM |
| **CC6.6** | External network access restrictions. | Hardened runner networking (Section 5.1.3) |
| **CC7.1** | Vulnerability detection and monitoring. | SAST/SCA scanning, Grype vuln scanning, Metrics (Section 7) |
| **CC7.2** | Monitoring and logging integrity. | Audit logs (Section 5.6), Splunk integrity (TC12) |

### 6.4 Physical and Environmental Controls (Pipeline Infrastructure)

All self-hosted CI/CD infrastructure resides within AWS US-East-1 and EU-West-2 regions within Meridian's SOC 2 in-scope VPCs. Physical security of data centers is the responsibility of AWS (covered under AWS SOC 2 report, reviewed annually by Meridian Compliance). Meridian-controlled hardware (HSMs for root CA) resides in Equinix DC6, access-controlled per SOP-SEC-009.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following KPIs are tracked monthly and presented in the Engineering Security Scorecard, distributed to the CTO, VP of Engineering, CISO, and Compliance Officer.

| KPI ID | Metric Name | Target | Measurement Method |
|---|---|---|---|
| **KPI-011-01** | Pipeline Security Scan Pass Rate | ≥ 95% of pipeline runs pass all security scans (SAST, SCA, secrets) on first attempt | Average across all repos, last 30 days (SonarQube aggregate + Snyk reporting API) |
| **KPI-011-02** | Mean Time to Remediate Critical Vulnerability | ≤ 48 hours from detection to verified fix | Jira ticket lifecycle; time from Snyk scan alert creation to PR merge with fix |
| **KPI-011-03** | Unsigned Production Artifact Rate | 0% (zero-tolerance) | ArgoCD audit log count of rejected deployments due to missing/invalid signature |
| **KPI-011-04** | Secret Leakage Detection Rate | 100% of secrets committed to VCS detected by pipeline within 1 minute of push | TruffleHog detection timestamp − commit timestamp |
| **KPI-011-05** | Pipeline Runner Hardening Compliance | 100% of runners match hardened baseline | AWS Config rule `meridian-hardened-runner` evaluating EC2 compliance |
| **KPI-011-06** | Mean Time to Production (MTP) | ≤ 4 hours (measured from merge to `main` to successful canary 100%) | Pipeline execution duration, excluding manual approval wait time |
| **KPI-011-07** | Deployment Failure (Rollback) Rate | ≤ 5% of production deployments trigger automatic rollback | ArgoCD Rollout `status.failedCanary` count / total promotion attempts |

### 7.2 Dashboard Configuration (Splunk Enterprise)

The **"CI/CD Security Posture Dashboard"** (Splunk Dashboard ID: `meridian-cicd-sec-v3`) displays the following panels:

**Panel 1: Real-Time Pipeline Execution Status**
- Table: Repository name, branch, commit SHA, pipeline stage, status (Success/Failure/InProgress), security scan results.
- Data Sources: `index=jenkins_jobs OR index=github_audit`
- Refresh: 1 minute

**Panel 2: Vulnerability Backlog by Severity**
- Stacked bar chart: Critical (CVSS ≥ 9.0), High (7.0-8.9), Medium (4.0-6.9).
- Data Source: `index=snyk_vulns | stats count by severity, repo`
- Time range: Current snapshot + 30-day trend

**Panel 3: Secret Detection Events (Last 24h)**
- Table: Timestamp, repository, detected pattern type (AWS Key, Private Key, etc.), status (Mitigated/Escalated).
- Data Source: `index=trufflehog_detections`

**Panel 4: Deployment Change Approval Log**
- Table: Timestamp, ServiceNow CHG ID, environment, artifact version, approver(s), status.
- Data Source: `index=servicenow_chg OR index=argocd_prod`

**Panel 5: SLSA Compliance by Repository**
- Traffic light report: Green (SLSA L3 achieved), Amber (SLSA L2, gap identified), Red (SLSA L1 or below).
- Metric: Repository SLSA level determined by attestation inspection.

### 7.3 Reporting Cadence

| Report | Frequency | Audience | Delivery Method |
|---|---|---|---|
| Engineering Security Scorecard (KPI Dashboard) | Monthly | CTO, VP Eng, CISO, Compliance, all Engineering Managers | PDF + Interactive Splunk Dashboard link (Confluence page `CI-CD-SEC-SCORECARD`) |
| Vulnerability Aging Report (Snyk) | Weekly | Engineering Team Leads, DevSecOps | Automated email from Snyk, Jira filter export |
| CI/CD Access Review (Entitlements) | Quarterly | Compliance Officer, VP Eng | ServiceNow report: all GitHub/Jenkins/Argo users and permissions, delta from prior review |
| Annual Third-Party Penetration Test | Annual | CISO, VP Eng, Board | External vendor report, findings tracked in Jira; remediation reviewed post-test |

---

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Process

Circumstances may arise where strict adherence to a pipeline security control is temporarily not feasible (e.g., a legacy dependency that cannot be immediately updated despite a High CVE). All exceptions must follow the formal risk acceptance process:

**Step 1: Exception Request Submission**

The Engineering Team Lead submits a **Pipeline Security Exception Request** via the ServiceNow catalog item (`CI/CD Security Exception`). The request must include:

- Control ID(s) being excepted (e.g., PENG-011-TC03)
- Artifact/repository/component affected
- Specific version(s) and deployment timeline
- Business justification for the exception
- Identified risk of proceeding
- Compensating controls proposed during the exception window
- Proposed remediation date (not to exceed 90 days)

**Step 2: Security Engineering Assessment**

Rajesh Thakur (or delegate) performs a risk assessment within **2 business days**:

- Validates the business justification
- Assesses the risk severity (Low/Medium/High/Critical)
- Evaluates the adequacy of compensating controls
- Documents the assessment in the ServiceNow record

**Step 3: Approval Authority (Risk-Based)**

| Risk Severity | Approval Required |
|---|---|
| **Low** | Security Engineering Lead (Rajesh Thakur) |
| **Medium** | Security Engineering Lead + VP of Engineering (David Park) |
| **High** | VP of Engineering + CISO + Business Unit Owner |
| **Critical** | CEO (Dr. Sarah Chen) — no exceptions granted for Critical risk without documented, CISO-endorsed mitigation |

**Step 4: Tracking and Closure**

All approved exceptions are:

- Added to the **Exception Register** (Confluence page `CI-CD-EXCEPTION-REGISTER`, linked to ServiceNow records).
- Reviewed monthly at the Engineering Security Council meeting.
- Automatically flagged 14 days before the remediation deadline; overdue exceptions escalate to the CISO and VP Eng.

### 8.2 Emergency Break-Glass Procedure

In the event of a production incident requiring immediate pipeline access to bypass a security control (e.g., emergency rollback blocked by artifact signing failure):

**Step 1:** Initiate the break-glass via the PagerDuty `devops-breakglass` escalation policy. This triggers a simultaneous alert to:
- Maria Okonkwo (DevOps Lead) — Primary
- Rajesh Thakur (Security Engineering Lead) — Secondary
- David Park (VP Engineering) — Tertiary

**Step 2:** Two authorized responders must acknowledge and join the War Room (Zoom Bridge `meridian-warroom`, pass stored in Vault).

**Step 3:** The emergency bypass is executed using the `meridian-emergency-deploy` CLI tool, which:
- Requires two distinct OAuth2 tokens (Okta-verified MFA)
- Logs the bypass event to a dedicated, immutable Splunk index (`audit_emergency`)
- Posts a message to `#incident-command` Slack channel with the bypass details
- Automatically opens a ServiceNow INC record

**Step 4:** All emergency bypass actions are reviewed at the next business day's Incident Postmortem. Any bypassed control must be reinstated within 24 hours or a formal exception (Section 8.1) must be filed.

### 8.3 Escalation Matrix

| Issue Type | First Escalation | Second Escalation | Time to Escalate |
|---|---|---|---|
| Critical vulnerability not remediated after 48h | Security Eng Lead → VP Eng | VP Eng → CTO | 24h after first miss |
| Unsigned artifact detected in production | SecEng → Incident Response | CISO → CEO | Immediate (auto-escalation via PagerDuty) |
| Secret committed and detected; rotation failure | DevOps Lead → SecEng | VP Eng → CISO | 1 hour |
| Repeated exception abuse (3+ overdue in 6 months) | VP Eng → CISO | CISO → CEO | Within business week |

---

## 9. Training Requirements

### 9.1 Required Training Curriculum

All personnel with responsibilities defined in Section 3 must complete the following training:

| Training Module | Audience | Frequency | Delivery Method | Tracking ID |
|---|---|---|---|---|
| **CI/CD Pipeline Security Fundamentals** | All Engineers, DevOps, QA | Annually | LMS (Workday Learning) | `TR-SEC-PENG011-001` |
| **Secure Coding Practices for Pipelines** | Software Engineers, DevOps | Annually | On-demand video + hands-on lab (GitHub sandbox) | `TR-SEC-PENG011-002` |
| **Secret Management and Hygiene** | All personnel with Vault access | Semi-annually | Live workshop (Security Engineering) | `TR-SEC-PENG011-003` |
| **SOC 2 Pipeline Compliance for Engineering Leads** | Engineering Team Leads, Managers | Annually | Instructor-led (Allison Vance, Compliance) | `TR-SEC-PENG011-004` |
| **Incident Response: Pipeline Compromise** | DevOps, Security Engineering | Quarterly tabletop exercise | Facilitated by CISO, 2-hour simulation | `TR-SEC-PENG011-005` |

### 9.2 Training Completion Tracking and Remediation

- Training completion is tracked via Workday Learning dashboards.
- **Compliance requirement**: 100% completion by assigned due date (Q1-end for annual training; June 30 / December 31 for semi-annual).
- **Non-compliance escalation**:
  - First overdue week: Automated reminder from Workday, cc: Team Lead.
  - Second overdue week: Team Lead notified by HR Business Partner; pipeline access flags set to "restricted" in Okta.
  - Third overdue week: Pipeline access suspended until training completed; VP of Engineering and CISO notified. Access reinstatement requires VP Eng approval.

### 9.3 Onboarding Requirements

New hires in Engineering, DevOps, and Security Engineering must complete `TR-SEC-PENG011-001`, `TR-SEC-PENG011-002`, and `TR-SEC-PENG011-003` within **14 calendar days** of their start date. Access to production pipeline resources (Jenkins, GitHub Admin, Vault production paths) is gated on training completion, enforced via Okta group membership provisioning rules.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Title | Relationship |
|---|---|---|
| **SOP-SEC-003** | Secret Lifecycle Management | Secret rotation automation referenced in Section 5.2.4 |
| **SOP-SEC-009** | HSM Key Management | Root CA and Tier-0 key management standards |
| **SOP-PENG-022** | Sandbox Environment Governance | R&D sandboxes out of scope for this SOP |
| **SOP-ITOP-045** | Legacy System Decommissioning | Legacy systems excluded from scope |
| **SOP-COMP-007** | SOC 2 Evidence Collection | Evidence mapping for SOC 2 audits |
| **SOP-PENG-015** | Incident Response for Engineering Systems | Pipeline compromise IR procedures |
| **SOP-CLIN-003** | Clinical AI Platform Change Control | EU MDR / FDA regulatory change management |
| **SOP-INFRA-001** | AWS Account and VPC Architecture | Network architecture for pipeline runners |

### 10.2 External Standards and Frameworks

| Reference | Version/Date | Application |
|---|---|---|
| **SOC 2 TSC 2017** (AICPA) | 2017 revision | Control framework for pipeline security and availability |
| **SLSA (Supply-chain Levels for Software Artifacts) v1.0** | April 2024 | Supply chain integrity framework; Meridian targets SLSA Level 3 |
| **NIST SP 800-204D** (Draft) | 2023 | Secure CI/CD guidance referenced in hardening design |
| **OWASP Top 10 CI/CD Security Risks** | 2022 | Risk assessment framework for pipeline security controls |
| **CNCF Software Supply Chain Best Practices** | 2023 | Artifact signing and SBOM guidance; Cosign usage |
| **AWS Well-Architected Framework — Security Pillar** | 2024 | Reference for IAM policy design and KMS key management |

---

## 11. Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 1.0 | 2022-11-15 | Maria Okonkwo | Initial version; defined pipeline security baseline for GitHub Actions and initial Jenkins migration. |
| 1.3 | 2023-03-08 | Rajesh Thakur | Added secret scanning integration (TruffleHog); introduced Artifact Signing section with Cosign pilot. |
| 2.0 | 2023-08-22 | David Park | Major revision: expanded scope to include ArgoCD deployment paths; added SLSA Level 3 requirements; mandated SBOM generation. |
| 2.4 | 2024-02-10 | Allison Vance | Compliance revision: mapped all controls to SOC 2 TSC; added formal roles table, metrics dashboard, and ServiceNow approval integration. |
| 3.0 | 2024-09-30 | Rajesh Thakur / Maria Okonkwo | Complete rewrite: added hardened runner baseline, ephemeral runner lifecycle, in-toto attestation, and break-glass emergency procedure. Moved from SLSA L2 to L3. |
| 3.5 | 2025-01-12 | David Park | Updated to comply with FDA 510(k) / CE-marked release requirements for Clinical AI Platform; added isolated runner pools for regulated workloads. |
| **3.8** | **2026-07-18** | Rajesh Thakur | Annual review: updated KPI targets for 2026, revised approver pool, added Snyk-to-Splunk integration details; updated external references (SLSA v1.0); no policy scope changes. |

---

**Document Control:**
This SOP is governed by Meridian's Policy Management Framework (SOP-GRC-001). Proposed changes to this document must be submitted via Pull Request to the `policies/cicd-security` repository or via a ServiceNow Policy Change Request. All changes require the documented approval of the SOP Owner and Approver. This document, when printed, is uncontrolled. The authoritative version resides at `https://policies.meridian.tech/sop/SOP-PENG-011`.