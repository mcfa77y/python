#!/usr/bin/python
import sys, re, SearchReplace
usage = "./fixIt.py file.java, filterName.txt, [output.txt]"

outputFileName = "output.txt"
filterFileName = "c:/cygwin/home/jlau/one.txt"
DO_MULTIPLE_REPLACE = True
def main():
	global outputFileName,filterFileName, DO_MULTIPLE_REPLACE
	# enforce usage
	if(len(sys.argv) <3):
		print usage
		sys.exit()
	
	# assign inputs
	if(len(sys.argv) == 4):
		outputFileName = sys.argv[3]
	filterFileName = sys.argv[2]
	javaFileName = sys.argv[1]

	filterList = SearchReplace.SearchReplace(filterFileName).listFile
	javaSR = SearchReplace.SearchReplace(javaFileName)
	java2db = mapJava2DB(filterList)
	
	for javaName, dbName in java2db.iteritems():
		javaSR.findFindDelete(r' get'+javaName,'@Transient',2,not DO_MULTIPLE_REPLACE)
		javaSR.findInsert(r' get'+javaName,'@Column(name=\"'+dbName+'\")\n',0, not DO_MULTIPLE_REPLACE)	
	javaSR.doImport("import javax.persistence.Column;")
	javaSR.findInsert('public int hashCode() {','@Transient"'+dbName+'\")\n',0, not DO_MULTIPLE_REPLACE)	
	javaSR.findInsert('public boolean isIdentical(Object other) {','@Transient"'+dbName+'\")\n',0, not DO_MULTIPLE_REPLACE)	
	javaSR.findInsert('public boolean equals(Object other) {','@Transient"'+dbName+'\")\n',0, not DO_MULTIPLE_REPLACE)	
	javaSR.findInsert('protected boolean hasIdentity() {','@Transient"'+dbName+'\")\n',0, not DO_MULTIPLE_REPLACE)	
	
	
	javaSR.listToFile(outputFileName)
	
# from the filter list it gets the java names
# and the db names and returns the java->db 
# mapping
def mapJava2DB(rist):
	p = re.compile(r'get(\w+)')
	db =[]
	java=[]
	# token for switching betwen db names and java
	# names
	switch = True
	for line in rist:
		s=p.search(line)
		if s:
			fieldName = s.group(1)
			if switch:
				fieldName = fieldName[0].lower()+fieldName[1:]
				db.append(fieldName)
			else:
				java.append(fieldName)
			switch = not switch
	return dict(zip(java,db))
	

main()
