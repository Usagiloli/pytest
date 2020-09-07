#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Author:usagiloli



import re

#ipregex
ipstr:str=r'(((25[0-5]\.)|(2[0-4][0-9]\.)|(1[0-9][0-9]\.)|([1-9][0-9]\.)|([0-9]\.)){3}((25[0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|([0-9])))'
ipreg=re.compile(ipstr)

linecount:int=0
ipbancount:int=0
wars:int=0

with open(r'ipinput.txt',encoding="utf-8") as ipinput:
    with open(r'cmdout.txt','w',encoding="utf-8") as cmdout:
        try:
            fl=ipinput.readlines()
        except:
            ipinput.close()
            ipinput=open(r'ipinput.txt',encoding="gbk")
            fl=ipinput.readlines()
        for i in fl:
            linecount+=1
            
            tem:list=ipreg.findall(i)
            if(len(tem)>0):
                if(len(tem)>1):
                    print(r'Waring:Too Many IPs   Line',linecount)
                    wars+=1
                cmdout.write(r'blist add ')
                cmdout.write(tem[0][0])
                cmdout.write(r' age forever')
                cmdout.write('\n')
                ipbancount+=1
            else:
                print(r'Waring:Emptyline   Line',linecount)
                wars+=1
        cmdout.close()
    ipinput.close()
print('\n'r'Read',linecount,'lines\nBan',ipbancount,'IPs\nWaring',wars,'\n',r'ok')
