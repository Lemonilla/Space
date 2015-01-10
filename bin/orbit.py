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
x_1=0
x_2=2
y_1=0
y_2=2
z_1=0
z_2=2


# Find axis of revolution via theta_x and theta_y
# theta_x is the angle measurment off the x axis
# theta_y is the angle measurement off the y axis
# All points should be 90* from the axis of revolution

# angles are in radian, theta[0] is x, theta[1] is y
theta = [2 * math.pi - math.acos((x_1-x_2)/math.sqrt((x_1-x_2)*(x_1-x_2)+(y_1-y_2)*(y_1-y_2)+(z_1-z_2)*(z_1-z_2))),2 * math.pi - math.atan((z_1-z_2)/(y_1-y_2))]

print "x_rad",theta[0]
print "y_rad",theta[1]
print "x_deg",theta[0]/(2*math.pi)*360
print "y_deg",theta[1]/(2*math.pi)*360


# Compute next point by using some kind of trig
# so far it looks like you need to know circle around axis of revolution
# then create a triangle with points on the current location, the sun
# and the last point on destination.  The distance from sun to both points
# should not change, and the distance between current location and destination
# is passed as sys.argv[2], drawn fromt he %move_dis% variable in settings.

# However it should be noted that the triangle is working with the axis of revolution
# and not with the regular xyz axis.  This has so far thrown off my math.


# After a new point is determined, rewrite the process to loop through the planets array
# and write the destination point to a file called 'planets_c'.  If this file already exists
# then delete it, but only on the first pass through the loop.  grav.vbs\.bat and 
# chkcrsh.vbs\.bat will have to be rewritten to read 'planets_c' and not planets and 
# master.bat will need to have orbit.py added to it after mov.bat.