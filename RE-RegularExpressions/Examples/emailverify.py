import re

str=input("Enter Email:")
match=re.fullmatch('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',str)

if match!=None:
    print("Email is valid")
else:
    print("Please check entered email")