---
sop_id: "SOP-LEGC-018"
title: "Cross-Jurisdictional Compliance Coordination"
business_unit: "Legal & Compliance"
version: "2.7"
effective_date: "2024-06-20"
last_reviewed: "2025-07-14"
next_review: "2026-01-22"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "EU AI Act"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Cross-Jurisdictional Compliance Coordination

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, governance, and operational processes for managing concurrent and potentially conflicting regulatory obligations across the jurisdictions in which Meridian Health Technologies, Inc. ("Meridian" or the "Company") operates. The Company's product portfolio—spanning clinical artificial intelligence, healthcare financial services, and population health analytics—is simultaneously subject to the European Union's General Data Protection Regulation (GDPR), the EU Artificial Intelligence Act (EU AI Act), and the U.S. Health Insurance Portability and Accountability Act (HIPAA), among other frameworks.

The purpose of this SOP is to ensure that Meridian:

1. Identifies and maps all applicable regulatory obligations across jurisdictions before product deployment or material change;
2. Applies a structured methodology for resolving conflicts between overlapping or inconsistent legal requirements;
3. Maintains a coordinated network of internal stakeholders and external local counsel to ensure consistent interpretation and implementation;
4. Achieves harmonization of compliance controls wherever operationally feasible and legally permissible, reducing redundancy and compliance debt;
5. Maintains auditable records of all jurisdictional analyses, conflict resolutions, and harmonization decisions for regulatory inspection and audit defense.

### 1.2 Scope

#### 1.2.1 Organizational Scope

This SOP applies to all business units, departments, and personnel involved in the design, development, deployment, operation, and support of Meridian products and services that process personal data, deploy AI systems, or handle protected health information. Specifically, this SOP binds:

