from engine import CyberTiXEngine
from models import SecurityEvent


def test_stress_batch_handling_for_large_event_volume():
    engine = CyberTiXEngine()
    events = [
        SecurityEvent(
            source=f"Source-{idx % 5}",
            event_id=f"evt_{idx}",
            timestamp="2026-06-06T12:00:00Z",
            severity="HIGH" if idx % 3 == 0 else "LOW",
            raw_payload={"agent_source": f"Source-{idx % 5}", "id": f"evt_{idx}", "sev": "HIGH" if idx % 3 == 0 else "LOW"},
        )
        for idx in range(2000)
    ]

    bundle = engine.bundle_evidence(events)

    assert len(bundle.evidence_logs) == 2000
    assert bundle.case_id.startswith("CASE-")
    assert len(bundle.integrity_hash) == 64
    assert bundle.risk_score in {4.0, 9.2}
