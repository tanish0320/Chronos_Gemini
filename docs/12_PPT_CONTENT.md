# CHRONOS — HackSprint Presentation Content (Slides 1–6)

**Document ID**: PPT-12  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team Name**: GGs  
**Presenter**: Tanish Renuka Suragihalli  

---

## Slide 1: The Problem — The Amnesia of Stateless AI

### Slide Title: Stateless AI Fails in Dynamic Industrial Environments
- **Real-Time Data Fragmentation**: Industrial assets generate fragmented streams of IoT telemetry, thermal inspection photos, SOP manuals, and operator logs.
- **The Stateless AI Vulnerability**: Standard multimodal LLMs analyze snapshot observations in isolation. They lack memory of past decisions, actions taken, and resulting outcomes.
- **Costly Operational Failures**:
  - **Symptomatic Over-Reaction**: Repeating failed interventions (e.g., boosting coolant for an already-cooling pump).
  - **Stale-Context Blindness**: Missing critical trend deltas and post-action sensor responses.
  - **Black-Box Unreliability**: Recommending un-grounded actions without verifiable audit trails or SOP governance compliance.

---

## Slide 2: The Solution — CHRONOS Temporal Intelligence Layer

### Slide Title: CHRONOS — Temporal Memory & Governance for Gemini
- **Core Concept**: Chronos acts as the temporal memory, context, and governance layer between enterprise data streams and Gemini AI.
- **The Closed-Loop Intelligence Cycle**:
  $$\text{Observe (GCP)} \longrightarrow \text{Remember (Chronos)} \longrightarrow \text{Reason (Gemini)} \longrightarrow \text{Decide} \longrightarrow \text{Act} \longrightarrow \text{Learn}$$
- **Key Capabilities**:
  - **Time-Indexed State Graph**: Tracks asset state deltas and moving averages across customizable time windows.
  - **Intervention & Outcome Memory**: Remembers past actions (`ACT-881`) and whether they succeeded or failed (`OUT-881`).
  - **Structured Context Package**: Compiles graph data into token-efficient JSON for Gemini reasoning.
  - **Grounded Explainability**: Ties recommendations to verifiable telemetry timestamps, image IDs, and SOP section clauses.

---

## Slide 3: Tech Stack & Architecture

### Slide Title: Google Cloud Infrastructure + Chronos MCP + Gemini 2.0

```text
┌─────────────────────────────────────────────────────────┐
│              STREAMLIT OPERATIONAL DASHBOARD            │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────┴─────────────────────────────┐
│          GOOGLE VERTEX AI / GEMINI 2.0 FLASH            │
│       (Multimodal Perception & Contextual Reasoning)     │
└───────────────────────────┬─────────────────────────────┘
                            │ Model Context Protocol (MCP)
┌───────────────────────────┴─────────────────────────────┐
│                      CHRONOS LAYER                      │
│   • Kùzu Embedded Graph DB  • SQLite Policy Governance  │
└───────────────────────────┬─────────────────────────────┘
                            │ SQL & Object Queries
┌───────────────────────────┴─────────────────────────────┐
│                 GOOGLE CLOUD DATA LAYER                 │
│   • Google BigQuery (Telemetry) • Cloud Storage (Images)│
└─────────────────────────────────────────────────────────┘
```

---

## Slide 4: Data Flow Diagram

### Slide Title: End-to-End Multimodal Data & Context Pipeline

$$\text{Telemetry/Photos} \xrightarrow{\text{1. Ingest}} \text{BigQuery/GCS} \xrightarrow{\text{2. Index}} \text{Chronos Kùzu Graph} \xrightarrow{\text{3. get\_context()}} \text{Context Package}$$

$$\text{Context Package} \xrightarrow{\text{4. Prompt}} \text{Gemini Multimodal Reasoning} \xrightarrow{\text{5. Recommend}} \text{Grounded Decision Report}$$

$$\text{Human Action} \xrightarrow{\text{6. Execute}} \text{Physical Repair} \xrightarrow{\text{7. record\_outcome()}} \text{Chronos State Writeback}$$

---

## Slide 5: Prototype Dashboard & Demo Highlights

### Slide Title: Operational Intelligence Dashboard — Pump-07 Diagnostic

- **Live Telemetry & Image Viewer**: Real-time visualization of 78°C temperature, 3.8 mm/s vibration anomaly, and inspection photo `IMG_20260926_0914.png`.
- **Comparative AI Reasoning Panel**:
  - *Baseline Gemini (Without Chronos)*: Recommends repeating coolant flow boost (Failed action `ACT-881`).
  - *Gemini + Chronos (Context-Enriched)*: Recommends immediate controlled shutdown & bearing replacement.
- **Interactive Evidence Provenance Drawer**: Displays auditable quad linking recommendation to telemetry timestamps, thermal image, past failed action, and SOP Section 4.2.

---

## Slide 6: Differentiation, Validation & Impact

### Slide Title: Proven Impact & 24-Hour Hackathon Scope

- **Core Differentiator**: CHRONOS is **not** a generic RAG text search engine. It is a time-indexed, causal state graph enforcing SOP safety rules and closed-loop outcome memory.
- **Empirical Validation (20 Temporal Scenarios)**:
  - **Decision Accuracy**: Baseline Gemini ($40\%$) vs. Gemini + Chronos ($\mathbf{95\%}$).
  - **Stale-Context Error Rate**: Baseline Gemini ($55\%$) vs. Gemini + Chronos ($\mathbf{0\%}$).
  - **Evidence Grounding**: Baseline Gemini ($15\%$) vs. Gemini + Chronos ($\mathbf{100\%}$).
- **24-Hour Scope**: 100% functional vertical slice for Pump-07 with zero-latency demo fallback mode.
