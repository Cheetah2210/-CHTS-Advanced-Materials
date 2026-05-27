
# Software Validation: CHTS-Advanced-Materials

This document outlines the testing suite for the CHTS AI Observer. Before any code is merged into the `main` branch, it must pass the following validation tests to ensure the integrity of the physics models and the safety of the hardware actuators.

## 1. Testing Philosophy
The system follows a "Physics-in-the-Loop" testing philosophy. We do not just test code execution; we test **Thermodynamic Validity**. If the code suggests an action that violates the `physics_dictionary.md`, the test fails.

## 2. Test Suite Categories

| Test ID | Module | Purpose | Validation Metric |
| :--- | :--- | :--- | :--- |
| **VAL-01** | `core.py` | Detects false positives in fouling | $\Delta P$ threshold accuracy |
| **VAL-02** | `core.py` | Validates Dead-Man switch | Response time < 50ms |
| **VAL-03** | `self_healing.py` | Verify actuator command sequencing | Order of operations safety |
| **VAL-04** | `definitions.py` | Consistency check of constants | Values within physical bounds |

## 3. Execution Protocols

### Unit Testing
All logic modules must be tested using `pytest`.
```bash
# Example command to run the suite
pytest tests/test_observer.py --verbose
