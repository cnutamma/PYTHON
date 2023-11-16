import mysql.connector

try:
    db=mysql.connector.connect(host="localhost",user='root',password='srinu',database="task")
    dbcursor=db.cursor()
    sql_data="""
         create table user(
         id int,
         firstName varchar(32),
         gender varchar(32)
         );

         """

    dbcursor.execute(sql_data)
    db.commit()
    print("table created successfully")

except mysql.connector.Error as err:
    print(err)

finally:
    dbcursor.close
    db.close