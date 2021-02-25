import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cov=pd.read_csv('2019-20 NCAA Results.csv')

dataframe= cov
y=dataframe['predict']
x=dataframe['School Name']
#jittered_y = y + 0.3 * np.random.rand(len(y)) -0.05



fig = plt.figure(figsize=(13,5),dpi=100, facecolor='w', edgecolor='k')

plt.scatter(x,y,marker="x",label='Predicted 2019-20 Tournament Results',s=100)



#Clean-up


plt.xticks(rotation=90);
plt.tick_params(axis='x', which='major', labelsize=10)
plt.gcf().subplots_adjust(left=0, right=10)
plt.gcf().set_size_inches(1.2, plt.gcf().get_size_inches()[1])


#plt.tight_layout()
#plt.subplots_adjust(right=2,left=.5,top=1.5,bottom=.5,wspace=10,hspace=10)


plt.title('2019-20 Predicted NCAA Tounament Results',size='xx-large')
plt.xlabel('School Name',size='x-large')
plt.ylabel('Placement',size='x-large')
#plt.legend(markerscale=.5);
plt.grid(b=None, which='major', axis='both');


dataframe= cov

y1=dataframe['FGA']
x1=dataframe['predict']
#jittered_y1 = y1 - 0.3 * np.random.rand(len(y1)) -0.05

y11=dataframe['AVG_FGA']
x11=dataframe['PREDICT']

y4=dataframe['FG']
x4=dataframe['predict']
#jittered_y1 = y1 - 0.3 * np.random.rand(len(y1)) -0.05

y44=dataframe['AVG_FG']
x44=dataframe['PREDICT']

y5=dataframe['TRB']
x5=dataframe['predict']
#jittered_y1 = y1 - 0.3 * np.random.rand(len(y1)) -0.05

y55=dataframe['AVG_TRB']
x55=dataframe['PREDICT']



#Plot

plt.scatter(x1,y1,marker="o",label='Field Goals Attempted',s=50, facecolors='none', edgecolors='red')
plt.plot(x11,y11,'r',label='Average Field Goals Attempted')

plt.scatter(x4,y4,marker="+",label='Field Goals Made',s=50)
plt.plot(x44,y44,'b',label='Average Field Goals Made')

plt.scatter(x5,y5,marker="x",label='Total Rebounds',s=50)
plt.plot(x55,y55,'orange',label='Average Total Rebounds')





#Clean-up


plt.xticks(rotation=0);
plt.tick_params(axis='x', which='major', labelsize=10)
plt.gcf().subplots_adjust(left=0, right=7)
plt.gcf().subplots_adjust(top=1.5, bottom=0)
plt.gcf().set_size_inches(1, plt.gcf().get_size_inches()[1])


#plt.tight_layout()
#plt.subplots_adjust(right=2,left=.5,top=1.5,bottom=.5,wspace=10,hspace=10)


plt.title('Field Goal and Rebound Comparisons',size='xx-large')
plt.xlabel('Placement',size='x-large')
plt.legend(markerscale=.5);
plt.grid(b=None, which='major', axis='x');
