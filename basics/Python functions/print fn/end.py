#end attribute

id=3
ename="srinu"

# end attribute has default vale is /n which means it starts with newline automatically.

print(ename,end=' ')
print(id) 
'''
output:
srinu 3
'''
print(ename,end='\n') #here \n mean it starts with new line.
print(id) 
'''
output:
srinu
3
'''
print(ename,end='\t') #here \t mean it gives fore space between them.
print(id) 
'''
output:
srinu   3
'''
