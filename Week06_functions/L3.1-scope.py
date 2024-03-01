# L3.1-scope.py
# # demonstrate scope
# Author: Sharon Curley (lecture)

# I don't want you to use Global variables

'''
x = 999

def fun():
    print(x)
    
fun ()
'''

# Python will allow us to have the same variable name inside a function
# Below program does exactly as above one

'''
x = 999

def fun(num):
    print(num)
   
def fun2(x):                                   # same variable name in a function as the one outside. This example is x. Better to call it x2.
    print(f"in fun2 x {x}")
    x=21
    print (f"in fun2 x {x}")

fun2 (x)                                       # pass in an x
print (f"after fun2 x is {x}")                 # print x
                                            # x is too many things here. There are two different x's.
'''

x = 999

def fun(num):
    print(num)
   
def fun2(x2):                                   
    print(f"in fun2 x {x2}")
    global x                                   # key word
    x=21
    print (f"in fun2 x {x2}")

fun2 (x)                                       # pass in an x
print (f"after fun2 x is {x}")                 # print x
                                            # x is too many things here. There are two different x's.
