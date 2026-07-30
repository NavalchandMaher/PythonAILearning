# Composition
# Composition is a design principle in object-oriented programming where a class is composed of one or more objects from other classes.
# It allows for building complex objects by combining simpler ones, promoting code reuse and flexibility.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine (composition)

    def start(self):
        self.engine.start()  # Delegating the start action to the Engine

my_car = Car()
my_car.start()  # Output: Engine started