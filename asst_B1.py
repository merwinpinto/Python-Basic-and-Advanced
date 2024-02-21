#ASSIGNMENT B1  ( Basic operations on mean median mode and central tendancy )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1

import pandas as pd

df = pd.read_csv('exams.csv')
print(df)

print("\n\t\tOverall Central tendancy of Maths Score \n")
print("\nCentral tendency  : ",df['MATHS SCORE'].describe())
print("\n================================================\n")

print("\n\t\t AVERAGE SCORE OF CLASS \n")
print("\nMaths score avg   : ",df['MATHS SCORE'].mean())
print("\nReading score avg : ",df['READING SCORE'].mean())
print("\nWriting score avg : ",df['WRITING SCORE'].mean())


print("\n================================================\n")
print("\n\t\tREADING SCORE \n")
print("\nMedian : ",df['READING SCORE'].median())
print("\nMode  : ",df['READING SCORE'].mode())

print("\n================================================\n")
print("\n\t\tWRITING SCORE VARIANCE\n")
print("\nvariance  : ",df['WRITING SCORE'].var())

print("\n================================================\n")
print("\n\t\tWRITING SCORE STANDARD DEVIATION \n")
print("\nStandard Deviation  : ",df['WRITING SCORE'].std())

print("\n================================================\n")