- **Legal & Compliance** (primary owner)
- **Clinical AI Products** (Dr. Aisha Okafor's organization)
- **HealthPay Financial Services** (Robert Liu's organization)
- **MedInsight Analytics**
- **Engineering** (David Park's organization, including platform and ML teams)
- **IT Operations** (Samantha Torres's organization)
- **Information Security** (Rachel Kim's organization)
- **Customer Operations** (Michael Chang's organization)
- **Human Resources** (for employee data processing)
- **Office of the Data Protection Officer** (Dr. Klaus Weber, Berlin)

#### 1.2.2 Product and Service Scope

This SOP covers all current and future products and services within Meridian's four business lines:

- **Clinical AI Platform**: All clinical decision support tools, diagnostic imaging analysis modules, patient risk scoring algorithms, and adverse event prediction systems. These systems are classified as "high-risk AI systems" under Annex III of the EU AI Act.
- **HealthPay Financial Services**: Payment processing, patient financing, medical lending, and claims automation platforms subject to SR 11-7 model risk management guidance.
- **MedInsight Analytics**: Population health analytics, care gap identification, and outcomes prediction platforms processing PHI from approximately 12 million patients.
- **Meridian SaaS Platform**: The multi-tenant cloud infrastructure hosted on AWS (us-east-1, eu-west-1) underlying all products, maintaining SOC 2 Type II certification.

#### 1.2.3 Jurisdictional Scope

The procedural requirements of this SOP activate whenever Meridian's data processing activities, AI deployments, or business operations implicate any of the following jurisdictions or legal frameworks:

| Jurisdiction | Primary Frameworks | Activation Trigger |
|---|---|---|
| European Union / European Economic Area | GDPR, EU AI Act, EU MDR | Processing personal data of EU data subjects; placing AI systems on EU market or putting into service; CE-marked medical devices |
| United States (Federal) | HIPAA, FTC Act | Processing PHI as covered entity or business associate; unfair or deceptive practices |
| United States (State) | California CMIA, Washington My Health My Data Act, state data privacy laws | Processing health data of state residents beyond HIPAA scope |
| United Kingdom | UK GDPR, UK AI regulatory framework | Processing personal data of UK data subjects; UK market deployment |
| Canada (Federal/Provincial) | PIPEDA, provincial health privacy laws | Processing personal health information in Canadian provinces; Toronto office operations |
| Singapore | PDPA | Singapore office operations; processing Singapore data subject data |

#### 1.2.4 Out of Scope

The following matters are explicitly excluded from this SOP and are governed by separate policies:

- Information security incident response (refer to SOP-ISIM-001: Security Incident Management)
- Product-specific AI model validation and performance monitoring (refer to SOP-AI-042: AI Model Lifecycle Management)
- Employee personal data processing for employment purposes (refer to SOP-HR-019: Employee Data Privacy)
- Financial reporting and SOX compliance (refer to SOP-FIN-031: Financial Controls Framework)

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Conflicts Analysis** | The structured process of identifying, documenting, evaluating, and resolving situations where two or more applicable regulations impose inconsistent, mutually exclusive, or operationally incompatible obligations. |
| **Conformity Assessment** | The process defined in EU AI Act Article 43 demonstrating that a high-risk AI system complies with the requirements set forth in Chapter 2 of the Act. For Meridian's clinical AI products, this requires third-party assessment by an EU-notified body. |
| **Data Protection Impact Assessment (DPIA)** | A process described in GDPR Article 35 required where processing is likely to result in high risk to the rights and freedoms of natural persons. |
| **Harmonized Control** | A single technical, administrative, or operational measure designed and implemented to satisfy the requirements of multiple regulatory frameworks simultaneously, where such convergence is legally permissible. |
| **High-Risk AI System** | As defined in EU AI Act Article 6 and Annex III, an AI system that poses significant risk of harm to health, safety, or fundamental rights. All Clinical AI Platform products fall within this classification. |
| **Human Oversight** | Measures built into high-risk AI systems as required by EU AI Act Article 14, enabling natural persons to fully understand, monitor, and intervene in the system's operation. |
| **Jurisdiction Mapping** | The systematic identification and documentation of all applicable legal requirements based on the geographic location of data subjects, deployment of systems, and entity registration. |
| **Lawful Basis** | The legal grounds for processing personal data enumerated in GDPR Article 6 (and Article 9 for special categories of data). |
| **Local Counsel** | Qualified legal practitioners licensed in a specific jurisdiction, engaged by Meridian to provide binding legal interpretation and compliance guidance for that jurisdiction's laws. |
| **Maximum Protection Principle** | A conflict resolution methodology applied when harmonization is impossible, requiring compliance with the most protective applicable standard among conflicting requirements, unless doing so would violate another applicable law. |
| **Protected Health Information (PHI)** | Individually identifiable health information maintained or transmitted by a covered entity or business associate, as defined under HIPAA. |
| **Regulatory Change Trigger** | Any event—including new legislation, regulatory guidance, enforcement action, or court decision—that materially alters Meridian's compliance obligations in an active jurisdiction. |
| **Special Categories of Personal Data** | Data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership; genetic data; biometric data; data concerning health; or data concerning a natural person's sex life or sexual orientation, as enumerated in GDPR Article 9. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| AI-GC | AI Governance Committee (Board-level, established 2024) |
| BAA | Business Associate Agreement |
| CAIO | Chief AI Officer (Dr. Marcus Rivera) |
| CCO | Chief Compliance Officer (Thomas Anderson) |
| CE | Conformité Européenne (European Conformity) |
| CMO | Chief Medical Officer (Dr. Priya Patel) |
| CISO | Chief Information Security Officer (under VP, Information Security) |
| CJCC | Cross-Jurisdictional Compliance Committee |
| CMIA | California Medical Information Act |
| DPIA | Data Protection Impact Assessment |
| DPO | Data Protection Officer (Dr. Klaus Weber) |
| EDPB | European Data Protection Board |
| EEA | European Economic Area |
| EU MDR | European Union Medical Device Regulation (2017/745) |
| FRIA | Fundamental Rights Impact Assessment |
| GC | General Counsel (Maria Gonzalez) |
| GRC | Governance, Risk, and Compliance (platform) |
| MPP | Maximum Protection Principle |
| NB | Notified Body (EU) |
| PIPEDA | Personal Information Protection and Electronic Documents Act (Canada) |
| PDPA | Personal Data Protection Act (Singapore) |
| QMS | Quality Management System |
| ROPA | Record of Processing Activities |
| SIG | Special Interest Group (regulatory-specific working groups) |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

The following matrix assigns Responsible (R), Accountable (A), Consulted (C), and Informed (I) designations for key activities under this SOP.

| Activity / Decision | CCO (Thomas Anderson) | GC (Maria Gonzalez) | DPO (Dr. Klaus Weber) | CAIO (Dr. Marcus Rivera) | Business Unit Leads | Local Counsel (Jurisdiction-Specific) | AI-GC (Board Level) | Engineering Lead (David Park) |
|---|---|---|---|---|---|---|---|---|
| **Jurisdiction Mapping** — Initial | A | C | R | C | C | C | I | I |
| **Jurisdiction Mapping** — Update (Triggered) | A | C | R | C | I | R | I | I |
| **Conflicts Analysis** — Identification | A | R | R | C | I | C | I | I |
| **Conflicts Analysis** — Resolution Decision | C | A | R | R | I | R | I | C |
| **Harmonization Control Design** | R | C | C | C | C | C | I | R |
| **Conformity Assessment (EU AI Act Art. 43)** | C | C | I | A | R | R | I | I |
| **DPIA Execution (GDPR Art. 35)** | C | I | A | C | R | C | I | I |
| **Human Oversight Implementation (EU AI Act Art. 14)** | C | I | I | A | R | C | I | R |
| **Local Counsel Engagement** | R | A | C | I | I | C | I | I |
| **Regulatory Change Monitoring** | A | C | R | C | I | R | I | I |
| **Compliance KPI Reporting** | A | I | R | R | I | I | C | I |
| **Exception Approval** | C | A | R | R | I | I | I | I |

### 3.2 Named Roles and Specific Responsibilities

#### 3.2.1 Chief Compliance Officer (Thomas Anderson)

- Serves as the executive owner of this SOP.
- Chairs the Cross-Jurisdictional Compliance Committee (CJCC) on a quarterly basis or when emergency jurisdiction conflicts arise.
- Maintains the definitive Jurisdictional Obligation Register in the Company's GRC platform (Vanta, as of this version).
- Approves all conflict resolution determinations that do not require General Counsel escalation (see Section 5.4.3).
- Reports jurisdictional compliance status and material conflicts to the AI Governance Committee and the Audit Committee bi-annually.
- Maintains a 24-hour response SLA for any inquiry flagged as "URGENT: Jurisdictional Conflict" by any business unit lead.

#### 3.2.2 General Counsel (Maria Gonzalez)

- Serves as the final internal escalation point for any jurisdictional conflict that cannot be resolved through the MPP or harmonization framework.
- Approves the engagement of all external local counsel and sets the scope of their engagement letters.
- Personally reviews and approves all legal memoranda where counsel opines that Meridian cannot simultaneously comply with two applicable laws (a "true conflict" determination).
- Maintains attorney-client privilege over all Conflicts Analysis Legal Memoranda produced under Section 5.4.
- Approves all jurisdictional compliance exceptions with a duration exceeding 90 days.

#### 3.2.3 Data Protection Officer (Dr. Klaus Weber)

- Maintains primary responsibility for all GDPR Article 35 DPIAs, including those triggered by high-risk AI systems under the EU AI Act's intersection with GDPR.
- Leads the Jurisdiction Mapping process for all EU member states, maintaining current knowledge of EDPB guidelines, national supervisory authority decisions, and local implementation laws.
- Serves as the primary point of contact for EU supervisory authorities (lead authority: Berliner Beauftragte für Datenschutz und Informationsfreiheit).
- Convenes the GDPR Special Interest Group (GDPR-SIG) monthly to review processing activities, data subject requests, breach notifications, and cross-border transfer mechanisms.
- Maintains direct responsibility for the Article 30 Record of Processing Activities (ROPA), updated within 10 business days of any new processing activity or material change.

#### 3.2.4 Chief AI Officer (Dr. Marcus Rivera)

- Bears organizational accountability for all EU AI Act conformity assessments, including engagement with Meridian's designated EU Notified Body (TÜV SÜD, NB 0123).
- Maintains the Fundamental Rights Impact Assessment (FRIA) framework required under EU AI Act Article 27.
- Ensures that all high-risk AI systems deployed or placed on the EU market maintain current CE marking and EU MDR certifications.
- Participates as a mandatory member in all Conflicts Analysis proceedings where EU AI Act obligations intersect with other regulatory requirements.
- Reports semi-annually to the AI-GC on the status of all EU AI Act compliance activities, including any unresolved jurisdictional conflicts.

#### 3.2.5 Business Unit Leads (Clinical AI: Dr. Aisha Okafor; HealthPay: Robert Liu; MedInsight: [as designated])

- Serve as the operational owners of products and services, responsible for implementing all compliance controls designed through this SOP.
- Identify and escalate potential jurisdictional conflicts during product planning, architecture review, and deployment phases (see Section 5.2 Trigger Events).
- Maintain current jurisdiction-specific deployment registries for their products (format specified in Appendix A: Deployment Jurisdiction Declaration Template).
- Attend CJCC meetings when agenda items pertain to their business unit.
- Bear responsibility for implementing approved harmonized controls within their operational environments within the timelines specified in Section 6.

#### 3.2.6 Local Counsel Network

Meridian maintains a network of qualified external counsel in each active jurisdiction. The current roster is maintained by the GC's office in the GRC platform. Local counsel responsibilities include:

- Providing formal written opinions on jurisdiction-specific regulatory interpretations within 10 business days of engagement.
- Reviewing and commenting on harmonized control designs for compatibility with local law.
- Alerting the CCO and GC's office to material regulatory changes or enforcement trends within 30 days of their occurrence.
- Participating in annual "Jurisdiction Deep Dive" sessions with the Legal & Compliance team.

### 3.3 Cross-Jurisdictional Compliance Committee (CJCC)

The CJCC serves as the standing operational body for executing this SOP. Its composition, cadence, and authority are defined in Section 5.3.

---

## 4. Policy Statements

### 4.1 Foundational Policy Commitments

Meridian adopts the following policy statements as the non-negotiable foundation of its cross-jurisdictional compliance program. All procedures, controls, and exceptions described in this SOP derive from and must be consistent with these commitments.

**PS-01: Comprehensive Jurisdictional Mapping**
Meridian shall maintain a continuously updated Jurisdictional Obligation Register that maps, for every product and data processing activity, all applicable regulatory requirements across every jurisdiction in which Meridian operates. No product or material feature shall be deployed to a new jurisdiction without completion and documented review of a Jurisdiction Mapping Worksheet.

**PS-02: Lawful Processing Primacy**
Meridian shall identify and document a valid lawful basis under GDPR Article 6 (and Article 9, where special categories of data are processed) for every processing activity involving personal data of EU/EEA data subjects. Where U.S. healthcare operations constitute the primary purpose of processing, Meridian shall nevertheless maintain GDPR-compliant lawful bases. No processing activity shall rely solely on U.S. legal requirements as justification for processing EU personal data.

**PS-03: Conflict Identification and Structured Resolution**
Meridian shall apply the structured methodology defined in Section 5.4 of this SOP to all identified regulatory conflicts. No conflict shall be resolved unilaterally by a single business unit. All resolution determinations shall be documented in the Conflicts Resolution Register and, where a "true conflict" (impossibility of simultaneous compliance) is identified, memorialized in a privileged Conflicts Analysis Legal Memorandum approved by the GC.

**PS-04: Harmonization by Default**
Where two or more jurisdictions impose overlapping but not mutually exclusive requirements, Meridian shall design and implement harmonized controls that satisfy all applicable standards simultaneously, unless such harmonization would conflict with a superseding local legal requirement. Harmonization shall be the default operational posture; separate jurisdictional controls ("Jurisdiction-Specific Controls") shall be implemented only where harmonization is demonstrably infeasible.

**PS-05: Maximum Protection Principle**
Where harmonization is impossible due to genuine incompatibility between applicable regulatory requirements, Meridian shall apply the Maximum Protection Principle (MPP). Under the MPP, Meridian shall adopt the control that provides the highest level of protection for the rights and freedoms of the affected individuals, unless: (a) such adoption would itself violate another applicable law, or (b) the GC determines, based on written local counsel opinion, that the less protective standard is expressly mandated and the more protective standard would constitute non-compliance.

**PS-06: Human Oversight of High-Risk AI**
All Clinical AI Platform products deployed or placed on the market in the EU shall incorporate human oversight measures as required by EU AI Act Article 14. Such measures shall be designed to enable the natural persons to whom oversight is assigned to: (a) fully understand the capacities and limitations of the system; (b) remain aware of automation bias tendencies; (c) correctly interpret system outputs; (d) decide not to use the system or to disregard, override, or reverse its output; and (e) intervene or halt the system's operation where necessary. These measures shall not be subordinated to operational efficiency considerations.

**PS-07: Transparency and Documentation**
All analyses, determinations, and actions taken pursuant to this SOP shall be documented in the Company's GRC platform (Vanta), maintaining complete audit trails including timestamps, decision-maker identities, and supporting artifacts. Documentation shall be maintained for a minimum period of 10 years from the date of creation, reflecting the maximum statute of limitations among applicable jurisdictions.

**PS-08: Regulatory Change Responsiveness**
Meridian shall respond to material regulatory changes (new legislation, revised guidance, enforcement precedent, or court decisions) with an initial impact assessment completed within 15 business days and a full Jurisdiction Mapping update within 45 business days. Failure to meet these timelines shall constitute a reportable compliance gap to the CJCC.

**PS-09: Prohibition of Regulatory Arbitrage**
Meridian prohibits the deliberate structuring of data flows, corporate entities, or processing operations for the primary purpose of circumventing or minimizing applicable regulatory obligations. All jurisdictional determinations shall be made based on the substantive reality of data processing activities and market presence.

**PS-10: Data Subject and Individual Rights**
Meridian shall maintain mechanisms enabling individuals to exercise their rights under applicable data protection laws. Under GDPR, these mechanisms shall facilitate the exercise of rights under Articles 15–22 (access, rectification, erasure, restriction, portability, objection, and automated decision-making rights) within the timelines specified by Article 12(3)—without undue delay and in any event within one month of receipt. Where requests are complex or numerous, the response period may be extended by two further months, with the individual informed of the extension within the initial one-month period. All such requests shall be logged in the GRC platform with an assigned SLA timer. Where individual rights requests conflict with other legal obligations (e.g., mandatory data retention under EU MDR), the CJCC shall adjudicate as a jurisdictional conflict under Section 5.4.

---

## 5. Detailed Procedures

### 5.1 Jurisdiction Mapping Procedure

#### 5.1.1 Overview

Jurisdiction Mapping is the foundational procedure of this SOP. It systematically identifies, for a defined scope (product, feature, processing activity, or data flow), every applicable regulatory obligation across all relevant jurisdictions. Jurisdiction Mapping must be completed and reviewed prior to any of the following events (collectively, "Jurisdiction Mapping Triggers"):

1. Initial deployment of a product or service in a new geographic market.
2. Introduction of a new product feature that materially changes data processing characteristics.
3. Entry into a new data processing relationship with a third party.
4. Establishment of a legal entity, office, or server infrastructure in a new jurisdiction.
5. Detection of a material regulatory change by the monitoring process described in Section 5.1.5.

#### 5.1.2 Initiating a Jurisdiction Mapping

The Business Unit Lead (or designated delegate) shall initiate Jurisdiction Mapping by completing the **Deployment Jurisdiction Declaration Template** (Appendix A) and submitting it via the GRC platform. The Declaration shall specify:

- Product name and version.
- Description of the processing activity, deployment, or change.
- Known target jurisdictions (including EU member states individually, not collectively).
- Data categories involved (reference Meridian Data Classification Policy SOP-ISEC-022).
- Data subject categories (e.g., patients, healthcare providers, payors).
- Whether the processing involves special categories of data (GDPR Art. 9) or PHI.
- Whether the deployment involves an AI system and, if so, its EU AI Act risk classification (per CAIO's office).

Upon submission, the GRC platform automatically creates a Jurisdiction Mapping Worksheet and assigns it to the DPO's office for EU jurisdictions and to the CCO's office for all other jurisdictions. The platform also triggers a notification to the relevant Local Counsel in each identified jurisdiction.

#### 5.1.3 Conducting the Obligation Analysis

For each jurisdiction identified in the Declaration, the responsible party (DPO for EU/EEA, CCO for all others) shall, within **10 business days** of Declaration submission:

1. **Catalogue Applicable Laws**: Identify all specific statutes, regulations, subordinate legislation, regulatory guidance, and binding codes of conduct applicable to the described processing activity. This catalogue shall reference specific articles, sections, and provisions at the granularity necessary to enable subsequent Conflicts Analysis.
2. **Identify Regulatory Overlaps**: Flag areas where requirements from two or more jurisdictions address the same subject matter (e.g., data subject rights, breach notification, security measures, transparency obligations, human oversight).
3. **Complete the Obligation Matrix**: Populate the standard Jurisdiction Mapping Worksheet fields for each identified obligation:

| Field | Description |
|---|---|
| Jurisdiction | Specific jurisdiction (e.g., "EU – GDPR Art. 16" not "EU") |
| Regulation & Citation | Precise legal citation |
| Obligation Category | (Notice, Consent, Rights, Security, Breach, AI Governance, Data Minimization, Retention, Transfer, Documentation) |
| Obligation Description | Concise statement of the legal requirement |
| Binding Nature | Mandatory / Conditionally Mandatory / Recommended |
| Meridian Product/Process Affected | Specific system, module, or data flow |
| Interacts With (Other Jurisdictions) | Cross-reference to other Obligation Matrix entries |
| Implementation Status | Implemented / In Progress / Planned / Not Applicable / Gap Identified |

4. **Identify Preliminary Conflicts**: For entries flagged in the "Interacts With" field, note any preliminary indications of inconsistency, incompatibility, or operational tension.

#### 5.1.4 Review and Approval of Jurisdiction Mapping

Completed Jurisdiction Mapping Worksheets shall be reviewed according to the following tiered approval workflow:

- **Tier 1 (Standard)**: Product deployment in jurisdictions where Meridian already maintains an active compliance program and where no preliminary conflicts are identified. Review: CCO (5 business days); Approval: CCO.
- **Tier 2 (Enhanced)**: Deployment in a new jurisdiction, or where preliminary conflicts between obligations are identified. Review: DPO (EU obligations), Local Counsel (per jurisdiction), CISO (security obligations); Approval: GC.
- **Tier 3 (Fundamental Rights Impact)**: Deployment of a high-risk AI system in the EU. Review: CAIO (conformity assessment integration), DPO, Local Counsel, CISO; Approval: GC and CAIO jointly, with notification to AI-GC.

No product deployment shall proceed to production launch without a fully approved Jurisdiction Mapping Worksheet at the required tier.

#### 5.1.5 Ongoing Jurisdictional Monitoring

The DPO's office, with support from Local Counsel in each jurisdiction, shall maintain a **Regulatory Change Calendar** tracking:

- Scheduled legislative amendments, regulatory guidance updates, and court decisions.
- Supervisory authority opinions and enforcement actions in jurisdictions relevant to Meridian's processing.
- EDPB guidelines and opinions.

The DPO shall distribute a **Monthly Regulatory Watch Brief** to all CJCC members by the 15th of each month, summarizing relevant developments and flagging items requiring Jurisdiction Mapping updates. Any CJCC member may also raise an ad-hoc regulatory change requiring an update.

### 5.2 Conflicts Analysis and Resolution

#### 5.2.1 Triggering Conflicts Analysis

Conflicts Analysis shall be initiated immediately when:

1. A Tier 2 or Tier 3 Jurisdiction Mapping identifies a preliminary conflict.
2. Any employee of Meridian identifies a situation where, in their reasonable assessment, complying with one applicable regulation would cause or risk non-compliance with another applicable regulation ("Operational Conflict Identification"). Employees may raise such identifications confidentially via the GRC platform, via direct communication to the CCO, or via the whistleblower hotline (EthicsPoint).
3. Local Counsel issues a formal opinion indicating inconsistency between local law and another jurisdiction's requirements applicable to Meridian's processing.
4. A supervisory authority, regulator, or notified body raises a concern regarding compliance compatibility.
5. The CJCC, during its quarterly review, identifies a latent conflict.

#### 5.2.2 Conflicts Classification

Upon initiation, the CCO (or designee) shall classify the conflict according to its severity and operational impact:

| Severity Level | Description | Example |
|---|---|---|
| **Level 1 – Interpretive Tension** | Two regulations address the same subject matter with different language or emphasis but can be simultaneously satisfied through a single control with appropriate configuration. | GDPR Art. 17 (right to erasure) and FDA medical device reporting requirements (data must be retained for reporting). Resolvable by designing erasure to apply only to non-reportable data elements. |
| **Level 2 – Operational Incompatibility** | Two regulations impose requirements that, while not legally contradictory, create significant operational friction requiring separate workflows or controls. | GDPR Art. 33 (72-hour breach notification) versus state-level breach notification timelines (e.g., 30–60 days). Resolvable by implementing the most stringent timeline but maintaining jurisdiction-specific notification templates. |
| **Level 3 – Legal Inconsistency** | Two regulations impose requirements where compliance with both is arguably or demonstrably impossible as a matter of law. | A court order in Jurisdiction A requiring disclosure of all data, while GDPR Art. 48 prohibits transfer based on foreign court orders without an international agreement. |

#### 5.2.3 Conflicts Analysis Procedure

**For Level 1 (Interpretive Tension) Conflicts:**

1. CCO Office drafts a **Harmonized Interpretation Memoranda** proposing a unified control description.
2. DPO reviews for GDPR consistency.
3. Relevant Local Counsel reviews (7 business day SLA) for local law consistency.
4. CCO approves and logs resolution in Conflicts Resolution Register.

**For Level 2 (Operational Incompatibility) Conflicts:**

1. GC's office convenes a **Conflicts Resolution Panel** comprising: GC, CCO, DPO, relevant Business Unit Lead, and relevant Local Counsel (may be multiple).
2. Panel applies the **Harmonization Feasibility Assessment**:
   - **Step A**: Identify the specific operational points of friction.
   - **Step B**: Determine whether a single harmonized control can satisfy all requirements with modifications (e.g., combining most-stringent timelines with jurisdiction-specific outputs).
   - **Step C**: If harmonization is feasible, Engineering Lead (or delegate) provides implementation estimate. Panel approves harmonized control design.
   - **Step D**: If harmonization is not feasible, proceed to Level 3 analysis.
3. Panel's determination, with rationale, is documented in a **Conflicts Resolution Memorandum** archived in the GRC platform.

**For Level 3 (Legal Inconsistency) Conflicts:**

1. GC immediately assumes personal oversight of the analysis.
2. GC commissions formal written opinions from Local Counsel in each relevant jurisdiction, posing specific questions regarding the alleged inconsistency. Opinions must be received within **15 business days** (or such other timeline as GC determines necessary based on urgency).
3. GC convenes a **True Conflict Determination Panel** comprising GC, CCO, DPO, CAIO, relevant Business Unit Lead, and all relevant Local Counsel.
4. The Panel applies the **Maximum Protection Principle (MPP)** as defined in PS-05:
   - Identify the standard that provides the highest level of protection for individual rights and freedoms.
   - Determine whether adopting that standard would violate another applicable law. If yes, and the violation cannot be cured, the Panel must escalate to the GC for determination of whether a compliance impossibility exists that requires Meridian to curtail or modify the relevant processing activity or market presence. In such a case, GC shall brief the CEO and the Board of Directors.
5. The Panel's determination, including any MPP application and any determination of compliance impossibility, is memorialized in a privileged **Conflicts Analysis Legal Memorandum** (attorney-client privileged, prepared under GC's direction). A non-privileged summary, sufficient for audit purposes, is logged in the Conflicts Resolution Register.

#### 5.2.4 Conflicts Resolution Register

The CCO shall maintain, within the GRC platform, a **Conflicts Resolution Register** containing the following fields for every conflict processed under this SOP:

| Register Field | Description |
|---|---|
| Conflict ID | Auto-generated unique identifier (format: CON-YYYY-NNN) |
| Date Identified | Date conflict was raised or detected |
| Identification Source | (Jurisdiction Mapping, Employee Report, Local Counsel Opinion, Regulatory Inquiry, CJCC Review) |
| Jurisdictions Involved | List of applicable jurisdictions and specific regulatory provisions |
| Conflict Classification | Level 1, 2, or 3 |
| Resolution Methodology | (Harmonized Interpretation, Harmonized Control, Jurisdiction-Specific Control, MPP Application, Processing Modification/Cessation) |
| Resolution Description | Detailed, auditable description of how the conflict was resolved, including the final control design or operational decision |
| Resolution Date | Date resolution was approved |
| Approver | GC (Level 3, or Level 2 unresolved), CCO (Level 1, Level 2 resolved) |
| Implementation Owner | Business Unit Lead or Engineering Lead responsible for implementing the resolution |
| Implementation Deadline | Date by which resolution must be operationalized |
| Status | (Open, Resolved-Implemented, Resolved-Pending Implementation, Escalated) |

### 5.3 Cross-Jurisdictional Compliance Committee (CJCC) Operating Procedure

The CJCC operationalizes the governance of this SOP. Its composition, meeting cadence, and agenda are specified below.

#### 5.3.1 Membership

- **Chair**: Chief Compliance Officer (Thomas Anderson) — standing member
- **Vice Chair**: Data Protection Officer (Dr. Klaus Weber) — standing member
- **Standing Members**: General Counsel (Maria Gonzalez), Chief AI Officer (Dr. Marcus Rivera), VP Information Security (or CISO delegate)
- **Rotating Members (per agenda)**: Relevant Business Unit Leads (Clinical AI, HealthPay, MedInsight), Engineering Lead (David Park or delegate), relevant Local Counsel
- **Secretariat**: GRC Analyst (assigned by CCO)

#### 5.3.2 Meeting Cadence

- **Quarterly Review Meetings**: Mandatory for all standing members. Held within the first two weeks of each calendar quarter (January, April, July, October). Comprehensive agenda covering all active conflicts, jurisdiction mapping updates, regulatory changes, KPI reviews, and harmonization initiative status.
- **Emergency CJCC Sessions**: Convened by the Chair within **72 hours** of any Level 3 conflict identification or upon notification of a material regulatory enforcement action or inquiry. Participation mandatory for all members with relevant subject matter expertise.
- **Annual Deep Dive**: Held each November. Extended session (full day) reviewing the comprehensive state of jurisdictional compliance, emerging regulatory trends, and forward-looking harmonization strategy. Results presented to AI-GC in December.

#### 5.3.3 Standard Quarterly Agenda

1. **Call to Order and Review of Previous Meeting Action Items** (Chair)
2. **Regulatory Watch Briefing**: Significant developments since last meeting (DPO)
3. **Jurisdiction Mapping Status**: New mappings completed, in progress, planned (CCO)
4. **Conflicts Resolution Review**: All open and newly resolved conflicts, aging report (CCO)
5. **Harmonization Initiative Status**: Active harmonization projects (CCO/BU Leads)
6. **Individual Rights Request Trends**: GDPR Articles 15–22 request volumes, response times, trends (DPO)
7. **AI Act Compliance Update**: Conformity assessments, notified body interactions, FRIA updates (CAIO)
8. **Exception Review**: All active exceptions, those approaching expiration, new exception requests (GC/CCO)
9. **Training Compliance Review** (CCO)
10. **Metrics Review**: KPI dashboard review (Section 7)
11. **Forward Outlook**: Planned product deployments, regulatory horizon scanning
12. **Action Item Assignment**

### 5.4 Local Counsel Coordination Procedure

#### 5.4.1 Engagement Protocol

Local Counsel shall be engaged under the following circumstances, using a standardized **Legal Services Request Form** (Appendix B) submitted through the Legal & Compliance matter management system (Legal Tracker):

- All Tier 2 and Tier 3 Jurisdiction Mappings.
- Any Level 2 or Level 3 Conflicts Analysis.
- Annual comprehensive review of jurisdiction-specific obligations.
- Any regulatory change flagged as "High Impact" in the Monthly Regulatory Watch Brief.
- Upon initiation of any DPIA involving cross-border data transfers.
- When supervisory authority guidance requires jurisdiction-specific interpretation.

The Legal Services Request Form shall specify:
- Jurisdiction(s) requiring local law interpretation.
- Specific legal questions posed.
- Relevant Meridian product or processing activity context.
- Required turnaround time (standard: 10 business days; expedited: 5 business days; emergency: 72 hours).
- Whether a formal written opinion is required.

#### 5.4.2 Local Counsel Opinion Management

All Local Counsel formal written opinions shall be:

1. Logged in the Legal & Compliance matter management system with a unique matter identifier.
2. Summarized in a standard **Local Counsel Opinion Summary Template** (Appendix C) capturing the specific legal conclusions, any qualifications or caveats, and the operational implications for Meridian.
3. Where the opinion relates to a specific conflict or jurisdiction mapping, linked to the relevant Conflicts Resolution Register entry or Jurisdiction Mapping Worksheet in the GRC platform.
4. Stored in the Company's document management system (iManage) with appropriate privilege designations.

#### 5.4.3 Annual Local Counsel Review

The GC's office, in coordination with the CCO, shall conduct an annual review of all Local Counsel relationships:

- Assess quality, timeliness, and utility of opinions provided.
- Evaluate cost-effectiveness.
- Verify current good standing with relevant bar associations.
- Confirm continued subject matter expertise in evolving regulatory areas (AI, health data).
- Update or rotate counsel as appropriate based on performance and evolving needs.

### 5.5 Harmonization Procedure

#### 5.5.1 Harmonization Identification

During Jurisdiction Mapping and Conflicts Analysis, the CCO, in collaboration with the relevant Business Unit and Engineering teams, shall proactively identify opportunities for control harmonization. A control is a candidate for harmonization if it satisfies requirements from two or more jurisdictions without diminishing the level of legal compliance for any single jurisdiction.

Priority harmonization targets include:

- **Data Subject / Individual Rights Request Handling**: Unified intake portal, routing logic based on data subject residency, and standardized response workflows.
- **Breach Notification**: Centralized incident response triggering the most stringent notification timeline (GDPR Art. 33: 72 hours to supervisory authority), with jurisdiction-specific notification templates for affected individuals.
- **Data Retention**: Unified retention schedules applying the most stringent applicable limitation period, with jurisdiction-specific legal hold overrides.
- **Transparency and Notice**: Layered privacy notice architecture with a global core notice supplemented by jurisdiction-specific appendices.
- **Security Measures**: Alignment of technical and organizational measures with the most comprehensive applicable standard (e.g., GDPR Art. 32 applied globally for all personal data processing, with additional specific HIPAA-required controls applied to PHI environments).
- **AI Documentation**: Unified technical documentation meeting both EU AI Act Annex IV requirements and any applicable U.S. regulatory expectations.

#### 5.5.2 Harmonization Design and Approval

For each identified harmonization opportunity, the CCO shall convene a **Harmonization Design Workshop** including the relevant Business Unit Lead, an Engineering representative, the DPO (for GDPR-relevant controls), the CAIO (for AI Act-relevant controls), and relevant Local Counsel.

The workshop shall produce a **Harmonized Control Specification** containing:

| Element | Description |
|---|---|
| Harmonized Control ID | Unique identifier |
| Jurisdictions Addressed | All jurisdictions whose requirements the control is designed to satisfy |
| Requirements Satisfied | Specific regulatory provisions (with citations) satisfied by the control |
| Control Description | Detailed technical, administrative, or operational description |
| Implementation Owner | Named individual responsible for deployment |
| Implementation Timeline | Target date for operationalization |
| Testing Methodology | How the control's effectiveness will be validated across all addressed jurisdictions |
| Local Counsel Concurrence | Confirmation (or objection) from each relevant Local Counsel |

The Harmonized Control Specification shall be approved by the GC (for controls involving potential legal interpretation risk) or the CCO (for operational controls), with CAIO concurrence required for any control addressing AI Act requirements.

#### 5.5.3 Jurisdiction-Specific Controls

Where harmonization is not feasible (e.g., due to a Level 2 or Level 3 conflict where MPP cannot be applied cleanly), the procedure shall produce a **Jurisdiction-Specific Control Specification** following the same format, clearly documenting:

- The specific regulatory requirement that cannot be harmonized.
- The technical or legal reason harmonization is infeasible.
- The specific control implemented for that jurisdiction alone.
- Any compensating controls or additional safeguards applied to mitigate the risk of control fragmentation.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Applies To | Owner |
|---|---|---|---|
| ADM-001 | **CJCC Quarterly Review**: Mandatory quarterly meeting with documented minutes, action items, and attendance records. | All BUs | CCO |
| ADM-002 | **Annual Compliance Program Assessment**: Independent (internal audit or external) review of the effectiveness of this SOP, covering a representative sample of jurisdiction mappings, conflict resolutions, and harmonized controls. | All BUs | GC (engages Internal Audit) |
| ADM-003 | **Regulatory Change Management Process**: Documented workflow from regulatory watch identification through Jurisdiction Mapping update, with SLAs: Initial Impact Assessment (15 business days), Full Mapping Update (45 business days). | All BUs | DPO, CCO |
| ADM-004 | **Local Counsel Annual Review**: Documented evaluation of all engaged Local Counsel per Section 5.4.3. | Global | GC |
| ADM-005 | **Compliance Training Program**: All personnel identified in Section 1.2.1 shall complete required training per Section 9. Training completion records maintained in Workday Learning. | All BUs | CCO, HR |
| ADM-006 | **Product Gate Review**: No product, feature, or processing activity proceeding through the Meridian Product Lifecycle (MPL) gate process shall pass Gate 4 (Deployment Approval) without evidence of completed Jurisdiction Mapping and resolution of any identified conflicts through this SOP. Refer to SOP-PLM-005: Product Lifecycle Management. | Engineering, Product | CCO, BU Leads |

### 6.2 Technical Controls

| Control ID | Control Description | Applies To | Owner |
|---|---|---|---|
| TEC-001 | **GRC Platform (Vanta) Configuration**: The GRC platform shall be configured with the workflows, forms, registers, and notification triggers specified in this SOP. This includes automated SLA monitoring for Jurisdiction Mapping timelines, escalation triggers for overdue Conflict Resolutions, and dashboard generation for KPI monitoring. | Global | CCO, IT Operations |
| TEC-002 | **Data Subject Request Portal**: A unified, jurisdiction-aware intake portal enabling individuals to submit rights requests. The portal shall perform initial jurisdiction identification based on residency indicators and route requests to the appropriate workflow (GDPR Articles 15–22, or jurisdiction-specific equivalent). | Global (customer-facing) | DPO, Engineering |
| TEC-003 | **Automated Retention Management**: Systems processing personal data subject to multiple retention obligations shall implement technical controls enforcing the most stringent applicable retention period, with legal-hold override capability managed through the Legal Hold module in the GRC platform. | All data systems | CCO, IT Operations |
| TEC-004 | **Cross-Border Transfer Logging**: All transfers of personal data across jurisdictional boundaries shall be automatically logged, including data categories, source and destination jurisdictions, transfer mechanism relied upon (e.g., Standard Contractual Clauses, Binding Corporate Rules, adequacy decision), and date of transfer. | Cloud infrastructure (AWS eu-west-1, us-east-1) | DPO, Engineering |
| TEC-005 | **AI System Registry**: A centralized technical registry of all AI systems deployed by Meridian, including their EU AI Act risk classification, conformity assessment status, CE marking status, and applicable harmonized controls. | Clinical AI Platform, MedInsight (as applicable) | CAIO, Engineering |

### 6.3 Physical and Environmental Controls

| Control ID | Control Description | Applies To | Owner |
|---|---|---|---|
| PHY-001 | **Jurisdiction-Specific Data Residency**: Where required by law or approved Jurisdiction-Specific Controls, Meridian shall enforce physical data residency constraints (e.g., EU personal data stored exclusively in AWS eu-west-1 region). Residency configurations shall be documented in the Jurisdiction Mapping Worksheet and enforced through AWS Control Tower policies. | Cloud Infrastructure | CISO, IT Operations |

### 6.4 GDPR-Specific Controls

The following controls are implemented specifically to satisfy GDPR obligations. Where these controls also satisfy requirements of other jurisdictions, they are designated as harmonized controls; where applicable solely to GDPR, they are designated as jurisdiction-specific.

| Control ID | GDPR Citation | Control Description | Type | Metric / SLA |
|---|---|---|---|---|
| GDPR-001 | Art. 5 (Principles) | **Data Minimization Assessment**: Each Jurisdiction Mapping Worksheet shall include a specific assessment of whether the data processed is adequate, relevant, and limited to what is necessary for the specified purposes. The DPO shall review and approve the minimization assessment. | Administrative | 100% of Tier 2/3 Mappings assessed |
| GDPR-002 | Art. 6, Art. 9 (Lawfulness) | **Lawful Basis Register**: The ROPA shall, for each processing activity, record the specific GDPR Article 6 and Article 9 lawful bases relied upon. The DPO shall verify the continuing validity of each lawful basis quarterly. | Administrative | Quarterly verification cycle |
| GDPR-003 | Art. 7 (Consent) | **Consent Management Platform**: Where consent is relied upon as a lawful basis, Meridian shall deploy a consent management platform (OneTrust) enabling granular, informed, and unambiguous consent collection with documented withdrawal mechanisms. Consent records shall be maintained with timestamp and scope. | Technical | Consent refresh per change in purpose |
| GDPR-004 | Art. 12 (Transparency) | **Layered Privacy Notice Architecture**: A core Meridian Privacy Notice supplemented by jurisdiction-specific appendices, all written in concise, transparent, intelligible, and easily accessible form, using clear and plain language. Notices shall be reviewed and updated within 30 days of any material processing change. | Administrative | Annual review; 30-day update trigger |
| GDPR-005 | Art. 15–22 (Data Subject Rights) | **Individual Rights Workflow**: Standardized workflows for handling access (Art. 15), rectification (Art. 16), erasure (Art. 17), restriction (Art. 18), notification (Art. 19), portability (Art. 20), objection (Art. 21), and automated decision-making (Art. 22) requests. All requests logged with SLA timer. Initial response within one month (Art. 12(3)). Complex requests may extend by two months with notification. | Administrative + Technical | 99% of requests responded to within statutory timeline |
| GDPR-006 | Art. 25 (Data Protection by Design and Default) | **DPbD Gate Check**: At each MPL Gate 2 (Architecture Review), Engineering shall demonstrate implementation of data protection by design and default principles, including pseudonymization and data minimization. DPO concurrence required. | Administrative | Every product/sprint cycle |
| GDPR-007 | Art. 28 (Processor Obligations) | **Processor Due Diligence and Contracting**: All processors shall undergo due diligence assessment and be bound by Art. 28-compliant Data Processing Agreements prior to processing. Processor compliance shall be audited annually on a risk-tiered basis (Tier 1 processors: on-site audit; Tier 2: questionnaire; Tier 3: self-assessment). | Administrative | 100% DPAs executed pre-processing |
| GDPR-008 | Art. 30 (Records of Processing) | **ROPA Maintenance**: The DPO shall maintain comprehensive ROPA in the GRC platform, updated within 10 business days of any new processing activity or material change. ROPA shall include all Art. 30(1) required elements. | Administrative | 10-business-day update SLA |
| GDPR-009 | Art. 32 (Security) | **Technical and Organizational Measures (TOMs)**: Implement TOMs appropriate to the risk, including encryption, pseudonymization, resilience, restoration, and regular testing. Refer to SOP-ISEC-002: Information Security Program. | Technical | Annual penetration testing; continuous monitoring |
| GDPR-010 | Art. 33–34 (Breach Notification) | **72-Hour Breach Notification Workflow**: Automated workflow initiating supervisory authority notification within 72 hours of breach discovery. Affected data subject notification without undue delay where high risk. Refer to SOP-ISIM-001: Security Incident Management. | Administrative + Technical | 72-hour notification SLA; tested semi-annually |
| GDPR-011 | Art. 35 (DPIA) | **DPIA Execution**: DPIAs shall be conducted for all high-risk processing (including all high-risk AI system processing) prior to processing initiation. DPIAs shall be reviewed by the DPO and updated at least annually or upon material change. | Administrative | Pre-processing; annual review |
| GDPR-012 | Art. 37–39 (DPO) | **DPO Independence and Resourcing**: The DPO shall report directly to the highest management level (CEO/Board). The DPO's office shall be adequately resourced with a dedicated budget line maintained by the CFO's office. No instruction shall be given to the DPO regarding the performance of their tasks. | Administrative | Annual budget review |
| GDPR-013 | Arts. 44–49 (Transfers) | **Transfer Mechanism Management**: All cross-border data transfers shall rely on valid transfer mechanisms (Art. 45 adequacy decisions, Art. 46 appropriate safeguards including Standard Contractual Clauses, or Art. 49 derogations). Transfer Impact Assessments (TIAs) shall be conducted and documented per EDPB guidance. | Administrative + Technical | TIA per new/high-risk transfer |

### 6.5 EU AI Act-Specific Controls

| Control ID | EU AI Act Citation | Control Description | Type | Metric / SLA |
|---|---|---|---|---|
| AIA-001 | Art. 8 (Compliance with Requirements) | **High-Risk AI Compliance Demonstration**: All high-risk AI systems shall demonstrate compliance with Chapter 2 requirements throughout their lifecycle. Compliance documentation maintained by CAIO's office. | Administrative | Continuous; reviewed quarterly |
| AIA-002 | Art. 9 (Risk Management System) | **Continuous Risk Management**: A risk management system shall be established, implemented, documented, and maintained for each high-risk AI system. Risks shall be identified, analyzed, and mitigated through iterative testing throughout the system lifecycle. | Administrative + Technical | Quarterly review cycle |
| AIA-003 | Art. 10 (Data and Data Governance) | **Training Data Governance**: Training, validation, and testing datasets shall be subject to governance practices addressing design choices, data collection, preparation, examination for biases, and identification of gaps. Datasets shall be relevant, representative, and free from errors to the best extent possible. | Technical | Per model training cycle |
| AIA-004 | Art. 11 (Technical Documentation) | **Technical Documentation Package**: Annex IV-compliant technical documentation shall be maintained for each high-risk AI system, updated continuously, and maintained for 10 years after system cessation. | Administrative + Technical | Real-time updates |
| AIA-005 | Art. 12 (Record-Keeping) | **Automatic Event Logging**: High-risk AI systems shall automatically record events (logs) over their lifetime. Logging shall include: date/time of system use; reference database against which input was checked; input data; identification of natural persons involved in verification of results. Logs retained for minimum 6 years. | Technical | Continuous logging; 6-year retention |
| AIA-006 | Art. 13 (Transparency and Provision of Information to Deployers) | **Deployer Information Package**: Prior to putting into service, Meridian shall provide deployers with comprehensive information enabling understanding and operation of the system, including: provider identity; system characteristics, capabilities, and limitations; intended purpose; accuracy, robustness, and cybersecurity performance; known circumstances that may lead to risks. | Administrative | Per deployer onboarding |
| AIA-007 | Art. 14 (Human Oversight) | **Human Oversight Mechanisms**: Each Clinical AI Platform product shall incorporate human-machine interface tools enabling human oversight as described in PS-06. Oversight personnel shall receive mandatory training on the specific AI system's capabilities, limitations, and bias awareness. Oversight capability shall be verified during conformity assessment. | Administrative + Technical | Per product release; training completion tracked |
| AIA-008 | Art. 15 (Accuracy, Robustness, and Cybersecurity) | **Resilience Testing**: High-risk AI systems shall undergo accuracy, robustness, and cybersecurity verification, including adversarial testing against attempts to exploit system vulnerabilities (data poisoning, adversarial inputs, model flaws). Results documented and addressed prior to each major release. | Technical | Per model release; penetration tested at least annually |
| AIA-009 | Art. 16 (Obligations of Providers) | **Provider Obligation Compliance**: As a provider, Meridian shall: ensure QMS compliance; draw up technical documentation; maintain logs; ensure conformity assessment; affix CE marking; draw up EU declaration of conformity; comply with registration obligations; take corrective actions; inform NB and deployers of non-compliance; cooperate with authorities. | Administrative | Continuous |
| AIA-010 | Art. 17 (Quality Management System) | **QMS Integration**: An ISO 13485-compatible QMS element specifically for AI system compliance shall be maintained, covering: regulatory compliance strategy; design control and verification procedures; examination, test, and validation procedures; technical specifications; risk management procedures. QMS shall be documented and auditable. | Administrative | ISO 13485:2016 certification maintained; annual audit |
| AIA-011 | Art. 19 (Automatically Generated Logs) | **Log Integrity Verification**: Logs generated under Art. 12 shall be subject to integrity verification (tamper-evident logging) through Meridian's centralized SIEM (Splunk). Quarterly log integrity reports shall be reviewed by the CISO. | Technical | Quarterly review |
| AIA-012 | Art. 27 (Fundamental Rights Impact Assessment) | **FRIA Execution**: For all high-risk AI systems, a Fundamental Rights Impact Assessment shall be conducted and documented, addressing: system's intended purpose; geographic and temporal scope; categories of persons affected; specific risks to fundamental rights; human oversight measures; measures to mitigate identified risks. FRIA shall be updated upon material system change and at least annually. | Administrative | Pre-deployment; annual update |
| AIA-013 | Art. 29 (Registration) | **EU Database Registration**: All high-risk AI systems shall be registered in the EU database prior to placing on the market or putting into service. CAIO's office responsible for timely registration and updates. | Administrative | Pre-market; updated upon material change |
| AIA-014 | Art. 43 (Conformity Assessment) | **Notified Body Engagement**: Clinical AI Platform products classified as high-risk AI systems shall undergo third-party conformity assessment by TÜV SÜD (NB 0123). CAIO's office manages the assessment process, document submission, and remediation tracking. | Administrative | Per assessment cycle |
| AIA-015 | Art. 61 (Post-Market Monitoring) | **Post-Market Monitoring System**: A systematic post-market monitoring process shall collect, document, and analyze data on the performance of high-risk AI systems throughout their lifetime. This includes proactive monitoring and reactive investigation of incidents. Results feed into risk management (Art. 9) and are reported to NB per schedule. | Administrative + Technical | Continuous; quarterly NB reporting |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The effectiveness of this SOP shall be monitored through the following KPIs, reported quarterly to the CJCC and semi-annually to the AI-GC.

| KPI ID | Metric | Target | Measurement Method | Owner |
|---|---|---|---|---|
| **JM-01** | Jurisdiction Mapping Completion Rate | 100% of Tier 1 mappings completed within 10 business days; 100% of Tier 2/3 within 20 business days | GRC platform SLA monitoring | CCO |
| **JM-02** | Mapping Trigger Coverage | 100% of applicable MPL Gate 4 approvals linked to approved Jurisdiction Mapping Worksheet | MPL gate review audit | CCO |
| **CF-01** | Unresolved Conflicts Aging | 0 conflicts > 90 days in Open status; 90% of Level 1 conflicts resolved within 30 days; 90% of Level 2/3 within 60 days | Conflicts Resolution Register aging report | CCO |
| **CF-02** | Conflict Identification Source Diversity | At least 20% of conflicts identified from sources other than Jurisdiction Mapping (i.e., employee reports, Local Counsel, or CJCC) — indicating healthy operational awareness | Source attribution in Register | CCO |
| **DSR-01** | GDPR Individual Rights Request Timeliness | 99% of requests under Arts. 15–22 responded to within statutory timeframe (Art. 12(3)) | GRC platform DSR module | DPO |
| **DSR-02** | Individual Rights Request Volume Trend | Monthly volume tracked; significant (>25% MoM) variance investigated and reported to CJCC | GRC platform DSR module | DPO |
| **BR-01** | Breach Notification Timeliness (GDPR) | 100% of notifiable breaches notified to supervisory authority within 72 hours of discovery | Incident management system (SOP-ISIM-001) | CISO, DPO |
| **TR-01** | Cross-Border Transfer Mechanism Validity | 100% of active cross-border transfers supported by valid mechanism (adequacy, SCCs, BCRs); 0 expired or superseded mechanisms | Transfer Register in GRC platform | DPO |
| **AI-01** | AI Act Registration Completeness | 100% of high-risk AI systems registered in EU database prior to market placement | EU database confirmation | CAIO |
| **AI-02** | Conformity Assessment Cycle Adherence | 0 conformity assessments exceeding their validity period; renewal initiated minimum 120 days prior to expiry | CAIO tracker | CAIO |
| **TR-02** | Training Compliance | 95% of assigned personnel current on required compliance training | Workday Learning LMS | CCO, HR |
| **EX-01** | Exception Count and Aging | Active exceptions < 10 at any time; mean exception duration < 180 days; 0 exceptions past expiry without renewal | GRC platform exceptions module | CCO |
| **AU-01** | Audit Finding Remediation | Critical findings: 30-day remediation; High findings: 90-day; Medium: 180-day; Low: next review cycle | GRC platform audit module | CCO |

### 7.2 Reporting Cadence

| Report | Audience | Frequency | Content | Preparer |
|---|---|---|---|---|
| **CJCC Quarterly Compliance Deck** | CJCC | Quarterly | KPI dashboard, open conflicts, regulatory watch highlights, exception report, training stats, forward outlook | CCO with DPO, CAIO input |
| **AI-GC Semi-Annual Briefing** | Board AI Governance Committee | Semi-Annual (June, December) | Executive summary of cross-jurisdictional compliance status, material conflicts, AI Act compliance progress, audit results, regulatory horizon | CCO, GC |
| **Monthly Regulatory Watch Brief** | CJCC Members (distribution list) | Monthly (15th) | Regulatory developments, enforcement actions, guidance updates | DPO |
| **Annual Compliance Program Effectiveness Report** | GC, Audit Committee | Annual (Q1) | Comprehensive assessment of SOP effectiveness per ADM-002, KPI trend analysis, external audit results | GC (via Internal Audit or external assessor) |

### 7.3 Dashboards

The GRC platform (Vanta) shall maintain real-time or near-real-time dashboards accessible to CJCC members and authorized personnel, displaying:

1. **Jurisdiction Mapping Status Dashboard**: All active, pending, and overdue Jurisdiction Mappings; visual SLA compliance indicator (green/yellow/red).
2. **Conflicts Resolution Dashboard**: Open conflicts by severity, age, and business unit; resolution trend (month-over-month); overdue conflicts.
3. **Individual Rights Request Dashboard**: Volume, source (jurisdiction), request type (access/erasure/rectification, etc.), response time SLA compliance.
4. **EU AI Act Compliance Dashboard**: Registration status, conformity assessment status and expiration, FRIA completion status per system.
5. **Exception Dashboard**: Active exceptions, expiration dates, renewal status.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Definition

An exception, for purposes of this SOP, is a documented, time-limited deviation from a specific procedural requirement, control implementation timeline, or policy commitment, approved by the designated authority prior to the deviation occurring.

Exceptions do not apply to:
- Non-compliance with mandatory legal requirements (Meridian cannot grant exceptions to law).
- The requirement to perform Jurisdiction Mapping prior to product deployment (this may be expedited but not waived).
- The requirement to resolve conflicts through the structured procedure (alternative procedures may be approved but the requirement for a structured, documented resolution cannot be waived).

### 8.2 Exception Request Procedure

1. **Initiation**: Any personnel identified in Section 1.2.1 may request an exception by completing the **Compliance Exception Request Form** (Appendix D) in the GRC platform. The request shall specify:
   - The specific SOP provision (section number) from which deviation is requested.
   - The business justification for the exception.
   - The proposed alternative control or compensating measure, if any.
   - The requested exception duration.
   - The impact of non-approval on business operations.

2. **Impact Assessment**: The CCO's office shall, within **5 business days**, prepare an impact assessment addressing:
   - Regulatory risk created by the deviation.
   - Impact on other jurisdictions' compliance posture (cross-jurisdictional ripple effects).
   - Impact on contractual obligations and customer commitments.
   - Whether compensating controls are sufficient to reduce residual risk to acceptable levels.

3. **Approval Authority**:
   - **Standard Exception** (duration ≤ 90 days, low-medium risk as determined by CCO): CCO approval.
   - **Extended Exception** (duration 91–365 days, or high risk): GC approval required.
   - **Extraordinary Exception** (duration > 365 days, or relates to high-risk AI system EU AI Act compliance): GC and CAIO joint approval required, with notification to AI-GC if duration exceeds 180 days.

4. **Approval/Rejection**: The approver shall render a decision within **10 business days** of request submission (or 5 business days if marked "Emergency" by the requestor and confirmed by CCO). Rationale shall be documented in the GRC platform.

5. **Exception Register**: Approved exceptions are logged in the Exceptions Register with automatic expiration date tracking and renewal reminder triggers (30, 15, and 7 days prior to expiration).

### 8.3 Escalation Path

If, at any point in the execution of this SOP, a matter cannot be resolved at the designated level, the following escalation path shall apply:

1. **CCO Office** (operational disputes, procedural interpretation)
2. **CJCC Chair (CCO)** (cross-BU impacts, resource conflicts)
3. **General Counsel** (legal interpretation disputes, true conflict determinations, high-risk exceptions)
4. **CEO** (determination of whether to continue processing activity in a jurisdiction where true compliance impossibility has been identified by GC)
5. **Board of Directors / AI-GC** (for matters impacting the fundamental risk profile of the Company or requiring public disclosure consideration)

---

## 9. Training Requirements

### 9.1 Required Training Modules

All personnel identified in the organizational scope (Section 1.2.1) shall complete the following training, tracked through the Workday Learning Management System:

| Training Module | Content | Target Audience | Frequency | Delivery Method | Owner |
|---|---|---|---|---|---|
| **TRAIN-CJC-001: Cross-Jurisdictional Compliance Fundamentals** | Overview of Meridian's regulatory landscape; purpose and operation of this SOP; roles and responsibilities; how to identify and escalate potential jurisdictional issues; case study exercises. | All in-scope personnel | Initial within 30 days of hire/role change; annual refresher | eLearning (Workday) + live workshop (virtual) for BU Leads and above | CCO |
| **TRAIN-GDPR-001: GDPR for Product and Engineering Teams** | In-depth GDPR principles, lawful bases, data subject rights (Arts. 15–22), DPIAs, cross-border transfer rules, processor obligations. Includes product-specific modules for Clinical AI, HealthPay, and MedInsight. | All Engineering, Product, Clinical AI, HealthPay, MedInsight personnel; DPO office | Annual | eLearning + live Q&A with DPO | DPO |
| **TRAIN-AIA-001: EU AI Act Compliance for AI Practitioners** | AI Act risk classification; requirements for high-risk AI systems (Chapter 2); provider obligations; human oversight requirements; conformity assessment process; Fundamental Rights Impact Assessment methodology. | Clinical AI personnel, ML Engineering, CAIO office, relevant QA | Initial; refresher upon material regulatory update | Instructor-led (CAIO office) | CAIO |
| **TRAIN-CON-001: Conflicts Identification and Reporting** | Practical training on recognizing operational regulatory conflicts; how to document and submit conflict identifications; confidentiality and non-retaliation. | All Engineering and Product personnel | Annual | eLearning (micro-module, 15 minutes) | CCO |

### 9.2 Training Compliance Monitoring

- The CCO's office, in coordination with HR, shall generate a monthly **Training Compliance Report** from Workday Learning.
- Managers of personnel not current on required training shall be notified automatically at 7 days past due, with escalation to BU Lead at 30 days past due.
- BU Leads shall report on training compliance at the CJCC quarterly meeting.
- Persistent non-compliance (>60 days past due) shall be escalated to the relevant VP and the GC for intervention.

### 9.3 Training Content Review

All jurisdictional compliance training content shall be reviewed and updated:
- Annually, as part of the training content review cycle.
- Within 45 business days of any material regulatory change affecting the training subject matter (per PS-08).
- Upon identification of a compliance gap where training deficiency was a root cause.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| SOP / Policy ID | Title | Relationship to This SOP |
|---|---|---|
| SOP-AI-042 | AI Model Lifecycle Management | Governs the technical lifecycle of AI models; this SOP addresses the regulatory compliance of those models across jurisdictions. |
| SOP-ISIM-001 | Security Incident Management | Provides the incident response framework referenced by GDPR-010 (breach notification) and AIA-008 (cybersecurity for AI). |
| SOP-ISEC-002 | Information Security Program | Defines the technical and organizational measures referenced in GDPR-009 and the security controls underpinning harmonized technical safeguards. |
| SOP-ISEC-022 | Data Classification Policy | Standard data classification taxonomy used in Jurisdiction Mapping data categorization. |
| SOP-PRIV-003 | Data Subject Rights Management | Operational procedures for handling individual rights requests; implements the workflow referenced in GDPR-005. |
| SOP-PRIV-005 | Data Protection Impact Assessment Methodology | Standard DPIA process, integrated with this SOP's jurisdictional considerations. |
| SOP-PLM-005 | Product Lifecycle Management | Defines MPL gates; this SOP's mapping requirements are integrated at Gate 4 per ADM-006. |
| SOP-FIN-031 | Financial Controls Framework | Relevant for HealthPay jurisdiction mapping involving financial services regulations. |
| SOP-HR-019 | Employee Data Privacy | Governs HR data processing; referenced as out of scope in Section 1.2.4. |
| SOP-LEGC-012 | External Legal Engagement and Matter Management | Governs engagement of Local Counsel (Legal Tracker system, engagement letters). |
| SOP-QMS-001 | Quality Management System (ISO 13485) | QMS into which EU AI Act Art. 17 QMS element integrates. |

### 10.2 External Standards and Frameworks

| Standard / Framework | Reference | Applicability |
|---|---|---|
| ISO 13485:2016 | Quality Management Systems for Medical Devices | Clinical AI Platform; referenced in AIA-010 |
| ISO 27001:2022 | Information Security Management | Information Security Program; foundational for technical controls |
| ISO 27701:2019 | Privacy Information Management | GDPR compliance enhancement |
| NIST AI Risk Management Framework (AI RMF 1.0) | U.S. AI governance reference | Referenced for U.S. jurisdictional AI considerations (not a binding framework) |
| EU Standard Contractual Clauses (2021/914) | Cross-border data transfer mechanism | Referenced in GDPR-013 |
| EDPB Guidelines (various) | GDPR interpretive guidance | Binding interpretive guidance for GDPR compliance |

### 10.3 Regulatory Texts

| Regulation | Citation |
|---|---|
| General Data Protection Regulation | Regulation (EU) 2016/679 |
| EU Artificial Intelligence Act | Regulation (EU) 2024/1689 |
| EU Medical Device Regulation | Regulation (EU) 2017/745 |
| Health Insurance Portability and Accountability Act | Public Law 104-191; 45 CFR Parts 160, 162, 164 |
| California Medical Information Act | Cal. Civ. Code §§ 56–56.37 |
| Washington My Health My Data Act | RCW Chapter 19.373 |
| Personal Information Protection and Electronic Documents Act (Canada) | S.C. 2000, c. 5 |
| Personal Data Protection Act 2012 (Singapore) | Act 26 of 2012 |

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2019-03-15 | A. Petrov (former CCO) | Initial SOP creation, covering GDPR-only cross-border coordination post-Schrems II preparations. |
| 1.5 | 2020-08-22 | K. Weber (DPO) | Major revision: Added CJCC governance structure; expanded Jurisdiction Mapping to include UK post-Brexit as separate jurisdiction; incorporated Schrems II Transfer Impact Assessment requirements. |
| 2.0 | 2022-01-10 | T. Anderson (CCO), M. Gonzalez (GC) | Comprehensive rewrite expanding scope from GDPR-primary to multi-jurisdictional framework; added harmonization methodology; incorporated state privacy law developments (CA, CO, VA); aligned with ISO 27701 certification effort. |
| 2.3 | 2023-06-05 | T. Anderson, M. Gonzalez, D. Rivera (CAIO) | Pre-EU AI Act readiness revision: Added preliminary AI Act compliance architecture (placeholder controls); established CAIO role responsibilities; incorporated Washington My Health My Data Act obligations. |
| 2.5 | 2024-02-01 | T. Anderson, M. Gonzalez, D. Rivera | EU AI Act finalization revision: Replaced placeholder AI Act controls with final Article-specific controls; updated Conformity Assessment procedures; designated TÜV SÜD as Notified Body; aligned with EU MDR CE marking transition. |
| 2.6 | 2024-06-01 | T. Anderson | Updated Training Requirements (TRAIN-AIA-001); refined KPI targets based on two quarters of operational data; added escalation path formalization; integrated ADM-006 Product Gate Review control. |
| 2.7 | 2024-06-20 | T. Anderson, M. Gonzalez | Version approved for external audit readiness: Added comprehensive GDPR technical control table (GDPR-001 through GDPR-013); refined MPP articulation; updated Local Counsel roster; incorporated CJCC Annual Deep Dive agenda; updated regulatory horizon assessment. |
| 2.8 (Draft) | — | T. Anderson (in preparation) | Integration with upcoming Canada Bill C-27 amendments; Singapore PDPA amendment alignment; U.S. federal AI executive order impact assessment framework; planned effective date: Q4 2025. |

---

**Document Classification: Internal**
Distribution: All personnel identified in Section 1.2.1; accessible via Meridian Policy Portal (Vanta).
Questions regarding this SOP should be directed to: compliance@meridian-healthtech.com or via the GRC platform inquiry workflow.