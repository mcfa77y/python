#!/usr/bin/python
import sys, re

def main():
	fn = sys.argv[1]
	index = open(fn, 'r')
	# this gets variable names
	# and initalizes them
	#indexTransformed = open(fn+".out",'w')
	d=dict()
	# get all errors
	for line in index:
		lina = filterType(line,'ERROR',2)
		if len(lina)<=0:
			continue
		d[line]=""
		for line2 in index:
			#print "just next line:"+str(len(line2))+"\n"+line2+"\n:END"
			d[line]=line2
			break
		# get all the sub lines 'at *'
		for line2 in index:
			lina2= filterType(line2,'at',0)
			if len(lina2)<=0:
				lina2= filterType(line2,'Caused',0)
			if len(lina2)<=0:
				print "\tno love line2: "+line2
				break
			#print "\t"+line2
			d[line]=d[line]+line2
		#print "\td[line]: "+d[line]
	index.close()
	printMap(d)
# checks type of line at k[index]
# and if it equals tipo then it returns the line
# otherwise you get an empty string
def filterType(line,tipo,index):
	if len(line)>0:
		k=line.split()
	else:
		return ""
	if len(k)>index:
		typo = k[index]
		if typo==tipo:
			return line
	return ""

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
