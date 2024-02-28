# lab3.2.1_round.py
# The program will take in a float and output an int (rounded up or down)
# be careful of round, it rounds to the nearest number, e.g. 4.5 rounds to 4
# but 5.5 rounds to 6
# Author: Sharon Curley

numbertoround = float (input("Enter a float number:"))
roundednumber = round(numbertoround)
print ("{} rounded is {}" .format(numbertoround, roundednumber))



