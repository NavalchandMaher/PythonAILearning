
# 1. Check if a number is even or odd.

num=10

if(num%2==0):
    print("Even")
else:
    print("Odd")

# 2. Check whether a person is eligible to vote.
age =20
if(age>20):
    print("eligible to vote")
else:
    print("not eligible to vote")

# 3. Find the largest of three numbers.
a = 10
b = 20
c = 15

if(a>b and a>c):
    print("a is largest")
elif(b>c):
    print("b is largest")
else:
    print("c is largest")

# 4. Print numbers from 1 to 100.

for i in range(1,101):
    print(i)

# 5. Print only even numbers from 1 to 100.
for i in range(1,101):
    if i%2==0:
        print(i)
# 6. Print the multiplication table of a given number.
num = 5
for i in range(1,11):
    print(num,"*",i,"=",num*i)
# 7. Calculate the sum of numbers from 1 to n.
num = 10
sum = 0
for i in range(1,num+1):
    sum += i
print("Sum:", sum)
# 8. Find the factorial of a number.
num = 5
factorial = 1
for i in range(1, num+1):
    factorial *= i
print("Factorial:", factorial)

# 9. Count vowels in a string.
string1 = "hello world"
vowels = "aeiou"
count = 0
for char in string1:
    if char.lower() in vowels:
        count += 1
print("Number of vowels:", count)

# 10. Reverse a string without using slicing.
string = "hello world"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)

# 11. Reverse a string with using slicing.
string2 = "hello world"
reversed_string2 = string2[::-1]
print("Reversed string with slicing:", reversed_string2)



