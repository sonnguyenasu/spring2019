import mysql.connector as mc

connection = mc.connect(user = 'root', password = 'password', auth_plugin = 'mysql_native_password', database = 'company')
cursor = connection.cursor()

cursor.execute("SELECT * FROM test2")
print("fetchall:")
result = cursor.fetchall()
for r in result:
	print(r)
cursor.execute("SELECT * FROM test2")
print("\nfetch one:")
res = cursor.fetchone()
print(res)