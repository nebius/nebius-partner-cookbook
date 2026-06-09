---
sop_id: "SOP-AIML-008"
title: "AI System Risk Classification"
business_unit: "AI/ML Engineering"
version: "4.1"
effective_date: "2025-11-17"
last_reviewed: "2026-12-25"
next_review: "2027-06-08"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: AI System Risk Classification

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the formal framework, criteria, and process for classifying all Artificial Intelligence (AI) and Machine Learning (ML) systems developed, deployed, acquired, or modified by Meridian Health Technologies, Inc. ("Meridian"). The purpose of this classification framework is to:

1.  **Ensure Regulatory Compliance:** Systematically identify AI systems subject to specific regulatory obligations, particularly the European Union's Artificial Intelligence Act (EU AI Act) and its classification tiers, as well as applicable U.S. federal guidance, including SR 11-7.
2.  **Implement Risk-Proportional Controls:** Apply governance, oversight, technical, and documentation controls commensurate with the level of risk and regulatory scrutiny a system presents to patients, payers, providers, and Meridian's operations.
3.  **Operationalize the NIST AI Risk Management Framework (RMF):** Provide a structured mechanism for executing the Map function of the NIST AI RMF by ensuring all AI systems are inventoried and categorized according to their risk profile, thereby informing the Measure and Manage functions.
4.  **Provide Clarity and Consistency:** Furnish a single, authoritative methodology for AI/ML Engineering, Product Management, Legal, and Compliance teams to determine the initial and ongoing risk classification of an AI system throughout its lifecycle.

### 1.2 Scope

This SOP applies to all AI systems, defined herein, that are developed, procured, or substantially modified by any business unit, department, or subsidiary of Meridian Health Technologies, Inc. The scope encompasses:

- **All Development Lifecycle Phases:** From initial research and ideation through design, development, validation, deployment, post-market monitoring, and decommissioning.
- **Internally Developed and Third-Party Systems:** Including commercial off-the-shelf (COTS) software with AI components, embedded AI in medical devices, software as a service (SaaS) incorporating ML models, and open-source models fine-tuned on proprietary data.
- **All Business Units:** Including but not limited to Clinical AI (Clara MedSuite), Diagnostics Imaging (NeuroSight), Revenue Cycle Management (ClaimPredict), and Corporate Operations (HR TalentMatch).
- **All Deployment Geographies:** Systems marketed or deployed in the European Union, the United States, and any other global market are subject to this SOP. Where regulatory requirements conflict, the most stringent requirement shall prevail.
- **Meridian Personnel and Contractors:** All full-time employees, part-time employees, interns, consultants, and third-party vendors who design, develop, test, deploy, procure, or manage AI systems.

This SOP does **not** cover:
- Basic statistical models or rules-based systems that do not learn from data (e.g., linear regression used for simple trend analysis, deterministic Expert Systems with no ML inference).
- Legacy software products without AI components as of the effective date of this SOP, unless such products undergo a material modification that introduces an AI-based feature.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
| :--- | :--- |
| **AI System** | A machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments. |
| **General-Purpose AI (GPAI) Model** | An AI model, including when trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks regardless of the way the model is placed on the market, including as open-source software. |
| **High-Risk AI System** | An AI system that is classified as posing a high risk to the health, safety, or fundamental rights of natural persons, as defined by the EU AI Act, Annex III, and detailed in this SOP. |
| **Limited Risk AI System** | An AI system that poses a risk of manipulation, impersonation, or deception, such as chatbots or emotion recognition systems, subject to specific transparency obligations under the EU AI Act. |
| **Minimal/No Risk AI System** | An AI system that does not fall into the prohibited, high-risk, or limited risk categories. The vast majority of AI systems currently fall under this category, e.g., AI-enabled video games or spam filters. |
| **Conformity Assessment** | The process demonstrating whether the specific requirements relating to a high-risk AI system have been fulfilled, as described in Article 43 of the EU AI Act. |
| **Substantial Modification** | A change to the AI system after its initial placing on the market or putting into service which is not foreseen in the initial risk classification and which affects the compliance of the AI system with its original regulatory obligations or results in a material change to its intended purpose. |
| **Intended Purpose** | The use for which an AI system is intended by the provider, including the specific context and conditions of use, as specified in the information supplied by the provider on the label, in the instructions for use, or in other promotional or sales materials or statements. |

