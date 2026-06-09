---
sop_id: "SOP-HR-006"
title: "Remote Work and BYOD Policy"
business_unit: "Human Resources"
version: "5.4"
effective_date: "2025-04-17"
last_reviewed: "2026-05-26"
next_review: "2026-11-22"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Remote Work and BYOD Policy

## 1. Purpose and Scope

### 1.1 Purpose
The purpose of this Standard Operating Procedure (SOP) is to establish a unified, risk-based framework governing remote work arrangements and the use of personally owned devices (Bring Your Own Device, or BYOD) to access Meridian Health Technologies, Inc. ("Meridian") information systems and data assets. This document operationalizes Meridian's commitment to securing Protected Health Information (PHI), Personally Identifiable Information (PII), and proprietary algorithmic intellectual property across all business lines—Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and Meridian SaaS Platform—irrespective of the end-user's physical location or device ownership.

### 1.2 Scope
This SOP applies to all Meridian employees, independent contractors, temporary workers, interns, and third-party vendors (collectively, "Personnel") who access, process, transmit, or store Meridian data from a non-corporate office environment or using a personally owned device. The scope is bounded by the following applicability matrix:

| Personnel Category | Remote Work Provision | BYOD Provision | Governing Addendum |
| :--- | :---: | :---: | :--- |
| Full-Time Employees (US, Canada) | Full Applicability | Full Applicability | Appendix A: Acceptable Use |
| Full-Time Employees (EU/EEA) | Full Applicability | Full Applicability | Appendix B: GDPR Works Council Agreement |
| Full-Time Employees (Singapore) | Full Applicability | Full Applicability | Standard Employment Contract Addendum |
| Contractors (< 90 days) | Applicable | Prohibited (Meridian-issued thin client required) | Appendix C: Contractor Security Addendum |
| Third-Party Vendors | Site-specific VPN only | Strictly Prohibited | SOP-SEC-012: Vendor Risk Management |
| Clinical Personnel (Radiology, Pathology) | Conditional (FDA-cleared workstation only) | Strictly Prohibited | SOP-CLIN-004: Clinical Imaging Workstation Standards |

### 1.3 Out of Scope
Explicitly excluded from this SOP:
- Accessing systems via a Meridian-managed device located in a Meridian corporate office (see SOP-IT-001: Office Network Access Control).
- Devices used solely for Multi-Factor Authentication (MFA) push notifications, unless the MFA app container is used to access Meridian email (then BYOD Section 5.4 applies).
- Paper records (see SOP-REC-003: Physical Records Management).

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **BYOD** (Bring Your Own Device) | A personally owned laptop, tablet, smartphone, or other computing device used to access Meridian Systems and Data. |
| **MTD** (Mobile Threat Detection) | Software deployed on endpoints to detect malicious applications, network attacks, and OS-level compromise (Meridian utilizes Lookout MTD). |
| **MAM** (Mobile Application Management) | The policy layer controlling corporate data within specific applications (Meridian utilizes Microsoft Intune MAM without device enrollment). |
| **MDP** (Managed Device Profile) | A corporate-controlled, device-level configuration profile (applicable only to Meridian-owned devices). BYOD devices use MAM exclusively, not MDP. |
| **PHI** | Protected Health Information, as defined by the HIPAA Privacy Rule (45 CFR § 160.103). |
| **ePHI** | Electronic Protected Health Information, as defined by HIPAA Security Rule (45 CFR § 164.304). |
| **Full-Tunnel VPN** | Virtual Private Network configuration routing 100% of device traffic through a Meridian security stack (Zscaler Internet Access). Required for BYOD workstations. |
| **Split-Tunnel VPN** | VPN configuration routing only Meridian-bound traffic through the corporate gateway. Strictly Prohibited for remote work. |
| **DSAR** | Data Subject Access Request. A formal request from an individual to exercise rights under GDPR or applicable state privacy laws. |
| **IRM** | Information Rights Management. Encryption technology (Microsoft Purview) that persists with data irrespective of its location. |
| **VDI** | Virtual Desktop Infrastructure. A virtualized, server-based desktop environment (Citrix Workspace). The mandated access method for BYOD workstations handling ePHI. |

---

