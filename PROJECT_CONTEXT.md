# CHRONOS: Project Context & Architectural Single Source of Truth

> **Single Source of Truth**: Future coding agents and developers MUST read this document before making architectural or implementation decisions for the CHRONOS project.

---

## 1. PROJECT CONTEXT

### Hackathon Problem Statement
> *Build a scalable, multimodal AI system using Google Gemini AI and integrated Google Cloud tools such as Vertex AI, Cloud Storage, and BigQuery that can process real-time, fragmented data (text, images, and documents) and deliver accurate, context-aware, and explainable decisions in complex and dynamic environments.*

### Proposed Solution
**CHRONOS — Temporal Intelligence for Explainable Industrial AI**

### Target Domain
**Industrial Operations & Predictive Maintenance**

### Core Positioning Statement
> **Chronos is a temporal context and decision-governance layer for Gemini-powered multimodal AI.**

*(Note: Chronos MUST NOT be described or implemented merely as an "AI memory system" or generic chat context store.)*

---

## 2. THE PROBLEM

Industrial operational environments generate vast streams of real-time, fragmented, and heterogeneous information:
- Real-time sensor / IoT telemetry (temperature, vibration, pressure, rpm)
- Equipment images and visual inspection photographs
- Textual logs, maintenance manuals, Standard Operating Procedures (SOPs), and incident reports
- Historical maintenance records, past AI decisions, and previous operational actions taken by engineers

A standard stateless multimodal AI pipeline can analyze incoming telemetry or images in isolation, but lacks persistent context over time. In safety-critical industrial settings, understanding an isolated input is insufficient. The system must answer critical longitudinal questions:

- **What is happening now?** (Current state observation)
- **What happened previously?** (Temporal event history)
- **What changed?** (State deltas and anomaly trends)
- **What decisions were made before?** (Historical decision context)
- **What actions were taken?** (Intervention history)
- **Did those actions work?** (Outcome feedback evaluation)
- **What evidence supports the current decision?** (Auditable provenance)
- **What policies or operational constraints apply?** (Governance context)
- **How should the system respond to a changing environment?** (Adaptive decision-making)

Without persistent temporal context and decision history, AI recommendations risk being reactive, repetitive, or unexplainable.

---

## 3. CORE SOLUTION

CHRONOS addresses these challenges through a continuous closed-loop architecture:

$$\text{Observe} \longrightarrow \text{Remember} \longrightarrow \text{Reason} \longrightarrow \text{Decide} \longrightarrow \text{Act} \longrightarrow \text{Observe Again}$$

### High-Level System Architecture

```text
Real-Time Data
   │
   ├── Sensors / IoT
   ├── Images
   ├── Documents
   ├── Text / Logs
   └── Events
          │
          ▼
   Google Cloud Infrastructure
   ├── Cloud Storage (Unstructured / Multimodal artifacts)
   ├── BigQuery (Telemetry, historical logs & analytics)
   └── Vertex AI (Model hosting & pipeline infrastructure)
          │
          ▼
   Gemini Multimodal AI (Perception & Initial Analysis)
          │
          ▼
   CHRONOS Layer
   ├── Temporal Context (Time-indexed state tracking)
   ├── Event / Decision History (Past decisions & contexts)
   ├── Evidence & Provenance (Audit trails & data source links)
   ├── State Reconstruction (Historical snapshot reconstruction)
   ├── Agent Intent / Action History (Recorded interventions)
   └── Governance / Policy Context (Operational SOPs & rules)
          │
          ▼
   Context-Enriched Gemini Reasoning
          │
          ▼
   Explainable Decision
          │
          ▼
   Action / Recommendation
          │
          ▼
   Outcome Feedback
          │
          └──────────→ Chronos (State Update)
```

---

## 4. ROLE OF GEMINI

Google Gemini serves as the primary **multimodal reasoning engine**.

### Responsibilities
- **Visual Understanding**: Analyzing thermal captures, optical inspection photographs, and equipment diagnostic images.
- **Document Understanding**: Extracting domain rules, SOP guidelines, and maintenance specifications from PDF manuals and reports.
- **Text & Log Processing**: Parsing operator notes, system logs, and telemetry alerts.
- **Multimodal Correlation**: Cross-referencing visual anomalies (e.g., surface discoloration) with sensor data (e.g., vibration spikes).
- **Anomaly Interpretation & Decision Support**: Reasoning over retrieved evidence to synthesize actionable recommendations and human-readable explanations.

