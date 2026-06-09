---
sop_id: "SOP-ISEC-019"
title: "Privileged Access Management"
business_unit: "Information Security"
version: "2.1"
effective_date: "2025-09-07"
last_reviewed: "2026-05-02"
next_review: "2026-11-06"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Privileged Access Management

**SOP-ISEC-019 | Version 2.1**
**Effective: 2025-09-07**
**Owner: Rachel Kim, Chief Information Security Officer**

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (“SOP”) establishes the enterprise-wide framework for Privileged Access Management (“PAM”) at Meridian Health Technologies, Inc. (“Meridian,” the “Company”). The purpose of this SOP is to mitigate the heightened risk associated with privileged accounts — those accounts possessing elevated permissions capable of causing material harm to the confidentiality, integrity, and availability of Meridian’s information assets, to patient protected health information (“PHI”), or to the financial services infrastructure under the Company’s management.

This SOP defines the mandatory controls governing the lifecycle of privileged credentials, the authentication and authorization mechanisms for privileged sessions, the monitoring and audit of privileged activity, and the emergency procedures required when standard access pathways are unavailable.

Given Meridian’s operations as an AI-powered healthcare fintech organization — with a Clinical AI Platform classified as high-risk under the EU AI Act, HealthPay Financial Services processing $4.2 billion annually, and MedInsight Analytics managing PHI for approximately 12 million patients — uncontrolled privileged access represents an existential operational, financial, and regulatory risk. A single compromised administrative credential exfiltrating model weights from the Clinical AI Platform, manipulating models subject to SR 11-7, or exposing multi-million record PHI datasets would trigger mandatory breach notifications across multiple jurisdictions, invalidate CE markings, and expose the Company to civil and criminal liability.

### 1.2 Scope

This SOP applies to all systems, applications, cloud workloads, databases, network devices, endpoints, and services operating within or on behalf of Meridian’s corporate and production environments — whether hosted on-premises within Meridian data centers, within the Amazon Web Services (“AWS”) commercial East/West tenant structures, or within Microsoft Azure tenancies supporting the MedInsight Analytics platform.

**In-Scope Access Types:**

| Category | Description | Examples |
|----------|-------------|----------|
| Administrative Accounts | Local or domain-level administrator, root, or equivalent | AWS IAM Administrator policies, Domain Admins in Meridian CORP forest, sudoers on Linux workloads hosting Clinical AI inference services |
| Application-to-Application (“A2A”) Service Accounts | Non-human identities used for automated service interactions | CI/CD pipeline service accounts under Okta SSO, CyberArk CCP-managed credentials for container orchestration |
| Emergency / Break-Glass Accounts | Highly privileged, restricted-use accounts reserved for crisis scenarios | Domain “BREAKGLASS-ADMIN” accounts, AWS Organization root user credentials secured under CyberArk |
| Third-Party / Vendor Remote Access | Temporary privileged sessions granted to external support personnel | Epic hyperspace support vendor temporary local admin, network hardware vendor TACACS+ shell access |
| API Keys, Secrets, and Tokens | Programmatic credentials granting privileged data-plane access | GitHub secret scanning-managed API tokens, HashiCorp Vault kv-v2 stored HMAC keys for PHI data services |

**In-Scope Environments:**

- Meridian CORP (Microsoft Active Directory Domain Services, Entra ID Connect synchronized)
- Meridian PROD (segregated Active Directory forest for clinical and financial services)
- AWS Organizations (Management Account + `audit`, `log-archive`, `Clinical-AI-Prod`, `HealthPay-Prod`, `MedInsight-Prod`, `Dev-Sandbox` Organizational Units)
- Azure AD / Entra ID tenant `meridianhealthtech.onmicrosoft.com`
- All network infrastructure, including Cisco Catalyst switches, Palo Alto Networks next-generation firewalls, and Aviatrix transit gateways
- All endpoint devices issued to personnel with privileged access rights (subject to endpoint privilege management via CyberArk Endpoint Privilege Manager [“EPM”])

**Out-of-Scope:** Standard user accounts lacking administrative or sensitive-data-plane permissions are governed under the Identity and Access Management SOP (SOP-ISEC-004) and are not addressed here, except where elevation from standard to privileged context is managed via the PAM solution.

---

## 2. Definitions and Acronyms

