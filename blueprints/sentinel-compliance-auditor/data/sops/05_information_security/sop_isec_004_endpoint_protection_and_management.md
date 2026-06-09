---
sop_id: "SOP-ISEC-004"
title: "Endpoint Protection and Management"
business_unit: "Information Security"
version: "3.9"
effective_date: "2024-05-27"
last_reviewed: "2025-07-24"
next_review: "2026-01-28"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Endpoint Protection and Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for securing, managing, and monitoring all endpoint devices that access, process, store, or transmit Meridian Health Technologies, Inc. ("Meridian") data. The purpose is to ensure the confidentiality, integrity, and availability of protected health information (PHI), personally identifiable information (PII), proprietary algorithms, and financial data by implementing a defense-in-depth endpoint security architecture. This document defines the minimum security baseline, operational procedures, and governance mechanisms required to protect Meridian's distributed computing environment against evolving threat landscapes while maintaining compliance with applicable regulatory frameworks.

### 1.2 Scope

This SOP applies to all endpoints within the Meridian enterprise, regardless of ownership, operating system, physical location, or connectivity state:

**In-Scope Devices:**
- Corporate-issued laptops and desktops (Windows 11 Enterprise, macOS 14+ Sonoma) for all approximately 2,400 employees across Boston, London, Berlin, Singapore, and Toronto offices
- Virtual desktop infrastructure (VDI) instances hosted in AWS us-east-1 and eu-west-1 regions, accessed via thin clients or HTML5 browsers
- Developer workstations used by engineering teams for PyTorch, TensorFlow, and Kubeflow development pipelines
- Clinical AI workstations deployed in 340+ hospital and clinic environments, running FDA 510(k)-cleared and CE-marked diagnostic imaging applications
- Servers running on-premises at Meridian corporate facilities, including build servers, local file servers, and security appliances
- Mobile devices enrolled in Meridian's Mobile Device Management (MDM) platform with access to corporate email, Slack, Zoom, and Meridian SaaS Platform administrative interfaces
- Point-of-sale and payment processing terminals operated by HealthPay Financial Services (where applicable)
- Air-gapped research systems in the AI Safety Lab (Boston headquarters, Lab 4-B)
- Bring-Your-Own-Device (BYOD) endpoints accessing Meridian systems via Okta-verified browser sessions
- Third-party contractor and Business Associate endpoints when accessing Meridian resources remotely

**Out-of-Scope:**
- Patient-owned personal devices not enrolled in MDM
- IoT building management sensors isolated from the corporate network on dedicated VLANs (governed by SOP-PHY-007, Physical Security and Environmental Controls)
- Medical devices (e.g., MRI, CT scanners) that do not run general-purpose operating systems; these are managed under SOP-CLIN-011, Clinical Device Security

### 1.3 Applicability

Compliance with this SOP is mandatory for all Meridian employees, contractors, temporary workers, interns, and third-party service providers who access Meridian information systems from any endpoint device. Non-compliance shall be addressed per the Meridian Employee Handbook Section 12.3 and may result in disciplinary action up to and including termination of employment or contract, in addition to any civil or criminal penalties under applicable law.

---

## 2. Definitions and Acronyms

| Term | Definition |
|------|------------|
| **Advanced Persistent Threat (APT)** | A sophisticated, long-term cyber intrusion operation typically conducted by nation-state actors targeting Meridian's clinical AI intellectual property |
| **Anti-Malware** | Software designed to detect, quarantine, and remove malicious code, including viruses, worms, trojans, ransomware, spyware, and fileless malware |
| **Asset Inventory** | The centralized repository of all Meridian-managed endpoints, maintained in ServiceNow Configuration Management Database (CMDB) |
| **Bring-Your-Own-Device (BYOD)** | Personal devices used by employees to access Meridian corporate resources via Okta-verified browser sessions, subject to containerization controls |
| **Crown Jewel Endpoint** | A classification assigned to endpoints that store, process, or have privileged access to PHI, model weights for production clinical AI systems, or HealthPay payment processing infrastructure |
| **CrowdStrike Falcon** | Meridian's enterprise Endpoint Detection and Response (EDR) platform, deployed across all endpoints |
| **Data at Rest (DAR)** | Data stored persistently on endpoint storage media (SSD, HDD), protected via full-disk encryption |
| **Endpoint Detection and Response (EDR)** | Continuous monitoring, threat detection, investigation, and automated response capabilities integrated at the endpoint level |
| **Endpoint Encryption** | Full-disk encryption applied via Microsoft BitLocker (Windows) or Apple FileVault2 (macOS) with keys escrowed in HashiCorp Vault |
| **Endpoint Protection Platform (EPP)** | The integrated suite of preventative controls comprising anti-malware, host firewall, device control, and web reputation filtering |
| **Mean Time to Detect (MTTD)** | The average time between initial compromise and detection by Meridian's security operations tools, measured in minutes from SIEM correlation timestamp |
| **Mean Time to Remediate (MTTR)** | The average time from detection confirmation to full containment, eradication, and return to validated secure state |
| **Patch Criticality** | Classification schema mapping vulnerability severity (CVSS score) and exploitability to mandated remediation timelines |
| **Privileged Access Workstation (PAW)** | A hardened, single-purpose endpoint dedicated exclusively to administration of Tier 0 assets (Active Directory, HashiCorp Vault, AWS Organization root accounts) |
| **Tenable.io** | Meridian's enterprise vulnerability management platform used for continuous scanning of all corporate endpoints and servers |
| **Zero Trust Architecture (ZTA)** | Security model assuming breach state, requiring continuous verification of endpoint health and user identity before granting access to resources |

### 2.2 Acronyms

