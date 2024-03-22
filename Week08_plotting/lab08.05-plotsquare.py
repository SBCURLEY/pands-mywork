# lab08.05-plotsquare.py
# Write a program that plots the function y = x2
# Author: Sharon Curley

import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints)
plt.show ()