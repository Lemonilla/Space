@echo off
echo.
echo.  Loading Game, Please Wait. . .
Python "bin\space.py" "%cd%\bin\save" "%cd%\bin\controls" "%cd%\bin\settings" "%cd%\bin\planets"
taskkill /im "python.exe" /f 1>nul 2>&1
pause