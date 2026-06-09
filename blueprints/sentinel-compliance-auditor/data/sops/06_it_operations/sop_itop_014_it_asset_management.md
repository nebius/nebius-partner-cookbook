---
sop_id: "SOP-ITOP-014"
title: "IT Asset Management"
business_unit: "IT Operations & Infrastructure"
version: "4.9"
effective_date: "2025-06-07"
last_reviewed: "2026-08-13"
next_review: "2027-02-23"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: IT Asset Management

## 1. Purpose and Scope

**Purpose**
This Standard Operating Procedure (SOP) establishes the framework for the end-to-end management of all Information Technology (IT) assets owned, leased, or operated by Meridian Health Technologies, Inc. (“Meridian” or “the Company”). The objective of this SOP is to maintain an accurate inventory of all IT assets, optimize asset utilization and cost, enforce security and compliance controls, and manage assets securely through their entire lifecycle—from procurement through disposal—in alignment with regulatory obligations and industry frameworks.

**Scope**
This SOP applies to all Meridian personnel, contractors, consultants, temporary workers, and third-party service providers who procure, deploy, manage, transfer, or dispose of any IT asset that connects to, stores, processes, or transmits Meridian data. All business units and all geographic locations, including Meridian’s global offices in Boston (HQ), London, Berlin, Singapore, and Toronto, are within scope.

**In-Scope Asset Categories**

| Asset Category | Description | Examples |
|----------------|-------------|----------|
| End-User Computing (EUC) | Devices assigned to individual users | Laptops, desktops, workstations, tablets, smartphones |
| Infrastructure Hardware | Data center and server room equipment | Servers, storage arrays, network switches, routers, firewalls, load balancers, backup appliances |
| Software Assets | Licensed software and cloud subscriptions | Operating systems, productivity suites, development tools, SaaS platforms, AI/ML platforms |
| Cloud Resources | IaaS/PaaS resources provisioned in public cloud | AWS EC2 instances, S3 buckets, Azure VMs, Snowflake warehouses |
| Media and Removable Storage | Portable storage devices and media | USB drives, external hard drives, backup tapes, optical media |
| Specialized Clinical Hardware | Devices supporting clinical and AI workloads | GPU clusters for ML training, medical-grade displays, DICOM workstations |
| Mobile and Peripheral Devices | Ancillary device assets | Printers, scanners, monitors, docking stations, VoIP phones |

**Out-of-Scope Items**
- Physical facility infrastructure not connected to Meridian networks (e.g., HVAC controllers managed by facilities, physical security access control panels managed by Physical Security).
- Personally owned devices not enrolled in Meridian’s Mobile Device Management (MDM) or Bring Your Own Device (BYOD) program.
- Assets owned entirely by third-party vendors and not used to store, process, or transmit Meridian data.

