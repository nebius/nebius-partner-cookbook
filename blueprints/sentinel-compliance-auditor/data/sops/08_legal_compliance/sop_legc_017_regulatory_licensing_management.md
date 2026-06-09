---
sop_id: "SOP-LEGC-017"
title: "Regulatory Licensing Management"
business_unit: "Legal & Compliance"
version: "5.1"
effective_date: "2025-02-23"
last_reviewed: "2026-01-20"
next_review: "2026-07-24"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Regulatory Licensing Management

**SOP-LEGC-017 | Version 5.1**
**Effective: 2025-02-23**
**Owner: Thomas Anderson, Chief Compliance Officer**
**Classification: Internal**

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure establishes the framework, processes, and controls for the end-to-end management of regulatory licenses, certifications, and accreditations held by Meridian Health Technologies, Inc. and its wholly-owned subsidiaries (collectively, "Meridian" or "the Company"). The purpose of this SOP is to ensure that all licenses required for the lawful operation of Meridian's business lines—including but not limited to healthcare fintech activities, AI/ML system deployments, medical device marketing, and data processing—are identified, obtained, maintained, renewed, and verified in a timely, auditable, and compliant manner.

### 1.2 Scope

This SOP applies to the following categories of licenses, certifications, and regulatory authorizations (collectively, "Regulatory Instruments"):

| Category | Examples | Business Unit Impact |
|---|---|---|
| **Financial Services Licenses** | Money transmitter licenses, lending licenses, debt collection licenses, payment processor registrations | HealthPay Financial Services |
| **Healthcare Regulatory Authorizations** | FDA 510(k) clearances, CE marking under EU MDR, HIPAA covered entity/business associate designations | Clinical AI Platform, MedInsight Analytics |
| **Data Protection Registrations** | GDPR Article 27 representative designations, data protection registrations with EU member state DPAs | All Business Units |
| **AI/ML System Certifications** | EU AI Act high-risk AI system conformity assessments, NIST AI RMF attestations | Clinical AI Platform |
| **Information Security Certifications** | SOC 2 Type II, HITRUST CSF, ISO 27001:2022 | Meridian SaaS Platform, All Business Units |
| **State-Specific Healthcare Licenses** | Clinical laboratory licenses, medical device distributor permits, telehealth registrations | Clinical AI Platform, MedInsight Analytics |
| **Corporate Registrations** | Certificates of authority to transact business, registered agent appointments, assumed name filings | All Business Units |

**In Scope:**
- All Meridian business units, subsidiaries, and global offices (Boston, London, Berlin, Singapore, Toronto)
- All employees, contractors, and third-party service providers who have responsibility for filing, maintaining, or verifying Regulatory Instruments
- All systems, platforms, and applications that process regulated data or perform regulated functions

**Out of Scope:**
- Individual professional licenses held by employees (e.g., medical licenses, bar admissions) are managed per SOP-HR-042 (Professional Credential Management)
- Intellectual property registrations (patents, trademarks) are managed per SOP-LEGC-012 (Intellectual Property Management)
- Environmental permits and facilities licenses are managed per SOP-OPS-008 (Facilities Compliance)

### 1.3 Applicability by Business Unit

| Business Unit | Applicable Regulatory Instruments | Primary Regulatory Frameworks |
|---|---|---|
| Clinical AI Platform | FDA 510(k), CE Marking (EU MDR), EU AI Act High-Risk AI Conformity, HIPAA | 21 CFR Part 800-898, EU MDR 2017/745, EU AI Act 2024/1689, HIPAA 45 CFR Parts 160-164 |
| HealthPay Financial Services | State Money Transmitter Licenses, State Lending Licenses, Payment Processor Registrations, NACHA participation | State-specific statutes, SR 11-7, Reg E, Reg Z, BSA/AML |
| MedInsight Analytics | HIPAA Business Associate Agreements, State Health Data Use Permits | HIPAA, State health information privacy laws |
| Meridian SaaS Platform | SOC 2 Type II, HITRUST CSF, ISO 27001:2022, GDPR Article 28 (Data Processing Agreements) | AICPA TSC 2017, HITRUST CSF v11.2, ISO/IEC 27001:2022 |

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Regulatory Instrument** | Any license, certification, registration, clearance, accreditation, conformity assessment, or authorization issued by a governmental authority, regulatory body, or recognized standards organization that is required for Meridian to lawfully conduct its business activities. |
| **License Inventory** | The authoritative, centrally maintained record of all Regulatory Instruments held by Meridian, stored in the Governance, Risk, and Compliance (GRC) platform. |
| **Renewal Critical Date** | The date by which a complete renewal application must be submitted to the issuing authority to ensure uninterrupted validity of a Regulatory Instrument, accounting for processing lead times, internal review cycles, and any statutory waiting periods. |
| **Control Owner** | The individual within Meridian who has operational responsibility for maintaining compliance with a specific regulatory requirement or control objective associated with a Regulatory Instrument. |
| **Regulatory Event** | Any event that could materially affect the status, validity, or terms of a Regulatory Instrument, including but not limited to: enforcement actions, regulatory examinations, changes in applicable law, material changes to business operations, or adverse audit findings. |
| **Compliance Verification** | The process of independently confirming that Regulatory Instruments remain valid and that associated control requirements are being met, performed at a cadence specified by the issuing authority or Meridian's internal risk appetite. |
| **Nationwide Multistate Licensing System (NMLS)** | The system of record for non-depository financial services licensing in the United States, used by Meridian for managing state-level financial services licenses. |
| **Standard Contractual Clauses (SCCs)** | European Commission-approved model clauses for the transfer of personal data to third countries, as updated from time to time. |

