import numpy as np
import mysql.connector as mc
import pandas as pd
import matplotlib.pyplot as plt
import sys

conn = mc.connect(user = 'root', database = 'soccer', password = 'password')
cursor = conn.cursor()
s = '*'
query = "SELECT substring(Date,3,5) AS Month,Team.HomeTeam, SUM(IF(season1516.HomeTeam = '%s', FTHG, FTAG)) AS Goals FROM season1516 JOIN Team ON season1516.HomeTeam = Team.HomeTeam OR season1516.AwayTeam = Team.HomeTeam WHERE Team.HomeTeam ='%s' GROUP BY month;"
query1 = "SELECT substring(Date,3,5) AS Month,Team.HomeTeam, SUM(FTHG+FTAG) AS Goals FROM season1516 JOIN Team ON season1516.HomeTeam = Team.HomeTeam GROUP BY month;"
query2 = "SELECT substring(Date,3,5) AS Month,Team.HomeTeam, SUM(IF(season1516.HomeTeam = '%s', FTHG, FTAG)) AS Goals FROM season1516 JOIN Team ON season1516.HomeTeam = Team.HomeTeam OR season1516.AwayTeam = Team.HomeTeam WHERE Team.HomeTeam = '%s' GROUP BY month;"
query3 = "SELECT substring(Date,3,5) AS Month,Team.HomeTeam, SUM(IF(season1718.HomeTeam = '%s', FTHG, FTAG)) AS Goals FROM season1718 JOIN Team ON season1718.HomeTeam = Team.HomeTeam OR season1718.AwayTeam = Team.HomeTeam WHERE Team.HomeTeam ='%s' GROUP BY month;"
query4 = "SELECT substring(Date,3,5) AS Month,Team.HomeTeam, SUM(IF(season1718.HomeTeam = '%s', FTHG, FTAG)) AS Goals FROM season1718 JOIN Team ON season1718.HomeTeam = Team.HomeTeam OR season1718.AwayTeam = Team.HomeTeam WHERE Team.HomeTeam ='%s' GROUP BY month;"

if sys.argv[1] != 'total':
	cursor.execute(query%(sys.argv[1],sys.argv[1])) 
else:
	cursor.execute(query1)
res = cursor.fetchall()
y = []
z = []
for i in range(len(res)):
	y.append(res[i][0])
	z.append(int(res[i][2]))
	
if sys.argv[1] != 'total':
	cursor.execute(query3%(sys.argv[1],sys.argv[1]))
	res = cursor.fetchall()
	for i in range(len(res)):
		y.append(res[i][0])
		z.append(int(res[i][2]))

p1 = plt.plot(y,z, label = sys.argv[1])
if len(sys.argv) > 2:
	cursor.execute(query2%(sys.argv[2],sys.argv[2]))
	res = cursor.fetchall()
	t = []
	for i in range(len(res)):
		t.append(int(res[i][2]))
	cursor.execute(query4%(sys.argv[2],sys.argv[2]))
	res = cursor.fetchall()
	for i in range(len(res)):
		t.append(int(res[i][2]))
	p2 = plt.plot(y,t, c = 'red', label = sys.argv[2])
plt.legend(loc = 'upper left')
plt.xlabel("month")
plt.ylabel("# goals")
if len(sys.argv) > 2:
	plt.savefig('%svs%s.jpg'%(sys.argv[1],sys.argv[2]))
else:
	plt.savefig('%s.jpg'%sys.argv[1])
plt.show()

