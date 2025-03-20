@echo off
REM filepath: c:\Users\ahmed\Downloads\Software Design And Analysis\SoftwareDesignProject\build_and_run.bat

:menu
echo.
echo Select an option:
echo 1. Run Stock.py
echo 2. Run UI2.py
echo 3. Install dependencies
echo 4. Clean up temporary files
echo 5. Exit
set /p choice=Enter your choice: 

if "%choice%"=="1" goto run_stock
if "%choice%"=="2" goto run_ui
if "%choice%"=="3" goto install
if "%choice%"=="4" goto clean
if "%choice%"=="5" goto exit
echo Invalid choice. Please try again.
goto menu

:run_stock
python Stock.py
goto menu

:run_ui
python UI2.py
goto menu

:install
if exist requirements.txt (
    python -m pip install -r requirements.txt
) else (
    echo No requirements.txt found. Skipping dependency installation.
)
goto menu

:clean
echo Cleaning up...
del /q *.pyc 2>nul || echo No .pyc files to delete.
rmdir /q /s __pycache__ 2>nul || echo No __pycache__ directory to delete.
echo Cleanup complete.
goto menu

:exit
echo Exiting...