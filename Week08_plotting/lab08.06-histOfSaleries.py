# lab08.06-histOfSaleries.py
# Write a program that plots a histogram of the salaries (from Question 1)
# Author: Sharon Curley

import numpy as np 
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries  = np.random.randint (minSalary, maxSalary, numberOfEntries)

plt.hist(salaries, edgecolor="black")
plt.show()