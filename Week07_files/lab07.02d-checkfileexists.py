# lab07.02d-checkfileexists.py
# This program checks if the file exists
# Author: Sharon Curley

import os.path

FILENAME = "count1.txt"
if not os.path.isfile(FILENAME):
    print("File does not exist")
    # initialise file here