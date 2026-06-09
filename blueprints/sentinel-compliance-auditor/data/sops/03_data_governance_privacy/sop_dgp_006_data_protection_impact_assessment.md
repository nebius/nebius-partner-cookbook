---
sop_id: "SOP-DGP-006"
title: "Data Protection Impact Assessment"
business_unit: "Data Governance & Privacy"
version: "1.4"
effective_date: "2025-11-12"
last_reviewed: "2026-12-19"
next_review: "2027-06-19"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Data Protection Impact Assessment

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the mandatory methodology for conducting, documenting, and maintaining Data Protection Impact Assessments (DPIAs) at Meridian Health Technologies, Inc. The procedure is designed to systematically identify, assess, and mitigate risks to the rights and freedoms of natural persons arising from the processing of personal data, with particular emphasis on high-risk processing activities inherent to Meridian’s AI-driven healthcare and financial services business lines.

### 1.2 Scope

#### 1.2.1 Organizational Scope
This SOP applies to all business units, subsidiaries, and global offices of Meridian Health Technologies, Inc., including but not limited to locations in Boston, London, Berlin, Singapore, and Toronto. All employees, contractors, consultants, and third-party vendors who design, develop, deploy, or maintain systems that process personal data are bound by the requirements herein.

#### 1.2.2 Functional Scope
The DPIA requirement applies to all processing activities involving personal data across the following business lines and technology platforms:
- Clinical AI Platform (including diagnostic imaging analysis, patient risk scoring, adverse event prediction)
- HealthPay Financial Services (including credit scoring models, fraud detection systems, automated lending decisions)
- MedInsight Analytics (including population health analytics, care gap identification, outcomes prediction)
- Meridian SaaS Platform (the underlying multi-tenant cloud infrastructure)
- Any new technology, system, or processing activity introduced after the effective date of this SOP
- Any significant modification to existing processing activities that alters the nature, scope, context, or purposes of processing
- Processing activities involving special categories of personal data, including health data, genetic data, and biometric data
- Systematic and extensive automated profiling that produces legal effects or similarly significant effects

#### 1.2.3 Geographic Scope
This SOP governs processing activities regardless of where the processing occurs, provided the data subjects are located within the European Union or the processing activities are subject to regulatory obligations by virtue of Meridian’s market presence, including but not limited to the EU AI Act and its extraterritorial provisions.

### 1.3 Policy Owner
The Chief Privacy Officer / Data Protection Officer (DPO), Dr. Klaus Weber, is the policy owner and maintains authority over DPIA methodology, threshold assessments, and final approval of completed DPIAs.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
|--------------|------------|
| **AI System** | As defined in Article 3(1) of the EU AI Act: a machine-based system designed to operate with varying levels of autonomy, that may exhibit adaptiveness after deployment and that, for explicit or implicit objectives, infers from the input it receives how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments. |
| **AIAO** | AI Assessment Officer – Meridian’s designated role responsible for coordinating AI Act compliance assessments, currently held by Deputy DPO Sandra Lim. |
| **CISO** | Chief Information Security Officer |
| **CRO** | Chief Risk Officer |
| **DPIA** | Data Protection Impact Assessment – A process designed to describe the processing, assess its necessity and proportionality, and help manage the risks to the rights and freedoms of natural persons resulting from the processing of personal data. |
| **DPO** | Data Protection Officer |
| **EU AI Act** | Regulation (EU) 2024/1689 laying down harmonized rules on artificial intelligence |
| **Fundamental Rights Impact Assessment (FRIA)** | The assessment required under Article 27 of the EU AI Act for high-risk AI systems, which Meridian integrates with its DPIA process as a combined assessment where applicable. |
| **High-Risk AI System** | AI systems classified under Annex III of the EU AI Act, including but not limited to AI systems intended to be used for the evaluation and classification of emergency calls, triaging patients, or as a safety component in the management and operation of critical digital infrastructure in healthcare. |
| **HITRUST** | Health Information Trust Alliance Common Security Framework |
| **MLOPS-REG-001** | Meridian’s internal registry identifier for model risk assessments |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework |
| **Personal Data** | Any information relating to an identified or identifiable natural person. |
| **PHI** | Protected Health Information |
| **RASP** | Risk Assessment Scoring Protocol – Meridian’s proprietary quantitative risk methodology (see Appendix B of internal risk manual). |
| **SR 11-7** | Federal Reserve Supervisory Guidance on Model Risk Management |
| **Standard Contractual Clauses (SCCs)** | European Commission-approved model clauses for the transfer of personal data to third countries. |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

| Activity / Deliverable | DPO (Dr. Weber) | AIAO (S. Lim) | Business Unit VP | System Owner | CISO (R. Kim) | Compliance (T. Anderson) | General Counsel (M. Gonzalez) |
|------------------------|-----------------|---------------|-------------------|--------------|---------------|--------------------------|-------------------------------|
| DPIA Threshold Assessment | A | R | C | C | I | I | I |
| DPIA Initiation Decision | A/R | C | I | I | I | C | I |
| DPIA Completion & Documentation | A | R | R | R | C | C | I |
| Risk Scoring (RASP Methodology) | A | R | C | C | I | I | I |
| Technical Control Validation | I | C | I | R | A/R | I | I |
| FRIA Integration (Article 27) | A | R | C | C | C | C | C |
| Residual Risk Acceptance | C | C | I | I | I | I | A/R |
| Regulatory Notification Decision | C | C | I | I | I | R | A |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

### 3.2 Detailed Role Descriptions

