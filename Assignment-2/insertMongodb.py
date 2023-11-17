import pymongo
import requests

response=requests.get("https://dummyjson.com/products")
products_data=response.json()
products_list=products_data["products"]
data=[]
for product in products_list:
    data.append((product["id"],product["title"],product["price"],product["brand"]))

# print(data)

client = pymongo.MongoClient()
db = client["assignment"]
collection = db["products"]

# Insert data into MongoDB
for item in data:
    product_dict = {
        'product_id': item[0],
        'name': item[1],
        'price': item[2],
        'brand': item[3],
    }
    collection.insert_one(product_dict)

print("Data has been inserted into MongoDB")