**Regulatory Drivers**
This SOP is designed to support compliance with:
- **SOC 2 (Service Organization Control 2):** Addresses the Common Criteria for security, availability, and confidentiality, specifically CC3.2 (system operations), CC4.1 (monitoring), CC6.1 (asset inventories), CC6.2 (access controls tied to asset classification), and CC7.1 (incident detection through asset monitoring).
- **HIPAA (Health Insurance Portability and Accountability Act):** Implements the administrative, physical, and technical safeguards required under the HIPAA Security Rule (45 CFR §§ 164.308–164.312), with particular emphasis on § 164.310(d)(1) – Device and Media Controls, including asset disposal and reuse, and § 164.310(d)(2) – Accountability for hardware and electronic media containing electronic Protected Health Information (ePHI).

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|----------------|------------|
| **AITR** | Authorized IT Requester – A manager or above authorized to submit IT procurement requests within their cost center |
| **AWS** | Amazon Web Services, Meridian’s primary public cloud provider |
| **BYOD** | Bring Your Own Device – Meridian’s program allowing personal devices to access corporate email and approved applications under MDM policy |
| **CMDB** | Configuration Management Database – Meridian’s system of record for IT asset configuration items, implemented in ServiceNow |
| **Custodian** | The individual assigned primary physical custody and accountability for an IT asset |
| **Disposal Ticket** | A ticket in ServiceNow of category “IT Asset Disposal” that tracks approvals, data sanitization validation, and chain-of-custody documentation |
| **ePHI** | Electronic Protected Health Information as defined under HIPAA (45 CFR § 160.103) |
| **EUC** | End-User Computing device |
| **Full-Lifecycle Asset** | Any asset tracked from requisition through disposal, receiving unique Meridian Asset Tag or cloud resource identifier |
| **HIA** | High-Impact Asset – An asset whose compromise, unavailability, or unauthorized access would cause a Significant Security Incident, as classified per SOP-ISMS-003 (Asset Classification and Handling) |
| **ITAM** | IT Asset Management |
| **Jamf Pro** | Meridian’s enterprise Apple device management platform for macOS and iOS assets |
| **LCM** | Lifecycle Management |
| **Meridian Asset Tag (MAT)** | A unique, scannable barcode and alphanumeric identifier assigned to each physical IT asset at intake |
| **NIST SP 800-88** | NIST Special Publication 800-88 Revision 1, “Guidelines for Media Sanitization” – Meridian’s standard for media sanitization |
| **Procurement Gateway** | The Oracle Fusion Cloud procurement platform through which all IT purchase requisitions are processed |
| **RACI** | Responsible, Accountable, Consulted, Informed – A responsibility assignment matrix |
| **ServiceNow** | Meridian’s enterprise IT Service Management (ITSM) and Configuration Management Database (CMDB) platform |
| **SOC 2** | Service Organization Control 2, as defined by the AICPA Trust Services Criteria |
| **Terraform** | Infrastructure-as-Code tool used by Meridian Cloud Engineering to provision and tag cloud resources |
| **VAR** | Value-Added Reseller |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| Activity / Decision | IT Asset Manager | VP, IT Operations (Owner) | SOC, InfoSec | End-User / Custodian | Procurement | Cloud Engineering | Legal & Compliance |
|----------------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Procurement Approval (<$50K) | R | A | C | I | C | I | – |
| Procurement Approval (≥$50K) | C | R | I | – | C | I | A |
| Asset Intake, Tagging & Registration | R | A | C | I | I | C | – |
| Annual Physical Inventory | R | A | I | I | – | – | – |
| ePHI Asset Classification | C | C | A | R | – | C | R |
| Software License Compliance Review | R | A | – | – | – | – | C |
| Asset Transfer / Reassignment | R | A | I | C | – | – | – |
| Asset Disposal Sanitization Approval | C | C | R | – | – | – | A |
| HIA Disposal Verification | I | I | R | – | – | – | A |
| Cloud Resource Tagging | I | C | A | – | – | R | – |

### 3.2 Named Role Descriptions

| Role | Assignment | Responsibilities |
|------|------------|------------------|
| **VP, IT Operations (Owner)** | Samantha Torres | Ultimate accountability for all IT asset management processes; approves asset management budget; final escalation authority for asset disposal holds and policy exceptions |
| **IT Asset Manager** | [Designated Full-Time FTE reporting to Samantha Torres] | Day-to-day operational ownership of the ITAM program; maintains CMDB asset integrity; conducts quarterly asset reconciliations; manages software license compliance; approves asset disposal requests up to $50K residual value; oversees physical inventory |
| **Senior Director, Information Security** | Reports to CISO | Approves classification of High-Impact Assets (HIAs); verifies data sanitization for assets containing ePHI; approves cryptographic erasure methods; conducts semi-annual asset disposal audits |
| **Procurement Manager, IT** | Reports to VP, Procurement | Routes all IT purchase requisitions through approved VARs; ensures assets are received against purchase orders in Oracle Fusion; triggers intake ticket creation in ServiceNow |
| **Cloud Engineering Manager** | Reports to David Park, VP, Engineering | Ensures Terraform manifests include mandatory tagging; manages cloud resource lifecycle automation; enforces cloud asset tagging compliance through AWS Config and ServiceNow Cloud Discovery |
| **End-User / Custodian** | All personnel assigned an asset | Maintains physical custody of assigned asset; reports loss, theft, or damage within 4 hours; returns asset upon termination or reassignment; completes Annual Asset Attestation form |
| **Facilities Coordinator** | Regional Office Manager | Receives physical shipments at loading dock; notifies IT Intake within 4 hours of delivery; maintains secure staging area for incoming IT hardware |
| **Legal & Compliance Counsel** | Office of the General Counsel | Approves disposal holds related to litigation or investigation; provides regulatory guidance on data sanitization requirements |

---

## 4. Policy Statements

Meridian Health Technologies, Inc. maintains the following policy commitments governing IT Asset Management:

1. **Complete Asset Inventory:** All IT assets that store, process, or transmit Meridian data SHALL be inventoried in the ServiceNow CMDB. The inventory SHALL be refreshed through automated discovery and manual reconciliation processes to maintain accuracy. Physical assets SHALL be uniquely identified by a scannable Meridian Asset Tag (MAT).

