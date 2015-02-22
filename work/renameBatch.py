#!/usr/bin/python
import sys, re, os, SearchReplace, string,Util
#change per use
SRC = "/Users/jlau/Downloads/iphone_ios7/glyphs"
U = Util.Util()

def main():
	d={}
	exclude=['.DS_Store']
	i=0
	isInitialFolder=True
	# get shapes/package from source folder
	
	for root, dirs, files in os.walk(SRC):
		
		if isInitialFolder:
			isInitialFolder=False
			continue

		#root = /Users/jlau/Downloads/iphone_ios7/glyphs/glyph-wifi
		
		#newDirName = glyph_wifi was glyph-wifi
		newDirName = root.split('/')[-1:][0].replace('-',"_")
		
		#preFn = /Users/jlau/Downloads/iphone_ios7/glyphs/    +  glyph_wifi
		newDir = root[0:root.rfind('/')+1]+newDirName
		print newDirName+"\n"+newDir+"\n"+root
		os.rename(root,newDir)

'''
		for f in files:
			print f
			if f.find('.DS_Store')!=-1:
				continue
			
			blerg = root[root.rfind('/'):]
			blerg = blerg.replace('_','-').replace('/','')+'-'
			newFn = blerg+f.replace('_',"-")
#			newName = root+f.
			#print(root,f)
			print(root+'/'+f+"\n"+root+'/'+newFn)
			#os.rename(root+'/'+f, root+'/'+newFn)
'''
main()


