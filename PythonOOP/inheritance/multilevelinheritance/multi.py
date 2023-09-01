#MultiLevel Inheritance

class GrandParent:
    pass
class Parent(GrandParent):
    pass
class Child(Parent):
    pass
class Subchild(Child):
    pass

#multi-level inheritance is possible.