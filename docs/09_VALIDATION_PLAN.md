# CHRONOS — Empirical Validation & Benchmark Specification

**Document ID**: VAL-09  
**Project**: CHRONOS  
**Track**: MAHE HackSprint Track PS42  
**Team**: GGs  
**Author**: Tanish Renuka Suragihalli  

---

## 1. Validation Philosophy & Objective

To prove the empirical value of CHRONOS, we design a rigorous, reproducible benchmark suite comprising **20 controlled temporal scenarios** across industrial asset operations.

Rather than making unverified claims about accuracy, this benchmark compares three distinct AI system configurations:

1. **System A — Baseline Gemini (Stateless)**: Gemini receives current snapshot telemetry and inspection images without historical context or past action memory.
2. **System B — Gemini + Raw History (Unstructured Dump)**: Gemini receives current data plus a raw SQL dump of all historical sensor logs ($> 5000\text{ tokens}$).
3. **System C — Gemini + Chronos Context Package**: Gemini receives current data plus Chronos' structured, time-indexed `Context Package` ($< 800\text{ tokens}$).

---

## 2. Evaluation Metrics Definition

$$\text{Decision Accuracy (\%)} = \frac{\text{Correct Recommendations}}{\text{Total Scenarios (20)}} \times 100$$

$$\text{Stale-Context Error Rate (\%)} = \frac{\text{Recommendations Repeating a Failed Action}}{\text{Total Scenarios (20)}} \times 100$$

$$\text{Grounding Precision (\%)} = \frac{\text{Valid Cited Evidence IDs}}{\text{Total Claims Made}} \times 100$$

| Metric | Target (Baseline Gemini) | Target (Gemini + Raw History) | Target (Gemini + Chronos) |
| :--- | :--- | :--- | :--- |
| **Temporal Decision Accuracy** | $< 45\%$ | $60\% - 70\%$ | $\mathbf{\ge 90\%}$ |
| **Stale-Context Error Rate** | $> 50\%$ | $30\% - 40\%$ | $\mathbf{0\% - 5\%}$ |
| **Evidence Grounding Precision**| $< 20\%$ | $50\% - 65\%$ | $\mathbf{\ge 95\%}$ |
| **Average Prompt Token Count** | $\approx 450\text{ tokens}$ | $> 5,200\text{ tokens}$ | $\mathbf{\approx 780\text{ tokens}}$ |
| **Average Query Latency** | $1.2\text{ s}$ | $4.8\text{ s}$ | $\mathbf{1.4\text{ s}}$ |

---

## 3. Sample Benchmark Scenario Schemas (20 Total Scenarios)

### Scenario 01: Pump-07 Post-Cooling Vibration Persistence (Reference Scenario)
- **Current State**: Temp: 78°C, Vibration: 3.8 mm/s, Thermal Image: Hotspot present.
- **Previous Intervention**: Coolant flow boosted 10 mins ago (`ACT-881`).
- **Observed Outcome**: Temp dropped 3°C, Vibration unchanged at 3.8 mm/s (`OUT-881`).
- **Governing SOP**: `MM-PUMP-07 Sec 4.2` (Vibration $> 3.5\text{ mm/s}$ post-cooling mandates physical inspection).
- **Expected Decision**: `BEARING_INSPECTION_AND_REPLACEMENT`.
- **Baseline Failure Mode**: Baseline Gemini sees high temp and recommends increasing coolant flow (repeating failed `ACT-881`).

### Scenario 02: Turbine-03 Transient Thermal Spike (False Anomaly)
- **Current State**: Temp: 85°C (Spike), Vibration: 1.1 mm/s (Normal).
- **Previous Intervention**: Load shift executed 5 mins ago (`ACT-412`).
- **Observed Outcome**: Historical trend shows thermal spikes resolve within 15 mins post-load shift.
- **Governing SOP**: `MM-TURBINE-03 Sec 2.1`.
- **Expected Decision**: `MONITOR_AND_WAIT`.
- **Baseline Failure Mode**: Baseline Gemini orders emergency shutdown, causing unnecessary plant downtime.

---

## 4. Automated Benchmark Execution Script (`run_benchmark.py`)

The validation engine executes all 20 scenarios programmatically and computes the evaluation matrix:

```python
"""
CHRONOS Benchmark Evaluation Suite
Executes 20 controlled temporal scenarios across 3 configurations:
- Config A: Baseline Gemini (Stateless)
- Config B: Gemini + Raw History Dump
- Config C: Gemini + Chronos Context Package
"""

import json
import time
from typing import Dict, Any

class ChronosBenchmarkRunner:
    def __init__(self, scenarios_path: str):
        with open(scenarios_path, 'r') as f:
            self.scenarios = json.load(f)
            
    def evaluate_scenario(self, scenario: Dict[str, Any], config_type: str) -> Dict[str, Any]:
        start_time = time.time()
        
        if config_type == "BASELINE":
            prompt = self.build_baseline_prompt(scenario)
        elif config_type == "RAW_HISTORY":
            prompt = self.build_raw_history_prompt(scenario)
        elif config_type == "CHRONOS":
            prompt = self.build_chronos_prompt(scenario)
            
        # Execute Gemini API call (or mock runner)
        response = self.execute_gemini(prompt)
        latency = time.time() - start_time
        
        # Grade response against expected decision & evidence
        is_correct = scenario["expected_action"] in response["recommendation"]
        is_stale_error = scenario.get("failed_past_action") in response["recommendation"]
        grounding_score = self.calculate_grounding(response, scenario["required_evidence"])
        
        return {
            "scenario_id": scenario["id"],
            "config": config_type,
            "is_correct": is_correct,
            "is_stale_error": is_stale_error,
            "grounding_score": grounding_score,
            "token_count": len(prompt.split()),
            "latency_s": round(latency, 2)
        }

    def run_all(self):
        results = []
        for s in self.scenarios:
            for config in ["BASELINE", "RAW_HISTORY", "CHRONOS"]:
                res = self.evaluate_scenario(s, config)
                results.append(res)
        return self.summarize_results(results)
```