### 2.2 Acronyms

| Acronym | Meaning |
|---|---|
| **AICPA** | American Institute of Certified Public Accountants |
| **BA** | Business Associate (as defined under HIPAA) |
| **BA** | The Meridian platform for tracking business associate agreements; also used in context of Business Associate under HIPAA |
| **BSA/AML** | Bank Secrecy Act / Anti-Money Laundering |
| **CCO** | Chief Compliance Officer |
| **CE** | Conformité Européenne |
| **CISO** | Chief Information Security Officer |
| **CPO/DPO** | Chief Privacy Officer / Data Protection Officer |
| **CSF** | Common Security Framework (HITRUST) |
| **DPA** | Data Protection Authority or Data Processing Agreement (context-dependent) |
| **DR** | Disaster Recovery |
| **FDA** | United States Food and Drug Administration |
| **FMO** | Financial Markets Operations (internal Meridian team) |
| **GC** | General Counsel |
| **GRC** | Governance, Risk, and Compliance |
| **HITRUST** | Health Information Trust Alliance |
| **MDR** | Medical Device Regulation (EU) 2017/745 |
| **ML** | Machine Learning |
| **MRM** | Model Risk Management |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework |
| **PHI** | Protected Health Information |
| **QMS** | Quality Management System |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **SCCs** | Standard Contractual Clauses |
| **SOC 2** | System and Organization Controls 2 |
| **TSC** | Trust Services Criteria (AICPA) |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

The following RACI matrix assigns responsibilities for the core activities within this SOP. Each regulatory activity must have a clearly identified Responsible party and Accountable party, with designated Consulted and Informed stakeholders.

| Activity/Decision | Chief Compliance Officer | General Counsel | CISO | CPO/DPO | VP Financial Services | VP Clinical AI | VP IT Ops | Regulatory Licensing Manager | BU Compliance Liaisons |
|---|---|---|---|---|---|---|---|---|---|
| **Regulatory Inventory Maintenance** | A | C | C | C | C | C | C | R | C |
| **New License Application** | A | R | C | C | C | C | I | R | C |
| **License Renewal Execution** | A | I | I | I | R | R | I | R | C |
| **SOC 2 Control Implementation** | C | I | R/A | C | C | C | R | I | C |
| **Regulatory Change Monitoring** | A | R | C | R | C | C | I | R | C |
| **Exception Approval** | R | A | C | C | C | C | I | C | I |
| **Board-Level Reporting** | R | A | C | C | I | I | I | C | I |
| **Enforcement Action Response** | C | A | C | C | R | R | I | R | I |

**Legend:** R = Responsible (performs the work) | A = Accountable (approves/signs off) | C = Consulted (provides input) | I = Informed (receives status updates)

### 3.2 Key Roles

**Chief Compliance Officer (Thomas Anderson)**
- Ultimate accountability for the Regulatory Licensing Management program.
- Approves all license applications and renewals for financial services Regulatory Instruments.
- Escalates material regulatory risks to the Board-Level AI Governance Committee and the Audit Committee.
- Reviews and approves this SOP biennially.

**General Counsel (Maria Gonzalez)**
- Provides legal interpretation of licensing requirements and regulatory changes.
- Approves all regulatory filings before submission.
- Represents Meridian before regulatory bodies in enforcement matters.
- Provides legal review of all licensing applications and supporting documentation.

**Chief Information Security Officer (Rachel Kim)**
- Accountable for the implementation and maintenance of technical controls required for SOC 2 Type II, HITRUST CSF, and ISO 27001:2022 certifications.
- Provides evidence and attestations for information security-related regulatory filings.
- Leads response to cybersecurity-related regulatory inquiries.

**Chief Privacy Officer / DPO (Dr. Klaus Weber)**
- Accountable for GDPR compliance verification and data protection registrations.
- Maintains the inventory of cross-border data transfer mechanisms (SCCs, adequacy decisions).
- Files required notifications and registrations with EU DPAs.
- Serves as the primary point of contact for data protection regulatory inquiries.

**Vice President, Financial Services (Robert Liu)**
- Provides subject matter expertise for financial services licensing requirements.
- Identifies new licensing requirements triggered by product expansion or market entry.
- Maintains familiarity with state-specific statutes governing money transmission and lending.

**Vice President, Clinical AI Products (Dr. Aisha Okafor)**
- Accountable for the clinical, safety, and performance evidence required for FDA 510(k) and EU MDR submissions.
- Ensures that AI/ML model documentation meets regulatory submission requirements.
- Identifies changes to AI systems that may require re-assessment or re-filing.

**Regulatory Licensing Manager** (Reports to CCO; a dedicated role within Legal & Compliance)
- Day-to-day management of the Regulatory Instrument inventory in the GRC platform.
- Primary Responsible party for license renewal execution and tracking.
- Coordinates the collection of materials required for regulatory filings.
- Monitors regulatory change feeds and triages impacts to Meridian's license portfolio.

**Business Unit Compliance Liaisons**
- Embedded within each business unit (HealthPay, Clinical AI, MedInsight, SaaS Platform).
- Provide first-line awareness of business changes that may have licensing implications.
- Coordinate evidence collection within their business units for regulatory filings.

