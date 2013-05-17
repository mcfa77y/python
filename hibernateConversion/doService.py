#!/usr/bin/python
import sys, re, SearchReplace
usage = "doService file.java [output.txt]"

oldSuperClass = ["BaseBusinessObjectSessionBean","BaseAncillaryObjectSessionBean","BaseSubObjectSessionBean","BaseSessionBean"]
newSuperClass = ["AbstractBizObjectService","AbstractChild1BizObjectService","AbstractChild1BizObjectService","AbstractBaseService"]
oldNewMap = dict(zip(oldSuperClass,newSuperClass))
outputFileName = "output.txt"
DO_MULTIPLE_REPLACE = True
global file
def main():
	global outputFileName, DO_MULTIPLE_REPLACE
	# enforce usage
	if(len(sys.argv) <2):
		print usage
		sys.exit()
	
	# assign inputs
	if(len(sys.argv) == 3):
		outputFileName = sys.argv[2]
	#filterFileName = sys.argv[1]
	javaFileName = sys.argv[1]

	sr = SearchReplace.SearchReplace(javaFileName)
	# step 2
	sr.printStep(2)
	replaceSuperClass(sr)
	# step 3
	sr.printStep(3)
	sr.replace("public abstract class","public class", not DO_MULTIPLE_REPLACE)
	# step 4
	sr.printStep(4)
	sr.replace("implements SessionBean","", not DO_MULTIPLE_REPLACE)
	# step 5
	sr.printStep(5)
	go = sr.replace("getUserPrincipal","ThreadUserPrincipal.getUserPrincipal", DO_MULTIPLE_REPLACE)
	if go:
		sr.doImport("import com.bricsnet.core.util.hibernate.ThreadUserPrincipal;")
	sr.deleteLines( "private UserPrincipal ThreadUserPrincipal\.getUserPrincipal", -3,6)
	# step 6
	sr.printStep(6)
	sr.replace("dto.localize\(principal\);","", DO_MULTIPLE_REPLACE)
	# step 7
	sr.printStep(7)
	sr.deleteLines( "public void setSessionContext", -4,8)
	sr.replace("dto.convertFromLocalized\(p\);","", DO_MULTIPLE_REPLACE)
	# step 12
	sr.printStep(12)
	go = sr.replace("EJBException","ServiceException", DO_MULTIPLE_REPLACE)
	if go:
		sr.doImport("import com.bricsnet.core.util.model.ServiceException;");
		sr.replace("import javax.ejb.ServiceException;","",not DO_MULTIPLE_REPLACE
		)
	# step 13
	sr.printStep(13)
	sr.replace("[\ \t]*/\*\*(\s*\*\s*)*(\s*\*\s*\@ejb.*\r)+(\s*\*\s*\R)*\s*\*/\s*?\r|([\ \t]*\*\s*)*(\s*\*\s*\@ejb.*\r)","", DO_MULTIPLE_REPLACE)
	
	# add throws service exception for create update delete
	sr.printStep("add throws service exception for create update delete")
	sr.replace(r'(public (.+) create\(.+\))',r'\1 throws ServiceException',DO_MULTIPLE_REPLACE)
	sr.replace(r'(public (.+) delete\(.+\))',r'\1 throws ServiceException',DO_MULTIPLE_REPLACE)
	sr.replace(r'(public (.+) update\(.+\))',r'\1 throws ServiceException',DO_MULTIPLE_REPLACE)
	sr.replace(r'(public (.+) get\w+\(.+\))',r'\1 throws ServiceException',DO_MULTIPLE_REPLACE)
	# fix thows throws service exception throws exception
	sr.printStep(" fix thows throws service exception throws exception")
	go=sr.replace(r'(throws ServiceException\s*throws Exception)',r'throws ServiceException',DO_MULTIPLE_REPLACE)
	if go:
		sr.replace("import com.bricsnet.core.util.model.ServiceException;","",not DO_MULTIPLE_REPLACE)
		sr.doImport("import com.bricsnet.core.util.model.ServiceException;");
	sr.listToFile( outputFileName)
	
	# replace other services
	sr.printStep("replace other services")
	sr.replace(r"List (\w+) = (\w+)Util\.getLocalHome\(\)\.create\(\)\s+\.get(.+)",r"List <> \1 = new \2().get\4",DO_MULTIPLE_REPLACE)
	
	# replace generic create services
	sr.replace(r"BusinessObjectObserver\.beforeCreate\(dto, null, p\);\s*(\w+)DTO (\w+) = (\w+)Util\.getLocalHome\(\)\.create\(dto\)\s*\.get(\w+)DTO\(\);\s*dto\.setId\(created\.getId\(\)\);\s*BusinessObjectObserver\.afterCreate\(dto, null, p\);\s*return (\w+);",r"return super.create(dto);", not DO_MULTIPLE_REPLACE);
# replaces the superclass of a file depending on mapping	
def replaceSuperClass(sr):
	finished = False
	file = sr.listFile
	for i,line in enumerate(file):
		for old, new in oldNewMap.items():
			p = re.compile("extends (\w+\.)*"+old)
			result = p.subn(new, line)
			if result[1]>0:
				print "super: "+old+"\t"+new+"\n\to:"+line
				line = line.replace(old, new)
				file[i] =line
				print "\tn:"+line+"\n\tr:"+result[0]
				sr.doImport( "import com.bricsnet.core.util.impl.service."+new+";")
				finished = DO_MULTIPLE_REPLACE
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
				file[i] = "\n//TODO: \n"+							"//\t1. If the DTO implements BizObject (including extending AbstractBizObject), the service extends AbstractBizObjectService.\n"+							"//\t2. Else, if the DTO has a getId() method that returns an Integer or int, the service extends AbstractSingleIdService.\n"							"//\t3. Else, the service extends AbstractBaseService. \n"
				file.insert(i+1, result.group(0)+" extends AbstractBizObjectService{"				+ "\n//"+result.group(0)+" extends AbstractSingleIdService{"				+ "\n//"+result.group(0)+" extends AbstractBaseService{")
				sr.doImport("import com.bricsnet.core.util.impl.service.AbstractBizObjectService;")
				sr.doImport("import com.bricsnet.core.util.impl.service.AbstractSingleIdService;")
				sr.doImport("import com.bricsnet.core.util.impl.service.AbstractBaseService;")
				break
				
	return finished

main()
