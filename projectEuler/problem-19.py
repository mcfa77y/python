#!/cygdrive/c/Python30/python
# -*- coding: utf-8 -*-
import datetime
"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""


def main():
	sum=0
	for year in range(1901,2001):
		print('year',year)
		for month in range(1,13):
			print('\tmonth',month)
			if datetime.date(year,month,1).weekday()==6:
				sum+=1
	print(sum)	
	print(datetime.date(1900,1,1).weekday()==0)
main() 
