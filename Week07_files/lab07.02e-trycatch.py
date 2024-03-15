# lab07.02e-trycatch.py
# This program uses try catch loop on the read
# Author: Sharon Curley

FILENAME = "count.txt"
def readNumber():
    try:
        with open (FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back
        # no file assumes first time running
        # ie 0 previous runs
        return 0

# Code from lab07.02c-readnumber.py
def writeNumber (number):
    with open (FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))
        
# main
num = readNumber()
num += 1
print(f"We have run this program {num} times")
writeNumber(num)