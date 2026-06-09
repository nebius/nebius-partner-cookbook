---
sop_id: "SOP-CLIN-002"
title: "Medical Device Software Classification"
business_unit: "Clinical AI Products"
version: "5.0"
effective_date: "2025-04-11"
last_reviewed: "2026-08-27"
next_review: "2027-02-15"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Medical Device Software Classification

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes a systematic, repeatable, and auditable framework for the classification, re-evaluation, and documentation of Software as a Medical Device (SaMD) and non-device Clinical AI software developed, deployed, or maintained by Meridian Health Technologies. The purpose of this SOP is to ensure that every Clinical AI Product that meets the definition of a medical device is correctly identified, assigned an appropriate risk class per applicable regulatory frameworks, and subjected to the requisite software lifecycle controls commensurate with that classification. This procedure operationalizes the classification requirements of Regulation (EU) 2017/745 (EU MDR), Annex VIII; International Medical Device Regulators Forum (IMDRF) N12 guidance on SaMD categorization; and IEC 62304:2006+AMD1:2015 (Medical Device Software—Software Lifecycle Processes).

This SOP further serves to trigger downstream processes including, but not limited to, Software Development Lifecycle (SDLC) pathway assignment (SOP-SW-015), Clinical Evaluation planning (SOP-CLIN-008), Post-Market Surveillance (SOP-PMS-003), Unique Device Identifier (UDI) assignment, and EU AI Act compliance activities.

### 1.2 Scope

#### 1.2.1 In-Scope Products and Activities

This SOP applies to all software products, modules, libraries, and algorithmic components that are intended by Meridian to be used—alone or in combination—for any of the following purposes as defined in Article 2(1) of EU MDR:
- Diagnosis, prevention, monitoring, prediction, prognosis, treatment, or alleviation of disease, injury, or disability;
- Investigation, replacement, or modification of an anatomical, physiological, or pathological process or state;
- Providing information by means of in vitro examination of specimens derived from the human body.

Specifically, this includes:
- **Radiology AI Suite**: Chest X-ray pneumothorax detection (ChestAI-PTX), intracranial hemorrhage triage (NeuroAI-ICH), and musculoskeletal fracture detection (OrthoAI-FX).
- **Digital Pathology Platform**: Whole-slide image analysis modules for tumor burden quantification (PathAI-OncoQuant).
- **Clinical Decision Support (CDS) Algorithms**: Sepsis prediction engine (SepsisAI-Predict), medication dosing optimization tools (DoseAI).
- **Mobile Medical Applications**: Patient-facing cardiac rhythm classification applications (CardioAI-Patient).
- **Platform Components**: Any shared libraries, inference engines, or data preprocessing pipelines that directly influence the clinical output of a SaMD.

#### 1.2.2 Out-of-Scope

The following are explicitly excluded from this SOP:
- Administrative, operational, and financial software (e.g., billing systems, inventory management).
- General-purpose communication platforms not intended for clinical decision support.
- Research-use-only (RUO) algorithms that have not received a formal "Intended Purpose" statement for clinical deployment.
- Wellness and fitness applications (e.g., step counters, sleep hygiene apps) unless specifically marketed as a disease management tool.

#### 1.2.3 Audience

- **Primary**: Clinical AI Product Managers, Clinical AI Software Engineers, Regulatory Affairs Specialists embedded within Clinical AI, Quality Assurance Engineers.
- **Secondary**: Clinical Affairs Specialists, Post-Market Surveillance Analysts, Technical Documentation Writers.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
| :--- | :--- |
| **Software as a Medical Device (SaMD)** | Software intended to perform a medical purpose, without being part of a hardware medical device, as defined by IMDRF/SaMD WG/N10. |
| **Medical Device Software (MDSW)** | A broader term used in the EU encompassing software driving or influencing the use of a hardware device, as well as standalone software. |
| **Intended Purpose** | The objective, stated intended use of the device as described in the labeling, instructions for use, or promotional materials by the manufacturer. This is the critical anchor for classification. |
| **Classification Rule** | A specific provision within a regulation (e.g., EU MDR Annex VIII) used to assign a risk class. |
| **Disease State** | A specific, defined pathological condition (e.g., Pneumothorax, not "lung finding"). |
| **Critical Situation** | A healthcare scenario or patient condition where an accurate, timely diagnosis is essential to prevent imminent death, irreversible morbidity, or significant patient deterioration. |
| **Drive Diagnosis** | A SaMD output that is intended by the manufacturer to be a principal and definitive factor in establishing a clinical diagnosis, without mandatory clinician reconciliation of the finding against all available patient data (a high degree of automation/dependence). |
| **Aid Diagnosis** | A SaMD output intended to provide information that a clinician will use as one input alongside other data points to arrive at a diagnosis (shared decision-making). |
| **Statistical Calibration** | The agreement between observed outcomes and model-predicted probabilities. A perfectly calibrated model producing a 0.7 confidence score would indicate that the finding is true 70% of the time. |
| **State of the Art (SOTA)** | The current, generally acknowledged good practice in the specific clinical and technological domain, per MEDDEV 2.7/1. |

