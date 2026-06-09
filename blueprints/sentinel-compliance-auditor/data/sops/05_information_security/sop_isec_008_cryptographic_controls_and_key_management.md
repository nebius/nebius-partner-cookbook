---
sop_id: "SOP-ISEC-008"
title: "Cryptographic Controls and Key Management"
business_unit: "Information Security"
version: "4.8"
effective_date: "2024-02-22"
last_reviewed: "2025-12-23"
next_review: "2026-06-09"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# SOP-ISEC-008: Cryptographic Controls and Key Management

## 1. Purpose and Scope

This Standard Operating Procedure (SOP) establishes the enterprise-wide requirements for the use of cryptographic controls, the management of cryptographic keys, and the lifecycle of digital certificates at Meridian Health Technologies. The purpose of this document is to protect the confidentiality, integrity, and authenticity of Covered Information through the consistent application of approved cryptographic standards and rigorous, auditable key management practices.

This SOP applies to all business units, subsidiaries, employees, contractors, consultants, and third-party service providers that manage, process, store, or transmit Meridian data, or that operate or manage information systems on behalf of Meridian. This includes, but is not limited to, the HealthInsight Clinical Platform, the MedInsight Analytics Engine, the Revenue Cycle Management (RCM) System, and all supporting infrastructure hosted via Meridian’s hybrid-cloud infrastructure across AWS, Azure, and on-premises data centers (PHY-A and PHY-B).

**In Scope:**
*   All symmetric and asymmetric encryption used for data at rest, data in transit, and data in use (where applicable).
*   All cryptographic keys generated, stored, or used within Meridian-managed systems, including cloud-native key management services (KMS) and on-premises Hardware Security Modules (HSMs).
*   All Transport Layer Security (TLS)/Secure Sockets Layer (SSL) certificates used for internal and external-facing services.
*   All digital signing operations for code, documents, and transactions.
*   All end-user devices (laptops, mobile phones, removable media) storing Covered Information.
*   All cryptographic modules and algorithms used in regulated medical devices (per MDR CE marking).

**Out of Scope:**
*   Physical locks and combination safes not considered IT assets (refer to physical security policy SOP-PSEC-002).
*   Proprietary encryption within third-party systems where Meridian does not manage the keys, provided these systems have been formally reviewed under the Vendor Risk Management Program (SOP-VRM-005).

## 2. Definitions and Acronyms

A comprehensive list of terms used throughout this policy is provided below. Personnel are expected to be familiar with these definitions.

| Term | Definition |
| :--- | :--- |
| **AES** | Advanced Encryption Standard. The symmetric encryption algorithm used for protecting data at rest and bulk data in transit. |
| **Asymmetric Cryptography** | Also called public-key cryptography. A system using a mathematically related key pair (public key and private key) for encryption, decryption, digital signatures, and key exchange. |
| **Certificate Authority (CA)** | A trusted internal or external entity that issues and revokes digital certificates. |
| **Certificate Revocation List (CRL)** | A list of digital certificates that have been revoked by the issuing CA before their scheduled expiration date. |
| **Covered Information** | Any data element classified as Electronic Protected Health Information (ePHI) under HIPAA, combined with any other Meridian proprietary data classified as "Confidential" or "Restricted" as per the Data Governance Policy. |
| **Cryptographic Module** | The set of hardware, software, and/or firmware that implements approved security functions (including cryptographic algorithms and key generation) contained within the cryptographic boundary. |
| **Cryptoperiod** | The maximum time span during which a specific cryptographic key is authorized for use. |
| **Data Encryption Key (DEK)** | A symmetric key used to encrypt/decrypt payload data (e.g., a file, a database cell, a message body). |
| **FIPS 140-2** | Federal Information Processing Standard Publication 140-2, a U.S. government security standard used to accredit cryptographic modules. |
| **Hardware Security Module (HSM)** | A dedicated, tamper-resistant hardware appliance certified to FIPS 140-2 Level 3 or higher, used for secure cryptographic processing and key lifecycle management. |
| **Key Encryption Key (KEK)** | An asymmetric or symmetric key used exclusively to encrypt/decrypt other cryptographic keys (e.g., wrapping a DEK before storage). |
| **Key Management Lifecycle** | The entire sequence of phases from key generation through destruction, including distribution, storage, backup, recovery, re-key, rotation, revocation, and destruction. |
| **Master Key (MK)** | The highest-level cryptographic key within a hierarchy, stored solely within a hardware security module (HSM). |
| **Online Certificate Status Protocol (OCSP)** | An internet protocol used for obtaining the revocation status of an X.509 digital certificate. |
| **RSA 4096** | Rivest-Shamir-Adleman algorithm using a 4096-bit key, used for asymmetric operations such as digital signatures and key exchange. |
| **Symmetric Cryptography** | An encryption methodology using a single, shared secret key for both encryption and decryption operations. |
| **TLS 1.2/1.3** | Transport Layer Security, the cryptographic protocol designed to provide communications security over a computer network. Meridian mandates TLS 1.2 or higher. |
| **X.509** | The ITU-T standard defining the format of public key certificates, used extensively in Meridian infrastructure. |

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and specific responsibilities for the execution of this SOP.

