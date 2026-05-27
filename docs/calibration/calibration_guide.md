# CHTS Calibration Guide

This guide details the procedure for establishing the "Digital Twin" baseline for your specific CHTS unit. Calibration is required after every assembly or major component change (e.g., swapping carbon-composite fin modules).

## 1. Prerequisites
* **Clean State:** Ensure the heat exchanger is free of debris.
* **Stable Ambient:** Conduct calibration in an environment with stable temperature ($T_{amb}$) and pressure ($P_{atm}$).
* **Instrumentation:** All sensors must be pre-verified against known standards as defined in `/src/data_stream/`.

## 2. The 100-Hour Break-in Procedure
To ensure the system reaches steady-state efficiency, perform the following:

1. **Warm-up:** Run the system at 50% load for 2 hours to stabilize the salt-hydrate PCM.
2. **Data Logging:** During the 100-hour window, the system must log the following to `/validation/calibration_logs/baseline.csv`:
   - Inlet/Outlet temperatures ($T_{in}, T_{out}$)
   - Pressure drop ($\Delta P$)
   - Mass flow rate ($\dot{m}$)
3. **Statistical Baseline:** Use the data from the final 24 hours of the break-in to calculate your baseline mean and standard deviation for $\Delta P$ and $\Delta T$.

## 3. Digital Twin Initialization
Once the 100-hour run is complete, update the following parameters in your `/src/observer/core.py` initialization:

```python

# Example of setting your baseline after calibration
baseline_pressure = 105.2 # Average from baseline.csv
baseline_temp_delta = 28.5 # Average from baseline.csv

detector = AnomalyDetector(baseline_pressure, baseline_temp_delta)

---


