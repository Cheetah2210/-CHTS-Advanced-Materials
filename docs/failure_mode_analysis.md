
# Failure Mode Analysis: CHTS-Advanced-Materials

This document outlines the potential failure modes of the Cascading Hybrid Thermal Scavenger (CHTS) and defines the required AI Observer response for each to ensure system safety and material integrity.

## 1. Failure Mode Identification Matrix

| Failure Mode | Root Cause | Severity | AI Observer Response |
| :--- | :--- | :--- | :--- |
| **Thermal Runaway** | Cooling system failure or external heat spike | Critical | Trigger emergency bypass + Full shutdown |
| **Fouling/Clogging** | Particulate buildup on carbon fins | Medium | Execute `SelfHealer.execute_thermal_shock()` |
| **PCM Leakage** | Structural breach of salt-hydrate container | High | Trigger isolation of stage + Warning alert |
| **Sensor Drift** | Calibration degradation over time | Low | Flag for recalibration + Use secondary sensor logic |
| **Actuator Seizure** | Mechanical valve failure | High | Halt automated flow control + Manual override prompt |

---

## 2. Risk Mitigation Protocols

### Thermal Runaway Protocol
If the internal temperature exceeds the `SAFETY_THRESHOLD_TEMP` defined in `definitions.py`, the AI **must** trigger a hard-coded "Safe State." This is a mechanical failsafe; the exhaust intake must close and the bypass must open immediately, regardless of software status.

### Fouling Management
The system tracks the pressure delta ($\Delta P$). When $\Delta P > 120\%$ of baseline, the AI initiates the `thermal_shock` routine. If pressure does not normalize within 30 seconds of the shock, the system logs a "Hard Foul" and signals for manual physical inspection.

### Salt Hydrate Containment
Phase Change Materials (PCMs) are critical to thermal stability. Any detected spike in external salt conductivity or inconsistent thermal lag indicates a container breach. The AI must trigger the "Bypass Protocol" to prevent contamination of the primary exhaust stream and protect downstream hardware.

---

## 3. Dead-Man Switch Logic
The "Dead-Man Switch" operates on a heartbeat signal. If the `/src/observer/` process fails to send a `status_ok` signal to the hardware controller for more than 500ms, the system defaults to the "Safe State":
1. **Intake Valve:** Closed.
2. **Exhaust Bypass:** Fully Open.
3. **Power:** Sustained to telemetry/logging systems only.

---

*This document is the reference guide for all safety-critical code in `/src/observer/core.py` and `self_healing.py`.*
