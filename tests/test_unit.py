from engine import CyberTiXEngine
from models import SecurityEvent


def test_normalize_telemetry_creates_expected_record():
    engine = CyberTiXEngine()
    raw_input = {
        "agent_source": "CrowdStrike/EDR",
        "id": "evt_9001",
        "ts": "2026-06-06T12:00:00Z",
        "sev": "HIGH",
        "details": {"process": "powershell.exe", "user": "admin", "action": "credential_access"},
    }

    event = engine.normalize_telemetry(raw_input)

    assert isinstance(event, SecurityEvent)
    assert event.source == "CrowdStrike/EDR"
    assert event.event_id == "evt_9001"
    assert event.timestamp == "2026-06-06T12:00:00Z"
    assert event.severity == "HIGH"
    assert event.raw_payload["details"]["action"] == "credential_access"
