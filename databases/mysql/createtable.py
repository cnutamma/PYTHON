# creating table in the database using python.

import mysql.connector

db=mysql.connector.connect(host="localhost",user='root',password='srinu',database="pythonsql")
dbcursor=db.cursor()
sql_data="""
         create table pro1(
         id int,
         name varchar(32)
         );

         """
dbcursor.execute(sql_data)
dbcursor.close()
db.close()