## 3. Roles and Responsibilities

The following RACI matrix assigns accountability for key process outcomes. Roles are defined by job function; delegations of authority must be recorded via ServiceNow task closure.

| Activity / Decision | Chief HR Officer (J. Walsh) | Chief Information Security Officer (A. Vance) | Director of IT Operations (P. Chen) | Data Protection Officer (L. Muller) | People Manager | Personnel (End-User) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Policy Approval & Exception Sign-off | **A** | **R** | C | C | I | I |
| BYOD Eligibility Determination | I | **A** | **R** | C | I | I |
| Remote Work Agreement Execution | **A** | C | I | I | **R** | **R** |
| MTD/MAM Compliance Status Review | I | **A** | **R** | I | I (Dashboard) | I |
| HIPAA Security Incident Declaration | I | **A** | **R** | **R** | I | **R** |
| Data Subject Consent Verification | I | I | **R** | **A** | I | I |
| Non-Compliance Disciplinary Action | **A** | C | I | I | **R** | I |
| Quarterly VPN Access Review | I | **A** | **R** | I | I | I |

**Key:**
- **R:** Responsible (executes the task)
- **A:** Accountable (approves the outcome, ultimate ownership)
- **C:** Consulted (two-way communication required before execution)
- **I:** Informed (one-way communication after decision)

---

## 4. Policy Statements

Meridian is committed to protecting the confidentiality, integrity, and availability (CIA) of all data assets while supporting a flexible, productive, and secure remote work environment. The following statements constitute non-negotiable control objectives. Derivation from these objectives requires a formal, documented exception as defined in Section 9.

1.  **Zero-Trust Network Access**: Implicit trust is never granted based on network location (corporate or public). Access to all Meridian systems requires continuous verification of user identity and device health posture. This aligns with SOC 2 CC6.1 and CC6.2.

2.  **Data Residency**: ePHI and PII pertaining to EU data subjects must remain at rest within the approved Azure EU West (Amsterdam) region. Remote workstations accessing this data must not cache, store, or replicate data outside the approved tenant boundary (aligned with GDPR Art. 44-49).

3.  **Least Privilege Access**: Remote access rights are provisioned based strictly on business need-to-know, reviewed quarterly.

4.  **Prohibition of Unmanaged Endpoints**: Personnel may not access Meridian systems rated "High Sensitivity" (per the Data Classification Policy, SOP-SEC-003) from a device that is not enrolled in MTD and does not meet minimum OS patch-level compliance.

5.  **Physical Security Obligation**: Personnel working remotely must ensure that data displayed on screens is not visible to unauthorized individuals (a.k.a. "Shoulder Surfing Prevention"). Working with ePHI in public spaces (cafes, airport lounges) is strictly prohibited and constitutes a reportable security incident. (HIPAA 45 CFR § 164.310(c) Workstation Use).

6.  **Right to Disconnect (EEA Only)**: For employees within the European Economic Area, adherence to the EU Working Time Directive is maintained. System access logging is used to monitor excessive out-of-hours activity to prevent burnout, not to penalize flexibility. Managers are prohibited from implicitly requiring connectivity outside of local standard business hours.

---

## 5. Detailed Procedures

### 5.1 Remote Work Eligibility and Enrollment

This process transforms a standard employee profile into a "Remote Ready" profile with appropriate security group memberships in Azure AD.

**Step 1: Initiation (Manager & Employee)**
- The People Manager initiates the "Remote Work Agreement" (RWA) via the ServiceNow HR Catalog (Form ID: HR-RWA-001).
- The Employee receives an automated DocuSign envelope containing:
    - The Remote Work and BYOD Policy Acknowledgment (Appendix A).
    - The Physical Workspace Self-Assessment Checklist (Appendix D).
    - IT Hardware Allocation Request (if applicable).

**Step 2: Workspace Assessment (Employee)**
- The Employee completes the Physical Workspace Self-Assessment Checklist within 5 business days of receiving the DocuSign envelope.
- The Checklist records: home internet speed test results (minimum 25 Mbps download / 5 Mbps upload required), physical security controls (locking door, privacy screen), and ergonomic setup.
- **Trigger**: If the employee indicates an inability to meet physical security standards (e.g., shared housing without a private lockable room), the RWA is automatically paused and routed to the CISO for a risk acceptance review.

