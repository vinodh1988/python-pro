import mysql.connector as mysql

mysqldb=mysql.connect(host="database-1.ckoufjtxq4s1.ap-south-1.rds.amazonaws.com",user="admin",password="Pass_123")

mycursor=mysqldb.cursor()

mycursor.execute("create database python")

mysqldb.close()