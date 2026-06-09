---
sop_id: "SOP-DGP-009"
title: "Cross-Border Data Transfer"
business_unit: "Data Governance & Privacy"
version: "3.4"
effective_date: "2024-12-11"
last_reviewed: "2025-06-07"
next_review: "2025-12-11"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Cross-Border Data Transfer

## SOP-DGP-009, Version 3.4

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the governance framework, operational controls, and procedural requirements governing the transfer of Personal Data and Personal Health Information (PHI) across jurisdictional borders within Meridian Health Technologies, Inc. and between Meridian and its third-party processors, sub-processors, and partners. The purpose is to ensure that all cross-border data flows comply with applicable data protection laws—principally the General Data Protection Regulation (GDPR)—while enabling Meridian's global business operations, clinical AI deployments, and financial services delivery.

This SOP operationalizes Meridian's commitment under Article 44 of the GDPR that any transfer of personal data to a third country or international organization shall take place only subject to the conditions laid down in the GDPR's Chapter V, ensuring that the level of protection guaranteed by the GDPR is not undermined.

### 1.2 Scope

#### 1.2.1 Geographic and Organizational Scope

This SOP applies to:

- All Meridian Health Technologies, Inc. legal entities, including Meridian Health Technologies GmbH (Berlin), Meridian Health Technologies UK Ltd. (London), Meridian Health Technologies Pte. Ltd. (Singapore), Meridian Health Technologies Canada Inc. (Toronto), and the corporate headquarters in Boston, MA.
- All permanent, temporary, and contract personnel who access, process, or manage data subject to cross-border transfer restrictions.
- All third-party vendors, processors, and sub-processors engaged by Meridian that receive, access, or process data originating from the European Union (EU) or European Economic Area (EEA).

#### 1.2.2 Data Scope

This SOP covers the following categories of data when transferred across international borders:

| Data Category | Description | Applicable Regulations |
|---|---|---|
| EU/EEA Personal Data | Any information relating to an identified or identifiable natural person in the EU/EEA | GDPR, EU Member State laws |
| EU/EEA Special Category Data | Health data, genetic data, biometric data of EU/EEA data subjects | GDPR Articles 9, 49 |
| PHI of EU Data Subjects | Protected Health Information combined with EU personal data | GDPR, HIPAA (where applicable) |
| Clinical AI Training Data | Datasets containing EU personal data used for model training | GDPR, EU AI Act |
| Financial Services Data | Credit scoring, lending, and payment data of EU data subjects | GDPR, SR 11-7 (US) |

#### 1.2.3 Business Unit and System Scope

This SOP applies to all Meridian business units and the following systems:

- **Clinical AI Platform**: Patient risk scoring data transfers between EU hospitals and US-based ML training infrastructure.
- **HealthPay Financial Services**: Payment processing data flows between EU merchants, US payment rails, and Singapore analytics.
- **MedInsight Analytics**: Population health data transfers from EU health systems to US-based Snowflake instances.
- **Meridian SaaS Platform**: Multi-tenant infrastructure spanning AWS us-east-1 and eu-west-1 regions.
- **Internal Corporate Systems**: HR data (Workday), collaboration (Microsoft 365), and CRM (Salesforce) containing EU employee and customer data.

#### 1.2.4 Out of Scope

- Transfers of data that are exclusively domestic within a single jurisdiction and do not involve routing, storage, or access from another jurisdiction.
- Data that has been fully and irreversibly anonymized in accordance with GDPR Recital 26 standards and confirmed as anonymous by the Data Governance team.
- Transfers between EU/EEA Member States (these are governed by intra-EU data sharing rules, though adequate safeguards per GDPR Article 46 may still apply).

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Adequacy Decision** | A formal decision by the European Commission confirming that a third country, territory, sector, or international organization ensures an adequate level of data protection, enabling free flow of personal data without additional safeguards. |
| **Binding Corporate Rules (BCRs)** | Legally binding internal data protection rules approved by a competent EU supervisory authority, governing transfers within a multinational corporate group. |
| **Cross-Border Data Transfer** | Any transmission, access, processing, or storage of personal data that crosses a national boundary, whether by electronic transmission, remote access, or physical media transport. |
| **Data Exporter** | The Meridian entity or controller/processor in the EU/EEA that transfers personal data to a recipient outside the EU/EEA. |
| **Data Importer** | The entity outside the EU/EEA that receives personal data from a Data Exporter. |
| **Data Protection Impact Assessment (DPIA)** | A process to identify and minimize data protection risks in a project or processing activity, required under GDPR Article 35 for high-risk processing. |
| **European Data Protection Board (EDPB)** | The independent EU body that ensures consistent application of the GDPR and issues guidance on data protection matters including international transfers. |
| **Restricted Transfer** | A cross-border transfer to a third country for which no adequacy decision exists and for which Article 46 safeguards have not been established. |
| **Standard Contractual Clauses (SCCs)** | European Commission-approved model contract clauses providing appropriate safeguards for data transfers to third countries (Commission Implementing Decision (EU) 2021/914 of 4 June 2021). |
| **Supplementary Measures** | Technical, contractual, and organizational measures implemented in addition to SCCs or BCRs to ensure effective protection equivalent to EU standards, particularly in light of third-country surveillance laws. |
| **Third Country** | Any country outside the EU/EEA not subject to an adequacy decision. |
| **Transfer Impact Assessment (TIA)** | A documented assessment evaluating the laws and practices of the destination country, the effectiveness of transfer safeguards, and the necessity for supplementary measures. |

### 2.2 Acronyms

