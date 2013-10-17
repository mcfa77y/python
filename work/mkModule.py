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
MODULE = "finalizeWizard"
COPY_MODULE = "moduleTemplate"

# directories
BASE_DIR = "c:/projects/trunk/bc/"
MODULE_DIR=BASE_DIR+"apps/"+MODULE+'/'
jspDir = MODULE_DIR+"web/jsp/"
javaDir = MODULE_DIR+"web/source/com/bricsnet/"+MODULE+"/web/"
langDir = BASE_DIR+"config/language/"+MODULE+"/"
xdocDir = BASE_DIR+"/apps/"+MODULE+"/xdoclet/web/"
# array of directories
DIR=(jspDir,jspDir+"decorators/",javaDir+"actions",javaDir+"forms",langDir, xdocDir)

# copy FROM directories
F_MODULE_DIR=BASE_DIR+"apps/"+COPY_MODULE+"/"
F_jspDir = F_MODULE_DIR+"web/jsp/"
F_javaDir = F_MODULE_DIR+"web/source/com/bricsnet/"+COPY_MODULE+"/web/"
F_langDir = BASE_DIR+"config/language/"+COPY_MODULE+"/"
F_xdocDir = BASE_DIR+"/apps/"+COPY_MODULE+"/xdoclet/web/"
# array of from directories
F_DIR=(F_jspDir,F_jspDir+"decorators/",F_javaDir+"actions",F_javaDir+"forms",F_langDir,F_xdocDir)

U = Util.Util()
IS_MULTI=True
def main():
	global F_jspDir, F_javaDir, F_langDir
	global jspDir, javaDir, langDir, U
	global COPY_MODULE, MODULE
	
	#buildStructure([F_jspDir],[jspDir])	
	#index = 2
	#buildStructure([F_DIR[index]],[DIR[index]])	
	#buildStructure([F_DIR[index+1]],[DIR[index+1]])
	buildStructure(F_DIR,DIR)	
	hooks()
	#undo()

def hooks():
	### add module to build.xml ###
	U.printStep("add module to build.xml")
	###
	sr = SearchReplace.SearchReplace(BASE_DIR+"build.xml")
	sr.writeTo(BASE_DIR+"build.xml.old")
	sr.replace(r'(value=\"core,[\w+,? ?]+)',r'\1,'+MODULE, not IS_MULTI)
	text ='\n\
	\t<copy todir=\"${build.dir}/${bc-web.war.name}/WEB-INF/classes/'+MODULE+'\">\n\
	\t\t<fileset dir=\"${'+MODULE+'.resources.dir}\" includes=\"*.properties\" />\n\
	\t</copy>\n'
	# insert the resource props before the web resources
	sr.findInsert('<!-- Copy Web Resources -->', text,-1,not IS_MULTI)
	
	text = '\n\
	\t<copy todir=\"${build.dir}/${bc-web.war.name}/'+MODULE+'\">\n\
    \t\t<fileset dir=\"${'+MODULE+'.web.dir}/jsp\" />\n\
    \t\t<fileset dir=\"${'+MODULE+'.web.dir}\" includes=\"js/**,css/**,images/**\" /> \n\
    \t</copy>\n'
	# insert the web resources before the birt platform dir
	sr.findInsert('<!-- Copy the birt platform dir -->', text,-1,not IS_MULTI)
	sr.write()
	
	### add module to build.properties  ###
	U.printStep("add module to build.properties")
	###
	sr = SearchReplace.SearchReplace(BASE_DIR+"build.properties")
	sr.writeTo(BASE_DIR+"build.properties.old")
	
	text=MODULE+".build.dir=${basedir}/apps/"+MODULE+"/build\n"
	sr.findInsert('wizard.build.dir', text,1,not IS_MULTI)
	
	text=MODULE+".web.dir=${basedir}/apps/"+MODULE+"/web\n"
	sr.findInsert('wizard.web.dir', text,1,not IS_MULTI)
	
	text=MODULE+".resources.dir=config/language/"+MODULE+"\n"
	sr.findInsert('wizard.resources.dir', text,1,not IS_MULTI)
	sr.write()
	
	### decorator.xml  ###
	U.printStep("decorator.xml")
	###
	sr = SearchReplace.SearchReplace(BASE_DIR+"WEB-INF/decorators.xml")
	sr.writeTo(BASE_DIR+"WEB-INF/decorators.xml.old")
	# text = '\t<decorator\n\
        # name=\"'+U.capitalize(MODULE)+'Decorator\"\n\
        # page=\"/'+MODULE+'/decorators/'+U.capitalize(MODULE)+'Decorator.jsp\" />\n\n'
	text = '\t<decorator\n\
		name=\"'+U.capitalize(MODULE)+'Decorator\"\n\
		page=\"/wizard/decorators/wizardDecorator.jsp\" />\n\n'
	sr.findInsert('<!-- Wizard Decorators -->', text,1,not IS_MULTI)
	sr.write()
	
	### ActionServlet.java  ###
	U.printStep("ActionServlet")
	###
	sr=SearchReplace.SearchReplace(BASE_DIR+"/apps/core/web/source/com/bricsnet/core/web/servlet/ActionServlet.java")
	sr.writeTo(BASE_DIR+"/apps/core/web/source/com/bricsnet/core/web/servlet/ActionServlet.java.old")
	text=' *\n * @web.servlet-init-param\n\
 *              name=\"config/'+MODULE+'\"\n\
 *              value=\"/WEB-INF/'+MODULE+'/struts-config.xml\"\n\
 *              description=\"Struts configuration file ('+MODULE+')\"\n'
	sr.findInsert('/WEB-INF/wizard/struts-config.xml', text,2,not IS_MULTI)
	sr.write()
	
	### HistoryActionUtil.java  ###
	U.printStep("HistoryActionUtil")
	###
	sr=SearchReplace.SearchReplace(BASE_DIR+"apps/core/source/com/bricsnet/core/util/audit/HistoryActionUtils.java")
	sr.writeTo(BASE_DIR+"apps/core/source/com/bricsnet/core/util/audit/HistoryActionUtils.java.old")
	text = r'\1, "/'+MODULE+'\"'
	sr.replace(r'(, \"/wizard\")',text,IS_MULTI)
	sr.write()
	
