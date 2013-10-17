#!/usr/bin/python27
f=open('../input/file.txt','r')
d={}
for l in f:
    
    s = l.split(',')
    #print s
    if s[1]=='F':

        d[int(s[2])]=s[0]
        
#print d
k=sorted(d.keys())
print k
print(d[k[len(k)-2]])