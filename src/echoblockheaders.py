#!/bin/python 

datafile = open(".\\data\\log1011.txt", "r") 

def isBlockHeaderLine(line): 
	# if line begins with 4 digits followed by a tab it's a block header line 
	bRval = False

	# Line must be at least 5 characters to be a block header line 
	if len(line) < 5: 
		return bRval

	firstFour = line[0:4]
	fifthChar = line[4]

	try: 
		firstFourAsNum = int(firstFour) 
		if (fifthChar == '\t'): 
			bRval = True 

	except ValueError: 
		bRval = False  

	return bRval 

for aLine in datafile:
	if isBlockHeaderLine(aLine):
		print(aLine) 

datafile.close() 
