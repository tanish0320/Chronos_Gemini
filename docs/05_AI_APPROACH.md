# CHRONOS — AI Approach & Gemini Integration Strategy

**Document ID**: AI-05  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team**: GGs  
**Author**: Tanish Renuka Suragihalli  

---

## 1. Division of Intelligence: Gemini vs. Chronos

The fundamental design pillar of CHRONOS is a strict separation of concerns between **Perception & Reasoning** (Gemini) and **Temporal Context & Governance** (Chronos).

```text
┌─────────────────────────────────────────────────────────┐
│               GOOGLE GEMINI 2.0 / FLASH                 │
│         (Perception, Understanding & Reasoning)          │
│                                                         │
│ • Visual Inspection Image Anomaly Extraction           │
│ • Natural Language Understanding & SOP Parsing          │
│ • High-dimensional Pattern Correlation                  │
│ • Contextual Decision Synthesis & Recommendations       │
└───────────────────────────┬─────────────────────────────┘
                            │
              MCP Context Call / Response
                            │
┌───────────────────────────┴─────────────────────────────┐
│                      CHRONOS LAYER                      │
│        (Temporal Context, Memory & Governance)          │
│                                                         │
│ • Time-indexed Asset State Tracking                     │
│ • Action & Intervention History (ACT-881)               │
│ • Closed-Loop Outcome Memory (OUT-881)                  │
│ • Historical Failure Precedent Indexing (EVT-2025-1104) │
│ • SOP Safety Policy Verification (POL-SOP-PUMP07)      │
│ • Verifiable Audit & Provenance Trail                   │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Detailed Responsibility Breakdown

### 2.1 Gemini Multimodal AI Responsibilities
1. **Multimodal Visual Interpretation**: Analyzing optical inspection photographs (`IMG_20260926_0914.png`) and thermal diagnostics to extract physical features (surface discoloration, heat localization, micro-cracks).
2. **Natural Language Document Understanding**: Reading PDF manuals (`MM-PUMP-07.pdf`) to extract rule definitions and operating constraints.
3. **Cross-Modal Reasoning**: Synthesizing visual observations with sensor telemetry deltas provided in the Chronos Context Package.
4. **Actionable Decision Generation**: Formulating human-readable operational recommendations, risk assessments, and step-by-step diagnostic reasoning.

### 2.2 Chronos Temporal Layer Responsibilities
1. **Temporal Context Retrieval**: Querying BigQuery and Kùzu to retrieve exact moving averages, sensor deltas, and state transitions across customizable time windows.
2. **Intervention & Outcome Memory**: Fetching previous actions taken on the asset and their observed effectiveness.
3. **Historical Event Retrieval**: Searching the temporal graph for past events sharing identical temporal signatures.
4. **Policy Governance Check**: Verifying proposed decisions against deterministic plant SOP thresholds.
5. **Auditable Provenance Linkage**: Structuring all cited data points into an immutable evidence graph.

---

## 3. Why Gemini + Chronos, Not Chronos as an LLM

A critical architectural decision in CHRONOS is **never attempting to make Chronos itself a generative language model**.

| Architectural Approach | Pros | Cons | Decision |
| :--- | :--- | :--- | :--- |
| **Approach A**: Fine-tune a custom LLM to store temporal history in model weights. | Single model artifact. | Extremely expensive; catastrophic forgetting; high hallucination rate on precise temporal data; non-auditable. | **REJECTED** |
| **Approach B**: Pure Gemini with raw data dump into prompt. | Easy implementation. | High latency & token cost; LLM easily confused by noise; no outcome feedback loop; unstructured explanations. | **REJECTED** |
| **Approach C**: **Gemini (Reasoning) + Chronos MCP (Context & Memory)**. | Deterministic temporal tracking; token-efficient; 100% auditable evidence; zero model retraining required; instant graph writeback. | Requires clean MCP interface definition. | **SELECTED** |

---

## 4. Grounded Explainability Mechanism

In CHRONOS, explainability is **structural, deterministic, and verifiable**, rather than a post-hoc LLM text summary.

Every decision rendered by Gemini must explicitly reference a 4-part **Grounded Evidence Quad**:

$$\text{Decision} \Longleftrightarrow \left\{ \text{Telemetry Timestamp}, \text{Visual Image ID}, \text{Past Action/Outcome ID}, \text{SOP Clause ID} \right\}$$

### Example Grounded Decision Output Structure:

```markdown
### OPERATIONAL DECISION REPORT
**Asset ID**: PUMP-07  
**Risk Level**: HIGH (Imminent Mechanical Failure Risk: 96%)  
**Recommended Action**: Initiate controlled shutdown and perform bearing replacement within 6 hours.

#### GROUNDED EVIDENCE TRAIL:
1. **Telemetry Anomaly**: Vibration elevated by +1.8 mm/s over baseline (3.8 mm/s at 09:40:00Z).
2. **Visual Evidence**: Inspection photo `IMG_20260926_0914.png` displays surface discoloration on bearing outer race.
3. **Past Action Failure**: Coolant flow boost (`ACT-881` at 09:30:00Z) reduced temp by 3°C but produced ZERO reduction in vibration.
4. **Historical Precedent**: Event `EVT-2025-1104` exhibited identical post-cooling vibration persistence, resulting in catastrophic seizure.
5. **SOP Governance**: `MM-PUMP-07 Section 4.2` explicitly mandates physical bearing inspection when vibration $> 3.5\text{ mm/s}$ persists post-coolant adjustment.
```

---

## 5. Gemini Prompt & Context Integration Structure

When Gemini is invoked via Vertex AI, the system prompt is assembled using the following strict template:

```python
GEMINI_SYSTEM_PROMPT = """
You are an expert Industrial Reliability AI Assistant powered by Google Gemini and CHRONOS.

Your task is to analyze the current industrial anomaly using the structured CHRONOS CONTEXT PACKAGE provided below.

CRITICAL REASONING RULES:
1. You MUST check past interventions in `recent_interventions`. If a past action (e.g. coolant boost) was already attempted and failed to resolve the core anomaly metric (vibration), DO NOT recommend repeating that action!
2. You MUST cite specific evidence IDs (Image IDs, Action IDs, Historical Event IDs, SOP Section IDs) for every diagnostic claim.
3. You MUST verify that your recommendation complies with the governing policy in `governing_policies`.

--- BEGIN CHRONOS CONTEXT PACKAGE ---
{context_package_json}
--- END CHRONOS CONTEXT PACKAGE ---

Now analyze the visual input and Chronos context package to provide your grounded operational recommendation.
"""
```
