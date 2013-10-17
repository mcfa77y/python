#!/cygdrive/c/Python30/python
# -*- coding: utf-8 -*-
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

import math
from decimal import *
MX = 0
DICT = {}
MX_NUM = 0
def main():
	c=Decimal(str(math.pow(2,1000)))
	print( c)
	cc = str(c)
	for x in range(999,1001):
		print (x,sumDigits(2**x))
		
def sumDigits(d):
	xx=0
	d = str(d)
	for x in d:
		xx += int(x)
	return xx
def remove_exponent(d):
	print( d)
	return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
main()


