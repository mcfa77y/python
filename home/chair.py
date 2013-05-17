#!/usr/bin/python
'''
You are in a room with a circle of 100 chairs. The chairs are 
numbered sequentially from 1 to 100.
At some point in time, the person in chair #1 will be asked to 
leave. The person in chair #2 will be skipped, and the person in 
chair #3 will be asked to leave. This pattern of skipping one 
person and asking the next to leave will keep going around the 
circle until there is one person left. the survivor.
Write a program to determine which chair the survivor is sitting 
in. Please send us the answer and your working code.

AUTHOR: Joe Lau - lau.joe.a@gmail.com
'''
MAX = 100

ERROR_INDEX = -1
REMOVE = 1
KEEP = 0
	
def main():
	global MAX
	#Solution for a general input
	#MAX=input()
	survivor = findSurvivor(MAX)
	print("survivor: "+str(survivor))

def findSurvivor(max):
	global REMOVE,KEEP, ERROR_INDEX
	
	#initialize list [1..max]
	seatNumber = [x for x in range(1,max+1)]
	# Bits for either KEEP or REMOVE
	bit = [KEEP for x in range(1,max+1)]
	# create a map of seatNumber to bit
	d=dict(zip(seatNumber,bit))
	
	seatNumber=0
	counter=0
	result=seatNumber
	# loop through seats until there are no more
	# available seats
	while seatNumber!=ERROR_INDEX:
		#print ("counter:"+str(counter))
		#print ("seatNumber:"+str(seatNumber))
		result=seatNumber
		seatNumber=findNextAvailableSeat(d,seatNumber)
		if seatNumber==ERROR_INDEX:
			#print("\tresetting seatNumber")
			seatNumber=findNextAvailableSeat(d,0)
		# skip every other seat	
		if counter%2==0:
			#print("mark for removal: "+str(seatNumber))
			d[seatNumber]=REMOVE
		#else:
			#print("skip key:"+str(seatNumber))
		counter+=1
	return result

# finds next available seat starting from an offset: startIndex	
def findNextAvailableSeat(d,startIndex):
	global KEEP, ERROR_INDEX
	#get a subset of the keys
	keys=d.keys()[startIndex:]
	# search keys for the keeper
	for key in keys:
		if d[key]==KEEP:
			#print("next available key:"+str(key))
			#print(str(d.keys()))
			#print(str(d.values()))
			return key
	return ERROR_INDEX
	
main()