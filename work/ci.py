#!/usr/bin/python
import Util, sys,os
U = Util.Util()

def main():
	dir = "/Users/joelau/Documents/workspace/kitchensink"
	os.chdir(dir)
	print(os.getcwd())
	message = sys.argv[1]
	#cmd = "git status; git commit -am "+message+"; git push; say 'done master'; cd -"
	cmd = "git status"
	print(cmd)
	U.runCmd(cmd)

main()
