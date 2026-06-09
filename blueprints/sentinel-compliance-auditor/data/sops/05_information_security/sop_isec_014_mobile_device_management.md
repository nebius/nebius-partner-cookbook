---
sop_id: "SOP-ISEC-014"
title: "Mobile Device Management"
business_unit: "Information Security"
version: "5.9"
effective_date: "2024-07-12"
last_reviewed: "2025-07-11"
next_review: "2026-01-16"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the enterprise framework for the provisioning, configuration, management, monitoring, and decommissioning of mobile devices that access Meridian Health Technologies, Inc. (“Meridian”) information systems, data, and applications. The objective is to safeguard the confidentiality, integrity, and availability (CIA) of Meridian’s intellectual property, protected health information (PHI), personally identifiable information (PII), and financial data processed, transmitted, or stored on mobile endpoints while enabling a productive and agile workforce. This SOP operationalizes the controls mandated by the Meridian Information Security Policy and the requirements of the System and Organization Controls (SOC) 2 Type II trust services criteria, specifically the Security and Confidentiality categories.

### 1.2 Scope
This SOP applies globally to:
- All employees of Meridian Health Technologies, Inc. and its subsidiaries (London, Berlin, Singapore, Toronto) including full-time, part-time, and temporary staff.
- All contractors, consultants, interns, and third-party personnel (collectively “Users”) who access Meridian corporate resources, including but not limited to the Meridian SaaS Platform, Clinical AI Platform, HealthPay Financial Services, and MedInsight Analytics, via a mobile device.
- All mobile computing devices capable of storing, processing, or transmitting Meridian data, including:
    - Corporate-owned, personally-enabled (COPE) smartphones and tablets (e.g., Apple iOS/iPadOS, Google Android).
    - Corporate-owned, business-only (COBO) smartphones and tablets.
    - Bring-your-own-device (BYOD) smartphones and tablets enrolled in the Meridian containerized management solution.
    - Wearables with cellular or Wi-Fi connectivity that synchronize with corporate email or messaging systems (e.g., Apple Watch with ActiveSync profile).
- All operating systems, applications, and network interfaces on or accessible from these devices.

### 1.3 Out of Scope
- Laptops (Windows and macOS) and Chromebooks. These are managed under **SOP-ISEC-008 (Endpoint Security and Configuration Management)** .
- Devices issued solely for the purpose of Multi-Factor Authentication (MFA) hardware tokens that do not possess a general-purpose operating system (e.g., YubiKey, RSA SecurID hardware token).
- Personally owned devices that have not been enrolled in the Meridian BYOD program via the self-service portal and possess zero access to Meridian corporate resources.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **ADE** | Apple Device Enrollment, formerly Device Enrollment Program (DEP). Apple's service for automating Mobile Device Management (MDM) enrollment and supervision for corporate-owned iOS/iPadOS devices. |
| **AML** | Anti-Money Laundering. Contextually relevant, as mobile devices used in transaction processing must not introduce laundering risks through compromised channels. |
| **BYOD** | Bring Your Own Device. A personal device used for corporate access, managed via a containerized agent (Microsoft Intune Company Portal) that separates corporate and personal data. |
| **COBO** | Corporate-Owned, Business-Only. A Meridian-owned device locked to business use only, typically fully supervised and managed via Automated Device Enrollment (ADE) or Zero-Touch Enrollment (ZTE). |
| **COPE** | Corporate-Owned, Personally-Enabled. A Meridian-owned device that allows for limited personal use under a strict, signed Acceptable Use Policy. Full MDM visibility is retained. |
| **Custodian** | The Meridian manager or director responsible for a pool of shared mobile devices (e.g., devices used in clinical trials, manufacturing plant floor tablets). |
| **Enrollment** | The process of adding a device to the Meridian Microsoft Intune MDM tenant, which establishes a trust relationship, pushes configuration profiles, and enforces compliance policies. |
| **Intune** | Microsoft Intune, Meridian’s unified endpoint management (UEM) platform, integrated with Microsoft Entra ID, for mobile device and application management. |
| **Jailbreak (iOS/iPadOS) / Root (Android)** | A process that removes manufacturer-imposed software restrictions, granting a User root-level access to the operating system. Device status is immediately classified as compromised. |
| **Lookout Mobile Endpoint Security** | Meridian’s mobile threat defense (MTD) solution, integrated with Intune via the mobile threat defense connector, to detect advanced device, network, app, and phishing threats at the device level. |
| **MDM** | Mobile Device Management. The administrative framework and technical infrastructure (Intune) for managing device configuration, security policies, app deployment, and lifecycle. |
| **MTP** | Managed Threat Protection. A continuous threat-hunting service provided by the Meridian Security Operations Center (SOC) focused on mobile endpoints. |
| **OOBE** | Out-of-Box Experience. The initial setup wizard presented to a User on a new or factory-reset device. |
| **Sanctions Screening** | An automated procedure that cross-references every new device enrollment and associated User identity against international sanctions lists, politically exposed persons (PEP) databases, and denied-party lists using the Refinitiv World-Check One platform. |
| **Supervised Mode** | An enhanced management state for Apple iOS/iPadOS devices, enforced via ADE. This mode unlocks advanced MDM controls, including Activation Lock bypass, silent app installation, and global proxy configuration. |
| **User** | Any Meridian employee, contractor, or third-party personnel using a Meridian-managed mobile device. |
| **ZTE** | Zero-Touch Enrollment. Android’s equivalent to ADE, managed via the Samsung Knox Mobile Enrollment (KME) and Google Zero-Touch portal, ensuring corporate devices enroll into MDM during the OOBE. |

