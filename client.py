import socket
import pickle
import json 

s = socket.socket()
hostname =[] 
port = []
x= input("Enter message: ")
for i in range(len(hostname)):
	s.connect((hostname[i],port[i]))

	while True:
		
		s.send(x.encode())
		count = True
		while count == True:
			data = (s.recv(4096))  # receive response
			if data.decode() == 'break':
				count = False
			else:
				print('Received from server: ' + data.decode())  # show in terminal
		break
	s.close()
