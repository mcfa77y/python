#!/usr/bin/python

def swap(x,y):
	temp = x
	x=y
	y=temp
	
def permute(array, i, n):
	if(i==n):
		print("a")
	else:
		for j in range(i,n):
			swap()