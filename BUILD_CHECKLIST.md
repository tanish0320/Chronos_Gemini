# CHRONOS — 24-Hour Hackathon Build Checklist

**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team Name**: GGs  

---

## Phase 1: Environment & Repository Initialization (Hours 00–02)
- [x] Initialize Git repository & branch structure (`master`, `dev`)
- [x] Create project directory layout (`/docs`, `/src`, `/tests`, `/data`, `/benchmark`)
- [x] Write `INTERNAL_ASSESSMENT.md` capability audit
- [x] Create complete documentation package (`01_PRD.md` through `13_JUDGES_QA.md`)
- [x] Generate Mermaid architecture & data flow diagrams in `docs/diagrams/`
- [ ] Configure Python virtualenv & install dependencies (`requirements.txt`)
- [ ] Set up environment variable credentials (`.env`)

---

## Phase 2: Data Layer & Google Cloud Setup (Hours 02–04)
- [ ] Generate synthetic Pump-07 telemetry stream (`data/telemetry_pump07.json`)
- [ ] Create mock inspection photo (`data/IMG_20260926_0914.png`)
- [ ] Parse SOP PDF manual rules (`data/MM-PUMP-07.pdf`)
- [ ] Implement Google BigQuery telemetry ingestion module (`src/cloud/bigquery_client.py`)
- [ ] Implement Google Cloud Storage client for image artifacts (`src/cloud/gcs_client.py`)

---

## Phase 3: Chronos Temporal Engine & MCP Server (Hours 04–06)
- [ ] Build Kùzu embedded graph database schema (`src/chronos/graph.py`)
- [ ] Implement `get_context()` MCP payload compiler (`src/chronos/context_builder.py`)
- [ ] Implement SOP policy governance engine (`src/chronos/policy.py`)
- [ ] Expose JSON-RPC 2.0 MCP server endpoints (`src/chronos/mcp_server.py`)

---

## Phase 4: Gemini 2.0 / Vertex AI Integration (Hours 06–08)
- [ ] Implement Vertex AI SDK client wrapper (`src/ai/gemini_reasoner.py`)
- [ ] Create Baseline (Stateless) vs. Chronos-Enriched prompt templates (`src/ai/prompts.py`)
- [ ] Build multimodal optical image + sensor prompt parser (`src/ai/multimodal_parser.py`)
- [ ] Build evidence citation parser & validation formatter (`src/ai/evidence_parser.py`)

---

## Phase 5: Closed-Loop Outcome Feedback & Writeback (Hours 08–10)
- [ ] Implement `record_decision()` MCP endpoint (`src/chronos/mcp_server.py`)
- [ ] Implement `record_outcome()` MCP endpoint (`src/chronos/mcp_server.py`)
- [ ] Connect post-action sensor state update to Kùzu graph nodes (`src/chronos/graph.py`)
- [ ] Verify outcome persistence across sequential query calls

---

## Phase 6: Streamlit Operational Dashboard UI (Hours 10–12)
- [ ] Scaffold Streamlit web application layout (`app.py`)
- [ ] Build live telemetry anomaly trigger & sensor chart components
- [ ] Build optical inspection photo & thermal overlay view
- [ ] Build comparative reasoning drawer (Baseline Gemini vs. Gemini + Chronos)
- [ ] Build interactive evidence provenance graph inspector

---

## Phase 7: System Integration & End-to-End Testing (Hours 12–14)
- [ ] Connect Streamlit UI $\rightarrow$ Gemini $\rightarrow$ Chronos MCP $\rightarrow$ BigQuery/GCS
- [ ] Execute full reference event chain (09:10–09:40 Pump-07 anomaly)
- [ ] Verify latency performance ($< 250\text{ ms}$ for MCP context query)
- [ ] Test cross-module error handling and reconnect logic

---

## Phase 8: Benchmark Suite & Validation Execution (Hours 14–18)
- [ ] Define 20 controlled temporal scenarios JSON (`benchmark/scenarios.json`)
- [ ] Implement automated evaluation runner (`benchmark/run_benchmark.py`)
- [ ] Execute comparative benchmark across Baseline, Raw History, and Chronos Context
- [ ] Compute metrics: Decision Accuracy, Stale-Context Errors, Grounding Score
- [ ] Export validation summary tables & charts for presentation

---

## Phase 9: Integration Freeze & Demo Fallback (Hours 18–21) [CRITICAL]
- [ ] **ENFORCE INTEGRATION FREEZE** (Stop all feature development at Hour 21)
- [ ] Verify offline zero-latency demo fallback engine (`demo_fallback_mock.py`)
- [ ] Conduct edge-case failure testing (network disconnection, API rate limits)
- [ ] Fix high-priority bug tickets only

---

## Phase 10: PPT Finalization, Rehearsal & Submission (Hours 21–24)
- [ ] Embed actual benchmark charts & UI screenshots into PPT (`compressed_Chronos_HackSprint_Final.pptx`)
- [ ] Conduct 3 dry-run presentations of the 3-minute judge demo
- [ ] Finalize GitHub repository clean commit log
- [ ] Push final master submission package
