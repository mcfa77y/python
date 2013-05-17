#!/usr/bin/python
# this script makes a stub version of a module by creating all the directories and stub files for a basic new module 
# TODO:
# copy over the build.properties from bc/apps/TEMPLATE and scrub it 
# create a apps/MODULE/web/WEB-INF dir
#  C:\projects\trunk\bc\apps\systemDefaultsWizard\xdoclet\web not found.
# struts-config-resources.xml needs to change the moduleTemplate.lable/action/etc to MODULE.*

import sys, os, Util, shutil, SearchReplace

# financialWizard organizationWizard peopleWizard propertyWizard reviewWizard finalizeWizard
# module name
MODULE = "Question"
COPY_MODULE = "MasterQuestion"
#MODULE = "Canidate"
#COPY_MODULE = "Member"

# directories
BASE_DIR = "/Users/joelau/Documents/workspace/kitchensink/src/main/java/org/jboss/as/quickstarts/kitchensink/"
FN = ['controller/'+COPY_MODULE+'Registration.java',\
'data/'+COPY_MODULE+'ListProducer.java',\
'model/'+COPY_MODULE+'.java',\
'rest/'+COPY_MODULE+'ResourceRESTService.java']

U = Util.Util()
IS_MULTI=True
def main():
	#undo()
	doClass()
def doClass():
	global BASE_DIR,DIR, U
	global COPY_MODULE, MODULE
	for d in FN:
		fn = BASE_DIR+d
		toFn = fn.replace(COPY_MODULE,MODULE)
		#print(fn,'\n',toFn)
		shutil.copy2(fn,toFn)
		scrubFile(toFn,COPY_MODULE,MODULE)
	
def undo():
	global BASE_DIR,DIR, U
	global COPY_MODULE, MODULE
	U.printStep("UNDO")
	for d in FN:
		fn = BASE_DIR+d
		toFn = fn.replace(COPY_MODULE,MODULE)
		os.remove(toFn)	

def scrubFile(fn, oldName,newName):
	U.printStep("scrubbing: "+fn)
	
	sr = SearchReplace.SearchReplace(fn)
	# replace capitalize
	oldNameCAP = U.capitalize(oldName)
	newNameCAP = U.capitalize(newName)
	sr.replace(oldNameCAP,newNameCAP,IS_MULTI)
	# replace lowercase
	oldName = U.unCapitalize(oldName)
	newName = U.unCapitalize(newName)
	sr.replace(oldName,newName,IS_MULTI)
	sr.write()
			
main()
