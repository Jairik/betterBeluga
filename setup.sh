#!/usr/bin/env bash
# Bash script to make and switch to a python env, because I am incredibly lazy

set -euo pipefail

# Install uv, if not already installed 
if ! command -v uv > /dev/null 2>&1; then
    python3 -m pip install --upgrade pip
    python3 -m pip install uv
    uv self update || true  # Silent fail if already up-to-date
fi

# Setup a uv venv, if it doesn't already exist
if [ ! -d ".venv" ]; then
    uv venv .venv
fi
source .venv/bin/activate

# Download dependencies and whatnot
if [ -f "docs/requirements.txt" ]; then
    uv pip sync docs/requirements.txt --allow-empty-requirements 
fi

echo "> virtual environment is activated"