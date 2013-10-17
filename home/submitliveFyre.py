#!/usr/bin/python3

import re,sys

# We use a corpus of four documents.  Each document has an id, and
# these are the keys in the following dict.  The values are the
# corresponding filenames.
DOCUMENT_URL = ""
docString = ""

# termFrequency: a defaultdict whose keys are terms, and whose values are 
# the count of them

termFrequency = {}

# The list of characters (mostly, punctuation) we want to strip out of
# terms in the document.
characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>"

def main():
	global DOCUMENT_URL
	#DOCUMENT_URL = input("Document URL >> ")
	DOCUMENT_URL = "../input/imdbShort.txt"
	global termFrequency
	
	print(("reading:\t"+DOCUMENT_URL))
	document = open(DOCUMENT_URL, 'r')
	terms = tokenize(document)
	#print("\ttokenized")
	unique_terms = set(terms)
	
	#reverse index
	reverseIndex = {}
	
	#print(docString)
	for term in unique_terms:
		termFrequency[term] = terms.count(term) # the value is the
											   # frequency of the
											   # term in the
											   # document
		foundIndexList = findGet(docString, term,0,[])
		reverseIndex[term]=foundIndexList
		print("Term: ",str(term),"value: ",str(foundIndexList),"\n\n")
	print(str(termFrequency))
	print("term frequency - END")
	print(str(reverseIndex))
	

def tokenize(document):
	global docString
	terms = []
	for line in document:
		terms.extend(line.lower().split())
		docString= docString+ line.lower()
	#print(terms)	
	#print("tokeninzing end")	
	#terms = document.split()
	return [term.strip(characters) for term in terms]

# finds a search term and returns the match object and the 
	# index that it was found at
	# is a list of tuples 
	# [(found string, index)+]
def findGet(docString, searchTerm, start, list):
	if len(searchTerm)<1:
		return []	
	docStringIndex = docString.find(searchTerm,start)
	print("searchTerm:",searchTerm,"\n\tstart",str(start),"\n\tindex", str(docStringIndex))
	if docStringIndex == -1:
		print('\tRETURNING list',str(list))
		return list
	else:
		list.extend([docStringIndex])
		val = findGet(docString,searchTerm,docStringIndex+1,list)
		if val !=None:
			print('\t\tVAL',val)
			print('\t\tLIST:',str(list))
			return list.extend(val)
	
if __name__ == "__main__":
	main()
