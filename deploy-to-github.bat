@echo off
REM DayZ Item Scraper - GitHub Deployment Script for Windows
REM This script prepares and deploys the project to GitHub

setlocal enabledelayedexpansion

echo 🚀 DayZ Item Scraper - GitHub Deployment (Windows)
echo ==================================================
echo.

REM GitHub repository details
set GITHUB_USER=SergeyZakh
set REPO_NAME=dayz-item-scraper
set REPO_URL=https://github.com/%GITHUB_USER%/%REPO_NAME%.git

echo Repository: %REPO_URL%
echo.

REM Check if we're in the right directory
if not exist "dayz_item_scraper.py" (
    echo ❌ Error: dayz_item_scraper.py not found in current directory
    echo Please run this script from the project root directory
    pause
    exit /b 1
)

echo ✅ Found main script file

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Git is not installed
    echo Please install Git first: https://git-scm.com/downloads
    pause
    exit /b 1
)

echo ✅ Git is available

REM Initialize git repository if not already done
if not exist ".git" (
    echo 📁 Initializing Git repository...
    git init
    echo ✅ Git repository initialized
) else (
    echo ✅ Git repository already exists
)

REM Check required files
echo 📋 Checking required files...
set "files=dayz_item_scraper.py requirements.txt README.md LICENSE .gitignore CONTRIBUTING.md .github/workflows/ci.yml"
set missing=0

for %%f in (%files%) do (
    if exist "%%f" (
        echo   ✅ %%f
    ) else (
        echo   ❌ %%f
        set missing=1
    )
)

if %missing%==1 (
    echo ❌ Missing required files. Please create them first.
    pause
    exit /b 1
)

echo ✅ All required files present
echo.

REM Add all files to git
echo 📦 Adding files to Git...
git add .

REM Check if there are changes to commit
git diff --staged --quiet
if errorlevel 1 (
    echo 💾 Committing changes...
    
    REM Get version from script
    for /f "tokens=*" %%i in ('python -c "import re; content=open('dayz_item_scraper.py').read(); match=re.search(r'__version__\s*=\s*[\"\']([\d\.]+)[\"\']', content); print(match.group(1) if match else '1.0.0')"') do set VERSION=%%i
    
    git commit -m "🎮 DayZ Item Scraper v!VERSION! - Ready for production"
    echo ✅ Changes committed
) else (
    echo ⚠️ No changes to commit
)

REM Set up remote repository
echo 🔗 Setting up remote repository...

REM Remove existing origin if it exists
git remote remove origin 2>nul

REM Add the correct origin
git remote add origin %REPO_URL%
echo ✅ Remote origin set to: %REPO_URL%

REM Check current branch and rename if necessary
for /f "tokens=*" %%i in ('git branch --show-current') do set CURRENT_BRANCH=%%i
if not "!CURRENT_BRANCH!"=="main" (
    echo 🔄 Renaming branch from '!CURRENT_BRANCH!' to 'main'...
    git branch -M main
    echo ✅ Branch renamed to 'main'
)

REM Push to GitHub
echo 🚀 Pushing to GitHub...
echo Repository URL: %REPO_URL%
echo.

set /p CONFIRM="🤔 Ready to push to GitHub? This will upload all files. (y/N): "
if /i "%CONFIRM%"=="y" (
    echo ⬆️ Pushing to GitHub...
    
    git push -u origin main
    if errorlevel 1 (
        echo ❌ Push failed. Please check your GitHub credentials and try again.
        echo 💡 You may need to authenticate with GitHub first:
        echo    git config --global user.name "Your Name"
        echo    git config --global user.email "your.email@example.com"
        pause
        exit /b 1
    ) else (
        echo.
        echo 🎉 SUCCESS! Project deployed to GitHub!
        echo.
        echo 📍 Repository: %REPO_URL%
        echo 🌐 GitHub Page: https://github.com/%GITHUB_USER%/%REPO_NAME%
        echo.
        echo 📋 Next steps:
        echo 1. 🔧 Go to repository settings and enable GitHub Actions
        echo 2. 📝 Create repository description and topics
        echo 3. 🏷️ Add topics: dayz, scraper, python, gaming, icons
        echo 4. 🌟 Share with the DayZ community!
        echo.
        echo ✅ Project is now live and ready for community contributions!
    )
) else (
    echo ⏸️ Deployment cancelled. Files are ready when you want to push.
    echo To deploy later, run: git push -u origin main
)

echo.
echo 🎮 DayZ Item Scraper deployment script completed!
echo.
pause
