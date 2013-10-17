#!/usr/bin/python
# This is a utility class for fucntions that i use often
import pickle, os, shutil
from subprocess import Popen, PIPE
class Util(object):
	def __init__(self):
		self.s=1
	# custom pickle?
	def cPickle(self,fn, obj):
		output = open(fn,'wb')
		pickle.dump(obj,output)
		output.close()
	# custom unPickle
	def cUnpickle(self,fn):
		output = open(fn,'rb')
		obj = pickle.load(output)
		output.close()
		return obj
	# runs a command and returns the standard out
	def runCmd(self,cmd):
		p = Popen(cmd, stdout=PIPE, stderr=PIPE)
		stdout = str(p.communicate()[0]).split('\\n')
		return stdout
	# writes to a file
	def write(self,fileName,msg):
		output = open(fileName,'w')			
		output.write(msg)
		output.close()
	# append to a file
	def append(self,fileName,msg):
		output = open(fileName,'a')			
		output.write(msg)
		output.close()

	#makes a directory
	# this fn will take in a path as the argument
	# and if it will create all the missing dir from the path
	# ex c:/quick/brown/fox
	# c:/quick exists but not brown/fox
	# so brown then fox will be created
	def mkDir(self,dirName):
		total = ""
		print("creating dir: " +dirName)

		for i in dirName.split("/"):
			total += i+"/"
			try:
				os.chdir(total)
			except WindowsError:
				os.mkdir(i)
				os.chdir(total)
				print("created dir: "+os.getcwd())
		os.chdir(dirName)
	
	# copies files from one directory to another
	def cpFilesToDir(self, fromDir,toDir, exclude):
		fromDirDict = dict()
		self.mapFilenames(fromDir,fromDirDict, exclude)
		for fn, path in fromDirDict.items():
			print("copying:\n\t"+path+"\n\t"+toDir)
			shutil.copy2(path,toDir)
	
	# from a directory rename files from oldName to 
	# newName
	# ex) batchRenameFiles("c:/quick/", "fox","hound",[])
	# this would yeild all the files under the quick with 
	# the word fox to hound
	def batchRenameFiles(self,dir, oldName, newName, exclude):
		fmap = dict()
		oldName = self.capitalize(oldName)
		newName = self.capitalize(newName)
		print("RENAME from: "+oldName+"\n\tto: "+newName)
		self.mapFilenames(dir,fmap,exclude)
		for fn, path in fmap.items():
			# path did not have oldName
			if path.rfind(oldName)<0:
				print("NO RENAME DONE\n\tfrom: "+fn+"\n\tto: "+newName)
				continue
			# get path name w/o file extention
			path2 = path[:path.rfind(oldName)]
			
			#print(path2+"\n"+path)
			if path2 == path:
				return
			# new file name with path
			newFN = path2+fn.replace(oldName,newName)
			#print("new filename: "+newFN)
			try:
				os.rename(path,newFN)
			except WindowsError:
				print("FILE ALREADY EXISTS")
	
	# batchPrint(links, "insert into Currency (code, currency) values(REPLACE_TERM)","REPLACE_TERM")
	# batch print takes in a list and uses the list elements to replace a term in a string
	def batchPrint(list, string, replacementTerm):
		for key in list:
			s = string.replace(replacementTerm,key.strip('\n'))
			print(s)
		
	# capitalizes the first letter in a word
	def capitalize(self, word):
		word = word[0].capitalize()+word[1:]
		return word
	# lowercases the first letter in a word
	def unCapitalize(self,word):
		word = word[0].lower()+word[1:]
		return word
	# maps file names to path+filename in a given directory
	# fn - directory
	# d - dictionary
	# exclude - is an array of strings to exclude
	# there are filters for .svn and files named SystemDefaults
	# @ line 73
	def mapFilenames(self,fn,dic, exclude):
		print("Mapping files: "+fn)
		for root, dirs, files in os.walk(fn):
			for name in files:
				# skip .svn files and excludes
				exclusionsFound = False
				if exclude and len(exclude)>0:
					for ex in exclude:
						#check name against every exclusion
						if name.find(ex)>-1:
							exclusionsFound=True
							break
				#print("exclustionsFound: "+str(exclusionsFound))
				if name.find('.svn')<1 and not exclusionsFound:
					# change the stroke type from windows to unix
					root = root.replace("\\","/")
					nameModRoot = root.replace(fn,"")+"/"+name
					# checks to make sure the last char of root
					# is a / if not then add a /
					lastCharOfRoot = root[len(root)-1:len(root)]
					if(lastCharOfRoot.find("/")<0):
						dic[name]=root+"/"+name
					else:
						dic[name]=root+name
					'''
					try:
						#print ("name:\n\t"+name+'\n\t'+root)
					except UnicodeEncodeError:
						print("NAME ERROR:")	
					'''
			if '.svn' in dirs:
				dirs.remove('.svn')  # don't visit svn directories
	# prints step line break
	def printStep(self,step):
		s = ""
		ss=""
		sz=25
		for i in range(sz):
			s+="#"
		for i in range(len(str(step))+2+2*sz):
			ss+="-"
		
		print("\n"+ss)
		print(s+" "+str(step)+" "+s)
		print(ss+"\n")
	#prints a dictionary
	def printDict(self,dic):
		for k,v in dic:
			print(k+"\t"+v)
	
	#prints a list 
	def printList(self,l):
		for i in l:
			print(str(i)+"\n")
	# convert from File turn the contents
	# into a list given a list
	# capitalizeFirstCharitalizeFirstChar is a boolean value 
	def fileToList(self,fileName, capitalizeFirstChar):
		l=[]
		f = open(fileName,'r')
		for line in f:
			if capitalizeFirstChar:
				if len(line.split())>0:
					line=line.split()[0]
				line = self.capitalize(line)
			l.append(line)
		f.close()
		return l
	
	
