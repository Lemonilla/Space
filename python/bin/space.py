# space.py <save_status> <controls> <settings> <planets>

from msvcrt import getch
import thread
import time
import os
import sys
import math
import socket


global stack
ships = {}
serverWait = True
stack = ['.']
pi = math.pi
username = "Lemonilla"
maxPlayer = 50


###########################################################################################################################################

def dis(p1,p2,d):
        if (d==1):
                return p1[0]-p2[0]
        if (d==2):
                return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))
        if (d==3):
                return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1])+(p1[2]-p2[2])*(p1[2]-p2[2]))
def redT(t):
        if t > 2*math.pi:
                t = t - 2*math.pi
                t = redT(t)
        return t
        
def distance(x1,y1,z1,x2,y2,z2):
	return math.sqrt((float(x1)-float(x2))*(float(x1)-float(x2))+(float(y1)-float(y2))*(float(y1)-float(y2))+(float(z1)-float(z2))*(float(z1)-float(z2)))

# Thread function for controller, adds key to stack
# Only works on windows machines
def ThreadingControl():
	while True:
		TC_cmd = getch()
		stack.append(TC_cmd)

def serverConnection():
	global ships
	try:
		server.sendall(str(status[0])+","+str(status[1])+","+str(status[2]))
		ships = server.recv(1024)
	except:
		print "Connection Lost."
		quit()
	serverWait = False


def clscn():
	#return 0
	os.system('cls')

def checkLandingGear():
	return
	if bool(status[7]) == True:
		if int(status[3]) > 1:
			pass	# landing gear tear off

def land():
	pass

def move():


	if status[6] < 0:
		status[3]=0

	old_status = [status[0],status[1],status[2]]

	status[0] = round((float(status[3])*math.cos(float(status[5]))*math.cos(float(status[4]))),2)+float(status[0])
	status[1] = round((float(status[3])*math.cos(float(status[5]))*math.sin(float(status[4]))),2)+float(status[1])
	status[2] = round((float(status[3])*math.sin(float(status[5]))),2)+float(status[2])


	if distance(old_status[0],old_status[1],old_status[2],status[0],status[1],status[2]) > 0.8:
		if status[3] > 0:
			status[6] = float(status[6]) - (0.1*float(status[3]))
	checkLandingGear()


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
			if status[6] < 0:
				status[3]=0
		if cmdp == controls[5]:
			status[3] = float(status[3]) - 1.0
			if status[6] < 0:
				status[3]=0
		if cmdp == controls[6]:
			pass # ping command not yet written
		if cmdp == controls[7]:
			endGame()
		if cmdp == controls[8]:
			pass # no idea what this command does
		if cmdp <> '.':
			disp()

		# debug backdoor
		if cmdp == 'N':
			crash("Adminius")


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

	print status[6]

	while time.clock() - tim < 0:
		pass

# Map
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  X  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  0  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
#  .  .  .  .  .  .  .  .  .  .  .  .  .  .
		

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
		if status[0] == int(cur[0]):
			if status[1] == int(cur[1]):
				if status[2] == int(cur[2]):
					if cur[4] <> "0": # change this line to impliment landing. 0 = gas giant, 1 = habital, 2 = star\dangerous
						
						if bool(status[7]) <> True:
							crash(cur[3])
						else:
							land()


def crash(name):
	clscn()
	print "\n  Your crashed into %s." % name

	save = open(sys.argv[1],'w')
	save.write("0,0,0,0,0,0")
	save.close()

	# shutdown Game
	stack.append("DIE")
	sys.exit()


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
	save.write(",")
	save.write(str(status[6]))
	save.close()

	clscn()

	stack.append("DIE")
	sys.exit()


def ckDie():
	try:
		if len(stack) <> 0:
			tmp = stack.pop()
			stack.append(tmp)
			if tmp == "DIE":
				sys.exit()
	except UnboundLocalError:	# required for empty stack case
		pass		  

def orbit():
	return None
	# a = angle in radians
	# cx,xy = center of circle
	x = cx + r * cos(a)
	y = cy + r * sin(a)



###########################################################################################################################################



# Load Game Data
# check if new game and import status
try:
	with open(sys.argv[1],'r') as argv_1:
		for line in argv_1:
			status=line.strip().split(',')
		argv_1.close()
except:
	# status = [pos_x, pos_y, pos_z, vel, theta_x, theta_y, fual,LandingGear]
	status = [      0,     0,     0,   0,       0,       0,100.0,      False]

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
	# Defaults 10,50,1,2,1,12

# Import planets file into 2D Array named 'planets'
# And strip commented lines for faster looping
# planets = [x,y,z,name,danger,grav,bound_sun_name]
with open(sys.argv[4],'r') as argv_4:
	planets = []
	for line in argv_4:
		tmp = line.strip().split(',')
		if tmp[3] <> "0":
			planets.append(tmp)
	argv_4.close()


def ServerControl():
	global ships,serverWait
	server.sendall(str(status[0])+","+str(status[1])+","+str(status[2]))
	ret = server.recv(1000000)
#	print str(ret)
	# parse ret into a hashmap and replace ships
	serverWait = False




# connect to server
for x in xrange(0,maxPlayer):
	try:
		print "\r                                    \r  Attempting socket %d" % (5000+x),
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.connect(('localhost',5000+x))
		port = 5000+x
		break
	except:
		pass
server.sendall(username)
print ""

# declare and start threads
thread.start_new_thread(ThreadingControl,())
thread.start_new_thread(contr,())
thread.start_new_thread(ServerControl,())



# Start main loop
print "  Connected to port %d" % port
while True:
	tim = time.clock()

	ckDie()
	orbit()
	move()
	chkcrsh()
	grav()

	while serverWait:
		serverConnection()
		pass
	serverWait = True
	disp()