### 2.2 Acronyms

| Acronym | Definition |
| :--- | :--- |
| **AI** | Artificial Intelligence |
| **AIML** | AI/ML Engineering Business Unit |
| **CIO** | Chief Information Officer |
| **CAO** | Chief AI Officer (Dr. Marcus Rivera) |
| **DPO** | Data Protection Officer |
| **EU** | European Union |
| **FTE** | Full-Time Equivalent |
| **GRC** | Governance, Risk, and Compliance Team |
| **GPAI** | General-Purpose AI |
| **KPI** | Key Performance Indicator |
| **ML** | Machine Learning |
| **MDR** | EU Medical Device Regulation (2017/745) |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RMF** | NIST AI Risk Management Framework |
| **SOP** | Standard Operating Procedure |
| **VP** | Vice President |

---

## 3. Roles and Responsibilities

The following RACI matrix delineates the roles and responsibilities for executing this SOP. These roles are accountable to the CAO for all AI risk classification matters.

| Role | Responsibility | RACI Code |
| :--- | :--- | :--- |
| **AI/ML Product Manager** | Initiates the risk classification process for new AI systems or modifications. Defines the system's intended purpose and use context. | R |
| **AI/ML Engineering Lead** | Performs the technical assessment, maps system capabilities to Annex III use cases, and completes the `AIML-008-FORM-1` (Risk Classification Worksheet). | R |
| **GRC Lead (AIML)** | Independent review and validation of the proposed risk classification. Ensures alignment with Article 6 and Annex III interpretations. Manages the risk registry. | R |
| **Legal Counsel (Regulatory)** | Provides binding interpretation of the EU AI Act and other relevant regulations. Approves the final classification for any system involving a borderline or ambiguous use case. | C |
| **Chief AI Officer (CAO)** | Approves the final risk classification for all High-Risk systems. Owns the overall AI risk classification framework and this SOP. | A |
| **VP of Engineering** | Accountable for ensuring engineering resources and tooling are available to support the classification process. Approves the final classification for Limited and Minimal Risk systems. | A |
| **Data Protection Officer (DPO)** | Consulted on all systems processing personal or special category data to ensure alignment with GDPR and HIPAA obligations. | C |
| **Internal Audit** | Audits the risk classification process annually for consistency, completeness, and compliance. | I |

---

## 4. Policy Statements

The following high-level policy statements govern all AI system risk classification activities at Meridian.

1.  **Mandatory Classification:** No AI system shall proceed beyond the initial design phase without a formal, documented risk classification approved in accordance with this SOP. This classification is a prerequisite for accessing compute resources, obtaining security approval (SOP-SEC-112), and initiating quality management workflows.
2.  **Prohibition of Unacceptable Risk Systems:** Meridian strictly prohibits the development, deployment, or marketing of any AI system defined under Article 5 of the EU AI Act as posing an unacceptable risk. This includes systems deploying subliminal, manipulative, or deceptive techniques to materially distort behavior, systems exploiting vulnerabilities of a specific group of persons due to their age or disability, and social scoring systems.
3.  **Precautionary Principle for Annex III Classification:** Unless an AI/ML Engineering Lead provides clear, documented, and legally-reviewed evidence that an AI system does not pose a significant risk of harm to the health, safety, or fundamental rights of natural persons, any system falling under the purview of Annex III shall be classified as High-Risk. This policy prohibits a default "minimal risk" classification for borderline Annex III use cases.
4.  **Dynamic Reclassification:** A system's risk classification is not static. Any substantial modification, unexpected adverse event, post-market safety signal, or change in regulatory interpretation requires an immediate reassessment and, if necessary, reclassification within 30 calendar days.
5.  **Transparency by Design:** All AI systems classified as Limited Risk (e.g., Clara Patient Portal Chatbot) shall be designed and deployed with clear, conspicuous, and compliant user-facing disclaimers as mandated by Article 52, regardless of deployment channel.

---

## 5. Detailed Procedures

This section details the step-by-step procedure for classifying an AI system. Each step is named, and the accountable role is explicitly identified.

### 5.1 Procedure: Initial System Risk Classification (AIML-008-PROC-01)

This procedure is a prerequisite for the System Release Authorization (SOP-SEC-205) and must be completed during the "Design & Feasibility" gate of the Meridian Product Lifecycle (MPL).