---

## 3. Roles and Responsibilities

The following Responsibility Assignment Matrix (RACI) delineates the roles for the lifecycle of the Mobile Device Management program.
- **R:** Responsible (The person who performs the work)
- **A:** Accountable (The person who signs off or approves the work; the single point of accountability)
- **C:** Consulted (Subject matter experts whose opinions are sought)
- **I:** Informed (Kept up to date on progress, often via automated reporting)

| Activity / Task | User | Manager | InfoSec Engineering (MDM Team) | SOC Analyst | Chief InfoSec Officer (CISO) | Data Protection Officer (DPO) | Internal Audit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Device Enrollment** | R | A | C | I | I | I | I |
| **BYOD Policy Acknowledgement** | R | I | I | I | I | I | I |
| **Lost/Stolen Device Reporting** | R | I | C | I | I | I | I |
| **Remote Device Wipe** | I | I | R | C | A | I | I |
| **Sanctions Screening (Initial)** | I | I | R | I | I | A | I |
| **Sanctions Screening (Ongoing 24-hr)** | I | I | I | R | I | A | I |
| **Compliance Policy Configuration** | I | I | R | C | A | I | I |
| **Mobile Threat Remediation** | R | I | C | R | I | I | I |
| **MDM Agent Health Monitoring** | I | I | R | C | I | I | I |
| **Exception Approval** | R | C | C | I | A | C | I |
| **Quarterly Access Review** | I | A | R | I | I | C | R |

---

## 4. Policy Statements

4.1 **Mandatory Enrollment:** All corporate-owned smartphones and tablets (COBO, COPE models) capable of accessing Meridian information systems MUST be enrolled in the Microsoft Intune MDM platform via Automated Device Enrollment (Apple) or Zero-Touch Enrollment (Android) before being assigned to a User. For BYOD scenarios, enrollment of the device into the Intune Company Portal for Application Protection Policies is mandatory before corporate app provisioning.

4.2 **Separation of Duties:** No single person shall possess both the ability to modify the Intune MDM Configuration Baseline and approve a device compliance policy exemption. The MDM Engineering team (Responsible) and the Chief Information Security Officer (Accountable) represent a logical separation.

4.3 **Sanctions and Watchlist Screening (SOC 2 CC3.2, CC6.1):** Every device enrollment request is tied to a specific Meridian User identity. Prior to the establishment of a management session and the provisioning of corporate data, this identity, its associated device phone number (SIM), and device International Mobile Equipment Identity (IMEI) are screened against the Refinitiv World-Check One database. A positive match results in an immediate, automated suspension of the enrollment, logged for the SOC and DPO.

4.4 **Data Sovereignty:** Configuration profiles deployed via Intune shall respect geographic data residency requirements. MDM enrollment for Users located in the EU subsidiary (Berlin) will be directed to the EU Microsoft 365 tenant boundary.

4.5 **Default Deny Posture for Jailbroken/Rooted Devices:** Any device detected with a compromised operating system (jailbreak or root) shall, via an automated Intune compliance policy action, be immediately marked as `non-compliant`. The associated User account will be blocked from accessing Entra ID-integrated applications (Conditional Access, Policy `CA011-DeviceCompliance`) within one (1) minute of detection. Retiring (selective wipe of corporate data) will be initiated automatically.

