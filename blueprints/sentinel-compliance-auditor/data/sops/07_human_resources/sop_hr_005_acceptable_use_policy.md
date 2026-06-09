---
sop_id: "SOP-HR-005"
title: "Acceptable Use Policy"
business_unit: "Human Resources"
version: "4.2"
effective_date: "2025-06-06"
last_reviewed: "2026-02-14"
next_review: "2026-08-11"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# STANDARD OPERATING PROCEDURE

## SOP-HR-005: Acceptable Use Policy

**Version 4.2**

---

## 1. Purpose and Scope

### 1.1 Purpose
The Meridian Health Technologies, Inc. (“Meridian,” “the Company”) Acceptable Use Policy (AUP) establishes the rules, responsibilities, and expectations governing the use of all Meridian Information Resources. This policy is designed to protect the confidentiality, integrity, and availability (CIA) of Meridian’s data assets—with particular emphasis on Protected Health Information (PHI) and Personally Identifiable Information (PII)—while enabling a productive, collaborative, and secure working environment. This policy embodies the principles of least privilege, need-to-know, and individual accountability, directly supporting our SOC 2 Type II trust services criteria and HIPAA Security Rule compliance.

### 1.2 Scope
This policy applies uniformly to:

| Category | Description |
|---|---|
| **All Workforce Members** | Full-time employees, part-time employees, contractors, consultants, temporary staff, interns, and volunteers. |
| **Third Parties** | Vendors, business associates, and their subcontractors who access, process, or store Meridian data through any Meridian Information Resource. Third-party obligations are codified in Business Associate Agreements (BAAs) and Master Services Agreements (MSAs), which incorporate this policy by reference. |
| **All Information Resources** | Company-issued devices (laptops, workstations, mobile devices), personally-owned devices used for work via BYOD program enrollment, servers, network infrastructure, cloud services, software applications, communication platforms, and data repositories across all Meridian environments (production, staging, development, QA). |
| **All Geographic Locations** | This policy extends globally to all Meridian offices (Boston HQ, London, Berlin, Singapore, Toronto) and any remote work location. Where local laws are more restrictive, local requirements shall prevail. |
| **All Data Classifications** | Including, but not limited to, Public, Internal, Confidential, and Restricted (see Section 2.1). |

### 1.3 Jurisdictional Overlay
Meridian operates a global business. Workforce members based in the European Union or processing personal data of EU data subjects are additionally bound by the GDPR and related policies (see SOP-DPO-001, *Data Protection Governance*). In the event of any conflict between this general AUP and a jurisdiction-specific addendum, the stricter standard controls. The EU AI Act classification of our Clinical AI Platform as high-risk AI imposes supplementary use restrictions on workforce members engaged in its development and maintenance.

---

## 2. Definitions and Acronyms

### 2.1 Data Classification Tiers

