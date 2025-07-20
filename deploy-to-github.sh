#!/bin/bash

# DayZ Item Scraper - GitHub Deployment Script
# This script prepares and deploys the project to GitHub

set -e

echo "🚀 DayZ Item Scraper - GitHub Deployment"
echo "========================================"
echo

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# GitHub repository details
GITHUB_USER="SergeyZakh"
REPO_NAME="dayz-item-scraper"
REPO_URL="https://github.com/${GITHUB_USER}/${REPO_NAME}.git"

echo -e "${BLUE}Repository: ${REPO_URL}${NC}"
echo

# Check if we're in the right directory
if [ ! -f "dayz_item_scraper.py" ]; then
    echo -e "${RED}❌ Error: dayz_item_scraper.py not found in current directory${NC}"
    echo "Please run this script from the project root directory"
    exit 1
fi

echo -e "${GREEN}✅ Found main script file${NC}"

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Error: Git is not installed${NC}"
    echo "Please install Git first: https://git-scm.com/downloads"
    exit 1
fi

echo -e "${GREEN}✅ Git is available${NC}"

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}📁 Initializing Git repository...${NC}"
    git init
    echo -e "${GREEN}✅ Git repository initialized${NC}"
else
    echo -e "${GREEN}✅ Git repository already exists${NC}"
fi

# Check required files
echo -e "${YELLOW}📋 Checking required files...${NC}"
required_files=(
    "dayz_item_scraper.py"
    "requirements.txt"
    "README.md"
    "LICENSE"
    ".gitignore"
    "CONTRIBUTING.md"
    ".github/workflows/ci.yml"
)

missing_files=()
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}  ✅ $file${NC}"
    else
        echo -e "${RED}  ❌ $file${NC}"
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -ne 0 ]; then
    echo -e "${RED}❌ Missing required files. Please create them first.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All required files present${NC}"
echo

# Add all files to git
echo -e "${YELLOW}📦 Adding files to Git...${NC}"
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo -e "${YELLOW}⚠️ No changes to commit${NC}"
else
    # Commit changes
    echo -e "${YELLOW}💾 Committing changes...${NC}"
    
    # Get version from script
    VERSION=$(python -c "
import re
with open('dayz_item_scraper.py', 'r') as f:
    content = f.read()
    match = re.search(r'__version__\s*=\s*[\"\']([\d\.]+)[\"\']', content)
    print(match.group(1) if match else '1.0.0')
")
    
    COMMIT_MESSAGE="🎮 DayZ Item Scraper v${VERSION} - Ready for production

✨ Features:
- Complete DayZ item scraping (37+ categories)
- Intelligent folder organization
- Cross-platform support
- Professional CI/CD pipeline
- Comprehensive documentation

🚀 Ready for community use!"

    git commit -m "$COMMIT_MESSAGE"
    echo -e "${GREEN}✅ Changes committed${NC}"
fi

# Set up remote repository
echo -e "${YELLOW}🔗 Setting up remote repository...${NC}"

# Remove existing origin if it exists
git remote remove origin 2>/dev/null || true

# Add the correct origin
git remote add origin "$REPO_URL"
echo -e "${GREEN}✅ Remote origin set to: $REPO_URL${NC}"

# Check current branch and rename if necessary
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo -e "${YELLOW}🔄 Renaming branch from '$CURRENT_BRANCH' to 'main'...${NC}"
    git branch -M main
    echo -e "${GREEN}✅ Branch renamed to 'main'${NC}"
fi

# Push to GitHub
echo -e "${YELLOW}🚀 Pushing to GitHub...${NC}"
echo -e "${BLUE}Repository URL: $REPO_URL${NC}"
echo

read -p "🤔 Ready to push to GitHub? This will upload all files. (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}⬆️ Pushing to GitHub...${NC}"
    
    # Push with upstream
    if git push -u origin main; then
        echo
        echo -e "${GREEN}🎉 SUCCESS! Project deployed to GitHub!${NC}"
        echo
        echo -e "${BLUE}📍 Repository: $REPO_URL${NC}"
        echo -e "${BLUE}🌐 GitHub Page: https://github.com/${GITHUB_USER}/${REPO_NAME}${NC}"
        echo
        echo -e "${YELLOW}📋 Next steps:${NC}"
        echo "1. 🔧 Go to repository settings and enable GitHub Actions"
        echo "2. 📝 Create repository description and topics"
        echo "3. 🏷️ Add topics: dayz, scraper, python, gaming, icons"
        echo "4. 🌟 Share with the DayZ community!"
        echo
        echo -e "${GREEN}✅ Project is now live and ready for community contributions!${NC}"
    else
        echo -e "${RED}❌ Push failed. Please check your GitHub credentials and try again.${NC}"
        echo "💡 You may need to authenticate with GitHub first:"
        echo "   git config --global user.name 'Your Name'"
        echo "   git config --global user.email 'your.email@example.com'"
        exit 1
    fi
else
    echo -e "${YELLOW}⏸️ Deployment cancelled. Files are ready when you want to push.${NC}"
    echo "To deploy later, run: git push -u origin main"
fi

echo
echo -e "${BLUE}🎮 DayZ Item Scraper deployment script completed!${NC}"
