# -*- coding: utf-8 -*-
"""
1.2 Calculator

@author: Lilleigh Stevie
"""

#input variables
x = 2
y = 12
z = 50

#list with 5 components
first = x + y
second = y * z + 3 * x
third = first ** 2
forth = (2 * second - x / 2) / first
fifth = 7 % 3

comps=[first, second, third, forth, fifth]

#changes
comps[2] = comps[2] + 3
comps[4] = comps[4] * 3 / 4

#sum of components
out = comps[0]+comps[1]+comps[2]+comps[3]+comps[4]
print("The sum of the five components is:", out)
