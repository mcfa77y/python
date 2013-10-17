#!/usr/bin/python
import sys, re, SearchReplace
usage = "USAGE: ./scrape.py file.java, [output.txt]"

outputFileName = "output.txt"
filterFileName = "c:/cygwin/home/jlau/one.txt"
DO_MULTIPLE = True
DTO_LIST = []
EJB_LIST = []
# list for looking at frequency information
master_ejb_anno_list = []
# ejb xdoclet annotations to search for
EJB_TERMS= [r'@bricsnet\.localize format=(.+)\r','@bricsnet.hiddenFromHistory',r'@bricsnet.validate maxlen=\"(.+)\"',r'@bricsnet.validate minValue=\"(.+)\"',r'@bricsnet.validate maxValue=\"(.+)\"']
# hibernate annotations to convert to
# this should map from EJB_TERMS 
# ex: bricsnet.localize format=X --> @formatStrings(format=X)
# ex: bricsnet.hiddenFromHistory --> @hiddenFromHistory
ANNOTATION_TRANSLATION = [r'@FormatString(format=\1)', '@HiddenFromHistory', r'@MaxLength(\1)', r'@MinValueInt(\1)',r'@MaxValueInt(\1)',]
def main():
	global outputFileName,filterFileName, DO_MULTIPLE_REPLACE,DTO_LIST, EJB_LIST, master_ejb_anno_list
	# enforce usage
	if(len(sys.argv) <2):
		print usage
		sys.exit()
	# assign inputs
	if(len(sys.argv) == 3):
		outputFileName = sys.argv[2]
		
	annoTermShort = []
	annoPattern = re.compile(r'@(\w+)')
	for annoTerm in ANNOTATION_TRANSLATION:
		annoTermShort.append(annoPattern.search(annoTerm).group(1))
	print annoTermShort
	
	split(SearchReplace.SearchReplace(sys.argv[1]).listFile)
	DTO_EJB = dict(zip(DTO_LIST,EJB_LIST))
	master_ejb_anno_list = []
	# loop through the mapped dto->ejb file names
	for dtoFN, ejbFN in DTO_EJB.iteritems():
		print "\n\n\n=================CONVERTING==============="
		ejbSR = SearchReplace.SearchReplace(ejbFN)
		dtoSR = SearchReplace.SearchReplace(dtoFN)
		dtoSR.printStep(ejbFN+"\n-->\n"+dtoFN)
		# list of getters
		getList = ejbSR.findGet(r'public .*( get\w+)',DO_MULTIPLE)
		rist = []
		terms = []
		field2Annotation = dict()
		# loop thru the getters and capture ejb comments
		for term, index in getList:
			terms.append(term.strip())
			start = ejbSR.findBackwards('/\*',index,not DO_MULTIPLE)
			#print "start: ",start
			# get the ejb comments
			rist.append(ejbSR.getBetween(start[1], '/\*','\*/')) 
			# translate them into hibernate annotations
			translateEJB2Annotation(rist)
			# if the annotations exist then pair them with the 
			# getter term
			if len(rist[0])>0:
				field2Annotation[term]=rist[0]
				
			rist = []
		#print "AFTER:\n"
		#printMap(field2Annotation)
		ERROR = ""
		# loop thru feild to annotation map
		baseUsed = False
		for term,annotations in field2Annotation.iteritems():
			# loop thru annotations
			for anno in annotations:
				# do imports
				try:
					for i, annoTerm in enumerate(annoTermShort):
						# is annotation one of the chose ones?
						if anno.find(annoTerm)>0:
							importStatment = "import com.bricsnet.core.util.model.meta."+annoTerm+";"
							if not dtoSR.findExist(importStatment):
								dtoSR.doImport(importStatment )
				except ValueError:
					print "annotation error:\t"+anno
				# INSERT field
				# term eg getObjectType
				print "term",term
				# find the getter method and insert the correstponding annotation
				# if that doesnt work then try inserting into the baseDTO
				if not dtoSR.findInsert(r'public .*'+term, anno, 0, not DO_MULTIPLE):
					dtoSR.printStep("checking base dto")
					try:
						baseDTOSR = SearchReplace.SearchReplace(getBaseName(dtoFN))
						baseDTOSR.findInsert(r'public .*'+term, anno, 0, not DO_MULTIPLE)
						baseUsed = True
						# do imports
						try:
							for i, annoTerm in enumerate(annoTermShort):
								# is annotation one of the chose ones?
								if anno.find(annoTerm)>0:
									importStatment = "import com.bricsnet.core.util.model.meta."+annoTerm+";"
									if not baseDTOSR.findExist(importStatment):
										baseDTOSR.doImport(importStatment )
						except ValueError:
							print "annotation error:\t"+anno
					except IOError:
						ERROR = "INSERT FAIL: \n\t"+dtoFN+"\n\t"+term+"\n\t"+anno+"\n\n"
						print ERROR
						
						fOut = open('ERROR.log','a')
						fOut.write(ERROR)
						fOut.close()
						continue
			if baseUsed:
				baseDTOSR.write(getBaseName(dtoFN))
				baseUsed=False
		print "DONE"
		
		#listToFile(master_ejb_anno_list, "anno.txt")
		#dtoSR.write(outputFileName)
