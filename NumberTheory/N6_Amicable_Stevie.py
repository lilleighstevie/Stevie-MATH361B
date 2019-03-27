# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:13:23 2019

@author: lille_000
"""

def divisors(n):
    divList = []
    div = 1
    while div < n:
        if n % div == 0:
            divList.append(div)
        div += 1
    return divList

N=100000
amicable=[]
for a in range(1,N):
    b = sum(divisors(a))
    if sum(divisors(b)) == a:
        aVal = a in amicable
        if aVal == False:
            amicable.append(a)
        bVal = b in amicable
        if bVal == False:
            amicable.append(b)
            
print("The amicable numbers are:", amicable)