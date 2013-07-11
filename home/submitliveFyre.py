#!/usr/bin/python3

import re,sys

# We use a corpus of four documents.  Each document has an id, and
# these are the keys in the following dict.  The values are the
# corresponding filenames.
DOCUMENT_URL = ""
docString = ""

# postings: a defaultdict whose keys are terms, and whose values are 
# the count of them

postings = {}

# The list of characters (mostly, punctuation) we want to strip out of
# terms in the document.
characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>"

def main():
	global DOCUMENT_URL
	DOCUMENT_URL = input("Document URL >> ")
	#DOCUMENT_URL = "../input/imdbShort.txt"
	global postings
	
	print(("reading:\t"+DOCUMENT_URL))
	document = open(DOCUMENT_URL, 'r')
	terms = tokenize(document)
	#print("\ttokenized")
	unique_terms = set(terms)
	
	#reverse index
	d = {}
	
	#print(docString)
	for term in unique_terms:
		postings[term] = terms.count(term) # the value is the
											   # frequency of the
											   # term in the
											   # document
		d[term]=findGet(docString, term,0)
	print(str(postings))
	print("posting end")
	print(str(d))
	

def tokenize(document):
	global docString
	terms = []
	for line in document:
		terms.extend(line.lower().split())
		docString= docString+ line
	print(terms)	
	print("tokeninzing end")	
	#terms = document.split()
	return [term.strip(characters) for term in terms]

# finds a search term and returns the match object and the 
	# index that it was found at
	# is a list of tuples 
	# [(found string, index)+]
def findGet(docString, searchTerm, start):
	global DOCUMENT_LIST_FORM
	docStringIndex = docString.find(searchTerm)
	if docStringIndex != -1:
		return [docStringIndex]
		#return [docStringIndex, findGet(docString,searchTerm,docStringIndex+1)]
	else:
		return []
    
if __name__ == "__main__":
	main()
