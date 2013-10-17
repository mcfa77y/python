#!/usr/bin/python
import sys, re, os, SearchReplace, string
#the dict of the fields from the db to java field names
db = dict()
#the dict is a map of java field names to their type	
jv = dict()
term = "report"
def main():
	global db, jb
	fileName = sys.argv[1]
	#term = sys.argv[2]
	sr = SearchReplace.SearchReplace(fileName)
	split(sr.listFile)
	# tab index
	i=0
	
	s=""
	leftOvers = []
	for dbName, javaName in db.items():
		#capitalize dbName
		dbName = dbName[0].capitalize()+dbName[1:]
		# type of field name
		tipo = ""
		try:
			tipo = jv[javaName]
		except KeyError:
			print "######################### this key skipped: "+javaName +"##############################"
			leftOvers.append(dbName)
			s+=doMissing(javaName,dbName)
			print s
			continue
		
		# capitalized version of java name
		cappedJavaName = javaName[0].upper()+javaName[1:]
		# write getter method
		s+= tab(i+0)+"public "+tipo+" get"+dbName+"() {\n"
		s+= tab(i+1)+"return get"+cappedJavaName+"();\n"
		s+= tab(i+0)+"}\n"
		# write setter method
		s+= tab(i+0)+"public void set"+dbName+"("+tipo +" "+javaName+") {\n"
		s+= tab(i+1)+"set"+cappedJavaName+"("+javaName+");\n"
		s+= tab(i+0)+"}\n"
	print s	
	
	output = open('output.txt','w')
	output.writeTo(s)	
	output.close()
	
	
def doMissing(javaName, dbName):
		s=""
		i=0
		tipo = "Integer"
		# capitalized version of java name
		cappedJavaName = javaName[0].upper()+javaName[1:]
		
		# write getter method
		s+= tab(i+0)+"public "+tipo+" get"+dbName+"() {\n"
		s+= "//TODO: change the getName\n"
		s+= tab(i+1)+"return get"+cappedJavaName+"();\n"
		s+= tab(i+0)+"}\n"
		# write setter method
		s+= tab(i+0)+"public void set"+dbName+"("+tipo +" "+javaName+") {\n"
		s+= "//TODO: change the setName\n"
		s+= tab(i+1)+"set"+cappedJavaName+"("+javaName+");\n"
		s+= tab(i+0)+"}\n"
		return s
# Converts DB name to java name
# ex Table_Sgt_Locale  -> tableId
def convertDbName(dbName):
	global term
	p = re.compile("_|"+term,re.I)
	m = re.compile("Sgt",re.I)
	n = re.compile("IdSec",re.I)
	# capitalize the letters
	nuName =string.capwords(dbName,'_')
	# remove the term eg _|local
	nuName = p.sub('', nuName)
	# replce the sgt with Id
	nuName = m.sub('Id',nuName)
	# replce the Sec of IdSec
	nuName = m.sub('Id',nuName)
	# lowercase the first letter
	nuName = nuName[0].lower()+nuName[1:]
	return nuName
# returs a string with i number of tabs		
def tab(i):
	s=""
	for j in range(i):
		s +="\t"
	return s
# reads list and splits it into list and dict
# db: dict is the name of the fields from the db maped to java field names
# jv: dict is a map of java field names to their type	
def split(l):
	global db, jv
	isDB = True
	for i in l:
		i=i.strip()
		if i=="#":
			isDB = False
			continue
		if isDB:
			db[i]=convertDbName(i)
		else:
			m = i.split()
			if len(m)>0:
				if m[2].find(';')>0:
					m[2]=m[2][0:-1]
				#m[2] is the field name
				#m[1] is the field type
				jv[m[2]]=m[1]
			
main()