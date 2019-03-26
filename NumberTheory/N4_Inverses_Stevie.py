# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:25:07 2019

@author: lille_000
"""

m = 21
inverses = []

for yy in range(1,m-1):
    for xx in range(1,m-1):
        if (xx*yy)%m == 1:
            xVal = xx in inverses
            if xVal == False:
                inverses.append(xx)
            yVal = yy in inverses
            if yVal == False:
                inverses.append(yy)
            
print("Inverses are:", inverses)            
print("The number of inverses is:", len(inverses))