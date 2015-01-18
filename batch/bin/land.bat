:: Displays crash information and 
:: calls reset for a new game.

set /p planet=<crashrep
for /f "tokens=1-4 delims=," %%A in (planets) do (
	if "%%D"=="%planet%" (
		echo %%A >pos_x
		echo %%B >pos_y
		echo %%C >pos_z
	)
)

if /i "%planet%"=="earth" call win.bat
call disp.bat

echo You've landed on %planet%
echo.
echo Press G to explore. . .

:l
if exist cmd set /p cmd=<cmd
if /i not "%cmd%"=="g" goto :l
echo .>cmd

call planet.bat
