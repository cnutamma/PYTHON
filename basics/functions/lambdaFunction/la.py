'''
Inbuilt functions in Python:
1)filter(fn,iterable)
2)reduce(fn,iterable)
3)map(fn,iterable)
'''

#without using lambda function

from functools import reduce
def addAll(a,b):
    return(a+b)
total=reduce(addAll,[99,199,299,399])
print(total)
#output:996


#Using lambda function

from functools import reduce
def addAll(a,b):
    return(a+b)
total=reduce(lambda a,b:a+b,[99,199,299,399])
print(total)
#output:996

