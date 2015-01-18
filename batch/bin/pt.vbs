' cscript //nologo pt.vbs "%vel%" "%theta_x%" "%theta_y%" "%cd%\Pos_x" "%cd%\Pos_y" "%cd%\Pos_z" "%pos_x%" "%pos_y%" "%pos_z%"
'
' x = vel * cos(theta_x) * cos(theta_y)
' y = vel * cos(theta_x) * sin(theta_y)
' z = vel * sin(theta_x)
'
' Changes the position of the ship by using theta_x, theta_y, and vel to
' determine the end point of that movement.  Is applied before gravity.


dim x,y,z,vel,xTheta,yTheta,cd1,cd2,cd3,px,py,pz,log,pi
vel = Wscript.Arguments(0)
xTheta = Wscript.Arguments(1)
yTheta = Wscript.Arguments(2)
cd1 = Wscript.Arguments(3)
cd2 = Wscript.Arguments(4)
cd3 = Wscript.Arguments(5)
px = Wscript.Arguments(6)
py = Wscript.Arguments(7)
pz = Wscript.Arguments(8)
pi = 4 * ATN(1)

' convert degree's to radians
xTheta = xTheta * pi / 180
yTheta = yTheta * pi / 180


x = round((vel*cos(yTheta)*cos(xTheta)),2)+px
z = round((vel*cos(yTheta)*sin(xTheta)),2)+pz
y = round((vel*sin(yTheta)),2)+py


set objFSO=CreateObject("Scripting.FileSystemObject")
outFile=cd1
Set objFile = objFSO.CreateTextFile(outFile,True)
objFile.Write x & vbCrLf
objFile.Close

outFile=cd2
Set objFile = objFSO.CreateTextFile(outFile,True)
objFile.Write y & vbCrLf
objFile.Close

outFile=cd3
Set objFile = objFSO.CreateTextFile(outFile,True)
objFile.Write z & vbCrLf
objFile.Close