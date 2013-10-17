#!/usr/bin/python
import sys, re, SearchReplace
usage = "doService file.java [output.txt]"

outputFileName = "output.txt"
DO_MULTIPLE_REPLACE = True
global file
def main():
	global outputFileName, DO_MULTIPLE_REPLACE
	# enforce usage
	if(len(sys.argv) <2):
		print usage
		sys.exit()
	
	# assign inputs
	if(len(sys.argv) == 3):
		outputFileName = sys.argv[2]
	#filterFileName = sys.argv[1]
	javaFileName = sys.argv[1]

	sr = SearchReplace.SearchReplace(javaFileName)
	
	# replace other services
	sr.printStep("replace other services")
	sr.regExReplace(r"List (\w+) = (\w+)Util\.getLocalHome\(\)\.create\(\)\s+\.get(.+)",r"List <> \1 = new \2().get\4",DO_MULTIPLE_REPLACE)
	
	# replace generic create services
	sr.regExReplace(r"BusinessObjectObserver\.beforeCreate\(dto, null, p\);\s*(\w+)DTO (\w+) = (\w+)Util\.getLocalHome\(\)\.create\(dto\)\s*\.get(\w+)DTO\(\);\s*dto\.setId\(created\.getId\(\)\);\s*BusinessObjectObserver\.afterCreate\(dto, null, p\);\s*return (\w+);",r"return super.create(dto);", not DO_MULTIPLE_REPLACE)
	
	sr.regExReplace(r"(\w+)Util\.getLocalHome\(\)\.findByPrimaryKey\((\w+)\)\.getAlphaId\(\)",r"new (\1)Service().getDTO(\2).getAlphaId()", DO_MULTIPLE_REPLACE)
	
	sr.regExReplace(r"(\w+)Local ejb = \w+Util\.getLocalHome\(\)\.findByPrimaryKey\((\w+)\);\s*(\w+ \w+ = )ejb\.get\w+DTO\(\);",r"\3=new \1Service().getDTO(\2)",DO_MULTIPLE_REPLACE)
	sr.listToFile(outputFileName)
main()