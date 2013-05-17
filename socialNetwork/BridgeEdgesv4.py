#!/usr/bin/python27
# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#       
import copy

def areAllGreenChildrenMarked(G,node,marked):
    add=True
    #check the neigbhors of the neighbors
    for neighbor2 in G[node].keys():
        if G[node][neighbor2]=='red':
            continue
        if neighbor2 not in marked:
            #print '\t\t unmarked neighbor',neighbor2
            return False
    return add
    
def getNeighborsPostOrder(po,S,current,openList):
    # get neighbors who are in not in the open list or are of the color red
    neighbors=[neighbor for neighbor in S[current].keys() if neighbor not in openList or S[current][neighbor]=='red']
    #print 'getNPO',neighbors,[po[neighbor] for neighbor in neighbors]
    return [po[neighbor] for neighbor in neighbors]

def create_rooted_spanning_tree(G, root):
    marked={}
    marked[root] = True
    total_marked = 1
    openList=[root]
    S=copy.deepcopy(G)
    while len(openList)>0:
        current=openList[0]
        del openList[0]
        for neighbor in G[current].keys():
            if neighbor not in marked:
                openList.append(neighbor)
                marked[neighbor]=True
                S[current][neighbor]='green'
                S[neighbor][current]='green'
                #print 'current', current
                #print '\tneighbor', neighbor
                total_marked +=1
            elif S[current][neighbor]==1:
                S[current][neighbor]='red'
                S[neighbor][current]='red'
                #print 'xcurrent', current
                #print '\txneighbor', neighbor
                
    #print 'S', S
    return S

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'red'}, 
                 'c': {'a': 'green', 'd': 'green'}, 
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

###########

def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    marked=[]
    marked.append(root)
    tally=0
    openList=[root]
    po={}
    while len(openList)>0:
        current=openList[len(openList)-1]
        #print 'current', current
        for neighbor in S[current].keys():
            if neighbor not in marked:
                openList.append(neighbor)
                marked.append(neighbor)
                #print '\topenList',openList
                #print '\tneighbor',neighbor
            # check the neighbors of the current node
            elif areAllGreenChildrenMarked(S,current,marked) and len(openList)>0:
                tally+=1
                po[current]=tally
                openList.pop()
                #print 'po',po
                #print '\topenList',openList
                #print '\tmarked',marked
                break
    #print 'po',po
    return po

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
    
#test_post_order()
##############

def number_of_descendants(S, root):
    marked = []
    marked.append(root)
    tally=0
    openList=[root]
    po={}
    while len(openList)>0:
        current=openList[len(openList)-1]
        #print 'current', current
        for neighbor in S[current].keys():
            if neighbor not in marked:
                openList.append(neighbor)
                marked.append(neighbor)
                #print '\topenList',openList
                #print '\tneighbor',neighbor
            # check the neighbors of the current node
            elif areAllGreenChildrenMarked(S,current,marked) and len(openList)>0:
                tally+=1
                #print 'keys',S[current].keys()
                # adds 1 to the sum of values from the children if they are not in open list
                # and they are not red paths
                po[current]= 1+sum(po[x] for x in S[current].keys() if x not in openList and S[current][x]!='red')
                openList.pop()
                #print 'po',po
                #print '\topenList',openList
                #print '\tmarked',marked
                break
        
    print 'xxpo',po
    return po

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}
#test_number_of_descendants()
###############

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    marked = []
    marked.append(root)
    openList=[root]
    lpo={}
    while len(openList)>0:
        current=openList[len(openList)-1]
        #print 'current', current
        #loop through the neighbors
        for neighbor in S[current].keys():
            if neighbor not in marked:
                openList.append(neighbor)
                marked.append(neighbor)
                #print '\topenList',openList
                #print '\tneighbor',neighbor
            # check the neighbors of the current node
            elif areAllGreenChildrenMarked(S,current,marked) and len(openList)>0:
                # gets the min for neigbhors 
                neighborValues = getNeighborsPostOrder(po,S,current,openList)
                if len(neighborValues)>0:
                    mn = min(po[current],min(neighborValues))
                    #print 'mn',mn
                else:
                    mn=po[current]
                # get reds
                redList=[]
                for neighbor in S[current].keys():
                    # dont go up the tree
                    if neighbor in openList:
                            continue
                    #print 'doing red search', neighbor
                    for neighbor2 in S[neighbor].keys():
                        #print '\t',neighbor2,' red?',S[neighbor][neighbor2]
                        if S[neighbor][neighbor2]=='red' and neighbor2 not in openList:
                            #print '\tneighbor2',neighbor2
                            redList.append(po[neighbor2])
                #print 'redList',redList
                if len(redList)>0:
                    lpo[current]= min(mn,min(redList))
                else:
                    lpo[current]=mn
            
                openList.pop()
                #print 'lpo',lpo
                #print '\topenList',openList
                #print '\tmarked',marked
                break
        
    #print 'xxlpo',lpo
    return lpo

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}

