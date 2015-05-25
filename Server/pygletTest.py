from pyglet.window import Window,key
from pyglet import app
from pyglet.text import Label
from pyglet.clock import schedule_interval
import random, socket



Keys = [False,False,False,False,False] # [W,A,S,D,FIRE]
last = Keys

bullets = []
bullet_speed = 3
bullet_life = 5


point = {'x':0,'y':0}
size = 100 # query server for size
map_size=10

username = "Lemonilla"


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
print "\n  Waiting for server to respond. . ."
size = server.recv(10)
print   "  Launching Game. . ."

win = Window()
ScreenMap = Label("")


def move():
        global Keys,point,last
        if Keys[0] == True: # W
                point['y']+=1
        if Keys[1] == True: # A
                point['x']-=1
        if Keys[2] == True: # S
                point['y']-=1
        if Keys[3] == True: # D
                point['x']+=1
        if Keys[4] == True: # SPACE
                Fire()
        last = Keys

def Fire():
        global last
        # bullet = [x, y, distance to travel, direction]
                                        #     (W, A, S, D, FIRE)
        bullets.append((point['x'], point['y'], bullet_life, list(last)))

def decay():
        global bullets
        index=0
        for b in bullets:
                bullet_x=b[0]
                bullet_y=b[1]

                if b[3][0] == True:
                        bullet_y=b[1]+bullet_speed
                if b[3][2] == True:
                        bullet_y=b[1]-bullet_speed
                if b[3][1] == True:
                        bullet_x=b[0]-bullet_speed
                if b[3][3] == True:
                        bullet_x=b[0]+bullet_speed
                if b[2]-1 > 0:
                        bullets[index] = (bullet_x, bullet_y, b[2]-1, b[3])
                else:
                        bullets[index] = None
                index+=1
        while bullets.count(None) > 0:
                bullets.remove(None)

def check_crash():
        return
        send = "{\'"+str(username)+"\':"+str(bullets)+"}"
        server.sendall(send)
        print send
        # Query Server for Colidables list
        collidables = server.recv(1000000)
        print collidables

def buildScreen():
        global ScreenMap, win, point, map_size
        screen = ""
        for y in xrange(point['y']+map_size+1,point['y']-map_size,-1):
                for x in xrange(point['x']-map_size-1,point['x']+map_size):
                        if not(x == point['x'] and y == point['y']):
                                printed = False
                                for b in bullets:
                                        if x == b[0] and y == b[1]:
                                                if not(printed):
                                                        screen+="  +"
                                                        printed = True
                                if not(printed):
                                        screen+="  . "
                        else:
                                screen+=" @"
                screen+="\n"
        ScreenMap = Label(str(screen), x=0, y=win.height, width=win.width, multiline=True)


@win.event
def on_key_press(symbol, modifiers):
        global Keys,ScreenMap
        if symbol == key.A:
                Keys[1] = True
        if symbol == key.S:
                Keys[2] = True
        if symbol == key.W:
                Keys[0] = True
        if symbol == key.D:
                Keys[3] = True
        if symbol == key.SPACE:
                Keys[4] = True
        win.clear()
        ScreenMap.draw()

@win.event
def on_key_release(symbol, modifiers):
        global Keys,ScreenMap
        if symbol == key.A:
                Keys[1] = False
        if symbol == key.S:
                Keys[2] = False
        if symbol == key.W:
                Keys[0] = False
        if symbol == key.D:
                Keys[3] = False
        if symbol == key.SPACE:
                Keys[4] = False
        win.clear()
        ScreenMap.draw()
        


def update(dt):
        global Keys,ScreenMap,point

        buildScreen()
        move()
        decay()
        check_crash()

        win.clear()
        ScreenMap.draw()

        point_label = Label("%d,%d" % (point['x'],point['y']))
        point_label.draw()
 

schedule_interval(update, 0.1)

app.run()
