#Positional Arguments.
#when we are invoking the function the arguments in that function is known as positional argumemts.
#when we are creating the function then the arguments in that function is known as actual argumemts.
#whenever the positional arguments is equalto actual arguments then only the output will come else it will show error.


def Cal_age(a,b,c):
    print(a+b+c)

x=Cal_age(1,2,3)
y=Cal_age(4,5)   #here invokingfn has only 2 arg but in main fn has 3 so it shows type error.
print(x) 
print(y)
