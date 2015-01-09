
REM load data
set /p pos_x=<pos_x
set /p pos_y=<pos_y
set /p pos_z=<pos_z
set /p vel=<vel
set /p theta_y=<theta_y
set /p theta_x=<theta_x
set /p turn=<turn
for /f "delims=" %%A in (settings) do set %%A


if not exist last goto :disp
for /f "delims=" %%A in (last) do set l_%%A
if "%pos_x: =%"=="%l_pos_x: =%" (
	if "%pos_y: =%"=="%l_pos_y: =%" (
		if "%pos_z: =%"=="%l_pos_z: =%" (
			if "%vel: =%"=="%l_vel: =%" (
				if "%theta_x: =%"=="%l_theta_x: =%" (
					if "%theta_y: =%"=="%l_theta_y: =%" (
						if not "%display%"=="1" goto :end
))))))
:disp
	cls
	echo.
	echo.  Possition: [%pos_x: =%],[%pos_y: =%],[%pos_z: =%]
	echo.  Direction: y [%theta_y: =%], x [%theta_x: =%]
	echo.  Velocity : [%vel: =%]
	echo.
if "%display%"=="1" (
	if exist v_grav type v_grav
	echo.
)
:end