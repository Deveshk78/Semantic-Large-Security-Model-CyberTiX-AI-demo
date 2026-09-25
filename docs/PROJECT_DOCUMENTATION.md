# Project Documentation

## 1. Overview

CyberTiX AI is a security operations simulation designed to show how evidence-bound AI reasoning can support a modern SOC workflow. The project demonstrates the flow from raw endpoint or cloud telemetry to a structured incident narrative and a deterministic policy response.

## 2. Objective

The project addresses the core challenge of unsafe AI behavior in cyber defense: model-driven reasoning without direct evidence can invent false threat narratives or trigger unauthorized automation. The system reduces this risk by requiring cryptographic evidence chaining and strict decision gates.

## 3. Scope

The current implementation covers:

- log normalization,
- case and evidence packaging,
- MITRE ATT&CK mapping,
- hash-based evidence provenance,
- AI narration constrained to a bundle,
- deterministic policy execution.

The project is intentionally lightweight and simulation-oriented so it can be run locally and extended to real SOC data pipelines.

## 4. Architecture

The code is split into three main modules:

- `models.py` defines the event and evidence structures.
- `engine.py` contains the cyber operations pipeline.
- `main.py` runs the demonstration scenario.

## 5. Data flow

1. Raw security telemetry arrives in a semi-structured JSON payload.
2. The engine normalizes the event into a `SecurityEvent` object.
3. The event is bundled into an `EvidenceBundle` with a case ID and MITRE mapping.
4. A SHA-256 payload hash is computed to ensure evidence integrity.
5. A bounded narrative is created using evidence-derived metadata.
6. A policy gate either triggers automation or routes the case for analyst review.

## 6. Design principles

- Evidence-based analysis
- Deterministic decisioning
- Human-in-the-loop review for sensitive actions
- Auditability through cryptographic lineage
- Simplicity for demonstration and education

## 7. Execution

```bash
python main.py
```

## 8. Testing strategy

The project contains tests for:

- unit behavior,
- regression coverage,
- user acceptance,
- production sanity,
- stress handling,
- performance validation.

## 9. Ownership and contact

- Devesh Kumar
- devesh2178@gmail.com

## 10. Expected use

This project is intended as a demonstration, reference, and teaching artifact for AI-driven cyber defense workflows. It is not a production-grade SOC platform by itself.