| Acronym | Full Form |
|---|---|
| BCR | Binding Corporate Rules |
| CJEU | Court of Justice of the European Union |
| CPO/DPO | Chief Privacy Officer / Data Protection Officer |
| DPIA | Data Protection Impact Assessment |
| EDPB | European Data Protection Board |
| EEA | European Economic Area |
| EU | European Union |
| HR | Human Resources |
| ICO | Information Commissioner's Office (UK) |
| KMS | Key Management Service |
| MFT | Managed File Transfer |
| PHI | Protected Health Information |
| ROPA | Record of Processing Activities |
| SaaS | Software as a Service |
| SCC | Standard Contractual Clauses |
| Schrems II | Data Protection Commissioner v. Facebook Ireland Limited, Maximillian Schrems (C-311/18) |
| SLA | Service Level Agreement |
| TIA | Transfer Impact Assessment |
| VPC | Virtual Private Cloud |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following RACI matrix defines responsibility, accountability, consulted, and informed roles for cross-border data transfer activities:

| Activity | CPO/DPO | General Counsel | VP IT Ops | VP Engineering | Business Unit VP | CISO | Chief Compliance Officer | Data Governance Manager |
|---|---|---|---|---|---|---|---|---|
| Transfer Impact Assessment approval | **A** | **A** | R | C | C | C | C | R |
| SCC execution and maintenance | **A** | R | I | I | I | I | I | R |
| Supplementary measures implementation | C | I | **A** | R | I | R | C | C |
| Cross-border transfer request approval | **A** | R | I | I | R | I | C | C |
| ROPA updates for transfers | I | I | I | I | R | I | C | **A** |
| Data subject rights fulfillment (transfers) | **A** | C | I | I | I | I | C | R |
| Breach notification (cross-border) | R | **A** | I | I | I | R | C | R |
| DPIA triggering for transfers | R | C | I | I | R | I | C | **A** |
| Annual transfer audit | C | R | C | C | C | C | **A** | R |
| Vendor transfer compliance review | R | C | I | I | R | C | **A** | R |

**R=Responsible (executes) | A=Accountable (approves) | C=Consulted | I=Informed**

### 3.2 Named Role Responsibilities

#### 3.2.1 Chief Privacy Officer / Data Protection Officer (Dr. Klaus Weber)
- Approves all cross-border data transfers involving EU/EEA personal data.
- Maintains the register of active SCCs, BCRs, and Transfer Impact Assessments.
- Serves as primary point of contact for EU supervisory authorities regarding international transfers.
- Reviews and updates this SOP annually.
- Approves supplementary measures recommendations.

#### 3.2.2 General Counsel (Maria Gonzalez)
- Provides legal review of Transfer Impact Assessments, with particular attention to third-country legal analysis.
- Approves SCC modifications and any derogation-based transfers under GDPR Article 49.
- Manages regulatory inquiries and enforcement actions related to cross-border transfers.
- Advises on legislative changes affecting transfer mechanisms.

#### 3.2.3 VP of IT Operations (Samantha Torres)
- Implements and maintains technical supplementary measures (encryption, tokenization, data residency controls).
- Ensures AWS region configurations align with approved transfer mechanisms.
- Manages data flow mapping and technical documentation for all cross-border pipelines.

#### 3.2.4 VP of Engineering (David Park)
- Architects data flows to minimize unnecessary cross-border transfers.
- Ensures platform architecture supports data residency requirements.
- Reviews and approves technical designs for new cross-border data flows.

#### 3.2.5 Chief Information Security Officer (Rachel Kim)
- Validates technical safeguards for in-transit and at-rest encryption.
- Monitors cross-border access patterns for anomalies.
- Ensures SOC 2 controls extend to cross-border data flows.
- Reviews third-country government access risks as part of the TIA security assessment.

#### 3.2.6 Chief Compliance Officer (Thomas Anderson)
- Coordinates cross-border transfer audits and regulatory examinations.
- Tracks regulatory developments affecting cross-border data transfer compliance.
- Reports transfer compliance metrics to the AI Governance Committee and Board.

#### 3.2.7 Data Governance Manager (Position reports to CPO/DPO)
- Maintains the cross-border data flow inventory and mapping.
- Prepares initial Transfer Impact Assessments for CPO/DPO and General Counsel review.
- Manages the SCC lifecycle (drafting, execution, renewal, archiving).
- Maintains the ROPA with cross-border transfer annotations.

#### 3.2.8 Business Unit Vice Presidents
- Identify and request approval for new cross-border data flows within their business units.
- Ensure business unit staff complete required training.
- Participate in DPIAs where cross-border transfers are a processing element.

---

## 4. Policy Statements

### 4.1 General Principles

**P1 - Lawful Transfer Requirement:** Meridian shall not transfer EU/EEA personal data to any third country or international organization unless a valid legal mechanism under GDPR Chapter V is in place prior to the transfer.

**P2 - Transfer Minimization:** Meridian shall, by design, minimize cross-border transfers of personal data. Where business purposes can be achieved without transferring data outside the EU/EEA, local processing shall be preferred.

**P3 - Supplementary Measures by Default:** For all transfers relying on SCCs or BCRs to third countries without an adequacy decision, Meridian shall conduct a Transfer Impact Assessment and implement documented supplementary measures where necessary to ensure a level of protection essentially equivalent to EU law.

**P4 - Transparency:** Meridian shall inform data subjects, through its privacy notices, of the existence of cross-border transfers, the countries involved, the transfer mechanism relied upon, and the means to obtain a copy of the safeguards.

**P5 - Accountability:** All cross-border data transfers shall be documented in the ROPA, with SCCs or BCRs maintained in a central register, and Transfer Impact Assessments retained on file for supervisory authority inspection.

**P6 - Prohibition of Unauthorized Transfers:** No employee, contractor, or vendor shall initiate a cross-border transfer of EU/EEA personal data without prior documented approval through the process defined in Section 5 of this SOP.

### 4.2 Transfer Mechanism Hierarchy

Meridian shall apply transfer mechanisms in the following order of preference:

