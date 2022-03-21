# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 22:47:33 2022

@author: David
"""

import math

x2=203;
y2=185;
cx=200;
cy=150;
def newcoordx(x2,y2,cx,cy,i):
    return (  (x2 - cx) * math.cos(math.radians(i)) + (y2 - cy) * math.sin(math.radians(i)) ) + cx;
def newcoordy(x2,y2,cx,cy,i):
    return (  -(x2 - cx) * math.sin(math.radians(i)) + (y2 - cy) * math.cos(math.radians(i)) ) + cy;

for i in range(0,12):
    print("let arrayx","[",i,"]=",round(newcoordx(x2,y2,cx,cy,-1*i*30),1),";");