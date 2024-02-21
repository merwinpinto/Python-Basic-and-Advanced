#ASSIGNMENT B7  ( Graphs and plots implementaion )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
width=0.2
#Districts and all votes

df = pd.read_csv("Data_analysis.csv")

#x = df['CONSTITUENCY']
n = 6
x = ['Alappuzha','Ambalapuzha','Chengannur','Ollur','Aroor','Thiruvananthapuram']
ldf = df['LDF'].head(n)
udf = df['UDF'].head(n)
nda = df['NDA'].head(n)
nota = df['NOTA'].head(n)
others = df['OTHERS'].head(n)

bar1 = np.arange(len(x))
bar2 = [i+width for i in bar1]
bar3 = [i+width for i in bar2]
bar4 = [i+width for i in bar3]
bar5 = [i+width for i in bar4]



plt.figure(figsize=(13,7))
plt.bar(bar1,ldf,width,color='red',label='LDF')
plt.bar(bar2,udf,width,color='Black',label='UDF')
plt.bar(bar3,nda,width,color='Blue',label='NDA')
plt.bar(bar4,nota,width,color='Green',label='NOTA')
plt.bar(bar5,others,width,color='Gold',label='OTHERS')
plt.legend()

plt.title('VOTES OF PEOPLE ',fontsize=20,color='Blue')
plt.xlabel('DISTRICTS ',fontsize=20,color='Blue')
plt.ylabel('NO OF VOTES ',fontsize=20,color='Blue')
plt.xticks(bar1,x,rotation=30)
plt.xticks(bar2,x,rotation=30)
plt.xticks(bar3,x,rotation=30)
plt.xticks(bar4,x,rotation=30)
plt.xticks(bar5,x,rotation=30)


# Show Plot
plt.show()
