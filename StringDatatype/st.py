#create operation
name='S'
ename="srinu"
empname='''
        Hello,Gm 
        Srinivas
        '''

#Read operation
#we can read string in two ways
#1)using indexing
#2)using slicling  syntax of slicing [startingindex:endingindex:stepvalue]


#indexing
print(ename)
print(ename[0])
print(ename[1])
print(ename[2])
print(ename[3])
print(ename[4])
'''
output:
   srinu
   s
   r
   i
   n
   u
'''

#we can iterate using while and for

#for-loop
for char in ename:
    print(char)
'''
output:
   s
   r
   i
   n
   u
'''
#while-loop
i=0
while i<=len(ename)-1:
    print(ename[i])
    i=i+1

'''
output:
   s
   r
   i
   n
   u
'''


