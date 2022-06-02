# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:37:21 2022

@author: SimoneSped
"""

from scipy.interpolate import lagrange, CubicSpline
import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolate(x_i, y_i):
    # Lagrange interpolation 
    
    return lagrange(x_i, y_i)

def cubic_spline_interpolate(x_i, y_i):
    # Cubic spline method
    
    return CubicSpline(x_i, y_i)
    
# Example Lagrange Interpolator
"""
# data
x_i = [0, 1, 2]
y_i = [1, 3, 2]

f = lagrange_interpolate(x_i, y_i)

fig = plt.figure(figsize = (10,8))

x_range = np.arange(np.amin(x_i), np.amax(x_i), 0.001)
plt.plot(x_range, f(x_range), 'b', x_i, y_i, 'ro')
plt.title('Lagrange Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
"""

# Example Cubic Spline Interpolator
x = np.arange(0.1, 10, 0.1)

# data
x_i = np.arange(10)
y_i = np.sin(x_i)
    
cs = cubic_spline_interpolate(x_i, y_i)

plt.plot(x, cs(x), 'b', x_i, y_i, 'ro')

plt.title('Cubic Spline Interpolator Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()