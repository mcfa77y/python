#!/usr/bin/python
import sys, re, SearchReplace
usage = "USAGE: ./scrape.py file.java, [output.txt]"

outputFileName = "output.txt"
filterFileName = "c:/cygwin/home/jlau/one.txt"
DO_MULTIPLE = True
def main():
	global outputFileName,filterFileName, DO_MULTIPLE_REPLACE
	# enforce usage
	if(len(sys.argv) <2):
		print usage
		sys.exit()
	
	# assign inputs
	if(len(sys.argv) == 3):
		outputFileName = sys.argv[2]
	javaFileName = sys.argv[1]

	filterList = SearchReplace.SearchReplace(filterFileName).listFile
	javaSR = SearchReplace.SearchReplace(javaFileName)
	getList = javaSR.findGet(r'(get\w+)',DO_MULTIPLE)
	for term, index in getList:
		print term
		print javaSR.getBetween(index -11, '/\*','\*/')
	print getList
	
	
	#javaSR.writeTo(outputFileName)
			
	

main()
