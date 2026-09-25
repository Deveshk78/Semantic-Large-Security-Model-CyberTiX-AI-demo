from engine import CyberTiXEngine


def test_end_to_end_threat_workflow_succeeds_for_demo_case():
    engine = CyberTiXEngine()
    raw_input = {
        "agent_source": "CrowdStrike/EDR",
        "id": "evt_99812",
        "ts": "2026-06-06T12:00:00Z",
        "sev": "CRITICAL",
        "details": {"process": "mimikatz.exe", "user": "SYSTEM", "action": "lsass_dump"},
    }

    normalized = engine.normalize_telemetry(raw_input)
    bundle = engine.bundle_evidence([normalized])
    narration = engine.bound_llm_narration(bundle)
    response = engine.execute_policy_gate(narration)

    assert normalized.severity == "CRITICAL"
    assert bundle.case_id.startswith("CASE-")
    assert bundle.mitre_technique.startswith("T")
    assert len(bundle.integrity_hash) == 64
    assert "POLICY GATE TRIGGERED" in response
