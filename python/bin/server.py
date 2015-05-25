import socket, thread, time

currentUsers = {}
maxPlayers = 50


def Timer():
        global waiting
        while True:
                waiting = False
                time.sleep(0.5)
                waiting = True
                time.sleep(1)

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
        global NeedNewThread, host, size, nextPort, waiting
        while True:
                try:

                        # Create socket and wait for connection
                        print "Creating User port  %s" % str(port)
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket
                        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # set to reusable
                        s.bind(('',port)) # bind said socket
                        s.listen(1)
                        client, address = s.accept() # wait for new connection
                        print "Port %s connected to %s" % (str(port),str(address))
                        NeedNewThread = True
                        currentUsers[str(port)] = str(address)+" | "+client.recv(100)

                        # Main loop, adds point to hashmap
                        while True:
                                data = client.recv(size)
                                while waiting:
                                        pass
                                if data:
                                        #print "Recieved from port  %s (%s)" % (port, str(address[1]))
                                        data_array = data.split(",")
                                        if len(data_array) == 3:
                                                hashMap[address] = data_array
                                                #print "Updated %s's location to %s" % (address, data)
                                client.sendall(".")
                                while not(waiting):
                                        pass

                        client.close()
                        s.close()
                        break
                except socket.error:           # Add something to check for timeouts \ Quitters
                        print "%s in port %s left" % (str(address),str(port))
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
size = 1024
NeedNewThread=True;
hashMap = {}
waiting = True
thread.start_new_thread(Admin,())
thread.start_new_thread(Timer,())
time.sleep(0.5)

while nextPort < 5500:
        if NeedNewThread:
                thread.start_new_thread(Thread,(nextPort,))
                nextPort+=1
                NeedNewThread = False


