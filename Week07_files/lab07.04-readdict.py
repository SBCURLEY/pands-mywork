# lab07.04-readdict.py
# Write a function that will read in a dict object from file.
# Author: Sharon Curley

import json
FILENAME = "testdict.json"

def readDict():
    # this will throw an error if the file does not exist
    # it should really just return an empty dic
    # # we can do this later
    with open(FILENAME) as f:
        return json.load(f)
    
# test the function
somedict = readDict()
print (somedict)