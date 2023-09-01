#Multiple inheritance is possible in python

class Parent1:
        def m1(self):
              print("Parent1 class")

class Parent2:
       def m1(self):
              print("Parent2 class")

class Child(Parent1,Parent2):
       def m2(self):
              print("child class")

c1=Child()
c1.m1() #parent1 class is output bcoz in child we are calling parent1 as first 
#if child class is calling child(parent2,parent1) then the output is parent2 class

