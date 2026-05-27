```python
"""
CHTS-Advanced-Materials: Hardware Controller
Direct interaction layer for sensors and actuators.
"""

import logging
import random

logger = logging.getLogger("CHTS-Hardware")


class HardwareController:
    def __init__(self, config):
        self.config = config
        logger.info("Hardware Controller initialized.")

    def get_pressure(self, port: str) -> float:
        """
        Mock pressure telemetry.
        Replace with real sensor I/O.
        """
        logger.debug(f"Reading pressure from {port}")

        base = 101.3

        if port == "inlet":
            return base + random.uniform(2.0, 6.0)

        elif port == "outlet":
            return base + random.uniform(-1.0, 2.0)

        return base

    def get_temp(self, location: str) -> float:
        """
        Mock thermal telemetry.
        Replace with thermocouple/RTD reads.
        """
        logger.debug(f"Reading temperature from {location}")

        if location == "exit":
            return random.uniform(20.0, 45.0)

        return 25.0

    def trigger_bypass(self):
        logger.info(
            "Hardware: Bypass valve activated."
        )

    def set_intake_valve(self, value: int):
        """
        Sets intake valve position (0–100%).
        """
        clamped = max(0, min(100, value))

        logger.info(
            f"Hardware: Intake valve set to {clamped}%."
        )
```
