import json
import requests

response=requests.get("https://dummyjson.com/users")
users_data=response.json()
users_list=users_data["users"]
data=[]
for user in users_list:
    data.append((user["id"],user["firstName"],user["gender"]))
#filtering male genders.
male_data = list(filter(lambda person: person[2] == 'male', data))

fp=open('male_list.json','w')
male_data_json = [{'ID': row[0], 'Name': row[1], 'Gender': row[2]} for row in male_data]
json.dump(male_data_json,fp,indent=2)
fp.close()
print("Data has been inserted into product.json file successfully")
