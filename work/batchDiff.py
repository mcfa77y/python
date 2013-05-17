#!/usr/bin/python
# this script reads two directories and diffs the files and writes that output to a file

import sys, os, Util


# result file for diffs results of the two directories
OUTPUT = "diff_results.diff"
# directories
FOLDER = "web"
USED_DIR="c:/projects/trunk/bc/apps/wizard/xdoclet/"+FOLDER
FRESH_DIR="c:/projects/trunk/bc/apps/program/xdoclet/"+FOLDER
#pickled versions of dictionaries
USED_FN = 'Pickles/used-'+FOLDER+'.pkl'
FRESH_FN = 'Pickles/fresh-'+FOLDER+'.pkl'

#dictionarys of names mapped to full path + name
USED = dict()
FRESH = dict()
U = Util.Util()

def main():
	global USED,FRESH
	writeDict()
	#loadDict()
	# clear output file
	U.write(OUTPUT,"")
	print("doing Diffs")
	for fn, pathNname in FRESH.items():
		if fn in USED:
			cmd = "diff -wEb "+pathNname+" "+USED[fn]
			cmd=cmd.replace("\\","/")
			out = U.runCmd(cmd)
			print("\tcolordiff "+fn+"\t"+str(out))
			if len(out)>1:
				out = prettify(out)
				msg = fn+"\n\t"+cmd+"\n"+str(out)+"\n\n"
				U.append(OUTPUT,msg)
				
	uSet = set(USED.keys())
	fSet = set(FRESH.keys())
	deltaSet = uSet-fSet
	print("The following files were not in the FRESH directory")
	for k in deltaSet:
		# skip index files
		if not k.find(".index")>0:
			print(k+"\t"+USED[k])
			

def prettify(msg):
	result = ""
	for line in msg:
		result+=line+"\n"
	return result
				
def writeDict():
	global USED,FRESH
	global USED_FN, FRESH_FN
	print("writing dict")
	mapFilenames(FRESH_DIR, FRESH)
	U.cPickle(FRESH_FN,FRESH)
	
	mapFilenames(USED_DIR, USED)
	U.cPickle(USED_FN, USED)

def loadDict():
	print("loading dict")
	global USED,FRESH
	global USED_FN, FRESH_FN
	USED = U.cUnpickle( USED_FN)
	FRESH =U.cUnpickle(FRESH_FN)
	
# maps file names to path+filename in a given directory
# fn - directory
# d - dictionary
def mapFilenames(fn, dic):
	print("mapping files: "+fn)
	for root, dirs, files in os.walk(fn):
		for name in files:
			#print(name)
			# skip .svn files
			if name.find('.svn')<1:
				# change the stroke type from windows to unix
				root = root.replace("\\","/")
				nameModRoot = root.replace(fn,"")+"/"+name
				dic[name]=root+"/"+name
				#print ("name:\n\t"+name+'\n\t\t'+root)
		if '.svn' in dirs:
			dirs.remove('.svn')  # don't visit svn directories

main()
