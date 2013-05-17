#!/usr/bin/python
import sys, re, SearchReplace
usage = "./subsitute.py from.txt, to.txt, [output.txt]"

outputFileName = "output.txt"
IS_MULTI = True
def main():
	global outputFileName, IS_MULTI
	# enforce usage
	if(len(sys.argv) <3):
		print usage
		sys.exit()
	
	# assign inputs
	if(len(sys.argv) == 4):
		outputFileName = sys.argv[3]
	toFN = sys.argv[2]
	fromFN = sys.argv[1]

	sr = SearchReplace.SearchReplace(toFN)
	localMap = fileToMap(fromFN)
	
	for key, value in localMap.iteritems():
		sr.replace('@'+key+'@',value, not IS_MULTI)
	sr.writeTo(outputFileName)
	

def printMap(m):
	maxKeyLength=0
	maxValLength=0
	i=0
	l = m.keys()
	l.sort()
	for key in l:
		value = m[key]
		if len(key)>maxKeyLength:
				maxKeyLength = len(key)
		if len(value)>maxValLength:
				maxValLength = len(value)
	for key in l:
		value = m[key]
		if value>1:
			i+=1
			print repr(i).rjust(2),repr(key).rjust(maxKeyLength)+"\t"+repr(value).ljust(maxValLength*2)
def fileToMap(fn):
	d=dict()
	f = open(fn.strip(),'r')
	for line in f:
		#if len(line.split())>0:
			#line=line.split()[0]
		line = line.strip()
		if len(line)==0 or line.find("#")!=-1:
			continue
		lineList = line.split("=")
		if len(lineList)>1:
			print "LINELIST",lineList
			key = lineList[0]
			value = lineList[1]
			d[key]=value
	f.close()
	return d




main()
