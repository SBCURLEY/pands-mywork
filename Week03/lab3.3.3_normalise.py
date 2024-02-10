# lab3.3.3_normalise.py
# This program reads in a string and strips any leading or trailing spaces
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string and the normalisied one
# Author: Sharon Curley

rawstring = input ("Please enter a String: ")
normalisedstring = rawstring.strip().lower()

lengthofrawstring = len(rawstring)
lengthofnormalised = len(normalisedstring)

print(f"That String normalised is : {normalisedstring}")
print (f"We reduced the input string from {lengthofrawstring} to {lengthofnormalised} characters")
