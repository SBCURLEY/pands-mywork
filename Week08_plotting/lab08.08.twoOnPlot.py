# lab08.08.twoOnPlot.py
# Write program that has a list of counties,
# make it a long list (pick from five counties).
# Make some counties appear more than others. 
# Make a pie chart of the 

import numpy as np 
import matplotlib.pyplot as plt 

possibleCounties = ["Mayo", "Galway", "Roscommon", "Dublin", "Donegal"]
counties = np.random.choice(possibleCounties, p=[0.1, 0.3, 0.2, 0.12, 0.28], size=(100))  # pick 100 random from possible counties with the freq. set in p - probability

# now we need the number of occurences of each county
# this returns a tuple of the unique value and how may times it appears.

unique, counts = np.unique (counties, return_counts=True)

# plt.pie (counts, labels = unique)

plt.bar(unique,counts, edgecolor="black")

#plt.show ()

plt.savefig("Two_On_Plot")
