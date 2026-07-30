
#  Which access modifier is most commonly used?
# Public (name) – Most common
# Protected (_name) – Common for internal APIs
# Private (__name) – Used when you want to discourage direct access


#Python doesn't have private keywords like Java.

class BankAccount:
    def __init__(self):
        self.__balance = 1000# Private variable
        self._account_number = "123456789"  # Protected variable
        self.account_holder = "John Doe"  # Public variable
account = BankAccount()
# Accessing private variable directly will raise an AttributeError

print(account._BankAccount__balance,account._account_number,account.account_holder )  # Accessing private variable using name mangling 


#Getters & Setters

class Student:
    def __init__(self):
        self.__name = "John"  # Private variable

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, name):
        self.__name = name
        
    # What is the difference between get_name()/set_name() and @property?

    # Answer:

    # get_name() and set_name() are ordinary methods that must be called explicitly,
    # similar to Java.
    # @property turns a method into a managed attribute,
    # allowing you to read and write it using normal attribute syntax
    # (student.name and student.name = value) while still executing getter/setter logic internally.
    # @property is considered the Pythonic approach because it provides a cleaner interface
    # and lets you add validation or computed behavior later without changing the code that uses the class.
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
student = Student()

student.set_name("Alice")  # Using setter method
student.name = "Bob"  # Using property

print(student.get_name())  # Using getter method
print(student.name)  # Using property


    