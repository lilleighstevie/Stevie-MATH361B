# -*- coding: utf-8 -*-
"""
@author: Lilleigh Stevie
"""

import numpy as np
import math

#input variables
N=100

#starts and arrays
S,T,M=0,0,0

Snp=np.zeros(N)
Tnp=np.zeros(N)
Mnp=np.zeros(N)

#loop product
for i in range(1,N+1):
    S += (math.log(i**4+i+3))/(math.sqrt(i)+3)
    T += (math.e**(i/100))/i**10
    M += (i**8+i**6+i**4+i**2)/8**i
    
    Snp[i-1] = S
    Tnp[i-1] = T
    Mnp[i-1] = M

#print outs
print("The first 15 terms of the S partial sum are", Snp[:15])
print("The last 15 terms are", Snp[N-15:])
print()
print("The first 15 terms of the T partial sum are", Tnp[:15])
print("The last 15 terms are", Tnp[N-15:])
print()
print("The first 15 terms of the M partial sum are", Mnp[:15])
print("The last 15 terms are", Mnp[N-15:])