#!/usr/bin/env python

'''

@Author: Balasubramanyam Evani
Manipal University Jaipur

Visualization helper script

'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.interpolate as interp


##### Objective functions

def f_M(X , Y):
    return -1.0 * ((np.sin(X) * np.power( np.sin( (X**2) / np.pi ) , 20)) + (np.sin(Y) * np.power( np.sin( (2 * Y**2) / np.pi ) , 20)))


def f_R(X, Y):
    return (1 - X)**2 + 100*(Y - X**2)**2


def f_S(X, Y):
    return X**2 + Y**2

def f_A(X, Y):
    return -20 * np.exp(-0.20 * np.sqrt(0.5*(X**2 + Y**2))) - np.exp(0.5*(np.cos(2*np.pi*X) + np.cos(2*np.pi*Y))) + 20 + np.e     


####### Surface Plots

def Visualization_Michalewicz():

    X = np.linspace(0 , np.pi , 100)
    Y = np.linspace(0 , np.pi , 100)
    X,Y = np.meshgrid(X , Y)
    Z = f_M(X , Y)
    plt.figure(1)
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

def Visualization_Rosenbrock():
  
    X, Y = np.meshgrid(np.linspace(-1.3, 1.3, 31), np.linspace(-0.9, 1.7, 31))
    Z = f_R(X, Y)
    plt.figure(1)
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)

def Visualization_Sphere():

    X, Y = np.meshgrid(np.linspace(-1.3, 1.3, 31), np.linspace(-1.3, 1.3, 31))
    Z = f_S(X, Y)
    plt.figure(1)
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)

def Visualization_Ackley():
    
    X,Y = np.meshgrid(np.linspace(-4, 4, 31), np.linspace(-4, 4, 31))
    Z = f_A(X, Y)
    plt.figure(1)
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)

######## Contour Visualization

def contour_Michalewicz():
    
    plt.figure(2)
    X = np.linspace(0 , np.pi , 100)
    Y = np.linspace(0 , np.pi , 100)
    X,Y = np.meshgrid(X , Y)
    Z = f_M(X , Y)
    plt.contourf(X,Y,Z)

def contour_Rosenbrock():

    plt.figure(2)
    X, Y = np.meshgrid(np.linspace(-1.3, 1.3, 31), np.linspace(-0.9, 1.7, 31))
    Z = f_R(X, Y)
    plt.contourf(X,Y,Z)

def contour_Sphere():

    plt.figure(2)
    X, Y = np.meshgrid(np.linspace(-1.3, 1.3, 31), np.linspace(-1.3, 1.3, 31))
    Z = f_S(X, Y)
    plt.contourf(X,Y,Z)

def contour_Ackley():

    plt.figure(2)
    X, Y = np.meshgrid(np.linspace(-4, 4, 31), np.linspace(-4, 4, 31))
    Z = f_A(X, Y)
    plt.contour(X,Y,Z)