### 2.2 Acronyms

| Acronym | Definition |
| :--- | :--- |
| **CE** | Conformité Européenne |
| **CDS** | Clinical Decision Support |
| **EU MDR** | European Union Medical Device Regulation 2017/745 |
| **IEC** | International Electrotechnical Commission |
| **IMDRF** | International Medical Device Regulators Forum |
| **MDSW** | Medical Device Software |
| **RUO** | Research Use Only |
| **SaMD** | Software as a Medical Device |
| **SDLC** | Software Development Lifecycle |
| **SOTA** | State of the Art |
| **SWE** | Software Engineering |

---

## 3. Roles and Responsibilities

The following matrix defines the Responsible (R), Accountable (A), Consulted (C), and Informed (I) parties for each major process step within this SOP.

| Activity Step | Product Manager (Clinical AI) | Clinical AI Engineering Lead | Regulatory Affairs Specialist (Clinical AI) | Clinical Evaluation Lead | Quality Assurance (QS) | Chief Medical Officer |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Initiation & Intended Purpose Draft** | A/R | C | C | - | I | - |
| **2. Preliminary SaMD Determination** | R | C | A | C | I | - |
| **3. Formal Risk Class Determination** | C | - | A/R | C | I | C |
| **4. IEC 62304 Safety Class Assignment** | - | A/R | C | C | I | - |
| **5. Classification Documentation (FORM-002-A)** | R | C | A | - | I | - |
| **6. Final Sign-off & Release Authorization** | - | - | R | - | A | C |
| **7. Post-Market Re-Classification** | R | C | A | R | I | C |

*R (Responsible): The doer; A (Accountable): The 'yes/no' authority; C (Consulted): Two-way communication; I (Informed): One-way notification.*

---

## 4. Policy Statements

The following overarching policy commitments govern medical device software classification at Meridian:

1.  **Intended Purpose as the Anchor**: Meridian classifies all SaMD based exclusively on its documented, approved Intended Purpose statement and the objective clinical significance of the information it provides. Marketing claims, customer perception, or non-clinical feature sets shall not influence classification decisions.

2.  **Holistic Classification**: Every SaMD component shall receive three interlocked classifications: (a) a regulatory risk class per EU MDR Annex VIII (Class I, IIa, IIb, III); (b) an IMDRF categorization (Categories I–IV); and (c) an IEC 62304 Software Safety Class (A, B, C). These are documented simultaneously in the SaMD Classification Matrix (FORM-002-A).

3.  **Conservative Defaults**: In any scenario where the intended purpose or clinical context creates ambiguity between two adjacent risk classes, the higher class shall govern until a formal, documented rationale from the Clinical Affairs and Regulatory teams justifies the lower classification.

4.  **Algorithmic Independence**: When multiple clinical algorithms reside within a single platform (e.g., a radiology viewer hosting pneumothorax detection and fracture detection), each distinct diagnostic algorithm with a separate clinical decision support goal is classified independently. The platform housing them inherits the controls necessary for the *highest* resident class.

5.  **Continuous Re-Classification**: Classification is not a one-time artifact. A mandatory re-classification review is triggered by any of the following change events per SOP-CLIN-008 (Clinical Evaluation Procedure):
    - Expansion of the Intended Purpose (e.g., adding a new finding type).
    - A change to the target patient population (e.g., from adults to pediatrics).
    - An architectural change that alters the degree of clinician dependency versus automated action.
    - Emergence of new SOTA data from Post-Market Surveillance requiring re-evaluation.

---

## 5. Detailed Procedures

