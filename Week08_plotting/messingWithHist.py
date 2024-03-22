# messingWithHist.py
# We are messing with Histograms
# Author: Sharon Curley

import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(1)                                   # numbers will come out same each time with a seed
normData = np.random.normal(size=10000)

plt.hist(normData)
plt.show ()