#!/usr/bin/python
import sys, re
from sets import Set

def main():
	index = open(sys.argv[1], 'r')
	# this gets file names from an index file
	# and puts them into a list
	f=[]
	for line in index:
		line = "/home/jlau/"+line
		line = re.sub('\r\n','',line)
		f.append(line)

	# gets frequency of words in files 
	mTotal=dict()
	for ff in f:
		print ff
		m=fileToMap(ff)
		#printMap(m)
		mTotal = combineMap(mTotal,m)
	printMap(mTotal)

def printMap(m):
	global maxKeyLength
	i=0
	l = m.keys()
	l.sort()	
	for key in l:
		value = m[key]
		if value>1:
			i+=1
			q="*"*value
			print repr(i).rjust(2),repr(value).rjust(2)+"\t"+repr(key).rjust(maxKeyLength)+" "+q
def fileToMap(fn):
	d=dict()
	f = open(fn,'r')
	for line in f:
		if len(line.split())>0:
			line=line.split()[0]
		line = re.sub('\r\n','',line)
		if len(line)==0:
			continue
		addToMap(d,line,1)
	f.close()
	return d

def combineMap(m0, m1):
	#print m0,m1
	for key in m0.keys():
		addToMap(m1,key,m0[key])

	return m1

def addToMap(m,key,value):
	global maxKeyLength
	if m.get(key):
		m[key]=m[key]+value
	else:
		m[key]=value
		if len(key)>maxKeyLength:
			maxKeyLength=len(key)
maxKeyLength=0
print maxKeyLength
main()
