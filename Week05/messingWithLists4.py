# messingWithLists3.py
# These code examples are in the Jupyter notebook in course material TUPLES
# Author: Sharon Curley

# Tuples are in many ways similar to lists, but they are defined with parentheses () rather than square brackets []:
# They allow you to pass back multiple functions

'''
t=(1,2,3)
print (t)           # prints (1, 2, 3)
'''

t=(1,2,3)
x,y,z=t          # 3 variables separated by a comma
print (z)        # very handy for passing back multiple functions. z = 3

'''
Adam mentions in lecture
https://github.com/andrewbeattycourseware/pands-course-material/blob/main/jupyternotebooks/topic05-data%20structures.ipynb

numerator, denominator = x.as_integer_ratio()
print("", numerator, " / ",  denominator)
1  /  8

The indexing and slicing logic covered earlier for lists works 
for tuples as well, along with a host of other methods. 
Refer to the online Python documentation for a more complete list of these.
'''
