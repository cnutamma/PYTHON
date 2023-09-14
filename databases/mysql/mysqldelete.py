import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="srinu",
  database="pythonsql"
)

mycursor = mydb.cursor()


sql = "DELETE FROM pro1 WHERE id = '2'"

mycursor.execute(sql)

mydb.commit()

# print(mycursor)

print(mycursor.rowcount, "record(s) deleted")