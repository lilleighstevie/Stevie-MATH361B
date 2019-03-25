# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:40:08 2019

@author: lille_000
"""
import numpy as np
oddComps = []
primes=[]

def prime_check(y):
    isprime = 0
    sqrt = int(np.sqrt(y))+1
    for div in range(2,sqrt,1):
        if y%div == 0 and y != div:
            isprime += 1
            break
        else:
            isprime = isprime
    if isprime == 0:
        return True
    else:
        return False
for num in range(2,6000):
    if prime_check(num) == True:
        primes.append(num)

for odd in range(9,5800,2):
    if prime_check(odd) == False:
        oddComps.append(odd)
        break

for odd in oddComps:
    GB = False
    for prime in primes:
        if odd>prime:
            nn=np.sqrt((odd-prime)/2)
        if nn.is_integer()==True:
            GB = True
      
    if GB == False:
        smallest = odd
        break
  
print("The smallest conterexample is the odd composite number", smallest)
                
        