2. **Classification at Intake:** Every IT asset SHALL be classified according to its data sensitivity and system criticality using the classification schema in SOP-ISMS-003. Assets that store, process, or transmit ePHI SHALL be designated as Restricted-class assets and tracked with a special ePHI flag in the CMDB.

3. **Procurement Controls:** All IT asset procurement SHALL route through the Procurement Gateway with IT Asset Manager approval prior to purchase order issuance. No IT asset may be purchased outside the approved procurement workflow or expensed via personal reimbursement.

4. **Lifecycle Tracking:** Every in-scope IT asset SHALL have its full lifecycle recorded in ServiceNow, including procurement date, assignment history, maintenance records, and disposal date. Status transitions SHALL be documented with timestamp and actor identity.

5. **License Management:** Software license entitlements SHALL be tracked against deployments. Meridian SHALL maintain license compliance within vendor grant periods. Under-licensed deployments exceeding 30 days SHALL be escalated to the VP, IT Operations for remediation funding authorization.

6. **Secure Disposal:** All IT assets containing Meridian data SHALL undergo validated data sanitization prior to disposal, reuse, or return to vendor, consistent with SOP-ISMS-007 (Media Sanitization and Disposal). Assets containing ePHI require specific HIPAA-compliant disposal procedures as detailed in Section 5.6.

7. **Availability Commitment:** Meridian commits to managing IT assets supporting critical business services such that asset-related disruptions are minimized. Hardware refresh cycles for infrastructure supporting critical clinical and corporate services SHALL be planned and executed on vendor-supported configurations.

8. **Monitoring and Detection:** Meridian SHALL monitor IT assets for unauthorized configuration changes, security violations, and performance anomalies through automated tools. Monitoring data informs the asset health dashboard reviewed at the weekly IT Operations standup.

9. **Annual Attestation:** All personnel assigned an IT asset SHALL complete an Annual Asset Attestation confirming physical custody and condition of assigned assets.

---

## 5. Detailed Procedures

### 5.1 Asset Procurement

#### 5.1.1 Requisition Initiation

1. The Authorized IT Requester (AITR) navigates to the **Meridian ServiceNow Service Portal** → **IT Asset Management** → **Request New IT Asset**.
2. The AITR completes the **IT Asset Requisition Form (Form ITAM-001)** which captures:
   - Requester name, department, and cost center code
   - Business justification narrative
   - Asset category and preferred specifications
   - Whether the asset will process or store ePHI
   - Target assignee/user (if pre-assigned)
   - Timeline requirement (Standard: 10 business days; Expedited: 3 business days)
3. Requisitions exceeding **$5,000** require cost center manager approval within the workflow.
4. Requisitions exceeding **$50,000** require VP, IT Operations and VP, Procurement co-approval.
5. All requisitions are routed to the **Procurement Manager, IT** for vendor selection and quotation.

#### 5.1.2 Purchase Order Processing

1. The Procurement Manager selects from Meridian’s pre-approved IT VARs:
   - **CDW Government LLC** (primary for EUC and infrastructure)
   - **SHI International Corp** (secondary for software licensing)
   - **Apple Education / Enterprise** (for macOS/iOS devices)
2. Quotations are attached to the ServiceNow requisition record.
3. Upon IT Asset Manager approval, the requisition is converted to a **Purchase Requisition** in Oracle Fusion Cloud.
4. Procurement issues the Purchase Order. The Procurement Manager records the **PO Number** in ServiceNow.
5. ServiceNow creates a pending **Asset Record** in `State = "On Order"`.

### 5.2 Asset Intake and Tagging

#### 5.2.1 Physical Receipt

1. The **Facilities Coordinator** at the receiving location takes custody of shipped assets against the packing slip.
2. Within **4 business hours** of delivery, the Facilities Coordinator opens a **Receiving Ticket** in ServiceNow: ITAM → Receiving → Log Shipment Received. The packing slip is attached.
3. The IT Asset Manager reviews the ticket, verifies against the open PO record, and dispatches an **IT Technician** for inspection and tagging.

#### 5.2.2 Inspection and Baseline Configuration

