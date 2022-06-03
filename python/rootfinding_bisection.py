# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 17:25:28 2022

@author: User
"""

import numpy as np

# Bisection Method, we need two inital guesses

def bisection(a, b, epsilon, n):
    if(a == b):
        # no interval specified
        
        return None
    if (f(b)*f(a) < 0):
        #there exists a root in the given interval
        
        #we compute the middle point
        x_m = (a+b)/2
        while True:
            if f(x_m) == 0.0 or np.abs(a-b)<epsilon:
                #zero found
                return x_m, n
            else:
                if f(x_m)*f(a)<0:
                    # new interval is [a, x_m]
                    n = n+1
                    return bisection(a, x_m, epsilon, n)

                else:
                    if f(x_m)*f(b)<0:
                        # new interval is [x_m, b]
                        n = n+1
                        return bisection(x_m, b, epsilon, n)

        
    else:
        #No zero in the given interval, better luck next time!
        
        return None

def f(x):
    #change the form of this to try other functions
    
    return np.sin(x) - x + x**3/6
    
x = np.linspace(-5, 5, 1000)
epsilon = 0.00001
n = 0
bisection_result = bisection(-1.0, 1.5, epsilon, n)
print("Zero found with the bisection method: ", bisection_result[0], "with", bisection_result[1], "iterations.")