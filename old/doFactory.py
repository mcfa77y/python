#!/usr/bin/python
import sys, re, SearchReplace
usage = "doFactory file.java, [output.txt]"
#number of inputs
INPUT_LEN = 2
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

	sr = SearchReplace.SearchReplace(javaFileName)
	# step 2 
	sr.printStep(2)
	sr.replace(r'(\w+)Home home = (\w+)Util.getLocalHome\(\);',r'', DO_MULTIPLE_REPLACE)
	# step 3
	sr.printStep(3)
	sr.replace(r'home\.findByAlphaId\(alphaId\).get(\w+)DTO\(\)',r'findByAlphaId(alphaId)', DO_MULTIPLE_REPLACE)
	# step 4
	sr.printStep(4)
	sr.replace(r'home\.findByPrimaryKey\((\w+)\)\.get(\w+)DTO\(\)',r'new \2Service().getDTO(\1)', DO_MULTIPLE_REPLACE)
	# step 5
	sr.printStep(5)
	sr.replace(r'home\.(.+)',r'\1', DO_MULTIPLE_REPLACE)
	
	sr.writeTo(outputFileName)

	
main()
