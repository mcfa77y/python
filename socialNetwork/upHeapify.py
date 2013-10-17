#!/usr/bin/python27
#
# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#



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

def up_heapify(L, i):
	# reached the root
	if i==0: return
	if L[i]<L[parent(i)]:
		# Swap into parent
		print 'swap up'
		(L[i], L[parent(i)]) = (L[parent(i)], L[i])
		up_heapify(L, parent(i))
		return
	return
    
def test():
	L = [2, 4, 3, 5, 9, 7, 7]
	L.append(1)
	up_heapify(L, 7)
	print L
	assert 1 == L[0]
	assert 2 == L[1]
test()