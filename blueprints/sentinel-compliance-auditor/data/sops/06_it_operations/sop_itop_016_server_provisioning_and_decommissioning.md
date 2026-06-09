---
sop_id: "SOP-ITOP-016"
title: "Server Provisioning and Decommissioning"
business_unit: "IT Operations & Infrastructure"
version: "2.1"
effective_date: "2024-09-05"
last_reviewed: "2025-08-21"
next_review: "2026-02-09"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Server Provisioning and Decommissioning

**SOP-ID:** SOP-ITOP-016
**Business Unit:** IT Operations & Infrastructure
**Version:** 2.1

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the standardized, auditable, and repeatable processes by which Meridian Health Technologies, Inc. provisions, configures, hardens, and decommissions server infrastructure across all environments. The purpose is to ensure the confidentiality, integrity, and availability of Meridian’s data and systems—including the Meridian SaaS Platform, Clinical AI Platform, HealthPay Financial Services, and MedInsight Analytics—by enforcing a common security baseline from the moment a compute instance is created until its final destruction. This SOP directly supports Meridian’s commitments under its SOC 2 Type II certification and facilitates the protection of electronic Protected Health Information (ePHI) as required by HIPAA.

### 1.2 Scope
This SOP applies to all virtual server instances, bare-metal hosts, and container host nodes that are used to store, process, or transmit Meridian corporate data or customer data, including ePHI and Personal Data subject to GDPR. The scope encompasses all environments across all Meridian global offices:

| Environment | Primary Cloud/Infrastructure | Locations |
| :--- | :--- | :--- |
| **Production** | AWS (us-east-1, eu-west-1) | North America, European Union |
| **Staging** | AWS (us-east-1) | North America |
| **Development/Test** | AWS (us-east-1) | North America |
| **Disaster Recovery** | Azure | North America |
| **Corporate IT/Back-Office** | AWS & On-Premise (Boston, London, Berlin, Singapore, Toronto) | Global |

This SOP applies to all employees, contractors, consultants, and third parties who are involved in the lifecycle management of server infrastructure. It is mandatory for the IT Operations & Infrastructure and Engineering departments. Observability tooling (Datadog, PagerDuty) deployment and basic agent installation are covered, but detailed configuration of specific application-layer monitoring dashboards is outside the scope of this document.

---

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **AMI** | Amazon Machine Image. A pre-configured template used to create EC2 instances in AWS. |
| **Asset Inventory** | The centralized system of record for all hardware and software assets, managed in ServiceNow’s Configuration Management Database (CMDB). |
| **CIS Benchmark** | Center for Internet Security benchmarks, a set of consensus-based, vendor-agnostic secure configuration guidelines. |
| **CSP** | Cloud Service Provider (e.g., AWS, Azure). |
| **Data Sanitization** | The process of deliberately, permanently, and irreversibly removing or destroying the data stored on a memory device to ensure it cannot be recovered. |
| **Decommissioning** | The complete process of removing a server asset from operations, including data sanitization, software license reclamation, and removal from the asset inventory. |
| **ePHI** | Electronic Protected Health Information, as defined by HIPAA. |
| **Golden Image** | A pre-configured base operating system image that includes mandatory security agents and baseline configuration, serving as the only approved starting point for new server instances. |
| **Hardening** | The process of securing a system by reducing its surface of vulnerability, accomplished by removing unnecessary software, services, and user accounts and applying strict configuration settings. |
| **Infrastructure as Code (IaC)** | The process of managing and provisioning infrastructure through machine-readable definition files (Meridian standard: Terraform). |
| **Patching Baseline** | A defined minimum patch level that all servers in a specific classification must meet. |
| **Provisioning** | The end-to-end process of creating, configuring, and deploying a new server instance into an environment. |
| **ServiceNow CMDB** | Meridian’s central Configuration Management Database, a component of the ServiceNow IT Service Management (ITSM) platform. |
| **Terraform** | Meridian’s standard Infrastructure as Code platform for provisioning cloud resources across AWS and Azure. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for the server lifecycle:

