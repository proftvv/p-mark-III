@echo off
REM P-Mark-III Startup Script
REM Version: 1.0.2

echo.
echo ========================================
echo    P-Mark-III - Starting Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Check if .env file exists, if not copy from example
if not exist .env (
    echo [INFO] Creating .env file from .env.example...
    copy .env.example .env >nul
)

REM Check if virtual environment exists
if not exist venv (
    echo [INFO] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/upgrade dependencies
echo [INFO] Installing dependencies...
pip install -r requirements.txt --quiet --upgrade

REM Start the application
echo [INFO] Starting P-Mark-III...
echo.
python app.py

REM If app exits, pause to show any errors
pause
