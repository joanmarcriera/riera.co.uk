# Create a comprehensive deployment script
deployment_script = '''#!/bin/bash

# Professional GitHub Pages Deployment Script for Marc Riera
# Created by Perplexity AI Research Agent
# Usage: ./deploy.sh

set -e  # Exit on any error

# Configuration
REPO_NAME="riera.co.uk"
GITHUB_USER="joanmarcriera"
DOMAIN="riera.co.uk"
BRANCH="main"

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[0;34m'
NC='\\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
check_prerequisites() {
    print_status "Checking prerequisites..."
    
    if ! command_exists git; then
        print_error "Git is not installed. Please install Git first."
        exit 1
    fi
    
    if ! command_exists curl; then
        print_error "curl is not installed. Please install curl first."
        exit 1
    fi
    
    print_success "All prerequisites met."
}

# Initialize or update repository
setup_repository() {
    print_status "Setting up repository..."
    
    if [ -d "$REPO_NAME" ]; then
        print_warning "Repository directory already exists. Updating..."
        cd "$REPO_NAME"
        git pull origin $BRANCH || print_warning "Could not pull latest changes"
    else
        print_status "Cloning repository..."
        git clone "https://github.com/$GITHUB_USER/$REPO_NAME.git" || {
            print_warning "Repository does not exist yet. Creating new repository structure..."
            mkdir "$REPO_NAME"
            cd "$REPO_NAME"
            git init
            git checkout -b $BRANCH
        }
    fi
}

# Create directory structure
create_structure() {
    print_status "Creating directory structure..."
    
    mkdir -p assets/documents
    mkdir -p assets/images
    
    print_success "Directory structure created."
}

# Download a placeholder hero image
download_hero_image() {
    print_status "Downloading hero image..."
    
    # Use a high-quality tech background from Unsplash
    HERO_URL="https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80"
    
    if curl -L "$HERO_URL" -o assets/images/hero.jpg --silent; then
        print_success "Hero image downloaded successfully."
    else
        print_warning "Could not download hero image. Using CSS gradient instead."
    fi
}

# Commit and push changes
deploy_site() {
    print_status "Deploying to GitHub Pages..."
    
    # Add all files
    git add .
    
    # Check if there are changes to commit
    if git diff --staged --quiet; then
        print_warning "No changes to commit."
    else
        # Commit changes
        TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
        git commit -m "Deploy professional portfolio - $TIMESTAMP"
        
        # Push to GitHub
        if git remote get-url origin >/dev/null 2>&1; then
            git push origin $BRANCH
        else
            print_status "Setting up remote repository..."
            git remote add origin "https://github.com/$GITHUB_USER/$REPO_NAME.git"
            git push -u origin $BRANCH
        fi
    fi
    
    print_success "Site deployed successfully!"
}

# Display post-deployment instructions
show_instructions() {
    echo
    echo "=================================="
    echo "   DEPLOYMENT COMPLETE!"
    echo "=================================="
    echo
    print_success "Your professional portfolio has been deployed successfully!"
    echo
    echo "📋 NEXT STEPS:"
    echo
    echo "1. 🔧 Enable GitHub Pages:"
    echo "   - Go to: https://github.com/$GITHUB_USER/$REPO_NAME/settings/pages"
    echo "   - Set Source to 'Deploy from a branch'"
    echo "   - Select '$BRANCH' branch and '/ (root)' folder"
    echo "   - Click 'Save'"
    echo
    echo "2. 🌐 Configure Custom Domain:"
    echo "   - In the same Pages settings, add custom domain: $DOMAIN"
    echo "   - Configure your DNS with these records:"
    echo "     Type: A,    Name: @,   Value: 185.199.108.153"
    echo "     Type: A,    Name: @,   Value: 185.199.109.153"
    echo "     Type: A,    Name: @,   Value: 185.199.110.153"
    echo "     Type: A,    Name: @,   Value: 185.199.111.153"
    echo "     Type: CNAME, Name: www, Value: $DOMAIN"
    echo
    echo "3. 📄 Upload Documents:"
    echo "   - Add your CV/cover letter PDFs to: assets/documents/"
    echo "   - Ensure filenames match the links in index.html"
    echo
    echo "4. 🎯 Your Site URLs:"
    echo "   - GitHub Pages: https://$GITHUB_USER.github.io/$REPO_NAME"
    echo "   - Custom Domain: https://$DOMAIN (after DNS setup)"
    echo
    echo "🔍 VERIFICATION:"
    echo "   - GitHub Pages deployment typically takes 5-10 minutes"
    echo "   - DNS propagation can take up to 24 hours"
    echo "   - Check GitHub Actions tab for deployment status"
    echo
    echo "💡 TIPS:"
    echo "   - Test your site locally: python -m http.server 8000"
    echo "   - View at: http://localhost:8000"
    echo "   - Monitor performance with Google PageSpeed Insights"
    echo
}

# Main execution
main() {
    echo "🚀 Professional GitHub Pages Deployment Script"
    echo "==============================================="
    echo
    
    check_prerequisites
    setup_repository
    create_structure
    download_hero_image
    deploy_site
    show_instructions
}

# Run main function
main "$@"'''

