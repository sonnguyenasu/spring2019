import mysql.connector as mc
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
cnx = mc.connect(user = 'root', password = 'password', database = 'nobel')
cursor = cnx.cursor()
query = 'SELECT %s, COUNT(*) FROM archive GROUP BY %s ORDER BY COUNT(*) DESC'
cursor.execute(query%(sys.argv[1], sys.argv[1]))
res = cursor.fetchall()
os.system('cls')
y = []
for i in range(0,len(res)):
	print(res[i][0], res[i][1])
	y.append(res[i][0])
