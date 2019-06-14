#import yyy
#yyy.yyy("harry-potter-1-7.txt","gb18030","h4","utf-8")
#import sys
#print("arv[0]=%s" %sys.argv[0])
#print("arv[1]=%s" %sys.argv[1])
#print("arv[2]=%s" %sys.argv[2])


#/usr/local/bin/python3

import sys
import os

root=sys.argv[1]



for d,s,f in os.walk(root):
    print("directory:%s" %d)
    for fa in f:
        print(fa)