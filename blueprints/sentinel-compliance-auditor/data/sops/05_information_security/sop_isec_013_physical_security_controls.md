---
sop_id: "SOP-ISEC-013"
title: "Physical Security Controls"
business_unit: "Information Security"
version: "4.4"
effective_date: "2025-10-18"
last_reviewed: "2026-12-19"
next_review: "2027-06-08"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Physical Security Controls

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the physical security controls, protocols, and accountability mechanisms necessary to protect Meridian Health Technologies, Inc. (“Meridian”) personnel, facilities, information assets, and supporting infrastructure from unauthorized physical access, damage, theft, environmental threats, and interference. This document defines the minimum baseline physical security requirements applicable across all Meridian facilities globally and provides the operational framework for implementing, monitoring, and continuously improving physical security controls in alignment with our regulatory obligations, contractual commitments, and enterprise risk appetite.

### 1.2 Scope

This SOP applies to:

| In Scope | Out of Scope |
|---|---|
| All Meridian-owned and leased facilities, including headquarters (Boston), regional offices (London, Berlin, Singapore, Toronto), and any co-location data center suites | Logical access controls for information systems (see SOP-ISEC-002) |
| All Meridian personnel (employees, contractors, temporary workers, interns) | Personal residences of remote/hybrid workers (except as specified for asset protection in Section 5.7) |
| All third-party visitors, vendors, service providers, and guests accessing Meridian facilities | Cloud provider physical infrastructure (addressed via third-party assurance per SOP-TPRM-004) |
| All Meridian-owned information processing equipment, including servers, workstations, networking hardware, and removable media | Business continuity and disaster recovery procedures (see SOP-BCDR-001) |
| Environmental controls supporting Meridian data centers and server rooms | Physical security of SaaS provider data centers (addressed via vendor SOC 2 reports per SOP-TPRM-004) |
| Physical media handling, storage, transportation, and disposal | |

### 1.3 Applicability by Facility Tier

Meridian facilities are classified into three tiers based on the sensitivity of information assets housed and criticality of operations supported. The specific controls applicable to each tier are delineated throughout this SOP.

| Facility Tier | Definition | Example Locations |
|---|---|---|
| **Tier 1 – Critical** | Facilities housing Production systems, PHI/PCI data processing equipment, or primary network infrastructure | Boston HQ Data Center Suite, Boston MDF (Main Distribution Frame), Boston Secure Records Room |
| **Tier 2 – Sensitive** | Facilities where Meridian personnel regularly access, process, or store Internal or Confidential data, but that do not house primary infrastructure | Boston HQ general office areas, London Office, Berlin Office, Singapore Office |
| **Tier 3 – Standard** | Small satellite offices, temporary project sites, or facilities where only Public/Internal data is handled | Toronto Office, Temporary off-site meeting venues (when Meridian-controlled) |

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **ACAMS** | Access Control and Alarm Monitoring System – Meridian’s centralized physical security management platform (Genetec Security Center), deployed across all Tier 1 and Tier 2 facilities. |
| **Badge** | A Meridian-issued proximity or smart card used for electronic access control and visual identification. |
| **BMS** | Building Management System – The centralized environmental monitoring platform (Schneider Electric EcoStruxure) managing HVAC, power, and fire suppression in Tier 1 facilities. |
| **CCTV** | Closed-Circuit Television – The IP-based video surveillance system integrated with ACAMS. |
| **CISO** | Chief Information Security Officer – Rachel Kim, owner of this SOP. |
| **Clean Desk Policy** | The requirement that all sensitive physical documents and portable computing devices be secured when not in use (see SOP-ISEC-008). |
| **CRAC** | Computer Room Air Conditioning – Precision cooling units serving Tier 1 data center environments. |
| **Data Center Suite** | The physically segregated area within Boston HQ housing production servers, storage arrays, and core network infrastructure. |
| **EAC** | Electronic Access Control – Card readers, biometric scanners, request-to-exit (REX) devices, and door controllers managed via ACAMS. |
| **Facilities Manager** | The designated individual responsible for day-to-day operation and maintenance of physical security controls at a specific Meridian site. |
| **FM-200** | The clean agent fire suppression system deployed in the Boston Data Center Suite. |
| **MDF / IDF** | Main Distribution Frame / Intermediate Distribution Frame – Telecommunications rooms housing network switches, patch panels, and structured cabling. |
| **MFA** | Multi-Factor Authentication – For physical access, MFA is defined as Badge (something you have) + Biometric/PIN (something you are/know). |
| **NIST SP 800-88** | National Institute of Standards and Technology Special Publication 800-88, "Guidelines for Media Sanitization," the standard against which Meridian’s media disposal procedures are aligned. |
| **PSIM** | Physical Security Information Management – The ACAMS software platform. |
| **PTZ** | Pan-Tilt-Zoom – A type of high-resolution surveillance camera. |
| **SCIF** | Sensitive Compartmented Information Facility – (Not applicable; included for awareness). |
| **SOC** | Security Operations Center – The 24/7 physical and logical security monitoring function (co-managed with vendor SecureWatch). |
| **UPS** | Uninterruptible Power Supply – Battery-backed power conditioning equipment. |

