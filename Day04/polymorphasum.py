

#method overloading
# Python does not support method overloading in the traditional sense like Java or C++.

#example of method overloading using default arguments:
class MathOperations:
    def add(self, a, b=0, c=0):
        if c != 0:
            return a + b + c
        elif b != 0:
            return a + b
        else:
            return a

addition = MathOperations()
print(addition.add(5))          # Output: 5


#method overriding
# Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in
# its superclass. The method in the subclass should have the same name, return type, and parameters as the method in the superclass.
#example of method overriding using inheritance:
class Animal:
    def sound(self):
        return "Some generic animal sound"
class Dog(Animal):
    def sound(self):
        return "Woof"

dog = Dog()
print(dog.sound())  # Output: Woof

#**********************************************************#

class Dog:
    def sound(self):
        return "Woof"
class Cat:
    def sound(self):
        return "Meow"
animals=[Dog(), Cat()]

for animal in animals:
    print(animal.sound())  # Output: Woof Meow