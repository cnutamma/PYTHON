import mysql.connector

try:
    db=mysql.connector.connect(host="localhost",user='root',password='srinu',database="assignment")
    dbcursor=db.cursor()
    sql_data="""
         create table products(
         pid int,
         pname varchar(100),
         price int,
         brand varchar(32)
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