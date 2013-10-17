#!/usr/bin/python
import sys, re, os, SearchReplace, string
DEBUG = True
fnList = []
def main():
	global DEBUG, fnList
	fnIndex = sys.argv[1]
	fnList = SearchReplace.SearchReplace(fnIndex).listFile;
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
	unix2dos(fnList)
	#webEjbRemoval(fnList)

def runCommand(command, paramsSize,debug):
	global fnList
	javaFn = fnList[0].strip()
	
	if not debug:
		command = command+" "+javaFn+" "+" "+javaFn
	else:
		command = command+" "+javaFn+" "+philter
	print command
	os.system(command)
def oneParam(command, debug):
	global fnList
	javaFn = fnList[0].strip()
	if not debug:
		command = command+" "+javaFn+" "+javaFn
	else:
		command = command+" "+javaFn
	print command
	os.system(command)
def twoParam(command, debug):
	global fnList
	javaFn = fnList[0].strip()
	philter = fnList[1].strip()
	if not debug:
		command = command+" "+javaFn+" "+philter+" "+javaFn
	else:
		command = command+" "+javaFn+" "+philter
	print command
	os.system(command)

def fixIt(fnList):	
	javaFn = fnList[0].strip()
	philter = fnList[1].strip()
	command = "./opFixIt.py "+javaFn+" "+philter+" "+javaFn
	#command = "./opFixIt.py "+javaFn+" "+philter
	print command
	os.system(command)	
def factory(fnList):
	javaFn = fnList[0].strip()
	#command = "./doFactory.py "+javaFn+" "+javaFn
	command = "./doFactory.py "+javaFn
	#command = "./doDTO.py "+javaFn+" "+philter
	print command
	os.system(command)		
def setGet(fnList):
	philter = fnList[1].strip()
	command = "./doSetGet.py "+philter
	print command
	os.system(command)
def webEjbRemoval(fnList):
	javaFn = fnList[0].strip()
	philter = fnList[1].strip()
	#command = "./doWebEjbRefRemoval.py "+javaFn+" "+philter+" "+javaFn
	command = "./doWebEjbRefRemoval.py "+javaFn+" "+philter+" "
	print command
	os.system(command)
	
def DTO(fnList):
	javaFn = fnList[0].strip()
	philter = fnList[1].strip()
	command = "./doDTO.py "+javaFn+" "+philter+" "+javaFn
	#command = "./doDTO.py "+javaFn+" "+philter
	print command
	os.system(command)

def BaseDTO(fnList):
	for fn in fnList:
		fn = fn.strip()
		command = "./doBaseDTO.py "+fn+" "+fn
		print command
		os.system(command)

def ServiceTouchUp(fnList):
	for fn in fnList:
		fn = fn.strip()
		#command = "./doServiceTouchUp.py "+fn+" "+fn
		command = "./doServiceTouchUp.py "+fn
		print command
		os.system(command)

def Service(fnList):
	for fn in fnList:
		fn = fn.strip()
		command = "./doService.py "+fn+" "+fn
		print command
		os.system(command)
		
def unix2dos(fnList):
	for fn in fnList:
		fn = fn.strip()
		command = "dos2unix"+fn
		print command
		os.system(command)	
main()


