```bash
#!/bin/bash

# ============================================================
# CHTS-Advanced-Materials
# Observation System Launch Script
# ============================================================

set -e

echo "===================================================="
echo "CHTS-Advanced-Materials Launch Sequence"
echo "Timestamp: $(date)"
echo "===================================================="

# ------------------------------------------------------------
# Move to project root
# ------------------------------------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "[INFO] Project root:"
echo "       $SCRIPT_DIR"

# ------------------------------------------------------------
# Verify Python
# ------------------------------------------------------------

if ! command -v python3 >/dev/null 2>&1; then
    echo "[ERROR] python3 not found."
    exit 1
fi

PYTHON_VERSION=$(python3 --version)

echo "[INFO] Python detected:"
echo "       $PYTHON_VERSION"

# ------------------------------------------------------------
# Export PYTHONPATH
# ------------------------------------------------------------

export PYTHONPATH="${PYTHONPATH}:$(pwd)"

echo "[INFO] PYTHONPATH configured."

# ------------------------------------------------------------
# Launch Observer
# ------------------------------------------------------------

echo "[INFO] Starting observer..."

python3 src/observer/main.py

EXIT_CODE=$?

# ------------------------------------------------------------
# Shutdown Status
# ------------------------------------------------------------

echo "----------------------------------------------------"

if [ $EXIT_CODE -ne 0 ]; then

    echo "[ERROR] System exited with code:"
    echo "        $EXIT_CODE"

else

    echo "[INFO] System shutdown gracefully."

fi

echo "----------------------------------------------------"

exit $EXIT_CODE
```
