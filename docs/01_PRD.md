# CHRONOS — Product Requirement Document (PRD)

**Document ID**: PRD-01  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team**: GGs  
**Author**: Tanish Renuka Suragihalli  

---

## 1. Product Identification & Overview

- **Product Name**: CHRONOS
- **One-Line Description**: Chronos is a temporal memory, context, and decision-governance layer for Gemini-powered multimodal AI systems in complex, dynamic environments.
- **Tagline**: *"Gemini understands multimodal information; Chronos allows it to understand that information in context — across time, decisions, actions, and outcomes."*

---

## 2. Problem Statement

### 2.1 Formal Problem Statement
Modern industrial operational environments generate massive, highly fragmented streams of real-time heterogeneous data, including IoT sensor telemetry, thermal/visual inspection photography, operator notes, maintenance logs, and Standard Operating Procedure (SOP) manuals. 

Current state-of-the-art AI systems powered by large multimodal models (LMMs) analyze incoming snapshots in isolation. Because they lack persistent, time-indexed historical context, past decision memory, and action outcome tracking, these systems suffer from critical operational vulnerabilities:
1. **Symptomatic Over-Reaction**: Treating recurring mechanical anomalies as novel events, leading to repeated, ineffective interventions (e.g., continually boosting coolant flow for a failing bearing).
2. **Stale-Context Blindness**: Failing to track whether a recent intervention successfully resolved an underlying anomaly or merely masked a secondary metric.
3. **Black-Box Decisioning**: Delivering unstructured text recommendations without auditable linkages to raw sensor data, inspection photos, or SOP governing clauses.

### 2.2 The Problem in Our Own Words
Stateless AI is like a brilliant doctor who suffers from severe short-term amnesia. Every time the doctor examines a patient (such as an industrial pump), they see the current elevated temperature and prescribe ice water. They have no memory that 10 minutes ago, another doctor already gave ice water, the temperature dropped slightly, but the patient's heart rate (vibration) remained dangerously high—indicating a fatal block. 

Chronos gives Gemini its long-term medical history, previous treatment records, and diagnostic SOPs so it can prescribe the correct life-saving surgery (bearing replacement) instead of repeating failed remedies.

---

## 3. Target Users & Persona Profile

| Persona | Role | Key Pain Points | Primary Goal with Chronos |
| :--- | :--- | :--- | :--- |
| **Plant Reliability Engineer** (e.g., Mark) | Operational Lead for Industrial Assets | Receives dozens of false alarms daily; AI suggestions lack context; cannot trace why AI advised specific actions. | Needs grounded, auditable recommendations backed by past intervention outcomes and SOP clauses. |
| **Maintenance Specialist** (e.g., Sarah) | Field Technician executing physical repairs | Dislikes vague AI suggestions; needs exact visual and historical evidence before shutting down critical pumps. | Requires step-by-step diagnostic reasoning linking historical failure signatures to current sensor deltas. |
| **AI Systems Architect** (e.g., Alex) | Technical Lead integrating LLMs into enterprise IoT | RAG vector databases only retrieve semantic text fragments and miss temporal state progressions and action feedback loops. | Needs an open Model Context Protocol (MCP) server that feeds structured temporal context packages directly into Gemini. |

---

## 4. User Journey & Core Use Case

### 4.1 Primary Use Case: Industrial Pump-07 Predictive Diagnostics
The primary demonstration domain is an industrial processing plant operating high-pressure centrifugal pumps (reference asset: **Pump-07**).