---

## 5. Detailed Procedures

### 5.1 Device Procurement and Staging
This procedure ensures Meridian-purchased devices are enrolled in the MDM program before reaching the User, achieving "zero-touch" provisioning in alignment with SOC 2 control objective CC7.1 (Logical Access Control).

1.  **Procurement Authorization:**
    - The requesting Manager completes the *IT Procurement Request Form* in ServiceNow, specifying the device model (from the approved Hardware Catalog) and the assignee User.
    - IT Finance verifies the request against the budget and the Hardware Refresh Cycle (SOP-FIN-002).

2.  **Vendor Enrollment Configuration:**
    - Upon order placement with the corporate reseller (e.g., CDW, Insight), the Meridian InfoSec Engineering (MDM Team) verifies the device serial numbers are populated in the respective enrollment portals:
        - **Apple Business Manager (ABM):** Verify the new serial numbers are assigned to the `Meridian Health Technologies, Inc.` MDM server within ABM.
        - **Samsung Knox Mobile Enrollment (KME) / Google Zero-Touch:** Verify the Reseller ID has pushed the new IMEI/serial numbers, and the default `Meridian-Standard-Profile` is assigned.
    - **Weekly Audit Control:** Every Monday, the "Unassigned Devices" report is pulled from ABM and Google Zero-Touch. Any device not assigned to the Meridian MDM server within five (5) business days of its purchase date triggers an alert to `mdm-engineering@meridian.com`.

3.  **Device Receipt and Staging:**
    - The receiving department (Corporate IT) unboxes the device for physical inspection and asset tagging.
    - An engineer powers on the device. The device connects to Wi-Fi, contacts Apple/Google activation servers, receives the MDM enrollment profile, and completes the OOBE into a "Kiosk" or "Staging" mode. No User credentials are entered at this stage.

### 5.2 User Enrollment and First-Time Setup (COPE/COBO)
This procedure covers the user-facing steps for a pre-staged corporate device.

1.  **Handover and Identity Verification:**
    - The User receives the staged, asset-tagged device from their Manager or local IT contact.
    - The User proceeds through the final device setup screens. At the login prompt, the User enters their Meridian corporate credentials (`username@meridian.com`) and completes Multi-Factor Authentication (MFA) via the Microsoft Authenticator app on their existing device or a hardware token.

2.  **Automated Compliance Check:**
    - The Intune Company Portal app auto-launches. An immediate device compliance check evaluates the following:
        - OS version ≥ `N-1` current release.
        - Encryption status (iOS: FileVault equivalent enabled by policy; Android: File-Based Encryption).
        - Passcode complexity (≥6 character alphanumeric OR biometric).
        - Lookout for Work agent status `Active`.
    - **Failure Handling:** If the device fails any compliance check, the User is blocked from proceeding and presented with a clear remediation message (e.g., "Please update your OS to continue").

3.  **Mandatory Agreement Acknowledgement:**
    - The User is presented with the *Meridian Acceptable Use Policy for Mobile Devices (M-AUP-001)* HTML form within the Intune Managed Home Screen.
    - The User MUST tap **"I Agree"** to proceed. This acceptance is time-stamped and permanently stored in the Intune audit logs linked to the Azure Monitor workspace. Non-acceptance results in the device remaining in a quarantined state with only the Company Portal accessible.

