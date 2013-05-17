#!/usr/bin/python
# this script makes a stub version of a module by creating all the directories and stub files for a basic new module 

import sys, os, Util, shutil, SearchReplace

# refactor
OLD = "listToFile\("
NEW = "writeTo("
# excluded files
EXCLUDE = ["SearchReplace","mkModule","Util","refactorWrite",".swp"]

# directories
BASE_DIR="c:/home/sofeng/python/"
IS_MULTI=True

U = Util.Util()

def main():
	global OLD, NEW, EXCLUDE, BASE_DIR, U
	fmap = dict()
	U.mapFilenames(BASE_DIR,fmap,EXCLUDE)
	for fn, path in fmap.items():
		if fn.find(".py")>0:
			U.printStep("replace in "+fn)
			sr = SearchReplace.SearchReplace(path)
			sr.replace("U.writeTo","U.write",IS_MULTI)
			sr.write()
	
main()
