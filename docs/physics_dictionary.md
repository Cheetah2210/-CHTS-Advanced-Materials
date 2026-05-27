
# Physics Dictionary: CHTS-Advanced-Materials

This document standardizes the terminology for the Cascading Hybrid Thermal Scavenger (CHTS) project. All hardware specifications, AI observer code, and simulation models must adhere to these definitions.

## 1. Thermodynamic Fundamentals

| Term | Definition |
| :--- | :--- |
| **Exergy (Ex)** | The maximum useful work extractable as a system reaches equilibrium. Primary metric for efficiency. |
| **Pinch Point ($\Delta T_{min}$)** | The minimum temperature difference between exhaust and working fluid. A critical heat exchanger constraint. |
| **Thermal Inertia** | The resistance to temperature change, managed here by **Salt-Hydrate Phase Change Materials (PCMs)**. |

---

## 2. Materials & Scavenging Metrics

* **Fouling:** The accumulation of particulates/soot on surfaces, leading to increased thermal resistance and pressure drop ($\Delta P$).
* **Phase Change Material (PCM):** A substance that absorbs/releases energy during phase transition to provide thermal buffering.
* **Thermal Conductivity ($k$):** The measure of a material's ability to conduct heat. High-$k$ carbon-composite structures are essential for maximum heat flux.
* **Nusselt Number ($Nu$):** The ratio of convective to conductive heat transfer at a boundary. Higher $Nu$ values represent more efficient heat removal.

---

## 3. AI & Observer Logic

* **Digital Twin:** A real-time virtual model of the CHTS system used as a baseline to predict "healthy" operational parameters.
* **Residual Analysis:** The mathematical comparison of real-world sensor data against Digital Twin predictions to isolate anomalies.
* **Dead-Man Switch:** A hard-coded safety routine that forces the scavenger into a "Safe State" (full exhaust bypass) if critical failures are detected.

---

## 4. System Variables

* **$\Delta P$ (Pressure Drop):** The loss of static pressure as exhaust passes through the scavenger. Used to detect **fouling**.
* **$\dot{m}$ (Mass Flow Rate):** The speed of the exhaust through the cascade (kg/s).
* **$\alpha$ (Phase State):** The melt fraction of the salt hydrate (0 = Solid, 1 = Liquid), indicating available thermal storage capacity.

---

### Usage Guidelines

1. **Consistency:** All variables defined in `src/observer/definitions.py` must align with these terms.
2. **Updates:** New physical variables must be added to this dictionary via Pull Request before implementation in the code to maintain repository integrity.
