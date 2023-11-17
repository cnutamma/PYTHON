import requests

response=requests.get("https://dummyjson.com/users")

users_data=response.json()

users_list=users_data["users"]

# print(type(users_list))
# print(type(users_data))
data=[]

for user in users_list:
    data.append((user["id"],user["firstName"],user["gender"]))

#filtering male genders.
male_data = list(filter(lambda person: person[2] == 'male', data))
# Print the filtered data
for person in male_data:
    print(person)
