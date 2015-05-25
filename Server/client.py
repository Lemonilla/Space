#!usr/bin/python

import thread, math, sys, os, time, socket, json, pygame
from msvcrt import getch
from pygame.locals import *

username = "Lemonilla"
otherShips = {}

# Game Setup
print "Enter IP of the server you with to connect to."
server_IP = raw_input(">")

port = None
while port == None:
        for x in xrange(0,50):
                try:
                        print "\r                                    \r  Attempting socket %d" % (5000+x),
                        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        server.connect((server_IP,5000+x))
                        port = 5000+x
                        break
                except:
                        pass

server.sendall(username)
os.system('cls')


point = {}
point['x'] = 0
point['y'] = 0

lastMove = 'd'
size = 100 # query server for size
bullets = []
map_size=10


def getCommand():
        while True:
                cmd = getch()
                if cmd == 'w':
                        point['y']+=1
                if cmd == 's':
                        point['y']-=1
                if cmd == 'a':  
                        point['x']-=1
                if cmd == 'd':   
                        point['x']+=1
                if cmd == ' ':
                        bullets.append((lastMove,point['x'],point['y'],0))
                if not(cmd) == ' ':
                        lastMove = cmd
                if point['x'] > size:
                        point['x']-=size


thread.start_new_thread(getCommand,())
while True:

        # print map
        screen = ""

        for y in xrange(point['y']-map_size,point['y']+map_size+1):
                for x in xrange(point['x']+map_size,point['x']-map_size-1,-1):
                        if not(x == point['x'] and y == point['y']):
                                printed = False
                                for b in bullets:
                                        if x == b[1] and y == b[2]:
                                                screen+=" +"
                                                printed = True
                                if not(printed):
                                        screen+=" ."
                        else:
                                screen+=" @"
                screen+="\n"
        os.system('cls')
        print point
        print screen

        # move bullets
        index = 0
        for b in bullets:
                if b[0] == 'a':
                        bullets[index] = (b[0],b[1]+2,b[2],b[3]+1)
                if b[0] == 'd':
                        bullets[index] = (b[0],b[1]-2,b[2],b[3]+1)
                if b[0] == 'w':
                        bullets[index] = (b[0],b[1],b[2]-2,b[3]+1)
                if b[0] == 's':
                        bullets[index] = (b[0],b[1],b[2]+2,b[3]+1)
                index+=1

        # remove bullets out of bounds
        index=0
        for b in bullets:
                if b[3] > 5: 
                        bullets.pop(index)
                else:
                        index+=1

        # Check crash
        # otherShips = json.loads(server.recv(10000))
        for x in otherShips:            # (<Name>,<x>,<y>)
                if x[1] == point['x'] and x[2] == point['y']:
                        # Crash 
                        point['x'] = 0
                        point['y'] = 0




        print "sleep"

        time.sleep(0.1)