#test_lowest_post_order()
################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    marked = []
    marked.append(root)
    tally=0
    openList=[root]
    lpo={}
    while len(openList)>0:
        current=openList[len(openList)-1]
        #print 'current', current
        for neighbor in S[current].keys():
            if neighbor not in marked:
                openList.append(neighbor)
                marked.append(neighbor)
                #print '\topenList',openList
                #print '\tneighbor',neighbor
            # check the neighbors of the current node
            elif areAllGreenChildrenMarked(S,current,marked) and len(openList)>0:
                tally+=1
                # gets the max for neigbhors 
                neighborValues = getNeighborsPostOrder(po,S,current,openList)
                if len(neighborValues)>0:
                    mn = max(po[current],max(neighborValues))
                else:
                    mn = po[current]
                # get reds
                redList=[]
                for neighbor in S[current].keys():
                    # dont go up the tree
                    if neighbor in openList:
                            continue
                    #print 'doing red search', neighbor
                    for neighbor2 in S[neighbor].keys():
                        #print '\t',neighbor2,' red?',S[neighbor][neighbor2]
                        if S[neighbor][neighbor2]=='red' and neighbor2 not in openList:
                            #print '\tneighbor2',neighbor2
                            redList.append(po[neighbor2])
                #print 'redList',redList
                if len(redList)>0:
                    lpo[current]= max(mn,max(redList))
                else:
                    lpo[current]=mn
                openList.pop()
                #print 'lpo',lpo
                #print '\topenList',openList
                #print '\tmarked',marked
                break
        
    #print 'xxlpo',lpo
    return lpo

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
#test_highest_post_order()
#################
def getParent(G,node,po):
    p=po[node]
    for neighbor in G[node].keys():
        v=po[neighbor]
        if v-p==1:
            print '\tparent',neighbor
            return neighbor
def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    S = create_rooted_spanning_tree(G,root)
    po=post_order(S, root)
    nd=number_of_descendants(S, root)
    l=lowest_post_order(S, root, po)
    h=highest_post_order(S, root, po)
    
    print 'po',po,'\nnd',nd,'\nl',l,'\nh',h,'\nhc<=poc and lc>(ndc-poc)'
    result=[]
    marked = []
    marked.append(root)
    openList=[root]
    while len(openList)>0:
        current=openList[len(openList)-1]
        #print 'current', current
        for neighbor in S[current].keys():
            if neighbor not in marked:
                openList.append(neighbor)
                marked.append(neighbor)
                #print '\topenList',openList
                #print '\tneighbor',neighbor
            # check the neighbors of the current node
            elif areAllGreenChildrenMarked(S,current,marked) and len(openList)>0:
                lc=l[current]
                hc=h[current]
                ndc=nd[current]
                poc=po[current]
                if hc<=poc and lc>(poc-ndc):
                    print 'bridge',current, hc,poc,hc<=poc,lc,ndc-poc,lc>(poc-ndc)
                    parent = getParent(S,current,po)
                    if parent:
                        result.append((parent,current))
                openList.pop()
                break
        
    print 'result',result
    return result

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]

test_bridge_edges()