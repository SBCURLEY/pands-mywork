# T2.1-readinnumbers.py
# read in two numbers and multiple them
# Author Andrew Beatty

'''
try:
    num1 = int(input("Enter a number "))
except ValueError:
    num1 = int(input("No Strings, enter a number please "))
    
num2 = int(input("and another "))

answer = num1 * num2

print(f"Answer is {answer}")
'''
# We now want to ensure that programs keeps asking us to enter a number 
# even if multiple string are entered.

'''
num1 = False
while (num1==False):
    try:
        num1 = int(input("Enter a number "))
    except ValueError:
        print ("That was not a number, ",end="")            #   end = keeps it on the same line

num2 = False
while (num2==False):
    try:
        num2 = int(input("and another number "))
    except ValueError:
        print ("That was not a number, ",end="")            #   end = keeps it on the same line

answer = num1 * num2

print(f"Answer is {answer}")
'''


# The above is a classic example of having to crete a function    
# If you want to make a small change you have to change in two places

def readNum(message="Enter a number: "):             # message will default to enter a number
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
            print ("That was not a number, ",end="")            #   end = keeps it on the same line
    return num

num1=readNum()
num2=readNum("Enter number 2: ")

answer = num1 * num2

print(f"Answer is {answer}")