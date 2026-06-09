---
sop_id: "SOP-PENG-006"
title: "Accessibility Standards"
business_unit: "Product & Engineering"
version: "3.8"
effective_date: "2024-09-07"
last_reviewed: "2025-12-10"
next_review: "2026-06-07"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Accessibility Standards

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory accessibility requirements, governance framework, and operational procedures for all digital products, platforms, and services developed, acquired, or maintained by Meridian Health Technologies, Inc. (“Meridian”). The purpose of this SOP is to ensure that Meridian’s technology ecosystem is perceivable, operable, understandable, and robust for all users, including individuals with disabilities, in alignment with our commitment to equitable healthcare technology and regulatory compliance obligations.

### 1.2 Scope

This SOP applies to all Meridian business units, employees, contractors, and third-party vendors who contribute to the design, development, procurement, testing, deployment, or maintenance of digital assets that are customer-facing, patient-facing, or internally used by Meridian personnel.

**In-Scope Digital Assets:**

| Asset Category | Examples |
|---|---|
| Customer-Facing Products | Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, Meridian SaaS Platform |
| Patient-Facing Interfaces | Patient portals, payment interfaces, mobile applications, diagnostic report viewers |
| Internal Tools | HR systems, intranet, internal dashboards, administrative consoles, employee self-service portals |
| Public-Facing Properties | meridianhealth.com, documentation portals, developer APIs, support ticketing systems |
| Electronic Documents | Patient-facing reports, billing statements, clinical summaries, training materials, PDFs published after effective date |
| Hardware-Integrated Software | Kiosk applications, medical device user interfaces, on-premise terminal software |
| AI-Generated Content | AI model outputs displayed to users, chatbot interfaces, clinical decision support notifications |
| Procurement | Third-party software acquisitions exceeding $50,000 annual contract value or used by more than 100 employees or patients |

### 1.3 Exclusions

- Legacy systems formally scheduled for decommissioning within 24 months (requires written exemption, see Section 8)
- Internal research prototypes not deployed to production environments
- Third-party content over which Meridian has no editorial control and which is not procured under contract (e.g., user-generated content in community forums before moderation)
- Archived content that is not actively maintained and is clearly marked as archival with alternative contact mechanisms provided

### 1.4 Accessibility and Data Protection

Meridian recognizes that accessible design shares foundational principles with data protection by design and by default. In accordance with the General Data Protection Regulation (GDPR), Meridian conducts Data Protection Impact Assessments (DPIAs) for processing activities involving personal data of individuals with disabilities where such processing may result in high risk to the rights and freedoms of data subjects. Accessibility-related data collection (e.g., user preferences for assistive technologies, accessibility-related analytics) shall be processed in accordance with Meridian’s data minimization and purpose limitation principles as defined in SOP-DATA-003 (Data Protection and Privacy Standards).

### 1.5 Distribution

This SOP shall be distributed to all Product & Engineering personnel, Product Managers, UX Designers, Quality Assurance Engineers, IT Operations staff, Procurement personnel, and any vendor personnel engaged in the development or maintenance of in-scope digital assets. Acknowledgment of receipt and understanding is required within 30 calendar days of onboarding or revision publication.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **A11y** | Abbreviated numeronym for “accessibility” (11 letters between ‘a’ and ‘y’) |
| **ADA** | Americans with Disabilities Act of 1990, as amended |
| **ARIA** | Accessible Rich Internet Applications; W3C technical specification |
| **Assistive Technology (AT)** | Hardware or software that increases, maintains, or improves functional capabilities of individuals with disabilities (e.g., screen readers, screen magnifiers, switch devices, voice recognition software, braille displays, eye-tracking systems) |
| **ATAG** | Authoring Tool Accessibility Guidelines (W3C) |
| **Conformance Level** | A, AA, or AAA as defined by WCAG |
| **DPIA** | Data Protection Impact Assessment |
| **EN 301 549** | European standard for accessibility requirements for ICT products and services |
| **Focus Order** | The sequence in which interactive elements receive keyboard focus during navigation |
| **GDPR** | General Data Protection Regulation (EU) 2016/679 |
| **Keyboard Accessible** | All functionality operable through keyboard interface without requiring specific timings for keystrokes, except where underlying function requires input dependent on path of user movement |
| **Non-Text Content** | Any content that is not a sequence of characters that can be programmatically determined, including images, icons, graphs, charts, audio, video, CAPTCHA, and sensory content |
| **POUR** | Perceivable, Operable, Understandable, Robust — the four WCAG principles |
| **Programmatically Determinable** | Content or properties that can be read and understood by assistive technologies via platform accessibility APIs |
| **Remediation** | The process of correcting accessibility defects identified through testing or user feedback |
| **Screen Reader** | Assistive technology that renders text and image content as speech or braille output (e.g., JAWS, NVDA, VoiceOver, TalkBack) |
| **Section 508** | U.S. Rehabilitation Act amendment requiring federal agencies’ ICT accessibility |
| **Time-Based Media** | Media with duration as a property (audio-only, video-only, audio-video, synchronized captions) |
| **UAAG** | User Agent Accessibility Guidelines (W3C) |
| **VPAT** | Voluntary Product Accessibility Template; document evaluating product against accessibility standards |
| **WCAG** | Web Content Accessibility Guidelines; current standard: WCAG 2.2 (W3C Recommendation, October 2023) |

---

## 3. Roles and Responsibilities

The following responsibility assignment matrix defines accountability for accessibility governance within Meridian Health Technologies.

