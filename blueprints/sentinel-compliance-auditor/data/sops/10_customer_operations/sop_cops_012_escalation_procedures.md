---
sop_id: "SOP-COPS-012"
title: "Escalation Procedures"
business_unit: "Customer Operations"
version: "2.4"
effective_date: "2025-11-25"
last_reviewed: "2026-03-20"
next_review: "2026-09-04"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# SOP-COPS-012: Escalation Procedures
**Version 2.4**
**Effective: 2025-11-25**
**Owner: Michael Chang, VP of Customer Operations**
**Classification: Internal**

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish a unified, multi-tiered framework for the identification, classification, escalation, and resolution of incidents, service requests, and critical events across Meridian’s product ecosystem. This SOP defines the pathways through which Customer Operations, Engineering, Clinical AI, Financial Services, and Security teams collaborate to ensure that issues impacting availability, data integrity, patient safety, or regulatory standing are resolved with appropriate urgency and visibility.

This SOP operationalizes Meridian’s commitment to maintaining service reliability for the Meridian SaaS Platform, Clinical AI Products, HealthPay Financial Services, and all supporting infrastructure. It defines escalation criteria that are objective, measurable, and auditable.

### 1.2 Scope

This SOP applies to all personnel, contractors, and third-party service providers who interact with Meridian’s production systems, handle Protected Health Information (PHI), or support Meridian products and customers. The scope encompasses:

| Domain | Coverage |
|--------|----------|
| **Products** | Meridian SaaS Platform, Clinical AI Suite (imaging, decision support), HealthPay Financial Services, Patient Analytics, Provider Portal |
| **Environments** | Production (AWS us-east-1, eu-west-1), Disaster Recovery (Azure), Staging, UAT |
| **Incident Types** | Service outages, data corruption, PHI exposure or mishandling, model degradation, security events, billing disputes, contractual SLA breaches |
| **Customer Segments** | Enterprise Healthcare Systems, Ambulatory Practices, Payers, Third-Party Integrators |
| **Regulatory Scope** | HIPAA Security Rule; SOC 2 Trust Services Criteria (Security, Availability); EU AI Act transparency obligations; GDPR incident notification; SR 11-7 model risk management |

### 1.3 Applicability

This SOP is binding on the following business units and roles:

- **Customer Operations** (Tier 1-3 Support, Customer Success Managers)
- **Engineering** (Platform, Clinical AI, Financial Services, Data Engineering)
- **Clinical AI Products** (Model Operations, Clinical Validation)
- **Information Security** (SOC Analysts, Incident Response)
- **Compliance** (Privacy Office, Regulatory Affairs)
- **Executive Leadership** (Escalation approvers, Crisis Management)

### 1.4 Out-of-Scope

This SOP does not cover internal IT help desk requests (see SOP-IT-005), employee relations matters (see HR-014), or product feature requests submitted through the Product Advisory Board (see SOP-PM-022). Financial audit escalations are governed by SOP-FIN-008.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|------|------------|
| **Escalation** | The formal transfer of an incident or service request from one support tier to a higher tier, or to a management authority, due to its severity, complexity, or failure to resolve within established timeframes. |
| **Severity Level** | A classification (SEV1–SEV5) assigned to an incident based on its business impact, regulatory implications, and patient safety risk. |
| **Response Time** | The time elapsed from initial ticket creation to the first human acknowledgement and engagement by a Meridian resource. This is distinct from Resolution Time. |
| **Resolution Time** | The time elapsed from ticket creation to the point at which the incident is fully remediated and validated, including root cause confirmation where required by severity. |
| **Hierarchical Escalation** | Escalation through management chains based on organizational authority, invoked when functional escalation fails or when crisis-level decisions are required. |
| **Functional Escalation** | Transfer of an incident to a team or individual with specialized skills, tools, or authority to resolve the issue (e.g., from Tier 2 to Clinical AI Engineering, or from Triage to Security). |
| **Patient Safety Impact (PSI)** | A designation applied when a system incident has caused, or has reasonable potential to cause, harm to a patient — including delayed diagnosis, incorrect clinical recommendation delivery, or diagnostic image corruption. PSI-classified incidents trigger mandatory notification to the Chief Medical Officer. |
| **Model Degradation Event** | A detected drift in ML model performance (accuracy, precision, recall) exceeding defined thresholds in the model monitoring dashboards (MLflow, LangSmith traces), potentially compromising clinical decision support quality. |
| **PHI Incident** | Any event involving unauthorized access, use, disclosure, modification, or destruction of Protected Health Information, as defined under HIPAA. Includes both confirmed breaches and suspected exposures. |

### 2.2 Acronyms

| Acronym | Full Form |
|---------|-----------|
| SEV | Severity Level (1-5) |
| TTR | Mean Time to Resolution |
| MTTA | Mean Time to Acknowledge |
| SLO | Service Level Objective |
| SLA | Service Level Agreement |
| PHI | Protected Health Information |
| PII | Personally Identifiable Information |
| BAA | Business Associate Agreement |
| P1/P2/P3 | Priority Levels (mapped to SEV) |
| RACI | Responsible, Accountable, Consulted, Informed |
| CM | Crisis Manager |
| CISO | Chief Information Security Officer |
| CPO | Chief Privacy Officer / Data Protection Officer |
| CMO | Chief Medical Officer |
| CAIO | Chief AI Officer |
| VP Eng | Vice President of Engineering |
| VP FinSvc | Vice President of Financial Services |
| VP CustOps | Vice President of Customer Operations |
| PSI | Patient Safety Impact |
| AWS | Amazon Web Services |
| DR | Disaster Recovery |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix for Escalation Procedures

