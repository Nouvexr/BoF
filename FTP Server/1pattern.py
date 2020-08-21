#!/usr/bin/python
import socket
bytes = ("valor do pattern create aqui")
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