## 3. Roles and Responsibilities

The following RACI matrix assigns accountability for the key physical security functions described in this SOP.

| Activity / Control Area | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| **Physical Security Strategy & Policy** | CISO (Rachel Kim) | CEO (Dr. Sarah Chen) | VP Infrastructure, General Counsel | Senior Leadership Team |
| **Facility Access Control Operations** | Regional Facilities Managers | VP Infrastructure | CISO, SOC Manager | Site Personnel |
| **Visitor Management** | Site Reception / Security Officers | Regional Facilities Manager | CISO | Host Employee |
| **Environmental Monitoring (Tier 1)** | Data Center Manager (Marcus Chen) | VP Infrastructure | CISO, Facilities Manager | CISO |
| **CCTV Surveillance & Review** | SOC Manager (Priya Patel) | CISO | VP Infrastructure, Legal | Facilities Manager |
| **Secure Media & Equipment Disposal** | IT Asset Manager (David Okafor) | CISO | VP Infrastructure, Compliance Officer | Data Owners |
| **Badge Administration** | HR Operations (for issuance/revocation); Facilities Manager (for access provisioning) | CISO | SOC Manager | Employee, Employee’s Manager |
| **Physical Penetration Testing** | Independent Assessor (Procured by VP of Compliance) | CISO | VP Infrastructure, Facilities Manager | Risk Management Committee |
| **Incident Response (Physical Breach)** | SOC Manager | CISO | VP Infrastructure, Legal, HR | CEO (Dr. Sarah Chen) |

### 3.1 Key Named Role Descriptions

| Role | Designee | Responsibilities Summary |
|---|---|---|
| **Chief Information Security Officer (CISO)** | Rachel Kim | Approver of physical security strategy, exception requests, and major incident response actions. Owner of this SOP. |
| **VP Infrastructure** | Omar Hassan | Accountable for physical infrastructure supporting IT operations; approves changes to Data Center Suite environmental controls. |
| **SOC Manager** | Priya Patel | Oversees 24/7 physical security monitoring, alarm triage, and incident response coordination via the Meridian SOC and SecureWatch partnership. |
| **IT Asset Manager** | David Okafor | Manages the full lifecycle of IT equipment, including secure disposal and chain of custody documentation. |
| **Data Center Manager** | Marcus Chen | Responsible for the day-to-day environmental health and physical security of the Tier 1 Data Center Suite and all MDF/IDF rooms globally. |
| **VP Compliance** | Lena Müller | Ensures physical security control alignment with SOC 2, HIPAA, and contractual obligations; coordinates independent audits. |

## 4. Policy Statements

Meridian Health Technologies is committed to maintaining a secure physical environment that protects the confidentiality, integrity, and availability of its information assets. The following high-level policy statements govern all physical security controls:

1.  **Layered Defense:** All Meridian facilities shall implement a minimum of three physical security layers (perimeter, building, suite/interior) to prevent unauthorized access. Tier 1 facilities shall implement a minimum of five layers.
2.  **Least Privilege:** Access to physical spaces shall be granted based on the principle of least privilege. Personnel shall be provisioned access only to those areas required for their specific job function. Access shall be reviewed quarterly and revoked promptly upon termination or role change.
3.  **Continuous Monitoring:** All ingress/egress points to Tier 1 and Tier 2 facilities, as well as critical interior areas, shall be monitored by electronic access control systems and recorded CCTV with a minimum retention of 90 days.
4.  **Environmental Protection:** Tier 1 data processing environments shall be protected by redundant environmental controls (power, HVAC, fire suppression) with automated alerting for any deviation from defined safe operating thresholds.
5.  **Visitor Accountability:** All visitors shall be registered, positively identified, escorted while in Sensitive areas, and their access period logged. Visitor access shall be limited to the minimum time necessary.
6.  **Secure Disposal:** All information processing equipment and physical media shall be sanitized, destroyed, or securely overwritten in accordance with NIST SP 800-88 guidelines prior to disposal, reuse, or return.
7.  **No Cameras/Recording:** Unauthorized photography, video, or audio recording is prohibited in all Tier 1 and Tier 2 secure areas (Data Centers, MDF/IDF rooms, Secure Records Rooms).