| Role | Responsibility | Authority |
|---|---|---|
| **VP of Engineering (David Park)** | Executive owner of this SOP; approves accessibility roadmap and resource allocation; reviews annual accessibility audit results; approves exceptions exceeding 12-month remediation timeline | Approves budget ≥$100,000 for remediation initiatives; may delegate operational decisions to A11y Program Manager |
| **A11y Program Manager** | Manages enterprise accessibility program; coordinates VPAT production; oversees external audits; maintains centralized Conformance Registry; tracks remediation SLAs; reports KPIs to AI Governance Committee quarterly | May block production releases for Critical severity accessibility defects (see Section 6.4) |
| **Chief AI Officer (Dr. Marcus Rivera)** | Ensures AI model outputs comply with accessibility requirements; integrates accessibility into ML lifecycle governance alongside NIST AI RMF controls | Approves AI-specific accessibility testing protocols |
| **Chief Information Security Officer (Rachel Kim)** | Ensures accessibility accommodations do not compromise security posture; reviews accessible authentication mechanisms | May veto accessibility accommodations that violate SOC 2 or ISO 27001 controls |
| **Chief Privacy Officer / DPO (Dr. Klaus Weber)** | Evaluates accessibility-related data processing for GDPR compliance; reviews accessibility monitoring tools for privacy implications | Approves accessibility user research protocols involving personal data collection |
| **VP of Clinical AI Products (Dr. Aisha Okafor)** | Accountable for accessibility of Clinical AI Platform outputs, including diagnostic reports, risk scores, and clinical decision support notifications | Approves clinical content accessibility requirements for diagnostic imaging AI |
| **VP of Financial Services (Robert Liu)** | Accountable for accessibility of HealthPay interfaces, patient financing workflows, and lending disclosures | Ensures SR 11-7 model outputs meet accessibility standards for consumer-facing disclosures |
| **Product Managers (per product line)** | Include accessibility requirements in PRDs and user stories; prioritize accessibility defects in backlog; sign off on accessibility acceptance criteria before release | May not release product to production without A11y acceptance sign-off |
| **UX Designers** | Produce accessible design artifacts; annotate designs with accessibility specifications (focus order, heading structure, ARIA roles, color contrast values); maintain Meridian Design System accessibility component library | — |
| **Software Engineers** | Implement designs per accessibility annotations; perform automated and manual accessibility checks during development; remediate defects within assigned SLA timelines | — |
| **QA Engineers** | Execute accessibility test cases per Section 5.3; document defects with severity classification; verify remediation effectiveness | May fail a release candidate on accessibility grounds per Quality Gate criteria |
| **VP of IT Operations (Samantha Torres)** | Ensures internal employee tools (HRIS, intranet, IT service management) meet enterprise accessibility standards; manages assistive technology procurement and support for employees with disabilities | Approves internal tool accessibility exceptions |
| **VP of Customer Operations (Michael Chang)** | Manages accessibility-related customer complaints and feedback channels (see Section 7.3); ensures support documentation is available in accessible formats | — |
| **Procurement Team** | Enforces VPAT requirement for third-party software acquisitions; escalates non-conformant vendor products through exception process | May not execute contracts ≥$50,000 without A11y Program Manager approval |
| **General Counsel (Maria Gonzalez)** | Advises on legal risk related to accessibility non-compliance (ADA, Section 508, EN 301 549, GDPR); reviews settlement agreements and remediation commitments | — |
| **All Meridian Personnel** | Complete annual Accessibility Awareness training (see Section 9); report accessibility barriers encountered in Meridian products per Section 8.3 | — |

---

## 4. Policy Statements

### 4.1 Conformance Standard

All in-scope digital assets shall conform to **WCAG 2.2 Level AA** as the minimum accessibility standard. Meridian additionally adopts the following WCAG 2.2 Level AAA success criteria as mandatory requirements for patient-facing and clinical products:

- **2.3.2 Three Flashes** (no content flashes more than three times per second)
- **3.1.6 Pronunciation** (mechanism for identifying specific pronunciation where meaning is ambiguous without pronunciation — required for clinical terminology in patient-facing diagnostic reports)

For internal employee tools, WCAG 2.2 Level AA applies. For public-facing marketing properties and documentation, WCAG 2.2 Level AA applies with Level AAA encouraged.

### 4.2 Accessible Procurement

Meridian shall not acquire, license, or deploy third-party software that does not meet WCAG 2.2 Level AA, unless a validated exception is approved per Section 8. All requests for proposal (RFPs) for software exceeding $50,000 annual contract value shall require a completed VPAT (or equivalent Accessibility Conformance Report) as a mandatory response requirement. Procurement shall consult the A11y Program Manager before finalizing vendor selection.

### 4.3 Accessible AI and Machine Learning

All AI-generated outputs displayed to users — including but not limited to diagnostic imaging analysis results, patient risk scores, clinical decision support recommendations, adverse event predictions, and claims automation decisions — shall be rendered in formats that conform to WCAG 2.2 Level AA and shall be compatible with screen readers and other assistive technologies. AI model explainability features shall be keyboard-accessible and shall not rely solely on visual cues (e.g., heatmaps) without text-based alternatives.

### 4.4 Inclusive Design

Accessibility shall be integrated into the Meridian Product Development Lifecycle (PDLC) from the requirements phase onward. Design reviews shall include accessibility acceptance criteria. Engineering shall implement accessibility specifications prior to feature completion. “Shift-left” accessibility testing shall be practiced: accessibility defects shall be identified and remediated as early as possible in the development cycle.

### 4.5 Non-Discrimination and Reasonable Accommodation

Meridian prohibits discrimination based on disability in accordance with applicable laws. Internal-facing tools shall be accessible to employees with disabilities. Reasonable accommodations, including provision of assistive technology (hardware and software), shall be provided to employees upon request through CHRO Jennifer Walsh’s office in coordination with VP of IT Operations Samantha Torres.

### 4.6 Continuous Improvement

Meridian commits to ongoing monitoring, auditing, and improvement of accessibility across all digital assets. The A11y Program Manager shall present an Accessibility Maturity Scorecard to the AI Governance Committee semi-annually. A comprehensive third-party accessibility audit shall be conducted annually for each product line.