| Acronym | Full Text |
|---------|-----------|
| **AV** | Antivirus |
| **BAA** | Business Associate Agreement |
| **BYOD** | Bring-Your-Own-Device |
| **CIS** | Center for Internet Security |
| **CMDB** | Configuration Management Database |
| **CVSS** | Common Vulnerability Scoring System |
| **DLP** | Data Loss Prevention |
| **EDR** | Endpoint Detection and Response |
| **FDE** | Full-Disk Encryption |
| **HITL** | Human-in-the-Loop |
| **IOC** | Indicator of Compromise |
| **JAMF** | Jamf Pro (macOS management platform) |
| **MDM** | Mobile Device Management (Microsoft Intune for corporate endpoints; Jamf Pro for Apple devices) |
| **NIST** | National Institute of Standards and Technology |
| **PAW** | Privileged Access Workstation |
| **PHI** | Protected Health Information |
| **SIEM** | Security Information and Event Management (Splunk Enterprise Security) |
| **SCCM** | Microsoft System Center Configuration Manager (co-managed with Intune) |
| **SSO** | Single Sign-On |
| **USB** | Universal Serial Bus |
| **VDI** | Virtual Desktop Infrastructure (AWS WorkSpaces) |

---

## 3. Roles and Responsibilities

The following RACI (Responsible, Accountable, Consulted, Informed) matrix defines the roles and responsibilities for execution of endpoint protection controls.

| Activity / Control | CISO (Rachel Kim) | Director, InfoSec Ops (Maria Santos) | IT Operations (VP: James Okafor) | Endpoint Security Engineer (Lead: Priya Sharma) | SOC Analysts (24x7) | Meridian Employees (All) | Business Associates |
|---------------------|--------------------|--------------------------------------|----------------------------------|------------------------------------------------|----------------------|--------------------------|----------------------|
| **Policy Governance & Approval** | **A** | **R** | C | C | I | I | I |
| **Endpoint Hardening Standards (CIS Benchmarks)** | A | **R** | C | **R** | I | I | I |
| **EDR Agent Deployment & Health** | I | A | C | **R** | **R** (monitoring) | I | I (compliance verification) |
| **Vulnerability Scanning & Patch Prioritization** | I | A | **R** (execution) | **R** (scheduling) | C | I | I |
| **Critical Patch Deployment (0–72-hour SLA)** | A | **R** | **R** | C | I | C (notification) | C (notification) |
| **Endpoint Encryption Key Management** | A | **R** | C | **R** (administration) | I | I | I |
| **SOC - Endpoint Alert Triage & Investigation** | I | A | C | C | **R** | I | I |
| **SOC - High-Fidelity Alert Containment** | I | **R** (escalation point) | C | C | **R** | I | I |
| **Asset Inventory Accuracy (CMDB)** | I | **R** (audit) | **A** | **R** | C | I (reporting new devices) | **R** (reporting) |
| **Acceptable Use Policy Adherence** | I | I | C | I | I (monitoring) | **R** | **R** |
| **Lost/Stolen Device Reporting (within 4 hours)** | I | I | **A** (process owner) | C | I | **R** | **R** |
| **BAA Compliance Verification** | **A** | **R** | C | I | I | I | I |

### Named Role Responsibilities

**Rachel Kim, Chief Information Security Officer (CISO)**
- Executive owner of the Endpoint Protection Program; approves all policy exceptions over 90 days; has delegated authority to approve critical breach containment measures; reviews and signs quarterly endpoint security posture reports for the CEO and Board Audit Committee.

**Maria Santos, Director of Information Security Operations**
- Operational owner of this SOP; manages the SOC team responsible for 24/7 endpoint alert monitoring; approves exception requests up to 90 days; conducts monthly posture review with Endpoint Security Engineering Lead; coordinates annual tabletop exercises simulating ransomware attacks on clinical AI endpoints.

**James Okafor, Vice President of IT Operations**
- Accountable for the operational execution of patch management across all corporate Windows, macOS, and Linux endpoints; owns ServiceNow CMDB completeness metric; ensures IT Service Desk staff are trained on lost device triage and BitLocker/FileVault key recovery procedures.

**Priya Sharma, Lead Endpoint Security Engineer**
- Responsible for the technical architecture of CrowdStrike Falcon, Tenable.io, and Microsoft Intune; authors endpoint hardening Group Policy Objects (GPOs) and configuration profiles; leads the monthly Vulnerability Review Board meeting to prioritize remediation; maintains the golden image for Windows and macOS deployment.

**SOC Analysts (Tier 1–3, rotating 24x7 shifts, Boston and Singapore SOC locations)**
- Tier 1: Monitor CrowdStrike Falcon console and Splunk ES dashboard continuously; triage and acknowledge critical detections within 15 minutes; initiate pre-approved containment playbooks (host isolation).
- Tier 2: Investigate escalated detections; perform forensic artifact collection using Velociraptor; authorize manual remediation actions.
- Tier 3: Conduct advanced threat hunting; reverse engineer novel malware samples; develop custom IOCs and CrowdStrike prevention policies.

**All Meridian Employees**
- Shall safeguard Meridian-issued endpoints from theft, loss, or unauthorized access; shall report lost or stolen devices to the IT Service Desk (servicedesk@meridian.com or extension 4357) within 4 hours of discovery; shall not disable or tamper with EDR, encryption, or patching agents; shall complete annual Security Awareness Training.

**Business Associates (Contractors, Third-Party Providers)**
- When accessing Meridian resources from their own endpoints, must attest endpoint meets Minimum Security Baseline (Section 6.5) or use Meridian-provisioned VDI; must report security incidents involving Meridian data within 4 hours to security@meridian.com; must comply with applicable Business Associate Agreement terms.

---

## 4. Policy Statements

### 4.1 Endpoint Protection Platform

All Meridian-managed endpoints shall have the CrowdStrike Falcon agent installed, running, and reporting to the Meridian Falcon cloud console before being permitted to connect to the corporate network. The Falcon agent must operate in Prevention Mode (not Detection Only) with all prevention policy settings applied. Endpoints discovered without active EDR protection shall be automatically isolated from the network using Network Access Control (NAC) enforcement via Cisco ISE, and IT Operations must remediate the missing agent within 4 operational hours.

### 4.2 Vulnerability and Patch Management

Meridian shall maintain a continuous vulnerability management program across all endpoints. Vulnerabilities shall be classified according to CVSS v3.1 severity and threat intelligence context. The following remediation timelines are mandatory and measured from the moment a vulnerability is confirmed present by Tenable.io scan, or from the vendor patch release date (whichever is later):

