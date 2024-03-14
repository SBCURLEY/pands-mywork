# lab07.02b-readnumber.py
# This program Write a function that takes in a number and overwrites a file with that number
# Author: Sharon Curley

FILENAME="count.txt"
def writeNumber (number):
    with open (FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))
        
# test it
writeNumber(3)
