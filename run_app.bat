@echo off
title Bulk Email Dispatcher Setup & Launch
cd /d "%~dp0"

:: 1. Check if the virtual environment folder exists
if not exist .venv (
    echo ====================================================
    echo [FIRST RUN DETECTED] Setting up environment...
    echo ====================================================
    
    :: Create the virtual environment
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo [ERROR] Python is not installed or not in your PATH variables.
        pause
        exit /b
    )
    
    :: Activate and install dependencies
    echo Installing requirements from requirements.txt...
    call .venv\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    
    echo Setup complete!
    echo ====================================================
) else (
    :: 2. Subsequent runs: Just activate the existing environment
    call .venv\Scripts\activate
)

:: 3. Launch the application
echo Launching Streamlit Application...
streamlit run app.py

:: Keep window open if it crashes
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Streamlit encountered an issue and closed.
    pause
)