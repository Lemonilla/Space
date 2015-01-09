:: Displays crash information and 
:: calls reset for a new game.


echo You've Crashed!
echo.
echo Press G to Start Over. . .

:l
if exist cmd set /p cmd=<cmd
if /i not "%cmd%"=="g" goto :l

call reset.bat