| Tier | Label | Definition | Examples at Meridian |
|---|---|---|---|
| Tier 0 | **Public** | Information approved for unrestricted public dissemination. | Official marketing materials, published press releases, public website content. |
| Tier 1 | **Internal** | Non-sensitive business information not intended for public release but unlikely to cause material harm if disclosed. | Internal newsletters, cafeteria menus, general policy documents (unredacted), anonymized process documents. |
| Tier 2 | **Confidential** | Proprietary business information, sensitive personal information, or data subject to contractual non-disclosure obligations. Unauthorized disclosure could cause significant reputational, financial, or competitive harm. | Source code (excluding AI models), financial projections, merger and acquisition activity, employee performance reviews, network diagrams, penetration test reports. |
| Tier 3 | **Restricted** | Highly sensitive data subject to stringent legal, regulatory, or contractual controls. Unauthorized access, use, or disclosure could result in severe legal penalties, irreparable patient harm, identity theft, or catastrophic business impact. | **Protected Health Information (PHI)** , electronic Protected Health Information (ePHI), personally identifiable information subject to GDPR/CCPA, production customer lists, Clinical AI model weights, CE-marked medical device raw data, encryption keys, privileged account credentials. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| AICPA | American Institute of Certified Public Accountants |
| AUP | Acceptable Use Policy |
| BAA | Business Associate Agreement |
| BYOD | Bring Your Own Device |
| CASB | Cloud Access Security Broker |
| CCPA | California Consumer Privacy Act |
| CEO | Chief Executive Officer |
| CHRO | Chief Human Resources Officer |
| CIA | Confidentiality, Integrity, Availability |
| CISO | Chief Information Security Officer |
| CSIRT | Computer Security Incident Response Team |
| DLP | Data Loss Prevention |
| DPO | Data Protection Officer |
| DLP | Data Loss Prevention |
| EDR | Endpoint Detection and Response |
| ePHI | Electronic Protected Health Information |
| GDPR | General Data Protection Regulation (EU) |
| HIPAA | Health Insurance Portability and Accountability Act of 1996 |
| HR | Human Resources |
| IDS/IPS | Intrusion Detection System / Intrusion Prevention System |
| IR | Information Resources |
| IT | Information Technology |
| KPI | Key Performance Indicator |
| LMS | Learning Management System |
| MDR | Medical Device Regulation (EU) |
| MFA | Multi-Factor Authentication |
| NIST | National Institute of Standards and Technology |
| PHI | Protected Health Information |
| PII | Personally Identifiable Information |
| POC | Point of Contact |
| RACI | Responsible, Accountable, Consulted, Informed |
| SIEM | Security Information and Event Management (Microsoft Sentinel) |
| SOC 2 | Service Organization Control 2 |
| SST | System Security Team (sub-team of IT Security) |
| VPN | Virtual Private Network (Zscaler Private Access) |
| UAM | User Activity Monitoring (Forcepoint) |

---

## 3. Roles and Responsibilities

The following RACI matrix delineates responsibility and authority for the implementation and enforcement of this AUP.

| Activity / Responsibility | Workforce Member | Manager | HR (People Operations) | IT Support | IT Security (CISO) | DPO (Berlin) | CHRO | CEO |
|---|---|---|---|---|---|---|---|---|
| Adhere to AUP daily | **R** | C | I | – | – | – | I | – |
| Report violations immediately | **R** | **R** | I | C | C | – | I | – |
| Approve standard exceptions | – | **R** | C | C | C | – | A | – |
| Approve high-risk exceptions | – | C | C | C | **R** | C | A | I |
| Execute monitoring (UAM, DLP, SIEM) | – | – | – | I | **R** | I | I | – |
| Investigate Tier 2/3 violations | – | – | **R** | C | **R** | C | C | – |
| Issue formal enforcement (discipline) | – | C | **R** | – | – | – | **A** | I |
| Annual SOP review & update | – | – | C | – | C | C | **R** | **A** |
| Authorize network termination (emergency) | – | – | – | – | **R** | – | C | C |

**Key:**
- R = Responsible (performs the work)
- A = Accountable (signs off, ultimate answerable)
- C = Consulted (must be asked, two-way communication)
- I = Informed (one-way communication, kept apprised)

### 3.1 Specific Named Roles

- **Policy Owner**: Jennifer Walsh, CHRO. The CHRO is ultimately Accountable for the maintenance and annual review of this SOP under delegated authority from the CEO.
- **Technical Enforcement Owner**: Chief Information Security Officer (CISO). The CISO, or their designated representative (Director of Security Operations), is Responsible for the technical controls that monitor and enforce provisions of this policy.
- **Data Protection Officer (DPO)**: Anja Vogel, DPO, Berlin Office. The DPO must be Consulted on any investigation involving the personal data of EU-based workforce members, or any incident with potential GDPR implications (see SOP-SEC-011, *Data Breach Response*).
- **Exception Authority**: Standard exceptions (Section 8.1.1) are approved by the requestor’s direct manager. Critical exceptions (Section 8.1.2), such as the temporary use of an unmanaged device for development, must be approved by the CISO and the relevant Vice President.

