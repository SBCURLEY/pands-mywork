# lab08.01-makeList.py
# Write a program that makes a list, called salaries, that has (say 10) random 
# numbers (20000 – 80000).
# Author: Sharon Curley

import numpy as np 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1)
salaries  = np.random.randint (minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000
salariesMult = salaries + 1.05
newSalaries = salariesMult.astype(int)

# print (salariesPlus)
# print (salariesMult)
print (newSalaries)