:: Waits for user input and writes it to the cmd file.
:: Closes upon finding the contr file, created by cmd.bat
:: when the exit command is found.

setlocal enableDelayedExpansion
for /f %%a in ('copy /Z "%~dpf0" nul') do set "CR=%%a"
set "key="
for /l %%. in () do (
	set "key="
	for /f "delims=" %%A in ('xcopy /w %~f0 %~f0 2^>nul') do if not defined key set "key=%%A"
	set key=!key:~-1!
	echo !key!>cmd
	if exist contr exit
)