| Role | Actor(s) | Responsibility | RACI |
| :--- | :--- | :--- | :--- |
| **Executive Approver** | Dr. Sarah Chen, CEO | Ultimate accountability for policy effectiveness and compliance. | A |
| **Policy Owner** | Rachel Kim, CISO | Owns policy content, defines standards, approves global exceptions, ensures alignment with HIPAA. | A, R |
| **Key Management Officer (KMO)** | Senior Security Architect, Information Security | Manages enterprise Key Management Platform (Entrust KeyControl), HSM operations, key generation ceremonies, Master Key lifecycle. | R |
| **Certificate Authority Administrator (CAA)** | Lead Infrastructure Engineer, IT Operations | Manages internal Microsoft CA, DigiCert external CA portal, certificate issuance, renewal automation, CRL/OCSP oversight. | R |
| **Application Security Champion (ASC)** | Lead Developer per Scrum Team | Ensures application-level encryption correctly uses DEKs provisioned by the KMS, ensures no hard-coded keys in source code. | R, C |
| **Database Administrator (DBA)** | Senior DBA, Data Services | Implements Transparent Data Encryption (TDE) and column-level encryption per the Database Encryption Standards in Section 5.5. Manages DB-level key rotation. | R, C |
| **System Administrator** | Windows/ Linux/ Network Admins | Deploys TLS certificates per procedure, configures full-disk encryption on end-user laptops, manages SSH keys. | R |
| **Compliance Officer** | VP of Regulatory Affairs | Monitors procedure for HIPAA § 164.304, § 164.312(a)(1), and § 164.312(e)(1) compliance. Conducts quarterly reviews of key management artifacts. | I |
| **Data Owner** | VP of Clinical Data, VP of Finance, etc. | Determines which data is ePHI and/or Covered Information and requires encryption; responsible for approving access to plaintext data. | C |

## 4. Policy Statements

Meridian Health Technologies commits to the following high-level cryptographic control policies to ensure the confidentiality, integrity, and availability of Covered Information, particularly as required under HIPAA Security Rule at 45 CFR Part 164, Subpart C.

**4.1. Prohibition of Non-Standard Cryptography**
The design, development, or deployment of proprietary, custom-built, or non-standard encryption algorithms or protocols is strictly forbidden. Only ciphers and key lengths approved under this SOP (Section 6.1) shall be used. Attempts by any personnel to bypass approved cryptographic controls, including but not limited to, using self-signed certificates on production systems, hard-coding encryption keys into application code, or utilizing unapproved cipher suites, will be considered a Level 1 Security Incident and will be escalated to the Vice President of Information Security and Chief Human Resources Officer for immediate disciplinary action, up to and including termination of employment.

**4.2. Mandatory Encryption of Protected Health Information (PHI)**
Per HIPAA §164.312(a)(1) (Access Control) and §164.312(e)(1) (Transmission Security), any system storing, processing, or transmitting Electronic Protected Health Information (ePHI) **MUST** implement cryptographic protection considered "Addressable" by encrypting such data to the standard specified within this SOP. This is not optional. All ePHI data at rest on servers, storage arrays, databases, end-user computing devices, and portable media must be encrypted using AES-256. All ePHI data in transit across public, untrusted, or internal networks must be encrypted using TLS 1.2 or higher with AES-256-GCM cipher suites.