**Dr. Klaus Weber, Chief Privacy Officer / DPO**
- Serves as the ultimate authority on DPIA adequacy and approval
- Maintains the DPIA methodology and updates this SOP as required
- Consults with supervisory authorities when residual risks are deemed unacceptable
- Provides final sign-off on all DPIAs involving high-risk AI systems
- Maintains the central DPIA register in Meridian’s governance, risk, and compliance (GRC) platform (Archer)

**Sandra Lim, AI Assessment Officer (AIAO)**
- Coordinates the operational execution of DPIAs for AI systems
- Ensures integration of DPIA and FRIA requirements under Article 27 of the EU AI Act
- Maintains the AI system inventory and classification register
- Validates that human oversight mechanisms are documented in the DPIA
- Reports quarterly to the AI Governance Committee on DPIA completion status

**Business Unit Vice Presidents (VP Clinical AI Products, VP Financial Services, VP Engineering)**
- Ensure that all new projects, products, or significant changes within their purview are submitted for DPIA threshold assessment
- Allocate resources for DPIA completion within mandated timelines
- Review and acknowledge DPIA findings and residual risk determinations
- Implement required risk mitigation measures within their business units

**System Owners**
- Complete the technical portions of the DPIA template, including data flow mapping, system architecture descriptions, and control inventories
- Maintain current data flow diagrams in Meridian’s enterprise architecture tool (LeanIX)
- Coordinate with engineering teams to provide technical accuracy of DPIA content
- Remediate identified control gaps within agreed timelines (see Section 8.3)

**Rachel Kim, Chief Information Security Officer**
- Validates technical and organizational security measures documented in the DPIA
- Consults on encryption standards, access controls, and incident response capabilities
- Provides assessment of security residual risk for DPIA documentation

**Thomas Anderson, Chief Compliance Officer**
- Ensures alignment between DPIA findings and Meridian’s broader compliance obligations
- Coordinates with CISO on SOC 2 control mapping where applicable
- Maintains regulatory notification procedures (see SOP-DGP-009)

**Maria Gonzalez, General Counsel**
- Provides final legal review of DPIA conclusions
- Approves acceptance of residual risks above the standard tolerance threshold
- Authorizes any regulatory notifications or consultations
- Approves exceptions to this SOP (see Section 8)

---

## 4. Policy Statements

### 4.1 Mandatory DPIA Requirement
Meridian Health Technologies shall conduct a DPIA prior to commencing any processing of personal data that, by virtue of its nature, scope, context, or purposes, is likely to result in a high risk to the rights and freedoms of natural persons. The DPIA shall be completed, reviewed, and approved before the first instance of processing commences.

### 4.2 Integration with AI Act Assessments
For all AI systems classified as high-risk under Annex III of the EU AI Act, Meridian shall integrate the DPIA with the Fundamental Rights Impact Assessment (FRIA) required under Article 27. The combined assessment shall be documented in Meridian's unified DPIA/FRIA template (see Appendix A of internal template repository) and shall specifically address the following elements mandated by Article 27(1):
- A detailed description of the intended purpose for which the high-risk AI system will be used
- A detailed description of the geographical and temporal scope within which the high-risk AI system is expected to be used
- Categories of natural persons and groups likely to be affected by the use of the high-risk AI system
- Verification that the use of the high-risk AI system is compliant with relevant Union and national law on fundamental rights
- The reasonably foreseeable adverse impact on fundamental rights
- The specific measures to be taken to mitigate the identified risks

### 4.3 AI System Classification
All AI systems developed, procured, or deployed by Meridian must undergo classification assessment against Annex III criteria within 30 calendar days of initiation of development or procurement. The classification matrix is maintained by the AIAO and reviewed quarterly by the AI Governance Committee.

### 4.4 Human Oversight Requirement
For all high-risk AI systems, Meridian shall design and implement human oversight mechanisms as required by Article 14 of the EU AI Act. These mechanisms shall be documented in the DPIA and shall enable natural persons to:
- Fully understand the capabilities and limitations of the high-risk AI system and be able to duly monitor its operation
- Remain aware of the possible tendency of automatically relying or over-relying on the output produced by the high-risk AI system
- Correctly interpret the system's output, taking into account the specific characteristics of the system and the interpretation tools and methods available
- Decide, in any particular situation, not to use the high-risk AI system or otherwise disregard, override, or reverse the output of the system
- Intervene in the operation of the high-risk AI system or interrupt the system

### 4.5 Transparency (EU AI Act, Article 13)
Meridian shall design and develop high-risk AI systems in such a way that their operation is sufficiently transparent to enable deployers to interpret the system's output and use it appropriately. Transparency information shall be documented in the DPIA and shall include:
- Instructions for use, including the identity and contact details of the provider
- The characteristics, capabilities, and limitations of performance of the AI system
- Any known or foreseeable circumstances that may lead to risks to health and safety, or to fundamental rights
- The specifications for input data, including data governance measures under Article 10
- Information on the accuracy, including where appropriate its metrics, levels of robustness and cybersecurity referred to in Article 15

### 4.6 Record-Keeping (EU AI Act, Articles 11 and 12)
For high-risk AI systems, Meridian shall maintain:
- Technical documentation demonstrating compliance with Chapter 2 of Title III of the EU AI Act
- Automatic logging capabilities (logs) over the duration of the system's lifetime as specified in Article 12
- Records of conformity assessment procedures

### 4.7 Prohibition on Certain AI Practices
Meridian unconditionally prohibits the development, deployment, or use of AI systems classified as prohibited practices under Article 5 of the EU AI Act, including:
- AI systems deploying subliminal techniques beyond a person's consciousness or purposefully manipulative or deceptive techniques
- AI systems exploiting vulnerabilities of individuals due to age, disability, or specific social/economic situation
- AI-based social scoring systems
- Real-time remote biometric identification systems in publicly accessible spaces

