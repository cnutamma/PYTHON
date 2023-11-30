'''
dir()-It is used to know all the members and some inbuilt attributes in the module.
help()-Display all inbuilt modules,keywords,symbols and topics.
'''

import random

print(dir())
#output:['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'random']

'''
In random there are different methods:
1)random()-To generate floating numbers between 0 and 1
2)randint()-To generate random int integers and it requires atleast two arguments
3)randrange()-To generate random numbers betwwn the range but there we have another argument called step value 
4)randchoice()-To generate random members in the list 
'''

from random import *
enames=["Rahul", "Sonia","Priyanka", "Modi"]
#print random element from list

for x in range(100):
    print(choice(enames))

 
for x in range(100):
    print(randint(50,100))

for x in range(11):
    print(random())