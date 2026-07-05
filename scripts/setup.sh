#!/bin/bash
set -euo pipefail
echo "Setting up Landing Zone Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
