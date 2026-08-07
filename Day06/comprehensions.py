
#instead of 
numbers = []
for i in range(10):
    numbers.append(i)
    
# we can use list comprehension instead
numbers = [i for i in range(10)]

print(numbers)

#Squares of numbers 
squares = [i**2 for i in range(10)] # Calculate square of each number in the range
print(squares)

#Even numbers
evens = [i for i in range(10) if i % 2 == 0]
print(evens)

#Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row] # Flatten the matrix into a single list
print(flattened)

#String uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words] # Convert each word to uppercase
print(uppercase_words)

numbers = [1,2,3,4,5]

result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(result)

print([[i for i in range(3)] for j in range(2)],end=" ") # Nested list comprehension to create a 2D list



##Dictionary & Set Comprehensions

#Dictionary comprehension

squares_dict = {i: i**2 for i in range(5)} # Create a dictionary with numbers and their squares
print(squares_dict)

#set comprehension
unique_squares = {i**2 for i in range(5)} # Create a set with unique squares of numbers
print(unique_squares)

#Lambda Functions

def add(x, y):
    return x + y

print(add(3, 5))
#Using lambda function
add_lambda = lambda x, y: x + y
print(add_lambda(3, 5))

#map(), filter(), reduce()

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, numbers)) # Square each number using map
print(result)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Filter even numbers using filter
print(even_numbers)

from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers) # Sum all numbers using reduce
print(sum_of_numbers)