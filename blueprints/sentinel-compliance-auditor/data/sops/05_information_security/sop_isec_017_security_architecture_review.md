---
sop_id: "SOP-ISEC-017"
title: "Security Architecture Review"
business_unit: "Information Security"
version: "1.3"
effective_date: "2024-02-25"
last_reviewed: "2025-07-13"
next_review: "2026-01-25"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Security Architecture Review

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish a formal, repeatable, and auditable process for conducting Security Architecture Reviews (SARs) across all technology initiatives at Meridian Health Technologies, Inc. This SOP defines the methodology by which the Information Security team evaluates the security posture of proposed and modified systems, applications, network segments, cloud configurations, and third-party integrations to ensure that security is designed in from inception, rather than retrofitted after deployment.

The Security Architecture Review process serves as a proactive governance gate within the Meridian Software Development Lifecycle (SDLC) and Infrastructure Change Management processes. It ensures that all architectural decisions align with Meridian's internal security policies, regulatory obligations, and industry best practices, including but not limited to SOC 2 Trust Services Criteria, the NIST AI Risk Management Framework, and relevant provisions of HIPAA, GDPR, and the EU AI Act.

### 1.2 Scope

This SOP applies to all technology-related projects, significant changes, and new initiatives within Meridian Health Technologies, including:

| In-Scope Activity | Examples |
|---|---|
| New Product Development | Launch of a new MedInsight Analytics module, new HealthPay API endpoint |
| Major Feature Enhancements | Addition of a new ML model to the Clinical AI Platform, new payment rail integration |
| Cloud Infrastructure Changes | Provisioning new AWS accounts, VPC peering, cross-region replication for eu-west-1 |
| Third-Party Integrations | Integrating a new SaaS vendor for claims processing, new data processor for PHI |
| Architectural Pattern Changes | Migration from monolithic to microservices, adoption of new messaging queue topology |
| Data Flow Modifications | New PHI data flows between Meridian SaaS Platform and an external partner, new analytics pipeline using Snowflake |
| Merger & Acquisition Technology Integration | Onboarding technology stacks from acquired entities |
| Significant Configuration Drift Remediation | Architectural rework stemming from audit findings |

This SOP applies to the following Meridian business units and departments:

- Clinical AI Platform Engineering (Dr. Aisha Okafor)
- HealthPay Financial Services Engineering (Robert Liu)
- MedInsight Analytics Engineering (David Park)
- Meridian SaaS Platform / IT Operations (Samantha Torres)
- All product development teams utilizing AWS, Azure, or on-premises resources
- Vendor Management, as it pertains to technical integration architecture

This SOP does **not** apply to:

- Routine operational changes managed via standard change management (e.g., OS patching within defined baselines, scaling existing AWS Auto Scaling Groups within approved limits, standard user provisioning via Okta).
- Minor UI text changes or cosmetic updates with no bearing on data handling or access controls.
- Emergency changes executed under SOP-ISEC-005 (Incident Response); however, a retrospective SAR must be completed within 5 business days of incident closure.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **SAR** | Security Architecture Review. The formal process defined by this SOP. |
| **STRIDE** | Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege. The primary threat modeling methodology adopted by Meridian. |
| **Architecture Review Board (ARB)** | A cross-functional governance body responsible for reviewing and approving significant architectural decisions. |
| **Security Design Pattern** | A reusable solution to a commonly occurring security problem within a specific context (e.g., API Gateway pattern, Mutual TLS pattern, Event Sourcing for audit logs). |
| **CIA Triad** | Confidentiality, Integrity, Availability. |
| **Trust Services Criteria (TSC)** | The control criteria used in SOC 2 examinations, categorized as Common Criteria (CC series) and supplementary criteria for Availability, Confidentiality, Processing Integrity, and Privacy. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **PII** | Personally Identifiable Information, as defined by GDPR and other privacy regulations. |
| **DPIA** | Data Protection Impact Assessment. Owned by the Privacy Office (Dr. Klaus Weber). Often a parallel or prerequisite activity to the SAR. |
| **SR 11-7 / MRM** | Supervisory Guidance on Model Risk Management. Applies to HealthPay Financial Services models. |
| **High-Risk AI System** | Classification under the EU AI Act (Annex III) applicable to Meridian's Clinical AI Platform products. |
| **Security by Design** | The principle of embedding security considerations into every phase of system development and architecture. |
| **Terraform / IaC** | Infrastructure as Code. The primary method by which Meridian provisions and manages cloud infrastructure. |
| **SDLC** | Software Development Lifecycle. The Meridian SDLC is defined in SOP-ENG-003. |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework. |
| **Data Classification** | Meridian data classification schema: Public, Internal, Confidential, Restricted (PHI/PII/payment card data). |

