#!/usr/bin/python
import sys, re, os, SearchReplace, string,Util
U = Util.Util()

def main(): 
	sr = SearchReplace.SearchReplace(sys.argv[1])
	fnList = sr.listFile
	for i in fnList:
		word_list =i.split("=")
		if len(word_list)>1:
			key=str(word_list[1]).lower()
			print(word_list[0]+"."+word_list[1].strip().replace(' ','_')+"="+key.strip())


main()


