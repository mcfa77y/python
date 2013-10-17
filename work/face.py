#!/usr/bin/python
import os, sys, re,Util,SearchReplace
FN_SPLIT=" "
def use():
	print ("USAGE:\n\t./HandBreak inputDir outputDir")
	exit()
def main():
	global FN_SPLIT
	if len(sys.argv)<3:
		use()
	inDir = sys.argv[1]
	outDir = sys.argv[2]
	#grab all avi
	p = re.compile(".+\.vnt",re.I)
	for name in os.listdir(inDir):
		if not os.path.isdir(name):
			m = p.search(name)
			if m:
				fn = m.group(0)
				#print(fn)
				sr = SearchReplace.SearchReplace(inDir+fn)
				
				st = sr.findGet(r"PRINTABLE:(.*?)\n",False)
				st=st[0][0].replace("=0D=0A","\n").replace("PRINTABLE:",fn.split(".")[0]+"\n")
				
				print(st)
				
def listToString(list):
	s=''
	for i in list:
		#s+=i+'.'
		s+=i
	#return s[0:-1]
	return s
main()
