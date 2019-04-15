# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:29:15 2019

@author: lille_000
"""
#polynomial written by coeffiencts in reversed order
P = [7,-4,1]
c = 4
x,y = 1,10


def evaluate(P,m):
    ans = 0
    for ii in range(0,len(P)):
        ans += P[ii]*m**ii
    return ans
    
def derivative(P):
    dP = []    
    for ii in range(1,len(P)):
        dP.append(P[ii]*ii)
    return dP
    
def defIntegral(P,a,b):
    integral = [0]
    for ii in range(0,len(P)):
        integral.append(P[ii]/(ii+1))
    ans = evaluate(integral,b)-evaluate(integral,a)
    return ans

print("The polynomial evalutated at", c ,"is", evaluate(P,c))
print("The coefficients of the derivative in reversed order are:", derivative(P))
print("The definite integral from", x,"to", y, "is", defIntegral(P,x,y))