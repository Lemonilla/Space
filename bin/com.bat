:: Checks file cmd generated by cont.bat for which command to execute
:: and then executes that command.  Uses values in controls file for
:: key to commnand bindings.

setlocal EnableDelayedExpansion

set /p cmd=<cmd
set /p pos_x=<pos_x
set /p pos_y=<pos_y
set /p pos_z=<pos_z
set /p vel=<vel
set /p theta_y=<theta_y
set /p theta_x=<theta_x
for /f "delims=" %%A in (controls) do set %%A

if "%cmd%"=="." goto :end

if /i "%cmd%"=="%move_+_y_theta%" (
	set /a theta_y+=%delta_theta%
	echo !theta_y!>theta_y
)
if /i "%cmd%"=="%move_-_y_theta%" (
	set /a theta_y-=%delta_theta%
	echo !theta_y!>theta_y
)
if /i "%cmd%"=="%move_+_x_theta%" (
	set /a theta_x+=%delta_theta%
	echo !theta_x!>theta_x
)
if /i "%cmd%"=="%move_-_x_theta%" (
	set /a theta_x-=%delta_theta%
	echo !theta_x!>theta_x
)
if /i "%cmd%"=="%move_+_vel%" (
	set /a vel+=1
	echo !vel!>vel
)
if /i "%cmd%"=="%move_-_vel%" (
	set /a vel-=1
	echo !vel!>vel
)
if /i "%cmd%"=="%move_ping%" call ping.bat
if /i "%cmd%"=="%move_quit%" (
	echo .>contr
	timeout /t 1 /nobreak >nul
	exit
)

echo .>cmd

:end