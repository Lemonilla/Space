:: Displays information on current planet you are on.
:: Also allows for takeoff.

set /p pos_x=<pos_x
set /p pos_y=<pos_y
set /p pos_z=<pos_z
set /p vel=<vel
set /p theta_y=<theta_y
set /p theta_x=<theta_x
set /p planet=<crashrep

:: chart planet on map
echo %planet% >chart


call disp.bat
type "..\desc\%planet%"
echo.
echo.
echo Press G to leave planet. . .

:l
if exist cmd set /p cmd=<cmd
if /i not "%cmd%"=="g" goto :l
echo .>cmd

set /a pos_x+=5
set /a pos_y+=5
set /a pos_z+=5

rem echo 1 >vel
echo %pos_x% >pos_x
echo %pos_y% >pos_y
echo %pos_z% >pos_z

del crashrep
