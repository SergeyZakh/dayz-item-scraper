@echo off
REM DayZ Item Scraper - Quick Setup Script for Windows
REM This script sets up the environment and dependencies for the DayZ Item Scraper

echo 🎮 DayZ Item Scraper - Quick Setup (Windows)
echo ===============================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH.
    echo    Please install Python 3.7+ from: https://www.python.org/downloads/
    echo    Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% detected

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip is not installed. Please reinstall Python with pip.
    pause
    exit /b 1
)

echo ✅ pip is available

REM Ask about virtual environment
set /p CREATE_VENV="🤔 Do you want to create a virtual environment? (recommended) [Y/n]: "
if "%CREATE_VENV%"=="" set CREATE_VENV=Y
if /i "%CREATE_VENV%"=="Y" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment created and activated
    echo    To activate it later, run: venv\Scripts\activate.bat
)

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo 📥 Installing dependencies...
if exist requirements.txt (
    pip install -r requirements.txt
    echo ✅ Dependencies installed successfully
) else (
    echo ⚠️  requirements.txt not found. Installing dependencies manually...
    pip install requests beautifulsoup4 lxml
    echo ✅ Dependencies installed manually
)

REM Create output directory
echo 📁 Creating output directory...
if not exist dayz_weapon_icons mkdir dayz_weapon_icons
echo ✅ Output directory created: dayz_weapon_icons\

REM Test the installation
echo 🧪 Testing installation...
python -c "import requests, bs4; print('✅ All dependencies working')" 2>nul
if errorlevel 1 (
    echo ❌ Installation test failed
    pause
    exit /b 1
) else (
    echo ✅ Installation test passed
)

REM Display usage information
echo.
echo 🎉 Setup completed successfully!
echo.
echo 🚀 Quick Start:
echo    python dayz_item_scraper.py
echo.
echo 📖 For more options:
echo    python dayz_item_scraper.py --help
echo.
echo 📁 Downloaded icons will be saved to: dayz_weapon_icons\
echo.
echo 📚 For detailed documentation, see: README.md
echo.
echo 🐛 If you encounter issues:
echo    1. Check the troubleshooting section in README.md
echo    2. Create an issue on GitHub
echo    3. Make sure you have a stable internet connection
echo    4. Try running as administrator if permission errors occur
echo.
echo Happy scraping! 🎮✨
echo.
pause
