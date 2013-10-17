#!/usr/bin/python27
# Write centrality_max to return the maximum distance
# from a node to all the other nodes it can reach
#
from operator import itemgetter

def centrality_avg(G, v):
    distanceFromStart={}
    openList=[v]
    distanceFromStart[v]=0
    while len(openList)>0:
        current=openList[0]
        del openList[0]
        for neighbor in G[current].keys():
            if neighbor not in distanceFromStart:
                distanceFromStart[neighbor]=distanceFromStart[current]+1.
                openList.append(neighbor)
    #print max(distanceFromStart.values()),v,distanceFromStart
    return sum(distanceFromStart.values())/(len(distanceFromStart.values()))

#################
# Testing code
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    f=open('../input/imdb.txt','r')
    G = {}
    actors=[]
    for l in f:
        (actor,movie,year)=l.split('\t')
        actors.append(actor)
        make_link(G,actor,movie+" "+year)
    actors=set(actors)
    
    J=[]

    for actor in actors:
        #print 'actor: ',actor
        c=centrality_avg(G, actor)
        #c=score
        J.append((c,actor))
    #print H
    vs=sorted(J, key=itemgetter(0))
    
    for i in range(21):
        print i,vs[i]
    print len(J),len(H)
test()