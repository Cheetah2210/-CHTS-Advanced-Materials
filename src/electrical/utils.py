"""
CHTS-Advanced-Materials: Electrical Utility Module
Signal conditioning and filtering for noisy sensor data.
"""

from collections import deque

class MovingAverageFilter:
    """
    Smooths out high-frequency noise from sensors (e.g., pressure transducers).
    """
    def __init__(self, window_size: int = 10):
        self.buffer = deque(maxlen=window_size)

    def process(self, value: float) -> float:
        self.buffer.append(value)
        return sum(self.buffer) / len(self.buffer)

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Ensures sensor values stay within physical bounds."""
    return max(min_val, min(value, max_val))

def convert_adc_to_pascal(raw_adc: int, v_ref: float = 3.3, max_adc: int = 4095) -> float:
    """
    Standard conversion formula for analog pressure sensors.
    Example: Mapping 12-bit ADC range to pressure units.
    """
    voltage = (raw_adc / max_adc) * v_ref
    # Add sensor-specific sensitivity slope here
    pressure = voltage * 1000.0 
    return pressure