---

## 4. Policy Statements

Meridian Health Technologies is committed to the following high-level principles:

### 4.1 Principle of Least Privilege
Users shall be granted access only to the specific Meridian Information Resources and data assets minimally necessary to perform their established job duties. Role-based access is reviewed at least quarterly by each line-of-business manager using IdentityNow certifications.

### 4.2 No Expectation of Privacy
While Meridian’s monitoring program is proportionate and business-relevant, workforce members must understand that they have no personal expectation of privacy for any activity conducted on, or data stored within, Meridian Information Resources. This monitoring is critical to satisfying **SOC 2 Common Criteria CC4.1 and CC4.2**, which require the entity to monitor system use and respond to security events.

### 4.3 Zero Tolerance for Malicious Prohibited Activities
Activities defined in Section 5.3.2 (Strictly Prohibited) constitute a direct threat to the security and integrity of Meridian’s HIPAA-regulated environment and will result in immediate suspension of access, escalation to the CSIRT, and possible summary termination of employment.

### 4.4 Protection of ePHI
The protection of electronic Protected Health Information (ePHI) is a shared responsibility. Any activity not explicitly directed toward the authorized creation, viewing, modification, or secure transmission of ePHI in the course of a patient-care-related workflow is presumptively unauthorized. This aligns directly with **HIPAA 45 CFR § 164.312 (Technical Safeguards)** , specifically Access Control (§ 164.312(a)(1)) and Audit Controls (§ 164.312(b)).

---

## 5. Detailed Procedures

### 5.1 Data Classification and Labeling Procedure

Correct labeling is the prerequisite for all technical controls. A data asset with an incorrect asset classification is a control failure.

#### 5.1.1 Data at Rest Labeling

| Asset Type | Labeling Mechanism | Responsible Party |
|---|---|---|
| Microsoft 365 Files (SharePoint, OneDrive, Teams) | Mandatory Sensitivity Label. Users must select one of four labels (Public, Internal, Confidential, Restricted) via the Microsoft Information Protection unified labeling client. A policy tip ("Tooltip") automatically alerts the user if a Restricted label is being applied to content not digitally fingerprinted as PHI. | File Creator / Last Editor |
| AWS S3 Buckets (Clinical Data Lake) | Automated tagging via AWS Lambda function. Any object placed in a bucket tagged `data-classification = restricted` is auto-labeled with `metadata:classification = Restricted`. Manual override is blocked. | System / DevOps |
| Physical Documents | Cover sheet color-coding: White (Public), Yellow (Internal), Blue (Confidential), Red (Restricted). Secure disposal bin matching the highest classification of batch. | Document Owner |

**Procedure Steps (End-User Labeling):**
1.  Upon finalizing any document, spreadsheet, or presentation, select the **Sensitivity** dropdown from the top ribbon in the Office application.
2.  Determine the correct classification based on Section 2.1. If uncertain, default to the higher-sensitivity tier. For example, an email discussing a potential clinical trial should be **Confidential**, not **Internal**.
3.  Apply the label. Automatic client-side encryption is enforced for any document labeled **Restricted**. The encryption key is service-managed Azure Rights Management (Azure RMS) within the Meridian tenant.
4.  Transmit the file according to the Handling Requirements Matrix (Section 5.2.1).

### 5.2 Permitted Use Procedures

#### 5.2.1 Handling Requirements Matrix

| Activity | Public (Tier 0) | Internal (Tier 1) | Confidential (Tier 2) | Restricted (Tier 3) |
|---|---|---|---|---|
| **Email (Internal)** | Permitted | Permitted | Permitted | Permitted ONLY with RMS Encryption. Subject line MUST contain `[Encrypt]`. |
| **Email (External)** | Permitted | Prohibited without Mgr approval | Prohibited | Prohibited (use Meridian Secure Link). |
| **Removable Media** | Permitted | Permitted (BitLocker-encrypted USB only) | Prohibited without CISO exception | **Strictly Prohibited (technically blocked by endpoint DLP)** |
| **Cloud Storage** | Any service | Meridian-approved (O365) | Meridian-approved (AWS/GovCloud) | Highly restricted (Designated HIPAA enclaves) |
| **Printing** | Permitted (B&W) | Permitted (B&W) | Permitted (Secure Print PIN required) | **Strictly Prohibited unless for direct patient care** |
| **Mobile Device Sync** | Permitted | Permitted (Intune Compliant) | Permitted (Intune Compliant, no local copy) | Prohibited by default; exception required |