def getBaseName(name):
	#C:/projects/HibernateMigration/bc/apps/core/source/com/bricsnet/project/dal/project/ProjectDTO.java
	pat = re.compile(r'(\w+DTO.java)')
	m = pat.subn(r'Base\1',name)
	if m:
		print m[0]
		return m[0]
	
def printMap(m):
	maxKeyLength=0
	maxValLength=0
	i=0
	l = m.keys()
	l.sort()
	for key in l:
		value = m[key]
		if len(key)>maxKeyLength:
				maxKeyLength = len(key)
		for v in value:
			if len(v)>maxValLength:
				maxValLength = len(v)
	for key in l:
		value = m[key]
		if value>1:
			i+=1
			print repr(i).rjust(2),repr(key).rjust(maxKeyLength)+"\t"+repr(value).ljust(maxValLength*2)
					
def listToFile(rist,fileName):
		output = open(fileName,'w')			
		for line in rist:
			output.write(line)
		output.close()
#translate EJBs to Annotations
# reads in EJB annotations and convertis it to 
# the hibernate annotation
def translateEJB2Annotation(ejbGroupList):
	global EJB_TERMS, master_ejb_anno_list
	#hiddenFromHistory
	ejbRegExs=[]
	delGroup=[]
	# put regular expressions into a list
	# so that adding a new term is easy
	for term in EJB_TERMS:
		ejbRegExs.append(re.compile(term))
	
	# loop thru group
	for ejbGroup in ejbGroupList:
		# loop thru ejbs
		for i,ejb in enumerate(ejbGroup):
			master_ejb_anno_list.append(ejb)
			# token for deciding whether or not
			# to delete ejb for not matching
			match = False
			# test each ejb against reg exs
			for j,regEx in enumerate(ejbRegExs):
				result = regEx.subn(ANNOTATION_TRANSLATION[j],ejb)
				# if there is a match then replace it
				# otherwise delete the entry
				if result[1]>0:
					#print "result: ",result[0]
					# strip '* ' from string
					re.subn('\* ', '',result[0])
					ejbGroup[i] = re.subn('\* ', '',result[0])[0]
					
					match = True
					
					
			#print "Delete Entry:"+str(not match)+"\n"+ejb
			# deleting entry
			if not match:
				#delGroup.append(ejbGroup[i])
				ejbGroup[i]=""
			# reset match token
			match = False
	#remove deleted values
	for i, ejbGroup in enumerate(ejbGroupList):
		ejbGroupList[i] = [ejb for ejb in ejbGroup if (len(ejb)>
			0)]
		#print ejbGroup 
	
	#javaSR.listToFile(outputFileName)
			
# reads list and splits it into list and dict
# db: dict is the name of the fields from the db maped to java field names
# jv: dict is a map of java field names to their type	
def split(l):
	global DTO_LIST, EJB_LIST
	isDB = True
	for i in l:
		i=i.strip()
		if i=="#":
			isDB = False
			continue
		if isDB:
			DTO_LIST.append(i)
		else:
			EJB_LIST.append(i)
main()
