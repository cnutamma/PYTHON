import csv

import requests

response=requests.get("https://dummyjson.com/products")
products_data=response.json()
products_list=products_data["products"]
data=[]
for product in products_list:
    data.append((product["id"],product["title"],product["price"],product["brand"]))




fp=open('products.csv','w',newline="")
cp=csv.writer(fp)
cp.writerows(data)
fp.close()
print("Data has been written into product.csv file successfully")

