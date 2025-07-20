#!/bin/bash

# DayZ Item Scraper - Quick Setup Script
# This script sets up the environment and dependencies for the DayZ Item Scraper

set -e  # Exit on any error

echo "🎮 DayZ Item Scraper - Quick Setup"
echo "=================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7+ first."
    echo "   Download from: https://www.python.org/downloads/"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.7"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 7) else 1)"; then
    echo "❌ Python 3.7+ is required. Current version: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

echo "✅ pip3 is available"

# Create virtual environment (optional but recommended)
read -p "🤔 Do you want to create a virtual environment? (recommended) [Y/n]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    
    # Activate virtual environment
    if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    
    echo "✅ Virtual environment created and activated"
    echo "   To activate it later, run: source venv/bin/activate"
fi

# Upgrade pip
echo "⬆️  Upgrading pip..."
python3 -m pip install --upgrade pip

# Install requirements
echo "📥 Installing dependencies..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
    echo "✅ Dependencies installed successfully"
else
    echo "⚠️  requirements.txt not found. Installing dependencies manually..."
    pip3 install requests beautifulsoup4 lxml
    echo "✅ Dependencies installed manually"
fi

# Create output directory
echo "📁 Creating output directory..."
mkdir -p dayz_weapon_icons
echo "✅ Output directory created: dayz_weapon_icons/"

# Test the installation
echo "🧪 Testing installation..."
if python3 -c "import requests, bs4; print('✅ All dependencies working')"; then
    echo "✅ Installation test passed"
else
    echo "❌ Installation test failed"
    exit 1
fi

# Display usage information
echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "🚀 Quick Start:"
echo "   python3 dayz_item_scraper.py"
echo ""
echo "📖 For more options:"
echo "   python3 dayz_item_scraper.py --help"
echo ""
echo "📁 Downloaded icons will be saved to: dayz_weapon_icons/"
echo ""
echo "📚 For detailed documentation, see: README.md"
echo ""
echo "🐛 If you encounter issues:"
echo "   1. Check the troubleshooting section in README.md"
echo "   2. Create an issue on GitHub"
echo "   3. Make sure you have a stable internet connection"
echo ""
echo "Happy scraping! 🎮✨"
