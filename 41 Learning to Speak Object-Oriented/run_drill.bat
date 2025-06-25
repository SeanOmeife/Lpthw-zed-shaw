@echo off
echo Choose mode:
echo 1. Code first
echo 2. English first
set /p mode=Enter 1 or 2:

if "%mode%" == "1"(
    python ex41.py
)
else if "%mode%" == "2"(
    python ex41.py english
)
else (
    echo Invalid choice.
)
pause