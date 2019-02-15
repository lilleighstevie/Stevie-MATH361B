# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:42:02 2019

@author: Lilleigh Stevie
"""
import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.linspace(-3,3, num=N)
y = np.zeros(N)


def function(x):
    if (x)<-2:
        f = -3*(x+2)**2+1
    elif (x)>=-2 and (x)<-1:
        f = 1
    elif (x)>=-1 and (x)<=1:
        f = (x-1)**3+3
    elif (x)>1 and (x)<2:
        f = np.sin(np.pi*x)+3
    else:
        f = 3*np.sqrt(x-2)+4
    return f
       
for ii in range(N):
    y[ii] = function(x[ii])


fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()
       