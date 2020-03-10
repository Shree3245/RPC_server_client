import socket
import time
from search import find_files
import apt

cache = apt.Cache()
if cache['mlocate'].is_installed:
    print ("package mlocate is installed")
else:
    command=['sudo apt install mlocate']
    output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
    output = output.decode()


listensocket = socket.socket()
Port = 8001
IP = socket.gethostname()
maxConnections = 999

#listensocket.close()
listensocket.bind(("",Port))
listensocket.listen(maxConnections)
print("Server Started at "+ IP + " on port: "+ str(Port))

clientsocket, address = listensocket.accept()
print("new connection made")

running = True
while  running:
    message = clientsocket.recv(1024).decode()
    #search = input("what are you searching for: ")
    x= (find_files(message))
    for i in x:
        clientsocket.send(i.encode())

    clientsocket.send('break'.encode())

