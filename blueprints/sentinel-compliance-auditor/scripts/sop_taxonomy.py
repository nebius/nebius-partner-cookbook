"""
Defines all 200 SOPs for Meridian Health Technologies with metadata,
compliance profiles, and weakness injection specifications.
"""

import hashlib
from typing import Any

WEAKNESS_TEMPLATES: dict[str, dict[str, list[str]]] = {
    "EU AI Act": {
        "partial": [
            "Risk classification is mentioned but lacks formal methodology per Article 6/Annex III",
            "Human oversight procedures exist but do not specify override mechanisms per Article 14",
            "Transparency requirements are addressed generically without referencing Article 13 specifics",
            "Technical documentation exists but does not cover all Annex IV requirements",
            "Quality management system references are vague and not linked to Article 17",
        ],
        "gap": [
            "No AI system risk classification or conformity assessment procedure",
            "Missing fundamental rights impact assessment for high-risk AI systems",
            "No provisions for AI system registration in the EU database per Article 49",
            "Human oversight mechanisms entirely absent despite high-risk classification",
            "No post-market monitoring plan as required by Article 72",
            "Missing data governance requirements for training data per Article 10",
        ],
    },
    "HIPAA": {
        "partial": [
            "Access controls mentioned but minimum necessary standard not operationalized",
            "Breach notification referenced but lacks the 60-day timeline specifics",
            "PHI handling procedures exist but workforce training is only annual, not role-based",
            "Business Associate Agreements mentioned but no BAA inventory or review cycle",
            "Audit controls referenced but logging granularity and retention unspecified",
        ],
        "gap": [
            "No PHI de-identification methodology (neither Safe Harbor nor Expert Determination)",
            "Missing breach notification procedures entirely — no reference to 45 CFR 164.400-414",
            "No documented minimum necessary policies for PHI access",
            "Business Associate oversight completely absent",
            "No individual rights procedures (access, amendment, accounting of disclosures)",
            "Missing risk analysis as required by 45 CFR 164.308(a)(1)(ii)(A)",
        ],
    },
    "SOC 2": {
        "partial": [
            "Change management exists but lacks segregation of duties for approvals",
            "Monitoring is mentioned but alert thresholds and escalation paths are undefined",
            "Availability commitments exist but recovery objectives (RTO/RPO) are not quantified",
            "Logical access controls described but periodic access reviews not mandated",
            "Incident response plan exists but tabletop exercises are not scheduled",
        ],
        "gap": [
            "No formal change management process — changes deployed without approval workflows",
            "Missing continuous monitoring — security events not aggregated or reviewed",
            "No penetration testing program or vulnerability scanning schedule",
            "Vendor/third-party risk assessment process entirely absent",
            "No documented system availability or processing integrity commitments",
            "Missing data classification scheme linked to confidentiality controls",
        ],
    },
    "GDPR": {
        "partial": [
            "Lawful basis for processing mentioned but not documented per processing activity",
            "Data subject rights procedures exist but response timelines exceed 30 days or are vague",
            "DPIA process described but threshold criteria for triggering a DPIA are missing",
            "International transfers acknowledged but Standard Contractual Clauses not referenced",
            "Privacy notices exist but lack the specificity required by Articles 13-14",
        ],
        "gap": [
            "No Record of Processing Activities (Article 30) maintained",
            "Data subject rights procedures completely absent — no access, erasure, or portability",
            "No Data Protection Impact Assessment process for high-risk processing",
            "Cross-border data transfers occur with no documented safeguards (Chapter V)",
            "No documented lawful basis for any processing activity",
            "Consent mechanisms missing — no opt-in, withdrawal, or records",
        ],
    },
    "SR 11-7": {
        "partial": [
            "Model inventory exists but lacks risk-tiering methodology",
            "Validation mentioned but not independent from development team",
            "Model documentation exists but does not include limitations and assumptions",
            "Ongoing monitoring referenced but performance thresholds not defined",
            "Governance structure mentioned but roles of model owner vs. validator not delineated",
        ],
        "gap": [
            "No model risk management framework or model inventory",
            "Independent model validation entirely absent",
            "No model performance monitoring or back-testing procedures",
            "Missing model documentation standards — no model cards or technical specs",
            "No escalation path for model risk findings to board/senior management",
            "Challenger models not required or used for high-impact decisions",
        ],
    },
    "NIST AI RMF": {
        "partial": [
            "AI risk categories referenced but GOVERN function not fully operationalized",
            "MAP function partially addressed — not all AI systems inventoried with risk profiles",
            "MEASURE function has some metrics but lacks systematic bias and fairness testing",
            "MANAGE function described at high level without specific mitigation procedures",
            "Stakeholder engagement mentioned but no structured feedback mechanisms",
        ],
        "gap": [
            "No AI risk management framework adopted or referenced",
            "AI system inventory does not exist — no mapping of AI to organizational risk",
            "No bias, fairness, or equity testing methodology for AI systems",
            "Missing AI impact assessment process",
            "No structured approach to AI trustworthiness (reliability, safety, accountability)",
            "GOVERN function absent — no AI governance body or accountability structure",
        ],
    },
}


def _compliance_level(sop_id: str, regulation: str) -> str:
    seed = hashlib.md5(f"{sop_id}:{regulation}".encode()).hexdigest()
    val = int(seed[:8], 16) % 100
    if val < 40:
        return "compliant"
    if val < 75:
        return "partial"
    return "gap"


def _pick_weaknesses(sop_id: str, regulation: str, level: str) -> list[str]:
    if level == "compliant":
        return []
    options = WEAKNESS_TEMPLATES[regulation][level]
    seed = int(hashlib.md5(f"{sop_id}:{regulation}:w".encode()).hexdigest()[:8], 16)
    count = 2 if level == "partial" else 3
    picked = []
    for i in range(count):
        picked.append(options[(seed + i) % len(options)])
    return picked


