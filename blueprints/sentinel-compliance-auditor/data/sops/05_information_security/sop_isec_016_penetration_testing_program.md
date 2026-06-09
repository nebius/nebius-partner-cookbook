---
sop_id: "SOP-ISEC-016"
title: "Penetration Testing Program"
business_unit: "Information Security"
version: "2.7"
effective_date: "2025-02-21"
last_reviewed: "2026-10-07"
next_review: "2027-04-24"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Penetration Testing Program

**SOP-ID:** SOP-ISEC-016
**Version:** 2.7
**Effective Date:** 2025-02-21
**Owner:** Rachel Kim, Chief Information Security Officer
**Classification:** Internal

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the formal framework for the Penetration Testing Program at Meridian Health Technologies, Inc. The program is designed to proactively identify, validate, and facilitate the remediation of security vulnerabilities across the organization's technology ecosystem. By simulating real-world adversarial attack scenarios, the program validates the effectiveness of existing security controls, identifies gaps in the defense-in-depth strategy, and provides actionable intelligence to continuously improve the organization's security posture. This program directly supports compliance obligations, including model risk management under SR 11-7 for HealthPay Financial Services and safeguarding electronic Protected Health Information (ePHI) under HIPAA.

### 1.2 Scope
The Penetration Testing Program applies to all information systems, cloud environments, applications, and network components owned, operated, or leased by Meridian Health Technologies. The scope is explicitly defined annually in a Penetration Testing Roadmap (document template **FRM-ISEC-016A**) and includes, but is not limited to:

- **SaaS Platform Infrastructure:** Multi-tenant AWS environments (`us-east-1`, `eu-west-1`), Azure DR instances, virtual private clouds (VPCs), container orchestration (Kubernetes/EKS), and serverless functions.
- **Clinical AI Platform:** High-risk AI systems as classified under the EU AI Act Annex III, including model endpoints, training pipelines (MLflow, SageMaker), and inference APIs. Testing must validate resilience against adversarial machine learning (ML) attacks, including model inversion, data poisoning, and evasion techniques.
- **HealthPay Financial Services:** High-velocity transactional systems processing over $4.2B annually, including payment gateways, medical lending origination platforms, and credit scoring models subject to SR 11-7 model risk management.
- **MedInsight Analytics:** Data warehousing environments (Snowflake), data lakes containing ePHI for ~12M patients, and associated Extract, Transform, Load (ETL) pipelines.
- **Corporate Systems:** Identity platforms (Okta), endpoint management, corporate WiFi, VPN gateways, and SaaS business tools (G-Suite, Slack Grid) used by the workforce of 1,400+ employees.
- **External Attack Surface:** All internet-facing assets, domain registrar accounts, DNS configurations, and third-party integrations.

**Out of Scope:** Physical security (e.g., badge reader cloning, mantrap bypass) is managed under **SOP-PHYS-004**. Social engineering simulations, including phishing campaigns, are managed by the Security Awareness Team under **SOP-ISEC-019**. Business Continuity and Disaster Recovery testing, including failover to Azure DR, is managed under **SOP-ISEC-022**; however, this Penetration Testing Program validates the logical isolation and integrity of those replicated assets where logical access mechanisms are concerned. In the context of our SOC 2 availability commitments, testing validates the availability of critical security controls, but specific quantitative Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) are outside the scope of this SOP's testing methodology and are addressed conceptually in operational continuity discussions.

---

## 2. Definitions and Acronyms

### 2.1 Key Definitions
The following terms are critical to the interpretation and execution of this SOP:

