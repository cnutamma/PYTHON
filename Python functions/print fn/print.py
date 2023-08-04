#python print fumction has some built in attributes in itself
# like end and sep 

# create
id=3
ename="srinu"

# read 
print(id)
print(ename)
'''
output:
3
srinu
'''
print(id,ename)
#output: 3 srinu
print("ename:",ename,"id:",id)
#output: ename:srinu id:3
print("ename{}id{}".format(ename,id))
#enamesrinuid3
print("ename{a}id{b}".format(a=ename,b=id))
#enamesrinuid3