#### 5.2.2 Secure Remote Access
Workforce members working from a non-Meridian managed network (home office, public Wi-Fi) must connect to Meridian resources exclusively via the Zscaler Private Access (ZPA) zero-trust architecture or the approved VPN client. Direct internet ingress to the Meridian network is disabled. All remote sessions are subject to session recording via Ekran System for privileged users and Forcepoint UAM for standard users.

#### 5.2.3 Use of Personally-Owned Devices (BYOD)
Meridian permits limited BYOD enrollment for access to Tier 0 (Public) and Tier 1 (Internal) data, like email and the corporate intranet (Meridian Central), through the Microsoft Intune Company Portal with Mobile Application Management (MAM) without full device enrollment ("MAM-WE"). This creates a secure container. Access to Tier 2 (Confidential) or Tier 3 (Restricted) data from a personally-owned device is strictly prohibited. Copy/paste functions from the MAM container to personal apps are blocked by Intune policy `POL-MAM-001`.

### 5.3 Prohibited Activities

#### 5.3.1 General Prohibitions
The following activities are prohibited for all users on Meridian Information Resources:
- **Circumvention:** Attempting to bypass, disable, or tamper with any security control, including antivirus software (Microsoft Defender for Endpoint), host-based firewalls, EDR agents, or web content filters (Zscaler Internet Access).
- **Personal Gain:** Selling, leasing, or offering Meridian data or access to any third party not authorized under a valid BAA or MSA.
- **Credential Sharing:** Sharing individual user account credentials (Active Directory / Entra ID) with any other person, including IT support staff or supervisors. All access must be attributable.
- **Resource Hogging:** Deliberately consuming excessive network bandwidth (e.g., personal crypto-mining, torrenting) that degrades clinical application performance. The SD-WAN policy carves out guaranteed QoS for the Epic Hyperspace clinical workspace; non-clinical traffic is scavenger-class.

#### 5.3.2 Strictly Prohibited Activities (Zero Tolerance)
Violation of these controls triggers Immediate Notification (Section 6.3.3) and CSIRT escalation. These directly contravene **SOC 2 CC6.1** (Logical and Physical Access Controls) and **HIPAA § 164.312(b)** , representing willful neglect.
1.  **ePHI Exfiltration:** Any deliberate attempt to email, copy, upload, or print ePHI outside of an authorized clinical or analytical workflow. DLP policies `DLP-PROD-01` and `DLP-PROD-02` are configured to block and alert on these actions out-of-the-box.
2.  **Malicious Software:** Intentional introduction of viruses, ransomware, worms, keyloggers, or any other malicious code into the Meridian environment.
3.  **Unauthorized Penetration Testing:** Any port scanning, vulnerability probing, or penetration testing against Meridian assets without written authorization from the CISO. All authorized testing is conducted under a strict Statement of Work by the Red Team.
4.  **Patient Data De-identification Outside Authorized Process:** Attempting to de-identify PHI without using the statistical methods approved by the DPO and General Counsel (as per 45 CFR § 164.514(a-b) Expert Determination). Manual ad-hoc de-identification is a prohibited act.

### 5.4 AI and Clinical Model Integrity (Supplemental Prohibition)

Given the CE-marked status of our clinical AI products under EU MDR, the feeding of any non-validated, ad-hoc production data into a model for "experimental" training is strictly prohibited. All model training and fine-tuning must follow the Quality Management System (QMS) change control in SOP-ENG-008 (*AI Model Change Management*). Violation constitutes a regulatory quality failure under MDR Annex IX (Conformity Assessment) and a Class I Incident under this policy.

