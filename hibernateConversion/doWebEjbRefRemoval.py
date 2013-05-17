#!/usr/bin/python
import sys, re, SearchReplace
usage = "doFactory file.java, filter.txt, [output.txt]"
#number of inputs
INPUT_LEN = 3
outputFileName = "output.txt"
DO_MULTIPLE_REPLACE = True
def main():
	global outputFileName,filterFileName, DO_MULTIPLE_REPLACE, INPUT_LEN
	# enforce usage
	if(len(sys.argv) <INPUT_LEN):
		print usage
		sys.exit()
	
	# assign inputs
	if(len(sys.argv) == INPUT_LEN+1):
		outputFileName = sys.argv[INPUT_LEN+1]
	javaFileName = sys.argv[1]
	filterFileName = sys.argv[2]

	sr = SearchReplace.SearchReplace(javaFileName)
	fsr = SearchReplace.SearchReplace(filterFileName)
	s=""
	for delete in fsr.listFile:
		if not sr.regExReplace(delete,"", DO_MULTIPLE_REPLACE):
	#	if not sr.deleteLines( delete.strip(), -3,7):
			s+=delete
	
	sr.printStep("DTOs not Removed")
	print "\n"+s
	sr.listToFile(outputFileName)

	
main()
