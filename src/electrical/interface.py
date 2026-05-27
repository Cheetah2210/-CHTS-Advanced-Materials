"""
CHTS-Advanced-Materials: Electrical Interface Layer
Maps physical sensor signals to normalized units.
"""

from .drivers import PressureSensor, ValveActuator

class HardwareController:
    def __init__(self, config):
        self.pressure_sensor = PressureSensor(pin=config['sensors']['pressure_transducer']['pin'])
        self.intake_valve = ValveActuator(pin=config['actuators']['intake_valve']['pin'])

    def get_pressure(self) -> float:
        """Returns normalized pressure in Pascals."""
        return self.pressure_sensor.read_pascal()

    def set_intake_valve(self, percentage: float):
        """Sets valve position 0-100%."""
        self.intake_valve.set_position(percentage)

    def pulse_flow(self, duration: int, intensity: str):
        """Hardware-specific pulsing routine for self-healing."""
        self.intake_valve.execute_pulse(duration, intensity)