The following matrix defines accountability across all escalation workflows. No single individual may serve as both Approver and Executor for any critical incident involving PHI — a two-person integrity control is mandatory for PHI-related SEV1 and SEV2 incidents.

| Activity | Responsible (Doer) | Accountable (Owner) | Consulted | Informed |
|----------|-------------------|---------------------|-----------|----------|
| Initial Triage & Classification | Tier 1 Support Agent | Tier 2 Shift Lead | None | Customer Operations Manager |
| SEV1 Incident Declaration | Incident Commander (Tier 3 Engineer) | VP of Customer Operations | CISO, CMO (if PSI), General Counsel | CEO, CAIO, VP Eng |
| SEV1 Resolution Coordination | Incident Commander | VP of Customer Operations | Platform Engineering Lead, Clinical AI Lead, Security Lead | C-Suite, Board AI Governance Committee (if AI-related) |
| PHI Breach Assessment | Privacy Incident Response Team | Chief Privacy Officer / DPO | CISO, General Counsel, CMO | CEO, Chief Compliance Officer |
| Model Degradation Escalation | MLOps Engineer (Tier 3) | VP of Clinical AI Products | CAIO, CMO (if clinical impact) | Customer Operations, affected customers (via CSM) |
| Financial Services (SR 11-7) Model Issue | Risk Analytics Engineer | VP of Financial Services | Chief Compliance Officer, CFO | CAIO, CEO |
| Customer Communication During Incident | Customer Success Manager (assigned to account) | VP of Customer Operations | Incident Commander, Legal | Executive team |
| Post-Incident Review (PIR) | Incident Commander | VP of Customer Operations | All involved teams | VP Eng, CISO, CMO, CAIO |

### 3.2 Named Escalation Contacts (as of Effective Date)

| Role | Name | Contact (Primary) | Contact (Escalation) |
|------|------|-------------------|----------------------|
| VP, Customer Operations | Michael Chang | Slack: @mchang, PagerDuty: mchang | (310) 555-0182 (mobile) |
| VP, Financial Services | Robert Liu | Slack: @rliu, PagerDuty: rliu | (415) 555-0193 (mobile) |
| VP, Engineering | Sarah Okonkwo | Slack: @sokonkwo, PagerDuty: sokonkwo | (512) 555-0147 (mobile) |
| VP, Clinical AI Products | Dr. Amina Diallo | Slack: @adiallo, PagerDuty: adiallo | (617) 555-0205 (mobile) |
| CISO | James Riordan | Slack: @jriordan, PagerDuty: jriordan | (212) 555-0162 (24/7 hotline) |
| Chief Privacy Officer / DPO | Maria Santos-Silva | Slack: @msantos, PagerDuty: msantos | +32 2 555 0198 (EU hotline) |
| Chief Medical Officer | Dr. Hiroshi Tanaka | Slack: @htanaka, PagerDuty: htanaka | (312) 555-0173 (24/7 clinical line) |
| Chief Compliance Officer | Priya Narayanan | Slack: @pnarayanan, PagerDuty: pnarayanan | (202) 555-0211 (mobile) |
| General Counsel | David Chen, Esq. | Slack: @dchen, PagerDuty: dchen | (917) 555-0154 (mobile) |
| CEO | Amara Singh | Slack: @asingh | (646) 555-0101 (office, forwarded) |

### 3.3 Escalation Authority

Only individuals holding the roles specified in §3.2, or their formally designated delegates (recorded in PagerDuty override schedules), may authorize:
- SEV1 declarations and closures
- Public or regulatory notification of incidents
- Service credits or SLA penalty waivers for customers
- Engagement of external incident response firms
- Activation of the Disaster Recovery environment for incident mitigation

---

## 4. Policy Statements

### 4.1 General Escalation Principles

Meridian Customer Operations adheres to the following principles in all escalations:

1. **Triage First, Escalate with Evidence**: No incident shall be escalated to a higher tier or management authority without first undergoing triage and classification. The escalating party must attach a completed Escalation Justification Document (see §5.2.3) containing relevant logs, impact assessment, and attempted remediation steps.
2. **Severity-Driven, Not Request-Driven**: Escalation priority is determined solely by the Severity Level assigned during triage, not by customer demands, contractual pressure, or internal political considerations.
3. **Patient Safety Overrides All Other Priorities**: Any incident with confirmed or suspected Patient Safety Impact shall be escalated immediately to SEV1, bypassing standard triage workflow.
4. **No Retaliation for Escalation**: Any Meridian employee who escalates an incident in good faith shall not face any negative consequence, regardless of whether the escalation later proves unnecessary.
5. **Transparency in Communication**: All escalated incidents shall maintain a single source of truth (the master ticket in ServiceNow), visible to all parties. No side-channel communications (private Slack DMs, personal email) may substitute for ticket updates.

### 4.2 Tiered Escalation Model

