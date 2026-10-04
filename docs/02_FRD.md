# CHRONOS — Functional Requirements Document (FRD)

**Document ID**: FRD-02  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team**: GGs  
**Author**: Tanish Renuka Suragihalli  

---

## 1. Overview & Priority Definitions

This document details all functional requirements for the **CHRONOS** Temporal Memory & Governance Context Layer system. 

Priority classifications:
- **P0 (Must Have)**: Critical core capabilities required for the 24-hour MVP demonstration slice.
- **P1 (Should Have)**: Core operational enhancements for robustness and visual feedback.
- **P2 (Optional / Future)**: Non-blocking features reserved for post-hackathon scaling.

---

## 2. Ingestion & Multimodal Data Requirements

### FR-ING-01: Multimodal Telemetry Ingestion
- **Priority**: P0
- **Description**: System must ingest real-time and historical IoT telemetry streams for industrial assets (e.g., Pump-07).
- **Input**: Sensor readings array `[timestamp, asset_id, temperature_c, vibration_mms, pressure_bar, rpm]`.
- **Processing**: Validate data ranges, index timestamps, push to BigQuery telemetry table and local Chronos time-series buffer.
- **Output**: Indexed time-series record with calculated moving average deltas.
- **Acceptance Criteria**: Telemetry ingested at 1 Hz update rate; moving delta computed within 10 ms.

### FR-ING-02: Visual Anomaly Image Storage & Ingestion
- **Priority**: P0
- **Description**: Ingest visual and thermal equipment inspection photographs into Google Cloud Storage (GCS) and link image metadata to asset timeline.
- **Input**: Image file binary (`.png`/`.jpg`), metadata JSON (`asset_id`, `timestamp`, `camera_id`, `resolution`).
- **Processing**: Upload binary to GCS bucket (`gs://chronos-industrial-artifacts/`), generate public/signed URI, create `ImageArtifact` graph node in Chronos.
- **Output**: `image_artifact_id`, GCS URI, temporal timestamp association.
- **Acceptance Criteria**: Image uploaded to GCS and graph node linked to timeline within 500 ms.

### FR-ING-03: SOP Document Parsing & Governance Rule Storage
- **Priority**: P0
- **Description**: Parse Standard Operating Procedure (SOP) PDF manuals and store extracted threshold rules in Chronos Policy Store.
- **Input**: SOP Document (`MM-PUMP-07.pdf`).
- **Processing**: Extract text, parse sections (e.g., Sec 4.2), extract rule tuples `(metric, threshold, condition, required_action)`.
- **Output**: Structured Policy Rule entities linked to target asset class.
- **Acceptance Criteria**: Rules extracted and queryable via `get_policy()` MCP call.

---

## 3. Chronos MCP & Context Requirements

### FR-MCP-01: MCP Protocol Integration
- **Priority**: P0
- **Description**: System must expose a standardized Model Context Protocol (MCP) server over JSON-RPC 2.0 transport for Gemini communication.
- **Input**: MCP Tool Call requests (`tools/call`, `tools/list`).
- **Processing**: Direct tool request to internal Chronos modules (Graph engine, Policy store, Outcome log).
- **Output**: MCP JSON-RPC 2.0 structured tool response.
- **Acceptance Criteria**: MCP server responds cleanly to `tools/list` and `tools/call` without standard transport errors.

### FR-MCP-02: Structured Context Package Generation (`get_context`)
- **Priority**: P0
- **Description**: Chronos must build and return a token-efficient, highly structured Context Package JSON for a specified asset and time window.
- **Input**: `entity_id` (string), `time_window_minutes` (integer), `query` (string).
- **Processing**: 
  1. Retrieve current state & telemetry deltas.
  2. Query past actions (`ACT-881`) and observed outcomes within time window.
  3. Search temporal graph for similar historical failure patterns (`EVT-2025-1104`).
  4. Fetch applicable SOP policy constraints (`MM-PUMP-07 Sec 4.2`).
  5. Compile JSON payload.
