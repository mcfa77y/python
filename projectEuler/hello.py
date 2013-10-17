#!/cygdrive/c/Python30/python
# -*- coding: utf-8 -*-
import math, string
"""
sum the digits of 100!
"""
FILE_NAME = 'names.txt'
ABC = string.ascii_uppercase
def fileToList(fileName):
        f0 = open(fileName,'r')
        l = []
        for line in f0:
              l=line.split(",")
        f0.close()
        return l
def scoreName(name):
        som = 0
        name = name.strip()
        #print(name)
        for x in name:
                #print(x, ABC.find(x)+1)
                i = ABC.find(x)
                som+=i+1
        return som
def main():
        l = fileToList(FILE_NAME)
        l.sort()
        som = 0
        for i,v in enumerate(l):
               #print(i,v,scoreName(v))
               som+=(i+1)*scoreName(v)
        print(som)

main() 