---

## 4. Policy Statements

### 4.1 General Policy

Meridian Health Technologies, Inc. is committed to conducting its business in full compliance with all applicable laws, regulations, and industry standards in every jurisdiction in which it operates. The Company shall:

1. **Identify:** Proactively identify all Regulatory Instruments required for its current and planned business activities through a structured regulatory scoping process.
2. **Obtain:** Secure all required licenses, certifications, and authorizations before commencing regulated activities in any jurisdiction.
3. **Maintain:** Continuously maintain the validity of all Regulatory Instruments through timely renewal, ongoing compliance with associated conditions, and prompt response to regulatory inquiries.
4. **Verify:** Independently verify the effectiveness of controls that underpin certifications and attestations.
5. **Document:** Maintain complete, accurate, and audit-ready records of all licensing activities.

### 4.2 Prohibition of Unlicensed Activity

No business unit, employee, or agent of Meridian shall initiate or conduct activities that require a Regulatory Instrument without first confirming that the required authorization has been obtained and is in good standing. Any proposed new product, service, market entry, or material change to existing operations must undergo a Regulatory Licensing Impact Assessment (RLIA) as part of the Product Approval and New Market Entry Process (SOP-PROD-003).

### 4.3 SOC 2 Type II Commitment

Meridian shall maintain SOC 2 Type II certification for the Meridian SaaS Platform, covering the Trust Services Criteria (TSC) of Security, Availability, and Confidentiality (as defined in TSP section 100, *2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy*, AICPA). The Company commits to:

- Annual SOC 2 Type II examinations conducted by an independent, AICPA-licensed CPA firm.
- A continuous monitoring program that bridges the gap between annual audit cycles.
- Prompt remediation of any control deficiencies or exceptions identified during SOC 2 examinations, with critical findings remediated within 30 calendar days and non-critical findings within 90 calendar days.
- Maintenance of a SOC 2 bridge letter for periods between the report end date and the subsequent report issuance date, upon customer request.

### 4.4 Commitment to Proactive Regulatory Engagement

Meridian shall maintain open, transparent, and proactive relationships with its regulatory bodies. The Company shall:

- Respond to all regulatory inquiries within the timeframe specified by the regulator, or within 10 business days if no specific timeframe is provided.
- Voluntarily disclose material regulatory events to affected regulators within 5 business days of identification.
- Participate in industry working groups and comment processes to stay abreast of regulatory developments.

---

## 5. Detailed Procedures

### 5.1 Regulatory Licensing Impact Assessment (RLIA)

This procedure must be completed for any proposed initiative that may have licensing implications.

#### 5.1.1 Triggering Events

An RLIA must be initiated for any of the following events:
- Launch of a new product or service
- Entry into a new geographic market (including new U.S. states)
- Material change to an existing product or service (see §5.1.2 for materiality thresholds)
- Merger, acquisition, or divestiture activity
- Deployment of a new AI/ML model into a regulated function
- Changes to data processing activities that affect cross-border data flows
- Changes to key vendors or service providers that support regulated functions

#### 5.1.2 Materiality Thresholds

A change is considered "material" for the purposes of RLIA if it meets any of the following criteria:
- Changes the intended use or indications for use of a regulated medical device
- Alters the risk classification of an AI system under the EU AI Act
- Modifies the nature of funds handling in a financial services product
- Changes the categories of data subjects or types of personal data processed
- Introduces processing in a new jurisdiction
- Results in a change to the control environment underlying a certification (SOC 2, HITRUST, ISO 27001)

#### 5.1.3 RLIA Procedure Steps

| Step | Action | Responsible | Timeframe |
|---|---|---|---|
| 1 | Business Unit submits RLIA Request Form (FRM-LEGC-017-A) through the GRC platform | Business Unit Sponsor | NLT 60 days before planned launch/change |
| 2 | Regulatory Licensing Manager triages the request and assigns a complexity rating (Low/Medium/High) | Regulatory Licensing Manager | 3 business days from submission |
| 3 | Legal & Compliance conducts regulatory scoping: identifies all potentially required new or amended Regulatory Instruments | Regulatory Licensing Manager, with GC consultation for High complexity | 10 business days (Low), 20 business days (Medium), 30 business days (High) |
| 4 | Regulatory Licensing Manager publishes RLIA Report summarizing findings, required actions, and estimated timelines | Regulatory Licensing Manager | Included in scoping timeframe |
| 5 | CCO reviews and approves RLIA Report; GC co-approves for High complexity assessments | CCO, GC | 5 business days |
| 6 | If new licenses are required, the License Acquisition Procedure (§5.2) is initiated | Regulatory Licensing Manager | Immediately upon approval |

**Output:** Form FRM-LEGC-017-B (RLIA Report), stored in the GRC platform with unique identifier RLIA-YYYY-NNN.

### 5.2 License Acquisition Procedure

#### 5.2.1 Pre-Application Phase

