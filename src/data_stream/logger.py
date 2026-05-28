
"""
CHTS-Advanced-Materials: Telemetry Logger

Persistent CSV logging for:

- System telemetry
- Net-benefit metrics
- Observer diagnostics
"""

import csv
import os
import logging

from datetime import datetime


logger = logging.getLogger(
    "CHTS-Logger"
)


class DataLogger:

    def __init__(
        self,
        log_dir="logs"
    ):

        self.log_dir = log_dir

        os.makedirs(
            self.log_dir,
            exist_ok=True
        )

        timestamp = (
            datetime.now()
            .strftime(
                "%Y%m%d_%H%M%S"
            )
        )

        self.filename = os.path.join(
            self.log_dir,
            f"telemetry_{timestamp}.csv"
        )

        self.headers = [

            # Time
            "timestamp",

            # Telemetry
            "pressure_in",
            "pressure_out",
            "temp_exit",

            # Diagnostics
            "fouling_score",

            # Energy Accounting
            "recovered",
            "parasitic",
            "penalty",
            "overhead",
            "net_benefit"
        ]

        try:

            with open(
                self.filename,
                "w",
                newline="",
                encoding="utf-8"
            ) as f:

                writer = csv.writer(f)
                writer.writerow(
                    self.headers
                )

            logger.info(
                f"Telemetry log created: "
                f"{self.filename}"
            )

        except Exception as e:

            logger.exception(
                f"Failed to create "
                f"log file: {e}"
            )

            raise

    # =====================================================
    # Log Observer Cycle
    # =====================================================

    def log_cycle(
        self,
        telemetry: dict,
        net_metrics: dict,
        fouling_score: float = 0.0
    ):

        try:

            with open(
                self.filename,
                "a",
                newline="",
                encoding="utf-8"
            ) as f:

                writer = csv.writer(f)

                writer.writerow([

                    # Timestamp
                    datetime.now().isoformat(),

                    # Telemetry
                    telemetry.get(
                        "pressure_in",
                        0.0
                    ),

                    telemetry.get(
                        "pressure_out",
                        0.0
                    ),

                    telemetry.get(
                        "temp_exit",
                        0.0
                    ),

                    # Diagnostics
                    fouling_score,

                    # Net Metrics
                    net_metrics.get(
                        "recovered",
                        0.0
                    ),

                    net_metrics.get(
                        "parasitic",
                        0.0
                    ),

                    net_metrics.get(
                        "penalty",
                        0.0
                    ),

                    net_metrics.get(
                        "overhead",
                        0.0
                    ),

                    net_metrics.get(
                        "net",
                        0.0
                    )
                ])

        except Exception as e:

            logger.exception(
                f"Telemetry write "
                f"failed: {e}"
            )