| Activity / Task | VP of IT Ops (S. Torres) | IT Ops Engineer | DevOps/Infra Engineer | CISO (R. Kim) | Business Unit VP | ServiceNow Asset Mgmt |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Policy and Standard Definition** | **A, R** | C | C | I | I | I |
| **Provisioning Request Approval** | A | R | C | I | I | I |
| **IaC Template Maintenance** | I | R | **A, R** | C | I | I |
| **Golden Image Maintenance** | I | I | **A, R** | R | I | I |
| **Server Build Execution** | I | **R** | **R** | I | I | I |
| **Hardening Script Execution** | I | **R** | **R** | I | I | I |
| **Asset Registration in CMDB** | A | C | C | I | I | **R** |
| **Monitoring Agent Installation** | I | **R** | **R** | I | I | I |
| **Decommissioning Request Approval** | **A** | I | I | C | I | R |
| **Data Sanitization Execution** | I | **R** | C | I | I | I |
| **Certificate of Destruction Issuance** | A | **R** | I | I | I | I |
| **Exception Handling & Approval** | **A, R** | C | C | C | C | C |

**R = Responsible** (executes the task), **A = Accountable** (approves and owns outcome), **C = Consulted**, **I = Informed**

---

## 4. Policy Statements

1.  **Infrastructure as Code Mandate:** All server provisioning in AWS and Azure production environments must be executed exclusively through Terraform. No manual console-based provisioning is permitted.
2.  **Golden Image Requirement:** All new servers must be provisioned from a Meridian-approved, pre-hardened Golden Image. Deployment of instances from community, marketplace, or non-standard AMIs is prohibited.
3.  **Baseline Configuration Standard:** All servers, regardless of operating system, must be hardened to the latest CIS Benchmark Level 1 recommendations within four (4) hours of initial boot.
4.  **Asset Lifecycle Management:** Every server instance must have a complete and accurate record in the ServiceNow CMDB before it is allowed to process any network traffic. The record must be updated at each lifecycle stage and marked for destruction within 24 hours of decommissioning.
5.  **Data Sanitization:** All storage volumes attached to a decommissioned server must be sanitized in accordance with NIST SP 800-88 Rev. 1 guidelines. A Certificate of Destruction must be generated and archived for every sanitized volume.
6.  **Segregation of Duties:** An individual who provisions a server may not be the sole individual responsible for approving the decommissioning and certifying data sanitization for that same asset.
7.  **Breach Notification:** In the event of a security incident involving a server, the incident response process in SOP-ISRM-002 must be initiated immediately. The General Counsel and Chief Privacy Officer must be notified to determine regulatory notification requirements for affected parties.

---

## 5. Detailed Procedures

This section details the step-by-step operational procedures for the two primary lifecycle stages: Provisioning and Decommissioning.

### 5.1 Server Provisioning Procedure

This procedure is triggered by an approved change request (CR) submitted through ServiceNow and approved by the IT Operations management as per the Change Management Policy (SOP-ITSM-001).

**Pre-requisites:**
- Approved ServiceNow Change Request (CR) number.
- Approved server classification determined by the Data Governance team.
- Allocated IP range from the Network Engineering team.
- Valid Meridian cost center and project code.

#### 5.1.1 Step-by-Step Provisioning Workflow

**Step 1: Validate Request and Assign Resources**
- The IT Operations Engineer receives the approved CR from the ServiceNow queue.
- Validate that all mandatory fields in the CR are complete: `environment`, `server_function`, `data_classification`, `os_version`, `instance_size`, `vpc_subnet`, `business_owner`, `patching_group`.
- Assign the provisioning task to a specific Infra Engineer.

**Step 2: Clone IaC Module**
- The Infra Engineer clones the `meridian-tf-modules` repository from GitHub Enterprise.
- Navigate to the `compute/` directory and copy the module that corresponds to the target environment and CSP (e.g., `ec2-prod-us-east-1`).
- Create a new feature branch named: `itop-016/<CR_NUMBER>-<hostname>`.

**Step 3: Define Infrastructure in Terraform**
- Populate the `terraform.tfvars` file with the exact specifications from the CR. An example block is below:

    ```hcl
    # terraform.tfvars
    hostname             = "prd-clinical-ai-ml-07"
    environment          = "prod"
    data_classification  = "ePHI"
    instance_type        = "p3.2xlarge"
    ami_id               = "ami-meridian-golden-v2.1.0" # From Golden Image library
    subnet_id            = "subnet-priv-app-us-east-1a"
    security_groups      = ["sg-clinical-ai-internal"]
    iam_instance_profile = "role-ec2-clinical-ai"
    patching_group       = "group-a-weekly-sun"
    backup_policy        = "daily-30-day-retention"
    cost_center          = "CC-3045"
    ```

