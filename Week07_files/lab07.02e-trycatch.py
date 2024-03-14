# lab07.02e-trycatch.py
# This program uses try catch loop on the read
# Author: Sharon Curley

def readNumber():
    try:
        with open (FILENAME) as F:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back
        # no file assumes first time running
        # ie 0 previous runs
        return 0