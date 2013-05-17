#!/usr/bin/python27
# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    hl = makeHashList(graph)
    #print connected_nodes(graph)
    r=[]
    fromNode=graph[0][0]
    r.append(fromNode)
    while len(hl)>0:
        # (0, [1,4])
        # fromList starts out at [1,4]
        fromList=hl[fromNode]
        print 'fromList',fromList
        # toNode = 4
        try:
            toNode=fromList.pop()
        except IndexError:
            print 'r',r,'\ngraph',graph
            #is_eulerian_tour(r, graph)
            return r
        r.append(toNode)
        
        # remove reverse edge ie 4,0
        hl[toNode].remove(fromNode)
        fromNode=toNode

def makeHashList(graph):
    d={}
    for node in graph:
        key = node[0]
        value=node[1]
        try:
            d[key].append(value)
        except KeyError:
            d[key]=[value]
        try:
            d[value].append(key)
        except KeyError:
            d[value]=[key]
    #print 'd',d
    return d
    
find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
find_eulerian_tour([(1, 2), (2, 3), (3, 1)])