Meridian operates a five-tier functional escalation model, supplemented by a three-level hierarchical escalation path for management decision-making:

| Functional Tier | Team | Scope of Authority |
|-----------------|------|-------------------|
| Tier 1 | Customer Operations Agents | Initial intake, classification, basic troubleshooting, SEV4-SEV5 resolution |
| Tier 2 | Senior Support Engineers | Advanced troubleshooting, SEV3 resolution, escalation initiation to Tier 3 |
| Tier 3 | Platform / Clinical AI / Financial Services Engineering | SEV2-SEV1 technical resolution, code-level fixes, infrastructure changes |
| Tier 4 | VP-level Leadership | Resource allocation, cross-team coordination, customer communication authority |
| Tier 5 | C-Suite / Crisis Management Team | Regulatory notification, legal engagement, business-continuity decisions |

| Hierarchical Level | Authority | Trigger |
|--------------------|----------|---------|
| Level 1 | Team Lead / Shift Lead | Breach of SLA by 15 minutes for SEV3, or upon SEV2 declaration |
| Level 2 | VP of Customer Operations | Breach of SLA by 30 minutes for SEV2, or upon SEV1 declaration |
| Level 3 | CEO / Board Notification | Any SEV1 exceeding 4 hours without resolution path, or any regulatory-reportable event |

### 4.3 PHI Incident Escalation (Mandatory)

All incidents involving actual or suspected PHI mishandling — including unauthorized access, data leakage, improper disposal, or transmission to an unauthorized third party — **must be escalated to the Chief Privacy Officer / DPO within 15 minutes of discovery**, regardless of severity classification. Failure to meet this timeline shall be treated as a process violation subject to personnel action per HR policy.

Upon PHI incident identification, the discovering agent shall:
1. Immediately lock the affected record(s) in the data platform (if accessible).
2. Notify the Privacy Incident Response Team via the dedicated PagerDuty service (`meridian-phi-emergency`), which pages the CPO, CISO, General Counsel, and Chief Compliance Officer simultaneously.
3. Document all known details in a ServiceNow incident ticket, marking it with the `PHI_BREACH` flag, which automatically restricts ticket visibility to authorized personnel only.
4. Cease all other activities until the CPO or CISO provides disposition instructions.

### 4.4 EU AI Act Transparency Escalation

Pursuant to Meridian’s obligations under the EU AI Act for high-risk AI systems, any incident involving the Clinical AI Suite deployed in EU member states that results in:
- Systematic model bias producing differential clinical outcomes by patient demographics
- Failure to provide required transparency explanations to a clinician upon request
- Any model behavior that a qualified clinician deems clinically inappropriate

shall be escalated simultaneously to the VP of Clinical AI Products and the Chief Compliance Officer within 60 minutes of confirmed observation.

### 4.5 Service Level Objectives (SLOs)

Meridian commits to the following SLOs for incident response, measured monthly:

| Severity | Acknowledgement SLO | Resolution Target SLO | Escalation Trigger (if unresolved) |
|----------|---------------------|-----------------------|-------------------------------------|
| SEV1 | 5 minutes | 2 hours | 1 hour → VP Eng + CAIO; 2 hours → CEO |
| SEV2 | 15 minutes | 8 hours | 4 hours → VP Eng; 8 hours → CISO |
| SEV3 | 1 hour | 24 hours | 12 hours → Tier 2 Lead; 20 hours → VP CustOps |
| SEV4 | 4 hours | 72 hours | 48 hours → Team Lead |
| SEV5 | 1 business day | 5 business days | 5 days → CSM for customer communication |

---

## 5. Detailed Procedures

### 5.1 Initial Intake and Classification (Tier 1)

All incidents enter the Meridian support ecosystem through one of the authorized channels:
- **ServiceNow Customer Portal** (primary channel for enterprise customers)
- **Email to support@meridian-health.com** (auto-creates ServiceNow ticket; agents must manually triage)
- **Phone to +1 (888) 555-MRDN** (24/7 hotline; Tier 1 agent creates ticket during call)
- **Automated monitoring alerts** (Datadog, PagerDuty auto-ticketing via ServiceNow API; these bypass Tier 1 classification and are routed directly to the on-call Tier 2/3 engineer per runbook mappings)

#### 5.1.1 Triage Decision Tree (Tier 1 Agent)

Upon ticket creation, the Tier 1 agent shall execute the following triage sequence within the first interaction:

```
┌─ Q1: Does this incident involve patient safety?
│  YES → Declare SEV1, skip to §5.4
│  NO  → Continue
│
├─ Q2: Does this incident involve PHI?
│  YES → Tag PHI_BREACH, invoke §4.3 procedure, continue
│  NO  → Continue
│
├─ Q3: Is a production system completely unavailable to all users?
│  YES → Declare SEV1, proceed to §5.4
│  NO  → Continue
│
├─ Q4: Is a critical business function (payments, clinical recs, image processing) unavailable, but not all users?
│  YES → Declare SEV2, proceed to §5.3
│  NO  → Continue
│
├─ Q5: Is this affecting multiple customers but with workaround available?
│  YES → Declare SEV3, proceed to §5.2
│  NO  → Continue
│
├─ Q6: Single customer, limited functionality impaired?
│  YES → Assign SEV4, resolve at Tier 1 or Tier 2
│
└─ Q7: Cosmetic issue, documentation request, or general inquiry?
   → Assign SEV5, queue for normal business hours handling
```

