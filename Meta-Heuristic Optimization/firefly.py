#!/usr/bin/env python

'''

@Author : Balasubramanyam Evani
email: balasubramanyam.evani@gmail.com

Firefly Algorithm

References:Firefly Algorithms for Multimodal Optimization, Xin-She Yang,
Department of Engineering, University of Cambridge

'''

import random
import numpy as np
import math
import operator
from visualization import *
from util import *

### Firefly Class

class Firefly(object):
    def __init__(self , k):
        self.dim = k
        self.position = []
        for i in range(0 , k):
            self.position.append(0.0)
        self.error = 0.0
        self.intensity = 0.0

### Error Definition

def Error(sel , pos):
    dim = len(pos)
    true_min = 0.0
    if sel == 'M':
    	if dim is 2:
    	    true_min = -1.8013
    	calculated = Michalewicz(pos)
    	return (true_min - calculated)*(true_min - calculated)
    elif sel == 'R':
	if dim is 2:
    	    true_min = 0
    	calculated = Rosenbrock(pos)
    	return (true_min - calculated)*(true_min - calculated)
    elif sel == 'S':
	if dim is 2:
    	    true_min = 0
    	calculated = Sphere(pos)
    	return (true_min - calculated)*(true_min - calculated)
    elif sel == 'A':
	if dim is 2:
    	    true_min = 0
    	calculated = Ackley(pos)
    	return (true_min - calculated)*(true_min - calculated)

### Distance Calculation

def Distance(pos_a , pos_b):
    ssd = 0.0
    for i in range(0 , len(pos_a)):
        ssd += (pos_a[i] - pos_b[i])**2
    return math.sqrt(ssd)

### Displaying the swarm over contour

def display(sel , swarm):

    if sel == 'M':
    	contour_Michalewicz()
    elif sel == 'R':
	contour_Rosenbrock()
    elif sel == 'S':
        contour_Sphere()
    elif sel == 'A':
        contour_Ackley()

    x = []
    y = []
    for i in range(0 , len(swarm)):
        x.append(swarm[i].position[0])
        y.append(swarm[i].position[1])

    plt.plot(x , y , 'x' , color='#5856c3')
    plt.pause(0.05)
    plt.clf()

###################### Start
n = 50 			#Number of Fireflies
dim = 2			# Dimensions
max_epochs = 1000	# Maximum Generations

###################### Selection of Objective Functions

print "Choose Objective Function"
print "M- Michalewicz , R- Rosenbrock , S- Sphere, A- Ackley"

sel = raw_input()


if sel == 'M':
   Visualization_Michalewicz()
   min_x = 0
   max_x = np.pi

elif sel == 'R':
   Visualization_Rosenbrock()
   min_x = 0
   max_x = 1

elif sel == 'S':
   Visualization_Sphere()
   min_x = 0
   max_x = 1

elif sel == 'A':
   Visualization_Ackley()
   min_x = -4
   max_x = 4

################# Firefly algorithm Parameters

beta =  1.0
gamma = 1.0
alpha = 0.20
alpha_damp = 0.9855

#################

display_interval = max_epochs / 10

best_error = float("inf")
best_pos = np.zeros(dim)

swarm = []


print "############## Initializing Fireflies ##############"

for i in range(0 , n):

    swarm.append(Firefly(dim))
    for j in range(0 , dim):
        swarm[i].position[j] = (max_x - min_x)*random.uniform(0 , 1) + min_x

    swarm[i].error = Error(sel,swarm[i].position)
    swarm[i].intensity = 1/(swarm[i].error + 1)

    if swarm[i].error < best_error:
        best_error = swarm[i].error
        for k in range(0 , dim):
            best_pos[k] = swarm[i].position[k]


################### Main Loop

for epoch in range(0 , max_epochs):
    #display(sel , swarm) uncomment if you want to see the visualization
    if epoch % display_interval == 0:
        print "current epoch", epoch, " best_error = ",best_error," best_pos = ",best_pos

    for i in range(0 , n):
        for j in range(0 , n):
            if(swarm[i].intensity < swarm[j].intensity):

                r = Distance(swarm[i].position , swarm[j].position)
                b = beta * math.exp(-gamma * r * r)

                for k in range(0, dim):

                    swarm[i].position[k] += b * (swarm[j].position[k] - swarm[i].position[k])
                    swarm[i].position[k] += alpha * (random.uniform(0 , 1) - 0.50)
                    if swarm[i].position[k] < min_x:
                        swarm[i].position[k] = (max_x - min_x) * (random.uniform(0 , 1)) + min_x
                    if swarm[i].position[k] > max_x:
                        swarm[i].position[k] = (max_x - min_x) * (random.uniform(0 , 1)) + min_x

                swarm[i].error = Error(sel,swarm[i].position)
                swarm[i].intensity = 1/(swarm[i].error + 1)

    swarm.sort(key=operator.attrgetter("error"), reverse = False)
    if swarm[0].error < best_error:
        best_error = swarm[0].error
        for k in range(0 ,dim):
            best_pos[k] = swarm[0].position[k]
    alpha = alpha * alpha_damp

print "Final Best Position = ", best_pos, "Final best_error = ",best_error
