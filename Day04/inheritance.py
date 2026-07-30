

class Animal:
    def _sound(self):
        return "Some generic animal sound"
    
class WildAnimal():
    
    def make_sound(self):
        return self._sound()
    
class Dog(Animal, WildAnimal):
    def bark(self):
        return "Bark"
    
    def sound(self):
        return "Woof"
    
    def make_sound(self):
        return self._sound()
    
dog = Dog()
print(dog._sound())  # Inherited method from Animal class
print(dog.bark())   # Method from Dog class
print(dog.sound())  # Accessing the public method of Dog class
print(dog.make_sound())  # Accessing the private method of WildAnimal class through a public method
print(dog.__class__.__mro__)  # Method Resolution Order (MRO) of Dog class


#interface example
from abc import ABC, abstractmethod 
class AnimalInterface(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    def make_sound(self):
        return self.sound()
    
class Dog(AnimalInterface):
    def sound(self):
        return "Woof"

class Cat(AnimalInterface):
    def sound(self):
        return "Meow"
    
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Woof
print(cat.sound())  # Output: Meow

    
