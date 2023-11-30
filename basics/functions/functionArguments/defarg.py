#Default argument
#To overcome the poitional argument error default arguments are used for implementation process.



def Cal_age(a,b,c=10):  #here we have given default value c=10  
    print(a+b+c)

x=Cal_age(1,2,3)  #6     #if invoking function contains the c value then this c value is considered for output.
y=Cal_age(4,5)    #19    #if invoking fn doesn't contains the c value then the default value is considered.
print(x) 
print(y)