---

## 6. Controls and Safeguards

This section details the administrative, physical, and technical safeguards that operationalize the Acceptable Use Policy. These controls are mapped directly to our SOC 2 Common Criteria (CC-series) and HIPAA Security Rule standards to facilitate annual audit testing by our external assessor, Schellman & Company.

### 6.1 Administrative Controls

| Control ID | Control Description | Control Owner | SOC 2 Trust Services Criteria (2024) | HIPAA Citation | Operational Cadence |
|---|---|---|---|---|---|
| **ADM-001** | **Acceptable Use Policy Acknowledgment.** All workforce members must formally acknowledge this AUP in the Workday LMS prior to being granted initial access. Re-acknowledgment is required annually and upon any major version release (e.g., v4.0 to v5.0). Failure to acknowledge within 10 business days triggers automatic access suspension. | CHRO / HRIS Director | CC1.2 | § 164.308(a)(5)(i) | Event-driven: Onboarding, Annually (Q3), Version Change |
| **ADM-002** | **Sanction Policy.** Meridian operates a formal, graduated HR Sanction Policy mapped to investigation findings. Sanctions range from mandatory retraining to termination. HR tracks sanction KPIs (Section 7) to demonstrate management commitment per CC1.4. | CHRO | CC1.2, CC1.4 | § 164.308(a)(1)(ii)(c) | Continual review; quarterly KPI report |
| **ADM-003** | **Third-Party Risk Management.** Standard AUP language is incorporated into all BAAs and MSAs. The Vendor Risk Management function (SOP-SEC-012) performs SOC 2 report reviews for critical vendors to confirm downstream AUP enforcement. | CISO / Legal | CC9.2 | § 164.308(b)(1) | Annual contract review |

### 6.2 Physical Controls
Physical access is governed under SOP-FAC-001, *Physical Security Policy*. All Restricted data processing centers (Boston data center, AWS us-east-1 designated enclave) require access control vestibules and biometric verification. Clean desk policy is enforced nightly by security patrol in Boston HQ, London, Berlin, and Singapore offices.

### 6.3 Technical Controls

#### 6.3.1 Endpoint Controls (Device-Level)
All Meridian-issued, managed endpoints (Windows 11 via Intune, macOS via Jamf Pro) receive the following baseline policy:
- **Encryption:** All drives encrypted with BitLocker (XTS-AES-256, Recovery Key escrowed in Entra ID) or FileVault (escrowed in Jamf). A non-encrypted device cannot establish a Zscaler Private Access tunnel.
- **Host Firewall:** `FW-STD-01` applied. Blocks all unsolicited inbound traffic.
- **EDR:** Microsoft Defender for Endpoint in Active mode. Any attempt to stop the `MsSense.exe` service generates a high-severity alert in Microsoft Sentinel.

#### 6.3.2 Network & Perimeter Controls
- **Secure Web Gateway (SWG):** Zscaler Internet Access (ZIA). All web traffic, whether on-network or off, is proxied through ZIA. The URL filtering policy `URL-FILTER-PROD-01` categorically blocks categories like "Peer-to-Peer," "Hacking," and "Personal VPN/Proxy."
- **Cloud Access Security Broker (CASB):** Microsoft Defender for Cloud Apps (formerly MCAS). Connected to all major sanctioned SaaS apps (M365, Box, AWS, Salesforce Health Cloud). Session policies monitor and control, in real time, unpermitted file downloads, mass deletions, and anomalous tenant activity.
- **Intrusion Prevention (IDS/IPS):** Meridian’s Palo Alto Networks perimeter firewalls (physical and VM-Series in AWS) inspect all north-south traffic. The IPS profile is tuned to block `critical` and `high` severity signatures for client-side exploits commonly used in drive-by download attacks.

