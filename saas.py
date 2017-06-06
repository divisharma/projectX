#!/usr/bin/python2


import  os
x="""
Press  1  to get  FIrefox
Press  2  to  get  gedit 
"""
print  x
ch=raw_input()

if  ch  ==  '1' :
	os.system('firefox')
elif   ch  ==   '2'  :
	os.system('gedit')

else  :
	print  "Wrong choice "