1. **Requirement Confirmation:** The Regulatory Licensing Manager confirms the specific licensing requirement with the issuing authority, including any pre-application meetings, fees, bonding requirements, and qualification criteria.
2. **Application Package Assembly:** A dedicated folder is created in the Legal & Compliance document management system (path: `/Legal-Compliance/Licensing/[Jurisdiction]/[License-Type]/[Year]/Application`). The following materials are assembled:
   - Business formation documents (certificates of incorporation, good standing certificates)
   - Financial statements (audited if required by the jurisdiction)
   - Biographical affidavits and fingerprint cards for control persons and key individuals
   - Surety bonds (coordinated with Treasury per SOP-FIN-019)
   - Policies and procedures demonstrating compliance capability
   - System and security documentation (for SOC 2 or HITRUST attestations)
   - Clinical evidence and QMS documentation (for medical device / AI submissions)
   - Engagement letter with external counsel or regulatory consultant (if applicable)
3. **Internal Review and Approval:** The completed application package undergoes the following review chain:
   - **Financial Services Licenses:** Regulatory Licensing Manager → VP Financial Services → CCO → GC
   - **Healthcare/Medical Device:** Regulatory Licensing Manager → VP Clinical AI → CCO → GC
   - **Data Protection:** Regulatory Licensing Manager → CPO/DPO → GC
   - **Information Security Certifications:** Regulatory Licensing Manager → CISO → CCO → GC
4. **GC Final Sign-off:** The General Counsel provides final legal review and approval of the application. No application shall be submitted without GC approval.

#### 5.2.2 Submission and Post-Submission

1. **Submission Tracking:** The application submission date, method, tracking number, and confirmation receipt are recorded in the GRC platform under the relevant Regulatory Instrument record.
2. **Regulatory Communication Log:** All communications with the regulator during the application review period are logged in the GRC platform. No substantive communications shall occur outside of the official record.
3. **Application Status Updates:** The Regulatory Licensing Manager provides status updates as follows:
   - **High complexity:** Weekly to CCO and relevant BU head
   - **Medium complexity:** Bi-weekly to CCO
   - **Low complexity:** Monthly to CCO dashboard
4. **Conditional Approvals:** If a regulator grants a conditional approval with requirements for post-issuance compliance, the conditions are entered into the GRC system as tasks with assigned owners and due dates.
5. **License Issuance:** Upon issuance, the Physical License Document (if applicable) is scanned and stored digitally. The original is stored in the fireproof Legal & Compliance filing cabinet in Boston HQ. The digital copy is uploaded to the GRC platform. The Regulatory Instrument record is updated to "Active" status.

### 5.3 License Renewal Tracking and Execution

#### 5.3.1 Renewal Calendar and Lead Times

The Regulatory Licensing Manager maintains a master renewal calendar in the GRC platform. Renewal Critical Dates are calculated as follows:

| License Type | Renewal Submission Lead Time | Internal Review Period | Total Lead Time (from Renewal Critical Date) |
|---|---|---|---|
| State Money Transmitter Licenses | 60 days before expiration | 20 business days | Renewal Critical Date set to 90 days before statute expiration |
| State Lending Licenses (annual) | 45 days before expiration | 15 business days | Renewal Critical Date set to 75 days before statute expiration |
| CE Marking (EU MDR) – Certificate Renewal | 120 days before expiration | 30 business days | Renewal Critical Date set to 180 days before certificate expiration |
| FDA 510(k) – No expiration, but changes trigger new filing | N/A (event-driven) | Per RLIA | N/A |
| SOC 2 Type II – Annual Examination | Examination window agreed with auditor | 4 weeks for readiness | Readiness assessment 60 days before examination start |
| HITRUST CSF – Validated Assessment | Assessment window per HITRUST MyCSF schedule | 4 weeks for readiness | Readiness assessment 60 days before assessment start |
| GDPR DPA Registrations | 30 days before expiration of registration period | 10 business days | Renewal Critical Date set to 60 days before expiration |
| Corporate Qualifications (Annual Reports) | Per state-specific filing deadline | 10 business days | Renewal Critical Date set to 45 days before state deadline |

#### 5.3.2 Renewal Procedure

| Step | Action | System/Record | Responsible |
|---|---|---|---|
| 1 | GRC platform generates automated renewal alert at Renewal Critical Date minus Total Lead Time. Auto-assigned task to Regulatory Licensing Manager. | GRC Platform (LogicGate or equivalent) | Automated |
| 2 | Regulatory Licensing Manager acknowledges alert within 3 business days and initiates a Renewal Project record in the GRC system. | GRC Platform: Project Record | Regulatory Licensing Manager |
| 3 | Renewal Project record auto-creates subtasks for required evidence collection, routed to the relevant Control Owners and BU Compliance Liaisons. | GRC Platform: Subtasks | Automated per pre-configured templates |
| 4 | Evidence collection due date: Renewal Critical Date minus 30 days. | GRC Platform | Control Owners |
| 5 | Regulatory Licensing Manager compiles renewal package and conducts completeness review. | Legal Document Management System | Regulatory Licensing Manager |
| 6 | Internal review chain (per §5.2.1, Step 3). Completed and approved no later than Renewal Critical Date minus 10 business days. | GRC Platform Workflow | Review Chain |
| 7 | GC final sign-off. | GRC Platform | GC |
| 8 | Submission to regulator. Confirmation receipt uploaded. | GRC Platform | Regulatory Licensing Manager |
| 9 | Post-submission tracking per §5.2.2. | GRC Platform | Regulatory Licensing Manager |

### 5.4 SOC 2 Type II Examination Management

