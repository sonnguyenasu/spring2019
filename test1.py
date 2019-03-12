import mysql.connector as mc

cnx = mc.connect(user = 'root', password = 'password', database = 'hello')
query = 'SELECT installs FROM AppData'
cur = cnx.cursor()
cur.execute(query)
res = cur.fetchall()
for i in range(0, len(res)):
	print(res[i][0])
