#!/usr/bin/python2

import  socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",9999))


while  True :

	data=s.recvfrom(100)
	print  "message  from  client  :   ",data[0]
	print  "__________________________________"
	print  "__________________________________"
	print   "Client  address  :  ",data[1][0]
	print  "__________________________________"
	r=raw_input("type your reply :  ")
	s.sendto(r,data[1])
