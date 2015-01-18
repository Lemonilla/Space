' chkcrsh.vbs "%cd%" %pos_x% %pos_y% %pos_z% "%cd%\planets" "%cd%\crashrep" 
'
' Checks for possition conflict between ship and the planets found in the planets file.

dim x,y,z,working_x,working_y,working_z,cd,errorlevel,file,arrline,cd1,lastX,lastY,lastZ,working_name,line,listFile

errorlevel=0
cd=Wscript.Arguments(0)
x=round(Wscript.Arguments(1),0)
y=round(Wscript.Arguments(2),0)
z=round(Wscript.Arguments(3),0)
file=Wscript.Arguments(4)
cd1=Wscript.Arguments(5)

Set fso = CreateObject("Scripting.FileSystemObject")
Set listFile = fso.OpenTextFile(file)
do until listFile.AtEndOfStream 
	line = listFile.ReadLine()

	'setup variables
	arrline=Split(line,",")
	working_x=round(arrline(0),0)
	working_y=round(arrline(1),0)
	working_z=round(arrline(2),0)
	working_name=arrline(3)
	working_dang=arrline(4)

	if x=working_x then
		if y=working_y then
			if z=working_z then
				if working_dang <> 0 Then
					set objFSO=CreateObject("Scripting.FileSystemObject")
						outFile=cd1
						Set objFile = objFSO.CreateTextFile(outFile,True)
						objFile.Write working_name & vbCrLf
					objFile.Close
				end if
			end if
		end if
	end if
loop