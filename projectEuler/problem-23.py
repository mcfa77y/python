#!/cygdrive/c/Python30/python
# -*- coding: utf-8 -*-
import math
ActionResources_en_US.properties
"""
sum the digits of 100!
"""
MAP = {}
LIST = set()
SET = set()
def genFactors(x):
	factors =[]
	iSqrt = int(math.ceil(math.sqrt(x)))
	for i in range(2,iSqrt):
	#	print(i)
		if x%i==0:
			factors.append(i)
			factors.append(int(x/i))
	if x%iSqrt==0:
		factors.append(iSqrt)
	factors.append(1)
	#print(factors)
	
	return set(factors)
def add(v):
	global LIST, SET
	LIST.add(v)
	l = len(LIST)
	if(l%100==0):
		print(l,v)
	for x in LIST:
		y = x+v
		SET.add(y)
		if y>28123:
			return True
	return False
def main():
	global SET
	done = False
	#print(sum(genFactors(220)))
	face=[]
	mmap = {}
	#28123
	for i in range(12,50):
		k =sum(genFactors(i))
		if (i<k):
		    face.append(i)
		    done = add(i)
		if done:
			break
	print (SET)
	notSpecial=set(range(24,28123))-SET

	#print(notSpecial, sum(notSpecial))
main() 

"""	for i in range(24,28123):
		l=len(notSepcial)
		if l%100==0:
			print(i,notSpecial[l-1])
		if i not in SET:
			notSpecial.append(i)
"""