#### 5.1.2 Ticket Field Requirements (Mandatory at Creation)

| Field | Required? | Validation |
|-------|-----------|------------|
| Customer Name/ID | Yes | Must match CRM record |
| Product/Module | Yes | Dropdown from product catalog |
| Environment | Yes | Production / Staging / UAT |
| Severity | Yes | Must follow tree above; Tier 2 may override |
| PHI Involved? | Yes | Boolean; if Yes → auto-triggers Privacy workflow |
| Patient Safety Impact? | Yes | Boolean; if Yes → blocks closure without CMO sign-off |
| Description | Yes | Free text, min 50 characters |
| Steps to Reproduce | Conditional | Required for SEV3+ |

### 5.2 Tier 2 Escalation (SEV3 Incidents)

When a Tier 1 agent cannot resolve an issue within 30 minutes of initial engagement, or when the triage decision tree assigns SEV3 or higher, the incident is escalated to Tier 2.

#### 5.2.1 Tier 2 Acceptance

The on-call Tier 2 Senior Support Engineer (roster maintained in PagerDuty, schedule `meridian-t2-support`) receives the escalated ticket via ServiceNow assignment notification. The Tier 2 engineer must:
1. Acknowledge the escalated ticket within **15 minutes** of assignment.
2. Review the triage notes and any attached logs.
3. Replicate the issue in the staging environment, if possible.
4. Determine if the issue requires code-level or infrastructure intervention.

#### 5.2.2 Tier 2 Resolution Authority

Tier 2 engineers may perform the following actions without further approval:
- Restart non-critical application services (via Kubernetes `kubectl rollout restart` on permitted namespaces)
- Clear application-layer caches (Redis secondary instances only; primary cache clearance requires Tier 3)
- Modify customer-specific configuration flags in LaunchDarkly (staging environment only; production flag changes require peer review)
- Apply database index recommendations generated by the performance monitoring system (AWS Performance Insights)

**Restricted actions** (require Tier 3 or VP Eng approval):
- Production database schema modifications
- Direct production data modification or deletion
- Firewall or security group changes
- Model endpoint updates or Clinical AI inference path changes
- Any action affecting PHI records beyond read-only access

#### 5.2.3 Tier 3 Escalation Justification Document

To escalate from Tier 2 to Tier 3 (SEV3 unresolved for >12 hours, or any SEV2/SEV1), the Tier 2 engineer must submit an Escalation Justification Document (EJD) via the ServiceNow "Escalate to Engineering" workflow. The EJD template includes:

```
ESCALATION JUSTIFICATION DOCUMENT
Ticket ID: ____________________
Escalating Engineer: ____________________
Time of Escalation: ____________________

1. INCIDENT SUMMARY (provide concise technical description)
   
2. IMPACT ASSESSMENT
   - Affected customer(s): 
   - Affected module(s): 
   - Number of users impacted (estimated): 
   - Regulatory implications (PHI, AI Act, FDA, CE marking): 
   
3. ATTEMPTED REMEDIATIONS (list all actions taken at Tier 1 and Tier 2,
   including timestamps and results):
   Action 1 (time): ________________ Result: ________________
   Action 2 (time): ________________ Result: ________________
   
4. LOGS ATTACHED (check all):
   [ ] Application logs (CloudWatch)
   [ ] Database logs (RDS Performance Insights)
   [ ] Model inference logs (MLflow)
   [ ] Network traces (VPC Flow Logs)
   [ ] Customer-side logs (if provided)

5. RECOMMENDED ENGINEERING TEAM:
   [ ] Platform Engineering (infrastructure, DB)
   [ ] Clinical AI Engineering (model, inference)
   [ ] Financial Services Engineering (payments, credit)
   [ ] Security Engineering (requires CISO approval for SEV2+)
```

### 5.3 Tier 3 Engineering Engagement (SEV2 Incidents)

#### 5.3.1 Incident Command Activation

Upon SEV2 classification, a Tier 3 engineer from the relevant engineering team assumes the role of **Incident Commander (IC)** . The IC shall:

1. Create a dedicated Slack channel `#incident-[ticket-id]` and invite all relevant engineering leads.
2. Open a Zoom bridge (persistent link: `https://meridian.zoom.us/incident-bridge`) for real-time collaboration.
3. Declare the incident in PagerDuty (`meridian-sev2-paging`) which alerts: VP CustOps, VP Eng, relevant VP (CAIO or VP FinSvc), and the on-call Security Engineer.
4. Establish a **War Room** (physical or virtual) staffed until resolution.
5. Initiate the incident log (Google Doc template: "Meridian Incident War Room Log") to capture all actions, decisions, and timestamps in real-time.

#### 5.3.2 Financial Services Model Escalation (SR 11-7)

For incidents involving HealthPay Financial Services credit models, fraud detection, or payment processing, additional procedures apply per Meridian’s model risk management framework:

