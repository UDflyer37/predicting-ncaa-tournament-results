import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


cov1=pd.read_csv('Model 1 Verification.csv')

cov2=pd.read_csv('Model 2 Verification.csv')

cov3=pd.read_csv('Model 3 Verification.csv')

cov=pd.read_csv('2018-19 Tournament.csv')

dataframe= cov
y=dataframe['Round Reached']
x=dataframe['School Name']
#jittered_y = y + 0.3 * np.random.rand(len(y)) -0.05

dataframe1=cov1
y1=dataframe1['predict']
x1=dataframe1['School Name']
#jittered_y1 = y1 - 0.3 * np.random.rand(len(y1)) -0.05

dataframe2=cov2
y2=dataframe2['predict']
x2=dataframe2['School Name']
#jittered_y2 = y2 + 0.3 * np.random.rand(len(y2)) -0.05

dataframe3=cov3
y3=dataframe3['predict']
x3=dataframe3['School Name']
#jittered_y3 = y3 - 0.3 * np.random.rand(len(y3)) -0.05

fig = plt.figure(figsize=(13,5),dpi=100, facecolor='w', edgecolor='k')

plt.scatter(x,y,marker="o",label='Actual 2018-19 Tournament Result',s=200, facecolors='none', edgecolors='red')

plt.scatter(x1,y1,marker="x",label='Model 1: Distributed Random Forest',s=200)

plt.scatter(x2,y2,marker="+",label='Model 2: Deep Learning',s=200)

plt.scatter(x3,y3,marker="v",label='Model 3: Gradient Boosting Machine',s=200, facecolors='none', edgecolors='green')


#Clean-up


plt.xticks(rotation=90);
plt.tick_params(axis='x', which='major', labelsize=10)
plt.gcf().subplots_adjust(left=0, right=15)
plt.gcf().set_size_inches(1.2, plt.gcf().get_size_inches()[1])


#plt.tight_layout()
#plt.subplots_adjust(right=2,left=.5,top=1.5,bottom=.5,wspace=10,hspace=10)


plt.title('Predicted vs. Acutal',size='xx-large')
plt.xlabel('School Name',size='x-large')
plt.ylabel('Placement',size='x-large')
plt.legend(markerscale=.5);
plt.grid(b=None, which='major', axis='x');
