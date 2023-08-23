#import method
import m1

print(m1.x) #10
print(x)  #NameError  beacuse x is not defined


#module method

from m1 import *

print(x)  #10
print(value())  #its a function
