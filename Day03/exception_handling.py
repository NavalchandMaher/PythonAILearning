
#without exception handling
# a=10
# b=0
# c=a/b
# print(c)

#with exception handling

try:
    print(10/0)
except:
    print("Error: Division by zero is not allowed.")
    
#3. Catch Specific Exceptions

try:
    num1 = int(input("Enter a number: "))
except ValueError:
    print("Error: Input value is not valid.")
    
#4. Multiple Exceptions

try:
    num1 = int(input("Enter a number: "))
    result = 10 / num1
except ValueError:
    print("Error: Input value is not valid.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#5. else

try:
    print(10/2)
except:
    print("error")
else:
    print("No error occurred.")
    
#6. finally

try:
    print(10/2)
except:
    print("error")
finally:
    print("This will always execute.")
    
#7. Raise Exception

age=15

if age<18:
    raise Exception("Age must be at least 18.")

#8. Custom Exception

class InvalidAgeError(Exception):
    pass

age = 15

if age < 18:
    raise InvalidAgeError("Age must be at least 18.")