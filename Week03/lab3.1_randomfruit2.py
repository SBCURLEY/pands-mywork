# lab3.1_randomfruit.py
# This program prints out a random fruit
# Author: Sharon Curley

import random    
# imports random module

fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# we want a random number between 0 and length -1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print ("A random fruit: {}".format(fruit))
