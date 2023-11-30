#dumps-To convert python dict to json string object


import json
py_dict={
    "id":1,
    "name":"srinivas",
    "sal":None,
    "avail":True

}

x=json.dumps(py_dict)

print(x)
print(type(x))    #python dic to json string object

