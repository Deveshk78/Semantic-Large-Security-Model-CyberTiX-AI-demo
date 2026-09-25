from dataclasses import dataclass
from typing import Dict, List, Any

@dataclass
class SecurityEvent:
    source: str
    event_id: str
    timestamp: str
    severity: str
    raw_payload: Dict[str, Any]

@dataclass
class EvidenceBundle:
    case_id: str
    mitre_technique: str
    risk_score: float
    evidence_logs: List[Dict[str, Any]]
    integrity_hash: str