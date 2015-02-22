#!/usr/bin/python
# this program kills -9 pids given by ps aux |grep java

import subprocess
ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]
processes = ps.split('\n')
# this specifies the number of splits, so the splitted lines
# will have (nfields+1) elements
nfields = len(processes[0].split()) - 1
for row in processes[1:]:
	# print "row: " + row
	rs = row.split()
	if len(rs)>0:
		lastProcesses = rs[10:]
		for lastProcess in lastProcesses:
			if "java" in lastProcess:
				print "row:" + str(rs[:10])
				print "\tlastProcess:"+lastProcess
				subprocess.Popen(['kill', '-9', rs[1]], stdout=subprocess.PIPE).communicate()[0]
				break;
	# print row.split(None, nfields)