---

## 5. Detailed Procedures

### 5.1 Accessibility in the Product Development Lifecycle

#### 5.1.1 Requirements Phase

Product Managers shall include accessibility as a non-functional requirement in all Product Requirement Documents (PRDs) and Epic definitions. The following accessibility-specific artifacts shall be produced or updated during this phase:

| Artifact | Owner | Repository |
|---|---|---|
| Accessibility Impact Assessment | Product Manager | Jira Epic (linked to Confluence) |
| User personas inclusive of disabilities | UX Designer | Meridian Design System (Figma) |
| Assistive technology compatibility matrix | UX Designer | Confluence (Product Accessibility Page) |
| VPAT gap analysis (if extending existing product) | A11y Program Manager | Confluence |
| DPIA trigger evaluation (for features collecting accessibility preference data) | Product Manager + DPO | GDPR Compliance Register (OneTrust) |

The **Accessibility Impact Assessment** shall address:

1. **User base affected:** Estimated number of users; known or anticipated disability prevalence in user population
2. **New interaction patterns:** Form controls, modal dialogs, dynamic content updates, drag-and-drop, touch gestures, voice input
3. **Time-based media:** Does the feature include audio, video, or animation?
4. **Data visualizations:** Charts, graphs, heatmaps, dashboards requiring alternative text representation
5. **AI outputs:** If AI-generated content is displayed, what format(s) and what fallback representations are provided?
6. **Authentication mechanisms:** CAPTCHA, biometric, multi-factor; evaluate accessible alternatives
7. **Third-party components:** Identify any libraries, widgets, or embedded content from external sources
8. **Platform matrix:** Target browsers, operating systems, and screen reader combinations per Section 5.3

#### 5.1.2 Design Phase

UX Designers shall produce design artifacts annotated with accessibility specifications. The Meridian Design System (hosted in Figma with linked Storybook components) shall maintain an Accessibility-Validated Component Library. Designers shall use only accessibility-validated components unless an exception is approved.

**Accessibility Design Annotation Checklist:**

| WCAG Principle | Annotation Required | Design Deliverable Reference |
|---|---|---|
| Perceivable | Color contrast ratios (minimum: 4.5:1 text, 3:1 large text, 3:1 UI components) | Design handoff annotations |
| Perceivable | Visible focus indicators for all interactive elements (minimum 2px outline with 3:1 contrast against adjacent colors) | Focus indicator specification in Design System |
| Perceivable | Heading hierarchy (H1-H6) programmatically defined, not implied by visual styling alone | Content structure annotation in wireframes/mockups |
| Perceivable | Alternative text descriptions for all informative images; decorative images marked as decorative | Content specification document |
| Operable | Focus order diagram showing tab sequence through all interactive elements on each screen/view | Focus order diagram (per screen state) |
| Operable | Target size minimum: 24x24 CSS pixels for pointer inputs (WCAG 2.2 Success Criterion 2.5.8) | Component specification |
| Operable | Consistent navigation mechanisms across repeated components (Success Criterion 3.2.3) | Navigation specification |
| Understandable | Labels and instructions for all input fields; error identification and suggestion specification | Error handling wireframes for each form state |
| Understandable | Language declaration per page and per-part language changes for multilingual content | Localization specification |
| Robust | ARIA roles, states, and properties annotated for all custom interactive components | ARIA annotation layer in Figma |

**Design Review Gate:** No design shall proceed to Engineering without documented accessibility annotation review. The A11y Program Manager or designated accessibility specialist (QA Engineer with accessibility certification) conducts this review within 3 business days of submission. Rejection reasons shall be documented in Jira.

#### 5.1.3 Development Phase

Software Engineers shall implement accessibility specifications concurrently with feature development. The following development workflow applies:

**Step 2: Pre-Commit Automated Checks**
Engineers shall configure their local development environment with the following linters and automated checkers:

| Tool | Purpose | Configuration |
|---|---|---|
| **axe-core Linter** (VS Code extension) | Real-time accessibility issue detection in code | Integrated with ESLint; ruleset: WCAG 2.2 AA |
| **eslint-plugin-jsx-a11y** | Static analysis of JSX for accessibility violations | Enabled in CI pipeline; violations = build failure |
| **Accessibility Insights for Web** (browser extension) | FastPass automated checks in development UI | Run before pushing feature branch |
| **Contrast Analyzer** (e.g., TPGi Colour Contrast Analyzer) | Verify color contrast of all UI elements | Run on component before merging to main |

**Step 3: Pull Request Accessibility Checklist**
All pull requests shall include an Accessibility Impact Statement in the PR description, using the following template:

```
### Accessibility Impact Statement
- [ ] No new UI components introduced (skip detailed checklist)
- [ ] New UI components introduced (complete checklist below)

#### New UI Components Checklist:
- [ ] All interactive elements are keyboard accessible (Tab, Enter, Space, Escape, Arrow keys)
- [ ] Focus management handled for dynamic content (modals, disclosures, live regions)
- [ ] Visible focus indicator present on all focusable elements
- [ ] Color contrast ≥4.5:1 for text, ≥3:1 for large text and UI components (verified with Contrast Analyzer)
- [ ] Images have appropriate alt text (informative, decorative, or functional as applicable)
- [ ] ARIA attributes applied only where necessary (per ARIA Authoring Practices)
- [ ] Form inputs have programmatically associated labels
- [ ] Error states are communicated programmatically (not color alone)
- [ ] Page `<title>` is unique and descriptive
- [ ] Heading structure is logical (no skipped levels)
- [ ] `lang` attribute declared on `<html>` element
- [ ] Dynamic content updates use appropriate ARIA live regions (`aria-live`, `aria-atomic`)
- [ ] Touch targets minimum 24x24 CSS pixels (for mobile/touch interfaces)
- [ ] No automatic content changes (auto-play, auto-refresh, auto-submit) without user mechanism to pause, stop, or hide
```