1. The IT Technician inspects physical condition and verifies specifications against the PO.
2. For EUC devices: the Technician imports the device serial number into **Jamf Pro** (macOS/iOS) or **Microsoft Intune** (Windows) and applies the Meridian baseline configuration profile per SOP-EUC-002 (Endpoint Configuration Baseline).
3. The device is joined to the `corp.meridianhealth.com` domain or enrolled in MDM.
4. Meridian’s **Endpoint Security Agent** (CrowdStrike Falcon) is installed and validated.
5. Full-disk encryption (FileVault2 for macOS; BitLocker for Windows) is enabled and the recovery key is escrowed to the Jamf Pro or Intune record.

#### 5.2.3 Tagging and Registration

1. The Technician affixes a durable **Meridian Asset Tag (MAT)** with scannable barcode and human-readable identifier. Tag format: `MAT-{Region}-{YYYY}-{NNNNNN}` (e.g., `MAT-BOS-2026-001423`).
2. The Technician completes the **Asset Registration Form** in ServiceNow, recording:
   - MAT number
   - Manufacturer, model, serial number
   - Processor, memory, storage specifications
   - MAC address(es) and assigned IP (if static)
   - Asset category and classification tier
   - ePHI flag (Yes/No) – if **Yes**, asset is marked **Restricted – ePHI Handling Required**
   - Assigned location (Building, Floor, Room)
   - Warranty expiration date (per vendor documentation)
3. The Asset state transitions to `"In Stock – Available"`.
4. For Cloud Resources: The Cloud Engineering Manager ensures all Terraform-module-provisioned instances include mandatory tag set: `AssetID`, `Environment`, `DataClassification`, `CostCenter`. AWS Config validates tagging compliance. Non-compliant resources are flagged in the ServiceNow CMDB via the AWS Config CMDB Integration.

### 5.3 Asset Assignment and Deployment

#### 5.3.1 User Assignment

1. The IT Asset Manager receives the assignment request through the HR onboarding workflow (SOP-HR-008 – Technology Provisioning for New Hires) or a ServiceNow transfer request.
2. The Technician retrieves the configured asset from the secure staging area.
3. For new hires: The asset is delivered to the hiring manager or at the Meridian IT Service Desk for Day-1 pickup. **Identity verification** (government-issued photo ID matched against Workday record) is required at handoff.
4. The Technician performs **IT Asset Custodian Assignment** in ServiceNow:
   - Custodian: the assigned end-user
   - Assignment Date/Time
   - Custodian acknowledgment: captured via digital signature on the iPad-based **Acceptance of Responsibility Form (ITAM-002)**, which includes:
     - Statement of physical responsibility
     - Obligation to report loss/theft/damage within 4 hours
     - Prohibition against storing personal ePHI on local storage
     - Consent to Meridian’s monitoring and remote wipe capability
5. Asset state transitions to `"Assigned"`.

#### 5.3.2 Cloud Resource Assignment

1. Cloud resources are provisioned by **Cloud Engineering** via the Infrastructure-as-Code pipeline.
2. The provisioning pipeline auto-populates the ServiceNow CMDB with the cloud resource record, including Resource ARN, tags, and owner team.
3. Owner assignment is set at the team/resource-group level. Individual access is governed by IAM policies (AWS) per SOP-ISMS-010 (Access Management for Cloud Infrastructure).

### 5.4 Asset Lifecycle Tracking and Maintenance

#### 5.4.1 Status Transitions

The CMDB enforces the following lifecycle state model:

| Current State | Permitted Next States | Trigger Condition |
|---------------|-----------------------|-------------------|
| On Order | Received, Cancelled | Physical receipt or PO cancellation |
| Received | In Stock – Available, Returned to Vendor | Inspection passed; failed inspection |
| In Stock – Available | Assigned, Reserved, Retired | Assignment; project reservation; decommissioning |
| Assigned | In Repair, Transfer, Offboarded, Lost/Stolen | Service ticket; user transfer; termination; incident report |
| In Repair | Assigned, Retired | Repair completed; repair not cost-effective |
| Offboarded | In Stock – Available, In Repair, Retired | Refresh, maintenance, or decommission decision |
| Lost/Stolen | (No transitions – investigation pending) | Security investigation per SOP-ISMS-012, Section 4.2.1 |
| Retired | Disposal Pending | Sanitization pending |
| Disposal Pending | Disposed | Verification of sanitization and disposal completion |

#### 5.4.2 Maintenance and Break/Fix

1. A user experiencing an asset issue opens a ServiceNow Incident: Category = `Hardware`, CI = their MAT.
2. IT Service Desk triages. If hardware repair is required:
   - EUC: Device is brought to the **IT Service Desk Bar**. A loaner asset is issued within 4 business hours.
   - Server/Infrastructure: Operations team engages vendor support under Meridian’s maintenance agreements. Hardware replacement is tracked against the parent asset record.

