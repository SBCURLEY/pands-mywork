# messingwithos.py
# This program plays around with the os - Miscellaneous operating system interfaces
# This module (os) provides a portable way of using operating system dependent functionality. 
# Author: Sharon Curley

import os

FILENAME = "messingwithfiles.py"
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line, end="")
else:
    print(FILENAME, "does not exist do you want to create it?")

# To remove a directory or file
# os.remove("data2.txt")

# Going up or down a directory
# FILENAME = "../messingwithfiles.py"