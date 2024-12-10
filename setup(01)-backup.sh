#!/bin/bash

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
  echo "Python 3 is not installed. Please install Python 3 and try again."
  exit 1
fi

# Check if pip is installed
if ! command -v pip3 &>/dev/null; then
  echo "pip is not installed. Installing pip..."
  python3 -m ensurepip --upgrade
fi

# Create a virtual environment (optional but recommended)
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
~                                                                                                                                                                                                                                                                                                                                               
