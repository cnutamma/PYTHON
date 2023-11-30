
import pymongo

client=pymongo.MongoClient()

db=client['pythonconnection']

col=db['verify']

#col.insert_one({"id":1,"name":"srinivas","location":"bangalore"})
col.insert_one({"id":2,"name":"mounika","location":"bangalore"})

print("data inserted successfully")