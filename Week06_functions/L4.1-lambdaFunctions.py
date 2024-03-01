# L4.1-lambdaFunctions.py
# More messing with functions
# Anonymous functions
# Author: Sharon Curley (lecture)

'''
x = lambda arg1: arg1**2        # arg 1 and return arg1 to the power of 2

answer = x(4)
print(answer)                

# what use is that? Two reasons for using functions as variables
# 1. passing a function into as a parameter into another function. Pandas later on. 
# 2. passing a function into another function as a variable.
'''

# Simple VAT rate - 
# create a  function call vatcalc which is going to calculate the simple VAT rate

#businesstype="standard"
businesstype="reduced"

vatcalc = lambda amount:amount * 0.23

if businesstype == "reduced":                       # if the business was standard
    vatcalc=lambda amount:amount *0.135
    
cash = 10

print (vatcalc(cash))


# Sort List

numbers = [2,33,55,1,4]
sortednumbers= sorted(numbers)

print (f"{numbers} sorted is {sortednumbers}")

'''
# Sorting a dictionary is more difficult
# sort dictionary

data = [{'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
        {'first': 'Grace', 'last': 'Hopper',     'YOB': 1906},
        {'first': 'Alan',  'last': 'Turing',     'YOB': 1912}]

sorteddata = sorted(data,key=lambda x: x["YOB"])             # in the sorted function, the key will be equal to the lambda function
# This function will take out one item of this "x"
# and return the year of birth

print (f"{data} sorted is {sorteddata}")    # comes out ugly - change to a for
'''

# Sorting a dictionary is more difficult
# sort dictionary

data = [{'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
        {'first': 'Grace', 'last': 'Hopper',     'YOB': 1906},
        {'first': 'Alan',  'last': 'Turing',     'YOB': 1912}]

sorteddata = sorted(data,key=lambda x: x["YOB"])             # in the sorted function, the key will be equal to the lambda function
# This function will take out one item of this "x"
# and return the year of birth

for item in sorteddata:
    print (item)                          # this sorts by year of birth
                                        # you can change "YOB" to "first" to sort by first name instead
    

