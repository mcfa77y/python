from itertools import permutations
def main():
	wires = ['O','Y','G','R']
	for a in permutations(wires, 4):
		print(a)
		
main()