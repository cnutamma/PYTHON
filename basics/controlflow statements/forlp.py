#print 1 to 10 numbers using for loop

for x in range(0,10,+1):
    print(x)

#output:0,1,2,3,4,5,6,7,8,9

#print 10 to 1 numbers

for x in range(10,0,-1):
    print(x)

#output:9,8,7,6,5,4,3,2,1,0



#here we need to take a list and we need do for loop
l=[0,1,2,3,4,5,6,7,8,9]
for x in l:
    print(x)

#output:0,1,2,3,4,5,6,7,8,9


enames=["srinu","vamsi","gopi"]
for x in enames:
    print(x)
#output:srinu,vamsi,gopi

ename="srinu"
id=[1,2,3]
for char in ename:
    print(char)
#output:s,r,i,n,u
for id in id:
    print(id)
#output:1,2,3