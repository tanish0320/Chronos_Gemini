# CHRONOS — 24-Hour Hackathon Build Plan

**Document ID**: PLAN-07  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team**: GGs  
**Author**: Tanish Renuka Suragihalli  

---

## 1. Master Timeline (2-Hour Blocks)

```text
 HOURS 00-02  ──► Architecture Lock, Repo Setup & Schema Finalization
 HOURS 02-04  ──► Synthetic Data Generation & GCP Storage Layer Setup
 HOURS 04-06  ──► Chronos MCP Engine & Context Package Builder
 HOURS 06-08  ──► Vertex AI / Gemini 2.0 Multimodal Pipeline Integration
 HOURS 08-10  ──► Closed-Loop Writeback & Policy Governance Engine
 HOURS 10-12  ──► Streamlit Operational Dashboard Prototype
 HOURS 12-14  ──► End-to-End System Integration (GCP + Chronos + Gemini + UI)
 HOURS 14-16  ──► Benchmark Suite Development (20 Temporal Scenarios)
 HOURS 16-18  ──► Validation Benchmark Execution & Empirical Scoring
 HOURS 18-21  ──► [INTEGRATION FREEZE] Bug Fixing & Demo Safety Fallbacks
 HOURS 21-24  ──► PPT Polish, Scripted Demo Rehearsal & Master Submission
```

---

## 2. Detailed Work Block Schedule

### Hours 00–02: Kickoff, Architecture Lock & Repo Initialization
- Initialize Git repository, structure `/docs`, `/src`, `/tests`, `/data`.
- Finalize schema specs for BigQuery, Kùzu graph DB, and MCP JSON-RPC endpoints.
- Environment setup: Python 3.11 virtualenv, Vertex AI SDK, Streamlit, Kùzu DB.

### Hours 02–04: Data Ingestion & Google Cloud Setup
- Generate Pump-07 synthetic telemetry stream (`telemetry_pump07.json` / BigQuery format).
- Create inspection photos (`IMG_20260926_0914.png`) and SOP PDF (`MM-PUMP-07.pdf`).
- Setup GCS storage client / local mock for image artifact loading.

### Hours 04–06: Chronos Core & MCP Server Implementation
- Implement `ChronosGraph` engine using Kùzu embedded graph DB.
- Implement `get_context()` MCP tool to generate structured JSON Context Packages.
- Implement `get_policy()` SOP constraint checker.

### Hours 06–08: Gemini 2.0 / Vertex AI Integration
- Implement `GeminiReasoner` wrapper supporting Vertex AI SDK & direct API fallback.
- Implement dual-mode prompting: **Baseline (Stateless)** vs. **Chronos-Enriched**.
- Implement multimodal image + text parsing.

### Hours 08–10: Closed-Loop Outcome Feedback & Governance Writeback
- Implement `record_decision()` and `record_outcome()` MCP endpoints.
- Connect post-action outcome writebacks to update asset state in Kùzu graph.
- Verify outcome persistence across sequential queries.

### Hours 10–12: Streamlit Operational Dashboard UI
- Build interactive Streamlit dashboard (`app.py`).
- Implement live telemetry anomaly trigger, optical inspection photo viewer, baseline vs. Chronos reasoning comparison panel, and auditable evidence graph.

### Hours 12–14: System Integration & End-to-End Testing
- Connect Streamlit UI $\rightarrow$ Vertex AI / Gemini $\rightarrow$ Chronos MCP $\rightarrow$ BigQuery/GCS.
- Execute full reference event chain (09:10–09:40 Pump-07 anomaly).
- Fix cross-module data model alignment bugs.

### Hours 14–16: Benchmark Suite Development
- Develop 20 controlled temporal scenarios (`benchmark_scenarios.json`).
- Write automated benchmark runner (`run_benchmark.py`).
- Implement metrics calculation: Accuracy, Stale-Context Errors, Grounding Score.

### Hours 17–18: Validation Execution & Metric Collection
- Execute `run_benchmark.py` across Baseline Gemini, Gemini + Raw History, and Gemini + Chronos.
- Generate comparative validation tables and chart artifacts.

---

## 3. Critical Final 3-Hour Buffer (Hours 21–24)

> **HARD RULE**: At Hour 21 (06:00 AM on Day 2), all feature development stops completely. No new code features may be introduced.

### Hours 21–22: Integration Freeze & Demo Safety Preparation
- Codebase lockdown; bug fixes only.
- Verify zero-network offline fallback mode (`demo_fallback_mock.py`).
- Verify all error handlers gracefully catch API timeout/rate limits.

### Hours 22–23: Presentation & PPT Finalization
- Embed actual benchmark charts and UI screenshots into PPT slides (`compressed_Chronos_HackSprint_Final.pptx`).
- Finalize judges Q&A answers sheet (`13_JUDGES_QA.md`).

### Hours 23–24: Rehearsal & Final Submission
- Conduct 3 dry-run presentations of the 3-minute judge demo.
- Verify Git repository cleanliness and push final submission tags.