- **Mandatory Tagging:** Ensure all Meridian-mandated tags are defined. The critical tags are:

    | Tag Key | Example Value | Required |
    | :--- | :--- | :---: |
    | `Name` | `prd-clinical-ai-ml-07` | Yes |
    | `Environment` | `prd` | Yes |
    | `Data-Class` | `ePHI` | Yes |
    | `Owner` | `clinical-ai-eng@meridian.com` | Yes |
    | `CR-Number` | `CR-2024-09872` | Yes |
    | `Backup` | `daily-30` | Yes |
    | `Patch-Group` | `group-a` | Yes |

- Run `terraform validate` and `terraform plan` locally. Save the `plan` output to a file for audit.

**Step 4: Peer Review and Merge**
- Commit the code and push the branch. Create a Pull Request (PR) in GitHub.
- At least one (1) senior Infra or DevOps Engineer must review and approve the PR. The approver checks for: correct AMI, correct subnet placement, appropriate IAM role, proper tagging, and storage encryption (AWS KMS CMK) settings.
- Upon approval, merge the PR to the `main` branch. A CI/CD pipeline in Jenkins automatically runs `terraform apply` against the target account.

**Step 5: Post-Provisioning Automation Validation**
- The Jenkins pipeline triggers an initial Ansible playbook run against the newly created instance.
- The Ansible playbook performs the following pre-hardening validation:
    1.  Confirms the instance is reachable and managed by Red Hat Satellite/AWS Systems Manager.
    2.  Installs the Meridian root CA certificate chain.
    3.  Verifies that all non-root, default AMI accounts are disabled.
    4.  Verifies that the root volume is encrypted with the correct KMS key ARN.

**Step 6: Execute OS Hardening (Ansible)**
- A second Ansible playbook executes the CIS Benchmark Level 1 hardening. The playbook applies the exact configuration specified in the `meridian-hardening` repository, which includes:
    - Disabling all non-essential TCP/UDP ports.
    - Configuring `auditd` for system call and file access logging.
    - Installing and configuring `auditbeat` to ship logs to the central Elastic SIEM cluster.
    - Enforcing password complexity, aging, and lockout policies on local accounts.
    - Removing unapproved packages and compilers.
    - Deploying `sudo` rulesets that map to the `iam_instance_profile` role.

**Step 7: Install Mandatory Security and Observability Agents**
- The final Ansible playbook installs and validates the Meridian agent stack:
    - **CrowdStrike Falcon Sensor:** Registered to the appropriate CID for the environment.
    - **Datadog Agent:** Configured with environment and role-specific tags.
    - **AWS CloudWatch Agent:** Configured for system-level metrics and custom log groups per the server’s function.
    - **HashiCorp Vault Agent:** For secret retrieval and dynamic credential management, if applicable.

**Step 8: Register Asset in ServiceNow CMDB**
- A successful `terraform apply` sends an API call to ServiceNow to auto-create a Configuration Item (CI).
- The IT Operations Engineer validates that the auto-populated CI record is complete, specifically the `Asset Tag`, `Data Classification`, `Patching Schedule`, and `Business Owner` fields.
- The server is placed into the `IN_MAINTENANCE` state until final application validation is complete.

**Step 9: Application Handover**
- The business unit application owner receives a notification from ServiceNow with the hostname, IP address, and OS login credentials (transmitted via an encrypted, one-time-use SecretStack link).
- The application team has a 72-hour window to deploy and validate its application.
- Upon written confirmation of successful validation from the business owner, the IT Operations Engineer updates the ServiceNow CI state to `OPERATIONAL`.

### 5.2 Server Decommissioning Procedure

This procedure is triggered by a decommissioning request (DR) in ServiceNow, approved by the VP of IT Operations and the server’s Business Owner.

**Pre-requisites:**
- Approved ServiceNow Decommissioning Request (DR).
- Written confirmation from the Business Owner that all dependent services have been migrated, and all application-specific data exports are complete.
- Identified backup retention hold expiration date, if applicable.

#### 5.2.1 Step-by-Step Decommissioning Workflow

**Step 1: Pre-Termination Preparation**
- The IT Operations Engineer verifies the DR has been approved by both the VP of IT Ops and the Business Owner.
- In the AWS Console (or Azure Portal for DR environment), the engineer places the instance in a `Quarantine` Security Group. This security group has no `ALLOW` ingress or egress rules, effectively isolating the server from all network traffic while leaving it running.
- The instance is left in quarantine for a 72-hour cool-down period. This allows for the safe rollback of the decommissioning in case of an unanticipated dependency.

