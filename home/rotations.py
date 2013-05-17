#!/usr/bin/python
# list.index(x) runs in O(n) time and so does min(list)
# O(n)+O(n) = O(2n) = O(n)
# this scripts effecientcy comes from using library code
# and minimal number of lines

# list that has been rotated right 4 times
L = [4,5,5,6,3,]

# this function prints how many times the array has been rotated
# to the right given a list.
def rotations(list):
	print(list.index(min(list)),'rotations')

def main():
	global L
	print(L)
	rotations(L)
main()