- The Tier 3 Financial Services Engineer must tag the incident with `SR11-7_MODEL_RISK`.
- The VP of Financial Services must be consulted before any model parameter change.
- If model performance degradation exceeds the Materiality Threshold (defined in the Model Risk Appetite Statement, SOP-RISK-031): loss-rate deviation >15 basis points from baseline, or fraud false-positive rate >2.0% — the Chief Compliance Officer shall be notified within 2 hours.
- Any model rollback in production requires a documented approval from the VP of Financial Services, logged in ServiceNow and in the model inventory.

#### 5.3.3 Clinical AI Model Escalation (EU AI Act / CE Marking)

For incidents involving Clinical AI products (Imaging Diagnostic Support, Clinical Decision Support Engine) deployed under CE marking:

- The Tier 3 MLOps Engineer shall engage the Clinical Validation Lead (Dr. Rachel Okonkwo, Slack: @rachel-okonkwo) to assess clinical safety implications.
- Any model serving degradation exceeding SLO thresholds (prediction latency >500ms p99, model accuracy deviation >0.5% from baseline for diagnostic endpoints) triggers a mandatory clinical review.
- For EU-deployed instances, the EU Authorized Representative (MedTech Europe GmbH, contact: `eu-rep@meridian-health.com`) must be notified within 24 hours if the incident impacts CE-marked functionality.

### 5.4 SEV1 Crisis Escalation

#### 5.4.1 SEV1 Declaration Authority

SEV1 may be declared by:
- Any Tier 1 agent applying the triage decision tree (Q1, Q3)
- Any Tier 2 or Tier 3 engineer observing conditions meeting SEV1 criteria
- Any automated monitoring alert triggering the `meridian-sev1-auto` PagerDuty service
- The CISO, for security incidents
- The CPO, for privacy incidents
- The CMO, for patient safety incidents

#### 5.4.2 SEV1 Execution Steps

**Step 1: Immediate Notification (T+0 minutes)**
The declaring party activates the SEV1 PagerDuty service (`meridian-sev1-critical`), which simultaneously pages:
- VP of Customer Operations (primary)
- VP of Engineering
- CISO
- On-call Incident Commander (Tier 3 Engineering)
- General Counsel

**Step 2: War Room Activation (T+5 minutes)**
The Incident Commander opens the dedicated SEV1 Zoom bridge (`https://meridian.zoom.us/sev1-bridge`) and Slack channel `#sev1-[ticket-id]`. All paged personnel must acknowledge within **5 minutes**.

**Step 3: Blast Radius Assessment (T+15 minutes)**
The Incident Commander, with Platform Engineering, determines:
- Which AWS services/regions are impacted
- Which customer segments are affected
- Estimated data loss or corruption scope
- Regulatory notification triggers crossed

**Step 4: Executive Briefing (T+30 minutes)**
A structured executive briefing (template in Appendix A) must be delivered by the Incident Commander to:
- CEO
- CAIO (if AI-related)
- CMO (if clinical)
- CFO (if financial)
- Board AI Governance Committee (if AI-related SEV1)

**Step 5: Customer Communication (T+60 minutes, or sooner if regulatory)**
The VP of Customer Operations, in consultation with Legal and the assigned Customer Success Manager, shall issue a customer-facing incident notification via:
- StatusPage (`status.meridian-health.com`) — public
- Direct email to affected enterprise customer contacts (from CRM)
- In-app banner for SaaS Platform users (via LaunchDarkly flag `incident-banner`)

**Step 6: Resolution and Validation (continuous until resolved)**
Engineering shall pursue parallel resolution paths:
- Path A: Root cause fix (permanent)
- Path B: Workaround restoration (temporary, to restore service)
- Path C: DR environment failover (if path A/B exceed 2 hours)

Validation criteria for SEV1 closure:
- All affected services restored and monitored for 30 minutes of stability
- All customer-reported symptoms resolved
- Patient Safety Impact cleared by CMO (if applicable)
- PHI exposure contained and assessed by CPO (if applicable)

**Step 7: Closure and Post-Incident Review (T+24 hours for PIR, T+7 days for final report)**
The Incident Commander shall schedule a blameless post-incident review (PIR) within 24 hours of resolution. The PIR shall produce:
- Incident Timeline (minute-by-minute)
- Contributing Factors (technical, process, human)
- Corrective Actions (assigned to owners with due dates)
- Severity Classification Validation (was it correctly classified?)

### 5.5 Hierarchical (Management) Escalation

When functional resolution stalls, or when a decision requires executive authority, hierarchical escalation proceeds through three levels:

#### 5.5.1 Level 1: Team Lead / Shift Lead

Triggered by:
- SEV3 ticket unresolved at 12 hours
- SEV4 ticket unresolved at 48 hours
- Any agent requesting supervisory override of severity classification

The Team Lead may re-assign resources, authorize overtime, or escalate to Level 2.

#### 5.5.2 Level 2: VP of Customer Operations

Triggered by:
- SEV2 unresolved at 4 hours
- SEV1 unresolved at 1 hour
- Any incident requiring customer-facing communication beyond standard status updates

The VP of Customer Operations may authorize:
- Engagement of external consultants (with CISO approval for security-sensitive work)
- Temporary service credits or remediation offers to customers
- Cross-department resource reallocation (request to VP Eng, VP FinSvc)

#### 5.5.3 Level 3: CEO / Board Notification

