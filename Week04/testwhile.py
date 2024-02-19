# Messing with while loops
# Author: Sharon Curley (lecture)

#while condition:
#    statements
#
# two types
#   Counter Controlled
#       we usually use for loops for counter controlled loops
#   Sentinal Controlled
#       if you are reading in from a user, one pattern is
#       read in from the user, check the while, and then read again in the 
#       body of the while loop
# be careful of infinite loops
#   make sure you modify what you are checking 

#Counter Controlled
count = 0                                                                   
while (count < 10):                                                        # Counter Controlled   Count 0 to 9
    print("Count is",count)
    count = count + 1             # count +=1
    
print ("At the end the count is ", count)

count = 10                                                                # Counter Controlled   Count down 10 to 0
while count >=0:
    print ("Countdown", count)
    count -=1
print ("Blast off")


#Sentinel Controlled Loops

val=input ("Type something (q to quit):")
while val != "q":
    print ("Hi Mom")
    val = input ("q to quit:")
    
print ("All done")