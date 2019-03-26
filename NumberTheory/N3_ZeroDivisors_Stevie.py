# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:14:06 2019

@author: lille_000
"""

m = 21
divList = []

for yy in range(1,m-1):
    for xx in range(1,m-1):
        if (xx*yy)%m == 0:
            xVal = xx in divList
            if xVal == False:
                divList.append(xx)
            yVal = yy in divList
            if yVal == False:
                divList.append(yy)
            
print("Zero divisors are:", divList)            
print("The number of zero divisor is:", len(divList))