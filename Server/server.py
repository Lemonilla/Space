#!usr/bin/python

import socket, thread, time, json

currentUsers = {}
collidables = json.loads(json.dumps(""))
map_size = 100
maxPlayers = 50
current_IP = socket.gethostbyname(socket.gethostname())

def Timer():
        global waiting
        while True:
                waiting = False
                time.sleep(0.05)
                print "-"
                waiting = True
                time.sleep(0.1)

def Admin():
        print "Creating Admin port %s" % str(4999)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # set to reusable
        s.bind(('',4999)) # bind said socket
        s.listen(1)
        client, address = s.accept() # wait for new connection
        while True:
                data = client.recv(size)
                if data == "/UserList":
                        client.sendall(str(currentUsers))
                        print currentUsers

def Thread(port):
        global host, size, nextPort, waiting, maxPlayers
        print "\r                                                                       \rCreating User ports %d/%d" % (port-5000, maxPlayers),
        while True:
                try:

                        # Create socket and wait for connection
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket
                        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # set to reusable
                        s.bind(('',port)) # bind said socket
                        s.listen(1)
                        client, address = s.accept() # wait for new connection
                        username = client.recv(100)
                        print "Port %s connected to \"%s\" %s" % (str(port), username, str(address))
                        currentUsers[str(port)] = str(address) + " | " + username
                        client.sendall(str(map_size))

                        # Main loop, adds point to hashmap
                        while True:
                                data = client.recv(size)
                                print data+"+"
                                while waiting:
                                        pass
                                if data:
                                        # print "Recieved from port  %s (%s)" % (port, str(address[1]))
                                        data_json = json.loads(json.dumps(data))
                                        collidables.append(data_json)
                                        client.sendall(str(collidables))
                                        print collidables+"."
                                while not(waiting):
                                        pass

                        client.close()
                        s.close()
                        break
                except socket.error:           # Add something to check for timeouts \ Quitters
                        print "\"%s\" in port %s left %s" % (username,str(port),str(address))
                        client.close()
                        s.close()

                except:
                        print "\nFailed to Create port %s" % str(port)
                        client.close()
                        s.close()
                        time.sleep(1)
                        nextPort-=1
                        NeedNewThread = True
                        break


host = 'localhost'
nextPort = 5000
size = 1000000
hashMap = {}
waiting = True
print current_IP
thread.start_new_thread(Admin,())
thread.start_new_thread(Timer,())
time.sleep(0.5)

while nextPort < 5000+maxPlayers+1:
        thread.start_new_thread(Thread,(nextPort,))
        time.sleep(0.1)
        nextPort+=1
print ""

while True:
        pass


