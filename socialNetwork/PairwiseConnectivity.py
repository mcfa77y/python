#!/usr/bin/python27
##################################################################
# Traversal...
# Call this routine on nodes being visited for the first time
# and fills marked value with nodes marked
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        print 'neighbor',neighbor
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked

def check_connection(G, v1, v2):
    # Return True if v1 is connected to v2 in G
    # or False if otherwise
    m1={}
    m2={}
    mc1=mark_component(G,v1,m1)
    b = v2 in m1
    print 'b',b 
    return b
    
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'), 
             ('b', 'f'), ('f', 'e'), ('e', 'h')]
    G = {}
    for v1, v2 in edges:
        make_link(G, v1, v2)
    assert check_connection(G, "a", "c") == True
    assert check_connection(G, 'a', 'b') == False
    


test()