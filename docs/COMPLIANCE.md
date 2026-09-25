# Compliance and Governance Notes

## Purpose

This document captures the compliance posture and governance expectations for the CyberTiX AI demonstration project. The implementation is designed to align with common principles used in regulated and security-conscious environments.

## Core compliance principles

### 1. Evidence integrity

Each evidence bundle is linked to a deterministic SHA-256 hash. This allows the project to demonstrate traceability and reduces the risk of unverifiable AI-generated claims.

### 2. Auditability

The workflow records the event source, timestamp, case ID, risk score, and evidence chain. This supports internal review and external audit readiness.

### 3. Human oversight

Sensitive actions are not executed without a policy gate check. The system requires clear thresholds and explicit action routing before autonomous containment is triggered.

### 4. Risk-based control

High-severity indicators are mapped to risk scores and MITRE ATT&CK references, making governance and response prioritization explicit.

### 5. Data minimization

The project uses representative synthetic telemetry and does not require production-sensitive data to operate.

## AI governance controls

- Model outputs are bounded to evidence-backed metadata.
- The threat narrative references the case hash and risk context.
- Policy gates enforce deterministic actions instead of latent model behavior.
- Human review remains a required path for lower-confidence or uncertain cases.

## Security posture summary

The project demonstrates a safe-by-design pattern for AI in security operations:

- detect, classify, and score telemetry,
- ensure evidence integrity,
- restrict automated remediation to approved decision paths,
- keep a traceable log of actions and evidence lineage.

## Data handling note

This repository is a demo project and should not be used with production logs or regulated data without appropriate legal review, data classification, and retention controls.

## Contact

Devesh Kumar  
devesh2178@gmail.com
