#inserting multiple data into the database.


import mysql.connector

db=mysql.connector.connect(host="localhost",user='root',password='srinu',database="pythonsql")
dbcursor=db.cursor()
sql_st="""
       insert into pro1 values(%s,%s);
       """
data=[(2,"gopi"),(3,"vamsi"),(4,"siva"),(5,"koti")]
dbcursor.executemany(sql_st,data)
db.commit()


dbcursor.close()
db.close()