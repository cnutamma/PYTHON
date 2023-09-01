''''
simple inheritance

'''


class Parent:
    def m1(self):
        print("Parent class")

#we can call parent class by using childclass name(Parent class name)
class Child(Parent): #here child class is inheriting parent class there is no need of extends and implements in python unlike in java.
    def m1(self):
        print("child class")

c1=Child()
c1.m1()    #child class 