#!/usr/bin/python27

#################
# Testing code
#
mxNode1=''
mxNode2=''
mx=0
def make_link(G, node1, node2):
	if node1 not in G:
		G[node1] = {}
	(G[node1])[node2] = 1
	if node2 not in G:
		G[node2] = {}
	(G[node2])[node1] = 1
	return G

	
def make_link_add(G, node1, node2):
	global mxNode1, mxNode2,mx
	if node1==node2:
		return G
	if node1 not in G:
		G[node1] = {}
	try:
		(G[node1])[node2] += 1
		if (G[node1])[node2]>mx:
			mxNode1=node1
			mxNode2=node2
			mx=(G[node1])[node2]
	except KeyError:
		(G[node1])[node2] = 1
	if node2 not in G:
		G[node2] = {}
	try:
		(G[node2])[node1] += 1
	except KeyError:
		(G[node2])[node1] = 1
	
	return G
	
def test():
	f=open('../input/marvelComic.txt','r')
	G = {}
	H = {}
	charactors=[]
	for l in f:
		(character,comic)=l.split('\t')
		charactors.append(character)
		make_link(G,character,comic)
	charactors=set(charactors)
	i=0
	for character in charactors:
		#print character,'\n\t',G[character]
		comics = G[character]
		for comic in comics:
			characters2 = G[comic]
			for character2 in characters2:
				make_link_add(H,character,character2)
		
		# i+=1
		# if i==5:
			# break
	# for character in charactors:
		# print character,'\n\t',H[character]
	print mx,mxNode1,mxNode2
test()