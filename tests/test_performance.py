import time

from engine import CyberTiXEngine
from models import SecurityEvent


def test_bundle_generation_remains_fast_for_repeat_loads():
    engine = CyberTiXEngine()
    events = [
        SecurityEvent(
            source="perf-source",
            event_id=f"evt_perf_{idx}",
            timestamp="2026-06-06T12:00:00Z",
            severity="CRITICAL" if idx % 5 == 0 else "LOW",
            raw_payload={"agent_source": "perf-source", "id": f"evt_perf_{idx}", "sev": "CRITICAL" if idx % 5 == 0 else "LOW"},
        )
        for idx in range(200)
    ]

    start = time.perf_counter()
    for _ in range(200):
        engine.bundle_evidence(events)
    elapsed = time.perf_counter() - start

    assert elapsed < 5.0
