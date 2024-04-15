# demonstrate reading from TSV and excel
# Author Sharon Curley Lecture

import pandas as pd
import re
import numpy as np
import dataManipulation

filename = 'originalData.tsv'
df = pd.read_table(filename)
#print(df.head(2))                               # prints first two columns
#print(df["Module ID"].head(2))                   # prints first two with Module ID
#print(df[["Module ID", "Duration"]].head(2))                   # prints first two with Module ID and Duration. Pass a list into the square brackets [[  ]]
                                                                # looks ugly so do the following

listOfCols = ['Module ID', 'Duration']
#print(df[listOfCols].head(2))

# create a new column

df['new'] = df['Duration'] * df['Number of Weeks']

listOfCols = ['Number of Weeks','Duration', 'new']

print(df[listOfCols].head(10))