This section provides the detailed procedure for Meridian's annual SOC 2 Type II examination cycle, addressing the AICPA *Trust Services Criteria* (TSC) Security, Availability, and Confidentiality categories in-scope for the Meridian SaaS Platform.

#### 5.4.1 Annual Examination Cycle

| Phase | Timeframe (Relative to Examination Start) | Activities | Key Outputs |
|---|---|---|---|
| **Pre-Assessment** | T-120 days to T-90 days | Readiness self-assessment against TSC; gap identification; remediation sprint if needed | Readiness Assessment Report |
| **Auditor Engagement** | T-90 days to T-60 days | Engagement letter executed; scope confirmed; control listing finalized | Signed Engagement Letter |
| **Evidence Collection** | T-60 days to T-0 (Examination Start) | Control Owners compile and upload evidence; Regulatory Licensing Manager reviews for completeness | Evidence Package |
| **Fieldwork** | T-0 to T+60 days | Auditor testing; inquiry; onsite/virtual walkthroughs; sample testing | Auditor Requests |
| **Reporting** | T+60 days to T+90 days | Management representation letter signed; draft report reviewed by CISO, CCO, and GC | Final SOC 2 Type II Report |
| **Distribution** | T+90 days onward | Report distributed to customers under NDA; bridge letter provision | SOC 2 Report Package |

#### 5.4.2 In-Scope Controls (SOC 2)

Meridian maintains the following control categories, mapped to the AICPA TSC (TSP Section 100, 2017):

**CC1: Control Environment**
- *CC1.1:* Meridian maintains a documented organizational structure with clear lines of authority. The Board-Level AI Governance Committee provides oversight of the compliance program.
- *CC1.2:* The Code of Conduct (SOP-HR-001) is acknowledged annually by all employees.
- *Control Owner:* Chief Compliance Officer

**CC2: Communication and Information**
- *CC2.1:* Control Owners are responsible for identifying and communicating relevant information to enable internal control over financial reporting and SOC 2 compliance.
- *CC2.2:* Internal control deficiencies are communicated to those responsible for taking corrective action, up to the Board.
- *Control Owner:* Chief Compliance Officer

**CC3: Risk Assessment**
- *CC3.1:* The Enterprise Risk Management (ERM) framework (SOP-RISK-001) includes a specific risk domain for "Regulatory & Compliance Risk."
- *CC3.2:* A fraud risk assessment is performed annually, considering pressures and opportunities.
- *Control Owner:* Chief Risk Officer (queries directed to CCO for licensing-specific risks)

**CC4: Monitoring Activities**
- *CC4.1:* Continuous monitoring of SOC 2 controls is performed through the GRC platform, with control self-assessments quarterly.
- *CC4.2:* The Chief Compliance Officer reports on monitoring results to the Audit Committee semi-annually.
- *Control Owner:* Chief Compliance Officer

**CC5: Control Activities (Selection and Development)**
- *CC5.1:* Meridian maintains a Control Matrix listing all controls mapped to the TSC, including control descriptions, test procedures, frequency, and Control Owners.
- *CC5.2:* Controls are selected and developed to mitigate risks to the achievement of the Trust Services Criteria.
- *Control Owner:* CISO (jointly with CCO for SOC 2 scope)

**CC6: Logical and Physical Access Controls**
- *CC6.1:* Access to the Meridian SaaS Platform is managed through Role-Based Access Control (RBAC). User access reviews are performed quarterly by system owners.
- *CC6.2:* Physical access to Meridian data centers (co-location facilities in Boston, MA, and Ashburn, VA) is restricted to authorized personnel with biometric access controls. Vendor access logs are reviewed monthly.
- *CC6.3:* Multi-Factor Authentication (MFA) is enforced for all privileged accounts and remote access to production environments.
- *Control Owner:* CISO

**CC7: System Operations**
- *CC7.1:* Change management for the production environment follows the Change Management SOP (SOP-IT-005), requiring CAB approval for all production changes.
- *CC7.2:* Security patches are deployed per the Vulnerability Management SLA (SOP-IS-011): Critical patches within 7 days, High within 30 days.
- *CC7.3:* Capacity monitoring alerts are configured for CPU, memory, and storage at thresholds of 75% (warning) and 90% (critical).
- *Control Owner:* VP IT Operations

**CC8: Change Management**
- *CC8.1:* All changes to infrastructure, software, and data are authorized, designed, developed, configured, documented, tested, approved, and implemented in accordance with SOP-IT-005.
- *CC8.2:* Emergency changes require post-implementation review within 24 hours.
- *Control Owner:* VP IT Operations / CISO

**CC9: Risk Mitigation**
- *CC9.1:* The ERM framework identifies and assesses risks, including those related to vendor management. A Vendor Risk Management program (SOP-VRM-001) is in place.
- *Control Owner:* Chief Risk Officer

**Additional Criteria (per AICPA TSP):**
- **A1.1 (Availability):** The Availability Management Plan documents Recovery Time Objectives (RTO) = 4 hours and Recovery Point Objectives (RPO) = 15 minutes for critical systems. Annual DR tests are conducted per SOP-IT-019 (Disaster Recovery).
- **C1.1 (Confidentiality):** Confidential information is identified and classified per the Data Classification Policy (SOP-IS-008). Data Loss Prevention (DLP) tools monitor egress points. Encryption standards: AES-256 for data at rest; TLS 1.3 for data in transit.

#### 5.4.3 SOC 2 Evidence Management