| Term | Definition |
|------|------------|
| **Break-Glass Account** | A highly privileged, dedicated account intended for emergency use only when the standard identity provider or PAM solution is unavailable. Use of a break-glass account triggers immediate, high-priority alerting. |
| **CyberArk** | The enterprise-selected PAM solution, encompassing the CyberArk Privileged Access Security Solution (PAS), including the Vault, Privileged Session Manager (“PSM”), Central Policy Manager (“CPM”), and Application Access Manager (“AAM”), deployed across all in-scope environments. |
| **Just-in-Time (“JIT”) Access** | A provisioning model wherein privileged elevation is granted on a temporary, purpose-specific basis immediately upon verified request, rather than standing entitlement. At Meridian, JIT is realized through CyberArk PSM for Secure Connect and direct integration with AWS IAM Identity Center and Azure Privileged Identity Management (“PIM”). |
| **Least Privilege** | The principle that an identity — human or non-human — shall possess only the minimum set of permissions, for the minimum duration, necessary to execute an authorized task. |
| **PHI** | Protected Health Information, as defined under the Health Insurance Portability and Accountability Act of 1996 (“HIPAA”) and its implementing regulations at 45 C.F.R. Parts 160 and 164. |
| **Privileged Session Manager (“PSM”)** | The CyberArk component that brokers, isolates, and records privileged sessions, ensuring that credentials are never directly exposed to the end-user workstation. |
| **Remote Access - Privileged** | Any access from a network outside Meridian’s direct administrative control (e.g., VPN from a vendor site), combined with privileged elevation. |
| **Secrets Management** | The lifecycle governance of non-human privileged credentials — API keys, tokens, certificates — including automated rotation, revocation, and access audit. |
| **Session Recording** | The full-fidelity, tamper-proof capture of all input and output (keystrokes, mouse events, screen video) occurring during a privileged session, stored in an immutable audit repository. |
| **Vault** | The CyberArk centralized, encrypted credential store where all managed privileged credentials are secured. |
| **CPM** | Central Policy Manager — the CyberArk component responsible for automated password rotation and verification for managed accounts. |
| **RTO / RPO** | Recovery Time Objective / Recovery Point Objective. Referenced conceptually within Meridian’s business continuity planning, but specific numeric targets for PAM infrastructure restoration are defined in the Business Continuity SOP (SOP-BCDR-002). |
| **SoD** | Segregation of Duties — the preventative control ensuring that no single individual can both request and approve their own privileged elevation. |
| **EPM** | CyberArk Endpoint Privilege Manager — agent-based solution enforcing least privilege on Windows and macOS endpoints, including application control and credential theft protection. |

---

## 3. Roles and Responsibilities

The following responsibility assignment matrix governs all activities under this SOP. All named roles correspond to established Meridian organizational positions or functional groups. The accountable party bears ultimate answerability; the responsible party executes the task; the consulted party provides mandatory input; the informed party receives status updates.

| Activity / Decision | Information Security Officer (R. Kim) | VP, Infrastructure & Cloud (M. Okonkwo) | Director, GRC (J. Reinhardt) | Engineering Leads (per BU) | SOC Manager (P. Varma) | Internal Audit | All Privileged Users |
|---------------------|----------------------------------------|----------------------------------------|-------------------------------|-----------------------------|------------------------|----------------|-----------------------|
| PAM Solution Architecture & Lifecycle | A | R | C | C | C | I | — |
| Privileged Access Request Approval (Standard) | — | A | — | R (submitter’s mgr) | — | — | R (requester) |
| Break-Glass Account Activation | A (post-hoc) | I | R (post-hoc review) | — | R (immediate response) | I | R (activator) |
| Quarterly Access Reviews | — | R | A | R | — | I | — |
| Session Recording Audit & Exception Flagging | — | — | — | — | R | I | — |
| Password Rotation Schedule Compliance | — | R | — | — | C (monitoring) | I | — |
| Vendor/Third-Party Privileged Access Approval | A | R | R | C | — | I | — |
| Annual PAM Policy Exception Review | A | C | R | C | C | I | — |
| Compliance with this SOP | — | — | — | — | — | I | R |

**Named Role-Specific Obligations:**

- **Rachel Kim, CISO:** Approves all break-glass activations post-hoc within 24 hours. Authorizes any permanent exception to this SOP. Sponsors the annual PAM program review to the Executive Risk Committee.
- **Moses Okonkwo, VP Infrastructure & Cloud:** Ensures CPM rotation health across all AWS and Azure environments. Authorizes integration of new cloud services into CyberArk AAM.
- **Jana Reinhardt, Director GRC:** Reviews quarterly access certifications for completeness. Flags privilege accumulation patterns during access reviews (e.g., a developer retaining production write access after rotating off a project). Validates evidence collection for SOC 2 CC6.x criteria mapping.
- **SOC Manager (Priya Varma):** Configures, tunes, and responds to all CyberArk PTA (Privileged Threat Analytics) alerts. Ensures DVR-like session recording indexing for rapid incident playback.

---

## 4. Policy Statements

### 4.1 Least Privilege and Segregation of Duties

Meridian grants privileged access exclusively on the principle of least privilege. No individual shall possess standing, unrestricted administrative access to any production system, database, network device, or cloud workload housing PHI, financial transaction processing logic, or model training pipelines. All privileged access requests shall demonstrate a legitimate business need, specify the exact scope of required permissions, and state the minimum duration for which those permissions are necessary.

Segregation of Duties shall be enforced programmatically: no individual may approve their own privileged access request. For break-glass activations, the segregation control exists post-hoc — the activators, the approver (CISO, within 24 hours), and the reviewer (GRC, within one business week) shall be distinct individuals to the greatest extent organizationally feasible.

### 4.2 CyberArk as Authoritative PAM Solution

CyberArk PAS constitutes the sole approved enterprise PAM solution. All in-scope privileged credentials shall be onboarded into and managed by the CyberArk Vault. Manual management (spreadsheets, shared password vaults, hard-coded credentials in scripts or configuration files) is expressly forbidden.

**Mandatory CyberArk Coverage:**
- All Active Directory Domain Admin, Enterprise Admin, and equivalent accounts.
- All `root` and `sudo-capable` Linux accounts on production hosts.
- All AWS IAM users, roles with `AdministratorAccess` or equivalent wildcard policies, and the Organization root user.
- All Azure Global Administrator and Privileged Role Administrator assignments.
- All local administrator accounts on Windows Server operating systems in CORP and PROD forests.
- All network device enable passwords and TACACS+/RADIUS shared secrets.

