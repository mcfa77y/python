#!/usr/bin/python
import sys, re, SearchReplace
usage = "USAGE: doService file.java [output.txt]"

oldSuperClass = ["SubObjectBaseDTO","SortOrderDTO","CustomizableDTO","LocalizableDTO", "ItemDTO"]
newSuperClass = ["AbstractSubObjectCustomizable","AbstractSortOrderObject","AbstractAuditableCustomizable","AbstractLocalizable","AbstractChild1BizObject"]
oldNewMap = dict(zip(oldSuperClass,newSuperClass))
outputFileName = "output.txt"
DO_MULTIPLE_REPLACE = True
def main():
	global outputFileName, DO_MULTIPLE_REPLACE
	# check usage	
	if(len(sys.argv) <2):
		print usage
		sys.exit()
	
	# assign inputs
	javaFileName = sys.argv[1]
	if(len(sys.argv) >= 2):
		outputFileName = sys.argv[2]
		print "using output file: " + outputFileName 
	

	#file = fileToList(javaFileName,False)
	sr = SearchReplace.SearchReplace(javaFileName)
	# step 2
	sr.printStep(2)
	replaceSuperClass(sr)
	# step 3 - 9
	# in dto
	# step 10
	sr.printStep(10)
	sr.regExReplace(r'(public\s+[^{}();]*\s+(get[A-Za-z0-9_]*|[A-Za-z0-9_]*HasBeenSet)\s*\(\s*\))',r'@Transient\n\1', DO_MULTIPLE_REPLACE)
	sr.doImport("import javax.persistence.Transient;");
	# step 11
	sr.printStep(11)
	go = sr.regExReplace(r'(public (\w+)DTO get.+)',r'@ManyToOne\n//TODO: enter column name\n@JoinColumn(name="\2Id")\n\1',DO_MULTIPLE_REPLACE)
	sr.regExReplace('@Transient\s@ManyToOne','@ManyToOne',DO_MULTIPLE_REPLACE)
	if go:
		sr.doImport("import javax.persistence.ManyToOne;")	
		sr.doImport("import javax.persistence.JoinColumn;")
		
	# step 12
	# in dto
	# step 13
	sr.printStep(13)
	sr.regExReplace('addValueToMap', 'resetLocalization',DO_MULTIPLE_REPLACE)
	
	# change StateFulBusinesSObject to Stateful
	sr.printStep("StateFulBusinesSObject to Stateful")
	sr.regExReplace('com.bricsnet.core.util.model.StatefulBusinessObject',"com.bricsnet.core.util.model.type.Stateful",not DO_MULTIPLE_REPLACE)
		
	sr.listToFile(outputFileName)

# replaces the superclass of a file depending on mapping	
def replaceSuperClass(sr):
	finished = False
	file = sr.listFile
	for i,line in enumerate(file):
		for old, new in oldNewMap.items():
			p = re.compile("extends (\w+\.)*\s*"+old)
			result = p.subn(r"extends "+new, line)
			
			if result[1]>0:
				print 'result: '+str(result)
				if old=="CustomizableDTO" and sr.checkImplements("RootObject"):
					new = "AbstractRootObject"
				if old=="LocalizableDTO" and sr.checkImplements("Auditable"):
					new = "AbstractBizObjectAuditable"
				if old=="ItemDTO" and sr.checkImplements("Auditable"):
					new = "AbstractChild1Auditable"
				print "super: match - "+old+"\t"+new+"\n\told:"+line
				
				line = line.replace(old, new)
				
				file[i] =line
				print "\tnew:"+line
				sr.doImport( "import com.bricsnet.core.util.impl.type."+new+";")
				finished = True
				break
		if finished:
			break

	if finished:
		print "Super Class replaced"
	else:
		print "Super Class NOT replaced"
		p = re.compile("public abstract class (\w+)")
		for i,line in enumerate(file):
			result = p.match(line)
			if(result):
				file[i] = result.group(0)+" extends AbstractBase"
				sr.doImport("import com.bricsnet.core.util.impl.type.AbstractBase;")
				break
				
	return finished

main()
