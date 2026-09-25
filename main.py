import json
from engine import CyberTiXEngine

def main():
    print("Initializing CyberTiX AI Security Operations Engine (Cygeniq Architecture Simulation)...\n")
    engine = CyberTiXEngine()
    
    # Simulate raw incoming EDR/Cloud log payload
    incoming_raw_log = {
        "agent_source": "CrowdStrike/EDR",
        "id": "evt_99812",
        "ts": "2026-06-06T12:00:00Z",
        "sev": "CRITICAL",
        "details": {"process": "mimikatz.exe", "user": "SYSTEM", "action": "lsass_dump"}
    }
    
    print("--- [1] Raw Ingest Payload ---")
    print(json.dumps(incoming_raw_log, indent=2))
    
    # Run pipeline stages
    normalized = engine.normalize_telemetry(incoming_raw_log)
    print("\n--- [2] Normalized Telemetry Event ---")
    print(normalized)
    
    bundle = engine.bundle_evidence([normalized])
    print("\n--- [3] Evidence Bundle & Cryptographic Hash ---")
    print(f"Case ID: {bundle.case_id}")
    print(f"MITRE Technique: {bundle.mitre_technique}")
    print(f"SHA-256 Hash: {bundle.integrity_hash}")
    
    narration = engine.bound_llm_narration(bundle)
    print("\n--- [4] Bounded LLM Threat Narration ---")
    print(json.dumps(narration, indent=2))
    
    response = engine.execute_policy_gate(narration)
    print("\n--- [5] Deterministic Policy Gate Action ---")
    print(response)

if __name__ == "__main__":
    main()