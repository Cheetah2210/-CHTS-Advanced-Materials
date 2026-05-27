# Safety Standards: CHTS-Advanced-Materials

Safety is the highest priority for the Cascading Hybrid Thermal Scavenger. Because this system interacts with high-temperature exhaust and high-pressure differentials, all hardware builds and software modifications must adhere to these safety protocols.

## 1. Safety Philosophy: "Safe State" by Default
The CHTS is designed on a **fail-safe principle**. If power is lost, the AI Observer crashes, or a critical sensor fails, the hardware is configured to default to a "Safe State":
* **Intake Valves:** Mechanically biased to the "Closed" position (via spring-return actuators).
* **Bypass Channels:** Mechanically biased to the "Open" position, ensuring exhaust gas can vent safely without passing through the scavenger matrix.

## 2. Risk Mitigation Categories

| Hazard Type | Mitigation Strategy | AI Observer Role |
| :--- | :--- | :--- |
| **Thermal Overload** | Thermal expansion joints & bypass routing | $T_{abs}$ monitoring + Auto-throttle |
| **Structural Failure** | Carbon-composite fatigue analysis | Vibration/Acoustic profile monitoring |
| **PCM Contamination** | Hermetic containment protocols | Salt conductivity sensing |
| **High Pressure** | Pressure relief valves (PRV) | $\Delta P$ limit monitoring |

---

## 3. Mandatory Safety Documentation
Every build must include a signed-off version of the following before live-testing:
1. **Failure Mode Analysis:** (Refer to `/docs/failure_mode_analysis.md`) — Assessment of all points of failure.
2. **Emergency Protocol:** A physical "E-Stop" button must be accessible and verified to interrupt the power supply to all actuators.
3. **Operational Logs:** All "Safe State" triggers must be logged to the `/validation/calibration_logs/` directory for post-incident review.

## 4. Hardware Safety Compliance
* **Component Certification:** All pressure vessels and valve seals must be rated for at least $1.5\times$ the maximum expected operating temperature/pressure.
* **Material Integrity:** Any carbon-composite component exhibiting structural fraying or delamination must be decommissioned immediately.

---

### How to contribute safely
If you are developing a new feature for the `/src/` directory, you must run your logic against the `SafetyValidationTest` suite in `/tests/`. **No code that interacts with physical actuators may be merged without a passing safety validation score.**

*See /docs/failure_mode_analysis.md for detailed breakdown of system hazards.*
