#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import math
MX = 0
DICT = {}
MX_NUM = 0
def doSeq(x):
	global DICT
	if x==1:
		
		return 1
	if x in DICT:
		return DICT[x]
	if x%2==0:
		DICT[x]=1+doSeq(x/2)
	else:
		DICT[x]=1+doSeq(3*x+1)
		
	return DICT[x]
def main():
	global MX,COUNT
	c=0
	for x in range(830000,1000000):
		c = doSeq(x)
                DICT[x]=c
		COUNT=0
		if c>MX:
			MX=c
			MX_NUM=x

		if x%10000==0:
			print x,MX,MX_NUM

main()


