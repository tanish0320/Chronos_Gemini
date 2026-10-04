"""
CHRONOS Zero-Latency Demo Fallback Engine
Provides 100% deterministic execution for judging in case of live API/network issues.
"""

import json
from typing import Dict, Any

DEMO_MOCK_CONTEXT: Dict[str, Any] = {
    "entity": {
        "asset_id": "PUMP-07",
        "asset_type": "Centrifugal High-Pressure Water Pump",
        "location": "Processing Bay 4"
    },
    "current_state": {
        "timestamp": "2026-09-26T09:40:00Z",
        "telemetry": {
            "temperature_c": 78.2,
            "vibration_mms": 3.8,
            "pressure_bar": 4.2
        },
        "deltas_last_30m": {
            "temperature_delta": "+13.2 C",
            "vibration_delta": "+1.8 mm/s"
        },
        "visual_inspection": {
            "image_id": "IMG_20260926_0914.png",
            "gcs_uri": "gs://chronos-industrial-artifacts/images/PUMP-07/IMG_20260926_0914.png",
            "thermal_hotspot_detected": True
        }
    },
    "recent_interventions": [
        {
            "action_id": "ACT-881",
            "timestamp": "2026-09-26T09:30:00Z",
            "action_type": "COOLANT_FLOW_BOOST",
            "parameters": {"target_flow_rate": "120%"},
            "observed_outcome": {
                "outcome_id": "OUT-881",
                "temperature_change": "-3.0 C (Slight improvement)",
                "vibration_change": "0.0 mm/s (REMAINED ELEVATED)",
                "success": False,
                "summary": "Cooling reduced temperature marginally but failed to damp vibration."
            }
        }
    ],
    "historical_precedents": [
        {
            "event_id": "EVT-2025-1104",
            "date": "2025-11-04",
            "signature": "Elevated temp + high vibration unaffected by cooling",
            "final_outcome": "Catastrophic bearing seizure within 12 hours of initial alert",
            "corrective_action_that_worked": "Controlled shutdown and bearing replacement"
        }
    ],
    "governing_policies": [
        {
            "policy_id": "POL-SOP-PUMP07-SEC4.2",
            "source_document": "MM-PUMP-07.pdf",
            "rule": "If vibration exceeds 3.5 mm/s and coolant adjustment produces no vibration reduction within 10 minutes, immediate physical bearing inspection is mandatory."
        }
    ],
    "provenance_signature": "CHRONOS-HASH-99F4A18B"
}

BASELINE_GEMINI_RESPONSE = """
### BASELINE GEMINI RECOMMENDATION (STATELESS)
**Asset ID**: PUMP-07  
**Observed Telemetry**: Temperature 78.2°C (Elevated), Vibration 3.8 mm/s (High).  
**Visual Analysis**: Thermal hotspot and race discoloration detected in `IMG_20260926_0914.png`.

**Recommendation**: Increase coolant flow rate to 120% to reduce operating temperature and re-monitor temperature levels in 15 minutes.
"""

CHRONOS_ENRICHED_GEMINI_RESPONSE = """
### CHRONOS-ENRICHED OPERATIONAL DECISION REPORT
**Asset ID**: PUMP-07  
**Risk Level**: CRITICAL (Imminent Mechanical Failure Risk: 96%)  
**Recommended Action**: Initiate controlled shutdown and perform bearing replacement within 6 hours.

#### GROUNDED EVIDENCE TRAIL:
1. **Telemetry Anomaly**: Vibration elevated by +1.8 mm/s over baseline (3.8 mm/s at 09:40:00Z).
2. **Visual Evidence**: Inspection photo `IMG_20260926_0914.png` displays outer race bearing surface discoloration.
3. **Past Action Failure**: Coolant flow boost (`ACT-881` at 09:30:00Z) reduced temperature by 3°C but produced ZERO vibration reduction (`OUT-881`).
4. **Historical Precedent**: Event `EVT-2025-1104` exhibited identical post-cooling vibration persistence, resulting in catastrophic bearing seizure.
5. **SOP Governance**: `MM-PUMP-07 Section 4.2` mandates physical bearing inspection when vibration $> 3.5\\text{ mm/s}$ persists post-coolant adjustment.
"""

def get_fallback_context(asset_id: str) -> Dict[str, Any]:
    return DEMO_MOCK_CONTEXT

def get_fallback_baseline_response() -> str:
    return BASELINE_GEMINI_RESPONSE

def get_fallback_chronos_response() -> str:
    return CHRONOS_ENRICHED_GEMINI_RESPONSE

if __name__ == "__main__":
    print("--- CHRONOS DEMO FALLBACK MOCK CHECK ---")
    print(json.dumps(get_fallback_context("PUMP-07"), indent=2))
    print("\n--- BASELINE RESP ---")
    print(get_fallback_baseline_response())
    print("\n--- CHRONOS ENRICHED RESP ---")
    print(get_fallback_chronos_response())