Control Owners upload evidence to the GRC platform's evidence repository. Evidence must be:
- **Timestamped:** Evidence must clearly show the period it covers.
- **Attributable:** Evidence must identify the system or individual that generated it.
- **Complete:** Evidence for a control must address all aspects of the control description.
- **Retained:** SOC 2 evidence is retained for a minimum of 7 years per Meridian's Records Retention Schedule.

### 5.5 State-by-State Regulatory Requirements Management

#### 5.5.1 Financial Services Licensing State Requirements

Meridian tracks state-specific requirements using a Matrix within the GRC platform. Key tracked attributes per state/per license type:

| Attribute | Description |
|---|---|
| Licensing Authority | State agency (e.g., Texas OCCC, California DFPI) |
| License Type | Money Transmitter, Lender, Loan Broker, etc. |
| NMLS Status | Whether the state participates in NMLS for this license type |
| Annual Report Deadline | Due date for annual reports or call reports |
| Assessment/Exam Cycle | Expected cadence of routine regulatory examinations |
| Bond Requirements | Current bond amount and issuer details |
| Net Worth Requirements | Whether the state has minimum net worth or tangible net worth requirements |
| BSA/AML Reporting | Whether SAR/CTR reporting obligations attach to the license |

#### 5.5.2 Corporate Qualification State Requirements

For each state where Meridian is qualified to do business, the following is tracked:
- Registered Agent name and address
- Annual Report filing deadline
- Franchise Tax / Annual Fee deadline
- State Secretary of State Business Entity Search confirmation (verified semi-annually)

### 5.6 Compliance Verification

#### 5.6.1 Verification Cadence

| Regulatory Instrument Category | Verification Cadence | Verification Method |
|---|---|---|
| Active Licenses (all types) | Quarterly | Automated check against License Inventory in GRC; manual visual verification that physical/digital licenses match |
| SOC 2 Controls (all CC series) | Quarterly | Control Self-Assessment (CSA) completed by Control Owners and reviewed by CCO |
| State Corporate Qualifications | Semi-Annually | Paralegal confirms "Good Standing" status on each State's Secretary of State portal |
| GDPR DPA Registrations | Annually | CPO/DPO confirms valid registration on each EU member state DPA portal |
| CE Marking / EU MDR Certificates | Per notified-body surveillance cycle | VP Clinical AI confirms ongoing compliance with QMS requirements |

#### 5.6.2 Compliance Verification Procedure

1. **Verification Task Generation:** Quarterly, the GRC platform generates Compliance Verification Tasks for all active Regulatory Instruments, auto-assigned to the Regulatory Licensing Manager.
2. **Evidence Collection:** The Manager requests status updates from BU Compliance Liaisons and Control Owners.
3. **Discrepancy Handling:** Any discrepancy (expired license, mismatch, control failure) is logged as an Incident (per §8) within 24 hours of identification.
4. **Verification Sign-Off:** The CCO reviews the quarterly Compliance Verification Report and provides digital sign-off in the GRC platform.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Control Owner |
|---|---|---|
| **ADM-017-01** | Segregation of Duties: License application preparer (Regulatory Licensing Manager) is distinct from application approver (CCO/GC). | CCO |
| **ADM-017-02** | Dual Authorization: All regulatory filings must be digitally signed by both the preparer and the approving attorney. | GC |
| **ADM-017-03** | Background Checks: All personnel with access to NMLS or state regulatory portals undergo enhanced background checks per SOP-HR-009. | VP HR |
| **ADM-017-04** | Periodic Review: This SOP is reviewed biennially by the CCO and GC, with ad-hoc reviews triggered by material regulatory changes. | CCO |
| **ADM-017-05** | Vendor Due Diligence: Regulatory consultants and outside counsel engaged for licensing matters undergo Vendor Risk Assessment per SOP-VRM-001. | CISO/CCO |

### 6.2 Technical Controls

| Control ID | Control Description | Applied To |
|---|---|---|
| **TEC-017-01** | GRC Platform Access Control: Access to the GRC License Inventory module is restricted by RBAC; read-only access for BU Compliance Liaisons; full access for Legal & Compliance personnel. | GRC Platform |
| **TEC-017-02** | Audit Logging: All changes to Regulatory Instrument records in the GRC platform are immutably logged with timestamp, user ID, and nature of change. | GRC Platform |
| **TEC-017-03** | Encryption at Rest: The Legal Document Management System storing licensing files uses AES-256 encryption (aligned with SOC 2 control CC6.1). | Legal DMS |
| **TEC-017-04** | Automated Renewal Alerts: The GRC platform generates automated email and dashboard alerts based on Renewal Critical Dates. | GRC Platform (Notify Module) |
| **TEC-017-05** | Document Retention: Licensing records and SOC 2 evidence are retained for a minimum of 7 years with a litigation hold capability. | Meridian DMS |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | Metric | Target | Measurement Method |
|---|---|---|---|
| **KPI-LEGC-017-01** | **License Renewal On-Time Rate** | ≥ 98% (renewals submitted before statute expiration) | GRC Report: count of on-time renewals / total renewals |
| **KPI-LEGC-017-02** | **Renewal Cycle Time** | Average ≤ 45 calendar days from alert to submission | GRC Analytics: timestamp delta (submission date - alert date) |
| **KPI-LEGC-017-03** | **RLIA Completion Timeliness** | ≥ 95% of RLIAs completed within stated SLA (per complexity tier) | GRC Dashboard |
| **KPI-LEGC-017-04** | **SOC 2 Control Effectiveness** | Zero (0) material exceptions in annual examination | SOC 2 Type II Report |
| **KPI-LEGC-017-05** | **Control Deficiency Remediation** | Critical findings: 100% remediated within 30 days; Non-critical: 100% remediated within 90 days | GRC Issue Tracker |
| **KPI-LEGC-017-06** | **Unlicensed Activity Incidents** | Zero (0) incidents of confirmed unlicensed regulated activity | Incident Management Log |
| **KPI-LEGC-017-07** | **Regulatory Inquiry Response Timeliness** | 100% responses within regulator-specified timeframe or 10 business days (whichever is shorter) | Regulatory Communication Log |