- **Output**: `ContextPackage` JSON structure.
- **Acceptance Criteria**: `get_context()` completes in $< 250\text{ ms}$ and includes current state, past action, historical precedent, and SOP clauses.

### FR-MCP-03: Policy Governance Evaluation (`get_policy`)
- **Priority**: P0
- **Description**: Evaluate active operational constraints and safety boundaries before executing or recommending an action.
- **Input**: `entity_id`, `proposed_action`, `current_metrics`.
- **Processing**: Match current metrics against stored SOP rule thresholds.
- **Output**: `PolicyResult` (`allowed: boolean`, `governing_clause`, `restriction_reason`).
- **Acceptance Criteria**: Correctly flags action as disallowed if metric exceeds safety escalation threshold.

---

## 4. Gemini Multimodal Reasoning Requirements

### FR-AI-01: Multimodal Anomaly Interpretation
- **Priority**: P0
- **Description**: Gemini 2.0 model must analyze visual equipment images alongside sensor telemetry deltas.
- **Input**: GCS Image URI + raw telemetry readings prompt.
- **Processing**: Multimodal forward pass via Vertex AI / Gemini API.
- **Output**: Perception summary (e.g., "Outer race discoloration observed; bearing temperature elevated").
- **Acceptance Criteria**: Correctly identifies visual discoloration and correlates with temperature delta.

### FR-AI-02: Context-Enriched Decision Reasoning
- **Priority**: P0
- **Description**: Gemini must reason over the Chronos `Context Package` to generate actionable recommendations.
- **Input**: System Prompt + User Anomaly Query + Chronos `Context Package`.
- **Processing**: Gemini context-aware synthesis pass.
- **Output**: Diagnosis, Actionable Recommendation, and Risk Score.
- **Acceptance Criteria**: Recommends bearing replacement instead of repeating coolant flow increase when context package proves coolant failed previously.

### FR-AI-03: Grounded Explanation Generation
- **Priority**: P0
- **Description**: Generate structured explanation referencing explicit evidence IDs rather than ungrounded free text.
- **Input**: Gemini synthesis output.
- **Processing**: Validate presence of telemetry timestamps, image IDs, past action IDs, and SOP section citations.
- **Output**: Grounded Explanation Markdown report.
- **Acceptance Criteria**: 100% of claims cite at least one empirical evidence ID (`IMG_...`, `ACT_...`, `EVT_...`, `SOP_...`).

---

## 5. Closed-Loop Feedback & User Interface Requirements

### FR-FBK-01: Decision & Outcome Writeback (`record_decision`, `record_outcome`)
- **Priority**: P0
- **Description**: Record final recommendations, human operator decisions, and subsequent sensor outcomes back into Chronos.
- **Input**: `decision_id`, `action_taken`, `post_action_telemetry_delta`, `success_flag`.
- **Processing**: Create `DecisionNode` and `OutcomeNode` in Chronos Kùzu graph; update asset temporal timeline state.
- **Output**: Confirmation receipt JSON.
- **Acceptance Criteria**: Outcome successfully committed to temporal graph and retrievable in subsequent `get_context()` calls.

### FR-DSH-01: Operational Intelligence Dashboard
- **Priority**: P1
- **Description**: Provide an interactive web dashboard for plant reliability engineers.
- **Input**: Asset selection, real-time trigger controls.
- **Processing**: Render telemetry charts, thermal image view, baseline vs. Chronos-enriched Gemini comparison, and interactive evidence graph.
- **Output**: Interactive Streamlit UI web application.
- **Acceptance Criteria**: Dashboard updates dynamically when simulated Pump-07 anomaly triggers.

### FR-VAL-01: Automated Validation & Benchmark Runner
- **Priority**: P0
- **Description**: Run automated decision quality comparison across 20 controlled temporal scenarios.
- **Input**: Benchmark scenario suite JSON.
- **Processing**: Execute Scenario across Baseline Gemini, Gemini + Raw History, and Gemini + Chronos Context Package. Compute metrics.
- **Output**: Accuracy, Stale-Context Error, and Grounding Score comparison report.
- **Acceptance Criteria**: Generates reproducible comparative CSV/JSON evaluation matrix.
