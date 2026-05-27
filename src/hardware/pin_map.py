"""
CHTS-Advanced-Materials: Hardware Pin Mapping
Centralized manifest for all physical wiring connections.
"""

# Mapping based on your CHTS-Alpha-Unit architecture
# Ensure this matches your physical PCB/Breadboard layout exactly.

# Sensors (Analog-to-Digital Converter Channels)
PINS = {
    "sensors": {
        "pressure_transducer": 0,    # ADC Channel 0
        "thermocouple_inlet": 1,     # ADC Channel 1
        "thermocouple_outlet": 2,    # ADC Channel 2
        "flow_meter": 3              # ADC Channel 3
    },
    
    # Actuators (Pulse Width Modulation Channels)
    "actuators": {
        "intake_valve": 17,          # GPIO 17 (PWM capable)
        "bypass_valve": 22           # GPIO 22 (PWM capable)
    },
    
    # Communication Protocols
    "i2c_bus": {
        "scl": 3,
        "sda": 2
    }
}

def get_pin(component_type, component_name):
    """Safely retrieve a pin assignment."""
    try:
        return PINS[component_type][component_name]
    except KeyError:
        raise ValueError(f"Pin configuration missing for: {component_type}.{component_name}")