#### 6.3.3 Data-Centric Controls
| Policy ID | Technology | Objective | Rule Logic |
|---|---|---|---|
| `DLP-PROD-01` | Microsoft Purview DLP | Block ePHI Exfiltration via Email | Block (with override and justification prompt) any email from Exchange Online containing a match count > 5 of the "Meridian Medical Record Number (MRN)" Sensitive Information Type heading to an external recipient. |
| `DLP-PROD-02` | Microsoft Purview DLP | Block ePHI on Removable Media | Block (silent audit) any attempt to write to a USB removable storage device if the file name, content fingerprint, or sensitivity label matches the "Meridian – Restricted" label. A policy tip alerts the user, "Writing Restricted data to USB is prohibited. Action audited." |
| `DLP-ENDP-03` | Microsoft Purview Endpoint DLP | Monitor Confidential AI Source | When any file with the label "Confidential AI Model" is copied from a developer workstation, a high-severity informational alert is raised in Sentinel, and the activity is recorded for forensic review. No block is active, but the action is fully attributable. |

---

## 7. Monitoring, Metrics, and Reporting

Meridian’s monitoring aims to be a secondary, detective control. We do not perform wholesale, indiscriminate surveillance of user activity but instead employ targeted, risk-based monitoring via Microsoft Sentinel, Forcepoint UAM, and AppDetectivePRO for database activity monitoring.

### 7.1 Audit Log Review
Per **HIPAA § 164.312(b)** and **SOC 2 CC4.2** (Monitoring of Deviations), the Security Operations Center (SOC) performs weekly audit log review. A tier-1 analyst reviews the “AUP Violations” dashboard, triages true positives from false positives, and escalates to a tier-2 Analyst for investigation. All tier-2 investigations are recorded in the ServiceNow Security Incident Response (SIR) module.

### 7.2 Key Performance Indicators (KPIs)
The ISMS Steering Committee reviews the following metrics monthly:

| Metric ID | KPI Description | Target | Source System | Responsible Owner |
|---|---|---|---|---|
| **AUP-01** | **AUP Violation Incidents per Quarter:** Total number of substantiated AUP violations broken down by classification tier (Tier 1, Tier 2, Tier 3). | Trending down quarter-over-quarter. Target: < 5 substantiated Tier 3 violations per quarter. | ServiceNow SIR | CISO |
| **AUP-02** | **Acknowledgment Compliance:** % of active user base with a current, signed Acknowledgment in Workday. | ≥ 99.5% at all times. | Workday HCM | HRIS Director |
| **AUP-03** | **Mean Time to Respond (MTTR) to High-Severity AUP Alerts:** Time from Sentinel alert firing (SIR creation) to a Tier-2 analyst beginning investigation. | < 60 minutes, 24/7/365. | Sentinel / ServiceNow | SOC Manager |
| **AUP-04** | **Repeat Violator Rate:** % of all violations committed by users who had a substantiated violation in the preceding rolling 12-month period. | < 5% of all violators. | ServiceNow SIR | CHRO |
| **AUP-05** | **Security Awareness Program Efficacy:** Score on the quarterly simulated phishing campaign for users who failed the previous quarter's campaign. | Mean pass rate > 85%. | KnowBe4 LMS | Director of GRC |

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Delivery Mechanism |
|---|---|---|---|
| **AUP Operational Dashboard** | IT Support Management, SOC Manager | Continuous (Near real-time) | Power BI Dashboard (`SEC-OPS-AUP-001`) |
| **ISMS Steering Committee AUP Briefing** | ISMS Committee (CISO, DPO, GC, CHRO) | Monthly | Formal slide deck, includes KPI run chart |
| **Quarterly Workforce AUP Reminder** | All Workforce Members | Quarterly | Email from CHRO, "The Safe Harbor," a simplified infographic on top 3 AUP risks observed that quarter. |
| **Annual AUP & SOC 2 Effectiveness Report** | Audit Committee of the Board | Annually | Formal PDF report submitted by the CISO and CHRO, including external audit findings. |

---

## 8. Exception Handling and Escalation

