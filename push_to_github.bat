@echo off
echo.
echo ============================================
echo  GitHub Repository Setup Helper
echo ============================================
echo.
echo Step 1: Creating the GitHub repository manually...
echo Please go to: https://github.com/new
echo.
echo Repository settings:
echo - Repository name: money
echo - Visibility: Private
echo - DO NOT initialize with README
echo.
echo Press any key after you've created the repository...
pause
echo.
echo Step 2: Pushing your code to GitHub...
echo.

REM Check if we have commits
git log --oneline -1 >nul 2>&1
if errorlevel 1 (
    echo Error: No commits found. Please commit your changes first.
    pause
    exit /b 1
)

REM Check if remote origin exists
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo Adding remote origin...
    git remote add origin https://github.com/dafkenaniah/money.git
) else (
    echo Remote origin already exists.
)

echo.
echo Pushing to GitHub...
git push -u origin master
if errorlevel 1 (
    echo.
    echo Trying with main branch...
    git push -u origin main
)

if errorlevel 1 (
    echo.
    echo Push failed. This might be because:
    echo 1. The repository doesn't exist on GitHub yet
    echo 2. You need to authenticate with GitHub
    echo 3. The branch name is different
    echo.
    echo Try running: git push -u origin HEAD
    pause
) else (
    echo.
    echo ============================================
    echo  SUCCESS! Your code is now on GitHub!
    echo  Repository URL: https://github.com/dafkenaniah/money
    echo ============================================
)

echo.
