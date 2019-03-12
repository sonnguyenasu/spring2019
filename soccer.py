import mysql.connector as mc
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
os.system('cls')
cnx = mc.connect(user = 'root', password = 'password', database = 'soccer')
cur = cnx.cursor()
query = 'SELECT substring(Date,3,5) AS Month, Team.HomeTeam, SUM(IF(%s.HomeTeam = \'%s\', FTHG, FTAG)) AS GOALS FROM %s JOIN Team ON %s.HomeTeam = Team.HomeTeam OR %s.AwayTeam = Team.HomeTeam WHERE Team.HomeTeam = \'%s\' GROUP BY Month'
cur.execute(query%(sys.argv[1],sys.argv[2],sys.argv[1],sys.argv[1],sys.argv[1],sys.argv[2]))
res = cur.fetchall()
y = []

for i in range(len(res)):
	print(res[i][:])
	y.append(float(res[i][2]))

x = np.arange(0,len(y),1)

a, b = np.polyfit(x, y, 1)
y_pred = a*x + b
plt.scatter(x,y, label = sys.argv[2])
plt.plot(x, y_pred)
plt.legend()

query = 'SELECT substring(Date,3,5) AS Month, Team.HomeTeam, SUM(IF(%s.HomeTeam = \'%s\', FTHG, FTAG)) AS GOALS FROM %s JOIN Team ON %s.HomeTeam = Team.HomeTeam OR %s.AwayTeam = Team.HomeTeam WHERE Team.HomeTeam = \'%s\' GROUP BY Month'
cur.execute(query%(sys.argv[1],sys.argv[3],sys.argv[1],sys.argv[1],sys.argv[1],sys.argv[3]))
res = cur.fetchall()
y = []

for i in range(len(res)):
	print(res[i][:])
	y.append(float(res[i][2]))

x = np.arange(0,len(y),1)

a, b = np.polyfit(x, y, 1)
y_pred = a*x + b
plt.scatter(x,y, color = 'red', label = sys.argv[3])
plt.plot(x, y_pred)
plt.legend()
plt.show()
