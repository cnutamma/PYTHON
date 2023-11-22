import re

num=input("Enter MobileNo:")
match=re.fullmatch('[6-9]\d{9}',num)

if match!=None:
    print("Number is valid mobile number")
else:
    print("Please enter valid mobile number")