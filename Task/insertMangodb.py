import pymongo
import requests

response=requests.get("https://dummyjson.com/users")
users_data=response.json()
users_list=users_data["users"]
data=[]
for user in users_list:
    data.append((user["id"],user["firstName"],user["gender"]))
#filtering male genders.
male_data = list(filter(lambda person: person[2] == 'male', data))

# MongoDB connection details
mongo_client = pymongo.MongoClient()
# Select or create a database
db = mongo_client["task"]

# Select or create a collection
collection = db["user"]

# Insert male_data into the collection
for person_data in male_data:
    record = {"ID": person_data[0], "Name": person_data[1], "Gender": person_data[2]}
    collection.insert_one(record)

print("Data has been inserted into MongoDB")
