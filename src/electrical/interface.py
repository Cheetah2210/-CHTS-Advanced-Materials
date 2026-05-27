"""
CHTS-Advanced-Materials: Electrical Interface
Acts as the Hardware Abstraction Layer (HAL) for the AI Observer.
"""

from src.hardware.controller import HardwareController

class ElectricalInterface:
    def __init__(self, config):
        """Initializes the connection to the hardware controller."""
        self.controller = HardwareController(config)

    def get_system_state(self):
        """
        Aggregates raw hardware data into a standardized telemetry dictionary.
        This is the source of truth for the AI Observer's loop.
        """
        return {
            "pressure_in": self.controller.get_pressure("inlet"),
            "pressure_out": self.controller.get_pressure("outlet"),
            "temp_exit": self.controller.get_temp("exit")
        }

    def trigger_bypass(self):
        """Standardized interface call to trigger hardware bypass."""
        self.controller.trigger_bypass()

    def set_intake(self, value: int):
        """Standardized interface call to modulate intake."""
        self.controller.set_intake_valve(value)