**Step 4: Peer Code Review — Accessibility**
At least one peer reviewer shall explicitly verify the Accessibility Impact Statement against the code diff. Any unchecked mandatory item where applicable shall result in a “Request Changes” review status.

**Step 5: Merge Gate — Automated Accessibility CI Check**
Upon PR approval, the CI/CD pipeline (currently GitHub Actions integrated with SonarQube version 10.x) executes:
1. **axe-core CLI** scanning (headless browser rendering of component storybook stories)
2. **HTML CodeSniffer** rule set: WCAG 2.2 AA
3. **Lighthouse CI** accessibility score threshold: **≥95** for new components, **no regression** below existing score for modified components (see Section 7.1 for monitoring thresholds)

Pipeline failure blocks merge. The Initiator must remediate all Critical and High severity findings before re-running.

### 5.2 Procedure: Third-Party Software Procurement Accessibility Review

**Step 1: Procurement Initiates Accessibility Evaluation**
Procurement identifies that a proposed acquisition falls under in-scope procurement criteria (see Section 1.2). Procurement issues RFP with mandatory VPAT requirement.

**Step 2: Vendor Submits VPAT**
The prospective vendor submits a completed VPAT (Version 2.4 Rev or later) or equivalent Accessibility Conformance Report based on WCAG 2.2. A self-declaration VPAT without third-party validation shall be accepted but weighted lower in evaluation than independently audited conformance reports.

**Step 3: A11y Program Manager Evaluates VPAT**
The A11y Program Manager reviews the VPAT within 5 business days and produces a **Vendor Accessibility Assessment (VAA)** using the standard template stored in Confluence at `/Accessibility/Procurement/VAA-Template`.

The VAA shall rate the vendor product as:
- **Accessibility Rating A (Acceptable):** VPAT declares conformance; Meridian-validated sample testing confirms core workflows accessible; no known open Critical or High accessibility defects.
- **Accessibility Rating B (Conditionally Acceptable):** VPAT identifies non-conformances limited to non-core workflows; vendor provides written remediation roadmap with committed timelines ≤6 months from contract start.
- **Accessibility Rating C (Unacceptable):** VPAT identifies non-conformances in core user workflows; vendor declines to commit to remediation roadmap; product cannot be procured without exception (see Section 8).

**Step 4: Procurement Decision**
Procurement shall not finalize vendor selection without A11y Program Manager sign-off on the VAA. For Accessibility Rating B vendors, the contract shall include a **Supplemental Accessibility Exhibit** requiring remediation deliverables by committed dates, with contractual remedies (e.g., service credits) for non-performance.

### 5.3 Procedure: Accessibility Testing

Testing is structured into four tiers, executed sequentially through the development pipeline.

#### 5.3.1 Tier 1: Automated CI Testing (Per Commit)

See Section 5.1.3 Steps 2-5. This tier catches high-confidence, low-false-positive violations at the earliest stage.

#### 5.3.2 Tier 2: Component-Level Manual Testing (Per Sprint)

QA Engineers execute manual accessibility test scripts against individual components in isolated Storybook/Chromatic environments during each sprint. Test coverage focuses on keyboard operability and screen reader output.

**Meridian Standard Assistive Technology Test Matrix (2025):**

| Assistive Technology | Version | Platform | Applicable Products |
|---|---|---|---|
| **JAWS** (Job Access With Speech) | 2025.x | Windows 11 + Chrome (latest) | Clinical AI Platform, MedInsight, HealthPay (employee-facing), Internal Tools |
| **NVDA** (NonVisual Desktop Access) | 2024.4+ | Windows 11 + Firefox ESR | All products |
| **VoiceOver** | macOS 15 Sequoia, iOS 19 | Safari (macOS), Safari (iOS) | All products |
| **TalkBack** | Android 15+ | Chrome for Android | Patient-facing mobile interfaces |
| **Dragon NaturallySpeaking** | 16 Professional | Windows 11 + Chrome | HealthPay financial workflows, Internal HR tools |
| **ZoomText** | 2025 | Windows 11 + Chrome | Clinical AI diagnostic report viewers |

**Manual Test Script Components:**
- **Keyboard Navigation Test:** Tab through all interactive elements; verify logical order, no keyboard traps, skip navigation links functional
- **Screen Reader Content Test (JAWS + NVDA minimum):** Verify heading structure, link purpose clarity, form label association, dynamic content announcement (e.g., error messages, confirmation modals, AI-generated clinical alerts)
- **Screen Magnifier Test (ZoomText minimum for clinical products):** Verify content does not overflow or truncate at 400% zoom; critical diagnostic information remains legible
- **Voice Recognition Test (Dragon minimum for HealthPay):** Verify all interactive controls are operable by voice command (“Click [button label]”); verify form fields are navigable by voice

#### 5.3.3 Tier 3: Integration Accessibility Testing (Per Release Candidate)

During the integration testing phase (typically sprint review cycle), QA performs end-to-end accessibility testing on complete user journeys:

| User Journey | Test Requirements |
|---|---|
| Clinical AI Platform: Clinician reviews diagnostic image AI analysis, views risk score, exports report | Full screen reader (JAWS + VoiceOver) walkthrough; keyboard-only operation; zoom to 400% |
| HealthPay: Patient logs in, views statement, makes payment, receives confirmation | Voice recognition (Dragon) walkthrough; screen reader; error recovery testing |
| MedInsight: Population health analyst runs report, filters data, exports CSV | Keyboard-only; screen reader data table navigation |

**Defect Documentation Standards:**
QA Engineers document accessibility defects in Jira with the following required fields:

| Field | Acceptable Values / Format | Instructions |
|---|---|---|
| **Issue Type** | Bug | — |
| **Component/s** | Select from component list | — |
| **Accessibility Severity** | Critical, High, Medium, Low | See Appendix A: Severity Classification Matrix |
| **WCAG Success Criterion Violated** | e.g., 1.3.1 Info and Relationships, 2.4.7 Focus Visible | Reference exact SC number |
| **Assistive Technology** (if AT-specific) | JAWS, NVDA, VoiceOver, etc. with version | — |
| **Actual Result** | [Describe barrier experienced by AT user] | Write from user perspective |
| **Expected Result** | [Describe accessible behavior] | Reference WCAG technique |
| **Steps to Reproduce** | Numbered steps | Include AT configuration |
| **Screenshot / Video** | Attachment | Screen reader audio recording strongly recommended for Critical/High |

**Appendix A: Accessibility Severity Classification Matrix**

| Severity | Definition | Example |
|---|---|---|
| **Critical** | User cannot complete a core task; no workaround exists | “Pay Now” button not keyboard-focusable; screen reader does not announce critical clinical alert; CAPTCHA without accessible alternative prevents form submission |
| **High** | User can complete task only with significant difficulty or assistance; workaround is impractical | Form error messages communicated solely by color; data table with no programmatic headers; missing heading structure in lengthy diagnostic report |
| **Medium** | User experiences friction but can complete task; workaround exists | Decorative image not hidden from screen reader; focus indicator present but low contrast; skip navigation link missing but page short |
| **Low** | Minor cosmetic or best-practice violation; no user task blocked | Redundant ARIA attribute; slightly suboptimal reading order (but still logical); deprecated ARIA technique still functional |

#### 5.3.4 Tier 4: External Audit (Annual + Triggered)

Annually, the A11y Program Manager engages an independent third-party accessibility audit firm (selected via RFP through Procurement) to conduct a comprehensive audit of each product line. The audit scope includes:

- Automated scan of full product surface
- Manual expert review per WCAG 2.2 AA and Meridian’s adopted AAA criteria
- Usability testing with assistive technology users (recruited through external accessibility consultancy)
- VPAT/ACR validation (does Meridian’s self-declared conformance match audit findings?)

The external audit report shall be delivered to VP of Engineering, General Counsel, and the AI Governance Committee within 30 calendar days of audit completion. Findings rated Critical or High shall be entered into Jira and tracked through the Remediation procedure (Section 5.5).

### 5.4 Procedure: Accessible AI Output Generation

This procedure governs how Clinical AI Platform and HealthPay AI model outputs are rendered in an accessible manner.

**Step 1: Model Output Format Definition**
During ML model specification, the Product Manager (Clinical AI: Dr. Aisha Okafor’s team; HealthPay: Robert Liu’s team) defines the output schema. For each output field, the schema shall include:

| Metadata Field | Purpose |
|---|---|
| `contentType` | e.g., `numeric_risk_score`, `textual_clinical_note`, `image_diagnostic_overlay`, `structured_tabular` |
| `accessibleRepresentation` | Specification for how this output is rendered to assistive technology |
| `fallbackRepresentation` | Specification for non-visual rendering when primary representation is visual |

**Step 2: Accessible Representation Rendering Rules**

| Output Type | Accessible Rendering Rule |
|---|---|
| **Numeric risk score** | Render as `<output>` element with programmatically associated descriptive label (e.g., “Atrial Fibrillation Stroke Risk Score: 4”). Provide text description of score range and interpretation. |
| **Textual clinical note** | Render as semantic HTML with proper heading structure reflecting note sections (Assessment, Plan, History, etc.). |
| **Diagnostic imaging overlay** (e.g., bounding box on suspected lesion) | Render alternative text-based description of overlay content: bounding box coordinates expressed as anatomical regions (e.g., “Highlighted region: upper lobe right lung, 14mm region of interest”). Text-based coordinate table available via disclosure widget. Do not rely on color alone to distinguish overlay elements. |
| **Chart / graph output** | Provide keyboard-accessible data table (HTML `<table>`) containing underlying data points. Provide text summary of chart trends. The visual chart shall implement accessible SVG patterns with appropriate `aria-label` on chart elements. |
| **Alert / notification** | Render using `role="alert"` or `aria-live="assertive"` for critical results (e.g., “Critical finding: possible pulmonary embolism detected — immediate review recommended”). |

**Step 3: Model Output Accessibility QA**
Before model deployment to production, QA Engineers execute Tier 2 and Tier 3 accessibility tests specifically on the model output rendering pipeline, using the Assistive Technology Test Matrix. Model outputs shall pass all Critical and High severity checks before deployment approval is granted.

**Step 4: Post-Deployment Monitoring**
Any user-reported accessibility defect related to AI outputs shall be triaged per Section 8.3. The A11y Program Manager and VP of Clinical AI Products jointly review AI-output-related accessibility defects quarterly to identify systemic issues requiring model output format redesign.

### 5.5 Procedure: Accessibility Defect Remediation

**Step 1: Defect Triage**
All accessibility defects are triaged during the standard defect triage meeting (weekly for each product line). The Product Manager and QA Lead shall classify each defect per the Severity Classification Matrix (Appendix A, Section 5.3.3).

**Step 2: Remediation Service Level Agreements (SLAs)**

| Severity | Remediation Target (from triage date) | Escalation Trigger |
|---|---|---|
| **Critical** | 5 business days or immediate hotfix | Escalate to A11y Program Manager and Product VP if remediation exceeds 5 business days |
| **High** | Next scheduled release (not to exceed 30 calendar days) | Escalate to A11y Program Manager if deferred beyond 30 calendar days; A11y Program Manager may require interim workaround publication |
| **Medium** | Within 2 release cycles (not to exceed 90 calendar days) | Track in Accessibility Defect Register; reported to A11y Program Manager monthly |
| **Low** | Prioritized in backlog; target within 180 calendar days | Reported in quarterly accessibility metrics |

