# Call as 'orbit.py "%cd%\planets" %move_dis%'

import sys
import math

# Debug function to print 2D array in a table format
def ppprint(arr):
	for l in arr:
		ppprint_tmp=""
		for x in l:
			ppprint_tmp="%s%s\t" % (ppprint_tmp,x)
		print ppprint_tmp
		del(ppprint_tmp)



def MovePlanet_stdout(move_planet,move_Sun):
	x1 = float(move_planet[0])
	y1 = float(move_planet[1])
	z1 = float(move_planet[2])
	x2 = float(move_Sun[0])
	y2 = float(move_Sun[1])
	z2 = float(move_Sun[2])


	# formula for orbit ellipse: (viewing x,y 2D plane)
	# ((x-k)*cos(t)+(y-h)*sin(t))^2/a^2 + (y-h)*cos(t)-(x-k)*sin(t))^2/b^2 = 1
	# where:
	# t = acos((dis^2+dis_1^2+1)/2*dis)
	# dis_1 = distance from x2,y2 to x1+1,y1
	a = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))
	b = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
	dis_1 = math.sqrt((x2-(x1+1))*(x2-(x1+1))+(y2-y1)*(y2-y1))
	dis = math.sqrt((x2-(x1))*(x2-(x1))+(y2-y1)*(y2-y1))


	# Fix out of bounds by lowering it into range and adding pi after computation
	try:
		t = math.acos((dis*dis-dis_1*dis_1-1)/(2*dis))
	except:
		t = math.acos((dis*dis-dis_1*dis_1-1)/(2*dis)+1)+math.pi

	# Assign g as 2nd argument
	try:
		g = sys.argv[2]
	except:
		g = math.pi/4



	# ((cos(t)*cos(t))/(a*a)+(sin(t)*sin(t))/(b*b))*x*x)-2*cos(t)*sin(t)*(1/(a*a)-1/(b*b))*y*x+((cos(t)*cos(t))/(a*a)+(sin(t)*sin(t))/(b*b))*y*y=1
	# where g = degrees of rotation and the sign is (+) if pi/2 > g > -pi/2
	x0 = (a*b)/(math.sqrt(a*a*math.tan(g)*math.tan(g)*math.sin(t)*math.sin(t)-2*b*b*math.tan(g)*math.cos(t)*math.sin(t)+2*a*a*math.tan(g)*math.cos(t)*math.sin(t)+b*b*math.tan(g)*math.tan(g)*math.cos(t)*math.cos(t)+b*b*math.cos(t)*math.cos(t)))
	y0 = (a*b*math.tan(g))/(math.sqrt(a*a*math.tan(g)*math.tan(g)*math.sin(t)*math.sin(t)-2*b*b*math.tan(g)*math.cos(t)*math.sin(t)+2*a*a*math.tan(g)*math.cos(t)*math.sin(t)+b*b*math.tan(g)*math.tan(g)*math.cos(t)*math.cos(t)+b*b*math.cos(t)*math.cos(t)))
	

	# z0 is then determined by this equation
	# dis = math.sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0)+(z1-z0)*(z1-z0))
	# from http://www.quickmath.com
	temp=-y0*-y0+2*y1*y0-y1*y1-x0*x0+2*x1*x0-x1*x1+dis*dis
	if temp < 0:
		temp=-temp
	try:
		z0=z1-math.sqrt(temp)
	except:
		z0=z1+math.sqrt(temp)


	# the new coordinate for the planet is now x0,y0,z0
	print move_planet[3]
	print "(",
	print x1,
	print ",",
	print y1,
	print ",",
	print z1,
	print ")\n(",
	print x2,
	print ",",
	print y2,
	print ",",
	print z2,
	print ")\n(",
	print x0,
	print ",",
	print y0,
	print ",",
	print z0,
	print ")"


# Debug statement
MovePlanet_stdout([0,0,0,"orgin"],[10,10,10,"1x1x1"])
'''

# Import planets file into 2D Array named 'planets'
# And strip commented lines for faster looping
with open(sys.argv[1],'r') as x:
	planets = []
	for line in x:
		tmp = line.strip().split(',')
		if tmp[0] <> "0":
			planets.append(tmp)
x.close()




# Loop through planets moving each around their bound Sun
# If the bounds sun's value is "0", this is a sun and should be skipped
for planet in planets:
	if planet[6] == "0":
		pass
	else:
		for Sun in planets:
			if Sun[3] == planet[6]:
				MovePlanet_stdout(planet,Sun)
			else:
				pass

'''


# After a new point is determined, rewrite the process to loop through the planets array
# and write the destination point to a file called 'planets_c'.  If this file already exists
# then delete it, but only on the first pass through the loop.  grav.vbs\.bat and 
# chkcrsh.vbs\.bat will have to be rewritten to read 'planets_c' and not planets.