### 5.5 Software Asset and License Management

#### 5.5.1 Entitlement Tracking

1. All software licenses are recorded in **ServiceNow Software Asset Management (SAM) Pro** module.
2. Procurement uploads license entitlement data (license keys, quantity, term) upon purchase.
3. Software deployments are reconciled against entitlements via:
   - **Jamf Pro** inventory (macOS applications)
   - **Microsoft Intune** inventory (Windows applications)
   - **AWS License Manager** (cloud-resident licensed workloads)
   - **Snow Software** discovery agent (data center and server estate)

#### 5.5.2 True-Up and Compliance

1. The IT Asset Manager conducts a **Monthly License Compliance Reconciliation**, generating the **License Position Report**.
2. Any license deficit exceeding **5% of entitlement** triggers remediation within 30 calendar days via either:
   - Purchase of additional licenses through standard procurement workflow
   - Removal of unauthorized installations through the Technical Remediation process
3. **Annual True-Up:** During April of each fiscal year, the IT Asset Manager facilitates the enterprise-wide software license true-up with major vendors (Microsoft, Salesforce, AWS Marketplace, Snowflake). Budgetary requirements are submitted to the VP, IT Operations by May 15.

### 5.6 Secure Asset Disposal

**HIPAA Requirement (45 CFR § 164.310(d)(1) and (d)(2)):** For any asset that at any point contained ePHI, Meridian SHALL implement procedures for the final disposition of that hardware and electronic media. This SOP implements those requirements by the detailed procedure below.

#### 5.6.1 Disposal Initiation

1. The IT Asset Manager initiates disposal for assets in `"Retired"` or `"Offboarded"` state via: ServiceNow → ITAM → Disposal → **Create Disposal Ticket**.
2. The Disposal Ticket captures:
   - MAT(s) for disposal (batch disposal allowed for up to 25 assets per ticket if same classification tier)
   - Data classification tier
   - ePHI flag status
   - Sanitization method required (see Table 3)
   - Disposal method (Recycle, Resell/Return to Lessor, Donation, Physical Destruction)
   - Residual value estimate (if any)

**Table 3: Sanitization Method by Asset Classification**

| Classification | ePHI Flag | Required Sanitization Method |
|----------------|-----------|------------------------------|
| Restricted – ePHI | Yes | NIST SP 800-88 **Purge** using cryptographic erase (ATA Secure Erase or NVM Express Format NVM) followed by **Physical Destruction** or validated overwrite. For solid-state media, physical destruction by shredding to 2mm particles is mandatory. |
| Restricted | No | NIST SP 800-88 **Purge** via cryptographic erase or block-level overwrite (3-pass minimum). Verification pass required. |
| Confidential | No | NIST SP 800-88 **Clear** via software-based sanitization using Blancco Drive Eraser or equivalent certified tool. Single-pass verification. |
| Internal | No | NIST SP 800-88 **Clear**: Secure erase or factory reset. Documented in ServiceNow. |
| Public | No | Factory reset recommended, not mandatory. |

#### 5.6.2 Sanitization Execution

1. The IT Technician assigned to the ticket:
   - Physically retrieves the asset from inventory.
   - For assets containing ePHI (Restricted – ePHI): A **Two-Person Sanitization** is required. A **Security Operations team member** witnesses the sanitization. Both sign the Sanitization Verification Form.
   - Executes the sanitization method per classification.
   - Documents the tool used, method, and a verification checksum or log in the Disposal Ticket.
2. For cloud resources (AWS EC2 volumes, S3 buckets containing structured data): **Cloud Engineering** executes the disposal by destroying the resource via Terraform and verifying no snapshot or derivative remains. EBS volumes are force-detached and deleted.

#### 5.6.3 Vendor / Third-Party Disposal

1. If disposal is handled by a certified vendor (e.g., **Sims Lifecycle Services** or **Iron Mountain Secure ITAD**), Meridian requires:
   - A signed **Business Associate Agreement (BAA)** if any asset may have contained ePHI.
   - A **Certificate of Destruction (CoD)** including serial number of each device destroyed, date, location, and method (NIST SP 800-88 Destroy).
   - Chain-of-custody documentation from Meridian facility handoff to vendor transport to destruction facility.
2. The IT Asset Manager reviews the CoD against the Disposal Ticket manifest within 10 business days of vendor service.

#### 5.6.4 Final Disposition and Record Closure