This section outlines the mandatory end-to-end procedure for classifying a new or modified Clinical AI product. No product may proceed to Stage-Gate 3 (Technical Design) in the Meridian Product Lifecycle Management (PLM) system prior to the completion of this procedure.

### 5.1 Procedure 1: Initial Intended Purpose Documentation

The classification process begins with a formal draft of the Intended Purpose. This is not a marketing document but a precise regulatory statement.

1.  **Product Manager Action**: The Product Manager for the new initiative creates a draft document in Meridian's Quality Management System (Grand Avenue QMS), using the **Intended Purpose Definition Template (TEMPLATE-CLIN-001)**.
2.  **Required Statements**: The draft must concisely articulate four key statements:
    - **Medical Purpose**: The exact disease, injury, or condition (e.g., "to detect radiological signs suggestive of pneumothorax," not "to analyze chest images").
    - **Target User & Environment**: Who uses it and where (e.g., "by emergency department attending physicians for adult patients in a tertiary care setting").
    - **Output & Clinical Action**: What information the software provides and how it is intended to be used (e.g., "provides an overlay heatmap and a binary ‘finding’/'no finding’ notification to aid in time-critical triage prioritization").
    - **Contraindications**: Explicitly stated limitations.
3.  **Review Cycle**: The draft is shared simultaneously with the Clinical Evaluation Lead, an embedded Regulatory Affairs Specialist, and the Clinical AI Engineering Lead for a round of commentary before the classification determination begins.

### 5.2 Procedure 2: Is it a Medical Device? (Qualification)

Before risk classification, a binary determination of device status is formalized.

**Step 2.1**: The Regulatory Affairs Specialist conducts a qualification analysis per EU MDR Article 2(1) and the MDCG 2019-11 guidance on qualification and classification of software. This analysis is recorded in Section A of FORM-002-A.

**Step 2.2**: The "Medical Purpose" statement from Procedure 1 is tested against the MDR definition. The core question: *Is the software’s intended purpose to perform a medical action, or primarily to drive or influence the use of a medical device?*
- **If YES**: The software is an MDSW. Proceed to Procedure 3.
- **If NO (e.g., purely administrative)** : The SOP is concluded. The output is an "Exempt—Non-Device" letter signed by the VP of Clinical AI Products.

**Step 2.3**: For SaMD, a secondary determination is made: *Is this standalone SaMD, or does it form part of a system (e.g., an app that drives a connected insulin pump)?* The platform team is consulted if hardware interaction is contemplated.

### 5.3 Procedure 3: EU MDR Annex VIII Risk Class Determination

This is the central regulatory classification procedure, utilizing the 22 rules of Annex VIII.

**Step 3.1: Rule Examination.**
The Regulatory Affairs Specialist, with clinical context from the Clinical Evaluation Lead, sequentially evaluates the Intended Purpose against the rules. For diagnostic AI at Meridian, the typical decision tree is:
- **Rule 1–2 (Non-invasive, not for active patient management)?** Usually, no, as Meridian's products are specifically for diagnostic/monitoring decisions.
- **Rule 3 (Non-invasive, specifically intended for...)**: Does the software directly influence the diagnosis or therapy of a patient?
    - If the SaMD is for "driving" or "directly influencing" the use of a device classified as Class IIb or higher, it becomes class IIb.
- **Rule 11 (Software—Critical):** **This is the most frequent rule for Meridian products.** "Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes..."
    - **Class III**: "If such decisions have the potential to cause... a serious, potentially lethal deterioration of the patient's state... or an irreversible deterioration of a patient's condition..." (e.g., *NeuroAI-ICH: triaging a critical condition where a delay leads to death/irreversible brain damage*).
    - **Class IIb**: "If such decisions have the potential to cause... a serious deterioration of a patient's state of health..." or any surgical intervention. (e.g., *ChestAI-PTX: failure to detect leads to tension pneumothorax, a serious deterioration. OrthoAI-FX: diagnosis driving surgical intervention.*)
    - **Class IIa**: For providing information for diagnostic or therapeutic purposes where no serious deterioration is immediate, or for monitoring vital physiological parameters *not* in a critical care setting. (e.g., *DoseAI: optimizing medication levels, but not providing the sole, real-time, life-sustaining decision. A clinician review step is mandated.*)
- **Rule 15 (Contraception/Disinfection)** : Generally N/A.
- **Rule 21 (Devices composed of substances)** : N/A for pure software.

