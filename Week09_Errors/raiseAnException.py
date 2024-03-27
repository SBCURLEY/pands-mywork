# raiseAnException.py
# This program prompts the user for an amount and withdraws it from an account
# Author: Sharon Curley (lecture notes)


'''
# This code gives no error if a minus value is input

balance = 100

def withdraw(amount):
    global balance
    balance = balance - amount
    return balance

amount = int(input("amount to withdraw: "))

print (withdraw (amount))

# We need to put in a check that if a minus value is input, it prompts the user to change
'''

balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("Amount should always be greater than 0")
    balance = balance - amount
    return balance

amount = int(input("Amount to withdraw: "))
print (withdraw (amount))

# 09: Errors and Exceptions — jvdp-jb (jbusse.de)
# Define Custom Errors