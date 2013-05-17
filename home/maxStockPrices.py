#!/usr/bin/python
# this script finds the best buy/sell stock prices
# using an array, stockPrices, that has prices in 
# accending chornological order index 0 is the past
# index N would be the present price
#
# The running time for this is O(n) since we only 
# iterate through the array once.
import random

# prints the best buy/sell and profit from stock prices	
# given a list of stock prices
def maxStockPrices(stockPrices):
	# initialize variables
	infinity = float('inf')
	# minimum stock price
	minimum = infinity
	# maximum stock price
	maximum = -infinity
	# maximum profit
	maxProfit=0.0;
	# best buy/sell prices
	buy=0.0
	sell=0.0
	
	# iterate through prices and find best sell/buy prices
	for price in stockPrices:
		if price<minimum:
			minimum=price
			maximum=0;
		if price>maximum:
			maximum=price
			profit = maximum-minimum
			# set maxProfit/sell/buy when
			# a new profit is found and a minimum is set
			if profit > maxProfit and minimum!=infinity:
				maxProfit = profit			
				sell=maximum
				buy=minimum
				
	# print solution		
	print('buy ',buy,'\nsell ',sell,'\nprofit ',maxProfit)
	if buy==0 and sell==0 and profit==0:
		print("there was no way to make a profit unless you short")

def main():
	# initialize variables
	stockPrices = []
	# test values
	# answer is buy:4 sell:20 profit: 16
	stockPrices=[50, 4,20,1,2,3,16,1,2,3]
	
	# this chunk of code generates random stock prices
	#numberOfPrices=20
	# select numberOfPrices random variables for stockPrices
	#for i in range(numberOfPrices):
	#	stockPrices.append(random.randint(0,100))
	
	print(stockPrices)
	maxStockPrice(stockPrices)	
	
main()