| CVSS Score | Severity | Remediation SLA | Scope |
|------------|----------|-----------------|-------|
| 9.0–10.0 | Critical | **72 hours** | All endpoints; emergency change management authorized |
| 7.0–8.9 | High | **14 calendar days** | All endpoints |
| 4.0–6.9 | Medium | **30 calendar days** | All endpoints |
| 0.1–3.9 | Low | **90 calendar days** or next maintenance window | All endpoints |

For Crown Jewel Endpoints (clinical AI workstations in hospital environments, HealthPay payment terminals, developer workstations with access to production model weights), the Critical SLAs are reduced to **24 hours**, and High vulnerabilities shall be remediated within **7 calendar days**.

### 4.3 Endpoint Hardening

All corporate endpoint operating systems shall be deployed in a hardened configuration based on the Center for Internet Security (CIS) Benchmarks Level 1 profile for the respective OS (Windows 11 Enterprise, macOS 14 Sonoma). Deviations from the CIS Level 1 benchmark must be documented as a configuration exception, risk-rated by Information Security Operations, and approved by the Director of Information Security Operations. Hardening configurations shall be enforced via Group Policy (Windows domains), Microsoft Intune Configuration Profiles (cloud-joined Windows and BYOD containers), and Jamf Pro Configuration Profiles (macOS).

### 4.4 Encryption at Rest

Full-disk encryption (FDE) is required on all portable endpoint devices (laptops, tablets) and strongly recommended for all desktop workstations within Meridian facilities. The following encryption standards shall be enforced:
- **Windows:** Microsoft BitLocker, XTS-AES 256-bit encryption algorithm, with TPM + PIN protector (minimum 6-digit PIN).
- **macOS:** Apple FileVault 2, XTS-AES 128-bit with 256-bit key wrapping, enforced via Jamf Pro Configuration Profile. Recovery keys must be escrowed in Jamf Pro and HashiCorp Vault.
- **Linux (Developer Workstations):** LUKS2 with AES-256-XTS, key escrow via custom automation to HashiCorp Vault.

Encryption must be enabled and key escrow verified prior to the device being released to the employee. Any endpoint discovered without active FDE shall have network access restricted to the isolated remediation VLAN only. Exceptions for fixed-location desktops in physically secured Meridian facilities (access-controlled badge entry, 24/7 video surveillance) require Director of Information Security Operations approval.

### 4.5 Data Loss Prevention (DLP)

Endpoints classified as Crown Jewel shall have CrowdStrike Falcon Insight for DLP policies enforced to monitor and restrict:
- Copy of PHI datasets to removable media (USB mass storage class)
- Upload of files containing specific HIPAA Safe Harbor identifiers to non-approved web services
- Email exfiltration via non-corporate webmail portals from clinical workstations

DLP policy violation events shall generate a Medium severity alert within the SIEM and be investigated by Tier 2 SOC analysts within 4 hours.

### 4.6 Acceptable Use

Meridian endpoints are provided for legitimate business purposes. Employees shall not use Meridian endpoints to access, store, or transmit illegal content, malicious code, or to conduct unauthorized penetration testing. Personal use of corporate endpoints is permissible provided it does not interfere with security controls (e.g., personal browsing within isolated browser sessions is allowed; installing personal unapproved software is prohibited under application control policies).

---

## 5. Detailed Procedures

### 5.1 Endpoint Provisioning and Deployment

**5.1.1 Standard Corporate Endpoints (Windows/macOS)**

**Step 1: Hardware Procurement and Asset Tagging**
IT Operations receives hardware from approved vendor (Dell Direct, Apple Business Manager) and assigns a unique Meridian Asset Tag. Asset record is created in ServiceNow CMDB with fields: Asset Tag, Serial Number, Make, Model, Procurement Date, PO Number.

**Step 2: Operating System Imaging**
IT Endpoint Engineering applies the current Meridian Golden Image using Microsoft Deployment Toolkit (MDT) for Windows or via Automated Device Enrollment (ADE/formerly DEP) for macOS.

- **Windows Golden Image Base:** Windows 11 Enterprise 23H2, with pre-installed agents: CrowdStrike Falcon Sensor v7.x, Tenable Nessus Agent v10.x, Microsoft Intune client, ServiceNow Discovery Agent.
- **macOS Golden Image Base:** macOS 14 Sonoma, provisioned via Jamf Pro PreStage Enrollment. Pre-installed agents: CrowdStrike Falcon (macOS kernel extension approved via MDM PPPC payload), Jamf Pro agent, Tenable Nessus Agent.

**Step 3: Configuration Baseline Application**
During provisioning, the endpoint receives its assigned Configuration Profiles and Group Policies:
- CIS Level 1 hardening settings applied (password policies, screen lock timeout of 10 minutes, disabling unnecessary services, enabling Windows Defender Firewall / macOS Application Firewall).
- BitLocker (Windows) or FileVault (macOS) encryption policy enforced.
- LAPS (Local Administrator Password Solution) configured to randomize local admin password, stored in Active Directory attribute for Windows endpoints.
- Assigned user account created and added to local 'Users' group only (not local Administrators). Standard user privileges for daily operations; separate Privileged Access Management (PAM) via CyberArk for administrative tasks.

**Step 4: Encryption Key Escrow Verification**
Before releasing device to employee, IT Technician verifies:
- BitLocker status: `Manage-bde -status C:` reports Protection Status: "On", Encryption Method: "XTS-AES 256". Recovery key visible in Active Directory and replicated to HashiCorp Vault within 1 hour.
- FileVault status: `fdesetup status` reports "FileVault is On." Recovery Key escrowed in Jamf Pro inventory record, synced to HashiCorp Vault vault path: `secret/meridian/macos/fv-recovery/{serial}`.

**Step 5: User Handover and Verification**
Device released to employee. Employee authenticates via Okta MFA during initial Windows Hello for Business / macOS Touch ID enrollment. Upon first login, CrowdStrike and Tenable agents phone home to cloud consoles. SOC receives automated alert if any agent fails to report within 2 hours; IT Operations ticket created.