SOP_DEFINITIONS: list[dict[str, Any]] = [
    # =========================================================================
    # 1. AI/ML Engineering (20 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-AIML-001", "title": "Model Development Lifecycle",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["model design", "development stages", "approval gates", "documentation requirements"],
        "regulations": ["EU AI Act", "NIST AI RMF", "SR 11-7"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-AIML-002", "title": "Training Data Management and Curation",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["data sourcing", "data quality", "labeling standards", "bias in training data", "data versioning"],
        "regulations": ["EU AI Act", "NIST AI RMF", "GDPR", "HIPAA"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-AIML-003", "title": "Model Training and Hyperparameter Optimization",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["training pipelines", "hyperparameter tuning", "compute allocation", "reproducibility"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-AIML-004", "title": "Model Versioning and Registry Management",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["model registry", "version control", "artifact storage", "lineage tracking"],
        "regulations": ["EU AI Act", "SR 11-7", "SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-AIML-005", "title": "Feature Engineering and Feature Store Operations",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["feature pipelines", "feature store", "feature documentation", "data leakage prevention"],
        "regulations": ["NIST AI RMF", "SR 11-7"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-AIML-006", "title": "Model Performance Monitoring",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["drift detection", "performance metrics", "alerting thresholds", "degradation response"],
        "regulations": ["EU AI Act", "SR 11-7", "NIST AI RMF"],
        "target_pages": 25,
    },
    {
        "sop_id": "SOP-AIML-007", "title": "Model Retraining and Continuous Learning",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["retraining triggers", "data freshness", "validation after retraining", "rollback procedures"],
        "regulations": ["EU AI Act", "SR 11-7", "NIST AI RMF"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-AIML-008", "title": "AI System Risk Classification",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["risk tiers", "classification criteria", "high-risk determination", "Annex III mapping"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-AIML-009", "title": "Algorithmic Bias Detection and Mitigation",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["bias metrics", "fairness testing", "protected attributes", "mitigation strategies", "disparate impact analysis"],
        "regulations": ["EU AI Act", "NIST AI RMF", "GDPR"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-AIML-010", "title": "Explainability and Interpretability Standards",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["SHAP/LIME", "model explanations", "interpretability requirements", "documentation"],
        "regulations": ["EU AI Act", "NIST AI RMF", "SR 11-7", "GDPR"],
        "target_pages": 25,
    },
    {
        "sop_id": "SOP-AIML-011", "title": "ML Pipeline Orchestration",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["pipeline design", "DAG management", "failure handling", "scheduling"],
        "regulations": ["SOC 2", "NIST AI RMF"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-AIML-012", "title": "GPU and Compute Resource Management",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["resource allocation", "cost management", "capacity planning", "access controls"],
        "regulations": ["SOC 2"],
        "target_pages": 16,
    },
    {
        "sop_id": "SOP-AIML-013", "title": "Experiment Tracking and Reproducibility",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["experiment logs", "reproducibility standards", "artifact management", "random seed control"],
        "regulations": ["EU AI Act", "NIST AI RMF", "SR 11-7"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-AIML-014", "title": "Model Documentation and Model Cards",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["model cards", "intended use", "limitations", "performance benchmarks", "ethical considerations"],
        "regulations": ["EU AI Act", "NIST AI RMF", "SR 11-7"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-AIML-015", "title": "Foundation Model and Transfer Learning Usage",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["foundation model selection", "fine-tuning", "license compliance", "supply chain risk"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-AIML-016", "title": "Synthetic Data Generation",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["synthetic data quality", "privacy preservation", "validation", "use case approval"],
        "regulations": ["GDPR", "HIPAA", "NIST AI RMF"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-AIML-017", "title": "Model Compression and Optimization",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["quantization", "pruning", "distillation", "performance validation post-compression"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-AIML-018", "title": "Model Serving and Inference Infrastructure",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["serving architecture", "latency requirements", "scaling", "A/B routing", "rollback"],
        "regulations": ["SOC 2", "EU AI Act"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-AIML-019", "title": "A/B Testing and Canary Releases for Models",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["experiment design", "statistical significance", "canary deployment", "rollback criteria"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-AIML-020", "title": "AI Safety and Alignment Testing",
        "business_unit": "AI/ML Engineering",
        "key_topics": ["safety testing", "red teaming", "adversarial robustness", "alignment verification"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 26,
    },

    # =========================================================================
    # 2. Clinical AI Products (20 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-CLIN-001", "title": "Clinical Decision Support System Validation",
        "business_unit": "Clinical AI Products",
        "key_topics": ["clinical validation", "performance benchmarks", "clinical endpoints", "gold standard comparison"],
        "regulations": ["EU AI Act", "HIPAA", "NIST AI RMF"],
        "target_pages": 32,
    },
    {
        "sop_id": "SOP-CLIN-002", "title": "Medical Device Software Classification",
        "business_unit": "Clinical AI Products",
        "key_topics": ["SaMD classification", "IEC 62304", "risk class determination", "intended purpose"],
        "regulations": ["EU AI Act"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-CLIN-003", "title": "Clinical Trial Data Integration",
        "business_unit": "Clinical AI Products",
        "key_topics": ["trial data ingestion", "data standards", "CDISC compliance", "data quality checks"],
        "regulations": ["HIPAA", "GDPR"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-CLIN-004", "title": "Patient Risk Scoring Algorithms",
        "business_unit": "Clinical AI Products",
        "key_topics": ["risk score design", "calibration", "clinical validation", "threshold setting"],
        "regulations": ["EU AI Act", "HIPAA", "SR 11-7", "NIST AI RMF"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-CLIN-005", "title": "Diagnostic AI Accuracy and Calibration",
        "business_unit": "Clinical AI Products",
        "key_topics": ["sensitivity/specificity", "calibration curves", "confidence intervals", "subgroup analysis"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-CLIN-006", "title": "Clinical AI Human Override Procedures",
        "business_unit": "Clinical AI Products",
        "key_topics": ["clinician override", "override logging", "escalation", "liability"],
        "regulations": ["EU AI Act", "HIPAA", "NIST AI RMF"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-CLIN-007", "title": "Adverse Event Detection and Reporting",
        "business_unit": "Clinical AI Products",
        "key_topics": ["adverse event identification", "severity classification", "reporting timelines", "root cause analysis"],
        "regulations": ["EU AI Act", "HIPAA"],
        "target_pages": 25,
    },
    {
        "sop_id": "SOP-CLIN-008", "title": "Electronic Health Record Integration",
        "business_unit": "Clinical AI Products",
        "key_topics": ["HL7 FHIR", "interoperability", "data mapping", "integration testing"],
        "regulations": ["HIPAA", "SOC 2"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-CLIN-009", "title": "Clinical Workflow Automation",
        "business_unit": "Clinical AI Products",
        "key_topics": ["workflow design", "automation rules", "exception handling", "clinical approval"],
        "regulations": ["EU AI Act", "HIPAA", "NIST AI RMF"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-CLIN-010", "title": "Medical Imaging AI Pipeline",
        "business_unit": "Clinical AI Products",
        "key_topics": ["DICOM handling", "image preprocessing", "inference pipeline", "radiologist review"],
        "regulations": ["EU AI Act", "HIPAA", "NIST AI RMF"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-CLIN-011", "title": "Drug Interaction Checking System",
        "business_unit": "Clinical AI Products",
        "key_topics": ["interaction database", "alert logic", "override documentation", "update cadence"],
        "regulations": ["EU AI Act", "HIPAA"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-CLIN-012", "title": "Clinical AI Output Documentation",
        "business_unit": "Clinical AI Products",
        "key_topics": ["output format", "confidence scores", "explanations", "clinical context"],
        "regulations": ["EU AI Act", "NIST AI RMF", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-CLIN-013", "title": "Patient Safety Monitoring",
        "business_unit": "Clinical AI Products",
        "key_topics": ["safety signals", "monitoring dashboards", "incident escalation", "safety review board"],
        "regulations": ["EU AI Act", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-CLIN-014", "title": "Clinical AI Feedback Loop Management",
        "business_unit": "Clinical AI Products",
        "key_topics": ["clinician feedback collection", "feedback analysis", "model improvement", "bias monitoring"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-CLIN-015", "title": "Regulatory Submission for AI Medical Devices",
        "business_unit": "Clinical AI Products",
        "key_topics": ["510(k) submission", "CE marking", "clinical evidence", "predicate device comparison"],
        "regulations": ["EU AI Act"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-CLIN-016", "title": "Clinical Validation Study Design",
        "business_unit": "Clinical AI Products",
        "key_topics": ["study protocol", "sample size", "endpoints", "statistical analysis plan"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-CLIN-017", "title": "Post-Market Surveillance for AI Products",
        "business_unit": "Clinical AI Products",
        "key_topics": ["surveillance plan", "real-world performance", "complaint handling", "field safety actions"],
        "regulations": ["EU AI Act", "HIPAA"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-CLIN-018", "title": "Clinical AI Labeling and Instructions for Use",
        "business_unit": "Clinical AI Products",
        "key_topics": ["labeling requirements", "intended use statement", "contraindications", "user instructions"],
        "regulations": ["EU AI Act"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-CLIN-019", "title": "Clinical Data De-identification",
        "business_unit": "Clinical AI Products",
        "key_topics": ["Safe Harbor method", "Expert Determination", "re-identification risk", "de-id validation"],
        "regulations": ["HIPAA", "GDPR"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-CLIN-020", "title": "Telehealth AI Integration",
        "business_unit": "Clinical AI Products",
        "key_topics": ["telehealth platform", "AI-assisted triage", "remote monitoring", "data transmission security"],
        "regulations": ["HIPAA", "EU AI Act", "GDPR"],
        "target_pages": 22,
    },

    # =========================================================================
    # 3. Data Governance & Privacy (22 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-DGP-001", "title": "Data Classification and Labeling",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["classification tiers", "labeling standards", "handling requirements per tier", "reclassification"],
        "regulations": ["GDPR", "HIPAA", "SOC 2"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-DGP-002", "title": "Data Retention and Disposal",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["retention schedules", "legal holds", "secure disposal", "certificate of destruction"],
        "regulations": ["GDPR", "HIPAA", "SOC 2"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-DGP-003", "title": "Data Quality Management",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["data quality dimensions", "profiling", "cleansing", "quality metrics and SLAs"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-DGP-004", "title": "Data Catalog and Metadata Management",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["data catalog", "metadata standards", "data dictionary", "search and discovery"],
        "regulations": ["GDPR", "SOC 2"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-DGP-005", "title": "Data Access Control and Authorization",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["role-based access", "access request workflow", "periodic review", "least privilege"],
        "regulations": ["HIPAA", "SOC 2", "GDPR"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-DGP-006", "title": "Data Protection Impact Assessment",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["DPIA methodology", "threshold assessment", "risk scoring", "DPO consultation", "documentation"],
        "regulations": ["GDPR", "EU AI Act"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-DGP-007", "title": "Data Subject Rights Management",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["access requests", "erasure", "portability", "rectification", "restriction", "objection", "response timelines"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-DGP-008", "title": "Consent Management",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["consent collection", "granularity", "withdrawal", "consent records", "re-consent"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-DGP-009", "title": "Cross-Border Data Transfer",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["adequacy decisions", "SCCs", "BCRs", "transfer impact assessments", "supplementary measures"],
        "regulations": ["GDPR"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-DGP-010", "title": "Data Breach Response and Notification",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["breach detection", "containment", "assessment", "notification timelines", "documentation"],
        "regulations": ["GDPR", "HIPAA", "SOC 2"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-DGP-011", "title": "Data Lineage Tracking",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["lineage capture", "transformation tracking", "impact analysis", "visualization"],
        "regulations": ["EU AI Act", "SOC 2", "NIST AI RMF"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-DGP-012", "title": "Data Sharing Agreements",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["agreement templates", "review process", "data use limitations", "termination clauses"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-DGP-013", "title": "Record of Processing Activities",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["ROPA template", "processing inventory", "update cadence", "controller vs processor records"],
        "regulations": ["GDPR"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-DGP-014", "title": "Anonymization and Pseudonymization",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["anonymization techniques", "pseudonymization", "re-identification risk", "key management"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-DGP-015", "title": "Third-Party Data Processor Oversight",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["processor selection", "DPA requirements", "audit rights", "sub-processor management"],
        "regulations": ["GDPR", "HIPAA", "SOC 2"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-DGP-016", "title": "Data Minimization Standards",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["collection limitation", "purpose limitation", "storage limitation", "periodic review"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-DGP-017", "title": "Privacy by Design and Default",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["design principles", "privacy requirements in SDLC", "default settings", "privacy review gates"],
        "regulations": ["GDPR", "EU AI Act"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-DGP-018", "title": "Cookie and Online Tracking Consent",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["cookie categories", "consent banner", "opt-in/opt-out", "cookie audit"],
        "regulations": ["GDPR"],
        "target_pages": 16,
    },
    {
        "sop_id": "SOP-DGP-019", "title": "Children's Data Protection",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["age verification", "parental consent", "data minimization for minors", "COPPA considerations"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-DGP-020", "title": "Data Protection Officer Responsibilities",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["DPO role", "independence", "reporting lines", "tasks per Article 39", "resources"],
        "regulations": ["GDPR"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-DGP-021", "title": "Lawful Basis Determination",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["six lawful bases", "legitimate interest assessment", "documentation", "basis selection"],
        "regulations": ["GDPR"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-DGP-022", "title": "Automated Decision-Making Transparency",
        "business_unit": "Data Governance & Privacy",
        "key_topics": ["Article 22 rights", "meaningful information", "human intervention", "impact on individuals"],
        "regulations": ["GDPR", "EU AI Act", "NIST AI RMF"],
        "target_pages": 24,
    },

    # =========================================================================
    # 4. Financial Services (20 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-FIN-001", "title": "Credit Scoring Model Governance",
        "business_unit": "Financial Services",
        "key_topics": ["model governance", "approval process", "model inventory", "risk tiering"],
        "regulations": ["SR 11-7", "EU AI Act", "NIST AI RMF"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-FIN-002", "title": "Fraud Detection System Operations",
        "business_unit": "Financial Services",
        "key_topics": ["fraud rules", "ML fraud models", "alert triage", "false positive management"],
        "regulations": ["SR 11-7", "SOC 2", "EU AI Act"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-FIN-003", "title": "Payment Processing Controls",
        "business_unit": "Financial Services",
        "key_topics": ["transaction processing", "reconciliation", "exception handling", "PCI DSS alignment"],
        "regulations": ["SOC 2"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-FIN-004", "title": "Anti-Money Laundering Procedures",
        "business_unit": "Financial Services",
        "key_topics": ["AML program", "suspicious activity reporting", "transaction monitoring", "sanctions screening"],
        "regulations": ["SOC 2", "GDPR"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-FIN-005", "title": "Know Your Customer Verification",
        "business_unit": "Financial Services",
        "key_topics": ["identity verification", "document requirements", "ongoing due diligence", "enhanced due diligence"],
        "regulations": ["GDPR", "SOC 2"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-FIN-006", "title": "Lending Decision Documentation",
        "business_unit": "Financial Services",
        "key_topics": ["decision rationale", "adverse action notices", "fair lending", "record retention"],
        "regulations": ["SR 11-7", "EU AI Act", "GDPR"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-FIN-007", "title": "Financial Model Validation",
        "business_unit": "Financial Services",
        "key_topics": ["independent validation", "challenger models", "back-testing", "validation reporting"],
        "regulations": ["SR 11-7"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-FIN-008", "title": "Market Risk Assessment",
        "business_unit": "Financial Services",
        "key_topics": ["risk identification", "measurement methodology", "stress scenarios", "risk limits"],
        "regulations": ["SR 11-7", "SOC 2"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-FIN-009", "title": "Operational Risk Management",
        "business_unit": "Financial Services",
        "key_topics": ["risk taxonomy", "RCSA", "loss event tracking", "key risk indicators"],
        "regulations": ["SR 11-7", "SOC 2"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-FIN-010", "title": "Regulatory Capital Reporting",
        "business_unit": "Financial Services",
        "key_topics": ["capital calculations", "reporting templates", "submission timelines", "data validation"],
        "regulations": ["SR 11-7"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-FIN-011", "title": "Interest Rate Risk Management",
        "business_unit": "Financial Services",
        "key_topics": ["gap analysis", "duration management", "hedging strategies", "rate scenarios"],
        "regulations": ["SR 11-7"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-FIN-012", "title": "Collections and Recovery Procedures",
        "business_unit": "Financial Services",
        "key_topics": ["collection strategies", "hardship programs", "fair debt practices", "recovery tracking"],
        "regulations": ["GDPR", "SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-FIN-013", "title": "Financial Data Reconciliation",
        "business_unit": "Financial Services",
        "key_topics": ["reconciliation procedures", "break resolution", "materiality thresholds", "audit trail"],
        "regulations": ["SOC 2"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-FIN-014", "title": "Third-Party Payment Provider Management",
        "business_unit": "Financial Services",
        "key_topics": ["provider selection", "due diligence", "ongoing monitoring", "contractual requirements"],
        "regulations": ["SOC 2", "GDPR"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-FIN-015", "title": "Transaction Monitoring and Alerts",
        "business_unit": "Financial Services",
        "key_topics": ["monitoring rules", "alert thresholds", "investigation procedures", "SAR filing"],
        "regulations": ["SOC 2", "SR 11-7"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-FIN-016", "title": "Financial Reporting and Disclosure",
        "business_unit": "Financial Services",
        "key_topics": ["reporting standards", "disclosure requirements", "internal controls", "review process"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-FIN-017", "title": "Customer Complaint Handling — Financial Products",
        "business_unit": "Financial Services",
        "key_topics": ["complaint intake", "investigation", "resolution timelines", "regulatory reporting"],
        "regulations": ["GDPR", "SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-FIN-018", "title": "Credit Risk Model Back-Testing",
        "business_unit": "Financial Services",
        "key_topics": ["back-testing methodology", "performance windows", "outcome analysis", "recalibration triggers"],
        "regulations": ["SR 11-7", "NIST AI RMF"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-FIN-019", "title": "Stress Testing Procedures",
        "business_unit": "Financial Services",
        "key_topics": ["scenario design", "sensitivity analysis", "reverse stress testing", "results reporting"],
        "regulations": ["SR 11-7"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-FIN-020", "title": "Fair Lending Compliance",
        "business_unit": "Financial Services",
        "key_topics": ["disparate impact testing", "fair lending monitoring", "ECOA/FCRA alignment", "remediation"],
        "regulations": ["SR 11-7", "EU AI Act", "GDPR"],
        "target_pages": 26,
    },

    # =========================================================================
    # 5. Information Security (22 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-ISEC-001", "title": "Information Security Policy Framework",
        "business_unit": "Information Security",
        "key_topics": ["policy hierarchy", "scope", "governance structure", "review cycle", "exception process"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-ISEC-002", "title": "Access Control and Identity Management",
        "business_unit": "Information Security",
        "key_topics": ["IAM framework", "authentication", "authorization", "SSO", "MFA", "access reviews"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-ISEC-003", "title": "Network Security and Segmentation",
        "business_unit": "Information Security",
        "key_topics": ["network architecture", "segmentation", "firewall rules", "IDS/IPS", "VPN"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-ISEC-004", "title": "Endpoint Protection and Management",
        "business_unit": "Information Security",
        "key_topics": ["EDR", "patch management", "device hardening", "encryption at rest"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-ISEC-005", "title": "Vulnerability Management and Patching",
        "business_unit": "Information Security",
        "key_topics": ["scanning cadence", "severity classification", "patching SLAs", "exception process"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-ISEC-006", "title": "Security Incident Response",
        "business_unit": "Information Security",
        "key_topics": ["incident classification", "response team", "containment", "eradication", "post-incident review"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-ISEC-007", "title": "Security Awareness Training",
        "business_unit": "Information Security",
        "key_topics": ["training program", "phishing simulations", "role-based training", "completion tracking"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-ISEC-008", "title": "Cryptographic Controls and Key Management",
        "business_unit": "Information Security",
        "key_topics": ["encryption standards", "key lifecycle", "key rotation", "HSM usage", "certificate management"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-ISEC-009", "title": "Cloud Security Standards",
        "business_unit": "Information Security",
        "key_topics": ["cloud configuration", "shared responsibility", "CIS benchmarks", "cloud access security"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-ISEC-010", "title": "Application Security Testing",
        "business_unit": "Information Security",
        "key_topics": ["SAST", "DAST", "SCA", "security requirements", "remediation SLAs"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-ISEC-011", "title": "Third-Party Security Assessment",
        "business_unit": "Information Security",
        "key_topics": ["vendor risk assessment", "security questionnaires", "risk tiering", "ongoing monitoring"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-ISEC-012", "title": "Security Logging and Monitoring",
        "business_unit": "Information Security",
        "key_topics": ["log sources", "SIEM", "correlation rules", "retention", "alerting"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-ISEC-013", "title": "Physical Security Controls",
        "business_unit": "Information Security",
        "key_topics": ["facility access", "visitor management", "environmental controls", "equipment disposal"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-ISEC-014", "title": "Mobile Device Management",
        "business_unit": "Information Security",
        "key_topics": ["MDM enrollment", "device policies", "remote wipe", "app management"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-ISEC-015", "title": "Data Loss Prevention",
        "business_unit": "Information Security",
        "key_topics": ["DLP policies", "content inspection", "channel controls", "incident handling"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-ISEC-016", "title": "Penetration Testing Program",
        "business_unit": "Information Security",
        "key_topics": ["scope", "methodology", "frequency", "finding classification", "remediation tracking"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-ISEC-017", "title": "Security Architecture Review",
        "business_unit": "Information Security",
        "key_topics": ["architecture review process", "threat modeling", "design patterns", "approval gates"],
        "regulations": ["SOC 2"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-ISEC-018", "title": "Zero Trust Network Architecture",
        "business_unit": "Information Security",
        "key_topics": ["zero trust principles", "micro-segmentation", "identity-centric security", "implementation roadmap"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-ISEC-019", "title": "Privileged Access Management",
        "business_unit": "Information Security",
        "key_topics": ["PAM solution", "just-in-time access", "session recording", "break-glass procedures"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-ISEC-020", "title": "Business Email Compromise Prevention",
        "business_unit": "Information Security",
        "key_topics": ["email security", "DMARC/DKIM/SPF", "BEC detection", "wire transfer verification"],
        "regulations": ["SOC 2"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-ISEC-021", "title": "Supply Chain Security",
        "business_unit": "Information Security",
        "key_topics": ["software supply chain", "SBOM", "dependency scanning", "vendor integrity"],
        "regulations": ["SOC 2", "EU AI Act"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-ISEC-022", "title": "Security Metrics and Reporting",
        "business_unit": "Information Security",
        "key_topics": ["KPIs", "KRIs", "dashboard design", "board reporting", "trend analysis"],
        "regulations": ["SOC 2"],
        "target_pages": 18,
    },

    # =========================================================================
    # 6. IT Operations & Infrastructure (20 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-ITOP-001", "title": "Change Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["change types", "CAB review", "approval workflow", "rollback procedures", "emergency changes"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-ITOP-002", "title": "Incident Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["incident classification", "severity levels", "escalation", "communication", "resolution"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-ITOP-003", "title": "Problem Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["root cause analysis", "known error database", "problem trends", "permanent fixes"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-ITOP-004", "title": "Configuration Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["CMDB", "configuration items", "baseline management", "drift detection"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-ITOP-005", "title": "Capacity Planning and Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["capacity monitoring", "forecasting", "scaling triggers", "performance baselines"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-ITOP-006", "title": "Disaster Recovery",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["DR plan", "RTO/RPO", "failover procedures", "DR testing", "communication plan"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-ITOP-007", "title": "Business Continuity Planning",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["BIA", "continuity strategies", "plan activation", "testing schedule"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-ITOP-008", "title": "Backup and Restoration",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["backup schedule", "backup types", "encryption", "restoration testing", "offsite storage"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-ITOP-009", "title": "System Availability Monitoring",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["uptime tracking", "health checks", "alerting", "SLA reporting"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-ITOP-010", "title": "Cloud Infrastructure Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["AWS governance", "account structure", "tagging", "cost management", "security groups"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-ITOP-011", "title": "Database Administration",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["database provisioning", "access controls", "backup", "performance tuning", "patching"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-ITOP-012", "title": "Release Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["release planning", "deployment windows", "go/no-go criteria", "release notes"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-ITOP-013", "title": "Service Level Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["SLA definition", "OLA/UC", "SLA monitoring", "service reviews"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-ITOP-014", "title": "IT Asset Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["asset inventory", "lifecycle tracking", "license management", "disposal"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-ITOP-015", "title": "Network Operations",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["network monitoring", "topology management", "bandwidth management", "troubleshooting"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-ITOP-016", "title": "Server Provisioning and Decommissioning",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["provisioning standards", "hardening", "decommission checklist", "data sanitization"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-ITOP-017", "title": "Environment Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["dev/stage/prod separation", "data masking", "environment refresh", "access controls"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-ITOP-018", "title": "Infrastructure as Code Standards",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["IaC tools", "code review", "drift detection", "state management"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-ITOP-019", "title": "Log Management and Retention",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["log collection", "centralization", "retention periods", "integrity protection"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-ITOP-020", "title": "DNS and Certificate Management",
        "business_unit": "IT Operations & Infrastructure",
        "key_topics": ["DNS governance", "certificate lifecycle", "renewal automation", "revocation"],
        "regulations": ["SOC 2"],
        "target_pages": 18,
    },

    # =========================================================================
    # 7. Human Resources (18 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-HR-001", "title": "Employee Onboarding and Access Provisioning",
        "business_unit": "Human Resources",
        "key_topics": ["onboarding checklist", "access provisioning", "orientation", "policy acknowledgment"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-HR-002", "title": "Background Check and Screening",
        "business_unit": "Human Resources",
        "key_topics": ["screening requirements", "check types", "adjudication", "adverse action", "GDPR considerations"],
        "regulations": ["GDPR", "HIPAA", "SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-HR-003", "title": "Security Clearance Management",
        "business_unit": "Human Resources",
        "key_topics": ["clearance levels", "investigation process", "access mapping", "periodic reinvestigation"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-HR-004", "title": "Employee Termination and Offboarding",
        "business_unit": "Human Resources",
        "key_topics": ["access revocation", "exit interview", "equipment return", "knowledge transfer"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-HR-005", "title": "Acceptable Use Policy",
        "business_unit": "Human Resources",
        "key_topics": ["permitted use", "prohibited activities", "monitoring", "enforcement"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-HR-006", "title": "Remote Work and BYOD Policy",
        "business_unit": "Human Resources",
        "key_topics": ["remote work security", "BYOD enrollment", "VPN requirements", "data handling"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-HR-007", "title": "Employee Data Privacy",
        "business_unit": "Human Resources",
        "key_topics": ["employee personal data", "processing purposes", "retention", "employee rights"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-HR-008", "title": "Mandatory Compliance Training",
        "business_unit": "Human Resources",
        "key_topics": ["training catalog", "role-based requirements", "completion tracking", "remedial training"],
        "regulations": ["HIPAA", "SOC 2", "GDPR", "EU AI Act"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-HR-009", "title": "Code of Ethics and Conduct",
        "business_unit": "Human Resources",
        "key_topics": ["ethical standards", "conflicts of interest", "gifts and entertainment", "reporting violations"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-HR-010", "title": "Whistleblower Protection",
        "business_unit": "Human Resources",
        "key_topics": ["reporting channels", "anonymity", "non-retaliation", "investigation process"],
        "regulations": ["SOC 2", "EU AI Act"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-HR-011", "title": "Conflict of Interest Disclosure",
        "business_unit": "Human Resources",
        "key_topics": ["disclosure requirements", "review process", "mitigation plans", "annual attestation"],
        "regulations": ["SOC 2"],
        "target_pages": 16,
    },
    {
        "sop_id": "SOP-HR-012", "title": "AI Ethics Committee Governance",
        "business_unit": "Human Resources",
        "key_topics": ["committee charter", "membership", "review process", "decision authority", "escalation"],
        "regulations": ["EU AI Act", "NIST AI RMF"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-HR-013", "title": "Diversity, Equity, and Non-Discrimination",
        "business_unit": "Human Resources",
        "key_topics": ["non-discrimination policy", "accommodations", "complaint procedures", "metrics"],
        "regulations": ["GDPR", "EU AI Act"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-HR-014", "title": "Workplace Health and Safety",
        "business_unit": "Human Resources",
        "key_topics": ["safety program", "incident reporting", "ergonomics", "emergency procedures"],
        "regulations": ["SOC 2"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-HR-015", "title": "Performance Review and Documentation",
        "business_unit": "Human Resources",
        "key_topics": ["review cycle", "documentation standards", "rating calibration", "performance improvement plans"],
        "regulations": ["GDPR"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-HR-016", "title": "Contractor and Temporary Staff Management",
        "business_unit": "Human Resources",
        "key_topics": ["contractor onboarding", "access limitations", "NDA requirements", "offboarding"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-HR-017", "title": "Employee Data Subject Access Requests",
        "business_unit": "Human Resources",
        "key_topics": ["DSAR process", "identity verification", "response timeline", "exemptions"],
        "regulations": ["GDPR"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-HR-018", "title": "AI-Assisted HR Decision Making",
        "business_unit": "Human Resources",
        "key_topics": ["AI in recruitment", "automated screening", "bias monitoring", "human oversight", "transparency"],
        "regulations": ["EU AI Act", "GDPR", "NIST AI RMF"],
        "target_pages": 26,
    },

    # =========================================================================
    # 8. Legal & Compliance (20 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-LEGC-001", "title": "Regulatory Change Management",
        "business_unit": "Legal & Compliance",
        "key_topics": ["regulatory horizon scanning", "impact assessment", "implementation planning", "tracking"],
        "regulations": ["EU AI Act", "HIPAA", "SOC 2", "GDPR", "SR 11-7", "NIST AI RMF"],
        "target_pages": 28,
    },
    {
        "sop_id": "SOP-LEGC-002", "title": "Compliance Risk Assessment",
        "business_unit": "Legal & Compliance",
        "key_topics": ["risk identification", "inherent vs residual risk", "risk appetite", "risk register"],
        "regulations": ["SOC 2", "SR 11-7", "EU AI Act"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-LEGC-003", "title": "Internal Audit Program",
        "business_unit": "Legal & Compliance",
        "key_topics": ["audit universe", "risk-based planning", "audit execution", "finding management"],
        "regulations": ["SOC 2", "HIPAA", "GDPR", "SR 11-7"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-LEGC-004", "title": "External Audit Coordination",
        "business_unit": "Legal & Compliance",
        "key_topics": ["auditor selection", "audit preparation", "evidence management", "finding remediation"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-LEGC-005", "title": "Regulatory Filing and Reporting",
        "business_unit": "Legal & Compliance",
        "key_topics": ["filing calendar", "reporting templates", "review workflow", "submission tracking"],
        "regulations": ["HIPAA", "GDPR", "SR 11-7"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-LEGC-006", "title": "Contract Review and Approval",
        "business_unit": "Legal & Compliance",
        "key_topics": ["review workflow", "clause library", "risk assessment", "approval authority"],
        "regulations": ["GDPR", "HIPAA", "SOC 2"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-LEGC-007", "title": "Intellectual Property Management",
        "business_unit": "Legal & Compliance",
        "key_topics": ["IP identification", "patent process", "trade secrets", "open source compliance"],
        "regulations": ["EU AI Act"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-LEGC-008", "title": "Litigation Hold and E-Discovery",
        "business_unit": "Legal & Compliance",
        "key_topics": ["hold notices", "data preservation", "collection", "production", "defensibility"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-LEGC-009", "title": "Compliance Training Program",
        "business_unit": "Legal & Compliance",
        "key_topics": ["training needs assessment", "curriculum design", "delivery methods", "effectiveness measurement"],
        "regulations": ["HIPAA", "GDPR", "EU AI Act", "SOC 2"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-LEGC-010", "title": "Policy Lifecycle Management",
        "business_unit": "Legal & Compliance",
        "key_topics": ["policy creation", "review cycle", "version control", "distribution", "attestation"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-LEGC-011", "title": "Regulatory Inquiry Response",
        "business_unit": "Legal & Compliance",
        "key_topics": ["inquiry triage", "response coordination", "document production", "communication protocols"],
        "regulations": ["HIPAA", "GDPR", "EU AI Act"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-LEGC-012", "title": "Board and Committee Governance",
        "business_unit": "Legal & Compliance",
        "key_topics": ["committee charters", "meeting cadence", "reporting requirements", "minutes and records"],
        "regulations": ["SOC 2", "SR 11-7"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-LEGC-013", "title": "Compliance Monitoring and Testing",
        "business_unit": "Legal & Compliance",
        "key_topics": ["monitoring plan", "testing methodology", "issue tracking", "remediation verification"],
        "regulations": ["SOC 2", "HIPAA", "GDPR", "SR 11-7"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-LEGC-014", "title": "Sanctions and Export Control",
        "business_unit": "Legal & Compliance",
        "key_topics": ["sanctions screening", "export classification", "restricted parties", "license management"],
        "regulations": ["SOC 2"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-LEGC-015", "title": "Ethics Hotline Management",
        "business_unit": "Legal & Compliance",
        "key_topics": ["hotline operations", "intake process", "investigation", "case management", "reporting"],
        "regulations": ["SOC 2", "EU AI Act"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-LEGC-016", "title": "Vendor Compliance Assessment",
        "business_unit": "Legal & Compliance",
        "key_topics": ["vendor risk tiering", "assessment methodology", "ongoing monitoring", "remediation"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-LEGC-017", "title": "Regulatory Licensing Management",
        "business_unit": "Legal & Compliance",
        "key_topics": ["license inventory", "renewal tracking", "state-by-state requirements", "compliance verification"],
        "regulations": ["SOC 2"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-LEGC-018", "title": "Cross-Jurisdictional Compliance Coordination",
        "business_unit": "Legal & Compliance",
        "key_topics": ["jurisdiction mapping", "conflict resolution", "local counsel coordination", "harmonization"],
        "regulations": ["GDPR", "EU AI Act", "HIPAA"],
        "target_pages": 26,
    },
    {
        "sop_id": "SOP-LEGC-019", "title": "AI Regulation Compliance Framework",
        "business_unit": "Legal & Compliance",
        "key_topics": ["AI regulatory mapping", "compliance controls", "evidence collection", "gap analysis"],
        "regulations": ["EU AI Act", "NIST AI RMF", "SR 11-7"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-LEGC-020", "title": "Enforcement Action Response Plan",
        "business_unit": "Legal & Compliance",
        "key_topics": ["action classification", "response team", "communication plan", "remediation", "lessons learned"],
        "regulations": ["EU AI Act", "HIPAA", "GDPR", "SR 11-7"],
        "target_pages": 24,
    },

    # =========================================================================
    # 9. Product & Engineering (20 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-PENG-001", "title": "Secure Software Development Lifecycle",
        "business_unit": "Product & Engineering",
        "key_topics": ["SDLC phases", "security gates", "threat modeling", "secure coding standards"],
        "regulations": ["SOC 2", "HIPAA", "EU AI Act"],
        "target_pages": 30,
    },
    {
        "sop_id": "SOP-PENG-002", "title": "Code Review and Approval",
        "business_unit": "Product & Engineering",
        "key_topics": ["review requirements", "approval matrix", "automated checks", "security review triggers"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-PENG-003", "title": "API Design and Security Standards",
        "business_unit": "Product & Engineering",
        "key_topics": ["API design guidelines", "authentication", "rate limiting", "input validation", "documentation"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-PENG-004", "title": "Software Quality Assurance",
        "business_unit": "Product & Engineering",
        "key_topics": ["QA strategy", "test coverage", "defect management", "release criteria"],
        "regulations": ["SOC 2"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-PENG-005", "title": "Performance Testing and Benchmarking",
        "business_unit": "Product & Engineering",
        "key_topics": ["load testing", "stress testing", "baseline metrics", "performance budgets"],
        "regulations": ["SOC 2"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-PENG-006", "title": "Accessibility Standards",
        "business_unit": "Product & Engineering",
        "key_topics": ["WCAG compliance", "accessibility testing", "assistive technology", "remediation"],
        "regulations": ["GDPR"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-PENG-007", "title": "Feature Flag Management",
        "business_unit": "Product & Engineering",
        "key_topics": ["flag lifecycle", "targeting rules", "cleanup process", "audit trail"],
        "regulations": ["SOC 2"],
        "target_pages": 16,
    },
    {
        "sop_id": "SOP-PENG-008", "title": "Technical Debt Management",
        "business_unit": "Product & Engineering",
        "key_topics": ["debt identification", "prioritization", "tracking", "remediation planning"],
        "regulations": ["SOC 2"],
        "target_pages": 16,
    },
    {
        "sop_id": "SOP-PENG-009", "title": "Open Source Software Usage",
        "business_unit": "Product & Engineering",
        "key_topics": ["license compliance", "vulnerability scanning", "approval process", "SBOM"],
        "regulations": ["SOC 2", "EU AI Act"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-PENG-010", "title": "Microservices Architecture Standards",
        "business_unit": "Product & Engineering",
        "key_topics": ["service boundaries", "communication patterns", "observability", "resilience"],
        "regulations": ["SOC 2"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-PENG-011", "title": "CI/CD Pipeline Security",
        "business_unit": "Product & Engineering",
        "key_topics": ["pipeline hardening", "secret management", "artifact signing", "deployment approvals"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-PENG-012", "title": "Software Bill of Materials",
        "business_unit": "Product & Engineering",
        "key_topics": ["SBOM generation", "dependency tracking", "vulnerability correlation", "customer disclosure"],
        "regulations": ["SOC 2", "EU AI Act"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-PENG-013", "title": "Product Security Incident Response",
        "business_unit": "Product & Engineering",
        "key_topics": ["vulnerability disclosure", "triage", "patching", "customer notification"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-PENG-014", "title": "User Acceptance Testing",
        "business_unit": "Product & Engineering",
        "key_topics": ["UAT planning", "test scenarios", "sign-off process", "defect resolution"],
        "regulations": ["SOC 2"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-PENG-015", "title": "Technical Documentation Standards",
        "business_unit": "Product & Engineering",
        "key_topics": ["documentation types", "templates", "review process", "versioning"],
        "regulations": ["SOC 2", "EU AI Act"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-PENG-016", "title": "Data Migration Procedures",
        "business_unit": "Product & Engineering",
        "key_topics": ["migration planning", "data validation", "rollback", "post-migration verification"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-PENG-017", "title": "Service Deprecation and Sunset",
        "business_unit": "Product & Engineering",
        "key_topics": ["deprecation policy", "customer notification", "migration support", "data handling"],
        "regulations": ["SOC 2", "GDPR"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-PENG-018", "title": "API Versioning and Backward Compatibility",
        "business_unit": "Product & Engineering",
        "key_topics": ["versioning strategy", "breaking changes", "deprecation timeline", "client migration"],
        "regulations": ["SOC 2"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-PENG-019", "title": "Platform Reliability Engineering",
        "business_unit": "Product & Engineering",
        "key_topics": ["SLOs/SLIs", "error budgets", "chaos engineering", "incident review"],
        "regulations": ["SOC 2"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-PENG-020", "title": "AI Feature Integration Standards",
        "business_unit": "Product & Engineering",
        "key_topics": ["AI integration patterns", "model serving integration", "fallback behavior", "user transparency"],
        "regulations": ["EU AI Act", "NIST AI RMF", "SOC 2"],
        "target_pages": 24,
    },

    # =========================================================================
    # 10. Customer Operations (18 SOPs)
    # =========================================================================
    {
        "sop_id": "SOP-COPS-001", "title": "Customer Data Handling",
        "business_unit": "Customer Operations",
        "key_topics": ["data handling procedures", "access controls", "data classification", "secure communication"],
        "regulations": ["GDPR", "HIPAA", "SOC 2"],
        "target_pages": 24,
    },
    {
        "sop_id": "SOP-COPS-002", "title": "Customer Onboarding",
        "business_unit": "Customer Operations",
        "key_topics": ["onboarding workflow", "data collection", "consent capture", "configuration setup"],
        "regulations": ["GDPR", "HIPAA", "SOC 2"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-COPS-003", "title": "Support Ticket Management",
        "business_unit": "Customer Operations",
        "key_topics": ["ticket lifecycle", "classification", "SLA tracking", "escalation", "resolution"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-COPS-004", "title": "Customer Identity Verification",
        "business_unit": "Customer Operations",
        "key_topics": ["verification methods", "authentication steps", "social engineering prevention"],
        "regulations": ["HIPAA", "SOC 2", "GDPR"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-COPS-005", "title": "Customer Communication Standards",
        "business_unit": "Customer Operations",
        "key_topics": ["communication channels", "templates", "PHI handling in communications", "record keeping"],
        "regulations": ["HIPAA", "GDPR"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-COPS-006", "title": "Complaint Resolution",
        "business_unit": "Customer Operations",
        "key_topics": ["complaint intake", "investigation", "resolution", "root cause analysis", "reporting"],
        "regulations": ["GDPR", "SOC 2"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-COPS-007", "title": "Service Level Agreement Management",
        "business_unit": "Customer Operations",
        "key_topics": ["SLA terms", "monitoring", "breach handling", "customer reporting"],
        "regulations": ["SOC 2"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-COPS-008", "title": "Customer Data Portability",
        "business_unit": "Customer Operations",
        "key_topics": ["data export formats", "request handling", "data completeness", "timelines"],
        "regulations": ["GDPR"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-COPS-009", "title": "Customer Account Termination",
        "business_unit": "Customer Operations",
        "key_topics": ["termination process", "data retention", "data deletion", "final billing"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-COPS-010", "title": "Customer Consent Management",
        "business_unit": "Customer Operations",
        "key_topics": ["consent tracking", "preference center", "withdrawal handling", "marketing consent"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 20,
    },
    {
        "sop_id": "SOP-COPS-011", "title": "Customer Feedback and NPS Program",
        "business_unit": "Customer Operations",
        "key_topics": ["survey design", "data collection", "analysis", "action planning"],
        "regulations": ["GDPR"],
        "target_pages": 16,
    },
    {
        "sop_id": "SOP-COPS-012", "title": "Escalation Procedures",
        "business_unit": "Customer Operations",
        "key_topics": ["escalation tiers", "criteria", "response times", "management notification"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-COPS-013", "title": "Customer Data Breach Communication",
        "business_unit": "Customer Operations",
        "key_topics": ["notification templates", "communication timelines", "channel selection", "follow-up"],
        "regulations": ["GDPR", "HIPAA"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-COPS-014", "title": "Knowledge Base Management",
        "business_unit": "Customer Operations",
        "key_topics": ["content creation", "review cycle", "accuracy verification", "access controls"],
        "regulations": ["SOC 2"],
        "target_pages": 16,
    },
    {
        "sop_id": "SOP-COPS-015", "title": "Customer Access to AI Explanations",
        "business_unit": "Customer Operations",
        "key_topics": ["explanation requests", "explanation formats", "escalation to data science", "documentation"],
        "regulations": ["EU AI Act", "GDPR", "NIST AI RMF"],
        "target_pages": 22,
    },
    {
        "sop_id": "SOP-COPS-016", "title": "Multi-Channel Support Standards",
        "business_unit": "Customer Operations",
        "key_topics": ["channel-specific procedures", "consistency", "handoff protocols", "quality assurance"],
        "regulations": ["SOC 2", "HIPAA"],
        "target_pages": 18,
    },
    {
        "sop_id": "SOP-COPS-017", "title": "Customer Satisfaction Monitoring",
        "business_unit": "Customer Operations",
        "key_topics": ["CSAT metrics", "monitoring cadence", "trend analysis", "improvement actions"],
        "regulations": ["SOC 2"],
        "target_pages": 16,
    },
    {
        "sop_id": "SOP-COPS-018", "title": "Third-Party Support Provider Management",
        "business_unit": "Customer Operations",
        "key_topics": ["provider selection", "training requirements", "quality monitoring", "data handling"],
        "regulations": ["SOC 2", "HIPAA", "GDPR"],
        "target_pages": 22,
    },
]


def build_taxonomy() -> list[dict[str, Any]]:
    """Build the full taxonomy with compliance profiles and weaknesses."""
    from scripts.company_context import BUSINESS_UNITS

    enriched = []
    for sop in SOP_DEFINITIONS:
        bu_info = BUSINESS_UNITS[sop["business_unit"]]
        compliance_profile = {}
        weaknesses = {}
        for reg in sop["regulations"]:
            level = _compliance_level(sop["sop_id"], reg)
            compliance_profile[reg] = level
            w = _pick_weaknesses(sop["sop_id"], reg, level)
            if w:
                weaknesses[reg] = w

        enriched.append({
            **sop,
            "owner": bu_info["head"],
            "approver": bu_info["approver"],
            "dir": bu_info["dir"],
            "prefix": bu_info["prefix"],
            "compliance_profile": compliance_profile,
            "weaknesses": weaknesses,
        })
    return enriched


if __name__ == "__main__":
    import sys
    sys.path.insert(0, "/Users/tikhon/Projects/sentinel_agent")
    taxonomy = build_taxonomy()
    total_pages = sum(s["target_pages"] for s in taxonomy)
    print(f"Total SOPs: {len(taxonomy)}")
    print(f"Total target pages: {total_pages}")

    compliant = partial = gap = 0
    for s in taxonomy:
        for level in s["compliance_profile"].values():
            if level == "compliant":
                compliant += 1
            elif level == "partial":
                partial += 1
            else:
                gap += 1
    total_cells = compliant + partial + gap
    print(f"\nCompliance distribution across {total_cells} audit cells:")
    print(f"  Compliant: {compliant} ({100*compliant/total_cells:.1f}%)")
    print(f"  Partial:   {partial} ({100*partial/total_cells:.1f}%)")
    print(f"  Gap:       {gap} ({100*gap/total_cells:.1f}%)")

    print(f"\nBusiness unit breakdown:")
    from collections import Counter
    bu_counts = Counter(s["business_unit"] for s in taxonomy)
    for bu, count in sorted(bu_counts.items()):
        print(f"  {bu}: {count}")
