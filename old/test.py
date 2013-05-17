#!/usr/bin/python
import sys, re

l="public Object create(Object dto, ValidationMethod[] list, boolean extended) {"
p = re.compile("(public (.+) create\(.+\))")
r = p.subn('\1 throws ServiceException',l)

print l
print r