1. Upon verification of sanitization and/or destruction, the IT Asset Manager:
   - Attaches sanitization log and CoD to the ServiceNow Disposal Ticket.
   - Transitions the asset state to `"Disposed"`.
   - Retires the MAT (tag not reused).
2. The CMDB record is retained for a minimum of **7 years** from disposal date per HIPAA retention requirements for asset disposition documentation.

**Decommissioning of HIA Clinical Workstations:**
Workstations processing clinical imaging (DICOM) containing Protected Health Information undergo an additional review by the **Clinical Engineering Team** (if located in clinical environments) to ensure all local modality worklists and patient context data has been purged prior to ITAM sanitization.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Frequency | Responsible |
|------------|---------------------|-----------|-------------|
| AC-01 | Asset Requisition approval workflow with management authorization thresholds ($5K / $50K) | Per transaction | IT Asset Manager, Procurement |
| AC-02 | Annual Asset Inventory: Physical verification of a sample (20% quarterly, achieving 100% annually) of EUC and infrastructure assets against CMDB records | Quarterly, cumulative annually | IT Asset Manager |
| AC-03 | Acceptance of Responsibility Form (ITAM-002) signed at assignment | Per assignment | End-User Custodian |
| AC-04 | Two-Person Sanitization for ePHI assets | Per disposal event | IT Technician + Security Operations |
| AC-05 | Monthly License Compliance Reconciliation | Monthly | IT Asset Manager |
| AC-06 | Semi-annual disposal audit by InfoSec | Semi-annual (March, September) | Senior Director, InfoSec |

### 6.2 Technical Controls

| Control ID | Control Description | Implementation Tool |
|------------|---------------------|---------------------|
| TC-01 | Automated CMDB population for cloud resources | AWS Config, ServiceNow Cloud Discovery |
| TC-02 | Mandatory asset tagging for cloud resources enforced via Policy-as-Code | Terraform Sentinel, AWS Config Rules `required-tags` |
| TC-03 | Full-disk encryption enforced on all EUC devices | Jamf Pro Policy, Intune Compliance Policy |
| TC-04 | MDM enrollment enforced: personally owned BYOD not permitted to store Meridian data unless enrolled | Jamf Pro / Intune Conditional Access |
| TC-05 | Endpoint detection and response (EDR) agent installed and active; alert if not running | CrowdStrike Falcon |
| TC-06 | Network access control (NAC) for infrastructure hardware: unknown MAC addresses are quarantined | Cisco ISE |
| TC-07 | Cryptographic erasure verification tooling (ATA Secure Erase verification, NVMe Format NVM verification log) | Blancco Drive Eraser, Parted Magic Secure Erase |

### 6.3 Physical Controls

| Control ID | Control Description |
|------------|---------------------|
| PC-01 | All IT asset inventory stored in access-controlled IT storerooms with badged entry logging |
| PC-02 | Asset disposal bin (pre-destruction) is a locked, access-controlled cage accessible only to IT Asset Management and Security Operations |
| PC-03 | Shipping/receiving dock for incoming IT assets is under video surveillance with 90-day retention |
| PC-04 | Media destruction shredder (for drives) located in restricted-access Data Center Mechanical Room, Boston HQ |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI | Target | Measurement Method | Reporting Audience | Cadence |
|-----|--------|-------------------|--------------------|---------|
| CMDB Accuracy – Physical Assets | ≥ 98% | Reconciliation of physical inventory scan vs. CMDB records | VP, IT Operations | Quarterly |
| CMDB Accuracy – Cloud Resources | ≥ 99% (auto-tagged) | AWS Config compliance dashboard | VP, Engineering | Monthly |
| Time-to-Assign (New Hire EUC) | ≤ 3 business days post account creation | ServiceNow `requested` → `assigned` time stamp delta | Director, People Operations | Monthly |
| Lost/Stolen Asset Incident Rate | < 0.5% of assigned endpoints per quarter | Count of `Lost/Stolen` state transitions | CISO | Quarterly |
| License Compliance | No true-up deficit >5% for top 20 vendors | SAM Pro License Position Report | VP, IT Operations | Monthly |
| ePHI Asset Disposal Completion | 100% sanitization verification within 30 days of offboarding | ServiceNow Disposal Ticket `created` → `disposed` closure time | Privacy Officer; CISO | Monthly |

### 7.2 Monitoring Approach