### 5.2 Endpoint Detection and Response (EDR) Operations

**5.2.1 Continuous Monitoring**

The Meridian Security Operations Center operates 24x7x365 with a follow-the-sun model between Boston (07:00–19:00 EST) and Singapore (19:00–07:00 EST). SOC Tier 1 Analysts actively monitor the CrowdStrike Falcon console and correlated Splunk Enterprise Security dashboards.

**Critical Detection Categories Requiring Immediate Response:**
- Malware/Ransomware Prevention Policy Violation (Prevention prevented execution)
- Suspicious process injection targeting LSASS.exe
- Credential dumping via Mimikatz or similar
- Lateral movement detection (PsExec, WMI, WinRM to Crown Jewel hosts)
- Known C2 (Command & Control) beaconing to adversary infrastructure
- Unauthorized BitLocker/FileVault suspension or decryption attempt

**5.2.2 Alert Triage (Tier 1)**

1.  **Acknowledge Alert:** Tier 1 Analyst acknowledges CrowdStrike detection within the Falcon console within **15 minutes** of the alert generating in the SIEM dashboard (measured by the time between Splunk index timestamp and console acknowledgement).
2.  **Initial Triage:**
    - Verify detection fidelity: Confirm that the detection is not a known false positive from Meridian's engineering tools (e.g., Visual Studio debugger invoking legitimate LSASS queries, flagged in Falcon tuning exceptions list).
    - Assess blast radius: Query Falcon for all other endpoints exhibiting the same IOC (hash, domain, IP) within the last 24 hours.
    - Determine asset criticality: Check the CMDB record to determine if affected endpoint is classified as Crown Jewel.
3.  **Containment (Automated where possible):**
    - If detection severity is Critical or High, and confidence is High (>90%), Tier 1 Analyst immediately invokes "Network Contain" action on affected endpoint(s) via Falcon console.
    - Contained host is isolated to a remediation VLAN segment with no access to production networks. Internet access is filtered to allow communication with CrowdStrike cloud and Microsoft patch repositories only.

**5.2.3 Incident Investigation (Tier 2 Escalation)**

1.  **Escalation:** Tier 1 Analyst escalates to Tier 2 SOC Lead within **30 minutes** of initial alert for all Critical/Severe detections.
2.  **Forensic Artifacts Acquisition:** Tier 2 Analyst uses CrowdStrike Falcon Real-Time Response (RTR) or Velociraptor to collect:
    - Running process list and associated command line arguments.
    - Recent network connections (netstat output).
    - Scheduled tasks and cron jobs.
    - Prefetch files (Windows) or Unified Logs (macOS).
    - Memory dump of suspicious process (if process still running) via Falcon CrowdStrike Memory Analysis.
3.  **Root Cause Analysis (RCA):** Determine initial access vector (phishing email link, exploited vulnerability, USB media, etc.).
4.  **Eradication and Recovery:**
    - Remove persistence mechanisms (registry run keys, LaunchDaemons, cron).
    - Quarantine and delete malicious files.
    - Reset compromised user credentials via Okta Admin forced password reset and revoke all active sessions.
    - If Crown Jewel or PHI data exposure suspected, notify Data Privacy Officer (DPO) and invoke SOP-LEG-002 (Data Breach Response).
5.  **Validation:** Run a full CrowdStrike on-demand scan and verify no further IOCs. Validate endpoint configuration against baseline hardening policies. Lift network containment only after validation complete and Tier 2 Lead approval.

### 5.3 Patch Management Operational Procedure

**5.3.1 Vulnerability Identification**

1.  **Continuous Scanning:** Tenable.io scanners perform authenticated vulnerability scans against all Meridian-managed IP ranges on a continuous basis (scans staggered across time zones, max scan window 12 hours per subnet).
2.  **Agent-Based Scanning:** Endpoints that are frequently off-network (traveling employees, field clinical workstations) report vulnerability data via Tenable Nessus Agent, beaconing to Tenable.io cloud.

**5.3.2 Patch Prioritization and Approval**

1.  **Monthly Vulnerability Review Board (VRB):** Chaired by Priya Sharma (Lead Endpoint Security Engineer), meets the **first Tuesday of each month, 10:00–11:30 AM EST**.
    - Members: Maria Santos (Dir. InfoSec Ops), James Okafor (VP IT Ops), Representative from Engineering, Representative from Clinical Informatics (for clinical workstation impact).
    - Agenda: Review Tenable Executive Summary for previous month; approve Critical/High patch exceptions; review SLA compliance metrics; approve upcoming patch deployment schedule.
2.  **Emergency Patch Process:** For Critical (CVSS 9.0+) actively exploited vulnerabilities (e.g., CISA Known Exploited Vulnerabilities Catalog additions), Priya Sharma may invoke emergency change management outside the monthly VRB.
    - Priya sends "Emergency Patch Advisory" email to `incident-response@meridian.com` with subject: "EMERGENCY PATCH - [CVE ID] - [CVSS Score]".
    - Within 24 hours, IT Operations packages and tests the patch against a representative sample (5 Crown Jewel clinical workstations in Boston HQ Lab).
    - After 4-hour soak period without critical application break, deployment is approved for all endpoints, targeting completion within the remaining 48 hours of the 72-hour SLA.

**5.3.3 Deployment Rings**

Meridian employs a ring-based deployment model to manage risk of patch-induced application incompatibility:

| Ring | Population | Deployment Offset | Purpose |
|------|------------|-------------------|---------|
| **Ring 0** | IT Operations Test Lab (20 VMs, 10 physical devices) | Immediately upon patch availability | Validate package integrity, reboot behaviour |
| **Ring 1** | Information Security Team (50 endpoints), IT Operations (40 endpoints) | Day 1 after Ring 0 success | Dogfooding; early detection of productivity tool impact |
| **Ring 2** | Non-critical departments (Marketing, Legal, HR) (300 endpoints) | Day 3–4 | Validate general business application compatibility |
| **Ring 3** | Crown Jewel endpoints - Clinical AI workstations (450 endpoints) | Day 5–6 (after clinical application team approval) | Final validation in production clinical environment |
| **Ring 4** | Remaining general population (1,700 endpoints) | Day 7–14 | Broad deployment |

