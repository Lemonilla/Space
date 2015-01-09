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

REM setup Var
set cmd=.
if exist cmd (
	set /p cmd=<cmd 
) else (
	echo . >cmd
)

REM Start moving
call mov.bat

REM read commands
call com.bat

REM start view
call disp.bat

REM apply gravity
call grav.bat

REM check crash
call chkcrsh.bat

REM wait
timeout /t 1 /nobreak >nul

goto :l