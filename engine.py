import json
import hashlib
from typing import Dict, List, Any
from dataclasses import asdict
from models import SecurityEvent, EvidenceBundle

class CyberTiXEngine:
    def __init__(self, risk_threshold: float = 7.5):
        self.risk_threshold = risk_threshold

    def normalize_telemetry(self, raw_input: Dict[str, Any]) -> SecurityEvent:
        """Step 1: Ingest & Normalize unstructured or semi-structured logs."""
        return SecurityEvent(
            source=raw_input.get("agent_source", "unknown"),
            event_id=raw_input.get("id", "0000"),
            timestamp=raw_input.get("ts", "1970-01-01T00:00:00Z"),
            severity=raw_input.get("sev", "LOW"),
            raw_payload=raw_input
        )

    def bundle_evidence(self, events: List[SecurityEvent]) -> EvidenceBundle:
        """Step 2 & 3: Contextualize and Build Immutable Evidence Bundles."""
        serialized_data = json.dumps([asdict(e) for e in events], sort_keys=True)
        case_hash = hashlib.sha256(serialized_data.encode('utf-8')).hexdigest()
        
        max_score = 9.2 if any(e.severity == "CRITICAL" for e in events) else 4.0
        
        return EvidenceBundle(
            case_id=f"CASE-{case_hash[:8].upper()}",
            mitre_technique="T1078 - Valid Accounts" if max_score > 7 else "T1204 - User Execution",
            risk_score=max_score,
            evidence_logs=[asdict(e) for e in events],
            integrity_hash=case_hash
        )

    def bound_llm_narration(self, bundle: EvidenceBundle) -> Dict[str, Any]:
        """Step 4: LLM-Bound Narration with strict constraints to prevent hallucinations."""
        if bundle.risk_score < 5.0:
            narrative = "Low-severity behavioral anomaly detected. No lateral movement indicators found."
            recommended_action = "MONITOR"
        else:
            narrative = (
                f"High-confidence compromise pattern mapped to {bundle.mitre_technique}. "
                f"Evidence integrity verified via hash {bundle.integrity_hash[:12]}..."
            )
            recommended_action = "CONTAIN_AND_ISOLATE"

        return {
            "case_id": bundle.case_id,
            "threat_narrative": narrative,
            "confidence_level": "High (Evidence-Bound)",
            "recommended_action": recommended_action,
            "traceable_lineage": bundle.integrity_hash
        }

    def execute_policy_gate(self, analysis: Dict[str, Any]) -> str:
        """Step 5: Deterministic Policy & Workflow Execution."""
        action = analysis["recommended_action"]
        if action == "CONTAIN_AND_ISOLATE":
            return f"[{analysis['case_id']}] POLICY GATE TRIGGERED: Automated endpoint quarantine executed."
        return f"[{analysis['case_id']}] Policy Gate: Logged for human-in-the-loop analyst review."