class Account:

    #there are four types of methods in class Constructor method,Instance method,static method,class method.\
    #self is pointer pointing to the current object.Unlike in java and javascript we usae this as a pointer.
    def __init__(self) -> None:
        print("constructor method")
     
    #Any method or varaible contains self keyword it is an instance method or instance variable.
    def get_bal(self):
        print("instance method")

    @classmethod
    def get_bal(cls):
        print("class method")

    @staticmethod
    def get_bal():
        print("static method")


#how to create object in class?Using class name we will used to create a object.

e1=Account()

#it will gives hexa decimal code it describes address.
print(e1)


#when we are using id it will converts hexa decimal to integer format.
print(id(e1))

#it is used to store in dictonary format when we are using(__dict__)
print(e1.__dict__)
    