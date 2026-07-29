
#1. What is a Function?
#A function is a reusable block of code that performs a specific

def greet():
    print("Hello, welcome to the program!")
    
greet()

#2. Function with Parameters

def greet(name):
    print(f"Hello, {name}! Welcome to the program!")
    
greet("Naval")

#4. Function Returning a Value
def add(num1, num2):
    return num1 + num2
result = add(5, 3)

print("The sum is:", result)

#5. Default Parameters
def name_age(name="naval", age=24):
    print(f"Name: {name}, Age: {age}")
    
name_age("Naval", 24)
name_age()

#6. Keyword Arguments
def student_info(name, age, address):
    print(f"Name: {name}, Age: {age}, Address: {address}")
    
student_info(name="Naval", age=24, address="Delhi")

#7. Variable Arguments (*args)

def sum_numbers(*args):
   print("Sum of numbers:", max(args))
sum_numbers(1, 2, 3, 4, 5)
sum_numbers(10, 20, 30)

#8. Keyword Variable Arguments (**kwargs)

def student_details(**kwargs):
    print("Student Details:", kwargs)
student_details(name="Naval", age=24, address="Delhi", salary=10000.00, is_active=True)

#10. Lambda Functions

square = lambda x: x ** 2
print("Square of 5:", square(5))