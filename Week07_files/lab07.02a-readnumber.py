# lab07.02a-readnumber.py
# This program reads in a number from an existing file (count.txt)
# Author: Sharon Curley

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
# test it
num = readNumber()
print(num)