Any employee becoming aware of activities that may contravene this prohibition shall escalate immediately via the procedure in Section 8.

---

## 5. Detailed Procedures

### 5.1 DPIA Initiation and Threshold Assessment

#### 5.1.1 Trigger Identification
A DPIA shall be initiated upon the occurrence of any of the following triggers:

| Trigger ID | Description | Responsible Party |
|------------|-------------|-------------------|
| T-001 | New product or feature involving personal data processing | Product Manager / System Owner |
| T-002 | New AI/ML model involving personal data inference | Data Science Lead / MLOps team |
| T-003 | Significant system architecture change affecting data flows | Engineering Lead / System Owner |
| T-004 | New third-party data processor engagement | Procurement / Vendor Management |
| T-005 | Processing of data concerning vulnerable persons identified in research datasets | Clinical Research Lead |
| T-006 | Cross-border data transfer to a country without adequacy decision | Legal (M. Gonzalez) |
| T-007 | Annual review cycle for existing high-risk processes (per this SOP, Section 5.8) | AIAO (S. Lim) |
| T-008 | Post-incident review recommendation from CISO | CISO (R. Kim) |

#### 5.1.2 Threshold Assessment Questionnaire
Upon trigger identification, the System Owner shall complete the DPIA Threshold Assessment Questionnaire in Meridian's GRC platform (Archer) within 5 business days. The questionnaire consists of the following scored elements:

**Section A: Nature of Data (Scored 0-15)**

| Question | Weight |
|----------|--------|
| Does the processing involve special categories of personal data (health, genetic, biometric, data revealing racial/ethnic origin, political opinions, religious beliefs, trade union membership, sex life/sexual orientation)? | 10 points |
| Does the processing involve data relating to criminal convictions and offenses? | 5 points |
| Does the processing involve financial data or credit information? | 3 points |

**Section B: Nature of Processing (Scored 0-20)**

