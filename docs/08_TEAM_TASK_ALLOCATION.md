# CHRONOS — Team Task Allocation & Workstream Matrix

**Document ID**: TEAM-08  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team Name**: GGs  
**Author / Team Lead**: Tanish Renuka Suragihalli  

---

## 1. Team Workstream Architecture

To maximize efficiency during the 24-hour hackathon, work is partitioned into four independent, highly parallelized workstreams with explicit contract interfaces.

```text
PERSON 1: Chronos & MCP Core Engine  ◄─────── (MCP JSON-RPC Interface) ────────► PERSON 2: Gemini & Vertex AI Pipeline
                                                                                               │
                                                                                        (Vertex AI Prompt)
                                                                                               ▼
PERSON 3: Google Cloud & BigQuery Data ◄───── (Data Feed & Telemetry) ────────► PERSON 4: Dashboard, Integration & Benchmark
```

---

## 2. Individual Workstream Matrix

### PERSON 1: Chronos Core, Graph Storage & MCP Server Lead
- **Primary Role**: Systems Architect & Temporal Memory Lead.
- **Key Responsibilities**: Kùzu embedded graph engine, state snapshot tracking, SOP policy lookup, MCP server implementation over JSON-RPC.
- **Deliverables**: `src/chronos/graph.py`, `src/chronos/mcp_server.py`, `src/chronos/policy.py`.
- **Dependencies**: Receives schema definitions from Person 3.
- **Phase Breakdown**:
  - **First 6 Hours**: Build Kùzu graph DB schema, implement `get_context()` payload builder.
  - **Middle 6 Hours**: Implement `get_policy()`, `record_decision()`, and `record_outcome()` writebacks.
  - **Final 6 Hours**: MCP performance optimization ($< 250\text{ ms}$ response) & integration support for UI.
  - **Final 6 Hours Support**: Code freeze lock, backend bug fixing, offline mock fallback validation.

---

### PERSON 2: Gemini 2.0 & Vertex AI Multimodal Pipeline Lead
- **Primary Role**: AI Engineer & Multimodal Reasoning Lead.
- **Key Responsibilities**: Vertex AI SDK integration, Gemini 2.0 Flash / 1.5 Pro prompt engineering, image feature correlation, grounded evidence citation parser.
- **Deliverables**: `src/ai/gemini_reasoner.py`, `src/ai/prompt_templates.py`, `src/ai/evidence_parser.py`.
- **Dependencies**: Consumes `Context Package` format from Person 1; image artifacts from Person 3.
- **Phase Breakdown**:
  - **First 6 Hours**: Setup Vertex AI SDK, build Baseline vs. Chronos prompt templates.
  - **Middle 6 Hours**: Implement image + text multimodal forward pass and evidence grounding parser.
  - **Final 6 Hours**: Tune prompt instructions to prevent hallucinated recommendations.
  - **Final 6 Hours Support**: Benchmark scenario evaluation support & slide 2/5 presentation graphics.

---

### PERSON 3: Google Cloud Infrastructure & Data Ingestion Lead
- **Primary Role**: Data Systems & Infrastructure Lead.
- **Key Responsibilities**: Google BigQuery telemetry tables, GCS object bucket layout, synthetic Pump-07 data generator, SOP PDF parser.
- **Deliverables**: `src/cloud/bigquery_client.py`, `src/cloud/gcs_client.py`, `data/generate_pump07_data.py`.
- **Dependencies**: Independent data layer producer.
- **Phase Breakdown**:
  - **First 6 Hours**: Generate Pump-07 telemetry stream, populate local/cloud BigQuery tables, upload inspection photos to GCS.
  - **Middle 6 Hours**: Build SOP PDF parser (`MM-PUMP-07.pdf`) and REST/gRPC endpoint bindings.
  - **Final 6 Hours**: Data pipeline stress testing and BigQuery query optimization.
  - **Final 6 Hours Support**: Infrastructure monitor, demo data reset scripts, PPT diagram review.

---

### PERSON 4: Frontend UI, Validation Benchmark & Team Lead (Tanish Renuka Suragihalli)
- **Primary Role**: Product Architect, UI Developer & Hackathon Lead.
- **Key Responsibilities**: Streamlit operational dashboard, end-to-end system integration, 20-scenario temporal benchmark suite, PPT slide deck, live demo presentation.
- **Deliverables**: `app.py` (Dashboard), `benchmark/run_benchmark.py`, PPT Slides, `SUBMISSION_MASTER.md`.
- **Dependencies**: Integrates components from Persons 1, 2, and 3.
- **Phase Breakdown**:
  - **First 6 Hours**: Project setup, docs creation (`PRD`, `FRD`, `Architecture`), Streamlit layout scaffold.
  - **Middle 6 Hours**: Complete Streamlit UI, build comparative reasoning view, implement benchmark runner script.
  - **Final 6 Hours**: Execute benchmark evaluation, populate metrics into PPT slide deck, conduct demo rehearsals.
  - **Final 6 Hours Support**: Integration freeze enforcement, master submission assembly, pitch presentation lead.

---

## 3. Communication Protocols & Coordination Syncs

To ensure seamless progress without bottlenecking:
1. **Sync 1 (Hour 02)**: Schema Contract Lock (BigQuery SQL schema, Graph schema, MCP JSON spec).
2. **Sync 2 (Hour 12)**: Integration Checkpoint (First end-to-end query from Streamlit $\rightarrow$ Gemini $\rightarrow$ Chronos).
3. **Sync 3 (Hour 18)**: Code Freeze & Benchmark Review (Lock master branch, review evaluation metrics).
4. **Sync 4 (Hour 22)**: Pitch Dry-Run (Full 3-minute demo rehearsal).
