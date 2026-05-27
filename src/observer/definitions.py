"""
CHTS-Advanced-Materials: Core Physical Definitions
This file standardizes the units and constants used by the AI Observer
and the Digital Twin, as defined in /docs/physics_dictionary.md.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class ThermalConstants:
    # Thermal Conductivity (W/mK) for carbon composite
    CARBON_COMPOSITE_K: float = 120.0 
    # Reference density for salt hydrate in kg/m^3
    SALT_HYDRATE_DENSITY: float = 1550.0
    # Minimum temperature threshold for safety (Celsius)
    SAFETY_THRESHOLD_TEMP: float = 85.0

@dataclass(frozen=True)
class OperationalLimits:
    # Max allowed Pressure Drop (Pa) before triggering "Fouling" alert
    MAX_PRESSURE_DROP_PA: float = 500.0
    # Minimum Nusselt Number threshold for efficiency tracking
    MIN_NUSSELT_NUMBER: float = 15.0
    # Sampling frequency for AI sensor ingestion (Hz)
    SENSOR_SAMPLE_RATE: float = 10.0

def calculate_nusselt(h, L, k):
    """
    Standard formula for Nusselt Number (Nu).
    h: convective heat transfer coefficient
    L: characteristic length
    k: thermal conductivity
    """
    return (h * L) / k
