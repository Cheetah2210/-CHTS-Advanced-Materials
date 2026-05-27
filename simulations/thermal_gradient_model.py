"""
CHTS-Advanced-Materials: Thermal Gradient Simulator
This module acts as the 'Digital Twin' to provide synthetic sensor data
for testing the AnomalyDetector and SelfHealer modules.
"""

import random

class CHTSSimulator:
    def __init__(self):
        self.pressure = 100.0  # Baseline Pa
        self.temp_delta = 25.0  # Baseline Delta T
        self.fouling_factor = 0.0

    def step(self):
        """
        Simulate one time step of the thermodynamic system.
        """
        # Simulate gradual fouling over time
        self.fouling_factor += 0.5
        current_pressure = self.pressure + self.fouling_factor + random.uniform(-1, 1)
        
        # Simulate thermal fluctuation
        current_temp_delta = self.temp_delta * (1 - (self.fouling_factor / 1000))
        
        return {
            "pressure": current_pressure,
            "temp_delta": current_temp_delta,
            "fouling": self.fouling_factor
        }

    def reset_fouling(self):
        """Simulates the effect of a 'Thermal Shock' cleaning."""
        self.fouling_factor = 0.0
