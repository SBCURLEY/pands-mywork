# Messing with for loops
# Author: Sharon Curley (lecture)

# for elem in list:
    # do something

# for number in range(1,10):
    # do something
    
boats = ["Sigma","x yacht", "swan"]                                       #list with 3 strings

for boat in boats:
    print ("I'd rather be out in a ", boat,sep="", end="\n\n")                               # Comma puts in extra space, so put in sep=""   I'd rather be out in a  Sigma  
# Appear on same line end=""
# line break between each of them end="\n\n"
# Built in Functions documentation to learn more

# if you want to count 1 to 10
for i in range (0,10):           # ranges do not do teh last (up to and not including) so this is 0 to 9
    print (i)

print ("All done i is now",i)

if "swan" in boats:
    print ("That is a Boat")