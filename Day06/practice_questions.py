

# Comprehensions
# Create a list of squares from 1–20.

list_of_squares = [x**2 for x in range(1, 21)]


# Create a dictionary of numbers and cubes.
dict_of_cubes = {x: x**3 for x in range(1, 21)}


# Create a set of even numbers.
set_of_evens = {x for x in range(1, 21) if x % 2 == 0}


# Lambda
# Sort students by marks.
students = [
    {'name': 'Alice', 'marks': 85},
    {'name': 'Bob', 'marks': 92},
    {'name': 'Charlie', 'marks': 78}
]
sorted_students = sorted(students, key=lambda x: x['marks'], reverse=True)
# Sort employees by salary.
employees = [
    {'name': 'Alice', 'salary': 50000},
    {'name': 'Bob', 'salary': 60000},
    {'name': 'Charlie', 'salary': 45000}
]
sorted_employees = sorted(employees, key=lambda x: x['salary'], reverse=True)
# map/filter/reduce

# Double every number.
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))

# Filter odd numbers.
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Find the product of a list.
from dataclasses import dataclass
from functools import reduce
product_of_numbers = reduce(lambda x, y: x * y, numbers)
# Iterators & Generators
# Build a custom iterator.
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
# Create a generator for Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Decorators
# Create a decorator to log function calls.

from time import time

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper
    
# Create a timer decorator.
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

# Context Managers
# Create a custom file context manager.
class MyFileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            
# Type Hints
# Add type hints to an Employee class.

class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name: str = name
        self.age: int = age
        self.salary: float = salary
        
        

# Dataclass
# Create a Product dataclass.
@dataclass
class Product:
    name: str
    price: float
    quantity: int

# Virtual Environment
# Create a project with a virtual environment and install requests.
# python -m venv myenv
# source myenv/bin/activate  # On Windows: myenv\Scripts\activate
# pip install requests
