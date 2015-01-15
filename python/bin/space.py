# space.py <save_status> <controls> <settings> <planets>

from msvcrt import getch
import thread
import time
import os
import sys
import math


global stack
stack = ['.','.']
pi = math.pi
loop=True



# Thread function for controller, adds key to stack
# Only works on windows machines
def ThreadingControl():
	while True:
		TC_cmd = getch()
		stack.append(TC_cmd)

def clscn():
	os.system('cls')

def move():
	status[0] = round((float(status[3])*math.cos(float(status[5]))*math.cos(float(status[4]))),2)+float(status[0])
	status[1] = round((float(status[3])*math.cos(float(status[5]))*math.sin(float(status[4]))),2)+float(status[2])
	status[2] = round((float(status[3])*math.sin(float(status[5]))),2)+float(status[1])

def contr():
	while True:
		global stack
		if len(stack) <> 0:
			cmdp=stack.pop()
		else:
			cmdp='.'
		if cmdp == controls[0]:
			status[5] = float(status[5]) + int(settings[0])
		if cmdp == controls[1]:
			status[5] = float(status[5]) - int(settings[0])
		if cmdp == controls[2]:
			status[4] = float(status[4]) + int(settings[0])
		if cmdp == controls[3]:
			status[4] = float(status[4]) - int(settings[0])
		if cmdp == controls[4]:
			status[3] = float(status[3]) + 1.0
		if cmdp == controls[5]:
			status[3] = float(status[3]) - 1.0
		if cmdp == controls[6]:
			pass # ping command not yet written
		if cmdp == controls[7]:
			endGame()
		if cmdp <> '.':
			disp()


def disp():
	#while True:
	tim_d = time.clock()
	clscn()

	ckDie()

	print "\n  Possition: [",
	print status[0],
	print "],[",
	print status[1],
	print "],[",
	print status[2],
	print "]"

	print "  Direction: y [",
	print status[5],
	print "], x [",
	print status[4],
	print "]"

	print "  Velocity : [",
	print status[3],
	print "]\n"

	while time.clock() - tim < 0:
		pass
		

def grav():
	for cur in planets:
		if cur[5] <> "0":
			dis = math.sqrt((status[0]-float(cur[0]))*(status[0]-float(cur[0]))+(status[1]-float(cur[1]))*(status[1]-float(cur[1]))+(status[2]-float(cur[2]))*(status[2]-float(cur[2])))
			wvec = dis / float(cur[5])
			if wvec < settings[3]:
				if dis == 0:
					dis = 0.0000000000001
				status[0] = status[0] + round((((status[0]-float(cur[0]))/dis)/float(cur[5])),2)
				status[1] = status[1] + round((((status[1]-float(cur[1]))/dis)/float(cur[5])),2)
				status[2] = status[2] + round((((status[2]-float(cur[2]))/dis)/float(cur[5])),2)

def chkcrsh():
	for cur in planets:
		if status[0] == float(cur[0]):
			if status[1] == float(cur[1]):
				if status[2] == float(cur[2]):
					if cur[4] <> "0":
						crash(cur[3])

def crash():
	pass

def endGame():
	clscn()
	print "\n  Saving Game, Please Wait. . ."
	save = open(sys.argv[1],'w')
	save.write(str(status[0]))
	save.write(",")
	save.write(str(status[1]))
	save.write(",")
	save.write(str(status[2]))
	save.write(",")
	save.write(str(status[3]))
	save.write(",")
	save.write(str(status[4]))
	save.write(",")
	save.write(str(status[5]))
	save.close()
	stack.append("DIE")
	sys.exit()

def ckDie():
	try:
		if len(stack) <> 0:
			tmp = stack.pop()
			stack.append(tmp)
			if tmp == "DIE":
				sys.exit()
	except UnboundLocalError:
		pass


#######################################################################################



# Load Game Data
# check if new game and import status
try:
	with open(sys.argv[1],'r') as argv_1:
		for line in argv_1:
			status=line.strip().split(',')
		argv_1.close()
except:
	# status = [pos_x, pos_y, pos_z, vel, theta_x, theta_y]
	status = [      0,     0,     0,   0,       0,       0]
	print "set"
# import controls
with open(sys.argv[2],'r') as argv_2:
	for line in argv_2:
		controls=line.strip().split(',')
	argv_2.close()
	# controls = [move_+_y_theta, move_-_y_theta, move_+_x_theta, move_-_x_theta, move_+_vel, move_-_vel, move_ping, move_quit, diplay_ex]
	# defaults = w,s,d,a,o,l,p,t,g

# import settings
with open(sys.argv[3],'r') as argv_3:
	for line in argv_3:
		settings=line.strip().split(',')
	argv_3.close()
	# Settings = [delta_theta, delay, display, wvec_lim, crash, orb_dis]
	# Defaults 10,50,1,2,1,1

# Import planets file into 2D Array named 'planets'
# And strip commented lines for faster looping
# planets = [x,y,z,name,danger,grav,bound_sun_name]
with open(sys.argv[4],'r') as argv_4:
	planets = []
	for line in argv_4:
		tmp = line.strip().split(',')
		if tmp[0] <> "0":
			planets.append(tmp)
	argv_4.close()

# declare and start threads
thread.start_new_thread(ThreadingControl,())
thread.start_new_thread(contr,())
# thread.start_new_thread(disp,())

# Start loop
while loop:

	tim = time.clock()
	# check Die
	ckDie()
	# move
	move()
	# gravity
	grav()
	# crash
	chkcrsh()
	# wait
	while time.clock() - tim < 1:
		pass
	disp()