from src.hardware.controller import HardwareController

class ElectricalInterface:
    def __init__(self, config):
        self.controller = HardwareController(config)

    def get_system_state(self):
        return {
            "pressure_in": self.controller.get_pressure("inlet"),
            "pressure_out": self.controller.get_pressure("outlet"),
            "temp_exit": self.controller.get_temp("exit")
        }

    def trigger_bypass(self):
        self.controller.trigger_bypass()

    def set_intake(self, value):
        self.controller.set_intake_valve(value)
