#!/usr/bin/env python
# coding: utf-8

# Puzzle: Janurary 2023
# Link: https://www.janestreet.com/puzzles/lesses-more-index/
# 
# Notes
# :f(a,b,c,d) = x, where x is the total number of squares drawn from this process.
# :Published solutions available 
# 
# Question: Consider the set S = {(a, b, c, d) | a, b, c, and d are all integers with 0 <= a, b, c, d <= 10,000,000}. Let M be the maximum value f obtains on S. Find (a, b, c, d) in S with minimum sum (a+b+c+d) where f(a, b, c, d) = M. Enter your answer as a semicolon-separated list, 10;6;3;1 for example.
# 
# Solution involves taking consider the four numbers on the corners of the active square to be an element of R^4. With the function f(a,b,c,d) defined as = (a-b,b-c,c-d,d-a), where a is the largest and b>d. Equations were also solved through Mathematica to check if code was correct.

# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import requests
import itertools


# In[24]:


def f(a,b,c,d):
    return abs(a-b),abs(b-c),abs(c-d),abs(d-a)

def steps(a,b,c,d):
    count = 1
    stop = 1
    while stop:
        w,x,y,z = f(a,b,c,d)
        a,b,c,d = w,x,y,z
        count +=1
        if sum([w,x,y,z]) == 0:
            stop = 0
    return count

def steps_show(a,b,c,d):
    count = 1
    stop = 1
    print("Row :", count," = ",a,b,c,d)    
    while stop:
        count +=1
        w,x,y,z = f(a,b,c,d)
        print("Row :", count," = ",w,x,y,z)
        a,b,c,d = w,x,y,z
        if sum([w,x,y,z]) == 0:
            stop = 0
    return count

def steps_output(a,b,c,d):
    count = 1
    stop = 1
    data = [(a,b,c,d)]
    while stop:
        count +=1
        w,x,y,z = f(a,b,c,d)
        a,b,c,d = w,x,y,z
        data.append((a,b,c,d))
        if sum([w,x,y,z]) == 0:
            stop = 0
    return data

def main(N):
    best = 0
    for a in range(1,int(N/3)):
        for b in range(1,N-2*a):
            for c in range(1,N-a-b):
                soln = steps(0,a,a+b,a+b+c)
                if soln> best:
                    print("\n",0,a,a+b,a+b+c,"takes",soln)
                    steps_show(0,a,a+b,a+b+c)
                    best = soln
            
start = time.time()
main(500)


# In[25]:


def build(data):
    if (data[0,3]-data[0,2]-data[0,1]) % 2 == 1:
        add = (2*data[0,3]-2*data[0,2]-2*data[0,1]) // 2
        second = data[0,:]*2+add
        top = np.array([0,second[0],second[0]+second[1],second[3]])
        new_rows = [top,second]
        outputs = np.concatenate([new_rows,data[1:,:]*2],axis=0)
    else:
        add = (data[0,3]-data[0,2]-data[0,1])//2
        second = data[0,:]+add
        top = np.array([0,second[0],second[0]+second[1],second[3]])
        new_rows = [top,second]
        outputs = np.concatenate([new_rows,data[1:,:]],axis=0)
    return outputs
        
inputs = np.array(steps_output(0,68,193,423))

while True:
    data = build(inputs)
    if data[0,3] < 10e6:
        inputs=data
        print(inputs.shape[0],end=" ")
    else:
        break
print("\n\n Answer is :",";".join([str(i) for i in inputs[0,:]]),"\n")
print(inputs)

