# Program to show the format of an if statement

# format of an if statement
# if condition:
#   statements

# if condition:
#   statements(if true)
# else:
#   statements(if false)

# if condition1:
#   statements(if true)
# elif condition2:
#   statements(if condition1 is false but 2 is true)
# else:
#   statements(if both false)

# Author: Sharon Curley (lecture 4.1)

if True:
    print ("we are in the if statement ln22")

print ("sanity ln24")


b=1
if True:                                                           
    print ("we are in the if statement ln28")           # The If statement must be indented
    b=22                                           # Multiple statements which will only get executed if statement is true

print ("sanity ln31 ",b)


c=-1                                                # c cannot be equal to text "" even if it is "!". That is a string and we are checking an integer
if c==1:                                            # Double == is checking if it is equal                                               
    print ("c is one ln36")
else:
    print ("c is not one ln38")    

print ("sanity ln40 ",b)


c=1                                              
if isinstance(c,int) and c==1:                      # checking if c is an instance of integer (not necessary)                                                                                 
    print ("c is one ln44")
else:
    print ("c is not one ln46")    

print ("sanity ln48 ",b)


c=1                                              
if c==1:                                                                                                
    print ("c is one ln53")
else:
    print ("c is not one ln55")    


d = 10
if not isinstance(d,int):
    print ("Please give me an int")
elif d < 0:
    print("d is negative")
elif d >= 10:
    print ("d is 10 or higher")
else:
    print ("d is between 0 and 9 (inclusive)")

print ("sanity ln67 ",b)