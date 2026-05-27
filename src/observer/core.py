"""
CHTS-Advanced-Materials: AI Observer Core
The central intelligence loop for thermodynamic management and self-healing.
"""

import logging
from src.electrical.interface import ElectricalInterface
from src.observer.self_healing import SelfHealingManager

# Setup logger for the observer
logger = logging.getLogger("CHTS-Observer")

class AIObserver:
    def __init__(self, config):
        """Initializes the observer with hardware interface and healing capabilities."""
        self.config = config
        self.interface = ElectricalInterface(config)
        self.healer = SelfHealingManager(self.interface)
        logger.info("AI Observer initialized.")

    def run_cycle(self):
        """Main observation loop: Monitor -> Analyze -> Act."""
        # 1. Gather Telemetry
        telemetry = self.interface.get_system_state()
        
        # 2. Analyze for Fouling (Anomaly Detection)
        fouling_score = self.calculate_fouling(telemetry)
        limit = self.config.get('thresholds', {}).get('fouling_limit', 0.5)
        
        if fouling_score > limit:
            logger.warning(f"Anomaly detected! Fouling score: {fouling_score:.2f}")
            # Determine severity based on score magnitude
            severity = "HIGH" if fouling_score > (limit * 2) else "MEDIUM"
            self.healer.execute_recovery_sequence(severity=severity)
        
        # 3. Optimize Cascade Stages
        self.optimize_cascade(telemetry)

    def calculate_fouling(self, data) -> float:
        """Determines if heat exchanger fins require thermal shock."""
        # Delta Pressure (dP) serves as a proxy for blockage/fouling
        delta_p = data.get('pressure_in', 0) - data.get('pressure_out', 0)
        return max(0.0, delta_p * 0.1)

    def optimize_cascade(self, data):
        """Monitors Stage 5 Entropy Harvesting performance."""
        exit_temp = data.get('temp_exit', 0)
        stage_5_limit = self.config.get('thresholds', {}).get('stage_5_entropy', 30.0)
        
        if exit_temp > stage_5_limit:
            logger.info("Stage 5: Entropy harvesting threshold exceeded. Adjusting flow.")
            # Interface logic for Stage 5 would go here
