COMPANY_PROFILE = """
Meridian Health Technologies, Inc.

Founded: 2018 | Headquarters: Boston, MA | Employees: ~2,400
Global Offices: London, Berlin, Singapore, Toronto

OVERVIEW
Meridian Health Technologies is an AI-powered healthcare fintech company that combines
advanced machine learning with healthcare domain expertise and financial services
infrastructure. The company serves healthcare providers, payers, and patients across
North America and the European Union.

BUSINESS LINES
1. Clinical AI Platform — AI-driven clinical decision support tools, diagnostic
   imaging analysis, patient risk scoring, and adverse event prediction systems.
   Deployed in 340+ hospitals and clinics. Classified as high-risk AI under EU AI Act.

2. HealthPay Financial Services — Healthcare-specific payment processing, patient
   financing, medical lending, and claims automation. Processes ~$4.2B annually.
   Subject to SR 11-7 model risk management and SOC 2 requirements.

3. MedInsight Analytics — Population health analytics, care gap identification,
   and outcomes prediction platform for health systems and insurers. Handles
   PHI from ~12M patients.

4. Meridian SaaS Platform — Cloud-based infrastructure underlying all products.
   Multi-tenant, hosted on AWS (us-east-1, eu-west-1). SOC 2 Type II certified.

REGULATORY ENVIRONMENT
- EU AI Act: Clinical AI products classified as high-risk AI systems (Annex III).
  Transparency and human oversight obligations in effect since August 2025.
- HIPAA: Covered entity and business associate. Handles PHI across all products.
- SOC 2: Type II certification for the SaaS platform. Annual audit cycle.
- GDPR: Processes personal data of EU data subjects (patients, providers, employees).
  Has appointed a Data Protection Officer based in Berlin.
- SR 11-7: Federal Reserve guidance applies to credit scoring, fraud detection,
  and lending models in HealthPay Financial Services.
- NIST AI RMF: Voluntarily adopted as the AI risk management framework.
  Board-level AI Governance Committee established in 2024.

ORGANIZATIONAL STRUCTURE
- CEO: Dr. Sarah Chen
- Chief AI Officer: Dr. Marcus Rivera
- Chief Medical Officer: Dr. Priya Patel
- Chief Financial Officer: James Thornton
- Chief Information Security Officer: Rachel Kim
- Chief Privacy Officer / DPO: Dr. Klaus Weber (Berlin)
- VP of Engineering: David Park
- VP of Clinical AI Products: Dr. Aisha Okafor
- General Counsel: Maria Gonzalez
- VP of Financial Services: Robert Liu
- VP of IT Operations: Samantha Torres
- VP of Customer Operations: Michael Chang
- Chief Human Resources Officer: Jennifer Walsh
- Chief Compliance Officer: Thomas Anderson

TECHNOLOGY STACK
- Cloud: AWS (primary), Azure (DR)
- ML: PyTorch, TensorFlow, Kubeflow, MLflow, SageMaker
- Data: Snowflake, PostgreSQL, Redis, Apache Kafka, Pinecone
- Security: CrowdStrike, Okta, HashiCorp Vault, AWS KMS
- Observability: Datadog, PagerDuty, LangSmith (for AI tracing)

CERTIFICATIONS & ACCREDITATIONS
- SOC 2 Type II (since 2021, annual renewal)
- HITRUST CSF Certified (since 2022)
- ISO 27001:2022 Certified
- FDA 510(k) clearance for diagnostic imaging AI (2024)
- CE marking under EU MDR for clinical AI products (2025)
"""

BUSINESS_UNITS = {
    "AI/ML Engineering": {
        "prefix": "AIML",
        "dir": "01_ai_ml_engineering",
        "head": "Dr. Marcus Rivera, Chief AI Officer",
        "approver": "David Park, VP of Engineering",
        "description": "Responsible for the development, training, deployment, and monitoring of all machine learning models and AI systems across Meridian's product lines. Manages the ML platform, model registry, feature store, and experiment tracking infrastructure.",
    },
    "Clinical AI Products": {
        "prefix": "CLIN",
        "dir": "02_clinical_ai_products",
        "head": "Dr. Aisha Okafor, VP of Clinical AI Products",
        "approver": "Dr. Priya Patel, Chief Medical Officer",
        "description": "Develops and maintains clinical decision support systems, diagnostic AI tools, patient risk scoring algorithms, and adverse event prediction models. Ensures clinical validation, regulatory approval, and ongoing post-market surveillance of all AI medical devices.",
    },
    "Data Governance & Privacy": {
        "prefix": "DGP",
        "dir": "03_data_governance_privacy",
        "head": "Dr. Klaus Weber, Chief Privacy Officer / DPO",
        "approver": "Maria Gonzalez, General Counsel",
        "description": "Manages the enterprise data governance framework including data classification, privacy impact assessments, consent management, data subject rights, cross-border transfers, and data quality. Oversees GDPR, HIPAA, and AI Act data governance compliance.",
    },
    "Financial Services": {
        "prefix": "FIN",
        "dir": "04_financial_services",
        "head": "Robert Liu, VP of Financial Services",
        "approver": "James Thornton, Chief Financial Officer",
        "description": "Operates HealthPay Financial Services including payment processing, patient financing, medical lending, fraud detection, and claims automation. Manages credit scoring models, AML/KYC programs, and financial regulatory reporting.",
    },
    "Information Security": {
        "prefix": "ISEC",
        "dir": "05_information_security",
        "head": "Rachel Kim, Chief Information Security Officer",
        "approver": "Dr. Sarah Chen, CEO",
        "description": "Maintains the enterprise information security program including access control, network security, vulnerability management, incident response, security monitoring, cloud security, and third-party risk management.",
    },
    "IT Operations & Infrastructure": {
        "prefix": "ITOP",
        "dir": "06_it_operations",
        "head": "Samantha Torres, VP of IT Operations",
        "approver": "David Park, VP of Engineering",
        "description": "Manages IT infrastructure, cloud operations, change management, incident management, disaster recovery, business continuity, capacity planning, and service level management across all environments.",
    },
    "Human Resources": {
        "prefix": "HR",
        "dir": "07_human_resources",
        "head": "Jennifer Walsh, Chief Human Resources Officer",
        "approver": "Dr. Sarah Chen, CEO",
        "description": "Oversees employee lifecycle management, compliance training, background checks, acceptable use policies, employee data privacy, AI ethics governance, and workforce-related regulatory compliance.",
    },
    "Legal & Compliance": {
        "prefix": "LEGC",
        "dir": "08_legal_compliance",
        "head": "Thomas Anderson, Chief Compliance Officer",
        "approver": "Maria Gonzalez, General Counsel",
        "description": "Manages the enterprise compliance program including regulatory change management, internal audit, compliance monitoring, policy lifecycle, vendor compliance, and cross-jurisdictional regulatory coordination across all six regulatory frameworks.",
    },
    "Product & Engineering": {
        "prefix": "PENG",
        "dir": "09_product_engineering",
        "head": "David Park, VP of Engineering",
        "approver": "Dr. Sarah Chen, CEO",
        "description": "Manages the software development lifecycle, code quality, API standards, CI/CD security, open source governance, platform reliability, and product security across all Meridian products and the underlying SaaS platform.",
    },
    "Customer Operations": {
        "prefix": "COPS",
        "dir": "10_customer_operations",
        "head": "Michael Chang, VP of Customer Operations",
        "approver": "Robert Liu, VP of Financial Services",
        "description": "Manages customer onboarding, support operations, complaint resolution, SLA management, customer data handling, consent management, data portability, and customer-facing AI transparency requirements.",
    },
}
