#!/usr/bin/python
import socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.2.108",110))
	r = s.recv(1024)
	print r

	s.send("USER oiiiiii\r\n")
	r = s.recv(1024)
	print r

	s.send("PASS tchauuuu\r\n")
	r = s.rec(1024)
	print r

	s.send("QUIT\r\n")
	r = s.recv(1024)
	print r
except:
	print "Erro ao conectar"
