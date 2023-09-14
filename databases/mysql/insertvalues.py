import mysql.connector

db=mysql.connector.connect(host="localhost",user='root',password='srinu',database="pythonsql")
dbcursor=db.cursor()
sql_data="""
        insert into pro1 values(1,"srinu");


         """
dbcursor.execute(sql_data)
db.commit()


dbcursor.close()
db.close()