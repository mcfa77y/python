#!/usr/bin/python
import sys,os
def svnFind(directory, key):
	for root, dirs, files in os.walk(directory):
		print "##### DIR ######\n"+str(dirs)
		if dirs or dirs[0]=='.svn':
			continue
		for f in files:
			command = "svn log "+f+" |grep "+sys.argv[2]
			print "\t"+ command
			#os.system(command)

def main():
	#svnFind(sys.argv[1],sys.argv[2])
	s=""
	for i in range(43):
		if i%2!=0:
			s+="\\"+str(i)
		else:
			#s+="new \\"+str(i)+"()"
			s+=""
	print s

main()