### 4.3 Just-in-Time Access Model

Effective from the date of this version, all production privileged access shall migrate to a Just-in-Time model. Standing privileged group membership is prohibited except for:
- Break-glass accounts (inherently standing but alerting-controlled).
- A strictly limited set of infrastructure automation service accounts, which shall be reviewed monthly by the VP, Infrastructure & Cloud.

JIT elevation shall be implemented via:
- CyberArk PSM for Secure Connect for Active Directory domain escalation.
- AWS IAM Identity Center for AWS Management Console and CLI access — temporary credential issuance, maximum session duration 1 hour.
- Azure Privileged Identity Management (“PIM”) for Azure and Microsoft 365 administrative roles — maximum activation duration of 1 hour, mandatory justification and ticketing reference.
- CyberArk AAM for application-level privileged, just-in-time credential delivery to containerized workloads.

### 4.4 Credential Lifecycle and Rotation

All managed privileged credentials shall be subject to automated, verifiable rotation via CyberArk CPM. Rotation intervals shall adhere to the following minimum schedule:

| Credential Type | Minimum Rotation Interval | Post-Use Rotation |
|-----------------|---------------------------|-------------------|
| Domain privileged accounts (Admin, EA, etc.) | Every 12 hours | Upon check-in |
| Local server administrator accounts | Every 24 hours | Upon check-in |
| Network device enable passwords | Every 72 hours | Upon session termination |
| A2A service account passwords | Every 30 days | Upon pipeline completion (triggered via API call to CPM) |
| Break-glass account passwords | Every 30 days (automated) + manual rotation upon any use | Upon any verified use |
| SSH private key passphrases | Every 90 days or upon key revocation | — |

CyberArk CPM shall log every rotation attempt — success or failure — to the centralized SIEM (`Sumo Logic`, Meridian log aggregation platform). Three consecutive rotation failures for any account shall trigger a P1 incident in the SOC ticketing system.

### 4.5 Session Recording and Audit

All privileged sessions brokered through CyberArk PSM shall be recorded — including full-motion video, indexed keystroke metadata, and typed command text. Recordings shall be cryptographically signed at generation and stored in an immutable, append-only repository within the SOC’s audit storage tier for a minimum retention period of one year.

### 4.6 Availability and Recovery

The CyberArk infrastructure — Vault, PSM, CPM, and PVWA (Password Vault Web Access) components — shall be deployed in a high-availability configuration spanning multiple AWS Availability Zones within the `us-east-1` region. The Meridian Incident Response Plan (SOP-IR-003) defines critical incident classification thresholds for PAM service degradation:

- P1 Incident: CyberArk Vault or PSM unavailability exceeding 15 minutes, preventing all privileged production access.
- P2 Incident: Degraded CPM rotation service (greater than 5% of accounts failing rotation within a single 2-hour window).

Recovery procedures for the CyberArk platform shall be documented in the runbooks under SOP-BCDR-002. The SOC Operations team shall maintain documented recovery procedures for the CyberArk platform, aligned with the Business Continuity plan. The specific recovery time objective and recovery point objective for the PAM infrastructure remain documented within the overall Meridian Business Continuity Plan (SOP-BCDR-002) and are exercised during the annual disaster recovery test.

### 4.7 Prohibited Practices

The following activities are explicitly prohibited and constitute a violation of this SOP subject to progressive disciplinary action per Meridian HR policy:
- Hard-coding privileged credentials in scripts, configuration files, source code repositories (including private repositories), or CI/CD pipeline definitions.
- Sharing privileged account credentials between individuals — each human privileged user shall have a uniquely identifiable, named account for auditing purposes. The only exception is the defined break-glass shared account model, which is monitored with compensating controls.
- Using privileged access for non-approved activities or data access not directly related to the approved business justification.
- Disabling or tampering with the CyberArk EPM agent, PSM recording function, or CPM rotation service.
- Storing privileged passwords in password managers (e.g., 1Password, LastPass) that are not the CyberArk Vault.

---

## 5. Detailed Procedures

### 5.1 Onboarding Privileged Accounts into CyberArk

This procedure applies when a new system, application, or account requiring privileged management is identified.

**Step 1: Discovery and Inventory Submission**
The System Owner or Application Owner shall identify all local administrator, service, root, and application accounts associated with the asset. This inventory shall be submitted via the `ITSM Privileged Access Onboarding` Service Catalog form (available at `meridian.service-now.com` → Information Security → PAM Operations). The form captures:
- Hostname/FQDN and IP address of the target system.
- Username convention (e.g., `svc_healthpay_db_reader`).
- Account type (Local Admin, Domain Account, Service Account, SSH Key).
- Business justification and the Meridian asset tag (CMDB reference).
- Designated primary and secondary owners (individuals or team distribution list).

**Step 2: Platform Verification (Infrastructure Engineering)**
Within two business days, the Infrastructure Engineering team (VP Okonkwo’s organization) validates that the target system is registered in the Configuration Management Database (“CMDB”) and that network connectivity exists (TCP/1858 for Vault protocol, TCP/443 for PVWA REST API) between the target and the CyberArk infrastructure security group.

