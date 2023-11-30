from sys import argv

print(argv)
print(type(argv))
print(argv[0])
print(argv[1])
print(argv[2])
print(argv[3])
print(argv[1]+argv[2]) #1020
print(int(argv[1])+int(argv[2])) #30

# argv module is used to read command line argument values.
# argv default type is string
# with int data type we used to change from string type to integer type and we added the argv values in lineno 10