**Step 3: IT Provisioning (IT Operations)**
- Upon "Completed" status of the RWA in DocuSign, a workflow triggers in Azure AD.
- The Employee's account is added to the `SG-REMOTE-ACCESS-APPROVED` security group.
- Standard software packages (Zscaler Client Connector, Microsoft 365 Apps for Enterprise, CrowdStrike Falcon Sensor) are pushed to eligible corporate devices.
- For BYOD users, the MyApps portal configuration is updated to surface the Citrix Workspace download and Intune Company Portal enrollment links.

### 5.2 BYOD Enrollment (Standard Tier - No Device Control)

Meridian utilizes a Mobile Application Management (MAM) architecture for BYOD. This ensures corporate data resides within an encrypted container on the personal device without Meridian IT administrators having visibility or control over personal photos, apps, or browser history.

**Step 1: Platform Validation**
- User navigates to `https://portal.manage.microsoft.com` from their personal device.
- The Intune platform performs a client-side check:
    - **iOS/iPadOS**: Minimum version 15.0.
    - **Android**: Minimum Android 12.0. Device must be Google Play Protect certified.
    - **macOS/Windows**: OS must be under mainstream vendor support (current or N-1 version).

**Step 2: MAM Enrollment (App Protection Policy)**
- User authenticates to Company Portal using Azure AD credentials with Multi-Factor Authentication (MFA).
- The Meridian "BYOD Standard App Protection Policy" is assigned.
- The user is prompted to install the following MAM-protected applications from the respective official store (`App Store` or `Google Play Store`):
    - **Microsoft Outlook**: Corporate Email and Calendar.
    - **Microsoft Teams**: Corporate Messaging and Collaboration.
    - **Microsoft Edge**: Corporate Intranet Browsing.
    - **Microsoft OneDrive**: Corporate File Sync and Share.
- Upon first launch of each app, the user logs in with their Meridian credentials. The app policy enforces:
    - **Data Encryption**: App data encrypted at rest using device-level crypto.
    - **Access Requirements**: PIN or biometric (FaceID/Fingerprint) required on app launch (`AccessContext: 15-min inactivity timeout`).
    - **Data Leakage Prevention**: "Save As" to personal storage locations is blocked. Copy/Paste between MAM-protected apps and personal apps is strictly blocked.
    - **App Conditional Launch**: Alert and block access if device passes a root/jailbreak detection check by the Lookout SDK integrated into Intune.

**Step 3: Mobile Threat Defense (MTD) Integration**
- During enrollment, user is redirected to install Lookout for Work.
- User activates Lookout for Work. This establishes the security health data feed to Intune Compliance Engine.
- **Failure to install Lookout for Work places the device in "Non-Compliant" status.** Conditional Access policy `CA-BLOCK-NONCOMPLIANT` immediately blocks access to all Meridian cloud resources until remediation.

### 5.3 Full-Tunnel VPN Connection Requirements

All remote workstations (corporate-owned laptops and BYOD desktops/laptops) must connect via the Meridian Full-Tunnel VPN (Zscaler Private Access, or ZPA) before any access to application tier (ePHI scope) or source code repositories is permitted. Split-tunnel configurations are disabled by policy globally.

**Connection Workflow:**
1.  **Launch Client**: User launches Zscaler Client Connector (v3.7+) from system tray.
2.  **Authentication**: User authenticates against Azure AD with Passwordless (FIDO2 security key or Microsoft Authenticator passcodes). SMS-based MFA is deprecated and blocked by this policy.
3.  **Device Health Check**: Zscaler sends a posture check call to CrowdStrike Falcon.
    - **Check**: Falcon sensor running and active?
    - **Check**: Anti-Malware protection state is `Active`?
    - **Check**: OS firewall enabled for `Domain` and `Private` profiles?
    - **Check**: Disk encryption (BitLocker/FileVault) active?
    - **Result**: If all checks pass, ZPA establishes a secure micro-tunnel to the Zscaler Zero Trust Exchange. If any check fails, connection is refused, and the user is redirected to a remediation portal.
