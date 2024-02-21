#ASSIGNMENT B2  ( Data cleaning )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1

import pandas as pd
import numpy as np

df = pd.read_csv('test1_unclean.csv')

#district column cleant ( " , ' )
df["DISTRICT"] = df["DISTRICT"].str.replace('"', "")
df["DISTRICT"] = df["DISTRICT"].str.replace("'", "")

#Total votes column cleant ( Total, = ,:)
df['TOTAL VOTES'] = df['TOTAL VOTES'].str.replace('Total', '')
df['TOTAL VOTES'] = df['TOTAL VOTES'].str.replace('=', '')
df['TOTAL VOTES'] = df['TOTAL VOTES'].str.replace(':', '')

df.to_csv('test1_clean.csv',index = False)

df = pd.read_csv("test1_clean.csv")

df['NOTA'] = ( df['TOTAL VOTES']-(df['LDF']+df['UDF']+df['NDA']+df['OTHERS']) ).fillna(df['NOTA'])
df['%LDF'] = ((df['LDF']/df['TOTAL VOTES'])*100).fillna(df['%LDF'])
df['%UDF'] = ((df['UDF']/df['TOTAL VOTES'])*100).fillna(df['%UDF'])
df['%NDA'] = ((df['NDA']/df['TOTAL VOTES'])*100).fillna(df['%NDA'])
df['%NOTA'] = ((df['NOTA']/df['TOTAL VOTES'])*100).fillna(df['%NOTA'])
df['%POSTAL'] = ((df['POSTAL VOTES']/df['TOTAL VOTES'])*100).fillna(df['%POSTAL'])
df['%LEAD'] = ((df['LEAD']/df['TOTAL VOTES'])*100).fillna(df['%LEAD'])
df['WINNER'] = np.where(df['LDF'] > df['UDF'], 'LDF', 'UDF')

df.to_csv("Data_analysis.csv",index=False)