**Step 2: Final Data Capture and Backup**
- After the 72-hour cool-down, the IT Operations Engineer creates a final, manual EBS snapshot (or Azure Managed Disk snapshot). The snapshot is tagged as `Decommission-Final-YYYY-MM-DD` and moved to a locked backup vault with immutable retention set to the policy defined for the server's data classification (e.g., 90 days for ePHI systems).

**Step 3: Data Sanitization**
- Upon completion of the final snapshot, the engineer proceeds with data sanitization.
- **For AWS Instances:** The engineer launches a purpose-built, air-gapped forensic instance. The non-boot volumes from the target server are detached and re-attached to the forensic instance.
- The engineer executes a data wipe utility on each attached volume. For standard volumes, a `shred` operation with three (3) passes is executed (e.g., `shred -v -n 3 -z /dev/nvme1n1`). For volumes that contained ePHI, a `wipe` utility configured to the ATA Secure Erase command is leveraged.
- A verification script performs a hex dump inspection on the first and last 1000 sectors of the drive to confirm data erasure.

**Step 4: Generate Certificate of Destruction**
- Upon successful verification, the forensic instance generates a digitally signed Certificate of Destruction (CoD) for each volume. The CoD is a JSON document containing the Meridian asset ID, the volume serial number, the sanitization method and verification checksum, and a UTC timestamp.
- The CoD is automatically uploaded to a sealed, write-once-read-many (WORM) AWS S3 bucket: `s3://meridian-audit/cod/`.

**Step 5: Execute Infrastructure Termination**
- With the CoD uploaded, the forensic instance is terminated.
- The original server's IaC module is updated. The resource block, or the complete module instance, is removed from the active codebase.
- A peer-reviewed PR is submitted and merged. The Jenkins pipeline executes `terraform apply`, which permanently deletes the server and all attached resources (ENIs, non-persistent volumes). The manually created final snapshot is retained.

**Step 6: CMDB and Asset Management Finalization**
- The IT Operations Engineer updates the ServiceNow CI record, setting the `Operational Status` to `Retired` and the `Substatus` to `Destroyed`.
- The engineer attaches the S3 metadata object link for the Certificate of Destruction to the CI record.
- The CI is archived 30 days after the `Retired` status is set.

---

## 6. Controls and Safeguards

Meridian employs a defense-in-depth model of controls to protect the server lifecycle.

### 6.1 Technical Controls

| Control | Implementation | Standard Reference |
| :--- | :--- | :--- |
| **Privileged Access Management** | All interactive server access requires temporary security credentials generated by HashiCorp Vault. No static SSH keys are allowed. PAM sessions are recorded by Teleport. | CIS v8, Control 5.6 |
| **Immutable Images** | Production Golden AMI pipeline builds from a hardened ISO. AMIs are shared only with authorized accounts and are immutable once built. | CIS v8, Control 4.1 |
| **Automated Vulnerability Scanning** | Amazon Inspector scans all EC2 instances and ECR container images on deployment and at 24-hour intervals. Findings are routed to ServiceNow for remediation tracking. | AWS Well-Architected |
| **Logging and Monitoring** | `auditd` logs all system calls from non-root users. CloudWatch Agent streams application and security logs to New Relic for real-time anomaly detection. Datadog monitors agent health; an agent-down status triggers a PagerDuty P3 alert. | Meridian Security Monitoring Standard |
| **Endpoint Detection and Response (EDR)** | CrowdStrike Falcon is present as the sole EDR solution. Its tamper-protection feature is enabled, and the uninstallation token requires dual-person approval. | CISO Policy MEMO-2024-07 |
| **Network Segmentation** | Server subnets are functionally isolated (e.g., `subnet-clinical-ai-app` is distinct from `subnet-healthpay-web`). A Palo Alto Prisma Cloud central firewall enforces a zero-trust, allow-list-only policy between subnets. | Meridian Network Architecture Standard |

### 6.2 Administrative Controls

- **Segregation of Duties:** The user who merges a Terraform PR to provision a server cannot be the same user who merges the PR to decommission it. ServiceNow workflows enforce this check.
- **Least Privilege Access:** IAM roles for servers follow a strict least-privilege model, allowing only the specific AWS API calls needed for the installed application to function. This is validated on every `terraform plan`.
- **Change Management:** No provisioning or decommissioning action occurs without a formally approved CR or DR in ServiceNow.

