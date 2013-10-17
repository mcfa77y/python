#!/usr/bin/python
# this script builds the project

import sys, os, Util
# directories
BUILD="HibernateMigration"
#BUILD="trunk"
BUILD_DIR="/cygdrive/c/projects/"+BUILD+"/bc/"

U = Util.Util()

def main():
	print(BUILD_DIR)
	U.runCmd("cd "+BUILD_DIR)
	cmd = "ant all.dev install.dev"
	out = U.runCmd(cmd)
	U.runCmd("cd -")



main()