4.  **Application Provisioning:**
    - Upon acceptance, Intune pushes the following **Core Security Applications**, tagged as "Required":
        - Microsoft Intune Company Portal
        - Microsoft Edge for Business
        - Microsoft Defender for Endpoint (Mobile)
        - Lookout for Work (Mobile Endpoint Security)
    - Subsequently, role-required applications (e.g., Microsoft Teams, Outlook, Power BI, authenticator apps for Meridian's Clinical AI Platform) are pushed based on the User's Entra ID group membership. App installation is silent and forced.

### 5.3 BYOD Enrollment (Personally-Owned Devices)
This procedure leverages User Privacy Bubble controls on Android and iOS “User Enrollment” to separate corporate and personal data.

1.  **Self-Service Invitation:**
    - The User downloads the "Microsoft Intune Company Portal" app from the Apple App Store or Google Play Store.
    - The User opens the app and signs in with their Meridian corporate credentials.
    - The app detects it is an unmanaged, personal device and presents the BYOD enrollment pathway.

2.  **Scope of Management and User Consent:**
    - Meridian’s Privacy Notice for BYOD (*SOP-HR-003 Appendix A*) is presented. It clearly stipulates what Meridian *can* and *cannot* see/control: inventory of corporate apps, corporate app data, and device compliance posture (OS version, encryption status). It explicitly states Meridian CANNOT see personal app data, browser history, SMS texts, photos, or GPS location (unless a corporate app, like the field service tool, is actively running in the foreground).
    - User taps **"Enroll"** to create the corporate work profile (Android) or begin User Enrollment (iOS).

3.  **Compliance and Application Protection:**
    - Instead of full device-level policies, Application Protection Policies (APP) are enforced for the corporate apps. For example, the Outlook mobile app will require a 6-digit passcode to open and will automatically encrypt its local app cache.
    - Conditional access for BYOD is policy `CA012-BYOD-LimitedAccess`, which restricts BYOD device access to only Office 365 web apps (browser) and prevents downloading files to unmanaged local storage.

### 5.4 AML-Specific: Sanctions Screening Procedure
This procedure is a critical control at the intersection of identity, device, and financial crime risk.

1.  **Trigger Event:** Every attempt to enroll a device, or when a new SIM/eSIM profile is detected by the MDM agent, triggers a User and Device (IMEI) cross-check.
2.  **Automated Screening Execution:**
    - A logic app (`AzureLogicApp-AML-Screen`) receives the enrollment signal from the Intune Data Warehouse.
    - It formats a query containing: `UserPrincipalName`, `DisplayName`, `CountryCode` of the detected carrier, and `DeviceIMEI`.
    - The query is sent to the Refinitiv World-Check One API.
3.  **Result Handling:**
    - **Clear:** The "Enrollment Approved" status is written back to the device record in Intune. The normal app provisioning workflow continues. Full transaction log is written to the SOC’s Sentinel workspace.
    - **Fuzzy Match (Low Confidence):** The device enrollment is suspended. A high-priority incident (`Inc-Tier2-Sanctions-Fuzzy`) is auto-created for the AML Compliance Team, who must manually review and clear the alert within **4 business-hours**. The DPO is notified of the pending review.
    - **Hit (High Confidence):** The device enrollment is terminated. The device receives a non-dismissible Managed Browser message: "Access Denied. Contact Security." The User identity in Entra ID is disabled for all Meridian resources. A Priority 1 (P1) incident is triggered for the SOC and CISO, and the AML Compliance Officer and General Counsel are paged immediately.

### 5.5 Lost, Stolen, or Compromised Device Response
This is a high-severity security incident response procedure involving immediate User action and MDM administrative control.

1.  **User Reporting (T+0):** The User MUST report a lost, stolen, or suspected compromised device within **15 minutes** of discovery or suspicion. The report must be made via one of the two (2) channels:
    - **Primary:** Call the 24/7 Meridian Service Desk at `+1-888-555-SEC1`. This initiates ticket `INC-LOST-DEV`.
    - **Secondary (if voice is unavailable):** Email `security@meridian.com` with the subject line `URGENT: Lost Device - [User UPN]`. This email inbox is connected to the PagerDuty alerting system for the SOC Tier 1 queue with a guaranteed 5-minute alert-to-acknowledgement SLA.

2.  **SOC/Service Desk Acknowledgment and Verification (T+5 min):**
    - The agent validates the User’s identity by asking two (2) pre-registered security questions or confirming a time-based one-time password (TOTP) push to their registered backup MFA method.
    - The agent confirms the device asset tag number from the CMDB record.

3.  **Immediate Containment Actions (T+10 min):**
    The Service Desk agent executes the following actions sequentially from the Intune admin console:
    - **Device Lock:** Sends a remote lock command to set a new, complex (16-character) alphanumeric PIN. This prevents physical access by an unauthorized person if the device is still on and connected.
    - **Locate Device:** Issues a locate device command. The last known GPS coordinates are logged for potential physical recovery or forensic evidence.
    - **Conditional Access Block:** Manually adds the specific device object to the Entra ID dynamic device group `GRP-SEC-Quarantined-Devices`. This group is excluded from ALL Meridian resource Conditional Access policies, immediately severing the data plane access, regardless of active user credentials.
    - **User Notification:** The User receives an automated email confirming the containment actions.

4.  **Determination and Recovery/Decommissioning:**
    - **If the device is RECOVERED within 24 hours and judged PHYSICALLY SECURE by InfoSec (e.g., left at home and not accessible to others):** The device MUST be factory-reset and re-enrolled from scratch. The "Lost Device" tag is removed from the CMDB asset record only after an MDM engineer confirms compliance post-re-enrollment.
    - **If the device is NOT RECOVERED within 24 hours OR is judged POSSIBLY COMPROMISED (e.g., left in a public place):** The final action is an irreversible "Enterprise Wipe.". This command removes all corporate data and apps and, for supervised corporate devices, removes the MDM profile and initiates a factory reset, rendering the device a brick. The device is written off as a financial asset by ITAM (SOP-FIN-002).

---

## 6. Controls and Safeguards

This section maps Meridian-specific technical and administrative controls to the SOC 2 Trust Services Criteria (TSC) for the Security and Confidentiality categories (Reference: TSP Section 100, *2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy*).

| Control ID | Control Description | TSC Mapping | Implementation Detail | Monitoring/Test Frequency |
| :--- | :--- | :--- | :--- | :--- |
| **MDM-01** | **Automated Device Enrollment** ensures that all corporate devices are enrolled in MDM before the User receives them, with no option to bypass. | CC6.8 (Controls Logical Access), A1.2 (Management Oversight) | Apple Business Manager (ABM) and Samsung Knox Mobile Enrollment (KME) portals are configured to automatically assign devices with Meridian-issued serial numbers to the `Meridian Corp Intune` MDM server. No manual unassignment is permitted by non-privileged IT. | Daily reconciliation report between ABM/KME portal and the live device list in the Intune console. |
| **MDM-02** | **Device Compliance Policy** enforces a set of minimum-security configurations, and non-compliance immediately revokes access to corporate resources via Conditional Access. | CC6.1 (Logical and Physical Access Controls), CC6.3 (Mitigation of Risks at Network Entry Points) | Intune Compliance Policy `COMP-001` checks: <br>1. OS < Minimum version (iOS/Android).<br>2. Jailbreak/Root detection.<br>3. Encrypted (File-level).<br>4. Passcode policy.<br>The "Action for non-compliance" schedules an immediate conditional access block, marking the device "In Grace Period" (0 days) for remediation. | Real-time, enforced at each Conditional Access token refresh (max 60 min token lifetime). Health dashboard tracks "Mean-Time-To-Remediate" for all non-compliant devices in a weekly InfoSec operations meeting. |
| **MDM-03** | **Mobile Threat Defense (MTD) Integration** provides runtime threat detection for device, network, app, and phishing risks, with automated risk-score-based remediation. | CC7.1 (Design of Detection Measures), CC7.2 (Monitoring Activities) | Lookout for Work is deployed as a `Required` app. The Intune MTD connector is configured to `High` severity level. The threat scoring is: <br>1. **High (e.g., Active Man-in-the-Middle Attack):** Immediate compliance change → `Non-Compliant` → Conditional Access Block. SOC P2 incident auto-created.<br>2. **Medium (e.g., Outdated OS, Suspicious App Detected):** User receives push notification to remediate. Non-compliance after 24 hours.<br>3. **Low:** Logged to SIEM only. | Lookout console monitored continuously by SOC Tier 1. Monthly MTD efficacy report sent to the CISO, detailing blocked threats by category. |
| **MDM-04** | **Application Protection Policies (APP)** are the primary safeguard for BYOD and provide data exfiltration prevention at the managed-app level, independent of device enrollment. | CC6.6 (Logical Access Measures for External Points), CC6.7 (Data Transmit, Removal, and Disposal) | Policy `APP-001-BaseDataProtection` is applied to all mobile Microsoft Office apps. It prevents "Save As" to unmanaged local storage, restricts cut/copy/paste between corporate and personal app containers, and requires a corporate PIN to access the managed app. Application-layer encryption is enforced. | Weekly review of Intune App Protection Status report. Quarterly audit by Internal Audit of the APP policy assignment and configuration using a PowerShell script against the Graph API. |
| **MDM-05** | **Restricted, Role-Based Administrative Access** to the Intune MDM console and related cloud resources minimizes the risk of a privileged account compromise. | CC6.3 (Mitigation of Risks), CC9.1 (Management of Control Activities) | Access to the `Intune Administrator` and `Global Administrator` Entra ID roles is strictly controlled. <br>1. These roles require a dedicated "privileged access workstation" (PAW) or a Privileged Identity Management (PIM) Just-in-Time (JIT) activation flow requiring MFA and a ticket number.<br>2. `Global Admin` activation requires *two* (2) separate approvers from the InfoSec leadership team (CISO + Deputy CISO).<br>3. All PIM role activations are logged to Azure Sentinel. | Real-time alerting for any `Global Admin` PIM activation without a matching P1/P2 incident ticket. Quarterly access certification review of PIM eligible roles. |
| **MDM-06** | **Configuration Drift Detection** continuously audits the deployed MDM configuration profiles against a defined "golden baseline" to identify and alert on unauthorized changes. | CC7.2 (Monitoring of Deviations), CC8.1 (Change Management) | The MDM team uses a Microsoft Defender for Cloud Apps (MDA) connector for Microsoft 365 that monitors the Graph API activity for the `DeviceManagementConfiguration` resource. Any creation, modification, or deletion of a configuration profile generates an alert. A weekly automated script uses the Graph API to diff the currently active profiles against the `Master-Profile-Baseline` stored in a secured Git repository. | Automated daily script run, results emailed to `mdm-engineering@meridian.com`. Weekly SOC dashboard shows all profile changes and their correlation to approved ServiceNow Change Requests (CHG). |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Service Level Objectives (SLOs)
The effectiveness of the MDM program is measured against the following quantitative metrics. These are reviewed by the VP of Information Security monthly.

| Metric Category | Key Performance Indicator (KPI) | Target / SLO | Measurement Tool | Calculation Method |
| :--- | :--- | :--- | :--- | :--- |
| **Enrollment** | % Corporate-Owned Devices Enrolled in MDM | 100% | Intune vs. CMDB Asset Record | `(Intune_Managed_Corp_Devices / Total_Corp_Devices_in_Asset_Register) * 100` |
| **Compliance** | % BYOD Devices Passing All Compliance Checks (Weekly Snapshot) | > 98% | Azure Monitor Workbook (`MDM Compliance Dashboard`) | `(Compliant_Devices / Total_Managed_Devices) * 100` |
| **Security Response** | Mean Time to Respond (MTTR) for Lost/Stolen Device Containment | < 15 minutes from report | ServiceNow `INC-LOST-DEV` tickets | `Avg(Time_of_Device_Mark_Non_Compliant - Time_of_Ticket_Creation)` |
| **Threat Management** | Time to Automatically Remediate a High-Risk MTD Finding | < 1 minute | Lookout Console & Intune Logs | `Avg(Time_of_Automated_Conditional_Access_Block - Time_of_Lookout_Detection_Timestamp)` |
| **Patch Management** | % of Corporate-Owned Devices on the Latest OS Major Version < 90 days post-release | > 95% | Intune Reports > "Device compliance" pivot by OS version | `(Devices_on_Target_OS / Total_Corp_Devices) * 100` |
| **Admin Control** | Time to Detect an Unauthorized MDM Configuration Change | < 24 hours | Sentinel Alert `MDM-Profile-Change-No-CHG` | `Time_of_Sentinel_Alert_Creation - Time_of_Actual_Change_API_Log` |

### 7.2 Reporting Cadence
- **Real-Time:** A wallboard display in the SOC visualizes active MDM alerts, ongoing sanctions screening statuses, and the count of non-compliant devices.
- **Weekly Operational Review:** The InfoSec Engineering Manager (Thomas Ashton) generates an automated report from Azure Monitor (Workbook `MDM-Weekly-Ops`) every Monday, 08:00 EST. This report covers enrollment, compliance drift, OS patch levels for the week prior. This is reviewed in the weekly Cloud Operations stand-up.
- **Monthly Business Review:** A formal slide deck is prepared by the MDM Lead, summarizing all KPI performance against targets, major incidents, exception reviews, and a rolling 6-month forecast of enrollment changes (driven by onboarding projections from HR). The audience is the VP, InfoSec (Robert Liu).
- **Quarterly Management Review:** The CISO (Rachel Kim) presents the MDM program state, including a SOC 2 control walkthrough and auditor feedback, to the Enterprise Risk Committee. This review includes ratification of any approved policy exceptions.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling Procedure
A formal exception process is required for any deviation from the prescriptive procedures and controls defined in this SOP. No permanent, undocumented "workarounds" are allowed.

1.  **Request Initiation:** The requesting User or Manager submits an *ISEC Exception Request* form via the Meridian Service Catalog in ServiceNow. The request must detail:
    - The specific SOP section(s) and control ID(s) from which the deviation is sought.
    - A rigorous, documented business justification.
    - The proposed compensating control(s) to mitigate the resulting risk.
    - Duration for the exception (maximum initial term: 90 days).

2.  **Risk Assessment:** The MDM Engineering Team Lead, in collaboration with a designated Risk Analyst, performs a formal risk assessment. They assign a risk rating (Low, Medium, High, Critical) using the Meridian Enterprise Risk Matrix (SOP-RISK-001).

3.  **Approval Chain:** The exception must be approved based on its risk rating:
    - **Low Risk:** Approved by the Manager, InfoSec Operations.
    - **Medium Risk:** Approved by the Manager, InfoSec Operations, and the business unit’s VP.
    - **High Risk:** Approved by the VP, Information Security (Robert Liu), and the Chief Data Officer.
    - **Critical Risk:** Approved by the CISO (Rachel Kim), the Chief Financial Officer (James Thornton), and the requestor’s Executive VP. A compensating control *must* be in place and verified by Internal Audit before the exception goes live.

4.  **Tracking and Expiry:** All approved exceptions are tracked centrally in the ServiceNow "MDM Exception Register." The exception automatically expires at the end of its approved term. The Service Desk creates a task five (5) business days prior to expiry, notifying the requestor and the InfoSec team to either certify remediation or initiate a re-certification and re-approval cycle.

### 8.2 Escalation Path for Operational Incidents
For a major system failure (e.g., Intune tenant-wide sync failure, a mass-impacting Lookout for Work false positive causing a DoS condition for > 50 users):

1.  **Tier 1 SOC / Service Desk:** Detects the anomaly, confirms the blast radius, and creates a Priority 1 (P1) incident following **SOP-ISEC-001 (Incident Response Plan)**.
2.  **On-Call MDM Engineer:** Engaged via PagerDuty automatically on P1 creation. SLA to join the war room bridge is **15 minutes**.
3.  **VP, InfoSec (Robert Liu):** Notified for all P1 incidents or any P2 incident involving a potential sanctions list "Fuzzy Match" that was mis-handled.
4.  **CISO (Rachel Kim):** Notified for any P1 incident with a duration exceeding 2 hours, any confirmed data breach, or any successful phishing campaign that compromised a managed device.
5.  **CFO (James Thornton) and General Counsel:** Notified immediately for any confirmed "Hit" (High Confidence) on the automated AML sanctions screening procedure.

---

## 9. Training Requirements

Mandatory training is a foundational SOC 2 administrative control to ensure personnel are competent to perform their assigned responsibilities.

| Training Module | Audience | Delivery Method | Frequency | Tracking Mechanism | Content Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SOP-FIN-004: Mobile Device User Fundamentals** | All Meridian Users receiving a managed device or enrolling in BYOD | Cornerstone LMS, e-learning module | **Initial:** Prior to device issuance/enrollment. **Annual Refresher:** Annually, based on hire date. | Completion status auto-reported to Cornerstone LMS and Azure Entra ID User Profile. Non-completion triggers a conditional access block on day +7 of non-compliance. | Covers: Acceptable Use Policy, how to identify a jailbroken device, how to report a lost device, phishing attack recognition via SMS/email on a mobile device, and the User’s responsibility for protecting corporate data. Includes a practical "Report a Phishing" simulation test. |
| **MDM Engineering: Technical Mastery** | All members of the InfoSec MDM Engineering Team | Instructor-led lab and assessment (Quarterly) | **Initial:** Within 30 days of hire. **Quarterly:** Every quarter, aligning to new Apple/Google OS releases. | Practical skills assessment scored by Manager, InfoSec Engineering (> 85% pass mark required). Records stored in personal HR files. | Advanced Intune administration, ABM/KME portal configuration, PowerShell/Graph API scripting for automated compliance drift detection, MTD integration troubleshooting, and sanctions screening API troubleshooting. |
| **SOC Analyst: Mobile Threat Triage** | All SOC Tier 1 and Tier 2 Analysts | Instructor-led and simulation exercises in the Meridian Cyber Range. | **Semi-Annual.** | Capture-the-Flag (CTF) exercise score and time-to-triage benchmark reported in the SOC analyst's performance dashboard. | Hands-on triage of Lookout for Work alerts (actual vs. false positive), executing the lost/stolen device containment procedure within the 15-minute MTTR SLO, investigating sanctions screening fuzzy match alerts, and correlating device logs with Sentinel SIEM. |

---

## 10. Related Policies and References

### 10.1 Meridian Internal Policies

| SOP-ID | Document Name | Relationship |
| :--- | :--- | :--- |
| **SOP-ISEC-001** | Information Security Incident Response Plan | Escalation procedures for lost/stolen devices and mobile malware outbreaks. |
| **SOP-ISEC-003** | Access Control Policy | Foundational policy for user and administrative access to Meridian systems, including Conditional Access enforcement. |
| **SOP-ISEC-005** | Data Classification and Handling Standard | Defines the data classification schema (Public, Internal, Confidential, Restricted) used to determine acceptable data types on BYOD. |
| **SOP-ISEC-008** | Endpoint Security and Configuration Management | Covers non-mobile endpoints (laptops, servers), but shares the common Defender for Endpoint and agent architecture. |
| **SOP-ISEC-015** | Network Security and Perimeter Defense | Defines the VPN and network infrastructure mobile devices connect from, including Wi-Fi security profiles pushed via MDM. |
| **SOP-PRIV-001** | Employee Data Privacy Notice | The foundational privacy document for the BYOD program, referenced in the User consent form. |
| **SOP-HR-003** | Employee Onboarding and Offboarding | The trigger mechanism from Workday (Hire/Terminate) that initiates or retires a User’s mobile device access lifecycle. |
| **SOP-RISK-001** | Enterprise Risk Management Framework | The risk matrix used to formally evaluate exception requests. |

### 10.2 External Standards and Regulations

- **SOC 2:** TSP Section 100, *2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy* (specifically CC6.1, CC6.3, CC6.6, CC6.7, CC6.8, CC7.1, CC7.2, A1.2).
- **HIPAA:** 45 CFR Part 164, Subpart C – Security Standards for the Protection of Electronic Protected Health Information (the “Security Rule”). This SOP implements technical safeguards for access control (§ 164.312(a)(1)), audit controls (§ 164.312(b)), integrity (§ 164.312(c)(1)), and person or entity authentication (§ 164.312(d)).
- **Microsoft Intune Documentation:** Microsoft official product documentation, serving as a procedural reference for the MDM technical team.

---

## 11. Revision History

| Version | Date | Author | Description of Change | Approved By |
| :--- | :--- | :--- | :--- | :--- |
| 5.1 | 2023-02-14 | Thomas Ashton, InfoSec Engineering Manager | Initial public version. Replaced AirWatch content with full Intune migration guidance. Added Lookout MTD integration procedures. | Rachel Kim, CISO |
| 5.3 | 2023-09-01 | Sarah Jenkins, Service Desk Lead | Updated Section 5.5 (Lost/Stolen) with new 24/7 Service Desk phone number and clarified TOTP identity verification step. | Robert Liu, VP InfoSec |
| 5.5 | 2024-01-10 | Thomas Ashton, InfoSec Engineering Manager | Added Section 5.4 AML-specific Sanctions Screening procedure. Added MDM-05 and MDM-06 controls to Section 6. Updated device platform minimums to iOS 17.0+. | James Thornton, CFO |
| 5.7 | 2024-06-28 | Elena Rossi, DPO | Integrated EU data boundary configuration statements into policy statements (Section 4.4) and enrollment procedure (Section 5.1) to align with new EUC tenant topology. | Rachel Kim, CISO |
| 5.8 | 2025-07-11 | Thomas Ashton, InfoSec Engineering Manager | Annual review. Updated Conditional Access policy naming, revised KPI targets for OS patch compliance to N-1, and added Microsoft Defender for Endpoint (Mobile) to the core stack. Corrected broken cross-references. | Robert Liu, VP InfoSec |
| **5.9** | **2025-01-22** | **Thomas Ashton, InfoSec Engineering Manager** | **Replaced "JIT Admin" with full PIM (Privileged Identity Management) procedure. Updated training curriculum to MAM/MTD modules. Refined sanctions screening logic for fuzzy match handling.** | **Dr. Sarah Chen, CEO** |