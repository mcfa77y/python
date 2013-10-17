#!/usr/bin/python27
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
# 


def dijkstra(G,v):
    dist_so_far_list = []
    dist_so_far_list.append((v,0))
    index={}
    dist_so_far = {}
    dist_so_far[v] = 0
    
    final_dist = {}
    while len(final_dist) < len(G):
        #shorty = shortest_dist_node(dist_so_far)
        # get minimum aka shorty
        shorty = getNode(dist_so_far_list[0])
        
        # lock it down!
        final_dist[shorty] = dist_so_far[shorty]
        #print "\ndist so far: ",dist_so_far
        #print "final dist: ",final_dist
        del dist_so_far[shorty]
       
        remove_min(dist_so_far_list,index)
       
        
        print 'shorty:',shorty
        for neighbor in G[shorty]:
            if neighbor not in final_dist: #if node not finalized
                weightShortyToNeighbor = final_dist[shorty] + G[shorty][neighbor]
                #print '\tneighbors of shorty:', neighbor,weightShortyToNeighbor
                if neighbor not in dist_so_far: # if node is not in dist_so_far
                    dist_so_far[neighbor] = weightShortyToNeighbor #init
                    print '\tadd',neighbor, dist_so_far[neighbor]
                    index[neighbor]=add_node(dist_so_far_list,(neighbor,weightShortyToNeighbor))
                elif weightShortyToNeighbor < dist_so_far[neighbor]:
                    print '\tremove',neighbor, dist_so_far[neighbor]
                    oldNodeIndex = index[neighbor]
                    dist_so_far[neighbor] = weightShortyToNeighbor #update
                    newNode = (neighbor,weightShortyToNeighbor)
                    #add_node(dist_so_far_list,(neighbor,weightShortyToNeighbor))
                    index[neighbor]=update_node(dist_so_far_list,oldNodeIndex,newNode)
                    
    print 'final_dist',final_dist
    return final_dist

    
############
# heap stuff
############
def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))
def getWeight(tuplet):
    #print 'getWeight tuplet',tuplet
    (node,weight)=tuplet
    return weight
def getNode(tuplet):
    #print 'getNode tuplet',tuplet
    (node,weight)=tuplet
    return node
def remove_min(L,index):
    print '\tremove min:'
    print '\t\tL',L
    last = len(L)-1
    # overwrite min node
    #del index[getNode(L[0])]
    L[0]=L[last]
    # remove last node
    L.pop()
    print '\t\tindex\':',index
    down_heapify(L,0,index)
    print '\t\tL\'',L
    print '\t\tindex\':',index
    return

def update_node(L,oldNodeIndex,newNode):
    print '\n\tupdate_node:\n\t\tL:',L,'\n\t\tnode:',oldNodeIndex,newNode
    # overwrite old node
    L[oldNodeIndex]=newNode
    index = up_heapify(L,oldNodeIndex)
    print '\tL\':',L
    print 'index:',index
    return index
    
def add_node(L,node):
    print '\n\tadd_node:\n\t\tL:',L,'\n\t\tnode:',node
    L.append(node)
    last = len(L)-1
    index = up_heapify(L,last)
    print '\t\tL\':',L
    return index

def up_heapify(L, i):
	# reached the root
	if i==0: return i
	if getWeight(L[i])<getWeight(L[parent(i)]):
		# Swap into parent
		print 'swap up'
		(L[i], L[parent(i)]) = (L[parent(i)], L[i])
		up_heapify(L, parent(i))
		return i
	return i
    
# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its immediate children
def down_heapify(L, i,index):
    # If i is a leaf, heap property holds
    if is_leaf(L, i): 
        print 'is leaf'
        return i
    # If i has one child...
    if one_child(L, i):
        # check heap property
        if getWeight(L[i]) > getWeight(L[left_child(i)]):
            # If it fails, swap, fixing i and its child (a leaf)
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
            print 'one child swap'
            index[getNode(L[i])]=left_child[i]
            index[getNode(L[left_child(i)])]=i
        return i
    # If i has two children...
    # check heap property
    if min(getWeight(L[left_child(i)]), getWeight(L[right_child(i)])) >= getWeight(L[i]): 
        print 'nothing'
        return i
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if getWeight(L[left_child(i)]) < getWeight(L[right_child(i)]):
        # Swap into left child
        print 'swap into left child'
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        index[getNode(L[i])]=left_child[i]
        index[getNode(L[left_child(i)])]=i
        down_heapify(L, left_child(i))
        return i
    else:
        print 'swap into left child'
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        index[getNode(L[i])]=right_child[i]
        index[getNode(L[right_child(i)])]=i
        down_heapify(L, right_child(i))
        return i

#########
# Testing Code
#

# build_heap
def build_heap(L):
    # count backwards from len(L) to -1
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i)
    return L

    
############
# 
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3), 
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)

test()    




