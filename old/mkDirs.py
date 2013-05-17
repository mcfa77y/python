#!/usr/bin/python
import sys, re, os, SearchReplace

def main():
	fn = sys.argv[1]
	path = sys.argv[2]
	
	dirList = SearchReplace.SearchReplace(fn).listFile
	for dirName in dirList:
		dirName = dirName.strip()
		print "making dir: "+ dirName
		os.mkdir(path+"/"+dirName,0700)
		
main()
