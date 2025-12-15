#!/bin/bash
# P-Mark-III Startup Script (Linux/Mac)
# Version: 1.0.2

echo ""
echo "========================================"
echo "   P-Mark-III - Starting Server"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "[INFO] Creating .env file from .env.example..."
    cp .env.example .env
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[INFO] Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "[INFO] Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "[INFO] Installing dependencies..."
pip install -r requirements.txt --quiet --upgrade

# Start the application
echo "[INFO] Starting P-Mark-III..."
echo ""
python3 app.py