## 3. Roles and Responsibilities

The following RACI matrix defines the roles involved in the Security Architecture Review process.

| Role | SAR Request | Threat Modeling | Security Assessment | ARB Review / Approval | Exception Approval |
|---|---|---|---|---|---|
| **Requesting Solution Architect / Lead Engineer** | **R** | C | C | C | I |
| **Information Security Officer (CISO)** - Rachel Kim | I | I | I | A | **R** |
| **Senior Security Architect** | A | **R** | **R** | C | C |
| **Security Engineering Team** | I | C | C | I | I |
| **Business Unit Engineering Lead** (e.g., VP FinTech, Dir. AI Platforms) | C | C | C | **R*** | I |
| **Chief Privacy Officer** - Dr. Klaus Weber | C | C | C | C | C |
| **VP of Engineering** - David Park | A | I | I | **R** | A |
| **Chief Technology Officer (CTO)** | I | I | I | A | A |
| **Internal Audit** | I | I | I | I | I |

**R = Responsible (executes the task); A = Accountable (signs off / ultimate ownership); C = Consulted (two-way communication); I = Informed (one-way communication)**
*Note: The Business Unit Engineering Lead is Responsible for presenting their architectural proposal to the ARB, not for the security assessment itself.

### 3.1 Specific Named Responsibilities

- **Rachel Kim, CISO:** Ultimate owner of this SOP. Has authority to approve or deny any architectural change based on security risk. Approver for all high-risk exceptions.
- **Senior Security Architect:** Operationally responsible for executing the SAR process, facilitating threat modeling sessions, validating implementation of security controls post-approval, and maintaining the library of approved Security Design Patterns.
- **David Park, VP of Engineering:** Accountable for ensuring all Engineering teams under his purview adhere to the SAR process. Co-chairs the ARB.
- **Dr. Klaus Weber, Chief Privacy Officer:** Mandatory consult for any architecture involving a new collection, storage, processing, or transmission of PII/PHI, triggering a parallel DPIA.

## 4. Policy Statements

Meridian Health Technologies is committed to a "Security by Design" philosophy. The following policy statements form the non-negotiable foundation of the SAR process:

1.  **Mandatory Review Gate:** No new product, significant feature, or material infrastructure change shall progress to production deployment without a formally approved and documented Security Architecture Review. The SAR is a mandatory "Go/No-Go" gate in the Meridian SDLC (SOP-ENG-003) and the formal Change Management process (SOP-ISEC-011).
2.  **Risk-Based Approach:** The depth and rigor of a SAR will be calibrated based on the inherent risk of the proposed change, assessed against the CIA Triad and the sensitivity of data involved. All reviews, regardless of depth, will culminate in a formal, documented risk acceptance or rejection.
3.  **Use of Approved Patterns:** Engineering teams must default to using Meridian-approved Security Design Patterns. Deviations from approved patterns are permissible only with explicit, documented approval from the CISO or Senior Security Architect, justified by a specific business or technical constraint.
4.  **Separation of Duties:** To maintain the integrity of our architecture governance, the individual architecting a solution **must not** be the sole performer of its security review. The Security Architecture Review process, as an independent function of the Information Security team, provides this segregation of duties.
5.  **Threat Modeling as a Standard:** All architectures classified as "Medium" or "High" inherent risk **must** undergo a structured threat modeling exercise, using the STRIDE methodology.
6.  **Continuous Compliance:** Security Architecture is not a one-time snapshot. All approved architectures are subject to continuous monitoring and periodic review to ensure ongoing compliance with the approved security posture. Material architectural drift is a violation of this policy.