```text
[09:10 AM - Telemetry Alert] ──► Temperature: 78°C (Elevated) | Vibration: 3.8 mm/s (High Anomaly)
                                       │
                                       ▼
[09:14 AM - Multimodal Capture] ─► Thermal image IMG_20260926_0914.png uploaded to GCS
                                       │
                                       ▼
[09:18 AM - Baseline Gemini] ────► Sees high temp & discoloration -> Recommends: "Increase cooling flow rate"
                                       │
                                       ▼
[09:20 AM - CHRONOS Intervenes] ─► Chronos queries Kùzu Graph & BigQuery:
                                   • Past Action (ACT-881 at 09:30): Coolant flow WAS increased.
                                   • Outcome: Temp dropped 3°C, but vibration remained elevated at 3.8 mm/s.
                                   • Historical Precedent (EVT-2025-1104): Identical pattern resulted in catastrophic bearing failure.
                                   • SOP Governance (MM-PUMP-07 Sec 4.2): Vibration > 3.5 mm/s post-cooling mandates physical bearing inspection.
                                       │
                                       ▼
[09:25 AM - Context-Enriched] ──► Gemini + Chronos Recommends: "Schedule controlled shutdown & bearing replacement within 6h."
```

---

## 5. Minimum Viable Product (MVP) Scope (24-Hour Hackathon)

The 24-hour MVP delivers a complete, functional vertical slice demonstrating end-to-end temporal intelligence:

1. **Multimodal Data Ingestion Layer**:
   - Time-series IoT sensor data for Pump-07 ingested into BigQuery / Local SQLite data structures.
   - Optical/thermal inspection images (`IMG_20260926_0914.png`) stored in Google Cloud Storage (GCS).
   - Maintenance manual SOP (`MM-PUMP-07.pdf`) indexed for rule extraction.
2. **Chronos MCP Context Server**:
   - Implementation of `get_context()` returning a structured `Context Package` JSON.
   - Temporal graph linking asset states, previous actions (`ACT-881`), outcomes, and historical events (`EVT-2025-1104`).
3. **Gemini 2.0 Multimodal Reasoning Engine**:
   - Integration via Vertex AI SDK / Gemini API.
   - Dual-mode reasoning: Baseline (Stateless) vs. Chronos-Enriched.
4. **Closed-Loop Outcome Feedback**:
   - Exposing `record_decision()` and `record_outcome()` tools to write back decisions and human operator actions to Chronos state.
5. **Operational Demo Dashboard**:
   - Streamlit visualizer demonstrating real-time telemetry, visual inspection image, Gemini prompt context comparison, and grounded audit trail.
6. **Empirical Validation Suite**:
   - Benchmark script evaluating 20 temporal scenarios across baseline vs. Chronos context enrichment.

---

## 6. Explicit Non-Goals for 24-Hour MVP

- **No Custom Fine-Tuning**: We do not retrain Gemini foundational weights.
- **No Physical Actuator Control**: Recommendations are human-in-the-loop only; no direct PLC/SCADA signal overrides.
- **No Multi-Site Kubernetes Deployment**: Cloud Run / Local microservices architecture is prioritized over complex K8s clusters.
- **No Unlimited Historical Time-Travel**: Temporal reconstruction is scoped to Pump-07 telemetry and event history.

---

## 7. Success Criteria

| Category | Metric / Target | Verification Method |
| :--- | :--- | :--- |
| **Functional** | 100% successful execution of 09:10–09:40 Pump-07 reference event chain. | End-to-end integration test execution. |
| **Explainability** | 100% of generated recommendations cite empirical sensor IDs, image IDs, and SOP clauses. | Automated evidence audit parser. |
| **Temporal Accuracy** | $\ge 90\%$ decision accuracy on 20 temporal benchmark scenarios vs $< 45\%$ for baseline Gemini. | Benchmark evaluation runner script. |
| **System Latency** | `get_context()` MCP query response latency $< 250\text{ ms}$. | Performance profiling logs. |

---

## 8. Future Scope & Roadmap

- **Phase 2 (Post-Hackathon)**: Multi-asset cross-site temporal graph mapping over 10,000 enterprise industrial nodes.
- **Phase 3**: Automated CMMS integration (SAP Plant Maintenance / IBM Maximo API sync).
- **Phase 4**: Real-time video stream ingestion with continuous temporal optical flow analysis.
