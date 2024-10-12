#!/bin/python 

datafile = open("./data/log1011_mac.txt", "r") 

for aLine in datafile:
	timeStamp = aLine[0:4]
	if (timeStamp.isnumeric()):
		print(timeStamp)

datafile.close() 