**Step 3: Safe and Account Creation (PAM Administrators – SOC Team)**
Upon receipt of the validated ticket, a PAM Administrator creates the corresponding CyberArk Safe (logical container) and onboards the account via the PVWA Account Upload wizard. The CPM plugin (e.g., “Unix via SSH,” “Windows Domain Account,” “AWS Access Key”) is associated, establishing the automated rotation mechanism.

**Step 4: Verification**
The PAM Administrator manually triggers one immediate rotation via CPM to verify end-to-end password management functionality (change, verify, reconcile). Successful verification updates the ITSM ticket to “Resolved,” notifying the requester.

**Timeline SLA:** Full onboarding from ticket submission to verified rotation shall not exceed five business days for standard platforms. For non-standard or legacy platforms requiring custom CPM plugin development, the timeline extends to a negotiated delivery date per the VP, Infrastructure & Cloud, in consultation with the CISO.

### 5.2 Requesting Privileged Access (Standard JIT)

Personnel requiring temporary privileged elevation for a defined task (e.g., database schema migration, production log analysis, application configuration change) shall use the standard JIT request pathway.

**Step 1: Initiate Request in ServiceNow**
Navigate to `ServiceNow → Service Catalog → Privileged Access – JIT Request`. Complete all mandatory fields:

| Field | Description |
|-------|-------------|
| Requester Identity | Auto-populated via SSO. |
| Business Justification | A specific, auditable description. “Performing approved maintenance per Change CHG0042913, patching production web nodes.” Vague entries (“admin work,” “fix issue”) are rejected. |
| Change Record Reference | Mandatory for production access. Must link to an approved Change Request in ServiceNow per the Change Management SOP (SOP-ITSM-002). |
| Target System(s) | FQDN, AWS Account ID and Role Name, or Azure Resource Scope. |
| Access Duration Requested | Maximum 4 hours for standard requests. Exceeding 4 hours requires explicit justification and VP-level approval. |
| Privileged Actions Anticipated | Checkboxes indicating expected activity (e.g., `sudo shell`, `Windows admin share access`, `AWS console IAM changes`) to enable SOC to baseline session recording review. |

**Step 2: Manager Approval**
The ServiceNow workflow routes the request to the requester’s direct line manager for business justification approval. Manager approval confirms that the task is legitimate and within the employee’s role scope. SoD is enforced — the manager cannot be the requester themselves.

**Step 3: Technical Approval (System Owner)**
For production assets, a second approval gate is required — the designated System Owner or their delegate confirms that the requested scope and duration are appropriate for the impacted system.

**Step 4: Automated Provisioning**
Upon dual approval, the workflow triggers:
- **Active Directory:** Temporary addition to the appropriate privileged Active Directory group (e.g., `PRD-SQL-Admins-TEMP`). The group membership has a Time-To-Live (“TTL”) attribute of the approved duration. A scheduled task purges expired members every 15 minutes.
- **AWS:** CyberArk PSM-SC (Secure Connect) invokes AWS IAM Identity Center `CreateAccountAssignment` API, assigning the requested Permission Set to the user’s SSO identity for the specified duration, after which a scheduled Lambda function revokes it.
- **Azure:** CyberArk triggers Azure PIM “Activate” for the requested role, setting the `Expiration` to the approved duration.

**Step 5: Session Initiation**
The requester receives a ServiceNow notification with a PVWA connection link. Clicking the link establishes a PSM-brokered, fully recorded session to the target. The session is automatically terminated — and any temporary group memberships/role assignments revoked — at the approved duration expiration.

### 5.3 Requesting Privileged Access for A2A / Secrets (CyberArk AAM / Conjur)

Application-to-Application (“A2A”) or DevOps pipeline requests follow a distinct pathway designed for non-human identities.

**Step 1: Application Credential Request**
The Development Lead or DevOps Engineer submits an `ITSM → PAM Operations → Application Credential Onboarding` request. The request specifies:
- The application identity name (e.g., `pipeline-clinical-ai-deploy-prod`).
- The target resource for which the credential is needed (e.g., a Kubernetes cluster secret store, an AWS Secrets Manager path).
- The authentication method (e.g., client certificate, API key with specific IP source restriction).
- The required credential rotation frequency (minimum: 30 days; maximum: 7 days for CI/CD production deploy secrets).

**Step 2: Security Review**
The SOC Manager (or delegate) reviews the request to ensure:
- The application identity has the least privilege necessary for its function.
- The authentication source IP or VPC endpoint is explicitly defined and restricted.
- The credential is not intended for interactive human use masquerading as a service account.

**Step 3: Safe and Conjur/Credential Provider Configuration**
The PAM Administrator configures the credential in CyberArk (AAM Credential Provider or Conjur Enterprise) and provides the consuming application team with the SDK configuration snippet or REST API endpoint — never the plaintext credential itself. The application retrieves the credential at runtime from the PAM enclave.

### 5.4 Break-Glass Emergency Procedure

The break-glass procedure is authorized only when the primary identity provider (Entra ID / Okta) or the CyberArk PAS platform itself is completely unavailable, **AND** a critical operational event requires immediate privileged action (e.g., active data breach containment, restoring PAM availability, life-safety system intervention).

