#load-Read json file and convert it into python dict object.


import json
f=open('load.json','r')
print(json.load(f))