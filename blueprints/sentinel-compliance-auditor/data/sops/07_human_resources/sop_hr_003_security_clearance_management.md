---
sop_id: "SOP-HR-003"
title: "Security Clearance Management"
business_unit: "Human Resources"
version: "4.8"
effective_date: "2025-07-28"
last_reviewed: "2026-02-02"
next_review: "2026-08-05"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Security Clearance Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, processes, and controls governing security clearance management for all Meridian personnel, contractors, vendors, and third parties who require access to Meridian information systems, Protected Health Information (PHI), Personally Identifiable Information (PII), financial data, clinical AI models, and cloud infrastructure. The purpose of this SOP is to ensure that access to sensitive resources is granted based on verified need, validated trustworthiness, and ongoing suitability, in alignment with regulatory obligations including HIPAA, SOC 2, GDPR, the EU Medical Device Regulation (MDR), and internal governance requirements.

### 1.2 Scope

This SOP applies to the following populations across all Meridian business units, geographies, and subsidiaries:

| Population | Coverage |
|------------|----------|
| Full-time employees (FTE) | All levels, including executive leadership |
| Part-time employees | All levels, prorated clearance requirements |
| Independent contractors (1099 or equivalent) | All engagements exceeding 30 calendar days or involving access to Restricted systems |
| Temporary personnel and agency staff | All assignments exceeding 15 calendar days or involving access to Internal systems |
| Third-party vendors and service providers | All engagements requiring logical or physical access to Meridian facilities or systems |
| Visiting researchers and clinical affiliates | All collaborations involving PHI, clinical trial data, or AI model training datasets |
| Board members | As required by fiduciary access obligations |
| Subsidiary personnel accessing Meridian systems | Full reciprocity under this SOP |

This SOP covers all phases of the clearance lifecycle: pre-employment vetting, initial clearance granting, clearance level assignment, access mapping, periodic reinvestigation, clearance modification, suspension, revocation, and offboarding clearance termination.

### 1.3 Applicability to Systems and Data Classifications

Security clearances governed by this SOP apply to the following Meridian data classifications as defined in SOP-IS-007 ("Data Classification and Handling"):

| Data Classification | Clearance Requirement |
|---------------------|----------------------|
| Public | No clearance required |
| Internal | Level 1 clearance minimum |
| Confidential | Level 2 clearance minimum |
| Restricted | Level 3 clearance minimum |
| Regulated (PHI, ePHI, clinical trial data) | Level 2 clearance plus HIPAA-specific authorization |

All systems enumerated in the Meridian System Inventory (maintained under SOP-IS-001) are subject to clearance-based access controls.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|------|------------|
| **Security Clearance** | A formal determination by the Human Resources Security Clearance Office (HR-SCO), in coordination with Information Security, that an individual has undergone prescribed vetting and is authorized to access specified Meridian assets at a designated level. |
| **Background Investigation** | The comprehensive process of verifying an individual's identity, employment history, education, criminal record, credit history (where legally permissible), professional licensure, and other relevant indicators of trustworthiness. |
| **Access Mapping** | The systematic assignment of logical and physical access rights to a cleared individual based on role, clearance level, and explicit authorization. |
| **Reinvestigation** | A periodic re-execution of specified background investigation components to confirm continued eligibility for clearance. |
| **Adjudication** | The evaluative process by which derogatory or discrepant information discovered during investigation is assessed against clearance standards, resulting in a grant, denial, suspension, or modification of clearance. |
| **Derogatory Information** | Any finding that may adversely reflect on an individual's suitability for clearance, including criminal convictions, falsified credentials, adverse financial judgments, or substantiated prior employment misconduct. |
| **Need-to-Know** | The principle that access to classified or sensitive information is granted only where the individual's role functions demonstrably require such access, irrespective of clearance level. |
| **Clearance Suspension** | A temporary withdrawal of clearance privileges pending investigation or adjudication of newly discovered derogatory information, during which the individual may be placed on administrative leave or assigned to non-sensitive duties. |
| **Clearance Revocation** | The permanent withdrawal of clearance privileges, resulting in immediate termination of access to all systems requiring said clearance. |
| **Reciprocity** | The acceptance by Meridian of a valid clearance granted by another authoritative entity, where the standards of the granting entity are determined by HR-SCO and InfoSec to meet or exceed Meridian requirements. |

### 2.2 Acronyms

