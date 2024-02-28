# lab04.02.05-average.py
# This program reads in numbers until 
# the user enters 0
# it will them print back out again 
# and their average
#
# Author: Sharon Curley

numbers = []
# First number we check if it is in the while loop
number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)
    
    # read the net number and check if zero
    number = int(input("enter number (0 to quit): "))
    
for value in numbers:
    print (value)
    
# I want average to be a float
average = float(sum(numbers))/len(numbers)
print(f"The average is {average}")

