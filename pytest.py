import mysql.connector as mc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conn = mc.connect(user = 'root', password = 'password', database = 'company')
cur = conn.cursor()

#get the data from database 
query = "SELECT totcalls FROM test2 GROUP BY totcalls; "
cur.execute(query)
res = np.array(cur.fetchall())

'''
query = " ALTER TABLE test2 ADD COLUMN rangeA VARCHAR(200) AFTER eqpdays; "
cur.execute(query)
'''

n_Points = 200
dx = float(res.max())/n_Points

# New list y to store data
y = []

for i in range(len(res)):
	y.append(res[i][0]/dx)
query = " UPDATE test2 SET rangeA = CONCAT('From ', (SELECT CAST(totcalls/%f AS SIGNED))*%f, ' to ', (SELECT CAST(totcalls/%f AS SIGNED))*%f + %f);" 
cur.execute(query %(dx, dx, dx, dx,dx))
plt.hist(y, bins = n_Points)

cur.execute("SELECT rangeA, COUNT(*) FROM test2 GROUP BY rangeA ORDER BY COUNT(*) DESC")
rs = cur.fetchall()

conn.commit()
conn.close()

for i in range(len(rs)):
	print("%-50s"%rs[i][0],"%10d"%rs[i][1])

plt.show()