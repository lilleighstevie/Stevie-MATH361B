# -*- coding: utf-8 -*-
"""
@author: Lilleigh Stevie
"""

#imports
import numpy as np
import math

#input variable
N=180

#starts and arrays
P,Q,R = 1,1,1

Pnp = np.zeros(N+1)
Qnp = np.zeros(N+1)
Rnp = np.zeros(N+1)

#loops
for i in range(2,N+3):
    P = P*(i**3-1)/(i**3+1)
    
    Pnp[i-2] = P
    
for j in range(1,N+2):
    Q = Q*(math.e**(j/100))/j**10
    R = R*math.e*j**2/(math.pi*j)
    
    Qnp[j-1] = Q
    Rnp[j-1] = R
    
#print outs
print("The first 15 terms of the P partial sum are", Pnp[:15])
print("The last 15 are", Pnp[N-15:])
print()
print("The first 15 terms of the Q partial sum are", Qnp[:15])
print("The last 15 are", Qnp[N-15:])
print()
print("The first 15 terms of the R partial sum are", Rnp[:15])
print("The last 15 are", Rnp[N-15:])
print()