**Step 1: Declare Break-Glass Activation**
The authorized Break-Glass Account holder (a predefined list of senior engineers and the VP, Infrastructure & Cloud — the “Break-Glass Custodians”) physically retrieves the sealed break-glass envelope from the dual-control safe in the Meridian primary data center cage (Rack MC-03-42). The safe access requires both a key held by the SOC Manager (or delegate) and a combination held by the VP, Infrastructure & Cloud (or delegate) — enforcing physical dual-control.

**Step 2: Authenticate and Log**
The custodian breaks the seal, retrieves the credential set (separate, uniquely named Active Directory accounts, e.g., `meridian\bg-mokonkwo`), and authenticates to the PROD forest domain controller directly from the secure administrative workstation (“SAW”) located in the SOC NOC.
- The SAW is a hardened, air-gapped console that automatically initiates an out-of-band alert to the SIEM upon any interactive login.
- The custodian verbally confirms activation with the SOC Manager and the incident commander (as defined in SOP-IR-003).

**Step 3: Execute Authorized Actions**
The custodian performs the minimum actions necessary to restore service or contain the immediate threat. All actions are logged locally on the SAW and streamed via an independent cellular out-of-band logging channel to Sumo Logic.

**Step 4: Deactivation and Post-Incident Review**
Immediately upon restoration of normal privileged access pathways:
1. The CISO (Rachel Kim) — or in her absence, the Chief Technology Officer — is notified and provides written post-hoc approval within 24 hours via email to `cISO-approvals@meridian.com`.
2. The SOC Manager triggers an immediate CPM rotation for all activated break-glass accounts, generating new passwords.
3. The Physical Security team reseals the new break-glass envelopes and the dual-control safe.
4. The GRC Director (J. Reinhardt) conducts a mandatory break-glass usage review within 5 business days, assessing appropriateness and any policy gaps.

---

## 6. Controls and Safeguards

### 6.1 Preventative Technical Controls

| Control ID | Control Description | Implementation Mechanism |
|------------|---------------------|--------------------------|
| PAM-PREV-01 | All interactive privileged logins must be brokered through PSM. Direct RDP/SSH from user endpoints to production targets is blocked. | Palo Alto Networks firewall policy (Rule: `Block-PROD-Direct-Privileged-Access`) restricts TCP/3389 and TCP/22 to production VLANs. Only CyberArk PSM jump host IPs are permitted egress. |
| PAM-PREV-02 | Privileged credentials shall not be exposed in plaintext to end-user sessions. | PSM injects credentials directly into the target session; the credential plaintext is never rendered on the user’s endpoint clipboard or display. |
| PAM-PREV-03 | Workstation-based credential theft prevention. | CyberArk EPM agent deployed to all SAWs and all privileged user endpoints. EPM prevents LSASS memory reads, blocks Mimikatz-identified patterns via DLL injection prevention, and restricts local administrator rights elevation. |
| PAM-PREV-04 | Multi-Factor Authentication (“MFA”) for all privileged access pathways. | Okta MFA via Okta Verify push notification, enforced at the PVWA login and at AWS IAM Identity Center and Azure PIM activation gates. FIDO2/U2F hardware tokens are mandated for all Break-Glass Custodian Okta accounts. |
| PAM-PREV-05 | Code repository credential scanning. | GitHub Advanced Security secret scanning enabled across all Meridian GitHub Organization repositories (`meridianh`). Push protections block commits containing patterns matching CyberArk Conjur tokens, AWS IAM access keys, or Azure SAS tokens. |
| PAM-PREV-06 | AWS Organization Service Control Policy (“SCP”) denying the ability to disable CloudTrail or remove PAM IAM roles. | SCP applied at the Organization Root level: `"Effect": "Deny", "Action": ["cloudtrail:StopLogging", "cloudtrail:DeleteTrail", "iam:DetachRolePolicy" with condition for PAM-specific role ARNs]`. |

### 6.2 Detective Technical Controls

| Control ID | Control Description | Implementation Mechanism |
|------------|---------------------|--------------------------|
| PAM-DET-01 | Real-time alerting on anomalous privileged activity. | CyberArk Privileged Threat Analytics (“PTA”) integrated with Sumo Logic. PTA baselines normal privileged behavior and scores sessions — high-risk scores (e.g., a database admin executing `SELECT * FROM patients` during non-business hours) generate SOC alerts. |
| PAM-DET-02 | Session recording and audit indexing. | PSM records all sessions to WebM format with indexed text metadata (keystroke log). Recordings are stored in an immutable S3 bucket with Object Lock enabled. |
| PAM-DET-03 | PHI data access alerting during privileged sessions. | AWS CloudTrail S3 Data Event logging enabled on all S3 buckets tagged `classification=PHI` or `classification=PCI`. Any `s3:GetObject` from a privileged role on these buckets generates a near-real-time Sumo Logic alert to SOC. |
| PAM-DET-04 | Change management reconciliation with privileged activity. | ServiceNow scheduled job compares approved Change Requests with CyberArk PSM session logs every 4 hours. Privileged sessions initiated outside an approved Change window are flagged to the GRC queue for follow-up. |

### 6.3 Administrative Controls

