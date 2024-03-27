# messingwithexcept.py
# This program is to show how to use try except
# Author: Sharon Curley (lecture notes)


# This runs with an error
# filename = sys.argv[1]
# IndexError: list index out of range
# No argument on teh command line

'''
# filename = "data.txt"
import sys

# print (sys.argv)
filename = sys.argv[1]
print (filename)
'''


# Run it with an except
# filename = "data.txt"

import sys

# print (sys.argv)     # list of the first thing it contains - name of ['.\\messingwithexcept.py']

try:
    filename = sys.argv[1]
    print(filename)
    with open(filename) as fp:                                                                              # open the file
       print(fp.read)
except IndexError as ie :                                                                                  # add in index error to catch the erro so we can solve
    print("Please enter the filename as an argument")
    # print(ie)                           # not very useful - comment out
except FileNotFoundError:
    print(f"File {filename} not found, please enter a filename that exists ")
    