Triggered by:
- SEV1 unresolved at 4 hours
- Any regulatory-reportable incident (HIPAA breach >500 individuals, EU AI Act serious incident)
- Any incident attracting media or regulatory inquiry

CEO notification is executed by the VP of Customer Operations via the CEO’s Chief of Staff. Board notification is executed by the CEO or General Counsel.

---

### 5.6 Escalation Tier Criteria Summary Table

| Criterion | SEV5 | SEV4 | SEV3 | SEV2 | SEV1 |
|-----------|------|------|------|------|------|
| **User Impact** | Single user, cosmetic | <10% of customer users, minor feature | Multiple customers, workaround exists | Critical function unavailable, no workaround | Complete service outage or patient safety impact |
| **Financial Impact** | None | <$1K potential | <$10K potential | <$100K potential | >$100K potential or regulatory fine risk |
| **PHI Exposure** | None | None | None | Potential, contained | Confirmed or high-probability breach |
| **Clinical Safety Impact** | None | None | None | Model degradation, no patient harm | Confirmed or potential patient harm |
| **Regulatory Notification** | Not required | Not required | Not required | CPO review required | Mandatory notification likely |
| **Response SLO** | 1 business day | 4 hours | 1 hour | 15 minutes | 5 minutes |
| **Resolution SLO** | 5 business days | 72 hours | 24 hours | 8 hours | 2 hours |
| **Escalation Tier** | Tier 1 | Tier 1-2 | Tier 2 | Tier 3 + VP | Tier 3 + C-Suite |
| **War Room Required?** | No | No | No | Yes | Yes |

---

## 6. Controls and Safeguards

### 6.1 Access Controls During Incident Management

During an active SEV1 or SEV2 incident, engineering personnel may require elevated access to production systems. Such access shall be:

| Control | Mechanism | Audit Trail |
|---------|-----------|-------------|
| **Just-in-Time Access** | PAM system grants temporary AWS IAM role elevation for duration of incident. Role auto-expires at resolution + 1 hour. | All role elevations logged to CloudTrail, correlated with incident ticket ID. |
| **Break-Glass Procedure** | In event PAM is unavailable, a pre-registered break-glass IAM role (max 4-hour duration) may be assumed by any Tier 3 engineer. | Break-glass usage generates immediate alert to CISO and Security Engineering. All actions logged. |
| **PHI Access During Incidents** | Access to PHI-bearing databases (Aurora `prod-clinical`, DynamoDB `prod-patient`) requires explicit CPO authorization, logged in ServiceNow. | All queries audited via database audit logging. |

### 6.2 Communication Controls

- **All SEV1 and SEV2 incident communications** must occur in the dedicated Slack channel `#incident-[ticket-id]`. No side-channel decisions.
- **Customer-facing communications** must be approved by Legal and VP CustOps before dispatch.
- **Regulatory communications** must be approved by General Counsel and the relevant executive (CPO for privacy, CMO for clinical, CCO for compliance, VP FinSvc for financial).

### 6.3 Data Integrity Controls

During incident remediation, any direct data modification (beyond standard application writes) requires:
1. A peer review of the proposed modification (by a second Tier 3 engineer, not the author).
2. A backup capture of the affected data set before modification (snapshot or export verified by checksum).
3. Logging of the modification in the incident log with exact query/command recorded.

### 6.4 Model Rollback Controls (Clinical AI and Financial Services)

For any production ML model rollback:
- The previous model artifact must be identified by its MLflow run ID and its performance validated against the pre-deployment baseline.
- Rollback must be executed via the standard CI/CD pipeline (ArgoCD, not manual `kubectl` commands).
- A post-rollback monitoring period of 24 hours with heightened alerting shall be observed.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Real-Time Monitoring Dashboards

The following dashboards are maintained for real-time escalation visibility:

| Dashboard | URL | Audience | Refresh Rate |
|-----------|-----|----------|--------------|
| **Customer Operations Command Center** | `grafana.meridian.io/dashboards/custops-cc` | Tier 1, Tier 2, VP CustOps | 30 seconds |
| **SEV1/SEV2 Active Incidents** | `grafana.meridian.io/dashboards/active-sev12` | All Engineering, C-Suite | 60 seconds |
| **Clinical AI Model Health** | `grafana.meridian.io/dashboards/clinical-models` | Clinical AI Eng, CMO | 5 minutes |
| **Financial Services Transaction Health** | `grafana.meridian.io/dashboards/finsvc-tx` | FinSvc Eng, VP FinSvc, CFO | 1 minute |
| **PII/PHI Data Access Monitor** | Internal only: `monitor.meridian.io/phi-access` | CPO, CISO, General Counsel | Near real-time |

### 7.2 Key Performance Indicators (KPIs)

Measured monthly and reported to the Executive Leadership Team:

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| **Mean Time to Acknowledge (MTTA) SEV1** | ≤ 3 minutes | ServiceNow → PagerDuty timestamp delta |
| **Mean Time to Resolution (MTTR) SEV1** | ≤ 90 minutes | ServiceNow created → resolved timestamp |
| **Escalation Accuracy (Tier 1 → Tier 2)** | ≥ 95% correct by severity | Monthly audit of 100 random escalations |
| **Escalation Justification Completeness** | ≥ 98% fully completed EJD | ServiceNow field validation |
| **Post-Incident Review Completion** | 100% within 7 calendar days | ServiceNow PIR task tracking |
| **Repeat Incident Rate** (same root cause within 30 days) | < 2% | Correlation engine on ServiceNow incidents |
| **Customer Satisfaction (post-incident survey)** | ≥ 4.2 / 5.0 | Medallia survey triggered at ticket closure |
| **PHI Incident Escalation Within 15 Minutes** | 100% (compliance mandatory) | CPO audit log vs. discovery timestamp |