**Step 3.2: Classification Matrix Documentation (FORM-002-A).**
The Regulatory Affairs Specialist populates the SaMD Classification Matrix Table 1 with the following mandatory fields:

**FORM-002-A, Table 1: Regulatory Classification**

| Attribute | Value |
| :--- | :--- |
| **Product Name & ID** | (e.g., ChestAI-Pneumothorax, PID: CLN-001-PTX) |
| **MDR Annex VIII Rule** | (e.g., Rule 11) |
| **Classification Rationale** | <500-word narrative explaining the disease severity, diagnostic urgency, role of AI output (aid vs. drive), and the consequence pathway of a false negative. |
| **EU Risk Class** | (Class I, IIa, IIb, or III) |
| **Conformity Route** | (e.g., Annex IX Ch. I & III, or Annex X) |

**Step 3.3: IMDRF SaMD Categorization (I-IV).**
Simultaneously, the product is categorized per IMDRF N12 to align with global strategy (FDA PreCert/510(k) planning).

**FORM-002-A, Table 2: IMDRF Framework**

| Axis | Description | Designation |
| :--- | :--- | :--- |
| **Clinical Significance** | Is the information to treat/diagnose critical, serious, or non-serious? | (e.g., Critical) |
| **User's Core Decision** | Does the SaMD drive, drive primarily, aid, or augment? | (e.g., Aid) |
| **IMDRF Category** | Derived from the 4x4 matrix. | (e.g., Category III) |

**Step 3.4: IEC 62304 Safety Class.**
Based on the hazard analysis, the Engineering Lead assigns the Software Safety Classification.

**Step 3.4.1: Hazard Identification.** Using Meridian's **Risk Management File (RMF)**, identify potential hazardous situations caused by software failures.
- *Example for ChestAI-PTX*: A false-negative notification (software fails to detect an obvious pneumothorax) leads to a significant delay in treatment.

**Step 3.4.2: Risk Control Determination.** Evaluate whether the Harm has been controlled to an acceptable level via external (non-software) controls. Meridian's policy is to only credit a clinician as a valid external control if the Intended Purpose explicitly states the output is "to aid" and is not the sole diagnostic input, and the Workflow Diagram shows a mandatory human confirmation step. No credit is given for silent automation of a critical task.

**Step 3.4.3: Safety Class Assignment:**
- **Class C**: A software failure could result in death or serious injury.
- **Class B**: A software failure could result in non-serious injury.
- **Class A**: No risk of injury.

The final IEC 62304 Safety Class is entered into FORM-002-A, Table 3. A discrepancy between the EU MDR Risk Class (e.g., IIb) and the IEC 62304 Safety Class (e.g., C) is normal but must always result in the product life-cycle being governed by the more demanding specification set.

### 5.4 Procedure 4: EU AI Act High-Risk Classification Overlay

As a supplementary procedure, every SaMD classified under Procedure 3 is also assessed against Regulation (EU) 2024/1689 (AI Act).

**Step 4.1: High-Risk Determination.** Meridian adopts a straightforward, conservative approach. Any software that is a safety component of a product, or is itself a product, covered by the Union harmonization legislation listed in Annex I, Section A (which explicitly includes Regulation (EU) 2017/745 for medical devices), is automatically considered a high-risk AI system under Article 6(1) of the AI Act.

**Step 4.2: Conformity Documentation.** The Product Manager creates a dedicated section in the Technical Documentation titled "AI Act Compliance—Article 6." This section records the determination that the device is a high-risk AI system by virtue of its MDR conformity assessment. No separate, de novo classification is performed; the MDR classification is the sole trigger.

### 5.5 Procedure 5: Human Oversight Designation

For all high-risk AI systems as determined in Procedure 4, Meridian defines the Human Oversight Measures.

