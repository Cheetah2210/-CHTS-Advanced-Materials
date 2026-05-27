# CHTS-Advanced-Materials: Build Automation
# Run 'make help' to see available commands

.PHONY: install test run clean help

# Default target: Run the development simulation
all: run-dev

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

test:
	@echo "Running validation suite..."
	pytest tests/test_observer.py --verbose

run-dev:
	@echo "Launching CHTS in development mode..."
	CHTS_ENV=dev python3 main.py

run-prod:
	@echo "Launching CHTS in production mode..."
	CHTS_ENV=prod python3 main.py

clean:
	@echo "Cleaning up generated logs and cache..."
	rm -rf __pycache__
	rm -rf validation/calibration_logs/*.csv
	find . -type f -name "*.pyc" -delete

help:
	@echo "Available commands:"
	@echo "  make install  - Install project dependencies"
	@echo "  make test     - Execute software validation tests"
	@echo "  make run-dev  - Run simulation for testing"
	@echo "  make run-prod - Execute production observer"
	@echo "  make clean    - Remove temp files and logs"
