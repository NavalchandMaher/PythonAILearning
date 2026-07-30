# Solve these without looking at notes:

# Functions
# Write a function to find the largest of three numbers.
def findLargeNumber():
    a=10
    b=20
    c=30
    
    if a>b and a>c:
        print("a is gratest")
    elif b>c:
        print("c is gratest")
    else:
        print("c is gratest")
    

# Write a function to check if a number is prime.

def findPrimeNum(num):
    if num<=1:
        print("number is not prime")
        
    for i in range(2, num):
        if num%i==0:
            print("number is not primt")
        else:
            print("number is prime")

# Write a function to calculate factorial.
def calculateFactural(num):
    fact=0;
    while num>0:
        fact=fact*num
        num=-1  

# Write a function to reverse a string.

def reverseString(str):
    revstring=""
    for char in str:
        revstring=char+revstring
    return revstring
        
    #return str[::-1]


# Write a function to count vowels.

def countVowels(str):
    vowel="aeiou"
    count =0
    for char in str:
        if char.lower() in vowel:
            count=count+1
            
    return count
         

# Modules
# Generate a random number between 1–100.

import random

print(f"random number between 1 to 100:",{random.randint(1,100)})

# Print today's date and time.

import datetime
print(f"print todays date:-",{datetime.date.__new__})

# Find the square root of a number.

import math

print(f"find sqrt :-",{ math.sqrt(16)})

# Exception Handling

def handleException():
    try:
        print(10/0)
    except ZeroDivisionError:
        print(" devode bu zero exception")
        

# Divide two numbers safely.
def devideTwoNum():
    num1,num2
    try:
        num1=int(input("Enter num one"))
    except ValueError:
        print("inter valid number")
    try:
        num2=int(input("enter num2"))
    except ValueError:
        print("enter valid number")
    
    try:
        print("numdevice:-"+num1/num2)
    except ZeroDivisionError:
        print("devide bu zero error")

# Validate user input for age.
def userInputAge():
    try:
        age=int(input("enter age"))
    except ValueError:
        print("enter valid age")

# Handle FileNotFoundError.

def checkFile():
    try:
        file=open("student.txt","r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("File Not Found")

# Raise a custom exception if salary is below 10,000.
class InvalidSalaryException(Exception):
    print(f"Salary is not Valid",{Exception})
    
def salaryException():
    salary=int(input("enter salary"))
    if salary<10000:
        raise InvalidSalaryException("invalid salary")
    
findLargeNumber(10)
findPrimeNum(10)
calculateFactural(10)
reverseString("hello")
countVowels("hello")
handleException()
devideTwoNum()
userInputAge()
checkFile()
salaryException()

