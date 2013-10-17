#!/usr/bin/python
# this script reads two directories and diffs the files and writes that output to a file

import Util


# result file for diffs results of the two directories
OUTPUT = "diff_results.txt"
FN_X = "input/core-util.txt"
FN_Y = "input/core-ejb.txt"
capitalizeFirstCharitalizeFirstChar = False
# trims off white space at the end of lines
DO_TRIM = True
def main():
	U = Util.Util()
	x = set(U.fileToList(FN_X,capitalizeFirstCharitalizeFirstChar))
	y = set(U.fileToList(FN_Y,capitalizeFirstCharitalizeFirstChar))
	if DO_TRIM:
		x=set([item.strip() for item in x])
		y=set([item.strip() for item in y])
	xy = x & y
	#print(str(xy),str(len(xy)))
	U.printList(xy)

main()