# lab3.2.4_ convert.py
# Messing around with this program to take in a float amount of dollars and returns that absolute amount in cent
# Author: Sharon Curley

import math
# First I tackle the input  - enter a float number with or without a minus sign
number = float(input("Please enter an amount: "))

# Change this to an absolute value
absolutevalue = abs(number)

# change the float to an integer. Is there a better way than multiplying by 100 ???????
ascent = int((absolutevalue)*100)

print (absolutevalue)
print("That amount in cent is {}".format (ascent))             # old way
print(f"That amount in cent is {ascent}")                      # better method