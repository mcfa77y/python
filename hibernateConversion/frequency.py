#!/usr/bin/python
import sys, re, SearchReplace
from sets import Set
DO_MULTI = True
def main():
	if len(sys.argv)>1:
		index = open(sys.argv[1], 'r')
	else:
		index = open('input/index.txt','r')
	resultMap = dict()
	for line in index:
		#print line
		line = line.strip()
		
		mz = fileToMap(line)
		combineMap(mz,resultMap)
	#mz = fileToMap(sys.argv[1])
	printMap(resultMap)
	
def printMap(m):
	global maxKeyLength
	i=0
	l = [(v, k) for k, v in m.items()]
	l.sort()
	l.reverse()             # so largest is first
	l= [(k, v) for v, k in l]
	f = open('output.txt','w')
	f.write('Error Count, Error\n') 
	f.close()
	f = open('output.txt','a')
	#print l
	for v in l:
		value = int(v[1])
		key =v[0]
		if value>0:
			i+=1
			q="*"*value
			#print repr(i).rjust(2),repr(value).rjust(2)+"\t"+repr(key).rjust(maxKeyLength)+" "+q
			s = repr(value).rjust(maxValueLength)+","+key+"\n"
			f.write(s)
			#print s
	f.close()
def fileToMap(fn):
	global DO_MULTI
	sr = SearchReplace.SearchReplace(fn)
	d=dict()
	f = open(fn,'r')
	p = re.compile("<error message=\"")
	q = re.compile("Exception (after|before) \w+; nested exception is:")
	for i,line in enumerate(f):
		#if len(line.split())>0:
			#line=line.split()[0]
		
		line = line.strip()
		if len(line)==0:
			continue
		# if error message found
		if p.search(line):
			# if error is apart of nested exception get caused by
			if q.search(line):
				causedBy = sr.findFrom("Caused by: .+$",i,not DO_MULTI)[0]
				#print causedBy
				line = line +" "+causedBy
			line = line.replace('<error message=\"','')
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
	global maxValueLength
	if m.get(key):
		m[key]=m[key]+value
		if len(str(value))>maxValueLength:
			maxValueLength=len(str(value))
	else:
		m[key]=value
		if len(key)>maxKeyLength:
			maxKeyLength=len(key)
maxKeyLength=0
maxValueLength=0
print maxKeyLength
main()