# Create a batch file for Windows users
windows_deployment = '''@echo off
REM Professional GitHub Pages Deployment Script for Marc Riera (Windows)
REM Created by Perplexity AI Research Agent

setlocal enabledelayedexpansion

REM Configuration
set REPO_NAME=riera.co.uk
set GITHUB_USER=joanmarcriera  
set DOMAIN=riera.co.uk
set BRANCH=main

echo.
echo =============================================
echo    Professional GitHub Pages Deployment
echo =============================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed. Please install Git first.
    pause
    exit /b 1
)

echo [INFO] Setting up repository...

REM Clone or update repository
if exist "%REPO_NAME%" (
    echo [WARNING] Repository directory already exists. Updating...
    cd "%REPO_NAME%"
    git pull origin %BRANCH%
) else (
    echo [INFO] Cloning repository...
    git clone https://github.com/%GITHUB_USER%/%REPO_NAME%.git
    if %errorlevel% neq 0 (
        echo [WARNING] Repository does not exist yet. Creating new repository structure...
        mkdir "%REPO_NAME%"
        cd "%REPO_NAME%"
        git init
        git checkout -b %BRANCH%
    )
)

REM Create directory structure
echo [INFO] Creating directory structure...
mkdir assets\\documents 2>nul
mkdir assets\\images 2>nul

REM Deploy site
echo [INFO] Deploying to GitHub Pages...
git add .

REM Check if there are changes
git diff --staged --quiet
if %errorlevel% neq 0 (
    REM Get current timestamp
    for /f "tokens=2-4 delims=/ " %%a in ('date /t') do set mydate=%%c-%%a-%%b
    for /f "tokens=1-2 delims=/:" %%a in ('time /t') do set mytime=%%a:%%b
    
    git commit -m "Deploy professional portfolio - !mydate! !mytime!"
    
    REM Check if remote exists
    git remote get-url origin >nul 2>&1
    if %errorlevel% neq 0 (
        echo [INFO] Setting up remote repository...
        git remote add origin https://github.com/%GITHUB_USER%/%REPO_NAME%.git
    )
    
    git push origin %BRANCH%
    if %errorlevel% neq 0 (
        git push -u origin %BRANCH%
    )
) else (
    echo [WARNING] No changes to commit.
)

echo.
echo ==================================
echo       DEPLOYMENT COMPLETE!
echo ==================================
echo.
echo [SUCCESS] Your professional portfolio has been deployed successfully!
echo.
echo NEXT STEPS:
echo.
echo 1. Enable GitHub Pages:
echo    - Go to: https://github.com/%GITHUB_USER%/%REPO_NAME%/settings/pages
echo    - Set Source to 'Deploy from a branch'
echo    - Select '%BRANCH%' branch and '/ (root)' folder
echo    - Click 'Save'
echo.
echo 2. Configure Custom Domain:
echo    - Add custom domain: %DOMAIN%
echo    - Configure DNS A records: 185.199.108.153, 185.199.109.153, etc.
echo.
echo 3. Upload Documents:
echo    - Add your PDFs to: assets\\documents\\
echo.
echo 4. Your Site URLs:
echo    - GitHub Pages: https://%GITHUB_USER%.github.io/%REPO_NAME%
echo    - Custom Domain: https://%DOMAIN%
echo.
pause'''

print("Deployment scripts created successfully!")
print(f"Linux/Mac script length: {len(deployment_script)} characters")
print(f"Windows script length: {len(windows_deployment)} characters")