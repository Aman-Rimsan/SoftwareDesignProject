@echo off
echo E-Stock Inventory Management System
echo ------------------------------
echo 1. Run GUI Version
echo 2. Run Console Version
echo 3. Clean up files
echo 4. Exit
echo.

choice /c 1234 /n /m "Please select an option (1-4): "

if errorlevel 4 goto exit
if errorlevel 3 goto clean
if errorlevel 2 goto console
if errorlevel 1 goto gui

:gui
cls
echo Starting GUI Version...
python UI2.py
goto end

:console
cls
echo Starting Console Version...
python Stock.py
goto end

:clean
cls
echo Cleaning up...
if exist exported_inventory.csv del exported_inventory.csv
echo Original data files (Estock.csv, data.csv) are preserved
pause
goto start

:exit
exit

:end
