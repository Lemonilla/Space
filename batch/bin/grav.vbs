' grav "%cd%\planets" %pos_x% %pos_y% %pos_z% "%cd%" %wvec_lim%
'
' Applies gravity for each planet withing range.  Uses wvec_lim variable
' from files settings to determine range.  if dis/grav < wvrc_lim then
' gravity is applied. Value of grav is taken from file settings as well.

dim x,y,z,working_x,working_y,working_z,dis,wvec,vec_x,vec_y,vec_z,x1,y1,z1,grav,wvec_lim,planets,name
dim file,fso,listFile,line,arrline
file=Wscript.Arguments(0)
x=Wscript.Arguments(1)
y=Wscript.Arguments(2)
z=Wscript.Arguments(3)
cd1=Wscript.Arguments(4)
wvec_lim=CSng(Wscript.Arguments(5))
vec_x=0
vec_y=0
vec_z=0


' Loop through planets list
Set fso = CreateObject("Scripting.FileSystemObject")
Set listFile = fso.OpenTextFile(file)
do while not listFile.AtEndOfStream 
	line =  listFile.ReadLine()


	' setup variables
	arrline=Split(line,",")
	working_x=arrline(0)
	working_y=arrline(1)
	working_z=arrline(2)
	name=arrline(3)
	grav=arrline(5)

	' Ignore all planets with 0 gravity
	' These are comments in the file
	If grav <> 0 Then
	
		'find distance
		dis=Sqr((x-working_x)*(x-working_x)+(y-working_y)*(y-working_y)+(z-working_z)*(z-working_z))
		wvec=dis/grav
	
		Wscript.echo name &"	|	"& round(wvec,2)


		'determine adding
		If wvec < wvec_lim Then
	
			' Find Vector length
			if dis=0 then dis=.0000001
			x1=round(((working_x-x)/dis/grav),2)
			y1=round(((working_y-y)/dis/grav),2)
			z1=round(((working_z-z)/dis/grav),2)

			' Display Data
			Wscript.echo "		"&x1&"	"&y1&"	"&z1

			' Add vector length to sum
			vec_x=vec_x+x1
			vec_y=vec_y+y1
			vec_z=vec_z+z1
	
		End If
	End If
Loop

' Make corrections on possition
x=x+vec_x
y=y+vec_y
z=z+vec_z

' Write to Files
set objFSO=CreateObject("Scripting.FileSystemObject")
outFile=cd & "pos_x"
Set objFile = objFSO.CreateTextFile(outFile,True)
objFile.Write x & vbCrLf
objFile.Close

outFile=cd & "pos_y"
Set objFile = objFSO.CreateTextFile(outFile,True)
objFile.Write y & vbCrLf
objFile.Close

outFile=cd & "pos_z"
Set objFile = objFSO.CreateTextFile(outFile,True)
objFile.Write z & vbCrLf
objFile.Close