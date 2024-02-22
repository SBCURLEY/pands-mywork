# messingWithLists2.py
# These code examples are in the Jupyter notebook in course material
# Author: Sharon Curley

'''
ages = [12,21,2# messingWithLists.py   # list of ages

sum=0                    # want to get hte sum of these so make a variable called sum
for age in ages:         # for each age in ages
    sum += age           # add it to the sum
print(sum)
'''


ages = [12,21,23,34,"string"]     # list of ages and add a string
                                # size is 5 but we start count at zero so it it 0,1,2,3,4

sum=0                    # want to get hte sum of these so make a variable called sum
for age in ages:         # for each age in ages
    sum += age           # add it to the sum
print(sum)               #  line 19, in <module> TypeError: unsupported operand type(s) for +=: 'int' and 'str'

# DEBUG

'''
# dont do it this way
length_of_list = len(ages)
for i in range (0,length_of_list):
    sum+= ages[i]
print(sum)
'''




