
from variable_access import college

class Student:
    #Constructor (__init__)
    
    def __init__(self, name="none", age=0, address="none", phone="none"):
        self.name = name
        self.age = age
        self.address=address
        self.phone=phone
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Phone: {self.phone}")  
    

student1 = Student("John", 20)
print(student1.name)
print(student1.age)

student2 = Student()
print(student2.name)
print(student2.age)

student3= Student("Alice", 22, "123 Main St", "555-1234")
print("Student 1 Info:")
student1.display_info()
print("Student 2 Info:")
student2.display_details()
print("Student 3 Info:")
student3.display_details()

#Method 3: Variable Number of Arguments (*args)

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

sum1 = sum_numbers(1, 2, 3)
print("Sum of numbers:", sum1)


def display_studentinfo(*args):
    for student in args:
        print(f"Name: {student.name}, Age: {student.age}")
        
display_studentinfo(student1, student2, student3)
        
#Method 4: Keyword Arguments (**kwargs)

def display_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
display_student_details(name="John", age=20, address="123 Main St", phone="555-1234")


#*********************************************************************#

#Part 2: Instance Variables & Methods (30 minutes)

#A global variable is declared outside all functions and classes. It can be accessed throughout the module.
company_name = "ABC Corporation" # Global Variable

class Employee:
    
    employeeAge = 30  # Class variable
    
    def __init__(self, name, salary, employeeAge=30):
        self.name = name 
        self.salary = salary
        Employee.employeeAge = employeeAge
    
    def display_info(self):
        address = "123 Main St"
        print(f"Name: {self.name}, Salary: {self.salary}, Employee Age: {Employee.employeeAge}, Address: {address},company: {company_name},college: {college}")
    
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} received a raise of {amount}. New salary: {self.salary}")
employee1 = Employee("Alice", 50000,employeeAge=30)
employee1.display_info()