## 5. Detailed Procedures

This section outlines the step-by-step procedure for executing a Security Architecture Review. The process is divided into five sequential phases.

### 5.1 Phase 1: Initiation and Triage (SLAs: 2 Business Days)

The process begins when a requesting Solution Architect or Lead Engineer (the "Requester") submits a Security Architecture Review Request via the ServiceNow "Architecture Review" catalog item.

**Procedure Steps:**
1.  **Ticket Creation:** The Requester completes the "Security Architecture Review Request" form in ServiceNow. The form requires:
    - Project/Initiative Name and Jira Epic Link.
    - High-level business justification.
    - Link to the proposed Architecture Decision Record (ADR) or technical design document in Confluence.
    - Link to preliminary data flow diagrams (DFDs) (e.g., Lucidchart, Draw.io).
    - Self-assessment of data handled using the Meridian Data Classification schema.
    - Identification of any net-new third-party vendor or service.

2.  **Automated Intake:** The ServiceNow workflow automatically assigns the ticket to the "InfoSec - Architecture" queue and posts a notification to the `#security-architecture-review` Slack channel.

3.  **Triage by Senior Security Architect:** The Senior Security Architect triages the request within **2 business days**. The triage process determines the review depth:
    - **Level 1: Standard Review (Inherent Risk: Low).** Change does not touch Restricted data, introduces no new authentication/authZ patterns, and uses purely approved design patterns. This is a documentation and attestation review.
    - **Level 2: Deep-Dive Review (Inherent Risk: Medium).** Change introduces a new system component, touch Confidential data, modifies a network boundary, or requires a DPIA. Includes a mandatory threat modeling session.
    - **Level 3: Full-Scale Review (Inherent Risk: High/Critical).** Change handles Restricted (PHI/PII) data; is a component of the Clinical AI Platform classified as High-Risk; alters core HealthPay payment processing; or introduces a new external trust boundary with a critical vendor. Includes mandatory STRIDE threat modeling, a formal ARB presentation, and sign-off from the CISO or CTO.

4.  **Triage Outcome:** The Senior Security Architect updates the ServiceNow ticket with the assigned Level, a tentative timeline, and a list of required prerequisites (e.g., completed DPIA from privacy office).

### 5.2 Phase 2: Documentation and Evidence Gathering (SLAs: 5 Business Days post-triage)

The Requester is responsible for providing comprehensive architectural documentation. Incomplete submissions are the single biggest cause of SAR delays.

**Procedure Steps:**
1.  The Senior Security Architect creates a dedicated Confluence Space "SAR-YYYY-MM-DD-<ProjectName>" and invites the Requester.
2.  The Requester must populate the Confluence space with the "SAR-017: Evidence Pack" template, which includes:
    - **System Context Diagram:** C4 Model – Level 1 & Level 2.
    - **Data Flow and Protection Matrix:**

| Data Object | Class | At Rest (Storage & Encryption) | In Transit (Protocol & Encryption) | In Use (Compute & Controls) |
|---|---|---|---|---|
| e.g., Patient Diagnosis (PHI) | Restricted | RDS: AES-256 (CMK); S3: AES-256-GCM (S3-Managed) | Mutual TLS 1.3 (API Gateway); Amazon VPC Peering | EC2 Instance w/ IMDSv2, SELinux Enforcing |
| e.g., Payment Token | Confidential | DynamoDB: AWS KMS CMK | HTTPS (TLS 1.2+) | Lambda Function (no persistent session state) |

    - **Identity and Access Management (IAM) Model:** Detailed roles, policies, trust relationships, and session management strategy.
    - **Network Architecture Diagram:** Including VPCs, subnets, Security Groups, NACLs, firewalls, CDN endpoints, and API Gateways.
    - **Audit Logging Strategy:** Explanation of what, when, and where operational and security events are logged, referencing the standard to ensure immutability.

