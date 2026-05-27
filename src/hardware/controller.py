"""
CHTS-Advanced-Materials: Hardware Controller
Direct interaction layer for sensors and actuators.
"""

import logging

logger = logging.getLogger("CHTS-Hardware")

class HardwareController:
    def __init__(self, config):
        """Initializes hardware interfaces (GPIO, I2C, SPI, etc.) based on config."""
        self.config = config
        logger.info("Hardware Controller initialized and ready.")

    def get_pressure(self, port: str) -> float:
        """
        Reads pressure from the specified port.
        Replace the return value with actual hardware I/O calls.
        """
        # Example: Mocking return value for system testing
        logger.debug(f"Reading pressure from {port}")
        return 101.3 

    def get_temp(self, location: str) -> float:
        """
        Reads temperature from the specified location.
        Replace the return value with actual hardware I/O calls.
        """
        # Example: Mocking return value for system testing
        logger.debug(f"Reading temperature from {location}")
        return 25.0

    def trigger_bypass(self):
        """Activates the physical bypass valve solenoid."""
        # Logic for GPIO pin toggle goes here
        logger.info("Hardware: Physical bypass valve solenoid activated.")

    def set_intake_valve(self, value: int):
        """
        Sets the intake valve position (0-100%).
        Logic for PWM or Servo control goes here.
        """
        # Example: Input validation
        clamped_value = max(0, min(100, value))
        logger.info(f"Hardware: Intake valve set to {clamped_value}%.")