### 7.2 Dashboards and Reporting

| Report Name | Audience | Cadence | Contents |
|---|---|---|---|
| **License Status Dashboard** | CCO, GC, BU Heads | Monthly (automated push, first business day of the month) | License inventory with status indicators (green/yellow/red), upcoming renewals (next 90 days), overdue items |
| **SOC 2 Control Monitoring Report** | CISO, CCO, Audit Committee | Quarterly | Control self-assessment results, any identified deficiencies, remediation progress |
| **Compliance Verification Report** | CCO, GC | Quarterly | Summary of verification activities, discrepancies found, and resolution status |
| **Board-Level Regulatory Report** | Board-Level AI Governance Committee, Audit Committee | Semi-Annually | High-level regulatory landscape, material risks, license portfolio health, enforcement exposure |
| **Regulatory Change Impact Report** | CCO, GC, Relevant BU Heads | Ad-hoc (within 10 days of a significant regulatory change) | Analysis of the change, impacted Regulatory Instruments, required action items |

### 7.3 Escalation Reporting Triggers

Automated alerts are generated from the GRC platform and escalated if the following conditions are met:
- **Renewal Overdue > 5 Business Days:** Alert to CCO and GC.
- **SOC 2 Control Failure (Critical):** Immediate alert to CISO and CCO.
- **Material Regulatory Event:** Immediate alert to CCO and GC; CCO escalates to Audit Committee Chair within 48 hours.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

| Exception Type | Examples | Process |
|---|---|---|
| **Renewal Delay Exception** | Circumstances beyond Meridian's control (e.g., regulator processing delay) prevent on-time renewal. | File Provisional Renewal Extension Request with regulator; document fully in GRC. GC and CCO approve the exception. |
| **Control Exception (SOC 2)** | A SOC 2 control fails during continuous monitoring or the annual examination. | Follow the SOC 2 Remediation Plan (see §8.2). CISO and CCO escalate per severity. |
| **New Product Launch Without Full License (Conditional)** | A business unit requests a conditional launch in a jurisdiction while a license is pending, where the regulator permits such activity. | Explicit written regulatory confirmation required. Risk acceptance signed by CCO, GC, and BU Head. Board notification if revenue > $1M. |
| **Interpretive Exception** | Ambiguity in whether a license is required for a specific activity. | Legal opinion from GC (or external counsel if instructed by GC). Opinion documented and stored in GRC as an Interpretive Memo. |

### 8.2 SOC 2 Remediation Plan

If a SOC 2 control deficiency or exception is identified (whether through internal monitoring, the annual examination, or an external inquiry), the following mandatory remediation process is initiated:

1.  **Immediate Containment (within 24 hours):** CISO or designated Control Owner implements temporary compensating controls, if the exception poses an active risk (e.g., restricting access to an affected system).
2.  **Root Cause Analysis (RCA):** A formal RCA is documented in the GRC platform within 5 business days of identification. The RCA must identify:
    - The failed control and the associated Trust Services Criterion
    - The root cause (design failure, operational failure, lack of training)
    - The impact on the system and data
3.  **Remediation Plan:** The Control Owner, working with the CISO and CCO, develops a Remediation Plan within 10 business days of identification. The plan must include specific corrective actions, a timeline for completion, and a verification step.
4.  **Remediation Execution and Verification:**
    - **Critical Findings:** Remediation complete within 30 calendar days. CCO verifies.
    - **Non-Critical Findings:** Remediation complete within 90 calendar days. Control Owner verifies, CCO confirms.
5.  **Auditor Notification:** For exceptions identified outside the annual examination that are deemed material to the SOC 2 opinion, the CCO notifies the external audit firm within 5 business days.

### 8.3 Authority for Exception Approval

| Exception Type | Approver(s) |
|---|---|
| Routine extension (≤ 30 days) | CCO |
| Significant extension (> 30 days) or involving enforcement risk | CCO and GC |
| Conditional launch (all) | CCO, GC, and relevant BU Head |
| Interpretive opinions | GC |
| SOC 2 Remediation Plan | CISO and CCO |

---

## 9. Training Requirements

### 9.1 Training Assignments

| Audience | Training Module | Frequency | Delivery Method | Tracking |
|---|---|---|---|---|
| **Legal & Compliance Staff** (including Regulatory Licensing Manager, BU Liaisons) | REG-101: Advanced Regulatory Licensing Management | Annually + upon significant regulatory change | Instructor-led or live virtual | LMS (Workday) |
| **All Control Owners** (IT, Security, Compliance) | REG-102: SOC 2 Control Ownership and Evidence Management | Annually | eLearning with assessment | LMS (Workday) |
| **BU Heads and Product Managers** | REG-103: Regulatory Licensing Impact Awareness | Annually | eLearning | LMS (Workday) |
| **All Employees** | CORP-001: Code of Conduct & Compliance Awareness (includes overview of prohibition of unlicensed activity) | Annually | eLearning | LMS (Workday) |