**Step 3: Remediation Verification**
After engineer marks defect as resolved, QA Engineer assigned to accessibility testing shall verify the fix:
- Re-execute the exact steps to reproduce from the defect report
- Verify fix does not introduce regression in related functionality
- Test with relevant assistive technology combination
- Update Jira defect status to “Resolved — Verified” or re-open with updated reproduction steps

**Step 4: Regression Prevention**
For each Critical-severity defect remediated, the QA team shall add an automated accessibility regression test to the CI/CD pipeline where technically feasible (e.g., axe-core rule mapping for the violated criterion).

### 5.6 Procedure: Accessibility Feedback and Complaint Handling

Meridian provides multiple channels for users to report accessibility barriers:

| Feedback Channel | Managed By | Response SLA |
|---|---|---|
| accessibility@meridianhealth.com | Customer Operations (Michael Chang’s team) | Acknowledgment within 1 business day; initial triage within 3 business days |
| Product in-app “Report Accessibility Issue” (accessible via Settings > Help > Report Accessibility Issue) | Product Manager + A11y Program Manager | Automatic Jira ticket creation; acknowledgment within 1 business day |
| Customer support phone line | Customer Operations | Triage accessible alternative offered if phone is barrier for caller |
| Employee Service Desk (ServiceNow) — internal accessibility issues | IT Operations (Samantha Torres) | Per IT Service Management SLA: Incident response within 4 hours (business hours) |

Customer Operations shall maintain an **Accessibility Feedback Register** in Confluence tracking all user-reported accessibility issues, resolution status, and communication back to the reporter where reporter identity is known and consent for follow-up is given.

---

## 6. Controls and Safeguards

### 6.1 Quality Gate: Accessibility Release Criteria

No product release candidate shall proceed to production without meeting the following accessibility quality gates:

| Quality Gate | Measurement | Threshold |
|---|---|---|
| **Automated Scan Violations** | axe-core CLI / SonarQube scan | Zero Critical, Zero High; Medium ≤3 per 1000 lines of new/changed code |
| **Manual Testing Completion** | Tier 2 test script execution report | 100% of Tier 2 test scripts executed; all Critical and High defects resolved |
| **Accessibility Acceptance Sign-Off** | Jira release checklist item | Signed by A11y Program Manager or designated QA Accessibility Specialist |
| **Regression Gate** | Lighthouse CI accessibility score comparison (current vs. previous release) | Score shall not decrease by more than 3 points; if current score <90, release blocked |

### 6.2 A11y Blocking Authority

The A11y Program Manager possesses blocking authority for any production release containing Critical-severity accessibility defects. This authority may be exercised by withholding the “Accessibility Acceptance” sign-off in the Jira release workflow. A disputed block shall be escalated to the VP of Engineering for final adjudication within 24 business hours. The VP of Engineering shall consult with General Counsel regarding potential legal risk before overriding a block based on accessibility grounds.

### 6.3 Accessible Authentication Safeguards

Authentication mechanisms shall provide accessible alternatives that do not degrade security posture. The following controls apply, coordinated with CISO Rachel Kim:

- **CAPTCHA:** Traditional visual CAPTCHA mechanisms shall provide an accessible alternative (audio CAPTCHA or accessible CAPTCHA service). Meridian endorses Google reCAPTCHA v3 (invisible score-based) where feasible, with a fallback accessible challenge for score-threshold failures.
- **Multi-Factor Authentication (MFA):** MFA options shall include methods accessible to users with disabilities, including authenticator apps compatible with screen readers, SMS for screen reader users (acknowledging SMS is not phishing-resistant), and hardware security keys with tactile indicators.
- **Biometric Authentication:** Biometric-only authentication shall not be the sole mechanism; a non-biometric alternative shall be provided that does not reduce security by more than one assurance level.

### 6.4 Privacy Controls in Accessibility Monitoring

To comply with GDPR obligations related to data processed for accessibility monitoring:

- Automated accessibility testing tools (axe-core, Lighthouse, Accessibility Insights) are configured in **telemetry-off** mode for production user sessions. Accessibility telemetry is collected only from internal pre-production environments and opt-in external beta programs.
- Any collection of accessibility-related analytics from production users (e.g., screen reader usage statistics, browser zoom preferences) shall be subject to a DPIA. The DPIA shall be prepared by the Product Manager and reviewed by the DPO before data collection commences. Data processing purpose limitation documentation shall be maintained in OneTrust.
- International transfers of accessibility analytics data (e.g., from EU-based Clinical AI Platform instances in AWS eu-west-1 to centralized analytics dashboards hosted in AWS us-east-1) are subject to Meridian’s data transfer framework as defined in SOP-DATA-003. The lawful transfer mechanism shall be documented in the Data Transfer Impact Assessment register maintained by the DPO.
- User accessibility preferences stored client-side (e.g., high-contrast mode toggle, reduced motion preference, font size selection) shall not be transmitted to Meridian servers unless explicitly consented to by the user for cross-device synchronization purposes.

### 6.5 Assistive Technology Security

