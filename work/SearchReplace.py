import re, Util
U = Util.Util()
class SearchReplace():
	def __init__(self, fileName):
		self.listFile = fileToList(fileName, False)
		self.fileName=fileName
		
	
	# delete lines from a given search term
	# offset is where to start the delete from
	#  1 would mean delete 1 line after search term 
	#  0 would mean delete at search term 
	#  -1 would mean start delete from one line before searchTerm
	# numOfDelete is how many lines to delete
	def deleteLines(self,searchTerm, offset,numOfDelete):
		for i,line in enumerate(self.listFile):
				s = re.search(searchTerm,line)
				if s:
					print("S: ")
					print(s.group()+"\tline:"+line)
					
					for j in range(numOfDelete):
						print(self.listFile[i+offset])
						del self.listFile[i+offset]
					print(searchTerm+" REMOVED")
					return True
		print(searchTerm+" NOT REMOVED")
		return False
	
		
	# adds importString in File		
	def doImport(self,importString):
		for i,line in enumerate(self.listFile):
			s = re.search("package",line)
			if s:
				self.listFile.insert(i+1, importString+"\r\n")
				break
	
	# deprecated use replace
	def regExReplace(self,searchTerm, replaceTerm, isMulti):
		return replace(self,searchTerm, replaceTerm, isMulti)
		
	# Replaces search term in a File with replace term. and if
	# the isMulti = True then search is done through entire File
	#  otherwise only the first instance is replaced
	def replace(self,searchTerm, replaceTerm, isMulti):
		found = False	
		print("\nreR: \n\tfind: ",searchTerm+"\n\treplace: "+ replaceTerm)
		p = re.compile(searchTerm)
		for i,line in enumerate(self.listFile):
			result = p.subn(replaceTerm, line)
			#print("result: "+str(result))
			if(result[len(result)-1]>0):
				self.listFile[i] = result[0]
				print(result)
				found = True
				if(not isMulti):
					print("done:"+str(found))
					return found
		print("done:"+str(found))
		return found
	# Finds search term in a File and inserts a term. 
	# offset
	#  1 would mean insert 1 line after search term 
	#  0 would mean insert at search term 
	#  -1 would mean start insertfrom one line before searchTerm
	# and if the isMulti = True then search is done through entire
	# File otherwise only the first instance is replaced
	def findInsert (self,searchTerm, insertTerm, offset, isMulti):
		# get the search term and the index
		foundObj = self.findGet(searchTerm, isMulti)
		if foundObj:
			print("Found Object now Inserting:")
			U.printList(foundObj)
			self.listFile.insert(foundObj[0][1]+offset,insertTerm)
			return True
		else:
			self.printStep(insertTerm+" NOT INSERTED")
			return False
	
	# finds a search term and returns the match object and the 
	# index that it was found at
	# is a list of tuples 
	# [(found string, index)+]
	def findGet(self, searchTerm, isMulti):
		p = re.compile(searchTerm)
		getList = []
		for i,line in enumerate(self.listFile):
			pResult = p.search(line)
			if pResult:
				getList.append((pResult.group(0),i))
				if not isMulti:
					return getList
				print(getList)
		return getList
	
	def findBackwards(self,searchTerm, index,isMulti):
		p = re.compile(searchTerm)
		getList = []
		for i in range(index,0,-1):
			line = self.listFile[i]
			#print(line)
			pResult = p.search(line)
			if pResult:
				if not isMulti:
					return (pResult.group(0),i)
				else:
					getList.append((pResult.group(0),i))
		return getList
		
	# gets lines between two terms
	def getBetween(self, index, startTerm, endTerm):
		#print(startTerm,endTerm)
		start = re.compile(startTerm)
		end = re.compile(endTerm)
		getList = []
		startIndex = 0;
		endIndex = 0;
		#print('index: ', index)
		for i,line in enumerate(self.listFile[index:]):
			sResult = start.search(line)
			eResult = end.search(line)
			#print(str(index+i),line)
			if sResult:
				startIndex = i+index
			if eResult:
				endIndex = i+index
				break
		#print(startIndex, endIndex, endIndex-startIndex)
		if startIndex<endIndex and (endIndex-startIndex)<10:
			for i,line in enumerate(self.listFile[startIndex:endIndex+1]):
				getList.append(line)
		return getList
	# DEPRICATED
	def regExFindGet(self,searchTerm, getTerm, offset):
		return findFindGet(searchTerm, getTerm, offset)
	# finds search term in a File and searches offset for a getTerm
	#  returns a list of found lines
	# offset is a window of search so if offset is -5 it will get
	# items 5 lines backwards
	# if offset is 5 then it will get itmes five lines forward
	def findFindGet(self,searchTerm, getTerm, offset):
		found = []
		print("\nreR: \n\tfind: ",searchTerm+"\n\tget: "+ getTerm)
		p = re.compile(searchTerm)
		q = re.compile(getTerm)
		r = re.compile('\" >')
		for i,line in enumerate(self.listFile):
			pResult = p.search(line)
			
			if pResult:
				# direction determis wheter we search forward or
				# backwards
				if (offset>0):
					direction = 1
				else:
					direction = -1
				for j in range(offset):
					lina = 	self.listFile[i+j*direction]
					qResult = q.search(lina)
					if qResult:
						rResult = r.subn('\">', lina)
						if rResult[len(rResult)-1]>0:
							found.append(rResult[0].strip())
						else:
							found.append(qResult.group(0))
						break
		return found	
		
	# finds search term in a File and searches offset for a getTerm
	#  deletes the getTerm and returns successful(True) or not(false)
	def findFindDelete(self,searchTerm, getTerm, offset, isMulti):
		found = False
		print("\nfindFindDelete")
		print("\n\tfind: ",searchTerm+"\n\tfind: "+ getTerm)
		p = re.compile(searchTerm)
		q = re.compile(getTerm)
		r = re.compile('\" >')
		for i,line in enumerate(self.listFile):
			pResult = p.search(line)
			if pResult:
				print("found: "+pResult.group(0))
				for j in range(offset):
					lina = 	self.listFile[i-j]
					print("lina: ",lina)
					print("offset: ", j)
					qResult = q.search(lina)
					if qResult:
						print("\tfound2: "+qResult.group(0))
						print("findFindDelete: " +searchTerm,getTerm+"\n"+lina)
						del self.listFile[i-j]
						if(not isMulti):
							return True
						else:
							found = True
		return found
	# starts looking for a search term from a given index
	# returns the foundItem and teh index it was found at
	def findFrom(self,searchTerm,fromIndex, isMulti):
		p = re.compile(searchTerm)
		getList = []
		listFileSubset = self.listFile[fromIndex:]
		for i,line in enumerate(listFileSubset):
			pResult = p.search(line)
			if pResult:
				if not isMulti:
					return (pResult.group(0),i+fromIndex)
				else:
					getList.append((pResult.group(0),i+fromIndex))
		return getList
				
	
	# depricated use findFindExist
	def regExFindGetExist(self,searchTerm, getTerm, offset):
		return findFindExist(searchTerm, getTerm, offset)
	
	# finds search term in a File and searches offset for a getTerm
	#  returns True if get term exists	
	def findFindExist(self,searchTerm, getTerm, offset):
		found = []
		print("\findFindExist: \n\tfind: ",searchTerm+"\n\tget: "+ getTerm)
		p = re.compile(searchTerm)
		q = re.compile(getTerm)
		
		for i,line in enumerate(self.listFile):
			pResult = p.search(line)
			if pResult:
				
				# direction determis wheter we search forward or
				# backwards
				if (offset>0):
					#forward
					direction = 1
				else:
					#backward
					direction = -1
				# search toward offset
				if(offset>0):
					for j in range(offset):
						print("j: ",j)
						try:
							lina = 	self.listFile[i+j*direction]
							qResult = q.search(lina)
							print("no place like home")
							#print(qResult,lina)
							if qResult:
								return True
						except IndexError:
							break
		return False
	# finds a term and returns of its existence
	def findExist(self,searchTerm):
		found = []
		print("\nreR: \n\tfind: ",searchTerm)
		p = re.compile(searchTerm)
		for i,line in enumerate(self.listFile):
			pResult = p.search(line)
			if pResult:
				print("\tTrue")
				return True
		print("\tFalse")
		return False
	# returns true if class is implemented
	# false if class is not implement
	def checkImplements(self,implementation):
		found = False	
		print("\nChecking for implementation: " + implementation)
		return self.regExFindGetExist('implements',implementation, 10)
	
	# removes transient from File using a list as a filter
	def removeTransient(self,filterFileName):
		print("Remove Transient: ")
		filterList = fileToList(filterFileName,True)
		for line in filterList:
			print(line)
		print(len(filterList))
		first = True
		i=1
		for i,line in enumerate(self.listFile):
			
			# skip the first line so we can have a previous
			# entry
			if first:
				first = False
				continue
			
			# check to see if line matches one of the filtes
			# if it does then remove that filter 
			#  and delete the @Transient line before if it exists
			for philter in filterList:
				# match get[Column Name]
				
				m=re.search(r"public .+ get"+philter,line, re.I)
				if m:
					
					# replace @Transient from previous line to ""
					#n = re.search("@Transient",self.listFile[i])
					n = re.subn(r"@Transient(\s+.*{)",r"\1",self.listFile[i])
					if n:
						self.listFile[i]=n[0]
					#print("m:"+m.group(0)+"\n\t"+line)
					filterList.remove(philter)
		print(len(filterList))
		if(len(filterList)>0):
			print("remaining filters: "+str(filterList))
			
	# DEPRICATED USE WRITE
	def listToFile(self,fileName):
		self.writeTo(fileName)
		
	#writes a list to file given the file name
	def writeTo(self,fileName):
		output = open(fileName,'w')			
		for line in self.listFile:
			output.write(line)
		output.close()
		
	#writes a list to file given the file name
	def write(self):
		output = open(self.fileName,'w')			
		for line in self.listFile:
			output.write(line)
		output.close()	
	# prints step line break
	def printStep(self,step):
		s = ""
		for i in range(20):
			s+="#"
		print(s+" "+str(step)+" "+s)
		
		
		
		
		
# convert from File turn the contents
# into a list given a list
# capitalizeFirstCharitalizeFirstChar is a boolean value 
def fileToList(fileName, capitalizeFirstChar):
	l=[]
	f = open(fileName,'r')
	for line in f:
		if capitalizeFirstChar:
			if len(line.split())>0:
				line=line.split()[0]
			line = line[0].capitalize()+line[1:]
		l.append(line)
	f.close()
	return l
