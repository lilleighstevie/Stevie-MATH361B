# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:01:43 2019

@author: lille_000
"""
import numpy as np 

#polynomials coeffients written reversed 
f = [-1,0,0,1,0,1]
g = [2,0,0,0,1]

q=[0]
r=list(f)

def LTs(r,g):
    lt = np.zeros((len(r))-(len(g))+1)
    a = (r[len(r)-1]/g[len(g)-1])
    lt[len(lt)-1] = a
    return lt
def degree(poly):
    return len(poly)-1
def addition(f,g):
    if len(f)>len(g):
        a=list(f)
        for ii in range(0,len(g)-1):
            a[ii]=f[ii]+g[ii]
    elif len(g)>len(f):
        a=list(g)
        for ii in range(0,len(f)-1):
            a[ii]=f[ii]+g[ii]
    else:
        a=[]
        for ii in range(0,len(f)-1):
            a.append(f[ii]+g[ii])
    return a
def subtraction(f,g):
    if len(f)>len(g):
        a=list(f)
        for ii in range(0,len(g)-1):
            a[ii]=f[ii]-g[ii]
    elif len(g)>len(f):
        a=list(g)
        for ii in range(0,len(f)-1):
            a[ii]=f[ii]-g[ii]
    else:
        a=[]
        for ii in range(0,len(f)-1):
            b=f[ii]-g[ii]
            a.append(b)
    return a
def LTs_g(r,g):
    b = LTs(r,g)
    prod = []
    for zz in range(0,len(b)-1):
        prod.append(0)
    for ii in range(0,len(g)):
        a = b[len(b)-1]*g[ii]
        prod.append(a)
    return prod
#Erase high degree terms that are now zero
#Assumed that highest degree of p is last element of list
def clean_poly(p):
    highest_deg = len(p) - 1   
    for ii in range(len(p)-1,-1,-1):
        #print('highest', highest_deg)
        #print('pii', p[ii])
        if np.abs(p[ii]) > 1e-15:
            break
        else:
            highest_deg -= 1        
    del p[highest_deg+1:]
    return p

    
while r!=[0] and degree(g)<=degree(r):
    L_one=LTs(r,g)
    q = clean_poly(addition(q,L_one))
    L_two=LTs_g(r,g)
    r = clean_poly(subtraction(r,L_two))

print("Final Polynomials")    
print("f=",f)
print("g=",g)
print("q=",q)
print("r=",r)
    
    
    
    