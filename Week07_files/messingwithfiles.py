# messingwithfiles.py
# This program will play around with files
# Author: Sharon Curley

FILENAME= "data.txt"

'''
with open(FILENAME,"rt") as f:
    for data in f:
        #print (data)                      # new line for file and new line as carriage return. Spaces exist.
        #print (data, end="")
        print (data.strip())               # best method
        #print(data[:-1])
'''        
        
with open("data2.txt","w+") as f:
    f.write("How Now\n")
    f.write("Brown Cow ")
    f.seek(0)                                   # goes to the beginning of the file
    data = f.read()
    print (data)                                # io.UnsupportedOperation: not readable when seek is not input into code
    
print("done")