### Scope & Accuracy Expectations
*Gemini does not guarantee 100% accuracy or absolute autonomous reliability.* Instead, CHRONOS improves decision quality by supplying Gemini with precise temporal context, grounded historical evidence, and verification bounds.

---

## 5. ROLE OF CHRONOS

Chronos is the engine responsible for maintaining the evolving temporal state and governance model of the industrial environment.

### Core Conceptual Components

1. **Temporal Context**: Time-series indexing of what happened, when, and in what sequence.
2. **Decision History**: Audit log of past AI recommendations, confidence levels, and context present at decision time.
3. **Action History**: Log of human operator interventions, automated control adjustments, or physical maintenance actions executed.
4. **Evidence & Provenance**: Explicit linkages between decisions and underlying data sources (sensor timestamps, image IDs, SOP clause references).
5. **State Reconstruction**: Capability to reconstruct the exact system state and understanding at any point in historical time.
6. **Governance & Policy Context**: Active operational constraints, safety thresholds, and regulatory SOP requirements.
7. **Agent Intent & Coordination**: Tracking active multi-agent objectives and ongoing operational procedures to prevent conflicting actions.

### Full Traceability Chain
Chronos makes it possible to audit and reconstruct every decision along the following complete lineage:

$$\text{Decision} \longrightarrow \text{Evidence} \longrightarrow \text{Historical Context} \longrightarrow \text{Policy} \longrightarrow \text{Action} \longrightarrow \text{Outcome}$$

---

## 6. EXPLAINABLE AI

Explainability in CHRONOS is structural rather than generative. The system **does NOT** rely on ungrounded post-hoc LLM text explanations after a decision is rendered.

Instead, every explanation is deterministically grounded in recorded evidence, historical context, and policy constraints.

### Example Grounded Decision Breakdown

- **Decision**: Schedule bearing inspection for Pump-07 within 6 hours.
- **Evidence**:
  - Vibration telemetry increased by 32% above baseline over the past 45 minutes.
  - Bearing housing temperature increased by 11°C.
  - Inspection photograph `IMG_20260926_0914.png` displays surface discoloration on outer race.
  - Maintenance Manual (Doc ID `MM-PUMP-07`, Sec 4.2) identifies this joint thermal/vibration signature as impending bearing fatigue.
  - Historical Event `EVT-2025-1104`: Identical signature preceded bearing failure within 12 hours.
- **Previous Action**: Automated coolant flow increase initiated at 09:30.
- **Outcome**: Temperature reduced by 3°C, but vibration levels remained elevated at 32% above baseline.
- **Result**: Escalation to physical inspection recommendation.

> **Key Rule**: *Chronos provides an auditable evidence trail supporting a decision; it does not expose or claim to reproduce Gemini's private chain-of-thought.*

---

## 7. GOOGLE CLOUD INTEGRATION

The architecture leverages native Google Cloud services for scalability, durability, and AI orchestration:

| Component | Technology | Primary Function |
| :--- | :--- | :--- |
| **AI Infrastructure** | Google Cloud Vertex AI | Gemini API integration, model deployment, and agent orchestration pipelines. |
| **Reasoning Engine** | Google Gemini 1.5 / 2.0 / Flash | Multimodal processing, document layout analysis, and contextual synthesis. |
| **Unstructured Storage** | Google Cloud Storage (GCS) | Blob storage for equipment images, thermal scans, PDF manuals, and inspection docs. |
| **Structured Data & Analytics** | Google BigQuery | High-throughput storage and SQL querying of IoT sensor streams, event logs, and audit metrics. |
| **Context & Governance** | CHRONOS Layer | Custom temporal state graph, decision history engine, and policy enforcement module. |

*Note: All module interfaces MUST remain modular to permit seamless expansion and local developer testing.*

---

## 8. DEMO SCENARIO

The standard reference demonstration scenario is **Pump-07 Predictive Maintenance**.

### Scenario Profile: Pump-07 Diagnostics
- **Current Real-Time State**:
  - Temperature: Elevated (78°C vs 65°C baseline)
  - Vibration: 3.8 mm/s (Significantly above 2.0 mm/s normal threshold)
  - Pressure: Normal (4.2 bar)
  - Camera Capture: Visual anomaly detected on pump casing/bearing housing
