#!/usr/bin/python
links = ['Language','Locale','Currency','Measurement','Display Formats','Automatic Logout']
inputFN = './input/variableNames.txt'
import Util
U = Util.Util()
def main():
	links=U.fileToList(inputFN,False)
	mkPropFile(links)
	#mkLinksFromList(links)
	#mkSections(links)
	
	#batchPrintSections(links, '<bean:message bundle="label" key="welcome00" />','welcome00')
	#batchPrint(links, "String REPLACE;","REPLACE")
	#batchPrint(links, "insert into Currency (code, currency) values(REPLACE_TERM)","REPLACE_TERM")

def batchPrint(list, string, replacementTerm):
	for key in list:
		s = string.replace(replacementTerm,key.strip('\n'))
		print(s)

def batchPrintSections(list, string, old):
	for key in list:
		normalizedKey=normalizeKey(key)
		s = string.replace(old,normalizedKey+"_description")
		section ='\
		<s:section key="'+key+'" bundle="header">\n\
		'+s+'\n\
		</s:section>'
		print(section)
def mkSections(list):
	i=0
	for key in list:
		i+=1
		section ='\
		<s:section key="'+key+'" bundle="header" state="close">\n\
		<h1>Hello World '+str(i)+'</h1>\n\
		</s:section>'
		
		print (section)
def mkPropFile(list):
	U.printStep("make property file")
	abcList = list.sort()
	for key in list:
		# replaces spaces with _ and lowercases key
		normalizedKey=normalizeKey(key)
		#print(normalizedKey+"="+key)
		#print(normalizedKey+"="+key)
		print(key.strip())

def normalizeKey(key):
	return key.lower().replace(' ', '_')
def mkLinksFromList(list):
	print('hi')
	for key in list:
		#print(key)
		lhLink = '\
<s:group rule=\"Navigation.searchDocuments\" ruleBean=\"null\">\n\
<li>\n\
	<!-- TODO: Set link action -->\n\
	<html:link action=\"\"\n\
		module=\"\" target=\"_top\" tabindex=\"-1\" styleClass=\"FormMenuLink nowrap suppressMod\">\n\
		<s:message bundle=\"navigation\" key=\"'+normalizeKey(key)+'\"/>\n\
	</html:link><br/>\n\
</li>\n\
</s:group>\n\n'
		print (lhLink)
	
main()
