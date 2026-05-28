```python
"""
CHTS-Advanced-Materials: AI Observer Core

Central intelligence loop for:

- Telemetry acquisition
- Fouling detection
- Net-benefit analysis
- Self-healing response
- Cascade optimization
"""

import logging

from src.electrical.interface import ElectricalInterface
from src.observer.self_healing import SelfHealingManager


logger = logging.getLogger(
    "CHTS-Observer"
)


class AIObserver:

    def __init__(
        self,
        config
    ):

        self.config = config

        self.interface = (
            ElectricalInterface(
                config
            )
        )

        self.healer = (
            SelfHealingManager(
                self.interface
            )
        )

        self.logger = logger

        self.logger.info(
            "AI Observer initialized."
        )

    # ========================================================
    # Main Observer Cycle
    # ========================================================

    def run_cycle(self):
        """
        Monitor -> Analyze -> Act
        """

        telemetry = (
            self.interface
            .get_system_state()
        )

        self.logger.debug(
            f"Telemetry: {telemetry}"
        )

        # -----------------------------------
        # Fouling Analysis
        # -----------------------------------

        fouling_score = (
            self.calculate_fouling(
                telemetry
            )
        )

        fouling_limit = (
            self.config
            .get(
                "thresholds",
                {}
            )
            .get(
                "fouling_limit",
                0.5
            )
        )

        self.logger.info(
            f"Fouling score: "
            f"{fouling_score:.3f}"
        )

        if fouling_score > fouling_limit:

            severity = (
                "HIGH"
                if fouling_score >
                (fouling_limit * 2)
                else "MEDIUM"
            )

            self.logger.warning(
                f"Anomaly detected | "
                f"Score={fouling_score:.3f} | "
                f"Severity={severity}"
            )

            self.healer.execute_recovery_sequence(
                severity
            )

        # -----------------------------------
        # Net Benefit Analysis
        # -----------------------------------

        active_loads = float(
            telemetry.get(
                "active_loads",
                0.0
            )
        )

        net_benefit = (
            self.calculate_net_benefit(
                telemetry,
                active_loads
            )
        )

        self.logger.info(
            f"Net benefit: "
            f"{net_benefit:.3f}"
        )

        # Optional future stage kill logic
        if net_benefit < 0:

            self.logger.warning(
                "Negative net benefit "
                "detected."
            )

        # -----------------------------------
        # Cascade Optimization
        # -----------------------------------

        self.optimize_cascade(
            telemetry
        )

    # ========================================================
    # Fouling Detection
    # ========================================================

    def calculate_fouling(
        self,
        data: dict
    ) -> float:
        """
        Fouling proxy using pressure drop.
        """

        delta_p = (
            data.get(
                "pressure_in",
                0.0
            )
            -
            data.get(
                "pressure_out",
                0.0
            )
        )

        score = max(
            0.0,
            delta_p * 0.1
        )

        return score

    # ========================================================
    # Net Benefit Accounting
    # ========================================================

    def calculate_net_benefit(
        self,
        data: dict,
        active_loads: float
    ) -> float:
        """
        Empirical Net Benefit calculation.

        Positive:
            Recovery exceeds cost

        Negative:
            Stage may not justify operation
        """

        # -----------------------------------
        # Recovered Energy
        # -----------------------------------

        recovered = float(
            data.get(
                "thermal_harvest_rate",
                0.0
            )
        )

        # -----------------------------------
        # Parasitic Loads
        # -----------------------------------

        parasitic = max(
            0.0,
            float(active_loads)
        )

        # -----------------------------------
        # Thermal Penalty
        # -----------------------------------

        penalty = max(
            0.0,
            float(
                data.get(
                    "thermal_coupling_loss",
                    0.0
                )
            )
        )

        # -----------------------------------
        # Compute / Sensor Overhead
        # -----------------------------------

        overhead = max(
            0.0,
            float(
                self.config.get(
                    "system_metadata",
                    {}
                ).get(
                    "compute_cost",
                    0.01
                )
            )
        )

        # -----------------------------------
        # Net Calculation
        # -----------------------------------

        net = (
            recovered
            -
            (
                parasitic
                +
                penalty
                +
                overhead
            )
        )

        self.logger.info(
            f"Net Benefit | "
            f"Recovered={recovered:.3f} | "
            f"Parasitic={parasitic:.3f} | "
            f"Penalty={penalty:.3f} | "
            f"Overhead={overhead:.3f} | "
            f"Net={net:.3f}"
        )

        return net

    # ========================================================
    # Stage Optimization
    # ========================================================

    def optimize_cascade(
        self,
        data: dict
    ):
        """
        Cascade monitoring and optimization.
        """

        exit_temp = (
            data.get(
                "temp_exit",
                0.0
            )
        )

        entropy_limit = (
            self.config
            .get(
                "thresholds",
                {}
            )
            .get(
                "stage_5_entropy",
                30.0
            )
        )

        if exit_temp > entropy_limit:

            self.logger.info(
                "Stage 5 threshold "
                "exceeded. "
                "Evaluating optimization."
            )

            # Future:
            # Flow adjustment
            # Stage tuning
            # Exergy analysis
```
