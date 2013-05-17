#!/usr/bin/python
import sys

def main():
	a = sys.argv[1]
	b = sys.argv[2]
	
	print("("+p(b+"|"+a)+" * "+p(a)+") / "+p(b))
	print("or")
	print("n * "+pp(a+"|"+b))
	print("n = "+"1 / [("+p(b+"|"+a)+" * "+p(a)+") + ("+p(b+"|^"+a)+" * "+p("^"+a)+"))")
	aa = float(raw_input(p(a)+"= "))
	ba = float(raw_input(p(b+"|"+a)+"= "))
	nba = float(raw_input(p(b+"|^"+a)+"= "))
	v = (aa*ba)/(aa*ba+(1-aa)*nba)
	print(v)
def pp(a):
		return ("P'("+a+")")

def p(a):
	return ("P("+a+")")
main()