4.  **Data Plane**: All user traffic exits to the internet via the Meridian Zscaler Internet Access (ZIA) node for TLS/SSL inspection and Data Loss Prevention (DLP) scanning. Exceptions in firewall posture are logged and reviewed continuously by the Security Operations Center (SOC).

### 5.4 Data Handling Classification and Remote Access Matrix

Not all data is accessible via all remote methods. The matrix in Table 5.4 overrides general connectivity. Violation of this matrix is an automatically flagged incident.

| Data Classification | Examples | Remote on Corp Laptop (VPN) | BYOD Smartphone (MAM) | BYOD Laptop (Citrix VDI) | Public Wi-Fi Permitted? |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Public** | Marketing press releases, public code docs | ✓ | ✓ | ✓ | ✓ |
| **Internal** | HR policies, IT process docs, staff directory | ✓ | ✓ | ✓ | ✓ |
| **Confidential** | Source code, financial projections, non-public roadmaps | ✓ | **Prohibited** | ✓ (No Download) | **Prohibited** |
| **Restricted (ePHI/PII)** | Patient imaging records, payment card data, EU citizen PII | ✓ (VDI or IRM only) | **Prohibited** | ✓ (VDI Session Only, Clipboard Disabled) | **Prohibited** |

*IRM = Information Rights Management. Microsoft Purview applied SharePoint/OneDrive files auto-encrypt on download.*

---

## 6. Controls and Safeguards

This section describes the administrative and technical controls implemented to meet specific articles and criteria of SOC 2, HIPAA, and GDPR.

### 6.1 SOC 2 Specific Controls (Trust Services Criteria: Security & Confidentiality)

Meridian's remote work and BYOD infrastructure directly maps to controls within the Common Criteria (CC) series.

- **Control CC6.1 (Logical and Physical Access Controls)**:
    - **Implementation**: The combination of Azure AD Conditional Access (identity) and Zscaler Private Access (logical gateway) operates under the Zero Trust model. No traffic reaches an application server without a valid cryptographic identity token and device compliance signal.
    - **Technical Control**: `Policy: CA-BLOCK-LEGACY-AUTH`. Legacy authentication protocols (IMAP, POP, ActiveSync basic auth) are blocked tenant-wide. This prevents token replay attacks against legacy mailboxes accessible via insecure personal devices.
    - **Measurement**: Bi-weekly review of the "Legacy Authentication Attempts" log in Log Analytics workspace.

- **Control CC6.3 (Roles and Responsibilities)**:
    - **Implementation**: Role-Based Access Control (RBAC) is enforced for remote access provisioning. `SG-REMOTE-ACCESS-PROV` membership is restricted to the IT Service Desk Tier 2, with access reviews conducted by the Security Engineering team.
    - **Measurement**: Monthly PIM (Privileged Identity Management) audit log review. Just-In-Time (JIT) access grants for Tier 2 expire after 4 hours.

- **Control CC7.2 (Monitoring of Deviations)**:
    - **Implementation**: Microsoft Sentinel analytic rule `SEN-RISK-UNUSUAL-GEO-LOGIN`. Logs Azure AD sign-ins.
    - **Alert Condition**: User signs in from a geolocation distance > 5,000km from the previous successful sign-in within a 24-hour period. (Impossible travel detection).
    - **Automated Playbook**: On alert, Sentinel triggers a Logic App that disables the user account, revokes current Zscaler session tokens, and creates a Priority 1 ticket in ServiceNow SOC queue. Account reactivation requires CISO verbal confirmation.

- **Control CC6.6 (External Threats)**:
    - **MTD Threat Scoring**: Lookout for Work assigns a risk score to each BYOD device based on detected threats (e.g., trojanized app, OS exploit attempt). Conditional Access policy `CA-BLOCK-HIGH-RISK-DEVICE` blocks access if Lookout reports a "High" threat state (Score > 80).
    - **Implementation**: MTD risk score is synced to Intune Compliance API every 15 minutes.

### 6.2 HIPAA Specific Controls (45 CFR Part 164, Subpart C - Security Standards)

Controls specifically protect the confidentiality, integrity, and availability of ePHI in remote settings, directly addressing the Administrative Safeguards of the HIPAA Security Rule.

