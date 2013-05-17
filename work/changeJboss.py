#!/usr/bin/python
# changes the JBoss 7 declaration in start/stop JBoss scripts to use JBoss 4

import SearchReplace
# this is the run directory
BASE_DIR = "c:/buildingcenter/5.1.2/run/"
# file names
FN_X = BASE_DIR+"startJBoss.cmd"
FN_Y = BASE_DIR+"stopJBoss.cmd"

DO_MULTI = False
def main():
	x = SearchReplace.SearchReplace(FN_X)
	y = SearchReplace.SearchReplace(FN_Y)
	# replace jboss7 with jboss4
	x.replace("jboss-as-web-7.0.2.Final", "jboss-4.2.3.GA", DO_MULTI)
	y.replace("jboss-as-web-7.0.2.Final", "jboss-4.2.3.GA", DO_MULTI)
	x.writeTo(FN_X)
	y.writeTo(FN_Y)

main()
