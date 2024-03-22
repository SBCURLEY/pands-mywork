# messingWithMatplotlib.py
# The following are introductions to matplotlib
# Author: Sharon Curley

import numpy as np 
import matplotlib.pyplot as plt 

''' 
# LINE PLOT           
xpoints = np.array (range(1,101))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints)
plt.show ()

# Save it
# plt.savefig("Lecture 1.png")

# Add labels
# plt.plot (xpoints, ypoints, label = "xsquared")
# plt.legend ()
# plt.show ()


# Add straight line
# plt.plot (xpoints, ypoints, label = "xsquared")
# plt.plot (xpoints, xpoints, label = "straight", color= "blue")
# plt.legend ()
# plt.show ()
'''

# SCATTER PLOT

xpoints = np.array (range(1,101))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints, label = "xsquared")
plt.plot (xpoints, xpoints, label = "straight", color= "blue")
plt.legend ()

randompoints = np.random.randint(1,1000,100)
plt.scatter(xpoints, randompoints, label="random")
plt.show ()