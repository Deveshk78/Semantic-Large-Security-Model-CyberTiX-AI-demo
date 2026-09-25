from engine import CyberTiXEngine
from models import SecurityEvent


def test_policy_gate_regression_for_critical_and_low_severity_events():
    engine = CyberTiXEngine()

    critical_event = SecurityEvent(
        source="SentinelOne",
        event_id="evt_critical_1",
        timestamp="2026-06-06T12:00:00Z",
        severity="CRITICAL",
        raw_payload={"agent_source": "SentinelOne", "sev": "CRITICAL"},
    )
    low_event = SecurityEvent(
        source="Defender",
        event_id="evt_low_1",
        timestamp="2026-06-06T12:01:00Z",
        severity="LOW",
        raw_payload={"agent_source": "Defender", "sev": "LOW"},
    )

    critical_bundle = engine.bundle_evidence([critical_event])
    critical_narration = engine.bound_llm_narration(critical_bundle)
    critical_output = engine.execute_policy_gate(critical_narration)

    low_bundle = engine.bundle_evidence([low_event])
    low_narration = engine.bound_llm_narration(low_bundle)
    low_output = engine.execute_policy_gate(low_narration)

    assert "POLICY GATE TRIGGERED" in critical_output
    assert "human-in-the-loop" in low_output.lower()
