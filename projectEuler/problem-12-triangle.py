#!/usr/bin/python
import math
"""The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
     10: 1,2,5,10
     15: 1,3,5,15
     21: 1,3,7,21
     28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""
def factors(x):
	factors =[]
	rootX = int(math.sqrt(x))
	if x%2==0:
		for i in range(2,rootX):
			if x%i==0:
				factors.append(i)
				factors.append(x/i)
	else:
		# if the number is odd then no even number will be a modulo
		for i in range(3,rootX,2):
			if x%i==0:
				factors.append(i)
				factors.append(x/i)
	if x%rootX==0:
				factors.append(rootX)

	#print factors
	return factors
def main():
        i=300
	while True:
        	x = (i*(i+1))/2
        	factorLength = len(factors(x))
		if factorLength%20==0:
			print x,factorLength
        	if factorLength >= 499:
        		print x,factorLength
			break
		else:
			i+=1
main()
