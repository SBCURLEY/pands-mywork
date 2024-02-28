# Messing with functions
# to demonstrate the defining and using functions
# Author: Sharon Curley (Lecture)


# https://docs.python.org/3/library/functions.html

# x,y,z = (1,2,3)                     # Using a tuple to find 3 variables

#print (x,y,z,sep="", end="")        # print is taking in 3 arguments, x, y, z.     
                                    # sep is a built in argument that we pass in to put in a space or not, dash, etc    
                                    # end is a built in argument that we pass in will bring up the next line
#print (f"{x} - {y} {z}")            # print is taking in one argument in a formatted string
#print("{}{}--{}".format(x, y, z))   # not recommended

# define a function that will cube something
def topower(number,power=3):       # pass in number and power
    # print(number)                # test the print function
    return (number**power)

# ans = topower (2)                # defined the function cube but it has not been executed. 
# print(f"We got {ans}")

num=2
# print(f"and {num} is {topower(num)}")    # gives an error TypeError: cube() missing 1 required positional argument: 'power' as I tried to run using one variable "num"

print(f"and {num} is {topower(num,4)}")      # pass in power = 3 default. Change this value to (num,4) to change the power to. 