**4.3. Separation of Duties for Key Management Ceremonies**
No single individual shall possess the ability to reconstruct or utilize a Master Key (MK) or Key Encryption Key (KEK) that protects ePHI at an infrastructure level. A physical, dual-controlled, split-knowledge key ceremony is required for the generation, backup, and restoration of all Master Keys within the on-premises HSM cluster. The mandatory participants are: (1) the Key Management Officer (KMO), and (2) the Chief Information Security Officer (CISO), or their delegated Deputy CISO. A trusted quorum of at least two of three appointed Key Custodians must be present to provide operational control.

**4.4. Cryptographic Module Validation**
All commercially-available cryptographic modules deployed at Meridian shall be, at minimum, under active Cryptographic Module Validation Program (CMVP) testing for Federal Information Processing Standards (FIPS) 140-2 Level 2 compliance. Modules used for Master Key protection (e.g., HSMs) must be FIPS 140-2 Level 3 validated with a valid certificate number, which shall be recorded and maintained in the Technology Asset Inventory (CMDB). Cloud-native modules (e.g., AWS KMS, Azure Dedicated HSM) must have their FIPS validation status reviewed and formally accepted by the CISO prior to use for protecting Covered Information.

**4.5. Right to Audit**
Cryptographic operations are subject to continuous and ad-hoc auditing by the Internal Audit team, acting on behalf of the Privacy Officer and CISO. Every access to, use of, or operation upon a plaintext cryptographic key by any human or automated system must generate a tamper-evident log entry. Failure to produce logs upon request from an authorized auditor within four (4) hours shall constitute a reportable security incident under SOP-ISEC-001.

## 5. Detailed Procedures

This section outlines the step-by-step, mandatory procedures for executing the cryptographic key lifecycle at Meridian.

### 5.1. Key Generation Procedure

All cryptographic keys protecting Covered Information must demonstrate proof of provenance from a FIPS 140-2 Level 3 validated source (hardware-based True Random Number Generator or Deterministic Random Bit Generator seeded from multiple high-entropy sources).

**Process:**
1.  **Key Request Submission:** The Requestor (e.g., ASC, DBA) must submit a formal key request via the ServiceNow "Key & Certificate Management" catalog item (SN-KCM-001). The request must specify:
    *   Application Name and CMDB Asset Tag.
    *   Requested cryptoperiod justification, if deviating from standard (see Section 6.3).
    *   Data Owner name for implicit authorization.
2.  **Authorization:** The ServiceNow workflow routes to the relevant Data Owner for approval. Upon approval, the status changes to "Ready for Generation."
3.  **Generation Execution:**
    *   **For HSM-protected keys (KEKs, MKs):** The KMO initiates a secure key generation ceremony. The KMO authenticates to the Entrust nShield HSM cluster using their physical, multi-factor (PIV smart card + biometric) credentials and a quorum of two Key Custodians present a physical iButton key. The KMO executes the `pki-keygen` tool, specifying the algorithm, key length (`-aes256` or `-rsa4096`), and a unique key ID (`-kid`) matching the ServiceNow ticket number. The HSM returns a key handle (a signed opaque object) and a public verification token, which are securely stored in the enterprise Password State Manager (PSM), CyberArk Vault, in a locked safe titled "Key Handles."
    *   **For Application/Cloud Keys (DEKs):** The service account (IAM role, Kerberos ID) authorized in the ServiceNow ticket executes an API call directly to the designated Key Management Service (AWS KMS or Azure Key Vault). The command (e.g., `aws kms generate-data-key` or `az keyvault key create`) is scripted as part of the CI/CD pipeline (GitLab) and never executed manually by a human.
4.  **Logging:** The execution creates an immutable, signed log entry in the central SIEM (Splunk), recording: timestamp, key ID, generation algorithm, authorizing ticket number, executing role, and the success/failure status.

### 5.2. Key Storage and Distribution Procedures

The secure distribution of a key from its point of generation to the authorized cryptographic module is the most critical operational step.

