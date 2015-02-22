#!/usr/bin/python
import sys, re, os, SearchReplace, string,Util
from Tkinter import Tk
#change per use
I18N_FN = "/Users/jlau/projects/gliffy-i18n/src/main/i18n/gliffy-online-message.properties"
TOPIC = "libraries"
PATH = "online.premium."
I18N_PREFIX = PATH+TOPIC

IS_MULTI=False

STOP_WORDS = set(["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours ","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves",])

U = Util.Util()


def main():
	# create a searchReplace instance from filename
	i18nSR = SearchReplace.SearchReplace(I18N_FN)
	# clipboard object
	r = Tk()
	print("TOPIC: "+TOPIC)
	while(True):
		s = str(raw_input('String to i18n >> '))
		
		
		#end prog
		if len(s)==0:
			r.destroy()
			sys.exit()

		# change topic
		if("chTopic" in s):
			global I18N_PREFIX,PATH,IS_MULTI
			topic = s.split()[1]
			print("new Topic: ",topic)
			nuPrefix = PATH+topic+"."
			#replace online.google.apps.welcome with online.google.apps.NEWTOPIC
			i18nSR.replace(I18N_PREFIX,nuPrefix+"\n\n",IS_MULTI)
			#write changes to file
			i18nSR.write()
			I18N_PREFIX = nuPrefix
			continue
		# update file
		if("upFile" in s):
			print("updated file")
			i18nSR.write()
			#update instance of i18nSR
			i18nSR = SearchReplace.SearchReplace(I18N_FN)
			continue

		key = keyString(s)
		custom = str(raw_input('Use suggested key - [ENTER]  enter your own key:\n'))
		
		if len(custom)>0:
			# use custom
			key = I18N_PREFIX+'.'+custom
		elif custom=='\'':
			key = I18N_PREFIX

		#find online.google.apps.welcome and insert 1 line afterwards with key=s
		i18nSR.findInsert(I18N_PREFIX, key+"="+s+"\n", 1, IS_MULTI)
		i18nSR.write()

		scalaMessage = '@Messages("'+key+'")'
		print(scalaMessage)		
		
		#push scala message to clipboard
		r.withdraw()
		r.clipboard_clear()
		r.clipboard_append(scalaMessage)
		
		


def keyString(s):
	ss =s.lower();
	print(ss)
	#remove ,.?!'"\@ <html tag> (tag)
	p = re.compile(r',|\.|\?|\'|\"|!|@|-|\<.*?\>|\(.*?\)')
	y = p.sub('',ss)
	print('remove punc and tags: ',y)
	
	for w in STOP_WORDS:
		y=y.replace(" "+w+" "," ")
	#replace spaces with .
	y = y.replace(' ','.')
	ss = I18N_PREFIX+'.'+y
	print(ss)
	return ss
main()


