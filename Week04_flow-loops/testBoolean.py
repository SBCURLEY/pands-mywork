# messing around with Booleans
# Booleans can be True or False
# Boolean is the return type of the mathematical operators
#  = < > <=  >=
#
# flipped with the not keyword
# be careful using and or
#
# Author: Sharon Curley (lecture 4.1)

is_alive = True
print (f"is alive = {is_alive}")

var = (2==4)                                     # Is 2 equal to 4
print (f"var1 is {var}")

var = (2!=4)                                     # 2 is not equal to 4
print (f"var2 is {var}")

var = (2<=4)                                     # Is 2 less than or equal to 4
print (f"var3 is {var}")

logic = (2 <= 100) and (2 >= 100)                # True and False will give back a False
print (f"logic1 is {logic}")

grade = 400
Invalid = (grade < 0) or (grade > 100)              # Invalid False and True will give back a True
print (f"Invalid1 is {Invalid}")

grade = 40
Invalid = (grade < 0) or (grade > 100)              # Invalid False and False will give back a False
print (f"Invalid2 is {Invalid}")