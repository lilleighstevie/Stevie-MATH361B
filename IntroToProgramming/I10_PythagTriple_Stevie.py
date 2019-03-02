# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:13:29 2019

@author: Lilleigh Stevie

"""
import numpy as np

N = 1000
pytrips = np.zeros( [0,4] )
flag = ""

for c in range(1,N):
    for b in range(1,c+1):
        for a in range(1,b+1):
            L = a**2 + b**2
            R = c**2
            abc = a+b+c
            if L == R:
                pytrips = np.vstack( [pytrips, np.array( [a,b,c,abc] )] )
            if L== R and abc == 1026:
                flag = "break"
                break
        if flag == "break":
            break
    if flag == "break":
        break

print("The Pythagorean Triple where a+b+c=1026 is when a is", pytrips[-1,0:1], "b is", pytrips[-1,1:2], ",and c is", pytrips[-1,2:3])
