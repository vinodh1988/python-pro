import mysql.connector as mysql

mysqldb=mysql.connect(host="database-1.ckoufjtxq4s1.ap-south-1.rds.amazonaws.com",user="admin",password="Pass_123",database="work")

cursor=mysqldb.cursor()

try:
    cursor.execute("insert into people values(1,'ravi','chennai')")
    mysqldb.commit()
except Exception as e:
    print(e)
    mysqldb.rollback()

mysqldb.close()