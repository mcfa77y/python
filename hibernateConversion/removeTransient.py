#!/usr/bin/python
import sys, re
usage = "removeTransient filter.txt file.java [output.txt]"

oldSuperClass = ["BaseBusinessObjectSessionBean","BaseAncillaryObjectSessionBean","BaseSubObjectSessionBean","BaseSessionBean"]
newSuperClass = ["AbstractBizObjectService","AbstractChild1BizObjectService","AbstractChild1BizObjectService","AbstractBaseService"]
oldNewMap = dict(zip(oldSuperClass,newSuperClass))
outputFileName = "output.txt"
global file
def main():
	global outputFileName
	if(len(sys.argv) <3):
		print usage
		sys.exit()
	
	
	if(len(sys.argv) == 4):
		outputFileName = sys.argv[3]
		
	filterFileName = sys.argv[1]
	javaFileName = sys.argv[2]

	file = fileToList(javaFileName,False)
	
	#removeGeneratedByXDoclet(lJavaFile)
	#listToFile(lFile,outputFileName)
	regExReplace(file,'public abstract class', r'@MappedSuperClass\r\npublic class', False)
	doImport(file, "import javax.persistence.MappedSuperclass;")
	removeTransient(filterFileName, file, outputFileName)	

def doImport(file, importString):
	for i,line in enumerate(file):
		s = re.search("import",line)
		if s:
			file.insert(i, importString+"\r\n")
			break
				
def regExReplace(file,searchTerm, replaceTerm, isMulti):
	found = False	
	print "\nreR: ",searchTerm, replaceTerm
	p = re.compile(searchTerm)
	for i,line in enumerate(file):
		result = p.subn(replaceTerm, line)
		if(result[1]>0):
			print "\t"+result[0]
			file[i] = result[0]
			print "\treplaced"
			found = True
			if(not isMulti):
				return found
	return found
	
def replaceSuperClass(file):
	finished = False
	
	for i,line in enumerate(file):
		for old, new in oldNewMap.items():
			s = re.search(old,line)
			if s:
				line.replace(old, new)
				doImport("import com.bricsnet.core.util.impl.service."+new+";")
				finished = True
				break
		if finished:
			break

	if finished:
		print "Super Class replaced"
	else:
		print "Super Class NOT replaced"
	return file
#removes transient from file using a list as a filter
def removeTransient(filterFileName, file, outputFileName):
	filterList = fileToList(filterFileName,True)
	
	for line in filterList:
		print line
	print len(filterList)
	first = True
	i=1
	for line in file:
		
		# skip the first line so we can have a previous
		# entry
		if first:
			first = False
			continue
		#Replace addValueToMap with resetLocalization. 
		line.replace('addValueToMap', 'resetLocalization')
		
		
	
		# check to see if line matches one of the filtes
		# if it does then remove that filter 
		#  and delete the @Transient line before if it exists
		for philter in filterList:
			# match get[Column Name]
			m=re.search("get"+philter,line)
			if m:
				# replace @Transient from previous line to ""
				n = re.search("@Transient",file[i-1])
				if n:
					file[i-1]=""
				print "m:"+m.group(0)
				filterList.remove(philter)
		i+=1
	listToFile(file,outputFileName)
	print len(filterList)
	if(len(filterList)>0):
		print "remaining filters: "+str(filterList)
		
#converts a file to a list of lines
def listToFile(file, fileName):
	output = open(fileName,'w')			
	for line in file:
		output.write(line)
	output.close()
	
# turn from a file name turn the contents
# into a list
def fileToList(fn, cap):
	l=[]
	f = open(fn,'r')
	for line in f:
		if cap:
			if len(line.split())>0:
				line=line.split()[0]
			line = line[0].capitalize()+line[1:]
		l.append(line)
	f.close()
	return l

main()
