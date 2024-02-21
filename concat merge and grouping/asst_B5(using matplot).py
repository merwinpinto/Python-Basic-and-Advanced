#ASSIGNMENT B5  ( Perfrom linear regression and correlation of 2 variables )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data_analysis.csv")
x = df['LDF'].values
y = df['LEAD'].values

#data = df['LDF'].corr(df['LEAD'])
data = (df['DISTRICT']).corr(df['LDF'],df['UDF'],df['NOTA'],df['NDA'],df['OTHERS'])

print("Correlation between UDF , LDF , NDA , NOTA , OTHERS votes :",data)
data = df.corr()



