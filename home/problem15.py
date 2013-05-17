#!/Library/Frameworks/Python.framework/Versions/3.2/bin/python3
DICT = {}
def main():
	for x in range(1,21):
		print(x,getCorner(x,x))

def getCorner(i,j):
	global DICT
	if i==0 and j==0:
		return 1
	if (i,j) in DICT:
		return DICT[(i,j)]
	if i==0:
		DICT[(i,j)]= getCorner(i,j-1)
		return DICT[(i,j)]
	if j==0:
		DICT[(i,j)]= getCorner(i-1,j)
		return DICT[(i,j)]
	DICT[(i,j)]= getCorner(i-1,j)+getCorner(i,j-1)
	return DICT[(i,j)]
main()