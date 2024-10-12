#!/bin/python 

datafile = open("./data/log1011_mac.txt", "r") 

def getDecimalTime(timeString):
	# Given a 4 digit time string, e.g. 1145 or 1430, 
	#   return a decimal value, e.g. 11.75 or 14.5
	rval = -1.0

	# confirm the time provided is numeric and length 4
	bValidTime = False 
	if (timeString.isnumeric() and len(timeString) == 4):
		bValidTime = True
	else:
		return(rval) 	
	
	# convert the 4 digit time to a decimal value 
	rval = int(timeString[0:2]) + int(timeString[2:4])/60

	return(rval) 


for aLine in datafile:
	timeStamp = aLine[0:4]
	if (timeStamp.isnumeric()):
		decimalTime = getDecimalTime(timeStamp)
		print(f"{timeStamp} aka {decimalTime}")

datafile.close() 
