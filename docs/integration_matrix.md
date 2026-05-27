
# Integration Matrix: CHTS-Advanced-Materials

This matrix maps the physical hardware components to the AI Observer’s logic modules and sensors. It serves as the primary reference for both hardware engineers and software developers.

## 1. System Logic Mapping

| Physical Component | Sensor/Data Input | AI Logic Module | Remediation Routine |
| :--- | :--- | :--- | :--- |
| **Intake Valve** | Flow Velocity ($\dot{m}$) | `core.py` (Monitor) | `self_healing.execute_thermal_shock` |
| **Carbon Fin Array** | Pressure Drop ($\Delta P$) | `core.py` (Residual Analysis) | `self_healing.execute_thermal_shock` |
| **Salt Hydrate Module** | Temp Gradient ($\Delta T$) | `core.py` (Thermal Drift) | `self_healing.execute_thermal_bypass` |
| **Exhaust Channel** | Absolute Temp ($T_{abs}$) | `core.py` (Safety Check) | `self_healing.emergency_shutdown` |

---

## 2. Data Stream Integration

* **`src/data_stream/`**: This directory acts as the HAL (Hardware Abstraction Layer). It collects raw signals (voltage/current/ADC) from physical sensors and converts them into normalized physical units (e.g., Pa, kg/s, °C).
* **AI Ingestion**: The `AnomalyDetector` class (defined in `src/observer/core.py`) ignores the raw hardware signal and consumes only these normalized units, ensuring the AI logic remains sensor-agnostic.

---

## 3. Feedback Loop Architecture



1. **Sense:** Hardware sensors stream data to `/src/data_stream/`.
2. **Normalize:** Data is converted to standardized units (defined in `physics_dictionary.md`).
3. **Analyze:** The `AnomalyDetector` compares data against the `Digital Twin` baseline.
4. **Act:** If a deviation is detected, the `SelfHealer` triggers the corresponding physical actuator (Valve/Bypass).

---

## 4. Operational Requirements for Integration
* **Synchronicity:** All sensor sampling must occur at the frequency defined in `OperationalLimits.SENSOR_SAMPLE_RATE` (default 10Hz) to prevent phase-shifting in the residual analysis.
* **Isolation:** The `SelfHealer` must maintain an asynchronous bridge to the hardware controller to ensure that a blocking call in one stage does not freeze the entire system's observation cycle.

---

*This matrix is the primary tool for debugging system-wide performance. If a sensor reports "NOMINAL" but the physical output is "DEGRADED," check the mapping between the hardware component and the logic module to ensure calibration constants are aligned.*