## 5. Detailed Procedures

### 5.1 Facility Access Control

#### 5.1.1 Access Badge Issuance

The HID Global iCLASS SE R90 badging system is used for all Meridian-issued access credentials.

- **New Hire/Contractor:** Upon completion of onboarding in Workday, HR Operations shall trigger a badge issuance request via the ServiceNow "Physical Access Request" (PAR) catalog item. The request must include the individual’s legal name, Meridian ID, photograph (passport-style, submitted by candidate), and designated home site.
- **Provisioning:** The Regional Facilities Manager reviews the PAR, verifies employment status, and provisions the badge with a baseline "General Office" access profile for the assigned site. Any additional access (e.g., Data Center Suite, MDF rooms) requires a separate PAR approved by the individual’s Manager and the CISO. The badge PIN is set by the user during first use at a dedicated enrollment reader.
- **Issuance:** The employee/contractor must present government-issued photo identification to the Facilities representative to receive their badge and sign the "Meridian Access Badge User Agreement" (Form SEC-013-A).
- **Temporary Badges:** Issued for visitors or personnel who have lost their badge. These are pre-configured with a maximum 48-hour active period for standard office access (no Tier 1 access). HR confirmation is required before issuance.

#### 5.1.2 Access Control Zones

Meridian Boston HQ utilizes the following layered access zones managed via ACAMS:

- **Zone 0 – Public (Perimeter):** Building lobby, exterior walkways. No Meridian badge required during business hours.
- **Zone 1 – Reception:** Meridian-suite glass doors. Accessible via badge or receptionist remote release during business hours (08:00–18:00 local).
- **Zone 2 – General Office:** Open-plan work areas, kitchens, meeting rooms. Badge + PIN required at all times.
- **Zone 3 – Secure Corridor:** Hallways leading to Zone 4 and 5 areas. Badge + Biometric (Fingerprint) authentication required.
- **Zone 4 – Data Center Suite & MDF Rooms:** Mantrap interlock. Badge + Biometric + PIN (MFA). Access logged and reviewed weekly.
- **Zone 5 – Secure Records Room:** Badge + Biometric. Access limited to approved Records Management and Compliance personnel.

#### 5.1.3 Quarterly Access Reviews

The SOC Manager, in coordination with Regional Facilities Managers, shall generate an "Access Zone Entitlement Report" from ACAMS on the first business day of each fiscal quarter (January, April, July, October). The report shall list all badge holders with access to Zone 3, 4, and 5 areas.

- **Action:** The report shall be distributed to each Department Head (VP-level and above). They must certify by the 15th of the month that all access for their direct reports is still job-function appropriate. Any non-response or non-certification shall result in the temporary suspension of Zone 3+ access for that department until certification is received.
- **Revocation:** Revoked access must be processed in ACAMS within 4 business hours of approval.

### 5.2 Visitor Management

All non-Meridian personnel entering Meridian facilities beyond Zone 0 must be managed via the secure visitor management module of ACAMS, integrated with ServiceNow.

1.  **Pre-Registration:** The Meridian Host must pre-register the visitor via the ServiceNow "Visitor Access Request" form a minimum of 24 business hours in advance. The form captures: Visitor Full Name, Organization, Citizenship, Government ID Type/Number, Host Name, Purpose of Visit, Date/Time of Arrival, and any equipment being brought on-site.
2.  **Approval:** The Host’s Manager receives the automated approval request. For visitors requiring access to Zone 2 or above, the CISO or SOC Manager must co-approve.
3.  **Arrival and Check-In:** At the Zone 1 Reception desk, the visitor presents their government ID. The Security Officer verifies the ID against the pre-registered information, photographs the visitor, and issues a color-coded "VISITOR" badge via the ACAMS Visitor Kiosk. The badge is automatically configured to expire at the end of the approved access window (maximum 8 hours).
4.  **Escort:** The Meridian Host is automatically notified (via MS Teams and SMS) of their visitor’s arrival. The Host must meet the visitor in the Reception area and escort them at all times while in Zone 2 and above.
5.  **Tailgating Policy:** Every individual is responsible for passing through access-controlled portals individually. "Piggybacking" or tailgating is strictly prohibited. Security Officers and all personnel are empowered to courteously challenge any unbadged or unknown individual.
6.  **Check-Out:** The visitor must return their badge to the Reception desk upon departure. The Host is responsible for ensuring their visitor properly checks out. A visitor log, including check-in/check-out timestamps, is maintained in ACAMS and retained for a minimum of one year.

