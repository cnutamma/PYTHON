# creating table in the database using python.
#Reading table values in the database.

import mysql.connector

db=mysql.connector.connect(host="localhost",user='root',password='srinu',database="pythonsql")
dbcursor=db.cursor()
dbcursor.execute("select * from pro1")
data=dbcursor.fetchall()
print(data)
dbcursor.close()
db.close()