# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:05:28 2019

@author: lille_000
"""
import numpy as np

count = np.zeros([0,2])
neg_one = np.zeros([0,2])

P = 100

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
primeList = []
for pp in range(2,P+1):
    if prime_check(pp)==True:
        primeList.append(pp)

for p in primeList:
    num=[]
    for n in range(0,p):
        for k in range(0,n+1):
            if n==(k**2)%p:
                nn = n in num
                if nn == False:
                    num.append(n)
                kk = k in num
                if kk == False:
                    num.append(k)
    count = np.vstack( [count, np.array( [p,len(num)] )] )
print("The quadratic residues are:")
print(count)


for p in primeList:
    QR="False"
    for n in range(0,p):
        if (p-1)==(n**2)%p:
            QR="True"
        
    neg_one = np.vstack( [neg_one, np.array([p, QR])])

print("When -1 is a quadratic residue:")
print(neg_one)        
