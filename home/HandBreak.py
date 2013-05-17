#!/usr/bin/python
import os, sys, re
FN_SPLIT=" "
def use():
	print "USAGE:\n\t./HandBreak inputDir outputDir"
	exit()
def main():
	global FN_SPLIT
	if len(sys.argv)<3:
		use()
	inDir = sys.argv[1]
	outDir = sys.argv[2]
	#grab all avi
	p = re.compile(".+\.avi",re.I)
	for name in os.listdir(inDir):
		if not os.path.isdir(name):
			m = p.search(name)
			if m:
				i=0
				# grab the first 3 words of file name
				# split by '.'
				# nuName=listToString(m.group(i).split('.')[0:3])
				
				# grab the good bits
				nuName=listToString(m.group(i).split(FN_SPLIT)[1:])
				#nuName=	outDir+nuName
				#outDir=outDir.replace('\\','/')
				nuName=	outDir
				inDir=inDir.replace('\\','/')
				name=name.replace(' ','\\ ')
				print('\noldName: ',name)
				print('\nnuName',nuName)
				name = inDir+name
				#command = "HandBrakeCLI -i "+name+" -o "+nuName+".mp4 --preset=\"iPhone & iPod Touch\" -a 2"
				#command = "HandBrakeCLI -i "+name+" -o "+nuName+".mp4 --preset=\"iPhone & iPod Touch\""
				#command = "HandBrakeCLI -i "+name+" -o "+nuName+".mp4 --preset='iPad'"
				command = "mv "+name+' '+nuName
				print( "--------COMMAND-------\n"+command+"\nnew fn:\t"+nuName+"\n")
				os.system(command)
def listToString(list):
	s=''
	for i in list:
		#s+=i+'.'
		s+=i
	#return s[0:-1]
	return s
main()