- **Standard: §164.308(a)(3)(ii)(A) - Workforce Security (Authorization/Supervision).**
    - **Procedure**: The "Restricted Data Handling Matrix" (Section 5.4) is programmatically enforced. Access to MedInsight Analytics APIs containing ePHI is restricted to IP ranges originating from `Citrix-VDI-EastUS` or `Citrix-VDI-WestEU`. Direct browser access from a personal laptop (even with VPN) is blocked by web application firewall (WAF) rules at the API gateway layer.
    - **Assignment**: Clinical data analysts requiring access to de-identified datasets have their role (`RBAC-CLIN-DEIDENT`), which fails VDI clipboard redirection, enforcing data immobility.

- **Standard: §164.308(a)(5)(ii)(B) - Security Awareness and Training (Protection from Malicious Software).**
    - **Implementation**: As documented in Section 5.2, Step 3, the installation of Lookout MTD is mandatory. The CrowdStrike Falcon sensor (Corporate Devices) also guards against malware. The combination ensures an endpoint meets the "Clean Source" standard before being trusted.
    - **Responsibility**: The Chief Information Security Officer (CISO, A. Vance) is responsible for ensuring the MTD platform is updated with threat intelligence relevant to healthcare data targeting.

- **Standard: §164.312(a)(2)(ii) - Access Controls (Encryption and Decryption).**
    - **Implementation**: Meridian employs BitLocker (AES-256) on all Windows corporate laptops, FileVault on all macOS corporate laptops, and leverages native hardware-backed encryption for MAM container data on BYOD devices. ePHI at rest is *always* encrypted. ePHI in transit over public networks is protected by the TLS 1.2+ full-tunnel VPN.
    - **Emergency Access Procedure**: In a disaster recovery scenario where VPN is unavailable, emergency access to ePHI is provisioned via a dedicated, air-gapped Meridian laptop and a physically escorted connection at a designated recovery site (DR Site SOP-DR-001).

- **Standard: §164.310(c) - Workstation Use.**
    - **Implementation**: The Physical Workspace Self-Assessment Checklist (Appendix D) requires the remote user to attest they have a "privacy screen" (a physical polarizing filter) installed on any laptop used to view patient data, or that the screen faces a solid wall with no line of sight from windows or doors.
    - **Audit**: Compliance auditors conduct random tele-video inspections (with 24 hours notice) for roles designated "High Risk" (e.g., Telehealth Review Physicians) to verify workstation configuration. This is a contractual condition of remote access for those roles.

### 6.3 GDPR Specific Controls

Controls operationalizing Meridian's obligations as a Data Controller for EU/EEA Personnel and as a Processor for client data.

- **Control: GDPR Art. 28 (Processor) - BYOD Sub-Processor Management.**
    - While Meridian Personnel are not external processors, the *vendors* on the BYOD device are. Microsoft (Intune MAM) and Lookout are sub-processors.
    - **Safeguard**: The MAM architecture ensures Microsoft cannot access personal data on the device. A Standard Contractual Clause (SCC) is executed between Meridian and Lookout, governing the transfer of limited MTD telemetry from the EU to the US. This SCC is reviewed annually by the Data Protection Officer (L. Muller).

- **Control: GDPR Art. 25 (Data Protection by Design and Default)**.
    - **MAM Defaults**: By default, the Intune App Protection Policy denies "Save Copies of Org Data" to any unprotected location. This is an operationalized "privacy by design" technical measure.
    - **Consent Management**: For non-essential cookies or tracking (strictly limited to Meridian internal HR portals for EU employees), the OneTrust consent management platform records the consent string and preference vector. It is not embedded in critical clinical pathways, ensuring patient safety is not reliant on cookie consent.

- **Control: GDPR Art. 33 (Breach Notification)**.
    - **Procedure**: If a personal device is lost or stolen, the user is obligated to report the incident to the SOC within **1 hour** of discovery. The SOC executes Playbook `SOC-PB-DEVICE-LOST`. The Sentinel automated response (Section 6.1) is triggered manually if automatic conditions aren't met. The DPO has a 72-hour statutory window for regulatory notification; the technical remediation (remote wipe of corporate MAM container) executes the SOC ticket `TASK-WIPE-CONTAINER` which must be completed within **60 minutes** of verified ticket creation.

