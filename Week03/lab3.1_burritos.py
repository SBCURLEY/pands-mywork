# lab3.1_burritos.py
# Why does this expression cause an error? How can you fix it? 
# Author: Sharon Curley

""""
message = "I have eaten" + 99 + "burritos."
print (message)
# TypeError: can only concatenate str (not "int") to str
# 99 is an integer and only strings cn be concatenated to other strings with a +
"""

message = "I have eaten " + str(99) + " burritos."      # Reference        https://docs.python.org/3.4/library/functions.html?#func-str
print (message)


# Question 7: Why is eggs a valid variable name while 100 is invalid?   Eggs is a string - word and 100 is an integer.
# Question 8: What three functions can be used to get the integer, floating-point number, or string version of a value?
# integer = int()   floating-point number= fl()   string version = str()add.