| Term | Definition |
| :--- | :--- |
| **Adversarial ML Testing** | Specialized penetration testing targeting ML models to subvert confidentiality (model extraction), integrity (data poisoning, adversarial examples/evasion), or availability (sponge attacks). |
| **Black Box Testing** | Testing performed with no prior knowledge of the target system's internal architecture or source code, simulating an external, uninformed attacker. |
| **Crown Jewel Analysis** | A threat modeling exercise conducted bi-annually to identify the specific data assets and systems whose compromise would have the most catastrophic business impact. |
| **Critical Finding** | A vulnerability that allows unauthenticated remote code execution, direct access to the ePHI data lake boundary, or compromise of code-signing infrastructure. |
| **Environment Drift** | Unmanaged configuration changes to infrastructure-as-code (IaC) deployed components, identified via repeatable automated security tests. |
| **Purple Team Exercise** | A collaborative testing methodology where the Security Operations Center (SOC) defenders (Blue Team) are given real-time visibility into the actions of the Penetration Testers (Red Team) to measure detection efficacy against specific attack chains identified in penetration tests, rather than full surreptitious emulation. |
| **Retesting** | Verification testing conducted exclusively to validate that a previously identified finding has been successfully remediated and can no longer be exploited. |
| **Segregation Test** | Validated attempt to traverse from a lower-security enclave (e.g., PCI-DSS cardholder data environment) to the corporate LAN or other restricted zones. |

### 2.2 Acronyms

| Acronym | Definition |
| :--- | :--- |
| **APT** | Advanced Persistent Threat |
| **CDE** | Cardholder Data Environment |
| **CISO** | Chief Information Security Officer |
| **CVSS** | Common Vulnerability Scoring System |
| **ePHI** | Electronic Protected Health Information |
| **EKS** | Elastic Kubernetes Service (AWS) |
| **MDR** | Medical Device Regulation (EU) |
| **PoC** | Proof of Concept (vulnerability exploitation) |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **SRT** | Security Remediation Ticket |
| **WAF** | Web Application Firewall |

---

## 3. Roles and Responsibilities

A clear RACI matrix ensures accountability for each phase of the penetration testing lifecycle.

| Activity / Task | Penetration Testing Lead (InfoSec) | Third-Party Testing Vendor | System/App Owner (Engineering) | CISO (Rachel Kim) | Cloud Security Architect | Legal & Compliance |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Annual Scoping & Roadmap** | R, A | C | C | I | C | I |
| **Rules of Engagement Definition** | R | C | I | A | C | R (EU MDR, SR 11-7) |
| **Penetration Test Execution** | I | R | C | I | C | I |
| **Finding Triage & Validation** | R | C | R | I | C | I |
| **Remediation Assignment (Jira SRT)** | R | I | A | I | C | I |
| **Risk Acceptance (Exception)** | I | I | R | A | I | C (GDPR Art. 32) |
| **Adversarial ML Model Testing** | I | R (Specialist) | C (MLOps Team) | A | I | C |
| **Retesting Validation** | R | R | I | A | I | I |

### 3.1 Named Roles

- **Chief Information Security Officer (CISO), Rachel Kim:** Holds ultimate accountability for the program's execution, resource allocation, and risk acceptance. Approver of the Annual Roadmap and any Critical findings requiring indefinite deferral.
- **Penetration Testing Lead (InfoSec):** Responsible for operational management of the program, scoping, vendor liaison, internal Purple Team logistics, and quality assurance of deliverables.
- **MLOps Engineering Lead:** Responsible for granting context-specific, sandboxed testing access to model replicas for Adversarial ML testing and for the remediation of model-level findings.
- **Site Reliability Engineering (SRE) Director:** Responsible for the remediation of infrastructure-level findings in AWS and Azure, including Kubernetes node hardening and IAM policy corrections.

---

## 4. Policy Statements

Meridian Health Technologies commits to the following high-level policy directives:

- **P-01: Risk-Based Cadence.** An enterprise-wide, full-scope internal and external penetration test shall be conducted at a minimum frequency of once per calendar year. High-velocity Financial and Clinical AI systems shall undergo additional continuous or semi-annual focused assessments.
- **P-02: Independent Execution.** All formal penetration testing required for regulatory compliance attestation (SOC 2, HIPAA) must be performed by a qualified, independent third-party firm with no conflict of interest in the architecture or management of the tested systems.
- **P-03: Production Safety.** Penetration testing in production environments must adhere to strict Rules of Engagement to avoid disruption to clinical decision support systems (availability) and financial transaction integrity (financial loss). Denial-of-Service (DoS) testing is strictly prohibited against production payment gateways.
- **P-04: Scope Assurance.** The scope of every penetration test must include the entire external attack surface, internal network segmentation controls protecting the ePHI data lake, and Application Programming Interface (API) endpoints serving the mobile health applications.
- **P-05: Model Integrity.** Systems classified as High-Risk AI under EU MDR must, as part of their scheduled testing, undergo specific Adversarial ML resilience evaluation to validate input sanitization and model theft protections.
- **P-06: Remediation Mandate.** All validated findings must be tracked to closure either via remediation (fix) or formal, documented risk acceptance.
- **P-07: Confidentiality.** All raw penetration testing reports, vulnerability logs, and exploitation videos are classified as "Internal - Secret" and must be stored exclusively within the InfoSec PGP-encrypted drive and not on broadly accessible Confluence spaces.

