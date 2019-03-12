import mysql.connector as mc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
connection = mc.connect(user = 'root', password = 'password', database = 'nobel')
cursor = connection.cursor()
query = "SELECT OrganizationName,COUNT(*) FROM archive WHERE Category = '%s' GROUP BY OrganizationName ORDER BY COUNT(*) DESC;"
cursor.execute(query%sys.argv[1])
#cursor.execute(query)
res = cursor.fetchall()

os.system('cls')
for i in range(0, len(res)):
	print("%-90s"%res[i][0], "%10d"%res[i][1])


connection.commit()
connection.close() 