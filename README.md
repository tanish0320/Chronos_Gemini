# CHRONOS — Temporal Memory & Governance Context Layer for Gemini AI

[![MAHE HackSprint 2026](https://img.shields.io/badge/MAHE_HackSprint-Track_PS42-blue.svg)](https://manipal.edu)
[![Google Gemini](https://img.shields.io/badge/Gemini_2.0-Multimodal-orange.svg)](https://ai.google.dev)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-Vertex_AI_%7C_BigQuery_%7C_GCS-4285F4.svg)](https://cloud.google.com)
[![MCP](https://img.shields.io/badge/MCP-Model_Context_Protocol-purple.svg)](https://modelcontextprotocol.io)

> **"Gemini understands multimodal information; Chronos allows it to understand that information in context — across time, decisions, actions, and outcomes."**

---

## 1. Executive Summary & Problem

Modern industrial operational environments generate fragmented streams of real-time heterogeneous data: IoT sensor telemetry, thermal/optical inspection photos, SOP PDF manuals, and operator maintenance logs. 

Current stateless multimodal AI models evaluate data snapshots in isolation. Because they lack persistent memory of past actions, state deltas over time, and intervention outcomes, they frequently make reactive, repetitive, or unexplainable recommendations (such as repeatedly increasing cooling flow for a pump whose internal bearing is physically tearing itself apart).

**CHRONOS** solves this by providing a time-indexed property graph, SOP policy enforcement engine, and closed-loop outcome memory accessible via the **Model Context Protocol (MCP)**.

---

## 2. High-Level Architecture

```text
REAL-TIME MULTIMODAL DATA (Sensors, Thermal Photos, SOP PDFs)
               │
               ▼
     GOOGLE CLOUD INFRASTRUCTURE (Cloud Storage & BigQuery)
               │
               ▼
     CHRONOS TEMPORAL LAYER (Kùzu Property Graph & Policy Store)
               │
               ▼  Model Context Protocol (get_context)
     GEMINI MULTIMODAL REASONING (Vertex AI Engine)
               │
               ▼
     GROUNDED EXPLAINABLE DECISION & AUDIT TRAIL
               │
               ▼
     HUMAN OPERATOR APPROVAL & ACTION
               │
               ▼
     CLOSED-LOOP OUTCOME WRITEBACK (record_outcome -> Chronos Graph)
```

---

## 3. Tech Stack

- **Reasoning Engine**: Google Gemini 2.0 Flash / 1.5 Pro (via Google Vertex AI SDK)
- **Cloud Infrastructure**: Google Cloud Storage (GCS) for images/SOPs, Google BigQuery for telemetry logs
- **Temporal Memory & Graph**: Kùzu Embedded Property Graph DB
- **Policy & Governance**: SQLite Operational Policy Store
- **Agent Interface**: Model Context Protocol (MCP) JSON-RPC 2.0
- **Dashboard UI**: Streamlit Interactive Web Application
- **Language & Environment**: Python 3.11+

---

## 4. Hackathon MVP Scope (What Will Actually Be Demonstrated)

During the 24-hour MAHE HackSprint, we deliver a 100% functional vertical slice focused on **Industrial Asset Pump-07**:

1. **Multimodal Data Ingestion**: Ingesting Pump-07 telemetry deltas into BigQuery and loading thermal photo `IMG_20260926_0914.png` from GCS.
2. **Chronos MCP Context Server**: `get_context()` returning structured JSON Context Packages containing past failed action `ACT-881` and precedent `EVT-2025-1104`.
3. **Gemini Reasoning Shift**: Demonstrating Baseline Gemini (recommending failed coolant boost) vs. Gemini + Chronos (recommending bearing replacement).
4. **Grounded Explainability**: Verifiable audit quad linking decision $\rightarrow$ image $\rightarrow$ telemetry $\rightarrow$ SOP clause.
5. **Closed-Loop Feedback**: Writing human operator action and normal post-repair sensor state back to Chronos.
6. **Empirical Validation**: Automated benchmark evaluation script scoring 20 temporal scenarios.

---

## 5. Repository Status

| Component | Status | Description |
| :--- | :--- | :--- |
| **Documentation Package** | **Complete** | PRD, FRD, Architecture, Data Specs, AI Strategy, MCP Specs, Build Plan, Allocation, Validation Plan, Risks, Demo Script, PPT, Judges Q&A. |
| **Mermaid Diagrams** | **Complete** | Architecture, Data Flow, Gemini-Chronos Interaction, Context Retrieval, Feedback Loop, Deployment. |
| **Pump-07 Demo Dataset** | **Complete** | Telemetry JSON streams, inspection photos, SOP rules. |
| **Chronos MCP Server** | **MVP Scaffold** | `get_context`, `get_policy`, `record_decision`, `record_outcome` endpoints. |
| **Streamlit UI** | **Prototype** | Interactive dashboard with real-time alert trigger and comparative AI reasoning drawer. |
| **Validation Benchmark** | **Complete** | Scenario suite generator and scoring script. |

---

## 6. Quick Start & Execution

### Prerequisites
- Python 3.11+ installed
- Google Cloud Service Account JSON (or local mock mode)

### Installation
```bash
# Clone the repository
git clone GITHUB_REPO_URL=TO_BE_CREATED
cd mahe

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup (`.env`)
```ini
GOOGLE_APPLICATION_CREDENTIALS="path/to/gcp_credentials.json"
GCP_PROJECT_ID="chronos-hacksprint-2026"
GEMINI_API_KEY="AIzaSy..."
CHRONOS_ENV="development"
```

### Run Demo Dashboard
```bash
streamlit run app.py
```

### Run Empirical Benchmark Suite
```bash
python benchmark/run_benchmark.py
```

---

## 7. Team & Contact Information

**Team Name**: GGs  
**Track**: MAHE HackSprint Track PS42  
**Lead Architect & Presenter**: Tanish Renuka Suragihalli  
**Team Members**: 4-person multidisciplinary engineering team  

---

## 8. License & Acknowledgments

Developed for the MAHE HackSprint 24-Hour Hackathon 2026. Built using Google Gemini AI, Google Cloud Platform, Kùzu Graph DB, and Model Context Protocol.
