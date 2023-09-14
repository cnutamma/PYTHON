# '''
# API URL: https://dummyjson.com/products/1
# Method Type:GET
# AccessType:Public 
# Requied filed: None
# '''


import requests 
import json 

response=requests.get('https://dummyjson.com/products/1')

product_data=response.json()
# print(product_data)
for name in product_data:
    print(name)