class MyClass:
    class_variable = "I am a class variable"

    @classmethod
    def class_method(cls):
        print(f"Class Method called with class variable: {cls.class_variable}")

# Calling the class method
MyClass.class_method()