---

## 5. Detailed Procedures

### 5.1 Penetration Testing Lifecycle

Testing shall follow a standardized seven-phase lifecycle to ensure rigor, safety, and business integration.

#### 5.1.1 Phase 1: Annual Scoping and Roadmap Development
**Timeline:** Completed no later than February 1st for the calendar year.
**Procedure:**
1.  The **Penetration Testing Lead** exports the complete asset inventory from the Configuration Management Database (ServiceNow CMDB).
2.  The **CISO** and **Cloud Security Architect** conduct a Crown Jewel Analysis, pinpointing assets containing the highest concentrations of ePHI (MedInsight Snowflake instances) and transactional records (HealthPay Aurora clusters).
3.  The Penetration Testing Lead creates the Penetration Testing Roadmap (**FRM-ISEC-016A**), defining three distinct testing vectors for the year:
    - **Vector Alpha (External Attack Surface):** All domains, subdomains, VPN gateways, and cloud buckets with public ingress.
    - **Vector Beta (Internal Assumed Breach):** Simulating a compromised workstation on the corporate LAN to test lateral movement to clinical data stores and HealthPay CDE.
    - **Vector Gamma (Application Deep Dive):** A full OWASP ASVS Level 3 assessment of the MedInsight Patient Portal API and the Clinical AI Inference API.
4.  The draft Roadmap is reviewed by System Owners and the SRE Director for potential resource constraints (e.g., production freeze periods).
5.  The finalized Roadmap is approved by the CISO.

#### 5.1.2 Phase 2: Vendor Selection and Onboarding
**Procedure:**
1.  The Penetration Testing Lead issues a Request for Proposal (RFP) using template **FRM-ISEC-016C** to the approved vendor panel. The panel is refreshed biennially.
2.  RFP evaluation criteria must include proven experience in container orchestration security (Kubernetes/EKS) and API Security, weighted at 40% of the scoring.
3.  The selected vendor must sign the Meridian Non-Disclosure Agreement (NDA) and a Data Processing Addendum (DPA) that explicitly confines ePHI exposure. The DPA must outline that any incidental exposure of ePHI during testing is subject to the breach notification window of 72 hours.

#### 5.1.3 Phase 3: Rules of Engagement (RoE) and Authorizations
**Procedure:**
1.  The Penetration Testing Lead drafts the RoE document (**FRM-ISEC-016E**), specifying:
    - **Allowed IP Addresses:** Source IPs of vendor testing rigs.
    - **Permitted Attack Techniques:** Categorized by infrastructure, web app, API, and cloud. SQL Injection and Cross-Site Scripting are permitted; destructive techniques (e.g., data deletion `DROP TABLE`, ransomware simulation against production storage) are strictly forbidden.
    - **Restricted Assets:** Explicitly exclude certain brittle legacy clinical gateway boxes identified by the Clinical Engineering team from scanning that could cause buffer overflows.
2.  The RoE must include the formal "Authorization to Attack" section, signed by the **CISO** and the **Chief Technology Officer.**
3.  The vendor must provide a "Go-Live" notification exactly 24 hours before testing commences.

#### 5.1.4 Phase 4: Internal and External Execution
**Procedure:**
1.  **External Testing (Vector Alpha):** Commences with reconnaissance, subdomain enumeration via Amass, and port scanning against the public `52.x.x.0/22` CIDR range.
2.  **Internal Testing (Vector Beta):** A purpose-built, hardened "pivot box" is deployed onto the `CORP-CLIENT-VLAN` (10.24.10.0/24). The vendor connects via an ephemeral WireGuard tunnel to this pivot box. Segregation testing shall focus on accessing the `10.24.200.0/24` subnet (PCI High-Security Zone).
3.  **Adversarial ML Testing (Specific to Clinical AI, SOP-ML-023):** The vendor creates surrogate models against the public API. They attempt Model Extraction via high-frequency querying of the clinical prediction response. The MLOps team monitors inference latency; if latency spikes exceed 40%, testing is paused to diagnose a potential model availability compromise.