### 5.3 Secure Work Areas

In accordance with the Clean Desk Policy (SOP-ISEC-008), the following controls are implemented:

- **Document Storage:** All physical documents classified as "Internal" or "Confidential" must be stored in lockable cabinets when not in active use and always outside of business hours. Documents classified as "Restricted" (e.g., containing PHI) must be double-locked (e.g., locked cabinet within a badge-access-controlled room).
- **Secure Printing:** Printers in Zone 2 areas use "Secure Print Release" technology. A document is held in the print queue until the originator badges into the printer’s reader.
- **Server Rooms (IDF/MDF):** All cabling is managed in overhead trays. Racks are kept locked. No cardboard, paper, or combustible materials are permitted in any MDF/IDF room. A quarterly "MDF/IDF Cleanliness Audit" is conducted by the Data Center Manager.

### 5.4 Environmental Controls (Tier 1 – Data Center Suite)

#### 5.4.1 Temperature and Humidity

Inlet air temperature to server racks shall be maintained at 24°C ± 2°C. Relative humidity shall be maintained at 45% ± 10%.

- **Monitoring:** Wireless sensors (AKCP Wireless Tunnel) are deployed at the front and rear of every third rack. Telemetry data is aggregated in the BMS and displayed in the SOC dashboards.
- **Alerts:**
    - **Warning Alert:** When temperature at any single inlet sensor exceeds 27.5°C or drops below 21.5°C for more than 5 minutes. A notification is sent to the Data Center Manager and SOC via MS Teams and email.
    - **Critical Alert:** When temperature at any single inlet sensor exceeds 29°C or drops below 18°C. This triggers an audible alarm in the SOC and an automated push notification to the on-call Data Center Facility Engineer (via PagerDuty). The on-call Engineer must acknowledge and begin investigation within 15 minutes of the alert.

#### 5.4.2 Power Systems

- **Primary Power:** Redundant utility feeds from separate substations enter through Automatic Transfer Switches (ATS).
- **UPS:** A Liebert N+1 redundant UPS system provides conditioned battery power. At 75% battery runtime remaining (estimated 10 minutes of full load), an automated graceful shutdown sequence for non-critical systems is initiated. At 20% runtime remaining, critical system shutdown begins.
- **Backup Generator:** Two 2MW diesel generators with a minimum 72-hour fuel supply at full load. Monthly load-testing under simulated failure is conducted by the Facilities Manager; results are logged in the Meridian Maintenance Management System (MegaMation).

#### 5.4.3 Fire Detection and Suppression

- **Detection:** Very Early Smoke Detection Apparatus (VESDA) aspirating smoke detection system provides Zone 4 with multi-level alerting (Alert, Action, Fire1, Fire2).
- **Suppression:** FM-200 clean agent system. Activation is automatic upon a "Fire1" trigger from two separate VESDA zones, but a 30-second pre-discharge delay is active, allowing for manual abort via an emergency stop button (E-Stop) located at the single egress door from the suite. Activation of the FM-200 system immediately triggers an emergency shutdown of all non-essential electrical power in the suite.

### 5.5 Secure Equipment and Media Disposal

All Meridian-owned IT assets and media must be tracked, degaussed, shredded, or wiped following this formal chain of custody, managed via the ServiceNow "Asset Retirement" workflow.

#### 5.5.1 Decommissioning and Sanitization Categories

