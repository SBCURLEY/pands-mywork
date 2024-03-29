# lab9.0- myFunctions.py
# This program is to show how to make a module,  
# that contains functions, and test cases for the functions
# it has a function called fibonacci that takes in number
# and returns a list containing a fibonacci sequence with that many numbers

# A Fibonacci sequence is a series of numbers that starts off with 0 and 1 and each 
# subsequence number is the sum of the previous two. 

import logging                                                  
#logging.basicConfig(level=logging.DEBUG)

def fibonacci (number):
    if number < 0:
        raise ValueError('number must be > 0')
    if number == 0:
        return []
    a=0
    b=1
    fibonacciSequence=[0]                                       # we have one in the list already so number - 1 times
    for i in range(1,number):
        fibonacciSequence.append(b)
        a, b=b,a+b
    logging.debug("%d: %s", number, fibonacciSequence)
    return fibonacciSequence


if __name__ == "__main__":    
    return7=[0,1,1,2,3,5,8]
    return11=[0,1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(7) == return7, "Incorrect return for 7)"
    assert fibonacci(11) == return11, "Incorrect return for 11"
    assert fibonacci (0) ==[], "Incorrect return value for 0"
    assert fibonacci (1) == [0], "incorrect value for 1"
    try:
        fibonacci(-1)
    except ValueError:                                          # we want this exception to be thrown
        pass                                                    # so this is an example where we want to do nothing
    else:                                                       # if the exception was not thrown we should throw an Assertion error
        assert False, "Fibonacci missing ValueError"            # # or raise AssertionError("fibonacci should have thrown a value Error ")
        
    
    
    

    # tests will go here
    print("all good")