1. **Adequacy Decision:** Where the destination country benefits from a valid European Commission adequacy decision, transfers may proceed freely without additional safeguards, provided the adequacy decision covers the specific transfer.
2. **Binding Corporate Rules (BCRs):** For intra-group transfers, Meridian shall maintain approved BCRs where feasible. BCRs are the preferred mechanism for recurring intra-Meridian transfers.
3. **Standard Contractual Clauses (SCCs):** For transfers to third parties or intra-group transfers where BCRs are not yet approved, the current EU SCCs (2021/914) shall be executed, accompanied by a TIA and supplementary measures.
4. **Derogations (Article 49):** Derogations shall be used only in exceptional, non-recurring circumstances and only where no other mechanism is available. Use requires prior approval from the General Counsel.

### 4.3 Data Subject Rights

Data subjects whose personal data is transferred cross-border retain all rights under GDPR Chapter III. Meridian shall respond to data subject requests related to cross-border transfers, including requests for copies of safeguards. Procedures for handling such requests are documented in SOP-DGP-004 (Data Subject Rights Management).

Meridian aims to respond to data subject access requests related to cross-border transfers within the timelines established by applicable regulations. Requests shall be logged, acknowledged promptly, and processed without undue delay.

### 4.4 DPIA Requirements

Cross-border transfers that involve high-risk processing or large-scale transfers of special category data require a Data Protection Impact Assessment. The DPIA shall specifically address the risks associated with the international transfer, including third-country government access risks identified in the TIA.

When a DPIA is required, it shall be completed prior to initiation of the transfer.

---

## 5. Detailed Procedures

### 5.1 Cross-Border Transfer Request and Approval Process

#### 5.1.1 Initiating a Transfer Request

Any Meridian employee or contractor who identifies a business need requiring cross-border transfer of EU/EEA personal data shall submit a Cross-Border Transfer Request via the Meridian Service Portal (Jira Service Management: Data Governance queue).

**Form FRM-DGP-009-1: Cross-Border Transfer Request**

| Field | Description | Required |
|---|---|---|
| Requestor Name & BU | Name and business unit of requesting individual | Yes |
| Business Justification | Detailed explanation of why data must be transferred cross-border | Yes |
| Data Categories | Types of personal data involved (use Meridian Data Taxonomy) | Yes |
| Data Subject Categories | e.g., Patients, Providers, Employees, Customers | Yes |
| Source Country(ies) | EU/EEA country of origin | Yes |
| Destination Country(ies) | Third country(ies) receiving data | Yes |
| Data Volume | Estimated records per month | Yes |
| Special Category Data? | Yes/No; if Yes, specify Article 9 grounds | Yes |
| Data Importer Details | Legal entity name, address, and contact | Yes |
| Processing Purpose | Specific processing activity description | Yes |
| Frequency | One-time / Recurring (specify interval) | Yes |
| Technical Transfer Method | API, MFT, Snowflake replication, AWS cross-region, etc. | Yes |
| Retention Period in Third Country | Duration data will be stored/processed outside EU | Yes |
| Sub-processor Involvement | Will the importer onward-transfer? | Yes |
| Encryption Details | In-transit and at-rest encryption protocols | Yes |

#### 5.1.2 Initial Triage

Upon submission, the Data Governance team shall perform initial triage within **3 business days**:

1. **Completeness Check:** Verify all required fields contain adequate information.
2. **Existing Transfer Check:** Review the Cross-Border Data Flow Inventory (maintained in Collibra) for existing approved transfers covering the same data and destination. If an existing approved transfer covers the request, the requestor is notified and a reference to the existing mechanism is provided.
3. **Categorization:** Assign the request a preliminary risk tier:
   - **Tier 1 (Low Risk):** Non-sensitive personal data to an adequacy decision country, limited volume.
   - **Tier 2 (Medium Risk):** Personal data to a non-adequacy country with strong supplementary measures; or special category data to an adequacy country.
   - **Tier 3 (High Risk):** Large-scale transfers of special category data to a non-adequacy country; transfers involving government access risk; or transfers enabling high-risk AI processing.

#### 5.1.3 Transfer Mechanism Determination

The Data Governance Manager, in consultation with the CPO/DPO, determines the appropriate transfer mechanism based on the destination country and data categories:

**Decision Flow for Transfer Mechanism:**

```
Destination Country
├── Adequacy Decision?
│   ├── Yes → Adequacy Decision applies. Document adequacy decision in ROPA. No SCCs required.
│   └── No → Is it Intra-Group?
│       ├── Yes → BCRs approved?
│       │   ├── Yes → Apply BCRs + conduct TIA.
│       │   └── No → Execute SCCs + conduct TIA.
│       └── No → Is importer a third-party vendor?
│           ├── Yes → Execute SCCs + conduct TIA + review vendor's own TIA/supplementary measures.
│           └── No (non-EU controller) → Execute SCCs (Module 1 applicable) + conduct TIA.
```

**Current Adequacy Decisions Recognized by Meridian** (as of effective date):

| Country/Territory | Adequacy Decision Date | Scope |
|---|---|---|
| Andorra | 2010 | All transfers |
| Argentina | 2003 | All transfers |
| Canada (PIPEDA commercial) | 2002 | Commercial organizations only |
| Israel | 2011 | All transfers |
| Japan | 2019 | Private sector transfers |
| New Zealand | 2013 | All transfers |
| Republic of Korea | 2021 | All transfers (with certification) |
| Switzerland | 2000 | All transfers |
| United Kingdom | 2021 | All transfers (subject to post-Brexit review) |
| Uruguay | 2012 | All transfers |
| USA | 2023 | EU-US Data Privacy Framework certified entities only |

For transfers to the US, the importer must provide proof of active Data Privacy Framework (DPF) certification. If certification cannot be verified, the transfer shall be treated as a non-adequacy transfer requiring SCCs.