| Category | Media Types | Approved Sanitization Method |
|---|---|---|
| **Category A: Electronic Media (Reuse)** | Server hard drives, SSDs, workstations being redeployed within Meridian | **Purge:** NIST SP 800-88 Rev. 1 compliant cryptographic erase using the onboard drive firmware (for self-encrypting drives), or, if unavailable, a single-pass overwrite using Tableau TD4 forensic imagers. The crypto-erase validation key must be logged. |
| **Category B: Electronic Media (Disposal/End-of-Life)** | All failed HDDs/SSDs, tape media (LTO, DLT), endpoint devices that are obsolete | **Destroy:** Physical destruction via a SEM Model 344 hard drive shredder, reducing media to particles no larger than 20mm edge dimension. Failed drives incapable of crypto-erase are immediately placed in a dual-lock "Destruction Holding" safe before weekly batch destruction. |
| **Category C: Paper/Physical Media** | All paper documents containing PHI, PCI cardholder data, or classified as "Confidential" | **Cross-Shred:** Cross-cut shredders located in secure copy rooms. Level P-5 shredding is required. |
| **Category D: Networking Equipment** | Routers, switches, firewalls | **Factory Reset & Purge:** Configuration files must be zeroized. A factory reset must be performed. For devices containing flash memory, Category A methods apply. |

#### 5.5.2 Disposal Procedure

1.  **Initiation:** IT Asset Manager (David Okafor) generates a "Disposal List" from the ServiceNow CMDB for all assets marked for end-of-life.
2.  **Physical Collection:** Designated Data Center Technicians physically locate the assets. Each asset’s barcode is scanned, and its status in ServiceNow is updated to `Pending Decommission`. Assets are physically segregated into a secure, caged "Decommission Zone" within the Boston Receiving Bay.
3.  **Sanitization:** An authorized technician, separate from the individual who decommissioned the server, performs the sanitization method as dictated by the asset’s category.
4.  **Verification:** For Category A (Purge) methods, a 10% random sample of wiped media is verified using a Tableau forensic bridge to confirm no readable data remains. Verification results are logged against the asset tag in ServiceNow.
5.  **Certification & Hand-off:** Upon successful sanitization/verification, the IT Asset Manager digitally signs the "Certificate of Media Sanitization" (ServiceNow record, Form SEC-013-B). The asset’s status is changed to `Decommissioned – Awaiting E-Waste`. Only after this step are the physical assets released to the approved, ISO 14001-certified e-waste recycling vendor (currently: ERI, Inc.). A Meridian employee must witness the loading of all media-bearing assets into the vendor’s secured, covered transport vehicle.

### 5.6 Workstation and Portable Device Security

- All workstations shall be physically secured to the desk or workstation with a Kensington lock or similar anchored cable kit.
- Personnel are prohibited from leaving laptops, tablets, or smartphones unattended in public areas. In all Meridian facilities and when traveling, devices must be stored out of sight or secured in a locked drawer.
- When a workstation is unattended, the user must lock the session (`Win + L` / equivalent).

### 5.7 Personal and Home Office Security

While personal residences are out of scope for facility-level controls, personnel accessing Meridian data from a home office must adhere to the following minimum controls, as established in the Telecommuting Policy (SOP-HR-019):

- Meridian-provided workstations must be situated in a dedicated, non-public area of the residence.
- Paper documents containing Internal or higher classification data must not be placed in unsecured home recycling bins. A cross-shredder, provided by Meridian upon request, must be used.

## 6. Controls and Safeguards

This section details physical safeguards mapped to specific regulatory and control framework requirements, demonstrating Meridian's commitment to robust, auditable controls.

### 6.1 Control Mapping: SOC 2 Trust Services Criteria (TSC 2017, with 2022 revision mapping)

Meridian’s physical security controls are primarily designed to meet the SOC 2 Common Criteria (CC6 series) and, where applicable, the Availability criteria (A1.x series). The following table provides thorough coverage of our physical SOC 2 controls.

