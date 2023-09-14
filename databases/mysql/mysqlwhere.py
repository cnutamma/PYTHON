import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="srinu",
  database="pythonsql"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM pro1 WHERE id ='1 '"

mycursor.execute(sql)

myresult = mycursor.fetchall()
# print(myresult)

for x in myresult:
  print(x)