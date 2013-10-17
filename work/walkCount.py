#!/usr/bin/python
import sys, re, os, SearchReplace

def main():
	#fn = sys.argv[1]
	global dic
	fn = "C:/projects/HibernateMigration/bc/WEB-INF/classes/com/bricsnet"
	print "hello"
	for root, dirs, files in os.walk(fn):
		for name in files:
			if name.find('hbm.xml')>0 and name.find('.svn')<1:
				print "name:\n\t"+name
				fm = doCount(root+"/"+name)
				if fm:
					print "combine maps"
					combineMap(fm, dic)
	printMap(dic)

def doCount(fileName):
	sr = SearchReplace.SearchReplace(fileName)
	f = sr.regExFindGet('hiddenFromHistory', r'<property name=.*>', 100)
	print f
	if len(f)>0:
		return ListToMap(f)
	else:
		return None
	
	
def combineMap(m0, m1):
	#print m0,m1
	for key in m0.keys():
		addToMap(m1,key,m0[key])
	return m1
		
def ListToMap(list):
	d=dict()
	for line in list:
		addToMap(d,line,1)
	return d
	
def addToMap(m,key,value):
	global maxKeyLength
	if m.get(key):
		m[key]=m[key]+value
	else:
		m[key]=value
		if len(key)>maxKeyLength:
			maxKeyLength=len(key)

def printMap(m):
	global maxKeyLength
	i=0
	l = m.keys()
	l.sort()	
	for key in l:
		value = m[key]
		if value>0:
			i+=1
			q="*"*value
			print repr(i).rjust(2),repr(value).rjust(2)+"\t"+repr(key).rjust(maxKeyLength)+" "+q
			
maxKeyLength=0
dic = dict()	
main()
