# lab06.07-extra1.py
# Variables can be of type function, and we can call those variables.

def fun1():
    print("This is fun1")
def fun2():
    print("This is fun2")
          
whichFun = fun1
whichFun()
whichFun = fun2
whichFun()

# This means that lists, tuples and dicts can have variables of type function in them
# we could have a dict that stores the letter of the menu and the function associated with that letter.
# We could access that function by that letter. 
#
#
