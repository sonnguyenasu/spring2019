import mysql.connector as mc
import numpy as np
import pandas as pd


cnx = mc.connect(user = 'root', password = 'password', database = 'sakila')
cur = cnx.cursor()

def select(column, table, condition):
	query = "SELECT %s FROM %s %s;"
	cur.execute(query %(column, table, condition))
	result = cur.fetchall()
	return result
'''
def select(column, table):
	query = "SELECT " + column + " FROM " + table
	cur.execute(query)
	result = cur.fetchall()
	return result
'''

def get_name(database_file, actor_id):
	query = "SELECT first_name, last_name FROM actor WHERE actor_id = "
	connection = mc.connect(user = 'root', password= 'password', database = database_file)
	cursor = connection.cursor()
	cursor.execute(query+actor_id+";")
	results = cursor.fetchall()
	cursor.close()
	connection.close()
	
	return results[0]

#print("Full name for actor:", get_name('sakila', "1")[0], get_name('sakila', "1")[1])
print(select("actor_id","actor", " ORDER BY actor_id"))
	