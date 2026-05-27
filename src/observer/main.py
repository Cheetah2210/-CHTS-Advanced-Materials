
"""
CHTS-Advanced-Materials: Execution Entry Point
Initializes configuration and enters the thermodynamic observer loop.
"""

import yaml
import logging
import sys
import os
import time
from src.observer.core import AIObserver

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("CHTS-Main")


def load_config():
    """
    Load YAML configuration relative to this file.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.abspath(
        os.path.join(
            base_dir,
            "..",
            "data_stream",
            "config.yaml"
        )
    )

    if not os.path.exists(config_path):
        logger.error(
            f"Configuration file missing: {config_path}"
        )
        sys.exit(1)

    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        logger.info("Configuration loaded.")
        return config

    except yaml.YAMLError as e:
        logger.error(
            f"YAML parsing failure: {e}"
        )
        sys.exit(1)


def main():

    config = load_config()

    try:
        observer = AIObserver(config)
        logger.info(
            "AI Observer initialized successfully."
        )

    except Exception as e:
        logger.error(
            f"Observer initialization failed: {e}"
        )
        sys.exit(1)

    sampling_rate = (
        config.get(
            "hardware_settings",
            {}
        ).get(
            "sampling_rate_hz",
            1.0
        )
    )

    delay = 1.0 / max(
        sampling_rate,
        0.1
    )

    logger.info(
        f"Observation loop active at "
        f"{sampling_rate:.2f} Hz."
    )

    try:
        while True:
            observer.run_cycle()
            time.sleep(delay)

    except KeyboardInterrupt:
        logger.info(
            "Shutdown received. "
            "Observer entering safe-state."
        )
        sys.exit(0)


if __name__ == "__main__":
    main()

