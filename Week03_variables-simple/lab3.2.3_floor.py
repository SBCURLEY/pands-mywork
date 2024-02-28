# lab3.2.3_floor.py
# This program takes in a float and outputs an int rounded down.
# Need the math module math.floor()
# Author: Sharon Curley

import math

numbertofloor = float (input("Enter a float number: "))
floorednumber = math.floor(numbertofloor)
print("{} floored is {}".format (numbertofloor, floorednumber))
