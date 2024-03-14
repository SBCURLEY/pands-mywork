# lab07.02c-readnumber.py
# This program uses these two functions, to count how many times the program has been run.
# Author: Sharon Curley

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

def writeNumber (number):
    with open (FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))
        
# main
num = readNumber()
num += 1
print(f"We have run this program {num} times")
writeNumber(num)
