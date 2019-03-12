import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

'''df = pd.read_csv('C:/Users/Hp-PC/Desktop/python/Telecom_customer_churn.csv')
x = df.iloc[1:,0]
print("sum of mean income is: ",x.sum())
'''
sample1 = pd.read_csv('C:/Users/Hp-PC/Desktop/python/Telecom_churn_data.csv')
X = sample1.iloc[101:200, [95,96]]
#getting rid of nan values
X.fillna(0)
#Kmeans clustering into 3 groups
#X = np.array(X, dtype = np.float32)
print(X)
#y_pred = KMeans(n_clusters = 3).fit_predict(X)
#plt.scatter(X[:,0], X[:,1])
#plt.scatter(X[:,0], X[:,1], c = y_pred)
#plt.show()