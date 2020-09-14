#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:usagiloli


import sys

inpl=[]
uchrl=[]
fl=16
for ar in sys.argv[1:len(sys.argv)]:
    if(ar[0]=='-'or ar[0]=='/'):
    	if(ar[1]=='b'):
    	    fl=2
    	elif(ar[1]=='d'):
    	    fl=10
    	elif(ar[1]=='h'):
    	    fl=16
    	elif(ar[1]=='o'):
    	    fl=8
    	else:
    	    pass
    else:
    	inpl.append(ar)
for ar in inpl:
    uchrl.append(chr(int(ar,fl)))
for u in uchrl:
    print(u,end=r" ")
print ("\n",end="")
