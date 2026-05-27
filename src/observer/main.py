"""
CHTS-Advanced-Materials: Execution Entry Point
This script initializes the environment and enters the observation loop.
"""

import yaml
import logging
import sys
import os
from src.observer.core import AIObserver

# Setup structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("CHTS-Main")

def main():
    # 1. Load Configuration
    config_path = "src/data_stream/config.yaml"
    
    if not os.path.exists(config_path):
        logger.error(f"Configuration file not found at {config_path}")
        sys.exit(1)
        
    with open(config_path, "r") as f:
        try:
            config = yaml.safe_load(f)
            logger.info("Configuration loaded successfully.")
        except yaml.YAMLError as e:
            logger.error(f"Error parsing YAML configuration: {e}")
            sys.exit(1)
    
    # 2. Initialize the AI Observer
    try:
        observer = AIObserver(config)
        logger.info("CHTS-Advanced-Materials Observer System initialized.")
    except Exception as e:
        logger.error(f"Failed to initialize AIObserver: {e}")
        sys.exit(1)
    
    # 3. Execution Loop
    logger.info("Starting thermodynamic observation loop. Press Ctrl+C to terminate.")
    try:
        while True:
            observer.run_cycle()
            # Optional: Add sleep if sampling frequency needs regulation
            # time.sleep(1.0 / config['hardware_settings']['sampling_rate_hz'])
    except KeyboardInterrupt:
        logger.info("System shutdown signal received. Executing safe-state protocol.")
        # Optional: Add explicit call to close hardware valves here
        sys.exit(0)

if __name__ == "__main__":
    main()
