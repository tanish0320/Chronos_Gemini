# CHRONOS — Model Context Protocol (MCP) Interface Specification

**Document ID**: MCP-06  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team**: GGs  
**Author**: Tanish Renuka Suragihalli  

---

## 1. Overview & Transport Protocol

Chronos exposes its temporal memory, state graph, and policy enforcement via the **Model Context Protocol (MCP)** using JSON-RPC 2.0 transport over HTTP/SSE or Standard I/O (stdio).

This interface enables Google Gemini (or any compliant LLM agent) to iteratively request temporal context, verify safety policies, and record decision outcomes.

---

## 2. Hackathon Minimum MCP Tool Suite

For the 24-hour MVP, Chronos implements four core MCP tools:

| Tool Name | Primary Purpose | Input Parameters | Output Payload |
| :--- | :--- | :--- | :--- |
| **`get_context`** | Retrieve structured temporal context package for an entity | `entity_id`, `time_window_minutes`, `query` | Structured `ContextPackage` JSON |
| **`get_policy`** | Evaluate SOP safety constraints for a proposed action | `entity_id`, `proposed_action`, `metrics` | `PolicyResult` JSON |
| **`record_decision`** | Commit Gemini recommendation & citations to Chronos graph | `asset_id`, `action`, `evidence_ids`, `confidence` | `DecisionReceipt` JSON |
| **`record_outcome`** | Write back human action execution & resulting sensor delta | `decision_id`, `action_executed`, `telemetry_delta`, `success` | `OutcomeReceipt` JSON |

---

## 3. Tool Specifications & Payload Examples

### 3.1 `get_context`

#### Request JSON-RPC 2.0:
```json
{
  "jsonrpc": "2.0",
  "id": "req-001",
  "method": "tools/call",
  "params": {
    "name": "get_context",
    "arguments": {
      "entity_id": "PUMP-07",
      "time_window_minutes": 60,
      "query": "Evaluate elevated temperature and vibration anomaly"
    }
  }
}
```

#### Response Payload:
```json
{
  "jsonrpc": "2.0",
  "id": "req-001",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\n  \"entity\": {\"asset_id\": \"PUMP-07\", \"type\": \"High-Pressure Pump\"},\n  \"current_state\": {\"temp_c\": 78.2, \"vibration_mms\": 3.8, \"image_id\": \"IMG_20260926_0914.png\"},\n  \"recent_interventions\": [{\"action_id\": \"ACT-881\", \"type\": \"COOLANT_BOOST\", \"outcome\": \"Temp dropped 3C, vibration unchanged\", \"success\": false}],\n  \"historical_precedents\": [{\"event_id\": \"EVT-2025-1104\", \"summary\": \"Cooling ineffective; bearing seized within 12h\"}],\n  \"governing_policies\": [{\"policy_id\": \"POL-SOP-SEC4.2\", \"rule\": \"Vibration > 3.5 mm/s post-cooling mandates physical inspection\"}]\n}"
      }
    ]
  }
}
```

---

### 3.2 `get_policy`

#### Request JSON-RPC 2.0:
```json
{
  "jsonrpc": "2.0",
  "id": "req-002",
  "method": "tools/call",
  "params": {
    "name": "get_policy",
    "arguments": {
      "entity_id": "PUMP-07",
      "proposed_action": "COOLANT_FLOW_BOOST_2ND_ATTEMPT",
      "current_vibration_mms": 3.8
    }
  }
}
```

#### Response Payload:
```json
{
  "jsonrpc": "2.0",
  "id": "req-002",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\n  \"allowed\": false,\n  \"governing_clause\": \"MM-PUMP-07 Section 4.2\",\n  \"restriction_reason\": \"Disallowed: Coolant adjustment already attempted at 09:30 without vibration reduction. SOP mandates immediate physical inspection.\"\n}"
      }
    ]
  }
}
```

---

### 3.3 `record_decision`

#### Request Payload:
```json
{
  "jsonrpc": "2.0",
  "id": "req-003",
  "method": "tools/call",
  "params": {
    "name": "record_decision",
    "arguments": {
      "asset_id": "PUMP-07",
      "recommended_action": "BEARING_INSPECTION_AND_REPLACEMENT",
      "confidence": 0.96,
      "cited_evidence": ["IMG_20260926_0914.png", "ACT-881", "EVT-2025-1104", "POL-SOP-SEC4.2"]
    }
  }
}
```

#### Response Payload:
```json
{
  "jsonrpc": "2.0",
  "id": "req-003",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"status\": \"SUCCESS\", \"decision_id\": \"DEC-20260926-0940\", \"committed_to_graph\": true}"
      }
    ]
  }
}
```

---

### 3.4 `record_outcome`

#### Request Payload:
```json
{
  "jsonrpc": "2.0",
  "id": "req-004",
  "method": "tools/call",
  "params": {
    "name": "record_outcome",
    "arguments": {
      "decision_id": "DEC-20260926-0940",
      "action_executed": "BEARING_REPLACEMENT",
      "resulting_telemetry": {"temp_c": 64.5, "vibration_mms": 1.9},
      "anomaly_resolved": true
    }
  }
}
```

#### Response Payload:
```json
{
  "jsonrpc": "2.0",
  "id": "req-004",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"status\": \"SUCCESS\", \"outcome_id\": \"OUT-20260926-1015\", \"temporal_state_updated\": true}"
      }
    ]
  }
}
```

---

## 4. Error Handling & Authentication

### 4.1 Error Codes
- `-32602`: Invalid params (e.g. missing `entity_id`).
- `-32603`: Internal Chronos Graph error (e.g. DB lock error).
- `-32001`: Asset state not found in temporal index.

### 4.2 Security & Authentication (Hackathon MVP Scope)
- Local HTTP transport secured via `Bearer` token (`CHRONOS_MCP_SECRET_KEY`).
- GCP IAM service account authentication used for GCS blob access and Vertex AI model calls.