**Procedures:**
1.  **Key Wrapping (HSM to App):** Immediately after generation, a DEK is wrapped (encrypted) by a KEK. The wrapping occurs entirely within the cryptographic boundary of the HSM or cloud KMS. The resulting ciphertext blob is the only form of the key that may exit the boundary. A plaintext key must never traverse a network.
2.  **Secure Distribution via Vault Proxy:** The ciphertext blob is pushed via TLS 1.2 mutual-auth to a secure proxy in the target environment's CyberArk Conjur vault.
3.  **Application Injection:** The authorized application container or VM agent authenticates to CyberArk Conjur using its Host-Based Authentication (HBA) token (a unique token fingerprinted to the machine). Upon authentication, it requests the ciphertext blob for Key-ID-X. CyberArk logs the request. The application, running with a service principal, then makes an API call to the local HSM/KMS endpoint to *unwrap* the DEK into its volatile memory for immediate use. The DEK is never stored in plaintext at rest on the application server's file system, swap, or crash dumps.

### 5.3. Key Rotation and Re-Key Procedure

Key rotation must be automated to the fullest extent possible using the integrated KMS and application libraries.

**Procedure for DEK Rotation:**
1.  **Trigger:** A chron job, managed by the enterprise scheduler (Control-M), checks the creation date of key handles against their cryptoperiod (Section 6.3). An auto-generated ticket is created in ServiceNow 72 hours before key expiry.
2.  **Automated Rotation (Policy-Conformant Apps):** For applications that integrate the Meridian Crypto-Agent, the rotation is zero-touch. The agent, recognizing the `KeyRotation` tag on the old key handle, calls the KMS to generate a *new* version of the DEK under the same key alias. New data writes are encrypted with the new key version. The app maintains the old key version in its metadata for decryption of existing data until the next backup lifecycle completes.
3.  **Manual Rotation (Legacy/One-off):** The ASC assigned to the ticket must:
    *   Schedule a maintenance window > 24 hours in advance.
    *   Run the approved `meridian-crypto-rotate` playbook from the Ansible Tower console against the target host group.
    *   Execute the `decrypt-reencrypt` task, which processes all data in the specified S3 bucket/ database column, replacing the ciphertext headers.
    *   Upon success, deactivate the legacy key handle in the KMS.
4.  **Verification:** The rotation playbook concludes with a verification task that writes a known test string, reads it back, and validates the decrypted plaintext is identical, ensuring no data corruption.

