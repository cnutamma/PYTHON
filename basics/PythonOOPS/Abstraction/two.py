from abc import *

class Test(ABC):
    @abstractmethod
    def openAcc():
        pass


'''
obj=Test()
print(obj.__dict__)
output:Error-bcoz method&class is an abstract we can't create object.'''