# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:36:51 2019

@author: Lilleigh Stevie
"""

N=100000
m=2
terms=[0,1]
multi = []

for ii in range(2,N):
    f = terms[ii-1]+terms[ii-2]
    terms.append(f)
    
    if f%m==0:
        multi.append(f)

        
length = len(multi)
percentage = (length/N)

print("Percentage of", m, "muliples:", percentage)