3.  The Senior Security Architect reviews the evidence pack for completeness and marks Phase 2 "Done" in ServiceNow. A review meeting cannot be scheduled until this phase is complete.

### 5.3 Phase 3: Threat Modeling and Assessment (Core Analysis Phase)

This is the core technical assessment, conducted jointly by the Information Security team and the Requester's engineering team.

**5.3.1 Level 1: Standard Review Process**
- The Senior Security Architect reviews the documentation for compliance with Meridian's Approved Security Design Patterns.
- Checks are performed against a review checklist: Is AWS Encryption being used correctly? Are S3 bucket policies not overly permissive? Are Security Groups least-privilege?
- Feedback is provided as inline comments within the Confluence document.
- No formal threat modeling workshop is required.

**5.3.2 Level 2 & 3: Deep-Dive and Full-Scale Review Process**
1.  **Threat Modeling Workshop:** The Senior Security Architect schedules a 2-4 hour workshop with the engineering team. The workshop operates against the prepared DFD.
2.  **Contextualized STRIDE:** We apply the STRIDE model per-element. For example, for the "API Gateway" element:
    - **Spoofing:** How are external caller identities authenticated? (e.g., API Key + OAuth 2.0 Client Credentials Grant). How is Gateway-to-service auth handled? (e.g., Mutual TLS).
    - **Tampering:** How is data integrity ensured between gateway and backend? (e.g., JSON Web Signatures (JWS) for payloads). Are WAF rules in place to prevent malicious injection?
    - **Repudiation:** Are all API calls logged to the immutable centralized logging service with a unique transaction ID? Are error codes logged?
    - **Information Disclosure:** Are stack traces, system versions, or internal IPs suppressed? Is sensitive data redacted in logs? Is TLS terminated at the Gateway?
    - **Denial of Service:** Is Rate Throttling in place? Are back-end services shielded behind resilient queues? Are AWS Shield Advanced protections active?
    - **Elevation of Privilege:** Is gateway admin access strictly controlled via SSO/MFA and separate from data-plane access? Can a compromised API key forge admin JWTs?

**5.3.3 Specific Threat Modeling Requirements by Domain:**
- **Clinical AI Platform (EU MDR / AI Act):** In addition to STRIDE, a specific focus is placed on adversarial AI threats (e.g., Model Evasion attacks, Data Poisoning during fine-tuning pipelines, Membership Inference from API responses). Architectural diagrams must clearly delineate the AI Pipeline (Data Ingestion, Training, Model Registry, Inference Serving).
- **HealthPay Financial Services (PCI-DSS / SR 11-7):** Reviews must specifically model the Cardholder Data Environment (CDE) boundary. STRIDE is applied with a heavy focus on model risk, including Tampering of input data to the scoring engine and Information Disclosure of model parameters.

3.  **Findings Log:** All identified threats and vulnerabilities are logged in a standard "Threat and Vulnerability Log" Confluence table within the SAR space.

| Threat ID | Threat Description (STRIDE Element) | Affected Component | Inherent Likelihood (1-5) | Inherent Impact (1-5) | Inherent Risk Level | Proposed Remediation / Control | Control Owner |
|---|---|---|---|---|---|---|---|
| SAR-017-042 | (Information Disclosure) Unencrypted backup of PHI being sent to public AWS S3 Glacier. | Data Lake Backup Pipeline | 3 | 5 | **High (15)** | Enforce bucket policy and KMS encryption at the AWS Backup Vault level. | Data Platform Team |

### 5.4 Phase 4: Decision and Approval (The ARB Gate)

The SAR culminates in a formal decision and approval gate, typically coinciding with the Architecture Review Board (ARB) for Medium and High-risk reviews.