---

## 7. Monitoring, Metrics, and Reporting

The health and efficacy of this SOP are tracked through continuous monitoring and key performance indicators (KPIs). Non-compliance is met with automated alerts and manual audits.

### 7.1 Key Performance Indicators (KPIs) and Service Level Agreements (SLAs)

| Metric | Target SLA | Measurement Tool | Reporting Cadence |
| :--- | :---: | :--- | :--- |
| **Provisioning Lead Time** (from Approved CR to `OPERATIONAL` state) | 24 hours for Standard instances, 72 hours for High-Performance Compute (HPC) | ServiceNow Performance Analytics | Weekly (IT Ops Team Dashboard) |
| **Post-Boot Hardening Completion** | 100% completion within 4 hours of instance launch | AWS Config rule: `required-tags` and `ec2-managedinstance-association-compliance`; Custom Ansible Tower/AWX dashboard | Real-time alerting via PagerDuty |
| **Provisioning IaC Compliance** | 100% of Production instances | AWS Config, `terraform-compliance` CI/CD | Monthly (Governance Report) |
| **CMDB Accuracy** | >99% correlation between running CSP instances and CMDB records | ServiceNow Discovery & Reconciliation Engine | Bi-Weekly |
| **Decommissioning Cool-Down Violations** | 0 per quarter | Custom CloudWatch Events rule monitoring Security Group changes | Quarterly (Audit Review) |
| **Certificate of Destruction Completeness** | 100% (every decommissioned ePHI & PII volume must have a valid CoD in the WORM bucket) | S3 Inventory and AWS Athena queries | Monthly (Audit Review) |

### 7.2 Dashboards and Reports

- **IT Operations Real-Time Dashboard:** A Grafana dashboard displays the state of all recent provisioning runs, including pipeline status, playbook success/failure, and CI status. This is displayed on the IT Ops NOC screens.
- **Monthly Governance Report:** The VP of IT Operations receives an automated report from ServiceNow and Prisma Cloud detailing: provisioning SLAs met vs. missed, all decommissioning activities, and a reconciliation of the CMDB-to-live-environment asset count. Any discrepancies are tracked as formal incidents.
- **Quarterly Audit Review:** David Park (VP of Engineering) and Samantha Torres (VP of IT Operations) conduct a joint review of a random 10% sample of all server lifecycle events from the previous quarter, covering from provisioning to final destruction, to ensure total procedural compliance.

---

## 8. Exception Handling and Escalation

Deviations from this SOP are permitted only through a formally documented and approved Exception Request. Routine operational convenience is not a valid justification for an exception.

### 8.1 Exception Process
1.  **Identification and Justification:** The requester identifies a specific procedural step or control that cannot be met and articulates a compelling business, technical, or research justification. A compensating control or a time-bound remediation plan must be provided.
2.  **Formal Request Submission:** The requester submits an Exception Request through the IT Governance request form in ServiceNow (Request Type: `Policy Exception`), referencing `SOP-ITOP-016`.
3.  **Risk Assessment:** The VP of IT Operations or their delegate performs a preliminary risk assessment, documented in the ServiceNow ticket. If the exception involves a system handling ePHI or PCI data, the CISO (Rachel Kim) must be consulted.
4.  **Approval Workflow:**
    - Exceptions involving a duration of less than 30 days and for `DEV/TEST` environments: Approval from VP of IT Operations.
    - Exceptions involving a duration of more than 30 days, `STAGING` environments, or minor controls: Concurrence from VP of IT Operations and VP of Engineering.
    - Exceptions involving any `PRODUCTION` environment, any ePHI data system, any decommissioning requirement, or any core security control (e.g., no CrowdStrike, no encryption): Full approval board, consisting of VP of IT Operations, VP of Engineering, and the CISO.
5.  **Tracking and Expiry:** All approved exceptions are logged in the ServiceNow Exception Register. Each exception has a specific expiration date. Three business days before expiry, the owner is automatically notified to provide revalidation or initiate remediation. An expired, un-remediated exception is escalated to a non-compliance incident and is reported to the Chief Privacy Officer.

### 8.2 Escalation Matrix
If any step in the provisioning or decommissioning procedure fails or is blocked, the following escalation path is followed:

