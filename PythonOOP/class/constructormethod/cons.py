
#constructor method

class Account:
    def __init__(self,id,name):
        print(self) #self is a varaiable pointing to the current object.
        self.id=id
        self.name=name


a1=Account(1,'srinu')

print(a1)      #it gives the address of the object
print(id(a1))  #it gives integer value of the object address
print(a1.id)   
print(a1.name)