#### 5.1.5 Phase 5: Triage and Validation
**Procedure:**
1.  The vendor submits findings via the secure portal daily.
2.  The **Penetration Testing Lead** triages each finding within **24 business hours**, removing false positives and validating the exploitation path.
3.  Valid findings are cross-referenced against the vulnerability management platform (DefectDojo / Wiz) to identify systemic issues (e.g., container escape due to shared Kernel).
4.  A "Proof of Concept" (PoC) script is embedded into the finding record to ensure repeatable validation.

#### 5.1.6 Phase 6: Remediation Tracking
**Procedure:**
1.  Validated findings are replicated into Jira using the `Security Remediation Ticket (SRT)` project.
2.  The ticket is assigned to the **System Owner** and the **SRE Director**.
3.  **Service Level Agreements (SLAs) commence:**
    - **Critical (CVSS 9.0 - 10.0):** Remediation effort must commence within **24 hours**. Verification must be complete within **7 calendar days**. (Example: Public S3 bucket containing raw MedInsight data allowing anonymous read).
    - **High (CVSS 7.0 - 8.9):** Verification complete within **30 calendar days**. (Example: AWS API Keys leaked via a public git repository granting access to non-production Dev environment).
    - **Medium (CVSS 4.0 - 6.9):** Verification complete within **90 calendar days**.
    - **Low / Informational:** Remediation scheduled in standard sprint cycles.
4.  The Penetration Testing Lead tracks the Remediation Burndown Chart weekly.

#### 5.1.7 Phase 7: Retesting and Audit Trail Closure
**Procedure:**
1.  Upon the System Owner marking the Jira SRT as "Resolved," the **Third-Party Vendor** conducts verification retesting.
2.  If the remediation is effective, the vendor marks the ticketing log as "Closed - Verified."
3.  If the remediation is ineffective or bypassed, the Jira SRT is re-opened with the bypass PoC and reassigned.
4.  A final Attestation Report (**FRM-ISEC-016R**) is generated by the vendor and signed by the CISO, providing the annual evidence required for the SOC 2 Type II and HIPAA audit.

### 5.2 Adversarial Machine Learning Specifics

This additional procedure applies specifically to the Clinical AI Platform.

1.  **Model Theft Assessment:** Using a custom script, the vendor probes the public prediction API to extract model parameters. Internal monitoring dashboards in Grafana track entropy rates. Rate limiting at the API Gateway (Kong) must be tuned during this phase.
2.  **Evasion Attack Validation:** The vendor crafts adversarial noise patterns (perturbations) to bypass the diagnostic classification model. The MLOps Team deploys the `defense_gan` pre-filter to validate resilience.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls
The following technical controls shall be activated and validated during each penetration test cycle:

- **Network Micro-Segmentation (Illumio Core):** Validated by internal lateral movement tests (Phase 4, Vector Beta). Tests confirm that unauthorized egress from the PCI-DSS High-Security Zone to the corporate wireless VLAN is blocked.
- **Web Application Firewall (AWS WAF + Imperva):** Validation ensures that the WAF blocks the OWASP Top 10 injection payloads sent during external testing without impacting legitimate clinical imaging upload traffic.
- **API Gateway Rate Limiting (Kong):** Specifically tested during Model Theft Assessments to ensure that excessive querying from a single public IP triggers progressive throttling and temporary blacklisting.
- **Endpoint Detection and Response (CrowdStrike Falcon):** During internal testing, the SOC measures the "Breakout Time." The penetration testing vendor attempts to run a common Mimikatz variant; Falcon must detect and kill the process within its configured SLA.