---

## 7. Monitoring, Metrics, and Reporting

Ongoing assurance is derived from automated technical controls mapped to a continuous monitoring dashboard.

### 7.1 Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs)

| Metric ID | Metric Description | Target / SLA | Measurement Source | Reporting Frequency |
| :--- | :--- | :--- | :--- | :--- |
| **CMP-BYD-01** | BYOD Device Compliance Rate | **> 98%** of enrolled devices passing Conditional Access checks | Microsoft Intune Compliance Dashboard | Weekly (Automated Report) |
| **RISK-VPN-01** | Split-Tunnel VPN Connection Attempts | **0** per week | Zscaler Private Access Logs -> Sentinel | Daily (SOC Monitor) |
| **CMP-PAT-01** | Corporate OS Patch Latency (Remote) | **Critical: < 72hrs; Important: < 14 days** | CrowdStrike Falcon / MS Intune | Weekly (IT Ops Meeting) |
| **INC-LOST-01** | Time-to-Container-Wipe on Reported Loss | **< 60 minutes** from SOC ticket creation | ServiceNow Field: `time_to_disable` | Per Incident, Quarterly Review |
| **TRN-REM-01** | Annual Remote Work Security Training Completion | **100%** of active remote employees | LMS (Workday) - Assignment `SEC-REM-202X` | Monthly during renewal period |

### 7.2 Reporting Cadence
- **SOC Manager (Daily)**: Reviews Zscaler Alerts for MTD misconfigurations and brute-force VPN attempts.
- **CISO (Weekly)**: Receives a "Remote Trust Score" snapshot generated from Intune and Zscaler dashboards, summarizing KPI trends.
- **Management Review (Quarterly)**: Jennifer Walsh (CHRO) and Adrian Vance (CISO) present a joint QBR to the Executive Risk Committee covering: exception aging, training non-compliance trends, and policy waiver re-evaluation.

---

## 8. Exception Handling and Escalation

Meridian recognizes that the standard technical controls may be incompatible with niche but critical business functions. The exception process is designed to be transparent and time-boxed.

### 8.1 Standard Exception Procedure
1.  **Request Initiation**: Personnel submits a "Policy Exception Request" in ServiceNow (Catalog Item `REQ-SEC-EXCEP`). The user must specify the control they are requesting relief from (e.g., "No MTD on Android device used as backup MFA"), the specific business justification, and a proposed compensating control.
2.  **Engineering Review**: The CISO office performs a technical analysis to determine if the compensating control adequately reduces residual risk to an acceptable level.
3.  **Approval Matrix**:
    - **Low Risk** (e.g., expired certificate on a dev-only internal portal): Auto-approved by ServiceNow with Director of IT (P. Chen) approval.
    - **Medium Risk** (e.g., macOS N-2 OS version used for isolated graphic design work): Requires CISO (A. Vance) approval. Validity: 30 days.
    - **High Risk** (e.g., accessing de-identified patient data on a BYOD device without VDI for field medical teams): Requires CISO **and** Chief Medical Officer joint approval. Validity: 7 days. Requires mandatory post-activity event log review. **Extremely rare.**
4.  **Expiry and Review**: Upon exception expiry, the control is automatically re-enforced. Renewal requires a new justification and review of any recorded incidents during the exception window.

### 8.2 Emergency Access (Break-Glass)
In the event of a critical system outage where standard VPN and VDI are unavailable, the SOC Manager can initiate the "Emergency Break-Glass Access" protocol (`SOP-SEC-015`). This process generates uniquely audited, one-time-use credentials that bypass Conditional Access. All actions performed under "Break-Glass" credentials are logged to an immutable write-once, read-many (WORM) Sentinel table and reviewed by the full Executive Risk Committee within 24 hours of issuance.

---

## 9. Training Requirements

All Personnel subject to this policy must complete mandatory, role-based training.