- **Quarterly Access Reviews:** Every calendar quarter, the VP Infrastructure & Cloud and the GRC Director shall jointly review all standing privileged group memberships and CyberArk Safe members. Any entitlement not reaffirmed by the owner’s manager within 10 business days shall be automatically revoked.
- **Annual Penetration Test:** The PAM infrastructure, including the break-glass pathway and CyberArk PSM isolation properties, shall be included in the annual external penetration test conducted per SOP-ISEC-005.
- **Vendor Risk Assessment:** Any third-party vendor requiring privileged remote access must undergo a vendor risk assessment per SOP-VRM-001 before CyberArk secure vendor access credentials are provisioned.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The SOC Manager shall maintain a real-time operational dashboard (Sumo Logic App Dashboard, titled “Meridian PAM Health”) displaying the following metrics. The dashboard shall be displayed on the SOC NOC wall monitors.

| KPI | Target | Measurement Method |
|-----|--------|---------------------|
| **CPM Rotation Success Rate** | ≥ 99.5% (rolling 24h) | CyberArk `cpm_<safe>_<account>.log` aggregated to Sumo Logic; count `Success` vs. `Failure` outcomes for all managed accounts. |
| **Unmanaged Privileged Account Count** | ≤ 0 for Production; ≤ 5 for Dev-Sandbox (tracked exception) | Weekly ITSM reconciliation — CMDB privileged account inventory vs. CyberArk Vault accounts report. |
| **Break-Glass Activations** | Trend toward zero; each activation is a reviewable event irrespective of justification | Count of `EventID 4625 / 4624` on PROD Domain Controllers for break-glass account naming convention (`bg-*`). |
| **Privileged Session Recording Completeness** | 100% | PSM Health Check script verifies recording components every 15 minutes. |
| **JIT Access Request Fulfillment Latency** | Mean time from dual approval to provisioned access < 5 minutes | ServiceNow workflow execution logs. |

### 7.2 Reporting Cadence

| Report | Recipients | Frequency | Content |
|--------|------------|-----------|---------|
| PAM Operational Health Report | VP Infra & Cloud, SOC Manager | Weekly (automated email) | Rotation success/failure, PSM session volume, top 10 privileged account users, unanswered PTA high-risk alerts. |
| Privileged Access Entitlement Review Package | GRC Director, System Owners | Quarterly | Full export of all CyberArk Safe memberships, group memberships, and AWS/Azure PIM eligible assignments. Owners attest to correctness. |
| PAM Program State to Executive Risk Committee | CISO, CEO, CFO, General Counsel | Annually | Aggregate metrics, program maturity score against industry benchmarks, resourcing needs, exception trending. |
| SOC 2 Control Walkthrough Evidence | GRC Director, External Auditors | Annually (audit cycle) | Evidence package of PSM session sampling, rotation logs, access review attestations, incident tickets related to PAM. |

### 7.3 Monitoring and Alerting Configuration

The SOC Manager (P. Varma) shall maintain, within Sumo Logic, a log-derived alert framework for privileged access anomalies. The framework includes correlation between CyberArk Vault audit logs, PSM session initiation/termination records, and relevant Active Directory Security Event Log entries (EventIDs 4672, 4624, 4625, 4768). When specific conditions evaluated against these correlated logs meet predefined severity thresholds, the monitoring platform generates an incident notification in the SOC’s PagerDuty queue.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Process

Meridian recognizes that certain operational scenarios may temporarily require deviations from the prescriptive controls in this SOP. All exceptions must be formally documented, risk-assessed, and approved before the deviation occurs, except in documented break-glass emergency scenarios where post-hoc review suffices.

**Formal Exception Procedure:**

1. **Request Submission:** The individual or team lead seeking an exception submits an `ITSM → GRC → Policy Exception Request` form. The form must contain:
   - Specific SOP section(s) from which deviation is requested.
   - Specific technical reason why compliance is not feasible or would cause disproportionate operational harm.
   - Proposed compensating controls to mitigate the risk introduced by the exception.
   - Duration for which the exception is requested (maximum 90 days).

2. **GRC Risk Assessment:** The Director of GRC (J. Reinhardt) performs a formal risk assessment of the proposed exception within five business days, documenting the residual risk level (Low / Medium / High / Critical).

3. **Approval Authority:**
   - **Low / Medium Residual Risk, Duration ≤ 30 days:** Approval by VP, Infrastructure & Cloud.
   - **Medium Residual Risk, Duration > 30 days or any Production PHI/PCI exposure:** Joint approval by VP, Infrastructure & Cloud and CISO.
   - **High / Critical Residual Risk, or any exception involving the Clinical AI Platform model storage or the AWS Organization management account:** Approval by CISO only.

4. **Tracking:** All approved exceptions are registered in the GRC Exceptions Register (maintained in ServiceNow GRC module), with an automatic reminder to the exception owner 7 days before expiration. Expired exceptions without renewal requests trigger automatic remediation (revocation of the non-compliant access).

### 8.2 Escalation Pathways

| Scenario | First Responder | Escalation (if unresolved in threshold) | Threshold |
|----------|-----------------|----------------------------------------|-----------|
| CPM rotation failure (individual account) | PAM Administrator (SOC) | VP, Infra & Cloud | 2 hours |
| CPM rotation failure (mass, >10 accounts) | VP, Infra & Cloud | CISO | 1 hour |
| Suspected compromised privileged credential | SOC Manager | CISO, VP Infra, Incident Commander (SOP-IR-003) | Immediate (15 min) |
| PAM platform unavailability | VP, Infra & Cloud | CISO, CTO | 15 minutes |

---

## 9. Training Requirements

### 9.1 Mandatory Training

