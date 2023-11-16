import csv
import requests

response=requests.get("https://dummyjson.com/users")

users_data=response.json()

users_list=users_data["users"]

data=[]

for user in users_list:
    data.append((user["id"],user["firstName"],user["gender"]))

#filtering male genders.
male_data = list(filter(lambda person: person[2] == 'male', data))


# Specify the CSV file path
csv_file_path = 'male_data.csv'

# Write male_data to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header if needed
    # csv_writer.writerow(['ID', 'Name', 'Gender'])
    
    # Write each row of data
    csv_writer.writerows(male_data)

print(f"Data has been written to {csv_file_path}")
