from engine import CyberTiXEngine


def test_production_sanity_for_high_and_low_security_responses():
    engine = CyberTiXEngine()

    high_risk = {
        "agent_source": "EDR",
        "id": "evt_high_1",
        "ts": "2026-06-06T12:05:00Z",
        "sev": "CRITICAL",
        "details": {"process": "rundll32.exe", "user": "SYSTEM", "action": "suspicious_load"},
    }
    low_risk = {
        "agent_source": "CloudTrail",
        "id": "evt_low_2",
        "ts": "2026-06-06T12:06:00Z",
        "sev": "LOW",
        "details": {"resource": "api-gateway", "user": "analyst", "action": "read_only"},
    }

    high_norm = engine.normalize_telemetry(high_risk)
    low_norm = engine.normalize_telemetry(low_risk)
    high_bundle = engine.bundle_evidence([high_norm])
    low_bundle = engine.bundle_evidence([low_norm])

    high_decision = engine.execute_policy_gate(engine.bound_llm_narration(high_bundle))
    low_decision = engine.execute_policy_gate(engine.bound_llm_narration(low_bundle))

    assert high_bundle.risk_score >= 7.5
    assert low_bundle.risk_score < 5.0
    assert "POLICY GATE TRIGGERED" in high_decision
    assert "human-in-the-loop" in low_decision.lower()