Deviations from this AUP are permitted only through a formal, documented exception process. Temporary, undocumented "workarounds" are a direct and serious policy violation.

### 8.1 Exception Process
All exception requests must be submitted via the ServiceNow Service Catalog ("Request a Security Exception"). The process is as follows:
1.  **Submit:** Requestor submits the form, detailing the specific policy section from which they need exception, the technical justification, the exact asset(s) affected, the compensating controls they will implement, and a proposed expiration date (not to exceed 90 days).
2.  **Technical Review:** The IT Security Engineering team validates the technical justification and assesses the risk of granting the exception.
3.  **Approval Routing:**
    - **Standard Exceptions (Risk Score < 20 on internal matrix):** Auto-routed to the user’s direct manager and then CISO’s delegate (Director of GRC).
    - **Critical Exceptions (Risk Score ≥ 20, e.g., temporary USB write access for a pathology microscope):** Routed to the DPO for data-privacy impact assessment, CISO for technical risk acceptance, and finally the relevant C-level officer (e.g., Chief Medical Information Officer for clinical workflows).
4.  **Closure:** Upon expiration, the control must be re-implemented. The SOC Manager verifies closure and closes the ServiceNow ticket. The exception is logged in the risk register.

### 8.2 Emergency Escalation Procedure
In the event a security incident is occurring in real-time (e.g., detected ransomware encryption, active ePHI data exfiltration):
1.  **Immediate Action:** SOC Analyst on duty follows SOP-SEC-011 (*Data Breach Response*) playbook. This playbook includes immediate, pre-authorized steps to contain the threat, which may include programmatically toggling a user’s Entra ID account to "Disabled," revoking all session tokens via Microsoft Entra admin center, or issuing an API call to Zscaler to quarantine the endpoint.
2.  **Declare Incident:** The Incident Commander (Director of IT Operations or CISO, per on-call rotation) is paged via PagerDuty.
3.  **Chain of Custody:** All forensic actions (memory dumps, disk imaging with FTK Imager) are taken by the Director of IT Forensics. A formal chain of custody is established to preserve evidence supporting potential HIPAA breach notification (per 45 CFR § 164.410 et seq.) or law enforcement referral.

---

## 9. Training Requirements

### 9.1 Initial Training
Within the first 5 business days of their start date, all new workforce members are assigned the mandatory "HIPAA & AUP Essentials for Meridian" learning path in the Workday LMS. This comprises three micro-learning modules (total 45 minutes) and a final 20-question graded assessment. A passing score of **85% or higher** is required. The provisioning of core network access accounts is gated behind a successful completion recorded in Workday via an automated API integration.

### 9.2 Annual Refresher Training
All workforce members must complete the “Annual Compliance & AUP Refresher” course during the Q4 training window (October 1 – November 15). This refresher uses real, anonymized case studies from Meridian’s CSIRT investigations from the prior year to illustrate consequences.

### 9.3 Role-Based Supplemental Training
Workforce members in the following privileged roles receive additional, specialized AUP training covering their elevated responsibilities:
- **Developers & AI Engineers:** GDPR pseudonymization techniques and AI model integrity (mandated by EU AI Act).
- **Clinicians & Researchers:** Common scenarios involving inadvertent AUP violation (e.g., using a personal phone camera to photograph a wound for a peer consult without proper secure platform workflow).
- **Managers:** The "Manager’s Guide to Reporting and Escalation," a deep dive into their responsibility to Consult and Report under Section 3.

### 9.4 Tracking and Metrics
The HR People Operations team generates a monthly KPI (AUP-02) tracking training completion and acknowledgment. A report listing any non-compliant user (past due on either training or policy acknowledgment) is automatically emailed to non-compliant users with their direct manager in CC. After 30 days of non-compliance, the user’s accounts are suspended per ADM-001.

---

## 10. Related Policies and References

### 10.1 Meridian Internal Policies

