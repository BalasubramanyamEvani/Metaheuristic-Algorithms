#!/usr/bin/env python
'''

@Author: Balasubramanyam Evani
Manipal University Jaipur

https://arxiv.org/pdf/1004.4170.pdf Bat Algorithm by Xin-She Yang

'''
import random
import numpy as np
import math
import operator
from visualization import *
from util import *

############## normalise

def bounds(val,lb,ub):
    if val < lb:
        val = lb
    elif val > ub:
        val = ub
    return val

##############

def display(X):
    global n,dim
    contour_Michalewicz()

    x = []
    y = []

    for i in range(0 , n):
        x.append(X[i][0])
        y.append(X[i][1])

    plt.plot(x , y , 'x' , color='#5856c3')
    plt.pause(0.05)
    plt.clf()


## parameters

dim = 2
n = 50
max_epochs = 1000
r0 = 0.5
alpha = 0.95
gamma = 0.90
fmin = 0
fmax = 2
lb = 0
ub = np.pi

### Loudness and Pulse Rate
A = [0.95 for i in range(n)]
r = [r0 for i in range(n)]

## initialisation of lowerbound and upperbound
upbound = [[ub for i in range(dim)] for j in range(n)]
lowbound = [[lb for i in range(dim)] for j in range(n)]

## initialisation of frequency
frequency = [0.0 for i in range(n)]


## initialisation of position and velocity and fitness
v = [[0.0 for i in range(dim)] for j in range(n)]
x = [[0.0 for i in range(dim)] for j in range(n)]
fitness = [0.0] * n

best_fitness = float("inf")
best_pos = [0.0] * dim

################## initialisation of bats
for i in range(n):
    for j in range(dim):
        rnd = random.uniform(0 , 1)
        x[i][j] = lowbound[i][j] + (upbound[i][j] - lowbound[i][j]) * rnd
    fitness[i] = Michalewicz(x[i])
    if fitness[i] < best_fitness:
        best_fitness = fitness[i]
        for j in range(0 , dim):
            best_pos[j] = x[i][j]

print "initial best solution => ",best_fitness,"best_pos= ",best_pos

###################

################### Main Process
temp = [[0.0 for i in range(dim)] for j in range(n)]
for epoch in range(0 , max_epochs):
    mean = np.mean(A)
    #display(x) uncomment to see visualization
    for i in range(0 , n):
        rand = np.random.uniform(0 , 1)
        frequency[i] = lb + (ub - lb)*rand
        for j in range(0 , dim):
            v[i][j] = v[i][j] + (x[i][j] - best_pos[j]) * frequency[i]
            temp[i][j] = bounds(x[i][j] + v[i][j] , lb , ub)

        rand = np.random.uniform(0 , 1)
        if rand > r[i]:
            for j in range(0, dim):
                rand = np.random.uniform(-1.0 , 1.0)
                temp[i][j] = best_pos[j] + rand * mean
                temp[i][j] = bounds(temp[i][j] , lb , ub)

        temp_fitness = Michalewicz(temp[i])
        rand = np.random.uniform(0, 1)
        if rand < A[i] and temp_fitness < fitness[i]:
            fitness[i] = temp_fitness
            for j in range(0 , dim):
                x[i][j] = temp[i][j]
        if fitness[i] < best_fitness:
            best_fitness = fitness[i]
            for j in range(0, dim):
                best_pos[j] = x[i][j]
            A[i] = alpha * A[i]
            r[i] = r0 * (1 - math.exp(-1.0 * gamma * i))

print "best_fitness= ",best_fitness,"best_pos= ",best_pos