For macOS, JAMF Patch Management policies follow an analogous phased rollout.

**5.3.4 Patch Deployment Execution**

- **Windows:** Deployed via Microsoft Intune Update Rings for Windows Update for Business, supplemented by SCCM for third-party application patches (Adobe, Google Chrome, Mozilla Firefox). SCCM deployments are targeted to device collections based on Ring membership.
- **macOS:** Managed Software Updates deployed via Jamf Pro Mass Actions, targeting Smart Groups (Ring 0, Ring 1, Ring 2–4).
- **Third-Party Library Patching (Developer Workstations):** Developers are responsible for updating programming language library dependencies (Python/PIP, Node.js/npm). CI/CD pipeline SAST scans (Snyk) will flag critical vulnerabilities in dependency files; Snyk alerts are directed to the owning development team via Jira auto-ticket. Overdue (>30 days High, >7 days Critical) library vulnerabilities will be escalated to the VP of Engineering.

**5.3.5 Validation and Reporting**

Tenable.io conducts a post-patch validation scan within 24 hours of the deployment deadline for each ring. Vulnerability closure rate is reported to the VRB and included in monthly CISO dashboards.

### 5.4 Endpoint Hardening Standards Implementation

Meridian leverages a configuration as code model using Git repository `meridian-it/infra/endpoint-configs` to manage group policies and configuration profiles. All changes require peer review pull request approved by a senior member of Endpoint Security Engineering.

Key hardening controls enforced:

- **Account Policies:**
    - Password history: 24 passwords remembered
    - Maximum password age: 90 days (exceptions for PAWs: 45 days)
    - Minimum password length: 14 characters
    - Account lockout threshold: 5 invalid attempts, lockout duration 30 minutes

- **Audit Policies (Windows: Advanced Audit Policy; macOS: OpenBSM via Jamf):**
    - Audit Logon Events: Success, Failure
    - Audit Account Management: Success, Failure
    - Audit Directory Service Access: Failure
    - Audit Object Access: Failure (PHI file access auditing enabled on Crown Jewel clinical workstations)

- **User Rights Assignment:**
    - `Access this computer from the network`: Administrators, Authenticated Users
    - `Allow log on locally`: Administrators, Users
    - `Deny log on through Remote Desktop Services`: Local Guest account

- **Security Options:**
    - `Interactive logon: Machine inactivity limit`: 900 seconds (15 minutes); screen saver password protected
    - `Microsoft network client: Digitally sign communications (always)`: Enabled
    - `User Account Control: Behavior of the elevation prompt for standard users`: Automatically deny elevation requests

### 5.5 Removable Media and Device Control

USB mass storage access is restricted based on endpoint classification and user role using CrowdStrike Falcon Device Control policies:

- **Non-Privileged Users (Standard Employees):** USB mass storage access set to **Block** by default. Exceptions for approved encrypted USB drives (Kingston IronKey D500S) are granted via ServiceNow request form "USB Exception Request," requiring manager and IT Security approval.
- **Privileged Users (System Administrators):** Allowed read-only access to USB mass storage for diagnostic purposes. Write operations trigger a Medium severity alert in SIEM.
- **Clinical AI Workstations (Hospital Environments):** All external media access disabled via group policy (USB ports physically disabled in BIOS where feasible, or USB block enforced via OS policy). Data transfer facilitated exclusively via Meridian SFTP or approved clinical data integration engine.

Any attempt to use a blocked USB device generates a security event logged to Splunk. Monthly report of USB exception requests and usage generated for Director of Information Security Operations.

### 5.6 Lost or Stolen Device Procedure

**Step 1: Immediate Notification**
Employee or contractor who discovers Meridian endpoint is lost or stolen must immediately (within 4 hours) notify IT Service Desk via phone (+1 617-555-0199) or email (servicedesk@meridian.com) and their direct manager.

**Step 2: Service Desk Triage**
Service Desk Agent creates a Priority 1 incident ticket in ServiceNow, categorizing as "Lost/Stolen Endpoint". Agent records:
- Asset tag
- Last known user
- Date/time of last known possession
- Circumstances of loss/theft
- Whether device was encrypted (verifies BitLocker/FileVault recovery key status in Vault)

**Step 3: SOC Containment Actions**
SOC Tier 1 Analyst is automatically notified. Within **30 minutes** of ticket creation, executes:
- Issue "host containment" command via CrowdStrike Falcon if endpoint is online.
- Issue remote wipe command via Intune (Windows) or Jamf Pro (macOS). Wipe command is queued and executes immediately upon endpoint next connecting to the internet.
- Revoke all Okta MFA device trust certificates associated with that device serial number.
- Rotate any corporate passwords or API tokens that may have been cached on the device (CyberArk automated credential rotation initiated for privileged accounts).

**Step 4: Post-Incident Review**
If device potentially contained PHI (Crown Jewel clinical workstation or mobile device with access to clinical systems via Epic Haiku/Canto):
- Director of Information Security Ops determines whether incident constitutes a breach under HIPAA Breach Notification Rule (45 CFR § 164.402). Considerations: Was PHI present? Was the device encrypted? Could PHI be readily accessed?
- Legal and Privacy Officer notified per SOP-LEG-002.

---

## 6. Controls and Safeguards

### 6.1 Preventative Controls