**Step 1: Initiate Classification Request**
- **Actor:** AI/ML Product Manager
- **Action:** The Product Manager creates a new entry in the `AIML Systems Registry` (Jira Project: `AIML-REG`). The entry type is "Classification Request." The Manager fills out Section A of the `AIML-008-FORM-1` (Risk Classification Worksheet), which includes:
    - System Technical Name (e.g., `ClaraMedSuite-PE-v3`)
    - System Commercial Name (e.g., "Clara Pulmonary Embolism Detection")
    - Intended Purpose Statement (a verbatim draft to be reviewed by Legal)
    - Business Unit owner
    - Deployment geography (checkboxes for EU/EEA, US, Canada, Other)
- **SLA:** This step must be completed within 5 business days of the MPL "Design & Feasibility" gate opening.

**Step 2: Technical Pre-Assessment**
- **Actor:** AI/ML Engineering Lead (assigned from the `AIML-008-Classifier` Jira group)
- **Action:** The Lead reviews the Intended Purpose and performs a technical pre-assessment, completing Section B of Form-1. This assessment determines:
    - **Data Source Classification:** Does the system ingest, process, or infer outputs based on special category data as defined by Article 9 of the GDPR (e.g., patient health data, biometric data for identification)? (Yes/No)
    - **Autonomy Level:** High (outputs directly influence clinical decisions with no mandatory human review), Medium (outputs are designed to be a primary input for a qualified professional's decision), Low (outputs are purely informational or advisory with a separate, mandatory expert review loop). This is assessed on a 4-point scale based on Meridian's Internal Control Framework.
    - **System Architecture:** Is the system a standalone AI medical device software (SaMD), a sub-component of a medical device, a clinical decision support tool, a back-office operational tool, or a non-medical user-facing application?
- **SLA:** 3 business days from Step 1 completion.

**Step 3: Preliminary Article 5 and Annex III Mapping**
- **Actor:** AI/ML Engineering Lead
- **Action:** The Lead uses the `AIML-008-TL-1` (Annex III Mapping Tool) to perform a structured mapping. This is an assisted, questionnaire-based tool. The Lead completes the following mandatory questionnaire in the tool, which determines if the system's intended purpose is an exact or analogous match to one of the exhaustive list in Annex III:

    **Annex III Mapping Questionnaire (administered via AIML-008-TL-1):**
    1.  Is this system intended to be used as a safety component of a product, or is the system itself a product, governed by the Union harmonization legislation listed in Annex II, Section A? (e.g., MDR 2017/745, In Vitro Diagnostic Medical Devices Regulation 2017/746). If Yes, specify the legislation.
    2.  Does the system’s intended purpose involve the use of biometric data for the remote biometric identification of natural persons? If Yes, is it in real-time or post? Note: real-time remote biometric identification in publicly accessible spaces is likely prohibited under Article 5(1)(d) and must be escalated immediately.
    3.  Does the intended purpose fall under any of the following critical infrastructure management tasks (Annex III, Point 2)?
        - Management and operation of road traffic.
        - Management and operation of the supply of water, gas, heating, or electricity. (Meridian is unlikely to directly manage these, but AI embedded in hospital command centers might interface with such systems.)
    4.  Does the intended purpose involve determining access, eligibility, or assignment to educational or vocational training institutions, or evaluating learning outcomes (Annex III, Point 3)? This applies to Meridian's internal HR TalentMatch and externally marketed education modules for patient compliance.
    5.  Does the intended purpose involve the recruitment or selection of natural persons, making decisions on terms of a work-related relationship, task allocation, performance monitoring, or termination (Annex III, Point 4)?
    6.  Does the intended purpose involve evaluating the creditworthiness of natural persons or establishing their credit score (Annex III, Point 5)?
    7.  Does the intended purpose involve dispatching or establishing priority in the dispatching of emergency first response services, including by firefighters and emergency medical aid (Annex III, Point 6)?
    8.  Does the intended purpose involve making risk assessments or pricing in relation to life or health insurance for natural persons (Annex III, Point 7)?
    9.  Does the intended purpose involve any of the following law enforcement, migration, or border control uses? (Generally not applicable to Meridian's commercial portfolio but included for completeness in the enterprise-wide framework.)
    10. Does the intended purpose involve assisting a judicial authority in researching and interpreting facts and the law and in applying the law to a concrete set of facts (Annex III, Point 8)?
    11. Is the system a medical device AI system, under the scope of the EU MDR, and perform a function that would be considered a "use case" under Annex III, Point 1 (e.g., biometric categorization, emotion recognition), OR does the system itself pose a significant risk of harm to the health and safety, or fundamental rights of a natural person as determined by the nature of the data, autonomy level, and severity of potential harm?

- **Output:** The tool generates a Preliminary Annex III Map. If ANY question from 1-10 is answered "Yes," the system is preliminarily classified as "Presumptively High-Risk." If only question 11 is answered "Yes," a deeper dive risk assessment (Step 4) is required to determine if the "significant risk of harm" threshold is met. If no questions are answered "Yes," the system is classified as "Not Annex III."
- **SLA:** 2 business days from completion of Step 2.

**Step 4: Formal Risk Determination for "Presumptively High-Risk" and "Annex III Borderline" Systems**
- **Actor:** GRC Lead (AIML), with mandatory consultation of Legal Counsel (Regulatory) and the DPO (if special category data is involved).
- **Action:** The GRC Lead schedules and chairs a "Risk Classification Board" (RCB) meeting. The board comprises the GRC Lead, the AI/ML Engineering Lead, the Product Manager, and a representative from Legal. The board reviews the completed Form-1 and the Annex III Map. The key decision gates are:
    1.  **Article 5 Prohibition Gate:** The board confirms definitively that the system's intended purpose and functionality does not invoke any Article 5 Prohibited AI Practices. If it does, the project is immediately terminated, and a "Red File" is created and escalated to the CAO and General Counsel.
    2.  **Article 6(1) Classification Gate:** If classified under any of the Annex III use cases (Points 1-8), the board confirms the system is a **High-Risk AI System**. A "Significant Harm Determination" document is drafted if the classification relies solely on Point 1 or 11 of Annex III.
    3.  **Article 6(3) Derogation Gate:** The board assesses if, despite being in an Annex III category, the system does NOT pose a significant risk of harm to the health, safety, or fundamental rights of natural persons, including by not materially influencing the decision-making outcome. This is a high-evidentiary bar assessment requiring documented proof. Derogation is not applicable if the system profiles natural persons.
    4.  **GPAI Tiering Gate:** If the system incorporates a General-Purpose AI model, the board determines whether the model constitutes a "GPAI with systemic risk" under Article 51. This is based on cumulative compute used for training (beyond 10^25 FLOPs), with a presumption of systemic risk. Meridian's `NeuroSight-Foundation-v2` is currently the only GPAI model in scope that has been evaluated under this criterion.

- **Final Decision:** The RCB's final classification (Prohibited, High-Risk, or Not High-Risk) is documented in the meeting minutes and recorded in the Jira ticket `AIML-REG-####`.
- **SLA:** The RCB must be convened and a decision rendered within 10 business days of Step 3 completion.

**Step 5: Limited and Minimal Risk Classification**
- **Actor:** GRC Lead (AIML)
- **Action:** For systems not falling under Article 5 or Article 6, the GRC Lead classifies them according to Title IV (Transparency Obligations).

    **Decision Tree for Non-High-Risk Systems:**
    - **Is the system a chatbot or an AI system intended to interact directly with natural persons?**
        - Yes → Tag as **Limited Risk: Transparency (Art. 52(1))** . Engineering must ensure deployment architecture allows for clear disclosure.
        - No → Proceed to next check.
    - **Is the system an emotion recognition system or a biometric categorization system?**
        - Yes → Tag as **Limited Risk: Transparency (Art. 52(2) & (3))** . This triggers specific UI/UX design mandates from Legal.
        - No → Proceed to next check.
    - **Does the system generate or manipulate image, audio, or video content that constitutes a "deep fake"?**
        - Yes → Tag as **Limited Risk: Transparency (Art. 52(4))** . The output file metadata must be permanently and audibly/visibly marked.
        - No → Classify as **Minimal/No Risk**. No specific EU AI Act obligations beyond Meridian's internal engineering standards (SOP-SEC-110).

**Step 6: Formal Approval and Registration**
- **Actor:** Final Approver, per the RACI.
    - **High-Risk Systems:** Dr. Marcus Rivera, Chief AI Officer.
    - **Limited and Minimal Risk Systems:** David Park, VP of Engineering (or delegate).
- **Action:** The approved classification ticket `AIML-REG-####` is closed, and its metadata is programmatically synced with the central AI Risk Registry in the GRC Archer platform. A unique `AI_SYSTEM_ID` is generated and linked to the system's Confluence documentation space and Jira Epic.
- **SLA:** 2 business days from Step 4 or Step 5 completion.

### 5.2 Procedure: Trigger-Based Reclassification (AIML-008-PROC-02)

An AI system's risk classification is dynamic. Any of the following triggers shall initiate this procedure.

**Reclassification Triggers:**
1.  **Substantial Modification (Article 43(4)):** A material change to the model's architecture, training data distribution, or intended purpose.
2.  **Regulatory Change:** An update to the EU AI Act, an Implementing Act, or a binding regulatory guidance from an authority (e.g., FDA, Notified Body) that impacts the classification rationale.
3.  **Adverse Event / Post-Market Signal:** An incident reported via the Meridian Incident Response (SOP-IR-045) involving potential psychological, financial, or physical harm.
4.  **Internal Audit Finding:** A formal finding by Internal Audit or an external auditor questioning the accuracy or documentation of the current classification.
5.  **Annual Mandatory Review:** As part of the Annual AI System Review (see Section 7.3).

**Reclassification Procedure:**

1.  **Event Trigger:** The GRC Lead is notified of a trigger via a Jira escalation or the annual review schedule.
2.  **Scope Determination:** The GRC Lead and the original AI/ML Engineering Lead determine if the trigger warrants a full reassessment (restarting from Procedure 5.1, Step 2) or a targeted review.
3.  **Targeted Review:** For a targeted review (e.g., a minor regulatory guidance update), the GRC Lead updates the existing `AIML-008-FORM-1` and `AIML-008-TL-1` output in the AIML Systems Registry.
4.  **Re-Approval:** The updated classification follows the same approval flow as the original, up to the CAO if the system remains High-Risk or changes tier.
5.  **Conformity Assessment Impact:** If a High-Risk system is reclassified or undergoes a substantial modification, the Conformity Assessment file (SOP-RA-201) is flagged for re-assessment within 30 days.

---

## 6. Controls and Safeguards

The following administrative and technical controls are mandatory to ensure the integrity and consistency of the risk classification process.

### 6.1 Administrative Controls

- **A-01: Four-Eyes Principle:** No classification, whether High-Risk or Minimal, shall be completed by a single individual. The initial assessment by the AI/ML Engineering Lead is always independently reviewed by the GRC Lead.
- **A-02: Mandatory Legal Consultation for High-Risk Systems:** For any system initially classified as High-Risk or any classification relying on Article 6(3) derogation, consultation with Legal Counsel (Regulatory) is mandatory and documented.
- **A-03: Classification Freeze:** Once a classification is approved, it cannot be changed without traversing the full reclassification procedure (AIML-008-PROC-02). The `status` field in the Jira `AIML-REG` project and the GRC Archer platform are immutable except through a controlled workflow transition.
- **A-04: Audit Trail Integrity:** Every data field change in the `AIML-008-FORM-1` and the Annex III Mapping Tool must be logged with a timestamp and user ID in a system of record (Jira/Archer). No changes shall be made outside of this audited environment.

### 6.2 Technical Controls

- **T-01: AIML Systems Registry (Jira):** All classification workflows are managed in a dedicated, schema-locked Jira project. Custom fields (`intended_purpose`, `annex_iii_map`, `risk_tier`) are mandatory and configured with validators that mirror the logic of Procedure 5.1.
- **T-02: Automated Annex III Mapping Tool (AIML-008-TL-1):** A containerized internal application that guides the Engineering Lead through the Annex III questionnaire. The tool prevents classification as "Minimal Risk" unless all Annex III questions are answered "No" and legally attested.
- **T-03: Integration Gateway with Archer GRC:** A nightly, automated middleware job (`AIML-Archer-Sync`) reconciles the status of all `High` and `Critical` risk tier systems in the Jira Registry with the Master Risk Register in Archer. Any mismatch creates an automatic ticket in the `GRC` Jira queue.
- **T-04: Model Card Guardrail:** The Model Card Generator (SOP-AIML-012) is configured to reject any input where the `AIML_SYSTEM_ID` does not match a completed and approved `risk_tier` in the AIML Systems Registry. This prevents unclassified systems from accessing documented, approved deployment pathways.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The effectiveness and efficiency of this SOP are measured by the following KPIs, which are monitored by the AIML GRC Lead and reported to the CAO monthly.

| KPI | Description | Target | Measurement Tool |
| :--- | :--- | :--- | :--- |
| **Classification Cycle Time** | Mean time from Step 1 initiation to final approval (Step 6), measured in business days. | < 25 business days | Jira `AIML-REG` dashboard |
| **Registry Coverage** | Percentage of active AIML engineering projects mapped by a unique `AIML_SYSTEM_ID` in the registry. | 100% | Jira `AIML-REG` vs. internal repos |
| **High-Risk Overdue Re-Assessments** | Number of High-Risk systems where the mandatory annual review is past due by more than 30 days. | 0 | Archer GRC Platform, Assessment Plan module |
| **Classification Reversal Rate** | The percentage of final classifications that are overturned or materially changed within 12 months of approval. | < 5% | AIML-008-FORM-1 change log |
| **NIST RMF MAP Coverage** | Percentage of inventoried AI systems with a completed and approved risk profile, contributing to the MAP function. | 95% | GRC Archer Platform |

### 7.2 Operational Dashboards

Two primary operational dashboards support this SOP, accessible via the `AIML Executive Hub` Confluence page.

1.  **Risk Classification Funnel:** A real-time Jira-based dashboard designed for the GRC team. It visualizes all `AIML-REG` tickets by their workflow stage (Initiation, Pre-Assessment, RCB Review, Pending Approval, Approved). It highlights bottlenecks and tickets breaching the defined SLAs.
2.  **AI System Portfolio Risk Map:** An Archer-powered dashboard for the CAO and VP of Engineering. It displays a bubble-chart view of the entire AI portfolio, where each bubble is an AI system. X-axis is the deployment geography (EU, US, Global, etc.), Y-axis is the risk tier (Prohibited, High, Limited, Minimal). Bubble size is proportional to the estimated revenue impact. This provides a single-pane-of-glass view of regulatory concentration risk.

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Content |
| :--- | :--- | :--- | :--- |
| **AI Risk Portfolio Status** | Chief AI Officer, VP Engineering | Monthly | Summary of classifications, aging tickets, KPI dashboard, any Article 5 escalations. |
| **Annual AI System Review** | System Owners (AI/ML Product Mgrs) | Annually | Triggered automatically from Archer. Owner must re-validate the `Intended Purpose` and confirm no unreported substantial modifications. Non-response is escalated. |
| **SOP Compliance Audit** | Internal Audit | Annually | Full audit of the process, a sample of 10% of all classified systems, and a review of procedure adherence against mandatory controls. |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling

Deviations from the mandated procedure timelines or control execution are considered exceptions. No exceptions to the core classification definitions (e.g., classifying an Annex III system as Minimal Risk) are permitted.

**Process for an Operational Exception (e.g., missing an SLA due to personnel absence):**

1.  **Exception Request:** The AI/ML Engineering Lead creates a Jira ticket of type `Exception`, linked to the parent `AIML-REG` ticket. The request must document the specific procedure step being deviated from, the justification, and a proposed mitigation plan with a concrete closure date.
2.  **Technical Review:** The GRC Lead (AIML) reviews the operational justification and risk of the exception.
3.  **Approval Authority:**
    - **Minor Exceptions** (SLA extension of < 10 days): Approvable by the GRC Lead.
    - **Major Exceptions** (any deviation from the RCB process or approval authority chain): Must be approved by the CAO, Dr. Marcus Rivera.
4.  **Closure:** The `Exception` ticket must be resolved by the agreed-upon closure date. An open exception past its due date is automatically escalated.

### 8.2 Escalation Path

The following hierarchical escalation path is to be followed when a high-risk classification or a prohibited practice is identified and the individual or team responsible is non-responsive.

1.  **Level 1: Direct Management.** The AI/ML Engineering Lead and Product Manager are the first point of escalation for non-responsiveness.
2.  **Level 2: Functional Leadership.** For unresolved issues, the matter is escalated to the Director of AIML Engineering and relevant Legal Counsel.
3.  **Level 3: Executive Leadership.** Any confirmed, actual, or suspected instance of unauthorized development or deployment of an Article 5 Prohibited Practice AI System, or the deliberate misclassification of an Article 6 High-Risk system, is directly and immediately escalated by the GRC Lead directly to the Chief AI Officer (Dr. Marcus Rivera) and the General Counsel. This is a "Stop the Line" event.

---

## 9. Training Requirements

### 9.1 Required Training Modules

All personnel in scope (Section 1.2) must complete the following training. Completion is tracked in Meridian's `Litmos` Learning Management System.

| Training Module ID | Name | Description | Target Audience | Frequency |
| :--- | :--- | :--- | :--- | :--- |
| **AIML-008-TRN-01** | S008 Foundations: EU AI Act & NIST RMF | An overview of the global AI regulatory landscape, deep dive into the EU AI Act's risk-based approach, and the structure of the NIST AI RMF. | All in-scope personnel | Annually |
| **AIML-008-TRN-02** | SOP-AIML-008 Procedural Certification | A role-based, hands-on walkthrough of this SOP, including a graded simulation of classifying three hypothetical AI systems using the AIML-008-TL-1 tool. | AI/ML Product Managers, AI/ML Engineering Leads, GRC Leads | Annually |
| **AIML-008-TRN-03** | AI Ethics for Developers: Beyond Classification | A workshop on identifying unintended consequences, algorithmic bias, and the human-centric design principles that underpin the High-Risk determination. | AI/ML Engineering Leads, Data Scientists | Annually |

### 9.2 Grace Period and Non-Compliance

Newly onboarded engineers and product managers have a **30-day grace period** from their start date to complete `AIML-008-TRN-01` and `AIML-008-TRN-02`.
Non-compliance will result in the revocation of the individual's permissions to the `AIML Systems Registry` in Jira, preventing them from initiating or contributing to a classification request, effectively halting their AI development work.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Title | Relationship to This SOP |
| :--- | :--- | :--- |
| **SOP-AIML-012** | AI Model Documentation and Model Cards | Consumes the output of this SOP. A valid `risk_tier` is a prerequisite for generating a model card. |
| **SOP-AIML-015** | AI System Post-Market Monitoring (PMM) | Defines the monitoring triggers that can initiate a reclassification under Procedure AIML-008-PROC-02. |
| **SOP-SEC-112** | Security Risk Assessment for AI/ML Systems | Requires the finalized risk classification as an input to determine the depth of the security assessment. |
| **SOP-IR-045** | AI Incident Response and Reporting | Establishes the adverse event reporting channel that serves as a reclassification trigger. |
| **SOP-RA-201** | Conformity Assessment for High-Risk AI Systems | This SOP is the primary control SOP for SOP-RA-201. Classification is the first step of the conformity assessment. |
| **SOP-DP-305** | Data Protection Impact Assessment (DPIA) | Classifications involving special category data trigger a mandatory DPIA, cross-referencing this SOP's output. |

### 10.2 External References

| Reference | Title |
| :--- | :--- |
| **REG-EU-001** | Regulation (EU) 2024/1689 (Artificial Intelligence Act) |
| **FRMW-NIST-001** | NIST AI 100-1: Artificial Intelligence Risk Management Framework (AI RMF 1.0) |
| **REG-EU-002** | Regulation (EU) 2017/745 (Medical Device Regulation) |
| **REG-EU-003** | Regulation (EU) 2016/679 (General Data Protection Regulation) |

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **1.0** | 2023-03-15 | A. Chen (GRC), M. Rossi (Legal) | Initial publication. Established the three-tier risk framework and basic Annex III mapping questionnaire. |
| **2.0** | 2024-01-22 | S. Kapoor (AIML Lead) | Major revision. Integrated NIST AI RMF MAP function mapping. Added the `AIML-008-TL-1` tool description. Updated roles to include the new VP of Engineering, David Park. |
| **3.1** | 2024-09-10 | J. Davies (GRC Lead) | Clarified GPAI Model tiering logic in Procedure 5.1, Step 4, following an Internal Audit finding. Added specific controls for `NeuroSight-Foundation-v2`. Updated KPI targets. |
| **4.0** | 2025-06-14 | L. Patel (Legal) | Comprehensive rewrite to align with the final published text of the EU AI Act. Replaced "conformity assessment" placeholder, refined derogation procedure, and updated all Article references. Mandated use of Archer GRC. |
| **4.1** | 2025-11-17 | J. Davies (GRC Lead) | Minor revision. Corrected regulatory mapping for emotion recognition systems under Article 52(2). Updated Responsible role for Step 5 classification from Lead to GRC Lead. Clarified quarterly dashboard to monthly reporting cadence in Section 7.2. |