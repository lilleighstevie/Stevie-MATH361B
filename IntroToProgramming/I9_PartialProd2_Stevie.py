# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:08:23 2019

@author: lille_000
"""
import numpy as np

a_n = lambda n: (1+(1)**n)

N = 100
p_n = np.zeros(N)
term = 1

for ii in range(1,N+1):
    term = term * a_n(ii)
    p_n[ii-1] = term
    
#print("The first 15 terms are:", terms[:15])
print("The last 15 terms are:", p_n[-15:])