#!/usr/bin/python2

import  socket,os,commands,time,sys

sip="192.168.10.171"
sport=1234

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# telnet  server  username  
user=raw_input("enter  user name :  ")
password=raw_input("enter  user password  :  ")



s.sendto(user,(sip,sport))
s.sendto(password,(sip,sport))

print  s.recvfrom(100)
while  True :
	cmd=raw_input("[root@station171 ]# ")
	s.sendto(cmd,(sip,sport))
	print   s.recvfrom(100)[0]


