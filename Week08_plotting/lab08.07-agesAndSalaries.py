# lab08.07-agesAndSalaries.py
# Write a program that makes a list called ages
# that has, the same number random values as salaries, (range:21 to 65) 
# Make scatter plot of this dat

import numpy as np 
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)                                                               # random numbers are the same each time
salaries  = np.random.randint (minSalary, maxSalary, numberOfEntries)
ages  = np.random.randint (low = 21, high = 65 , size = numberOfEntries)        # values should be at the top

plt.scatter(ages, salaries, label="Salaries")
# plt.show()                                                                    # if you show at this point the program will stop here

xpoints = np.array(range(1,101))                                                # add x squared
ypoints = xpoints * xpoints                                                     # multiply each by each

plt.plot(xpoints, ypoints, color="r", label = "x squared")

plt.title("Random Plot")
plt.xlabel ("Salaries")
plt.ylabel ("Age")
plt.legend ()
# plt.show ()

plt.savefig("Ages_Salaries.png")