**Procedure Steps:**
1.  **Report Generation:** The Senior Security Architect produces the final "Security Architecture Assessment Report." It contains:
    - An Executive Summary.
    - The final Threat and Vulnerability Log (Phase 3 output).
    - The official Information Security Risk Recommendation:
        - **Approved with No Conditions:** All risks are within Meridian's risk appetite.
        - **Approved with Conditions:** Specific, time-bound remedial actions (post-conditions) must be met before Go-Live or within a defined post-deployment grace period (e.g., "Implement File Integrity Monitoring on clinical report server before Q3 2025").
        - **Rejected:** The residual risk is unacceptable. The architecture cannot proceed. A fundamental rework is required.

2.  **ARB Submission:** For Level 2 and 3 reviews, the final report is submitted to the ARB at least 48 hours before the scheduled review meeting. The Requester creates an ARB presentation based on the standard template.
3.  **ARB Decision:** The ARB, with the VP of Engineering and CISO as key voting members, reviews the proposal and the Security Assessment Report. They vote to approve (with or without conditions) or reject the architecture. The CISO retains a veto power for security and risk concerns.
4.  **Approval Recording:** The formal decision is recorded in the ARB minutes and is the definitive "Approval Gate" for the SDLC. The ServiceNow SAR ticket is updated to reflect the outcome (e.g., "State: Approved with Conditions"). The Requester is now permitted to proceed with production implementation.

### 5.5 Phase 5: Post-Implementation Verification

Security Architecture is proven effective only once implemented.

**Procedure Steps:**
1.  **Readiness Signal:** As part of the Go-Live checklist (SOP-REL-002), the Requester signals that the approved architecture is deployed to staging/production.
2.  **Verification by Security Engineering:** A member of the Security Engineering team (not the approving architect to ensure segregation of duties for verification) executes the Post-Implementation Verification. This is not a penetration test; it is a technical, config-level audit to confirm the implementation matches the approved specification. Methods include:
    - **IaC Code Review:** Directly reviewing Terraform `tfstate` and `.tf` module sources.
    - **Cloud Security Posture Management (CSPM):** Verifying the implementation of approved configurations against Wiz.
    - **Configuration Auditing:** Running AWS Config rules to confirm approved encryption, network, and IAM settings.
3.  **Closure:** Once verification passes, the Security Architect closes the SAR ticket. Any critical deviations are immediately flagged as a Post-Implementation Finding (a high-severity exception) and must be remediated post-haste.

## 6. Controls and Safeguards

The following technical and administrative controls are implemented to support this SOP and the security architecture of Meridian.

| Control ID | Control Description | Control Type | Related SAR Phase |
|---|---|---|---|
| **CTL-ISEC-017-001** | **Architecture Review as a CI/CD Gate:** All infrastructure changes deployed via IaC pipelines must have a valid, approved change identifier. For SAR-required changes, the pipeline must query the ServiceNow ticket state before applying `terraform apply` to production. | Technical / Preventative | Phase 4, 5 |
| **CTL-ISEC-017-002** | **CSPM Continuous Drift Detection:** Wiz continuously compares our live production state against the approved SAR baselines. A "High" severity drift alert on Restricted-data infrastructure triggers an automated rollback to the last known good state in staging and a page to the Security Architect on-call. | Technical / Detective / Corrective | Phase 5 |
| **CTL-ISEC-017-003** | **Approved Security Design Pattern Library:** A Confluence library, maintained by the Senior Security Architect, catalogs all approved patterns (e.g., "Standard Microservice, PHI-bearing," "Standard Public-Facing HealthPay API"). Every Level 2 or 3 review must map to one or more approved patterns or explicitly document the deviation. | Administrative / Preventative | Phase 1, 3 |
| **CTL-ISEC-017-004** | **Change Management Integration:** The ServiceNow SAR ticket ID is a mandatory field in the formal Change Request (CR) for any in-scope infrastructure or application change. The Change Management module (SOP-ISEC-011) is configured to automatically block a CR from being scheduled for implementation if the linked SAR is not in an "Approved" state. | Administrative / Preventative | Phase 4 |
| **CTL-ISEC-017-005** | **Quarterly Retrospective:** The Senior Security Architect performs a retrospective on a random sample of 10% of all approved Level 1 and 2 reviews from the previous quarter. This validates that post-implementation configurations have not drifted from the approved architecture in a way that creates risk. | Administrative / Detective | Phase 5 |

