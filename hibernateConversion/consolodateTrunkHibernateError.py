#!/usr/bin/python
import sys, re, SearchReplace
usage = "USAGE: ./scrape.py file.java, [output.txt]"

outputFileName = "output.txt"
filterFileName = "c:/cygwin/home/jlau/one.txt"
DO_MULTIPLE = True
DTO_LIST = dict()
EJB_LIST = dict()

def main():
	global outputFileName,filterFileName, DO_MULTIPLE_REPLACE,DTO_LIST, EJB_LIST, master_ejb_anno_list
	# enforce usage
	if(len(sys.argv) <2):
		print usage
		sys.exit()
	# assign inputs
	if(len(sys.argv) == 3):
		outputFileName = sys.argv[2]
		
	splitt(SearchReplace.SearchReplace(sys.argv[1]).listFile)
	result = []
	for k,v in DTO_LIST.iteritems():
		vv=0
		try:
			vv = EJB_LIST[k]
		except KeyError:
			continue
		result.append(k+","+v+","+vv)
	writeTo(result,outputFileName)
	
					
def writeTo(rist,fileName):
		output = open(fileName,'w')			
		for line in rist:
			output.writeTo(line+"\n")
		output.close()

			
# reads list and splits it into list and dict
# db: dict is the name of the fields from the db maped to java field names
# jv: dict is a map of java field names to their type	
def splitt(l):
	global DTO_LIST, EJB_LIST
	isDB = True
	for i in l:
		i=i.strip()
		if i=="#":
			isDB = False
			continue
			
		ll = i.split()
		if len(ll)==0:
			continue
		k =ll[0]
		v = ll[1:]
		valueString = ''
		
		if isDB:
			#Class   	Duration   	Fail   	(diff)   	Skip   	(diff)   	Total   	(diff)   
			#FloorDrawingLegendUtilsCostCenterTest 	11 sec	0		0		1	
			#get only fail
			#valueString+=str(v[2])
			#DTO_LIST[k]=valueString
			#Name									Tests	Errors	Failures	Time(s)
			#FloorDrawingLegendUtilsCostCenterTest	1		1		0			16.813
			# get only errors and failures
			for z in v[1:3]:
				valueString+=z+','
			DTO_LIST[k]=valueString
		else:
			#Name									Tests	Errors	Failures	Time(s)
			#FloorDrawingLegendUtilsCostCenterTest	1		1		0			16.813
			# get only errors and failures
			for z in v[1:3]:
				valueString+=z+','
			EJB_LIST[k]=valueString
main()