**Step 5.1 Oversight Architecture Selection.** The Product Manager and Engineering Lead select from a pre-defined library of oversight architectures:
- **Type 1: Human-in-the-loop (HITL) Review.** The AI provides a preliminary output that is queued for review before any clinical action. This is the default for all Meridian triage products (e.g., NeuroAI-ICH).
- **Type 2: Human-on-the-loop (HOTL) Monitoring.** The AI operates autonomously, with a human operator monitoring outputs and able to intervene. (Currently limited to DoseAI's back-end pharmacokinetic calculations, where the intervention is a pharmacist overriding a displayed recommendation.)
- **Type 3: Human-in-command (HIC) Approval.** The AI does not act; it only produces a finalized report that a qualified physician can incorporate. (e.g., PathAI-OncoQuant's automated cell counting, which is embedded in a signed pathology report.)

**Step 5.2 Measure Documentation.** For each product, the chosen architecture is documented in the Design History File (DHF). The documentation includes the UI/UX wireframes showing the point of human intervention (e.g., the "Accept/Reject/Override" dialog box). The review process mandates that the interface is designed to allow a qualified clinician to, at minimum, review, overrule, and dismiss the AI's recommendation.

### 5.6 Procedure 6: Transparency Requirements Definition

Meridian ensures a level of transparency suitable for clinical users.

**Step 6.1 User Information.** The Product Manager drafts a "Transparency Note" for inclusion in the Instructions for Use (IFU) and in-app notifications. This note contains:
- A plain-language statement that the software is an AI system.
- The intended purpose of the AI system.
- The level of accuracy and calibration, expressed in clinically interpretable metrics (e.g., sensitivity, specificity, PPV/NPV for the specific setting).

**Step 6.2 Technical Communication.** The Engineering Lead ensures that the output of the software is accompanied by an interpretable "confidence score" where technically feasible. The IFU explains that this score is a statistical probability, not a clinical certainty, and must be interpreted by a qualified clinician.

### 5.7 Final Classification Review and Release (Stage-Gate 3)

The completed FORM-002-A and all supporting documents are submitted for a formal sign-off via the Grand Avenue QMS "Classification Approval" workflow.

1.  **Regulatory Affairs Specialist**: Submits the package.
2.  **Clinical Evaluation Lead**: Reviews the IMDRF categorization, clinical risk rationale, and the proposed Clinical Evaluation Plan triggers.
3.  **Chief Medical Officer**: Provides final approval of the risk classification and the adequacy of the clinical safety measures, or returns the package with a query. All CMO queries must be formally closed out with a documented response.
4.  **Quality Assurance**: Confirms the SDLC pathway (SOP-SW-015) is correctly set in the QMS based on the approved Safety Class (Class C requiring the most rigorous process), and releases the Stage-Gate 3 artifact lock.

---

## 6. Controls and Safeguards

The following administrative, procedural, and technical controls are implemented to safeguard the classification process and the subsequent product integrity.

### 6.1 Administrative Controls

| Control ID | Control Description | Implementation |
| :--- | :--- | :--- |
| **ADM-001** | **Separation of Duties**: The individual drafting the Intended Purpose (Product Manager) cannot be the sole individual responsible for its regulatory classification. | Enforced via Grand Avenue QMS Workflow: PM submits Intended Purpose; Regulatory Affairs completes and signs Classification. |
| **ADM-002** | **Four-Eyes Principle for Class III**: All Class III (EU) and IMDRF Category IV determinations require a mandatory, independent second review by a Regulatory Affairs Specialist outside of the product's immediate development squad. | The QMS workflow routes the FORM-002-A to the Director of Regulatory Affairs for automatic assignment to a blinded reviewer. |
| **ADM-003** | **Labeling Reconciliation**: Before any CE-marked product release, the Intended Purpose statement on the FORM-002-A is reconciled against the exact text in the IFU, product label, and any public marketing materials. | A mandatory "Lab-Label Match" checklist (CHK-002-A) is signed by the Product Manager and Regulatory Affairs at Stage-Gate 5 (Release). |

### 6.2 Technical Controls

| Control ID | Control Description | Implementation |
| :--- | :--- | :--- |
| **TEC-001** | **Feature Flag & Code Isolation**: Modular SaMD algorithms are deployed behind feature flags and isolated in containerized microservices. Activating a new algorithm (e.g., adding spine fracture to OrthoAI-FX) requires an explicit code change and is not achievable by config change alone. | Kubernetes deployments with strict network policies and immutable image tags. The "Intended Purpose" field in the QMS is tied to a specific list of enabled feature flags. |
| **TEC-002** | **Automated Workflow Enforcement**: In the Meridian CI/CD pipeline (GitLab), a job (`regulatory-lint`) is scripted to automatically fail a build destined for a production branch if the corresponding FORM-002-A in Grand Avenue QMS is not in "Approved" status and linked to the specific commit SHA. | Integration between the GitLab Runner and the Grand Avenue REST API. |
| **TEC-003** | **Output Marking**: Every clinical notification, DICOM Structured Report, or HL7 FHIR message generated by a Meridian SaMD shall include a machine-readable content tag containing the SaMD Product ID and version. | This tag is enforced by a sidecar container in the inference service pod. |

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness of this SOP and the performance of classified SaMD are monitored through a defined set of key performance indicators (KPIs).

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | Metric | Target | Measurement Tool | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **KPI-CLAS-01** | **Classification Cycle Time**: Mean time from initiation of Intended Purpose to FORM-002-A "Approved" date. | < 15 business days for new Class IIa; < 25 days for Class IIb/III. | Grand Avenue QMS Reports | Head of Regulatory Affairs |
| **KPI-CLAS-02** | **Re-Classification Trigger Compliance**: Percentage of Change Requests (PCRs) that correctly trigger a re-classification review per SOP-CLIN-008. | 100% (measured quarterly via QS audit). | CAPA Log Audit | QA Manager |
| **KPI-SAF-01** | **Model Calibration Drift**: The statistical calibration error (Expected Calibration Error, ECE) of a deployed model against a rolling production data window. | ECE < 0.05 for all Class III devices; < 0.10 for Class IIb devices. | ML Observability Platform (Arize AI) | Algorithm Engineering Lead |
| **KPI-SAF-02** | **Clinical Decision Override Rate**: The rate at which a supervising clinician explicitly overrides or dismisses a SaMD's primary finding. | Monitored per product; an Upper Control Limit (UCL) deviation is set at ±3 sigma from the 90-day baseline. | SaMD User Interface Audit Logs | Clinical Evaluation Lead |

### 7.2 Reporting Cadence

- **Product-Specific Dashboard**: A real-time "Device Health" dashboard is maintained for each Class III device, displaying KPI-SAF-01 and KPI-SAF-02. Access is granted to the VP of Clinical AI Products and the CMO.
- **Monthly Classification Review**: A standing meeting between the Clinical AI Regulatory Affairs team and the Clinical Evaluation Lead to review all newly classified products and any open re-classification tasks.
- **Quarterly Management Review (QMR) Presentation**: A consolidated report on all KPI-CLAS metrics, including a report on the effectiveness of the classification process, is presented to the Chief Medical Officer as part of the overall Quality System Management Review.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

A formal exception to a mandate within this SOP must be documented using the **Regulatory Exception Request (RER-001)** form. The most common exception types are:
- **Classification Disagreement**: A Product Manager or Engineering Lead formally disagrees with the risk class determined by the Regulatory Affairs Specialist.
- **Timeline Override**: A business executive requests a product launch without completed classification.
- **External Control Credit Dispute**: Disagreement over whether a human operator constitutes a valid risk control for IEC 62304 Class C downgrade to B.

### 8.2 Exception Approval Hierarchy

| Exception Level | Description | Approval Authority |
| :--- | :--- | :--- |
| **Minor** | Procedural error (e.g., missing a single reviewer signature but all parties concurred). Can be corrected without altering the safety class. | Director of Quality Assurance |
| **Major** | Disagreement on class leading to a higher-class pathway (conservative default). (e.g., Engineer thinks Class B, Regulatory says Class C; Engineer refuses to sign). | VP of Clinical AI Products & Chief Medical Officer jointly |
| **Critical** | Any act that would result in a down-classification of a SaMD from a higher to a lower risk class. | **No single individual.** Reviewed by the Meridian Clinical Advisory Board, with final sign-off by the Chief Medical Officer and General Counsel. |

### 8.3 Escalation Path

If the primary Classification approver (Regulatory Affairs Specialist) and the Engineering Lead reach a deadlock:
1.  The issue is jointly documented in an RER-001.
2.  The RER is escalated to the Director of Regulatory Affairs and the VP of Clinical AI Products within 5 business days.
3.  If unresolved, the product is placed on "Regulatory Hold" in the QMS, and no further development milestones can be passed.

---

## 9. Training Requirements

All personnel identified in Section 3 must be demonstrably competent in the procedures defined in this SOP before they are assigned responsibilities for a SaMD product.

### 9.1 Training Curriculum

| Role(s) | Required Training Module (LMS ID) | Frequency | Competency Assessment |
| :--- | :--- | :--- | :--- |
| **Product Managers** | LMS-CLIN-002A: "Intended Purpose & SaMD Classification for Product Owners" | Annual. Initial before Stage-Gate 1 access is granted. | Passing score of 90% on the "Intended Purpose Drafting" simulation quiz. |
| **Engineering Leads & SWE** | LMS-CLIN-002B: "Engineering Implications of IEC 62304 (Classes A, B, C)" | Annual. | Successful completion of a mock DHF for a fictional Class C device. |
| **Regulatory Affairs Specialists** | LMS-CLIN-002C: "Master Classification under EU MDR Annex VIII" | Bi-annual. Initial certification. | A "Black Belt" certification requiring a live, unassisted classification of 3 historical Meridian products with 100% accuracy. |
| **All In-Scope Roles** | LMS-CLIN-002-X: "SOP-CLIN-002 Version 5.0 Awareness Training" | Once per major Version release. | Acknowledgment via the Grand Avenue QMS training module. |

### 9.2 Tracking and Non-Compliance

- Training records are maintained in the Grand Avenue QMS "Personnel and Training" module.
- **Stage-Gate 2 Non-Compliance**: An individual assigned to a project team who has not completed the relevant LMS-CLIN-002 modules will have their QMS workflow access temporarily suspended until compliance is achieved. Project schedules will not be adjusted to accommodate this non-compliance.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title |
| :--- | :--- |
| SOP-CLIN-008 | Clinical Evaluation and Investigation Procedure for Medical Devices |
| SOP-SW-015 | Software Development Lifecycle (SDLC) for Medical Device Software |
| SOP-RSK-001 | Risk Management File (RMF) Creation and Maintenance |
| SOP-PMS-003 | Proactive Post-Market Surveillance Plan |
| SOP-QMS-001 | Document Control and Grand Avenue QMS Usage |
| SOP-UDI-001 | Unique Device Identification (UDI) Assignment and Labeling Work Instruction |

### 10.2 External Standards and Regulations

| Document ID | Title |
| :--- | :--- |
| EU 2017/745 | Regulation (EU) 2017/745 on Medical Devices (EU MDR), Annex VIII |
| EU 2017/745 | Regulation (EU) 2017/745 on Medical Devices (EU MDR), Annex II (Technical Documentation) |
| IEC 62304:2006/AMD1:2015 | Health software — Software life cycle processes |
| IMDRF/SaMD WG/N12 | "Software as a Medical Device": Possible Framework for Risk Categorization and Corresponding Considerations |
| MDCG 2019-11 | Guidance on Qualification and Classification of Software in Regulation (EU) 2017/745 – MDR and Regulation (EU) 2017/746 – IVDR |
| (EU) 2024/1689 | Regulation (EU) 2024/1689 (Artificial Intelligence Act) |

---

## 11. Revision History

| Version | Date | Author | Section(s) Modified | Description of Change |
| :--- | :--- | :--- | :--- | :--- |
| **5.0** | 2025-04-11 | Dr. Aisha Okafor | All | Major revision: Integrated EU AI Act High-Risk classification overlay (Section 5.4), Human Oversight Designation (5.5), and Transparency Requirements (5.6). Removed obsolete MDD 93/42/EEC references. |
| **4.0** | 2024-03-15 | Dr. Samuel Grey | 5.3, 8 | Updated classification rules per new MDCG guidance on diagnostic imaging software. Added Critical exception escalation path (Section 8.2). Updated ChestAI-PTX to Class IIb per Rule 11. |
| **3.1** | 2023-08-11 | Sarah Chen | 7 | Corrected KPI-SAF-01 target for Class IIb devices from erroneous "< 0.01" to achievable "< 0.10". Minor typographical corrections. |
| **3.0** | 2023-02-15 | Dr. Aisha Okafor | 2, 3, 5 | Comprehensive rewrite to align roles with new PLM structure. Defined Technical Controls for CI/CD enforcement (TEC-002). Removed legacy "Engineering Owner" role, replacing with cross-functional RACI. |
| **2.1** | 2022-06-01 | Raj Patel | 8, 10 | Added RER-001 form and defined exception hierarchy. Updated cross-references to SOP-SW-015 (v3.0). |
| **2.0** | 2021-09-01 | Dr. Aisha Okafor | 5.3, 5.7 | Major update transitioning classification from a document-centric to a workflow-centric process in Grand Avenue QMS. Added formal IMDRF categorization table. |