- **Historical Temporal Context**:
  - 6 months prior: Similar vibration signature observed.
  - Historical outcome: Ignoring signature led to catastrophic bearing failure.
  - 10 minutes prior: Cooling valve action attempted (Action ID `ACT-881`).
  - Observed result: Temperature stabilized slightly, but vibration remained critical.
- **Integrated System Output**:
  - **Risk Assessment**: High risk of imminent mechanical bearing failure.
  - **Recommended Action**: Initiate controlled shutdown and schedule bearing replacement within 6 hours.
  - **Evidence-Grounded Explanation**: Clear time-indexed report citing sensor telemetry trends, visual proof, SOP clauses, previous failed intervention, and historical precedent.

---

## 9. EXAMPLE TEMPORAL EVENT CHAIN

```text
09:10 — Vibration anomaly detected (3.8 mm/s on Pump-07)
09:14 — High-resolution equipment camera capture triggered
09:18 — Gemini analyzes image, identifies surface discoloration / possible bearing anomaly
09:21 — Chronos retrieves similar historical failure pattern (EVT-2025-1104)
09:25 — Chronos consults SOP Document MM-PUMP-07 Sec 4.2
09:30 — Action executed: Cooling flow rate increased to 120%
09:35 — Sensor telemetry update: Temperature decreases by 3°C
09:36 — Sensor telemetry update: Vibration remains elevated at 3.8 mm/s
09:40 — Gemini + Chronos generate grounded decision: Recommend bearing inspection within 6h
```

---

## 10. DATA FLOW

```text
INGEST        ──► Sensors / IoT, Images, Documents, Text Logs, Events
                     │
                     ▼
STORE         ──► Cloud Storage (Files/Images) & BigQuery (Telemetry/Events)
                     │
                     ▼
UNDERSTAND    ──► Gemini / Vertex AI Multimodal Parsing
                     │
                     ▼
EXTRACT       ──► Observations, Entities, Anomalies, Key Features
                     │
                     ▼
CONTEXTUALIZE ──► Chronos Temporal State & History Query
                     │
                     ▼
REASON        ──► Gemini receives context-enriched prompt + grounded evidence
                     │
                     ▼
DECIDE        ──► Risk Assessment / Diagnosis / Actionable Recommendation
                     │
                     ▼
EXPLAIN       ──► Grounded Evidence Trail (Decision → Evidence → History → SOP)
                     │
                     ▼
FEEDBACK      ──► Action Execution & Outcome recorded back to Chronos timeline
```

---

## 11. WHAT MAKES THE PROJECT DIFFERENT

The core differentiation of CHRONOS lies in its three-pillar architectural synergy:

$$\text{Gemini (Multimodal Reasoning)} + \text{Chronos (Temporal Context \& Governance)} + \text{Google Cloud (Scalable AI Stack)}$$

### Key Distinctions
- **NOT a simple chatbot**: CHRONOS is an industrial operational decision pipeline.
- **NOT a generic RAG system**: Beyond vector search, CHRONOS manages time-indexed state, temporal delta trends, and action outcomes.
- **NOT an unstructured AI memory DB**: Chronos enforces operational SOP governance, evidence provenance, and state reconstruction.
- **NOT a static predictive-maintenance dashboard**: CHRONOS combines multimodal perception with reasoning and action-feedback loops.
- **NOT a Gemini wrapper**: Chronos acts as an independent decision-governance layer controlling how context is fed to and evaluated by Gemini.

---

## 12. DESIGN PRINCIPLES

1. **Evidence First**: All decisions MUST be grounded in verifiable telemetry, visual evidence, or documented SOP clauses.
2. **Temporal Awareness**: Current observations MUST always be interpreted in relation to preceding events and trend trajectories.
3. **Traceability**: Every output recommendation MUST offer an auditable lineage back to raw observations and rules.
4. **Separation of Concerns**: Gemini handles perception and reasoning; Chronos manages temporal state and governance; Google Cloud provides storage/compute infrastructure.
5. **Modularity**: Core components MUST communicate via clean interfaces, avoiding hard dependencies on specific model versions or rigid storage implementations.
6. **Scalability**: Design pipelines capable of handling high-frequency IoT data, thousands of documents, and concurrent multi-asset workflows.
7. **Human Oversight**: Recommendations MUST be actionable and reviewable by domain engineers rather than assuming dangerous autonomous control over critical infrastructure.
8. **No Unsupported Claims**: Do not claim guaranteed zero-error accuracy, perfect explainability, or unvalidated autonomous safety.