Assistive technologies approved for internal employee use shall be procured through IT Operations and shall undergo standard security review per SOP-IT-002 (Software Acquisition and Vendor Risk Management). Employees shall not install unauthorized screen readers or other AT that may intercept secure session data without IT Operations approval, due to the inherent capability of some AT to access rendering content that may include Protected Health Information (PHI) or payment card data. VP of IT Operations Samantha Torres shall maintain an Approved Assistive Technology Catalog in ServiceNow.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI | Target | Measurement Method | Reporting Cadence |
|---|---|---|---|
| **Mean Time to Remediate Critical Accessibility Defects** | ≤5 business days | Jira query: `severity = Critical AND issueType = Bug AND labels = a11y AND status = Resolved` | Monthly, per product line |
| **Mean Time to Remediate High Accessibility Defects** | ≤30 calendar days | Jira query as above with `severity = High` | Monthly, per product line |
| **Accessibility Defect Backlog Health (% beyond SLA)** | <10% of total open a11y defects | Jira query: compare `created` date to current date per severity SLA | Monthly |
| **Automated Accessibility Score** | ≥95 Lighthouse Accessibility score (all production pages) | Lighthouse CI automated daily scan of critical user flows | Weekly dashboard to Product Managers |
| **Critical User Journey Accessibility Pass Rate** | 100% for Tier 3 manual testing before release | TestRail test case execution results | Per release |
| **VPAT Currency** | All product VPATs updated within 30 calendar days of any major release (version X.0) | Confluence VPAT Register review | Quarterly |
| **Training Completion Rate** | 100% of in-scope personnel completed annual training | Docebo LMS reporting | Quarterly |
| **External Accessibility Feedback Response SLA** | 100% acknowledgment within 1 business day | Confluence Accessibility Feedback Register | Monthly |

### 7.2 Dashboards

The A11y Program Manager maintains:

1. **Accessibility Conformance Registry (Confluence):** Central record of each in-scope digital asset, its current conformance status (Conformant / Partially Conformant / Non-Conformant), current VPAT, and open remediation plan with target dates.
2. **Accessibility Defect Dashboard (Jira Dashboard):** Real-time view of open accessibility defects by severity, product line, and SLA status.
3. **Accessibility Maturity Scorecard (Confluence, semi-annual):** Assessment of Meridian’s accessibility program maturity against the W3C Accessibility Maturity Model dimensions: Policy, Procurement, Development, Testing, Training.

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Owner |
|---|---|---|---|
| Accessibility Defect SLA Compliance | Product Managers, Engineering Managers | Monthly | A11y Program Manager |
| Automated Score Trend Analysis | Product & Engineering leadership | Monthly | QA Lead (automated reporting from Lighthouse CI) |
| Accessibility Maturity Scorecard | AI Governance Committee, VP of Engineering, CEO | Semi-Annual (Q2, Q4) | A11y Program Manager |
| Third-Party Audit Findings | AI Governance Committee, VP of Engineering, General Counsel | Annual (within 30 days of audit completion) | A11y Program Manager |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Categories

Meridian recognizes that in limited circumstances, full conformance to WCAG 2.2 Level AA may not be technically achievable in the immediate term. Exceptions are categorized as follows:

| Category | Definition | Maximum Duration | Approval Authority |
|---|---|---|---|
| **Technical Feasibility Exception** | WCAG success criterion cannot be met due to fundamental limitation of underlying technology platform (e.g., legacy closed-source component that vendor has confirmed will not remediate) | 24 months; must replatform or replace at end of exception period | VP of Engineering + A11y Program Manager |
| **Legacy Decommissioning Exception** | In-scope system formally scheduled for decommissioning; applying accessibility remediation disproportionately costly relative to remaining lifespan | Decommissioning date (max 24 months) | VP of Engineering |
| **Procurement Exception** | Third-party product rated Accessibility Rating C but no accessible alternative exists that meets functional requirements; required for business-critical operation | Contract term (max 36 months); must re-evaluate market at renewal | VP of Engineering + General Counsel |
| **Equivalent Facilitation Exception** | Alternative design or technology provides substantially equivalent or greater accessibility than strict WCAG conformance for a specific user need | Reviewed annually | A11y Program Manager (with external audit validation) |

### 8.2 Exception Request Process

1. **Requestor** (Product Manager or Engineering Manager) submits **Accessibility Exception Request Form** in Confluence (`/Accessibility/Exceptions/Request`). Form must include:
   - WCAG success criterion(ia) affected
   - User impact assessment (affected user population, tasks impacted, workarounds available)
   - Proposed alternative accommodation (e.g., alternative accessible workflow, telephone support line, alternative format documents upon request)
   - Business justification (including cost analysis if financial)
   - Proposed sunset date and remediation conditions

2. **A11y Program Manager** reviews within 10 business days and provides written recommendation (Approve / Approve with Conditions / Deny) with rationale.

3. **Approval Authority** (per table above) makes final determination. General Counsel review is required for any exception that may be subject to legal complaint or that affects patient-facing clinical products.

4. **Published Exception:** All approved exceptions shall be published in the Accessibility Conformance Registry with sunset date. Alternative accommodations shall be communicated to affected users where user population is identifiable.

### 8.3 Escalation Path

| Escalation Level | Trigger | Escalate To | Response Time |
|---|---|---|---|
| Level 1 | Accessibility defect blocking release; standard Quality Gate exercised | VP of Engineering | Within 1 business day |
| Level 2 | Accessibility-related user complaint received by Legal or Executive office | General Counsel + VP of Engineering + A11y Program Manager | Within 24 hours |
| Level 3 | Receipt of formal legal demand letter, government agency inquiry, or litigation filing related to accessibility | General Counsel (lead); CEO + VP of Engineering + A11y Program Manager (response team) | Within 4 hours of receipt |

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum

