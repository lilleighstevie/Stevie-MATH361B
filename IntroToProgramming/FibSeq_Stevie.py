# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:04:31 2019

@author: Lilleigh Stevie
"""

F0 = 0
F1 = 1
N = 20
terms = [F0,F1]
print(terms)

for ii in range(2,N):
    t = terms[ii-1] + terms[ii-2]
    terms.append(t)

#check of cassini's identity
for n in range(1,N-1):
    left = (terms[n])**2-(terms[n-1]*terms[n+1])
    right = (-1**(n-1))
    print("Cassini's identity, term is", terms[n], ":", left == right)

print("The last 10 terms in the sequence are:", terms[-10:])