### 7.3 Reporting Cadence

| Report | Recipients | Frequency | Owner |
|--------|------------|-----------|-------|
| **Weekly Escalation Summary** | VP CustOps, VP Eng, VP ClinAI, VP FinSvc | Every Monday 09:00 ET | VP CustOps |
| **Monthly SEV1/SEV2 Trends** | C-Suite | 1st business day of month | VP CustOps + CISO |
| **Quarterly Regulatory Escalation Report** | Chief Compliance Officer, General Counsel, Board Risk Committee | 15th of month after quarter end | CCO |
| **Annual Escalation Program Review** | Board of Directors | December | VP CustOps + CEO |

---

## 8. Exception Handling and Escalation

While this SOP establishes standardized processes, Meridian recognizes that exceptional circumstances may require deviation. All exceptions must be documented, justified, and approved — no informal exceptions are permitted.

### 8.1 Exception Types

| Exception Type | Example Scenario | Approver |
|---------------|-----------------|----------|
| **Severity Override** | Tier 1 assigns SEV2, but Engineering Lead believes condition is SEV3 (or vice versa) | VP CustOps + VP Eng jointly |
| **Timeline Waiver** | Resolution SLO cannot be met due to dependency on external vendor (e.g., AWS outage) | VP CustOps, communicated to customer |
| **Process Bypass** | Incident declared during Tier 1 triage without full EJD (urgency precludes documentation) | Retroactive approval by VP CustOps within 24 hours |
| **Access Exception** | Engineer requires PHI access beyond scope defined in §6.1 during incident resolution | CPO + CISO jointly |
| **Communication Delay** | Customer notification delayed due to law enforcement or regulatory instruction | General Counsel |

### 8.2 Exception Request Procedure

1. Any team member identifying a need for exception shall file an **Exception Request** in ServiceNow (form: "Escalation Exception Request").
2. The request must state: (a) the specific section of this SOP from which deviation is sought, (b) the justification, (c) the proposed alternative, and (d) the expected duration.
3. The designated Approver(s) per §8.1 shall approve, deny, or modify the request within:
   - SEV1/SEV2 incidents: **30 minutes**
   - All other incidents: **4 business hours**
4. Approved exceptions shall be attached to the master incident ticket and logged in the Exception Registry (ServiceNow table `sn_exception_log`).

### 8.3 Exception Registry and Review

The Exception Registry is reviewed:
- Monthly by the VP of Customer Operations for patterns (repeated exceptions may indicate SOP deficiencies).
- Quarterly by the Chief Compliance Officer for regulatory implications.
- Annually by Internal Audit (if audit program is active).

---

## 9. Training Requirements

### 9.1 Training Program Overview

All individuals with responsibilities under this SOP shall complete training as specified below.

| Role | Training Module | Frequency | Delivery Method | Assessment |
|------|----------------|-----------|-----------------|------------|
| **Tier 1 Agents** | ESC-101: Escalation Procedures Fundamentals | Annually, at hire | LMS (Workday Learning) | 80% pass on module quiz |
| **Tier 2 Engineers** | ESC-201: Advanced Triage & Escalation | Annually | Instructor-led virtual | Hands-on simulation |
| **Tier 3 Engineers (all specialties)** | ESC-301: Incident Command & Crisis Management | Annually | In-person 2-day workshop (Austin HQ) | Live-fire simulation (must pass) |
| **Customer Success Managers** | ESC-401: Customer Communication During Incidents | Annually | LMS + video recording | Scenario-based test |
| **VP-level and above** | ESC-501: Executive Incident Management | Annually | 1:1 briefing by VP CustOps | Tabletop exercise |
| **All staff with PHI access** | HIPAA Incident Response & PHI Handling | Annually | LMS module HIP-101 | 90% pass required; auto-remediation assignment for failures |

### 9.2 Training Tracking

Training completion shall be recorded in Workday Learning. Managers are responsible for ensuring direct reports complete training by the assigned due date. Non-compliance past the due date triggers:
- 7 days past due: Automated reminder to employee and manager
- 14 days past due: Notification to VP CustOps
- 30 days past due: Temporary revocation of production access (for Tier 1-3) until training completed

### 9.3 New Hire Onboarding

No new hire in a role covered by this SOP shall be granted access to production systems, customer data, or incident management tools (ServiceNow agent role, PagerDuty schedules, incident Slack channels) until:
- ESC-101 (or role-equivalent) is completed and passed
- A 4-hour shadowing session with a senior team member is completed, covering at least one live incident handling event.

---

## 10. Related Policies and References

### 10.1 Meridian Internal SOPs