#### 5.1.4 Transfer Impact Assessment (TIA) Process

For all transfers requiring SCCs or BCRs (i.e., transfers to non-adequacy countries), a Transfer Impact Assessment shall be completed before transfer initiation.

**TIA Procedure:**

**Step 1: Data Flow Mapping** — The Data Governance team, working with the VP of IT Operations, documents the complete data flow, including all intermediary systems, sub-processors, and onward transfers. This mapping is recorded in the Meridian Data Flow Diagram tool (Lucidchart, linked to Collibra).

**Step 2: Third-Country Legal Analysis** — The General Counsel's office, with support from external local counsel where necessary, prepares an analysis addressing:

- The legal framework of the destination country regarding government access to data (surveillance laws, national security access).
- Whether the destination country's laws provide effective judicial redress for data subjects.
- Any conflicting legal obligations that the data importer may face.
- Recent regulatory guidance or enforcement actions related to the destination country.

**Step 3: Contractual Safeguard Assessment** — The Data Governance team evaluates:

- Whether the executed SCCs adequately address identified risks.
- Whether the SCCs can be enforced in practice in the destination country.
- Whether the data importer has the technical and organizational capability to comply with SCCs.

**Step 4: Supplementary Measures Determination** — Based on the legal analysis and contractual assessment, the CPO/DPO, CISO, and VP of IT Operations determine necessary supplementary measures using the EDPB's Recommendations 01/2020 on measures that supplement transfer tools:

| Risk Identified | Potential Supplementary Measures |
|---|---|
| Government access without independent oversight | End-to-end encryption with key held exclusively by Meridian EU entity; warrant canary |
| Inadequate judicial redress | Data subject notification commitment; indemnification provisions |
| Onward transfer risk | Contractual restrictions on sub-processing; prior approval requirements |
| Insufficient data minimization | Pseudonymization before transfer; tokenization in transit |
| Data localization inadequacy | AWS eu-west-1 as processing locus; restricting US access to pseudonymized data only |

**Step 5: TIA Documentation and Approval** — The completed TIA is documented using template **FRM-DGP-009-2: Transfer Impact Assessment Report**, which includes:

- Executive summary
- Data flow description
- Legal analysis (with external counsel memorandum referenced)
- Identified risks and risk ratings (using Meridian Risk Matrix)
- Supplementary measures selected
- Residual risk assessment
- Approval signatures (CPO/DPO, General Counsel)

**TIA Approval Timelines:**

| Risk Tier | TIA Completion Target | Approval Authority |
|---|---|---|
| Tier 1 (Low) | 10 business days | CPO/DPO |
| Tier 2 (Medium) | 20 business days | CPO/DPO + General Counsel |
| Tier 3 (High) | 30 business days | CPO/DPO + General Counsel + AI Governance Committee (if AI-related) |

#### 5.1.5 SCC Execution and Management

**SCC Module Selection:**

| Transfer Scenario | SCC Module |
|---|---|
| EU Controller to Non-EU Controller | Module 1 |
| EU Controller to Non-EU Processor | Module 2 |
| EU Processor to Non-EU Processor (sub-processing) | Module 3 |
| EU Processor to Non-EU Controller | Module 4 |

**SCC Execution Procedure:**

1. The Data Governance Manager drafts SCCs using Meridian's SCC template library (maintained in iManage document management system).
2. The draft incorporates:
   - Annex I.A: List of Parties (Meridian entity as exporter, vendor/entity as importer).
   - Annex I.B: Description of Transfer (data subjects, categories, purposes, retention).
   - Annex I.C: Competent Supervisory Authority (Berlin Data Protection Authority for Meridian GmbH).
   - Annex II: Technical and Organizational Measures (populated from the TIA supplementary measures determination).
   - Annex III: List of Sub-processors (if applicable, with authorization mechanism).
3. Draft SCCs are reviewed by General Counsel.
4. SCCs are executed via DocuSign by the CPO/DPO for Meridian and the authorized signatory of the data importer.
5. Executed SCCs are registered in the Cross-Border Transfer Register (SharePoint: Data Governance > Cross-Border Transfers) and linked to the ROPA entry.

**SCC Update and Renewal:**

- SCCs shall be reviewed every **2 years** and upon any material change to the transfer or applicable law.
- Upon invalidation or amendment of SCCs by the European Commission, Meridian shall transition to new SCCs within the grace period specified by the Commission (typically 18 months).

#### 5.1.6 BCR Management (Intra-Group Transfers)

Meridian maintains Binding Corporate Rules for intra-group transfers of personal data. The BCRs were submitted to the Berlin Data Protection Authority (lead authority) for approval in Q2 2024. Approval status is tracked in the Data Governance dashboard.

**BCR Applicability:** BCRs govern transfers between:
- Meridian Health Technologies GmbH (Berlin) → Meridian Health Technologies, Inc. (Boston)
- Meridian Health Technologies GmbH (Berlin) → Meridian Health Technologies UK Ltd. (London, for transfers outside adequacy scope)
- Meridian Health Technologies GmbH (Berlin) → Meridian Health Technologies Pte. Ltd. (Singapore)
- Meridian Health Technologies GmbH (Berlin) → Meridian Health Technologies Canada Inc. (Toronto, for commercial data outside PIPEDA adequacy)

**BCR Compliance Requirements:**
- All intra-group transfers must reference the Meridian BCR Policy (SOP-DGP-010).
- Employees receiving data under BCRs must complete annual BCR compliance training (see Section 9).
- A BCR compliance audit shall be conducted annually by the Chief Compliance Officer.

#### 5.1.7 Derogation-Based Transfers (Article 49)

Derogations under GDPR Article 49 may be used only in narrowly defined, exceptional circumstances. Derogation-based transfers require **pre-approval by the General Counsel**.

The following Article 49 derogations are recognized:

| Derogation | Applicable Circumstances | Approval Requirements |
|---|---|---|
| Explicit Consent (Art. 49(1)(a)) | Data subject has given explicit consent after being informed of risks | Consent form reviewed by CPO/DPO; consent logged in OneTrust |
| Contractual Necessity (Art. 49(1)(b),(c)) | Transfer necessary for performance or conclusion of contract with data subject | General Counsel review of contract |
| Important Reasons of Public Interest (Art. 49(1)(d)) | Recognized public interest basis | CEO + CPO/DPO + General Counsel approval |
| Vital Interests (Art. 49(1)(f)) | Necessary to protect vital interests of data subject incapable of giving consent | CPO/DPO + Chief Medical Officer approval; strictly interpreted |
| Compelling Legitimate Interests (Art. 49(1) subpara 2) | Not repetitive, limited number of data subjects, compelling interests not overridden by data subject rights | CEO + General Counsel approval; supervisory authority notification within 30 days |

#### 5.1.8 Post-Approval Implementation

Upon approval, the VP of IT Operations, working with the requesting business unit, implements the technical transfer:

1. **Technical Configuration:** Configure AWS regions, VPC peering, security groups, and encryption per SCC Annex II specifications.
2. **Data Inventory Update:** The Data Governance team updates the ROPA and Cross-Border Data Flow Inventory within **5 business days**.
3. **Monitoring Activation:** Data transfer monitoring rules are configured in Datadog (see Section 7).
4. **Notification to Data Subjects:** If required by the TIA or transparency obligations, the Privacy Team updates Meridian's external privacy notice to reflect the new transfer.

### 5.2 Ongoing Cross-Border Transfer Management

#### 5.2.1 Transfer Register Maintenance

The Data Governance Manager maintains the centralized Cross-Border Transfer Register with the following fields for each active transfer:

| Field | Description |
|---|---|
| Transfer ID | Unique identifier (TFR-YYYY-NNN) |
| ROPA Reference | Link to ROPA entry |
| Status | Active / Suspended / Terminated |
| Data Exporter Entity | Meridian legal entity |
| Data Importer | Legal entity name and jurisdiction |
| Transfer Mechanism | Adequacy Decision / SCC (module) / BCR / Derogation |
| SCC Execution Date | Date of execution |
| SCC Expiry / Review Date | Next review date |
| TIA Reference | Link to TIA report |
| Supplementary Measures | Brief description of key measures |
| Data Categories | Per Meridian Data Taxonomy |
| Volume (records/month) | Estimated transfer volume |
| Last Audit Date | Date of last compliance review |

#### 5.2.2 Sub-Processor Management

When a data importer engages sub-processors for processing of Meridian's EU data:

1. The data importer must obtain prior written authorization from Meridian (general written authorization with objection mechanism is acceptable under SCC Clause 7.5).
2. The data importer must flow down equivalent data protection obligations to the sub-processor via a written contract.
3. The data importer must notify Meridian of any intended changes to sub-processors at least **30 days** in advance.
4. Meridian's Data Governance team reviews sub-processor changes and may object within the 30-day notice period if the sub-processor's jurisdiction or practices introduce unacceptable risk.
5. Sub-processor engagements are tracked in the Vendor Risk Management system (OneTrust Vendorpedia).

#### 5.2.3 Transfer Suspension and Termination

A cross-border transfer shall be suspended or terminated under the following circumstances:

- The legal basis for transfer is invalidated (e.g., adequacy decision revoked, SCCs invalidated by court).
- The data importer breaches SCCs or BCRs and fails to remedy within **15 business days**.
- A TIA re-assessment determines that supplementary measures are no longer effective and residual risk exceeds Meridian's risk appetite.
- The data importer receives a government access request incompatible with EU law standards and lacks the ability to challenge it.
- The data importer ceases operations, enters insolvency, or undergoes a change of control resulting in unacceptable risk.

**Suspension Procedure:** The CPO/DPO, in consultation with General Counsel, issues a written suspension notice to the data importer, requiring cessation of data processing and secure return or deletion of data within **30 calendar days**. The VP of IT Operations implements technical measures to halt the data flow.

### 5.3 Data Subject Rights in Cross-Border Context

#### 5.3.1 DSAR Processing for Transferred Data

When a data subject exercises rights under GDPR and their data has been transferred cross-border:

1. The Data Subject Request is logged in the Privacy Request Manager (OneTrust) per SOP-DGP-004.
2. The Privacy Team identifies all cross-border transfers involving the data subject's data by querying the ROPA.
3. The Privacy Team notifies all data importers holding the data subject's data of the request within **5 business days**.
4. Data importers must respond to Meridian with relevant data or confirmation of action taken.
5. Meridian consolidates responses and provides the data subject with a comprehensive response.

Meridian shall process data subject requests related to transferred data diligently, ensuring requests are fulfilled and responses provided without undue delay.

#### 5.3.2 Transparency Obligations

Data subjects shall be informed of cross-border transfers through:

- **External Privacy Notice:** Describes categories of recipients, countries involved, mechanisms relied upon (adequacy, SCCs, BCRs), and how to obtain copies.
- **Direct Notification:** For transfers based on explicit consent, the consent form must clearly identify destination countries, absence of adequacy decision (if applicable), and specific risks.
- **Access Request Responses:** When data subjects request copies of safeguards, redacted SCCs or BCR summaries shall be provided.

### 5.4 Cross-Border Data Breach Response

#### 5.4.1 Breach Identification and Notification

In the event of a personal data breach involving cross-border transferred data:

1. **Detection and Assessment:** The Security Operations Center (SOC) team analyzes the breach per SOP-ISM-015 (Information Security Incident Response). The CISO assesses whether the breach affects EU/EEA personal data that has been transferred cross-border.
2. **Data Importer Notification:** If the breach occurs at the data importer, the importer must notify Meridian without undue delay and no later than **24 hours** from discovery, per SCC Clause 15.
3. **Supervisory Authority Notification:** The CPO/DPO determines whether the breach is notifiable to the lead supervisory authority (Berlin DPA). If notifiable, notification is made within **72 hours** of Meridian becoming aware.
4. **Data Subject Notification:** If the breach poses high risk to data subjects, notification is made without undue delay per GDPR Article 34.
5. **Cross-Border Specific Assessment:** The breach notification shall specifically address whether the cross-border nature of the processing exacerbated the breach risk (e.g., exposure to additional legal regimes).

#### 5.4.2 Breach Remediation

Post-breach, a cross-border transfer review shall be triggered:

- Re-assessment of the TIA for the affected transfer.
- Review of supplementary measures effectiveness.
- Determination of whether the transfer should be suspended, supplemented with additional measures, or terminated.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

#### 6.1.1 Encryption Standards

All cross-border data transfers shall be encrypted per Meridian's Encryption Standard (SOP-ISM-008). Minimum requirements:

| State | Standard | Key Management |
|---|---|---|
| In-Transit | TLS 1.3 (minimum TLS 1.2 with approved cipher suites) | AWS KMS (Meridian-managed keys) |
| At-Rest (EU Region) | AES-256-GCM | AWS KMS (eu-west-1 restricted key policy) |
| At-Rest (Third Country) | AES-256-GCM | Customer-managed keys in AWS KMS |
| End-to-End (Supplementary Measure) | Application-layer AES-256-GCM | Key held exclusively in AWS KMS eu-west-1, access restricted to Meridian EU personnel |

#### 6.1.2 Data Residency and Locality Controls

- **Primary Processing Locale:** Where feasible, EU personal data shall be processed in the AWS eu-west-1 (Ireland) region.
- **Cross-Region Replication Restrictions:** Snowflake data replication from eu-west-1 to us-east-1 is disabled by default. Exceptions require documented approval per Section 5.
- **Backup Locality:** Backups containing unencrypted or pseudonymized EU personal data shall not be stored in third countries unless SCCs and TIA cover such storage.
- **Access Geography Restrictions:** Access to systems containing EU personal data shall be restricted by geography where possible using Okta Adaptive MFA policies (block access from non-whitelisted countries).

#### 6.1.3 Pseudonymization and Tokenization

As a supplementary measure for high-risk transfers:

- **Pseudonymization:** Direct identifiers shall be stripped and replaced with pseudonymous tokens prior to transfer. The mapping table shall remain in the EU region.
- **Tokenization:** For HealthPay financial data, PCI-compliant tokenization (via Vault) shall be applied before cross-border transmission.
- **Clinical Data De-identification:** Clinical AI training data shall undergo de-identification per HIPAA Safe Harbor method (18 identifiers removed) plus additional EU-specific safeguards (removal of national ID numbers, social security numbers).

#### 6.1.4 Access Controls

- **Role-Based Access:** Access to EU personal data after cross-border transfer shall be restricted to roles with documented business need, enforced via IAM policies.
- **Privileged Access Management:** Administrative access to systems storing cross-border EU data requires PIM (Privileged Identity Management) just-in-time elevation and approval.
- **Access Logging:** All access to EU personal data in third-country systems shall be logged to AWS CloudTrail, with logs shipped to a dedicated, immutable log bucket in the EU region.

### 6.2 Administrative Controls

| Control | Description | Frequency |
|---|---|---|
| Cross-Border Data Flow Inventory | Centralized register of all cross-border transfers | Continuous update; quarterly review |
| SCC Register | Repository of all executed SCCs with metadata | Continuous update; annual audit |
| TIA Library | Approved Transfer Impact Assessments | Maintained for duration of transfer + 6 years |
| Vendor Transfer Compliance Review | Review of data importer's compliance with SCC Annex II | Annual for Tier 3 transfers; biennial for Tier 2 |
| Data Transfer Audit Logs | Logging of all approval decisions and changes | Continuous |
| DPIA Register | Register of DPIAs that include cross-border elements | Continuous; reviewed quarterly |

### 6.3 Organizational Controls

- **Segregation of Duties:** The CPO/DPO approves transfers but does not initiate them. The General Counsel provides independent legal review.
- **AI Governance Committee Oversight:** High-risk cross-border transfers involving AI processing are reported to the AI Governance Committee quarterly.
- **Whistleblowing:** Employees may report concerns about unauthorized or non-compliant cross-border transfers via the Ethics Hotline (Convercent platform), with non-retaliation protection.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| Metric ID | Metric | Target | Measurement Method | Owner |
|---|---|---|---|---|
| CBT-01 | % of cross-border transfers with approved mechanism in place | 100% | Monthly audit of active transfers vs. Cross-Border Register | Data Governance Manager |
| CBT-02 | % of non-adequacy transfers with valid TIA | 100% | Quarterly reconciliation | CPO/DPO |
| CBT-03 | TIA completion within target timeline | ≥ 90% | Jira report: TIA request to approval cycle time | Data Governance Manager |
| CBT-04 | SCC review currency (not past review date) | 100% | Monthly register review | Data Governance Manager |
| CBT-05 | Unauthorized cross-border data flows detected | ≤ 1 per quarter | Datadog anomaly detection + CloudTrail analysis | CISO |
| CBT-06 | Data subject access request response compliance (cross-border) | ≥ 95% | OneTrust DSAR dashboard | Privacy Team Lead |
| CBT-07 | Sub-processor change notification compliance | 100% | Vendor management review | VP IT Ops |
| CBT-08 | Cross-border breach notification within 72 hours | 100% | Incident response post-mortem | CISO + CPO/DPO |

### 7.2 Monitoring Mechanisms

#### 7.2.1 Technical Monitoring

