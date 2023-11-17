import mysql.connector
import requests

try:
    db=mysql.connector.connect(host="localhost",user='root',password='srinu',database="assignment")
    dbcursor=db.cursor()
    sql_st="""
            insert into products(pid,pname,price,brand) values(%s,%s,%s,%s);
           """
    
    
    response=requests.get("https://dummyjson.com/products")
    products_data=response.json()

    products_list=products_data["products"]
    data=[]
    for product in products_list:
        data.append((product["id"],product["title"],product["price"],product["brand"]))



    dbcursor.executemany(sql_st,data)
    db.commit()
    print("data inserted successfully")

except mysql.connector.Error as err:
    print(err)

finally:
    dbcursor.close
    db.close
