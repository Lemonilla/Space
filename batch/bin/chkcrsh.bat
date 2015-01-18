:: Checks for a conflict in possition with ship and any planets
:: calls upon chkcrsh.vbs for math and comparison.

set crashrep=
set /p pos_x=<pos_x
set /p pos_y=<pos_y
set /p pos_z=<pos_z
set /p vel=<vel

cscript //nologo chkcrsh.vbs "%cd%" %pos_x% %pos_y% %pos_z% "%cd%\planets" "%cd%\crashrep"


REM for after planet based movement is possable
if exist crashrep if %vel% GTR 0 call crash.bat
if exist crashrep if %vel% EQU 0 call land.bat
