@echo off

REM Define the name of the Python script
set SCRIPT_NAME=microcontroller_comms.py

REM Install required Python packages using pip
pip install pyserial requests

REM Check if the installation was successful
if %errorlevel% neq 0 (
    echo Error: Failed to install required packages.
    pause
    exit /b 1
)

REM Run the Python script
python %SCRIPT_NAME%

REM Pause to keep the command prompt window open
pause
