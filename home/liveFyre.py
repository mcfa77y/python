#!/usr/bin/python3
from urllib.request import urlopen,urlretrieve,FancyURLopener
from bs4 import BeautifulSoup
from math import log, sqrt
from itertools import combinations

import re,sys,functools, pickle

"""vsm.py implements a toy search engine to illustrate the vector
space model for documents.

It asks you to enter a search query, and then returns all documents
matching the query, in decreasing order of cosine similarity,
according to the vector space model."""

from collections import defaultdict
import math
import sys



# dup a user agent to bypass 403 HTTP errors
class MyOpener(FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

MAX=120
COUNTER=0
#URL='http://greenwake.keenspot.com/d/20120206.html'
#IMG_PATTERN=re.compile('http://cdn.greenwake.keenspot.com/comics/gw\d+\.jpg')
#URL='http://sfbay.craigslist.org/sfc/sof/3786775038.html'
URL='http://sfbay.craigslist.org/search/sof/sfc?zoomToPosting=&query=java+-qa&srchType=A'
BASE_URL='http://sfbay.craigslist.org'
IMG_PATTERN=re.compile('http://dis-connection.com/comics/\d+\.jpg')
SCRIPT_TAG=re.compile(r'<script.*?>.*?</script>')
TAGS=re.compile(r'</?.*?>|\[|\]')

def getUrlList(soup):
	links = soup.find_all(href=re.compile('/sfc/sof/'))
	urls={}
	i=0
	ll=[]
	for link in links:
		#print(("link: "+link.attrs['href']))
		ll.append(BASE_URL+link.attrs['href'])
	ll=set(ll)
	for l in ll:	
		urls[i]=l
		i+=1
	#print(str(urls))
	return urls

# We use a corpus of four documents.  Each document has an id, and
# these are the keys in the following dict.  The values are the
# corresponding filenames.
document_filenames = getUrlList(BeautifulSoup(urlopen(URL)))

# The size of the corpus
N = len(document_filenames)

# dictionary: a set to contain all terms (i.e., words) in the document
# corpus.
dictionary = set()

# postings: a defaultdict whose keys are terms, and whose
# corresponding values are the so-called "postings list" for that
# term, i.e., the list of documents the term appears in.
#
# The way we implement the postings list is actually not as a Python
# list.  Rather, it's as a dict whose keys are the document ids of
# documents that the term appears in, with corresponding values equal
# to the frequency with which the term occurs in the document.
#
# As a result, postings[term] is the postings list for term, and
# postings[term][id] is the frequency with which term appears in
# document id.
postings = defaultdict(dict)
doc_tf = defaultdict(dict)
doc_tfidf = defaultdict(dict)
page_text = {}
# document_frequency: a defaultdict whose keys are terms, with
# corresponding values equal to the number of documents which contain
# the key, i.e., the document frequency.
document_frequency = defaultdict(int)

# length: a defaultdict whose keys are document ids, with values equal
# to the Euclidean length of the corresponding document vector.
length = defaultdict(float)

# The list of characters (mostly, punctuation) we want to strip out of
# terms in the document.
characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>"


def readUrl(url):	
	global MAX, COUNTER, IMG_PATTERN,URL, page_text

	soup = BeautifulSoup(urlopen(url))
	pageText =str(soup.find(id='postingbody'))
	page_text[url]=re.compile(r'<.*section.*>').sub('',pageText)
	pagePosition=str(soup.find_all('h2'))
	pageText = removeTags(pageText)
	pagePosition = removeTags(pagePosition)
	
	return (pagePosition+"\n"+pageText)
	
def removeTags(s):
	return TAGS.sub('',s)


def getEmail(url):
	soup = BeautifulSoup(urlopen(url))
	#pageText = soup.find(classs='postingtitle')
	pageText = str(soup.find("a", { "class" : "gmail" }))
	#pageText = removeTags(pageText).strip()
	print("email: "+pageText)
	
	return (pageText)
	
def getTitle(url):
	soup = BeautifulSoup(urlopen(url))
	#pageText = soup.find(classs='postingtitle')
	pageText = str(soup.find("h2", { "class" : "postingtitle" }))
	pageText = removeTags(pageText).strip()
	print("title: "+pageText)
	
	return (pageText)

def main():
	global doc_tfidf,page_text
	#initialize_terms_and_postings()
	#initialize_document_frequencies()
	#initialize_lengths()
	
	#pickle.dump(doc_tfidf,open('../input/doc_tfidf.p','wb'))
	#pickle.dump(document_filenames,open('../input/document_filenames','wb'))
	#pickle.dump(page_text,open('../input/page_text.p','wb'))
	
	doc_tfidf= pickle.load( open( "../input/doc_tfidf.p", "rb" ) )
	document_filenames = pickle.load( open( "../input/document_filenames.p", "rb" ) )
	page_text = pickle.load( open( "../input/page_text.p", "rb" ) )

	
	dist_graph = get_distance_graph(doc_tfidf)
	#pickle.dump(dist_graph,open('../input/dist_graph.p','wb'))
	#dist_graph= pickle.load( open( "../input/dist_graph.p", "rb" ) )
	#document_filenames = pickle.load( open( "../input/document_filenames.p", "rb" ) )
	f = open("jorbOutput.html",'w')
	g = open("../input/htmlHeader.html",'r')
	for line in g:
		f.write(line)
	i=0
	for cluster in majorclust(dist_graph):
		print("=========")
		f.write("<div id=\"accordion-"+str(i)+"\">")
		i+=1
		for doc_id in cluster:
			docUrl = str(document_filenames[doc_id])
			title = getTitle(docUrl)
			emailUrl = getEmail(docUrl)
			f.write("\n<h3>"+title+"</h3>\n\t<div>")
			f.write("<div style=\"text-align:right\"><a href=\""+docUrl+"\">"+title+"</a>")
			f.write
			f.write("</div><br>\n")
			f.write(page_text[docUrl])
			f.write("\t</div>")
			print(docUrl)
		f.write("</div>")
		f.write("<hr>")
	f.write("</body></html>\n")
	f.close()
	
def initialize_terms_and_postings():
	"""Reads in each document in document_filenames, splits it into a
	list of terms (i.e., tokenizes it), adds new terms to the global
	dictionary, and adds the document to the posting list for each
	term, with value equal to the frequency of the term in the
	document."""
	global dictionary, postings,N, document_frequency, doc_tf,doc_tfidf
	
	for id in document_filenames:
		print(("reading: "+str(id)+"\t"+document_filenames[id]))
		document = readUrl(document_filenames[id])
		terms = tokenize(document)
		#print("\ttokenized")
		unique_terms = set(terms)
		#print("\tuniqued")
		dictionary = dictionary.union(unique_terms)
		#print("\tdict union")
		for term in unique_terms:
			postings[term][id] = terms.count(term) # the value is the
												   # frequency of the
												   # term in the
												   # document
		num_tokens = len(unique_terms)
		if num_tokens >0:
			for term in unique_terms:
				score = float(postings[term][id])/num_tokens
				doc_tf[term][id]=score
				#print("term: "+term+"\tid:"+str(id)+"\tscore:"+str(doc_tf[term][id]))
	for term,docIds in list(doc_tf.items()):
		docLen = len(doc_tf[term])
		if docLen>0:
			idf = log(N/docLen)
			for id, tf in list(docIds.items()):
				tfidf = doc_tf[term][id]*idf
				if tfidf>0:
					doc_tfidf[id][term]=tfidf
					
					
def init_document_term_tfidf():
	tokens = {}
	for id, doc in enumerate(documents):
		tf = {}
		doc["tfidf"] = {}
		doc_tokens = doc.get("tokens", [])
		for token in doc_tokens:
			tf[token] = tf.get(token, 0) + 1
		num_tokens = len(doc_tokens)
		if num_tokens > 0:
			for token, freq in tf.items():
				tokens.setdefault(token, []).append((id, float(freq) / num_tokens))

	doc_count = float(len(documents))
	for token, docs in tokens.items():
		idf = log(doc_count / len(docs))
		for id, tf in docs:
			tfidf = tf * idf
			if tfidf > 0:
				documents[id]["tfidf"][token] = tfidf

	for doc in documents:
		doc["tfidf"] = normalize(doc["tfidf"])
def tokenize(document):
	"""Returns a list whose elements are the separate terms in
	document.  Something of a hack, but for the simple documents we're
	using, it's okay.  Note that we case-fold when we tokenize, i.e.,
	we lowercase everything."""
	terms = document.lower().split()
	return [term.strip(characters) for term in terms]

def initialize_document_frequencies():
	"""For each term in the dictionary, count the number of documents
	it appears in, and store the value in document_frequncy[term]."""
	global document_frequency
	for term in dictionary:
		document_frequency[term] = len(postings[term])

def initialize_lengths():
	"""Computes the length for each document."""
	global length
	for id in document_filenames:
		l = 0
		for term in dictionary:
			l += imp(term,id)**2
		length[id] = math.sqrt(l)

def imp(term,id):
	"""Returns the importance of term in document id.  If the term
	isn't in the document, then return 0."""
	if id in postings[term]:
		return postings[term][id]*inverse_document_frequency(term)
	else:
		return 0.0

def inverse_document_frequency(term):
	"""Returns the inverse document frequency of term.  Note that if
	term isn't in the dictionary then it returns 0, by convention."""
	N = len(document_filenames)
	if term in dictionary:
		print(("IDF:\n\t"+str(N)+":"+str(document_frequency[term])))
		return math.log(N/document_frequency[term],2)
	else:
		return 0.0

def do_search():
	"""Asks the user what they would like to search for, and returns a
	list of relevant documents, in decreasing order of cosine
	similarity."""
	query = tokenize(eval(input("Search query >> ")))
	if query == []:
		sys.exit()
	# find document ids containing all query terms.  Works by
	# intersecting the posting lists for all query terms.
	relevant_document_ids = intersection(
			[set(postings[term].keys()) for term in query])
	if not relevant_document_ids:
		print("No documents matched all query terms.")
	else:
		scores = sorted([(id,similarity(query,id))
						 for id in relevant_document_ids],
						key=lambda x: x[1],
						reverse=True)
		print("Score: filename")
		for (id,score) in scores:
			print((str(score)+": "+document_filenames[id]))

def intersection(sets):
	"""Returns the intersection of all sets in the list sets. Requires
	that the list sets contains at least one element, otherwise it
	raises an error."""
	return functools.reduce(set.intersection, [s for s in sets])

def similarity(query,id):
	"""Returns the cosine similarity between query and document id.
	Note that we don't bother dividing by the length of the query
	vector, since this doesn't make any difference to the ordering of
	search results."""
	similarity = 0.0
	for term in query:
		if term in dictionary:
			similarity += inverse_document_frequency(term)*imp(term,id)
	print(("id: "+str(id)))
	if length[id]==0:
		return 0.0
	similarity = similarity / length[id]
	return similarity
	
def document_similarity(id0,id1):
	"""Returns the cosine similarity between query and document id.
	Note that we don't bother dividing by the length of the query
	vector, since this doesn't make any difference to the ordering of
	search results."""
	similarity = 0.0
	for term in query:
		if term in dictionary:
			similarity += inverse_document_frequency(term)*imp(term,id1)
	print(("id1: "+str(id1)))
	if length[id1]==0:
		return 0.0
	similarity = similarity / length[id1]
	return similarity
	
def cosine_distance(a, b):
	cos = 0.0
	a_tfidf = a
	for token in b:
		if token in a_tfidf:
			cos += b[token] * a_tfidf[token]
	return cos
	
def choose_cluster(node, cluster_lookup, edges):
	new = cluster_lookup[node]
	if node in edges:
		seen, num_seen = {}, {}
		for target, weight in edges.get(node, []):
			seen[cluster_lookup[target]] = seen.get(
				cluster_lookup[target], 0.0) + weight
		for k, v in list(seen.items()):
			num_seen.setdefault(v, []).append(k)
		new = num_seen[max(num_seen)][0]
	return new

def majorclust(graph):
	cluster_lookup = dict((node, i) for i, node in enumerate(graph.nodes))

	count = 0
	movements = set()
	finished = False
	while not finished:
		finished = True
		for node in graph.nodes:
			new = choose_cluster(node, cluster_lookup, graph.edges)
			move = (node, cluster_lookup[node], new)
			if new != cluster_lookup[node] and move not in movements:
				movements.add(move)
				cluster_lookup[node] = new
				finished = False

	clusters = {}
	for k, v in cluster_lookup.items():
		clusters.setdefault(v, []).append(k)

	return list(clusters.values())

def get_distance_graph(documents):
	global document_filenames, N
	class Graph(object):
		def __init__(self):
			self.edges = {}

		def add_edge(self, n1, n2, w):
			self.edges.setdefault(n1, []).append((n2, w))
			self.edges.setdefault(n2, []).append((n1, w))

	graph = Graph()
	doc_ids = list(range(N))
	graph.nodes = set(document_filenames)
	for a, b in combinations(document_filenames, 2):
		print(("doc A:"+str(documents[a])))
		graph.add_edge(a, b, cosine_distance(documents[a], documents[b]))
	return graph

if __name__ == "__main__":
	main()
