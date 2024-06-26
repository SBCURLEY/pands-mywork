# in this program I do some basic analysis of the grades.csv
# author: Sharon Curley (Lecture)

import pandas as pd
import matplotlib.pyplot as plt

# I made this var to make it easier to change the location of the files

path = '../data/'
filenameForGrades = path + 'grades.csv'

# df = pd.read_csv (filenameForGrades)         indexes are messed up
#print(df)

# there is an index col in this csv

df = pd.read_csv(filenameForGrades, index_col=0)    # starts counting from zero
#print(df)

# get rid of nulls and duplicates
# we could have chained these calls
# df = df.dropna().drop_duplicates()


df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Remove the lower grade for John as he has two for Programming
df = df.pivot_table(values='grade',index=['name','subject'],aggfunc='max').reset_index()

print(df)
print(type(df))

#   meanValues = df.groupby('name').mean() 
#   print(meanValues)

meanValues = df.groupby('name').mean('grade')          # group by name, subject.Can get mean, max, min, etc

print(meanValues)

meanValues = df.groupby('name')['grade'].mean()

print(meanValues)
print(type(meanValues))

# https://www.statology.org/pandas-mean-by-group/


df = df.pivot(index='name',columns='subject',values='grade')     # add labels to bar
print(df.corr())                # statistics - print a corralation table 
df.plot.bar()               # plot a bar graph
#plt.show()

# look at plot on Panda documentation   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot


'''
# I meant to say in the lecture if you want to plot a sub-set of the dataframe
# then just select the parts you want to plot
# eg
# df[['math', 'SIEM']].plot.bar()

plt.show()
'''