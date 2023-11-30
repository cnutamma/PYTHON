'''
There are some variable properties and methods of file object:
1)readable
2)writable
3)closed
4)name-to know the name of the text file
'''

file=open("data.txt",'w')

print(file.readable())  #false
print(file.writable())  #true
print(file.closed)  #false
print(file.name)  #data.txt
