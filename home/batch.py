#!/usr/bin/python
import os, sys, re
def main():
	inDir = open(sys.argv[1],'r')
	for n in inDir:
		n=n.strip()
		nn = n.split('\ ')
		p=''
		for nnn in nn:
			p += nnn
		print p
		command = "mv " +n+" "+p
		print command
		os.system(command)

main()