All personnel granted privileged access of any kind — including JIT elevation eligibility — shall complete the following mandatory training:

| Training Module | Delivery Method | Frequency | Audience |
|-----------------|-----------------|-----------|----------|
| **MER-PAM-101: Privileged Access Awareness** | Meridian LMS (Workday Learning), computer-based training | Annually | All users who have been granted any privileged access in the prior 12-month period |
| **CyberArk PVWA End-User Operation** | Hands-on lab session (virtual) | Once, before first privileged access grant; refresher available | All new privileged users |
| **Break-Glass Procedure Drill** | Tabletop exercise | Semi-annually | Break-Glass Custodians only |
| **PHI and Data Handling Refresher** | Meridian LMS (Workday Learning), computer-based training, referenced to SOP-CPL-002 | Annually | All users with access to systems hosting PHI |

### 9.2 Training Tracking and Compliance

The Meridian Learning Management System (“LMS”) — Workday Learning — shall track all PAM-related training assignments and completion status. Completion records shall be retained for a minimum of three years. The SOC Manager shall generate a monthly compliance report identifying any privileged user whose annual training is overdue. Access shall be suspended for any user whose annual training is more than 30 calendar days past due, until such training is completed. Quarterly, the SOC Manager provides a training compliance summary to the CISO. The GRC Director has audit oversight of the completeness and accuracy of the LMS privilege-to-training assignment mapping.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Title | Relationship |
|--------|-------|--------------|
| SOP-ISEC-004 | Identity and Access Management | Defines standard user lifecycle, provisioning, and deprovisioning upon which privileged account JIT relies. |
| SOP-IR-003 | Incident Response Plan | Governs the incident declaration process triggered by potential privileged account compromise or PAM platform unavailability. |
| SOP-BCDR-002 | Business Continuity and Disaster Recovery | Defines the PAM infrastructure recovery runbooks, RTO/RPO commitments, and annual DR test. |
| SOP-ITSM-002 | Change Management | Defines the Change Request process required as a prerequisite for production JIT privileged access. |
| SOP-CPL-002 | Data Classification and Handling | Defines PHI handling procedures and breach notification obligations which privileged access controls are designed to protect. |
| SOP-VRM-001 | Vendor Risk Management | Governs assessment of third-party vendors prior to granting privileged remote access. |
| SOP-ISEC-005 | Penetration Testing | Mandates annual external penetration testing, inclusive of PAM controls and break-glass pathways. |

### 10.2 External Standards and Frameworks

- **NIST Special Publication 800-53, Revision 5:** AC-2 (Account Management), AC-6 (Least Privilege), AC-17 (Remote Access), IA-5 (Authenticator Management), AU-12 (Audit Record Generation).
- **NIST Cybersecurity Framework v2.0:** PR.AA (Identity Management, Authentication, and Access Control), PR.AT (Awareness and Training), DE.CM (Continuous Monitoring).
- **HIPAA Security Rule (45 C.F.R. § 164.312):** § 164.312(a)(2)(i) — Unique User Identification; § 164.312(d) — Person or Entity Authentication; § 164.312(b) — Audit Controls.
- **SOC 2 Criteria (AICPA TSP Section 100, 2017):** CC6.1 (Logical and Physical Access Controls), CC6.2 (User Access Provisioning), CC6.3 (Access Review), CC7.2 (Monitoring of Deviations).

---

## 11. Revision History

| Version | Effective Date | Author | Summary of Changes |
|---------|----------------|--------|---------------------|
| 1.0 | 2023-01-17 | R. Kim | Initial publication. Established foundational PAM controls, CyberArk deployment scope, basic rotation schedule. Break-glass procedure documented for first time. |
| 1.1 | 2023-06-05 | P. Varma | Minor revision. Added Break-Glass Custodian semi-annual tabletop requirement. Clarified PSM recording retention as one year. Updated role titles post-reorganization. |
| 2.0 | 2024-11-12 | R. Kim, M. Okonkwo | Major revision. Introduced mandatory JIT access model for all production privileged access; deprecated standing privilege entirely except break-glass; added AWS IAM Identity Center and Azure PIM integration procedures; introduced mandatory GitHub Advanced Security secret scanning for all repositories; expanded CPM rotation schedule and added 3x failure → P1 incident trigger; added CyberArk EPM deployment requirement for SAWs. |
| 2.0 (Errata 1) | 2024-12-03 | R. Kim | Correction: Changed Break-Glass post-hoc approval timeline from 48 hours to 24 hours (correcting typographical error in Section 5.4 Step 4). No substantive policy change. |
| 2.1 | 2025-09-07 | R. Kim | Updated Section 7 (Monitoring, Metrics) with explicit Sumo Logic dashboard KPIs; updated Section 7.3 alert framework to reference PagerDuty integration; refined Exception Handling Section 8.1 to include maximum 90-day duration and explicit approval authorities based on residual risk level; updated Section 9 Training — clarified annual PAM user training requirement; updated Section 10 for revised SOP cross-references. No substantive change to technical privileged access controls themselves. |

---

**Document Classification: Internal**
**Warning:** This document contains Meridian Health Technologies, Inc. proprietary information. Unauthorized reproduction, distribution, or disclosure is strictly prohibited and may result in disciplinary action up to and including termination of employment, contract cancellation, and pursuit of applicable civil and criminal remedies.

---