| Question | Weight |
|----------|--------|
| Is the processing performed by an AI system that produces legal effects or similarly significant effects on data subjects? | 8 points |
| Does the processing involve systematic and extensive profiling or automated decision-making? | 7 points |
| Does the processing involve large-scale processing of personal data (as defined in Meridian's data classification policy, SOP-DGP-001)? | 5 points |

**Section C: Impact on Data Subjects (Scored 0-15)**

| Question | Weight |
|----------|--------|
| Does the processing relate to vulnerable data subjects, including patients, children, elderly persons, or individuals with diminished decision-making capacity? | 8 points |
| Does the processing involve evaluation or scoring of individuals, including creditworthiness, economic situation, health, personal preferences or interests, reliability or behavior, location or movements? | 7 points |

**Section D: Systematic Monitoring (Scored 0-10)**

| Question | Weight |
|----------|--------|
| Does the processing involve systematic monitoring of data subjects, including of publicly accessible areas? | 5 points |
| Does the processing combine, compare, or match personal data from multiple sources? | 5 points |

**Section E: Technological Novelty (Scored 0-10)**

| Question | Weight |
|----------|--------|
| Does the processing involve the use of new technologies or novel applications of existing technologies, including AI, machine learning, large language models, or computer vision? | 10 points |

**Threshold Determination:**
- **Total Score ≥ 25: DPIA is MANDATORY.** Proceed immediately to Section 5.2. No processing may commence until DPIA is approved.
- **Total Score 15-24: DPIA is REQUIRED unless waived by DPO.** The AIAO reviews the assessment and may, with DPO written concurrence, authorize a streamlined assessment per Section 5.2.3.
- **Total Score 8-14: DPO Discretionary Review.** The AIAO reviews and presents to the DPO within 5 business days. The DPO may require a full DPIA if qualitative risk factors are present.
- **Total Score 0-7: No DPIA required.** The System Owner shall document the no-DPIA determination in Archer. This determination is valid for 12 months or until the processing materially changes, whichever occurs first.

#### 5.1.3 AI System Concurrent Classification
If the processing involves any automated decision-making or AI/ML components, the AIAO shall simultaneously initiate the AI system classification process against Annex III of the EU AI Act. This process runs in parallel with the DPIA threshold assessment and uses the following classification criteria:

| Classification Criterion | Assessment |
|--------------------------|------------|
| Is the system a medical device or safety component? | Evaluate against EU MDR. Meridian's CE-marked Clinical AI Platform products (2025) are **automatically classified as high-risk** if they perform diagnostic classification. |
| Is the system intended for emergency patient triage? | Evaluate against Annex III, point 1. |
| Is the system biometric categorization or emotion recognition? | Evaluate against Annex III, point 1(b) and 1(c). |
| Is the system used for credit evaluation or assessment? | Evaluate against Annex III, point 5(b). All HealthPay automated lending models are subject to classification. |
| Is the system used for determining access to essential private or public services? | Evaluate against Annex III, point 5. |

A confirmed high-risk classification under Annex III automatically triggers a score of ≥ 25 on the DPIA threshold assessment, mandating a full DPIA regardless of other scores.

### 5.2 DPIA Execution Methodology

#### 5.2.1 Initiation Phase (Days 1-5)
Upon determination that a DPIA is mandatory, the AIAO shall:

1. **Open the DPIA record in Archer** (Form DPIA-F-001) and assign a unique DPIA identifier using the format: `DPIA-YYYY-NNN`, where YYYY is the year and NNN is a sequential identifier.

2. **Convene a DPIA kickoff meeting** within 5 business days. Required attendees include:
   - AIAO (S. Lim) — Chair
   - System Owner or designated technical lead
   - Business Unit VP or delegate
   - CISO representative (for technical control assessment)
   - DPO (Dr. Weber) or delegate
   - Data Science Lead (if AI/ML processing is involved)

3. **Define the DPIA scope and data flow boundaries.** The System Owner must present current data flow diagrams in LeanIX. If no current diagrams exist, they must be produced within 5 additional business days and validated by the CISO representative.

4. **Identify all data processors (sub-processors)** involved in the processing activity. The Vendor Management office must provide current Data Processing Agreements for all identified processors.

#### 5.2.2 Full DPIA Execution (Days 6-30)

The full DPIA shall be documented in Archer (Form DPIA-F-002) and shall address the following mandatory sections:

**Part 1: Systematic Description of the Processing**
The System Owner must provide a detailed, plain-language description that includes:
- The nature of the processing: What personal data is collected, how it is collected, storage mechanisms, transmission paths
- The scope of the processing: Geographic coverage, volume estimations (records/data subjects processed annually), frequency of processing cycles
- The context of the processing: The specific business purpose, the relationship between Meridian and the data subjects, the degree of control Meridian exercises
- The purposes of the processing: Specific, explicit, and legitimate purposes articulated at a granular level of detail. For AI/ML systems, include the model's intended purpose, the inferential objectives, and the decision domain.
- Technical description: Include system architecture diagrams, cloud service provider configurations, encryption at rest and in transit specifications, geographic locations of primary and backup data centers

**Part 2: Necessity and Proportionality Assessment**
The AIAO leads this assessment, examining:
- Is the processing necessary to achieve the stated purpose? Document why less intrusive alternatives are insufficient.
- Is the data collected proportionate to the purpose? Justify each data element collected against the specific purpose.
- For AI systems: Evaluate data minimization against the requirements of Article 10 of the EU AI Act. Document training, validation, and testing dataset governance measures, including:
  - Dataset provenance documentation
  - Bias examination and correction procedures
  - Data quality verification against specified metrics (accuracy, completeness, currency, consistency)
  - Relevance of data to the intended purpose

**Part 3: Risk Assessment (RASP Methodology)**
Meridian uses the Risk Assessment Scoring Protocol (RASP) to quantify risks to the rights and freedoms of data subjects. The methodology assesses:

**A. Risk Identification**
For each risk identified, document:
- Risk ID (format: R-XXXX)
- Risk scenario description
- Threat source(s): internal, external, environmental
- Affected data subject categories
- Potential impact description

**B. Impact Assessment**
Impact is scored on a 1-5 scale across the following dimensions:

| Dimension | Score 1 | Score 3 | Score 5 |
|-----------|---------|---------|---------|
| Physical harm potential | Negligible | Moderate temporary impairment | Significant injury or long-term health damage |
| Psychological harm | No distress | Moderate distress | Severe psychological harm |
| Economic harm | < €100 | €500-€5,000 | > €50,000 or life-altering |
| Discrimination risk | No differential impact | Potential disparate impact | Documented discriminatory outcomes |
| Loss of autonomy | No effect on decision-making | Reduced ability to exercise rights | Complete loss of control over personal data |
| Social disadvantage | No stigmatization | Risk of stigmatization | Documented social exclusion |

**C. Likelihood Assessment**
Likelihood is scored on a 1-5 scale:
- 1: Remote (< 1% probability in 12-month period)
- 2: Unlikely (1-5%)
- 3: Possible (6-20%)
- 4: Likely (21-50%)
- 5: Almost Certain (> 50%)

**D. Risk Scoring Calculation**
`RASP Score = (Impact Score × Likelihood Score)`

Risk levels are classified as:
- **Critical (Score 20-25):** Immediate DPO escalation. Processing shall not proceed. The DPO shall consult the relevant supervisory authority.
- **High (Score 15-19):** DPO review required. Mitigation plan with specific measurable milestones must be approved by DPO and General Counsel before processing may commence.
- **Medium (Score 10-14):** AIAO approval with documented mitigation controls. Processing may commence once controls are validated.
- **Low (Score 5-9):** Standard monitoring. AIAO records acceptance.
- **Negligible (Score 1-4):** Accepted risk. No active mitigation required.

**E. FRIA Integration (EU AI Act, Article 27)**
For AI systems classified as high-risk under Annex III, the DPIA must be augmented with the specific FRIA elements. The combined assessment document shall include:

1. **FRIA Section 1: Intended Purpose and Deployment Context**
   - Detailed description of system's intended use
   - Geographical deployment plan (which Meridian offices will use the system)
   - Temporal scope (is the system intended for permanent or temporary use? minimum expected lifetime?)

2. **FRIA Section 2: Affected Groups**
   - Identification of all categories of natural persons and groups reasonably expected to be affected
   - Specific analysis of vulnerable groups at disproportionate risk
   - For Clinical AI Platform: Include patient population demographics, disease prevalence considerations, and healthcare access disparities analysis

3. **FRIA Section 3: Fundamental Rights Impact Assessment**
   For each right in the EU Charter of Fundamental Rights that may be impacted, document:
   - The specific right at issue (e.g., Article 8 — Protection of personal data; Article 21 — Non-discrimination; Article 35 — Health care)
   - The reasonably foreseeable adverse impact
   - Severity and probability
   - The specific measures to mitigate

4. **FRIA Section 4: Specific Mitigation Measures**
   - Detailed technical measures
   - Operational measures (human oversight procedures, training)
   - Organizational measures (governance, audit, reporting)
   - Timeline for implementation
   - Responsible roles

#### 5.2.3 Streamlined DPIA (When Authorized)
When the threshold assessment score is 15-24 and the DPO has authorized a streamlined assessment, the AIAO shall complete a shortened DPIA (Archer Form DPIA-F-003) that comprises:
- Part 1 (Systematic Description) — Abbreviated
- Part 2 (Necessity and Proportionality) — Abbreviated
- Part 3 (Risk Assessment) — Full RASP assessment, including AI system classification if applicable

The streamlined assessment must be completed within 15 business days of initiation.

---

### 5.3 DPIA for HealthPay Financial Services (Credit Scoring & Automated Decisions)

Given the elevated risk profile of automated creditworthiness assessments and the potential for significant economic impact on data subjects, the following enhanced DPIA requirements apply to all HealthPay models that produce automated decisions:

**5.3.1 SR 11-7 Alignment**
While DPIAs serve a distinct regulatory purpose, the risk assessment methodologies shall incorporate model risk concepts aligned with SR 11-7. The DPIA for HealthPay models must address:
- Conceptual soundness of the model's methodology
- Ongoing monitoring and validation procedures
- Governance and controls
- Documentation standards
- Outcomes analysis, including disproportionality testing across protected demographic categories

**5.3.2 Specific Risk Scenarios**
The DPIA for HealthPay automated decisions must specifically address:
- Risk of inaccurate credit denial (false negative impact)
- Risk of predatory inclusion (false positive approval leading to unsustainable debt)
- Risk of proxy discrimination through correlated variables
- Risk of data staleness in training sets leading to systematic bias

---

### 5.4 DPIA Review and Approval Workflow

```
[Draft Complete] → AIAO Peer Review → System Owner Addresses Comments
                                        ↓
                              DPO Review (Section 5.4.1)
                                        ↓
                ┌───────────────────────┴───────────────────────┐
                ↓                                               ↓
    [Residual Risk ≤ Medium]                      [Residual Risk ≥ High]
                ↓                                               ↓
      AIAO Approval                                        Legal Review
     (S. Lim signs)                                    (M. Gonzalez reviews)
                ↓                                               ↓
       DPO Final Sign-off                             DPO and GC jointly
                ↓                                      determine if DPO must
        Processing May Commence                        consult supervisory
                                                       authority (Section 5.5)
```

#### 5.4.1 DPO Review Criteria
Dr. Weber (or delegate) shall review each DPIA and assess:
- Completeness of the description against this SOP's Part 1 requirements
- Adequacy of the proportionality justification
- Appropriate application of the RASP methodology
- Plausibility and completeness of risk identification
- Effectiveness of proposed mitigation measures
- Integration of FRIA elements for high-risk AI systems
- Compliance with Article 27 documentation requirements

Review must be completed within 10 business days of DPIA submission to DPO.

---

### 5.5 Regulatory Consultation

If the DPIA identifies residual risks that cannot be mitigated to an acceptable level (RASP ≥ 15 after all feasible mitigation), the DPO shall prepare a consultation submission to the competent supervisory authority.

| Office | Supervisory Authority | DPO Notification Timeline |
|--------|----------------------|---------------------------|
| Berlin | Berliner Beauftragte für Datenschutz und Informationsfreiheit | Within 30 days of DPIA conclusion |
| Other EU locations | Per local supervisory authority directory | Within 30 days of DPIA conclusion |

The consultation dossier shall include:
- Meridian's DPIA (redacted where legally protected)
- Risk assessment methodology
- Proposed residual risk acceptance rationale (if seeking acceptance) or remediation plan with time-bound milestones
- AI Act conformity assessment documentation (if applicable)

No processing shall commence until the supervisory authority provides written response or the statutory consultation period expires without objection.

---

### 5.6 Documentation Standards

**5.6.1 DPIA Content Requirements**
Every completed DPIA shall:
- Be stored in Archer in a non-editable format (PDF/A) upon approval
- Include the full audit trail of reviews, revisions, and approvals
- Contain version-controlled data flow diagrams (exported from LeanIX)
- Include evidence of all processor agreements (uploaded from Vendor Management system)
- Be date-stamped with all review dates
- Carry the digital signatures/approvals of all approvers in the RACI matrix

**5.6.2 EU AI Act Documentation (Articles 11 and 18)**
For high-risk AI systems, Meridian shall maintain as part of or alongside the DPIA:
- Technical documentation per Annex IV of the EU AI Act (detailed technical specifications)
- Instructions for use per Article 13(3)
- Declaration of conformity per Article 16
- CE marking documentation per Article 16
- Quality management system documentation per Article 17
- Logs automatically generated per Article 12 (retained for a period appropriate to the intended purpose of the system, minimum 6 months)

---

### 5.7 DPIA Validation and Effectiveness Review

Within 90 days of system deployment, the AIAO shall conduct a DPIA validation review that assesses:
- Whether the processing as operated matches the processing as described in the DPIA
- Whether the identified risks have materialized
- Whether the implemented mitigation measures are operating effectively
- Whether any new risks have emerged

The validation review shall be documented in Archer as an amendment to the original DPIA.

---

### 5.8 DPIA Periodic Review Cycle

| Processing Risk Level | Review Frequency | Trigger |
|-----------------------|------------------|---------|
| High-Risk AI System (Annex III) | Every 12 months | Next review date specified in DPIA |
| RASP Score ≥ 15 | Every 12 months | Next review date specified in DPIA |
| RASP Score 10-14 | Every 18 months | Next review date specified in DPIA |
| RASP Score 5-9 | Every 24 months | Next review date specified in DPIA |
| Any processing | Within 30 days of a data breach or significant incident | Incident response trigger (SOP-SEC-003) |
| Any processing | Within 60 days of regulatory change | Regulatory monitoring trigger |

The AIAO maintains a DPIA review calendar and sends automated reminders via Archer 30 days and 14 days before each review due date.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Applicable To | Validation Method |
|------------|---------------------|---------------|-------------------|
| TC-001 | AES-256 encryption at rest for all personal data stores | All Meridian data platforms | Quarterly vulnerability assessment (CISO) |
| TC-002 | TLS 1.3 encryption in transit for all data transmissions | All Meridian APIs and services | Automated certificate monitoring (CISO) |
| TC-003 | Attribute-based access control (ABAC) for clinical data stores | Clinical AI Platform | Monthly access review (System Owner + CISO) |
| TC-004 | Automated logging per Article 12 of EU AI Act | All high-risk AI systems | Log completeness review every 90 days (AIAO) |
| TC-005 | Data minimization enforcement — automated retention schedule | All Meridian data platforms | Quarterly compliance scan (CISO) |
| TC-006 | Input data quality verification pipeline | Clinical AI Platform, MedInsight | Pre-processing validation reports (Data Science Lead) |
| TC-007 | Explainability module (LIME/SHAP output) integrated into clinical AI dashboard | Clinical AI Platform (CE-marked products) | User acceptance testing per release cycle |
| TC-008 | Automated bias detection for protected attribute proxies | HealthPay, MedInsight | Monthly bias report (AIAO review) |
| TC-009 | Anomaly detection for AI model output drift | All AI systems | Real-time monitoring dashboard (MLOps team) |
| TC-010 | Kill-switch capability for high-risk AI systems (instant model output halt) | Clinical AI Platform, HealthPay | Quarterly failover drill (Engineering Lead + CISO) |

### 6.2 Administrative Controls

| Control ID | Control Description | Frequency | Responsible |
|------------|---------------------|-----------|-------------|
| AC-001 | DPIA completeness audit (independent sampling) | Quarterly | Internal Audit |
| AC-002 | FRIA documentation spot-check for high-risk AI systems | Monthly | AIAO (S. Lim) |
| AC-003 | Processor DPIA review (vendor-provided DPIAs) | Upon contract, annually thereafter | Vendor Management + AIAO |
| AC-004 | AI Governance Committee review of DPIA compliance metrics | Quarterly | AI Governance Committee |
| AC-005 | Human oversight personnel competency verification | Semi-annually | Business Unit VP + AIAO |
| AC-006 | DPIA methodology effectiveness review (this SOP's cycle) | Per SOP metadata (next review 2027-06-19) | DPO (Dr. Weber) |

### 6.3 Human Oversight Controls (EU AI Act, Article 14)

For each high-risk AI system, the DPIA must document the specific implementation of the following mandatory human oversight controls:

| Control ID | Oversight Mechanism | Measurement |
|------------|---------------------|-------------|
| HO-001 | Qualified human-in-the-loop for all clinical diagnostic outputs | Review rate ≥ 100% (every output reviewed before clinical use) |
| HO-002 | Override capability for automated credit denial | Override available to designated credit review officers 24/7 |
| HO-003 | Interpretability dashboard accessible to human overseers | Dashboard uptime ≥ 99.9% |
| HO-004 | Mandated cool-off period for model output reliance | 24-hour review window for non-urgent adverse decisions |
| HO-005 | Bias concern escalation mechanism | Any overseer can flag for immediate AIAO review; review completed within 48 hours |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | Metric | Target | Measurement Method | Reporting Cadence |
|--------|--------|--------|-------------------|-------------------|
| KPI-01 | DPIA completion rate (trigger to DPO approval within SLA) | ≥ 95% | Archer workflow analytics | Monthly (AIAO to DPO) |
| KPI-02 | DPIA timeliness: Days from mandatory DPIA trigger to approval | ≤ 40 business days for Full; ≤ 20 business days for Streamlined | Archer timestamp delta | Quarterly (DPO to AI Governance Committee) |
| KPI-03 | DPIA overdue review rate | 0 overdue at any time | Archer review calendar vs. completion status | Monthly (AIAO) |
| KPI-04 | RASP residual risk ≥ 15 after mitigation (requiring regulatory notification) | Cases tracked | Archer DPIA records | Per occurrence (DPO to C-Suite) |
| KPI-05 | DPIA validation review completion within 90 days of deployment | ≥ 90% | Archer DPIA records | Quarterly (AIAO) |
| KPI-06 | High-risk AI system classification accuracy (false classifications) | 0 miscategorized systems | AI system inventory vs. independent audit sampling | Semi-annually (AIAO + Internal Audit) |
| KPI-07 | Bias detection trigger events per system per month | Tracked per system | Bias detection pipeline (TC-008) output | Monthly (AIAO) |
| KPI-08 | Human oversight intervention frequency (overrides/contradictions of AI output) | Tracked per system | Human oversight logs (HO controls) | Monthly (System Owner to AIAO) |

### 7.2 Reporting Dashboards

**DPIA Operational Dashboard (Archer)**
Accessible to: DPO, AIAO, Business Unit VPs, CISO
Refresh rate: Real-time
Displays:
- All active DPIAs with status (Draft, In Review, Approved, Overdue Review)
- DPIA pipeline: triggers identified vs. DPIAs initiated
- SLA compliance visualization (green/yellow/red)
- RASP heat map across all active DPIAs
- High-risk AI system register with linked DPIA/FRIA records

**AI Governance Committee Quarterly Report**
Prepared by: AIAO (S. Lim)
Contents:
- DPIA volume metrics (new, completed, overdue review)
- RASP score trends (are residual risks improving?)
- FRIA coverage completeness metrics
- Regulatory notification and consultation status (Section 5.5)
- Human oversight effectiveness (KPI-08 analysis)
- Exception report (all active exceptions under Section 8)
- AI system classification register (Annex III classification status for all AI systems)

### 7.3 Annual DPIA Program Effectiveness Review
The DPO shall commission an independent review of the DPIA program, conducted by an external qualified assessor, at intervals not exceeding 24 months. The review shall assess:
- DPIA methodology adequacy against evolving regulatory expectations
- Effectiveness of DPIA risk mitigation outcomes
- Integration with AI governance frameworks
- Recommendations for this SOP's revision

Results shall be presented to the AI Governance Committee and the Board-level Risk Committee.

---

## 8. Exception Handling and Escalation

### 8.1 Exception to DPIA Requirement

A Business Unit VP may request an exception to the requirement to conduct a DPIA for a processing activity that scored ≥ 15 on the threshold assessment. Exception requests shall be submitted in writing to the DPO and General Counsel using the Exception Request Form (Archer Form EXC-F-001).

The request must articulate:
- The specific processing activity for which exception is sought
- The compelling business justification for proceeding without a complete DPIA
- The alternative risk assessment measures that will substitute for the DPIA
- The specific time period for which the exception applies

### 8.2 Exception Approval Authority

| Exception Scope | Approval Required |
|-----------------|-------------------|
| Delay DPIA completion by ≤ 15 business days | AIAO (S. Lim) |
| Delay DPIA completion by 16-30 business days | DPO (Dr. Weber) |
| Exempt specific data element from DPIA scope | DPO + General Counsel (M. Gonzalez) jointly |
| Fully exempt a processing activity from DPIA | General Counsel ONLY (DPO must be consulted; DPO veto authority applies) |

No exception may extend beyond 90 calendar days. Permanent exemptions are prohibited.

### 8.3 Escalation Procedures

| Escalation Trigger | Escalation Path | Response Time |
|--------------------|-----------------|---------------|
| Risk identified during DPIA execution with RASP ≥ 20 (Critical) | AIAO → DPO same business day → DPO escalates to General Counsel and supervisory authority if unmitigatable | Immediate stop-processing order within 4 hours; DPO consultation within 24 hours |
| DPIA SLA breach (approval not achieved within mandated timeline) | AIAO → DPO → Business Unit VP | AIAO notifies DPO within 1 business day; DPO notifies BU VP within 2 business days with remediation directive |
| Suspected prohibited AI practice (Article 5, EU AI Act) | Any employee → DPO and General Counsel directly (anonymous reporting channel available via Meridian Ethics Hotline) | Acknowledgment within 24 hours; investigation launched within 3 business days |
| Material change to processing not reflected in DPIA (inadequate DPIA maintenance) | AIAO audits detection or System Owner identification → AIAO notifies DPO | DPIA amendment initiated within 5 business days |
| Processor DPIA non-delivery (vendor fails to provide DPIA within 30 days of request) | AIAO → DPO → Vendor Management (for contractual enforcement) | Escalation to Vendor Management within 5 business days of deadline |

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum

| Target Audience | Training Module | Initial Duration | Refresher Frequency | Delivery Method | Tracking System |
|-----------------|-----------------|------------------|---------------------|-----------------|-----------------|
| All Meridian employees | "Introduction to Data Protection at Meridian" (Module PRIV-100) | 45 minutes | Annually | Workday Learning | Workday |
| System Owners, Engineering Leads, Data Science Leads | "DPIA Execution and System Owner Responsibilities" (Module PRIV-DPIA-200) | 4 hours | Annually | Instructor-led (virtual or in-person) + practical DPIA exercise | Workday + practical exercise scored by AIAO |
| AIAO, DPO office staff | "Advanced DPIA Methodology and EU AI Act Integration" (Module PRIV-DPIA-300) | 16 hours (2-day intensive) | Semi-annually updates quarterly | External certified training provider | Certificate tracked in Workday |
| Business Unit VPs, Directors | "DPIA Governance and Risk Acceptance for Leadership" (Module PRIV-DPIA-LDR) | 2 hours | Annually | Executive briefing (DPO delivery) | Attendance tracked by DPO office |
| CISO team participating in DPIAs | "Technical Control Validation in DPIA Context" (Module PRIV-DPIA-TECH) | 3 hours | Annually | Technical workshop (CISO + AIAO co-delivery) | Workday |
| Human Oversight Personnel (clinical reviewers, credit review officers) | "Human Oversight of AI Systems: Operational Procedures" (Module AI-OVERSIGHT-100) | 6 hours initial + 2 hours quarterly update | Quarterly update | Instructor-led + supervised practical sessions | Competency verification tracked; overseers who fail verification are removed from oversight rosters until retrained |

### 9.2 Training Effectiveness Measurement
- Module PRIV-DPIA-200: System Owners must complete a scored practical DPIA exercise (pass threshold ≥ 85%) within 30 days of training. Failure requires retraining within 15 days.
- Module PRIV-DPIA-300: DPIA team must pass a certification assessment annually.
- Module AI-OVERSIGHT-100: Quarterly competency assessment via supervised case review. Failure triggers removal from oversight duties and mandatory retraining.

### 9.3 Training Compliance Reporting
The DPO office shall report training compliance rates quarterly to the AI Governance Committee. A compliance rate below 90% for any required audience triggers a remediation plan with escalation to the relevant Business Unit VP.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship to This SOP |
|--------|-------|--------------------------|
| SOP-DGP-001 | Data Classification and Handling Policy | Defines data classification levels referenced in DPIA risk scoring |
| SOP-DGP-003 | International Data Transfer Procedure | Governs SCCs and transfer impact assessments that may be attached to DPIAs |
| SOP-DGP-004 | Vendor Data Protection Assessment | Processor assessment procedure; processors identified in DPIAs must have current assessments per this SOP |
| SOP-DGP-009 | Regulatory Notification and Breach Response | Governs supervisory authority notifications referenced in Section 5.5 of this SOP |
| SOP-SEC-003 | Information Security Incident Response | Incident response triggers that may initiate DPIA review per Section 5.8 of this SOP |
| SOP-MLOPS-001 | AI Model Development Lifecycle | Covers model risk assessment registry (MLOPS-REG-001) entries that must cross-reference DPIA records |
| SOP-MLOPS-004 | Model Bias Detection and Mitigation | Details bias detection pipeline that feeds DPIA risk assessment for AI systems |
| SOP-COMP-001 | Compliance Risk Management Framework | Enterprise risk appetite statements that inform residual risk acceptance decisions |
| SOP-VND-002 | Third-Party Vendor Onboarding and Due Diligence | Vendor DPIA requirements triggered during procurement |

### 10.2 External Regulatory References

| Document | Reference |
|----------|-----------|
| Regulation (EU) 2016/679 (General Data Protection Regulation) | Articles 35, 36 (DPIA and prior consultation) |
| Regulation (EU) 2024/1689 (Artificial Intelligence Act) | Articles 5 (Prohibited Practices), 10 (Data Governance), 11 (Technical Documentation), 12 (Record-Keeping), 13 (Transparency), 14 (Human Oversight), 15 (Accuracy, Robustness, Cybersecurity), 16 (CE Marking, Declaration of Conformity), 17 (Quality Management System), 18 (Documentation Retention), 27 (Fundamental Rights Impact Assessment), Annex III (High-Risk Classification), Annex IV (Technical Documentation) |
| Federal Reserve SR 11-7 (Model Risk Management) | Model validation and governance standards for HealthPay credit models |
| NIST AI RMF 1.0 (AI Risk Management Framework) | Govern, Map, Measure, Manage functions integrated into RASP methodology |
| ISO/IEC 27001:2022 | Information security controls validation framework |
| HITRUST CSF v11 | Control validation framework for PHI-related systems |

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
|---------|------|--------|----------|---------------------|
| 1.0 | 2019-04-03 | Dr. Klaus Weber | Maria Gonzalez | Initial publication. Established basic DPIA methodology per GDPR Article 35. Scope limited to EU operations. |
| 2.0 | 2021-08-15 | Dr. Klaus Weber | Maria Gonzalez | Major revision. Expanded scope to all Meridian global operations. Introduced RASP quantitative methodology. Added health data specific risk dimensions for Clinical AI Platform. Incorporated HITRUST control references. |
| 2.1 | 2022-01-22 | Sandra Lim (AIAO) | Dr. Klaus Weber | Minor revision. Added MLOps integration references (SOP-MLOPS-001). Clarified System Owner responsibilities for LeanIX data flow diagrams. |
| 3.0 | 2023-11-01 | Dr. Klaus Weber | Maria Gonzalez | Major revision. Complete DPIA methodology overhaul to integrate EU AI Act requirements (FRIA integration). Added Section 5.1.3 (AI System Concurrent Classification). Expanded Section 6 (Controls) for AI-specific safeguards. Added Section 6.3 (Human Oversight Controls). Introduced AIAO role. Updated RACI matrix. Extended DPIA execution timeline from 20 to 40 business days to accommodate AI Act assessment depth. |
| 3.1 | 2024-01-30 | Sandra Lim | Dr. Klaus Weber | Minor revision. Corrected AI system classification references to adopted EU AI Act (Regulation 2024/1689). Added Article 5 prohibition policy statement (Section 4.7). Added escalation procedure for suspected prohibited practices. Updated training modules (AI-OVERSIGHT-100). |
| 3.2 | 2024-04-12 | Dr. Klaus Weber | Maria Gonzalez | Minor revision. Updated to reflect CE marking under EU MDR obtained for clinical AI products. Added HealthPay-specific DPIA enhancements (Section 5.3). Aligned HealthPay model risk concepts with SR 11-7. Added KPI-07 and KPI-08 for bias and human oversight tracking. |
| 3.3 | 2024-08-05 | Sandra Lim | Dr. Klaus Weber | Minor revision. Updated DPIA validation review timeline from 180 days to 90 days (Section 5.7). Added external DPIA program effectiveness review requirement (Section 7.3). Refined exception handling SLA response times. Clarified kill-switch drill frequency (TC-010). |
| 3.4 | 2025-02-14 | Dr. Klaus Weber | Maria Gonzalez | Minor revision. Effective date updated post-regulatory alignment. Minor corrections to RASP scoring examples. Updated vendor DPIA reference to SOP-VND-002 v2.1. Training module version numbers updated. |
| 3.5 | 2025-11-12 | Dr. Klaus Weber | Maria Gonzalez | Current version. Comprehensive review and update. Enhanced EU AI Act Article 27 FRIA integration procedures (Section 5.2.2 Part E). Updated for Meridian's expanded AI system inventory. Clarified combined DPIA/FRIA template usage. Updated Archer form references. Added detailed prohibited AI practices policy (Section 4.7). Updated Section 10 cross-references to current SOP versions. Revised review frequency table (Section 5.8). Training curriculum alignment. Next review scheduled for 2027-06-19. |

---

**END OF DOCUMENT**

© 2025 Meridian Health Technologies, Inc. | Classification: Internal | SOP-DGP-007 v3.5
This document is proprietary and confidential. Unauthorized reproduction, distribution, or disclosure is prohibited.