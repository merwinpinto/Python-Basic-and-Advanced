#ASSIGNMENT B3  ( Perform Merging Grouping and concat on a data set )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1

import pandas as pd

df = pd.read_csv('Data_analysis.csv')

d1 = pd.read_csv('Data_analysis1.csv')
d2 = pd.read_csv('Data_analysis2.csv')

Merge_data = d1.merge(d2, how='outer')

grouping = df.groupby('DISTRICT')

concat_data = pd.concat([d1,d2])

#index=True which is the default,CSV will include the
#row numbers in its first column;
#if you have specify index=False then your CSV will not.

concat_data.to_csv('concat_Data_analysis1_and_Data_analysis1.csv', index = False)

Merge_data.to_csv('Merged_Data_analysis1_and_Data_analysis2.csv', index = False)

for DISTRICT in grouping:
    print(DISTRICT)
