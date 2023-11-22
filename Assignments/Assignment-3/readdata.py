import re

fp = open("Assignments/Assignment-3/data.txt","r")
data = fp.read()

match = re.findall("[6-9]\d{9}|[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",data)

fp2 =open("data1.txt",'w')

for i in match:
    fp2.write(i+"\n")
  
print("Data has been successfully written into data1.txt ")
# print(match)


fp2.close()
fp.close()