# lab3.1_sub.py
# This program subtracts one number from another
# Author: Sharon Curley

""""
x = (input("Enter first number: "))
y = (input("Enter second number: "))
answer = x-y
print("{} minus {} ".format(x,y,answer))

# input reads in a string so we need to convert it inot an int 
# so we can perform mathematical operations
# error received - TypeError: unsupported operand type(s) for -: 'str' and 'str'
"""

x = int (input("Enter first number: "))
y = int (input("Enter second number: "))
answer = x-y
print("{} minus {} ".format(x,y,answer))

# When one inputs a value that is not an integer - errors are return
# ValueError: invalid literal for int() with base 10: 'hello'
# ValueError: invalid literal for int() with base 10: '10.1'