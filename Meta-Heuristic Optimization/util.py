#!/usr/bin/env python

'''

@Author:Balasubramanyam Evani
Manipal University Jaipur

Objective Functions

'''

import math

def Michalewicz(pos):
    result = 0.0
    for i in range(0 , len(pos)):
        a = math.sin(pos[i])
        b = math.sin(((i+1) * pos[i] * pos[i] ) / math.pi)
        c = math.pow(b , 20)
        result += a*c
    return -1.0 * result

def Rosenbrock(pos):
    return (1 - pos[0])**2 + 100*(pos[1] - pos[0])**2

def Sphere(pos):
    return pos[0]**2 + pos[1]**2

def Ackley(pos):
    return -20 * math.exp(-0.20 * math.sqrt(0.5*(pos[0]**2 + pos[1]**2))) - math.exp(0.5*(math.cos(2*math.pi*pos[0]) + math.cos(2*math.pi*pos[1]))) + 20 + math.e 
