'''
format()-to format string replacement operator{}
        -If you want to replace variable as a string we use replacement operator.
'''

id=1
ename="sriniva{}"  #we can define using empty value
ename="sriniva{0}"  #we can define using key values
ename="sriniva{age}"  #we can define using names.

print(ename.format("sa"))