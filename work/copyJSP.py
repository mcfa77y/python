#!/usr/bin/python
# this script reads two directories and diffs the files and writes that output to a file

import sys, os, Util

#JSP DIRECTORY SET
#DIR_SET=["organizationWizard"]
DIR_SET=["finalizeWizard","financialWizard","organizationWizard","peopleWizard","propertyWizard","reviewWizard","systemDefaultsWizard",]

# directories
FOLDER = "C:/projects/trunk/bc/"
FROM_DIR=FOLDER+"apps/REPLACE/web/jsp"
TO_DIR  =FOLDER+"build/bc.ear/bc-web.war/REPLACE"

U = Util.Util()

def main():
	global FROM_DIR,TO_DIR, DIR_SET
	for dir in DIR_SET:
		nuFrom = FROM_DIR.replace("REPLACE",dir)
		nuTo = TO_DIR.replace("REPLACE",dir)
		#U.cpFilesToDir(nuFrom,nuTo,[])
		U.cpFilesToDir(nuTo,nuFrom,[])


main()