**End of SOP-ISEC-019, Version 2.1**

---

## Appendix A: Meridian Problem Log and Work Log

### A.1 Problem and Decision Log (PAM-Specific)

This log captures recurring issues, design decisions, and lessons learned related to privileged access management at Meridian. It is maintained to prevent recurrence of previously identified problems and to inform future revisions of this SOP.

| Log ID | Date | Problem / Decision Description | Impact | Resolution / Decision | Recorded By |
|--------|------|-------------------------------|--------|----------------------|-------------|
| PAM-PL-001 | 2022-09-15 | Pre-PAM implementation: Local Administrator accounts on 450+ Windows servers all shared identical password stored in an encrypted but shared IT team KeePass database. Auditor flagged as SOC 2 CC6.1 deficiency. | Audit finding; manual rotation unmanageable. | Initiated CyberArk PAS procurement. Decision: CyberArk selected over HashiCorp Vault Enterprise for human privileged access due to session recording capabilities. Vault retained for A2A secrets. | R. Kim |
| PAM-PL-002 | 2023-03-22 | CPM rotation failures across 30% of Linux PROD hosts. Root cause: SSH `PasswordAuthentication` disabled on hardened AMIs; CPM attempted password rotation but target used pubkey auth exclusively. | Rotation KPIs missed for two consecutive weeks. | Documented decision: CPM rotated the SSH private key passphrase, not the `root` password directly. Updated AMI hardening baseline (DevOps ticket DEVOPS-2841) to ensure compatibility: target AMIs must support both key-based and password-based authentication on loopback for CPM verification step. | M. Okonkwo |
| PAM-PL-003 | 2023-08-11 | Break-Glass activation (first real usage): PAM Vault HA cluster failed over due to AWS Availability Zone networking partition. During 23-minute PSM outage, on-call DBA needed emergency access to production Oracle RAC to restart listener. Break-Glass procedure worked but post-hoc review found custodian did not verbally confirm with SOC Manager before activation. | Non-conformance with SOP 1.1, Section 5.4 Step 2 verbal confirmation requirement. | **Decision:** Clarified break-glass procedure to explicitly state verbal confirmation is mandatory *before* authentication. Revised SAW provisioning to include an on-screen SOP summary before any interactive session is launched. | R. Kim, J. Reinhardt |
| PAM-PL-004 | 2024-05-07 | Penetration test finding: An AWS IAM role (`ClinicalAI-SageMaker-Admin`) had attached policy allowing `iam:PassRole` to any role, effectively privilege escalation to full Organization administration. | Critical penetration test finding; immediate remediation required. | Immediate IAM policy scope-down. Root cause documented: role was created manually outside Terraform pipeline during a P1 incident and never remediated. Decision: All AWS IAM Role creation is now blocked via SCP except through approved Terraform Cloud pipelines. | M. Okonkwo, P. Varma |

### A.2 Key Architectural / Procedural Decisions Record

| Decision ID | Date | Decision | Rationale | Proponents |
|-------------|------|----------|-----------|------------|
| PAM-DEC-001 | 2024-06-18 | **JIT Access Model mandated for all production privileged access effective v2.0 (2024-11-12).** Standing privileged group memberships (except break-glass) eliminated. | Mitigation of lateral movement risk following initial access. Aligns with CyberArk best practices and NIST SP 800-53 AC-6(1). | R. Kim, M. Okonkwo |
| PAM-DEC-002 | 2024-06-18 | **Break-glass shared account model retained** but with compensating controls: physical dual-control safe, immediate post-hoc CISO approval, mandatory post-use rotation and GRC review. | Full individualization of break-glass accounts is theoretically ideal but operationally challenging for extreme disaster scenarios where named accounts may be unavailable (e.g., forest functional level issues). Risk accepted by CISO. | R. Kim (risk acceptance) |
| PAM-DEC-003 | 2024-08-12 | **PSM session recording retention period set at 1 year.** | Balance between forensic needs, SOC 2 audit evidence requirements, and storage cost (immutable S3 Object Lock tier). | P. Varma, J. Reinhardt |

### A.3 Work Log (Current Revision Cycle: v2.1)

| Date | Activity | Personnel | Notes |
|------|----------|-----------|-------|
| 2025-08-12 | Annual review cycle initiation | J. Reinhardt | Notified R. Kim of upcoming review obligation per SOP-ISEC-001 (Policy Management). |
| 2025-08-19 | Evidence collection for SOC 2 CC6.1-CC6.3 testing | P. Varma | Extracted Q2-Q3 PSM session sampling, rotation success logs, access review attestations. No control exceptions identified. |
| 2025-08-26 | Stakeholder review of draft v2.1 | R. Kim, M. Okonkwo, J. Reinhardt | Reviewed Section 7 KPI updates, Section 8 approval authority refinement, Section 9 training language. Okonkwo confirmed rotation schedules technically feasible. |
| 2025-09-02 | Final approval | R. Kim (Owner), Dr. S. Chen (Approver) | Approved via DocuSign envelope. |
| 2025-09-07 | Effective date; published to PolicyPortal | J. Reinhardt | Version 2.0 superseded; archived. |
| 2026-05-02 | Scheduled mid-cycle review | R. Kim | Reviewed for any emergent operational issues; no amendments required. Last reviewed date updated in YAML metadata. Next full review remains 2026-11-06. |

---