| Control ID | SOC 2 Criteria Reference | Meridian Safeguard Implementation |
|---|---|---|
| **PHY-01** | **CC6.1 / CC6.2 (Logical and Physical Access Controls)** | **Layered Perimeter Defense:** The five-zone access control model (Section 5.1.2) ensures no single compromised credential grants access to Critical assets. The Zone 4 mantrap physically isolates threat actors and enforces MFA. |
| **PHY-02** | **CC6.1** | **Annual Physical Penetration Test:** The CISO shall engage an independent, licensed physical security firm (currently: Bishop Fox) to conduct a no-notice, covert penetration testing exercise against Boston HQ, including social engineering and tailgating attempts. The test report and remediation plan shall be presented to the Risk Management Committee within 30 days. |
| **PHY-03** | **CC6.1** | **Biometric MFA for Tier 1:** Access to the Data Center Suite (Zone 4) requires a valid Badge (contactless smart card with MIFARE DESFire EV3 chip), a 6-digit PIN, and a live fingerprint scan matched against the ACAMS biometric server. Stored fingerprint data is encrypted at rest via AES-256. |
| **PHY-04** | **CC6.3 (Restrict Access)** | **Quarterly Access Recertification:** The procedure defined in Section 5.1.3 is the formal control enforcing least privilege for physical access. The VP Compliance (Lena Müller) includes a report on recertification timeliness and any associated findings in the quarterly GRC review with the CISO. |
| **PHY-05** | **CC7.1 (Detection of Anomalies)** | **CCTV with Video Analytics:** 1080p PTZ cameras are deployed at all ingress/egress points of Zone 1 and above, loading bays, and Data Center Suite interior. The Genetec video analytics module is configured to detect and flag anomalous motion (e.g., loitering, object left behind, camera tampering) and generate an alert in the SOC. All footage is retained in a RAID-60 storage array for a minimum of 90 days, with forensic copies for critical incidents retained indefinitely. Time synchronization with pool.ntp.org ensures legal admissibility. |
| **PHY-06** | **CC7.3 (Incident Response)** | **Physical Incident Response Runbook:** A detailed runbook is maintained in the Meridian Incident Management System (ServiceNow GRC module). Runbook triggers include: Duress alarm activation, forced door alarm sustained for >10 seconds, Zone 4 mantrap interlock alarm, and VESDA Fire2 alert. The runbook assigns specific investigation and containment tasks to the SOC Manager (Priya Patel), VP Infrastructure (Omar Hassan), and CISO (Rachel Kim) within SLA timelines (15 min acknowledge, 4 hrs. containment). |
| **PHY-07** | **A1.2 (Environmental Protections)** | **Redundant Environmental Controls:** As detailed in Section 5.4, the N+1 redundant UPS, 2N CRAC units, and generator with 72-hour fuel contract (with AmeriGas, verified annually) ensure continuous operation. The BMS maintains a real-time operational log of all environmental telemetry with 365-day retention. |
| **PHY-08** | **A1.2** | **Annual Generator Load Test:** The monthly test (Section 5.4.2) is supplemented by an annual, simulated, full building load test where the Data Center Suite runs exclusively on generator power for 4 hours. This test is overseen by the VP Infrastructure and an authorized electrical contractor. |
| **PHY-09** | **PI1.4 (Disposal of Information)** | **NIST SP 800-88 Data Sanitization:** We do not make operational decisions solely based on media classification labels—our controls follow NIST methodology. The formal chain of custody and sanitization verification procedures detailed in Section 5.5 ensure complete media destruction for end-of-life assets. The 10% verification sample is documented in ServiceNow. The separate, dual-locked destruction holding area ensures security for failed drives. |
| **PHY-10** | **CC6.6 (External Threats)** | **Bollards & Anti-Ram Barriers:** The Boston HQ loading bay and Data Center Suite exterior wall facing the public road are protected by K12-rated anti-ram bollards. Perimeter fence integrity (where applicable) is checked weekly by Facilities. |

### 6.2 HIPAA Physical Safeguards Coverage

Meridian implements physical safeguards to ensure the confidentiality, integrity, and availability of electronic Protected Health Information (ePHI) in the Data Center Suite and associated facilities, in support of our HIPAA Security Rule obligations. The following physical controls are in place:

- **Facility Access Controls (45 CFR §164.310(a)(1)):** The layered zone access model (Section 5.1.2), quarterly access reviews, and mandatory multi-factor authentication for data center access directly support HIPAA facility access requirements. Meridian maintains a formal, documented process for granting, reviewing, and revoking physical access privileges.
- **Workstation Security (45 CFR §164.310(b)):** The Clean Desk Policy, physical locks for workstations, and session-locking procedures (Section 5.6) restrict unauthorized access to workstations that may hold or provide access to ePHI.
- **Device and Media Controls (45 CFR §164.310(d)(1)):** Procedures for the disposal and final disposition of hardware and electronic media containing ePHI are detailed in Section 5.5. All such disposal actions are formally tracked and authorized within the ServiceNow CMDB. Movement of hardware and media containing ePHI to and from the Data Center Suite is tracked by the SOC.

## 7. Monitoring, Metrics, and Reporting

The effectiveness of physical security controls is continuously monitored and formally reported to demonstrate compliance and drive improvement.

### 7.1 Key Performance Indicators (KPIs)

