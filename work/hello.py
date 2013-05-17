#!/cygdrive/c/Python30/python
# -*- coding: utf-8 -*-
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""
WORD_9 = ['','one','two','three','four','five','six','seven','eight','nine']
WORD_10_19 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',\
		'seventeen','eighteen','nineteen']
WORD_20_90=['','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
WORD_1000=['thousand']
t=0
count=0
maap = {}
def add(word):
	global t,count, maap

	if len(word)<3:
		return
	count+=1
	t+=len(word)
	
	maap[word]=len(word)
	print(count,word,t,len(word))
def subtract(word):
	global t,count,maap
	count-=1
	t-=len(word)
	del(maap[word])
	#print(count,word,t,len(word),)

def main():
	global WORD_9, WORD_20_100,WORD_1000
	global t,count
	count = 0
	c=0

	# 0-9,20-99
	for w1 in WORD_20_90:
		for w2 in WORD_9:
			add(w1+w2)
	c+=10+99-20
	print ('# 0-9,20-99',count,c)
	assert count==c
	# 10-19
	for word in WORD_10_19:       
		add(word)
	c+=10
	assert count == c
	# (1-9)00
	for w0 in WORD_9:
		add(w0+'hundred')
	subtract('hundred')
	c+=9
	print ('# 10-19',count,c)
	assert count==c
	
	# (1-9)01 - (1-9)19
	# WORD_1-19
	WORD_9.extend(WORD_10_19)
	for w0 in WORD_9[: 10]:
		if w0=='':
			continue
		for w2 in WORD_9:
			if w2=='':
				continue
			add(w0+'hundredand'+w2)
	c+=19*9
	print ('# (1-9)01 - (1-9)19',count,c)
	assert count==c

	WORD_9=WORD_9[:10]
	# (1-9)20 - (1-9)99
	for w0 in WORD_9:
		if w0=='':continue
		for w1 in WORD_20_90:
			if w1=='':continue
			for w2 in WORD_9:
				add(w0+'hundredand'+w1+w2)
				#print(w0+'hundredand'+w1+w2)

	c+=(99-20+1)*9
	print ('# (1-9)20 - (1-9)99',count,c)
	assert count==c
	add('onethousand')
	print(t,count)
	count2 = 0
	t2=0
	for num,l in maap.items():
	    t2+=l
	    count2+=1
	print(t2,count2)
		
main()
		