IT Operations maintains active monitoring of the IT asset fleet through:
- **Jamf Pro / Intune dashboards** – device compliance, encryption status, last check-in.
- **ServiceNow Performance Analytics** – asset lifecycle metrics, open procurement requests aging.
- **CrowdStrike Falcon Console** – endpoint detection coverage, agent health across all deployed endpoints.

Detection of assets exhibiting anomalous behavior (prolonged offline, unauthorized software, ePHI access from non-approved location) triggers an incident ticket in the Security Operations queue. The IT Asset Manager receives the weekly **Asset Health Summary** report from ServiceNow.

### 7.3 Management Reporting

| Report | Content | Audience | Cadence |
|--------|---------|----------|---------|
| ITAM Monthly Operations Report | KPI trends, inventory aging, license position, open exceptions | Samantha Torres, VP of IT Operations | Monthly (first Tuesday) |
| Asset Compliance Review | ePHI asset tracking, disposal timeliness, lost/stolen report | CISO; Privacy Officer | Quarterly |
| Annual State of IT Assets | Full fleet lifecycle summary, refresh plan, budget projection | David Park, VP Engineering; CFO | Annually (November) |

---

## 8. Exception Handling and Escalation

### 8.1 Policy Exceptions

1. Any deviation from the procedures defined in this SOP requires an **Exception Request** submitted through ServiceNow → ITAM → Request Exception.
2. The request SHALL include:
   - Specific SOP section for which deviation is sought
   - Business justification
   - Compensating controls to be applied
   - Duration of exception (not to exceed 12 months)
   - Risk acknowledgment from the requesting department head
3. Exception approval authorities:
   - **Low-risk exceptions** (no ePHI, no HIA, <90-day duration): IT Asset Manager
   - **Medium-risk exceptions** (Confidential data, infrastructure assets): VP, IT Operations (Samantha Torres) with consultation from InfoSec
   - **High-risk exceptions** (ePHI, HIA, cloud administrative access deviations): VP, IT Operations + CISO joint approval
4. Approved exceptions are documented in the **Exception Register** and reviewed quarterly. Expired exceptions automatically rescind unless renewed.

### 8.2 Lost or Stolen Asset Escalation

This is managed per **SOP-ISMS-012 (Security Incident Response)** and triggers the **Lost/Stolen Asset Procedure**:

1. User discovers loss/theft → immediately (within 4 hours) reports to IT Service Desk (ext. 4500 or ServiceNow P1 Incident).
2. IT Service Desk triages and escalates to Security Operations for incident creation.
3. IT Asset Manager transitions asset to `Lost/Stolen` state in CMDB, noting the Security Incident number.
4. Security Operations initiates remote lock and/or wipe via Jamf Pro or Intune. GPS location retrieval attempted.
5. Within **24 hours**, a **Lost Asset Report** is filed with:
   - Meridian Security (Physical Security team)
   - If ePHI was on the device: Meridian Privacy Officer, for assessment against HIPAA Breach Notification Rule (45 CFR §§ 164.400–414)
6. If asset is unrecovered after 30 days, IT Asset Manager retires the MAT and removes from active inventory.

### 8.3 Escalation Path for Procedural Blockers

| Level | Contact | Response SLA |
|-------|---------|-------------|
| L1 – IT Asset Technician | ServiceNow Queue: ITAM | 8 business hours |
| L2 – IT Asset Manager | Direct email / Teams | 4 business hours |
| L3 – VP, IT Operations (Samantha Torres) | Escalation via ServiceNow with L1/L2 context | 1 business day |
| L4 – VP, Engineering (David Park) / CISO | For cross-functional or budget impacting blockers | 2 business days |

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Training Module | Target Audience | Delivery Method | Frequency | Tracking |
|-----------------|-----------------|-----------------|-----------|----------|
| ITAM-100: IT Asset Management Fundamentals | IT Asset Manager, IT Technicians, Procurement Manager | Instructor-led (virtual) | Once upon role assignment; refresher biennially | Workday Learning |
| ITAM-200: Asset Disposal and HIPAA Sanitization | IT Technicians, Security Operations personnel involved in disposal | Instructor-led with hands-on lab (Blancco tooling) | Annually | Workday Learning + practical validation |
| ITAM-300: SAM Pro License Management for Administrators | IT Asset Manager, SAM module administrators | Vendor-provided (ServiceNow SAM Pro certification recommended) | Once; update upon major release change | Certification record |
| ITAM-400: End-User Asset Custodian Awareness | All personnel assigned an IT asset upon onboarding | eLearning (15-minute module) | During Day-1 IT orientation; annual refresher | Workday Learning |
| ITAM-500: Cloud Resource Tagging for Engineers | Cloud Engineering, DevOps teams | Knowledge base article + mandatory checklist acknowledgment | Upon Terraform repo access grant; changes to tagging standard require re-acknowledgment | Git commit sign-off record |

