import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df = pd.read_csv('C:/Users/Hp-PC/Desktop/python/Telecom_customer_churn.csv')
X = df.iloc[:,55].values #number of call
#X = X.sort()
y = [] #to store the label

'''
===========
divide the set into 3 groups:
Small number of calls: X[i] < 6000
Med number of calls: 6000 < X[i] < 20000
High number of calls: X[i] > 20000
===========
'''
for i in range(0,len(X)):
	if(np.isnan(X[i])):
		y.append('null')
		X[i] = 0
	if(X[i] < 6000):
		y.append('low')
	elif(6000 < X[i] and X[i] < 20000):
		y.append('med')
	else:
		y.append('high')
color = ('green','blue','red')
marker = ('x','s','o')
#print(len(y))
X1 = pd.DataFrame({'total call' : X, 'amount' : y})
print(X1.groupby('amount').count())
'''
x = (range(0,299))
#plt.scatter(x, X)
fig, ax = plt.subplots()
ax.grid()
ax.margins(0)

ax.axhspan(0,6000, facecolor = 'green', alpha = 0.5)
ax.axhspan(6000, 20000, facecolor = 'blue', alpha = 0.5)
ax.axhspan(20000,100000, facecolor =  'red', alpha = 0.5)

for i in range(0,299):
	if(y[i] == 'low'):
		ax.scatter(x[i],X[i], c = color[0], marker = marker[0])
	elif(y[i] == 'high'):
		ax.scatter(x[i],X[i], c = color[2], marker = marker[2])
	elif(y[i] == 'med'):
		ax.scatter(x[i],X[i], c = color[1], marker = marker[1])
			
		
plt.title('Number of calls')
plt.xlabel('Order')
plt.ylabel('Number of call made')
plt.savefig('data1.jpg')
plt.show()
'''