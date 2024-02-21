#ASSIGNMENT B4  ( Perform Distribution graphs on a data set such as binomial , poisson ..) )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Data_analysis.csv')

d1 = data['WINNER'].value_counts()
grp = data.groupby('DISTRICT')['LDF', 'UDF', 'NDA', 'NOTA', 'OTHERS'].sum()

d2 = data['LDF'].hist(bins= 15)

plt.title('Normal Distribution of LDF')
plt.xlabel('No of Votes',fontsize = 16 ,color = 'Red')
plt.ylabel('LDF',fontsize = 16 ,color = 'Red')
plt.show()

d3 = data['UDF'].hist(bins= 15)

plt.title('Normal Distribution of UDF')
plt.xlabel('No of Votes',fontsize = 16 ,color = 'Red')
plt.ylabel('UDF',fontsize=20,color = 'Red')
plt.show()

d4 = data['NOTA'].hist(bins= 15)

plt.title('Normal Distribution of NOTA')
plt.xlabel('No of Votes',fontsize = 16 ,color = 'Red')
plt.ylabel('NOTA',fontsize = 16 ,color = 'Red')
plt.show()


d6 = data['OTHERS'].hist(bins= 15)

plt.title('Normal Distribution of OTHERS')
plt.xlabel('No of Votes',fontsize = 16 ,color = 'Red')
plt.ylabel('OTHERS',fontsize = 16 ,color = 'Red')
plt.show()


d5 = data['NDA'].hist(bins= 15)

plt.title('Normal Distribution of NDA')
plt.xlabel('No of Votes',fontsize = 16 ,color = 'Red')
plt.ylabel('NDA',fontsize = 16 ,color = 'Red')
plt.show()
