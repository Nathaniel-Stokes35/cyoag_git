@echo off
echo Checking if Python 3 is installed...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python 3 is not installed. Please install Python 3 and try again.
    exit /b 1
)

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo Setup complete! You can now run the game with "python game.py".
pause