#L5.1-messing-WithModules.py
# Messing with modules
# anaconda has installed a lot of modules already onto out machines

# from constraint import *
# from github import Github
# import nltk
# Two ways to di it


from github import Github
from constraint import *

import math as m                       # 1
from math import cos                   # 2

var = m.cos(3.14)
#var = cos(3.14)

print(var)
