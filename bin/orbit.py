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

# Import planets file into 2D Array named 'planets'
# And strip commented lines for faster looping
# How to read array: x,y,z,name,danger,grav,bound_sun_name
#   danger 0 = can't land, 1 = can safely land, 2 = crash
#   bound_sun_name=0 if self bound
#   smaller the grav the harder the pull
with open(sys.argv[1],'r') as x:
	planets = []
	for line in x:
		tmp = line.strip().split(',')
		if tmp[0] <> "0":
			planets.append(tmp)
x.close()


# debug, remove later
ppprint(planets)
x1=0
x2=2
y1=0
y2=2
z1=0
z2=2


# Find axis of revolution via theta_x and theta_y
# theta_x is the angle measurment off the x axis
# theta_y is the angle measurement off the y axis
# All points should be 90* from the axis of revolution

# angles are in radian, theta[0] is x, theta[1] is y
theta = [2 * math.pi - math.acos((x1-x2)/math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))),2 * math.pi - math.atan((z1-z2)/(y1-y2))]

print "xrad",theta[0]
print "yrad",theta[1]
print "xdeg",theta[0]/(2*math.pi)*360
print "ydeg",theta[1]/(2*math.pi)*360
print "\n"


# formula for orbit ellipse: (viewing x,y 2D plane)
# ((x-k)*cos(t)+(y-h)*sin(t))^2/a^2 + (y-h)*cos(t)-(x-k)*sin(t))^2/b^2 = 1
# where:
# t = acos((dis^2+dis_1^2+1)/2*dis)
# dis_1 = distance from x2,y2 to x1+1,y1
a = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))
b = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
dis_1 = math.sqrt((x2-(x1+1))*(x2-(x1+1))+(y2-y1)*(y2-y1))
dis = math.sqrt((x2-(x1))*(x2-(x1))+(y2-y1)*(y2-y1))
t = math.acos((dis*dis-dis_1*dis_1-1)/(2*dis))
r = sys.argv[2]
r = 1

print "dis:%d\ndis_1:%d\nt:%d\ns:%d" % (dis,dis_1,t,s)

# Need to solve this equation for x0 and then for y0 to get coordinates
# x^2+y^2-r^2 = ((x-x1)*math.cos(t)+(y-y1)*math.sin(t))^2/a+((y-y1)*math.cos(t)-(x-x1)*math.sin(t))^2/b-1


# z0 is then determined by this equation
# dis = math.sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0)+(z1-z0)*(z1-z0))

# the new coordinate for the planet is now x0,y0,z0 instead of x,y,z





# After a new point is determined, rewrite the process to loop through the planets array
# and write the destination point to a file called 'planets_c'.  If this file already exists
# then delete it, but only on the first pass through the loop.  grav.vbs\.bat and 
# chkcrsh.vbs\.bat will have to be rewritten to read 'planets_c' and not planets.