import json
import requests

response=requests.get("https://dummyjson.com/products")
products_data=response.json()
products_list=products_data["products"]
data=[]
for product in products_list:
    data.append((product["id"],product["title"],product["price"],product["brand"]))


fp=open('product.json','w')
json_data = [{'pid': item[0], 'pname': item[1], 'price': item[2], 'brand': item[3]} for item in data]
json.dump(json_data,fp,indent=2)
fp.close()
print("Data has been inserted into product.json file successfully")