## 7. Monitoring, Metrics, and Reporting

The security and success of the SAR process itself is governed by a set of Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs).

### 7.1 Key Performance Indicators (KPIs)

KPIs are tracked in a dedicated ServiceNow dashboard and reviewed monthly by the InfoSec leadership team.

| KPI | Target | Measurement Method |
|---|---|---|
| **Average Time to Decision (TTD):** From service request to ARB/review decision. | Level 1: < 10 business days; Level 2: < 20 business days; Level 3: < 30 business days | ServiceNow report on ticket duration. |
| **First-Pass Approval Rate:** Percentage of SARs approved without requiring major rework. | > 80% | ServiceNow ticket outcomes (Approved vs. Rejected/Pending Rework). A low rate signals a knowledge gap in engineering. |
| **Post-Implementation Finding Rate:** Number of verification findings requiring remediation after go-live. | Target: Zero Critical or High findings. Medium findings must be < 2 per quarter. | Verification reports logged against the SAR. |
| **SAR Backlog Health:** Number of pending triage requests. | Zero tickets older than the Phase 1 SLA (2 business days). | Open, un-triaged tickets in the `InfoSec - Architecture` queue. |

### 7.2 Key Risk Indicators (KRIs)

KRIs are included in the monthly CISO report to the VP of Engineering and CTO.

| KRI | Measurement Method |
|---|---|
| **Architecture Drift Events:** Count and severity of alerts from CTL-ISEC-017-002 (CSPM Drift Detection). A single critical event requires an immediate post-mortem. | Wiz Alerts correlated to approved SARs. |
| **SAR Gate Circumvention Attempts:** Number of production changes detected by CSPM that lack a corresponding approved SAR and Change Request ticket. | Process audit correlating AWS CloudTrail/Config production changes against the Change Management database. |
| **Aged Exception Backlog:** Number of approved "Approved with Conditions" SARs where the mandatory post-condition remediation is past its due date. | ServiceNow report on SAR Conditions. |

## 8. Exception Handling and Escalation

### 8.1 Exception Handling

Situations may arise where a project cannot fully meet the technical requirements of this SOP due to a critical business constraint, a technical limitation of a critical third-party component, or an unmanageable legacy system migration path.

**Procedure for Requesting an Exception:**
1.  The Requester initiates an "Exception Request" from the SAR ticket in ServiceNow. The request must specify:
    - The exact policy control or technical requirement being deviated from.
    - A detailed technical and business justification for why compliance is not achievable within the required timeline.
    - A proposed compensating control, if applicable.
    - A defined "sunset period" or planned date for resolving the non-compliance. Permanent exceptions are not permitted.
2.  The Senior Security Architect reviews the request and appends their technical risk assessment.
3.  The request is then routed based on the residual risk level, as assessed by the Security Architect:

| Residual Risk Level | Approval Body |
|---|---|
| **Low** | Senior Security Architect |
| **Medium** | Rachel Kim, CISO |
| **High / Critical** | Rachel Kim, CISO, and either David Park (VP Eng) or the CTO, jointly |

4.  The exception, if approved, is logged as a formal "Condition" in the SAR Approval record and is subject to its specific sunset timeline. The CISO maintains final veto authority.

### 8.2 Escalation Paths

- **Project Schedule Risk:** If the SAR process itself poses a risk to a critical business timeline, the Requester can escalate the triage priority by notifying their Business Unit lead to discuss with Rachel Kim, CISO. The CISO has the authority to re-prioritize the Information Security team's review queue based on validated business impact.
- **Dispute over Risk Acceptance:** If the Requester disagrees with the Senior Security Architect's risk assessment (e.g., a Level 2 finding deemed "Rejected"), the matter is escalated to the Architecture Review Board. The ARB will hear both technical arguments and make a final ruling, documented in the minutes.
- **CISO-to-CEO Escalation:** A disagreement on a critical architectural risk (e.g., a core HealthPay architecture decision) that cannot be resolved at the ARB level is escalated to the CEO (Dr. Sarah Chen) by the CISO for final binding arbitration.

