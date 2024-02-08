# lab3.1_randomGenerator.py
# This program prints out a random number between 1 and 10.
# Author: Sharon Curley

""""
import random
number = random.randint(1,10)
print ("Here is a random number {}".format(number))
"""

# Extra
# modifying the program so that the user inputs the range
import random
range1 = int (input ("Enter a number range from: "))
range2 = int (input ("Enter a number range to: "))
answer = random.randint(range1, range2)
print ("Here is a random number {}".format (answer))          # Reference https://www.w3schools.com/python/ref_random_randint.asp