| Acronym | Definition |
|---------|------------|
| **BI** | Background Investigation |
| **CCS** | Clearance Classification Schema |
| **CJIS** | Criminal Justice Information Services (FBI division) |
| **E-QIP** | Electronic Questionnaires for Investigations Processing (Meridian's internal investigation platform, hosted on Workday) |
| **ePHI** | Electronic Protected Health Information |
| **FCL** | Facility Clearance Level |
| **HR-SCO** | Human Resources Security Clearance Office |
| **IAM** | Identity and Access Management (Okta platform) |
| **InfoSec** | Information Security |
| **ISMS** | Information Security Management System |
| **MDR** | Medical Device Regulation (EU 2017/745) |
| **NAC** | National Agency Check |
| **NBIB** | National Background Investigations Bureau (reference standard) |
| **PCL** | Personnel Clearance Level |
| **PHI** | Protected Health Information |
| **PR** | Periodic Reinvestigation |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RBAC** | Role-Based Access Control |
| **RTO** | Recovery Time Objective |
| **SCO** | Security Clearance Office |
| **TIN** | Taxpayer Identification Number |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| Activity | HR-SCO Director | HR Clearance Analyst | InfoSec CISO | Hiring Manager | Employee/ Candidate | Legal & Compliance | CEO |
|----------|-----------------|----------------------|--------------|----------------|---------------------|--------------------|-----|
| Initial background investigation authorization | A | R | C | I | I | I | — |
| BI execution and vendor management | A | R | C | — | C | I | — |
| Adjudication of derogatory information | A | R | C | I | I | C | — |
| Clearance level determination | A | R | C | I | I | — | — |
| Access mapping (logical) | I | C | A/R | — | I | — | — |
| Access mapping (physical) | A | R | C | — | I | — | — |
| Periodic reinvestigation (PR) | A | R | I | I | C | — | — |
| Clearance suspension decision | A/R | C | C | I | I | C | I |
| Clearance revocation decision | R | C | C | I | I | A | I |
| Exception approval (Level 1–2) | A/R | R | C | I | — | I | — |
| Exception approval (Level 3+) | R | C | C | I | — | A | I |
| Quarterly compliance reporting | A | R | C | — | — | I | I |

**R = Responsible** (performs the work); **A = Accountable** (approves and is answerable for outcome); **C = Consulted** (provides input); **I = Informed** (receives notification).

### 3.2 Specific Roles

| Role | Designation | Authority |
|------|-------------|-----------|
| **Chief Human Resources Officer (CHRO)** | Jennifer Walsh | Ultimate owner of this SOP; approves clearance policy changes; adjudicates escalated Level 3 derogatory cases. |
| **HR-SCO Director** | [Currently: Thomas Eberhardt] | Day-to-day oversight of all clearance operations; authorization of BI initiation; chairing the Clearance Adjudication Board. |
| **HR Clearance Analysts** | Team of 6 FTE | Execution of BI processing, document verification, initial adjudication recommendations, reinvestigation scheduling. |
| **Chief Information Security Officer (CISO)** | [Information Security] | Co-authority for access mapping of systems handling ePHI and Restricted data; consultation on technical access controls. |
| **Data Protection Officer (DPO)** | [Berlin-based; reports to Legal & Compliance] | Consultation on GDPR implications of investigative data handling for EU candidates and personnel. |
| **Hiring Managers** | All personnel with hiring authority | Initiation of clearance requests; submission of role-based access requirements; notification of role changes triggering clearance review. |
| **Clearance Adjudication Board** | Standing body: HR-SCO Director, CISO or designee, Chief Legal Counsel or designee, one independent member from Ethics | Adjudication of derogatory information for Level 2 and 3 clearances; decisions by majority vote; CHRO holds veto authority. |
| **AI Governance Committee** | Board-level committee established 2024 | Advisory review of clearance standards for personnel accessing clinical AI training datasets and model weights. |

---

## 4. Policy Statements

### 4.1 General Principles

**4.1.1** Meridian grants security clearances solely on the basis of verified identity, demonstrated trustworthiness, and validated business need. No individual shall receive access to any Meridian system, facility, or data asset above the Public classification without a completed, favorably adjudicated clearance at the requisite level.

**4.1.2** Clearance decisions shall be made without regard to race, color, religion, sex (including pregnancy, sexual orientation, and gender identity), national origin, age (40 or older), disability, genetic information, or any other characteristic protected by applicable law. All investigative procedures shall comply with the Fair Credit Reporting Act (FCRA), GDPR Article 22 (automated decision-making), and applicable local labor codes.

**4.1.3** Meridian adheres to the "need-to-know" principle. Possession of a clearance at a given level does not confer unrestricted access to all assets at that level. Access shall be explicitly granted, mapped, and periodically reviewed.

### 4.2 Clearance Levels

Meridian maintains a four-tier Personnel Clearance Level (PCL) schema, designated PCL-0 through PCL-3, corresponding to increasing depth of investigation and progressively restricted access authorization.

| Clearance Level | Designation | Investigation Depth | Maximum Data Access |
|-----------------|-------------|---------------------|---------------------|
| **PCL-0** | No Clearance | Identity verification only (I-9 or equivalent) | Public data only |
| **PCL-1** | Basic Clearance | Identity + employment verification + criminal record check (7-year, all jurisdictions of residence) + education verification (highest claimed degree) | Internal data; SaaS platform basic user functions; building access (general areas) |
| **PCL-2** | Intermediate Clearance | All PCL-1 components + credit history check + professional licensure verification + 10-year residence history + 3 professional references + drug screening (where role-required) | Confidential data; PHI access under HIPAA authorization; financial systems (non-administrative); AWS Console read-only access (non-prod); clinical AI model inference endpoints |
| **PCL-3** | Advanced Clearance | All PCL-2 components + FBI Identity History Summary Check (or CJIS equivalent) + psychological evaluation (if role-required) + foreign contact/foreign influence screening + financial disclosure review | Restricted data; PHI bulk access; AWS administrative access; clinical AI model training pipelines and weights; credit scoring and fraud detection model access (SR 11-7 governed); Facility Clearance for secure areas |

### 4.3 HIPAA-Specific Authorization

Pursuant to HIPAA Privacy Rule (45 CFR § 164.508) and Security Rule (45 CFR § 164.308(a)(3)(ii)(A) — Workforce Security):

**4.3.1** Any individual requiring access to PHI or ePHI must hold a minimum PCL-2 clearance and must execute a **HIPAA Workforce Security Authorization** (Form HR-003-A) prior to such access being provisioned.

**4.3.2** The HIPAA Workforce Security Authorization shall explicitly enumerate:
- (a) The categories of PHI to which access is authorized;
- (b) The specific systems, applications, and databases through which access shall occur;
- (c) The permissible purposes of access (treatment, payment, healthcare operations, or research as defined under 45 CFR § 164.506);
- (d) The expiration date of the authorization, not to exceed 12 months from the date of signature;
- (e) Explicit acknowledgment of criminal and civil penalties under HIPAA for unauthorized access or disclosure (42 USC § 1320d-5 and § 1320d-6).

**4.3.3** Under HIPAA § 164.308(a)(3)(ii)(B) — Workforce Clearance Procedure — Meridian shall verify that the individual's PCL-2 or PCL-3 background investigation has been completed and favorably adjudicated prior to granting any PHI access credential.

**4.3.4** Access to psychotherapy notes (where held), genetic information, or HIV/AIDS-related information shall require enhanced authorization beyond standard PCL-2, as specified in SOP-IS-004 ("HIPAA Special Categories Access").

### 4.4 GDPR Considerations

**4.4.1** Background investigations of EU-based candidates or personnel shall be conducted in compliance with GDPR Article 6 (lawfulness of processing), with the lawful basis documented as either consent (Article 6(1)(a)) for non-mandatory investigative components, or legitimate interest balanced against data subject rights (Article 6(1)(f)) for criminal record checks where required by the role.

**4.4.2** EU data subjects shall receive, prior to investigation commencement, a **GDPR Processing Notice — Background Investigations** (available from the DPO) specifying the categories of personal data to be processed, the purposes, the retention period (see Section 5.8), and their rights under Articles 15–22.

**4.4.3** All investigative data pertaining to EU data subjects shall be stored within Meridian's eu-west-1 AWS region and shall be subject to Data Protection Impact Assessment (DPIA) requirements under GDPR Article 35, conducted by the DPO in coordination with HR-SCO.

### 4.5 SOC 2 Commitments

**4.5.1** Availability: Meridian commits to maintaining the availability of clearance processing services such that clearance initiation, adjudication, and access provisioning are not unduly delayed so as to impact business operations. The HR-SCO shall establish reasonable processing timelines (Section 5) and shall make commercially reasonable efforts to meet them.

**4.5.2** Security: Meridian implements logical access controls to the E-QIP investigation platform such that only authorized HR-SCO personnel may access investigative records. Access shall be granted based on role and shall be subject to review.

**4.5.3** Processing Integrity: All clearance determinations shall be made through the documented adjudication procedures set forth in Section 5.4 of this SOP, ensuring complete, accurate, and authorized processing of background investigation data.

**4.5.4** Confidentiality: All investigative records, including BI reports, credit reports, criminal history, and reference responses, shall be classified as Restricted data, stored with encryption at rest and in transit, and accessible only to personnel with an explicit business need.

**4.5.5** Privacy: Meridian shall collect, use, retain, and dispose of personal information obtained during the clearance process in accordance with the commitments in Meridian's Privacy Notice, this SOP, and applicable data protection laws.

### 4.6 Non-Discrimination in Security Clearance Adjudication

**4.6.1** The presence of derogatory information does not constitute automatic grounds for clearance denial. Each finding shall be adjudicated according to the **Whole-Person Concept**, evaluating the nature, severity, recency, frequency, and circumstances of the derogatory information against evidence of rehabilitation, reliability, and current trustworthiness.

**4.6.2** The following adjudicative factors shall be considered:
- Nature and seriousness of the conduct;
- Circumstances surrounding the conduct;
- Frequency and recency of the conduct;
- Age of the individual at the time of the conduct;
- Whether the conduct was isolated or part of a pattern;
- Motives for the conduct;
- Whether there has been rehabilitation or other behavioral changes;
- The potential pressure, coercion, exploitation, or duress that may have existed.

---

## 5. Detailed Procedures

### 5.1 Clearance Request Initiation

**5.1.1 Triggering Events**

A security clearance investigation shall be initiated upon any of the following triggering events, processed through the Workday Security Clearance Module (hereafter "Workday SCM"):

| Trigger | Initiator | Processing SLA |
|---------|-----------|----------------|
| Contingent offer of employment extended and accepted | Hiring Manager | BI initiation within 2 business days of offer acceptance |
| Contractor or vendor engagement approval | Meridian sponsoring manager | BI initiation within 3 business days of vendor agreement execution |
| Internal transfer to a role requiring a higher clearance level | Hiring Manager (receiving dept.) | BI initiation within 1 business day of transfer approval |
| Temporary elevation of clearance (incident response, clinical emergency) | CISO or CMO | Expedited BI initiation within 4 business hours |
| Merger/acquisition personnel integration | CHRO or designee | BI initiation batch processing within 10 business days |

**5.1.2 Clearance Request Form (Workday SCM)**

The Hiring Manager or sponsoring manager shall complete the **Security Clearance Request** form containing:

- (a) Candidate personal identifiers (full legal name, date of birth, Social Security Number or national identification number, place of birth, citizenship status);
- (b) Role title, department, and Meridian employee/contractor classification;
- (c) Justification for clearance level requested, including a description of systems, data classifications, and facilities to which access is required;
- (d) Identification of any PHI access required (triggering HIPAA Workforce Security Authorization requirement);
- (e) Identification of any role responsibilities governed by SR 11-7 (credit scoring, fraud detection, or lending models);
- (f) Whether the role requires EU data subject access (triggering GDPR DPO consultation);
- (g) Name of the sponsoring manager accepting responsibility for ongoing need-to-know validation;
- (h) Requested start date.

**5.1.3 Clearance Level Determination**

Upon receipt of the request, the assigned HR Clearance Analyst shall verify the requested clearance level against the **Role-to-Clearance Mapping Matrix** maintained by HR-SCO and InfoSec in the Workday SCM. The matrix shall be reviewed and revalidated semi-annually (see SOP-IS-005, "Access Control Policy"). If the requested level exceeds the standard mapping for the role, the Analyst shall escalate to the HR-SCO Director for adjudication (see Section 8, Exception Handling).

**5.1.4 Acknowledgement and Consent**

Prior to BI initiation, the candidate shall receive, through Workday SCM, the following documents for electronic signature:

- **Consent to Background Investigation** (Form HR-003-B): Authorizing Meridian to conduct the investigation at the specified depth, compliant with FCRA (U.S. candidates) and applicable local law.
- **Summary of Rights Under the Fair Credit Reporting Act** (U.S. candidates only).
- **HIPAA Workforce Security Authorization** (Form HR-003-A, if PHI access is required).
- **GDPR Processing Notice** (EU data subjects only).
- **Meridian Non-Disclosure Agreement** (SOP-LEG-001), if not previously executed.

Candidates who decline to provide consent shall not proceed in the clearance process, and the Hiring Manager shall be notified immediately.

### 5.2 Background Investigation Execution

**5.2.1 Investigation Components by Clearance Level**

The investigation executed shall correspond precisely to the clearance level as defined in Section 4.2. Meridian utilizes Acme Background Investigations, Inc. ("Acme") as its primary consumer reporting agency (CRA) for U.S. investigations, and GlobalVet GmbH for EU-based investigations, integrated via API with Workday SCM.

| Component | PCL-1 | PCL-2 | PCL-3 |
|-----------|-------|-------|-------|
| Identity verification (SSN trace, passport validation) | ✓ | ✓ | ✓ |
| 7-year criminal record check (all jurisdictions of residence) | ✓ | ✓ | ✓ |
| Federal criminal record check (PACER, all federal districts) | — | ✓ | ✓ |
| Employment verification (7 years) | ✓ | ✓ | ✓ |
| Education verification (highest claimed degree only, PCL-1; all claimed degrees, PCL-2+) | ✓ | ✓ | ✓ |
| Professional licensure verification | — | ✓ | ✓ |
| Credit history report (where legally permissible) | — | ✓ | ✓ |
| 10-year residence history | — | ✓ | ✓ |
| 3 professional references (manager-level or above) | — | ✓ | ✓ |
| Drug screening (5-panel or 10-panel, per role requirements) | — | ✓ | ✓ |
| FBI Identity History Summary Check (fingerprint-based) | — | — | ✓ |
| Financial disclosure review (SF-714 equivalent) | — | — | ✓ |
| Foreign contact/foreign influence questionnaire | — | — | ✓ |
| Psychological evaluation (roles involving clinical AI training data access, per AI Governance Committee recommendation) | — | — | ✓ |
| National Agency Check with Local Agency Checks (NACLC equivalent, for U.S. personnel with national security implications) | — | — | ✓ |

**5.2.2 Investigation Timeline**

| Clearance Level | Target Completion (Business Days) | Escalation Trigger |
|-----------------|-----------------------------------|--------------------|
| PCL-1 | 5 business days | Not completed by day 8; escalate to HR-SCO Director |
| PCL-2 | 10 business days | Not completed by day 15; escalate to HR-SCO Director |
| PCL-3 | 20 business days | Not completed by day 30; escalate to CHRO and CISO |

**5.2.3 Interim Clearance (Conditional Access)**

Under exceptional circumstances where business continuity is critically impacted by clearance processing delays, an **Interim PCL-1** clearance may be granted upon:

- (a) Completion of identity verification with no discrepancies;
- (b) Return of a "clear" criminal record check for all jurisdictions of current residence (past 3 years);
- (c) Written approval of the HR-SCO Director and the CISO;
- (d) Execution of an **Interim Clearance Acknowledgement** (Form HR-003-C) by the candidate and the sponsoring manager, acknowledging that interim clearance may be revoked at any time without appeal.

Interim clearances shall not, under any circumstances, authorize access to PHI, ePHI, financial systems governed by SR 11-7, clinical AI model training data, or administrative access to production AWS environments. Interim clearance duration shall not exceed 15 business days, by which time the full investigation must be completed.

### 5.3 Investigation Reporting

**5.3.1** Acme (or GlobalVet for EU investigations) shall return a **Background Investigation Report** (BIR) to the HR-SCO through the secure API integration with Workday SCM. The BIR shall flag any derogatory findings, discrepancies, or "unable to verify" results.

**5.3.2** Upon BIR receipt, the assigned HR Clearance Analyst shall review the report for completeness. If any component returns as "unable to verify," the Analyst shall request supplementary documentation from the candidate within 3 business days. Failure to provide requested documentation shall be treated as an adverse finding in adjudication.

### 5.4 Adjudication

**5.4.1 Clear (No Derogatory Findings)**

If the BIR contains no derogatory findings and all components are verified as satisfactory, the HR Clearance Analyst shall make an **Adjudication Recommendation: Grant** in Workday SCM. For PCL-1, the Analyst is authorized to adjudicate directly. For PCL-2 and PCL-3, the recommendation shall proceed to the HR-SCO Director for approval (PCL-2) or to the Clearance Adjudication Board for approval (PCL-3).

Upon approval, Workday SCM shall:
- (a) Update the employee's personnel record with the granted PCL and expiration date;
- (b) Trigger an automated workflow to Okta (IAM) for access provisioning based on role-to-entitlement mapping (see Section 5.6);
- (c) Notify the Hiring Manager, the employee, and InfoSec of the clearance grant.

**5.4.2 Derogatory Findings Present**

If the BIR contains derogatory findings, the HR Clearance Analyst shall prepare a **Derogatory Information Summary** (DIS) containing:

- (a) A factual, objective description of each derogatory finding;
- (b) Reference to the specific BI component that returned the finding;
- (c) Classification of severity: **Minor** (e.g., single dismissed misdemeanor, minor credit delinquency), **Moderate** (e.g., multiple misdemeanor convictions, significant credit delinquency, single unverified employment gap >6 months), or **Serious** (e.g., felony conviction, active warrant, falsified credentials, identity fraud, financial judgments exceeding $50,000);
- (d) An initial Whole-Person Concept analysis.

The DIS shall be provided to the candidate via secure electronic delivery through Workday SCM. The candidate shall have **5 business days** to respond in writing with mitigating information, corrections, or contextual explanation.

**5.4.3 Adjudication Pathway by Severity**

| Severity | PCL-1 | PCL-2 | PCL-3 |
|----------|-------|-------|-------|
| Minor | HR Clearance Analyst adjudicates; may grant with documentation | HR-SCO Director adjudicates; may grant with documentation and/or conditions | Clearance Adjudication Board adjudicates |
| Moderate | HR-SCO Director adjudicates | Clearance Adjudication Board adjudicates | Clearance Adjudication Board adjudicates; CHRO notified |
| Serious | Clearance Adjudication Board adjudicates | Clearance Adjudication Board adjudicates | Clearance Adjudication Board adjudicates; CHRO and CEO notified |

**5.4.4 Adjudication Outcomes**

| Outcome | Definition | Effect |
|---------|------------|--------|
| **Grant — Unconditional** | Derogatory findings assessed as not material to trustworthiness or security | Full clearance granted at requested level; standard expiration |
| **Grant — Conditional** | Derogatory findings warrant monitoring or restrictions | Clearance granted with specific, documented conditions (e.g., quarterly PR for 2 years, restriction from specific systems) |
| **Grant — Downgraded** | Findings do not support requested level, but support a lower level | Clearance granted at the highest supportable level; Hiring Manager to reassess role requirements |
| **Denial** | Findings materially impact trustworthiness assessment; Whole-Person analysis does not support clearance | Clearance denied; candidate notified in writing; may request reconsideration (see below) |
| **Pending Further Investigation** | Findings warrant additional investigative steps | BI reopened for specified components; timeline extended by mutual determination |

**5.4.5 Notification of Adverse Action**

For U.S. candidates, any denial or conditional grant based in whole or in part on a consumer report shall be handled in strict compliance with the FCRA adverse action process:

- (a) **Pre-Adverse Action Notice**: Prior to final decision, Meridian shall provide the candidate with a copy of the consumer report, a summary of rights under FCRA, and written notice of the specific derogatory findings under consideration. The candidate shall have a reasonable period (minimum 5 business days) to respond.
- (b) **Adverse Action Notice**: If the final decision is adverse, Meridian shall provide written notice including: the name, address, and telephone number of the CRA that supplied the report; a statement that the CRA did not make the adverse decision and cannot explain the specific reasons; notice of the candidate's right to obtain a free copy of the report from the CRA within 60 days; and notice of the right to dispute the accuracy or completeness of any information in the report.

**5.4.6 Reconsideration**

A candidate who receives a denial may request reconsideration within **10 business days** of receiving the adverse action notice. The request must:
- (a) Be in writing and submitted to the HR-SCO Director;
- (b) Identify specific factual errors alleged or provide new mitigating evidence not previously available.

The Clearance Adjudication Board shall reconvene within 10 business days to consider the request. The Board's reconsideration decision shall be final, with no further internal appeal. The CEO retains discretionary authority to review any denial determination, exercised only in extraordinary circumstances.

### 5.5 Clearance Grant and Documentation

**5.5.1 Clearance Certificate**

Upon favorable adjudication, the HR Clearance Analyst shall issue a **Security Clearance Certificate** (generated in Workday SCM) containing:

- Holder's full name and Meridian employee/contractor ID;
- Clearance level (PCL-1, PCL-2, PCL-3);
- Date of grant;
- Expiration date (see Section 5.8);
- Any conditions or restrictions;
- HIPAA authorization indicator (yes/no) and expiration (if applicable);
- Certifying official's name and signature block;
- Unique clearance certificate identifier.

The certificate shall be stored in the employee's secure personnel file in Workday, with a copy available to the employee upon request. No paper copies shall be maintained.

**5.5.2 Central Clearance Registry**

HR-SCO shall maintain the **Central Clearance Registry**, a secure database within Workday SCM containing the current clearance status of all personnel. The Registry shall serve as the authoritative source for all access provisioning decisions.

### 5.6 Access Mapping

**5.6.1 Principle**

Access mapping is the process of provisioning specific logical and physical access rights based on an individual's clearance level, role, and need-to-know. Clearance alone does not grant access.

**5.6.2 Logical Access Provisioning**

Upon clearance grant, Workday SCM shall trigger an automated workflow to Okta (IAM) with the following data payload:

- Employee unique identifier;
- Clearance level (PCL-1, PCL-2, PCL-3);
- Role-Based Access Control (RBAC) group assignments derived from the employee's position in Workday;
- HIPAA authorization indicator;
- SR 11-7 governed role indicator;
- Clearance expiration date.

Okta shall execute automated provisioning rules as defined in the **Access Control Matrix** (maintained by InfoSec in SOP-IS-005). Provisioning shall be completed within **4 business hours** of the automated trigger for standard roles, and within **1 business hour** for roles requiring expedited access (e.g., clinical incident response personnel).

**5.6.3 Physical Access Provisioning**

Simultaneously, Workday SCM shall trigger a notification to the **Physical Security Management System** (LenelS2), authorizing the issuance of access badges programmed with the clearance-appropriate zone access. Access zone mapping is defined in SOP-PS-001 ("Physical Security and Access Control").

**5.6.4 Access Verification**

Within 3 business days of access provisioning, the sponsoring manager shall conduct an **Initial Access Verification** in Okta, confirming that the provisioned access is appropriate, complete, and does not exceed the role's need-to-know. The manager shall acknowledge the verification in Okta. Unacknowledged access grants shall be automatically suspended after 7 business days.

### 5.7 Periodic Reinvestigation (PR)

**5.7.1 Reinvestigation Schedule**

All personnel holding PCL-2 or PCL-3 clearances shall undergo periodic reinvestigation according to the following schedule:

| Clearance Level | Reinvestigation Interval | Trigger |
|-----------------|--------------------------|---------|
| PCL-2 | Every 3 years from date of grant or last PR | Automated Workday SCM notification at 180, 90, 60, and 30 days prior to expiration |
| PCL-3 | Every 2 years from date of grant or last PR | Automated Workday SCM notification at 180, 90, 60, and 30 days prior to expiration |
| PCL-2 or PCL-3 with Conditional grant | As specified in conditions (minimum annually) | Workday SCM tracking per condition schedule |

**5.7.2 PR Scope**

Periodic reinvestigation shall repeat the investigation components for the respective clearance level (Section 5.2.1), limited to the period since the last investigation or reinvestigation.

**5.7.3 Lapsed Reinvestigation**

If a reinvestigation is not completed by the clearance expiration date, the clearance shall automatically be downgraded to PCL-0 (no clearance), and all access requiring the higher clearance shall be suspended. Automatic suspension shall be executed by Workday SCM integration with Okta and LenelS2 with no manual override. The sponsoring manager, the HR-SCO Director, and InfoSec shall receive immediate notification.

**5.7.4 Reinvestigation Adjudication**

PR adjudication shall follow the same procedures as initial adjudication (Section 5.4), except that the individual maintains their currently granted clearance during PR processing unless derogatory information of Serious severity is discovered, in which case immediate clearance suspension (Section 5.9) shall apply.

### 5.8 Clearance Expiration and Renewal

**5.8.1 Clearance Validity Periods**

| Clearance Level | Standard Validity Period |
|-----------------|--------------------------|
| PCL-1 | Indefinite (subject to continuous employment and annual reaffirmation) |
| PCL-2 | 3 years |
| PCL-3 | 2 years |

The expiration date shall be calculated from the date of the favorable adjudication decision.

**5.8.2 Renewal Process**

Renewal follows the periodic reinvestigation process (Section 5.7). A new clearance certificate shall be issued upon successful PR adjudication, with a new expiration date calculated from the date of the PR adjudication decision.

### 5.9 Clearance Suspension and Revocation

**5.9.1 Mandatory Suspension Triggers**

Clearance shall be immediately suspended (temporary withdrawal of all access privileges) upon:

- (a) Notification of a felony arrest or indictment;
- (b) Discovery of a material falsification on the original BI submission;
- (c) Notification of active financial judgment exceeding $100,000 or bankruptcy filing (for PCL-3 holders with financial system access);
- (d) Credentialed report from InfoSec of anomalous access behavior exceeding defined thresholds (see SOP-IS-009, "Security Incident Response");
- (e) Formal written complaint of workplace violence, harassment, or unauthorized data access, pending investigation;
- (f) Failure to complete periodic reinvestigation by expiration date (automatic suspension, Section 5.7.3).

**5.9.2 Suspension Procedure**

- (a) The triggering party (HR-SCO, InfoSec, Legal & Compliance, or sponsoring manager) shall submit a **Clearance Suspension Request** in Workday SCM, documenting the specific derogatory information.
- (b) The HR-SCO Director (or CHRO for PCL-3 holders) shall make the suspension determination within **1 business day**.
- (c) Upon suspension determination, Workday SCM shall trigger immediate suspension of all logical access in Okta and badge deactivation in LenelS2.
- (d) The individual shall receive written notice of suspension (delivered in person or via secure electronic communication) specifying that the suspension is temporary pending investigation and that the individual is placed on administrative leave (if employee) or access-restricted status (if contractor/vendor).
- (e) An expedited investigation shall be initiated, with a target completion of 10 business days, after which the suspension shall be resolved to either reinstatement or revocation.

**5.9.3 Revocation**

Clearance revocation is permanent. Revocation follows the same adjudication pathway as initial clearance denial (Section 5.4.3) and carries the same adverse action notification requirements.

**5.9.4 Offboarding Clearance Termination**

Upon separation of employment or termination of contract, the clearance shall be formally terminated in Workday SCM. The separation date serves as the clearance termination date. All access provisioning shall be immediately revoked through the standard offboarding process (SOP-HR-002, "Employee Offboarding").

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control | Description | Reference |
|---------|-------------|-----------|
| **Segregation of Duties** | No single individual may both initiate a clearance request and adjudicate the resulting BI; HR Clearance Analysts adjudicating PCL-1 cases may not adjudicate their own requests | This SOP |
| **Least Privilege** | Access mapping (Section 5.6) provisions access at the minimum necessary level to perform role functions, consistent with the HIPAA Minimum Necessary Rule (45 CFR § 164.502(b)) | SOP-IS-005 |
| **Clearance Adjudication Board** | Multi-member adjudication body ensures no single individual has unilateral authority for PCL-3 and contested cases | Section 3.2 |
| **Background Investigation Documentation** | All BI reports, adjudication decisions, and supporting evidence shall be maintained as a complete, auditable record in Workday SCM | Records SOP (SOP-LEG-003) |

### 6.2 Technical Controls

| Control | Description |
|---------|-------------|
| **Workday SCM Access Control** | Role-based access to clearance data: HR Clearance Analysts (read/write for assigned cases), HR-SCO Director (read/write all), Hiring Managers (read-only for direct reports' clearance status), employees (read-only for own clearance certificate); all access logged |
| **Encryption** | All investigative data at rest encrypted with AES-256; data in transit encrypted with TLS 1.2 minimum |
| **API Security** | CRA integration (Acme, GlobalVet) via mTLS-authenticated API; all transmissions logged |
| **Okta IAM Integration** | Automated provisioning/suspension via SCIM 2.0 protocol; manual override requires dual authorization (sponsoring manager + InfoSec) |
| **Workday Audit Trail** | All clearance actions (request, BI initiation, adjudication, grant, suspension, revocation) timestamped with user identity; audit logs retained for 7 years |
| **Separation of Environments** | HR-SCO Workday SCM environment logically separated from general HR Workday environment; CRA data segregated in dedicated encrypted data store |

### 6.3 Physical Controls

| Control | Description |
|---------|-------------|
| **HR-SCO Secure Area** | HR Clearance Analysts operate from a badge-access-controlled suite within the HR facility; PCL-3 required for unescorted access |
| **Investigative Records** | No paper investigative records shall be created or maintained; all records electronic within Workday SCM |
| **Adjudication Board Meeting Space** | Adjudication Board meetings conducted in SCIF-equivalent secure conference room; no external devices permitted |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI | Definition | Target | Measurement Frequency |
|-----|------------|--------|------------------------|
| **BI Initiation Timeliness** | Percentage of BI investigations initiated within SLA from triggering event (Section 5.1.1) | ≥ 95% | Monthly |
| **BI Completion Timeliness** | Percentage of BI investigations completed within SLA (Section 5.2.2) | ≥ 90% | Monthly |
| **Adjudication Timeliness** | Mean time from BIR receipt to adjudication decision | PCL-1: ≤ 2 business days; PCL-2: ≤ 5 business days; PCL-3: ≤ 10 business days | Monthly |
| **Access Provisioning Timeliness** | Percentage of access provisioning completed within SLA from clearance grant (Section 5.6.2) | ≥ 98% | Monthly |
| **PR Completion Rate** | Percentage of periodic reinvestigations completed prior to clearance expiration | ≥ 95% | Quarterly |
| **Clearance Suspension Response Time** | Mean time from suspension trigger to access suspension execution | ≤ 4 business hours | Quarterly |
| **Clearance Accuracy** | Number of instances where post-grant review identifies inappropriate clearance level assignment | ≤ 2 per quarter | Quarterly |

### 7.2 Reporting

| Report | Content | Audience | Frequency | Delivery |
|--------|---------|----------|-----------|----------|
| **Clearance Operations Dashboard** | All KPIs, clearance inventory by level, aging investigations | HR-SCO Director, CHRO | Real-time | Workday SCM dashboard |
| **Quarterly Clearance Compliance Report** | Summary KPIs, PR compliance, derogatory finding trends, exception log | CHRO, CISO, Legal & Compliance | Quarterly | Written report |
| **Annual Clearance Program Review** | Comprehensive program metrics, regulatory alignment assessment, policy recommendations | CEO, CHRO, CISO, AI Governance Committee | Annually | Written report with presentation |
| **SOC 2 Control Evidence Package** | Clearance program documentation, investigation samples (de-identified), PR logs, exception approvals | External auditors | Per audit cycle | Secure data room |

### 7.3 Continuous Monitoring

**7.3.1** InfoSec shall maintain automated monitoring of logical access patterns for all PCL-2 and PCL-3 holders. Anomalous access patterns (off-hours access, unusual data volume queries, repeated unauthorized access attempts) shall trigger an alert to the HR-SCO Director and CISO, which may result in clearance suspension investigation per Section 5.9.

**7.3.2** The Central Clearance Registry shall be reconciled against Okta active user directories on a monthly basis by the Identity and Access Management team. Any clearance held by an individual without corresponding access, or access held without corresponding clearance, shall be flagged for immediate remediation.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

| Exception Type | Description | Approval Authority |
|----------------|-------------|---------------------|
| **Clearance Level Upgrade (Expedited)** | Request for clearance at a level higher than role mapping, on an expedited timeline | HR-SCO Director (PCL-1 to PCL-2); CHRO + CISO jointly (to PCL-3) |
| **Interim Clearance Beyond Standard** | Interim PCL-2 (standard interim is PCL-1 only); requires extraordinary business justification | CHRO + CISO + CEO jointly |
| **Conditional Grant Modification** | Request to modify or remove conditions on a Conditional grant prior to standard review period | Clearance Adjudication Board |
| **Waiver of Specific BI Component** | Request to waive a specific investigation component (e.g., credit check for non-financial role where legally permissible) | HR-SCO Director; CHRO if PCL-3 |
| **Clearance Reciprocity Acceptance** | Acceptance of a clearance granted by another authoritative entity (government agency, partner institution) | HR-SCO Director with InfoSec consultation |
| **Extended Expiration** | Request to extend clearance validity period without full PR | Not permitted — no exceptions to PR timing |

### 8.2 Exception Request Procedure

**8.2.1** The sponsoring manager shall submit an **Exception Request** in Workday SCM, containing:
- (a) Specific exception type requested;
- (b) Detailed business justification, including impact assessment if the exception is not granted;
- (c) Proposed compensating controls for the duration of the exception;
- (d) Proposed duration of the exception (if temporary).

**8.2.2** The HR Clearance Analyst shall review the request for completeness, append a recommendation, and route to the appropriate approval authority.

**8.2.3** The approval authority shall render a decision within:
- **1 business day** for expedited clearance upgrades (incident response);
- **3 business days** for all other exceptions.

**8.2.4** All approved exceptions, including justification, compensating controls, and approval, shall be documented in the **Exception Log** in Workday SCM, reviewed quarterly by Legal & Compliance.

**8.2.5** No exception shall permit access to PHI or ePHI without a completed, favorably adjudicated investigation at the depth specified for the clearance level (HIPAA § 164.308(a)(3)(ii)(B)). This prohibition is absolute and may not be waived.

### 8.3 Escalation Pathway

| Escalation Level | Trigger | Escalation Recipient | Response SLA |
|------------------|---------|----------------------|--------------|
| **Level 1** | Standard operational issue; BI delay beyond SLA; minor candidate dispute | HR-SCO Director | 2 business days |
| **Level 2** | Moderate derogatory finding without resolution; clearance suspension beyond 5 business days without resolution; repeated exception requests from same department | CHRO | 3 business days |
| **Level 3** | Serious derogatory finding involving potential criminal conduct; suspected data breach related to clearance failure; clearance denial disputed with legal representation | CEO, Chief Legal Counsel, CISO | 1 business day |

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Role | Training Module | Initial Training | Refresher Training | Assessment |
|------|-----------------|------------------|--------------------|------------|
| **HR Clearance Analysts** | HR-003-T1: "Security Clearance Operations" (full-day instructor-led) | Prior to system access; must pass written exam with ≥85% | Annually (half-day) | Written exam + practical adjudication simulation |
| **HR-SCO Director** | HR-003-T2: "Security Clearance Oversight and Adjudication" (2-day instructor-led) | Prior to assuming role | Annually | Written exam + adjudication board simulation |
| **Hiring Managers** | HR-003-T3: "Security Clearance Awareness for Managers" (eLearning, 45 minutes) | Within 30 days of hire or promotion to management role | Every 2 years | eLearning quiz (≥80% to pass) |
| **Clearance Adjudication Board Members** | HR-003-T2 plus HR-003-T4: "Advanced Adjudication: Whole-Person Concept Application" (half-day workshop) | Prior to first Board session | Annually | Workshop participation and case study |
| **All Personnel Holding PCL-2 or PCL-3** | HR-003-T5: "Security Clearance Holder Responsibilities" (eLearning, 30 minutes) | Within 15 days of clearance grant | Annually (as condition of clearance maintenance) | eLearning quiz (≥80% to pass; failure to complete results in clearance suspension) |

### 9.2 Training Content Requirements

All training modules shall include:
- (a) Explanation of Meridian clearance levels and their meaning;
- (b) Description of the clearance lifecycle (request, investigation, adjudication, grant, access mapping, reinvestigation, revocation);
- (c) Individual responsibilities of clearance holders, including duty to self-report derogatory information;
- (d) HIPAA-specific content (for roles with PHI access): overview of HIPAA Privacy and Security Rules, penalties for unauthorized disclosure, case examples of HIPAA violations;
- (e) Non-discrimination and Whole-Person Concept principles (for adjudicators);
- (f) Relevant SOPs and where to find them.

### 9.3 Training Tracking

All training completions, assessments, and expiration dates shall be recorded in Workday Learning. The HR-SCO Director shall review training compliance quarterly. Personnel who fail to complete required training within the specified timeframe shall have their clearance suspended until training is completed.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|--------|-------|--------------|
| SOP-IS-001 | "Information System Inventory and Classification" | Defines systems subject to clearance-based access |
| SOP-IS-005 | "Access Control Policy" | Detailed logical access provisioning, RBAC definitions, access review |
| SOP-IS-007 | "Data Classification and Handling" | Data classification schema referenced in clearance access mapping |
| SOP-IS-009 | "Security Incident Response" | Incident response procedures, anomalous access behavior thresholds |
| SOP-HR-001 | "Recruitment and Hiring" | Pre-offer procedures; integration with clearance initiation |
| SOP-HR-002 | "Employee Offboarding" | Clearance termination procedures upon separation |
| SOP-HR-006 | "Code of Conduct and Ethics" | Self-reporting obligations; conduct standards relevant to clearance |
| SOP-LEG-001 | "Non-Disclosure Agreement Policy" | NDA execution required for clearance |
| SOP-LEG-003 | "Records Retention and Disposition" | Retention schedules for investigative records |
| SOP-PS-001 | "Physical Security and Access Control" | Badge issuance, zone access mapping, physical access controls |
| SOP-RM-004 | "Third-Party Risk Management" | Vendor and contractor vetting integration |

### 10.2 External References

| Reference | Title | Applicability |
|-----------|-------|---------------|
| 45 CFR Part 164, Subpart C | HIPAA Security Standards for the Protection of Electronic Protected Health Information (Security Rule) | Workforce security (§ 164.308(a)(3)) |
| 45 CFR Part 164, Subpart E | HIPAA Privacy of Individually Identifiable Health Information (Privacy Rule) | Minimum necessary (§ 164.502(b)); uses and disclosures (§ 164.506) |
| 15 USC § 1681 et seq. | Fair Credit Reporting Act (FCRA) | Background investigation consumer report procedures |
| Regulation (EU) 2016/679 | General Data Protection Regulation (GDPR) | Processing of EU data subject information; DPIA (Art. 35) |
| Regulation (EU) 2017/745 | Medical Device Regulation (MDR) | Clinical AI product personnel suitability |
| TSC 2017 (2022 Revision) | AICPA Trust Services Criteria for SOC 2 | CC6.1–CC6.8 (Logical and Physical Access Controls); CC7.1–CC7.5 (System Operations — Availability) |
| ISO/IEC 27001:2022 | Information Security Management Systems — Requirements | A.5.15 (Access Control), A.6.1 (Screening), A.6.2 (Terms and Conditions of Employment) |
| NIST SP 800-53 Rev. 5 | Security and Privacy Controls for Information Systems and Organizations | PS-3 (Personnel Screening), PS-4 (Personnel Termination), AC-1 through AC-6 (Access Control) |

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
|---------|------|--------|------------------------|
| 1.0 | 2019-03-15 | M. Chen (Interim HR Director) | Initial policy; established PCL-1 through PCL-3 schema; manual clearance processing (pre-Workday) |
| 2.1 | 2020-01-10 | J. Walsh (CHRO) | Full revision; incorporation of HIPAA Workforce Security Authorization; Clearance Adjudication Board established |
| 3.0 | 2021-06-01 | J. Walsh; T. Eberhardt (HR-SCO Director) | Migration to Workday SCM; automated Okta provisioning; interim clearance procedures added |
| 3.4 | 2022-09-20 | T. Eberhardt | EU GDPR compliance provisions added; GlobalVet GmbH as EU CRA; DPIA requirement |
| 4.0 | 2023-11-15 | J. Walsh; T. Eberhardt; InfoSec CISO | PCL-3 enhanced controls for AI Governance; SR 11-7 governed roles; Whole-Person Concept adjudication formalized; PR schedules refined |
| 4.5 | 2024-08-22 | T. Eberhardt | CE marking and EU MDR 2025 compliance alignment; clinical AI access controls expanded; adverse action notification updates |
| 4.8 | 2025-07-28 | J. Walsh; T. Eberhardt | Comprehensive review; HIPAA § 164.308 controls cross-referenced with precision; exception handling tightened (no PR waivers); training module IDs assigned; SOC 2 controls narratives updated; psychological evaluation trigger for clinical AI roles; CEO review added for PCL-3 denials |

---

**Document Control Statement:** This document is classified as **Internal**. It may be accessed by Meridian personnel and authorized contractors as necessary for the execution of their duties. It shall not be distributed externally without the written authorization of the Chief Human Resources Officer or Chief Legal Counsel. Printed copies are uncontrolled; the authoritative version is maintained in the Meridian Document Management System (Workday Documents).

**Compliance Statement:** All personnel are required to comply with this SOP. Non-compliance shall be reported to the HR-SCO Director and may result in clearance suspension or revocation, disciplinary action up to and including termination of employment, and referral to Legal & Compliance for regulatory violation assessment.

*End of SOP-HR-003 (Version 4.8)*
</output>