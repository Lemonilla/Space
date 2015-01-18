:: apply gravity by calling grav.vbs

set /p pos_x=<pos_x
set /p pos_y=<pos_y
set /p pos_z=<pos_z
for /f "delims=" %%A in (settings) do set %%A

cscript //nologo grav.vbs "%cd%\planets" %pos_x% %pos_y% %pos_z% "%cd%" "%wvec_lim%" 1>v_grav