# lab06.02-menu.py
# Write a function that prints out a menu of commands we can perform, ie add, view and quit.
# The function should return what the user chose.
# Author: Sharon Curley (lab)

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice=input("Type one letter (a/v/q): ").strip()    # The strip() method removes any leading, and trailing whitespaces.
    
    return choice

# Test the function

choice  = displayMenu()
print(F"You chose {choice}")