| Metric | KPI Target | Measurement Location | Responsible Owner |
|---|---|---|---|
| **Quarterly Access Recertification Completion** | 100% completion by Day 15 of the fiscal quarter | ACAMS & ServiceNow Dashboard | CISO (Rachel Kim) |
| **Time to Revoke Access (Post-Termination)** | < 4 hours from Workday termination event to ACAMS deactivation | Automated integration between Workday, ServiceNow, and ACAMS. | HR Operations / SOC Manager |
| **MDF/IDF Cleanliness Audit Score** | ≥ 95% on quarterly audit checklist | MegaMation Maintenance System | Data Center Manager (Marcus Chen) |
| **Critical Environmental Alert MTTA (Mean Time to Acknowledge)** | < 15 minutes | PagerDuty & BMS | VP Infrastructure (Omar Hassan) |
| **Visitor Management Compliance** | <2% deviation; monthly audit of Visitor Access Requests vs. actual ACAMS visitor log | ACAMS Visitor Management module | Regional Facilities Manager |
| **Asset Disposal Chain of Custody Deviation** | Zero (0) instances of assets released to vendor without completed Form SEC-013-B | ServiceNow IT Asset Management module | IT Asset Manager (David Okafor) |

### 7.2 Reporting Cadence

- **SOC Real-Time Dashboard:** Continuously staffed. Monitors all Zone 3+ door forced/open-too-long alarms, duress alarms, and Tier 1 critical environmental alerts.
- **Monthly Security Operations Report:** The SOC Manager (Priya Patel) compiles a report summarizing all physical security alarms (false/real), visitor volume, tailgating incident reports, and key metric dashboards. Distributed to the CISO and VP Infrastructure.
- **Quarterly Physical Security Review:** The CISO presents the KPI dashboard, recent audit findings, exception log (Section 8), and any new or emerging physical threats to the Enterprise Risk Management Committee (Chair: CEO Dr. Sarah Chen).
- **Annual SOC 2 & HIPAA Audit:** Independent, external auditors (currently: Schellman & Company, LLC) perform an integrated physical security audit. This includes facility walk-throughs, control testing, record sampling (badge reports, disposal certificates), and interviews with key roles.

## 8. Exception Handling and Escalation

### 8.1 Requesting an Exception

Operational or business requirements may occasionally necessitate a temporary deviation from a control detailed in this SOP. A formal exception process is required.

1.  **Request Submission:** The requestor’s Manager shall submit a "Physical Security Control Exception Request" via the ServiceNow GRC module. The request must clearly state the specific control (e.g., PHY-01, badge MFA for a one-time maintenance event), the business justification, an analysis of associated risk, and compensating controls to be implemented for the duration of the exception.
2.  **Risk Assessment:** The CISO (or delegate) will review the request and conduct a formal risk assessment. Requests for exception to controls in Zone 4 (Data Center Suite) automatically trigger a high-risk assessment.
3.  **Approval Authorities:**
    - Exceptions affecting Zone 0-2, with a duration of ≤7 days: **CISO Approval.**
    - Exceptions affecting Zone 3-5, or any exception with a duration >7 days: **CISO and CEO (Dr. Sarah Chen) Approval.**
    - Exceptions extending beyond 90 days are not permitted. A permanent risk acceptance or project for control redesign must be initiated.

### 8.2 Emergency Escalation (Physical Breach / "Incident")

In the event of a suspected or confirmed physical security incident (e.g., unauthorized access, theft of equipment, environmental failure leading to data center damage), the "Physical Incident Response Runbook" is activated. The communication and escalation path is as follows:

1.  **Triage & Immediate Containment (0-60 min):** SOC Manager (Priya Patel) acknowledges the automated alarm or manual report. She dispatches on-site security or a Data Center Technician per runbook procedures and places a P1 incident call with SecureWatch.
2.  **Crisis Notification (<4 hours):** After initial containment is achieved, the SOC Manager sends a "P1 Physical Incident Notification" via the corporate notification tree, immediately alerting the CISO (Rachel Kim), VP Infrastructure (Omar Hassan), General Counsel, and the Head of Internal Communications. If the incident involves potential PHI exposure, the VP Compliance (Lena Müller) must be notified within 1 hour.
3.  **Executive Escalation:** The CISO is responsible for notifying the CEO (Dr. Sarah Chen) and the Chair of the Audit Committee within 24 hours if the incident severity is rated Critical (e.g., successful breach of Zone 4, confirmed asset theft from a secured area).

