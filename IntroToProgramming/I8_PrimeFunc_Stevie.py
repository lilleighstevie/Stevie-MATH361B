# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:52:47 2019

@author: lille_000
"""
import numpy as np

n=10
primes=[2,3]
length=len(primes)

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


num = 4 
while n >= length:
    if prime_check(num) == True:
        primes.append(num)

    length = len(primes)
    num += 1
       
print("The", n, "prime is", primes[n-1])