### 9.2 Training Content and Review

The Regulatory Licensing Manager, in collaboration with the CCO and the Learning & Development team, is responsible for maintaining and updating the content of training modules REG-101, REG-102, and REG-103. Content must be reviewed at least annually to ensure alignment with the current regulatory landscape and Meridian's internal procedures.

### 9.3 Compliance Tracking

The CCO shall review training completion metrics quarterly. Any employee who has not completed required training within 30 days of the due date shall be flagged to their manager and the CCO. Access to relevant systems (GRC, NMLS) may be suspended for non-completion of mandatory training, per the System Access Policy (SOP-IT-001).

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| SOP-PROD-003 | Product Approval and New Market Entry Process | RLIA is a mandatory sub-process of this SOP |
| SOP-RISK-001 | Enterprise Risk Management Framework | Controls and risk escalation align with ERM framework |
| SOP-LEGC-012 | Intellectual Property Management | Out-of-scope separation of duties |
| SOP-IT-019 | Disaster Recovery and Business Continuity | Availability controls for SOC 2 |
| SOP-IT-005 | Change Management | SOC 2 control CC8.1 evidence source |
| SOP-IS-011 | Vulnerability and Patch Management | SOC 2 control CC7.2 evidence source |
| SOP-IS-008 | Data Classification and Handling Policy | SOC 2 Confidentiality control C1.1 source |
| SOP-VRM-001 | Vendor Risk Management | Vendor due diligence for regulatory consultants |
| SOP-HR-001 | Code of Conduct | Control environment for SOC 2 CC1.2 |
| SOP-HR-009 | Background Check Policy | Enhanced checks for licensing portal access |
| SOP-HR-042 | Professional Credential Management | Out-of-scope separation |
| SOP-IT-001 | System Access Policy | Enforcement for non-completion of training |
| SOP-FIN-019 | Surety Bond Management | Financial management of license bonds |
| SOP-OPS-008 | Facilities Compliance | Out-of-scope environmental permits |

### 10.2 External Standards and Regulations

| Reference | Identifier | Relevance |
|---|---|---|
| AICPA Trust Services Criteria (TSP Section 100) | *2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy* | SOC 2 examination criteria |
| SOC 2 Guide | *AICPA Guide: Reporting on an Examination of Controls at a Service Organization Relevant to Security, Availability, Processing Integrity, Confidentiality, or Privacy* | SOC 2 examination methodology |
| HITRUST CSF | *HITRUST CSF v11.2* | HITRUST certification requirements |
| ISO/IEC 27001:2022 | *Information Security, Cybersecurity and Privacy Protection — Information Security Management Systems — Requirements* | ISO 27001 certification standard |
| FDIC / State Regulatory Standards | *Money Transmitter Model Law, relevant state statutes* | Financial services licensing basis |
| 21 CFR Parts 800-898 | *FDA Medical Device Regulations* | FDA 510(k) clearance basis |
| EU MDR 2017/745 | *Regulation (EU) 2017/745 on Medical Devices* | CE marking basis |
| EU AI Act 2024/1689 | *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence* | High-risk AI system conformity basis |
| HIPAA | *45 CFR Parts 160 and 164* | Healthcare data privacy and security rules |

---

## 11. Revision History

| Version | Effective Date | Last Reviewed | Author | Summary of Changes |
|---|---|---|---|---|
| 1.0 | 2020-03-15 | N/A | M. Chen (former CCO) | Initial publication of Regulatory Licensing Management SOP. |
| 2.0 | 2021-05-01 | 2021-04-15 | M. Chen | Added SOC 2 procedures following initial Type II certification. Integrated NMLS tracking for state financial services licenses. |
| 3.0 | 2022-11-10 | 2022-10-20 | T. Anderson (CCO) | Full rewrite to align with new GRC platform (LogicGate implementation). Added RLIA procedure (Section 5.1). Revised RACI matrix to reflect post-restructuring roles. |
| 4.0 | 2024-03-05 | 2024-02-15 | T. Anderson | Added EU AI Act and updated EU MDR references. Included CE marking under MDR. Added HITRUST CSF controls. Updated SOC 2 TSC mapping for 2024 cycle. Expanded state-by-state tracking requirements (§5.5). |
| 5.0 | 2025-02-23 | 2025-01-30 | T. Anderson | Major revision: restructured sections for clarity; added detailed SOC 2 controls (CC1-CC9, A1.1, C1.1); introduced quantitative KPIs; defined training modules; updated to ISO 27001:2022. Aligned with NIST AI RMF attestation requirements. |
| 5.1 | 2026-01-20 | 2026-01-20 | T. Anderson | Minor revision: updated regulatory reference for EU AI Act to final published version; added bridge letter procedure for SOC 2; refined renewal lead times for state money transmitter licenses; corrected typographical errors; added KPI-LEGC-017-07. |

---

**Document End**
**SOP-LEGC-017 | Version 5.1**
**All printed copies are uncontrolled. Refer to the GRC platform for the current official version.**