#!/bin/bash

# Create a virtual environment
python3 -m venv claude-env

# Activate the virtual environment
source claude-env/bin/activate

# Install the anthropic package
pip install anthropic

# Run the Python script with command-line arguments
python ./claude_content_to_md.py "$@"

# Deactivate the virtual environment
deactivate
