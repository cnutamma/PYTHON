import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="srinu",
  database="pythonsql"
)

mycursor = mydb.cursor()


sql = "UPDATE pro1 SET id='3' WHERE id = '5'"

mycursor.execute(sql)

mydb.commit()

# print(mycursor)

print(mycursor.rowcount, "record(s) affected")