# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:15:28 2019

@author: lille_000
"""
import numpy as np
import matplotlib.pyplot as plt

N = 8
print("Iterations: ", N)

    #initial square
    #Uncomment out A4,B4, W4 and Next.append(W4)
#S0 = [np.array([[0],[0]]),np.array([[0],[1]]),np.array([[1],[0]]),np.array([[1],[1]])]#matrices

    #initial triangle
    #Comment out A4,B4, W4 and Next.append(W4)
S0 = [np.array([[8],[6]]),np.array([[2],[-5]]),np.array([[-5],[1]]),np.array([[3],[-3]]),np.array([[-1.5],[-2]]),np.array([[0],[3]])]

    #matrices
a=.5
A1 = np.array([[a,0],[0,a]])
A2 = np.array([[a,0],[0,a]])
A3 = np.array([[a,0],[0,a]])
#A4 = np.array([[a,0],[0,a]])

    #vectors
B1 = np.array([[0],[0]])
B2 = np.array([[2],[0]])
B3 = np.array([[4],[6]])
#B4 = np.array([[0],[8]])


    #the first R is the rotation
    #the second R is the identity matrix
    #one of the Rs must be commented out
p = np.pi
#R = np.array([[np.cos(3*p/4),-np.sin(3*p/4)],[np.sin(3*p/4),np.cos(3*p/4)]])
R = np.array([[1,0],[0,1]])

S = list(S0)
Next = []
n=0
while n<N:
    for jj in range(0,len(S)):
        c=[]
        b=[]
        v=S[jj]
        W1 = (R @ A1 @ v) + B1
        W2 = (R @ A2 @ v) + B2
        W3 = (R @ A3 @ v) + B3
        #W4 = (R @ A4 @ v) + B4
        Next.append(W1)
        Next.append(W2)
        Next.append(W3)
        #Next.append(W4)
    for jj in range(0,len(Next)):
        c.append(Next[jj][0])
        b.append(Next[jj][1])
    S = list(Next)
    n+=1    
    
plt.plot(c,b, '.', ms=1)
plt.show()