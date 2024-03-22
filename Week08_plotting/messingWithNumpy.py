# messingWithNumpy.py
# This program plays around with numpy
# Author: Sharon Curley

import numpy as np

list_of_numbers = [1,2,3,"4"]
list_of_numbers = list_of_numbers + [3]
print ("list", list_of_numbers)

numbers = np.array ([1,2,3,4])
print ("array", numbers)

numbers = np.array ([1,2,3, "cat"])
print ("array", numbers)

numbers = np.array ([1,2,3])
numbers = numbers + 3
print ("array", numbers)

numbers = np.array ([1,2,3])
numbers = numbers * [1,2,3]
print ("array", numbers)

rando = np.random.randint (100,200,30)
print(rando)

normalrando = np.random.normal (100)
print (normalrando)

#Generating 
normalrando = np.random.normal (loc=50, scale=20, size=100)
print (normalrando)

