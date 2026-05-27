"""
CHTS-Advanced-Materials: Anomaly Detector Core
This module compares real-time sensor data against physical baselines 
to detect degradation (fouling) or system anomalies.
"""

from .definitions import ThermalConstants, OperationalLimits

class AnomalyDetector:
    def __init__(self, baseline_pressure: float, baseline_temp_delta: float):
        self.baseline_pressure = baseline_pressure
        self.baseline_temp_delta = baseline_temp_delta
        self.limits = OperationalLimits()
        self.constants = ThermalConstants()

    def check_for_fouling(self, current_pressure: float) -> bool:
        """
        Detects if fin clogging (fouling) has exceeded safe limits.
        """
        pressure_delta = current_pressure - self.baseline_pressure
        if pressure_delta > self.limits.MAX_PRESSURE_DROP_PA:
            return True # Trigger self-healing: Thermal Shock
        return False

    def assess_thermal_drift(self, current_temp_delta: float) -> str:
        """
        Assesses if the cascade efficiency is degrading.
        """
        # Logic: If delta T drops below 90% of baseline, system is underperforming
        if current_temp_delta < (self.baseline_temp_delta * 0.90):
            return "DEGRADED"
        return "NOMINAL"

    def safety_check(self, current_temp: float) -> bool:
        """
        Dead-man switch: Forces shutdown if temp exceeds hardware limits.
        """
        return current_temp > self.constants.SAFETY_THRESHOLD_TEMP
