
# Practice Questions

# Create a Car class with attributes and methods.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.make} {self.model} engine has started."

    def stop_engine(self):
        return f"The {self.make} {self.model} engine has stopped."

car = Car("Toyota", "Camry", 2020)
print(car.start_engine())  # Output: The Toyota Camry engine has started.
print(car.stop_engine())   # Output: The Toyota Camry engine has stopped.
    

# Create a Student class with marks and percentage.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_percentage(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / (len(self.marks) * 100)) * 100
        return percentage

student = Student("Alice", [85, 90, 78])
print(student.calculate_percentage())  # Output: 84.33333333333334


# Create Animal → Dog → Puppy inheritance.
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Puppy(Dog):
    def sound(self):
        return "Yip"

Puppy = Puppy()
print(Puppy.sound())  # Output: Yip

# Override a method in a subclass.

class Vehicle:
    def start(self):
        return "Vehicle is starting"

class Car(Vehicle):
    def start(self):
        return "Car is starting"
    
car = Car()
print(car.start())  # Output: Car is starting



# Use super() to call the parent constructor.

class Vehicle:
    def __init__(self, make):
        self.make = make
        
class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)  # Call the parent constructor
        self.model = model
        
car = Car("Toyota", "Camry")
print(car.make)   # Output: Toyota
print(car.model)  # Output: Camry

# Create a BankAccount class with private balance.

class BankAccount:
    def __init__(self):
        self.__balance = 1000  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew: {amount}. New balance: {self.__balance}"
        else:
            return "Invalid withdrawal amount."

    def get_balance(self):
        return self.__balance
# Implement getters and setters using @property.
class BankAccount:
    def __init__(self):
        self.__balance = 1000  # Private variable

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative.")
        
bank_account = BankAccount()
print(bank_account.balance)  # Output: 1000
bank_account.balance = 1500
print(bank_account.balance)  # Output: 1500

# Create a static method to calculate simple interest.

class BankAccount:
    def __init__(self):
        self.__balance = 1000  # Private variable

    @staticmethod
    def calculate_simple_interest(principal, rate, time):
        return (principal * rate * time) / 100
    
# Create a class method to update a class variable.

class BankAccount:
    interest_rate = 5  # Class variable

    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        
# Build a Library class containing multiple Book objects (composition).

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")
            
