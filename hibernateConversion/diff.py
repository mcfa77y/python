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

	f0 = open(f[0], 'r')
	f1 = open(f[1], 'r')
	# run mergesort
	ms(f)	

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
	s3 = list(s0-s1)
	s3.sort()
	print ""
	i=0
	for x in s3:
		i+=1
		print str(i)+" "+x
	print "\ntotal matches: "+str(len(s3))
	return s3

main()
