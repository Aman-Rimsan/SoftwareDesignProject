@echo off
REM filepath: c:\Users\ahmed\Downloads\Software Design And Analysis\SoftwareDesignProject\build_and_run.bat

REM Step 1: Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

REM Step 2: Install required dependencies (if any)
echo Installing required dependencies...
pip install -r requirements.txt >nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to install dependencies. Ensure pip is installed and try again.
    exit /b 1
)

REM Step 3: Run the program
echo Running the Inventory Management System...
python Stock.py
if %errorlevel% neq 0 (
    echo Failed to run the program. Check for errors in Stock.py.
    exit /b 1
)

REM Step 4: Completion message
echo Program executed successfully.
pause