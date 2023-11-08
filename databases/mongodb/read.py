import pymongo

client = pymongo.MongoClient()

db = client['pythonconnection']
col = db['verify']

# print user with name

user_list = col.find({})

for user in user_list:
    print(user['name'])