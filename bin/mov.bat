:: Changes ship position through the use of pt.vbs

set /p pos_x=<pos_x
set /p pos_y=<pos_y
set /p pos_z=<pos_z
set /p vel=<vel
set /p theta_y=<theta_y
set /p theta_x=<theta_x

cscript //nologo pt.vbs "%vel%" "%theta_x%" "%theta_y%" "%cd%\Pos_x" "%cd%\Pos_y" "%cd%\Pos_z" "%pos_x%" "%pos_y%" "%pos_z%" 
