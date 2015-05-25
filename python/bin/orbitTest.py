import math
import time


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

p1 = [39000,47000,-3800]          # sun
p2 = [42666,47000,-14000]          # planet
'''
p1 = [ 0, 0, 0]
p2 = [10,10,10]
#'''

a = dis(p1,p2,3)
b = dis(p1,p2,2)

t = 0

while True:

        t = redT(t)

        x = (a*b) / (math.sqrt(a*a+b*b*math.tan(t)*math.tan(t)))
        y = (a*b*math.tan(t)) / (math.sqrt(a*a+b*b*math.tan(t)*math.tan(t)))

        if (0 < t and t < math.pi):     # in Quadrant I or II
                if y < 0:
                        y = y * -1      # make (+)
        else:                           # in Quadrant III or IV
                if y > 0:
                        y = y * -1      # make (-)
        if (0 < t and t < math.pi/2) or (math.pi*3/2 < t and t < math.pi*2):
                if x < 0:               # in Quadrants I or IV
                        x = x * -1      # make (+)
        else:
                if x > 0:               # in Quadrants II or III
                        x = x * -1      # make (-)

        # not comming out negative when it should
      #  try:
        print "d3=",a*a
        print "d2=",dis([x,y],p1,2)*dis([x,y],p1,2)
        print a*a-dis([x,y],p1,2)*dis([x,y],p1,2)
        if (dis([x,y,0],p2,3) > a):
                z = -1*math.sqrt(a*a-dis([x,y],p1,2)*dis([x,y],p1,2))
        else:
                z = math.sqrt(a*a-dis([x,y],p1,2)*dis([x,y],p1,2))
       # except:
               # z = 0


        # move from sun:
        x = x + p1[0]
        y = y + p1[1]
        z = z + p1[2]


        print "(",
        print x,
        print ",",
        print y,
        print ",",
        print z,
        print ")",
        print "",
        print t / math.pi
        
        t = t + math.pi / 12
        if t == math.pi * 2:
                t = 0
        time.sleep(1)