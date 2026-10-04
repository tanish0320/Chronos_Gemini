# CHRONOS — Master Hackathon Submission Package

**Project Title**: CHRONOS — Temporal Memory & Governance Context Layer for Gemini AI  
**Hackathon**: MAHE HackSprint 24-Hour Hackathon (October 17–18, 2026)  
**Track**: PS42 — Multimodal AI Systems using Google Gemini & Google Cloud  
**Team Name**: GGs  
**Author & Team Lead**: Tanish Renuka Suragihalli  
**GitHub Repository**: https://github.com/tanish0320/Chronos_Gemini  

---

## 1. Problem Statement & Operational Challenge

Modern industrial plants generate massive, fragmented streams of multimodal data (IoT sensor telemetry, thermal/optical photos, SOP manuals, operator logs). Current stateless multimodal AI systems evaluate data snapshots in isolation. Lacking memory of past decisions, actions taken, and observed outcomes, they suffer from:
1. **Symptomatic Over-Reaction**: Repeatedly recommending failed actions (e.g., continually boosting coolant for a pump whose internal bearing is physically failing).
2. **Stale-Context Blindness**: Missing trend deltas and post-action sensor responses.
3. **Black-Box Decisions**: Generating ungrounded text without auditable linkages to telemetry or SOP governing rules.

---

## 2. Core Solution & What Chronos Is

**CHRONOS** is a temporal memory, context, and governance layer for Gemini-powered multimodal AI systems. 

$$\text{Observe (GCP)} \longrightarrow \text{Remember (Chronos)} \longrightarrow \text{Reason (Gemini)} \longrightarrow \text{Decide} \longrightarrow \text{Act} \longrightarrow \text{Learn}$$

- **Gemini** handles multimodal perception, visual interpretation, and natural language reasoning.
- **Chronos** maintains the persistent time-indexed property graph, SOP policy rules, and closed-loop outcome memory.
- **Google Cloud** provides scalable data ingestion (BigQuery) and object storage (Cloud Storage).

---

## 3. Architecture & Tech Stack

- **Reasoning**: Google Gemini 2.0 Flash / 1.5 Pro via Vertex AI SDK.
- **Enterprise Data Layer**: Google Cloud Storage (images/SOPs) & Google BigQuery (telemetry streams).
- **Temporal Context Engine**: Kùzu Embedded Property Graph DB & SQLite Policy Store.
- **Protocol Bridge**: Model Context Protocol (MCP) JSON-RPC 2.0.
- **User Interface**: Streamlit Operational Dashboard.

---

## 4. Minimum Viable Product (MVP) Scope

During the 24-hour hackathon, we deliver a functional vertical slice for industrial **Pump-07**:
1. Multimodal telemetry ingestion & GCS optical photo loading (`IMG_20260926_0914.png`).
2. `get_context()` MCP endpoint returning structured JSON Context Packages containing past failed action `ACT-881` and precedent `EVT-2025-1104`.
3. Gemini reasoning shift: Baseline (recommending failed coolant boost) vs. Gemini + Chronos (recommending bearing replacement).
4. Grounded audit quad linking decision $\rightarrow$ image $\rightarrow$ telemetry $\rightarrow$ SOP Section 4.2.
5. Closed-loop outcome writeback via `record_outcome()`.
6. Empirical benchmark evaluation across 20 temporal scenarios.

---

## 5. Google Cloud & Gemini Integration

Google Cloud Storage stores high-resolution thermal inspection images and SOP manuals. BigQuery handles high-throughput time-series sensor streams. Vertex AI hosts Gemini 2.0 models. Chronos queries GCP data layers, builds a structured `< 800 token` Context Package, and feeds it to Gemini over MCP.

---

## 6. Model Context Protocol (MCP) Interface

Chronos implements four core tools:
- `get_context(entity_id, time_window, query)` $\rightarrow$ Returns Context Package JSON.
- `get_policy(entity_id, proposed_action, metrics)` $\rightarrow$ Verifies SOP safety constraints.
- `record_decision(asset_id, action, evidence_ids, confidence)` $\rightarrow$ Persists recommendation.
- `record_outcome(decision_id, action_executed, telemetry_delta, success)` $\rightarrow$ Updates temporal graph.

---

## 7. Empirical Validation Strategy

We benchmark 20 controlled temporal scenarios across 3 configurations:
- **Config A**: Baseline Gemini (Stateless)
- **Config B**: Gemini + Raw History (Unstructured SQL Dump)
- **Config C**: Gemini + Chronos Context Package

**Target Benchmark Results**:
- Decision Accuracy: Baseline ($40\%$) vs. Chronos ($\mathbf{95\%}$)
- Stale-Context Error Rate: Baseline ($55\%$) vs. Chronos ($\mathbf{0\%}$)
- Grounding Precision: Baseline ($15\%$) vs. Chronos ($\mathbf{100\%}$)

---

## 8. 24-Hour Build Plan & Task Allocation

- **Hours 00-06**: Architecture lock, BigQuery/GCS setup, Chronos Kùzu graph & MCP core.
- **Hours 06-12**: Vertex AI Gemini integration, SOP policy store, Streamlit UI prototype.
- **Hours 12-18**: End-to-end integration, 20-scenario benchmark suite development & execution.
- **Hours 18-21**: **[INTEGRATION FREEZE]** Code lockdown, bug fixes, offline fallback validation.
- **Hours 21-24**: PPT finalization, script rehearsal, master submission.

**Team Roles (4 Members)**:
- **Person 1**: Chronos Core & MCP Server Lead
- **Person 2**: Gemini & Vertex AI Multimodal Lead
- **Person 3**: Google Cloud & BigQuery Data Lead
- **Person 4**: UI Dashboard, Integration, Benchmark & Team Lead (Tanish Renuka Suragihalli)

---

## 9. Risk Assessment & Demo Safety Fallback

Includes zero-latency offline fallback engine (`demo_fallback_mock.py`). If cloud WiFi or GCP API fails during judging, Chronos deterministically serves pre-cached context packages and verified Gemini decision trails.

---

## 10. Live Demo Script & PPT Content Summary

- **3-Minute Demo Flow**: Real-Time Alert $\rightarrow$ Baseline Gemini Failure $\rightarrow$ Chronos MCP `get_context()` Retrieval $\rightarrow$ Context-Enriched Recommendation $\rightarrow$ Grounded Evidence Trail $\rightarrow$ Closed-Loop Writeback.
- **PPT Content (6 Slides)**: Slide 1 (Problem), Slide 2 (Solution), Slide 3 (Tech Stack & Architecture), Slide 4 (Data Flow), Slide 5 (Prototype Dashboard), Slide 6 (Differentiation & Validation).