| Time Unresolved | Escalation Target |
| :--- | :--- |
| At first failure | IT Ops Shift Lead (Monitoring PagerDuty alert) |
| > 2 hours | IT Operations Manager |
| > 8 hours (impacts PROD change window) | **Samantha Torres**, VP of IT Operations |
| > 24 hours (impacts a clinical system or ePHI) | **Rachel Kim**, CISO, **David Park**, VP of Engineering |

---

## 9. Training Requirements

All individuals assigned a role in the RACI matrix of this SOP must complete mandatory, role-specific training on the server lifecycle, Meridian tooling, and the procedures outlined herein.

| Training Module | Target Audience | Method | Frequency | Tracking System |
| :--- | :--- | :--- | :--- | :--- |
| **SOP-ITOP-016 Policy Acknowledgment** | All IT Ops, DevOps, and Engineering Staff | Digital acknowledgment of the policy document in ServiceNow | **Annually** | ServiceNow Employee Center |
| **IaC Server Lifecycle Workshop** | IT Ops Engineers, Infra/DevOps Engineers | Instructor-led, 4-hour workshop covering the full Terraform provisioning pipeline, Ansible playbook structure, and decommissioning workflow | **Upon hire; refresher annually** | MyLearn LMS (Cornerstone) |
| **HIPAA & Data Handling for Infrastructure** | IT Ops Engineers managing `ePHI`-tagged infrastructure | Asynchronous eLearning module focused on the specific controls required for ePHI-bearing hosts | **Annually** | MyLearn LMS (Cornerstone) |
| **Secure Sanitization & Forensic Procedure** | Senior IT Ops Engineers designated to execute decommissions | 2-day intensive lab, including a hands-on practical examination on the forensic sanitization procedure and CoD generation | **Upon designation; re-certification every 2 years** | MyLearn LMS; Practical exam results tracked by CISO office |

Training compliance is monitored by the VP of IT Operations. System access to perform provisioning and decommissioning tasks is automatically revoked for any individual whose training has expired for more than 30 days, enforced via automated group membership in Active Directory and AWS SSO.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP-ID | Policy Name |
| :--- | :--- |
| SOP-ITSM-001 | Change Management Policy |
| SOP-ISRM-002 | Information Security Risk Management and Incident Response |
| SOP-ISRM-004 | Vulnerability Management and Patching Standard |
| SOP-DAT-002 | Cryptographic Controls and Key Management Standard (for KMS usage) |
| SOP-NET-005 | Network Segmentation, Firewall, and Subnetting Standard |
| SOP-ITSEC-010 | Endpoint Security Standard (Agent Deployment) |
| SOP-CM-001 | Configuration and Asset Management Standard (ServiceNow CMDB) |
| SOP-BCDR-001 | Backup and Disaster Recovery Standard |

### 10.2 External Standards and Frameworks

- **AICPA TSC 2017** (Trust Services Criteria for Security, Availability, and Confidentiality)
- **HIPAA Security Rule** (45 CFR Part 160 and Subparts A and C of Part 164)
- **NIST SP 800-88 Rev. 1**, “Guidelines for Media Sanitization”
- **Center for Internet Security (CIS) Benchmarks**
    - CIS Amazon Web Services Foundations Benchmark
    - CIS Red Hat Enterprise Linux 8 Benchmark
    - CIS Microsoft Windows Server 2022 Benchmark

---

## 11. Revision History

| Version | Date | Author(s) | Description of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2022-01-12 | J. Doe (IT Ops Manager) | Initial release of server lifecycle SOP. |
| 1.1 | 2022-09-18 | M. Patel (Sr. Infra Eng) | Added Terraform IaC mandate for Production, updated AMI hardening pipeline description. |
| 2.0 | 2023-06-01 | S. Torres (VP IT Ops) | Major revision: merged Provisioning (SOP-ITOP-009) and Decommissioning (SOP-ITOP-013) into a single lifecycle SOP. Introduced forensic sanitization procedure and CoD requirement for ePHI volumes. Added explicit KPI/SLA tables. |
| 2.0.1 | 2023-10-19 | K. Li (GRC Analyst) | Minor edit: updated title of related SOP-ITSEC-010 and added missing `Approver` field in YAML. |
| 2.1 | 2024-09-05 | S. Torres (VP IT Ops) | Major revision: Updated tagging schema and CMDB registration process to align with new ServiceNow Vancouver release. Expanded Ansible playbook workflow to include new Datadog agent configuration standard. Revised exception process to include formal approval board for production systems. Effective immediately. |