# CHRONOS — Risk Assessment & Demo Fallback Strategy

**Document ID**: RISK-10  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team**: GGs  
**Author**: Tanish Renuka Suragihalli  

---

## 1. Hackathon Risk Matrix

| Risk ID | Risk Description | Prob. | Impact | Early Warning Indicator | Primary Mitigation | Fallback Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **R-01** | **Vertex AI / Gemini API Rate Limit or Timeout** | Med | High | HTTP 429 errors or latency $> 10\text{ s}$ during test calls. | Implement retry exponential backoff + fallback to standard Gemini 1.5 Flash API key. | Activate pre-cached local Gemini response mock layer (`src/ai/mock_gemini.py`). |
| **R-02** | **MCP JSON-RPC Server Connection Crash** | Low | High | Standard I/O pipe closed or socket connection refused. | Wrap MCP server with auto-restart supervisor script. | Fallback to direct Python in-process function invocation of `get_context()`. |
| **R-03** | **Google Cloud Storage / BigQuery Credential Failure** | Med | Med | GCP Auth Exception / missing service account file. | Set local environment credentials (`GOOGLE_APPLICATION_CREDENTIALS`). | Use local SQLite + file-system image directory fallback mode. |
| **R-04** | **Kùzu Graph DB Lock File Error** | Low | Med | `RuntimeError: Database path locked by another process`. | Use single-threaded embedded process handle or read-only mode for UI. | Fallback to in-memory JSON state dictionary graph. |
| **R-05** | **Multimodal Image Payload Rejection** | Low | High | Gemini API error processing image dimensions/MIME type. | Pre-convert all images to standard $1024 \times 1024$ PNG format. | Provide text-only optical feature extraction string in prompt. |
| **R-06** | **Streamlit UI Rendering Crash** | Med | Med | Blank screen or unhandled exception during live demo. | Wrap Streamlit components in strict `try-except` blocks with error banners. | Present terminal CLI demo interface with formatted markdown output. |
| **R-07** | **Time Running Out Before Complete Integration** | High | High | Hour 18 reached with un-integrated modules. | Strict adherence to Hour 21 Integration Freeze; Person 4 lead enforcement. | Cut non-essential features (P1/P2); showcase complete narrow vertical slice for Pump-07. |

---

## 2. Demo-Safe Fallback Architecture

To guarantee a flawless presentation to judges regardless of network conditions or Google Cloud API downtime, CHRONOS incorporates a zero-latency, deterministic **Demo Fallback System**.

```text
               ┌───────────────────────────┐
               │    Streamlit Dashboard    │
               └─────────────┬─────────────┘
                             │
            Check Network / API Availability
                             │
          ┌──────────────────┴──────────────────┐
          │                                     │
    [ ONLINE MODE ]                    [ FALLBACK MOCK MODE ]
  Vertex AI + Live GCP                Cached Provenance Payloads
  Live Chronos Graph                  Pre-Recorded Gemini Responses
```

### 2.1 Demo Fallback Implementation (`demo_fallback_mock.py`)

```python
"""
CHRONOS Zero-Network Demo Fallback Engine
Ensures 100% deterministic demo execution even if WiFi fails or GCP quota is hit.
"""

import json

DEMO_MOCK_CONTEXT = {
    "entity": {"asset_id": "PUMP-07", "type": "High-Pressure Water Pump"},
    "current_state": {"temp_c": 78.2, "vibration_mms": 3.8, "image_id": "IMG_20260926_0914.png"},
    "recent_interventions": [
        {"action_id": "ACT-881", "type": "COOLANT_BOOST", "outcome": "Temp dropped 3C, vibration unchanged", "success": False}
    ],
    "historical_precedents": [
        {"event_id": "EVT-2025-1104", "summary": "Cooling ineffective; bearing seized within 12h"}
    ],
    "governing_policies": [
        {"policy_id": "POL-SOP-SEC4.2", "rule": "Vibration > 3.5 mm/s post-cooling mandates physical inspection"}
    ]
}

DEMO_MOCK_RESPONSE = """
### OPERATIONAL DECISION REPORT (FALLBACK MODE)
**Asset ID**: PUMP-07  
**Risk Level**: HIGH (Imminent Bearing Failure)  
**Recommended Action**: Schedule controlled shutdown & bearing replacement within 6 hours.

#### GROUNDED EVIDENCE TRAIL:
1. **Telemetry**: Vibration elevated at 3.8 mm/s (+1.8 mm/s above baseline).
2. **Visual**: Thermal hotspot and race discoloration in `IMG_20260926_0914.png`.
3. **Past Action**: Coolant boost (`ACT-881`) failed to reduce vibration.
4. **Precedent**: Matches catastrophic seizure pattern in `EVT-2025-1104`.
5. **SOP Rule**: Mandated by `MM-PUMP-07 Section 4.2`.
"""

def get_demo_context(asset_id: str):
    return DEMO_MOCK_CONTEXT

def get_demo_gemini_response(context: dict):
    return DEMO_MOCK_RESPONSE
```