### 9.2 Compliance Tracking

1. Meridian’s **Workday Learning Management System (LMS)** manages enrollment, completion tracking, and non-compliance notification.
2. **Monthly Non-Compliance Report**: Person/Team with overdue training assignments, escalated to their manager.
3. Personnel who fail to complete mandatory training within **15 calendar days** of due date lose access to ITAM workflows until completion is verified.

---

## 10. Related Policies and References

### 10.1 Meridian Internal SOPs

| SOP ID | Title | Relationship |
|--------|-------|--------------|
| SOP-ISMS-001 | Information Security Management System – Overview | Overall governance framework |
| SOP-ISMS-003 | Asset Classification and Handling | Classification schema used in Section 5.2.3 |
| SOP-ISMS-007 | Media Sanitization and Disposal | Specific procedures for sanitization techniques referenced in Section 5.6 |
| SOP-ISMS-010 | Access Management for Cloud Infrastructure | IAM controls referenced in 5.3.2 |
| SOP-ISMS-012 | Security Incident Response | Lost/stolen escalation referenced in Section 8.2 |
| SOP-EUC-002 | Endpoint Configuration Baseline | Baseline configuration standard applied during intake (5.2.2) |
| SOP-HR-008 | Technology Provisioning for New Hires | HR onboarding trigger for asset assignment |
| SOP-CLD-005 | Cloud Resource Provisioning and Tagging | Terraform tagging standard |
| SOP-PRIV-004 | HIPAA Breach Notification Procedure | Privacy Officer notification for lost ePHI asset |
| SOP-ITOP-001 | Change Management | Changes to CMDB schemas and tagging standards |

### 10.2 External Standards and Regulations

| Reference | Title | Applicability |
|-----------|-------|---------------|
| NIST SP 800-88 Rev. 1 | Guidelines for Media Sanitization | Sanitization standard for all asset disposal |
| HIPAA Security Rule (45 CFR §§ 164.308–164.312) | Administrative, Physical, and Technical Safeguards | Controls for ePHI assets, disposal procedures |
| HIPAA Breach Notification Rule (45 CFR §§ 164.400–414) | Breach Notification | Triggered procedure in lost/stolen ePHI device |
| AICPA TSC 2017 (SOC 2) | Trust Services Criteria: CC3.2, CC4.1, CC6.1, CC6.2, CC7.1 | Criteria addressed by this SOP |
| ISO/IEC 27002:2022 | Section 5.9 – Inventory of Information and Other Associated Assets | Alignment for asset inventory framework |
| IEC 62443-3-3 | FR 7 – Resource Availability | HIA clinical asset availability considerations |

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
|---------|------|--------|----------|--------------------|
| 4.0 | 2024-11-15 | M. Chen, IT Asset Manager | Samantha Torres | Reorganized SOP into modular procedure sections; moved from Excel-based inventory to ServiceNow CMDB as authoritative system of record; implemented MAT barcode tagging standard |
| 4.5 | 2025-02-28 | J. Okonkwo, IT Asset Manager (Interim) | Samantha Torres | Added cloud resource tagging controls (Section 5.2.3); aligned procurement workflow with Oracle Fusion Cloud integration; updated ePHI disposal to reference NIST SP 800-88 Rev. 1 explicitly |
| 4.7 | 2025-04-10 | J. Okonkwo, IT Asset Manager | David Park | Adjusted two-person destruction requirement threshold for HIA; added Annual Asset Attestation procedure; updated roles reflecting Cloud Engineering Manager position |
| 4.8 | 2025-08-22 | S. Patel, Senior IT Asset Manager | Samantha Torres | Enhanced software license management procedures with SAM Pro module; added KPI targets and management reporting cadence; revised exception handling tiers |
| 4.9 | 2026-08-13 | S. Patel, Senior IT Asset Manager | David Park | Comprehensive review: aligned disposal controls with updated SOP-ISMS-007; extended cloud tagging compliance to AWS Config integration; added training compliance tracking and escalation; incorporated quarterly inventory and semi-annual disposal audit cycles; minor formatting and reference updates |

---

**End of Document – SOP-ITOP-014 v4.9**

*This document contains proprietary information of Meridian Health Technologies, Inc. Distribution is limited to personnel with a valid business need.*