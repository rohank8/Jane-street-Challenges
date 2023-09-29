# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:55:08 2022

@author: kadams
"""

import numpy as np
import matplotlib.pyplot as plt
import statistics as st

z = np.zeros((1000,2))
print(z)

def function(z,a,b):
    m = sum(z)**a
    n = sum(z)**b
    return[m,n]
set = np.arange(0,1,0.001)
zn = np.random.random(10)
x,y = function(zn,2,3)
print('calling the function with a 10 element array of random numbers between 0 and 1')


OurGaussianDist = np.random.normal(size = 500)
sigma = st.stdev(OurGaussianDist)
plt.hist(OurGaussianDist,20)
plt.xlim(sigma*-3,sigma*3)
plt.title('Histogram showing at least ±3 standard deviations with 20 bins')
plt.show()





r = [-10,10]
first = np.random.choice(r,20)
second = np.random.choice(r,20)
third = np.random.choice(r,20)
print(first)
print(second)
print(third)
print('we have created 3 arrays of 20 elements chosen randomly to have the value +10 or -10')


e = np.linspace(-50,50,51)
zempty = []
for a in range (50):
    b = 0
    while b < 100:
        r = np.linspace(e[a],e[a+1],100)
        z = np.random.choice(r)
        b += 1
        zempty.append(z)
plt.hist(zempty,bins = 30)
plt.title('Histogram of 30 bins, 1000 values uniformly distributed from -50 to 50')
plt.xlim(-60,60)
plt.show()






























