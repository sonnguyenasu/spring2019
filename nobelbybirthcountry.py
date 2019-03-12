import numpy as np
import matplotlib.pyplot as plt
import mysql.connector as mc
import os
import sys
cnx = mc.connect(user = 'root', password = 'password', database = 'nobel')
cur = cnx.cursor()
query = 'SELECT FullName, Year FROM archive WHERE BirthCountry = "%s";'
cur.execute(query%sys.argv[1])
res = cur.fetchall()
os.system('cls')
for col in range(len(res)):
	print("%-20s%-25d"%(res[col][0],res[col][1]))
