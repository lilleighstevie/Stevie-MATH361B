# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:13:22 2019

@author: lille_000
"""
import numpy as np

N = 500
TOL = 0.0001
Z0 = -7.6
iterations = [Z0]
spacing = []

f = lambda z : np.tan(z)-z-2
g = lambda z : (1/np.cos(z))**2-1

newton = 2
i = 0
Zn = Z0
while newton > TOL and i < N:
    Zn1 = Zn -(f(Zn)/g(Zn))
    iterations.append(Zn1)
    newton = np.abs(Zn1 - Zn)
    spacing.append(newton)
    i += 1
    Zn = Zn1

if i==N:
    print("The iterations stopped because it did the max number of iterations.")
else:
    print("The iterations stopped due to reaching tolerance.")

print("The iterations are", iterations)
print()
print("The spacing between iterations are:", spacing)


