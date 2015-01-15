@echo off
echo Loading Game, Please Wait. . .
"bin\space.py" "%cd%\bin\save" "%cd%\bin\controls" "%cd%\bin\settings" "%cd%\bin\planets"
cls
taskkill /im "python.exe" /f 1>nul 2>&1