import socket
import pickle
import json 

s = socket.socket()
hostname =[] 
port = []

for i in range(len(hostname)):
	s.connect((hostname[i],port[i]))

	while True:
		x= input("Enter message: ")
		s.send(x.encode())
		count = True
		while count == True:
			data = (s.recv(4096))  # receive response
			if data.decode() == 'break':
				count = False
			else:
				print('Received from server: ' + data.decode())  # show in terminal
