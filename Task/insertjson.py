import json
import requests

response=requests.get("https://dummyjson.com/users")
users_data=response.json()
users_list=users_data["users"]
data=[]
for user in users_list:
    data.append((user["id"],user["firstName"],user["gender"]))
#filtering male genders.
male_data = list(filter(lambda person: person[2] == 'male', data))
# Specify the JSON file path
json_file_path = 'male_data.json'

# Convert male_data to a list of dictionaries for better JSON structure
male_data_json = [{'ID': row[0], 'Name': row[1], 'Gender': row[2]} for row in male_data]

# Write male_data to the JSON file
with open(json_file_path, 'w') as jsonfile:
    json.dump(male_data_json, jsonfile, indent=2)

print(f"Data has been written to {json_file_path}")