- **Datadog Dashboards:** Custom dashboards monitor cross-region data transfer volumes (AWS CloudWatch metrics), with alerts for anomalous spikes or transfers to unexpected AWS regions.
- **AWS CloudTrail:** Monitored for S3 cross-region replication events, EC2 cross-region AMI sharing, and RDS cross-region snapshots that may contain EU data.
- **Snowflake Access History:** Queried weekly to detect queries originating from non-EU IP ranges against tables tagged as containing EU personal data.
- **Okta Log Analysis:** Monitored for successful authentications from restricted geographies to systems holding EU data.

#### 7.2.2 Process Monitoring

- **Weekly Data Governance Stand-up:** Review of new transfer requests, TIA progress, and any transfer-related incidents.
- **Monthly SCC Expiry Review:** Automated Power Automate workflow notifies Data Governance team of SCCs approaching review date (90, 60, 30 days).
- **Quarterly Transfer Register Audit:** Full reconciliation of active transfers, ROPA entries, and technical data flows.

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Content |
|---|---|---|---|
| Cross-Border Transfer Dashboard | CPO/DPO, CISO, General Counsel | Monthly | Active transfers by mechanism, country, risk tier; KPIs; open TIAs |
| TIA Status Report | CPO/DPO, General Counsel | Bi-weekly | In-progress TIAs, escalation items, overdue actions |
| Transfer Compliance Report | AI Governance Committee | Quarterly | High-risk transfers, regulatory developments, incident summary |
| Annual Transfer Program Review | Board of Directors (via Audit Committee) | Annually | Program maturity, regulatory horizon scan, major changes, audit results |
| Supervisory Authority Report | Berlin DPA | As required | BCR approval updates, Art. 49 notifications |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

Exceptions to this SOP may be requested for:

| Exception Type | Examples | Approval Level |
|---|---|---|
| **Urgent Business Need** | Critical patient transfer requiring temporary data access from restricted country | CPO/DPO + CISO (temporary, max 72 hours) |
| **Technical Limitation** | Legacy system incapable of granular data residency controls (with remediation plan) | CPO/DPO + VP Engineering + General Counsel |
| **Contract Negotiation** | Vendor refusing to execute Meridian's SCC template (alternative wording acceptable under GDPR) | General Counsel |
| **Derogation Dependency** | Reliance on Article 49 derogation where SCC/BCR not feasible | General Counsel (Section 5.1.7) |
| **M&A / Corporate Restructuring** | Data transfers resulting from acquisition or divestiture | CEO + CPO/DPO + General Counsel |

### 8.2 Exception Request Procedure

1. **Submission:** Requestor submits Exception Request via the Meridian Service Portal using form **FRM-DGP-009-3: Cross-Border Transfer Exception Request**, including:
   - Detailed justification for the exception
   - Duration of exception requested
   - Risk mitigation measures proposed
   - Remediation plan to achieve compliance
2. **Risk Assessment:** The Data Governance team prepares a risk assessment within **5 business days**.
3. **Approval/Denial:** The designated approver(s) render a decision within **10 business days** (or **48 hours** for Urgent Business Need exceptions).
4. **Registration:** Approved exceptions are registered in the Exception Log (SharePoint: Data Governance > Exceptions), with automated expiry date tracking.
5. **Remediation Tracking:** The requestor is responsible for executing the remediation plan; progress is reported monthly to the CPO/DPO.

### 8.3 Escalation Path

| Escalation Level | Trigger | Escalated To | Response Time |
|---|---|---|---|
| Level 1 | TIA identifies residual risk exceeding threshold | CPO/DPO, General Counsel | 5 business days |
| Level 2 | Level 1 unresolved; or transfer poses systemic risk | Chief Compliance Officer, CISO | 3 business days |
| Level 3 | Level 2 unresolved; regulatory risk to Meridian; or potential supervisory authority enforcement | AI Governance Committee, CEO | Emergency meeting within 48 hours |
| Regulatory | Receipt of supervisory authority inquiry or order | General Counsel → CEO → Board | Per legal advice |

### 8.4 Unauthorized Transfer Response

If an unauthorized cross-border transfer is detected:

1. **Immediate Containment:** The CISO and VP of IT Operations shall take immediate action to halt the data flow and isolate affected systems.
2. **Incident Declaration:** A privacy incident shall be declared in the PagerDuty system and the Incident Response SOP (SOP-ISM-015) invoked.
3. **Investigation:** Within **48 hours**, the Data Governance team, CISO, and General Counsel shall determine:
   - Scope of data transferred
   - Data subjects affected
   - Whether the data has been exfiltrated or merely exposed
   - Whether a breach notification obligation exists
4. **Remediation:** If the transfer was to a party with whom SCCs could be retroactively executed, the transfer mechanism shall be regularized. If to an unauthorized party, data deletion shall be verified.
5. **Disciplinary Action:** Per Meridian's Acceptable Use Policy (SOP-HR-015), unauthorized transfers may result in disciplinary action up to and including termination.

---

## 9. Training Requirements

### 9.1 Training Matrix

| Training Module | Audience | Frequency | Delivery Method | Provider |
|---|---|---|---|---|
| Cross-Border Data Transfer Awareness | All employees | Annual | LMS (Workday Learning) | Data Governance Team |
| GDPR International Transfers Deep Dive | Data Governance, Privacy, Legal Teams | Annual + on regulatory change | Instructor-led (virtual) | External counsel / CPO/DPO |
| BCR Compliance Training | All employees handling intra-group EU data | Annual | LMS (Workday Learning) | CPO/DPO |
| TIA Methodology Workshop | Data Governance team, relevant BU leads | Biannual | Hands-on workshop | CPO/DPO + General Counsel |
| Vendor Transfer Compliance | Vendor Management, Procurement | Annual | LMS | Data Governance Team |
| Role-Based Access & Cross-Border Data | IT Operations, Engineering | Annual | Instructor-led | CISO + VP IT Ops |

