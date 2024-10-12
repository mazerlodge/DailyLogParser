#!/bin/python 

datafile = open("./data/log1011_mac.txt", "r") 

for aLine in datafile:
	print(aLine) 

datafile.close() 
