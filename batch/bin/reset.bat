:: Resets the game.  Does not call any other functions.

if exist contr del contr
if exist last del last
if exist turn del turn
if exist cmd del cmd
if exist crashrep del crashrep

echo 0 >pos_x
echo 0 >pos_y
echo 0 >pos_z
echo 0 >vel
echo 0 >theta_x
echo 0 >theta_y
echo 0 >turn
:: echo delta_theta=10 >settings
:: echo delay=50 >>settings
:: echo grav=1 >>settings
echo vel=0 >last
echo .>cmd