---

## 13. EVALUATION PLAN

To prove the value of CHRONOS, future evaluation will benchmark performance against a standard baseline:

- **Baseline System**: Gemini + Google Cloud (Stateless multimodal analysis without Chronos temporal context).
- **Proposed System**: Gemini + Google Cloud + **CHRONOS** (Temporal Context & Decision Governance).

### Target Evaluation Metrics
- **Contextual Decision Accuracy**: Correctness of diagnoses requiring historical temporal awareness.
- **Temporal Reasoning Accuracy**: Ability to recognize progression across sequential events.
- **Evidence Retrieval Quality**: Precision and recall of cited telemetry and SOP sources.
- **Decision Consistency**: Stability of recommendations under identical operational conditions over time.
- **Contradiction Rate**: Prevention of conflicting operational actions across consecutive steps.
- **Stale-Context Error Rate**: Frequency of decisions based on outdated environment states.
- **Explanation Grounding Score**: Percentage of output statements tied to empirical data vs hallucinated text.
- **System Latency & Token Efficiency**: Performance and cost metrics for context-enriched prompts.

---

## 14. FUTURE EXTENSIONS

- **Multi-Agent Industrial Operations**: Autonomous agent specialization for diagnostic, safety, and supply chain logistics.
- **Cross-Site Equipment Intelligence**: Aggregating temporal anomaly trends across multiple manufacturing facilities.
- **Continuous Learning from Outcomes**: Automatic calibration of decision weights based on long-term historical maintenance outcomes.
- **Autonomous Workflow Orchestration**: Integration with enterprise asset management (EAM/CMMS) tools like SAP/Maximo.
- **Richer Multimodal Temporal Graphs**: Graph-based representations of temporal and causal equipment relationships.
- **Human-in-the-Loop Approval Workflows**: Interactive dashboards for chief engineers to approve, modify, or reject AI recommendations.

---

## 15. IMPLEMENTATION STATUS

| Component / Module | Status | Description |
| :--- | :--- | :--- |
| **`PROJECT_CONTEXT.md`** | **Implemented** | Foundational architectural specification and single source of truth. |
| **Chronos Temporal Context Engine** | Planned | Core state graph, time-series event indexer, and state snapshot reconstructor. |
| **Gemini Vertex AI Integration** | Planned | Multimodal prompt synthesis, image/doc extraction, and reasoning pipelines. |
| **GCP Data Layer (GCS & BigQuery)** | Planned | Schema definitions for sensor telemetry ingestion and blob storage links. |
| **Pump-07 Demo Scenario Pipeline** | Planned | End-to-end integration test demonstrating the 09:10-09:40 temporal event chain. |
| **Evidence & Provenance Audit Visualizer**| Planned | UI / API reporting layer for grounded explainability reports. |

*(Note: As components transition from Planned to Prototype or Implemented, this table MUST be updated by the contributing agent.)*

---

## 16. IMPORTANT INSTRUCTIONS FOR FUTURE AI AGENTS

Future AI agents working on this codebase MUST adhere strictly to the following 10 directives:

1. **Read `PROJECT_CONTEXT.md` First**: Always read this file in full before proposing or executing architectural changes or substantial code additions.
2. **Inspect Existing Repository**: Check what files, schemas, and modules are actually implemented before writing new code.
3. **Reflect Real Codebase State**: Never claim an unwritten module is implemented. Keep Section 15 updated.
4. **Preserve Architectural Separation**: Maintain strict boundaries between Gemini (reasoning), Google Cloud (infrastructure), and Chronos (temporal governance).
5. **Do Not Dilute Chronos**: Do not reduce Chronos to a generic LLM chat memory or simple key-value store.
6. **Enforce Grounded Explainability**: Ensure all explanations cite recorded evidence, telemetry, images, or SOP clauses rather than LLM chain-of-thought text.
7. **Focus on Measurable Value**: Prefer concrete benchmark implementations and empirical demonstrations over unverified assertions.
8. **Follow Design Principles**: Adhere to all 8 principles outlined in Section 12.
9. **Update This Document on Major Changes**: If architectural decisions evolve, update `PROJECT_CONTEXT.md` immediately.
10. **Respect the Hackathon Problem Statement**: Maintain alignment with Google Cloud tools (Vertex AI, GCS, BigQuery) and Gemini multimodal capabilities.