### 6.2 Administrative Controls
- **Access Review During Remediation:** During the remediation phase for lateral movement findings, the InfoSec team reviews the effectiveness of network segmentation as a logical access control, analyzing if unauthorized cross-VLAN traversal occurred during the simulation.
- **Audit Trails:** All penetration testing activity logs (vendor IP connections, executed commands, timestamps) are centralized into S3 immutable logging buckets. These logs serve as crucial audit controls, providing evidence that testing activity originated from authorized, segmented locations and not from an actual malicious intrusion masquerading as a test.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
The effectiveness of the Penetration Testing Program is measured against the following quantitative metrics, reported quarterly to the Risk and Compliance Committee:

| Metric | Target | Measurement Tool |
| :--- | :---: | :--- |
| **Critical Finding Remediation within SLA** | ≥ 99% | Jira SRT Dashboard |
| **High Finding Remediation within 30-Day SLA** | ≥ 90% | Jira SRT Dashboard |
| **Retesting Efficiency (Findings verified per week)** | > 15 | Vendor Weekly Status Report |
| **Detection Rate (Simulated Attacks)** | ≥ 85% | SOC Purple Team Analysis |
| **Model Theft Resilience Score** | > 9.0 / 10.0 | Adversarial Robustness Toolbox |

### 7.2 Management Dashboards and Cadence
1.  **Operational Dashboard (Live):** A real-time dashboard, built on Jira Gadgets and displayed on the InfoSec NOC screens, tracks remediation tickets approaching or breaching SLA. This dashboard is reviewed daily by the Penetration Testing Lead.
2.  **Monthly Remediation Status Report:** An automated report distributed to Engineering Directors listing all open, unverified findings against their business unit.
3.  **Quarterly Business Review (QBR):** The CISO presents a consolidated state of the program to the CEO and the Board Audit Committee, including:
    - Executive summary of the most recent large-scale penetration test.
    - Risk heat map of non-remediated findings.
    - Trends in Environment Drift identified via retesting failures.

---

## 8. Exception Handling and Escalation

### 8.1 Risk Acceptance Process
There are scenarios where immediate remediation is operationally impossible (e.g., a critical legacy API that cannot support TLS 1.3). In these cases:
1.  The **System Owner** must complete a Security Risk Acceptance Request (**FRM-ISEC-016X**).
2.  The form must detail the technical rationale, a compensating control (e.g., isolating the legacy API within a severely restricted micro-segment that disallows any lateral movement), and a binding sunset date for ultimate remediation or decommissioning.
3.  **Approval Authority:**
    - **CVSS Medium (4.0 - 6.9) Risk:** Approved by the Penetration Testing Lead.
    - **CVSS High (7.0 - 8.9) Risk:** Approved by the CISO. Maximum acceptance duration is **90 days**.
    - **CVSS Critical (9.0 - 10.0) Risk:** Approval requires a joint sign-off from the CISO and the Chief Architect. Maximum acceptance duration is **30 days**, subject to weekly review. No Critical finding involving direct exposure of ePHI can be accepted for more than 7 days without an internal breach notification filed.

### 8.2 Escalation Matrix
If a System Owner fails to respond to a Critical remediation assignment within 4 hours:
1.  The Penetration Testing Lead escalates to the **VP of Engineering**.
2.  If no acknowledgment occurs within 24 hours, the CISO is authorized to unilaterally revoke the affected system's production access via security automation runbooks to enforce isolation, thereby securing availability for the broader platform, even if that specific component's uptime is compromised.

---

## 9. Training Requirements

### 9.1 Secure Coding and OWASP Training
All software engineers, data engineers, and DevOps personnel identified as System Owners or Remediation Assignees must complete annual training:
- **Course:** Meridian Internal "Secure Coding for HealthTech" (LMS-MTH-201) and an external OWASP Top 10 Advanced Course.
- **Timing:** Completion must be recorded in the Litmos Learning Management System (LMS) within 45 days of the fiscal year start (Feb 15).
- **Non-Compliance:** System Owners who are out of compliance with training are not eligible to receive exceptions (see Section 8) for penetration test findings.

### 9.2 Adversarial ML Awareness
ML Engineers (MLOps) working on the Clinical AI models must complete the specialized "AIML Security Testing Fundamentals" workshop biennially, which covers adversarial perturbations and model poisoning defenses.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies
The Penetration Testing Program operates in conjunction with the following Meridian SOPs:

| Reference ID | Document Title | Relationship |
| :--- | :--- | :--- |
| **SOP-ISEC-003** | Vulnerability and Patch Management Standard | Defines the routine process for scanner-based flaws; Penetration Testing captures the exploitable logic flaws missed by scanners. |
| **SOP-ISEC-009** | Incident Response Plan | Penetration Testing activities inadvertently triggering an Incident Response playbook (e.g., an aggressive scan crashes a clinical gateway) must follow this plan. |
| **SOP-ISEC-019** | Security Awareness & Phishing Program | Social engineering and phishing are excluded from Pen Testing and covered by this SOP. |
| **SOP-ISEC-022** | Disaster Recovery and Business Continuity | DR/BC testing validates environment recreation; Pen Testing validates that the recreated environment is secure and logically isolated. |
| **SOP-DEV-044** | Secure SDLC & Code Promotion | Findings must feed into the secure development lifecycle to prevent recurrence. |
| **SOP-ML-023** | Clinical AI Model Lifecycle Management | Defines the model versioning and A/B testing framework required for adversarial testing without impacting production diagnostic stability. |
| **SOP-CMP-007** | Data Classification and Handling | Defines the ePHI and PCI data classification schemas that inform Crown Jewel targeting. |

### 10.2 External Regulatory & Framework Mapping
- **SOC 2 (Trust Services Criteria - CC7.1):** Internal and external penetration tests serve as detective controls to verify that the system of internal control is operating effectively to meet security and availability commitments. The program validates the logical access controls restricting entry to the production enclaves.
- **HIPAA (45 CFR § 164.312):** The penetration testing acts as a mechanism to verify that technical security measures appropriately protect against accessing ePHI. Audit trails and access reports generated from the penetration test activities serve as supporting evidence that ePHI access is monitored and controlled.
- **PCI-DSS (Requirement 11.4):** External penetration testing validates segmentation controls and external defense of the CDE, defined by the HealthPay perimeter.
- **EU Medical Device Regulation (EU MDR) 2017/745:** Testing ensures the clinical AI platform's software life cycle processes include an assessment of cybersecurity risk leading to unacceptable residual risk.
- **NIST SP 800-115:** Technical Guide to Information Security Testing and Assessment (Adopted as the core methodological framework).
- **OWASP ASVS 4.0:** Application Security Verification Standard (Level 2/3, adopted for Clinical API deep dive assessments).

---

## 11. Revision History

| Version | Date | Author | Revision Summary |
| :--- | :--- | :--- | :--- |
| **2.7** | **2026-10-07** | Rachel Kim, CISO | Full biennial review. Updated Section 5.1.3 RoE to formally restrict destructive DoS testing against the upgraded Aurora Financial DB. Updated Section 5.1.4 to mandate WireGuard tunnel for internal pivot. Added adversarial ML validation specifics in Section 5.2 to align with new FDA/EU MDR cybersecurity guidances. |
| **2.6** | **2026-04-15** | Marcus Thorne, Penetration Testing Lead | Modified Section 6.1 technical controls to include the new Kong API Gateway rate limit parameters. Streamlined the Risk Acceptance workflow in Section 8.1 based on Q1 audit feedback. |
| **2.5** | **2025-02-21** | Rachel Kim, CISO | Major revision. Formally integrated the HealthPay Financial Services environment (PCI-DSS) and MedInsight Analytics data lake into the mandated internal testing scope. Changed minimum frequency from bi-annual to annual for full-scope testing, with semi-annual mandates for high-velocity assets only. Implemented the new Jira SRT tracking project (Section 5.1.6). |
| **2.1** | **2024-04-17** | Marcus Thorne, Penetration Testing Lead | Minor revision. Updated asset inventory reference to ServiceNow CMDB. Clarified secure storage location (Section 4 P-07) following internal data spillage incident. |
| **2.0** | **2023-09-01** | Sarah Jenkins, Former CISO | Initial enterprise rollout. Replaced siloed product-specific manual assessments with a centralized, unified Lifecycle methodology. Formalized the "Authorization to Attack" sign-off procedure. |