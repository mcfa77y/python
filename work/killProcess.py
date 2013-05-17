#!/usr/bin/python
# this program kills jboss by process id number
from os import system
from subprocess import Popen, PIPE
PROCESS_NAME = 'jboss'
def main():
	global PROCESS_NAME
	print("killing jboss is what I do best!")
	# run ps command and get standard output
	cmd = 'ps'
	p = Popen(cmd, stdout=PIPE, stderr=PIPE)
	stdout = str(p.communicate()[0]).split('\\n')
	# read standard output for standalone.bat
	for line in stdout:
		if line.find(PROCESS_NAME)>0:
			l = line.split()
			command = "kill -9 "+str(l[0])
			print(command)
			# kill standalone.bat
			system(command)
			break
main()
