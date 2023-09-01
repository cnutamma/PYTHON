#class method
#in classs method we dont need to create an object without creating oject we can access directly

class Account:
    min_bal=500    #it is a static variable

    @classmethod
    def updatemin_bal(cls):
       return cls.min_bal+500   #we can call static varaible inside a class method using cls.varaible
    

print(Account.updatemin_bal())


