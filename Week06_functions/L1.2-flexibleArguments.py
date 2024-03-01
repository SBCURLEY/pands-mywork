# L1.2-flexibleArguments.py
# More messing with functions
# flexible arguments
# Author: Andrew Beatty

print (1,2,3, sep="", end="\t")
print ("hi")


# passing in Tuples

def fun1(*args):
    print (type(args))
    print (args)
    
fun1 ("a", "b", "c")


# passing in values - unnamed arguments

def fun1(*args):
    print (type(args))
    for val in args:
        print (val)
    
fun1 ("d", "e", "f")


# keyword arguments

def fun2(**kwargs):                      # keyword arguments
    print (type(kwargs))
    print (kwargs)
    # for val in args:
    # print (val)
fun2 (name = "Joe", age = "21", gender = "M")        # Makes a dictionary   {'name': 'Joe', 'age': '21', 'gender': 'M'}


# sample code
def ave (*values):
    number_of_values=len(values)
    sum=0
    for value in values:
        sum+=value
        
    average = sum / number_of_values
    return average

print(ave(1,2,3,4,5,6))            # ans = 3.5
        

# sample code  - return multiple variables as a Tuple
def ave (*values):
    number_of_values=len(values)
    sum=0
    for value in values:
        sum+=value
        
    average = sum / number_of_values                 # variables in the code here do not have anything to do with below
    return average, sum                              # average and sum vs av1 and sum_of_numbers

av1, sum_of_numbers = ave(1,2,3,4,5,6)       
print (f"{av1} and sum is {sum_of_numbers}")