# messingWithLists.py
# These code examples are in the Jupyter notebook in course material
# Author: Sharon Curley (lecture)

boats = ["sigma", 23, [1,2,3,],{}]     # {} is dictionary

boats = boats + [1,2,3]

#print (len (boats))                  prints the length of boats - 4 in the list     4

#print(boats)                          # concatenate the two strings together         ['sigma', 23, [1, 2, 3], {}, 1, 2, 3]

#If you want to use a for Loop to go through what type of data you have
for  boat in boats:
    print(type(boat))





