:: The master file that calls all other components.
:: Loops forever, always reading the cmd file for 
:: commands to execute.

@echo off
if exist last del last
if exist contr del contr
if exist turn set /p turn=<turn
if "%~1"=="l" goto :l

start /b cmd /c cont.bat 2>nul 1>&2
cmd /c ^""%~f0" l ^"
rem ^<nul
exit /b 0


:l

:: setup Var
set cmd=.
if exist cmd (
	set /p cmd=<cmd 
) else (
	echo . >cmd
)

:: Start moving
call mov.bat

:: orbit planets
:: orbit.py "%cd%\planets_c" %move_dis%

:: read commands
call com.bat

:: start view
call disp.bat

:: apply gravity
call grav.bat

:: check crash
call chkcrsh.bat

:: wait
timeout /t 1 /nobreak >nul

goto :l