## 9. Training Requirements

All personnel must be equipped with the knowledge to uphold Meridian's physical security posture. Training requirements are managed and tracked via the Workday Learning Management System.

1.  **New Hire Onboarding (SOP-HR-015):** All new employees and contractors must complete the “Meridian Security Awareness: Physical Access” course (Module ISEC-013-TRN-01) within their first 5 business days. The 20-minute course covers tailgating policy, clean desk, visitor escort responsibilities, and how to report suspicious activity.
2.  **Annual Security Awareness Training:** The physical security module is included in the mandatory annual refresher course (ISEC-ALL-TRN-01). Completion is required by October 31st each year with a 99% completion target.
3.  **Role-Based Specialized Training:**
    - **SOC Operators & Facilities Managers:** Must attend biannual, hands-on PSIM (ACAMS) and BMS operational training.
    - **Data Center Technicians:** Must complete formal training on VESDA alarm response, FM-200 emergency abort procedures, and the Asset Retirement workflow chain-of-custody process.
4.  **Phishing & Tailgating Drills:** The SOC team, in coordination with HR, will conduct biannual physical tailgating tests ("red team lite") at main entrance points and data center doors. Results, including successful interventions by vigilant employees, are anonymized and shared in a company-wide "Security Spotlight" communication.

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Document Title |
|---|---|
| SOP-ISEC-002 | Information Security: Logical Access Controls |
| SOP-ISEC-008 | Information Security: Clean Desk and Clear Screen Policy |
| SOP-ISEC-011 | Information Security: Cryptographic Key Management |
| SOP-ISEC-015 | Information Security: Incident Response Management |
| SOP-TPRM-004 | Third-Party Risk Management: Vendor SOC Report Review |
| SOP-BCDR-001 | Business Continuity & IT Disaster Recovery Planning |
| SOP-HR-015 | Human Resources: New Hire Onboarding & Orientation |
| SOP-HR-019 | Human Resources: Telecommuting and Remote Work Policy |
| SOP-FAC-001 | Facilities: Preventative Maintenance Program |

### 10.2 External Standards and Regulations

- **SOC 2:** AICPA Trust Services Criteria (TSC 2017, Revised 2022): Common Criteria CC6.1–CC6.8, CC7.1–CC7.5, and Availability Criteria A1.1–A1.3.
- **HIPAA:** U.S. Department of Health and Human Services 45 CFR Part 164, Subpart C – Security Standards for the Protection of Electronic Protected Health Information, Section §164.310 (Physical Safeguards).
- **NIST SP 800-53r5:** Security and Privacy Controls for Information Systems and Organizations (PE Family of controls).
- **NIST SP 800-88r1:** Guidelines for Media Sanitization.
- **ISO/IEC 27002:2022:** Controls 7.1–7.14 (Physical Security).
- **PCI DSS v4.0:** Requirement 9: Restrict physical access to cardholder data.

## 11. Revision History

| Version | Date | Author / Editor | Summary of Changes |
|---|---|---|---|
| 4.4 | 2026-12-19 | R. Kim, CISO | Minor revision; updated NIST 800-88 reference to Rev. 1; added clarification on 10% media verification sample size; updated CISO name spelling. |
| 4.3 | 2026-08-22 | P. Patel, SOC Manager | Updated escalation paths for new SOC structure; replaced "DataLocker" with secure Decommission Zone in loading bay; enhanced visitor badge language for clarity. |
| 4.2 | 2026-03-15 | O. Hassan, VP Infra. | Major revision of Section 5.4, Environmental Controls; commissioned new generator fuel contract; updated all references from Brivo to Genetec ACAMS after migration. |
| 4.1 | 2025-10-18 | R. Kim, CISO | Full SOP review and re-write for version 4; integrated new Toronto office as Tier 3; merged previous SOPs on Disposal and Visitor Management; aligned all controls to 2022 TSC mapping. |
| 3.2 | 2024-05-11 | J. Martinez, former CISO | Updated role-based training requirements; minor grammatical fixes. |

---

**APPENDIX: Forms and Templates**

- **Form SEC-013-A:** Access Badge User Agreement (Available in ServiceNow Knowledge Base).
- **Form SEC-013-B:** Certificate of Media Sanitization (Digital record generated within ServiceNow Asset Retirement workflow).
- **Form SEC-013-C:** MDF/IDF Cleanliness Audit Checklist (Managed in MegaMation).