| Control | Implementation Detail | SOC 2 Mapping | HIPAA Mapping |
|---------|------------------------|---------------|---------------|
| **Endpoint Encryption (FDE)** | BitLocker XTS-AES 256 (Windows); FileVault 2 (macOS); enforced via GPO/Jamf | CC6.1 (Logical Access Security) | 45 CFR § 164.312(a)(2)(iv) – Encryption and Decryption (Addressable, Meridian implements as Required) |
| **Anti-Malware / Next-Gen AV** | CrowdStrike Falcon prevention policy: Machine Learning On, Sensor Anti-malware (Quarantine), Cloud Anti-malware | CC7.1 (Detection of Anomalies) | 45 CFR § 164.308(a)(5)(ii)(B) – Protection from Malicious Software |
| **Host-Based Firewall** | Windows Defender Firewall (Domain: Block Inbound, Allow Outbound); macOS Application Firewall (built-in, enabled) | CC6.1 | 45 CFR § 164.312(c)(1) – Integrity Controls |
| **Application Control** | Microsoft AppLocker (Windows: Publisher rules for approved apps, path rules); Jamf Pro Restricted Software (macOS) | CC6.1 | Not Directly Mapped; General Access Control |
| **USB Device Control** | CrowdStrike Falcon Device Control (Block except for IronKey approved encrypted drives) | CC6.1 | 45 CFR § 164.312(a)(2)(iii) – Access Control, § 164.310(d) – Device and Media Controls |
| **Secure Baseline Configuration** | CIS Level 1 Benchmarks enforced via Intune/GPO/Jamf | CC7.1, CC7.2 | 45 CFR § 164.308(a)(3)(ii)(A) – Risk Analysis (basis for hardening) |
| **Web Content Filtering** | Cisco Umbrella DNS-layer security enforced on Meridian endpoints; blocks access to known malicious domains, phishing sites, and categories per HR acceptable use policy | CC6.1 | Not Directly Mapped; general security measure |

### 6.2 Detective Controls

| Control | Implementation Detail | SOC 2 Mapping | HIPAA Mapping |
|---------|------------------------|---------------|---------------|
| **EDR Continuous Monitoring** | CrowdStrike Falcon Insight; all detection events > Medium severity flow to Splunk ES dashboard | CC7.1, CC7.2 (Detection of Anomalies, Monitoring) | 45 CFR § 164.308(a)(1)(ii)(D) – Information System Activity Review |
| **Vulnerability Scanning (Authenticated)** | Tenable.io continuous authenticated scans; Tenable Nessus Agent for roaming endpoints | CC7.1, CC7.2 | 45 CFR § 164.308(a)(8) – Evaluation |
| **File Integrity Monitoring (FIM)** | CrowdStrike Falcon FileVantage; monitoring changes to critical system files, registry keys on Crown Jewel workstations | CC7.1 | 45 CFR § 164.312(c)(1) – Integrity Controls |
| **SIEM Correlation (Splunk ES)** | Splunk ES ingests Windows Event Logs, Sysmon, CrowdStrike alerts, Okta auth logs, Cisco ISE auth logs; correlation searches for lateral movement, privilege escalation | CC7.1, CC7.3 | 45 CFR § 164.308(a)(1)(ii)(D) |
| **Asset Inventory** | ServiceNow CMDB populated by ServiceNow Discovery Agent (Windows/Linux), Jamf Inventory (macOS), Intune Inventory | CC7.1, CC3.2 | 45 CFR § 164.310(d) – Device and Media Controls (Accountability) |

### 6.3 Corrective Controls

| Control | Implementation Detail | SOC 2 Mapping |
|---------|------------------------|---------------|
| **Automated Host Containment** | CrowdStrike Falcon `contain` command blocks all network traffic except to Falcon cloud; initiated manually by SOC or automatically via Fusion workflow for known ransomware IOCs | CC7.3, CC7.4 |
| **Automated Incident Response Playbooks** | Splunk Phantom SOAR: Playbook "Ransomware Endpoint Containment" - upon Splunk ES correlation alert, automatically invokes Falcon containment, creates ServiceNow Priority 1 ticket, emails incident commander | CC7.3, CC7.5 |
| **Patch Deployment Automation** | SCCM/Intune Automatic Deployment Rules for Critical (CVSS 9+) Windows patches; Jamf Pro Patch Management for macOS | CC7.5 |
| **Remote Wipe** | Intune retire/wipe (Windows); Jamf Pro remote wipe (macOS) sent upon Lost/Stolen ticket creation | CC6.7 |

### 6.4 SOC 2 Detailed Controls Mapping

This SOP directly addresses Trust Services Criteria (TSC) 2017 (with 2022 updates) for the Security category:

- **CC6.1 Logical and Physical Access Controls:**
    - FDE ensures logical access to data at rest is prevented without valid credentials (TPM+PIN or FileVault with SecureToken).
    - AppLocker/Application Control restricts execution to authorized software only, preventing unauthorized code from accessing PHI.
    - USB Device Control prevents mass exfiltration of data to removable media without approved, encrypted device and audit trail.

- **CC7.1, CC7.2 System Operations (Detection & Monitoring):**
    - CrowdStrike EDR, Tenable vulnerability scanning, Cisco Umbrella, and Splunk SIEM provide continuous monitoring for security anomalies across the endpoint estate.
    - SOC 24x7 operations with defined SLA (15-minute alert acknowledgment) ensures deviations are promptly identified.

- **CC7.3, CC7.4, CC7.5 Incident Response and Remediation:**
    - Written procedures in Section 5.2 and 5.6 ensure consistent response to security incidents and lost devices.
    - Ring-based patch management (Section 5.3) ensures timely remediation of vulnerabilities, minimizing the window of exposure. SLA compliance is monitored monthly.

### 6.5 Business Associate Endpoint Compliance

Business Associates who access Meridian systems from their own endpoints (non-Meridian-managed) are subject to the terms of their Business Associate Agreement (BAA). The BAA obligates the Business Associate to maintain an equivalent endpoint security posture, including:
- Endpoint encryption at rest (FDE or equivalent).
- Current anti-malware protection.
- Prompt patching of operating systems and applications.

Meridian provides access to resources via Okta-verified browser sessions (for web-based applications) or Meridian-provisioned AWS WorkSpaces VDI instances (for thick-client or administrative access). The VDI provides a Meridian-managed, compliant endpoint environment that isolates any potential compromise on the Business Associate's native endpoint. Workforce training on the secure use of these VDI environments is provided to Business Associates upon onboarding and is included in Meridian's annual Security Awareness Training module.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following KPIs are continuously measured and reported to gauge the effectiveness of endpoint protection controls.

