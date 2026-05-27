
"""
CHTS-Advanced-Materials: AI Observer Core
Central intelligence loop for monitoring,
diagnostics, and thermodynamic recovery logic.
"""

import logging

from src.electrical.interface import ElectricalInterface
from src.observer.self_healing import SelfHealingManager

logger = logging.getLogger("CHTS-Observer")


class AIObserver:

    def __init__(self, config):

        self.config = config

        self.interface = ElectricalInterface(
            config
        )

        self.healer = SelfHealingManager(
            self.interface
        )

        logger.info(
            "AI Observer initialized."
        )

    def run_cycle(self):
        """
        Monitor -> Analyze -> Act
        """

        telemetry = (
            self.interface
            .get_system_state()
        )

        logger.debug(
            f"Telemetry: {telemetry}"
        )

        fouling_score = (
            self.calculate_fouling(
                telemetry
            )
        )

        limit = (
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

        logger.info(
            f"Fouling score: "
            f"{fouling_score:.3f}"
        )

        if fouling_score > limit:

            severity = (
                "HIGH"
                if fouling_score >
                (limit * 2)
                else "MEDIUM"
            )

            logger.warning(
                f"Anomaly detected | "
                f"Score={fouling_score:.3f} | "
                f"Severity={severity}"
            )

            self.healer.execute_recovery_sequence(
                severity
            )

        self.optimize_cascade(
            telemetry
        )

    def calculate_fouling(
        self,
        data
    ) -> float:
        """
        Fouling proxy using pressure drop.
        """

        delta_p = (
            data.get(
                "pressure_in",
                0
            )
            -
            data.get(
                "pressure_out",
                0
            )
        )

        score = max(
            0.0,
            delta_p * 0.1
        )

        return score

    def optimize_cascade(
        self,
        data
    ):
        """
        Stage monitoring logic.
        """

        exit_temp = data.get(
            "temp_exit",
            0
        )

        stage_limit = (
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

        if exit_temp > stage_limit:

            logger.info(
                "Stage 5 threshold exceeded. "
                "Evaluating flow adjustment."
            )

            # Future cascade control logic