| Training Module | Course Code | Assigned To | Frequency | Method |
| :--- | :--- | :--- | :--- | :--- |
| **Remote Work & BYOD Security Essentials** | `SEC-REM-001` | All Remote Users | Annually | Workday Learning (Video + Quiz, 80% pass mark) |
| **HIPAA for Remote Clinicians** | `CLIN-REM-HIPAA` | Telehealth Physicians, Clinical Analysts accessing PHI | Annually + On Hire | VDI-based interactive scenario workshop |
| **GDPR Data Protection for Managers** | `DPO-GDPR-MGR` | People Managers of EU/EEA Personnel | Biannually | E-learning module + Q&A webinar with Legal |
| **Phishing Simulation** | `SEC-SIM-PHISH` | All Users | Quarterly | Automated simulated phishing platform (KnowBe4). Failure results in mandatory remedial 20-minute training session within 72 hours. |

**Training Tracking**: Completion status is tracked in the Workday Learning Management System (LMS). Non-completion within the assigned window (30 days from assignment) will trigger automated notification to the People Manager and IT to initiate an automated "Conditional Access Review." Access rights may be downgraded to "Email Only" until training is completed.

---

## 10. Related Policies and References

This SOP is part of an interconnected policy library. It must be read alongside the following Meridian internal documents and external standards.

### 10.1 Internal Meridian SOPs
| SOP ID | Document Title |
| :--- | :--- |
| SOP-SEC-001 | Information Security Management System (ISMS) Manual |
| SOP-SEC-003 | Data Classification and Handling Standard |
| SOP-SEC-012 | Third-Party Vendor Security Risk Management |
| SOP-SEC-015 | Incident Response and SOC Playbook |
| SOP-IT-001 | Office Network and Corporate Device Access Control |
| SOP-IT-005 | Endpoint Management and Patching Standard (Intune & Jamf) |
| SOP-HR-002 | Employee Acceptable Use and Monitoring Policy |
| SOP-HR-005 | Disciplinary Action Policy |
| SOP-CLIN-004 | Clinical Imaging Workstation and Viewing Environment Standard |

### 10.2 External Regulatory and Standards References
- **SOC 2**: TSP Section 100 (2017 Trust Services Criteria for Security, Availability, and Confidentiality), specifically CC6.1 through CC6.8 and CC7.1 through CC7.5.
- **HIPAA**: 45 CFR Part 160 and Subparts A/E of Part 164. NIST SP 800-66r2 (An Implementable Guide for the Security Rule).
- **GDPR**: Regulation (EU) 2016/679, specifically Article 5 (Principles), Article 25 (Protection by Design), Article 32 (Security), and Article 33 (Notification).
- **NIST**: NIST SP 800-63B (Digital Identity Guidelines), NIST SP 800-171 (Protecting Controlled Unclassified Information).

---

## 11. Revision History

This document undergoes a formal review bi-annually by the owner and the policy approval board.

| Version | Effective Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **5.4** | 2025-04-17 | J. Walsh (CHRO) | Full document rewrite to align with new Zscaler ZPA architecture. Added explicit SOC 2 CC6 mapping table. Updated BYOD Intune MAM procedures to remove legacy Device Admin profiles. Changed VPN split-tunnel wording from "discouraged" to "technically blocked." |
| **5.3** | 2024-11-15 | P. Chen (IT Ops) | Added Appendix C: Contractor Security Addendum. Updated Section 7 KPIs to include `RISK-VPN-01` metric requiring a zero-threshold. Updated Crowdstrike sensor version prerequisite. |
| **5.2** | 2024-05-02 | A. Vance (CISO) | Major overhaul: Replaced legacy AnyConnect VPN procedures with Zscaler Private Access (ZPA) full-tunnel micro-segmentation. Updated DLP controls to align with Microsoft Purview IRM. Added GDPR Art. 28 Sub-Processor matrix for MTD tools. |
| **5.1** | 2023-09-10 | M. Li (HR Ops) | Updated Section 1.2 Scope to include Clinical Personnel restrictions. Revised Training section to reflect Workday LMS migration from Saba. |
| **5.0** | 2023-01-15 | J. Walsh (CHRO) | Initial unified policy version, merging legacy "Remote Access" (SOP-IT-004) and "Personal Device" (SOP-HR-004) into a single holistic SOP. Added CEO-level approval requirement. |