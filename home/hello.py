#!/Library/Frameworks/Python.framework/Versions/3.2/bin/python3
import fractions
mx=2000000
def isPrime(n):
		import math
		n = abs(n)
		i = 3
		if n==1:
			return False
		if n==2:
			return True
		if n%2==0:
			return False
		limit = math.sqrt(n)+1
		while i <= limit:
			if n % i == 0:
				return False
			i += 2
		return True
def main():
	global mx
	s=2
	for i in range(1,mx,2):
		if isPrime(i):
			s+=i
			print(i)
	print(s)
		
def other():
	i = 1
	for k in (range(1, 21)):
		if i % k > 0:
			for j in range(1, 21):
				if (i*j) % k == 0:
					i *= j
					break
	print(i)
	
	
maxPrime = 2000000
primeRange = range(3,maxPrime,2)
primes = [2]
stop = 0


#main()