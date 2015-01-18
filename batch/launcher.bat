:: Launches the game.  Displays the controls found
:: in the controls file.

@echo off

cd bin
for /f "delims=" %%A in (controls) do set %%A

echo.
echo.controls 
echo.
echo.  %move_+_y_theta% = + y theta
echo.  %move_-_y_theta% = - y theta
echo.  %move_+_x_theta% = + x theta
echo.  %move_-_x_theta% = - x theta
echo.  %move_+_vel% = + vel
echo.  %move_-_vel% = - vel
echo.  %move_ping% = ping
echo.  %move_quit% = quit
echo.
pause

call master.bat