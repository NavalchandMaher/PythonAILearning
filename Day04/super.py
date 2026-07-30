#super()
# The super() function is used to call a method from the parent class.
#example:
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        parent_sound = super().sound()  # Call the method from the parent class
        return parent_sound + " Woof"

dog = Dog()
print(dog.sound())  # Output: Some generic animal sound Woof

#constructor super()
# The super() function can also be used to call the constructor of the parent class.
class Animal:
    def __init__(self, species):
        self.species = species
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")  # Call the constructor of the parent class
        self.name = name

dog = Dog("Buddy")
print(dog.species)  # Output: Dog
print(dog.name)     # Output: Buddy