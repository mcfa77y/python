#!/usr/bin/python
inputFN = './input/constants.txt'
DIR="C:\\projects\\trunk\\bc\\apps\\organizationWizard\\web\\jsp\\"
SOURCE=DIR+"OrganizationWizardReviewTypes.jsp"
import Util
U = Util.Util()
def main():
	global DIR, SOURCE,inputFN
	list=U.fileToList(inputFN,False)
	result=mkPutter2(list)
	#result=mkPutter(list)
	#result=mkConstants2(list)
	#result=mkFormSetterGetter(list,"systemDefaultsWizard")
	#result=mkValidationFields(list,"systemDefaultsWizardDTO")
	#result = mkConstants(list)
	print (result)

# writes putter for constants
# dtoClasses.put(OBJECT_TYPE_SPACE_ACTIVE_COST_CENTER,
 #                    "com.bricsnet.space.dal.activecostcenter.SpaceActiveCostCenterDTO"); from
# OBJECT_TYPE_FINACIAL_WIZARD
def mkPutter2(list):
	result=''
	for key in list:
		key =key.strip()
		normalKey=U.capitalize(toNormalKey(key))
		
		result+='dtoClasses.put(REPLACE_0,"com.bricsnet.wizard.dal.systemdefaultswizard.REPLACE_1DTO")'.replace("REPLACE_0",key).replace("REPLACE_1",normalKey)+"\n"
	return result
	
# writes putter for constants
# modules.put(OBJECT_TYPE_SYSTEM_DEFAULTS_WIZARD, "systemDefaultsWizard"); from
# OBJECT_TYPE_FINACIAL_WIZARD
def mkPutter(list):
	result=''
	for key in list:
		key =key.strip()
		normalKey=toNormalKey(key)
		result+='modules.put(REPLACE_0, "REPLACE_1");'.replace("REPLACE_0",key).replace("REPLACE_1",normalKey)+"\n"
	return result
# turns OBJECT_TYPE_SYSTEM_DEFAULTS_WIZARD into systemDefaultsWizard
def toNormalKey(name):
	name=name.strip()
	result=""
	if not len(name)>0:
		return result
	result+=name.replace('OBJECT_TYPE_','').title().replace('_','')
	result=U.unCapitalize(result);
	return result
# writes contants for contstants.java
# public static final int OBJECT_TYPE_MEASUREMENT_MATRIX = 5205006;
def mkConstants2(list):
	result=''
	for key in list:
		key =key.strip()
		key=key.upper().replace(" ","_") 
		print('key',key)
		result+='public static final int OBJECT_TYPE_REPLACE = 5205006;'.replace("REPLACE",key)+"\n"
	return result	
	
# make setters and getters from form
# String languageMatrix = getStringParam(request, "systemDefaultsWizard(languageMatrix", false);
#        dto.setLanguageMatrix(languageMatrix);	
def mkFormSetterGetter(list,dtoName):
	result=''
	for key in list:
		key =key.strip()
		result+='String REPLACE = getStringParam(request, "DTO(REPLACE)", true);'.replace('DTO',dtoName).replace("REPLACE",key)+"\n"
		capKey=U.capitalize(key)
		result+=' dto.setREPLACE_0(REPLACE_1);\n'.replace('REPLACE_0',capKey).replace("REPLACE_1",key)+"\n"
	return result
#make validation fields from a list
# ex)
# <field property="project(name)" depends="required,maxlength">
#				<arg0 key="ProjectDTO.name" />
#				<arg1 name="maxlength" key="${var:maxlength}" resource="false" />
#				<var>
#					<var-name>maxlength</var-name>
#					<var-value>50</var-value>
#				</var>
#			</field>	

def mkValidationFields(list,dtoName):
	result=''
	for key in list:
		key =key.strip()
		result+='			<field property="project(REPLACE)" depends="required,maxlength">'.replace("REPLACE",key)+"\n"
		result+='				<arg0 key="DTO.REPLACE" />'.replace('DTO',dtoName).replace("REPLACE",key)+"\n"
		result+='				<arg1 name="maxlength" key="${var:maxlength}" resource="false" />\n'+\
		'				<var>\n'+\
		'					<var-name>maxlength</var-name>\n'+\
		'					<var-value>50</var-value>\n'+\
		'				</var>\n'+\
		'			</field>\n\n'
		
	return result
#make struts message-resources
#public static final Integer OBJECT_TYPE_FINALIZE_WIZARD = 5205000;
def mkConstants(list):
	result=''
	for key in list:
		key =key.strip()
		result+="public static final Integer REPLACE = 5205000;".replace("REPLACE",key)+"\n"
	return result

#make struts message-resources
def mkStutsMsgResourecs(list):
	result=''
	for key in list:
		key =key.strip()
		result+= '<message-resources parameter="systemDefaultsWizard.REPLACE" key="REPLACE" null="false"'.replace('REPLACE',key)
		result+='\n\tfactory="com.bricsnet.core.util.BricsnetPropertyMessageResourcesFactory"/>\n'
	return result
# copy template to names
def copyTemplateToList(list):
	global DIR, SOURCE,inputFN
	for key in list:
			#mkStrutsComments(key):
			command = "cp "+SOURCE+" "+DIR+toJspName(key)
			U.runCmd(command)
			print(command)
			
def mkStrutsComments(key):
	out =""
	key=key.strip()
	#print("'"+key+"'")
	
	out+="* @struts.action-forward\n"
	out+="*      name=\"success_"+key.lower()+"\"\n"
	out+="*      path=\"/"+toJspName(key)+"\"\n"
	out+="*\n"
	return out

# turns REVIEW_FIELDS_MODE into OrganizationWizardReviewFields.jsp
def toJspName(name):
	name=name.strip()
	result=""
	if not len(name)>0:
		return result
	result+="OrganizationWizard"
	result+=name.title().replace('_','').replace('Mode','')
	result+=".jsp"
	return result
	
main()
