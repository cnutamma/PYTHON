'''
index()-returns the index number of the first occurence of the given string
       -if the given string is not there then it leads to the value error.
find()-returns the index number of the first occurence of the given string
       -if the given string is not there then it gives the output as -1.
'''

ename="hi,Gm Srinivas have a beautiful day"

print(ename.index("a"))   #12
print(ename.index("b"))   #22
print(ename.index("Gm"))  #3
print(ename.index("abc"))  #Value error

print(ename.find("a"))   #12
print(ename.find("b"))   #22
print(ename.find("Gm"))  #3
print(ename.find("abc")) #-1