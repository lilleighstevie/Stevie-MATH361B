# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:03:31 2019

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

N=1000

print(divisors(N))
    