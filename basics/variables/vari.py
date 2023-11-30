# variables

class Test:
    #static variables are created within class anad outside methods.
    staticvaraible =10
    
    def __init__(self,value):
        self.instancevariable=value 

print(Test.staticvaraible)
obj1=Test(2)
print(obj1.instancevariable)
# --------------------------------------------------
# local variables are created within the function
def my_function():
    local_variable = 5
    print(local_variable)

my_function()



