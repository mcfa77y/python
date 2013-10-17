#!/usr/bin/python
import sys, re, SearchReplace
DESC = "This program switches the build.sh/cleanBuild.sh files from doing trunk to/from hibernate"
USAGE = DESC+"\n\t./switchBraches.py <H for hibernate>/<T for trunk>"
ROOT_DIR = 'c:/home/sofeng/bricsnetScripts'
# you can add more files to this list
FILE_LIST = ['build.sh','cleanBuild.sh','start.sh','test.sh','dbBuild.sh','dbClean.sh']
IS_MULTI = False
def main():
	global IS_MULTI, USAGE
	# enforce USAGE
	if(len(sys.argv) <2):
		print(USAGE)
		sys.exit()
	
	# assign inputs
	toBranch = sys.argv[1]
	for f in FILE_LIST:
		ff= ROOT_DIR+"/"+f
		sr = SearchReplace.SearchReplace(ff)
		print("c\nonvert file: ",f)
		if toBranch.upper()=='H':
			sr.replace('(#+)BUILD=HibernateMigration','BUILD=HibernateMigration',IS_MULTI)
			sr.replace('BUILD=trunk','#BUILD=trunk',IS_MULTI)
		else:
			sr.replace('BUILD=HibernateMigration','#BUILD=HibernateMigration',IS_MULTI)
			sr.replace('(#+)BUILD=trunk','BUILD=trunk',IS_MULTI)
		sr.writeTo(ff)

main()
