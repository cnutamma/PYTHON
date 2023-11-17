import csv
import requests

response=requests.get("https://dummyjson.com/users")

users_data=response.json()

users_list=users_data["users"]

data=[]

for user in users_list:
    data.append((user["id"],user["firstName"],user["gender"]))
#Filtering male genders.
male_data = list(filter(lambda person: person[2] == 'male', data))


fp=open('male_list.csv','w',newline="")
cp=csv.writer(fp)
cp.writerows(male_data)
fp.close()
print("Data has been written into male_list.csv file successfully")
