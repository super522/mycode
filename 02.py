#!/usr/bin/python3
# -*- coding:utf-8 -*-

import codecs
import sys

if len(sys.argv) > 1:
    FILE=sys.argv[1]
else:
    FILE="qing-tong-kui-hua-gbk.txt"

 #gb18303, gbk, gb2312, 
fp = codecs.open(FILE, 'r', 'gb18030')
texts = fp.read()
fp.close()
print(texts)
ing = open("a","w")
ing.write(texts)



list1=[]
for ch in texts:
    list1.append(ch)
#print(list1)
d1={}
d2={}
for ch in list1:
    m=ord(ch)
    if m>40869 and m<19968:
        if ch in d1:
            d1[ch]+=1
        else:
            d1[ch]=1
    else :
        if ch in d2:
            d2[ch]+=1
        else:
            d2[ch]=1:
print(d2) 
print(len(d2))  