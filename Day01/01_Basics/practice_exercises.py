"""
Practice Exercises

Complete these without looking at the notes:

1. Print "Hello, AI Engineer!".
2. Create variables for your name, age, and current company, then print them using an f-string.
3. Take two numbers as input and print their sum, difference, product, and quotient.
4. Convert "123" to an integer and "45.67" to a float.
5. Display the type of an int, float, str, list, dict, and bool.
6. Create a dictionary containing your profile (name, experience, city, skills) and print each value.
7. Create a list of five AI technologies you want to learn and print them one by one.
8. Intentionally create and then fix a TypeError, NameError, and SyntaxError to understand these common mistakes.

"""

#1. Print "Hello, AI Engineer!".
print("Hello, AI Engineer!")

#2. Create variables for your name, age, and current company, then print them using an f-string.
name="Naval"
age=24
company="AI Learning"
print(f"My name is {name}, I am {age} years old, and I work at {company}.")

#3. Take two numbers as input and print their sum, difference, product, and quotient.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum {num1+num2}")
print(f"Difference: {num1-num2}")
print(f"Product: {num1*num2}")
if num2 != 0:
    print(f"Quotient: {num1/num2}")
    
#4. Convert "123" to an integer and "45.67" to a float.
int_num=int("123")
float_num=float("45.67")

print(f"Integer: {int_num}, Float: {float_num}")

#5. Display the type of an int, float, str, list, dict, and bool.
print(f"Type of int: {type(int_num)}")
print(f"Type of float: {type(float_num)}")
print(f"Type of str: {type(name)}")
print(f"Type of list: {type([1,2,3])}")
print(f"Type of dict: {type({'key':'value'})}")
print(f"Type of bool: {type(True)}")

#6. Create a dictionary containing your profile (name, experience, city, skills) and print each value.

profile={"name":"Naval","experience":"6 yrams","city":"Pune","Skills":["Python","AI","ML"]}

print(f"Name      :{profile['name']}")
print(f"Experience:{profile['experience']}")
print(f"City      :{profile['city']}")
print(f"Skills    :{profile['Skills']}")

#7. Create a list of five AI technologies you want to learn and print them one by one.
ai_technologies=["Machine Learning","Deep Learning","Natural Language Processing","Computer Vision","Reinforcement Learning"]
print("AI Technologies I want to learn:")
for tech in ai_technologies:
    print(tech)
    
#8. Intentionally create and then fix a TypeError, NameError, and SyntaxError to understand these common mistakes.
#TypeError
try:
    result = "5" + 5  # This will raise a TypeError
except TypeError as e:
    print(f"TypeError: {e}")
    

