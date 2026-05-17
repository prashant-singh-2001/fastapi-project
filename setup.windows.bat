@echo off

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing requirements...
pip install -r requirements.txt

echo.
echo Setup completed successfully!
echo To activate the environment later use:
echo venv\Scripts\activate

pause