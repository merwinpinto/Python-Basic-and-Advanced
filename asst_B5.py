#ASSIGNMENT B5 (Corr and Linear reg )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv("Data_analysis.csv")

data1 = df['LDF'].corr(df['TOTAL VOTES'])

print("Correlation between LDF and TOTAL VOTES Column :",data1)

sn.regplot(data = df ,x = 'LDF',y = 'TOTAL VOTES')

plt.show()
