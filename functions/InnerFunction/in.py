def outer():
    print("outer function")
    def inner():
        print("inner function")
    return inner

x=outer()
x()   #inner function


print(outer)  #outer function
#print(inner)  #Name error because we can't call directly inner function it is not defined.
