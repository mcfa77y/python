#!/usr/bin/python
import sys, re
from sets import Set

def main():
	fn = sys.argv[1]
	index = open(fn, 'r')
	# this gets variable names
	# and initalizes them
	indexTransformed = open(fn+".out",'w')
	for line in index:
		line=line.split()[0]
		if(line.find("HasBeenSet")>=0):
			line = line +" = true;"
		else:
			line = "this."+line+" = other."+line+";"
		indexTransformed.writeTo(line+"\n")
	index.close()

def printMap(m):
	i=0
	l = m.keys()
	l.sort()	
	for key in l:
		value = m[key]
		if value>1:
			i+=1
			print i,str(value)+"\t"+key
#merge sort
def ms(rist):
	print len(rist)
	if len(rist)<2:
		return rist 
	else:
		middle = len(rist)/2
		left = ms(rist[:middle])
		right = ms(rist[middle:])
		return merge(left, right)

# merge this is where the main logic occurs
def merge(a, b):

	if(a!=None and b!=None):
		print "a\n"+str(a)
		print "\nb\n"+str(b)
		print ""
		# if the list size is one then 
		# file to set
		# else use the already merged set
		if len(a)==1:
			aSet = fileToSet(a[0])
		else:
			aSet =Set(a[1])
		if len(b)==1:
			bSet = fileToSet(b[0])
		else:
			bSet=Set(b[1])
		# antiDiff the two sets
		results = [a,b],antiDiff(aSet,bSet)
	elif a!=None:
		aSet = fileToSet(a[0])
		results = a, aSet
	else:
		bSet = fileToSet(b[0])
		results = b,bSet
	return results

def fileToMap(fn):
	d=dict()
	f = open(fn,'r')
	for line in f:
		line=line.split()[0]
		if d.get(line):
			d[line]=d[line]+1
		else:
			d[line]=1
	return d

# turn from a file name turn the contents
# into a set
def fileToSet(fn):
	s=Set()
	f = open(fn,'r')
	for line in f:
		line=line.split()[0]
		s.add(line)
	return s

# get the intersection of the sets
def antiDiff(s0,s1):
	s3 = list(s0&s1)
	s3.sort()
	print ""
	i=0
	for x in s3:
		i+=1
		print str(i)+" "+x
	print "\ntotal matches: "+str(len(s3))
	return s3

main()