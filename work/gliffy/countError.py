#!/usr/bin/python
import sys,re
import json

class ErrLog:
	def __init__(self, time, tipo, key, extra):
		self.time = time
		self.tipo = tipo 
		self.key = key
		self.extra = extra
	
	def to_JSON(self):
		s = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
		#print 's',s
		return s
	
	def __str__(self):
		#return self.time+" "+self.tipo+" "+self.key+" "+self.extra[:40]+"..."
		return self.key+" "+self.extra[:40]+"..."


def main():
	filename = sys.argv[1]
	print 'filename',filename
	f = open(filename,'r')
	
	d = dict()
	p= re.compile(r'(?P<time>\d+-\d+-\d+ \d+:\d+:\d+,\d+) (?P<tipo>[A-Z]+) (?P<key>\[.*?\] \[.*?\]) (?P<extra>.*$)')
	prevErrLog = None
	for l in f:
#		print l
		m=p.match(l)

		if m:
#			print "==============================================================================="
			#print 'D',d
			ti = m.group('time')
			ty = m.group('tipo')
			ky = m.group('key')
			ex = m.group('extra')

			errLog = ErrLog(ti,ty,ky,ex)
#			print '\n\nvalue\n\t',errLog
			try:
#				print 'UPDATING'
				errLogList = d[ky]
#				print 'eList',errLogList
#				print 'updating key - before:\n\tkey-',ky,'\n\tvalue-',d[ky],'\n\terrLog-',errLog
				d[ky].append(errLog)
				
#				print 'updating key - after:\n\tkey-',ky,'\n\tvalue-',d[ky]
			except KeyError:
#				print 'adding key\n\t',errLog
				d[ky]=[errLog]	
#				print 'done adding key - after:\n\tkey-',ky,'\n\tvalue-',d[ky]
		else:
			# append non-error headers to the end of the extra of ErrLog
			lastErrLog = d[ky][-1]
			lastErrLog.extra+=l
				
			
	f.close()
	print '\n\nDone'
	jsonObj = {}
	jsonList={}
	jsonList["aaData"]=[]
	finish = 3
	i=0
	for k,v in d.items():
		v2 = []
		i+=1
		for vi in v:
			v2.append(vi.to_JSON())
			#print 'vi',vi.to_JSON()
			jsonList["aaData"].append(vi.to_JSON())
		jsonObj[k]=v2
		
		if i==finish:
			break
	js = json.dumps(jsonList, ensure_ascii=False,sort_keys=True, indent=4, separators=(',', ': '))
	#js = json.loads(json.loads(js))
	#js = json.dumps(jsonList, sort_keys=True, indent=4, separators=(',', ': '))
	# remove new lines chars \n --> ''
	js = re.sub(r"\\+n","",js)
	# keys
	js = re.sub(r"\\(\"\w+)\\(\"\:)",r"\1\2",js)
	# time value
	js = re.sub(r"\\(\"\d+-\d+-\d+ \d+:\d+:\d+,\d+)\\\"",r"\1"+"\"",js)
	# key value
	js = re.sub(r"\\(\"\[.*?\] \[.*?\])\\\"",r"\1"+"\"",js)
	# tipo value
	js = re.sub(r"\\(\"[A-Z]+)\\\"",r"\1"+"\"",js)
	# extra value
	js = re.sub(r"(\"extra\": )\\(\".+?)\\(\",\W+\"key\")",r"\1\2\3",js)
	#js = re.sub(r"",r"",js)
	#js = re.sub(r"",r"",js)
	# \\\ --> \
	js = re.sub(r"(\\)+",r"\\",js)
	# "{ ... }" --> { ... }
	js = re.sub(r"\"(\{.+?\})\"(,?)",r"\1\2",js)
	
	print js
	#print js.replace('\n','').replace(r'\"\{','\{').replace(r'\}\"','\}')
	o = file('output.txt','w')
	o.write(js)
	o.close()
	
def printErrLogDict(d):
	for k,v in d.items():
		print k,len(v)

		for vi in v:
			print '\t',vi	
			#print 'vi.extra',vi.extra
main()

