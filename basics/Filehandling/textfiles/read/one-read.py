#how to read text files?

file=open("data1.txt",'r')
data=file.read()
print(data)
file.close()

'''
In read we have different types of methods-
read()-reading whole text data
readline()-reading first line of the text data
readlines()-read whole text data in the form of list
'''
