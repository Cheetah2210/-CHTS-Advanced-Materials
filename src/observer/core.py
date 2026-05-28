
"""
CHTS-Advanced-Materials: AI Observer Core

Central intelligence loop for:

- Telemetry acquisition
- Fouling detection
- Net-benefit accounting
- Persistent telemetry logging
- Self-healing recovery
- Cascade optimization
"""

import logging

from src.electrical.interface import ElectricalInterface
from src.observer.self_healing import SelfHealingManager
from src.observer.logger import DataLogger


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

        self.data_logger = (
            DataLogger()
        )

        self.logger = logger

        self.logger.info(
            "AI Observer initialized "
            "with persistence layer."
        )

    # =====================================================
    # Main Observer Cycle
    # =====================================================

    def run_cycle(self):
        """
        Monitor -> Analyze -> Act -> Log
        """

        # ---------------------------------
        # 1. Gather Telemetry
        # ---------------------------------

        telemetry = (
            self.interface
            .get_system_state()
        )

        self.logger.debug(
            f"Telemetry: {telemetry}"
        )

        active_loads = float(
            telemetry.get(
                "active_loads",
                0.0
            )
        )

        # ---------------------------------
        # 2. Fouling Analysis
        # ---------------------------------

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
                (
                    fouling_limit
                    * 2
                )
                else "MEDIUM"
            )

            self.logger.warning(
                f"Fouling threshold "
                f"exceeded | "
                f"Severity={severity}"
            )

            self.healer.execute_recovery_sequence(
                severity=severity
            )

        # ---------------------------------
        # 3. Net Benefit Accounting
        # ---------------------------------

        net_metrics = (
            self.calculate_net_metrics(
                telemetry,
                active_loads
            )
        )

        net_benefit = (
            net_metrics["net"]
        )

        self.logger.info(
            f"Net Benefit: "
            f"{net_benefit:.3f}"
        )

        if net_benefit < 0:

            self.logger.warning(
                "Negative net benefit "
                "detected."
            )

        # ---------------------------------
        # 4. Persistent Logging
        # ---------------------------------

        self.data_logger.log_cycle(
            telemetry,
            net_metrics,
            fouling_score
        )

        # ---------------------------------
        # 5. Cascade Optimization
        # ---------------------------------

        self.optimize_cascade(
            telemetry
        )

    # =====================================================
    # Fouling Analysis
    # =====================================================

    def calculate_fouling(
        self,
        data: dict
    ) -> float:
        """
        Pressure-drop fouling proxy.
        """

        pressure_in = float(
            data.get(
                "pressure_in",
                0.0
            )
        )

        pressure_out = float(
            data.get(
                "pressure_out",
                0.0
            )
        )

        delta_p = (
            pressure_in
            -
            pressure_out
        )

        return max(
            0.0,
            delta_p * 0.1
        )

    # =====================================================
    # Net Benefit Accounting
    # =====================================================

    def calculate_net_metrics(
        self,
        data: dict,
        active_loads: float
    ) -> dict:
        """
        Empirical energy accounting.
        """

        recovered = float(
            data.get(
                "thermal_harvest_rate",
                0.0
            )
        )

        parasitic = max(
            0.0,
            float(
                active_loads
            )
        )

        penalty = max(
            0.0,
            float(
                data.get(
                    "thermal_coupling_loss",
                    0.0
                )
            )
        )

        overhead = max(
            0.0,
            float(
                self.config
                .get(
                    "system_metadata",
                    {}
                )
                .get(
                    "compute_cost",
                    0.01
                )
            )
        )

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

        return {

            "recovered":
                recovered,

            "parasitic":
                parasitic,

            "penalty":
                penalty,

            "overhead":
                overhead,

            "net":
                net
        }

    # =====================================================
    # Cascade Optimization
    # =====================================================

    def optimize_cascade(
        self,
        data: dict
    ):
        """
        Stage 5 monitoring.
        """

        exit_temp = float(
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
                f"Stage 5 threshold "
                f"exceeded | "
                f"Exit={exit_temp:.2f}C | "
                f"Limit={entropy_limit:.2f}C"
            )

            # Future:
            # Flow tuning
            # Exergy routing
            # Stage disable logic