| Document ID | Document Title | Relationship to AUP |
|---|---|---|
| **SOP-FAC-001** | Physical Security Policy | Governs the physical access controls that protect Information Resources. |
| **SOP-IT-002** | Access Control and Identity Management Policy | Specifies user provisioning, role definitions, and quarterly manager access reviews. |
| **SOP-IT-003** | Password and Authentication Standard | Sets standards for the credentials used to access Meridian systems. |
| **SOP-SEC-008** | Vulnerability and Patch Management SOP | Governs the scanning activities that are a prohibited “self-service” under this policy. |
| **SOP-SEC-011** | Data Breach Response and Notification SOP | Describes the official playbook for what happens when AUP is violated disastrously. |
| **SOP-SEC-012** | Third-Party Risk Management SOP | Enforces the AUP on vendors via contractual controls. |
| **SOP-DPO-001** | Data Protection Governance (GDPR) | Overlays EU-specific requirements for personal data and legitimate interest. |
| **SOP-HR-004** | Employee Disciplinary Action SOP | The enforcement arm behind the AUP’s sanctions. |
| **SOP-ENG-008** | AI Model Change Management | Governs the acceptable use of training data for clinical AI models. |
| **SOP-CORP-001** | Code of Conduct | Foundational ethics policy, referenced for broad "integrity" obligations. |

### 10.2 External Standards and Regulatory References

| Standard | Reference in this Document |
|---|---|
| **SOC 2 (AICPA TSP Section 100, 2024 Revision)** | CC1.2 (Management Commitment), CC1.4 (Accountability), CC4.1 (Monitoring of Deviations), CC4.2 (Monitoring), CC6.1 (Logical Access), CC9.2 (Vendor Risk Management). |
| **HIPAA Security Rule (45 CFR Part 164, Subpart C)** | § 164.308 (Administrative Safeguards, incl. Sanction Policy), § 164.310 (Physical Safeguards), § 164.312 (Technical Safeguards, incl. Access Control, Audit Controls, Integrity). |
| **HIPAA Privacy Rule (45 CFR Part 164, Subpart E)** | § 164.514 (De-identification of PHI). |
| **EU General Data Protection Regulation (GDPR)** | Art. 5 (Principles), Art. 25 (Data Protection by Design and Default), Art. 32 (Security of Processing). |
| **EU AI Act** | Recital 32, Art. 10 (Data Governance for High-Risk Systems). |
| **NIST SP 800-53 Rev. 5** | Incorporated as a best-practice framework, not a strict compliance mandate, for control catalog alignment. |

---

## 11. Revision History

| Version | Effective Date | Revision Author | Summary of Changes |
|---|---|---|---|
| 4.0 | 2023-10-04 | Michael Chen (former CHRO) | Major revision. Combined former separate Internet Use Policy and Data Handling Policy. Introduced new Data Classification Tiers (Public to Restricted) and RACI matrix. Full policy restructure. |
| 4.1 | 2024-07-22 | Jennifer Walsh (CHRO) | Minor revision. Updated Section 8 (Exception Handling) with new ServiceNow workflow IDs. Added SOC 2 CC9.2 references for third-party risk in Section 6.1. Added role-based training for AI engineers. |
| 4.2 | 2025-06-06 | Jennifer Walsh (CHRO) | Major revision. Incorporated EU AI Act requirements. Updated definitions for Restricted data to explicitly include "CE-marked medical device raw data." Expanded AI and Clinical Model Integrity section (5.4). Updated technical controls to reflect Zscaler Private Access migration and MAM-WE program launch. Annual review completed six weeks early to align with EU MDR CE marking audit. |
| 4.3 | *(Draft in Progress)* | Jennifer Walsh (CHRO) / Anja Vogel (DPO) | Update to incorporate EU-US Data Privacy Framework (EU-US DPF) certification language into Section 1.3 (Jurisdictional Overlay). |

---

**END OF DOCUMENT**

*This document is the property of Meridian Health Technologies, Inc. Unauthorized reproduction, distribution, or use of this document is a violation of SOP-HR-005.*