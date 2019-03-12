import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

df = pd.read_csv('C:/Users/Hp-PC/Desktop/python/Telecom_customer_churn.csv')
X = df.iloc[:,55].values #
n_Points = 2000. #number of points
dx = np.nanmax(X)/n_Points #dx on hist
y = []
for i in range(0,len(X)):
	if(np.isnan(X[i])):
		y.append('null')
	if(~np.isnan(X[i])):
		number = int(X[i]/dx)*dx
		y.append(number)
		#print(X[i])
	
X1 = pd.DataFrame({"amount" : X, "range": y})
print(X1.groupby("range").count().sort_values(by = "amount", ascending = False))
#X2 = pd.DataFrame({"amount" : X[int(int(sys.argv[1])/dx):int(int(sys.argv[2])/dx)], "range" : y[int(int(sys.argv[1])/dx):int(int(sys.argv[2])/dx)]})
X1.hist(column = 'range',bins = int(n_Points))#, range = (int(sys.argv[1]), int(sys.argv[2])))

'''Setting up the plot'''
#set limit for the plot
#plt.xlim(X.min(), np.nanmax(X))
plt.xlim(int(sys.argv[1]), int(sys.argv[2]))
#plt.ylim(0,400)
plt.xlabel('range')
plt.ylabel('frequency')

#plt.savefig('20190220.jpg')
plt.show()