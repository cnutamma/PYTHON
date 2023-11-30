class MyClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print(f"Instance Method called with value: {self.value}")

# Creating an instance of MyClass
obj = MyClass("Hello")

# Calling the instance method
obj.instance_method()

# print(obj.value)-Hello