| KPI | Target | Measurement Method | Reporting Frequency |
|-----|--------|--------------------|---------------------|
| **EDR Agent Coverage** | 99.5% of all managed endpoints reporting active | CrowdStrike Falcon console → Splunk → PowerBI | Weekly dashboard; Monthly CISO report |
| **FDE Compliance** | 100% of portable endpoints; >95% of desktops | SCCM/Intune BitLocker report + Jamf Pro FileVault report | Weekly |
| **Critical Vulnerability (CVSS 9+) Remediation SLA** | 95% remediated within 72 hours | Tenable.io → PowerBI (SLA clock: detection time to closure time) | Weekly; Exception report at VRB |
| **High Vulnerability (CVSS 7-8.9) Remediation SLA** | 90% remediated within 14 days | Tenable.io → PowerBI | Monthly |
| **SOC Alert Mean Time to Acknowledge (MTTA)** | < 15 minutes for Critical/Severe alerts | Splunk (`index=falcon` earliest=-1h latest=now) | Weekly SOC team review; Monthly CISO report |
| **SOC Alert Mean Time to Contain (MTTC)** | < 30 minutes from alert acknowledgement | Splunk + CrowdStrike audit log | Monthly |
| **Patch Deployment Success Rate** | >98% of targeted endpoints successfully installed within deadline | SCCM/Microsoft Intune/Jamf reporting | Per patch cycle; Monthly CISO report |
| **Lost/Stolen Device Notification Time** | < 4 hours from discovery | ServiceNow ticket creation timestamp vs. employee reported timestamp | Quarterly trend report |
| **CMDB Accuracy** | >98% of active endpoints in CMDB match EDR console within 24 hours | Automated reconciliation script: CrowdStrike API ↔ ServiceNow CMDB | Weekly reconciliation, monthly audit reported to VP IT Ops |

### 7.2 Reporting Cadence

- **Daily:** SOC Shift Report, detailing all critical and high EDR detections triaged, containment actions, and any endpoint hygiene issues (agents down, FDE disabled alerts).
- **Weekly:** Endpoint Security Posture Dashboard (PowerBI) shared with Maria Santos, James Okafor. Review of SLA misses, current vulnerability trending.
- **Monthly:** CISO Endpoint Security Report, incorporating KPI dashboards, SLA adherence trends, incident summary, patch cycle completion reports. This report is included in the materials for the quarterly Audit Committee meeting.
- **Quarterly:** Board-level Executive Summary prepared by Rachel Kim summarizing endpoint risk posture against the evolving threat landscape.

### 7.3 Security Controls Auditing

To fulfill SOC 2 monitoring requirements, a quarterly endpoint security controls audit is performed by the GRC team (or an independent internal audit function). The audit verifies:
- A random sample of 50 endpoints is tested to confirm: CrowdStrike agent operational and in Prevention mode, BitLocker/FileVault enabled per policy, local firewall enabled, CIS baseline deviation documentation exists for any exceptions.
- Review of patch management records for the quarter: Verify VRB meeting minutes exist, verify Critical patch SLA was met for relevant CVEs.
- Review lost/stolen device tickets: Verify containment actions (wipe, revocation) were executed within defined timeline.
- Review exception register: Confirm all active exceptions are still justified and approved.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

Deviations from the requirements of this SOP may be necessary for specific business or technical scenarios (e.g., legacy clinical workstation connected to an MRI scanner that cannot run CrowdStrike due to vendor certification requirements). All exceptions must be formally documented, risk-assessed, and approved via ServiceNow "Security Exception Request" catalog item.

**Required Information in Request:**
1.  **Requestor Name & Department:** Individual requesting the exception and cost center.
2.  **Affected Asset(s):** Hostname(s), IP address(es), asset tag(s).
3.  **SOP Section Deviation:** Specific control requirement for which exception is sought.
4.  **Business Justification:** Detailed explanation of why the control cannot be implemented and the business impact of non-compliance.
5.  **Compensating Controls:** Detailed description of alternative controls implemented to reduce risk to an acceptable level (e.g., network segmentation, physical isolation, enhanced manual monitoring).
6.  **Duration:** Proposed start and end date. Temporary exceptions > 90 days must have VP-level sponsor.

### 8.2 Approval Authority

| Risk Level | Criteria | Approver | Max Duration |
|------------|----------|----------|--------------|
| **Low** | Compensating controls demonstrably equivalent; no PHI exposure | Maria Santos, Director of InfoSec Ops | 12 months |
| **Medium** | PHI present but compensating controls reduce risk to Low | Maria Santos + Data Privacy Officer (DPO) | 6 months |
| **High** | PHI present on unencrypted device; or Crown Jewel without EDR | Rachel Kim, CISO | 90 days |
| **Critical** | Any exception requested for FDA-validated clinical system | Rachel Kim, CISO + VP of Clinical Informatics + VP of Regulatory Affairs | Per validation lifecycle |

Approved exceptions are logged in the ServiceNow Exception Register. A dashboard of all active exceptions is reviewed at each monthly Vulnerability Review Board meeting. Expired exceptions that have not been renewed are automatically flagged as "Non-Compliant" and IT Operations must remediate within 30 days.

### 8.3 Escalation Procedure for SLA Breaches

If a Critical or High vulnerability SLA is at risk of breach:
1.  **24 hours before SLA deadline:** Priya Sharma (Lead Endpoint Security Engineer) sends email notification to Maria Santos and James Okafor.
2.  **SLA deadline breach:** Maria Santos escalates to Rachel Kim (CISO) and the VP of IT Operations. The affected endpoint(s) shall be quarantined (Section 5.2.2 containment procedures applied) until remediation can be verified, unless a risk-based decision to defer is authorized by Rachel Kim. SLA breach is recorded in the CISO monthly report.

---

## 9. Training Requirements

### 9.1 Roles and Training Assignment

All Meridian workforce members who interact with corporate endpoints must complete relevant security training. Training is assigned based on job function and access privilege.

