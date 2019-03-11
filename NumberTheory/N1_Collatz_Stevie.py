# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:07:37 2019

@author: Lilleigh Stevie
"""

an = 500
N = 100000
terms = [an]


for ii in range(N):
    if an % 2 == 0:
        an = an//2
        terms.append(an)
        
    else:
        an = 3*an+1
        terms.append(an)
     
    if an == 1:
        break
    
print("The sequence of terms to 1 with a0 as", terms[0], "is", terms)
