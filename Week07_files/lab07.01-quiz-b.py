# the with statement will atomatically close the file
# when it is finished with it

with open("test-b.txt", "w") as f:
    data = f.write("test b\n") # returns the number of chars written
    print (data)


with open("test-b.txt", "w") as f2: # open file again
    data = f2.write("another line") # returns the number of chars written
    print (data)
    
    
# b) file test-b is created
 #  7
 #  12


# c) another line   - overwrites the initial line
#    

