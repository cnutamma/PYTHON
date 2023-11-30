'''
Abstraction-Hiding the essential data to the user.It contains one module called abc.
abc modules consists of two types:
1)@abstractmethod -(decarator)
2)ABC -(class)
-----------------------------------------------------------------------

'''

from abc import *

class Test:
    @abstractmethod
    def openAcc():
        pass

obj=Test()
print(obj.__dict__)

'''
output:{}   bcoz method is an abstract we can create object.
'''