| Role | Required Training Modules | Frequency |
|------|---------------------------|----------|
| **All Meridian Employees** | General Security Awareness Training (via KnowBe4 platform), including: Acceptable Use Policy review, Phishing Awareness, Reporting Security Incidents, Lost/Stolen Device procedure | Annual |
| **IT Service Desk Agents** | Endpoint Security Fundamentals (BitLocker/FileVault recovery, lost device triage procedure). Hands-on lab exercise. | Annual |
| **IT Endpoint Engineering (Windows, macOS administrators)** | Advanced Endpoint Hardening Workshop (CIS Benchmarks, GPO/Intune authoring, Falcon policy management). | On hire; Annual refresher |
| **SOC Analysts (All Tiers)** | CrowdStrike Falcon incident response drills; Splunk ES alert triage exercises; Monthly purple team exercises (joint with Red Team). | Monthly tabletop; Quarterly live-fire |
| **Clinical Informatics & Field Engineers** | Clinical Endpoint Security; procedures for safe connection of clinical workstations to hospital networks; Physical security of endpoints. | On hire; Annual refresher |
| **Developers** | Secure Coding Practices (OWASP Top 10); secrets management; dependency patch management (Snyk usage). | Annual |
| **Business Associates** | Meridian Security Awareness for Business Associates module (via Meridian LMS), covering: Acceptable use of Meridian systems, reporting incidents, endpoint hygiene for non-Meridian devices accessing Meridian VDI. | Annual |

### 9.2 Training Tracking and Compliance

Completion of training is tracked via the KnowBe4 Learner Management System (LMS), with automated reminders at 15, 7, and 1 day before annual due date. Managers receive monthly compliance reports for their teams. Employees who fail to complete required training by their due date will have their Okta SSO access to non-essential systems temporarily suspended until training is completed, per Human Resources policy.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| SOP-ISEC-001 | Information Security Policy Framework | Overarching policy |
| SOP-ISEC-002 | Access Control and Identity Management | Okta MFA, privileged access provisioning |
| SOP-ISEC-003 | Vulnerability Management Program | Tenable scanning standards, broader vulnerability governance |
| SOP-ISEC-005 | Network Security and Segmentation | Firewall rules, NAC enforcement for endpoints |
| SOP-ISEC-009 | Incident Response and Breach Notification | Breach notification timelines triggered by lost/stolen PHI endpoints |
| SOP-ISEC-012 | Cryptography and Key Management | HashiCorp Vault usage, BitLocker/FileVault key lifecycle |
| SOP-CLIN-011 | Clinical Device Security | Specialized security for medical devices (outside this SOP scope) |
| SOP-LEG-002 | Data Breach Response and PHI Notification | Legal notification requirements for PHI exposure from endpoint loss |
| SOP-VM-022 | Vendor Offboarding and Contract Termination | Procedures for reclaiming endpoints from departed BA users |
| SOP-PHY-007 | Physical Security and Environmental Controls | Physical access controls for endpoints in Meridian facilities |

### 10.2 External Standards and Regulatory References

- **NIST Special Publication 800-53 Rev 5:** Security and Privacy Controls for Information Systems and Organizations (specifically control families: AC, CM, MP, RA, SC, SI).
- **NIST Special Publication 800-53B:** Control Baselines for Information Systems and Organizations (Moderate baseline applicable to Meridian).
- **Center for Internet Security (CIS) Benchmarks:** CIS Microsoft Windows 11 Enterprise Benchmark v3.0.0; CIS Apple macOS 14.0 Sonoma Benchmark v1.0.0. Level 1 profile referenced.
- **SOC 2 TSC 2017 (with 2022 updates):** Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (Security category).
- **HIPAA Security Rule (45 CFR Part 160 and Subparts A and C of Part 164):** Administrative, Physical, and Technical Safeguards for Electronic Protected Health Information.

### 10.3 Meridian Business Associate Agreements

All Business Associates engaged by Meridian who create, receive, maintain, or transmit electronic PHI on behalf of Meridian are contracted under a Meridian standard Business Associate Agreement. The BAA template includes clauses requiring the Business Associate to:
- Implement administrative, physical, and technical safeguards that reasonably and appropriately protect the confidentiality, integrity, and availability of ePHI.
- Ensure that any agent, including a subcontractor, to whom it provides ePHI agrees to the same restrictions and conditions.
- Report any security incident involving Meridian data within 24 hours.
- Cooperate with Meridian to terminate access to Meridian systems promptly upon contract conclusion.

Business Associates using their own endpoints to access Meridian resources are expected to maintain endpoint security standards equivalent to those described in this SOP for non-Meridian-managed devices. Evidence of compliance may be requested during a security assessment review.

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | 2019-03-12 | Rachel Kim | Initial publication. Established foundational endpoint protection, anti-malware (Symantec Endpoint Protection), basic patch management |
| 1.5 | 2020-01-15 | Rachel Kim | Transitioned from Symantec to CrowdStrike Falcon; introduced FDE requirement via BitLocker/FileVault; defined initial 30-day patching SLA |
| 2.1 | 2021-06-10 | Maria Santos | Added ring-based deployment model for patches (post-SolarWinds lessons learned); expanded DLP section; introduced SOC 24x7 follow-the-sun model |
| 3.0 | 2023-09-22 | Maria Santos | Major revision: Full SOC 2 TSC mapping; migration to Intune co-management; addition of Apple Silicon (M3) support; increased Critical SLA to 72 hours; introduced Tenable.io continuous scanning; defined Crown Jewel endpoint classification for clinical AI workstations post-FDA clearance |
| 3.5 | 2024-02-18 | Priya Sharma | Technical update: Added LUKS2 specifications for Linux developer workstations; refined AppLocker policy exceptions for Visual Studio development; updated CIS benchmark version references |
| 3.9 | 2024-05-27 | Rachel Kim | Current version: Comprehensive update to RACI matrix for new clinical informatics roles; incorporated CE marking under EU MDR for clinical endpoints; enhanced Business Associate endpoint compliance section; adjusted FDE desktop exception criteria; final version approved by Dr. Sarah Chen, CEO |

---

**END OF DOCUMENT**

© 2024 Meridian Health Technologies, Inc. All rights reserved. This document contains proprietary and confidential information. Unauthorized reproduction or distribution is prohibited.