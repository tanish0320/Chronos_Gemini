# CHRONOS — 3-Minute Live Demo Script & Pitch Guide

**Document ID**: DEMO-11  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team**: GGs  
**Presenter**: Tanish Renuka Suragihalli  

---

## 1. 30-Second Elevator Pitch (The Hook)

> "Judges, stateless AI models are like brilliant doctors with short-term amnesia. When an industrial pump overheats, Gemini sees high temperature and prescribes more cooling. But it doesn't know that 10 minutes ago, cooling was already tried and failed because the bearing inside is physically tearing itself apart.
> 
> **CHRONOS** is the temporal memory and governance layer for Gemini. By giving Gemini time-indexed context across actions, outcomes, and SOP rules, Chronos prevents catastrophic plant failures, delivering auditable, grounded decisions in real-time."

---

## 2. Step-by-Step 3-Minute Live Demo Script

```text
TIME       DEMO STEP                                      ACTION / UI DISPLAY
00:00  ──► Step 1: The Alert                          ──► Show Streamlit Dashboard; Pump-07 red alert.
00:30  ──► Step 2: Baseline Gemini Failure             ──► Run Baseline Gemini (Recommends Coolant Boost).
01:00  ──► Step 3: Chronos MCP Context Retrieval      ──► Click "Analyze with Chronos"; show get_context() JSON.
01:30  ──► Step 4: Context-Enriched Gemini Reasoning  ──► Show Gemini output changing to "Bearing Replacement".
02:15  ──► Step 5: Grounded Evidence Trail             ──► Expand Audit Drawer (Image + SOP + ACT-881 + EVT-1104).
02:45  ──► Step 6: Closed-Loop Outcome Writeback       ──► Click "Approve & Record Outcome"; show graph update.
```

---

### Step 1: Real-Time Anomaly Alert (00:00 – 00:30)
- **Presenter**: *"Welcome judges. We are looking at our live Streamlit operational dashboard monitoring Processing Bay 4. At 09:40 AM, an anomaly alert triggers on Pump-07. Telemetry shows temperature elevated at 78°C and vibration at 3.8 mm/s. In addition, an optical inspection camera uploaded photo `IMG_20260926_0914.png` showing surface discoloration on the bearing housing."*

### Step 2: The Stateless AI Trap (00:30 – 01:00)
- **Presenter**: *"If we ask standard, stateless Gemini what to do, it sees 78°C temperature and surface discoloration. It recommends: 'Increase coolant flow rate to reduce pump temperature.' This sounds reasonable—until you check recent history."*

### Step 3: Chronos MCP Context Retrieval (01:00 – 01:30)
- **Presenter**: *"Now watch what happens when we enable CHRONOS. Gemini invokes the `get_context()` tool over the Model Context Protocol. Chronos queries BigQuery and our Kùzu temporal graph, returning this structured Context Package. 
Notice what Chronos revealed: 10 minutes ago at 09:30, action `ACT-881` WAS executed—coolant flow was increased by 20%. The outcome? Temperature dropped 3°C, but vibration remained dangerously high at 3.8 mm/s!"*

### Step 4: Gemini + Chronos Context-Enriched Decision (01:30 – 02:15)
- **Presenter**: *" armed with this temporal context, Gemini updates its reasoning completely. Instead of repeating the failed coolant boost, Gemini recommends: 'Schedule a controlled shutdown and execute bearing replacement within 6 hours.' It also cites past event `EVT-2025-1104`, where an identical vibration signature resulted in catastrophic pump seizure."*

### Step 5: Grounded Evidence Trail & Governance (02:15 – 02:45)
- **Presenter**: *"Crucially, this is not a black-box answer. We click on the Evidence Provenance tab. Chronos produces an auditable evidence quad linking the recommendation to telemetry timestamps, image `IMG_20260926_0914`, failed action `ACT-881`, and Section 4.2 of our plant SOP manual."*

### Step 6: Closed-Loop Outcome Writeback (02:45 – 03:00)
- **Presenter**: *"Finally, our plant engineer approves the bearing replacement. We click 'Approve & Execute'. Gemini calls the `record_outcome()` MCP tool, writing the decision and subsequent normal sensor state back into Chronos' graph. Chronos has remembered, learned, and governed. Thank you!"*

---

## 3. Demo Visual Checklist & Backup Assets

- Streamlit UI running locally at `http://localhost:8501`.
- Secondary terminal tab open with CLI fallback script (`python src/demo_fallback_mock.py`).
- Screenshots of UI cached in `docs/diagrams/` in case screen sharing fails.
