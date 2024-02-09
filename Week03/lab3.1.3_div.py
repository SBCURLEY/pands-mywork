# lab3.1.3_div.py
# This program reads in two numbers and divides the first one by the second and give the integer result and the remainder.
# Author: Sharon Curley

x = int(input("Enter first number: "))
y = int (input("Enter the number you want to divide by: "))
answer = int(x//y)    # // gives the into division
remainder = x%y       # gives the remainder
print("{} divided by {} is {} with remainder {}". format (x, y, answer, remainder))
