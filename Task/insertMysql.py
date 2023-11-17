import mysql.connector
import requests

try:
    db=mysql.connector.connect(host="localhost",user='root',password='srinu',database="task")
    dbcursor=db.cursor()
    sql_st="""
       insert into user(id,firstName,gender) values(%s,%s,%s);
       """
    
    
    response=requests.get("https://dummyjson.com/users")
    users_data=response.json()
    users_list=users_data["users"]
    data=[]
    for user in users_list:
        data.append((user["id"],user["firstName"],user["gender"]))
    
#filtering male genders.
    male_data = list(filter(lambda person: person[2] == 'male', data))


    dbcursor.executemany(sql_st,male_data)
    db.commit()
    print("data inserted successfully in mysql")

except mysql.connector.Error as err:
    print(err)

finally:
    dbcursor.close
    db.close
