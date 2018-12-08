#!/usr/bin/python
#coding=utf-8

import re

str = '025-985757728'
pattern = r'\d{3}-\d{5}'
print (re.findall(pattern,str))

re_p = re.compile(pattern)
print( re_p.findall(str))

