#!/usr/bin/python
import sys, re, os, SearchReplace, string,Util

#change per use
#MASTER_LIST=LIB+"glyphs.json"
#SRC = "/Users/jlau/Downloads/iphone_ios7/elements/"
#SRC = "/Users/jlau/Downloads/Archive/forms_controls/"
SRC = "/Users/jlau/Downloads/Archive/containers_content/"
##SRC = "/Users/jlau/Downloads/icon_symbols/"
PKG_SLASH = "/ui/ui_v3/"


PKG_DOT = PKG_SLASH.replace('/','.')
BASE_URL="/Users/jlau/projects/gliffy-shape/shape/src/main/resources/com/gliffy/"
LIB=BASE_URL+"libraries"+PKG_SLASH
STENCIL=BASE_URL+"stencil"+PKG_SLASH
STENCIL_REF="com.gliffy.stencil"+PKG_DOT
SHAPE=BASE_URL+"shape"+PKG_SLASH
SHAPE_REF="com.gliffy.shape"+PKG_DOT
MULTI_SEARCH = True

# these arrays are triplets [templateURL, replacementString, description]
JSON_TEMPLATES=["/Users/jlau/projects/gliffy-shape/shape/src/main/resources/com/gliffy/shape/iphone/iphone7/glyphs/glyph_add.json",\
				"/Users/jlau/projects/gliffy-shape/shape/src/main/resources/com/gliffy/shape/iphone/iphone7/navigation/navbar_01.json",\
				"/Users/jlau/projects/gliffy-shape/shape/src/main/resources/com/gliffy/shape/iphone/iphone7/elements/rounded_top_10_px.json"]
JSON_REPLACE_STRINGS=["iphone.iphone7.glyphs.glyph_add",\
					"iphone.iphone7.navigation.navbar_01",\
					"iphone.iphone7.elements.rounded_top_10_px"]
JSON_TEMPLATE_DESC=["simple shape and text", "compound shape", "compound shape with one text"]

#JSON_TEMPLATE="/Users/jlau/projects/gliffy-shape/shape/src/main/resources/com/gliffy/shape/iphone/iphone7/navigation/navbar_01.json"
#JSON_REPLACE_STRING="iphone.iphone7.navigation.navbar_01"


OLD_CHIOCE=0

U = Util.Util()

def main():
	d={}
	exclude=['.DS_Store']
	i=0
	package=""
	shapes=[]
	emptyShapes=[]
	sameShapes=[]
	isInitialFolder=True
	
	# get shapes/package from source folder
	for root, dirs, files in os.walk(SRC):
		if isInitialFolder:
			isInitialFolder=False
			continue
		#print("root",root)
		things = root.split("/")
		#print("things: "+str(things))
		if len(things)>5:
			#print(things[-2:])
			pAndS =things[-2:] 
			package = pAndS[0]
			shape = pAndS[1]
			shapes.append(shape.replace('-','_'))
	i=0
	for s in shapes:
		print ("["+str(i)+"]"+" "+s)
		i+=1
	try:
	    mode=int(raw_input('Input:'))
	    shapes=[str(shapes[mode])]
	    #shapes=shapes[mode]
	except ValueError:
	    print "Not a number"
	    sys.exit(0)


	print(shapes)
	
	for eS in shapes:
		''' CREATING EMPTY JSON FILE
		U.printStep("create empty *.json file: "+eS)
		U.printStep(SHAPE+package+"/"+eS+".json")
		try:
			emptyShape = open(SHAPE+package+"/"+eS+".json",'w')
		except IOError:
			U.mkDir(SHAPE+package+"/")
			emptyShape = open(SHAPE+package+"/"+eS+".json",'w')

		emptyShape.write('"tids": ["'+STENCIL_REF+package+'.'+eS+']",\n')
		emptyShape.write('"uid": "'+SHAPE_REF+package+'.'+eS+'"\n')
		emptyShape.close()
		'''

		U.printStep("create template *.json file: "+eS)
		newJson = SHAPE+package+"/"+eS+".json"
		U.printStep(newJson)
		try:
			createSimpleJson(PKG_DOT[1:]+package+"."+eS,newJson)
		except IOError:
			U.mkDir(SHAPE+package+"/")
			createSimpleJson(PKG_DOT[1:]+package+"."+eS,newJson)

		

	# add to master list of shapes for package
	masterListFn = LIB+package+".json"
	#masterListFn = MASTER_LIST
	try:
		masterListSr = SearchReplace.SearchReplace(masterListFn)
	except  IOError:
		masterListFnNew = open(masterListFn,'w')
		masterListSr = SearchReplace.SearchReplace(masterListFn)
		masterListFnNew.close()
	for shape in shapes:
		if shape.find(".DS_Store")>-1 or shape.find(".png")>-1:
			continue
		#com.gliffy.shape.ui.ui_v3.forms_controls.slider
		shapeClass = ",\n        \""+SHAPE_REF+package+"."+shape+"\"\n\t"
		masterListSr.findInsert("]",shapeClass,0,not MULTI_SEARCH)

		
		# create shape stencil with empty template
		U.printStep("mkdir: "+STENCIL+package+"/"+shape)
		U.mkDir(STENCIL+package+"/"+shape)
		
		
		U.printStep("add empty template: "+STENCIL+shape+"/template.svg")
		emptyTemplate = open(STENCIL+package+"/"+shape+"/template.svg","w")
		emptyTemplate.close()
		
		# remove used folder
		cmd = "rm -r "+SRC+shape
		U.printStep("remove used folder "+cmd)
		#U.runCmd(cmd)


	U.printStep("writing masterlist")
	print("masterList",masterListSr.listFile)
	masterListSr.write()
	main()

def createSimpleJson(newName,fileName):
	mode=0
	i=0
	for s in JSON_TEMPLATE_DESC:
		print ("["+str(i)+"]"+" "+s)
		i+=1

	try:
	    mode=int(raw_input('choice: '))
	except ValueError:
	    print "Default chosen 0"
	    mode=0

	
	sr = SearchReplace.SearchReplace(JSON_TEMPLATES[mode])
	sr.replace(JSON_REPLACE_STRINGS[mode],newName,MULTI_SEARCH)
	sr.writeTo(fileName)

main()