## 9. Training Requirements

All personnel involved in the Security Architecture Review process must be adequately trained on their responsibilities.

| Target Audience | Training Module | Mandatory Frequency | Tracking Method |
|---|---|---|---|
| **All Software & Cloud Engineers** | "Meridian Security by Design & Intro to SAR" (Online, Workday Learning) | Annual | Workday Learning Transcript |
| **Solution Architects, Tech Leads, Staff Engineers** | "Conducting Effective Threat Modeling with STRIDE" (In-Person/Live-Virtual Workshop) | Bi-Annual | Registration & Completion in HR LMS |
| **Senior Security Architects (Trainer)** | "Advanced STRIDE & Security Design Pattern Development" (External/Conference-based) | Annual | Certification record; Confluence contribution |
| **Architecture Review Board Members** | "Risk Acceptance and Governance Training" | Annual | Registration in HR LMS |

**Tracking and Remediation:**
- Training completion is automatically tracked. Personnel whose mandatory training has lapsed will have their Jira and CI/CD system access restricted until completion is verified.

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Document Title | Relationship |
|---|---|---|
| SOP-ISEC-005 | Incident Response Plan | Mandates retrospective SAR for emergency changes. |
| SOP-ISEC-011 | Information Technology Change Management | Consumes SAR approval as a gate; also is the parent policy for general change approvals. |
| SOP-ISEC-012 | Risk Assessment and Treatment | Provides the enterprise risk framework (scale, appetite) for the SAR. |
| SOP-PRIV-003 | Data Protection Impact Assessment (DPIA) | A parallel process mandated for PII/PHI changes, feeding into the SAR. |
| SOP-ENG-003 | Secure Software Development Lifecycle (S-SDLC) | The overarching engineering process the SAR supports. |
| SOP-VEND-001 | Third-Party Vendor Risk Management | For reviews involving new external integrations. |
| SOP-AI-001 | AI Model Governance and Risk Management | For specific requirements pertaining to the Clinical AI Platform. |

### 10.2 External Standards and Frameworks

- AICPA Trust Services Criteria (TSC) 2017 (Security, Availability, and Confidentiality categories, specifically CC3.2, CC5.1, CC6.1, A1.2)
- NIST AI 100-1 (Artificial Intelligence Risk Management Framework)
- EU Medical Device Regulation (MDR) 2017/745, Annex I - General Safety and Performance Requirements (for CE marked products)
- OWASP Top 10 (2021) & OWASP API Security Top 10 (2023)

## 11. Revision History

| Version | Date | Author | Summary of Changes | Approver |
|---|---|---|---|---|
| 0.9 | 2024-01-10 | Rachel Kim (CISO) | Initial Draft for review cycle 1. | N/A |
| 1.0 | 2024-02-25 | Rachel Kim (CISO) | Initial Publication. Formalized SAR gates, STRIDE methodology, and ARB integration. | Dr. Sarah Chen |
| 1.1 | 2024-06-30 | James Okonkwo (Sr. Sec. Architect) | Minor update to Phase 1 intake form, adding "Data Classification" self-assessment field. Added KPI dashboard reference. Updated training links. | Rachel Kim |
| 1.2 | 2024-10-15 | Priya Sharma (InfoSec GRC) | Integrated CSPM continuous drift detection (Wiz) as a control (CTL-017-002) and added Phase 5.5. Added specific sub-section 5.3.3 for AI and HealthPay threat modeling. | Rachel Kim |
| 1.3 | 2025-07-13 | Rachel Kim (CISO) | Major revision following SOC 2 Type II observation period. Refined Post-Implementation Verification to explicitly separate duties from Phase 3 review. Updated RACI and approval matrix for clarity. Enhanced the formal Change Management integration logic (CTL-017-004). Updated "Next Review" date. | Dr. Sarah Chen |