| Role | Required Training | Frequency | Delivery Method | Minimum Score |
|---|---|---|---|---|
| **All Meridian Personnel** | Accessibility Awareness (Module A11y-100): overview of disability types, assistive technologies, Meridian accessibility policy summary, how to report barriers | Annually | Docebo LMS (e-learning, ~30 minutes) | 80% on knowledge check |
| **UX Designers** | Accessible Design Practices (Module A11y-200): WCAG 2.2 applied to design, accessible design system use, color contrast, typography, inclusive design methods | Annually | Docebo LMS + instructor-led workshop (half day) | 85% on exam + design exercise pass/fail |
| **Software Engineers** | Accessible Development Practices (Module A11y-300): semantic HTML, ARIA (First Rule: Don't Use ARIA), keyboard accessibility, focus management, accessible forms, testing with screen readers | Annually | Docebo LMS + hands-on lab (full day) | 85% on exam + code challenge pass/fail |
| **QA Engineers** | Accessibility Testing (Module A11y-400): manual testing with AT matrix, test script execution, defect severity classification, automated tool configuration | Annually | Docebo LMS + instructor-led certification workshop (2 days) | 85% on exam + practical AT testing evaluation (must demonstrate proficiency with JAWS or NVDA + one mobile screen reader) |
| **Product Managers** | Accessibility in Product Management (Module A11y-500): impact assessment, backlog prioritization, VPAT interpretation, procurement evaluation, user research inclusive of disability | Annually | Instructor-led workshop (half day) | Pass/fail based on Accessibility Impact Assessment exercise |
| **Procurement Team** | Accessible Procurement (Module A11y-600): VPAT evaluation, VAA process, contract exhibits, vendor escalation | Annually | Docebo LMS (~45 minutes) + live session with A11y Program Manager | 80% on knowledge check |

### 9.2 New Hire Onboarding

New hires in roles requiring specialized accessibility training (Design, Engineering, QA, Product Management) shall complete their role-specific accessibility training within **60 calendar days** of start date. The “All Personnel” module (A11y-100) shall be completed within **30 calendar days** of start date.

### 9.3 Training Compliance Tracking

Training completion is tracked via Docebo LMS. Compliance reports are generated monthly by the A11y Program Manager. Managers of personnel with overdue training shall receive automated notification; non-compliance exceeding 90 days shall be escalated to the relevant VP and CHRO.

### 9.4 Supplemental Resources

The A11y Program Manager maintains a Confluence knowledge base (`/Accessibility/Training/Resources`) containing:
- Assistive Technology Quick Reference Guides
- Screen reader keyboard shortcut cheat sheets (JAWS, NVDA, VoiceOver)
- Design annotation templates
- Code snippet library (accessible component patterns)
- Quarterly Accessibility Lunch & Learn recordings

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| SOP-DATA-003 | Data Protection and Privacy Standards | Governs accessibility-related data processing, DPIA process, and international transfers |
| SOP-IT-002 | Software Acquisition and Vendor Risk Management | Overlaps with accessible procurement; security review of assistive technology |
| SOP-DES-001 | Meridian Design System Governance | Design system component library shall align with this Accessibility Standards SOP |
| SOP-QA-004 | Software Quality Assurance and Testing Standards | Testing standards incorporate accessibility Tier 1-3 testing |
| SOP-ML-002 | Machine Learning Model Lifecycle Governance | AI model output accessibility requirements integrate at model specification and release gates |
| SOP-PM-001 | Product Management Lifecycle | PRD template includes Accessibility Impact Assessment requirement |
| SOP-SEC-001 | Identity and Access Management | Accessible authentication controls defined in Section 6.3 |
| SOP-CHRO-001 | Employee Accommodations and Workplace Accessibility | Governs internal employee assistive technology provision and reasonable accommodations |

### 10.2 External Standards and References

| Reference | Version / Date | Applicability |
|---|---|---|
| **WCAG 2.2** (W3C Recommendation) | 5 October 2023 | Conformance standard |
| **ARIA 1.3** (WAI-ARIA) | Current W3C Working Draft (referenced for future-readiness; implement 1.2 stable) | Custom component semantics |
| **EN 301 549** | V3.2.1 (2021-03) | EU accessibility standard for ICT; applicable to CE-marked products |
| **Section 508 Standards** | Revised 2017 (36 CFR Part 1194) | Applicable to products sold to U.S. federal agencies |
| **ADA Title III** (Americans with Disabilities Act) | Public Accommodation applicability to digital services | Legal framework for U.S. patient-facing products |
| **Accessibility Conformance Report (ACR / VPAT)** | ITI VPAT 2.4 Rev (February 2024) | Template version used for conformance documentation |

---

## 11. Revision History

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.0 | 2021-03-15 | A11y Program Manager (initial) | Initial publication. Established WCAG 2.1 Level AA conformance standard. |
| 2.0 | 2022-01-20 | A11y Program Manager | Major revision: expanded scope to include MedInsight and HealthPay post-launch; added accessible procurement section; introduced Tier 1-3 testing framework; aligned with WCAG 2.1 Level AA. |
| 2.5 | 2022-09-10 | A11y Program Manager + CISO (Rachel Kim) | Added Section 6.3 (Accessible Authentication Safeguards); updated AT Test Matrix to include Dragon NaturallySpeaking; revised Quality Gate thresholds. |
| 3.0 | 2023-06-01 | A11y Program Manager + VP of Engineering | Major revision: migrated conformance target to WCAG 2.2 Level AA; introduced Section 5.4 (Accessible AI Output Generation) for Clinical AI Platform; adopted mandatory VPAT requirement for procurement >$50k. |
| 3.5 | 2024-02-15 | A11y Program Manager | Annual review update: revised severity SLA targets based on operational data; updated AT matrix for JAWS 2024 and NVDA 2024.x; integrated DPIA acknowledgment per GDPR compliance review. |
| 3.7 | 2024-07-01 | A11y Program Manager | Mid-cycle update: added WCAG 2.2 SC 2.5.8 (Target Size) design requirement; updated external audit RFP language; added Section 7.1 KPI for accessibility feedback response SLA. |
| **3.8** | **2025-12-10** | **A11y Program Manager** | **Annual comprehensive review: updated AT Test Matrix to 2025 versions (JAWS 2025, VoiceOver on macOS 15/iOS 19, Android 15+ TalkBack); aligned with organizational restructuring (Dr. Aisha Okafor named VP Clinical AI Products, Robert Liu named VP Financial Services); clarified procurement threshold; updated VPAT template reference to ITI 2.4 Rev.** |

---

*This Standard Operating Procedure has been reviewed and approved per Meridian’s Policy Governance Framework. Inquiries regarding this document should be directed to the SOP Owner listed in the document metadata.*