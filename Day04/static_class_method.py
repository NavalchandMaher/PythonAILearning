
# Static Methods are methods that belong to a class rather than an instance of a class.
# zThey do not require an instance to be called and do not have access to the instance (self)
# or class (cls) variables.
# Static methods are defined using the @staticmethod decorator.

class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
    
print(Math.add(5, 3))       # Output: 8
print(Math.multiply(5, 3))  # Output: 15

#class method
# Class methods are methods that belong to a class rather than an instance of a class.
# They have access to the class itself (cls) and can modify class state that applies across 
# all instances of the class.
# Class methods are defined using the @classmethod decorator.

class Student:
    school_name = "ABC School"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

    @classmethod
    def get_school_name(cls):
        return cls.school_name
print(Student.get_school_name())  # Output: ABC School

