#loads-To convert json string objects to python dict object we use loads.

import json

# JSON string:
# Multi-line string
x = """{
	"Name": "srinivas",
    "Avail":true,
    "sal":null
	}"""

# parse x:
y = json.loads(x)

# Print the data stored in y
# print(y)
for data in y.items():
    print(data)