def undo():
	U.printStep("UNDO")
	shutil.move(BASE_DIR+"build.xml.old",BASE_DIR+"build.xml")
	shutil.move(BASE_DIR+"build.properties.old",BASE_DIR+"build.properties")
	shutil.move(BASE_DIR+"WEB-INF/decorators.xml.old",BASE_DIR+"WEB-INF/decorators.xml")
	shutil.move(BASE_DIR+"/apps/core/web/source/com/bricsnet/core/web/servlet/ActionServlet.java.old",BASE_DIR+"/apps/core/web/source/com/bricsnet/core/web/servlet/ActionServlet.java")
	shutil.move(BASE_DIR+"apps/core/source/com/bricsnet/core/util/audit/HistoryActionUtils.java.old",BASE_DIR+"apps/core/source/com/bricsnet/core/util/audit/HistoryActionUtils.java")
	
def buildStructure(fromDir, toDir):
	global U
	global COPY_MODULE, MODULE
	U.printStep("build file sturcture and move over files")
	for i in range(len(fromDir)):
		print(fromDir[i], toDir[i])
		tDir =toDir[i]
		fDir = fromDir[i]
		# make directories
		U.mkDir(toDir[i])
		U.printStep("copy:\n\tfrom: "+str(fDir)+"\n\tto: "+str(tDir))
		U.cpFilesToDir(fDir, tDir, ["System"])
		# rename 
		U.printStep("rename")
		U.batchRenameFiles(tDir, COPY_MODULE, MODULE, [".swp"])
		# scrub files
		U.printStep("scrubbing files")
		scrubFiles(tDir,COPY_MODULE, MODULE)
	U.mkDir(BASE_DIR+"/apps/"+MODULE+"/source/com/bricsnet/"+MODULE+"/ws")
	U.mkDir(BASE_DIR+"/apps/"+MODULE+"/web/WEB-INF")
	U.mkDir(BASE_DIR+"/apps/"+MODULE+"/build")
	U.mkDir(BASE_DIR+"/apps/"+MODULE+"/xdoclet/web/")
	shutil.copy2(F_MODULE_DIR+"build.properties",MODULE_DIR)
	scrubFile(MODULE_DIR+"build.properties", COPY_MODULE, MODULE)
	os.remove(jspDir+MODULE+"Decorator.jsp")
def scrubFile(fn, oldName,newName):
	U.printStep("scrubbing: "+fn)
	
	sr = SearchReplace.SearchReplace(fn)
	# replace capitalize
	oldNameCAP = U.capitalize(oldName)
	newNameCAP = U.capitalize(newName)
	sr.replace(oldNameCAP,newNameCAP,IS_MULTI)
	# replace lowercase
	sr.replace(oldName,newName,IS_MULTI)
	sr.write()
			
# replaces all oldName with newName in a Directory	
def scrubFiles(dir,oldName,newName):
	print("enter Scrubbing\n\t"+dir)
	fmap = dict()
	U.mapFilenames(dir,fmap,[".swp"])
	#print("fmap: "+str(fmap))
	isMulti = True
	#capitalized names
	oldNameCAP = U.capitalize(oldName)
	newNameCAP = U.capitalize(newName)
	for fn, path in fmap.items():
		print("scrubbing: "+fn)
		sr = SearchReplace.SearchReplace(path)
		# replace capitalize
		sr.replace(oldNameCAP,newNameCAP,isMulti)
		# replace lowercase
		sr.replace(oldName,newName,isMulti)
		sr.write()
	


main()