#### 5.2.2 HSM Master Key Rotation
This occurs annually during the pre-approved IT service continuity maintenance window in January. The ceremony requires the CISO + KMO + two Key Custodians. The old Master Key is not destroyed but deactivated, stored in a series of PIV-secured smart cards inside a dual-control safe located off-site in a secure archival facility managed by Iron Mountain (Account # 88752-MTN). This ensures access to backups encrypted under old MKs.

### 5.4. Key Revocation and Destruction Procedure

**5.4.1. Emergency Key Revocation**
Triggered by a confirmed security incident (e.g., key compromise indicated by anomalous KMS access pattern alert). The CISO or Deputy CISO declares the incident via the PagerDuty incident war room "CRYPTO-COMPROMISE" playbook.
1.  **Consensus:** The CISO and General Counsel must jointly approve the emergency revocation in the war room comm channel.
2.  **Execution:** The KMO enforces the block on the affected Key ID. Actions include: (a) deleting the key handle from the primary and DR HSMs using the `--revoke` command with both administrators' credentials, and (b) pushing a blacklist to all CyberArk Conjur proxies.
3.  **Notification:** All IT Service Desk and NOC staff are notified via the #sec-ops-emergency Slack channel. A "Code Red" notification is issued to all Application Owners, who are required to immediately rotate their impacted DEKs.

**5.4.2. Standard Key Decommissioning**
At end-of-cryptoperiod plus a mandatory 90-day key archival hold (where the key exists only in a deactivated, non-operational state for legal/ forensics purposes), a decommission ticket is opened. The KMO verifies that no objects in the data repository (verified by a hash-sum check on the repository metadata) still reference the deactivated key. The KMO then issues the `--destroy` command to the HSM. A certificate of destruction is generated by the HSM, logged in Splunk, and attached to the ServiceNow ticket for permanent record.

### 5.5. Data-at-Rest Encryption Procedures

**ePHI Database Encryption (Transparent Data Encryption - TDE):**
*   All Microsoft SQL Server instances hosting ePHI must use TDE with AES-256. The Database Encryption Key (DEK) for each database is stored symmetrically encrypted in the database boot record by the SQL Server Service Master Key. The Service Master Key is, in turn, protected by the Operating System's Data Protection API (DPAPI), which stores the secret in the server's registry. No manual key management is required for TDE, but a backup of the Service Master Key (`BACKUP SERVICE MASTER KEY TO FILE = 'SvcMasterKey_Prod_SQL01.key' ENCRYPTION BY PASSWORD = 'StrongPassword!23'`) must be performed by the DBA after each SQL Server Service Pack update and stored in CyberArk.
*   For granular encryption, column-level encryption using `ENCRYPTBYKEY` and `DECRYPTBYKEY` with an asymmetric key stored in the EKM provider (AWS KMS) is required for specific ePHI fields (e.g., Medical Record Number, SSN) defined in the Data Classification Index. This asymmetric key is backed up as specified in Section 5.2.

### 5.6. Certificate Management Procedure

The entire lifecycle for TLS/SSL certificates must be managed via the AppViewX Enterprise Certificate Management console.

**5.6.1. Certificate Enrollment (Internal & Public)**
1.  **Request:** The System Administrator submits a Certificate Signing Request (CSR) via AppViewX. The CSR template is pre-populated: Key Algorithm: RSA 4096, Signature Algorithm: SHA256, Validity: 1 year maximum.
2.  **Approval:** For public-facing services (e.g., `*.meridianhealth.com`), the CSR requires approval from the Director of IT Operations. For internal-facing services (e.g., `*.medinsight.internal`), the CSR is auto-approved based on group membership in Active Directory (`AppViewX_Internal_Users`).
3.  **Issuance:** AppViewX forwards the CSR to the correct CA: DigiCert for public TLS, and the internal MS Windows CA for internal TLS. The issued certificate and its private key are securely pushed to the target server's local certificate store (Windows Cert:\> or Linux /etc/pki/tls) by the AppViewX agent.

**5.6.2. Certificate Renewal and Revocation**
*   **Renewal:** AppViewX continuously monitors all managed certificates. When a certificate reaches 80% of its lifetime, an automated re-enrollment is triggered. The new certificate is deployed, and the web service (IIS/Apache) is gracefully reloaded. The old certificate is then revoked.
*   **Revocation:** Upon decommissioning a server, a System Administrator must manually revoke its associated certificate in AppViewX. The AppViewX service account must be configured to immediately publish a new Certificate Revocation List (CRL) to the CDP path at `http://pki.meridianhealth.com/crls/MeridianInternalCA.crl` with a publication interval of 4 hours.

## 6. Controls and Safeguards

Meridian implements a multi-layered defense-in-depth model for cryptographic controls, incorporating technical, administrative, and physical safeguards consistent with HIPAA §164.312.

### 6.1. Technical Controls and Encryption Standards

The following technology standards are mandated. Any deviation requires a formal exception (Section 8).

| Control Category | Approved Standard(s) | Usage Context |
| :--- | :--- | :--- |
| **Symmetric Encryption** | AES-256 (GCM mode for authenticated encryption) | All data at rest, including database TDE, file servers, S3 bucket server-side encryption (SSE-KMS), endpoint disk encryption. |
| **Symmetric Encryption - Bulk Transit** | AES-256-GCM for SSH2 session keys. | Securing bulk file transfers via SFTP, administrative tunnels. |
| **Asymmetric Encryption/ Key Exchange** | RSA 4096, Elliptic Curve Diffie-Hellman (ECDHE) with P-384 curve. | TLS handshakes, digital signatures for code and documents. |
| **Hashing** | SHA-384, SHA-512. SHA-1 is prohibited. | Digital signing, HMAC for API integrity, password storage (via bcrypt, which is the mandated KDF). |
| **Communication Protocols** | TLS 1.2, TLS 1.3. SSLv3, TLS 1.0, and TLS 1.1 are globally disabled via Group Policy and AWS Security Group rules. | All web-based and API communications. |
| **Wi-Fi Security** | WPA3-Enterprise using EAP-TLS and AES-256-GCM. | Corporate and Guest wireless networks. WPA2-Personal is prohibited. |
| **Full Disk Encryption (FDE)** | BitLocker (Windows) with AES-256-XTS stored in TPM 2.0 + PIN. FileVault2 (macOS) with institutional recovery key escrowed in JAMF Pro. | All corporate-issued laptops and workstations. |
| **Portable Media Encryption** | VeraCrypt or hardware encryption sticks (Apricorn Aegis Padlock 3.0). | Any USB drive used for transporting Covered Information. |

### 6.2. Hardware Security Module (HSM) Controls

The on-premises infrastructure relies on an nCipher (Entrust) nShield Connect+ cluster, deployed in an N+1 configuration across PHY-A and PHY-B data centers.

*   **Physical Security:** HSMs reside in a dedicated, double-locked, non-contiguous rack inside the SOC-monitored, biometric-controlled cage within each data center. Any tampering event causes an automatic erasure of all private keys and a forensic audit event sent to the 24/7 CSOC.
*   **Access Control:** Administrative access to the HSM Secure Console is not granted to any named user. Access is mediated exclusively by a dedicated jump host (`HSMPROXY01`), which enforces Role-Based Access Control (RBAC) via Active Directory. The group `HSM_KM_Officers` (containing the KMO and Deputy) can authenticate but requires an "n of m" quorum (2 of 3 cards) to perform any operational command on Master Keys. All commands are logged.
*   **Backup and Replication:** The HSM configuration and protected key material are mirrored between the primary and DR cluster. The key material is replicated in encrypted form via the `enquiry` backplane protocol. A local backup is taken to a physical HSM Backup Device stored in a fireproof safe in the CISO’s office, and a DR backup is similarly stored in Facility B. Logs compare the quantity and name of stored key handles on primary and DR to ensure consistency; any drift generates an immediate P1 ticket.

### 6.3. Key Cryptoperiods

The maximum lifetime for each key type is defined. Keys must be destroyed at the end of their cryptoperiod as per Section 5.4.2. The KMO publishes an annual "Key Reaper Report" to identify non-compliant keys.

| Key Type | Maximum Cryptoperiod |
| :--- | :--- |
| Master Key (HSM) | 5 Years |
| Key Encryption Key (KEK) | 2 Years |
| Data Encryption Key (DEK) - Data at Rest (S3, DB TDE) | 1 Year |
| Data Encryption Key (DEK) - Data in Transit / Session Keys | 1 Hour or Session |
| SSH User Private Key (User access) | 270 Days |
| TLS/SSL Certificate Private Key | 1 Year |
| Digital Signature Private Key (Code/ Document Signing) | 3 Years |

### 6.4. Administrative Safeguards (HIPAA §164.312(b) Audit Controls)

The system, which stores cryptographic keys and related audit logs, must meet the HIPAA requirements for audit controls. The Key Management Subsystem (KMS, HSM, and CyberArk Vault) is designated a "Critical HIPAA Application" and therefore must implement hardware, software, and/or procedural audit controls that record and examine activity in information systems that use or access ePHI.

### 6.5. SSH Key Management Safeguards

The use of unmanaged SSH keys is an information security finding that must be remediated. All user-generated SSH key pairs for accessing production systems are forbidden. Access to Linux/Unix production systems from privileged access workstations (PAWs) is brokered exclusively through the HashiCorp Vault SSH Secrets Engine. A short-lived, 4-hour maximum, SSH certificate is issued and signed by the internal Vault CA after successful authentication via Okta MFA. All SSH sessions are recorded and audit-logged by Teleport.

## 7. Monitoring, Metrics, and Reporting

Continuous monitoring of cryptographic controls is performed through automated technical solutions and human review processes to ensure control effectiveness and adherence to this SOP.

### 7.1. Key Performance Indicators and Dashboards

The SOC team manages a real-time "Crypto Controls & Compliance" dashboard in Splunk to track the following KPIs. A weekly automated report is emailed to the CISO and the Information Security management team.

| Metric / KPI | Target | Source System(s) |
| :--- | :--- | :--- |
| **% of ePHI Stores w/ Valid Encryption** | 100% | AWS Config, Azure Policy, DB Audit Scripts |
| **Key Rotation Compliance** | ≥ 99.5% rotated within 48 hrs of expiry | ServiceNow, AppViewX, Splunk correlation |
| **Unauthorized Cryptographic API Calls** | 0 per 24-hour interval | CloudTrail, Windows Security Log, AppLocker |
| **Certificate Expiration Status** | 0 expired certificates in production | AppViewX Enterprise |
| **HCM Quorum Integrity (HSM)** | 0 unauthorized access attempts | HSM Audit Log via syslog to Splunk |
| **TLS Protocol Drift** | 0.0% traffic uses TLS < 1.2 | AWS ALB Logs, Azure App Gateway Logs, NIDS |
| **ePHI Decryption Events on Endpoints** | 0 in non-approved, non-protected enclaves | DLP Endpoint Module logs |

### 7.2. Formal Reporting Cadence

1.  **Daily NOC Hand-off Report:** A summary of all certificate expiration warnings and automated key lifecycle events for the preceding 24 hours.
2.  **Weekly "Keys to the Kingdom" Report:** Generated by the Splunk dashboard, it highlights all KPI deviations, pending manual rotations, and all administrative access to the HSM console. Reviewed by the KMO.
3.  **Quarterly HIPAA Encryption Review:** The Compliance Officer and CISO conduct a formal, documented review of:
    *   All cryptographic key inventories and their lifecycle events.
    *   All open exceptions related to cryptographic controls (Section 8).
    *   Any changes in technology, environment, or operations that impact the protection of ePHI, per HIPAA §164.306(b).
    *   A sample audit of 10% of decommissioned keys to cross-validate the Certificate of Destruction.
4.  **Annual Enterprise Risk Report:** A summary of cryptographic control failures, trends, and risk decisions made is included in the annual enterprise risk report presented to the Board's Audit and Compliance Committee by the CISO.

### 7.3. Audit Log Review

The SIEM Correlation Engine (Splunk ES) has been configured with specific correlation rules to detect critical cryptographic events including: multiple failed HSM authentication events, mass certificate revocation, manual execution of any KMS administrative command, and decryption of a DEK outside an approved application's memory space. These rules generate a "P2" actionable alert in the SOC queue, with an SLA of 60 minutes for initial triage and acknowledgment.

## 8. Exception Handling and Escalation

Any deviation from the specific technical controls, standards, or procedures defined in this SOP requires a formal, time-bound exception granted solely by the Policy Owner.

**8.1. Exception Request Process**
1.  **Submission:** A Requestor submits a "Policy Exception Request" in ServiceNow, Module SN-EXC-GEN. The request must contain:
    *   The specific policy statement or procedure for which the exception is sought.
    *   The Business Justification, outlining the critical need.
    *   Detailed technical description of the non-compliant system, including its CMDB asset tag.
    *   A Detailed Risk Assessment: The Requestor must identify how ePHI (or other sensitive data) will be protected in lieu of the standard, what residual risks exist, and what compensating controls are proposed.
    *   A Sunset Date: A specific calendar date (not to exceed 12 months) when the system will be remediated and brought into full compliance or decommissioned.
2.  **Review and Approval:**
    *   The request is automatically routed to the Information Security Architecture team for technical review and scoring (risk score 1-10).
    *   If the risk score is 1-4 (Low), the CISO can approve directly. If 5-7 (Medium), the CISO and the relevant Data Owner must approve. If 8-10 (High/ Critical), or the exception involves a Master Key component, the CISO must present the exception to the Executive Risk Committee (ERC) for formal acceptance by Dr. Sarah Chen, CEO, or the General Counsel.
3.  **Registration and Tracking:** All granted exceptions are registered in the "Crypto Exception Tracker" Splunk dashboard with a public-facing sunset date. A P3 ticket is automatically created for 30 days before sunset, mandating a status update.

**8.2. Emergency Procedures**
If a cryptographic compromise or failure prevents the secure protection of data, the CISO is authorized to take immediate emergency action, including isolation of the affected system, revocation of all linked keys, and activation of the Disaster Recovery Plan (SOP-BCP-004). A post-incident review, inclusive of full regulatory disclosure if ePHI was placed at risk, will be conducted within 72 hours of the emergency's conclusion.

## 9. Training Requirements

All personnel assigned roles identified in Section 3 must complete specialized training commensurate with their responsibilities.

**9.1. Role-Based Training Courses**

| Required Role | Training Module | Frequency | Hosted By |
| :--- | :--- | :--- | :--- |
| All Employees (general) | MHT-SEC-AWARE: Annual Security Awareness, Module 5: "Security Hygiene & Encryption." | Annually | Workday LMS |
| System Administrators, DBAs, ASCs | MHT-CRYPTO-100: "Applied Cryptography and Key Management at Meridian." (4-hour instructor-led course). Includes hands-on lab: "Executing a Certificate Renewal" and "Investigating a Crypto Incident." | On Hire, then Biennially | InfoSec Team |
| Key Custodians, KMO, CISO | MHT-CRYPTO-200: "HSM Operations and Master Key Ceremony." (Full-day, on-site practical). Includes practical assessment on split-knowledge authentication and key backup procedures. | Annually | Vendor (Entrust) & InfoSec |

**9.2. Training Effectiveness Measurement**
The effectiveness of role-based training is measured via:
1.  **Post-Training Exam:** A 25-question, scenario-based exam. A passing score of 85% is required for `MHT-CRYPTO-100`. Failure results in a 1-week remediation window and a retest.
2.  **Annual Tabletop Exercise:** The CISO will conduct an annual tabletop exercise simulating a Master Key compromise. This is mandatory for the Key Custodian team. A lessons-learned document is produced and a corrective action plan is tracked through resolution. This directly satisfies the HIPAA §164.308(a)(8) requirement to evaluate the effectiveness of security measures.

## 10. Related Policies and References

This SOP is part of the Meridian Information Security and HIPAA Compliance Frameworks. It should be read in conjunction with the following internal documents and external standards:

| Reference ID | Document Title / Standard |
| :--- | :--- |
| **SOP-ISEC-001** | Incident Response and Management Policy |
| **SOP-ISEC-003** | Access Control Policy and Procedures |
| **SOP-ISEC-009** | Data Classification and Handling Standard |
| **SOP-ISEC-014** | Secure Software Development Lifecycle (S-SDLC) Policy |
| **SOP-BCP-004** | IT Disaster Recovery and Business Continuity Plan |
| **POL-HR-007** | Employee Acceptable Use and Disciplinary Action Policy |
| **External Standard** | NIST Special Publication 800-57, Part 1, Rev. 5: "Recommendation for Key Management." |
| **External Standard** | ISO/IEC 27001:2013, Control A.10.1: "Cryptographic Controls." |
| **Regulation** | HIPAA Privacy and Security Rules, 45 CFR Part 160 and Subparts A, C, and E of Part 164. |
| **Regulation** | EU Medical Device Regulation (MDR) 2017/745, Annex I, General Safety and Performance Requirements (GSPR) 17.4. |

## 11. Revision History

This document has evolved through multiple review cycles to reflect changes in technology, threats, and regulatory requirements.

| Version | Date | Author/Editor | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2019-05-15 | J. Williams, CISO | Initial enterprise policy drafted. Established basic standards and HSM onboarding. |
| 2.0 | 2020-11-18 | R. Kim, CISO | Major rewrite following migration to hybrid-cloud model. Added AWS KMS/Azure Key Vault procedures, SSH key management, and full Key Management Lifecycle. |
| 3.5 | 2022-04-06 | A. Bell, Sr. Sec Architect | Post-regulatory audit revision. Strengthened HIPAA-specific controls, added emergency key revocation procedure, defined cryptoperiod table, and migrated to ServiceNow/Ansible workflows. |
| 4.0 | 2023-02-10 | R. Kim, CISO | Updated to include MDR and CE marking requirements for medical device cryptography. Replaced deprecated SHA-256 for code signing with SHA-384. Added AppViewX certificate lifecycle automation. |
| 4.8 | 2024-02-22 | R. Kim, CISO | Current version. Refreshed roles and responsibilities to match new org chart. Updated cryptoperiod for SSH User Private Keys. Added Section 7.1 KPIs. Formalized the integration between CyberArk Conjur and the CI/CD pipeline for zero-touch secrets injection. |