### 9.2 Training Content Requirements

**Cross-Border Data Transfer Awareness (All Employees):**
- What constitutes a cross-border data transfer
- Meridian's obligations under GDPR Chapter V
- Recognizing unauthorized transfer scenarios (e.g., emailing EU data to US personal email; using unauthorized cloud services)
- Reporting mechanisms for concerns
- Case studies from enforcement actions

**GDPR International Transfers Deep Dive:**
- Schrems II and its implications
- EDPB Supplementary Measures Recommendations
- SCC lifecycle management
- TIA methodology (step-by-step)
- Regulatory horizon scanning (EU-US DPF, UK adequacy review)
- Enforcement trends

### 9.3 Training Compliance Tracking

- Completion rates are tracked in Workday Learning.
- Target completion rate: **100% for assigned audiences**.
- Non-completion within **30 days** of assignment triggers notification to the employee's manager and HR.
- Non-completion within **60 days** results in suspension of access to systems handling EU data until training is completed.
- Training completion metrics are reported quarterly to the Chief Compliance Officer.

### 9.4 Training Review

Training content shall be reviewed and updated:
- Annually as part of the SOP review cycle.
- Upon any material change to GDPR cross-border transfer requirements (e.g., new SCCs, CJEU rulings).
- Upon any changes to Meridian's transfer mechanisms or supplementary measures framework.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| SOP-DGP-001 | Data Governance Framework | Overarching data governance policy |
| SOP-DGP-004 | Data Subject Rights Management | DSAR processing, including cross-border data |
| SOP-DGP-010 | Binding Corporate Rules (BCR) Policy | BCR governance for intra-group transfers |
| SOP-DGP-003 | Records of Processing Activities (ROPA) Management | ROPA entries for cross-border transfers |
| SOP-DGP-005 | Data Protection Impact Assessment (DPIA) Procedure | DPIA methodology, including transfer risk assessment |
| SOP-ISM-008 | Encryption and Key Management Standard | Encryption standards for data in-transit and at-rest |
| SOP-ISM-015 | Information Security Incident Response | Breach response for cross-border incidents |
| SOP-ISM-012 | Vendor Security and Privacy Assessment | Third-party risk management including transfer compliance |
| SOP-AI-003 | AI Model Data Governance | Data handling for AI/ML models, including cross-border training data |

### 10.2 External References

| Reference | Description |
|---|---|
| EU General Data Protection Regulation (GDPR) (Regulation (EU) 2016/679) | Primary regulation, particularly Chapter V |
| Commission Implementing Decision (EU) 2021/914 | Current Standard Contractual Clauses |
| EDPB Recommendations 01/2020 | Supplementary measures guidance |
| EDPB Guidelines 2/2018 (Derogations, Article 49) | Derogation interpretation |
| EDPB Guidelines 4/2018 (Binding Corporate Rules) | BCR requirements |
| EU-US Data Privacy Framework Principles | Adequacy mechanism for US transfers |
| CJEU C-311/18 (Schrems II) | Foundational case law on transfers |
| NIST AI RMF 1.0 | Cross-reference for AI-related transfer risks |
| Meridian AI Governance Charter | Board-level governance document |
| Meridian Data Taxonomy v3.2 | Data classification framework |

### 10.3 Forms and Templates

| Form ID | Document | Location |
|---|---|---|
| FRM-DGP-009-1 | Cross-Border Transfer Request Form | Jira Service Management (Data Governance queue) |
| FRM-DGP-009-2 | Transfer Impact Assessment Report Template | SharePoint: Data Governance > Templates |
| FRM-DGP-009-3 | Cross-Border Transfer Exception Request | Jira Service Management (Data Governance queue) |
| FRM-DGP-009-4 | SCC Annex I-III Template | iManage: Legal > Data Protection > SCCs |
| FRM-DGP-009-5 | Cross-Border Data Flow Inventory Template | Collibra > Data Governance > Cross-Border |

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2021-03-15 | Dr. Klaus Weber | Initial SOP creation. Established foundational cross-border transfer procedures post-Schrems II. Introduced SCC-centric approach. |
| 2.0 | 2022-08-22 | Dr. Klaus Weber | Major revision. Incorporated new EU SCCs (2021/914). Added TIA requirement and supplementary measures framework. Expanded scope to cover UK post-Brexit adequacy. |
| 2.1 | 2023-01-10 | Maria Gonzalez | Minor revision. Added EU-US Data Privacy Framework provisions. Clarified derogation pre-approval requirements. |
| 3.0 | 2024-02-28 | Dr. Klaus Weber | Major revision. Added BCR framework for intra-group transfers. Integrated AI Act considerations for clinical data transfers. Expanded sub-processor management procedures. Restructured Section 5 for clarity. |
| 3.1 | 2024-06-14 | Thomas Anderson | Added comprehensive KPI metrics and monitoring mechanisms (Section 7). Revised reporting cadence. |
| 3.2 | 2024-08-05 | Dr. Klaus Weber | Updated adequacy decisions list. Revised TIA approval timelines based on operational experience. Added pseudonymization and tokenization controls. |
| 3.3 | 2024-11-18 | Samantha Torres | Technical controls update. Expanded AWS KMS key management specifications. Added Datadog monitoring configuration details. |
| 3.4 | 2024-12-11 | Dr. Klaus Weber | Full SOP review cycle. Updated exception handling to include M&A scenarios. Added Section 8.4 Unauthorized Transfer Response. Refined training content requirements. Updated related policies cross-references. |

---

**END OF DOCUMENT**

---
*SOP-DGP-009, Version 3.4 | Classification: Internal | © 2024 Meridian Health Technologies, Inc. All rights reserved.*
*This document is controlled. Printed copies are uncontrolled. Verify current version in the Meridian Policy Portal.*