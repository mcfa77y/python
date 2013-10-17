#!/usr/bin/python
import sys, re, os, SearchReplace, string
DEBUG = True
fnList = []
DTO_LIST = []
EJB_LIST = []
def main():
	global DEBUG, fnList
	fnIndex = sys.argv[1]
	fnList = SearchReplace.SearchReplace(fnIndex).listFile
	diffAgainstList(fnList)
	#makeDirs(fnList)
	#fixIt(fnList)
	#twoParam("./opFixIt.py", not DEBUG)
	#BaseDTO(fnList)	
	#DTO(fnList)
	#factory(fnList)
	#scrape
	#oneParam("./scrape.py", DEBUG)
	#Service(fnList)
	#ServiceTouchUp(fnList)
	#setGet(fnList)
	#substitue
	#twoParam("./substitute.py",DEBUG)
	#unix2dos(fnList)
	#webEjbRemoval(fnList)

def runCommand(command, paramsSize,debug):
	global fnList
	javaFn = fnList[0].strip()
	
	if not debug:
		command = command+" "+javaFn+" "+" "+javaFn
	else:
		command = command+" "+javaFn+" "+philter
	print(command)
	os.system(command)


def oneParam(command, debug):
	global fnList
	javaFn = fnList[0].strip()
	if not debug:
		command = command+" "+javaFn+" "+javaFn
	else:
		command = command+" "+javaFn
	print(command)
	os.system(command)
def twoParam(command, debug):
	global fnList
	javaFn = fnList[0].strip()
	philter = fnList[1].strip()
	if not debug:
		command = command+" "+javaFn+" "+philter+" "+javaFn
	else:
		command = command+" "+javaFn+" "+philter
	print(command)
	os.system(command)
def diffAgainstList(fnList):
	command = "cd c:\\projects\\trunk\\bc\\"
	print(command)
	os.system(command)
	os.system("ls")
	
	dir = "c:\\projects\\trunk\\bc\\"
	x = dir+fnList[0].strip()
	for item in fnList[1:]:
		# command = "diff "+x+" "+item
		item = dir+item.strip()
		name = "diff-"+x.split("/")[2]+"-"+item.split("/")[2]+".diff"
		command = "diff -w "+x+" "+item+" >"+name
		print(command)
		os.system(command)
		
def makeDirs(fnList):
	command = "cd c:\\projects\\trunk\\bc\\apps\\wizard"
	print(command)
	os.system(command)
	for name in fnList:
		command = "mkdir "+name
		print(command)
		os.system(command)
		command ="cd "+name
		print(command)
		os.system(command)
		
def fixIt(fnList):	
	javaFn = fnList[0].strip()
	philter = fnList[1].strip()
	command = "./opFixIt.py "+javaFn+" "+philter+" "+javaFn
	#command = "./opFixIt.py "+javaFn+" "+philter
	print(command)
	os.system(command)	
def factory(fnList):
	javaFn = fnList[0].strip()
	#command = "./doFactory.py "+javaFn+" "+javaFn
	command = "./doFactory.py "+javaFn
	#command = "./doDTO.py "+javaFn+" "+philter
	print(command)
	os.system(command)		
def setGet(fnList):
	philter = fnList[1].strip()
	command = "./doSetGet.py "+philter
	print(command)
	os.system(command)
def webEjbRemoval(fnList):
	javaFn = fnList[0].strip()
	philter = fnList[1].strip()
	#command = "./doWebEjbRefRemoval.py "+javaFn+" "+philter+" "+javaFn
	command = "./doWebEjbRefRemoval.py "+javaFn+" "+philter+" "
	print(command)
	os.system(command)
	
def DTO(fnList):
	javaFn = fnList[0].strip()
	philter = fnList[1].strip()
	command = "./doDTO.py "+javaFn+" "+philter+" "+javaFn
	#command = "./doDTO.py "+javaFn+" "+philter
	print(command)
	os.system(command)

def BaseDTO(fnList):
	for fn in fnList:
		fn = fn.strip()
		command = "./doBaseDTO.py "+fn+" "+fn
		print(command)
		os.system(command)

def ServiceTouchUp(fnList):
	for fn in fnList:
		fn = fn.strip()
		#command = "./doServiceTouchUp.py "+fn+" "+fn
		command = "./doServiceTouchUp.py "+fn
		print(command)
		os.system(command)

def Service(fnList):
	for fn in fnList:
		fn = fn.strip()
		command = "./doService.py "+fn+" "+fn
		print(command)
		os.system(command)
		
def unix2dos(fnList):
	for fn in fnList:
		fn = fn.strip()
		command = "unix2dos "+fn
		print(command)
		os.system(command)	
			
# reads list and splits it into 2 list via delimeter #
def split(l):
	aList=[]
	bList=[]
	isListA = True
	for i in l:
		i=i.strip()
		if i=="#":
			isListA= False
			continue
		if isListA:
			aList.append(i)
		else:
			bList.append(i)
	return aList, bList
main()

main()


