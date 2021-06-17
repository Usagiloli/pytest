#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from txtmt import txfanyi
import cv2
import numpy as np
import pyautogui as pag
from time import sleep
import pynput
import pytesseract
import re
import configparser

def press(x,y,but,p):
    if(p):
        return False
def unpress(x,y,but,p):
    if(not p):
        return False

def waitclick(fx=press):
    with pynput.mouse.Listener(on_click=fx) as linster:
        linster.join()

def getpos3(sample=1):
    while (1):
        pos1 = pag.position()
        sleep(sample/2)
        pos2 = pag.position()
        if (pos1 != pos2):
            continue
        sleep(sample/2)
        pos1 = pag.position()
        if (pos1 == pos2):
            return(pos1)

def getrgn(sample=1,mode='pos3'):
    while(1):
        if mode=='pos3':
            pag.alert(text='getrgn,pos3')
            pos1=getpos3(sample)
            print(pos1)
            pos2=getpos3(sample)
            print(pos2)
        elif mode=='clk':
            pag.alert(text='getrgn,clk')
            waitclick(press)
            pos1=pag.position()
            waitclick(unpress)
            pos2=pag.position()

        if (pos2[0] - pos1[0] > 0 and pos2[1] - pos1[1] > 0):
            break
        else:
            print("Out of range")
    rgn = (pos1[0], pos1[1], pos2[0] - pos1[0], pos2[1] - pos1[1])
    #print(rgn)
    return rgn


def resformat(input):
    input=re.sub('\\s+',' ',input)
    return input

#res=pag.size()
#print(res)

def shotrgn(rgn):
    fr = pag.screenshot(region=rgn)
    img = np.asarray(fr)
    imgcv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgcv=cv2.bilateralFilter(imgcv,5,21,21)
    imgcv = cv2.threshold(imgcv, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # imgcv=cv2.medianBlur(imgcv,1)
    sleep(0.1)
    return imgcv


def sltrgn(mode='pos3'):
    while(1):
        rgn=getrgn(mode=mode)
        sleep(0.1)
        imgcv=shotrgn(rgn)
        cv2.imshow("opencv", imgcv)
        cv2.waitKey()
        cv2.destroyAllWindows()
        if(pag.confirm("OK?") == 'OK'):
            break
    return rgn


cf=configparser.ConfigParser()
cf.read("usarot.cfg")
mode = cf.get("cfg","mode")
st1 = cf.get("cfg","id")
st2 = cf.get("cfg","key")

rgn=sltrgn(mode)

while(1):
    imgcv=shotrgn(rgn)
    code=pytesseract.image_to_string(imgcv,lang='eng')
    resformat(code)
    print(code)
    fanyi=txfanyi(code,st1,st2)
    fanyi=resformat(fanyi)
    print(fanyi)
    waitclick()