| SOP ID | Title | Relationship |
|--------|-------|--------------|
| SOP-ISEC-005 | Incident Response Plan | Governs security incident handling; referenced for PHI breach escalation |
| SOP-COPS-008 | Customer Communication Standards | Defines templates and tone for customer-facing incident updates |
| SOP-RISK-031 | Model Risk Management Framework | Defines materiality thresholds and SR 11-7 model risk policies |
| SOP-CLAI-014 | Clinical AI Model Monitoring & Rollback | Operational runbook for model degradation detection and remediation |
| SOP-FIN-022 | HealthPay Incident Financial Reconciliation | Governs financial impact assessment during payment incidents |
| SOP-LEG-003 | Regulatory Notification Procedures | Legal review and external notification obligations for reportable events |
| SOP-HR-014 | Employee Relations Escalations | Out-of-scope; included for completeness of escalation landscape |
| SOP-DATA-019 | PHI Data Handling and Access Controls | Defines PHI access roles and audit controls |
| SOP-IT-005 | Internal IT Help Desk Procedures | Distinguishes internal IT from customer-facing support escalation |
| SOP-PM-022 | Product Feature Escalation Process | Covers product enhancement requests, not incident escalation |

### 10.2 External Standards and Frameworks

| Reference | Applicability |
|-----------|---------------|
| NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide) | Guidance for security incident escalation procedures |
| AICPA SOC 2 Trust Services Criteria (CC7.3, CC7.4, CC7.5) | Criteria for incident detection, response, and communication |
| HIPAA Security Rule 45 CFR § 164.308(a)(6)(i) and (ii) | Security incident procedures and response |
| EU AI Act Art. 62 (Reporting of serious incidents) | High-risk AI incident reporting obligations |
| SR 11-7 / OCC 2011-12 (Model Risk Management) | Model validation and incident escalation for financial models |
| EU MDR 2017/745 Art. 87 (Vigilance reporting) | Serious incident reporting for medical devices (CE-marked products) |
| ISO/IEC 27035:2016 (Information Security Incident Management) | Framework alignment for incident management lifecycle |

### 10.3 Tools and Systems Referenced

| System | Purpose |
|--------|---------|
| ServiceNow | Primary ticketing and incident management system |
| PagerDuty | On-call alerting and escalation paging |
| Slack | Real-time incident communication (`#incident-[id]` channels) |
| Zoom | Incident war room bridge |
| AWS IAM / PAM | Just-in-time access management |
| AWS CloudTrail | Audit logging for all AWS actions |
| Datadog | Infrastructure and application monitoring |
| MLflow | Model artifact registry and rollback tracking |
| ArgoCD | GitOps deployment pipeline for model rollbacks |
| LaunchDarkly | Feature flag management for in-app incident banners |
| Medallia | Post-incident customer satisfaction surveys |
| Workday Learning | LMS for training tracking |
| StatusPage (`status.meridian-health.com`) | Public-facing incident status communication |

---

## 11. Revision History

| Version | Date | Author | Description of Change |
|---------|------|--------|----------------------|
| 2.4 | 2025-11-25 | Michael Chang (VP CustOps) | Major revision: added EU AI Act transparency escalation pathway (§4.4); updated Clinical AI escalation to include CE marking considerations (§5.3.3); revised SLOs for SEV1 to 5-min acknowledgement; updated contact roster for Q4 2025 personnel changes (new CISO James Riordan, CPO Maria Santos-Silva); added §6.3 Data Integrity Controls; expanded training program to include live-fire simulation for Tier 3. |
| 2.3 | 2025-06-10 | Michael Chang (VP CustOps) | Added §5.2.3 Escalation Justification Document template; updated §4.3 PHI escalation to 15-minute mandatory timeline (from 30-min); revised SEV3 resolution target to 24h from 48h; added Financial Services model escalation per SR 11-7 guidance; updated approver to Robert Liu per org change. |
| 2.2 | 2025-01-18 | Sarah Chen (former VP CustOps) | Added EU AI Act Art. 62 reference; added Clinical AI Model degradation escalation pathway (§5.3.3); revised §8 Exception Handling to formalize exception types and registry; updated related SOP references for new SOP-ISEC-005 and SOP-RISK-031. |
| 2.1 | 2024-09-02 | Sarah Chen (former VP CustOps) | Restructured §5 Detailed Procedures into subsections for clarity; added RACI matrix (§3.1); added §7 Monitoring & Metrics formal KPI table; removed redundant escalation paths; added BAA mention in scope; expanded training requirements to include simulation for Tier 3; minor formatting fixes. |
| 2.0 | 2024-03-15 | Sarah Chen (former VP CustOps) | Complete rewrite. Merged prior separate escalation SOPs for Support, Engineering, and Security into unified SOP-COPS-012. Introduced tiered model (Tier 1-5, Hierarchy Level 1-3). Added Regulatory Coverage mapping. Approved by Robert Liu (VP FinSvc) and CISO at time. |
| 1.1 | 2023-11-08 | Marcus Williams (former Dir. Support) | Adjusted SEV1 paging roster. Added PagerDuty integration details. |
| 1.0 | 2023-07-17 | Marcus Williams (former Dir. Support) | Initial publication. Based on legacy escalation runbook v5.2. |

---

**End of Document - SOP-COPS-012 v2.4**

*Classification: Internal. This document contains proprietary operating procedures of Meridian Health Technologies, Inc. Unauthorized distribution or reproduction is prohibited.*